from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND, REFUEL_FACILITIES
from common.feasibility import leg_flight_minutes
from q3.config import MANDATORY_TASKS
from q3.fleet import FLEET_BY_ID
from q3.io.csv_writer import ASSIGNMENT_COLUMNS, ROUTE_COLUMNS


@dataclass(frozen=True)
class Q3Metrics:
    mandatory_served: int = 0
    temporary_served: int = 0
    total_aircraft_time: int = 0
    total_passenger_time: int = 0
    total_fuel: float = 0.0
    number_of_flights: int = 0
    passenger_km: float = 0.0
    available_seat_km: float = 0.0

    @property
    def seat_utilization(self) -> float:
        return self.passenger_km / self.available_seat_km if self.available_seat_km else 0.0


@dataclass(frozen=True)
class ValidationReport:
    valid: bool
    violations: tuple[str, ...]
    mandatory_missing: int
    duplicate_persons: int
    invalid_temporary: int
    metrics: Q3Metrics


def _time(value, errors, label):
    if pd.isna(value) or str(value).strip() == "":
        return None
    try:
        return pd.Timestamp(value).to_pydatetime()
    except Exception:
        errors.append(f"{label} 时刻格式非法")
        return None


def validate_q3_csv(
    *, routes_path: Path, assignments_path: Path, people_path: Path, distances_path: Path
) -> ValidationReport:
    people = pd.read_csv(people_path)
    routes = pd.read_csv(routes_path)
    assignments = pd.read_csv(assignments_path, dtype={"person_id": str})
    raw_distances = pd.read_csv(distances_path)
    distances = {
        (str(row.from_id), destination): float(getattr(row, destination))
        for row in raw_distances.itertuples(index=False)
        for destination in raw_distances.columns[1:]
    }
    errors = []
    if list(routes.columns) != ROUTE_COLUMNS:
        errors.append("路线 CSV schema 错误")
    if list(assignments.columns) != ASSIGNMENT_COLUMNS:
        errors.append("人员 CSV schema 错误")
    expected = people["person_id"].astype(str).tolist()
    actual = assignments["person_id"].astype(str).tolist()
    duplicates = int(pd.Series(actual).duplicated().sum())
    if len(actual) != 4000 and len(people) == 4000:
        errors.append(f"人员行数 {len(actual)} != 4000")
    if actual != expected:
        errors.append("person_id 集合或顺序与模板不一致")
    if duplicates:
        errors.append("存在重复 person_id")

    route_map = {}
    aircraft_flights: dict[str, list[tuple]] = {}
    total_air = total_pax = 0
    total_fuel = pk = ak = 0.0
    for raw_key, frame in routes.groupby(["aircraft_id", "flight_no"], sort=False):
        aircraft_id, flight_no = str(raw_key[0]), int(raw_key[1])
        aircraft = FLEET_BY_ID.get(aircraft_id)
        if aircraft is None:
            errors.append(f"非法 aircraft_id {aircraft_id}")
            continue
        frame = frame.sort_values("stop_order")
        if frame["stop_order"].astype(int).tolist() != list(range(len(frame))):
            errors.append(f"{raw_key} stop_order 不连续")
        locations = tuple(frame["facility_id"].astype(str))
        refuels = tuple(frame["refuel"].astype(int))
        arrivals = tuple(_time(v, errors, f"{raw_key}") for v in frame["arrival_time"])
        departures = tuple(_time(v, errors, f"{raw_key}") for v in frame["departure_time"])
        if (
            len(locations) < 3
            or locations[0] != aircraft.base_airport
            or locations[-1] != locations[0]
        ):
            errors.append(f"{raw_key} 未从所属机场闭环")
            continue
        if len(locations) - 2 > 5 or any(x in AIRPORTS for x in locations[1:-1]):
            errors.append(f"{raw_key} 海上着陆违规")
        if arrivals[0] is not None or departures[-1] is not None:
            errors.append(f"{raw_key} 首末时刻空值规则错误")
        if departures[0] is None or arrivals[-1] is None:
            errors.append(f"{raw_key} 缺少起飞/返场时刻")
            continue
        if departures[0].date() != arrivals[-1].date():
            errors.append(f"{raw_key} 跨日或海上过夜")
        departure_clock = departures[0].hour * 60 + departures[0].minute
        return_clock = arrivals[-1].hour * 60 + arrivals[-1].minute
        if not 360 <= departure_clock <= 1080:
            errors.append(f"{raw_key} 起飞不在06:00-18:00")
        if return_clock > 1200:
            errors.append(f"{raw_key} 返场晚于20:00")
        spec = AIRCRAFT_SPECS[aircraft.aircraft_type]
        fuel = spec.tank_capacity_kg
        leg_distances = []
        for leg, arc in enumerate(zip(locations, locations[1:])):
            distance = distances[arc]
            leg_distances.append(distance)
            expected_arrival = departures[leg] + pd.Timedelta(
                minutes=leg_flight_minutes(distance, spec.speed_kmh)
            )
            if arrivals[leg + 1] != expected_arrival:
                errors.append(f"{raw_key} 航段 {leg} 时间传播错误")
            fuel -= spec.fuel_consumption_kg_per_km * distance
            if fuel < spec.reserve_fuel_kg - 1e-9:
                errors.append(f"{raw_key} 到达站 {leg + 1} 余油不足")
            if leg + 1 < len(locations) - 1:
                if arrivals[leg + 1] is None or departures[leg + 1] is None:
                    errors.append(f"{raw_key} 中间站缺少时刻")
                else:
                    minimum = 20 if refuels[leg + 1] else 10
                    dwell = int((departures[leg + 1] - arrivals[leg + 1]).total_seconds() // 60)
                    if dwell < minimum:
                        errors.append(f"{raw_key} 停靠时间不足")
                if refuels[leg + 1]:
                    if locations[leg + 1] not in REFUEL_FACILITIES:
                        errors.append(f"{raw_key} 非法加油站")
                    fuel = spec.tank_capacity_kg
        if refuels[0] or refuels[-1] or any(v not in (0, 1) for v in refuels):
            errors.append(f"{raw_key} refuel 违规")
        route_map[(aircraft_id, flight_no)] = (locations, arrivals, departures, leg_distances, spec)
        aircraft_flights.setdefault(aircraft_id, []).append(
            (flight_no, departures[0], arrivals[-1])
        )
        total_air += int((arrivals[-1] - departures[0]).total_seconds() // 60)
        total_distance = sum(leg_distances)
        total_fuel += spec.fuel_consumption_kg_per_km * total_distance
        ak += spec.capacity * total_distance

    for aircraft_id, flights in aircraft_flights.items():
        by_number = sorted(flights)
        if [item[0] for item in by_number] != list(range(1, len(by_number) + 1)):
            errors.append(f"{aircraft_id} flight_no 不从1连续")
        chronological = sorted(flights, key=lambda item: item[1])
        if [item[0] for item in chronological] != list(range(1, len(chronological) + 1)):
            errors.append(f"{aircraft_id} flight_no 未按起飞时刻编号")
        for previous, following in zip(chronological, chronological[1:]):
            if following[1] < previous[2] + pd.Timedelta(minutes=30):
                errors.append(f"{aircraft_id} 相邻架次周转不足30分钟")

    people_by_id = people.set_index(people["person_id"].astype(str)).to_dict("index")
    loads = {key: [0] * (len(value[0]) - 1) for key, value in route_map.items()}
    mandatory_missing = invalid_temporary = mandatory_served = temporary_served = 0
    for _, row in assignments.iterrows():
        person = str(row["person_id"])
        request = people_by_id.get(person)
        if request is None:
            continue
        fields = [row[name] for name in ASSIGNMENT_COLUMNS[1:]]
        blank = all(pd.isna(value) or str(value).strip() == "" for value in fields)
        partial = any(pd.isna(value) or str(value).strip() == "" for value in fields) and not blank
        mandatory = str(request["task_type"]) in MANDATORY_TASKS
        if blank:
            if mandatory:
                mandatory_missing += 1
            continue
        if partial:
            errors.append(f"{person} assignment 部分为空")
            invalid_temporary += int(not mandatory)
            continue
        key = (str(row["aircraft_id"]), int(row["flight_no"]))
        route_data = route_map.get(key)
        if route_data is None:
            errors.append(f"{person} 引用未知架次")
            invalid_temporary += int(not mandatory)
            continue
        locations, arrivals, departures, leg_distances, spec = route_data
        pickup, delivery = int(row["pickup_stop_order"]), int(row["delivery_stop_order"])
        if not 0 <= pickup < delivery < len(locations):
            errors.append(f"{person} pickup/delivery 非法")
            continue
        base = locations[0]
        origin = base if request["origin_id"] == LAND else str(request["origin_id"])
        destination = base if request["destination_id"] == LAND else str(request["destination_id"])
        if request["origin_id"] in AIRPORTS and request["origin_id"] != base:
            errors.append(f"{person} 起点机场不兼容")
        if request["destination_id"] in AIRPORTS and request["destination_id"] != base:
            errors.append(f"{person} 终点机场不兼容")
        if locations[pickup] != origin or locations[delivery] != destination:
            errors.append(f"{person} OD 与停靠不匹配")
        first = next(
            (i for i in range(pickup + 1, len(locations)) if locations[i] == destination), None
        )
        if delivery != first:
            errors.append(f"{person} 未在首次到达终点下机")
        if departures[pickup] < pd.Timestamp(request["earliest_pickup_time"]):
            errors.append(f"{person} 早于 earliest pickup")
        if arrivals[delivery] > pd.Timestamp(request["latest_arrival_time"]):
            errors.append(f"{person} 晚于 latest arrival")
        for leg in range(pickup, delivery):
            loads[key][leg] += 1
        total_pax += int((arrivals[delivery] - departures[pickup]).total_seconds() // 60)
        if mandatory:
            mandatory_served += 1
        else:
            temporary_served += 1
    if mandatory_missing:
        errors.append(f"mandatory 缺失 {mandatory_missing}")
    for key, leg_loads in loads.items():
        capacity = route_map[key][4].capacity
        if any(load > capacity for load in leg_loads):
            errors.append(f"{key} 逐航段超容量")
        pk += sum(load * distance for load, distance in zip(leg_loads, route_map[key][3]))
    metrics = Q3Metrics(
        mandatory_served,
        temporary_served,
        total_air,
        total_pax,
        total_fuel,
        len(route_map),
        pk,
        ak,
    )
    return ValidationReport(
        not errors,
        tuple(dict.fromkeys(errors)),
        mandatory_missing,
        duplicates,
        invalid_temporary,
        metrics,
    )
