from scenarios.runner import run_monte_carlo


def test_monte_carlo_returns_summary_metrics():
    summary = run_monte_carlo("scenarios/cold_morning.yaml", n_runs=2)

    assert set(summary) == {
        "mean_absolute_error_C",
        "minimum_room_temp_C",
        "heater_duty",
    }
    for values in summary.values():
        assert set(values) == {"mean", "std"}
        assert values["std"] >= 0.0


def test_monte_carlo_requires_at_least_one_run():
    try:
        run_monte_carlo("scenarios/cold_morning.yaml", n_runs=0)
    except ValueError:
        pass
    else:
        raise AssertionError("At least one Monte Carlo run should be required")