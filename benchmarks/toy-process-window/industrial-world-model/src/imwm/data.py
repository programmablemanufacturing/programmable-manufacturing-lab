from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np
import torch
from torch.utils.data import Dataset

from imwm.envs.toy_process import ToyManufacturingEnv
from imwm.physics import DEFECT_INDEX, QUALITY_INDEX


@dataclass
class WorldModelArrays:
    histories: np.ndarray
    actions: np.ndarray
    next_states: np.ndarray
    feasible: np.ndarray
    rewards: np.ndarray
    input_dim: int
    action_dim: int
    state_dim: int

    def sample_history(self, index: int = 0) -> torch.Tensor:
        return torch.tensor(self.histories[index:index + 1], dtype=torch.float32)


class ManufacturingSequenceDataset(Dataset):
    def __init__(self, arrays: WorldModelArrays):
        self.histories = torch.tensor(arrays.histories, dtype=torch.float32)
        self.actions = torch.tensor(arrays.actions, dtype=torch.float32)
        self.next_states = torch.tensor(arrays.next_states, dtype=torch.float32)
        self.feasible = torch.tensor(arrays.feasible, dtype=torch.float32)
        self.rewards = torch.tensor(arrays.rewards, dtype=torch.float32)

    def __len__(self) -> int:
        return self.histories.shape[0]

    def __getitem__(self, idx: int):
        return {"history": self.histories[idx], "action": self.actions[idx], "next_state": self.next_states[idx], "feasible": self.feasible[idx], "reward": self.rewards[idx]}


def generate_episodes(num_episodes: int = 80, episode_length: int = 40, seed: int = 7) -> Dict[str, np.ndarray]:
    states, actions, rewards = [], [], []
    for ep in range(num_episodes):
        env = ToyManufacturingEnv(episode_length=episode_length, seed=seed + ep)
        state = env.reset()
        previous_action = None
        ep_states = [state]
        ep_actions = []
        ep_rewards = []
        for _ in range(episode_length):
            action = env.sample_action(previous_action)
            result = env.step(action)
            ep_actions.append(action)
            ep_rewards.append(result.reward)
            ep_states.append(result.state)
            previous_action = action
        states.append(np.stack(ep_states, axis=0))
        actions.append(np.stack(ep_actions, axis=0))
        rewards.append(np.asarray(ep_rewards, dtype=np.float32))
    return {"states": np.stack(states).astype(np.float32), "actions": np.stack(actions).astype(np.float32), "rewards": np.stack(rewards).astype(np.float32)}


def make_supervised_world_model_arrays(episodes: Dict[str, np.ndarray], history_length: int = 8, quality_threshold: float = 0.72, max_defect_risk: float = 0.25) -> WorldModelArrays:
    states = episodes["states"]
    actions = episodes["actions"]
    rewards = episodes["rewards"]
    num_episodes, _, state_dim = states.shape
    _, episode_length, action_dim = actions.shape
    input_dim = state_dim + action_dim
    histories, target_actions, next_states, feasible, target_rewards = [], [], [], [], []
    zero_action = np.zeros(action_dim, dtype=np.float32)
    for ep in range(num_episodes):
        for t in range(history_length, episode_length):
            hist_rows = []
            for k in range(t - history_length, t):
                prev_action = zero_action if k == 0 else actions[ep, k - 1]
                hist_rows.append(np.concatenate([states[ep, k], prev_action], axis=0))
            next_state = states[ep, t + 1]
            is_feasible = next_state[QUALITY_INDEX] >= quality_threshold and next_state[DEFECT_INDEX] <= max_defect_risk
            histories.append(np.stack(hist_rows, axis=0))
            target_actions.append(actions[ep, t])
            next_states.append(next_state)
            feasible.append([float(is_feasible)])
            target_rewards.append([rewards[ep, t]])
    return WorldModelArrays(np.stack(histories).astype(np.float32), np.stack(target_actions).astype(np.float32), np.stack(next_states).astype(np.float32), np.asarray(feasible, dtype=np.float32), np.asarray(target_rewards, dtype=np.float32), input_dim, action_dim, state_dim)


def generate_world_model_dataset(num_episodes: int = 80, episode_length: int = 40, history_length: int = 8, seed: int = 7) -> WorldModelArrays:
    episodes = generate_episodes(num_episodes=num_episodes, episode_length=episode_length, seed=seed)
    return make_supervised_world_model_arrays(episodes, history_length=history_length)


def split_dataset(arrays: WorldModelArrays, train_fraction: float = 0.8, seed: int = 7):
    rng = np.random.default_rng(seed)
    n = arrays.histories.shape[0]
    indices = rng.permutation(n)
    train_n = int(train_fraction * n)
    def subset(idx):
        return WorldModelArrays(arrays.histories[idx], arrays.actions[idx], arrays.next_states[idx], arrays.feasible[idx], arrays.rewards[idx], arrays.input_dim, arrays.action_dim, arrays.state_dim)
    return subset(indices[:train_n]), subset(indices[train_n:])
