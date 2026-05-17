from imwm.data import generate_world_model_dataset
from imwm.models.rssm import ManufacturingRSSM
from imwm.training import train_world_model


def main():
    arrays = generate_world_model_dataset(num_episodes=120, episode_length=50, history_length=8)
    model = ManufacturingRSSM(input_dim=arrays.input_dim, action_dim=arrays.action_dim, state_dim=arrays.state_dim)
    train_world_model(model, arrays, epochs=30, batch_size=128)


if __name__ == "__main__":
    main()
