from __future__ import annotations

from dataclasses import dataclass

from mathmodel.algorithms import DijkstraPlugin
from mathmodel.contracts import CheckStatus, RunStatus, SolveResult
from mathmodel.runtime import run_p1


def test_p1_accepts_dijkstra_only_after_known_oracle_passes() -> None:
    report = run_p1(DijkstraPlugin())

    assert report.status is CheckStatus.PASS
    assert report.plugin_id == "graph.dijkstra"
    assert report.reasons == ()
    assert "known_answer" in report.passed_checks


@dataclass
class WrongDijkstra:
    metadata = DijkstraPlugin().metadata

    def supports(self, problem, data):
        return DijkstraPlugin().supports(problem, data)

    def solve(self, problem, data, config):
        return SolveResult(
            status=RunStatus.SUCCESS,
            plugin_id=self.metadata.plugin_id,
            solution={"path": ["s", "t"], "distance": 99.0},
        )

    def validate_result(self, result):
        return ()


def test_p1_rejects_shape_correct_but_numerically_wrong_result() -> None:
    report = run_p1(WrongDijkstra())

    assert report.status is CheckStatus.FAIL
    assert "known_answer_mismatch" in report.reasons
