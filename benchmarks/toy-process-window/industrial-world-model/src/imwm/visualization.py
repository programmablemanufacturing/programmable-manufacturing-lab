from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import torch


def plot_process_window(model: torch.nn.Module, history: torch.Tensor, output_path: str | Path, grid_resolution: int = 60, recommended_action: Optional[np.ndarray] = None, device: Optional[str] = None) -> Path:
    """Save a process-window quality map for the current history."""
    import matplotlib.pyplot as plt
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    output_path = Path(output_path)
    model.to(device)
    model.eval()
    if history.dim() == 2:
        history = history.unsqueeze(0)
    history = history.to(device)
    x = np.linspace(0.0, 1.0, grid_resolution, dtype=np.float32)
    y = np.linspace(0.0, 1.0, grid_resolution, dtype=np.float32)
    X, Y = np.meshgrid(x, y)
    actions = np.stack([X.ravel(), Y.ravel()], axis=-1).astype(np.float32)
    with torch.no_grad():
        hist_batch = history.repeat(actions.shape[0], 1, 1)
        action_batch = torch.tensor(actions, dtype=torch.float32, device=device)
        pred = model.forward(hist_batch, action_batch, rollout_steps=1, deterministic=True)
        quality = pred["state_mean"][:, 0, 4].detach().cpu().numpy().reshape(grid_resolution, grid_resolution)
        defect = pred["state_mean"][:, 0, 3].detach().cpu().numpy().reshape(grid_resolution, grid_resolution)
    plt.figure(figsize=(7.5, 6.0))
    surface = plt.contourf(X, Y, quality, levels=30)
    plt.colorbar(surface, label="Predicted quality score")
    plt.contour(X, Y, defect, levels=[0.25], linewidths=2.0)
    if recommended_action is not None:
        plt.scatter([recommended_action[0]], [recommended_action[1]], marker="*", s=220, label="Recommended action")
        plt.legend()
    plt.xlabel("Normalized laser power control")
    plt.ylabel("Normalized scan speed control")
    plt.title("Industrial World Model Process Window")
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=180)
    plt.close()
    return output_path
