from __future__ import annotations

from typing import Dict, Optional

import torch
from torch.utils.data import DataLoader

from imwm.data import ManufacturingSequenceDataset, WorldModelArrays
from imwm.physics import DEFECT_INDEX, QUALITY_INDEX


def evaluate_world_model(model: torch.nn.Module, arrays: WorldModelArrays, batch_size: int = 256, device: Optional[str] = None) -> Dict[str, float]:
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_device = torch.device(device)
    model.to(torch_device)
    model.eval()
    dataset = ManufacturingSequenceDataset(arrays)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    all_mean, all_std, all_target, all_feasible_prob, all_feasible_target = [], [], [], [], []
    with torch.no_grad():
        for batch in loader:
            history = batch["history"].to(torch_device)
            action = batch["action"].to(torch_device)
            target = batch["next_state"].to(torch_device)
            feasible = batch["feasible"].to(torch_device)
            pred = model.forward(history, action, rollout_steps=1, deterministic=True)
            mean = pred["state_mean"][:, 0, :]
            std = pred["state_std"][:, 0, :]
            feasible_prob = torch.sigmoid(pred["feasibility_logit"][:, 0, :])
            all_mean.append(mean.cpu())
            all_std.append(std.cpu())
            all_target.append(target.cpu())
            all_feasible_prob.append(feasible_prob.cpu())
            all_feasible_target.append(feasible.cpu())
    mean = torch.cat(all_mean, dim=0)
    std = torch.cat(all_std, dim=0)
    target = torch.cat(all_target, dim=0)
    feasible_prob = torch.cat(all_feasible_prob, dim=0)
    feasible_target = torch.cat(all_feasible_target, dim=0)
    error = mean - target
    mae = torch.abs(error).mean().item()
    rmse = torch.sqrt((error ** 2).mean()).item()
    lower = mean - 1.96 * std
    upper = mean + 1.96 * std
    picp = ((target >= lower) & (target <= upper)).float().mean().item()
    feasible_pred = (feasible_prob >= 0.5).float()
    feasible_acc = (feasible_pred == feasible_target).float().mean().item()
    quality_mae = torch.abs(error[:, QUALITY_INDEX]).mean().item()
    defect_mae = torch.abs(error[:, DEFECT_INDEX]).mean().item()
    return {"mae": mae, "rmse": rmse, "picp_95": picp, "feasible_accuracy": feasible_acc, "quality_mae": quality_mae, "defect_mae": defect_mae}
