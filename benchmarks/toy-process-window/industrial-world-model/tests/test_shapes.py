import torch

from imwm.data import generate_world_model_dataset
from imwm.models.rssm import ManufacturingRSSM
from imwm.planning import CEMPlanner


def test_dataset_shapes():
    arrays = generate_world_model_dataset(num_episodes=3, episode_length=12, history_length=4)
    assert arrays.histories.ndim == 3
    assert arrays.actions.shape[-1] == 2
    assert arrays.next_states.shape[-1] == 5
    assert arrays.input_dim == 7


def test_model_forward_shapes():
    arrays = generate_world_model_dataset(num_episodes=3, episode_length=12, history_length=4)
    model = ManufacturingRSSM(input_dim=arrays.input_dim, action_dim=2, state_dim=5)
    history = torch.tensor(arrays.histories[:6], dtype=torch.float32)
    action = torch.tensor(arrays.actions[:6], dtype=torch.float32)
    pred = model.forward(history, action, rollout_steps=3, deterministic=True)
    assert pred["state_mean"].shape == (6, 3, 5)
    assert pred["state_std"].shape == (6, 3, 5)
    assert pred["feasibility_logit"].shape == (6, 3, 1)


def test_planner_returns_action():
    arrays = generate_world_model_dataset(num_episodes=3, episode_length=12, history_length=4)
    model = ManufacturingRSSM(input_dim=arrays.input_dim, action_dim=2, state_dim=5)
    planner = CEMPlanner(candidates=16, iterations=2, horizon=2)
    action, report = planner.plan(model, arrays.sample_history(0), device="cpu")
    assert action.shape == (2,)
    assert 0.0 <= action[0] <= 1.0
    assert 0.0 <= action[1] <= 1.0
    assert "laser_power" in report.best_action_physical
