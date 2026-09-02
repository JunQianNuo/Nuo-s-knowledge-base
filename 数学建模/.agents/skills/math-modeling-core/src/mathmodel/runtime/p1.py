from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Any, Callable

import numpy as np

from mathmodel.algorithms import AlgorithmPlugin, SupportStatus
from mathmodel.contracts import (
    CheckStatus,
    DataBundle,
    ProblemSpec,
    RunStatus,
    SolveConfig,
    SolveResult,
)

from .dependencies import check_dependencies


@dataclass(frozen=True, slots=True)
class P1Report:
    plugin_id: str
    status: CheckStatus
    passed_checks: tuple[str, ...]
    reasons: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class _P1Case:
    data: DataBundle
    oracle: Callable[[SolveResult], bool]


def run_p1(plugin: AlgorithmPlugin) -> P1Report:
    """Run a tiny known-answer case before exposing a plugin to full data."""
    plugin_id = plugin.metadata.plugin_id
    case = _cases().get(plugin_id)
    if case is None:
        return P1Report(plugin_id, CheckStatus.BLOCKED, (), ("p1_case_missing",))

    dependency_report = check_dependencies(plugin.metadata.dependencies)
    if dependency_report.missing:
        return P1Report(
            plugin_id,
            CheckStatus.BLOCKED,
            (),
            tuple(f"missing_dependency:{item}" for item in dependency_report.missing),
        )

    required_outputs = tuple(
        field.name for field in plugin.metadata.io_contract.output_fields if field.required
    )
    family = min(plugin.metadata.model_families)
    problem = ProblemSpec(
        problem_id=f"p1-{plugin_id}",
        model_family=family,
        mandatory_outputs=required_outputs,
    )
    config = SolveConfig(seed=7, max_iterations=2_000)
    passed: list[str] = ["dependencies"]
    reasons = list(plugin.metadata.io_contract.validate_inputs(case.data))
    reasons.extend(plugin.metadata.io_contract.validate_config(config))
    if reasons:
        return P1Report(plugin_id, CheckStatus.FAIL, tuple(passed), tuple(reasons))
    passed.extend(("input_contract", "config_contract"))

    support = plugin.supports(problem, case.data)
    if support.status is not SupportStatus.SUPPORTED:
        return P1Report(
            plugin_id,
            CheckStatus.FAIL,
            tuple(passed),
            support.reasons or (f"support:{support.status.value}",),
        )
    passed.append("support")
    try:
        result = plugin.solve(problem, case.data, config)
    except Exception as exc:
        return P1Report(
            plugin_id,
            CheckStatus.FAIL,
            tuple(passed),
            (f"p1_exception:{type(exc).__name__}:{exc}",),
        )
    if result.status is not RunStatus.SUCCESS:
        return P1Report(
            plugin_id,
            CheckStatus.FAIL,
            tuple(passed),
            (f"p1_run_status:{result.status.value}",),
        )
    passed.append("run_status")
    output_reasons = plugin.metadata.io_contract.validate_output(result)
    if output_reasons:
        return P1Report(
            plugin_id, CheckStatus.FAIL, tuple(passed), output_reasons
        )
    passed.append("output_contract")
    if result.validation_report and result.validation_report.status in {
        CheckStatus.FAIL,
        CheckStatus.BLOCKED,
        CheckStatus.SKIPPED,
    }:
        return P1Report(
            plugin_id,
            CheckStatus.FAIL,
            tuple(passed),
            (f"p1_validation:{result.validation_report.status.value}",),
        )
    passed.append("plugin_validation")
    if not case.oracle(result):
        return P1Report(
            plugin_id,
            CheckStatus.FAIL,
            tuple(passed),
            ("known_answer_mismatch",),
        )
    passed.append("known_answer")
    return P1Report(plugin_id, CheckStatus.PASS, tuple(passed), ())


def _cases() -> dict[str, _P1Case]:
    x_supervised = np.array([[0.0], [1.0], [2.0], [3.0]])
    y_supervised = 1.0 + 2.0 * x_supervised[:, 0]
    supervised = DataBundle(
        arrays={
            "X": x_supervised,
            "y": y_supervised,
            "X_predict": np.array([[4.0]]),
        }
    )
    return {
        "evaluation.ahp": _P1Case(
            DataBundle(arrays={"pairwise": np.array([[1.0, 2.0], [0.5, 1.0]])}),
            lambda result: np.allclose(result.solution["weights"], [2 / 3, 1 / 3]),
        ),
        "evaluation.entropy-weight": _P1Case(
            DataBundle(
                arrays={
                    "decision_matrix": np.array(
                        [[1.0, 5.0], [2.0, 5.0], [4.0, 5.0]]
                    )
                }
            ),
            lambda result: np.allclose(result.solution["weights"], [1.0, 0.0]),
        ),
        "evaluation.topsis": _P1Case(
            DataBundle(
                arrays={
                    "decision_matrix": np.array([[1.0, 3.0], [3.0, 1.0]]),
                    "weights": np.array([0.5, 0.5]),
                },
                metadata={"directions": ("benefit", "cost")},
            ),
            lambda result: result.solution["rank"] == [1, 0],
        ),
        "graph.dijkstra": _P1Case(
            DataBundle(
                tables={
                    "graph": {
                        "s": {"a": 1.0, "t": 4.0},
                        "a": {"t": 1.0},
                        "t": {},
                    }
                },
                scalars={"source": "s", "target": "t"},
            ),
            lambda result: result.solution["path"] == ["s", "a", "t"]
            and np.isclose(result.solution["distance"], 2.0),
        ),
        "graph.edmonds-karp": _P1Case(
            DataBundle(
                tables={
                    "capacities": {"s": {"a": 2.0}, "a": {"t": 2.0}, "t": {}}
                },
                scalars={"source": "s", "sink": "t"},
            ),
            lambda result: np.isclose(result.solution["min_cut_value"], 2.0),
        ),
        "mechanistic.solve-ivp": _P1Case(
            DataBundle(
                arrays={"y0": np.array([1.0]), "t_eval": np.linspace(0.0, 1.0, 5)},
                scalars={"t0": 0.0, "t1": 1.0},
                metadata={"rhs": lambda _time, state: state},
            ),
            lambda result: np.isclose(
                np.asarray(result.solution["state"])[0, -1], exp(1.0), rtol=1e-4
            ),
        ),
        "optimization.linear-programming": _P1Case(
            DataBundle(
                arrays={"c": np.array([-1.0])}, metadata={"bounds": [(0.0, 1.0)]}
            ),
            lambda result: np.allclose(result.solution["x"], [1.0])
            and np.isclose(result.objective, -1.0),
        ),
        "optimization.mixed-integer-linear-programming": _P1Case(
            DataBundle(
                arrays={
                    "values": np.array([2.0, 3.0]),
                    "weights": np.array([1.0, 2.0]),
                },
                scalars={"capacity": 2.0},
            ),
            lambda result: np.allclose(result.solution["x"], [0.0, 1.0])
            and np.isclose(result.objective, 3.0),
        ),
        "optimization.nonlinear": _P1Case(
            DataBundle(
                arrays={"x0": np.array([0.0])},
                metadata={"objective": lambda vector: (vector[0] - 2.0) ** 2},
            ),
            lambda result: np.allclose(result.solution["x"], [2.0], atol=1e-5),
        ),
        "prediction.arima": _P1Case(
            DataBundle(
                arrays={
                    "series": np.array([1.0, 1.2, 1.1, 1.3, 1.25, 1.4, 1.35, 1.5])
                },
                scalars={"horizon": 2},
                metadata={"order": (1, 0, 0)},
            ),
            lambda result: len(result.solution["forecast"]) == 2
            and np.all(np.isfinite(result.solution["forecast"])),
        ),
        "prediction.linear-regression": _P1Case(
            supervised,
            lambda result: np.allclose(result.solution["predictions"], [9.0]),
        ),
        "prediction.ridge-regression": _P1Case(
            DataBundle(
                arrays=supervised.arrays,
                scalars={"alpha": 0.0},
            ),
            lambda result: np.allclose(result.solution["predictions"], [9.0]),
        ),
        "prediction.random-forest": _P1Case(
            DataBundle(
                arrays={
                    "X": np.array([[-2.0], [-1.0], [1.0], [2.0]]),
                    "y": np.array([0, 0, 1, 1]),
                    "X_predict": np.array([[-1.5], [1.5]]),
                },
                scalars={"n_estimators": 20},
                metadata={"task": "classification"},
            ),
            lambda result: result.solution["predictions"] == [0, 1],
        ),
        "simulation.monte-carlo": _P1Case(
            DataBundle(
                arrays={"bounds": np.array([[0.0, 1.0]])},
                scalars={"n_samples": 20_000, "confidence": 0.95},
                metadata={"integrand": lambda points: points[:, 0]},
            ),
            lambda result: abs(result.solution["estimate"] - 0.5) < 0.02
            and result.solution["ci_low"] < 0.5 < result.solution["ci_high"],
        ),
        "statistics.pca": _P1Case(
            DataBundle(
                arrays={"X": np.array([[2.0, 0.0], [-2.0, 0.0], [0.0, 1.0], [0.0, -1.0]])},
                scalars={"n_components": 2},
            ),
            lambda result: np.allclose(
                np.asarray(result.solution["components"])
                @ np.asarray(result.solution["components"]).T,
                np.eye(2),
            ),
        ),
    }
