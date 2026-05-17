from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import torch
import torch.nn as nn
import torch.nn.functional as F

from imwm.physics import DEFECT_INDEX, QUALITY_INDEX, torch_physics_proxy


@dataclass
class RSSMConfig:
    input_dim: int
    action_dim: int = 2
    state_dim: int = 5
    hidden_dim: int = 128
    latent_dim: int = 32
    min_std: float = 0.03
    max_std: float = 1.00
    physics_weight: float = 0.20
    feasibility_weight: float = 0.35
    kl_weight: float = 1e-4


class ManufacturingRSSM(nn.Module):
    """RSSM-inspired latent dynamics model for manufacturing processes."""

    def __init__(self, input_dim: int, action_dim: int = 2, state_dim: int = 5, hidden_dim: int = 128, latent_dim: int = 32, min_std: float = 0.03, max_std: float = 1.00):
        super().__init__()
        self.config = RSSMConfig(input_dim=input_dim, action_dim=action_dim, state_dim=state_dim, hidden_dim=hidden_dim, latent_dim=latent_dim, min_std=min_std, max_std=max_std)
        self.history_encoder = nn.GRU(input_size=input_dim, hidden_size=hidden_dim, batch_first=True)
        self.posterior = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, 2 * latent_dim))
        self.dynamics = nn.GRUCell(latent_dim + action_dim, hidden_dim)
        self.prior = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, 2 * latent_dim))
        self.decoder = nn.Sequential(nn.Linear(hidden_dim + latent_dim + action_dim, hidden_dim), nn.SiLU(), nn.Linear(hidden_dim, hidden_dim), nn.SiLU())
        self.state_mean = nn.Linear(hidden_dim, state_dim)
        self.state_log_std = nn.Linear(hidden_dim, state_dim)
        self.feasibility_logit = nn.Linear(hidden_dim, 1)
        self.reward_head = nn.Linear(hidden_dim, 1)

    def _split_dist(self, stats: torch.Tensor):
        mean, log_std = torch.chunk(stats, chunks=2, dim=-1)
        log_std = torch.clamp(log_std, -5.0, 2.0)
        std = torch.clamp(torch.exp(log_std), self.config.min_std, self.config.max_std)
        return mean, std

    def _sample(self, mean: torch.Tensor, std: torch.Tensor, deterministic: bool):
        return mean if deterministic else mean + torch.randn_like(std) * std

    def encode_history(self, history: torch.Tensor, deterministic: bool = False):
        _, h = self.history_encoder(history)
        h = h[-1]
        post_mean, post_std = self._split_dist(self.posterior(h))
        z = self._sample(post_mean, post_std, deterministic=deterministic)
        return h, z, post_mean, post_std

    def forward(self, history: torch.Tensor, action: torch.Tensor, rollout_steps: int = 1, deterministic: bool = False) -> Dict[str, torch.Tensor]:
        h, z, post_mean, post_std = self.encode_history(history, deterministic=deterministic)
        if action.dim() == 2:
            action_sequence = action[:, None, :].repeat(1, rollout_steps, 1)
        elif action.dim() == 3:
            action_sequence = action
            rollout_steps = action.shape[1]
        else:
            raise ValueError("action must have shape [B, A] or [B, T, A]")
        state_means, state_stds, feasibility_logits, rewards, prior_means, prior_stds, latents = [], [], [], [], [], [], []
        for t in range(rollout_steps):
            a_t = torch.clamp(action_sequence[:, t, :], 0.0, 1.0)
            h = self.dynamics(torch.cat([z, a_t], dim=-1), h)
            prior_mean, prior_std = self._split_dist(self.prior(h))
            z = self._sample(prior_mean, prior_std, deterministic=deterministic)
            features = self.decoder(torch.cat([h, z, a_t], dim=-1))
            mean = torch.sigmoid(self.state_mean(features))
            std = torch.clamp(torch.exp(self.state_log_std(features)), self.config.min_std, self.config.max_std)
            state_means.append(mean)
            state_stds.append(std)
            feasibility_logits.append(self.feasibility_logit(features))
            rewards.append(self.reward_head(features))
            prior_means.append(prior_mean)
            prior_stds.append(prior_std)
            latents.append(z)
        return {"state_mean": torch.stack(state_means, dim=1), "state_std": torch.stack(state_stds, dim=1), "feasibility_logit": torch.stack(feasibility_logits, dim=1), "reward": torch.stack(rewards, dim=1), "latent": torch.stack(latents, dim=1), "posterior_mean": post_mean, "posterior_std": post_std, "prior_mean": torch.stack(prior_means, dim=1), "prior_std": torch.stack(prior_stds, dim=1)}

    def compute_loss(self, batch: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        history = batch["history"]
        action = batch["action"]
        target_state = batch["next_state"]
        target_feasible = batch["feasible"]
        target_reward = batch["reward"]
        pred = self.forward(history, action, rollout_steps=1, deterministic=False)
        mean = pred["state_mean"][:, 0, :]
        std = pred["state_std"][:, 0, :]
        feasibility_logit = pred["feasibility_logit"][:, 0, :]
        reward_pred = pred["reward"][:, 0, :]
        nll = 0.5 * (((target_state - mean) / std) ** 2 + 2.0 * torch.log(std)).mean()
        feasibility_loss = F.binary_cross_entropy_with_logits(feasibility_logit, target_feasible)
        reward_loss = F.mse_loss(reward_pred, target_reward)
        proxy = torch_physics_proxy(action)
        predicted_quality_defect = torch.stack([mean[:, QUALITY_INDEX], mean[:, DEFECT_INDEX]], dim=-1)
        physics_loss = F.mse_loss(predicted_quality_defect, proxy)
        post_mean = pred["posterior_mean"]
        post_std = pred["posterior_std"]
        kl_to_standard_normal = 0.5 * (post_mean.pow(2) + post_std.pow(2) - torch.log(post_std.pow(2) + 1e-8) - 1.0).mean()
        total = nll + self.config.feasibility_weight * feasibility_loss + 0.10 * reward_loss + self.config.physics_weight * physics_loss + self.config.kl_weight * kl_to_standard_normal
        return {"total": total, "nll": nll.detach(), "feasibility": feasibility_loss.detach(), "reward": reward_loss.detach(), "physics": physics_loss.detach(), "kl": kl_to_standard_normal.detach()}
