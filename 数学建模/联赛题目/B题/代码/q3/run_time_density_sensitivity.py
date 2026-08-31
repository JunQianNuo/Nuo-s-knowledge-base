"""Q3 critical-start density sensitivity with isolated validated pipelines."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import pandas as pd

from common.paths import CODE_ROOT


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Q3 time-column density sensitivity")
    parser.add_argument(
        "--densities", nargs="+", choices=("baseline", "dense"), default=("baseline", "dense")
    )
    parser.add_argument("--seed", type=int, default=20260815)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument(
        "--output-dir", type=Path, default=CODE_ROOT / "q3" / "outputs" / "sensitivity"
    )
    return parser.parse_args(argv)


def _run_stage(args, density, run_dir, stage):
    command = [
        sys.executable,
        "-m",
        "q3",
        f"--stage-{stage}",
        "--workers",
        str(args.workers),
        "--seed",
        str(args.seed),
        "--time-sampling-density",
        density,
        "--output-dir",
        str(run_dir),
    ]
    if args.quick:
        command.append("--quick")
    baseline_dir = args.output_dir / "baseline"
    if stage == "a" and density != "baseline" and baseline_dir.is_dir():
        command.extend(("--stage-a-hint-dir", str(baseline_dir)))
    subprocess.run(command, check=True)


def _summary_path(run_dir, stage, quick):
    prefix = "" if quick else "formal_"
    return run_dir / f"{prefix}stage_{stage}_summary.json"


def main(argv=None) -> int:
    args = parse_args(argv)
    print(f"Q3 density sensitivity: {args.densities}, seed={args.seed}")
    if not args.execute and not args.collect_only:
        print("dry-run; add --execute to run or --collect-only to rebuild the summary")
        return 0
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_csv = args.output_dir / "time_density_sensitivity.csv"
    records = (
        pd.read_csv(summary_csv).to_dict("records") if summary_csv.is_file() else []
    )
    for density in args.densities:
        run_dir = args.output_dir / density
        if args.execute:
            for stage in "abc":
                _run_stage(args, density, run_dir, stage)
        a = json.loads(_summary_path(run_dir, "a", args.quick).read_text(encoding="utf-8"))
        b = json.loads(_summary_path(run_dir, "b", args.quick).read_text(encoding="utf-8"))
        c = json.loads(_summary_path(run_dir, "c", args.quick).read_text(encoding="utf-8"))
        if not all(item["validation"]["independent"] for item in (a, b, c)):
            raise RuntimeError(f"{density} sensitivity pipeline did not validate")
        records = [row for row in records if row["time_sampling_density"] != density]
        records.append(
            {
                "time_sampling_density": density,
                "timed_columns": a["timed_columns"],
                "service_options": a["service_options"],
                "StageA_T_air": a["T_air"],
                "StageB_temporary_served": b["temporary_served"],
                "StageC_T_air": c["T_air"],
                "StageC_T_pax": c["T_pax"],
                "StageC_fuel": c["fuel"],
                "StageC_flights": c["flights"],
                "StageC_utilization": c["utilization"],
                "runtime": sum(item["runtime"]["total"] for item in (a, b, c)),
                "seed": args.seed,
                "validator": "PASS",
            }
        )
        pd.DataFrame(records).sort_values("time_sampling_density").to_csv(
            summary_csv, index=False
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
