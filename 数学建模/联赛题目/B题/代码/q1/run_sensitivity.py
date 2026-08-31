"""Q1 refuel-candidate sensitivity runs isolated from formal outputs."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import pandas as pd

from common.paths import Q1_OUTPUT_DIR


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Q1 refuel_keep sensitivity")
    parser.add_argument("--refuel-keeps", type=int, nargs="+", default=(4, 8))
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Q1_OUTPUT_DIR / "sensitivity")
    return parser.parse_args(argv)


def _record(refuel_keep: int, summary: dict) -> dict:
    return {
        "refuel_keep": refuel_keep,
        "candidate_pool_size": summary["pool_columns"],
        "T_air": summary["T_air"],
        "T_pax": summary["T_pax"],
        "fuel": summary["fuel"],
        "flights": summary["flights"],
        "utilization": summary["seat_utilization"],
        "runtime": summary["wall_time_total"],
        "seed": summary["seed"],
        "validator": "PASS",
    }


def main(argv=None) -> int:
    args = parse_args(argv)
    matrix = list(dict.fromkeys(args.refuel_keeps))
    print(f"Q1 sensitivity: refuel_keep={matrix}, seed={args.seed}")
    if not args.execute:
        print("dry-run; add --execute to run isolated validated solves")
        return 0
    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for keep in matrix:
        run_dir = args.output_dir / f"refuel_keep_{keep}"
        command = [
            sys.executable,
            "-m",
            "q1",
            "--workers",
            str(args.workers),
            "--seed",
            str(args.seed),
            "--refuel-keep",
            str(keep),
            "--output-dir",
            str(run_dir),
        ]
        if args.quick:
            command.append("--quick")
        subprocess.run(command, check=True)
        summary = json.loads((run_dir / "q1-summary.json").read_text(encoding="utf-8"))
        records.append(_record(keep, summary))
        pd.DataFrame(records).to_csv(args.output_dir / "sensitivity_q1.csv", index=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
