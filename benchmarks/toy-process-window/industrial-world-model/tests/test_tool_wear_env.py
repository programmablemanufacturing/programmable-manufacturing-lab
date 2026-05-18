import numpy as np

from imwm.envs import ToolWearEnvironment


def test_tool_wear_environment_steps_with_bounded_state():
    env = ToolWearEnvironment(episode_length=2, seed=4)

    initial_state = env.reset()
    result = env.step(np.array([0.80, 0.25], dtype=np.float32))

    assert initial_state.shape == (4,)
    assert result.state.shape == (4,)
    assert np.all(result.state >= 0.0)
    assert np.all(result.state <= 1.0)
    assert result.info["wear_level"] >= float(initial_state[0])
    assert result.info["wear_increment"] >= 0.0
    assert result.done is False

    second = env.step(np.array([0.60, 0.70], dtype=np.float32))
    assert second.done is True


def test_tool_wear_environment_is_seed_reproducible():
    first = ToolWearEnvironment(seed=9)
    second = ToolWearEnvironment(seed=9)

    np.testing.assert_allclose(first.reset(), second.reset())
    np.testing.assert_allclose(first.step([0.45, 0.75]).state, second.step([0.45, 0.75]).state)
