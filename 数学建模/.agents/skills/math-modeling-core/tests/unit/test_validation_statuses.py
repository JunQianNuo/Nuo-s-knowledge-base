from __future__ import annotations

import pytest

from mathmodel.contracts import CheckStatus, Severity, ValidationCheck
from mathmodel.validation import aggregate_report


def make_check(
    severity: Severity,
    status: CheckStatus,
    *,
    required: bool = True,
) -> ValidationCheck:
    return ValidationCheck(
        name=f"{severity.value}-{status.value}",
        status=status,
        severity=severity,
        required=required,
    )


@pytest.mark.parametrize(
    ("checks", "expected"),
    [
        ([make_check(Severity.CRITICAL, CheckStatus.FAIL)], CheckStatus.FAIL),
        (
            [make_check(Severity.CRITICAL, CheckStatus.BLOCKED)],
            CheckStatus.BLOCKED,
        ),
        ([make_check(Severity.MAJOR, CheckStatus.FAIL)], CheckStatus.WARN),
        ([make_check(Severity.MINOR, CheckStatus.WARN)], CheckStatus.WARN),
        ([make_check(Severity.CRITICAL, CheckStatus.PASS)], CheckStatus.PASS),
    ],
)
def test_report_status_is_deterministically_aggregated(
    checks: list[ValidationCheck], expected: CheckStatus
) -> None:
    assert aggregate_report(checks).status is expected


def test_critical_failure_precedes_blocked_check() -> None:
    report = aggregate_report(
        [
            make_check(Severity.CRITICAL, CheckStatus.BLOCKED),
            make_check(Severity.CRITICAL, CheckStatus.FAIL),
        ]
    )

    assert report.status is CheckStatus.FAIL


def test_accepted_risk_does_not_rewrite_failure() -> None:
    report = aggregate_report(
        [make_check(Severity.CRITICAL, CheckStatus.FAIL)],
        accepted_risk="user accepted",
    )

    assert report.status is CheckStatus.FAIL
    assert report.accepted_risk == "user accepted"


def test_empty_required_check_set_is_blocked() -> None:
    assert aggregate_report([]).status is CheckStatus.BLOCKED
