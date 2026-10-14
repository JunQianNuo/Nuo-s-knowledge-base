from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / ".agents" / "scripts" / "check_markdown_math.py"


def run_checker(
    tmp_path: Path, content: str, filename: str = "sample.md"
) -> subprocess.CompletedProcess[str]:
    markdown = tmp_path / filename
    markdown.write_text(content, encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(CHECKER), str(markdown)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def test_accepts_cross_renderer_math_and_ignores_code_examples(tmp_path: Path) -> None:
    result = run_checker(
        tmp_path,
        """Inline $x^2$ and currency \\$20.

$$
E[X] = \\sum_i x_i p_i
$$

`legacy example: \\(x\\)`

```markdown
\\[legacy display example\\]
```
""",
    )

    assert result.returncode == 0, (result.stdout or "") + (result.stderr or "")


def test_rejects_legacy_tex_delimiters_outside_code(tmp_path: Path) -> None:
    result = run_checker(
        tmp_path,
        """Bad inline \\(x^2\\).

\\[
y = 2x
\\]
""",
    )

    assert result.returncode == 1
    assert "legacy inline delimiter" in result.stdout
    assert "legacy display delimiter" in result.stdout


def test_rejects_raw_equation_environment(tmp_path: Path) -> None:
    result = run_checker(
        tmp_path,
        """\\begin{equation}
x = 1
\\end{equation}
""",
    )

    assert result.returncode == 1
    assert "raw equation environment" in result.stdout


def test_rejects_unmatched_dollar_math_delimiter(tmp_path: Path) -> None:
    result = run_checker(tmp_path, "Broken inline $x^2.\n")

    assert result.returncode == 1
    assert "unmatched dollar delimiter" in result.stdout


def test_rejects_unwrapped_formula_notation(tmp_path: Path) -> None:
    result = run_checker(
        tmp_path,
        """P_D(X_n=x)=C(D,x)C(N-D,n-x)/C(N,n).
The threshold is \\theta=0.10.
""",
    )

    assert result.returncode == 1
    assert result.stdout.count("unwrapped formula candidate") == 2


def test_reports_unicode_markdown_paths_as_utf8(tmp_path: Path) -> None:
    result = run_checker(tmp_path, "Bad \\(x\\).\n", filename="公式.md")

    assert result.returncode == 1
    assert "公式.md" in result.stdout
