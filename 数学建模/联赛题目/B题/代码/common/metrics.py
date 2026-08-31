from __future__ import annotations

from collections.abc import Iterable

from .models import SolutionMetrics, SortieColumn


def compute_solution_metrics(
    columns_with_counts: Iterable[tuple[SortieColumn, int]],
) -> SolutionMetrics:
    total_aircraft_time = 0
    total_passenger_time = 0
    total_fuel = 0.0
    number_of_flights = 0
    passenger_km = 0.0
    available_seat_km = 0.0
    for column, count in columns_with_counts:
        if count < 0:
            raise ValueError("架次列执行次数不得为负")
        total_aircraft_time += column.aircraft_time * count
        total_passenger_time += column.passenger_time * count
        total_fuel += column.fuel_used * count
        number_of_flights += count
        passenger_km += column.passenger_km * count
        available_seat_km += column.available_seat_km * count
    utilization = passenger_km / available_seat_km if available_seat_km else 0.0
    return SolutionMetrics(
        total_aircraft_time,
        total_passenger_time,
        total_fuel,
        number_of_flights,
        passenger_km,
        available_seat_km,
        utilization,
    )
