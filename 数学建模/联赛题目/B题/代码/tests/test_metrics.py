from __future__ import annotations

from common.metrics import compute_solution_metrics
from common.models import SortieColumn


def column(column_id, time, passenger_time, fuel, pk, ak):
    return SortieColumn(
        column_id,
        "A01",
        "T1",
        ("A01", "F001", "A01"),
        (False, False, False),
        (),
        time,
        passenger_time,
        fuel,
        pk,
        ak,
    )


def test_metrics_and_weighted_utilization() -> None:
    first = column("C1", 10, 20, 30, 50, 100)
    second = column("C2", 20, 40, 60, 10, 1000)
    metrics = compute_solution_metrics([(first, 2), (second, 1)])
    assert metrics.total_aircraft_time == 40
    assert metrics.total_passenger_time == 80
    assert metrics.total_fuel == 120
    assert metrics.number_of_flights == 3
    assert metrics.passenger_km == 110
    assert metrics.available_seat_km == 1200
    assert metrics.seat_utilization == 110 / 1200
