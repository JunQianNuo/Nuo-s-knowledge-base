from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pytest

from mathmodel.algorithms import (
    AlgorithmMetadata,
    AlgorithmRegistry,
    FieldSpec,
    IOContract,
    PermissionSpec,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig, SolveResult


@dataclass
class DummyPlugin:
    metadata: AlgorithmMetadata
    support: SupportDecision = SupportDecision(SupportStatus.SUPPORTED)

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        return self.support

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"value": 1},
        )

    def validate_result(self, result: SolveResult):
        return ()


def metadata(
    plugin_id: str,
    *,
    status: PluginStatus = PluginStatus.STABLE,
    required_field: str = "x",
) -> AlgorithmMetadata:
    return AlgorithmMetadata(
        plugin_id=plugin_id,
        name=plugin_id,
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=status,
        capabilities=frozenset({"regression"}),
        model_families=frozenset({"regression"}),
        dependencies=frozenset({"numpy"}),
        solver_guarantee="deterministic",
        validation_capabilities=frozenset({"oracle"}),
        deterministic=True,
        resource_tier=1,
        permissions=PermissionSpec(),
        io_contract=IOContract(
            input_fields=(FieldSpec("arrays", required_field, "ndarray"),),
            output_fields=(FieldSpec("solution", "value", "number"),),
        ),
        content_hash=f"hash-{plugin_id}",
    )


def problem() -> ProblemSpec:
    return ProblemSpec(
        problem_id="p",
        model_family="regression",
        mandatory_outputs=("prediction",),
        required_capabilities={"regression"},
    )


def test_registry_rejects_duplicate_plugin_id_and_version() -> None:
    registry = AlgorithmRegistry()
    registry.register(DummyPlugin(metadata("stats.linear-regression")))

    with pytest.raises(ValueError, match="duplicate plugin"):
        registry.register(DummyPlugin(metadata("stats.linear-regression")))


def test_registry_excludes_unknown_support() -> None:
    plugin = DummyPlugin(
        metadata("stats.unknown"),
        SupportDecision(SupportStatus.UNKNOWN, ("scale_not_declared",)),
    )
    registry = AlgorithmRegistry([plugin])

    decision = registry.match(
        problem(),
        DataBundle(arrays={"x": np.ones((2, 1))}),
        installed_dependencies={"numpy"},
    )

    assert decision.matches == ()
    assert decision.rejected["stats.unknown"] == ("scale_not_declared",)


def test_registry_rejects_missing_input_field_before_solve() -> None:
    registry = AlgorithmRegistry([DummyPlugin(metadata("stats.linear-regression"))])

    decision = registry.match(
        problem(), DataBundle(), installed_dependencies={"numpy"}
    )

    assert decision.matches == ()
    assert decision.rejected["stats.linear-regression"] == (
        "missing_input:arrays.x",
    )


def test_registry_orders_stable_before_experimental() -> None:
    registry = AlgorithmRegistry(
        [
            DummyPlugin(metadata("stats.experimental", status=PluginStatus.EXPERIMENTAL)),
            DummyPlugin(metadata("stats.stable", status=PluginStatus.STABLE)),
        ]
    )

    decision = registry.match(
        problem(),
        DataBundle(arrays={"x": np.ones((2, 1))}),
        installed_dependencies={"numpy"},
        allow_experimental=True,
    )

    assert tuple(plugin.metadata.plugin_id for plugin in decision.matches) == (
        "stats.stable",
        "stats.experimental",
    )


def test_registry_blocks_missing_dependency_without_substitution() -> None:
    registry = AlgorithmRegistry([DummyPlugin(metadata("stats.linear-regression"))])

    decision = registry.match(
        problem(),
        DataBundle(arrays={"x": np.ones((2, 1))}),
        installed_dependencies=set(),
    )

    assert decision.matches == ()
    assert decision.rejected["stats.linear-regression"] == (
        "missing_dependencies:numpy",
    )
