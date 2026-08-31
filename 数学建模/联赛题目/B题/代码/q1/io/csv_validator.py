from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from common.config import (
    AIRCRAFT_SPECS,
    AIRPORTS,
    LAND,
    MAX_OFFSHORE_LANDINGS,
    OFFSHORE_FACILITIES,
    REFUEL_FACILITIES,
)
from common.models import SolutionMetrics
from q1.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS


@dataclass(frozen=True)
class CsvValidationReport:
    passed: bool
    violations: tuple[str, ...]
    metrics: SolutionMetrics
    assignment_rows: int
    missing: int
    duplicates: int

    def __str__(self) -> str:
        if self.passed:
            return "PASS"
        return "FAIL:\n" + "\n".join(f"- {item}" for item in self.violations)


def validate_q1_csv(
    routes_path: Path,
    assignments_path: Path,
    people: pd.DataFrame,
    distances: dict[tuple[str, str], float],
) -> CsvValidationReport:
    """不调用 evaluate_sortie，直接从正式 CSV 独立重建并验证。"""
    routes = pd.read_csv(routes_path)
    assignments = pd.read_csv(assignments_path)
    violations: list[str] = []
    if list(routes.columns) != ROUTE_COLUMNS:
        violations.append("q1-routes.csv 字段或顺序与官方模板不一致")
    if list(assignments.columns) != ASSIGNMENT_COLUMNS:
        violations.append("q1-assignments.csv 字段或顺序与官方模板不一致")
    expected_people = people["person_id"].astype(str).tolist()
    actual_people = assignments.get("person_id", pd.Series(dtype=str)).astype(str).tolist()
    counts = Counter(actual_people)
    missing_ids = set(expected_people) - set(actual_people)
    duplicate_ids = {person_id for person_id, count in counts.items() if count > 1}
    extra_ids = set(actual_people) - set(expected_people)
    if missing_ids:
        violations.append(f"遗漏人员 {len(missing_ids)} 名")
    if duplicate_ids:
        violations.append(f"重复人员 {len(duplicate_ids)} 名")
    if extra_ids:
        violations.append(f"未知人员 {len(extra_ids)} 名")
    if actual_people != expected_people:
        violations.append("assignments 未保持官方模板 person_id 顺序")

    people_index = people.set_index("person_id")
    flight_routes: dict[tuple[str, int], tuple[list[str], list[int]]] = {}
    for key, rows in routes.groupby(["aircraft_type", "flight_no"], sort=False):
        aircraft_type, flight_no = str(key[0]), int(key[1])
        ordered = rows.sort_values("stop_order")
        stop_orders = ordered["stop_order"].astype(int).tolist()
        if stop_orders != list(range(len(stop_orders))):
            violations.append(f"架次 {aircraft_type}-{flight_no} stop_order 不连续")
        facilities = ordered["facility_id"].astype(str).tolist()
        refuels = ordered["refuel"].astype(int).tolist()
        flight_routes[(aircraft_type, flight_no)] = (facilities, refuels)
    for aircraft_type, rows in routes.groupby("aircraft_type"):
        flight_numbers = sorted(rows["flight_no"].astype(int).unique())
        if flight_numbers != list(range(1, len(flight_numbers) + 1)):
            violations.append(f"机型 {aircraft_type} 的 flight_no 未从1连续编号")

    total_aircraft_time = 0
    total_passenger_time = 0
    total_fuel = 0.0
    total_pk = 0.0
    total_ak = 0.0
    for key, (route, refuels) in flight_routes.items():
        aircraft_type, flight_no = key
        spec = AIRCRAFT_SPECS.get(aircraft_type)
        if spec is None:
            violations.append(f"未知机型 {aircraft_type}")
            continue
        if len(route) < 3 or route[0] not in AIRPORTS or route[-1] != route[0]:
            violations.append(f"架次 {aircraft_type}-{flight_no} 未同机场闭环")
            continue
        if not 1 <= len(route) - 2 <= MAX_OFFSHORE_LANDINGS:
            violations.append(f"架次 {aircraft_type}-{flight_no} 海上着陆次数非法")
        if any(location not in OFFSHORE_FACILITIES for location in route[1:-1]):
            violations.append(f"架次 {aircraft_type}-{flight_no} 含非法海上停靠")
        if any(value not in (0, 1) for value in refuels):
            violations.append(f"架次 {aircraft_type}-{flight_no} refuel 非0/1")
        if refuels[0] or refuels[-1]:
            violations.append(f"架次 {aircraft_type}-{flight_no} 机场行 refuel 必须为0")
        for location, refuel in zip(route[1:-1], refuels[1:-1]):
            if refuel and location not in REFUEL_FACILITIES:
                violations.append(f"架次 {aircraft_type}-{flight_no} 在非法设施加油")

        rows = assignments[
            (assignments["aircraft_type"].astype(str) == aircraft_type)
            & (assignments["flight_no"].astype(int) == flight_no)
        ]
        leg_loads = [0] * (len(route) - 1)
        passenger_time = 0
        arrivals = [0]
        departures = [0]
        elapsed = 0
        leg_distances = []
        for leg, (origin, destination) in enumerate(zip(route, route[1:])):
            distance = distances.get((origin, destination))
            if distance is None or distance < 0:
                violations.append(f"架次 {aircraft_type}-{flight_no} 距离弧缺失")
                distance = 0.0
            leg_distances.append(distance)
            elapsed += math.ceil(60 * distance / spec.speed_kmh)
            arrivals.append(elapsed)
            if leg + 1 < len(route) - 1:
                elapsed += 10 + 10 * refuels[leg + 1]
            departures.append(elapsed)
        for assignment in rows.itertuples(index=False):
            person_id = str(assignment.person_id)
            if person_id not in people_index.index:
                continue
            pickup = int(assignment.pickup_stop_order)
            delivery = int(assignment.delivery_stop_order)
            if not 0 <= pickup < delivery < len(route):
                violations.append(f"人员 {person_id} 上下机序号非法")
                continue
            person = people_index.loc[person_id]
            origin = route[0] if person.origin_id == LAND else str(person.origin_id)
            destination = route[0] if person.destination_id == LAND else str(person.destination_id)
            if route[pickup] != origin or route[delivery] != destination:
                violations.append(f"人员 {person_id} 上下机地点与OD不一致")
                continue
            first_delivery = next(
                (index for index in range(pickup + 1, len(route)) if route[index] == destination),
                None,
            )
            if delivery != first_delivery:
                violations.append(f"人员 {person_id} 未在首次抵达终点时下机")
            for leg in range(pickup, delivery):
                leg_loads[leg] += 1
            passenger_time += arrivals[delivery] - departures[pickup]
        if any(load > spec.capacity for load in leg_loads):
            violations.append(f"架次 {aircraft_type}-{flight_no} 动态载客超容量")
        fuel = spec.tank_capacity_kg
        for leg, distance in enumerate(leg_distances):
            fuel -= spec.fuel_consumption_kg_per_km * distance
            if fuel < spec.reserve_fuel_kg - 1e-9:
                violations.append(f"架次 {aircraft_type}-{flight_no} 到站燃油低于安全余油")
            if leg + 1 < len(route) - 1 and refuels[leg + 1]:
                fuel = spec.tank_capacity_kg
        total_aircraft_time += elapsed
        total_passenger_time += passenger_time
        total_fuel += spec.fuel_consumption_kg_per_km * sum(leg_distances)
        total_pk += sum(load * distance for load, distance in zip(leg_loads, leg_distances))
        total_ak += spec.capacity * sum(leg_distances)

    referenced = set(
        zip(assignments["aircraft_type"].astype(str), assignments["flight_no"].astype(int))
    )
    missing_flights = referenced - set(flight_routes)
    if missing_flights:
        violations.append(f"人员引用不存在的架次 {sorted(missing_flights)[:3]}")
    metrics = SolutionMetrics(
        total_aircraft_time,
        total_passenger_time,
        total_fuel,
        len(flight_routes),
        total_pk,
        total_ak,
        total_pk / total_ak if total_ak else 0.0,
    )
    return CsvValidationReport(
        passed=not violations,
        violations=tuple(dict.fromkeys(violations)),
        metrics=metrics,
        assignment_rows=len(assignments),
        missing=len(missing_ids),
        duplicates=len(duplicate_ids),
    )
