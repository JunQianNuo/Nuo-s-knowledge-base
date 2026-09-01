from __future__ import annotations

from collections.abc import Sequence

from mathmodel.contracts import (
    CheckStatus,
    Severity,
    ValidationCheck,
    ValidationReport,
)


def aggregate_report(
    checks: Sequence[ValidationCheck],
    *,
    accepted_risk: str | None = None,
) -> ValidationReport:
    normalized = tuple(checks)
    if not normalized:
        return ValidationReport(
            status=CheckStatus.BLOCKED,
            checks=(),
            accepted_risk=accepted_risk,
            rollback_stage="validation",
        )

    critical_failure = next(
        (
            check
            for check in normalized
            if check.severity is Severity.CRITICAL
            and check.status is CheckStatus.FAIL
        ),
        None,
    )
    if critical_failure is not None:
        status = CheckStatus.FAIL
        rollback_stage = critical_failure.rollback_stage
    else:
        required_block = next(
            (
                check
                for check in normalized
                if check.required
                and check.status in {CheckStatus.BLOCKED, CheckStatus.SKIPPED}
            ),
            None,
        )
        if required_block is not None:
            status = CheckStatus.BLOCKED
            rollback_stage = required_block.rollback_stage
        elif any(
            check.status in {CheckStatus.WARN, CheckStatus.FAIL, CheckStatus.BLOCKED}
            for check in normalized
        ):
            status = CheckStatus.WARN
            rollback_stage = None
        else:
            status = CheckStatus.PASS
            rollback_stage = None

    return ValidationReport(
        status=status,
        checks=normalized,
        accepted_risk=accepted_risk,
        rollback_stage=rollback_stage,
    )
