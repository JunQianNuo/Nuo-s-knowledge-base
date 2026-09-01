from __future__ import annotations

import numpy as np

from mathmodel.algorithms import PCAPlugin
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def test_pca_orders_literal_diagonal_covariance_and_is_orthonormal() -> None:
    x = np.array([[2.0, 0.0], [-2.0, 0.0], [0.0, 1.0], [0.0, -1.0]])
    problem = ProblemSpec(
        problem_id="test-pca",
        model_family="pca",
        mandatory_outputs=("components",),
        required_capabilities={"pca"},
    )

    result = PCAPlugin().solve(
        problem,
        DataBundle(arrays={"X": x}, scalars={"n_components": 2}),
        SolveConfig(),
    )

    components = np.asarray(result.solution["components"])
    assert result.status is RunStatus.SUCCESS
    np.testing.assert_allclose(result.solution["explained_variance"], [8 / 3, 2 / 3])
    np.testing.assert_allclose(components @ components.T, np.eye(2), atol=1e-12)
    assert result.solution["explained_variance"][0] > result.solution["explained_variance"][1]
