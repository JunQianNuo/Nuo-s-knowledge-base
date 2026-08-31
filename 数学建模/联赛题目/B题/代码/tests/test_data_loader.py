from __future__ import annotations

import pandas as pd
import pytest

from common.data_loader import load_distances, load_people_q1, load_people_q2, load_people_q3


def test_real_data_are_readable() -> None:
    distances = load_distances()
    assert len(distances.locations) == 55
    assert distances.get("A01", "A02") == 35
    assert len(load_people_q1()) == 1600
    assert len(load_people_q2()) == 4000
    assert len(load_people_q3()) == 4000


def test_people_reject_duplicate_id(tmp_path) -> None:
    path = tmp_path / "peopleQ1.csv"
    pd.DataFrame(
        [
            {"person_id": "P1", "origin_id": "LAND", "destination_id": "F001"},
            {"person_id": "P1", "origin_id": "LAND", "destination_id": "F002"},
        ]
    ).to_csv(path, index=False)
    with pytest.raises(ValueError, match="重复 person_id"):
        load_people_q1(path)


def test_distance_rejects_negative_value(tmp_path) -> None:
    path = tmp_path / "distances.csv"
    pd.DataFrame({"from_id": ["A01"], "A01": [-1]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="负距离"):
        load_distances(path)
