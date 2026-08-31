"""Q1 参数敏感性实验：候选池筛选强度 × LNS 轮次 × 时间预算。

正式流水线是确定性的（无随机种子），因此稳定性实验考察的是**参数**而非随机
重复：候选池越大，主问题可行域越大但搜索越慢；LNS 轮次越多，解引导扩池越充分。
每组参数跑一次 `python -m q1`，汇总五项指标与 LP 下界。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

import pandas as pd

from common.paths import Q1_OUTPUT_DIR

EXPERIMENT_DIR = Q1_OUTPUT_DIR / "experiments"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Q1 参数敏感性实验")
    parser.add_argument("--slacks", type=float, nargs="+", default=[0.10, 0.16, 0.24])
    parser.add_argument("--lns-rounds", type=int, nargs="+", default=[1, 4])
    parser.add_argument("--primary-seconds", type=float, default=180.0)
    parser.add_argument("--secondary-seconds", type=float, default=120.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="真正执行；不加该参数只打印实验矩阵。",
    )
    return parser.parse_args()


def _record(slack: float, rounds: int, summary: dict) -> dict:
    return {
        "efficiency_slack": slack,
        "lns_rounds": rounds,
        "pool_columns": summary.get("pool_columns"),
        "T_air": summary.get("T_air"),
        "T_pax": summary.get("T_pax"),
        "fuel": summary.get("fuel"),
        "flights": summary.get("flights"),
        "seat_utilization": summary.get("seat_utilization"),
        "lp_lower_bound": summary.get("lp_lower_bound"),
        "gap_vs_pool_lp": summary.get("optimality_gap_vs_pool_lp"),
        "wall_time": summary.get("wall_time_total"),
    }


def main() -> int:
    args = parse_args()
    matrix = [(slack, rounds) for slack in args.slacks for rounds in args.lns_rounds]
    print(f"实验矩阵（{len(matrix)} 组）: {matrix}")
    if not args.execute:
        print("当前为试运行；确认矩阵后加 --execute 真正执行")
        return 0

    EXPERIMENT_DIR.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    for slack, rounds in matrix:
        output_dir = EXPERIMENT_DIR / f"slack{slack}_lns{rounds}"
        subprocess.run(
            [
                sys.executable, "-m", "q1",
                "--efficiency-slack", str(slack),
                "--lns-rounds", str(rounds),
                "--primary-seconds", str(args.primary_seconds),
                "--secondary-seconds", str(args.secondary_seconds),
                "--workers", str(args.workers),
                "--output-dir", str(output_dir),
            ],
            check=True,
        )
        summary = json.loads((output_dir / "q1-summary.json").read_text(encoding="utf-8"))
        records.append(_record(slack, rounds, summary))
        pd.DataFrame(records).to_csv(EXPERIMENT_DIR / "q1-experiments.csv", index=False)

    frame = pd.DataFrame(records)
    numeric = ["T_air", "T_pax", "fuel", "flights", "seat_utilization", "wall_time"]
    statistics = frame[numeric].agg(["mean", "std", "min", "max"])
    statistics.to_csv(EXPERIMENT_DIR / "q1-experiments-statistics.csv")
    print(statistics)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
