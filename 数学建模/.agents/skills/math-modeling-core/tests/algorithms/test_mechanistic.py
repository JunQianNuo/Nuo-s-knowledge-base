from __future__ import annotations

from math import exp

import numpy as np

from mathmodel.algorithms import ODESolverPlugin
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def test_ode_matches_exponential_analytic_solution() -> None:
    problem = ProblemSpec(
        problem_id="test-ode",
        model_family="ode",
        mandatory_outputs=("trajectory",),
        required_capabilities={"ode"},
    )
    t_eval = np.linspace(0.0, 1.0, 21)
    data = DataBundle(
        arrays={"y0": np.array([1.0]), "t_eval": t_eval},
        scalars={"t0": 0.0, "t1": 1.0},
        metadata={"rhs": lambda time, state: 2.0 * state},
    )

    result = ODESolverPlugin().solve(
        problem, data, SolveConfig(tolerance=1e-10)
    )

    assert result.status is RunStatus.SUCCESS
    times = np.asarray(result.solution["time"])
    states = np.asarray(result.solution["state"])
    assert np.all(np.diff(times) > 0)
    assert abs(states[0, -1] - exp(2.0)) < 1e-5
