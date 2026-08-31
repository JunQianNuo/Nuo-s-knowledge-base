from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Optional, Sequence

from .feasibility import evaluate_sortie
from .models import (
    AircraftSpec,
    DistanceMap,
    PersonAssignment,
    RequestGroup,
    SortieColumn,
)


@dataclass(frozen=True)
class ValidationReport:
    passed: bool
    violations: tuple[str, ...]

    def __str__(self) -> str:
        if self.passed:
            return "PASS"
        return "FAIL:\n" + "\n".join(f"- {item}" for item in self.violations)


def validate_sortie(
    column: SortieColumn,
    aircraft: AircraftSpec,
    groups: dict[str, RequestGroup],
    distances: DistanceMap,
) -> ValidationReport:
    result = evaluate_sortie(
        base_airport=column.base_airport,
        aircraft=aircraft,
        route=column.route,
        refuel_decisions=column.refuel_decisions,
        allocations=column.allocations,
        groups=groups,
        distances=distances,
    )
    violations = list(result.violations)
    expected = (
        result.aircraft_time,
        result.passenger_time,
        result.fuel_used,
        result.passenger_km,
        result.available_seat_km,
    )
    recorded = (
        column.aircraft_time,
        column.passenger_time,
        column.fuel_used,
        column.passenger_km,
        column.available_seat_km,
    )
    labels = ("飞机时间", "人员时间", "燃油", "PK", "AK")
    for label, actual, stored in zip(labels, expected, recorded):
        if abs(actual - stored) > 1e-6:
            violations.append(f"列 {column.column_id} 的{label}记录值与重算值不一致")
    return ValidationReport(not violations, tuple(violations))


def validate_solution(
    *,
    groups: Sequence[RequestGroup],
    columns: Sequence[SortieColumn],
    multiplicities: dict[str, int],
    aircraft_specs: dict[str, AircraftSpec],
    distances: DistanceMap,
    assignments: Optional[Iterable[PersonAssignment]] = None,
) -> ValidationReport:
    violations: list[str] = []
    group_index = {group.group_id: group for group in groups}
    column_index = {column.column_id: column for column in columns}
    served = Counter()
    for column_id, count in multiplicities.items():
        if count < 0:
            violations.append(f"列 {column_id} 执行次数为负")
            continue
        column = column_index.get(column_id)
        if column is None:
            violations.append(f"解引用未知列: {column_id}")
            continue
        aircraft = aircraft_specs.get(column.aircraft_type)
        if aircraft is None:
            violations.append(f"列 {column_id} 使用未知机型: {column.aircraft_type}")
            continue
        report = validate_sortie(column, aircraft, group_index, distances)
        violations.extend(report.violations)
        for allocation in column.allocations:
            served[allocation.group_id] += allocation.quantity * count
    for group in groups:
        if served[group.group_id] != group.quantity:
            violations.append(
                f"组 {group.group_id} 服务量 {served[group.group_id]} != {group.quantity}"
            )
    if assignments is not None:
        rows = list(assignments)
        person_counts = Counter(row.person_id for row in rows)
        expected_people = {person for group in groups for person in group.person_ids}
        missing = sorted(person for person in expected_people if person_counts[person] == 0)
        duplicate = sorted(person for person, count in person_counts.items() if count > 1)
        extra = sorted(set(person_counts) - expected_people)
        if missing:
            violations.append(f"遗漏人员: {missing[:5]}")
        if duplicate:
            violations.append(f"重复人员: {duplicate[:5]}")
        if extra:
            violations.append(f"未知人员: {extra[:5]}")
        for row in rows:
            column = column_index.get(row.column_id)
            if column is None:
                violations.append(f"人员 {row.person_id} 引用未知列 {row.column_id}")
            elif row.aircraft_type != column.aircraft_type:
                violations.append(f"人员 {row.person_id} 机型外键不一致")
    return ValidationReport(not violations, tuple(dict.fromkeys(violations)))


def validate_q1_csv(*args, **kwargs):
    raise NotImplementedError("Q1 CSV 验证接口已预留，将在正式输出映射阶段实现")


def validate_q2_csv(*args, **kwargs):
    raise NotImplementedError("Q2 CSV 验证接口已预留")


def validate_q3_csv(*args, **kwargs):
    raise NotImplementedError("Q3 CSV 验证接口已预留")
