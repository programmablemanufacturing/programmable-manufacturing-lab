from __future__ import annotations

import numpy as np

from imwm.envs.toy_process import StepResult
from imwm.physics import clip01


class ToolWearEnvironment:
    """Synthetic tool-wear environment for testing maintenance-aware decisions.

    State dimensions:
    0. wear_level
    1. tool_temperature
    2. surface_quality
    3. defect_risk

    Action dimensions:
    0. feed_rate in [0, 1]
    1. coolant_flow in [0, 1]
    """

    obs_dim = 4
    action_dim = 2

    def __init__(self, episode_length: int = 30, noise_std: float = 0.01, seed: int | None = None):
        self.episode_length = episode_length
        self.noise_std = noise_std
        self.rng = np.random.default_rng(seed)
        self.t = 0
        self.state = np.zeros(self.obs_dim, dtype=np.float32)

    def reset(self) -> np.ndarray:
        self.t = 0
        self.state = np.array([
            self.rng.uniform(0.02, 0.08),
            self.rng.uniform(0.30, 0.45),
            self.rng.uniform(0.82, 0.94),
            self.rng.uniform(0.02, 0.08),
        ], dtype=np.float32)
        return self.state.copy()

    def step(self, action: np.ndarray) -> StepResult:
        action = clip01(np.asarray(action, dtype=np.float32))
        feed_rate = float(action[0])
        coolant_flow = float(action[1])
        prev_wear, prev_temperature, _, _ = self.state

        cutting_load = 0.35 + 0.65 * feed_rate
        cooling_effect = 0.25 + 0.75 * coolant_flow
        tool_temperature = clip01(
            0.62 * prev_temperature
            + 0.30 * cutting_load
            + 0.16 * (1.0 - cooling_effect)
            + self.rng.normal(0.0, self.noise_std)
        )
        thermal_excess = max(0.0, float(tool_temperature) - 0.55)
        wear_increment = max(
            0.0,
            0.010
            + 0.055 * cutting_load
            + 0.040 * thermal_excess
            - 0.020 * cooling_effect
            + self.rng.normal(0.0, self.noise_std),
        )
        wear_level = clip01(prev_wear + wear_increment)
        defect_risk = clip01(
            0.05
            + 0.48 * wear_level
            + 0.22 * thermal_excess
            + 0.12 * max(0.0, feed_rate - coolant_flow)
            + self.rng.normal(0.0, self.noise_std)
        )
        surface_quality = clip01(
            0.94
            - 0.55 * wear_level
            - 0.25 * defect_risk
            - 0.10 * abs(float(tool_temperature) - 0.45)
            + self.rng.normal(0.0, self.noise_std)
        )

        self.state = np.array([wear_level, tool_temperature, surface_quality, defect_risk], dtype=np.float32)
        self.t += 1
        reward = float(surface_quality - 0.45 * defect_risk - 0.08 * wear_level)
        done = self.t >= self.episode_length
        info = {
            "feed_rate": feed_rate,
            "coolant_flow": coolant_flow,
            "cutting_load": float(cutting_load),
            "wear_increment": float(wear_increment),
            "wear_level": float(wear_level),
            "tool_temperature": float(tool_temperature),
            "surface_quality": float(surface_quality),
            "defect_risk": float(defect_risk),
            "reward": reward,
        }
        return StepResult(state=self.state.copy(), reward=reward, done=done, info=info)

    def sample_action(self) -> np.ndarray:
        return self.rng.uniform(0.0, 1.0, size=(self.action_dim,)).astype(np.float32)
