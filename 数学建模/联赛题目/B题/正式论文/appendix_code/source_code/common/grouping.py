from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from .models import RequestGroup


def _group(frame: pd.DataFrame, keys: list[str], prefix: str) -> list[RequestGroup]:
    groups: list[RequestGroup] = []
    grouped = frame.groupby(keys, sort=False, dropna=False)
    for index, (values, rows) in enumerate(grouped, start=1):
        key_values = values if isinstance(values, tuple) else (values,)
        record = dict(zip(keys, key_values))
        groups.append(
            RequestGroup(
                group_id=f"{prefix}{index:04d}",
                person_ids=tuple(rows["person_id"].astype(str)),
                origin_id=str(record["origin_id"]),
                destination_id=str(record["destination_id"]),
                earliest_pickup_time=_python_datetime(record.get("earliest_pickup_time")),
                latest_arrival_time=_python_datetime(record.get("latest_arrival_time")),
                task_type=_optional_string(record.get("task_type")),
            )
        )
    return groups


def _python_datetime(value: object):
    if value is None:
        return None
    return pd.Timestamp(value).to_pydatetime()


def _optional_string(value: object):
    return None if value is None else str(value)


def group_q1(frame: pd.DataFrame) -> list[RequestGroup]:
    return _group(frame, ["origin_id", "destination_id"], "Q1G")


def group_q2(frame: pd.DataFrame) -> list[RequestGroup]:
    return _group(frame, ["origin_id", "destination_id"], "Q2G")


def group_q3(frame: pd.DataFrame) -> list[RequestGroup]:
    return _group(
        frame,
        [
            "origin_id",
            "destination_id",
            "earliest_pickup_time",
            "latest_arrival_time",
            "task_type",
        ],
        "Q3G",
    )


def index_groups(groups: Iterable[RequestGroup]) -> dict[str, RequestGroup]:
    return {group.group_id: group for group in groups}
