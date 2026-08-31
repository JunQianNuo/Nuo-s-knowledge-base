from __future__ import annotations

from datetime import timedelta
from types import SimpleNamespace

from q3.algorithms import stage_a_pool
from q3.config import HORIZON_START
from q3.run_q3 import _temporary_certification


def test_stage_b_temporary_certification_is_strict():
    feasible = SimpleNamespace(
        restricted_pool_bound=160.0, temporary_served=149, status="FEASIBLE"
    )
    result = _temporary_certification(feasible)
    assert result["temporary_incumbent"] == 149
    assert result["temporary_best_bound"] == 160.0
    assert result["temporary_gap"] == 11 / 149
    assert not result["temporary_certified_optimal"]
    optimal = SimpleNamespace(
        restricted_pool_bound=149.0, temporary_served=149, status="OPTIMAL"
    )
    assert _temporary_certification(optimal)["temporary_certified_optimal"]


def test_dense_time_sampling_only_adds_quartiles(monkeypatch):
    route = SimpleNamespace(
        departure_minutes=(0, 0), arrival_minutes=(0, 0), aircraft_time=60
    )
    group = SimpleNamespace(
        earliest_pickup_time=HORIZON_START + timedelta(minutes=360),
        latest_arrival_time=HORIZON_START + timedelta(minutes=420),
    )
    option = SimpleNamespace(pickup=0, delivery=1)
    monkeypatch.setattr(stage_a_pool, "physical_options", lambda *_: [option])
    assert stage_a_pool._critical_starts(route, [group], "baseline") == {360, 390, 420}
    assert stage_a_pool._critical_starts(route, [group], "dense") == {
        360,
        375,
        390,
        405,
        420,
    }


def test_sensitivity_entrypoints_are_dry_run_by_default(tmp_path):
    from q1.run_sensitivity import main as q1_main
    from q3.run_time_density_sensitivity import main as q3_main

    assert q1_main(["--output-dir", str(tmp_path / "q1")]) == 0
    assert q3_main(["--output-dir", str(tmp_path / "q3")]) == 0
    assert not list(tmp_path.iterdir())
