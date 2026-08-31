"""Q1 架次复制次数与人员流的词典序整数规划主问题。"""

from __future__ import annotations

import math
import os
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Optional, Sequence

from ortools.sat.python import cp_model

from common.models import RequestGroup
from q1.algorithms.clusters import RouteColumn

_STAGE_NAMES = ("aircraft_time", "passenger_time", "fuel", "flights", "seat_utilization")


@dataclass(frozen=True)
class StageResult:
    name: str
    status: str
    objective: Optional[int]
    best_bound: Optional[float]
    gap: Optional[float]
    wall_time: float
    certified_optimal: bool
    conditioned_on_uncertified_parent: bool = False


@dataclass(frozen=True)
class FlowSolution:
    status: str
    stages: tuple[StageResult, ...]
    multiplicities: dict[str, int]
    flows: dict[tuple[str, str], int]
    aircraft_time: int
    passenger_time: int
    fuel: float
    flights: int
    passenger_km: float
    available_seat_km: float
    wall_time: float

    @property
    def seat_utilization(self) -> float:
        return self.passenger_km / self.available_seat_km if self.available_seat_km else 0.0

    @property
    def certified_primary_optimal(self) -> bool:
        return bool(self.stages) and self.stages[0].certified_optimal


def _integral_scale(values: Sequence[float], maximum_digits: int = 4) -> int:
    """求能把全部取值精确整数化的最小 10 次幂。"""
    scale = 1
    for _ in range(maximum_digits + 1):
        if all(math.isclose(value * scale, round(value * scale), abs_tol=1e-7) for value in values):
            return scale
        scale *= 10
    raise ValueError("存在无法精确整数化的系数")


class FlowMaster:
    """在固定候选航线池上求解 Q1 词典序主问题。"""

    def __init__(self, groups: Sequence[RequestGroup], columns: Sequence[RouteColumn]) -> None:
        self.groups = list(groups)
        self.columns = list(columns)
        self.group_index = {group.group_id: index for index, group in enumerate(self.groups)}
        self.column_index = {column.column_id: index for index, column in enumerate(self.columns)}

        by_destination: dict[str, list[RequestGroup]] = {}
        for group in self.groups:
            by_destination.setdefault(group.destination_id, []).append(group)

        # 每条航线可服务的请求组，以及该 (组, 航线) 对的到达时刻与累计距离。
        self.pairs: list[tuple[int, int]] = []
        self.arrival: list[int] = []
        self.cumulative: list[float] = []
        self.pairs_by_column: list[list[int]] = [[] for _ in self.columns]
        self.pairs_by_group: list[list[int]] = [[] for _ in self.groups]
        for column_position, column in enumerate(self.columns):
            for facility in column.cluster:
                for group in by_destination.get(facility, ()):
                    if group.origin_id != "LAND" and group.origin_id != column.base_airport:
                        continue
                    position = len(self.pairs)
                    group_position = self.group_index[group.group_id]
                    self.pairs.append((group_position, column_position))
                    self.arrival.append(column.arrival_minutes[facility])
                    self.cumulative.append(column.cumulative_distance[facility])
                    self.pairs_by_column[column_position].append(position)
                    self.pairs_by_group[group_position].append(position)

        missing = [
            self.groups[index].group_id
            for index, positions in enumerate(self.pairs_by_group)
            if not positions
        ]
        if missing:
            raise RuntimeError(f"候选航线池未覆盖请求组: {missing}")

        distance_scale = _integral_scale(
            [column.total_distance for column in self.columns] + self.cumulative
        )
        fuel_scale = _integral_scale([column.fuel_used for column in self.columns])
        self.distance_scale = distance_scale
        self.fuel_scale = fuel_scale
        self.time_coefficient = [column.aircraft_time for column in self.columns]
        self.fuel_coefficient = [round(column.fuel_used * fuel_scale) for column in self.columns]
        self.seat_km_coefficient = [
            round(column.available_seat_km * distance_scale) for column in self.columns
        ]
        self.pk_coefficient = [round(value * distance_scale) for value in self.cumulative]
        self.upper_bounds = [
            max(
                1,
                math.ceil(
                    sum(self.groups[self.pairs[p][0]].quantity for p in positions)
                    / self.columns[index].capacity
                ),
            )
            if positions
            else 0
            for index, positions in enumerate(self.pairs_by_column)
        ]
        # 由 LP 松弛得到的有效下界，作为割加入 CP-SAT，可大幅收紧对偶界；
        # upper_bounds 用于把已知最好解作为目标上界注入，避免重解时回退。
        self.lower_bounds: dict[str, int] = {}
        self.upper_bounds_by_metric: dict[str, int] = {}
        self.cardinality_cuts = self._cardinality_cuts()

    def _cardinality_cuts(self) -> list[tuple[tuple[int, ...], int]]:
        """架次数下界割：任意一组请求最多每架次运走 max_cap 人。

        对请求组集合 F，能服务 F 中任一组的航线集合记为 R(F)，则
            Σ_{r∈R(F)} y_r ≥ ⌈ Σ_{g∈F} q_g / max_{r∈R(F)} cap_r ⌉ 。
        取 F = 全体、F = 单个设施的全部组、F = 单个组，得到三族有效不等式。
        它们不被 LP 松弛蕴含（LP 只给出容量加权形式），能显著收紧对偶界。
        """
        cuts: list[tuple[tuple[int, ...], int]] = []
        families: list[list[int]] = [list(range(len(self.groups)))]
        by_destination: dict[str, list[int]] = {}
        for position, group in enumerate(self.groups):
            by_destination.setdefault(group.destination_id, []).append(position)
        families.extend(by_destination.values())
        families.extend([position] for position in range(len(self.groups)))
        seen: set[tuple[int, ...]] = set()
        for family in families:
            columns = sorted(
                {
                    self.pairs[position][1]
                    for member in family
                    for position in self.pairs_by_group[member]
                }
            )
            if not columns:
                continue
            key = tuple(columns)
            if key in seen:
                continue
            seen.add(key)
            demand = sum(self.groups[member].quantity for member in family)
            capacity = max(self.columns[index].capacity for index in columns)
            bound = math.ceil(demand / capacity)
            if bound > 1:
                cuts.append((key, bound))
        return cuts

    def _model(
        self,
        fixed: Mapping[str, int],
        objective: str,
        *,
        ratio: Optional[Fraction] = None,
        hint: Optional[tuple[dict[str, int], dict[tuple[str, str], int]]] = None,
    ) -> tuple[cp_model.CpModel, list, list]:
        model = cp_model.CpModel()
        y = [
            model.new_int_var(0, bound, f"y{index}")
            for index, bound in enumerate(self.upper_bounds)
        ]
        z = [
            model.new_int_var(
                0,
                min(
                    self.groups[group_position].quantity,
                    self.columns[column_position].capacity
                    * self.upper_bounds[column_position],
                ),
                f"z{position}",
            )
            for position, (group_position, column_position) in enumerate(self.pairs)
        ]
        for group_position, group in enumerate(self.groups):
            model.add(
                sum(z[position] for position in self.pairs_by_group[group_position])
                == group.quantity
            )
        for column_position, column in enumerate(self.columns):
            positions = self.pairs_by_column[column_position]
            if positions:
                model.add(
                    sum(z[position] for position in positions)
                    <= column.capacity * y[column_position]
                )
            else:
                model.add(y[column_position] == 0)

        for name, value in fixed.items():
            model.add(self._expression(name, y, z) == value)
        for name, value in self.lower_bounds.items():
            if name not in fixed:
                model.add(self._expression(name, y, z) >= value)
        for name, value in self.upper_bounds_by_metric.items():
            if name not in fixed:
                model.add(self._expression(name, y, z) <= value)
        for indices, bound in self.cardinality_cuts:
            model.add(sum(y[index] for index in indices) >= bound)

        if ratio is not None:
            model.maximize(
                sum(
                    ratio.denominator * coefficient * variable
                    for coefficient, variable in zip(self.pk_coefficient, z)
                )
                - sum(
                    ratio.numerator * coefficient * variable
                    for coefficient, variable in zip(self.seat_km_coefficient, y)
                )
            )
        else:
            model.minimize(self._expression(objective, y, z))

        if hint is not None:
            multiplicities, flows = hint
            for index, column in enumerate(self.columns):
                model.add_hint(y[index], multiplicities.get(column.column_id, 0))
            for position, (group_position, column_position) in enumerate(self.pairs):
                key = (
                    self.groups[group_position].group_id,
                    self.columns[column_position].column_id,
                )
                model.add_hint(z[position], flows.get(key, 0))
        return model, y, z

    def _expression(self, name: str, y: list, z: list):
        if name == "aircraft_time":
            return sum(c * v for c, v in zip(self.time_coefficient, y) if c)
        if name == "fuel":
            return sum(c * v for c, v in zip(self.fuel_coefficient, y) if c)
        if name == "flights":
            return sum(y)
        if name == "passenger_time":
            return sum(c * v for c, v in zip(self.arrival, z) if c)
        raise KeyError(name)

    def solve(
        self,
        *,
        time_limit_seconds: float = 120.0,
        workers: Optional[int] = None,
        deadline: Optional[float] = None,
        warm_start: Optional[FlowSolution] = None,
        dinkelbach_max_iterations: int = 12,
        stages: Sequence[str] = _STAGE_NAMES,
        seed: Optional[int] = None,
    ) -> FlowSolution:
        cpu = workers or max(1, min(os.cpu_count() or 1, 8))
        fixed: dict[str, int] = {}
        records: list[StageResult] = []
        hint = (
            (dict(warm_start.multiplicities), dict(warm_start.flows))
            if warm_start is not None
            else None
        )
        status = "UNKNOWN"
        y_values: list[int] = []
        z_values: list[int] = []

        for name in stages:
            if name == "seat_utilization":
                break
            budget = self._budget(time_limit_seconds, deadline)
            model, y, z = self._model(fixed, name, hint=hint)
            solver, status, y_values, z_values = self._run(model, y, z, budget, cpu, seed)
            if not y_values:
                return self._empty(status, records)
            objective = self._value(name, y_values, z_values)
            fixed[name] = objective
            hint = self._hint(y_values, z_values)
            records.append(
                StageResult(
                    name,
                    status,
                    objective,
                    solver.best_objective_bound,
                    abs(objective - solver.best_objective_bound) / max(1.0, abs(objective)),
                    solver.wall_time,
                    status == "OPTIMAL",
                    any(not record.certified_optimal for record in records),
                )
            )

        if "seat_utilization" in stages:
            ratio = Fraction(0)
            converged = False
            certified = all(record.certified_optimal for record in records)
            started = time.perf_counter()
            for _ in range(dinkelbach_max_iterations):
                budget = self._budget(time_limit_seconds, deadline)
                model, y, z = self._model(fixed, "pk", ratio=ratio, hint=hint)
                solver, status, candidate_y, candidate_z = self._run(model, y, z, budget, cpu, seed)
                if not candidate_y:
                    certified = False
                    break
                y_values, z_values = candidate_y, candidate_z
                hint = self._hint(y_values, z_values)
                certified = certified and status == "OPTIMAL"
                pk = sum(c * v for c, v in zip(self.pk_coefficient, z_values))
                ak = sum(c * v for c, v in zip(self.seat_km_coefficient, y_values))
                updated = Fraction(pk, ak) if ak else Fraction(0)
                if updated == ratio:
                    converged = True
                    break
                ratio = updated
            records.append(
                StageResult(
                    "seat_utilization",
                    status,
                    None,
                    None,
                    None,
                    time.perf_counter() - started,
                    certified and converged,
                    any(not record.certified_optimal for record in records),
                )
            )

        return self._solution(status, records, y_values, z_values)

    def _budget(self, limit: float, deadline: Optional[float]) -> float:
        if deadline is None:
            return limit
        return min(limit, max(0.05, deadline - time.perf_counter()))

    def _run(self, model, y, z, budget: float, workers: int, seed: Optional[int] = None):
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = budget
        solver.parameters.num_search_workers = workers
        if seed is not None:
            solver.parameters.random_seed = seed
        code = solver.solve(model)
        status = solver.status_name(code)
        if code not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return solver, status, [], []
        return (
            solver,
            status,
            [solver.value(variable) for variable in y],
            [solver.value(variable) for variable in z],
        )

    def _value(self, name: str, y_values: list[int], z_values: list[int]) -> int:
        if name == "aircraft_time":
            return sum(c * v for c, v in zip(self.time_coefficient, y_values))
        if name == "fuel":
            return sum(c * v for c, v in zip(self.fuel_coefficient, y_values))
        if name == "flights":
            return sum(y_values)
        if name == "passenger_time":
            return sum(c * v for c, v in zip(self.arrival, z_values))
        raise KeyError(name)

    def _hint(self, y_values, z_values):
        multiplicities = {
            column.column_id: value
            for column, value in zip(self.columns, y_values)
            if value
        }
        flows = {
            (self.groups[g].group_id, self.columns[r].column_id): z_values[position]
            for position, (g, r) in enumerate(self.pairs)
            if z_values[position]
        }
        return multiplicities, flows

    def _empty(self, status: str, records: list[StageResult]) -> FlowSolution:
        return FlowSolution(
            status, tuple(records), {}, {}, 0, 0, 0.0, 0, 0.0, 0.0,
            sum(record.wall_time for record in records),
        )

    def _solution(self, status, records, y_values, z_values) -> FlowSolution:
        multiplicities, flows = self._hint(y_values, z_values)
        return FlowSolution(
            status=status,
            stages=tuple(records),
            multiplicities=multiplicities,
            flows=flows,
            aircraft_time=self._value("aircraft_time", y_values, z_values),
            passenger_time=self._value("passenger_time", y_values, z_values),
            fuel=self._value("fuel", y_values, z_values) / self.fuel_scale,
            flights=self._value("flights", y_values, z_values),
            passenger_km=sum(c * v for c, v in zip(self.pk_coefficient, z_values))
            / self.distance_scale,
            available_seat_km=sum(c * v for c, v in zip(self.seat_km_coefficient, y_values))
            / self.distance_scale,
            wall_time=sum(record.wall_time for record in records),
        )

    def linear_relaxation_bound(self, time_limit_seconds: float = 60.0) -> Optional[float]:
        """候选池上 T_air 的 LP 松弛下界（只对本候选池有效，不是全局下界）。"""
        from ortools.linear_solver import pywraplp

        solver = pywraplp.Solver.CreateSolver("GLOP")
        if solver is None:
            return None
        solver.set_time_limit(int(time_limit_seconds * 1000))
        y = [solver.NumVar(0, bound, "") for bound in self.upper_bounds]
        z = [solver.NumVar(0, solver.infinity(), "") for _ in self.pairs]
        for group_position, group in enumerate(self.groups):
            solver.Add(
                sum(z[position] for position in self.pairs_by_group[group_position])
                == group.quantity
            )
        for column_position, column in enumerate(self.columns):
            positions = self.pairs_by_column[column_position]
            if positions:
                solver.Add(
                    sum(z[position] for position in positions)
                    <= column.capacity * y[column_position]
                )
        for indices, bound in self.cardinality_cuts:
            solver.Add(sum(y[index] for index in indices) >= bound)
        solver.Minimize(sum(c * v for c, v in zip(self.time_coefficient, y)))
        if solver.Solve() != pywraplp.Solver.OPTIMAL:
            return None
        return solver.Objective().Value()
