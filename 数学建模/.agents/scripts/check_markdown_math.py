#!/usr/bin/env python3
"""Check Markdown math delimiters for GitHub/Obsidian compatibility."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


INLINE_CODE = re.compile(r"(`+).*?\1")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
TEX_COMMAND = re.compile(r"\\[A-Za-z]+")
FORMULA_ASSIGNMENT = re.compile(
    r"\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9{}]+)+"
    r"\s*(?:\([^`\n]*\))?\s*="
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    message: str


def markdown_files(paths: Iterable[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.add(path)
        elif path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*.md")
                if ".git" not in candidate.parts
            )
    return sorted(files)


def unescaped_dollar(text: str, index: int) -> bool:
    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 0


def check_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False
    fence_marker = ""
    display_open_line: int | None = None

    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        fence_match = FENCE.match(raw_line)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        line = INLINE_CODE.sub("", raw_line)
        if "\\(" in line or "\\)" in line:
            findings.append(
                Finding(path, line_number, "legacy inline delimiter: use $...$")
            )
        if "\\[" in line or "\\]" in line:
            findings.append(
                Finding(path, line_number, "legacy display delimiter: use $$...$$")
            )
        if re.search(r"\\(?:begin|end)\{equation\*?\}", line):
            findings.append(
                Finding(
                    path,
                    line_number,
                    "raw equation environment: use a $$...$$ display block",
                )
            )

        inline_open = False
        outside_math: list[str] = []
        index = 0
        while index < len(line):
            if line[index] != "$" or not unescaped_dollar(line, index):
                if display_open_line is None and not inline_open:
                    outside_math.append(line[index])
                index += 1
                continue
            if index + 1 < len(line) and line[index + 1] == "$":
                if inline_open:
                    findings.append(
                        Finding(
                            path,
                            line_number,
                            "unmatched dollar delimiter: inline math meets display math",
                        )
                    )
                    inline_open = False
                display_open_line = (
                    None if display_open_line is not None else line_number
                )
                index += 2
                continue
            if display_open_line is None:
                inline_open = not inline_open
            index += 1

        if inline_open:
            findings.append(
                Finding(
                    path,
                    line_number,
                    "unmatched dollar delimiter: inline math must close on the same line",
                )
            )

        outside_text = "".join(outside_math)
        if TEX_COMMAND.search(outside_text) or FORMULA_ASSIGNMENT.search(outside_text):
            findings.append(
                Finding(
                    path,
                    line_number,
                    "unwrapped formula candidate: wrap intended math in $...$ or $$...$$",
                )
            )

    if display_open_line is not None:
        findings.append(
            Finding(
                path,
                display_open_line,
                "unmatched dollar delimiter: display math block is not closed",
            )
        )
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check Markdown for renderer-safe math delimiters."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown files or folders")
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = build_parser().parse_args(argv)
    files = markdown_files(args.paths)
    findings = [finding for path in files for finding in check_file(path)]
    for finding in findings:
        print(f"{finding.path}:{finding.line}: {finding.message}")
    if findings:
        print(f"FAILED: {len(findings)} Markdown math issue(s) in {len(files)} file(s)")
        return 1
    print(f"PASSED: {len(files)} Markdown file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
