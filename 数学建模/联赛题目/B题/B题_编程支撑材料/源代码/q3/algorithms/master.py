from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Optional, Sequence

from ortools.sat.python import cp_model

from common.models import RequestGroup
from q3.fleet import FLEET


@dataclass(frozen=True)
class StageASolution:
    status: str
    restricted_pool_bound: Optional[float]
    aircraft_by_column: dict[str, tuple[str, ...]]
    flows: dict[str, int]
    aircraft_time: int
    passenger_time: int
    fuel: float
    flights: int
    passenger_km: float
    available_seat_km: float
    wall_time: float
    temporary_served: int = 0


class StageAMaster:
    def __init__(self, groups: Sequence[RequestGroup], columns, options, optional_group_ids=()):
        self.groups, self.columns, self.options = list(groups), list(columns), list(options)
        self.group_pos = {g.group_id: i for i, g in enumerate(self.groups)}
        self.column_pos = {r.column_id: i for i, r in enumerate(self.columns)}
        self.by_group = [[] for _ in self.groups]
        self.by_column = [[] for _ in self.columns]
        for i, option in enumerate(self.options):
            self.by_group[self.group_pos[option.group_id]].append(i)
            self.by_column[self.column_pos[option.column_id]].append(i)
        optional_group_ids = frozenset(optional_group_ids)
        missing = [
            g.group_id
            for i, g in enumerate(self.groups)
            if not self.by_group[i] and g.group_id not in optional_group_ids
        ]
        if missing:
            raise RuntimeError(f"zero-option mandatory groups: {missing[:20]}")

    def solve(
        self,
        deadline: float,
        workers: int = 8,
        temporary_group_ids=(),
        aircraft_time_budget: Optional[int] = None,
        hint_aircraft_by_column=None,
        hint_flows=None,
        seed: Optional[int] = None,
    ) -> StageASolution:
        temporary_group_ids = frozenset(temporary_group_ids)
        model = cp_model.CpModel()
        x = {}
        intervals = {aircraft.aircraft_id: [] for aircraft in FLEET}
        for ri, column in enumerate(self.columns):
            for aircraft_id in column.compatible_aircraft_ids:
                variable = model.new_bool_var(f"x_{ri}_{aircraft_id}")
                x[(ri, aircraft_id)] = variable
                intervals[aircraft_id].append(
                    model.new_optional_fixed_size_interval_var(
                        column.departure_time,
                        column.aircraft_time + 30,
                        variable,
                        f"i_{ri}_{aircraft_id}",
                    )
                )
        for aircraft_intervals in intervals.values():
            model.add_no_overlap(aircraft_intervals)
        y = [
            sum(x[(ri, a)] for a in column.compatible_aircraft_ids)
            for ri, column in enumerate(self.columns)
        ]
        z = [
            model.new_int_var(0, self.groups[self.group_pos[o.group_id]].quantity, f"z_{i}")
            for i, o in enumerate(self.options)
        ]
        hint_aircraft_by_column = hint_aircraft_by_column or {}
        hint_flows = hint_flows or {}
        for (ri, aircraft_id), variable in x.items():
            model.add_hint(
                variable,
                int(aircraft_id in hint_aircraft_by_column.get(self.columns[ri].column_id, ())),
            )
        for i, option in enumerate(self.options):
            model.add_hint(z[i], hint_flows.get(option.option_id, 0))
        for gi, group in enumerate(self.groups):
            demand = sum(z[i] for i in self.by_group[gi])
            if group.group_id in temporary_group_ids:
                model.add(demand <= group.quantity)
            else:
                model.add(demand == group.quantity)
        for ri, column in enumerate(self.columns):
            for leg in range(len(column.route) - 1):
                active = [
                    i
                    for i in self.by_column[ri]
                    if self.options[i].pickup <= leg < self.options[i].delivery
                ]
                if active:
                    model.add(sum(z[i] for i in active) <= column.capacity * y[ri])
            model.add(y[ri] <= sum(z[i] for i in self.by_column[ri]))
        aircraft_time = sum(column.aircraft_time * y[i] for i, column in enumerate(self.columns))
        if aircraft_time_budget is None:
            model.minimize(aircraft_time)
        else:
            model.add(aircraft_time <= aircraft_time_budget)
            model.maximize(
                sum(
                    z[i]
                    for i, option in enumerate(self.options)
                    if option.group_id in temporary_group_ids
                )
            )
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = max(0.05, deadline - time.perf_counter())
        solver.parameters.num_search_workers = workers
        if seed is not None:
            solver.parameters.random_seed = seed
        code = solver.solve(model)
        status = solver.status_name(code)
        if code not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
            return StageASolution(
                status, solver.best_objective_bound, {}, {}, 0, 0, 0, 0, 0, 0, solver.wall_time
            )
        selected = {
            column.column_id: tuple(
                aircraft_id
                for aircraft_id in column.compatible_aircraft_ids
                if solver.value(x[(ri, aircraft_id)])
            )
            for ri, column in enumerate(self.columns)
            if any(solver.value(x[(ri, a)]) for a in column.compatible_aircraft_ids)
        }
        flows = {
            o.option_id: solver.value(z[i])
            for i, o in enumerate(self.options)
            if solver.value(z[i])
        }
        count = {column_id: len(ids) for column_id, ids in selected.items()}
        return StageASolution(
            status,
            solver.best_objective_bound,
            selected,
            flows,
            sum(r.aircraft_time * count.get(r.column_id, 0) for r in self.columns),
            sum(o.passenger_time * flows.get(o.option_id, 0) for o in self.options),
            sum(r.fuel_used * count.get(r.column_id, 0) for r in self.columns),
            sum(count.values()),
            sum(o.passenger_distance * flows.get(o.option_id, 0) for o in self.options),
            sum(r.capacity * r.distance * count.get(r.column_id, 0) for r in self.columns),
            solver.wall_time,
            sum(
                solver.value(z[i])
                for i, option in enumerate(self.options)
                if option.group_id in temporary_group_ids
            ),
        )
