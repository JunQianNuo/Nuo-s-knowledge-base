from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "src"))

from mathmodel.algorithms import (  # noqa: E402
    AHPPlugin,
    ARIMAPlugin,
    DijkstraPlugin,
    EntropyWeightPlugin,
    LinearProgrammingPlugin,
    LinearRegressionPlugin,
    MaxFlowPlugin,
    MixedIntegerLinearProgrammingPlugin,
    MonteCarloPlugin,
    NonlinearOptimizationPlugin,
    ODESolverPlugin,
    PCAPlugin,
    RandomForestPlugin,
    RidgeRegressionPlugin,
    TOPSISPlugin,
)
from mathmodel.contracts import (  # noqa: E402
    CheckStatus,
    DataBundle,
    ProblemSpec,
    RunStatus,
    SolveConfig,
)
from mathmodel.runtime import (  # noqa: E402
    ArtifactStore,
    RunContext,
    build_manifest,
    execute_plugin,
)


PLUGIN_TYPES = {
    "linear_programming": LinearProgrammingPlugin,
    "mixed_integer_linear_programming": MixedIntegerLinearProgrammingPlugin,
    "nonlinear_optimization": NonlinearOptimizationPlugin,
    "shortest_path": DijkstraPlugin,
    "maximum_flow": MaxFlowPlugin,
    "ahp": AHPPlugin,
    "entropy_weight": EntropyWeightPlugin,
    "topsis": TOPSISPlugin,
    "linear_regression": LinearRegressionPlugin,
    "ridge_regression": RidgeRegressionPlugin,
    "arima": ARIMAPlugin,
    "pca": PCAPlugin,
    "random_forest": RandomForestPlugin,
    "ode": ODESolverPlugin,
    "monte_carlo": MonteCarloPlugin,
}


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(
        description="Run a validated math-modeling-core plugin"
    )
    value.add_argument("--project-root", required=True)
    value.add_argument("--problem", required=True)
    value.add_argument("--data")
    value.add_argument(
        "--mode", choices=("analyze", "solve", "review", "evidence"), default="solve"
    )
    value.add_argument("--output")
    value.add_argument("--refresh-evidence", action="store_true")
    return value


def main(argv: list[str] | None = None) -> int:
    arguments = parser().parse_args(argv)
    project_root = Path(arguments.project_root)
    if not project_root.is_absolute():
        print("project root must be absolute", file=sys.stderr)
        return 2

    problem_path = Path(arguments.problem).resolve()
    data_path = Path(arguments.data).resolve() if arguments.data else None
    try:
        problem_raw = _load_mapping(problem_path)
        problem = _problem_spec(problem_raw)
        data = _data_bundle(_load_mapping(data_path)) if data_path else DataBundle()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"invalid problem schema: {exc}", file=sys.stderr)
        return 2

    output = arguments.output or _default_output(problem_path, data_path)
    try:
        context = RunContext.create(
            skill_root=SKILL_ROOT,
            project_root=project_root,
            output=output,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    store = ArtifactStore(context)
    store.initialize()
    created_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )
    input_hashes = {"problem": _file_hash(problem_path)}
    if data_path:
        input_hashes["data"] = _file_hash(data_path)

    plugin_type = PLUGIN_TYPES.get(problem.model_family)
    if plugin_type is None:
        store.write_json("diagnostics.json", {"reason": "no_registered_plugin"})
        print(f"no plugin for model family: {problem.model_family}", file=sys.stderr)
        return 3
    plugin = plugin_type()
    additional_dependencies = frozenset(
        str(name) for name in problem_raw.get("required_dependencies", ())
    )
    config = SolveConfig()

    try:
        outcome = execute_plugin(
            plugin,
            problem,
            data,
            config,
            additional_dependencies=additional_dependencies,
        )
        if outcome.result is None:
            validation_status = CheckStatus.BLOCKED
            store.write_json(
                "diagnostics.json",
                {
                    "missing_dependencies": outcome.dependencies.missing,
                    "reasons": outcome.reasons,
                },
            )
        else:
            result = outcome.result
            validation_status = (
                result.validation_report.status
                if result.validation_report
                else (
                    CheckStatus.PASS
                    if result.status is RunStatus.SUCCESS
                    else CheckStatus.FAIL
                )
            )
            store.write_json("solve/result.json", result)
            store.write_json(
                "diagnostics.json",
                {"exit_code": outcome.exit_code, "diagnostics": result.diagnostics},
            )
        manifest = build_manifest(
            context=context,
            problem=problem,
            plugin=plugin.metadata,
            config=config,
            input_hashes=input_hashes,
            validation_status=validation_status,
            evidence_revision=None,
            created_at=created_at,
        )
        store.write_json("manifest.json", manifest)
        return outcome.exit_code
    except Exception as exc:
        store.write_json(
            "diagnostics.json",
            {"internal_error": type(exc).__name__, "message": str(exc)},
        )
        print(f"internal runtime error: {exc}", file=sys.stderr)
        return 5


def _problem_spec(value: Mapping[str, Any]) -> ProblemSpec:
    return ProblemSpec(
        problem_id=str(value["problem_id"]),
        model_family=str(value["model_family"]),
        mandatory_outputs=tuple(str(item) for item in value["mandatory_outputs"]),
        required_capabilities=frozenset(
            str(item) for item in value.get("required_capabilities", ())
        ),
        assumptions=dict(value.get("assumptions", {})),
        preference_weights=dict(value.get("preference_weights", {})),
        minimum_practical_improvement=value.get("minimum_practical_improvement"),
    )


def _data_bundle(value: Mapping[str, Any]) -> DataBundle:
    return DataBundle(
        arrays=dict(value.get("arrays", {})),
        scalars=dict(value.get("scalars", {})),
        tables=dict(value.get("tables", {})),
        targets=dict(value.get("targets", {})),
        metadata=dict(value.get("metadata", {})),
    )


def _load_mapping(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml
        except ImportError as exc:
            raise ValueError("YAML input requires PyYAML") from exc
        value = yaml.safe_load(text)
    if not isinstance(value, Mapping):
        raise ValueError("document root must be a mapping")
    return value


def _default_output(problem_path: Path, data_path: Path | None) -> str:
    digest = hashlib.sha256(problem_path.read_bytes())
    if data_path:
        digest.update(data_path.read_bytes())
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"results/{stamp}-{digest.hexdigest()[:8]}"


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
