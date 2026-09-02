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
    FieldSpec,
    IOContract,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)


def _metadata(plugin_id: str, family: str) -> AlgorithmMetadata:
    input_fields = {
        "linear_programming": (FieldSpec("arrays", "c", "vector"),),
        "mixed_integer_linear_programming": (
            FieldSpec("arrays", "c", "vector", required=False),
            FieldSpec("arrays", "values", "vector", required=False),
        ),
        "nonlinear_optimization": (
            FieldSpec("arrays", "x0", "vector"),
            FieldSpec("metadata", "objective", "callable"),
        ),
    }[family]
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
        io_contract=IOContract(
            input_fields=input_fields,
            output_fields=(FieldSpec("solution", "x", "vector"),),
            config_fields=(
                FieldSpec("config", "timeout", "positive_number"),
                FieldSpec("config", "tolerance", "positive_number"),
            ),
        ),
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
        if result.x is None:
            solution: list[float] = []
        else:
            solution_array = np.asarray(result.x, dtype=float).copy()
            integer_mask = integrality != 0
            solution_array[integer_mask] = np.rint(solution_array[integer_mask])
            solution = solution_array.tolist()
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
        constraints = data.metadata.get("constraints", ())
        bounds = data.metadata.get("bounds")
        declared_method = data.metadata.get("method")
        if declared_method is None:
            if constraints:
                method = "SLSQP"
            elif bounds is not None:
                method = "L-BFGS-B"
            else:
                method = "BFGS"
        else:
            method = str(declared_method)
        options: dict[str, Any] = {"maxiter": config.max_iterations}
        if method.upper() == "SLSQP":
            options["ftol"] = config.tolerance
        else:
            options["gtol"] = config.tolerance
        result = minimize(
            data.metadata["objective"],
            np.asarray(data.arrays["x0"], dtype=float),
            method=method,
            bounds=bounds,
            constraints=constraints,
            options=options,
        )
        violation = max(
            _constraint_violation(constraints, np.asarray(result.x, dtype=float)),
            _bounds_violation(bounds, np.asarray(result.x, dtype=float)),
        )
        feasible = violation <= max(config.tolerance * 10, 1e-7)
        passed = bool(result.success and feasible)
        report = _report(
            "solver_success_and_feasibility",
            passed,
            {
                "message": str(result.message),
                "max_constraint_violation": violation,
            },
        )
        return SolveResult(
            status=RunStatus.SUCCESS if passed else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"x": result.x.tolist()},
            objective=float(result.fun),
            diagnostics={
                "iterations": int(result.nit),
                "message": str(result.message),
                "method": method,
                "max_constraint_violation": violation,
            },
            validation_report=report,
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _optional_array(data: DataBundle, name: str) -> np.ndarray | None:
    value = data.arrays.get(name)
    return None if value is None else np.asarray(value, dtype=float)


def _constraint_violation(constraints: Any, x: np.ndarray) -> float:
    if constraints is None:
        return 0.0
    if isinstance(constraints, (tuple, list)) and not constraints:
        return 0.0
    items = constraints if isinstance(constraints, (tuple, list)) else (constraints,)
    maximum = 0.0
    for constraint in items:
        if isinstance(constraint, dict):
            observed = np.asarray(constraint["fun"](x), dtype=float)
            if constraint.get("type") == "eq":
                maximum = max(maximum, float(np.max(np.abs(observed))))
            else:
                maximum = max(maximum, float(np.max(np.maximum(-observed, 0.0))))
            continue
        if isinstance(constraint, LinearConstraint):
            observed = np.asarray(constraint.A @ x, dtype=float)
        elif hasattr(constraint, "fun"):
            observed = np.asarray(constraint.fun(x), dtype=float)
        else:
            continue
        lower = np.broadcast_to(np.asarray(constraint.lb, dtype=float), observed.shape)
        upper = np.broadcast_to(np.asarray(constraint.ub, dtype=float), observed.shape)
        maximum = max(
            maximum,
            float(np.max(np.maximum(lower - observed, 0.0))),
            float(np.max(np.maximum(observed - upper, 0.0))),
        )
    return maximum


def _bounds_violation(bounds: Any, x: np.ndarray) -> float:
    if bounds is None:
        return 0.0
    if isinstance(bounds, Bounds):
        lower = np.broadcast_to(np.asarray(bounds.lb, dtype=float), x.shape)
        upper = np.broadcast_to(np.asarray(bounds.ub, dtype=float), x.shape)
    else:
        normalized = list(bounds)
        lower = np.asarray(
            [-np.inf if item[0] is None else item[0] for item in normalized],
            dtype=float,
        )
        upper = np.asarray(
            [np.inf if item[1] is None else item[1] for item in normalized],
            dtype=float,
        )
    return max(
        float(np.max(np.maximum(lower - x, 0.0))),
        float(np.max(np.maximum(x - upper, 0.0))),
    )


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
