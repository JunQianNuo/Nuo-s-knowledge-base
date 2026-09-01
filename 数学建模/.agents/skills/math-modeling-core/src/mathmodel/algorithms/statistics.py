from __future__ import annotations

from dataclasses import dataclass

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


@dataclass(slots=True)
class PCAPlugin:
    metadata: AlgorithmMetadata = AlgorithmMetadata(
        plugin_id="statistics.pca",
        name="statistics.pca",
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({"pca"}),
        model_families=frozenset({"pca"}),
        dependencies=frozenset({"numpy"}),
        solver_guarantee="deterministic singular-value decomposition",
        validation_capabilities=frozenset({"orthonormality", "variance_order"}),
        deterministic=True,
        resource_tier=1,
        io_contract=IOContract(),
        content_hash="builtin:statistics.pca:1.0.0",
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "pca":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        if "X" not in data.arrays:
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_input:arrays.X",))
        x = np.asarray(data.arrays["X"], dtype=float)
        n_components = int(data.scalars.get("n_components", min(x.shape)))
        if (
            x.ndim != 2
            or x.shape[0] < 2
            or x.shape[1] == 0
            or not np.all(np.isfinite(x))
        ):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_feature_matrix",))
        if not 1 <= n_components <= min(x.shape):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_n_components",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        x = np.asarray(data.arrays["X"], dtype=float)
        n_components = int(data.scalars.get("n_components", min(x.shape)))
        mean = x.mean(axis=0)
        centered = x - mean
        _, singular_values, right_vectors = np.linalg.svd(
            centered, full_matrices=False
        )
        components = right_vectors[:n_components]
        explained_variance = singular_values[:n_components] ** 2 / (x.shape[0] - 1)
        total_variance = float(np.sum(singular_values**2 / (x.shape[0] - 1)))
        ratios = (
            np.zeros_like(explained_variance)
            if total_variance == 0
            else explained_variance / total_variance
        )
        transformed = centered @ components.T
        orthonormal_error = float(
            np.max(np.abs(components @ components.T - np.eye(n_components)))
        )
        status = (
            CheckStatus.PASS
            if orthonormal_error <= max(config.tolerance, 1e-12)
            else CheckStatus.FAIL
        )
        check = ValidationCheck(
            name="component_orthonormality",
            status=status,
            severity=Severity.CRITICAL,
            observed=orthonormal_error,
            threshold=max(config.tolerance, 1e-12),
        )
        return SolveResult(
            status=RunStatus.SUCCESS if status is CheckStatus.PASS else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={
                "components": components.tolist(),
                "explained_variance": explained_variance.tolist(),
                "explained_variance_ratio": ratios.tolist(),
                "mean": mean.tolist(),
                "transformed": transformed.tolist(),
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
