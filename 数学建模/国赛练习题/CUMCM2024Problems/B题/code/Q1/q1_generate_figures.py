"""Generate the approved Q1 submission figures from verified round3 evidence."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault(
    "MPLCONFIGDIR", str(DEFAULT_ROOT / "scratch" / "q1_matplotlib_cache")
)

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from mpl_toolkits.axes_grid1.inset_locator import inset_axes  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402


EXPECTED_SOURCE_HASHES = {
    "results/Q1/experiments/round3/tables/comparison.csv":
        "ce4fd627464e3f366fff7da408fc45238f277c53e96dcd61fdc38fd7b8af9074",
    "results/Q1/experiments/round3/tables/operating_characteristics.csv":
        "95e5e297f5118fb06a1529727303a48875a5cd2553f0c3e6bba26aa6a05166c8",
    "robustness/Q1/q1_robustness_summary.json":
        "49736fc3485ab1781cafa562f2d3211bfd04d3e4ddbf9f4d500e0e6b1afc9101",
    "methods/Q1/q1_figure_table_plan.md":
        "71a66ac7d697d19053c9ece944169f2b535f44043d10bd24cdc869805983b9d4",
}

FIGURE_STEMS = (
    "q1_main_baseline_tradeoff",
    "q1_undecided_probability_near_threshold",
    "q1_cap_nonnesting_sensitivity",
)

BLUE = "#1A6FC4"
GREY = "#767676"
GREEN = "#2E9E44"
RED = "#E53935"
TEXT = "#333333"
GRID = "#D8D8D8"
WINDOW = "#DCEBFA"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_sha256(path: Path, expected: str) -> str:
    actual = sha256_file(path)
    if actual.lower() != expected.lower():
        raise ValueError(
            f"Source hash mismatch for {path}: expected {expected}, got {actual}"
        )
    return actual


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def configure_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Microsoft YaHei", "SimHei", "DejaVu Sans"],
            "font.size": 9.5,
            "axes.titlesize": 11,
            "axes.labelsize": 10,
            "axes.edgecolor": TEXT,
            "axes.labelcolor": TEXT,
            "axes.titlecolor": TEXT,
            "xtick.color": TEXT,
            "ytick.color": TEXT,
            "text.color": TEXT,
            "legend.frameon": False,
            "axes.unicode_minus": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
        }
    )


def style_axis(axis: plt.Axes) -> None:
    axis.grid(True, color=GRID, linewidth=0.65, alpha=0.75)
    axis.set_axisbelow(True)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)


def save_figure(fig: plt.Figure, output_dir: Path, stem: str, title: str) -> None:
    fig.savefig(
        output_dir / f"{stem}.png",
        dpi=300,
        bbox_inches="tight",
        metadata={"Software": "q1_generate_figures.py"},
    )
    fig.savefig(
        output_dir / f"{stem}.pdf",
        bbox_inches="tight",
        metadata={"Creator": "q1_generate_figures.py", "Title": title},
    )
    plt.close(fig)


def plot_tradeoff(
    rows: list[dict[str, str]], output_dir: Path
) -> dict[str, Any]:
    selected = sorted(
        (row for row in rows if int(row["cap"]) == 1000),
        key=lambda row: float(row["theta"]),
    )
    if len(selected) != 1001:
        raise ValueError(f"Expected 1001 comparison rows, got {len(selected)}")

    theta = np.array([float(row["theta"]) for row in selected])
    delta_asn = np.array([float(row["ASN_B1_minus_M1"]) for row in selected])
    delta_pu = np.array([float(row["P_U_B1_minus_M1"]) for row in selected])
    near = (theta >= 0.08 - 1e-12) & (theta <= 0.12 + 1e-12)
    local = (theta >= 0.05 - 1e-12) & (theta <= 0.15 + 1e-12)

    fig, axes = plt.subplots(2, 1, figsize=(7.2, 6.0), sharex=True)
    specs = (
        (axes[0], delta_asn, r"$\Delta\,\mathrm{ASN}$（件）", "ASN"),
        (axes[1], delta_pu, r"$\Delta P_U$", r"$P_U$"),
    )
    for axis, values, label, short_label in specs:
        style_axis(axis)
        axis.axvspan(0.08, 0.12, color=WINDOW, alpha=0.75, linewidth=0)
        axis.axhline(0, color=TEXT, linewidth=0.9)
        axis.axvline(0.10, color=BLUE, linewidth=1.0, linestyle=":")
        axis.plot(theta, values, color=GREY, linewidth=1.6)
        axis.fill_between(
            theta, values, 0, where=values <= 0, color=GREEN, alpha=0.20,
            interpolate=False, label="B1较低",
        )
        axis.fill_between(
            theta, values, 0, where=values > 0, color=RED, alpha=0.16,
            interpolate=False, label="B1较高",
        )
        axis.set_ylabel(label)
        axis.set_xlim(0.0, 1.0)

        inset = inset_axes(
            axis, width="33%", height="45%", loc="upper right", borderpad=1.0
        )
        inset.axvspan(0.08, 0.12, color=WINDOW, alpha=0.75, linewidth=0)
        inset.axhline(0, color=TEXT, linewidth=0.7)
        inset.axvline(0.10, color=BLUE, linewidth=0.8, linestyle=":")
        inset.plot(theta[local], values[local], color=GREY, linewidth=1.15)
        inset.fill_between(
            theta[local], values[local], 0, where=values[local] <= 0,
            color=GREEN, alpha=0.20,
        )
        inset.fill_between(
            theta[local], values[local], 0, where=values[local] > 0,
            color=RED, alpha=0.16,
        )
        inset.set_xlim(0.05, 0.15)
        inset.tick_params(labelsize=7, pad=1)
        inset.set_title(f"阈值附近：{short_label}", fontsize=7.5, pad=2)
        inset.grid(True, color=GRID, linewidth=0.45, alpha=0.65)

    axes[0].set_title("B1 相对 M1 的效率—未决权衡（主预算 1000）")
    axes[0].legend(loc="lower right", ncol=2, fontsize=8)
    axes[1].set_xlabel(r"真实次品率 $\theta$")
    fig.text(
        0.51, 0.012,
        "负值表示 B1 指标较低；蓝色阴影为 8%—12% 展示窗口。",
        ha="center", va="bottom", fontsize=8.5,
    )
    fig.subplots_adjust(
        left=0.12, right=0.98, top=0.94, bottom=0.11, hspace=0.13
    )
    save_figure(
        fig, output_dir, FIGURE_STEMS[0], "B1 相对 M1 的效率—未决权衡"
    )

    return {
        "id": "Q1-T3-F01",
        "files": [f"{FIGURE_STEMS[0]}.pdf", f"{FIGURE_STEMS[0]}.png"],
        "source_rows": len(selected),
        "x_range": [float(theta.min()), float(theta.max())],
        "near_window_points": int(near.sum()),
        "B1_lower_ASN_points": int((delta_asn < 0).sum()),
        "claim_id": "C-Q1-02",
        "caption": (
            "主预算1000下，8%--12%的41个网格点上 B1 的 ASN 与未决率均低于 M1；"
            "但全区间仅145点的 ASN 更低，且未提供真实次品率权重，不能外推为全局优势。"
        ),
    }


def plot_undecided(
    rows: list[dict[str, str]], output_dir: Path
) -> dict[str, Any]:
    selected = sorted(
        (
            row for row in rows
            if int(row["cap"]) == 1000
            and row["method_id"] in {"B1", "M1"}
            and 0.05 - 1e-12 <= float(row["theta"]) <= 0.15 + 1e-12
        ),
        key=lambda row: (row["method_id"], float(row["theta"])),
    )
    if len(selected) != 202:
        raise ValueError(
            f"Expected 202 threshold-window rows, got {len(selected)}"
        )
    by_method = {
        method: sorted(
            (row for row in selected if row["method_id"] == method),
            key=lambda row: float(row["theta"]),
        )
        for method in ("B1", "M1")
    }
    theta = np.array([float(row["theta"]) for row in by_method["B1"]])
    b1 = np.array([float(row["P_U"]) for row in by_method["B1"]])
    m1 = np.array([float(row["P_U"]) for row in by_method["M1"]])
    p0_index = int(np.flatnonzero(np.isclose(theta, 0.10, atol=1e-12))[0])
    b1_p0, m1_p0 = float(b1[p0_index]), float(m1[p0_index])

    fig, axis = plt.subplots(figsize=(7.2, 4.8))
    style_axis(axis)
    axis.axvspan(0.08, 0.12, color=WINDOW, alpha=0.75, linewidth=0)
    axis.axhline(
        0.9, color=TEXT, linewidth=0.85, linestyle=":",
        label=r"描述性参考 $P_U=0.9$",
    )
    axis.axvline(0.10, color=BLUE, linewidth=1.0, linestyle=":")
    axis.plot(theta, b1, color=BLUE, linewidth=2.0, label="B1（主方法）")
    axis.plot(
        theta, m1, color=GREY, linewidth=1.8, linestyle="--",
        label="M1（基线）",
    )
    axis.scatter([0.10], [b1_p0], color=BLUE, s=28, zorder=4)
    axis.scatter([0.10], [m1_p0], color=GREY, s=28, zorder=4)
    axis.annotate(
        f"B1: {b1_p0:.5f}", xy=(0.10, b1_p0), xytext=(0.103, 0.77),
        fontsize=8.5, color=BLUE,
        arrowprops={"arrowstyle": "-", "color": BLUE, "linewidth": 0.8},
    )
    axis.annotate(
        f"M1: {m1_p0:.5f}", xy=(0.10, m1_p0), xytext=(0.119, 0.965),
        fontsize=8.5, color=GREY,
        arrowprops={"arrowstyle": "-", "color": GREY, "linewidth": 0.8},
    )
    axis.set_xlim(0.05, 0.15)
    axis.set_ylim(0.0, 1.02)
    axis.set_xlabel(r"真实次品率 $\theta$")
    axis.set_ylabel(r"未决概率 $P_U(\theta)$")
    axis.set_title("阈值附近的绝对未决概率（主预算 1000）")
    axis.legend(
        loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=3, fontsize=8.5
    )
    fig.subplots_adjust(left=0.10, right=0.98, top=0.92, bottom=0.22)
    save_figure(
        fig, output_dir, FIGURE_STEMS[1], "阈值附近的绝对未决概率"
    )

    return {
        "id": "Q1-T3-F02",
        "files": [f"{FIGURE_STEMS[1]}.pdf", f"{FIGURE_STEMS[1]}.png"],
        "source_rows": len(selected),
        "x_range": [float(theta.min()), float(theta.max())],
        "B1_P_U_at_p0": b1_p0,
        "M1_P_U_at_p0": m1_p0,
        "claim_id": "C-Q1-03",
        "caption": (
            "B1 的高未决带较 M1 更窄，但在 theta=0.10 时未决概率仍为0.93641；"
            "0.9仅是描述性集中阈值，不是人工验收标准。"
        ),
    }


def plot_cap_sensitivity(
    rows: list[dict[str, str]],
    robustness: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    selected = sorted(
        (
            row for row in rows
            if row["method_id"] == "B1"
            and int(row["cap"]) in {900, 1000, 1100}
            and 0.08 - 1e-12 <= float(row["theta"]) <= 0.13 + 1e-12
        ),
        key=lambda row: (int(row["cap"]), float(row["theta"])),
    )
    if len(selected) != 153:
        raise ValueError(f"Expected 153 cap-sensitivity rows, got {len(selected)}")
    by_cap = {
        cap: sorted(
            (row for row in selected if int(row["cap"]) == cap),
            key=lambda row: float(row["theta"]),
        )
        for cap in (900, 1000, 1100)
    }
    theta = np.array([float(row["theta"]) for row in by_cap[1000]])
    pu = {
        cap: np.array([float(row["P_U"]) for row in by_cap[cap]])
        for cap in (900, 1000, 1100)
    }
    delta_900 = pu[900] - pu[1000]
    delta_1100 = pu[1100] - pu[1000]
    max_index = int(np.argmax(delta_1100))
    max_theta = float(theta[max_index])
    max_increase = float(delta_1100[max_index])
    robust_observed = next(
        check["observed"] for check in robustness["checks"]
        if check["id"] == "terminal_schedule_discreteness"
    )["maximum_P_U_increase_1000_to_1100"]
    if not (
        abs(max_theta - float(robust_observed["theta"])) < 1e-12
        and abs(max_increase - float(robust_observed["increase"])) < 1e-12
    ):
        raise ValueError("Cap sensitivity does not match robustness summary")

    fig, axis = plt.subplots(figsize=(7.2, 4.8))
    style_axis(axis)
    axis.axhline(0, color=TEXT, linewidth=0.9)
    axis.plot(
        theta, delta_900, color=GREY, linewidth=1.8, linestyle="--",
        label=r"$P_U^{(900)}-P_U^{(1000)}$",
    )
    axis.plot(
        theta, delta_1100, color=BLUE, linewidth=2.0,
        label=r"$P_U^{(1100)}-P_U^{(1000)}$",
    )
    axis.scatter([max_theta], [max_increase], color=RED, s=30, zorder=4)
    axis.annotate(
        rf"$\theta={max_theta:.3f}$" + f"\n+{max_increase:.6f}",
        xy=(max_theta, max_increase), xytext=(0.111, 0.032), fontsize=8.5,
        arrowprops={"arrowstyle": "-", "color": RED, "linewidth": 0.8},
    )
    axis.set_xlim(0.08, 0.13)
    axis.set_xlabel(r"真实次品率 $\theta$")
    axis.set_ylabel("相对主预算1000的未决概率差")
    axis.set_title("不同检测上限下的非嵌套末次检查效应（B1）")
    axis.legend(loc="lower left", fontsize=8.5)
    fig.tight_layout(pad=1.0)
    save_figure(
        fig, output_dir, FIGURE_STEMS[2], "检测上限非嵌套敏感性"
    )

    return {
        "id": "Q1-T4-F01",
        "files": [f"{FIGURE_STEMS[2]}.pdf", f"{FIGURE_STEMS[2]}.png"],
        "source_rows": len(selected),
        "x_range": [float(theta.min()), float(theta.max())],
        "max_increase_theta": max_theta,
        "max_increase_1000_to_1100": max_increase,
        "claim_id": "C-Q1-04",
        "caption": (
            "三种方案均为8次检查并使用相同逐次错误预算，但末次检查点不同，因而方案不嵌套；"
            "theta=0.107处的局部正差不能表述为增加上限一般会增加未决率。"
        ),
    }


def inspect_output(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "path": path.name,
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }
    if path.suffix == ".png":
        with Image.open(path) as image:
            dpi = image.info.get("dpi", (0.0, 0.0))
            result.update(
                {
                    "width_px": image.width,
                    "height_px": image.height,
                    "dpi": [round(float(dpi[0]), 3), round(float(dpi[1]), 3)],
                }
            )
            if image.width < 2100 or image.height < 1300 or min(dpi) < 299:
                raise ValueError(
                    f"PNG output does not meet submission resolution: {path}"
                )
    elif path.read_bytes()[:4] != b"%PDF":
        raise ValueError(f"Invalid PDF output: {path}")
    if result["bytes"] <= 1000:
        raise ValueError(f"Suspiciously small output: {path}")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    output_dir = (args.output_dir or root / "paper" / "figures").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_outputs = [
        output_dir / f"{stem}.{suffix}"
        for stem in FIGURE_STEMS for suffix in ("pdf", "png")
    ] + [output_dir / "q1_figure_manifest.json"]
    existing = [path for path in expected_outputs if path.exists()]
    if existing and not args.overwrite:
        raise FileExistsError(
            "Refusing to overwrite existing outputs: "
            + ", ".join(path.name for path in existing)
        )

    source_paths = {
        relative: root / relative for relative in EXPECTED_SOURCE_HASHES
    }
    verified_hashes = {
        relative: verify_sha256(source_paths[relative], expected)
        for relative, expected in EXPECTED_SOURCE_HASHES.items()
    }
    comparison = read_csv(
        root / "results/Q1/experiments/round3/tables/comparison.csv"
    )
    operating = read_csv(
        root / "results/Q1/experiments/round3/tables/operating_characteristics.csv"
    )
    robustness = json.loads(
        (root / "robustness/Q1/q1_robustness_summary.json").read_text(
            encoding="utf-8"
        )
    )

    configure_style()
    figures = [
        plot_tradeoff(comparison, output_dir),
        plot_undecided(operating, output_dir),
        plot_cap_sensitivity(operating, robustness, output_dir),
    ]
    output_checks = [inspect_output(path) for path in expected_outputs[:-1]]
    manifest = {
        "schema_version": 1,
        "question_id": "Q1",
        "generated_by": "code/Q1/q1_generate_figures.py",
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(),
        "status": "GENERATED_AUTOMATED_CHECKS_PASSED_VISUAL_INSPECTION_PENDING",
        "rigor_profile": "submission",
        "decision_id": "q1_final_result_verdict_v2",
        "figure_plan": "methods/Q1/q1_figure_table_plan.md",
        "interpolation": False,
        "source_sha256": verified_hashes,
        "environment": {
            "python": platform.python_version(),
            "matplotlib": matplotlib.__version__,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "style_contract": {
            "main_method": {"id": "B1", "color": BLUE, "line": "solid"},
            "baseline": {"id": "M1", "color": GREY, "line": "dashed"},
            "dpi": 300,
            "paper_format": "vector PDF",
        },
        "figures": figures,
        "output_checks": output_checks,
        "limitations": [
            "The theta grid has no supplied population weights.",
            "The 0.9 line is descriptive, not an acceptance criterion.",
            "Cap schedules are nonnested, so no general cap monotonicity is claimed.",
        ],
    }
    (output_dir / "q1_figure_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
