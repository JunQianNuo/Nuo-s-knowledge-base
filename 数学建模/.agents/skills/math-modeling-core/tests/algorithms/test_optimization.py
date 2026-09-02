from __future__ import annotations

import numpy as np
from scipy.optimize import LinearConstraint

from mathmodel.algorithms import (
    LinearProgrammingPlugin,
    MixedIntegerLinearProgrammingPlugin,
    NonlinearOptimizationPlugin,
    SupportStatus,
)
from mathmodel.contracts import CheckStatus, DataBundle, ProblemSpec, RunStatus, SolveConfig


def optimization_problem(model_family: str) -> ProblemSpec:
    return ProblemSpec(
        problem_id=f"test-{model_family}",
        model_family=model_family,
        mandatory_outputs=("decision",),
        required_capabilities={model_family},
    )


def test_linear_programming_finds_hand_computed_optimum() -> None:
    plugin = LinearProgrammingPlugin()
    data = DataBundle(
        arrays={
            "c": np.array([-3.0, -2.0]),
            "A_ub": np.array([[1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]),
            "b_ub": np.array([4.0, 2.0, 3.0]),
        },
        metadata={"bounds": [(0.0, None), (0.0, None)]},
    )

    assert plugin.supports(optimization_problem("linear_programming"), data).status is SupportStatus.SUPPORTED
    result = plugin.solve(
        optimization_problem("linear_programming"), data, SolveConfig()
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["x"], [2.0, 2.0], atol=1e-8)
    assert abs(result.objective - (-10.0)) < 1e-8
    assert result.validation_report is not None
    assert result.validation_report.status is CheckStatus.PASS


def test_milp_knapsack_finds_enumerated_optimum() -> None:
    plugin = MixedIntegerLinearProgrammingPlugin()
    data = DataBundle(
        arrays={
            "values": np.array([3.0, 4.0, 5.0]),
            "weights": np.array([2.0, 3.0, 4.0]),
        },
        scalars={"capacity": 6.0},
    )

    result = plugin.solve(
        optimization_problem("mixed_integer_linear_programming"),
        data,
        SolveConfig(),
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_array_equal(result.solution["x"], [1, 0, 1])
    assert result.objective == 8.0
    assert float(np.dot(data.arrays["weights"], result.solution["x"])) <= 6.0


def test_nonlinear_convex_quadratic_matches_analytic_optimum() -> None:
    plugin = NonlinearOptimizationPlugin()
    data = DataBundle(
        arrays={"x0": np.array([4.0, 4.0])},
        metadata={
            "objective": lambda x: (x[0] - 1.0) ** 2 + (x[1] + 2.0) ** 2,
        },
    )

    result = plugin.solve(
        optimization_problem("nonlinear_optimization"), data, SolveConfig()
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["x"], [1.0, -2.0], atol=1e-6)
    assert result.objective is not None and result.objective < 1e-12


def test_nonlinear_default_honors_declared_inequality_constraint() -> None:
    plugin = NonlinearOptimizationPlugin()
    data = DataBundle(
        arrays={"x0": np.array([0.0])},
        metadata={
            "objective": lambda x: x[0] ** 2,
            "constraints": ({"type": "ineq", "fun": lambda x: x[0] - 1.0},),
        },
    )

    result = plugin.solve(
        optimization_problem("nonlinear_optimization"), data, SolveConfig()
    )

    assert result.status is RunStatus.SUCCESS
    assert result.solution["x"][0] >= 1.0 - 1e-7


def test_milp_preserves_continuous_components_of_mixed_solution() -> None:
    plugin = MixedIntegerLinearProgrammingPlugin()
    data = DataBundle(
        arrays={
            "c": np.array([0.0, 1.0]),
            "integrality": np.array([1, 0]),
            "lower_bounds": np.array([0.0, 0.0]),
            "upper_bounds": np.array([1.0, 1.0]),
            "constraints": np.array([[0.0, 1.0]]),
            "constraint_lower": np.array([0.5]),
            "constraint_upper": np.array([np.inf]),
        }
    )

    result = plugin.solve(
        optimization_problem("mixed_integer_linear_programming"), data, SolveConfig()
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["x"], [0.0, 0.5], atol=1e-10)


def test_nonlinear_accepts_scipy_constraint_object_without_ambiguous_comparison() -> None:
    result = NonlinearOptimizationPlugin().solve(
        optimization_problem("nonlinear_optimization"),
        DataBundle(
            arrays={"x0": np.array([0.0])},
            metadata={
                "objective": lambda x: x[0] ** 2,
                "constraints": LinearConstraint([[1.0]], [1.0], [np.inf]),
            },
        ),
        SolveConfig(),
    )

    assert result.status is RunStatus.SUCCESS
    assert result.solution["x"][0] >= 1.0 - 1e-7
