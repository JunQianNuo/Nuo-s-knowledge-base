"""T_pax 分类分解审计（Q2）：联合方案 vs 分离基线，按 出海/海返/穿梭 三类。

纯 pandas + common 层实现，不依赖 ortools。供论文"人员总在途时间回归"解释使用。

用法（在 代码/ 目录）：
    python scripts/audit_tpax_breakdown.py
输出：
    q2/outputs/q2-tpax-by-category.csv
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

CODE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE_ROOT))

from common.config import AIRCRAFT_SPECS, AIRPORTS, LAND
from common.data_loader import load_distances, load_people_q2
from common.feasibility import leg_flight_minutes
from common.grouping import group_q2
from q2.algorithms.route_pool import build_route_pool

Q2_OUT = CODE_ROOT / "q2" / "outputs"
CATEGORY_CN = {"outbound": "出海", "return": "海返", "shuttle": "穿梭"}


def category_of(origin: str, destination: str) -> str:
    airport_like = {*AIRPORTS, LAND}
    if origin in airport_like and destination not in airport_like:
        return "outbound"
    if origin not in airport_like and destination in airport_like:
        return "return"
    return "shuttle"


def joint_breakdown(distances) -> pd.DataFrame:
    routes = pd.read_csv(Q2_OUT / "q2-routes.csv")
    assignments = pd.read_csv(Q2_OUT / "q2-assignments.csv")
    people = load_people_q2()
    request = people.set_index(people["person_id"].astype(str)).to_dict("index")

    route_map: dict[tuple[str, int], tuple[tuple[str, ...], tuple[int, ...]]] = {}
    for key, frame in routes.groupby(["aircraft_type", "flight_no"], sort=False):
        frame = frame.sort_values("stop_order")
        route_map[(str(key[0]), int(key[1]))] = (
            tuple(frame["facility_id"].astype(str)),
            tuple(frame["refuel"].astype(int)),
        )

    rows = []
    for key, (route, refuels) in route_map.items():
        spec = AIRCRAFT_SPECS[key[0]]
        arrival, departure = [0], [0]
        elapsed = 0
        for leg, (origin, destination) in enumerate(zip(route, route[1:])):
            elapsed += leg_flight_minutes(float(distances[(origin, destination)]), spec.speed_kmh)
            arrival.append(elapsed)
            if leg + 1 < len(route) - 1:
                elapsed += 20 if refuels[leg + 1] else 10
            departure.append(elapsed)
        frame = assignments[
            (assignments["aircraft_type"] == key[0]) & (assignments["flight_no"] == key[1])
        ]
        for _, row in frame.iterrows():
            person = str(row["person_id"])
            pickup, delivery = int(row["pickup_stop_order"]), int(row["delivery_stop_order"])
            info = request[person]
            category = category_of(str(info["origin_id"]), str(info["destination_id"]))
            pax_time = arrival[delivery] - departure[pickup]
            pax_km = sum(
                float(distances[(route[leg], route[leg + 1])]) for leg in range(pickup, delivery)
            )
            rows.append(
                {
                    "person_id": person,
                    "category": category,
                    "category_cn": CATEGORY_CN[category],
                    "aircraft_type": key[0],
                    "flight_no": key[1],
                    "pickup_stop_order": pickup,
                    "delivery_stop_order": delivery,
                    "t_pax": pax_time,
                    "pax_km": pax_km,
                    "stops_between": delivery - pickup - 1,
                }
            )
    return pd.DataFrame(rows)


def separated_breakdown(distances) -> pd.DataFrame:
    people = load_people_q2()
    groups = group_q2(people)
    routes, options = build_route_pool(groups, distances, pair_limit=700)
    routes_by_id = {route.route_id: route for route in routes}
    by_group: dict[str, list] = {group.group_id: [] for group in groups}
    for option in options:
        by_group[option.group_id].append(option)

    rows = []
    for group in groups:
        candidates = []
        for option in by_group[group.group_id]:
            route = routes_by_id[option.route_id]
            copies = math.ceil(group.quantity / route.capacity)
            candidates.append(
                (
                    copies * route.aircraft_time,
                    group.quantity * option.passenger_time,
                    copies * route.fuel_used,
                    copies,
                    -group.quantity * option.passenger_km / (copies * route.available_seat_km),
                    option.option_id,
                    route,
                    option,
                )
            )
        if not candidates:
            raise RuntimeError(f"separated baseline 未覆盖请求组 {group.group_id}")
        _, _, _, copies, _, _, route, option = min(candidates)
        category = category_of(group.origin_id, group.destination_id)
        rows.append(
            {
                "group_id": group.group_id,
                "category": category,
                "category_cn": CATEGORY_CN[category],
                "quantity": group.quantity,
                "t_pax": group.quantity * option.passenger_time,
                "t_air": copies * route.aircraft_time,
                "flights": copies,
                "pax_km": group.quantity * option.passenger_km,
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    distances = load_distances().distances
    joint = joint_breakdown(distances)
    separated = separated_breakdown(distances)

    def agg(frame, value_col: str):
        return (
            frame.groupby("category_cn")
            .agg(count=("category", "size"), value=(value_col, "sum"))
            .reindex(["出海", "海返", "穿梭"])
        )

    j = agg(joint, "t_pax")
    s = agg(separated, "t_pax")
    print("=== 人员总在途时间 T_pax 分类分解 ===")
    print(
        f"{'类别':<6}{'人数':>6}{'联合T_pax':>12}{'分离基线T_pax':>14}{'差值':>10}{'人均(联合)':>12}"
    )
    total_j = total_s = 0
    for cat in ["出海", "海返", "穿梭"]:
        jv, sv = int(j.loc[cat, "value"]), int(s.loc[cat, "value"])
        n = int(j.loc[cat, "count"])
        avg = jv / n if n else 0.0
        total_j += jv
        total_s += sv
        print(f"{cat:<6}{n:>6}{jv:>12}{sv:>14}{jv - sv:>10}{avg:>12.1f}")
    print(f"{'合计':<6}{len(joint):>6}{total_j:>12}{total_s:>14}{total_j - total_s:>10}")
    print()
    print("=== 联合方案绕行诊断 ===")
    detour = joint[joint["stops_between"] > 0]
    print(
        f"有中间停靠(绕行)的人员: {len(detour)}/{len(joint)} "
        f"({len(detour) / len(joint):.1%})"
    )
    out_path = Q2_OUT / "q2-tpax-by-category.csv"
    joint.to_csv(out_path, index=False)
    print(f"明细已写入 {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
