from __future__ import annotations

from dataclasses import dataclass
from typing import Any

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
        dependencies=frozenset({"numpy"}),
        solver_guarantee="deterministic evaluation transform",
        validation_capabilities=frozenset(
            {"normalization", "direction", "consistency"}
        ),
        deterministic=True,
        resource_tier=1,
        io_contract=IOContract(),
        content_hash=f"builtin:{plugin_id}:1.0.0",
    )


def _report(
    name: str,
    status: CheckStatus,
    observed: Any = None,
    threshold: Any = None,
) -> ValidationReport:
    return ValidationReport(
        status=status,
        checks=(
            ValidationCheck(
                name=name,
                status=status,
                severity=Severity.MAJOR,
                observed=observed,
                threshold=threshold,
            ),
        ),
    )


@dataclass(slots=True)
class AHPPlugin:
    metadata: AlgorithmMetadata = _metadata("evaluation.ahp", "ahp")

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "ahp":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        if "pairwise" not in data.arrays:
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_input:arrays.pairwise",)
            )
        matrix = np.asarray(data.arrays["pairwise"], dtype=float)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            return SupportDecision(
                SupportStatus.UNSUPPORTED, ("pairwise_matrix_must_be_square",)
            )
        if matrix.shape[0] == 0 or np.any(matrix <= 0):
            return SupportDecision(
                SupportStatus.UNSUPPORTED, ("pairwise_entries_must_be_positive",)
            )
        if not np.allclose(matrix * matrix.T, 1.0, rtol=1e-7, atol=1e-9):
            return SupportDecision(
                SupportStatus.UNSUPPORTED, ("pairwise_matrix_not_reciprocal",)
            )
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        matrix = np.asarray(data.arrays["pairwise"], dtype=float)
        geometric_means = np.exp(np.mean(np.log(matrix), axis=1))
        weights = geometric_means / geometric_means.sum()
        n = matrix.shape[0]
        lambda_max = float(np.max(np.linalg.eigvals(matrix).real))
        consistency_index = 0.0 if n <= 1 else max(0.0, (lambda_max - n) / (n - 1))
        random_index = {
            1: 0.0,
            2: 0.0,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49,
        }.get(n, 1.49)
        consistency_ratio = (
            0.0 if random_index == 0 else consistency_index / random_index
        )
        status = CheckStatus.PASS if consistency_ratio <= 0.1 else CheckStatus.WARN
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"weights": weights.tolist()},
            metrics={
                "lambda_max": lambda_max,
                "consistency_index": consistency_index,
                "consistency_ratio": consistency_ratio,
            },
            validation_report=_report(
                "ahp_consistency_ratio", status, consistency_ratio, 0.1
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class EntropyWeightPlugin:
    metadata: AlgorithmMetadata = _metadata(
        "evaluation.entropy-weight", "entropy_weight"
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        return _matrix_support(problem, data, "entropy_weight")

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        matrix = np.asarray(data.arrays["decision_matrix"], dtype=float)
        ranges = np.ptp(matrix, axis=0)
        varying = ranges > 0
        normalized = np.zeros_like(matrix, dtype=float)
        normalized[:, varying] = (
            matrix[:, varying] - np.min(matrix[:, varying], axis=0)
        ) / ranges[varying]
        column_sums = normalized.sum(axis=0)
        proportions = np.zeros_like(normalized)
        nonzero = column_sums > 0
        proportions[:, nonzero] = normalized[:, nonzero] / column_sums[nonzero]
        logs = np.zeros_like(proportions)
        positive = proportions > 0
        logs[positive] = np.log(proportions[positive])
        entropy = -np.sum(proportions * logs, axis=0) / np.log(matrix.shape[0])
        divergence = np.where(varying, 1.0 - entropy, 0.0)
        if float(divergence.sum()) <= config.tolerance:
            weights = np.full(matrix.shape[1], 1.0 / matrix.shape[1])
            status = CheckStatus.WARN
        else:
            weights = divergence / divergence.sum()
            status = CheckStatus.PASS
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"weights": weights.tolist(), "entropy": entropy.tolist()},
            diagnostics={"constant_columns": np.flatnonzero(~varying).tolist()},
            validation_report=_report(
                "informative_variation", status, int(varying.sum()), ">=1"
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class TOPSISPlugin:
    metadata: AlgorithmMetadata = _metadata("evaluation.topsis", "topsis")

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        decision = _matrix_support(problem, data, "topsis")
        if decision.status is not SupportStatus.SUPPORTED:
            return decision
        matrix = np.asarray(data.arrays["decision_matrix"], dtype=float)
        if "weights" not in data.arrays:
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_input:arrays.weights",)
            )
        weights = np.asarray(data.arrays["weights"], dtype=float)
        if weights.shape != (matrix.shape[1],) or np.any(weights < 0) or weights.sum() <= 0:
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_weights",))
        directions = tuple(data.metadata.get("directions", ()))
        if len(directions) != matrix.shape[1] or any(
            item not in {"benefit", "cost"} for item in directions
        ):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_directions",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        matrix = np.asarray(data.arrays["decision_matrix"], dtype=float)
        weights = np.asarray(data.arrays["weights"], dtype=float)
        weights = weights / weights.sum()
        directions = tuple(data.metadata["directions"])
        norms = np.linalg.norm(matrix, axis=0)
        normalized = np.divide(
            matrix,
            norms,
            out=np.zeros_like(matrix, dtype=float),
            where=norms != 0,
        )
        weighted = normalized * weights
        ideal_best = np.array(
            [
                weighted[:, index].max()
                if direction == "benefit"
                else weighted[:, index].min()
                for index, direction in enumerate(directions)
            ]
        )
        ideal_worst = np.array(
            [
                weighted[:, index].min()
                if direction == "benefit"
                else weighted[:, index].max()
                for index, direction in enumerate(directions)
            ]
        )
        distance_best = np.linalg.norm(weighted - ideal_best, axis=1)
        distance_worst = np.linalg.norm(weighted - ideal_worst, axis=1)
        denominator = distance_best + distance_worst
        scores = np.divide(
            distance_worst,
            denominator,
            out=np.full_like(distance_worst, 0.5),
            where=denominator != 0,
        )
        rank = np.argsort(-scores, kind="stable").tolist()
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"scores": scores.tolist(), "rank": rank},
            validation_report=_report(
                "score_range",
                CheckStatus.PASS,
                [float(scores.min()), float(scores.max())],
                [0.0, 1.0],
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _matrix_support(
    problem: ProblemSpec, data: DataBundle, family: str
) -> SupportDecision:
    if problem.model_family != family:
        return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
    if "decision_matrix" not in data.arrays:
        return SupportDecision(
            SupportStatus.UNKNOWN, ("missing_input:arrays.decision_matrix",)
        )
    matrix = np.asarray(data.arrays["decision_matrix"], dtype=float)
    if matrix.ndim != 2 or min(matrix.shape) == 0 or not np.all(np.isfinite(matrix)):
        return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_decision_matrix",))
    if matrix.shape[0] < 2:
        return SupportDecision(
            SupportStatus.UNSUPPORTED, ("at_least_two_alternatives_required",)
        )
    return SupportDecision(SupportStatus.SUPPORTED)


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
