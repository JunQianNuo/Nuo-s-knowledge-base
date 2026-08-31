"""只读扫描 Obsidian 仓库并生成质量审查报告。"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
SKIP_DIRECTORIES = {
    ".git",
    ".obsidian",
    ".claude",
    ".claudian",
    ".agents",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
    ".playwright",
    ".playwright-cli",
    ".codex-tmp",
    ".superpowers",
}
PENDING_DIRECTORIES = {"未处理", "未处理项"}
MAX_REPORT_ITEMS = 200
GENERATED_AUDIT_DIRECTORY = ("总览", "审查报告")


@dataclass(frozen=True)
class LinkIssue:
    source: str
    target: str


@dataclass(frozen=True)
class AuditResult:
    unresolved_links: list[LinkIssue]
    empty_markdown: list[str]
    orphan_markdown: list[str]
    pending_files: list[str]


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _iter_vault_files(root: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and not any(part in SKIP_DIRECTORIES for part in path.parts)
            and path.relative_to(root).parts[:2] != GENERATED_AUDIT_DIRECTORY
        ),
        key=lambda path: _relative(path, root).casefold(),
    )


def _normalise_target(raw_target: str) -> str | None:
    target = raw_target.split("|", maxsplit=1)[0].strip()
    target = target.split("#", maxsplit=1)[0].split("^", maxsplit=1)[0].strip()
    if not target:
        return None
    return target.replace("\\", "/")


def _content_without_fenced_code(content: str) -> str:
    """移除 fenced code block，避免把语法示例误报成链接。"""
    visible_lines: list[str] = []
    in_fence = False
    for line in content.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence:
            visible_lines.append(line)
    return "".join(visible_lines)


def _candidate_paths(root: Path, source: Path, target: str) -> list[Path]:
    target_path = Path(target.lstrip("/"))
    bases = [source.parent, root]
    candidates: list[Path] = []
    for base in bases:
        candidate = base / target_path
        candidates.append(candidate)
        if not target_path.suffix:
            candidates.append(candidate.with_suffix(".md"))
    return candidates


def _resolve_target(
    root: Path,
    source: Path,
    target: str,
    files_by_stem: dict[str, list[Path]],
) -> bool:
    if any(candidate.is_file() for candidate in _candidate_paths(root, source, target)):
        return True
    if "/" not in target:
        stem = Path(target).stem
        return len(files_by_stem.get(stem.casefold(), [])) == 1
    return False


def scan_vault(root: Path) -> AuditResult:
    """扫描仓库，不修改任何文件。"""
    root = root.resolve()
    files = _iter_vault_files(root)
    markdown_files = [path for path in files if path.suffix.casefold() == ".md"]
    files_by_stem: dict[str, list[Path]] = {}
    for path in files:
        files_by_stem.setdefault(path.stem.casefold(), []).append(path)

    unresolved_links: list[LinkIssue] = []
    empty_markdown: list[str] = []
    outgoing: dict[Path, set[Path]] = {path: set() for path in markdown_files}
    incoming: dict[Path, set[Path]] = {path: set() for path in markdown_files}

    for source in markdown_files:
        content = source.read_text(encoding="utf-8", errors="replace")
        if not content.strip():
            empty_markdown.append(_relative(source, root))
        for raw_target in WIKILINK_PATTERN.findall(_content_without_fenced_code(content)):
            target = _normalise_target(raw_target)
            if target is None:
                continue
            resolved = next(
                (
                    candidate
                    for candidate in _candidate_paths(root, source, target)
                    if candidate.is_file() and candidate.suffix.casefold() == ".md"
                ),
                None,
            )
            if resolved is not None:
                outgoing[source].add(resolved)
                incoming.setdefault(resolved, set()).add(source)
            elif not _resolve_target(root, source, target, files_by_stem):
                unresolved_links.append(LinkIssue(_relative(source, root), target))

    orphan_markdown = sorted(
        _relative(path, root)
        for path in markdown_files
        if not outgoing[path]
        and not incoming.get(path)
        and path.name.casefold() not in {"readme.md", "index.md"}
    )
    pending_files = sorted(
        _relative(path, root)
        for path in files
        if any(part in PENDING_DIRECTORIES for part in path.parts)
    )

    return AuditResult(
        unresolved_links=sorted(
            unresolved_links, key=lambda issue: (issue.source.casefold(), issue.target.casefold())
        ),
        empty_markdown=sorted(empty_markdown),
        orphan_markdown=orphan_markdown,
        pending_files=pending_files,
    )


def _table_rows(items: list[str]) -> str:
    if not items:
        return "| 通过 | 0 | - |"
    return "\n".join(
        f"| 警告 | 1 | `{item.replace('|', '\\|')}` |" for item in items[:MAX_REPORT_ITEMS]
    )


def _limit_notice(total: int) -> str:
    if total <= MAX_REPORT_ITEMS:
        return ""
    return f"\n\n> [!info]\n> 仅显示前 {MAX_REPORT_ITEMS} 项，共 {total} 项。"


def render_report(result: AuditResult, root: Path) -> str:
    link_rows = (
        "\n".join(
            f"| `{issue.source.replace('|', '\\|')}` | `[[{issue.target.replace('|', '\\|')}]]` |"
            for issue in result.unresolved_links[:MAX_REPORT_ITEMS]
        )
        or "| - | - |"
    )
    return f"""---
title: 知识库质量审查
type: 审查报告
date: {date.today().isoformat()}
status: 待人工复核
---

# 知识库质量审查

> [!warning]
> 本报告由只读扫描生成。未解析链接和孤立笔记均为候选项，修复、移动或删除前必须人工确认。

## 摘要

| 项目 | 数量 |
|---|---:|
| 未解析 Wiki-link | {len(result.unresolved_links)} |
| 空 Markdown | {len(result.empty_markdown)} |
| 孤立 Markdown 候选 | {len(result.orphan_markdown)} |
| 未处理项文件 | {len(result.pending_files)} |

扫描根目录：`{root.as_posix()}`

## 未解析 Wiki-link

| 来源 | 目标 |
|---|---|
{link_rows}
{_limit_notice(len(result.unresolved_links))}

## 空 Markdown

| 级别 | 数量 | 文件 |
|---|---:|---|
{_table_rows(result.empty_markdown)}
{_limit_notice(len(result.empty_markdown))}

## 孤立 Markdown 候选

| 级别 | 数量 | 文件 |
|---|---:|---|
{_table_rows(result.orphan_markdown)}
{_limit_notice(len(result.orphan_markdown))}

## 未处理项文件

| 级别 | 数量 | 文件 |
|---|---:|---|
{_table_rows(result.pending_files)}
{_limit_notice(len(result.pending_files))}

## 修复闭环

发现问题 → 人工确认 → 修复 → 重新运行审查 → 通过
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="只读扫描 Obsidian 仓库并输出审查报告")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="仓库根目录")
    parser.add_argument("--output", type=Path, help="报告输出路径")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output or root / "总览" / "审查报告" / f"{date.today().isoformat()}-知识库质量审查.md"
    result = scan_vault(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(result, root), encoding="utf-8")
    print(output)
    print(
        "unresolved={0}, empty={1}, orphan_candidates={2}, pending={3}".format(
            len(result.unresolved_links),
            len(result.empty_markdown),
            len(result.orphan_markdown),
            len(result.pending_files),
        )
    )


if __name__ == "__main__":
    main()
