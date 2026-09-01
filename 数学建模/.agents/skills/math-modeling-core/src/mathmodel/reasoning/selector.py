from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from types import MappingProxyType
from typing import Mapping, Sequence

from mathmodel.contracts import (
    CheckStatus,
    ModelCandidate,
    ModelRequirements,
)


class GateState(StrEnum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True, slots=True)
class GateResult:
    name: str
    state: GateState
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class CandidateAssessment:
    candidate: ModelCandidate
    gates: tuple[GateResult, ...]

    @property
    def eligible(self) -> bool:
        return all(gate.state is GateState.PASS for gate in self.gates)

    @property
    def rejection_reasons(self) -> tuple[str, ...]:
        return tuple(reason for gate in self.gates for reason in gate.reasons)


@dataclass(frozen=True, slots=True)
class ModelSelectionDecision:
    status: CheckStatus
    main: ModelCandidate | None
    challenger: ModelCandidate | None
    assessments: tuple[CandidateAssessment, ...]
    rejected: Mapping[str, tuple[str, ...]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "assessments", tuple(self.assessments))
        object.__setattr__(self, "rejected", MappingProxyType(dict(self.rejected)))


@dataclass(frozen=True, slots=True)
class PromotionDecision:
    promoted: bool
    reason: str


def _boolean_gate(name: str, value: bool | None, reason: str) -> GateResult:
    if value is True:
        return GateResult(name=name, state=GateState.PASS)
    if value is False:
        return GateResult(name=name, state=GateState.FAIL, reasons=(reason,))
    return GateResult(
        name=name,
        state=GateState.UNKNOWN,
        reasons=(f"{reason}_unknown",),
    )


def assess_candidate(
    requirements: ModelRequirements, candidate: ModelCandidate
) -> CandidateAssessment:
    coverage_reasons: list[str] = []
    missing_capabilities = sorted(
        requirements.mandatory_capabilities - candidate.capabilities
    )
    if missing_capabilities:
        coverage_reasons.append(
            "missing_capabilities:" + ",".join(missing_capabilities)
        )
    missing_outputs = sorted(requirements.mandatory_outputs - candidate.covered_outputs)
    if missing_outputs:
        coverage_reasons.append("missing_outputs:" + ",".join(missing_outputs))
    coverage = GateResult(
        name="coverage",
        state=GateState.FAIL if coverage_reasons else GateState.PASS,
        reasons=tuple(coverage_reasons),
    )

    structure_ok = requirements.structural_features.issubset(
        candidate.structural_features
    )
    structure = GateResult(
        name="structure",
        state=GateState.PASS if structure_ok else GateState.FAIL,
        reasons=() if structure_ok else ("structure_mismatch",),
    )

    constraints = _boolean_gate(
        "constraints", candidate.constraints_supported, "constraints_unsupported"
    )
    assumptions = _boolean_gate(
        "assumptions", candidate.assumptions_verified, "assumptions_unverified"
    )

    missing_data = sorted(candidate.required_data - requirements.available_fields)
    data = GateResult(
        name="data",
        state=GateState.FAIL if missing_data else GateState.PASS,
        reasons=tuple(f"missing_data:{name}" for name in missing_data),
    )
    identifiable = _boolean_gate(
        "identifiability", candidate.identifiable, "not_identifiable"
    )
    validation = _boolean_gate(
        "validation", candidate.validation_path, "validation_path_missing"
    )

    return CandidateAssessment(
        candidate=candidate,
        gates=(
            coverage,
            structure,
            constraints,
            assumptions,
            data,
            identifiable,
            validation,
        ),
    )


def _complexity_vector(candidate: ModelCandidate) -> tuple[int, ...]:
    profile = candidate.complexity
    return (
        profile.additional_data_fields,
        profile.latent_parameters,
        profile.unverified_critical_assumptions,
        profile.model_dimension_tier,
        profile.time_tier,
        profile.memory_tier,
    )


def _dominates(left: ModelCandidate, right: ModelCandidate) -> bool:
    left_vector = _complexity_vector(left)
    right_vector = _complexity_vector(right)
    return all(a <= b for a, b in zip(left_vector, right_vector, strict=True)) and any(
        a < b for a, b in zip(left_vector, right_vector, strict=True)
    )


def _minimum_sufficient(candidates: Sequence[ModelCandidate]) -> ModelCandidate:
    nondominated = [
        candidate
        for candidate in candidates
        if not any(
            other is not candidate and _dominates(other, candidate)
            for other in candidates
        )
    ]
    return min(
        nondominated,
        key=lambda candidate: (candidate.complexity.sort_key(), candidate.candidate_id),
    )


def select_models(
    requirements: ModelRequirements,
    candidates: Sequence[ModelCandidate],
) -> ModelSelectionDecision:
    assessments = tuple(
        assess_candidate(requirements, candidate) for candidate in candidates
    )
    rejected: dict[str, tuple[str, ...]] = {
        assessment.candidate.candidate_id: assessment.rejection_reasons
        for assessment in assessments
        if not assessment.eligible
    }
    eligible = [
        assessment.candidate for assessment in assessments if assessment.eligible
    ]
    baseline_candidates = [
        candidate
        for candidate in eligible
        if candidate.gap_closure is None and not candidate.structurally_independent
    ]
    if not baseline_candidates:
        for candidate in eligible:
            rejected.setdefault(candidate.candidate_id, ("no_eligible_baseline",))
        return ModelSelectionDecision(
            status=CheckStatus.BLOCKED,
            main=None,
            challenger=None,
            assessments=assessments,
            rejected=rejected,
        )

    main = _minimum_sufficient(baseline_candidates)
    challenger_candidates: list[ModelCandidate] = []
    for candidate in eligible:
        if candidate.candidate_id == main.candidate_id:
            continue
        if candidate.gap_closure is not None or candidate.structurally_independent:
            challenger_candidates.append(candidate)
        else:
            rejected[candidate.candidate_id] = ("missing_gap_closure_claim",)

    challenger = (
        _minimum_sufficient(challenger_candidates)
        if challenger_candidates
        else None
    )
    for candidate in challenger_candidates:
        if challenger is not None and candidate.candidate_id != challenger.candidate_id:
            rejected[candidate.candidate_id] = ("challenger_limit_exceeded",)

    return ModelSelectionDecision(
        status=CheckStatus.PASS,
        main=main,
        challenger=challenger,
        assessments=assessments,
        rejected=rejected,
    )


def evaluate_challenger(
    *,
    observed_improvement: float,
    minimum_practical_improvement: float | None,
    stable: bool,
    has_critical_failure: bool,
    uncertainty_overlaps_zero: bool,
) -> PromotionDecision:
    if has_critical_failure:
        return PromotionDecision(False, "critical_validation_failure")
    if not stable:
        return PromotionDecision(False, "improvement_not_stable")
    if minimum_practical_improvement is None:
        return PromotionDecision(
            False, "practical_improvement_threshold_not_frozen"
        )
    if uncertainty_overlaps_zero:
        return PromotionDecision(False, "improvement_within_uncertainty")
    if observed_improvement < minimum_practical_improvement:
        return PromotionDecision(False, "practical_improvement_not_reached")
    return PromotionDecision(True, "validated_practical_improvement")
