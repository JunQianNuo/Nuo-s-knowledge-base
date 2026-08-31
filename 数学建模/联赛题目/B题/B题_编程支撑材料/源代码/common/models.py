from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Mapping, Optional, Sequence


@dataclass(frozen=True)
class AircraftSpec:
    aircraft_type: str
    capacity: int
    speed_kmh: int
    fuel_consumption_kg_per_km: float
    tank_capacity_kg: float
    reserve_fuel_kg: float


@dataclass(frozen=True)
class Request:
    person_id: str
    origin_id: str
    destination_id: str
    earliest_pickup_time: Optional[datetime] = None
    latest_arrival_time: Optional[datetime] = None
    task_type: Optional[str] = None


@dataclass(frozen=True)
class RequestGroup:
    group_id: str
    person_ids: tuple[str, ...]
    origin_id: str
    destination_id: str
    earliest_pickup_time: Optional[datetime] = None
    latest_arrival_time: Optional[datetime] = None
    task_type: Optional[str] = None

    @property
    def quantity(self) -> int:
        return len(self.person_ids)


@dataclass(frozen=True)
class PassengerAllocation:
    group_id: str
    quantity: int
    pickup_stop: int
    delivery_stop: int


@dataclass(frozen=True)
class SortieColumn:
    column_id: str
    base_airport: str
    aircraft_type: str
    route: tuple[str, ...]
    refuel_decisions: tuple[bool, ...]
    allocations: tuple[PassengerAllocation, ...]
    aircraft_time: int = 0
    passenger_time: int = 0
    fuel_used: float = 0.0
    passenger_km: float = 0.0
    available_seat_km: float = 0.0

    def service_quantity(self, group_id: str) -> int:
        return sum(item.quantity for item in self.allocations if item.group_id == group_id)


@dataclass(frozen=True)
class TimedSortieColumn(SortieColumn):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    arrival_times: tuple[datetime, ...] = ()
    departure_times: tuple[datetime, ...] = ()
    compatible_aircraft: tuple[str, ...] = ()


@dataclass(frozen=True)
class FeasibilityResult:
    feasible: bool
    violations: tuple[str, ...]
    aircraft_time: int
    passenger_time: int
    fuel_used: float
    passenger_km: float
    available_seat_km: float
    leg_loads: tuple[int, ...] = ()
    arrival_fuel: tuple[float, ...] = ()
    arrival_minutes: tuple[int, ...] = ()
    departure_minutes: tuple[int, ...] = ()


@dataclass(frozen=True)
class SolutionMetrics:
    total_aircraft_time: int
    total_passenger_time: int
    total_fuel: float
    number_of_flights: int
    passenger_km: float
    available_seat_km: float
    seat_utilization: float


@dataclass(frozen=True)
class SolverResult:
    status: str
    objective: Optional[float]
    best_bound: Optional[float]
    wall_time: float
    multiplicities: Mapping[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class PersonAssignment:
    person_id: str
    aircraft_type: str
    flight_no: int
    pickup_stop_order: int
    delivery_stop_order: int
    column_id: str


DistanceMap = Mapping[tuple[str, str], float]
GroupMap = Mapping[str, RequestGroup]
ColumnSequence = Sequence[SortieColumn]
