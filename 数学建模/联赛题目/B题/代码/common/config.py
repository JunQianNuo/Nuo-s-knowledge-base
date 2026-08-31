from __future__ import annotations

from .models import AircraftSpec

AIRPORTS = frozenset({"A01", "A02", "A03"})
OFFSHORE_FACILITIES = frozenset(f"F{number:03d}" for number in range(1, 53))
REFUEL_FACILITIES = frozenset({"F006", "F011", "F018", "F024", "F031", "F038", "F044", "F050"})
LAND = "LAND"

# 题面表1
AIRCRAFT_SPECS = {
    "T1": AircraftSpec("T1", 12, 250, 3.4, 1000, 150),
    "T2": AircraftSpec("T2", 16, 220, 2.5, 1150, 150),
    "T3": AircraftSpec("T3", 19, 190, 2.9, 1600, 200),
}

# K-5
MAX_OFFSHORE_LANDINGS = 5
# K-20
STOP_DURATION_MINUTES = 10
REFUEL_EXTRA_MINUTES = 10
# K-27, Q3-2
Q3_FIRST_DEPARTURE_MINUTE = 6 * 60
Q3_LAST_DEPARTURE_MINUTE = 18 * 60
Q3_RETURN_DEADLINE_MINUTE = 20 * 60
AIRCRAFT_TURNAROUND_MINUTES = 30
