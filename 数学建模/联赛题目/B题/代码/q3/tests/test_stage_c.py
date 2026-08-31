from __future__ import annotations

import time
from dataclasses import replace

from q3.algorithms.lex import StageCLexMaster
from q3.tests.test_q3_foundation import _column
from q3.tests.test_stage_a import _group, _option


def test_stage_c_exact_temporary_lex_and_uncertified_parent():
    mandatory = _group(1)
    temporary = replace(_group(1, "temporary"), group_id="T")
    column = _column()
    options = [_option(column), _option(column, "T")]
    hint = ({column.column_id: ("A01-T1-H01",)}, {o.option_id: 1 for o in options})
    solution = StageCLexMaster(
        [mandatory, temporary],
        [column],
        options,
        {"T"},
        temporary_served=1,
        budget=column.aircraft_time,
    ).solve_lex(time.perf_counter() + 10, 1, hint, parent_certified=False)
    assert solution.aircraft_time == column.aircraft_time
    assert solution.flights == 1
    assert solution.utilization == 2 * 20 / (column.capacity * column.distance)
    assert not solution.full_certified
    assert all(stage.conditioned_on_uncertified_parent for stage in solution.stages)


def test_stage_c_shared_deadline_returns_legal_incumbent():
    mandatory = _group(1)
    column = _column()
    option = _option(column)
    hint = ({column.column_id: ("A01-T1-H01",)}, {option.option_id: 1})
    solution = StageCLexMaster(
        [mandatory],
        [column],
        [option],
        set(),
        temporary_served=0,
        budget=column.aircraft_time,
    ).solve_lex(time.perf_counter() + 2, 1, hint)
    assert solution.aircraft_time == column.aircraft_time
