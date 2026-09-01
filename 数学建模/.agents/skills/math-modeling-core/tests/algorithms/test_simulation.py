from __future__ import annotations

import numpy as np

from mathmodel.algorithms import MonteCarloPlugin
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def test_monte_carlo_integral_is_seeded_and_interval_covers_truth() -> None:
    problem = ProblemSpec(
        problem_id="test-monte-carlo",
        model_family="monte_carlo",
        mandatory_outputs=("estimate", "confidence_interval"),
        required_capabilities={"monte_carlo"},
    )
    data = DataBundle(
        arrays={"bounds": np.array([[0.0, 1.0]])},
        scalars={"n_samples": 100_000, "confidence": 0.95},
        metadata={"integrand": lambda points: points[:, 0] ** 2},
    )
    plugin = MonteCarloPlugin()

    first = plugin.solve(problem, data, SolveConfig(seed=123))
    second = plugin.solve(problem, data, SolveConfig(seed=123))

    assert first.status is RunStatus.SUCCESS
    assert first.solution == second.solution
    assert first.solution["ci_low"] < 1 / 3 < first.solution["ci_high"]
    assert first.solution["ci_low"] <= first.solution["estimate"] <= first.solution["ci_high"]
