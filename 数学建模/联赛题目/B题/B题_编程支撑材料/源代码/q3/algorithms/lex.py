from __future__ import annotations

import time
from dataclasses import dataclass
from fractions import Fraction

from ortools.sat.python import cp_model

from q2.algorithms.master import StageResult, _scale
from q3.algorithms.master import StageAMaster
from q3.fleet import FLEET


@dataclass(frozen=True)
class StageCSolution:
    status: str
    stages: tuple[StageResult, ...]
    aircraft_by_column: dict[str, tuple[str, ...]]
    flows: dict[str, int]
    aircraft_time: int
    passenger_time: int
    fuel: float
    flights: int
    passenger_km: float
    available_seat_km: float
    wall_time: float
    dinkelbach_iterations: int

    @property
    def utilization(self):
        return self.passenger_km / self.available_seat_km

    @property
    def full_certified(self):
        return len(self.stages) == 5 and all(stage.certified_optimal for stage in self.stages)


class StageCLexMaster(StageAMaster):
    def __init__(self, groups, columns, options, temporary_ids, *, temporary_served, budget):
        super().__init__(groups, columns, options, temporary_ids)
        self.temporary_ids = frozenset(temporary_ids)
        self.temporary_served = temporary_served
        self.budget = budget
        self.fuel_scale = _scale([column.fuel_used for column in self.columns])
        self.distance_scale = _scale(
            [column.capacity * column.distance for column in self.columns]
            + [option.passenger_distance for option in self.options]
        )

    def _build(self, fixed, objective, hint, ratio=None):
        model = cp_model.CpModel()
        x, intervals = {}, {aircraft.aircraft_id: [] for aircraft in FLEET}
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
        for values in intervals.values():
            model.add_no_overlap(values)
        y = [
            sum(x[(ri, aircraft_id)] for aircraft_id in column.compatible_aircraft_ids)
            for ri, column in enumerate(self.columns)
        ]
        z = [
            model.new_int_var(0, self.groups[self.group_pos[o.group_id]].quantity, f"z_{i}")
            for i, o in enumerate(self.options)
        ]
        for gi, group in enumerate(self.groups):
            demand = sum(z[i] for i in self.by_group[gi])
            model.add(
                demand <= group.quantity
                if group.group_id in self.temporary_ids
                else demand == group.quantity
            )
        model.add(
            sum(
                z[i]
                for i, option in enumerate(self.options)
                if option.group_id in self.temporary_ids
            )
            == self.temporary_served
        )
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
        expressions = {
            "aircraft_time": sum(c.aircraft_time * y[i] for i, c in enumerate(self.columns)),
            "passenger_time": sum(o.passenger_time * z[i] for i, o in enumerate(self.options)),
            "fuel": sum(
                round(c.fuel_used * self.fuel_scale) * y[i] for i, c in enumerate(self.columns)
            ),
            "flights": sum(y),
        }
        model.add(expressions["aircraft_time"] <= self.budget)
        for name, value in fixed.items():
            model.add(expressions[name] == value)
        pk = sum(
            round(o.passenger_distance * self.distance_scale) * z[i]
            for i, o in enumerate(self.options)
        )
        ak = sum(
            round(c.capacity * c.distance * self.distance_scale) * y[i]
            for i, c in enumerate(self.columns)
        )
        if ratio is None:
            model.minimize(expressions[objective])
        else:
            model.maximize(ratio.denominator * pk - ratio.numerator * ak)
        hint_aircraft, hint_flows = hint
        for (ri, aircraft_id), variable in x.items():
            model.add_hint(
                variable, int(aircraft_id in hint_aircraft.get(self.columns[ri].column_id, ()))
            )
        for i, option in enumerate(self.options):
            model.add_hint(z[i], hint_flows.get(option.option_id, 0))
        return model, x, y, z, expressions, pk, ak

    def solve_lex(self, deadline, workers, hint, parent_certified=False, seed=None):
        fixed, records, incumbent = {}, [], None
        status, iterations = "UNKNOWN", 0
        names = ("aircraft_time", "passenger_time", "fuel", "flights")
        for position, name in enumerate(names):
            remaining = deadline - time.perf_counter()
            if remaining <= 0.1:
                break
            model, x, y, z, expressions, _, _ = self._build(fixed, name, hint)
            solver = cp_model.CpSolver()
            solver.parameters.max_time_in_seconds = max(0.1, remaining / (5 - position))
            solver.parameters.num_search_workers = workers
            if seed is not None:
                solver.parameters.random_seed = seed
            code = solver.solve(model)
            status = solver.status_name(code)
            if code not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
                break
            incumbent = self._extract(solver, x, y, z)
            value = (
                sum(
                    (c.aircraft_time if name == "aircraft_time" else 1) * incumbent[2][i]
                    for i, c in enumerate(self.columns)
                )
                if name in ("aircraft_time", "flights")
                else int(solver.value(expressions[name]))
            )
            fixed[name] = value
            hint = (incumbent[0], incumbent[1])
            conditioned = (not parent_certified) or any(
                not record.certified_optimal for record in records
            )
            records.append(
                StageResult(
                    name,
                    status,
                    value,
                    solver.best_objective_bound,
                    solver.wall_time,
                    status == "OPTIMAL",
                    conditioned,
                )
            )
        ratio, converged = Fraction(0), False
        if incumbent is not None and len(records) == 4:
            started = time.perf_counter()
            bound = None
            while iterations < 12 and deadline - time.perf_counter() > 0.1:
                iterations += 1
                model, x, y, z, _, pk, ak = self._build(fixed, "flights", hint, ratio)
                solver = cp_model.CpSolver()
                solver.parameters.max_time_in_seconds = max(0.1, deadline - time.perf_counter())
                solver.parameters.num_search_workers = workers
                if seed is not None:
                    solver.parameters.random_seed = seed
                code = solver.solve(model)
                status, bound = solver.status_name(code), solver.best_objective_bound
                if code not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
                    break
                incumbent = self._extract(solver, x, y, z)
                hint = (incumbent[0], incumbent[1])
                updated = Fraction(solver.value(pk), solver.value(ak))
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
                    parent_certified
                    and all(record.certified_optimal for record in records)
                    and converged
                    and status == "OPTIMAL",
                    (not parent_certified)
                    or any(not record.certified_optimal for record in records),
                )
            )
        return self._solution(status, records, incumbent, iterations)

    def _extract(self, solver, x, y, z):
        aircraft = {
            column.column_id: tuple(
                aid for aid in column.compatible_aircraft_ids if solver.value(x[(ri, aid)])
            )
            for ri, column in enumerate(self.columns)
            if solver.value(y[ri])
        }
        flows = {
            o.option_id: solver.value(z[i])
            for i, o in enumerate(self.options)
            if solver.value(z[i])
        }
        return (
            aircraft,
            flows,
            [solver.value(value) for value in y],
            [solver.value(value) for value in z],
        )

    def _solution(self, status, records, incumbent, iterations):
        if incumbent is None:
            raise RuntimeError("Stage C failed before producing an incumbent")
        aircraft, flows, y, z = incumbent
        return StageCSolution(
            status,
            tuple(records),
            aircraft,
            flows,
            sum(c.aircraft_time * y[i] for i, c in enumerate(self.columns)),
            sum(o.passenger_time * z[i] for i, o in enumerate(self.options)),
            sum(c.fuel_used * y[i] for i, c in enumerate(self.columns)),
            sum(y),
            sum(o.passenger_distance * z[i] for i, o in enumerate(self.options)),
            sum(c.capacity * c.distance * y[i] for i, c in enumerate(self.columns)),
            sum(record.wall_time for record in records),
            iterations,
        )
