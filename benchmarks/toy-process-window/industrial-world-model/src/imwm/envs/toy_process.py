from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np

from imwm.physics import clip01, process_physics_proxy


@dataclass
class StepResult:
    state: np.ndarray
    reward: float
    done: bool
    info: Dict[str, float]


class ToyManufacturingEnv:
    """Synthetic manufacturing process environment."""

    obs_dim = 5
    action_dim = 2

    def __init__(self, episode_length: int = 40, noise_std: float = 0.015, seed: int | None = None):
        self.episode_length = episode_length
        self.noise_std = noise_std
        self.rng = np.random.default_rng(seed)
        self.t = 0
        self.state = np.zeros(self.obs_dim, dtype=np.float32)
        self.drift = 0.0

    def reset(self) -> np.ndarray:
        self.t = 0
        self.drift = float(self.rng.normal(0.0, 0.03))
        self.state = np.array([
            self.rng.uniform(0.25, 0.55),
            self.rng.uniform(0.25, 0.55),
            self.rng.uniform(0.35, 0.65),
            self.rng.uniform(0.20, 0.45),
            self.rng.uniform(0.35, 0.65),
        ], dtype=np.float32)
        return self.state.copy()

    def step(self, action: np.ndarray) -> StepResult:
        action = clip01(np.asarray(action, dtype=np.float32))
        proxy = process_physics_proxy(action)
        _, prev_thermal, prev_structure, prev_defect, prev_quality = self.state
        energy = proxy["normalized_energy"]
        thermal = clip01(0.70 * prev_thermal + 0.30 * energy + self.drift + self.rng.normal(0.0, self.noise_std))
        structure = clip01(0.68 * prev_structure + 0.25 * proxy["stability"] + 0.07 * (1.0 - proxy["defect_risk"]) + self.rng.normal(0.0, self.noise_std))
        dynamic_defect = clip01(0.60 * proxy["defect_risk"] + 0.25 * prev_defect + 0.15 * abs(thermal - 0.50) + self.rng.normal(0.0, self.noise_std))
        quality = clip01(0.62 * proxy["quality_score"] + 0.20 * structure + 0.13 * (1.0 - dynamic_defect) + 0.05 * prev_quality + self.rng.normal(0.0, self.noise_std))
        self.state = np.array([energy, thermal, structure, dynamic_defect, quality], dtype=np.float32)
        self.t += 1
        reward = float(quality - 0.55 * dynamic_defect - 0.02 * np.square(action - 0.5).sum())
        done = self.t >= self.episode_length
        info = {**proxy, "reward": reward, "thermal_state": float(thermal), "structure_score": float(structure), "dynamic_defect_risk": float(dynamic_defect), "quality_score": float(quality)}
        return StepResult(state=self.state.copy(), reward=reward, done=done, info=info)

    def sample_action(self, previous_action: np.ndarray | None = None, smoothness: float = 0.65) -> np.ndarray:
        if previous_action is None:
            return self.rng.uniform(0.0, 1.0, size=(self.action_dim,)).astype(np.float32)
        random_action = self.rng.uniform(0.0, 1.0, size=(self.action_dim,))
        action = smoothness * previous_action + (1.0 - smoothness) * random_action
        action += self.rng.normal(0.0, 0.05, size=(self.action_dim,))
        return clip01(action).astype(np.float32)
