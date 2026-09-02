from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any, Mapping

from .base import FieldSpec, IOContract, PermissionSpec, PluginStatus


MANIFEST_FIELDS = frozenset(
    {
        "plugin_id",
        "algorithm_version",
        "api_version",
        "schema_version",
        "status",
        "entrypoint",
        "dependencies",
        "permissions",
        "input_schema",
        "output_schema",
        "config_schema",
        "content_hash",
    }
)
PERMISSION_FIELDS = frozenset(
    {
        "filesystem_read",
        "filesystem_write",
        "network",
        "subprocess",
        "secrets",
        "executables",
    }
)
FIELD_SPEC_FIELDS = frozenset({"container", "name", "kind", "required"})


@dataclass(frozen=True, slots=True)
class PluginManifest:
    plugin_id: str
    algorithm_version: str
    api_version: int
    schema_version: int
    status: PluginStatus
    entrypoint: str
    dependencies: frozenset[str]
    permissions: PermissionSpec
    io_contract: IOContract
    content_hash: str
    manifest_path: Path
    source_path: Path


def load_plugin_manifest(
    path: str | Path, *, allowed_roots: tuple[Path, ...] | list[Path]
) -> PluginManifest:
    """Validate extension metadata and source integrity without importing code."""
    manifest_path = Path(path).resolve()
    roots = tuple(Path(root).resolve() for root in allowed_roots)
    _require_in_allowed_roots(manifest_path, roots, label="plugin manifest")
    if manifest_path.suffix.casefold() not in {".json", ".yaml", ".yml"}:
        raise ValueError("plugin manifest must be JSON or YAML")

    value = _load_mapping(manifest_path)
    _require_exact_fields(value, MANIFEST_FIELDS, label="manifest")

    plugin_id = str(value["plugin_id"])
    version = str(value["algorithm_version"])
    entrypoint = str(value["entrypoint"])
    content_hash = str(value["content_hash"])
    if not re.fullmatch(r"[a-z0-9]+(?:[._-][a-z0-9]+)+", plugin_id):
        raise ValueError("invalid plugin_id")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("algorithm_version must be semantic x.y.z")
    if not re.fullmatch(
        r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*:[A-Za-z_]\w*", entrypoint
    ):
        raise ValueError("entrypoint must be module.path:ObjectName")

    api_version = int(value["api_version"])
    schema_version = int(value["schema_version"])
    if api_version <= 0 or schema_version <= 0:
        raise ValueError("api_version and schema_version must be positive")
    try:
        status = PluginStatus(str(value["status"]))
    except ValueError as exc:
        raise ValueError("invalid plugin status") from exc

    dependencies = _parse_dependencies(value["dependencies"])
    permissions = _parse_permissions(value["permissions"])
    io_contract = IOContract(
        input_fields=_parse_field_specs(value["input_schema"], "input_schema"),
        output_fields=_parse_field_specs(value["output_schema"], "output_schema"),
        config_fields=_parse_field_specs(value["config_schema"], "config_schema"),
    )

    module_name = entrypoint.partition(":")[0]
    source_path = (
        manifest_path.parent.joinpath(*module_name.split(".")).with_suffix(".py").resolve()
    )
    _require_in_allowed_roots(source_path, roots, label="plugin source")
    if not source_path.is_file():
        raise ValueError(f"plugin source does not exist: {source_path}")
    actual_hash = f"sha256:{sha256(source_path.read_bytes()).hexdigest()}"
    if not re.fullmatch(r"sha256:[0-9a-fA-F]+", content_hash) or not _same_hash(
        content_hash, actual_hash
    ):
        raise ValueError("content hash mismatch")

    return PluginManifest(
        plugin_id=plugin_id,
        algorithm_version=version,
        api_version=api_version,
        schema_version=schema_version,
        status=status,
        entrypoint=entrypoint,
        dependencies=dependencies,
        permissions=permissions,
        io_contract=io_contract,
        content_hash=actual_hash,
        manifest_path=manifest_path,
        source_path=source_path,
    )


def _require_in_allowed_roots(path: Path, roots: tuple[Path, ...], *, label: str) -> None:
    if not roots or not any(path.is_relative_to(root) for root in roots):
        raise ValueError(f"{label} is outside allowed roots")


def _require_exact_fields(
    value: Mapping[str, Any], expected: frozenset[str], *, label: str
) -> None:
    unknown = set(value) - expected
    missing = expected - set(value)
    if unknown:
        raise ValueError(f"unknown {label} fields: " + ",".join(sorted(unknown)))
    if missing:
        raise ValueError(f"missing {label} fields: " + ",".join(sorted(missing)))


def _parse_dependencies(value: Any) -> frozenset[str]:
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise ValueError("dependencies must be a list of non-empty package names")
    return frozenset(value)


def _parse_permissions(value: Any) -> PermissionSpec:
    if not isinstance(value, Mapping):
        raise ValueError("permissions must be a mapping")
    _require_exact_fields(value, PERMISSION_FIELDS, label="permissions")
    for field_name in ("filesystem_read", "filesystem_write", "executables"):
        items = value[field_name]
        if not isinstance(items, list) or not all(isinstance(item, str) for item in items):
            raise ValueError(f"permissions.{field_name} must be a list of strings")
    for field_name in ("network", "subprocess", "secrets"):
        if not isinstance(value[field_name], bool):
            raise ValueError(f"permissions.{field_name} must be boolean")
    return PermissionSpec(
        filesystem_read=tuple(value["filesystem_read"]),
        filesystem_write=tuple(value["filesystem_write"]),
        network=value["network"],
        subprocess=value["subprocess"],
        secrets=value["secrets"],
        executables=tuple(value["executables"]),
    )


def _parse_field_specs(value: Any, label: str) -> tuple[FieldSpec, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a list")
    fields: list[FieldSpec] = []
    for item in value:
        if not isinstance(item, Mapping):
            raise ValueError(f"{label} entries must be mappings")
        _require_exact_fields(item, FIELD_SPEC_FIELDS, label=f"{label} entry")
        if not isinstance(item["required"], bool):
            raise ValueError(f"{label}.required must be boolean")
        fields.append(
            FieldSpec(
                container=str(item["container"]),
                name=str(item["name"]),
                kind=str(item["kind"]),
                required=item["required"],
            )
        )
    return tuple(fields)


def _same_hash(left: str, right: str) -> bool:
    return left.casefold() == right.casefold()


def _load_mapping(path: Path) -> Mapping[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml
        except ImportError as exc:
            raise ValueError("YAML plugin manifests require PyYAML") from exc
        value = yaml.safe_load(text)
    if not isinstance(value, Mapping):
        raise ValueError("plugin manifest root must be a mapping")
    return value
