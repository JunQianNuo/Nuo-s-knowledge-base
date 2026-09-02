from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import heapq
from itertools import count
from math import inf
from typing import Any, Mapping

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


def _metadata(plugin_id: str, family: str) -> AlgorithmMetadata:
    if family == "shortest_path":
        input_fields = (
            FieldSpec("tables", "graph", "weighted_adjacency"),
            FieldSpec("scalars", "source", "node"),
            FieldSpec("scalars", "target", "node"),
        )
        output_fields = (
            FieldSpec("solution", "path", "node_sequence"),
            FieldSpec("solution", "distance", "number"),
        )
    else:
        input_fields = (
            FieldSpec("tables", "capacities", "capacity_adjacency"),
            FieldSpec("scalars", "source", "node"),
            FieldSpec("scalars", "sink", "node"),
        )
        output_fields = (
            FieldSpec("solution", "flows", "flow_adjacency"),
            FieldSpec("solution", "min_cut_value", "number"),
        )
    return AlgorithmMetadata(
        plugin_id=plugin_id,
        name=plugin_id,
        algorithm_version="1.0.0",
        api_version=1,
        schema_version=1,
        status=PluginStatus.STABLE,
        capabilities=frozenset({family}),
        model_families=frozenset({family}),
        dependencies=frozenset(),
        solver_guarantee="exact for declared graph assumptions",
        validation_capabilities=frozenset({"path", "flow_conservation", "min_cut"}),
        deterministic=True,
        resource_tier=1,
        io_contract=IOContract(
            input_fields=input_fields,
            output_fields=output_fields,
            config_fields=(FieldSpec("config", "tolerance", "positive_number"),),
        ),
        content_hash=f"builtin:{plugin_id}:1.0.0",
    )


def _validation(name: str, passed: bool, observed: Any = None) -> ValidationReport:
    status = CheckStatus.PASS if passed else CheckStatus.FAIL
    return ValidationReport(
        status=status,
        checks=(
            ValidationCheck(
                name=name,
                status=status,
                severity=Severity.CRITICAL,
                observed=observed,
            ),
        ),
    )


@dataclass(slots=True)
class DijkstraPlugin:
    metadata: AlgorithmMetadata = _metadata("graph.dijkstra", "shortest_path")

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "shortest_path":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        graph = data.tables.get("graph")
        if not isinstance(graph, Mapping):
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_input:tables.graph",))
        if "source" not in data.scalars or "target" not in data.scalars:
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_source_or_target",)
            )
        if any(float(weight) < 0 for row in graph.values() for weight in row.values()):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("negative_edge_weight",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        graph = data.tables["graph"]
        source, target = data.scalars["source"], data.scalars["target"]
        distances: dict[Any, float] = {source: 0.0}
        previous: dict[Any, Any] = {}
        serial = count()
        queue: list[tuple[float, int, Any]] = [(0.0, next(serial), source)]
        while queue:
            distance, _, node = heapq.heappop(queue)
            if distance != distances.get(node):
                continue
            if node == target:
                break
            for neighbor, weight in graph.get(node, {}).items():
                candidate = distance + float(weight)
                if candidate < distances.get(neighbor, inf):
                    distances[neighbor] = candidate
                    previous[neighbor] = node
                    heapq.heappush(queue, (candidate, next(serial), neighbor))

        if target not in distances:
            return SolveResult(
                status=RunStatus.FAIL,
                plugin_id=self.metadata.plugin_id,
                diagnostics={"reason": "target_unreachable"},
                validation_report=_validation("target_reachable", False),
            )
        path = [target]
        while path[-1] != source:
            path.append(previous[path[-1]])
        path.reverse()
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"path": path, "distance": distances[target]},
            objective=distances[target],
            validation_report=_validation("path_reconstruction", True, path),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


@dataclass(slots=True)
class MaxFlowPlugin:
    metadata: AlgorithmMetadata = _metadata("graph.edmonds-karp", "maximum_flow")

    def supports(self, problem: ProblemSpec, data: DataBundle) -> SupportDecision:
        if problem.model_family != "maximum_flow":
            return SupportDecision(SupportStatus.UNSUPPORTED, ("wrong_model_family",))
        capacities = data.tables.get("capacities")
        if not isinstance(capacities, Mapping):
            return SupportDecision(
                SupportStatus.UNKNOWN, ("missing_input:tables.capacities",)
            )
        if "source" not in data.scalars or "sink" not in data.scalars:
            return SupportDecision(SupportStatus.UNKNOWN, ("missing_source_or_sink",))
        if any(
            float(capacity) < 0
            for row in capacities.values()
            for capacity in row.values()
        ):
            return SupportDecision(SupportStatus.UNSUPPORTED, ("negative_capacity",))
        return SupportDecision(SupportStatus.SUPPORTED)

    def solve(
        self, problem: ProblemSpec, data: DataBundle, config: SolveConfig
    ) -> SolveResult:
        support = self.supports(problem, data)
        if support.status is not SupportStatus.SUPPORTED:
            return _blocked(self.metadata.plugin_id, support.reasons)
        capacities = data.tables["capacities"]
        source, sink = data.scalars["source"], data.scalars["sink"]
        nodes = set(capacities)
        for row in capacities.values():
            nodes.update(row)
        capacity_matrix = {node: {other: 0.0 for other in nodes} for node in nodes}
        for start, row in capacities.items():
            for end, capacity in row.items():
                capacity_matrix[start][end] = float(capacity)
        net_flow = {node: {other: 0.0 for other in nodes} for node in nodes}

        total = 0.0
        while True:
            residual = _residual_graph(capacity_matrix, net_flow)
            parent = _augmenting_path(residual, source, sink)
            if parent is None:
                break
            bottleneck = inf
            node = sink
            while node != source:
                previous = parent[node]
                bottleneck = min(bottleneck, residual[previous][node])
                node = previous
            node = sink
            while node != source:
                previous = parent[node]
                net_flow[previous][node] += bottleneck
                net_flow[node][previous] -= bottleneck
                node = previous
            total += bottleneck

        flows = {
            start: {
                end: max(0.0, net_flow[start][end]) for end in row
            }
            for start, row in capacities.items()
        }
        residual = _residual_graph(capacity_matrix, net_flow)
        reachable = _reachable_nodes(residual, source)
        cut_value = sum(
            float(capacity)
            for start, row in capacities.items()
            if start in reachable
            for end, capacity in row.items()
            if end not in reachable
        )
        valid = abs(total - cut_value) <= config.tolerance
        return SolveResult(
            status=RunStatus.SUCCESS if valid else RunStatus.FAIL,
            plugin_id=self.metadata.plugin_id,
            solution={
                "flows": flows,
                "min_cut": {
                    "source_side": sorted(reachable, key=str),
                    "sink_side": sorted(nodes - reachable, key=str),
                },
                "min_cut_value": cut_value,
            },
            objective=total,
            validation_report=_validation(
                "max_flow_equals_min_cut", valid, {"flow": total, "cut": cut_value}
            ),
        )

    def validate_result(self, result: SolveResult) -> tuple[ValidationCheck, ...]:
        return result.validation_report.checks if result.validation_report else ()


def _augmenting_path(
    residual: Mapping[Any, Mapping[Any, float]], source: Any, sink: Any
) -> dict[Any, Any] | None:
    parent: dict[Any, Any] = {}
    visited = {source}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor, capacity in residual[node].items():
            if capacity > 0 and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == sink:
                    return parent
                queue.append(neighbor)
    return None


def _residual_graph(
    capacities: Mapping[Any, Mapping[Any, float]],
    net_flow: Mapping[Any, Mapping[Any, float]],
) -> dict[Any, dict[Any, float]]:
    return {
        start: {
            end: float(capacity) - float(net_flow[start][end])
            for end, capacity in row.items()
        }
        for start, row in capacities.items()
    }


def _reachable_nodes(
    residual: Mapping[Any, Mapping[Any, float]], source: Any
) -> set[Any]:
    visited = {source}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor, capacity in residual[node].items():
            if capacity > 0 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def _blocked(plugin_id: str, reasons: tuple[str, ...]) -> SolveResult:
    report = _validation("support_precondition", False, reasons)
    return SolveResult(
        status=RunStatus.BLOCKED,
        plugin_id=plugin_id,
        diagnostics={"reasons": reasons},
        validation_report=ValidationReport(
            status=CheckStatus.BLOCKED,
            checks=report.checks,
            rollback_stage="model_selection",
        ),
    )
