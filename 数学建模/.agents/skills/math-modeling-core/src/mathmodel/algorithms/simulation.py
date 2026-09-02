from __future__ import annotations

from dataclasses import dataclass
from statistics import NormalDist

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
    FieldSpec,
    IOContract,
    PluginStatus,
    SupportDecision,
    SupportStatus,
)


@dataclass(slots=True)
class MonteCarloPlugin:
    metadata: AlgorithmMetadata = AlgorithmMetadata(
        plugin_id="simulation.monte-carlo",
        name="simulation.monte-carlo",
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({"monte_carlo"}),
        model_families=frozenset({"monte_carlo"}),
        dependencies=frozenset({"numpy"}),
        solver_guarantee="seeded independent uniform sampling with normal interval",
        validation_capabilities=frozenset(
            {"seed_replay", "finite_samples", "confidence_interval"}
        ),
        deterministic=True,
        resource_tier=2,
        io_contract=IOContract(
            input_fields=(
                FieldSpec("arrays", "bounds", "dimension_by_two_matrix"),
                FieldSpec("metadata", "integrand", "vectorized_callable"),
                FieldSpec("scalars", "n_samples", "integer"),
            ),
            output_fields=(
                FieldSpec("solution", "estimate", "number"),
                FieldSpec("solution", "ci_low", "number"),
                FieldSpec("solution", "ci_high", "number"),
            ),
            config_fields=(FieldSpec("config", "seed", "integer"),),
        ),
        content_hash="builtin:simulation.monte-carlo:1.0.0",
    )

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "monte_carlo":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        if "bounds" not in data.arrays:
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_input:arrays.bounds",))
        if not callable(data.metadata.get("integrand")):
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_callable:metadata.integrand",)
            )
        bounds = np.asarray(data.arrays["bounds"], dtype=float)
        n_samples = int(data.scalars.get("n_samples", 0))
        confidence = float(data.scalars.get("confidence", 0.95))
        if (
            bounds.ndim != 2
            or bounds.shape[1:] != (2,)
            or bounds.shape[0] == 0
            or not np.all(np.isfinite(bounds))
            or np.any(bounds[:, 1] <= bounds[:, 0])
        ):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_bounds",))
        if n_samples < 2:
            return SupportDecision(SupportStatus.UNSUPPORTED, ("insufficient_samples",))
        if not 0.0 < confidence < 1.0:
            return SupportDecision(SupportStatus.UNSUPPORTED, ("invalid_confidence",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        bounds = np.asarray(data.arrays["bounds"], dtype=float)
        n_samples = int(data.scalars["n_samples"])
        confidence = float(data.scalars.get("confidence", 0.95))
        rng = np.random.default_rng(config.seed)
        unit_samples = rng.random((n_samples, bounds.shape[0]))
        points = bounds[:, 0] + unit_samples * (bounds[:, 1] - bounds[:, 0])
        values = np.asarray(data.metadata["integrand"](points), dtype=float)
        if values.shape != (n_samples,) or not np.all(np.isfinite(values)):
            return _blocked(self.metadata.plugin_id, ("invalid_integrand_output",))
        volume = float(np.prod(bounds[:, 1] - bounds[:, 0]))
        estimate = volume * float(values.mean())
        standard_error = volume * float(values.std(ddof=1)) / np.sqrt(n_samples)
        quantile = NormalDist().inv_cdf(0.5 + confidence / 2.0)
        margin = quantile * standard_error
        ci_low, ci_high = estimate - margin, estimate + margin
        check = ValidationCheck(
            name="finite_ordered_confidence_interval",
            status=CheckStatus.PASS,
            severity=Severity.MAJOR,
            observed=[ci_low, estimate, ci_high],
        )
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={
                "estimate": estimate,
                "standard_error": standard_error,
                "ci_low": ci_low,
                "ci_high": ci_high,
            },
            diagnostics={
                "seed": config.seed,
                "n_samples": n_samples,
                "confidence": confidence,
                "dimension": int(bounds.shape[0]),
            },
            validation_report=ValidationReport(
                status=CheckStatus.PASS, checks=(check,)
            ),
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
