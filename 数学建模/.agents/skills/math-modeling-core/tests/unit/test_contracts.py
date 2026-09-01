from __future__ import annotations

import numpy as np
import pytest

from mathmodel.contracts import (
    CheckStatus,
    ComplexityProfile,
    DataBundle,
    GapClosureClaim,
    ModelCandidate,
    ModelRequirements,
    ProblemSpec,
    RunStatus,
    Severity,
    SolveConfig,
    SolveResult,
    ValidationCheck,
    ValidationReport,
)


def test_data_bundle_separates_arrays_scalars_and_metadata() -> None:
    bundle = DataBundle(
        arrays={"x": np.array([1.0])},
        scalars={"alpha": 2.0},
        metadata={"unit": "m"},
    )

    assert bundle.arrays["x"].tolist() == [1.0]
    assert bundle.scalars == {"alpha": 2.0}
    assert bundle.metadata == {"unit": "m"}


def test_problem_spec_rejects_empty_mandatory_outputs() -> None:
    with pytest.raises(ValueError, match="mandatory_outputs"):
        ProblemSpec(problem_id="p", model_family="graph", mandatory_outputs=())


def test_problem_spec_normalizes_capabilities_to_frozenset() -> None:
    problem = ProblemSpec(
        problem_id="p",
        model_family="graph",
        mandatory_outputs=("path",),
        required_capabilities={"shortest_path", "nonnegative_edges"},
    )

    assert problem.required_capabilities == frozenset(
        {"shortest_path", "nonnegative_edges"}
    )


def test_solve_config_rejects_nonpositive_timeout() -> None:
    with pytest.raises(ValueError, match="timeout"):
        SolveConfig(timeout=0)


def test_complexity_profile_rejects_negative_counts() -> None:
    with pytest.raises(ValueError, match="nonnegative"):
        ComplexityProfile(additional_data_fields=-1)


def test_model_requirements_requires_capabilities() -> None:
    with pytest.raises(ValueError, match="mandatory_capabilities"):
        ModelRequirements(mandatory_capabilities=frozenset())


def test_gap_closure_claim_requires_a_measurable_gain() -> None:
    with pytest.raises(ValueError, match="expected_gain"):
        GapClosureClaim(
            baseline_model="classic.linear-program",
            addresses_gap="captures nonlinear loss",
            expected_gain="",
            validation_test="held-out objective",
        )


def test_model_candidate_requires_stable_id() -> None:
    with pytest.raises(ValueError, match="candidate_id"):
        ModelCandidate(candidate_id="", model_family="linear-program")


def test_validation_contracts_keep_status_and_severity() -> None:
    check = ValidationCheck(
        name="finite-objective",
        status=CheckStatus.PASS,
        severity=Severity.CRITICAL,
        observed=True,
        threshold=True,
    )
    report = ValidationReport(status=CheckStatus.PASS, checks=(check,))

    assert report.checks == (check,)
    assert report.status is CheckStatus.PASS


def test_solve_result_exposes_machine_status_and_solution() -> None:
    result = SolveResult(
        status=RunStatus.SUCCESS,
        plugin_id="graph.dijkstra",
        solution={"path": ["A", "B"]},
        objective=3.0,
    )

    assert result.status is RunStatus.SUCCESS
    assert result.solution["path"] == ["A", "B"]
