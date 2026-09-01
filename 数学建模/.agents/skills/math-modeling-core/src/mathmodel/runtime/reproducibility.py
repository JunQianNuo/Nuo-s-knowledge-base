from __future__ import annotations

import hashlib
from importlib import metadata
import json
import platform
import sys
from typing import Any, Mapping

from mathmodel.algorithms import AlgorithmMetadata
from mathmodel.contracts import CheckStatus, ProblemSpec, SolveConfig

from .artifacts import RunContext, to_jsonable


def build_manifest(
    *,
    context: RunContext,
    problem: ProblemSpec,
    plugin: AlgorithmMetadata,
    config: SolveConfig,
    input_hashes: Mapping[str, str],
    validation_status: CheckStatus,
    evidence_revision: str | None,
    created_at: str,
) -> dict[str, Any]:
    try:
        skill_version = metadata.version("math-modeling-core")
    except metadata.PackageNotFoundError:
        skill_version = "0.1.0"
    manifest: dict[str, Any] = {
        "schema_version": 1,
        "skill_version": skill_version,
        "run_id": context.run_id,
        "created_at": created_at,
        "problem": to_jsonable(problem),
        "plugin": to_jsonable(plugin),
        "solve_config": to_jsonable(config),
        "input_hashes": dict(sorted(input_hashes.items())),
        "validation_status": validation_status.value,
        "evidence_revision": evidence_revision,
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "reproduce_command": (
            f'python "{context.skill_root / "scripts" / "run_model.py"}" '
            f'--project-root "{context.project_root}" --output "results/{context.run_id}"'
        ),
    }
    manifest["manifest_hash"] = _hash_manifest(manifest)
    return manifest


def _hash_manifest(manifest: Mapping[str, Any]) -> str:
    canonical = json.dumps(
        to_jsonable(manifest),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
