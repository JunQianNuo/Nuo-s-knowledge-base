from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp, minimize

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
    IOContract,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)


def _metadata(plugin_id: str, family: str) -> AlgorithmMetadata:
    return AlgorithmMetadata(
        plugin_id=plugin_id,
        name=plugin_id,
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({family}),
        model_families=frozenset({family}),
        dependencies=frozenset({"numpy", "scipy"}),
        solver_guarantee="solver-reported optimum subject to numerical tolerance",
        validation_capabilities=frozenset({"feasibility", "solver_status"}),
        deterministic=True,
        resource_tier=2,
        io_contract=IOContract(),
        content_hash=f"builtin:{plugin_id}:1.0.0",
    )


def _report(name: str, passed: bool, observed: Any = None) -> ValidationReport:
    status = CheckStatus.PASS if passed else CheckStatus.FAIL
    check = ValidationCheck(
        name=name,
        status=status,
        severity=Severity.CRITICAL,
        observed=observed,
        required=True,
    )
    return ValidationReport(status=status, checks=(check,))


@dataclass(slots=True)
class LinearProgrammingPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "optimization.linear-programming", "linear_programming"
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "linear_programming":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        missing = tuple(name for name in ("c",) if name not in data.arrays)
        if missing:
            return SupportDecision(
                SupportStatus.UNKNOWN,
                tuple(f"missing_input:arrays.{name}" for name in missing),
            )
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        result = linprog(
            np.asarray(data.arrays["c"], dtype=float),
            A_ub=_optional_array(data, "A_ub"),
            b_ub=_optional_array(data, "b_ub"),
            A_eq=_optional_array(data, "A_eq"),
            b_eq=_optional_array(data, "b_eq"),
            bounds=data.metadata.get("bounds", (0, None)),
            method="highs",
            options={"time_limit": config.timeout},
        )
        report = _report("solver_success", bool(result.success), result.message)
        return SolveResult(
            status=RunStatus.SUCCESS if result.success else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"x": result.x.tolist() if result.x is not None else []},
            objective=float(result.fun) if result.fun is not None else None,
            diagnostics={"solver_status": int(result.status), "message": result.message},
            validation_report=report,
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class MixedIntegerLinearProgrammingPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "optimization.mixed-integer-linear-programming",
        "mixed_integer_linear_programming",
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "mixed_integer_linear_programming":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        is_knapsack = all(name in data.arrays for name in ("values", "weights")) and (
            "capacity" in data.scalars
        )
        is_standard = "c" in data.arrays and "integrality" in data.arrays
        if not (is_knapsack or is_standard):
            return SupportDecision(
                SupportStatus.UNKNOWN, ("milp_schema_not_recognized",)
            )
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)

        if "values" in data.arrays:
            values = np.asarray(data.arrays["values"], dtype=float)
            weights = np.asarray(data.arrays["weights"], dtype=float)
            c = -values
            integrality = np.ones(values.size, dtype=int)
            bounds = Bounds(np.zeros(values.size), np.ones(values.size))
            constraints = LinearConstraint(
                weights.reshape(1, -1), -np.inf, float(data.scalars["capacity"])
            )
            maximize = True
        else:
            c = np.asarray(data.arrays["c"], dtype=float)
            integrality = np.asarray(data.arrays["integrality"], dtype=int)
            lower = np.asarray(data.arrays.get("lower_bounds", np.full(c.size, -np.inf)))
            upper = np.asarray(data.arrays.get("upper_bounds", np.full(c.size, np.inf)))
            bounds = Bounds(lower, upper)
            matrix = _optional_array(data, "constraints")
            constraints = None
            if matrix is not None:
                constraints = LinearConstraint(
                    matrix,
                    np.asarray(data.arrays.get("constraint_lower", -np.inf)),
                    np.asarray(data.arrays.get("constraint_upper", np.inf)),
                )
            maximize = bool(data.scalars.get("maximize", False))
            if maximize:
                c = -c

        result = milp(
            c,
            integrality=integrality,
            bounds=bounds,
            constraints=constraints,
            options={"time_limit": config.timeout},
        )
        solution = [] if result.x is None else np.rint(result.x).astype(int).tolist()
        objective = None
        if result.fun is not None:
            objective = float(-result.fun if maximize else result.fun)
        report = _report("solver_success", bool(result.success), result.message)
        return SolveResult(
            status=RunStatus.SUCCESS if result.success else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"x": solution},
            objective=objective,
            diagnostics={"solver_status": int(result.status), "message": result.message},
            validation_report=report,
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class NonlinearOptimizationPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "optimization.nonlinear", "nonlinear_optimization"
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "nonlinear_optimization":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        if "x0" not in data.arrays:
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_input:arrays.x0",))
        if not callable(data.metadata.get("objective")):
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_callable:metadata.objective",)
            )
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        result = minimize(
            data.metadata["objective"],
            np.asarray(data.arrays["x0"], dtype=float),
            method=str(data.metadata.get("method", "BFGS")),
            bounds=data.metadata.get("bounds"),
            constraints=data.metadata.get("constraints", ()),
            options={"maxiter": config.max_iterations, "gtol": config.tolerance},
        )
        report = _report("solver_success", bool(result.success), result.message)
        return SolveResult(
            status=RunStatus.SUCCESS if result.success else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"x": result.x.tolist()},
            objective=float(result.fun),
            diagnostics={"iterations": int(result.nit), "message": str(result.message)},
            validation_report=report,
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _optional_array(data: DataBundle, name: str) -> np.ndarray | None:
    value = data.arrays.get(name)
    return None if value is None else np.asarray(value, dtype=float)


def _blocked(plugin_id: str, reasons: tuple[str, ...]) -> SolveResult:
    report = _report("support_precondition", False, reasons)
    return SolveResult(
        status=RunStatus.BLOCKED,
        plugin_id=plugin_id,
        diagnostics={"reasons": reasons},
        validation_report=ValidationReport(
            status=CheckStatus.BLOCKED,
            checks=report.checks,
            rollback_stage="model_selection",
        ),
    )
