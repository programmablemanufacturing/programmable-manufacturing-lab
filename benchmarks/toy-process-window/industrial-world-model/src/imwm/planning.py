from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np
import torch

from imwm.physics import DEFECT_INDEX, QUALITY_INDEX, scale_action


@dataclass
class PlanningReport:
    best_score: float
    best_action_normalized: np.ndarray
    best_action_physical: Dict[str, float]
    predicted_quality: float
    predicted_defect_risk: float
    predicted_quality_uncertainty: float
    feasible_probability: float
    iterations: int
    candidates: int


class CEMPlanner:
    """Cross-Entropy Method planner for process-window recommendation."""

    def __init__(self, candidates: int = 512, elite_fraction: float = 0.10, iterations: int = 5, horizon: int = 3, quality_weight: float = 1.00, defect_weight: float = 0.75, uncertainty_weight: float = 0.20, feasibility_weight: float = 0.25, seed: int = 7):
        self.candidates = candidates
        self.elite_fraction = elite_fraction
        self.iterations = iterations
        self.horizon = horizon
        self.quality_weight = quality_weight
        self.defect_weight = defect_weight
        self.uncertainty_weight = uncertainty_weight
        self.feasibility_weight = feasibility_weight
        self.rng = np.random.default_rng(seed)

    def _score(self, pred: Dict[str, torch.Tensor]) -> torch.Tensor:
        state_mean = pred["state_mean"]
        state_std = pred["state_std"]
        feasible = torch.sigmoid(pred["feasibility_logit"])
        quality = state_mean[:, :, QUALITY_INDEX].mean(dim=1)
        defect = state_mean[:, :, DEFECT_INDEX].mean(dim=1)
        quality_uncertainty = state_std[:, :, QUALITY_INDEX].mean(dim=1)
        feasible_prob = feasible.mean(dim=(1, 2))
        return self.quality_weight * quality - self.defect_weight * defect - self.uncertainty_weight * quality_uncertainty + self.feasibility_weight * feasible_prob

    def plan(self, model: torch.nn.Module, history: torch.Tensor, device: Optional[str] = None) -> Tuple[np.ndarray, PlanningReport]:
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        torch_device = torch.device(device)
        model.to(torch_device)
        model.eval()
        if history.dim() == 2:
            history = history.unsqueeze(0)
        history = history.to(torch_device)
        mean = np.full((self.horizon, model.config.action_dim), 0.5, dtype=np.float32)
        std = np.full((self.horizon, model.config.action_dim), 0.30, dtype=np.float32)
        elite_count = max(4, int(self.candidates * self.elite_fraction))
        best_action_sequence = None
        best_score = -float("inf")
        best_pred = None
        with torch.no_grad():
            for _ in range(self.iterations):
                samples = self.rng.normal(loc=mean[None, :, :], scale=std[None, :, :], size=(self.candidates, self.horizon, model.config.action_dim)).astype(np.float32)
                samples = np.clip(samples, 0.0, 1.0)
                hist_batch = history.repeat(self.candidates, 1, 1)
                action_batch = torch.tensor(samples, dtype=torch.float32, device=torch_device)
                pred = model.forward(hist_batch, action_batch, deterministic=True)
                scores = self._score(pred)
                elite_idx = torch.topk(scores, k=elite_count).indices.cpu().numpy()
                elites = samples[elite_idx]
                mean = elites.mean(axis=0)
                std = np.maximum(elites.std(axis=0), 0.03)
                current_best_idx = int(torch.argmax(scores).detach().cpu())
                current_best_score = float(scores[current_best_idx].detach().cpu())
                if current_best_score > best_score:
                    best_score = current_best_score
                    best_action_sequence = samples[current_best_idx]
                    best_pred = {k: v[current_best_idx:current_best_idx + 1].detach().cpu() for k, v in pred.items()}
        assert best_action_sequence is not None
        assert best_pred is not None
        first_action = best_action_sequence[0]
        state_mean = best_pred["state_mean"][0, 0]
        state_std = best_pred["state_std"][0, 0]
        feasible = torch.sigmoid(best_pred["feasibility_logit"])[0, 0, 0]
        report = PlanningReport(best_score=best_score, best_action_normalized=first_action, best_action_physical=scale_action(first_action), predicted_quality=float(state_mean[QUALITY_INDEX]), predicted_defect_risk=float(state_mean[DEFECT_INDEX]), predicted_quality_uncertainty=float(state_std[QUALITY_INDEX]), feasible_probability=float(feasible), iterations=self.iterations, candidates=self.candidates)
        return first_action, report
