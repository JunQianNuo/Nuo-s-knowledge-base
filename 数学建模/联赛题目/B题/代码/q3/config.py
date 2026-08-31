from __future__ import annotations

from datetime import datetime, timedelta

HORIZON_START = datetime(2026, 8, 3)
HORIZON_DAYS = 7
MANDATORY_TASKS = frozenset({"shift", "production", "emergency"})
TEMPORARY_TASK = "temporary"


def datetime_to_minute(value: datetime) -> int:
    delta = value - HORIZON_START
    minute = int(delta.total_seconds() // 60)
    if delta.total_seconds() != minute * 60:
        raise ValueError("Q3 时刻必须精确到整分钟")
    return minute


def minute_to_datetime(minute: int) -> datetime:
    if not isinstance(minute, int):
        raise TypeError("Q3 内部时间必须为 integer minute")
    return HORIZON_START + timedelta(minutes=minute)
