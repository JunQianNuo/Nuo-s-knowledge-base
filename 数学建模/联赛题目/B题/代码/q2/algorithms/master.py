from __future__ import annotations

import math
import os
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Optional, Sequence

from ortools.sat.python import cp_model

from common.models import RequestGroup
from q2.algorithms.route_pool import PhysicalRoute, ServiceOption


@dataclass(frozen=True)
class StageResult:
    name: str
    status: str
    objective: Optional[int]
    best_bound: Optional[float]
    wall_time: float
    certified_optimal: bool
    conditioned_on_uncertified_parent: bool


@dataclass(frozen=True)
class MasterSolution:
    status: str
    stages: tuple[StageResult, ...]
    multiplicities: dict[str, int]
    flows: dict[str, int]
    aircraft_time: int
    passenger_time: int
    fuel: float
    flights: int
    passenger_km: float
    available_seat_km: float
    wall_time: float

    @property
    def utilization(self) -> float:
        return self.passenger_km / self.available_seat_km if self.available_seat_km else 0.0

    @property
    def full_certified(self) -> bool:
        return len(self.stages) == 5 and all(stage.certified_optimal for stage in self.stages)


def _scale(values: Sequence[float]) -> int:
    for scale in (1, 10, 100, 1000, 10000):
        if all(math.isclose(value * scale, round(value * scale), abs_tol=1e-7) for value in values):
            return scale
    raise ValueError("系数无法安全整数化")


class RouteFlowMaster:
    def __init__(
        self,
        groups: Sequence[RequestGroup],
        routes: Sequence[PhysicalRoute],
        options: Sequence[ServiceOption],
    ):
        self.groups = list(groups)
        self.routes = list(routes)
        self.options = list(options)
        self.group_pos = {g.group_id: i for i, g in enumerate(self.groups)}
        self.route_pos = {r.route_id: i for i, r in enumerate(self.routes)}
        self.by_group = [[] for _ in self.groups]
        self.by_route = [[] for _ in self.routes]
        for i, option in enumerate(self.options):
            self.by_group[self.group_pos[option.group_id]].append(i)
            self.by_route[self.route_pos[option.route_id]].append(i)
        missing = [g.group_id for i, g in enumerate(self.groups) if not self.by_group[i]]
        if missing:
            raise RuntimeError(f"无 service option 的请求组: {missing}")
        self.fuel_scale = _scale([r.fuel_used for r in self.routes])
        self.distance_scale = _scale(
            [r.available_seat_km for r in self.routes] + [o.passenger_km for o in self.options]
        )
        total = sum(group.quantity for group in self.groups)
        self.y_ub = [
            max(1, math.ceil(total / route.capacity)) if self.by_route[i] else 0
            for i, route in enumerate(self.routes)
        ]

    def _build(
        self,
        fixed: dict[str, int],
        objective: str,
        ratio: Optional[Fraction] = None,
        hint=None,
    ):
        model = cp_model.CpModel()
        y = [model.new_int_var(0, upper, f"y{i}") for i, upper in enumerate(self.y_ub)]
        z = [
            model.new_int_var(0, self.groups[self.group_pos[o.group_id]].quantity, f"z{i}")
            for i, o in enumerate(self.options)
        ]
        for group_i, group in enumerate(self.groups):
            model.add(sum(z[i] for i in self.by_group[group_i]) == group.quantity)
        for route_i, route in enumerate(self.routes):
            positions = self.by_route[route_i]
            if not positions:
                model.add(y[route_i] == 0)
                continue
            for leg in range(len(route.route) - 1):
                active = [
                    i for i in positions if self.options[i].pickup <= leg < self.options[i].delivery
                ]
                if active:
                    model.add(sum(z[i] for i in active) <= route.capacity * y[route_i])
            model.add(y[route_i] <= sum(z[i] for i in positions))
        for name, value in fixed.items():
            model.add(self._expr(name, y, z) == value)
        if ratio is None:
            model.minimize(self._expr(objective, y, z))
        else:
            pk = sum(
                round(o.passenger_km * self.distance_scale) * z[i]
                for i, o in enumerate(self.options)
            )
            ak = sum(
                round(r.available_seat_km * self.distance_scale) * y[i]
                for i, r in enumerate(self.routes)
            )
            model.maximize(ratio.denominator * pk - ratio.numerator * ak)
        if hint:
            counts, flows = hint
            for i, route in enumerate(self.routes):
                model.add_hint(y[i], counts.get(route.route_id, 0))
            for i, option in enumerate(self.options):
                model.add_hint(z[i], flows.get(option.option_id, 0))
        return model, y, z

    def _expr(self, name, y, z):
        if name == "aircraft_time":
            return sum(r.aircraft_time * y[i] for i, r in enumerate(self.routes))
        if name == "passenger_time":
            return sum(o.passenger_time * z[i] for i, o in enumerate(self.options))
        if name == "fuel":
            return sum(
                round(r.fuel_used * self.fuel_scale) * y[i] for i, r in enumerate(self.routes)
            )
        if name == "flights":
            return sum(y)
        raise KeyError(name)

    def _values(self, name, y, z):
        if name == "aircraft_time":
            return sum(r.aircraft_time * y[i] for i, r in enumerate(self.routes))
        if name == "passenger_time":
            return sum(o.passenger_time * z[i] for i, o in enumerate(self.options))
        if name == "fuel":
            return sum(
                round(r.fuel_used * self.fuel_scale) * y[i] for i, r in enumerate(self.routes)
            )
        if name == "flights":
            return sum(y)
        raise KeyError(name)

    def solve(
        self,
        *,
        deadline: float,
        workers: Optional[int] = None,
        stages=("aircraft_time", "passenger_time", "fuel", "flights", "seat_utilization"),
        seed: Optional[int] = None,
        primary_time_limit_seconds: float = 700.0,
        secondary_time_limit_seconds: float = 300.0,
    ) -> MasterSolution:
        fixed: dict[str, int] = {}
        records = []
        yv: list[int] = []
        zv: list[int] = []
        hint = None
        status = "UNKNOWN"
        cpu = workers or min(8, os.cpu_count() or 1)

        def _budget(name: str) -> float:
            limit = (
                primary_time_limit_seconds
                if name == "aircraft_time"
                else secondary_time_limit_seconds
            )
            return min(limit, max(0.05, deadline - time.perf_counter()))

        for name in stages:
            if name == "seat_utilization":
                break
            budget = _budget(name)
            if budget <= 0.05:
                break
            model, y, z = self._build(fixed, name, hint=hint)
            solver = cp_model.CpSolver()
            solver.parameters.max_time_in_seconds = budget
            solver.parameters.num_search_workers = cpu
            if seed is not None:
                solver.parameters.random_seed = seed
            code = solver.solve(model)
            status = solver.status_name(code)
            if code not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                break
            yv = [solver.value(v) for v in y]
            zv = [solver.value(v) for v in z]
            value = self._values(name, yv, zv)
            fixed[name] = value
            hint = self._hint(yv, zv)
            records.append(
                StageResult(
                    name,
                    status,
                    value,
                    solver.best_objective_bound,
                    solver.wall_time,
                    status == "OPTIMAL",
                    any(not r.certified_optimal for r in records),
                )
            )
        if "seat_utilization" in stages and yv and deadline - time.perf_counter() > 0.05:
            started = time.perf_counter()
            ratio = Fraction(0)
            converged = False
            certified = all(r.certified_optimal for r in records)
            bound = None
            for _ in range(12):
                remaining = deadline - time.perf_counter()
                if remaining <= 0.05:
                    certified = False
                    break
                model, y, z = self._build(fixed, "ratio", ratio, hint)
                solver = cp_model.CpSolver()
                solver.parameters.max_time_in_seconds = min(
                    secondary_time_limit_seconds, max(0.05, remaining)
                )
                solver.parameters.num_search_workers = cpu
                if seed is not None:
                    solver.parameters.random_seed = seed
                code = solver.solve(model)
                status = solver.status_name(code)
                if code not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                    certified = False
                    break
                yv, zv = [solver.value(v) for v in y], [solver.value(v) for v in z]
                hint = self._hint(yv, zv)
                pk = sum(
                    round(o.passenger_km * self.distance_scale) * zv[i]
                    for i, o in enumerate(self.options)
                )
                ak = sum(
                    round(r.available_seat_km * self.distance_scale) * yv[i]
                    for i, r in enumerate(self.routes)
                )
                updated = Fraction(pk, ak) if ak else Fraction(0)
                bound = solver.best_objective_bound
                certified = certified and status == "OPTIMAL"
                if updated == ratio:
                    converged = True
                    break
                ratio = updated
            records.append(
                StageResult(
                    "seat_utilization",
                    status,
                    None,
                    bound,
                    time.perf_counter() - started,
                    certified and converged,
                    any(not r.certified_optimal for r in records),
                )
            )
        if not yv:
            return MasterSolution(
                status,
                tuple(records),
                {},
                {},
                0,
                0,
                0.0,
                0,
                0.0,
                0.0,
                sum(r.wall_time for r in records),
            )
        return self._solution(status, records, yv, zv)

    def _hint(self, yv, zv):
        return (
            {r.route_id: yv[i] for i, r in enumerate(self.routes) if yv[i]},
            {o.option_id: zv[i] for i, o in enumerate(self.options) if zv[i]},
        )

    def _solution(self, status, records, yv, zv):
        counts, flows = self._hint(yv, zv)
        return MasterSolution(
            status,
            tuple(records),
            counts,
            flows,
            self._values("aircraft_time", yv, zv),
            self._values("passenger_time", yv, zv),
            self._values("fuel", yv, zv) / self.fuel_scale,
            self._values("flights", yv, zv),
            sum(o.passenger_km * zv[i] for i, o in enumerate(self.options)),
            sum(r.available_seat_km * yv[i] for i, r in enumerate(self.routes)),
            sum(r.wall_time for r in records),
        )
