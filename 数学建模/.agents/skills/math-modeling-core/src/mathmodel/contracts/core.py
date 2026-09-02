from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Mapping

from .domain import (
    BusinessRuleSpec,
    ConstraintKind,
    DomainContext,
    MechanismKind,
    MechanismSpec,
    VariableSpec,
)


class CheckStatus(StrEnum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"
    SKIPPED = "SKIPPED"


class Severity(StrEnum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"


class RunStatus(StrEnum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True, slots=True)
class ProblemSpec:
    problem_id: str
    model_family: str
    mandatory_outputs: tuple[str, ...]
    required_capabilities: frozenset[str] = frozenset()
    assumptions: Mapping[str, Any] = field(default_factory=dict)
    preference_weights: Mapping[str, float] = field(default_factory=dict)
    minimum_practical_improvement: float | None = None
    domain_context: DomainContext | None = None
    variables: tuple[VariableSpec, ...] = ()
    mechanisms: tuple[MechanismSpec, ...] = ()
    business_rules: tuple[BusinessRuleSpec, ...] = ()

    def __post_init__(self) -> None:
        if not self.problem_id.strip():
            raise ValueError("problem_id must not be empty")
        if not self.model_family.strip():
            raise ValueError("model_family must not be empty")
        outputs = tuple(self.mandatory_outputs)
        if not outputs:
            raise ValueError("mandatory_outputs must not be empty")
        object.__setattr__(self, "mandatory_outputs", outputs)
        object.__setattr__(
            self, "required_capabilities", frozenset(self.required_capabilities)
        )
        object.__setattr__(self, "assumptions", dict(self.assumptions))
        object.__setattr__(self, "preference_weights", dict(self.preference_weights))
        object.__setattr__(self, "variables", tuple(self.variables))
        object.__setattr__(self, "mechanisms", tuple(self.mechanisms))
        object.__setattr__(self, "business_rules", tuple(self.business_rules))
        variable_names = [item.name.casefold() for item in self.variables]
        variable_symbols = [item.symbol.casefold() for item in self.variables]
        if len(variable_names) != len(set(variable_names)) or len(
            variable_symbols
        ) != len(set(variable_symbols)):
            raise ValueError("problem variables require unique variable names and symbols")
        ineligible_variables = [item.name for item in self.variables if not item.freeze_eligible]
        if ineligible_variables:
            raise ValueError(
                "variable is not freeze-eligible: " + ",".join(ineligible_variables)
            )
        invalid_laws = [
            item.mechanism_id
            for item in self.mechanisms
            if item.kind is MechanismKind.PHYSICAL_LAW
            and not item.physical_law_eligible
        ]
        if invalid_laws:
            raise ValueError(
                "physical law is not freeze-eligible: " + ",".join(invalid_laws)
            )
        invalid_hard_rules = [
            item.rule_id
            for item in self.business_rules
            if item.constraint_kind is ConstraintKind.HARD
            and not item.hard_constraint_eligible
        ]
        if invalid_hard_rules:
            raise ValueError(
                "hard business rule is not freeze-eligible: "
                + ",".join(invalid_hard_rules)
            )


@dataclass(frozen=True, slots=True)
class ModelRequirements:
    mandatory_capabilities: frozenset[str]
    mandatory_outputs: frozenset[str] = frozenset()
    structural_features: frozenset[str] = frozenset()
    hard_constraints: tuple[str, ...] = ()
    available_fields: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        capabilities = frozenset(self.mandatory_capabilities)
        if not capabilities:
            raise ValueError("mandatory_capabilities must not be empty")
        object.__setattr__(self, "mandatory_capabilities", capabilities)
        object.__setattr__(self, "mandatory_outputs", frozenset(self.mandatory_outputs))
        object.__setattr__(self, "structural_features", frozenset(self.structural_features))
        object.__setattr__(self, "hard_constraints", tuple(self.hard_constraints))
        object.__setattr__(self, "available_fields", frozenset(self.available_fields))


@dataclass(frozen=True, slots=True)
class ComplexityProfile:
    additional_data_fields: int = 0
    latent_parameters: int = 0
    unverified_critical_assumptions: int = 0
    model_dimension_tier: int = 0
    time_tier: int = 0
    memory_tier: int = 0

    def __post_init__(self) -> None:
        values = (
            self.additional_data_fields,
            self.latent_parameters,
            self.unverified_critical_assumptions,
            self.model_dimension_tier,
            self.time_tier,
            self.memory_tier,
        )
        if any(value < 0 for value in values):
            raise ValueError("complexity counts and tiers must be nonnegative")

    def sort_key(self) -> tuple[int, ...]:
        return (
            self.unverified_critical_assumptions,
            self.additional_data_fields,
            self.latent_parameters,
            self.time_tier,
            self.memory_tier,
            self.model_dimension_tier,
        )


@dataclass(frozen=True, slots=True)
class GapClosureClaim:
    baseline_model: str
    addresses_gap: str
    expected_gain: str
    validation_test: str
    minimum_practical_improvement: float | None = None
    added_variables: tuple[str, ...] = ()
    added_assumptions: tuple[str, ...] = ()
    added_data: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "baseline_model",
            "addresses_gap",
            "expected_gain",
            "validation_test",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must not be empty")
        object.__setattr__(self, "added_variables", tuple(self.added_variables))
        object.__setattr__(self, "added_assumptions", tuple(self.added_assumptions))
        object.__setattr__(self, "added_data", tuple(self.added_data))


@dataclass(frozen=True, slots=True)
class ModelCandidate:
    candidate_id: str
    model_family: str
    capabilities: frozenset[str] = frozenset()
    covered_outputs: frozenset[str] = frozenset()
    structural_features: frozenset[str] = frozenset()
    required_data: frozenset[str] = frozenset()
    constraints_supported: bool | None = True
    assumptions_verified: bool | None = True
    identifiable: bool | None = True
    validation_path: bool | None = True
    complexity: ComplexityProfile = field(default_factory=ComplexityProfile)
    gap_closure: GapClosureClaim | None = None
    structurally_independent: bool = False
    evidence_count: int = 0

    def __post_init__(self) -> None:
        if not self.candidate_id.strip():
            raise ValueError("candidate_id must not be empty")
        if not self.model_family.strip():
            raise ValueError("model_family must not be empty")
        for name in (
            "capabilities",
            "covered_outputs",
            "structural_features",
            "required_data",
        ):
            object.__setattr__(self, name, frozenset(getattr(self, name)))
        if self.evidence_count < 0:
            raise ValueError("evidence_count must be nonnegative")


@dataclass(frozen=True, slots=True)
class DataBundle:
    arrays: Mapping[str, Any] = field(default_factory=dict)
    scalars: Mapping[str, Any] = field(default_factory=dict)
    tables: Mapping[str, Any] = field(default_factory=dict)
    targets: Mapping[str, Any] = field(default_factory=dict)
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name in ("arrays", "scalars", "tables", "targets", "metadata"):
            object.__setattr__(self, name, dict(getattr(self, name)))


@dataclass(frozen=True, slots=True)
class SolveConfig:
    seed: int = 42
    timeout: float = 60.0
    tolerance: float = 1e-8
    max_iterations: int = 10_000
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.timeout <= 0:
            raise ValueError("timeout must be positive")
        if self.tolerance <= 0:
            raise ValueError("tolerance must be positive")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be positive")
        object.__setattr__(self, "parameters", dict(self.parameters))


@dataclass(frozen=True, slots=True)
class ValidationCheck:
    name: str
    status: CheckStatus
    severity: Severity
    observed: Any = None
    threshold: Any = None
    evidence: tuple[str, ...] = ()
    required: bool = True
    rollback_stage: str | None = None

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("validation check name must not be empty")
        object.__setattr__(self, "evidence", tuple(self.evidence))


@dataclass(frozen=True, slots=True)
class ValidationReport:
    status: CheckStatus
    checks: tuple[ValidationCheck, ...]
    accepted_risk: str | None = None
    rollback_stage: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "checks", tuple(self.checks))


@dataclass(frozen=True, slots=True)
class SolveResult:
    status: RunStatus
    plugin_id: str
    solution: Mapping[str, Any] = field(default_factory=dict)
    objective: float | None = None
    metrics: Mapping[str, float] = field(default_factory=dict)
    diagnostics: Mapping[str, Any] = field(default_factory=dict)
    artifacts: tuple[str, ...] = ()
    validation_report: ValidationReport | None = None

    def __post_init__(self) -> None:
        if not self.plugin_id.strip():
            raise ValueError("plugin_id must not be empty")
        object.__setattr__(self, "solution", dict(self.solution))
        object.__setattr__(self, "metrics", dict(self.metrics))
        object.__setattr__(self, "diagnostics", dict(self.diagnostics))
        object.__setattr__(self, "artifacts", tuple(self.artifacts))
