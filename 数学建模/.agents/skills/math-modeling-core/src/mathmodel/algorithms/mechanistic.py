from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp

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

from .base import (
    AlgorithmMetadata,
    FieldSpec,
    IOContract,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)


@dataclass(slots=True)
class ODESolverPlugin:
    metadata: AlgorithmMetadata = AlgorithmMetadata(
        plugin_id="mechanistic.solve-ivp",
        name="mechanistic.solve-ivp",
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({"ode"}),
        model_families=frozenset({"ode"}),
        dependencies=frozenset({"numpy", "scipy"}),
        solver_guarantee="adaptive numerical integration with declared tolerances",
        validation_capabilities=frozenset({"solver_status", "monotone_time"}),
        deterministic=True,
        resource_tier=2,
        io_contract=IOContract(
            input_fields=(
                FieldSpec("arrays", "y0", "state_vector"),
                FieldSpec("arrays", "t_eval", "increasing_vector"),
                FieldSpec("metadata", "rhs", "callable"),
            ),
            output_fields=(
                FieldSpec("solution", "time", "increasing_vector"),
                FieldSpec("solution", "state", "trajectory_matrix"),
            ),
            config_fields=(FieldSpec("config", "tolerance", "positive_number"),),
        ),
        content_hash="builtin:mechanistic.solve-ivp:1.0.0",
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "ode":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        missing = [name for name in ("y0", "t_eval") if name not in data.arrays]
        if missing:
            return SupportDecision(
                SupportStatus.UNKNOWN,
                tuple(f"missing_input:arrays.{name}" for name in missing),
            )
        if "t0" not in data.scalars or "t1" not in data.scalars:
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_time_span",))
        if not callable(data.metadata.get("rhs")):
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_callable:metadata.rhs",))
        y0 = np.asarray(data.arrays["y0"], dtype=float)
        times = np.asarray(data.arrays["t_eval"], dtype=float)
        t0, t1 = float(data.scalars["t0"]), float(data.scalars["t1"])
        if y0.ndim != 1 or y0.size == 0 or not np.all(np.isfinite(y0)):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_initial_state",))
        if (
            times.ndim != 1
            or times.size == 0
            or not np.all(np.diff(times) > 0)
            or times[0] < t0
            or times[-1] > t1
            or t1 <= t0
        ):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_time_grid",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        result = solve_ivp(
            data.metadata["rhs"],
            (float(data.scalars["t0"]), float(data.scalars["t1"])),
            np.asarray(data.arrays["y0"], dtype=float),
            t_eval=np.asarray(data.arrays["t_eval"], dtype=float),
            rtol=config.tolerance,
            atol=config.tolerance,
            method=str(data.metadata.get("method", "RK45")),
        )
        monotone = bool(result.t.size and np.all(np.diff(result.t) > 0))
        passed = bool(result.success and monotone and np.all(np.isfinite(result.y)))
        status = CheckStatus.PASS if passed else CheckStatus.FAIL
        check = ValidationCheck(
            name="successful_monotone_trajectory",
            status=status,
            severity=Severity.CRITICAL,
            observed={"success": bool(result.success), "monotone_time": monotone},
        )
        return SolveResult(
            status=RunStatus.SUCCESS if passed else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"time": result.t.tolist(), "state": result.y.tolist()},
            diagnostics={
                "message": result.message,
                "function_evaluations": int(result.nfev),
            },
            validation_report=ValidationReport(status=status, checks=(check,)),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _blocked(plugin_id: str, reasons: tuple[str, ...]) -> SolveResult:
    check = ValidationCheck(
        name="support_precondition",
        status=CheckStatus.BLOCKED,
        severity=Severity.CRITICAL,
        observed=reasons,
        rollback_stage="model_selection",
    )
    return SolveResult(
        status=RunStatus.BLOCKED,
        plugin_id=plugin_id,
        diagnostics={"reasons": reasons},
        validation_report=ValidationReport(
            status=CheckStatus.BLOCKED,
            checks=(check,),
            rollback_stage="model_selection",
        ),
    )
