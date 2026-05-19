# Industrial Manufacturing World Model v0.1

A minimal, runnable open-source scaffold for **industrial manufacturing world models**.

This project represents manufacturing as:

```text
history of process states + controllable process action
    -> predicted next process state
    -> uncertainty estimate
    -> feasibility / defect risk
    -> recommended next process action
```

It is inspired by latent world-model ideas such as RSSM-style dynamics, but it is intentionally adapted to manufacturing process modeling rather than games, robotics video, or general 3D scene generation.

## What this package includes

- A synthetic manufacturing environment with explicit process physics proxies
- A sequence dataset generator for manufacturing process histories
- An RSSM-inspired latent dynamics model
- Uncertainty-aware state prediction
- Feasibility and defect-risk prediction
- Physics-consistency regularization
- CEM-based process-window planning
- Evaluation metrics for prediction and uncertainty calibration
- Visualization for process-window recommendations
- A runnable demo
- Unit tests

## What this package does not include

This repository does **not** include proprietary industrial datasets, partner-specific workflows, sensitive process parameters, or production optimization logic.

The included process model is synthetic and educational. It is designed to make the architecture concrete and extensible.

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Run the demo

```bash
python examples/run_demo.py
```

The demo will:

1. Generate synthetic manufacturing process episodes
2. Train an RSSM-inspired world model
3. Evaluate prediction and uncertainty metrics
4. Recommend the next process action using CEM planning
5. Save a process-window visualization

Expected output includes:

```text
Recommended normalized action: [...]
Recommended physical action: {'laser_power': ..., 'scan_speed': ...}
Saved plot: examples/process_window_recommendation.png
```

## Uncertainty calibration plot

```bash
python examples/plot_uncertainty_calibration.py
```

This example trains the demo model on a smaller dataset, runs it on the held-out test set, and saves a scatter plot at `examples/uncertainty_calibration.png` comparing the predicted quality uncertainty (x-axis) with the absolute prediction error (y-axis). A roughly rising trend means the model's uncertainty grows with its real error; a flat cloud suggests the uncertainty estimate is not tracking error well.

## Project structure

```text
src/imwm/
  core.py                    # Dataclasses and common interfaces
  physics.py                 # Synthetic manufacturing physics proxies
  data.py                    # Episode generation and dataset utilities
  training.py                # Training loop
  evaluation.py              # Evaluation metrics
  planning.py                # CEM process-window planner
  visualization.py           # Process-window plotting
  envs/toy_process.py        # Synthetic manufacturing environment
  models/rssm.py             # RSSM-inspired latent dynamics model

examples/
  run_demo.py                       # End-to-end runnable demo
  plot_uncertainty_calibration.py   # Scatter plot of predicted uncertainty vs. absolute error

tests/
  test_shapes.py             # Basic shape and planner tests
```

## Conceptual API

```python
from imwm.data import generate_world_model_dataset
from imwm.models.rssm import ManufacturingRSSM
from imwm.training import train_world_model
from imwm.planning import CEMPlanner

dataset = generate_world_model_dataset(num_episodes=80, episode_length=40, history_length=8)

model = ManufacturingRSSM(
    input_dim=dataset.input_dim,
    action_dim=dataset.action_dim,
    state_dim=dataset.state_dim,
)

train_world_model(model, dataset, epochs=10)

planner = CEMPlanner()
best_action, report = planner.plan(model, dataset.sample_history())
```

## Extension ideas

Good first contributions:

- Add a new synthetic manufacturing environment
- Add real CSV time-series loading
- Add alternative planning policies
- Add new industrial metrics such as Cp/Cpk-style capability proxies
- Add uncertainty calibration diagnostics
- Add a notebook comparing physics-only vs. learned world-model planning
