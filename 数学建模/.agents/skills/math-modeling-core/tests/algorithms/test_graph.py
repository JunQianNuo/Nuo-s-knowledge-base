from __future__ import annotations

from mathmodel.algorithms import DijkstraPlugin, MaxFlowPlugin, SupportStatus
from mathmodel.contracts import DataBundle, ProblemSpec, RunStatus, SolveConfig


def graph_problem(model_family: str) -> ProblemSpec:
    return ProblemSpec(
        problem_id=f"test-{model_family}",
        model_family=model_family,
        mandatory_outputs=("graph_solution",),
        required_capabilities={model_family},
    )


def test_dijkstra_finds_literal_shortest_path() -> None:
    plugin = DijkstraPlugin()
    data = DataBundle(
        tables={
            "graph": {
                "A": {"B": 1.0, "C": 5.0},
                "B": {"C": 2.0},
                "C": {},
            }
        },
        scalars={"source": "A", "target": "C"},
    )

    result = plugin.solve(graph_problem("shortest_path"), data, SolveConfig())

    assert result.status is RunStatus.SUCCESS
    assert result.solution["path"] == ["A", "B", "C"]
    assert result.solution["distance"] == 3.0


def test_dijkstra_rejects_negative_edge_before_execution() -> None:
    plugin = DijkstraPlugin()
    data = DataBundle(
        tables={"graph": {"A": {"B": -1.0}, "B": {}}},
        scalars={"source": "A", "target": "B"},
    )

    decision = plugin.supports(graph_problem("shortest_path"), data)

    assert decision.status is SupportStatus.UNSUPPORTED
    assert decision.reasons == ("negative_edge_weight",)


def test_max_flow_matches_hand_min_cut_and_conserves_flow() -> None:
    plugin = MaxFlowPlugin()
    capacities = {
        "s": {"a": 3.0, "b": 2.0},
        "a": {"b": 1.0, "t": 2.0},
        "b": {"t": 3.0},
        "t": {},
    }
    data = DataBundle(
        tables={"capacities": capacities},
        scalars={"source": "s", "sink": "t"},
    )

    result = plugin.solve(graph_problem("maximum_flow"), data, SolveConfig())

    assert result.status is RunStatus.SUCCESS
    assert result.objective == 5.0
    assert result.solution["min_cut_value"] == 5.0
    flows = result.solution["flows"]
    for node in ("a", "b"):
        incoming = sum(row.get(node, 0.0) for row in flows.values())
        outgoing = sum(flows.get(node, {}).values())
        assert abs(incoming - outgoing) < 1e-10
    for start, row in flows.items():
        for end, value in row.items():
            assert 0.0 <= value <= capacities[start][end]
