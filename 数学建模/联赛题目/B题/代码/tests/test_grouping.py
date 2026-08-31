from __future__ import annotations

import pandas as pd

from common.data_loader import load_people_q1, load_people_q2, load_people_q3
from common.grouping import group_q1, group_q2, group_q3


def test_q1_q2_group_only_by_od() -> None:
    frame = pd.DataFrame(
        [
            {"person_id": "P2", "origin_id": "LAND", "destination_id": "F001"},
            {"person_id": "P1", "origin_id": "LAND", "destination_id": "F001"},
            {"person_id": "P3", "origin_id": "A01", "destination_id": "F001"},
        ]
    )
    groups = group_q1(frame)
    assert len(groups) == 2
    assert groups[0].person_ids == ("P2", "P1")
    assert len(group_q2(frame)) == 2


def test_q3_group_uses_all_five_fields() -> None:
    base = {
        "origin_id": "LAND",
        "destination_id": "F001",
        "earliest_pickup_time": pd.Timestamp("2026-08-03 06:00"),
        "latest_arrival_time": pd.Timestamp("2026-08-03 10:00"),
        "task_type": "shift",
    }
    frame = pd.DataFrame(
        [
            dict(base, person_id="P1"),
            dict(base, person_id="P2"),
            dict(base, person_id="P3", task_type="temp"),
        ]
    )
    assert [group.quantity for group in group_q3(frame)] == [2, 1]


def test_real_group_counts() -> None:
    assert len(group_q1(load_people_q1())) == 104
    assert len(group_q2(load_people_q2())) == 264
    assert len(group_q3(load_people_q3())) == 1877
