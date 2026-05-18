from imwm.envs import ToolWearEnvironment


def main():
    env = ToolWearEnvironment(episode_length=3, seed=11)
    state = env.reset()
    print("Initial state:", state)

    for action in ([0.35, 0.80], [0.65, 0.55], [0.85, 0.35]):
        result = env.step(action)
        print(
            "step",
            env.t,
            "state=",
            result.state,
            "reward=",
            round(result.reward, 4),
            "done=",
            result.done,
        )


if __name__ == "__main__":
    main()
