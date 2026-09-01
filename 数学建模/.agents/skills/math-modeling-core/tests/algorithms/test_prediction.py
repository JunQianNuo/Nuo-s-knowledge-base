from __future__ import annotations

import numpy as np

from mathmodel.algorithms import (
    ARIMAPlugin,
    LinearRegressionPlugin,
    RandomForestPlugin,
    RidgeRegressionPlugin,
)
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def problem(model_family: str) -> ProblemSpec:
    return ProblemSpec(
        problem_id=f"test-{model_family}",
        model_family=model_family,
        mandatory_outputs=("prediction",),
        required_capabilities={model_family},
    )


def test_linear_regression_recovers_noiseless_coefficients() -> None:
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1], [2, -1]], dtype=float)
    y = 3.0 + 2.0 * x[:, 0] - x[:, 1]

    result = LinearRegressionPlugin().solve(
        problem("linear_regression"),
        DataBundle(arrays={"X": x, "y": y, "X_predict": x}),
        SolveConfig(),
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["coefficients"], [2.0, -1.0], atol=1e-12)
    assert abs(result.solution["intercept"] - 3.0) < 1e-12
    assert result.metrics["residual_mse"] < 1e-24


def test_ridge_matches_closed_form_on_orthogonal_design() -> None:
    x = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]], dtype=float)
    y = x @ np.array([4.0, -2.0])

    result = RidgeRegressionPlugin().solve(
        problem("ridge_regression"),
        DataBundle(
            arrays={"X": x, "y": y, "X_predict": x},
            scalars={"alpha": 2.0, "fit_intercept": False},
        ),
        SolveConfig(),
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["coefficients"], [2.0, -1.0], atol=1e-12)
    assert result.solution["intercept"] == 0.0


def test_arima_forecast_is_chronological_finite_and_repeatable() -> None:
    series = np.array([1.0, 0.8, 0.7, 0.55, 0.5, 0.4, 0.34, 0.28, 0.23, 0.2])
    data = DataBundle(
        arrays={"series": series},
        scalars={"horizon": 3},
        metadata={"order": (1, 0, 0)},
    )
    plugin = ARIMAPlugin()

    first = plugin.solve(problem("arima"), data, SolveConfig(seed=7))
    second = plugin.solve(problem("arima"), data, SolveConfig(seed=7))

    forecasts = np.asarray(first.solution["forecast"])
    assert first.status is RunStatus.SUCCESS
    assert forecasts.shape == (3,)
    assert np.all(np.isfinite(forecasts))
    np.testing.assert_allclose(first.solution["forecast"], second.solution["forecast"])
    assert first.diagnostics["train_end_index"] == 9
    assert first.diagnostics["forecast_start_index"] == 10


def test_seeded_random_forest_predictions_are_repeatable_probabilities() -> None:
    x = np.array(
        [[-2, -1], [-1, -2], [-1, -1], [1, 1], [1, 2], [2, 1]],
        dtype=float,
    )
    y = np.array([0, 0, 0, 1, 1, 1])
    x_predict = np.array([[-1.5, -1.5], [1.5, 1.5]])
    data = DataBundle(
        arrays={"X": x, "y": y, "X_predict": x_predict},
        scalars={"n_estimators": 40},
        metadata={"task": "classification"},
    )
    plugin = RandomForestPlugin()

    first = plugin.solve(problem("random_forest"), data, SolveConfig(seed=11))
    second = plugin.solve(problem("random_forest"), data, SolveConfig(seed=11))

    assert first.status is RunStatus.SUCCESS
    np.testing.assert_array_equal(first.solution["predictions"], [0, 1])
    np.testing.assert_array_equal(first.solution["predictions"], second.solution["predictions"])
    probabilities = np.asarray(first.solution["probabilities"])
    assert np.all((0.0 <= probabilities) & (probabilities <= 1.0))
    np.testing.assert_allclose(probabilities.sum(axis=1), 1.0)
