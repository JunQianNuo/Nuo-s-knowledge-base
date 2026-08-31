from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND, REFUEL_FACILITIES
from common.feasibility import leg_flight_minutes
from common.models import SolutionMetrics
from q2.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS


@dataclass(frozen=True)
class ValidationReport:
    valid: bool
    violations: tuple[str, ...]
    missing: int
    duplicates: int
    extra: int
    metrics: SolutionMetrics


def validate_q2_csv(
    *, routes_path: Path, assignments_path: Path, people: pd.DataFrame, distances
) -> ValidationReport:
    routes = pd.read_csv(routes_path)
    assignments = pd.read_csv(assignments_path)
    errors = []
    if list(routes.columns) != ROUTE_COLUMNS:
        errors.append("路线 CSV schema 错误")
    if list(assignments.columns) != ASSIGNMENT_COLUMNS:
        errors.append("人员 CSV schema 错误")
    expected = people["person_id"].astype(str).tolist()
    actual = assignments["person_id"].astype(str).tolist() if "person_id" in assignments else []
    expected_set, actual_set = set(expected), set(actual)
    missing, extra = len(expected_set - actual_set), len(actual_set - expected_set)
    duplicates = int(pd.Series(actual).duplicated().sum())
    if missing or extra or duplicates:
        errors.append(f"人员集合错误 missing={missing}, duplicates={duplicates}, extra={extra}")
    if actual != expected:
        errors.append("person_id 顺序与模板不一致")
    people_by_id = people.set_index(people["person_id"].astype(str)).to_dict("index")
    route_map = {}
    total_air, total_pax, total_fuel, pk, ak = 0, 0, 0.0, 0.0, 0.0
    for key, frame in routes.groupby(["aircraft_type", "flight_no"], sort=False):
        aircraft_type, flight_no = str(key[0]), int(key[1])
        if aircraft_type not in AIRCRAFT_SPECS:
            errors.append(f"非法机型 {aircraft_type}")
            continue
        frame = frame.sort_values("stop_order")
        orders = frame["stop_order"].astype(int).tolist()
        if orders != list(range(len(frame))):
            errors.append(f"{key} stop_order 不连续")
        route = tuple(frame["facility_id"].astype(str))
        refuels = tuple(frame["refuel"].astype(int))
        if len(route) < 3 or route[0] not in AIRPORTS or route[-1] != route[0]:
            errors.append(f"{key} 未同机场闭环")
            continue
        if len(route) - 2 > 5 or any(location in AIRPORTS for location in route[1:-1]):
            errors.append(f"{key} 海上着陆违规")
        if any(value not in (0, 1) for value in refuels):
            errors.append(f"{key} refuel 非 0/1")
        if refuels[0] or refuels[-1]:
            errors.append(f"{key} 机场 refuel 必须为0")
        if any(refuels[i] and route[i] not in REFUEL_FACILITIES for i in range(1, len(route) - 1)):
            errors.append(f"{key} 非法加油站")
        route_map[(aircraft_type, flight_no)] = (route, refuels)
    for aircraft_type, frame in routes.groupby("aircraft_type"):
        numbers = sorted(frame["flight_no"].astype(int).unique())
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append(f"{aircraft_type} flight_no 不连续")

    assignments_by_flight = {
        key: frame for key, frame in assignments.groupby(["aircraft_type", "flight_no"])
    }
    for key, (route, refuels) in route_map.items():
        spec = AIRCRAFT_SPECS[key[0]]
        loads = [0] * (len(route) - 1)
        frame = assignments_by_flight.get(key, assignments.iloc[0:0])
        arrival, departure = [0], [0]
        elapsed, fuel = 0, spec.tank_capacity_kg
        leg_distances = []
        for leg, (origin, destination) in enumerate(zip(route, route[1:])):
            distance = float(distances[(origin, destination)])
            leg_distances.append(distance)
            fuel -= spec.fuel_consumption_kg_per_km * distance
            if fuel < spec.reserve_fuel_kg - 1e-9:
                errors.append(f"{key} 到达站 {leg + 1} 余油不足")
            elapsed += leg_flight_minutes(distance, spec.speed_kmh)
            arrival.append(elapsed)
            if leg + 1 < len(route) - 1:
                elapsed += 20 if refuels[leg + 1] else 10
                if refuels[leg + 1]:
                    fuel = spec.tank_capacity_kg
            departure.append(elapsed)
        for _, row in frame.iterrows():
            person = str(row["person_id"])
            if person not in people_by_id:
                continue
            pickup, delivery = int(row["pickup_stop_order"]), int(row["delivery_stop_order"])
            if not 0 <= pickup < delivery < len(route):
                errors.append(f"{person} pickup/delivery 非法")
                continue
            request = people_by_id[person]
            origin = route[0] if request["origin_id"] == LAND else str(request["origin_id"])
            destination = (
                route[0] if request["destination_id"] == LAND else str(request["destination_id"])
            )
            if request["origin_id"] in AIRPORTS and request["origin_id"] != route[0]:
                errors.append(f"{person} 起点机场不兼容")
            if request["destination_id"] in AIRPORTS and request["destination_id"] != route[0]:
                errors.append(f"{person} 终点机场不兼容")
            if route[pickup] != origin or route[delivery] != destination:
                errors.append(f"{person} OD 与停靠不匹配")
            first = next(
                (i for i in range(pickup + 1, len(route)) if route[i] == destination), None
            )
            if delivery != first:
                errors.append(f"{person} 未在首次到达终点下机")
            for leg in range(pickup, delivery):
                loads[leg] += 1
            total_pax += arrival[delivery] - departure[pickup]
        if any(load > spec.capacity for load in loads):
            errors.append(f"{key} 逐航段超容量")
        total_distance = sum(leg_distances)
        total_air += elapsed
        total_fuel += spec.fuel_consumption_kg_per_km * total_distance
        pk += sum(load * distance for load, distance in zip(loads, leg_distances))
        ak += spec.capacity * total_distance
    metrics = SolutionMetrics(
        total_air, total_pax, total_fuel, len(route_map), pk, ak, pk / ak if ak else 0.0
    )
    return ValidationReport(not errors, tuple(errors), missing, duplicates, extra, metrics)
