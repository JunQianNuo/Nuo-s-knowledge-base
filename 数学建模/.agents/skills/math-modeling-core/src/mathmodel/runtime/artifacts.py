from __future__ import annotations

from dataclasses import asdict, dataclass, is_dataclass
from datetime import date, datetime
from enum import Enum
import json
import os
from pathlib import Path
import tempfile
from typing import Any, Mapping

from mathmodel.contracts import CheckStatus


ARTIFACT_DIRECTORIES = (
    "inputs",
    "domain",
    "evidence",
    "selection",
    "solve",
    "validation",
    "figures",
    "paper-handoff",
)


@dataclass(frozen=True, slots=True)
class RunContext:
    skill_root: Path
    project_root: Path
    run_root: Path
    run_id: str

    @classmethod
    def create(
        cls,
        *,
        skill_root: Path,
        project_root: Path,
        output: str | Path,
    ) -> RunContext:
        project_path = Path(project_root)
        if not project_path.is_absolute():
            raise ValueError("project root must be absolute")
        project_path = project_path.resolve()
        output_path = Path(output)
        run_root = (
            output_path.resolve()
            if output_path.is_absolute()
            else (project_path / output_path).resolve()
        )
        if not run_root.is_relative_to(project_path):
            raise ValueError("output must be inside project root")
        results_root = (project_path / "results").resolve()
        if not run_root.is_relative_to(results_root) or run_root == results_root:
            raise ValueError("output must be inside project root results directory")
        if run_root.exists():
            raise ValueError(f"run output already exists: {run_root}")
        return cls(
            skill_root=Path(skill_root).resolve(),
            project_root=project_path,
            run_root=run_root,
            run_id=run_root.name,
        )


class ArtifactStore:
    def __init__(self, context: RunContext) -> None:
        self.context = context

    def initialize(self) -> None:
        try:
            self.context.run_root.mkdir(parents=True, exist_ok=False)
        except FileExistsError as exc:
            raise ValueError(
                f"run output already exists: {self.context.run_root}"
            ) from exc
        for directory in ARTIFACT_DIRECTORIES:
            (self.context.run_root / directory).mkdir(exist_ok=True)

    def resolve(self, relative_path: str | Path) -> Path:
        relative = Path(relative_path)
        if relative.is_absolute():
            raise ValueError("artifact path must be relative")
        resolved = (self.context.run_root / relative).resolve()
        if not resolved.is_relative_to(self.context.run_root):
            raise ValueError("artifact path escapes run root")
        return resolved

    def write_json(self, relative_path: str | Path, value: Any) -> Path:
        destination = self.resolve(relative_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(
            to_jsonable(value),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
        )
        try:
            with os.fdopen(file_descriptor, "w", encoding="utf-8", newline="\n") as stream:
                stream.write(payload)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary_name, destination)
        finally:
            temporary = Path(temporary_name)
            if temporary.exists():
                temporary.unlink()
        return destination


@dataclass(frozen=True, slots=True)
class PaperHandoff:
    manifest_hash: str
    validation_status: CheckStatus
    payload: Mapping[str, Any]
    warnings: tuple[str, ...]
    final_result: bool

    @classmethod
    def create(
        cls,
        *,
        manifest_hash: str,
        validation_status: CheckStatus,
        payload: Mapping[str, Any],
        warnings: tuple[str, ...] = (),
        final_result: bool = True,
    ) -> PaperHandoff:
        if final_result and validation_status in {CheckStatus.FAIL, CheckStatus.BLOCKED}:
            raise ValueError(
                f"cannot create final-result handoff from {validation_status.value}"
            )
        normalized_warnings = tuple(warnings)
        if validation_status is CheckStatus.WARN and not normalized_warnings:
            raise ValueError("WARN handoff must preserve at least one visible warning")
        if not manifest_hash.strip():
            raise ValueError("manifest_hash must not be empty")
        return cls(
            manifest_hash=manifest_hash,
            validation_status=validation_status,
            payload=dict(payload),
            warnings=normalized_warnings,
            final_result=final_result,
        )


def to_jsonable(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if is_dataclass(value):
        return to_jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): to_jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        items = [to_jsonable(item) for item in value]
        return sorted(items, key=str) if isinstance(value, (set, frozenset)) else items
    if hasattr(value, "tolist"):
        return value.tolist()
    return value
