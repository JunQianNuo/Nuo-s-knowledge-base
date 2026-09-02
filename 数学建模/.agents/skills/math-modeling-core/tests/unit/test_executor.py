from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mathmodel.algorithms import (
    AlgorithmMetadata,
    FieldSpec,
    IOContract,
    PermissionSpec,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)
from mathmodel.contracts import (
    CheckStatus,
    DataBundle,
    ProblemSpec,
    RunStatus,
    Severity,
    SolveConfig,
    SolveResult,
    ValidationCheck,
    ValidationReport,
)
from mathmodel.runtime import CapabilityPolicy, execute_plugin


@dataclass
class RuntimePlugin:
    metadata: AlgorithmMetadata
    solve_calls: int = 0

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        self.solve_calls += 1
        critical_fail = ValidationCheck(
            name="critical",
            status=CheckStatus.FAIL,
            severity=Severity.CRITICAL,
        )
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            validation_report=ValidationReport(
                status=CheckStatus.FAIL, checks=(critical_fail,)
            ),
        )

    def validate_result(self, result: SolveResult):
        return result.validation_report.checks if result.validation_report else ()


def metadata() -> AlgorithmMetadata:
    return AlgorithmMetadata(
        plugin_id="test.runtime",
        name="test.runtime",
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({"test"}),
        model_families=frozenset({"test"}),
        dependencies=frozenset(),
        solver_guarantee="test",
        validation_capabilities=frozenset({"critical"}),
        deterministic=True,
        resource_tier=0,
        permissions=PermissionSpec(),
        io_contract=IOContract(
            input_fields=(FieldSpec("arrays", "x", "vector"),),
            output_fields=(FieldSpec("solution", "x", "vector"),),
            config_fields=(FieldSpec("config", "seed", "integer"),),
        ),
        content_hash="test-runtime",
    )


def problem() -> ProblemSpec:
    return ProblemSpec(
        problem_id="p",
        model_family="test",
        mandatory_outputs=("x",),
        required_capabilities={"test"},
    )


def test_critical_validation_fail_maps_to_exit_four() -> None:
    outcome = execute_plugin(
        RuntimePlugin(metadata()),
        problem(),
        DataBundle(arrays={"x": [1]}),
        SolveConfig(),
    )

    assert outcome.result is not None
    assert outcome.result.status is RunStatus.SUCCESS
    assert outcome.exit_code == 4


def test_capability_preflight_blocks_outside_write_before_solve(tmp_path: Path) -> None:
    project_root = tmp_path / "project"
    run_root = project_root / "results" / "run"
    run_root.mkdir(parents=True)
    plugin = RuntimePlugin(metadata())
    policy = CapabilityPolicy(
        skill_root=tmp_path / "skill",
        project_root=project_root,
        run_root=run_root,
    )

    outcome = execute_plugin(
        plugin,
        problem(),
        DataBundle(arrays={"x": [1]}),
        SolveConfig(),
        capability_policy=policy,
        requested_writes=(project_root / "outside.json",),
    )

    assert outcome.exit_code == 3
    assert outcome.reasons == ("write_outside_run_root",)
    assert plugin.solve_calls == 0
