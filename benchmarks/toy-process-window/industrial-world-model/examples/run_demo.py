from pathlib import Path

from imwm.data import generate_world_model_dataset, split_dataset
from imwm.evaluation import evaluate_world_model
from imwm.models.rssm import ManufacturingRSSM
from imwm.planning import CEMPlanner
from imwm.training import train_world_model
from imwm.visualization import plot_process_window


def main():
    arrays = generate_world_model_dataset(num_episodes=80, episode_length=40, history_length=8, seed=7)
    train_arrays, test_arrays = split_dataset(arrays, train_fraction=0.82, seed=7)
    model = ManufacturingRSSM(input_dim=arrays.input_dim, action_dim=arrays.action_dim, state_dim=arrays.state_dim, hidden_dim=128, latent_dim=32)
    train_world_model(model=model, arrays=train_arrays, epochs=20, batch_size=128, learning_rate=1e-3, verbose=True)
    metrics = evaluate_world_model(model, test_arrays)
    print("\nEvaluation metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value:.4f}")
    history = test_arrays.sample_history(index=0)
    planner = CEMPlanner(candidates=512, iterations=5, horizon=3, seed=11)
    best_action, report = planner.plan(model, history)
    print("\nRecommended normalized action:")
    print(f"  {best_action}")
    print("\nRecommended physical action:")
    for key, value in report.best_action_physical.items():
        print(f"  {key}: {value:.3f}")
    print("\nPredicted planning report:")
    print(f"  score: {report.best_score:.4f}")
    print(f"  predicted_quality: {report.predicted_quality:.4f}")
    print(f"  predicted_defect_risk: {report.predicted_defect_risk:.4f}")
    print(f"  predicted_quality_uncertainty: {report.predicted_quality_uncertainty:.4f}")
    print(f"  feasible_probability: {report.feasible_probability:.4f}")
    output_path = Path(__file__).with_name("process_window_recommendation.png")
    plot_process_window(model, history, output_path=output_path, recommended_action=best_action)
    print(f"\nSaved plot: {output_path}")


if __name__ == "__main__":
    main()
