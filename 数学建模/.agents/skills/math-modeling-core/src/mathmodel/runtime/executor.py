from __future__ import annotations

from dataclasses import dataclass

from mathmodel.algorithms import AlgorithmPlugin, SupportStatus
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig, SolveResult

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
    support = plugin.supports(problem, data)
    if support.status is not SupportStatus.SUPPORTED:
        return ExecutionOutcome(3, None, dependencies, support.reasons)
    result = plugin.solve(problem, data, config)
    if result.status is RunStatus.BLOCKED:
        exit_code = 3
    elif result.status is RunStatus.FAIL:
        exit_code = 4
    else:
        exit_code = 0
    return ExecutionOutcome(exit_code, result, dependencies)
