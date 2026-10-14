import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "code" / "Q1" / "q1_generate_figures.py"
EXPECTED_SOURCE_HASHES = {
    "results/Q1/experiments/round3/tables/comparison.csv":
        "ce4fd627464e3f366fff7da408fc45238f277c53e96dcd61fdc38fd7b8af9074",
    "results/Q1/experiments/round3/tables/operating_characteristics.csv":
        "95e5e297f5118fb06a1529727303a48875a5cd2553f0c3e6bba26aa6a05166c8",
    "robustness/Q1/q1_robustness_summary.json":
        "49736fc3485ab1781cafa562f2d3211bfd04d3e4ddbf9f4d500e0e6b1afc9101",
    "methods/Q1/q1_figure_table_plan.md": "71a66ac7d697d19053c9ece944169f2b535f44043d10bd24cdc869805983b9d4",
}
EXPECTED_FILES = {
    "q1_main_baseline_tradeoff.pdf",
    "q1_main_baseline_tradeoff.png",
    "q1_undecided_probability_near_threshold.pdf",
    "q1_undecided_probability_near_threshold.png",
    "q1_cap_nonnesting_sensitivity.pdf",
    "q1_cap_nonnesting_sensitivity.png",
    "q1_figure_manifest.json",
}


class Q1FigureGeneratorTests(unittest.TestCase):
    def test_submission_figures_match_approved_source_contract(self):
        """Catches missing outputs, wrong source slices, low DPI, or weak captions."""
        self.assertTrue(SCRIPT.is_file(), "production figure generator is missing")
        scratch = ROOT / "scratch"
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as tmp:
            out = Path(tmp) / "figures"
            env = os.environ.copy()
            env["MPLCONFIGDIR"] = str(Path(tmp) / "mplconfig")
            run = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), "--root", str(ROOT),
                 "--output-dir", str(out)],
                cwd=ROOT, env=env, text=True, capture_output=True, check=False,
            )
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertEqual({p.name for p in out.iterdir()}, EXPECTED_FILES)

            manifest = json.loads((out / "q1_figure_manifest.json").read_text(
                encoding="utf-8"))
            self.assertEqual(
                manifest["status"],
                "GENERATED_AUTOMATED_CHECKS_PASSED_VISUAL_INSPECTION_PENDING",
            )
            self.assertFalse(manifest["interpolation"])
            self.assertEqual(manifest["source_sha256"], EXPECTED_SOURCE_HASHES)
            figures = {row["id"]: row for row in manifest["figures"]}
            self.assertEqual(set(figures), {"Q1-T3-F01", "Q1-T3-F02", "Q1-T4-F01"})
            self.assertEqual(figures["Q1-T3-F01"]["source_rows"], 1001)
            self.assertEqual(figures["Q1-T3-F01"]["x_range"], [0.0, 1.0])
            self.assertEqual(figures["Q1-T3-F01"]["near_window_points"], 41)
            self.assertEqual(figures["Q1-T3-F01"]["B1_lower_ASN_points"], 145)
            self.assertEqual(figures["Q1-T3-F02"]["source_rows"], 202)
            self.assertEqual(figures["Q1-T3-F02"]["x_range"], [0.05, 0.15])
            self.assertAlmostEqual(figures["Q1-T3-F02"]["B1_P_U_at_p0"], 0.936410476842364)
            self.assertAlmostEqual(figures["Q1-T3-F02"]["M1_P_U_at_p0"], 0.9649192733664852)
            self.assertEqual(figures["Q1-T4-F01"]["source_rows"], 153)
            self.assertEqual(figures["Q1-T4-F01"]["x_range"], [0.08, 0.13])
            self.assertAlmostEqual(figures["Q1-T4-F01"]["max_increase_theta"], 0.107)
            self.assertAlmostEqual(
                figures["Q1-T4-F01"]["max_increase_1000_to_1100"],
                0.001336920773054917,
            )
            self.assertIn("不能外推", figures["Q1-T3-F01"]["caption"])
            self.assertIn("仍", figures["Q1-T3-F02"]["caption"])
            self.assertIn("不嵌套", figures["Q1-T4-F01"]["caption"])

            for name in EXPECTED_FILES:
                path = out / name
                self.assertGreater(path.stat().st_size, 1000, name)
                if path.suffix == ".png":
                    with Image.open(path) as image:
                        self.assertGreaterEqual(image.width, 2100, name)
                        self.assertGreaterEqual(image.height, 1300, name)
                        dpi = image.info.get("dpi", (0, 0))
                        self.assertGreaterEqual(dpi[0], 299, name)
                        self.assertGreaterEqual(dpi[1], 299, name)
                elif path.suffix == ".pdf":
                    self.assertEqual(path.read_bytes()[:4], b"%PDF", name)

    def test_source_hash_mismatch_is_rejected(self):
        """Catches silently plotting changed evidence under the approved claim."""
        self.assertTrue(SCRIPT.is_file(), "production figure generator is missing")
        spec = importlib.util.spec_from_file_location("q1_generate_figures", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        source = ROOT / "results/Q1/experiments/round3/tables/comparison.csv"
        with self.assertRaisesRegex(ValueError, "Source hash mismatch"):
            module.verify_sha256(source, "0" * 64)


if __name__ == "__main__":
    unittest.main(verbosity=2)
