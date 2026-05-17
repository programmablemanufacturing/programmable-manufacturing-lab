from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Mapping, Optional

import numpy as np


@dataclass(frozen=True)
class ManufacturingState:
    """A compact manufacturing process state.

    Default state dimensions:
    0. normalized_energy
    1. thermal_state
    2. structure_score
    3. defect_risk
    4. quality_score
    """

    values: np.ndarray
    metadata: Optional[Mapping[str, float]] = None


@dataclass(frozen=True)
class ProcessAction:
    """A controllable manufacturing action.

    Default action dimensions:
    0. laser_power control in [0, 1]
    1. scan_speed control in [0, 1]
    """

    values: np.ndarray
    metadata: Optional[Mapping[str, float]] = None


@dataclass(frozen=True)
class WorldModelPrediction:
    """A single-step or multi-step world-model prediction."""

    state_mean: np.ndarray
    state_std: np.ndarray
    feasible_probability: np.ndarray
    metadata: Optional[Dict] = None
