from __future__ import annotations

import time
from dataclasses import replace
from datetime import datetime

import pytest

from common.models import RequestGroup
from q3.algorithms.master import StageAMaster
from q3.algorithms.realize import realize_stage_a
from q3.algorithms.timed_pool import ServiceOption
from q3.tests.test_q3_foundation import _column


def _group(quantity=12, task="shift"):
    return RequestGroup(
        "G",
        tuple(f"P{i}" for i in range(quantity)),
        "LAND",
        "F001",
        datetime(2026, 8, 3, 6),
        datetime(2026, 8, 3, 20),
        task,
    )


def _option(column, group_id="G", pickup=0, delivery=1):
    return ServiceOption(
        f"{group_id}@{column.column_id}",
        group_id,
        column.column_id,
        pickup,
        delivery,
        column.arrival_times[delivery] - column.departure_times[pickup],
        20.0,
    )


def test_mandatory_exact_coverage_dynamic_capacity_and_parallel_copies():
    group = _group(24)
    column = _column()
    solution = StageAMaster([group], [column], [_option(column)]).solve(time.perf_counter() + 10, 1)
    assert solution.status == "OPTIMAL"
    assert sum(solution.flows.values()) == 24
    assert len(solution.aircraft_by_column[column.column_id]) == 2


def test_zero_option_rejected_before_solve():
    with pytest.raises(RuntimeError, match="zero-option"):
        StageAMaster([_group()], [_column()], [])


def test_no_overlap_and_exact_30_minute_turnaround():
    group = _group(24)
    first = _column()
    second = replace(_column(start=first.return_time + 30), column_id="C2")
    options = [_option(first), _option(second)]
    solution = StageAMaster([group], [first, second], options).solve(time.perf_counter() + 10, 1)
    assert solution.status == "OPTIMAL"


def test_incompatible_aircraft_has_no_assignment_and_restricted_bound_name():
    column = _column()
    solution = StageAMaster([_group()], [column], [_option(column)]).solve(
        time.perf_counter() + 10, 1
    )
    selected = set(solution.aircraft_by_column[column.column_id])
    assert selected and all(value.startswith("A01-T1-") for value in selected)
    assert solution.restricted_pool_bound is not None
    assert not hasattr(solution, "global_lower_bound")


def test_interval_decomposition_and_solver_delivery_metrics():
    group = _group(24)
    column = _column()
    option = _option(column)
    solution = StageAMaster([group], [column], [option]).solve(time.perf_counter() + 10, 1)
    flights, assignments = realize_stage_a([group], [column], [option], solution)
    assert len(flights) == solution.flights == 2
    assert len(assignments) == sum(solution.flows.values()) == 24
    assert sum(len(flight.passengers) for flight in flights) == 24


def test_temporary_is_not_part_of_stage_a_demand():
    mandatory = _group(1)
    temporary = replace(_group(7, "temporary"), group_id="T")
    column = _column()
    solution = StageAMaster([mandatory], [column], [_option(column)]).solve(
        time.perf_counter() + 10, 1
    )
    assert sum(solution.flows.values()) == mandatory.quantity
    assert temporary.group_id not in {option.group_id for option in [_option(column)]}


def test_stage_b_optional_temporary_and_budget_boundary():
    mandatory = _group(12)
    temporary = replace(_group(12, "temporary"), group_id="T")
    column = _column()
    options = [_option(column), _option(column, "T")]
    master = StageAMaster([mandatory, temporary], [column], options, {"T"})
    solution = master.solve(
        time.perf_counter() + 10,
        1,
        {"T"},
        column.aircraft_time,
    )
    assert solution.status == "OPTIMAL"
    assert solution.aircraft_time == column.aircraft_time
    assert solution.temporary_served == 0  # mandatory already fills the shared leg.


def test_stage_b_zero_extra_time_insertion_and_over_budget_forbidden():
    mandatory = _group(1)
    temporary = replace(_group(1, "temporary"), group_id="T")
    column = _column()
    options = [_option(column), _option(column, "T")]
    master = StageAMaster([mandatory, temporary], [column], options, {"T"})
    feasible = master.solve(time.perf_counter() + 10, 1, {"T"}, column.aircraft_time)
    assert feasible.temporary_served == 1
    forbidden = master.solve(time.perf_counter() + 10, 1, {"T"}, column.aircraft_time - 1)
    assert forbidden.status == "INFEASIBLE"
