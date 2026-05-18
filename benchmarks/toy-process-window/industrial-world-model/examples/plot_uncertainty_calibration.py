"""Plot predicted uncertainty vs. absolute prediction error on the test set.

This is a simple diagnostic example for the synthetic industrial world model.
It trains the demo model with small defaults so it stays beginner-friendly,
runs the trained model on the held-out test set, and saves a scatter plot
that shows whether the model's quality uncertainty grows with its error.

A well-calibrated model should roughly show larger predicted uncertainty
where the absolute error is also larger. Points clustered far from that
trend reveal under- or over-confident predictions.

Run from the ``industrial-world-model`` directory:

    python examples/plot_uncertainty_calibration.py
"""

from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader

from imwm.data import ManufacturingSequenceDataset, generate_world_model_dataset, split_dataset
from imwm.models.rssm import ManufacturingRSSM
from imwm.physics import QUALITY_INDEX
from imwm.training import train_world_model


def main():
    # Smaller defaults than run_demo.py so the script stays quick for first-time contributors.
    arrays = generate_world_model_dataset(num_episodes=40, episode_length=30, history_length=8, seed=7)
    train_arrays, test_arrays = split_dataset(arrays, train_fraction=0.8, seed=7)
    model = ManufacturingRSSM(
        input_dim=arrays.input_dim,
        action_dim=arrays.action_dim,
        state_dim=arrays.state_dim,
        hidden_dim=128,
        latent_dim=32,
    )
    train_world_model(model=model, arrays=train_arrays, epochs=10, batch_size=128, learning_rate=1e-3, verbose=True)

    # Iterate the test set and collect predicted quality, predicted uncertainty, and target quality.
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    model.eval()
    dataset = ManufacturingSequenceDataset(test_arrays)
    loader = DataLoader(dataset, batch_size=256, shuffle=False)
    predicted_quality, predicted_uncertainty, target_quality = [], [], []
    with torch.no_grad():
        for batch in loader:
            history = batch["history"].to(device)
            action = batch["action"].to(device)
            target = batch["next_state"].to(device)
            pred = model.forward(history, action, rollout_steps=1, deterministic=True)
            predicted_quality.append(pred["state_mean"][:, 0, QUALITY_INDEX].cpu().numpy())
            predicted_uncertainty.append(pred["state_std"][:, 0, QUALITY_INDEX].cpu().numpy())
            target_quality.append(target[:, QUALITY_INDEX].cpu().numpy())
    predicted_quality = np.concatenate(predicted_quality)
    predicted_uncertainty = np.concatenate(predicted_uncertainty)
    target_quality = np.concatenate(target_quality)
    absolute_error = np.abs(predicted_quality - target_quality)

    # Print a tiny numeric summary so the plot is easy to interpret without opening the file.
    print("\nTest-set quality summary:")
    print(f"  samples: {predicted_quality.shape[0]}")
    print(f"  mean absolute error: {absolute_error.mean():.4f}")
    print(f"  mean predicted uncertainty: {predicted_uncertainty.mean():.4f}")
    correlation = float(np.corrcoef(predicted_uncertainty, absolute_error)[0, 1])
    print(f"  uncertainty/error correlation: {correlation:.4f}")

    # Save a single scatter plot: x = predicted uncertainty, y = absolute prediction error.
    # Points near a rising diagonal mean the model is roughly calibrated; flat or noisy
    # clouds suggest the uncertainty estimate doesn't track real error.
    import matplotlib.pyplot as plt

    output_path = Path(__file__).with_name("uncertainty_calibration.png")
    plt.figure(figsize=(6.5, 5.5))
    plt.scatter(predicted_uncertainty, absolute_error, alpha=0.5, s=18)
    plt.xlabel("Predicted uncertainty (state_std on quality)")
    plt.ylabel("Absolute prediction error on quality")
    plt.title("Uncertainty calibration: predicted std vs. observed error")
    plt.grid(True, linestyle=":", linewidth=0.6)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=180)
    plt.close()
    print(f"\nSaved plot: {output_path}")


if __name__ == "__main__":
    main()
