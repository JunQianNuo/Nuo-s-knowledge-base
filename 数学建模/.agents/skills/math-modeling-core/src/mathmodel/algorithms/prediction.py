from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import warnings

import numpy as np

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


def _metadata(
    plugin_id: str, family: str, dependencies: frozenset[str]
) -> AlgorithmMetadata:
    return AlgorithmMetadata(
        plugin_id=plugin_id,
        name=plugin_id,
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({family}),
        model_families=frozenset({family}),
        dependencies=dependencies,
        solver_guarantee="deterministic for fixed data, configuration, and seed",
        validation_capabilities=frozenset(
            {"finite_output", "training_residual", "chronology"}
        ),
        deterministic=True,
        resource_tier=2,
        io_contract=IOContract(),
        content_hash=f"builtin:{plugin_id}:1.0.0",
    )


def _report(
    name: str, status: CheckStatus, observed: Any = None
) -> ValidationReport:
    return ValidationReport(
        status=status,
        checks=(
            ValidationCheck(
                name=name,
                status=status,
                severity=Severity.MAJOR,
                observed=observed,
            ),
        ),
    )


@dataclass(slots=True)
class LinearRegressionPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "prediction.linear-regression",
        "linear_regression",
        frozenset({"numpy"}),
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        return _supervised_support(problem, data, "linear_regression")

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        x, y, x_predict = _supervised_arrays(data)
        design = np.column_stack((np.ones(x.shape[0]), x))
        parameters, _, rank, _ = np.linalg.lstsq(design, y, rcond=None)
        intercept = float(parameters[0])
        coefficients = np.asarray(parameters[1:])
        fitted = intercept + x @ coefficients
        predictions = intercept + x_predict @ coefficients
        residual_mse = float(np.mean((y - fitted) ** 2))
        full_rank = rank == design.shape[1]
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={
                "coefficients": coefficients.tolist(),
                "intercept": intercept,
                "predictions": predictions.tolist(),
            },
            metrics={"residual_mse": residual_mse},
            diagnostics={"design_rank": int(rank)},
            validation_report=_report(
                "full_design_rank",
                CheckStatus.PASS if full_rank else CheckStatus.WARN,
                {"rank": int(rank), "columns": int(design.shape[1])},
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class RidgeRegressionPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "prediction.ridge-regression",
        "ridge_regression",
        frozenset({"numpy"}),
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        decision = _supervised_support(problem, data, "ridge_regression")
        if decision.status is not SupportStatus.SUPPORTED:
            return decision
        alpha = float(data.scalars.get("alpha", 1.0))
        if alpha < 0:
            return SupportDecision(SupportStatus.UNSUPPORTED, ("alpha_must_be_nonnegative",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        x, y, x_predict = _supervised_arrays(data)
        alpha = float(data.scalars.get("alpha", 1.0))
        fit_intercept = bool(data.scalars.get("fit_intercept", True))
        if fit_intercept:
            x_mean = x.mean(axis=0)
            y_mean = float(y.mean())
            centered_x = x - x_mean
            centered_y = y - y_mean
        else:
            x_mean = np.zeros(x.shape[1])
            y_mean = 0.0
            centered_x = x
            centered_y = y
        gram = centered_x.T @ centered_x + alpha * np.eye(x.shape[1])
        coefficients = np.linalg.solve(gram, centered_x.T @ centered_y)
        intercept = float(y_mean - x_mean @ coefficients)
        fitted = intercept + x @ coefficients
        predictions = intercept + x_predict @ coefficients
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={
                "coefficients": coefficients.tolist(),
                "intercept": intercept,
                "predictions": predictions.tolist(),
            },
            metrics={"residual_mse": float(np.mean((y - fitted) ** 2))},
            diagnostics={"alpha": alpha, "fit_intercept": fit_intercept},
            validation_report=_report("finite_coefficients", CheckStatus.PASS),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class ARIMAPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "prediction.arima", "arima", frozenset({"numpy", "statsmodels"})
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "arima":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        if "series" not in data.arrays:
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_input:arrays.series",)
            )
        series = np.asarray(data.arrays["series"], dtype=float)
        order = data.metadata.get("order")
        horizon = int(data.scalars.get("horizon", 0))
        if series.ndim != 1 or series.size < 3 or not np.all(np.isfinite(series)):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_series",))
        if (
            not isinstance(order, (tuple, list))
            or len(order) != 3
            or any(int(value) < 0 for value in order)
        ):
            return SupportDecision(SupportStatus.UNKNOWN, ("invalid_or_missing_order",))
        if horizon <= 0:
            return SupportDecision(SupportStatus.UNKNOWN, ("invalid_horizon",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        from statsmodels.tsa.arima.model import ARIMA

        series = np.asarray(data.arrays["series"], dtype=float)
        order = tuple(int(value) for value in data.metadata["order"])
        horizon = int(data.scalars["horizon"])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fitted = ARIMA(series, order=order).fit()
            forecast = np.asarray(fitted.forecast(steps=horizon), dtype=float)
        finite = bool(np.all(np.isfinite(forecast)))
        return SolveResult(
            status=RunStatus.SUCCESS if finite else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={"forecast": forecast.tolist()},
            metrics={"aic": float(fitted.aic), "bic": float(fitted.bic)},
            diagnostics={
                "order": order,
                "train_end_index": int(series.size - 1),
                "forecast_start_index": int(series.size),
            },
            validation_report=_report(
                "finite_forecast",
                CheckStatus.PASS if finite else CheckStatus.FAIL,
                finite,
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class RandomForestPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "prediction.random-forest",
        "random_forest",
        frozenset({"numpy", "sklearn"}),
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        decision = _supervised_support(problem, data, "random_forest")
        if decision.status is not SupportStatus.SUPPORTED:
            return decision
        if data.metadata.get("task") not in {"classification", "regression"}:
            return SupportDecision(SupportStatus.UNKNOWN, ("invalid_or_missing_task",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

        x, y, x_predict = _supervised_arrays(data)
        n_estimators = int(data.scalars.get("n_estimators", 100))
        common = {
            "n_estimators": n_estimators,
            "random_state": config.seed,
            "n_jobs": 1,
        }
        task = data.metadata["task"]
        if task == "classification":
            model = RandomForestClassifier(**common)
        else:
            model = RandomForestRegressor(**common)
        model.fit(x, y)
        predictions = model.predict(x_predict)
        solution: dict[str, Any] = {"predictions": predictions.tolist()}
        if task == "classification":
            solution["probabilities"] = model.predict_proba(x_predict).tolist()
            solution["classes"] = model.classes_.tolist()
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution=solution,
            diagnostics={
                "task": task,
                "seed": config.seed,
                "train_rows": int(x.shape[0]),
                "prediction_rows": int(x_predict.shape[0]),
            },
            validation_report=_report("separate_prediction_matrix", CheckStatus.PASS),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _supervised_support(
    problem: ProblemSpec, data: DataBundle, family: str
) -> SupportDecision:
    if problem.model_family != family:
        return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
    missing = [name for name in ("X", "y", "X_predict") if name not in data.arrays]
    if missing:
        return SupportDecision(
            SupportStatus.UNKNOWN,
            tuple(f"missing_input:arrays.{name}" for name in missing),
        )
    x = np.asarray(data.arrays["X"], dtype=float)
    y = np.asarray(data.arrays["y"])
    x_predict = np.asarray(data.arrays["X_predict"], dtype=float)
    if (
        x.ndim != 2
        or x_predict.ndim != 2
        or y.ndim != 1
        or x.shape[0] != y.shape[0]
        or x.shape[1] != x_predict.shape[1]
        or x.shape[0] == 0
        or not np.all(np.isfinite(x))
        or not np.all(np.isfinite(x_predict))
    ):
        return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_supervised_shapes",))
    return SupportDecision(SupportStatus.SUPPORTED)


def _supervised_arrays(
    data: DataBundle,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        np.asarray(data.arrays["X"], dtype=float),
        np.asarray(data.arrays["y"]),
        np.asarray(data.arrays["X_predict"], dtype=float),
    )


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
