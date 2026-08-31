from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import tempfile
import time
from dataclasses import replace
from pathlib import Path

import pandas as pd

from common.config import AIRCRAFT_SPECS
from common.data_loader import load_distances, load_people_q2, load_people_q3
from common.grouping import group_q3
from common.paths import CODE_ROOT, resolve_data_dir
from q3.algorithms.lex import StageCLexMaster
from q3.algorithms.master import StageAMaster
from q3.algorithms.realize import realize_stage_a
from q3.algorithms.stage_a_pool import TIME_SAMPLING_FRACTIONS, build_skeletons, build_timed_pool
from q3.algorithms.timed_pool import TimedColumn, service_options
from q3.config import MANDATORY_TASKS, TEMPORARY_TASK, datetime_to_minute
from q3.fleet import FLEET_BY_ID, compatible_aircraft_ids
from q3.io.csv_validator import validate_q3_csv
from q3.io.csv_writer import write_q3_csv


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Q3 Stage A timed-column solver")
    parser.add_argument("--stage-a", action="store_true")
    parser.add_argument("--stage-b", action="store_true")
    parser.add_argument("--stage-c", action="store_true")
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--time-budget", type=float)
    parser.add_argument("--stage-a-budget", type=float)
    parser.add_argument("--stage-b-budget", type=float)
    parser.add_argument("--stage-c-budget", type=float)
    parser.add_argument(
        "--time-sampling-density",
        choices=tuple(TIME_SAMPLING_FRACTIONS),
        default="baseline",
    )
    parser.add_argument("--seed", type=int)
    parser.add_argument("--stage-a-hint-dir", type=Path)
    parser.add_argument("--stage-b-hint-dir", type=Path)
    parser.add_argument("--parent-route-seeds", type=Path)
    parser.add_argument("--incumbent-columns", type=Path)
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    if args.stage_c:
        return run_stage_c(args)
    if args.stage_b:
        return run_stage_b(args)
    if args.quick and not args.stage_a:
        return run_stage_c(args)
    if not args.stage_a:
        run_stage_a(args)
        run_stage_b(args)
        return run_stage_c(args)
    return run_stage_a(args)


def _artifact(output_dir, stage, kind, quick):
    prefix = "" if quick else "formal_"
    suffix = "json" if kind == "summary" else "csv"
    return output_dir / f"{prefix}stage_{stage}_{kind}.{suffix}"


def _budget(args, stage):
    explicit = getattr(args, f"stage_{stage}_budget")
    if args.time_budget is not None:
        return args.time_budget
    if explicit is not None:
        return explicit
    return {
        "a": 240.0 if args.quick else 600.0,
        "b": 180.0 if args.quick else 360.0,
        "c": 240.0 if args.quick else 360.0,
    }[stage]


def _temporary_certification(solution):
    bound = solution.restricted_pool_bound
    gap = (
        max(0.0, float(bound) - solution.temporary_served)
        / max(1, solution.temporary_served)
        if bound is not None
        else None
    )
    return {
        "temporary_incumbent": solution.temporary_served,
        "temporary_best_bound": bound,
        "temporary_gap": gap,
        "temporary_certified_optimal": solution.status == "OPTIMAL",
    }


def _load_validated_timed_columns(path, distances):
    routes = pd.read_csv(path)
    result = {}
    for (aircraft_id, _), frame in routes.groupby(["aircraft_id", "flight_no"]):
        frame = frame.sort_values("stop_order")
        aircraft = FLEET_BY_ID[str(aircraft_id)]
        route = tuple(frame["facility_id"].astype(str))
        arrivals = [
            None
            if pd.isna(value)
            else datetime_to_minute(pd.Timestamp(value).to_pydatetime())
            for value in frame["arrival_time"]
        ]
        departures = [
            None
            if pd.isna(value)
            else datetime_to_minute(pd.Timestamp(value).to_pydatetime())
            for value in frame["departure_time"]
        ]
        arrivals[0], departures[-1] = departures[0], arrivals[-1]
        refuels = tuple(bool(value) for value in frame["refuel"].astype(int))
        signature = (
            route,
            refuels,
            tuple(arrivals),
            tuple(departures),
            aircraft.aircraft_type,
        )
        column_id = "INC" + hashlib.sha1(repr(signature).encode()).hexdigest()[:14]
        distance = sum(float(distances[arc]) for arc in zip(route, route[1:]))
        result[signature] = TimedColumn(
            column_id=column_id,
            day=departures[0] // 1440,
            base_airport=aircraft.base_airport,
            aircraft_type=aircraft.aircraft_type,
            route=route,
            refuel_decisions=refuels,
            departure_time=departures[0],
            return_time=arrivals[-1],
            arrival_times=tuple(arrivals),
            departure_times=tuple(departures),
            aircraft_time=arrivals[-1] - departures[0],
            distance=distance,
            fuel_used=AIRCRAFT_SPECS[aircraft.aircraft_type].fuel_consumption_kg_per_km
            * distance,
            compatible_aircraft_ids=compatible_aircraft_ids(
                aircraft.base_airport, aircraft.aircraft_type
            ),
        )
    return list(result.values())


def _augment_incumbent_columns(groups, columns, options, path, distances):
    known = {
        (
            column.base_airport,
            column.aircraft_type,
            column.route,
            column.arrival_times,
            column.departure_times,
        ): column
        for column in columns
    }
    selected_columns = []
    for column in _load_validated_timed_columns(path, distances):
        signature = (
            column.base_airport,
            column.aircraft_type,
            column.route,
            column.arrival_times,
            column.departure_times,
        )
        selected = known.get(signature)
        if selected is None:
            columns.append(column)
            known[signature] = column
            selected = column
        selected_columns.append(selected)
    options.extend(
        option
        for group in groups
        for column in selected_columns
        for option in service_options(group, column, distances)
    )
    return columns, list({option.option_id: option for option in options}.values())


def run_stage_a(args) -> int:
    started = time.perf_counter()
    deadline = started + _budget(args, "a")
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or CODE_ROOT / "q3" / "outputs").resolve()
    distance_data = load_distances(data_dir=data_dir)
    people = load_people_q3(data_dir=data_dir)
    q2_people = load_people_q2(data_dir=data_dir)
    identity = ["person_id", "origin_id", "destination_id"]
    if not q2_people[identity].astype(str).equals(people[identity].astype(str)):
        raise RuntimeError("Q2/Q3 person+OD mismatch")
    mandatory_people = people[people["task_type"].isin(MANDATORY_TASKS)].copy()
    groups = group_q3(mandatory_people)
    if len(people) != 4000 or len(mandatory_people) != 3840:
        raise RuntimeError("Q3 data contract mismatch")
    skeleton_started = time.perf_counter()
    q2_seed = CODE_ROOT / "q2" / "outputs" / "q2-routes.csv"
    skeletons = build_skeletons(groups, distance_data.distances, q2_seed)
    skeleton_seconds = time.perf_counter() - skeleton_started
    embed_started = time.perf_counter()
    columns, options, pool_stats = build_timed_pool(
        groups,
        skeletons,
        distance_data.distances,
        args.time_sampling_density,
    )
    embed_seconds = time.perf_counter() - embed_started
    print(
        f"pool skeletons={pool_stats.physical_skeletons} columns={pool_stats.timed_columns} "
        f"options={pool_stats.service_options}; coverage mandatory groups={len(groups)} "
        f"min={pool_stats.minimum_group_coverage} zero=0"
    )
    hint_aircraft, hint_flows = {}, {}
    if args.stage_a_hint_dir is not None:
        hint_aircraft, hint_flows = _stage_hint(
            args.stage_a_hint_dir.resolve(), groups, columns, options, "a", args.quick
        )
    solution = StageAMaster(groups, columns, options).solve(
        deadline,
        args.workers,
        hint_aircraft_by_column=hint_aircraft,
        hint_flows=hint_flows,
        seed=args.seed,
    )
    if not solution.aircraft_by_column:
        raise RuntimeError(f"Stage A restricted master has no feasible solution: {solution.status}")
    flights, assignments = realize_stage_a(groups, columns, options, solution)
    stage_routes = _artifact(output_dir, "a", "routes", args.quick)
    stage_assignments = _artifact(output_dir, "a", "assignments", args.quick)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="q3-stage-a-", dir=output_dir) as directory:
        routes_path, assignments_path = write_q3_csv(Path(directory), people, flights, assignments)
        routes_path.replace(stage_routes)
        assignments_path.replace(stage_assignments)
    report = validate_q3_csv(
        routes_path=stage_routes,
        assignments_path=stage_assignments,
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    delivered = report.metrics
    solver_matches = (
        delivered.mandatory_served == 3840
        and delivered.total_aircraft_time == solution.aircraft_time
        and delivered.number_of_flights == solution.flights
        and delivered.total_passenger_time == solution.passenger_time
        and math.isclose(delivered.total_fuel, solution.fuel, abs_tol=1e-6)
        and math.isclose(delivered.passenger_km, solution.passenger_km, abs_tol=1e-6)
        and math.isclose(delivered.available_seat_km, solution.available_seat_km, abs_tol=1e-6)
    )
    if not report.valid or not solver_matches:
        raise RuntimeError(
            "Stage A independent validation failed:\n" + "\n".join(report.violations[:30])
        )
    by_aircraft = {}
    for flight in flights:
        by_aircraft[flight.aircraft_id] = by_aircraft.get(flight.aircraft_id, 0) + 1
    summary = {
        "stage": "A",
        "mode": "quick" if args.quick else "formal",
        "baseline_kind": (
            "quick_best_validated_feasible"
            if args.quick
            else (
                "formal_finite_timed_pool_optimal"
                if solution.status == "OPTIMAL"
                else "formal_best_validated_feasible"
            )
        ),
        "mandatory_served": delivered.mandatory_served,
        "mandatory_total": 3840,
        "physical_skeletons": pool_stats.physical_skeletons,
        "timed_columns": pool_stats.timed_columns,
        "service_options": pool_stats.service_options,
        "minimum_group_coverage": pool_stats.minimum_group_coverage,
        "selected_flights": solution.flights,
        "aircraft_used": len(by_aircraft),
        "T_air": solution.aircraft_time,
        "restricted_pool_bound": solution.restricted_pool_bound,
        "status": solution.status,
        "time_sampling_density": args.time_sampling_density,
        "seed": args.seed,
        "validation": {"independent": report.valid, "solver_equals_delivery": solver_matches},
        "runtime": {
            "skeleton_generation": skeleton_seconds,
            "time_embedding": embed_seconds,
            "master": solution.wall_time,
            "total": time.perf_counter() - started,
        },
    }
    with _artifact(output_dir, "a", "summary", args.quick).open("w", encoding="utf-8") as stream:
        json.dump(summary, stream, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def _validated_baseline(output_dir, data_dir, quick):
    summary_path = _artifact(output_dir, "a", "summary", quick)
    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError("Stage A summary missing or damaged") from exc
    report = validate_q3_csv(
        routes_path=_artifact(output_dir, "a", "routes", quick),
        assignments_path=_artifact(output_dir, "a", "assignments", quick),
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    if (
        summary.get("mandatory_served") != 3840
        or not summary.get("validation", {}).get("independent")
        or not report.valid
        or report.metrics.mandatory_served != 3840
        or report.metrics.total_aircraft_time != summary.get("T_air")
        or summary.get("mode") != ("quick" if quick else "formal")
    ):
        raise RuntimeError("Stage A baseline inconsistent or stale")
    return summary


def run_stage_b(args) -> int:
    started = time.perf_counter()
    deadline = started + _budget(args, "b")
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or CODE_ROOT / "q3" / "outputs").resolve()
    parent = _validated_baseline(output_dir, data_dir, args.quick)
    b0 = int(parent["T_air"])
    distances = load_distances(data_dir=data_dir).distances
    people = load_people_q3(data_dir=data_dir)
    mandatory_people = people[people["task_type"].isin(MANDATORY_TASKS)].copy()
    temporary_people = people[people["task_type"].eq(TEMPORARY_TASK)].copy()
    mandatory_groups = group_q3(mandatory_people)
    temporary_groups = [
        replace(group, group_id=f"TMP{index:04d}")
        for index, group in enumerate(group_q3(temporary_people), 1)
    ]
    q2_seed = CODE_ROOT / "q2" / "outputs" / "q2-routes.csv"
    skeletons = build_skeletons(
        mandatory_groups, distances, q2_seed, args.parent_route_seeds
    )
    columns, mandatory_options, _ = build_timed_pool(
        mandatory_groups, skeletons, distances, args.time_sampling_density
    )
    option_started = time.perf_counter()
    temporary_options = []
    coverage = {group.group_id: 0 for group in temporary_groups}
    for group in temporary_groups:
        candidates = [
            option for column in columns for option in service_options(group, column, distances)
        ]
        candidates.sort(key=lambda option: (option.passenger_time, option.column_id))
        temporary_options.extend(candidates[:60])
        coverage[group.group_id] = len(candidates[:60])
    option_seconds = time.perf_counter() - option_started
    covered = {group.group_id for group in temporary_groups if coverage[group.group_id]}
    persons_coverable = sum(
        group.quantity for group in temporary_groups if group.group_id in covered
    )
    groups = [*mandatory_groups, *temporary_groups]
    options = [*mandatory_options, *temporary_options]
    if args.incumbent_columns is not None:
        columns, options = _augment_incumbent_columns(
            groups, columns, options, args.incumbent_columns, distances
        )
    temporary_ids = {group.group_id for group in temporary_groups}
    if args.stage_b_hint_dir is None:
        hint_aircraft, hint_flows = _stage_hint(
            output_dir, mandatory_groups, columns, mandatory_options, "a", args.quick
        )
    else:
        hint_aircraft, hint_flows = _stage_hint(
            args.stage_b_hint_dir.resolve(),
            groups,
            columns,
            options,
            "b",
            args.quick,
        )
    master_started = time.perf_counter()
    solution = StageAMaster(groups, columns, options, temporary_ids).solve(
        deadline,
        args.workers,
        temporary_ids,
        b0,
        hint_aircraft,
        hint_flows,
        args.seed,
    )
    master_seconds = time.perf_counter() - master_started
    if not solution.aircraft_by_column:
        raise RuntimeError(f"Stage B has no feasible solution: {solution.status}")
    realize_started = time.perf_counter()
    flights, assignments = realize_stage_a(groups, columns, options, solution, temporary_ids)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="q3-stage-b-", dir=output_dir) as directory:
        route_path, assignment_path = write_q3_csv(Path(directory), people, flights, assignments)
        route_path.replace(_artifact(output_dir, "b", "routes", args.quick))
        assignment_path.replace(_artifact(output_dir, "b", "assignments", args.quick))
    report = validate_q3_csv(
        routes_path=_artifact(output_dir, "b", "routes", args.quick),
        assignments_path=_artifact(output_dir, "b", "assignments", args.quick),
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    delivered = report.metrics
    solver_matches = (
        delivered.mandatory_served == 3840
        and delivered.temporary_served == solution.temporary_served
        and delivered.total_aircraft_time == solution.aircraft_time
        and delivered.number_of_flights == solution.flights
        and delivered.total_passenger_time == solution.passenger_time
        and math.isclose(delivered.total_fuel, solution.fuel, abs_tol=1e-6)
        and math.isclose(delivered.passenger_km, solution.passenger_km, abs_tol=1e-6)
        and math.isclose(delivered.available_seat_km, solution.available_seat_km, abs_tol=1e-6)
    )
    if not report.valid or not solver_matches or solution.aircraft_time > b0:
        raise RuntimeError("Stage B independent validation or metric reconciliation failed")
    validation_seconds = time.perf_counter() - realize_started
    certification = _temporary_certification(solution)
    summary = {
        "stage": "B",
        "mode": "quick" if args.quick else "formal",
        "baseline_kind": parent.get(
            "baseline_kind",
            "quick_best_validated_feasible" if args.quick else "formal_best_validated_feasible",
        ),
        "B0": b0,
        "mandatory_served": delivered.mandatory_served,
        "temporary_served": delivered.temporary_served,
        "temporary_total": 160,
        "temporary_satisfaction_rate": delivered.temporary_served / 160,
        "T_air": delivered.total_aircraft_time,
        "status": solution.status,
        "solver_status": solution.status,
        **certification,
        "solver_best_bound": solution.restricted_pool_bound,
        "solver_wall_time": solution.wall_time,
        "time_sampling_density": args.time_sampling_density,
        "seed": args.seed,
        "temporary_groups": len(temporary_groups),
        "temporary_groups_covered": len(covered),
        "temporary_persons_coverable": persons_coverable,
        "zero_option_temporary_groups": len(temporary_groups) - len(covered),
        "selected_flights": solution.flights,
        "aircraft_used": len({flight.aircraft_id for flight in flights}),
        "validation": {"independent": report.valid, "solver_equals_delivery": solver_matches},
        "runtime": {
            "option_generation": option_seconds,
            "master": master_seconds,
            "realization_validation": validation_seconds,
            "total": time.perf_counter() - started,
        },
    }
    _artifact(output_dir, "b", "summary", args.quick).write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def _stage_hint(output_dir, groups, columns, options, stage, quick):
    routes = pd.read_csv(_artifact(output_dir, stage, "routes", quick))
    assignments = pd.read_csv(_artifact(output_dir, stage, "assignments", quick))
    by_signature = {
        (
            column.base_airport,
            column.aircraft_type,
            column.route,
            tuple(column.arrival_times),
            tuple(column.departure_times),
        ): column.column_id
        for column in columns
    }
    from q3.config import datetime_to_minute

    flight_column = {}
    hint_aircraft = {}
    for (aircraft_id, flight_no), frame in routes.groupby(["aircraft_id", "flight_no"]):
        frame = frame.sort_values("stop_order")
        route = tuple(frame["facility_id"].astype(str))
        parsed_arrivals = [
            None if pd.isna(value) else datetime_to_minute(pd.Timestamp(value).to_pydatetime())
            for value in frame["arrival_time"]
        ]
        parsed_departures = [
            None if pd.isna(value) else datetime_to_minute(pd.Timestamp(value).to_pydatetime())
            for value in frame["departure_time"]
        ]
        parsed_arrivals[0] = parsed_departures[0]
        parsed_departures[-1] = parsed_arrivals[-1]
        arrivals, departures = tuple(parsed_arrivals), tuple(parsed_departures)
        kind = str(aircraft_id).split("-")[1]
        column_id = by_signature.get((route[0], kind, route, arrivals, departures))
        if column_id is None:
            continue
        flight_column[(str(aircraft_id), int(flight_no))] = column_id
        hint_aircraft.setdefault(column_id, []).append(str(aircraft_id))
    person_group = {person: group.group_id for group in groups for person in group.person_ids}
    option_id = {
        (option.group_id, option.column_id, option.pickup, option.delivery): option.option_id
        for option in options
    }
    hint_flows = {}
    for row in assignments.dropna(subset=["aircraft_id"]).itertuples(index=False):
        group_id = person_group[str(row.person_id)]
        column_id = flight_column.get((str(row.aircraft_id), int(row.flight_no)))
        if column_id is None:
            continue
        key = (group_id, column_id, int(row.pickup_stop_order), int(row.delivery_stop_order))
        selected = option_id.get(key)
        if selected is None:
            continue
        hint_flows[selected] = hint_flows.get(selected, 0) + 1
    return hint_aircraft, hint_flows


def _validated_stage_b(output_dir, data_dir, quick, stage_a_summary):
    try:
        summary = json.loads(
            _artifact(output_dir, "b", "summary", quick).read_text(encoding="utf-8")
        )
    except Exception as exc:
        raise RuntimeError("Stage B summary missing or damaged") from exc
    report = validate_q3_csv(
        routes_path=_artifact(output_dir, "b", "routes", quick),
        assignments_path=_artifact(output_dir, "b", "assignments", quick),
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    if (
        not report.valid
        or not summary.get("validation", {}).get("independent")
        or summary.get("B0") != stage_a_summary.get("T_air")
        or summary.get("mandatory_served") != report.metrics.mandatory_served
        or summary.get("temporary_served") != report.metrics.temporary_served
        or summary.get("T_air") != report.metrics.total_aircraft_time
        or report.metrics.mandatory_served != 3840
        or summary.get("mode") != ("quick" if quick else "formal")
    ):
        raise RuntimeError("Stage B baseline inconsistent or stale")
    return summary


def run_stage_c(args):
    started = time.perf_counter()
    deadline = started + _budget(args, "c")
    data_dir = resolve_data_dir(args.data_dir)
    output_dir = (args.output_dir or CODE_ROOT / "q3" / "outputs").resolve()
    stage_a = _validated_baseline(output_dir, data_dir, args.quick)
    stage_b = _validated_stage_b(output_dir, data_dir, args.quick, stage_a)
    b0 = int(stage_a["T_air"])
    temporary_served = int(stage_b["temporary_served"])
    parent_aircraft_time = int(stage_b["T_air"])
    distances = load_distances(data_dir=data_dir).distances
    people = load_people_q3(data_dir=data_dir)
    mandatory_groups = group_q3(people[people["task_type"].isin(MANDATORY_TASKS)].copy())
    temporary_groups = [
        replace(group, group_id=f"TMP{index:04d}")
        for index, group in enumerate(
            group_q3(people[people["task_type"].eq(TEMPORARY_TASK)].copy()), 1
        )
    ]
    skeletons = build_skeletons(
        mandatory_groups, distances, CODE_ROOT / "q2" / "outputs" / "q2-routes.csv"
    )
    columns, mandatory_options, _ = build_timed_pool(
        mandatory_groups, skeletons, distances, args.time_sampling_density
    )
    temporary_options = []
    for group in temporary_groups:
        candidates = [
            option for column in columns for option in service_options(group, column, distances)
        ]
        temporary_options.extend(
            sorted(candidates, key=lambda option: (option.passenger_time, option.column_id))[:60]
        )
    groups, options = (
        [*mandatory_groups, *temporary_groups],
        [
            *mandatory_options,
            *temporary_options,
        ],
    )
    columns, options = _augment_incumbent_columns(
        groups,
        columns,
        options,
        _artifact(output_dir, "b", "routes", args.quick),
        distances,
    )
    temporary_ids = {group.group_id for group in temporary_groups}
    hint = _stage_hint(output_dir, groups, columns, options, "b", args.quick)
    master = StageCLexMaster(
        groups,
        columns,
        options,
        temporary_ids,
        temporary_served=temporary_served,
        budget=b0,
    )
    parent_certified = bool(stage_b.get("temporary_certified_optimal"))
    solution = master.solve_lex(
        deadline, args.workers, hint, parent_certified, seed=args.seed
    )
    if solution.aircraft_time > parent_aircraft_time:
        raise RuntimeError("Stage C1/final T_air regressed above Stage B incumbent")
    realization_started = time.perf_counter()
    flights, assignments = realize_stage_a(groups, columns, options, solution, temporary_ids)
    with tempfile.TemporaryDirectory(prefix="q3-stage-c-", dir=output_dir) as directory:
        route_path, assignment_path = write_q3_csv(Path(directory), people, flights, assignments)
        route_path.replace(_artifact(output_dir, "c", "routes", args.quick))
        assignment_path.replace(_artifact(output_dir, "c", "assignments", args.quick))
    report = validate_q3_csv(
        routes_path=_artifact(output_dir, "c", "routes", args.quick),
        assignments_path=_artifact(output_dir, "c", "assignments", args.quick),
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    metrics = report.metrics
    solver_matches = (
        metrics.mandatory_served == 3840
        and metrics.temporary_served == temporary_served
        and metrics.total_aircraft_time == solution.aircraft_time
        and metrics.total_passenger_time == solution.passenger_time
        and metrics.number_of_flights == solution.flights
        and math.isclose(metrics.total_fuel, solution.fuel, abs_tol=1e-6)
        and math.isclose(metrics.passenger_km, solution.passenger_km, abs_tol=1e-6)
        and math.isclose(metrics.available_seat_km, solution.available_seat_km, abs_tol=1e-6)
    )
    if not report.valid or not solver_matches:
        raise RuntimeError("Stage C independent validation or metric reconciliation failed")
    pd.DataFrame(
        [
            {
                "stage": record.name,
                "status": record.status,
                "objective": record.objective,
                "best_bound": record.best_bound,
                "wall_time": record.wall_time,
                "certified_optimal": record.certified_optimal,
                "conditioned_on_uncertified_parent": record.conditioned_on_uncertified_parent,
                "dinkelbach_iterations": solution.dinkelbach_iterations
                if record.name == "seat_utilization"
                else "",
                "utilization": solution.utilization if record.name == "seat_utilization" else "",
            }
            for record in solution.stages
        ]
    ).to_csv(_artifact(output_dir, "c", "history", args.quick), index=False)
    stage_values = {record.name: record for record in solution.stages}
    summary = {
        "stage": "C",
        "mode": "quick" if args.quick else "formal",
        "parent_B0": b0,
        "fixed_temporary_served": temporary_served,
        "conditioned_on_uncertified_parent": (not parent_certified)
        or any(not record.certified_optimal for record in solution.stages),
        "full_certified": solution.full_certified,
        "status": solution.status,
        "temporary_incumbent": stage_b.get("temporary_incumbent", temporary_served),
        "temporary_best_bound": stage_b.get("temporary_best_bound"),
        "temporary_gap": stage_b.get("temporary_gap"),
        "temporary_certified_optimal": stage_b.get(
            "temporary_certified_optimal", stage_b.get("status") == "OPTIMAL"
        ),
        "stage_b_solver_status": stage_b.get("solver_status", stage_b.get("status")),
        "stage_b_solver_best_bound": stage_b.get("solver_best_bound"),
        "stage_b_solver_wall_time": stage_b.get("solver_wall_time"),
        "time_sampling_density": args.time_sampling_density,
        "seed": args.seed,
        "T_air": solution.aircraft_time,
        "T_pax": solution.passenger_time,
        "fuel": solution.fuel,
        "flights": solution.flights,
        "PK": solution.passenger_km,
        "AK": solution.available_seat_km,
        "utilization": solution.utilization,
        "selected_flights": solution.flights,
        "aircraft_used": len({flight.aircraft_id for flight in flights}),
        "stages": {
            name: {
                "status": record.status,
                "objective": record.objective,
                "best_bound": record.best_bound,
                "certified_optimal": record.certified_optimal,
                "conditioned_on_uncertified_parent": record.conditioned_on_uncertified_parent,
                "wall_time": record.wall_time,
            }
            for name, record in stage_values.items()
        },
        "dinkelbach_iterations": solution.dinkelbach_iterations,
        "seat_utilization_status": stage_values.get("seat_utilization").status
        if "seat_utilization" in stage_values
        else "NOT_RUN",
        "final_solution_source": (
            "C5 incumbent"
            if stage_values.get("seat_utilization")
            and stage_values["seat_utilization"].status in ("FEASIBLE", "OPTIMAL")
            else "C4 incumbent"
        ),
        "validation": {"independent": report.valid, "solver_equals_delivery": solver_matches},
        "runtime": {
            "master": solution.wall_time,
            "realization_validation": time.perf_counter() - realization_started,
            "total": time.perf_counter() - started,
        },
    }
    summary_path = _artifact(output_dir, "c", "summary", args.quick)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    if not args.quick:
        _publish_formal(output_dir, data_dir, temporary_served, report, solver_matches)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def _publish_formal(output_dir, data_dir, temporary_served, report, solver_matches):
    if not report.valid or not solver_matches:
        raise RuntimeError("formal Stage C is not publishable")
    shutil.copyfile(_artifact(output_dir, "c", "routes", False), output_dir / "q3-routes.csv")
    shutil.copyfile(
        _artifact(output_dir, "c", "assignments", False), output_dir / "q3-assignments.csv"
    )
    shutil.copyfile(_artifact(output_dir, "c", "summary", False), output_dir / "q3-summary.json")
    shutil.copyfile(_artifact(output_dir, "c", "history", False), output_dir / "q3-history.csv")
    final_report = validate_q3_csv(
        routes_path=output_dir / "q3-routes.csv",
        assignments_path=output_dir / "q3-assignments.csv",
        people_path=data_dir / "peopleQ3.csv",
        distances_path=data_dir / "distances.csv",
    )
    if (
        not final_report.valid
        or final_report.metrics.mandatory_served != 3840
        or final_report.metrics.temporary_served != temporary_served
    ):
        raise RuntimeError("published official Q3 CSV failed independent validation")


if __name__ == "__main__":
    raise SystemExit(main())
