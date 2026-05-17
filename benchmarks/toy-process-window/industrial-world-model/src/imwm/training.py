from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

import torch
from torch.utils.data import DataLoader

from imwm.data import ManufacturingSequenceDataset, WorldModelArrays


@dataclass
class TrainingReport:
    final_loss: float
    epochs: int
    device: str
    history: list[dict]


def _move_batch(batch: Dict[str, torch.Tensor], device: torch.device):
    return {k: v.to(device) for k, v in batch.items()}


def train_world_model(model: torch.nn.Module, arrays: WorldModelArrays, epochs: int = 20, batch_size: int = 128, learning_rate: float = 1e-3, weight_decay: float = 1e-5, device: Optional[str] = None, verbose: bool = True) -> TrainingReport:
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_device = torch.device(device)
    model.to(torch_device)
    dataset = ManufacturingSequenceDataset(arrays)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
    history = []
    final_loss = float("nan")
    for epoch in range(epochs):
        model.train()
        totals = {"total": 0.0, "nll": 0.0, "feasibility": 0.0, "reward": 0.0, "physics": 0.0, "kl": 0.0}
        count = 0
        for batch in loader:
            batch = _move_batch(batch, torch_device)
            optimizer.zero_grad()
            loss_dict = model.compute_loss(batch)
            loss_dict["total"].backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=5.0)
            optimizer.step()
            batch_size_actual = batch["history"].shape[0]
            count += batch_size_actual
            for key in totals:
                value = loss_dict[key]
                if torch.is_tensor(value):
                    value = float(value.detach().cpu())
                totals[key] += value * batch_size_actual
        epoch_report = {key: value / max(count, 1) for key, value in totals.items()}
        history.append(epoch_report)
        final_loss = epoch_report["total"]
        if verbose and (epoch == 0 or (epoch + 1) % 5 == 0 or epoch == epochs - 1):
            print(f"Epoch {epoch + 1:03d}/{epochs} | loss={epoch_report['total']:.4f} | nll={epoch_report['nll']:.4f} | physics={epoch_report['physics']:.4f}")
    return TrainingReport(final_loss=final_loss, epochs=epochs, device=device, history=history)
