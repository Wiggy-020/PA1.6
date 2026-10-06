import argparse
from scenarios.runner import run_monte_carlo, run_scenario

def main():
    parser = argparse.ArgumentParser(description="Run a room temperature scenario")
    parser.add_argument("--scenario", required=True, help="Path to YAML scenario file")
    parser.add_argument(
        "--monte-carlo",
        type=int,
        metavar="N",
        help="Run N simulations with different random seeds and summarize the results",
    )
    args = parser.parse_args()
    if args.monte_carlo is None:
        run_scenario(args.scenario)
        return
    if args.monte_carlo < 1:
        parser.error("--monte-carlo must be at least 1")

    summary = run_monte_carlo(args.scenario, n_runs=args.monte_carlo)
    print(f"Completed {args.monte_carlo} simulations")
    for metric, values in summary.items():
        print(f"{metric}: mean={values['mean']:.3f}, std={values['std']:.3f}")

if __name__ == "__main__":
    main()
