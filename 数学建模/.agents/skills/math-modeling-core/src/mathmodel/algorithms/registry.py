from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

from mathmodel.contracts import DataBundle, ProblemSpec

from .base import AlgorithmPlugin, PluginStatus, SupportStatus


@dataclass(frozen=True, slots=True)
class RegistryDecision:
    matches: tuple[AlgorithmPlugin, ...]
    rejected: Mapping[str, tuple[str, ...]]


class AlgorithmRegistry:
    def __init__(self, plugins: Iterable[AlgorithmPlugin] = ()) -> None:
        self._plugins: dict[tuple[str, str], AlgorithmPlugin] = {}
        for plugin in plugins:
            self.register(plugin)

    def register(self, plugin: AlgorithmPlugin) -> None:
        key = (plugin.metadata.plugin_id, plugin.metadata.algorithm_version)
        if key in self._plugins:
            raise ValueError(
                "duplicate plugin "
                f"{plugin.metadata.plugin_id}@{plugin.metadata.algorithm_version}"
            )
        self._plugins[key] = plugin

    def match(
        self,
        problem: ProblemSpec,
        data: DataBundle,
        *,
        installed_dependencies: set[str] | frozenset[str],
        allow_experimental: bool = False,
        api_version: int = 1,
        schema_version: int = 1,
    ) -> RegistryDecision:
        accepted: list[AlgorithmPlugin] = []
        rejected: dict[str, tuple[str, ...]] = {}

        for plugin in self._plugins.values():
            metadata = plugin.metadata
            reasons: list[str] = []
            if metadata.api_version != api_version:
                reasons.append(f"api_version_mismatch:{metadata.api_version}")
            if metadata.schema_version != schema_version:
                reasons.append(f"schema_version_mismatch:{metadata.schema_version}")
            if metadata.status is PluginStatus.EXPERIMENTAL and not allow_experimental:
                reasons.append("experimental_not_allowed")
            if problem.model_family not in metadata.model_families:
                reasons.append(f"unsupported_model_family:{problem.model_family}")
            missing_capabilities = problem.required_capabilities - metadata.capabilities
            if missing_capabilities:
                reasons.append(
                    "missing_capabilities:" + ",".join(sorted(missing_capabilities))
                )
            missing_dependencies = metadata.dependencies - set(installed_dependencies)
            if missing_dependencies:
                reasons.append(
                    "missing_dependencies:" + ",".join(sorted(missing_dependencies))
                )
            reasons.extend(metadata.io_contract.missing_inputs(data))

            if not reasons:
                support = plugin.supports(problem, data)
                if support.status is not SupportStatus.SUPPORTED:
                    reasons.extend(support.reasons or (support.status.value,))

            if reasons:
                rejected[metadata.plugin_id] = tuple(reasons)
            else:
                accepted.append(plugin)

        accepted.sort(key=self._sort_key)
        return RegistryDecision(tuple(accepted), rejected)

    @staticmethod
    def _sort_key(plugin: AlgorithmPlugin) -> tuple[object, ...]:
        metadata = plugin.metadata
        return (
            0 if metadata.status is PluginStatus.STABLE else 1,
            metadata.resource_tier,
            0 if metadata.deterministic else 1,
            metadata.plugin_id,
            metadata.algorithm_version,
        )
