from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Mapping


class EvidenceStatus(StrEnum):
    VERIFIED = "VERIFIED"
    PARTIAL = "PARTIAL"
    UNVERIFIED = "UNVERIFIED"


class VariableRole(StrEnum):
    INPUT = "input"
    STATE = "state"
    DECISION = "decision"
    OUTPUT = "output"
    LATENT = "latent"
    CONFOUNDER = "confounder"


class MechanismKind(StrEnum):
    CORRELATION = "correlation"
    EMPIRICAL = "empirical"
    CAUSAL = "causal"
    PHYSICAL_LAW = "physical_law"
    BUSINESS_CONSTRAINT = "business_constraint"


class ConstraintKind(StrEnum):
    HARD = "hard"
    SOFT = "soft"


@dataclass(frozen=True, slots=True)
class DomainContext:
    object_name: str
    system_boundary: str
    stakeholders: tuple[str, ...]
    temporal_scale: str
    spatial_scale: str
    terminology: Mapping[str, str] = field(default_factory=dict)
    typical_magnitudes: Mapping[str, tuple[float, float]] = field(default_factory=dict)
    unresolved_ambiguities: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "object_name",
            "system_boundary",
            "temporal_scale",
            "spatial_scale",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        object.__setattr__(self, "stakeholders", tuple(self.stakeholders))
        object.__setattr__(self, "terminology", dict(self.terminology))
        object.__setattr__(self, "typical_magnitudes", dict(self.typical_magnitudes))
        object.__setattr__(
            self, "unresolved_ambiguities", tuple(self.unresolved_ambiguities)
        )
        for name, bounds in self.typical_magnitudes.items():
            if len(bounds) != 2 or bounds[0] > bounds[1]:
                raise ValueError(f"invalid typical magnitude bounds for {name}")

    @property
    def ready_to_freeze(self) -> bool:
        return not self.unresolved_ambiguities


@dataclass(frozen=True, slots=True)
class VariableSpec:
    name: str
    symbol: str
    definition: str
    role: VariableRole
    data_type: str
    unit: str
    measurement: str
    observable: bool
    data_available: bool
    identifiable: bool
    reasonable_range: tuple[float, float] | None = None
    evidence_claims: tuple[str, ...] = ()
    evidence_status: EvidenceStatus = EvidenceStatus.UNVERIFIED

    def __post_init__(self) -> None:
        for name in ("name", "symbol", "definition", "data_type", "measurement"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        if not self.unit.strip():
            raise ValueError("unit must be explicit; use '1' for dimensionless")
        if self.reasonable_range is not None and (
            len(self.reasonable_range) != 2
            or self.reasonable_range[0] > self.reasonable_range[1]
        ):
            raise ValueError("reasonable_range must be ordered")
        object.__setattr__(self, "evidence_claims", tuple(self.evidence_claims))

    @property
    def freeze_eligible(self) -> bool:
        evidence_ready = bool(self.evidence_claims) and (
            self.evidence_status is not EvidenceStatus.UNVERIFIED
        )
        if self.role is VariableRole.LATENT:
            return self.identifiable and evidence_ready
        return (
            self.observable
            and self.data_available
            and self.identifiable
            and evidence_ready
        )


@dataclass(frozen=True, slots=True)
class MechanismSpec:
    mechanism_id: str
    upstream_variables: tuple[str, ...]
    downstream_variables: tuple[str, ...]
    kind: MechanismKind
    direction: str
    mathematical_relation: str
    conditions: tuple[str, ...]
    applicable_scale: str
    evidence_claims: tuple[str, ...]
    evidence_status: EvidenceStatus

    def __post_init__(self) -> None:
        for name in (
            "mechanism_id",
            "direction",
            "mathematical_relation",
            "applicable_scale",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        for name in (
            "upstream_variables",
            "downstream_variables",
            "conditions",
            "evidence_claims",
        ):
            object.__setattr__(self, name, tuple(getattr(self, name)))
        if not self.upstream_variables or not self.downstream_variables:
            raise ValueError("mechanism must have upstream and downstream variables")

    @property
    def physical_law_eligible(self) -> bool:
        return (
            self.kind is MechanismKind.PHYSICAL_LAW
            and self.evidence_status is EvidenceStatus.VERIFIED
            and bool(self.conditions)
            and bool(self.evidence_claims)
        )


@dataclass(frozen=True, slots=True)
class BusinessRuleSpec:
    rule_id: str
    text: str
    source_type: str
    effective_period: str
    region: str
    organization: str
    version: str
    constraint_kind: ConstraintKind
    formal_constraint: str
    evidence_claims: tuple[str, ...]
    evidence_status: EvidenceStatus
    conflict_status: str = "none"

    def __post_init__(self) -> None:
        for name in (
            "rule_id",
            "text",
            "source_type",
            "effective_period",
            "region",
            "organization",
            "version",
            "formal_constraint",
            "conflict_status",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        object.__setattr__(self, "evidence_claims", tuple(self.evidence_claims))

    @property
    def hard_constraint_eligible(self) -> bool:
        applicability_known = all(
            value.casefold() not in {"unknown", "unspecified"}
            for value in (
                self.effective_period,
                self.region,
                self.organization,
                self.version,
            )
        )
        return (
            self.constraint_kind is ConstraintKind.HARD
            and self.evidence_status is EvidenceStatus.VERIFIED
            and bool(self.evidence_claims)
            and applicability_known
            and self.conflict_status == "none"
        )
