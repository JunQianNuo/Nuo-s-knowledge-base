from __future__ import annotations

from mathmodel.contracts import (
    CheckStatus,
    ComplexityProfile,
    GapClosureClaim,
    ModelCandidate,
    ModelRequirements,
)
from mathmodel.reasoning import evaluate_challenger, select_models


def shortest_path_requirements(*, negative: bool = False) -> ModelRequirements:
    edge_feature = "negative_edges" if negative else "nonnegative_edges"
    return ModelRequirements(
        mandatory_capabilities={"shortest_path"},
        mandatory_outputs={"path", "distance"},
        structural_features={"static", edge_feature},
        available_fields={"edges"},
    )


def dijkstra_candidate(*, evidence_count: int = 0) -> ModelCandidate:
    return ModelCandidate(
        candidate_id="classic.shortest-path",
        model_family="shortest-path",
        capabilities={"shortest_path"},
        covered_outputs={"path", "distance"},
        structural_features={"static", "nonnegative_edges"},
        required_data={"edges"},
        complexity=ComplexityProfile(time_tier=1, memory_tier=1),
        evidence_count=evidence_count,
    )


def dynamic_ant_colony_candidate(*, evidence_count: int = 20) -> ModelCandidate:
    return ModelCandidate(
        candidate_id="paper.dynamic-ant-colony",
        model_family="dynamic-routing",
        capabilities={"shortest_path"},
        covered_outputs={"path", "distance"},
        structural_features={"dynamic", "nonnegative_edges", "multiobjective"},
        required_data={"edges", "traffic_stream"},
        complexity=ComplexityProfile(
            additional_data_fields=1,
            latent_parameters=4,
            time_tier=4,
            memory_tier=2,
        ),
        evidence_count=evidence_count,
    )


def linear_program_requirements() -> ModelRequirements:
    return ModelRequirements(
        mandatory_capabilities={"linear_optimization"},
        mandatory_outputs={"decision", "objective"},
        structural_features={"linear", "continuous"},
        available_fields={"objective", "constraints"},
    )


def lp_candidate() -> ModelCandidate:
    return ModelCandidate(
        candidate_id="classic.linear-program",
        model_family="linear-program",
        capabilities={"linear_optimization"},
        covered_outputs={"decision", "objective"},
        structural_features={"linear", "continuous"},
        required_data={"objective", "constraints"},
        complexity=ComplexityProfile(time_tier=1, memory_tier=1),
    )


def ga_candidate(gap: GapClosureClaim | None) -> ModelCandidate:
    return ModelCandidate(
        candidate_id="heuristic.ga",
        model_family="linear-program",
        capabilities={"linear_optimization"},
        covered_outputs={"decision", "objective"},
        structural_features={"linear", "continuous"},
        required_data={"objective", "constraints"},
        complexity=ComplexityProfile(latent_parameters=3, time_tier=4),
        gap_closure=gap,
        evidence_count=30,
    )


def test_static_nonnegative_shortest_path_prefers_dijkstra_model() -> None:
    decision = select_models(
        shortest_path_requirements(),
        [dijkstra_candidate(), dynamic_ant_colony_candidate()],
    )

    assert decision.main is not None
    assert decision.main.candidate_id == "classic.shortest-path"
    assert decision.challenger is None
    assert decision.rejected["paper.dynamic-ant-colony"] == (
        "structure_mismatch",
        "missing_data:traffic_stream",
    )


def test_linear_problem_rejects_complex_candidate_without_gap_claim() -> None:
    decision = select_models(
        linear_program_requirements(),
        [lp_candidate(), ga_candidate(gap=None)],
    )

    assert decision.main is not None
    assert decision.main.candidate_id == "classic.linear-program"
    assert "missing_gap_closure_claim" in decision.rejected["heuristic.ga"]


def test_negative_edges_reject_dijkstra_structure() -> None:
    decision = select_models(
        shortest_path_requirements(negative=True), [dijkstra_candidate()]
    )

    assert decision.main is None
    assert decision.status is CheckStatus.BLOCKED
    assert decision.rejected["classic.shortest-path"] == ("structure_mismatch",)


def test_paper_count_cannot_override_a_failed_gate() -> None:
    decision = select_models(
        shortest_path_requirements(),
        [dynamic_ant_colony_candidate(evidence_count=10_000), dijkstra_candidate()],
    )

    assert decision.main is not None
    assert decision.main.candidate_id == "classic.shortest-path"


def test_valid_gap_claim_admits_at_most_one_challenger() -> None:
    gap = GapClosureClaim(
        baseline_model="classic.linear-program",
        addresses_gap="captures nonlinear loss",
        expected_gain="lower held-out decision cost",
        validation_test="same constraints and resource budget",
        minimum_practical_improvement=0.05,
    )
    decision = select_models(
        linear_program_requirements(),
        [ga_candidate(gap), lp_candidate()],
    )

    assert decision.main is not None
    assert decision.main.candidate_id == "classic.linear-program"
    assert decision.challenger is not None
    assert decision.challenger.candidate_id == "heuristic.ga"


def test_challenger_without_frozen_threshold_cannot_be_promoted() -> None:
    promotion = evaluate_challenger(
        observed_improvement=0.5,
        minimum_practical_improvement=None,
        stable=True,
        has_critical_failure=False,
        uncertainty_overlaps_zero=False,
    )

    assert promotion.promoted is False
    assert promotion.reason == "practical_improvement_threshold_not_frozen"


def test_challenger_promotes_only_after_stable_practical_gain() -> None:
    promotion = evaluate_challenger(
        observed_improvement=0.08,
        minimum_practical_improvement=0.05,
        stable=True,
        has_critical_failure=False,
        uncertainty_overlaps_zero=False,
    )

    assert promotion.promoted is True
    assert promotion.reason == "validated_practical_improvement"
