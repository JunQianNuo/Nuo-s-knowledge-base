"""Build the final Q3 temporary-task compatibility profile used by Fig.13.

This submission version keeps only the evidence needed by the final 160/160
formal result.  It rebuilds candidate timed columns from the official data,
checks the validated formal Stage-B artifacts, and exports one row per temporary
person plus a compact JSON summary.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import replace
from pathlib import Path

import pandas as pd

from common.data_loader import load_distances, load_people_q3
from common.grouping import group_q3
from common.paths import CODE_ROOT, resolve_data_dir
from q3.algorithms.stage_a_pool import build_skeletons, build_timed_pool
from q3.algorithms.timed_pool import service_options
from q3.config import MANDATORY_TASKS, TEMPORARY_TASK
from q3.run_q3 import _artifact, _validated_baseline, _validated_stage_b


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Q3 final temporary-task compatibility profile")
    p.add_argument("--quick", action="store_true")
    p.add_argument("--data-dir", type=Path)
    p.add_argument("--output-dir", type=Path)
    return p.parse_args(argv)


def _window_stats(frame: pd.DataFrame) -> dict:
    values = frame["window_minutes"]
    return {
        "min": int(values.min()),
        "median": float(values.median()),
        "max": int(values.max()),
    }


def main(argv=None) -> int:
    args = parse_args(argv)
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or CODE_ROOT / "q3" / "outputs").resolve()

    stage_a = _validated_baseline(output_dir, data_dir, args.quick)
    stage_b = _validated_stage_b(output_dir, data_dir, args.quick, stage_a)
    if not (
        int(stage_b.get("temporary_served", -1)) == 160
        and int(stage_b.get("temporary_total", -1)) == 160
        and bool(stage_b.get("temporary_certified_optimal"))
        and float(stage_b.get("temporary_best_bound", -1)) == 160.0
    ):
        raise RuntimeError("Fig.13 requires the final certified Stage B result: 160/160, OPTIMAL.")

    people = load_people_q3(data_dir=data_dir)
    distances = load_distances(data_dir=data_dir).distances
    mandatory = group_q3(people[people["task_type"].isin(MANDATORY_TASKS)].copy())
    temporary = [
        replace(group, group_id=f"TMP{i:04d}")
        for i, group in enumerate(
            group_q3(people[people["task_type"].eq(TEMPORARY_TASK)].copy()), 1
        )
    ]

    q2_seed = CODE_ROOT / "q2" / "outputs" / "q2-routes.csv"
    if not q2_seed.is_file():
        raise FileNotFoundError("缺少 q2/outputs/q2-routes.csv；请先保留/运行 Q2 正式结果。")
    skeletons = build_skeletons(mandatory, distances, q2_seed)
    density = stage_b.get("time_sampling_density", "baseline")
    columns, _, _ = build_timed_pool(mandatory, skeletons, distances, density)
    column_by_id = {column.column_id: column for column in columns}

    by_group = {}
    for group in temporary:
        opts = [
            option
            for column in columns
            for option in service_options(group, column, distances)
        ]
        by_group[group.group_id] = sorted(
            opts, key=lambda o: (o.passenger_time, o.column_id)
        )[:60]

    assignments_path = _artifact(output_dir, "b", "assignments", args.quick)
    if not assignments_path.is_file():
        raise FileNotFoundError(
            f"缺少 {assignments_path.name}；请先运行 Q3 Stage A/B 以生成 Stage-B 正式交付文件。"
        )
    assignments = pd.read_csv(assignments_path, dtype={"person_id": str})
    served_ids = set(
        assignments.loc[assignments["aircraft_id"].notna(), "person_id"].astype(str)
    )

    group_by_person = {
        str(person_id): group for group in temporary for person_id in group.person_ids
    }
    temp_people = people[people["task_type"].eq(TEMPORARY_TASK)].copy()
    rows = []
    base_counter = Counter()
    type_counter = Counter()

    for person in temp_people.itertuples(index=False):
        pid = str(person.person_id)
        group = group_by_person[pid]
        opts = by_group[group.group_id]
        col_ids = {o.column_id for o in opts}
        aircraft_ids = {
            aircraft_id
            for cid in col_ids
            for aircraft_id in column_by_id[cid].compatible_aircraft_ids
        }
        types = sorted({column_by_id[cid].aircraft_type for cid in col_ids})
        bases = sorted({column_by_id[cid].base_airport for cid in col_ids})
        facilities = sorted(
            {
                node
                for cid in col_ids
                for node in column_by_id[cid].route[1:-1]
                if not str(node).startswith("A")
            }
        )
        for value in types:
            type_counter[value] += 1
        for value in bases:
            base_counter[value] += 1
        rows.append(
            {
                "person_id": pid,
                "group_id": group.group_id,
                "date": group.earliest_pickup_time.date().isoformat(),
                "earliest_pickup": group.earliest_pickup_time.isoformat(sep=" "),
                "latest_arrival": group.latest_arrival_time.isoformat(sep=" "),
                "origin": group.origin_id,
                "destination": group.destination_id,
                "service_option_count": len(opts),
                "compatible_aircraft_count": len(aircraft_ids),
                "aircraft_types": ";".join(types),
                "related_facilities": ";".join(facilities),
                "served": pid in served_ids,
                "reason": "served" if pid in served_ids else "unexpected-unserved",
            }
        )

    frame = pd.DataFrame(rows)
    if len(frame) != 160 or not frame["served"].all():
        raise RuntimeError("Stage-B CSV 与 160/160 正式结果不一致。")
    frame["window_minutes"] = (
        (pd.to_datetime(frame["latest_arrival"]) - pd.to_datetime(frame["earliest_pickup"]))
        .dt.total_seconds()
        .floordiv(60)
        .astype(int)
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    frame.drop(columns="window_minutes").to_csv(
        output_dir / "temporary_bottleneck.csv", index=False
    )
    summary = {
        "mode": "quick" if args.quick else "formal",
        "source_stage_b_validator": "PASS",
        "analysis_csv_validated": True,
        "all_temporary_count": 160,
        "all_temporary_served_count": 160,
        "all_temporary_unserved_count": 0,
        "all_temporary_compatible_airport_distribution": dict(sorted(base_counter.items())),
        "all_temporary_aircraft_type_distribution": dict(sorted(type_counter.items())),
        "compatibility_distribution_basis": (
            "one count per person and compatible base/type; multi-compatible persons may count twice"
        ),
        "all_temporary_time_window_width_minutes": _window_stats(frame),
        "diagnostic_scope": "restricted timed-column pool; final certified Stage-B solution",
    }
    (output_dir / "temporary_bottleneck_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        "temporary compatibility profile: total=160 served=160 "
        f"types={dict(sorted(type_counter.items()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
