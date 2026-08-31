"""Evidence-based diagnostics for Q3 temporary requests."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import replace
from pathlib import Path

import pandas as pd

from common.config import AIRPORTS, LAND
from common.data_loader import load_distances, load_people_q3
from common.grouping import group_q3
from common.paths import CODE_ROOT, resolve_data_dir
from q3.algorithms.stage_a_pool import build_skeletons, build_timed_pool
from q3.algorithms.timed_pool import service_options
from q3.config import MANDATORY_TASKS, TEMPORARY_TASK, datetime_to_minute
from q3.run_q3 import _artifact, _validated_baseline, _validated_stage_b

OUTPUT_COLUMNS = [
    "person_id",
    "group_id",
    "date",
    "earliest_pickup",
    "latest_arrival",
    "origin",
    "destination",
    "service_option_count",
    "compatible_aircraft_count",
    "aircraft_types",
    "related_facilities",
    "served",
    "reason",
]


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Analyze Q3 temporary requests")
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    return parser.parse_args(argv)


def _overlaps(column, occupied):
    start, end = column.departure_time, column.return_time + 30
    return any(
        start < other_end and other_start < end
        for other_start, other_end in occupied
    )


def _reason(
    group,
    candidates,
    column_by_id,
    selected,
    occupied,
    budget_slack,
):
    if not candidates:
        return "TimedColumn不足"

    candidate_columns = {
        option.column_id
        for option in candidates
    }

    if candidate_columns & selected:
        return "与mandatory或已接纳人员的航段容量/流量冲突"

    aircraft_available = False

    for column_id in candidate_columns:
        column = column_by_id[column_id]

        if any(
            not _overlaps(
                column,
                occupied.get(aircraft, ()),
            )
            for aircraft in column.compatible_aircraft_ids
        ):
            aircraft_available = True
            break

    if not aircraft_available:
        return "具体飞机资源冲突"

    if min(
        column_by_id[column_id].aircraft_time
        for column_id in candidate_columns
    ) > budget_slack:
        return "B0飞机时间限制"

    width = int(
        (
            group.latest_arrival_time
            - group.earliest_pickup_time
        ).total_seconds()
        // 60
    )

    if width <= 120:
        return "时间窗过窄"

    return "受限列池内组合约束"


def _width_bin(minutes):
    if minutes <= 120:
        return "<=120"
    if minutes <= 240:
        return "121-240"
    if minutes <= 480:
        return "241-480"
    return ">480"


def _window_stats(frame):
    """Return safe window statistics, including for an empty frame."""
    if frame.empty:
        return {
            "min": None,
            "median": None,
            "max": None,
            "distribution": {},
        }

    window = frame["window_minutes"]

    return {
        "min": int(window.min()),
        "median": float(window.median()),
        "max": int(window.max()),
        "distribution": (
            window.map(_width_bin)
            .value_counts()
            .to_dict()
        ),
    }


def _validate_analysis_frame(
    frame,
    temporary_people,
    served_ids,
):
    if list(frame.columns) != [
        *OUTPUT_COLUMNS,
        "window_minutes",
    ]:
        raise RuntimeError(
            "temporary bottleneck CSV schema mismatch"
        )

    expected = (
        temporary_people["person_id"]
        .astype(str)
        .tolist()
    )

    if frame["person_id"].tolist() != expected:
        raise RuntimeError(
            "temporary bottleneck person order mismatch"
        )

    actual_served = set(
        frame.loc[
            frame["served"],
            "person_id",
        ]
    )

    expected_served = (
        set(expected)
        & served_ids
    )

    if actual_served != expected_served:
        raise RuntimeError(
            "temporary bottleneck served flags mismatch Stage B CSV"
        )


def main(argv=None) -> int:
    args = parse_args(argv)

    data_dir = resolve_data_dir(args.data_dir)

    output_dir = (
        args.output_dir
        or CODE_ROOT / "q3" / "outputs"
    ).resolve()

    stage_a = _validated_baseline(
        output_dir,
        data_dir,
        args.quick,
    )

    stage_b = _validated_stage_b(
        output_dir,
        data_dir,
        args.quick,
        stage_a,
    )

    people = load_people_q3(
        data_dir=data_dir
    )

    distances = load_distances(
        data_dir=data_dir
    ).distances

    mandatory_groups = group_q3(
        people[
            people["task_type"].isin(MANDATORY_TASKS)
        ].copy()
    )

    temporary_groups = [
        replace(
            group,
            group_id=f"TMP{index:04d}",
        )
        for index, group in enumerate(
            group_q3(
                people[
                    people["task_type"].eq(
                        TEMPORARY_TASK
                    )
                ].copy()
            ),
            1,
        )
    ]

    density = stage_b.get(
        "time_sampling_density",
        "baseline",
    )

    skeletons = build_skeletons(
        mandatory_groups,
        distances,
        CODE_ROOT
        / "q2"
        / "outputs"
        / "q2-routes.csv",
    )

    columns, _, _ = build_timed_pool(
        mandatory_groups,
        skeletons,
        distances,
        density,
    )

    by_group = {}

    for group in temporary_groups:
        candidates = [
            option
            for column in columns
            for option in service_options(
                group,
                column,
                distances,
            )
        ]

        candidates = sorted(
            candidates,
            key=lambda option: (
                option.passenger_time,
                option.column_id,
            ),
        )[:60]

        by_group[group.group_id] = candidates

    column_by_id = {
        column.column_id: column
        for column in columns
    }

    columns_by_signature = {}

    for column in columns:
        columns_by_signature.setdefault(
            (
                column.base_airport,
                column.aircraft_type,
                column.route,
                column.departure_time,
            ),
            [],
        ).append(column.column_id)

    routes = pd.read_csv(
        _artifact(
            output_dir,
            "b",
            "routes",
            args.quick,
        )
    )

    selected = set()
    occupied = {}

    for (
        aircraft_id,
        _,
    ), flight in routes.groupby(
        ["aircraft_id", "flight_no"]
    ):
        flight = flight.sort_values(
            "stop_order"
        )

        start = datetime_to_minute(
            pd.Timestamp(
                flight.iloc[0]["departure_time"]
            ).to_pydatetime()
        )

        end = datetime_to_minute(
            pd.Timestamp(
                flight.iloc[-1]["arrival_time"]
            ).to_pydatetime()
        )

        aircraft_id = str(aircraft_id)

        occupied.setdefault(
            aircraft_id,
            [],
        ).append(
            (start, end + 30)
        )

        signature = (
            str(
                flight.iloc[0]["facility_id"]
            ),
            aircraft_id.split("-")[1],
            tuple(
                flight["facility_id"].astype(str)
            ),
            start,
        )

        selected.update(
            columns_by_signature.get(
                signature,
                (),
            )
        )

    assignments = pd.read_csv(
        _artifact(
            output_dir,
            "b",
            "assignments",
            args.quick,
        ),
        dtype={"person_id": str},
    )

    served_ids = set(
        assignments.loc[
            assignments["aircraft_id"].notna(),
            "person_id",
        ].astype(str)
    )

    budget_slack = (
        int(stage_b["B0"])
        - int(stage_b["T_air"])
    )

    rows = []
    airport_counts = Counter()

    group_by_person = {
        str(person_id): group
        for group in temporary_groups
        for person_id in group.person_ids
    }

    temporary_people = people[
        people["task_type"].eq(
            TEMPORARY_TASK
        )
    ]

    for person in temporary_people.itertuples(
        index=False
    ):
        person_id = str(
            person.person_id
        )

        group = group_by_person[
            person_id
        ]

        candidates = by_group[
            group.group_id
        ]

        candidate_columns = {
            option.column_id
            for option in candidates
        }

        aircraft_ids = {
            aircraft
            for column_id in candidate_columns
            for aircraft in (
                column_by_id[
                    column_id
                ].compatible_aircraft_ids
            )
        }

        aircraft_types = sorted(
            {
                column_by_id[
                    column_id
                ].aircraft_type
                for column_id in candidate_columns
            }
        )

        compatible_bases = {
            column_by_id[
                column_id
            ].base_airport
            for column_id in candidate_columns
        }

        airport_counts.update(
            compatible_bases
        )

        facilities = sorted(
            {
                location
                for column_id
                in candidate_columns
                for location
                in column_by_id[
                    column_id
                ].route[1:-1]
                if location not in AIRPORTS
            }
        )

        served = person_id in served_ids

        reason = (
            "served"
            if served
            else _reason(
                group,
                candidates,
                column_by_id,
                selected,
                occupied,
                budget_slack,
            )
        )

        rows.append(
            {
                "person_id": person_id,
                "group_id": group.group_id,
                "date": (
                    group.earliest_pickup_time
                    .date()
                    .isoformat()
                ),
                "earliest_pickup": (
                    group.earliest_pickup_time
                    .isoformat(sep=" ")
                ),
                "latest_arrival": (
                    group.latest_arrival_time
                    .isoformat(sep=" ")
                ),
                "origin": group.origin_id,
                "destination": (
                    group.destination_id
                ),
                "service_option_count": (
                    len(candidates)
                ),
                "compatible_aircraft_count": (
                    len(aircraft_ids)
                ),
                "aircraft_types": ";".join(
                    aircraft_types
                ),
                "related_facilities": ";".join(
                    facilities
                ),
                "served": served,
                "reason": reason,
            }
        )

    frame = pd.DataFrame(rows)

    frame["window_minutes"] = (
        (
            pd.to_datetime(
                frame["latest_arrival"]
            )
            - pd.to_datetime(
                frame["earliest_pickup"]
            )
        ).dt.total_seconds()
        // 60
    )

    _validate_analysis_frame(
        frame,
        temporary_people,
        served_ids,
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    frame.drop(
        columns="window_minutes"
    ).to_csv(
        output_dir
        / "temporary_bottleneck.csv",
        index=False,
    )

    type_counts = Counter(
        aircraft_type
        for values in frame[
            "aircraft_types"
        ]
        for aircraft_type in values.split(";")
        if aircraft_type
    )

    unserved = frame.loc[
        ~frame["served"]
    ].copy()

    unserved_type_counts = Counter(
        aircraft_type
        for values in unserved[
            "aircraft_types"
        ]
        for aircraft_type in values.split(";")
        if aircraft_type
    )

    unserved_airports = Counter(
        value
        for column in (
            "origin",
            "destination",
        )
        for value in unserved[column]
        if (
            value == LAND
            or value in AIRPORTS
        )
    )

    all_window_stats = _window_stats(
        frame
    )

    unserved_window_stats = (
        _window_stats(unserved)
    )

    summary = {
        "mode": (
            "quick"
            if args.quick
            else "formal"
        ),
        "source_stage_b_validator": "PASS",
        "analysis_csv_validated": True,
        "all_temporary_count": len(frame),
        "all_temporary_served_count": int(
            frame["served"].sum()
        ),
        "all_temporary_unserved_count": len(
            unserved
        ),
        "all_temporary_date_distribution": (
            frame["date"]
            .value_counts()
            .sort_index()
            .to_dict()
        ),
        "all_temporary_origin_distribution": (
            frame["origin"]
            .value_counts()
            .to_dict()
        ),
        "all_temporary_destination_distribution": (
            frame["destination"]
            .value_counts()
            .to_dict()
        ),
        "all_temporary_compatible_airport_distribution": (
            dict(
                sorted(
                    airport_counts.items()
                )
            )
        ),
        "all_temporary_aircraft_type_distribution": (
            dict(
                sorted(
                    type_counts.items()
                )
            )
        ),
        "compatibility_distribution_basis": (
            "one count per person and compatible base/type; "
            "multi-compatible persons may count twice"
        ),
        "all_temporary_time_window_width_distribution": (
            all_window_stats[
                "distribution"
            ]
        ),
        "all_temporary_time_window_width_minutes": {
            "min": all_window_stats["min"],
            "median": all_window_stats["median"],
            "max": all_window_stats["max"],
        },
        "unserved_count": len(unserved),
        "unserved_date_distribution": (
            unserved["date"]
            .value_counts()
            .sort_index()
            .to_dict()
        ),
        "unserved_origin_distribution": (
            unserved["origin"]
            .value_counts()
            .to_dict()
        ),
        "unserved_destination_distribution": (
            unserved["destination"]
            .value_counts()
            .to_dict()
        ),
        "unserved_airport_distribution": (
            dict(
                sorted(
                    unserved_airports.items()
                )
            )
        ),
        "unserved_aircraft_type_distribution": (
            dict(
                sorted(
                    unserved_type_counts.items()
                )
            )
        ),
        "unserved_time_window_width_minutes": (
            unserved_window_stats
        ),
        "unserved_reason_distribution": (
            unserved["reason"]
            .value_counts()
            .to_dict()
        ),
        "diagnostic_scope": (
            "restricted timed-column pool; "
            "reasons are evidence-based categories"
        ),
    }

    (
        output_dir
        / "temporary_bottleneck_summary.json"
    ).write_text(
        json.dumps(
            summary,
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "temporary analysis:"
        f" total={len(frame)}"
        f" served={int(frame['served'].sum())}"
        f" unserved={len(unserved)}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())