from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Aircraft:
    aircraft_id: str
    base_airport: str
    aircraft_type: str


# 题面表3：各机场 T1/T2/T3 数量。H 序号在每个机场—机型内连续。
FLEET_COUNTS = {
    "A01": {"T1": 3, "T2": 3, "T3": 2},
    "A02": {"T1": 2, "T2": 4, "T3": 2},
    "A03": {"T1": 2, "T2": 3, "T3": 3},
}

FLEET = tuple(
    Aircraft(f"{base}-{kind}-H{number:02d}", base, kind)
    for base, counts in FLEET_COUNTS.items()
    for kind, count in counts.items()
    for number in range(1, count + 1)
)
FLEET_BY_ID = {aircraft.aircraft_id: aircraft for aircraft in FLEET}


def compatible_aircraft_ids(base_airport: str, aircraft_type: str) -> tuple[str, ...]:
    return tuple(
        aircraft.aircraft_id
        for aircraft in FLEET
        if aircraft.base_airport == base_airport and aircraft.aircraft_type == aircraft_type
    )
