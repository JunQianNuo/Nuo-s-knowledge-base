from __future__ import annotations

import json
import hashlib
from pathlib import Path

import pytest

from mathmodel.algorithms import PluginStatus, load_plugin_manifest


def manifest_value(content_hash: str = "sha256:abc") -> dict[str, object]:
    return {
        "plugin_id": "personal.example",
        "algorithm_version": "1.2.0",
        "api_version": 1,
        "schema_version": 1,
        "status": "experimental",
        "entrypoint": "personal_example:Plugin",
        "dependencies": ["numpy"],
        "permissions": {
            "filesystem_read": ["declared_inputs"],
            "filesystem_write": ["run_artifacts"],
            "network": False,
            "subprocess": False,
            "secrets": False,
            "executables": [],
        },
        "input_schema": [
            {"container": "arrays", "name": "x", "kind": "vector", "required": True}
        ],
        "output_schema": [
            {"container": "solution", "name": "value", "kind": "number", "required": True}
        ],
        "config_schema": [
            {"container": "config", "name": "seed", "kind": "integer", "required": True}
        ],
        "content_hash": content_hash,
    }


def write_plugin(root: Path) -> tuple[Path, str]:
    source = root / "personal_example.py"
    source.write_text("class Plugin:\n    pass\n", encoding="utf-8")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    return source, f"sha256:{digest}"


def test_loads_explicit_json_compatible_yaml_manifest(tmp_path: Path) -> None:
    extension_root = tmp_path / "extensions"
    extension_root.mkdir()
    _, content_hash = write_plugin(extension_root)
    manifest_path = extension_root / "plugin.yaml"
    manifest_path.write_text(json.dumps(manifest_value(content_hash)), encoding="utf-8")

    manifest = load_plugin_manifest(manifest_path, allowed_roots=(extension_root,))

    assert manifest.plugin_id == "personal.example"
    assert manifest.status is PluginStatus.EXPERIMENTAL
    assert manifest.entrypoint == "personal_example:Plugin"
    assert manifest.dependencies == frozenset({"numpy"})
    assert manifest.permissions.network is False
    assert manifest.io_contract.input_fields[0].name == "x"


def test_loader_rejects_manifest_outside_explicit_root(tmp_path: Path) -> None:
    allowed = tmp_path / "allowed"
    allowed.mkdir()
    _, content_hash = write_plugin(tmp_path)
    outside = tmp_path / "outside.yaml"
    outside.write_text(json.dumps(manifest_value(content_hash)), encoding="utf-8")

    with pytest.raises(ValueError, match="outside allowed roots"):
        load_plugin_manifest(outside, allowed_roots=(allowed,))


def test_loader_rejects_unknown_fields_instead_of_guessing(tmp_path: Path) -> None:
    _, content_hash = write_plugin(tmp_path)
    manifest_path = tmp_path / "plugin.yaml"
    value = manifest_value(content_hash)
    value["install_command"] = "pip install arbitrary-package"
    manifest_path.write_text(json.dumps(value), encoding="utf-8")

    with pytest.raises(ValueError, match="unknown manifest fields"):
        load_plugin_manifest(manifest_path, allowed_roots=(tmp_path,))


def test_loader_rejects_content_hash_mismatch(tmp_path: Path) -> None:
    write_plugin(tmp_path)
    manifest_path = tmp_path / "plugin.yaml"
    manifest_path.write_text(json.dumps(manifest_value("sha256:deadbeef")), encoding="utf-8")

    with pytest.raises(ValueError, match="content hash mismatch"):
        load_plugin_manifest(manifest_path, allowed_roots=(tmp_path,))
