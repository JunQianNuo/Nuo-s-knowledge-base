from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mathmodel.algorithms import AlgorithmPlugin, SupportStatus
from mathmodel.contracts import (
    CheckStatus,
    DataBundle,
    ProblemSpec,
    RunStatus,
    SolveConfig,
    SolveResult,
)

from .capabilities import CapabilityPolicy
from .dependencies import DependencyReport, check_dependencies


@dataclass(frozen=True, slots=True)
class ExecutionOutcome:
    exit_code: int
    result: SolveResult | None
    dependencies: DependencyReport
    reasons: tuple[str, ...] = ()


def execute_plugin(
    plugin: AlgorithmPlugin,
    problem: ProblemSpec,
    data: DataBundle,
    config: SolveConfig,
    *,
    additional_dependencies: set[str] | frozenset[str] = frozenset(),
    capability_policy: CapabilityPolicy | None = None,
    requested_reads: tuple[Path, ...] = (),
    requested_writes: tuple[Path, ...] = (),
    requested_network: bool = False,
    requested_subprocesses: tuple[str, ...] = (),
) -> ExecutionOutcome:
    dependencies = check_dependencies(
        plugin.metadata.dependencies | frozenset(additional_dependencies)
    )
    if dependencies.missing:
        return ExecutionOutcome(
            exit_code=3,
            result=None,
            dependencies=dependencies,
            reasons=tuple(
                f"missing_dependency:{name}" for name in dependencies.missing
            ),
        )
    capability_reasons = _capability_reasons(
        plugin,
        capability_policy,
        requested_reads,
        requested_writes,
        requested_network,
        requested_subprocesses,
    )
    if capability_reasons:
        return ExecutionOutcome(3, None, dependencies, capability_reasons)
    config_reasons = plugin.metadata.io_contract.validate_config(config)
    if config_reasons:
        return ExecutionOutcome(3, None, dependencies, config_reasons)
    support = plugin.supports(problem, data)
    if support.status is not SupportStatus.SUPPORTED:
        return ExecutionOutcome(3, None, dependencies, support.reasons)
    result = plugin.solve(problem, data, config)
    output_reasons = plugin.metadata.io_contract.validate_output(result)
    validation_status = (
        result.validation_report.status if result.validation_report else None
    )
    if result.status is RunStatus.BLOCKED or validation_status in {
        CheckStatus.BLOCKED,
        CheckStatus.SKIPPED,
    }:
        exit_code = 3
    elif (
        result.status is RunStatus.FAIL
        or validation_status is CheckStatus.FAIL
        or output_reasons
    ):
        exit_code = 4
    else:
        exit_code = 0
    return ExecutionOutcome(exit_code, result, dependencies, output_reasons)


def _capability_reasons(
    plugin: AlgorithmPlugin,
    policy: CapabilityPolicy | None,
    reads: tuple[Path, ...],
    writes: tuple[Path, ...],
    network: bool,
    subprocesses: tuple[str, ...],
) -> tuple[str, ...]:
    if not (reads or writes or network or subprocesses):
        return ()
    if policy is None:
        return ("capability_policy_missing",)
    permissions = plugin.metadata.permissions
    reasons: list[str] = []
    if reads and "declared_inputs" not in permissions.filesystem_read:
        reasons.append("filesystem_read_not_declared")
    else:
        reasons.extend(
            decision.reason
            for decision in (policy.check_read(path) for path in reads)
            if decision.status is CheckStatus.BLOCKED and decision.reason
        )
    if writes and "run_artifacts" not in permissions.filesystem_write:
        reasons.append("filesystem_write_not_declared")
    else:
        reasons.extend(
            decision.reason
            for decision in (policy.check_write(path) for path in writes)
            if decision.status is CheckStatus.BLOCKED and decision.reason
        )
    if network:
        decision = policy.check_network(permissions)
        if decision.status is CheckStatus.BLOCKED and decision.reason:
            reasons.append(decision.reason)
    for executable in subprocesses:
        decision = policy.check_subprocess(permissions, executable)
        if decision.status is CheckStatus.BLOCKED and decision.reason:
            reasons.append(decision.reason)
    return tuple(dict.fromkeys(reasons))
