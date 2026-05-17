from __future__ import annotations

from typing import Dict

import numpy as np

ACTION_LOW = np.array([100.0, 200.0], dtype=np.float32)
ACTION_HIGH = np.array([400.0, 1200.0], dtype=np.float32)
STATE_NAMES = ["normalized_energy", "thermal_state", "structure_score", "defect_risk", "quality_score"]
ACTION_NAMES = ["laser_power", "scan_speed"]
QUALITY_INDEX = 4
DEFECT_INDEX = 3


def clip01(x):
    return np.clip(x, 0.0, 1.0)


def scale_action(normalized_action: np.ndarray) -> Dict[str, float]:
    """Convert normalized controls in [0, 1] to physical toy units."""
    a = np.asarray(normalized_action, dtype=np.float32)
    physical = ACTION_LOW + clip01(a) * (ACTION_HIGH - ACTION_LOW)
    return {"laser_power": float(physical[0]), "scan_speed": float(physical[1])}


def normalized_energy_from_action(normalized_action: np.ndarray) -> float:
    """Synthetic normalized energy proxy. Not a real process model."""
    physical = scale_action(normalized_action)
    energy = (physical["laser_power"] / physical["scan_speed"]) * 2.4
    return float(np.clip(energy, 0.0, 2.0) / 2.0)


def gaussian_score(x: float, center: float, width: float) -> float:
    return float(np.exp(-0.5 * ((x - center) / width) ** 2))


def process_physics_proxy(normalized_action: np.ndarray) -> Dict[str, float]:
    """Return synthetic physics-inspired proxies for a candidate action."""
    e01 = normalized_energy_from_action(normalized_action)
    energy = 2.0 * e01
    target_energy = 0.75
    energy_score = gaussian_score(energy, center=target_energy, width=0.22)
    speed01 = float(clip01(np.asarray(normalized_action)[1]))
    stability = 0.5 * energy_score + 0.5 * gaussian_score(speed01, center=0.42, width=0.24)
    stability = float(clip01(stability))
    lack_of_fusion = float(clip01((target_energy - energy) / target_energy))
    overheating = float(clip01((energy - target_energy) / target_energy))
    defect_risk = float(clip01(0.55 * lack_of_fusion + 0.30 * overheating + 0.15 * (1.0 - stability)))
    quality = float(clip01(0.70 * energy_score + 0.20 * stability + 0.10 * (1.0 - defect_risk)))
    return {
        "normalized_energy": e01,
        "stability": stability,
        "lack_of_fusion_risk": lack_of_fusion,
        "overheating_risk": overheating,
        "defect_risk": defect_risk,
        "quality_score": quality,
    }


def torch_physics_proxy(action):
    """Differentiable torch proxy returning [quality_proxy, defect_proxy]."""
    import torch
    a = torch.clamp(action, 0.0, 1.0)
    low = torch.as_tensor(ACTION_LOW, device=a.device, dtype=a.dtype)
    span = torch.as_tensor(ACTION_HIGH - ACTION_LOW, device=a.device, dtype=a.dtype)
    physical = low + a * span
    laser_power = physical[..., 0]
    scan_speed = physical[..., 1]
    energy = torch.clamp((laser_power / scan_speed) * 2.4, 0.0, 2.0)
    target_energy = 0.75
    energy_score = torch.exp(-0.5 * ((energy - target_energy) / 0.22) ** 2)
    speed_score = torch.exp(-0.5 * ((a[..., 1] - 0.42) / 0.24) ** 2)
    stability = torch.clamp(0.5 * energy_score + 0.5 * speed_score, 0.0, 1.0)
    lack_of_fusion = torch.clamp((target_energy - energy) / target_energy, 0.0, 1.0)
    overheating = torch.clamp((energy - target_energy) / target_energy, 0.0, 1.0)
    defect_risk = torch.clamp(0.55 * lack_of_fusion + 0.30 * overheating + 0.15 * (1.0 - stability), 0.0, 1.0)
    quality = torch.clamp(0.70 * energy_score + 0.20 * stability + 0.10 * (1.0 - defect_risk), 0.0, 1.0)
    return torch.stack([quality, defect_risk], dim=-1)
