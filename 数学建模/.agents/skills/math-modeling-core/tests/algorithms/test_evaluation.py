from __future__ import annotations

import numpy as np

from mathmodel.algorithms import AHPPlugin, EntropyWeightPlugin, TOPSISPlugin
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def evaluation_problem(model_family: str) -> ProblemSpec:
    return ProblemSpec(
        problem_id=f"test-{model_family}",
        model_family=model_family,
        mandatory_outputs=("weights_or_rank",),
        required_capabilities={model_family},
    )


def test_ahp_recovers_consistent_literal_weights() -> None:
    expected = np.array([0.5, 0.3, 0.2])
    pairwise = expected[:, None] / expected[None, :]

    result = AHPPlugin().solve(
        evaluation_problem("ahp"),
        DataBundle(arrays={"pairwise": pairwise}),
        SolveConfig(),
    )

    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["weights"], expected, atol=1e-12)
    assert abs(result.metrics["consistency_ratio"]) < 1e-12


def test_entropy_weight_handles_constant_column_deterministically() -> None:
    matrix = np.array(
        [
            [1.0, 7.0, 4.0],
            [2.0, 7.0, 2.0],
            [4.0, 7.0, 1.0],
        ]
    )
    plugin = EntropyWeightPlugin()

    first = plugin.solve(
        evaluation_problem("entropy_weight"),
        DataBundle(arrays={"decision_matrix": matrix}),
        SolveConfig(),
    )
    second = plugin.solve(
        evaluation_problem("entropy_weight"),
        DataBundle(arrays={"decision_matrix": matrix}),
        SolveConfig(),
    )

    weights = np.asarray(first.solution["weights"])
    assert first.status is RunStatus.SUCCESS
    assert np.all(weights >= 0)
    assert abs(weights.sum() - 1.0) < 1e-12
    assert weights[1] == 0.0
    np.testing.assert_array_equal(first.solution["weights"], second.solution["weights"])


def test_topsis_honors_benefit_and_cost_directions() -> None:
    matrix = np.array(
        [
            [8.0, 5.0],
            [9.0, 3.0],
            [6.0, 8.0],
        ]
    )

    result = TOPSISPlugin().solve(
        evaluation_problem("topsis"),
        DataBundle(
            arrays={
                "decision_matrix": matrix,
                "weights": np.array([0.5, 0.5]),
            },
            metadata={"directions": ("benefit", "cost")},
        ),
        SolveConfig(),
    )

    scores = np.asarray(result.solution["scores"])
    assert result.status is RunStatus.SUCCESS
    assert result.solution["rank"] == [1, 0, 2]
    assert np.all((0.0 <= scores) & (scores <= 1.0))
