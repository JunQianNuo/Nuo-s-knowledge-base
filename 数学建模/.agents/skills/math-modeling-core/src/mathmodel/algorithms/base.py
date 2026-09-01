from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Protocol

from mathmodel.contracts import DataBundle, ProblemSpec, SolveConfig, SolveResult


class PluginStatus(StrEnum):
    STABLE = "stable"
    EXPERIMENTAL = "experimental"


class SupportStatus(StrEnum):
    SUPPORTED = "supported"
    UNSUPPORTED = "unsupported"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class SupportDecision:
    status: SupportStatus
    reasons: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "reasons", tuple(self.reasons))


@dataclass(frozen=True, slots=True)
class PermissionSpec:
    filesystem_read: tuple[str, ...] = ("declared_inputs",)
    filesystem_write: tuple[str, ...] = ("run_artifacts",)
    network: bool = False
    subprocess: bool = False
    secrets: bool = False
    executables: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "filesystem_read", tuple(self.filesystem_read))
        object.__setattr__(self, "filesystem_write", tuple(self.filesystem_write))
        object.__setattr__(self, "executables", tuple(self.executables))


@dataclass(frozen=True, slots=True)
class FieldSpec:
    container: str
    name: str
    kind: str
    required: bool = True

    def __post_init__(self) -> None:
        if not self.container.strip() or not self.name.strip() or not self.kind.strip():
            raise ValueError("field container, name, and kind must not be empty")


@dataclass(frozen=True, slots=True)
class IOContract:
    input_fields: tuple[FieldSpec, ...] = ()
    output_fields: tuple[FieldSpec, ...] = ()
    config_fields: tuple[FieldSpec, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "input_fields", tuple(self.input_fields))
        object.__setattr__(self, "output_fields", tuple(self.output_fields))
        object.__setattr__(self, "config_fields", tuple(self.config_fields))

    def missing_inputs(self, data: DataBundle) -> tuple[str, ...]:
        missing: list[str] = []
        for item in self.input_fields:
            if not item.required:
                continue
            container = getattr(data, item.container, None)
            if container is None or item.name not in container:
                missing.append(f"missing_input:{item.container}.{item.name}")
        return tuple(missing)


@dataclass(frozen=True, slots=True)
class AlgorithmMetadata:
    plugin_id: str
    name: str
    algorithm_version: str
    api_version: int
    schema_version: int
    status: PluginStatus
    capabilities: frozenset[str]
    model_families: frozenset[str]
    dependencies: frozenset[str]
    solver_guarantee: str
    validation_capabilities: frozenset[str]
    deterministic: bool
    resource_tier: int
    permissions: PermissionSpec = field(default_factory=PermissionSpec)
    io_contract: IOContract = field(default_factory=IOContract)
    content_hash: str = ""

    def __post_init__(self) -> None:
        for name in ("plugin_id", "name", "algorithm_version", "solver_guarantee"):
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} must not be empty")
        if self.api_version <= 0 or self.schema_version <= 0:
            raise ValueError("api_version and schema_version must be positive")
        if self.resource_tier < 0:
            raise ValueError("resource_tier must be nonnegative")
        if not self.content_hash.strip():
            raise ValueError("content_hash must not be empty")
        for name in (
            "capabilities",
            "model_families",
            "dependencies",
            "validation_capabilities",
        ):
            object.__setattr__(self, name, frozenset(getattr(self, name)))


class AlgorithmPlugin(Protocol):
    metadata: AlgorithmMetadata

    def supports(
        self, problem: ProblemSpec, data: DataBundle
    ) -> SupportDecision: ...

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult: ...

    def validate_result(self, result: SolveResult) -> tuple[object, ...]: ...
