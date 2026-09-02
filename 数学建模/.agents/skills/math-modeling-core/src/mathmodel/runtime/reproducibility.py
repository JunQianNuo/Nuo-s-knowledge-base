from __future__ import annotations

import hashlib
from importlib import metadata
import json
import platform
from pathlib import Path
from typing import Any, Mapping

from mathmodel.algorithms import AlgorithmMetadata
from mathmodel.contracts import CheckStatus, ProblemSpec, SolveConfig

from .artifacts import RunContext, to_jsonable


def build_manifest(
    *,
    context: RunContext,
    problem: ProblemSpec,
    plugin: AlgorithmMetadata | None,
    config: SolveConfig,
    input_hashes: Mapping[str, str],
    validation_status: CheckStatus,
    evidence_revision: str | None,
    created_at: str,
    mode: str = "solve",
    problem_path: Path | None = None,
    data_path: Path | None = None,
    review_artifact: Path | None = None,
    evidence_refreshed: bool = False,
    artifacts: tuple[str, ...] = (),
) -> dict[str, Any]:
    try:
        skill_version = metadata.version("math-modeling-core")
    except metadata.PackageNotFoundError:
        skill_version = "0.1.0"
    manifest: dict[str, Any] = {
        "schema_version": 2,
        "skill_version": skill_version,
        "run_id": context.run_id,
        "created_at": created_at,
        "mode": mode,
        "problem": to_jsonable(problem),
        "plugin": to_jsonable(plugin) if plugin is not None else None,
        "solve_config": to_jsonable(config),
        "input_hashes": dict(sorted(input_hashes.items())),
        "validation_status": validation_status.value,
        "evidence_revision": evidence_revision,
        "evidence": {
            "revision": evidence_revision,
            "refreshed": evidence_refreshed,
        },
        "selection": {
            "algorithm_plugin_id": plugin.plugin_id if plugin is not None else None,
            "algorithm_version": (
                plugin.algorithm_version if plugin is not None else None
            ),
        },
        "evaluation_protocol": {
            "mandatory_outputs": list(problem.mandatory_outputs),
            "required_capabilities": sorted(problem.required_capabilities),
            "minimum_practical_improvement": problem.minimum_practical_improvement,
        },
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "dependencies": _dependency_versions(plugin),
        },
        "inputs": _input_locations(
            problem_path, data_path, review_artifact, input_hashes
        ),
        "artifacts": _artifact_hashes(context, artifacts),
        "reproduce_command": _reproduce_command(
            context=context,
            problem_path=problem_path,
            data_path=data_path,
            mode=mode,
            evidence_refreshed=evidence_refreshed,
            review_artifact=review_artifact,
        ),
    }
    manifest["manifest_hash"] = _hash_manifest(manifest)
    return manifest


def _dependency_versions(plugin: AlgorithmMetadata | None) -> dict[str, str]:
    if plugin is None:
        return {}
    versions: dict[str, str] = {}
    for name in sorted(plugin.dependencies):
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = "missing"
    return versions


def _artifact_hashes(
    context: RunContext, artifacts: tuple[str, ...]
) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_name in sorted(set(artifacts)):
        relative_path = Path(relative_name)
        candidate = (context.run_root / relative_path).resolve()
        if relative_path.is_absolute() or not candidate.is_relative_to(context.run_root):
            raise ValueError(f"artifact path escapes run root: {relative_name}")
        hashes[relative_name] = (
            hashlib.sha256(candidate.read_bytes()).hexdigest()
            if candidate.is_file()
            else "missing"
        )
    return hashes


def _input_locations(
    problem_path: Path | None,
    data_path: Path | None,
    review_artifact: Path | None,
    input_hashes: Mapping[str, str],
) -> dict[str, dict[str, str]]:
    locations: dict[str, dict[str, str]] = {}
    for name, path in (
        ("problem", problem_path),
        ("data", data_path),
        ("review_artifact", review_artifact),
    ):
        if path is not None:
            locations[name] = {
                "path": str(Path(path).resolve()),
                "sha256": str(input_hashes.get(name, "")),
            }
    return locations


def _reproduce_command(
    *,
    context: RunContext,
    problem_path: Path | None,
    data_path: Path | None,
    mode: str,
    evidence_refreshed: bool,
    review_artifact: Path | None,
) -> str:
    command = [
        "python",
        f'"{context.skill_root / "scripts" / "run_model.py"}"',
        "--project-root",
        f'"{context.project_root}"',
    ]
    if problem_path is not None:
        command.extend(("--problem", f'"{Path(problem_path).resolve()}"'))
    if data_path is not None:
        command.extend(("--data", f'"{Path(data_path).resolve()}"'))
    if review_artifact is not None:
        command.extend(
            ("--review-artifact", f'"{Path(review_artifact).resolve()}"')
        )
    command.extend(
        (
            "--mode",
            f'"{mode}"',
            "--output",
            f'"results/{context.run_id}"',
        )
    )
    if evidence_refreshed:
        command.append("--refresh-evidence")
    return " ".join(command)


def _hash_manifest(manifest: Mapping[str, Any]) -> str:
    canonical = json.dumps(
        to_jsonable(manifest),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_manifest(manifest: Mapping[str, Any]) -> bool:
    """Verify a stored manifest without trusting its declared digest."""
    declared = manifest.get("manifest_hash")
    if not isinstance(declared, str) or not declared:
        return False
    payload = dict(manifest)
    payload.pop("manifest_hash", None)
    return declared == _hash_manifest(payload)
