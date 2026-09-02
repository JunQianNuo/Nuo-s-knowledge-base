from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from numbers import Integral, Real
from collections.abc import Mapping, Sequence
from typing import Any, Protocol

import numpy as np

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

    def validate_inputs(self, data: DataBundle) -> tuple[str, ...]:
        reasons: list[str] = []
        for item in self.input_fields:
            container = getattr(data, item.container, None)
            if container is None or item.name not in container:
                if item.required:
                    reasons.append(f"missing_input:{item.container}.{item.name}")
                continue
            if not _matches_kind(container[item.name], item.kind):
                reasons.append(
                    f"invalid_input:{item.container}.{item.name}:{item.kind}"
                )
        return tuple(reasons)

    def missing_inputs(self, data: DataBundle) -> tuple[str, ...]:
        return tuple(
            reason for reason in self.validate_inputs(data) if reason.startswith("missing_")
        )

    def validate_config(self, config: SolveConfig) -> tuple[str, ...]:
        reasons: list[str] = []
        for item in self.config_fields:
            value = getattr(config, item.name, None)
            if value is None:
                if item.required:
                    reasons.append(f"missing_config:{item.name}")
                continue
            if not _matches_kind(value, item.kind):
                reasons.append(f"invalid_config:{item.name}:{item.kind}")
        return tuple(reasons)

    def validate_output(self, result: SolveResult) -> tuple[str, ...]:
        reasons: list[str] = []
        for item in self.output_fields:
            container = getattr(result, item.container, None)
            if container is None or item.name not in container:
                if item.required:
                    reasons.append(f"missing_output:{item.container}.{item.name}")
                continue
            if not _matches_kind(container[item.name], item.kind):
                reasons.append(
                    f"invalid_output:{item.container}.{item.name}:{item.kind}"
                )
        return tuple(reasons)


def _matches_kind(value: Any, kind: str) -> bool:
    if kind == "callable" or kind == "vectorized_callable":
        return callable(value)
    if kind == "ndarray":
        return isinstance(value, np.ndarray)
    if kind in {"number", "positive_number"}:
        valid = isinstance(value, Real) and not isinstance(value, bool) and np.isfinite(value)
        return bool(valid and (kind != "positive_number" or value > 0))
    if kind in {"integer", "positive_integer"}:
        valid = isinstance(value, Integral) and not isinstance(value, bool)
        return bool(valid and (kind != "positive_integer" or value > 0))
    if kind == "node":
        try:
            hash(value)
        except TypeError:
            return False
        return True
    if kind in {"weighted_adjacency", "capacity_adjacency", "flow_adjacency"}:
        if not isinstance(value, Mapping):
            return False
        try:
            weights = [
                float(weight)
                for row in value.values()
                for weight in row.values()
                if isinstance(row, Mapping)
            ]
        except (TypeError, ValueError):
            return False
        return all(isinstance(row, Mapping) for row in value.values()) and bool(
            np.all(np.isfinite(weights))
        )
    if kind == "arima_order":
        return (
            isinstance(value, (tuple, list))
            and len(value) == 3
            and all(isinstance(item, Integral) and item >= 0 for item in value)
        )
    if kind == "benefit_cost_sequence":
        return isinstance(value, (tuple, list)) and all(
            item in {"benefit", "cost"} for item in value
        )
    if kind in {"node_sequence", "index_sequence"}:
        return isinstance(value, Sequence) and not isinstance(value, (str, bytes))

    try:
        array = np.asarray(value)
    except (TypeError, ValueError):
        return False
    vector_kinds = {
        "vector",
        "probability_vector",
        "bounded_vector",
        "ordered_vector",
        "increasing_vector",
        "chronological_vector",
        "state_vector",
        "target_vector",
    }
    matrix_kinds = {
        "matrix",
        "positive_square_matrix",
        "feature_matrix",
        "orthonormal_matrix",
        "trajectory_matrix",
        "dimension_by_two_matrix",
    }
    if kind in vector_kinds:
        if array.ndim != 1:
            return False
        if kind == "target_vector":
            if np.issubdtype(array.dtype, np.number):
                return bool(np.all(np.isfinite(array.astype(float))))
            return bool(all(item is not None and str(item) != "" for item in array))
        try:
            numeric = np.asarray(value, dtype=float)
        except (TypeError, ValueError):
            return False
        if not np.all(np.isfinite(numeric)):
            return False
        if kind == "probability_vector":
            return bool(np.all(numeric >= 0) and np.isclose(numeric.sum(), 1.0))
        if kind == "bounded_vector":
            return bool(np.all((numeric >= 0) & (numeric <= 1)))
        if kind == "increasing_vector":
            return bool(numeric.size > 0 and np.all(np.diff(numeric) > 0))
        if kind == "ordered_vector":
            return bool(np.all(np.diff(numeric) <= 0))
        return True
    if kind in matrix_kinds:
        if array.ndim != 2:
            return False
        try:
            numeric = np.asarray(value, dtype=float)
        except (TypeError, ValueError):
            return False
        if not np.all(np.isfinite(numeric)):
            return False
        if kind == "positive_square_matrix":
            return bool(
                numeric.shape[0] == numeric.shape[1] and np.all(numeric > 0)
            )
        if kind == "dimension_by_two_matrix":
            return array.shape[1:] == (2,)
        return True
    return False


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
