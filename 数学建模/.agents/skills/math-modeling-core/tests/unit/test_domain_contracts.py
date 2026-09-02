from __future__ import annotations

import pytest

from mathmodel.contracts import (
    BusinessRuleSpec,
    ConstraintKind,
    DomainContext,
    EvidenceStatus,
    MechanismKind,
    MechanismSpec,
    ProblemSpec,
    VariableRole,
    VariableSpec,
)


def test_variable_requires_explicit_unit_measurement_and_identifiability() -> None:
    variable = VariableSpec(
        name="traffic density",
        symbol="k",
        definition="vehicles per unit road length",
        role=VariableRole.STATE,
        data_type="continuous",
        unit="veh/km",
        measurement="count vehicles in a fixed road segment",
        observable=True,
        data_available=True,
        identifiable=True,
        evidence_claims=("claim-density-definition",),
        evidence_status=EvidenceStatus.VERIFIED,
    )

    assert variable.freeze_eligible is True
    with pytest.raises(ValueError, match="unit must be explicit"):
        VariableSpec(
            name="density",
            symbol="k",
            definition="density",
            role=VariableRole.STATE,
            data_type="continuous",
            unit="",
            measurement="sensor",
            observable=True,
            data_available=True,
            identifiable=True,
        )


def test_unverified_business_rule_cannot_be_frozen_as_hard_constraint() -> None:
    rule = BusinessRuleSpec(
        rule_id="r1",
        text="Maximum operating speed is 80 km/h",
        source_type="paper",
        effective_period="unknown",
        region="region-a",
        organization="operator-a",
        version="unknown",
        constraint_kind=ConstraintKind.HARD,
        formal_constraint="v <= 80",
        evidence_claims=("claim-speed-rule",),
        evidence_status=EvidenceStatus.UNVERIFIED,
    )

    assert rule.hard_constraint_eligible is False


def test_correlation_is_not_promoted_to_physical_law() -> None:
    mechanism = MechanismSpec(
        mechanism_id="m1",
        upstream_variables=("rainfall",),
        downstream_variables=("demand",),
        kind=MechanismKind.CORRELATION,
        direction="positive",
        mathematical_relation="corr(rainfall, demand) > 0",
        conditions=("summer",),
        applicable_scale="daily city level",
        evidence_claims=("claim-correlation",),
        evidence_status=EvidenceStatus.VERIFIED,
    )

    assert mechanism.physical_law_eligible is False


def test_domain_context_preserves_unresolved_ambiguities() -> None:
    context = DomainContext(
        object_name="urban road traffic",
        system_boundary="one arterial corridor",
        stakeholders=("traffic authority", "drivers"),
        temporal_scale="peak hour",
        spatial_scale="corridor",
        terminology={"flow": "vehicles crossing a section per hour"},
        typical_magnitudes={"speed_km_h": (0.0, 80.0)},
        unresolved_ambiguities=("whether incidents are included",),
    )

    assert context.ready_to_freeze is False


def test_problem_spec_refuses_unverified_rule_as_frozen_hard_constraint() -> None:
    rule = BusinessRuleSpec(
        rule_id="r1",
        text="Maximum operating speed is 80 km/h",
        source_type="paper",
        effective_period="unknown",
        region="region-a",
        organization="operator-a",
        version="unknown",
        constraint_kind=ConstraintKind.HARD,
        formal_constraint="v <= 80",
        evidence_claims=("claim-speed-rule",),
        evidence_status=EvidenceStatus.UNVERIFIED,
    )

    with pytest.raises(ValueError, match="hard business rule is not freeze-eligible"):
        ProblemSpec(
            problem_id="p",
            model_family="optimization",
            mandatory_outputs=("decision",),
            business_rules=(rule,),
        )


@pytest.mark.parametrize(
    "second",
    [
        {"name": "traffic density", "symbol": "rho"},
        {"name": "vehicle concentration", "symbol": "k"},
    ],
)
def test_problem_variables_require_unique_names_and_symbols(
    second: dict[str, str],
) -> None:
    def variable(name: str, symbol: str) -> VariableSpec:
        return VariableSpec(
            name=name,
            symbol=symbol,
            definition="a measured traffic state",
            role=VariableRole.STATE,
            data_type="continuous",
            unit="veh/km",
            measurement="verified sensor field",
            observable=True,
            data_available=True,
            identifiable=True,
            evidence_claims=("claim-variable",),
            evidence_status=EvidenceStatus.VERIFIED,
        )

    with pytest.raises(ValueError, match="unique variable names and symbols"):
        ProblemSpec(
            problem_id="p",
            model_family="traffic",
            mandatory_outputs=("state",),
            variables=(
                variable("traffic density", "k"),
                variable(second["name"], second["symbol"]),
            ),
        )
