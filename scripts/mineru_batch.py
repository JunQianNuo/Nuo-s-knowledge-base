#!/usr/bin/env python3
"""MinerU 批处理脚本 — 串行处理课程的 PDF/PPTX 文件。

用法:
    python scripts/mineru_batch.py --course "马克思主义原理"
    python scripts/mineru_batch.py --course "概率论" --dry-run
    python scripts/mineru_batch.py --course "最优化方法" --backend pipeline --method ocr
"""

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

# Windows Git Bash 终端使用 GBK，需重配置为 UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# === 配置 ===
VAULT_ROOT = Path("D:/知识库")
MINERU_CMD = "mineru"
DEFAULT_BACKEND = "hybrid-auto-engine"
DEFAULT_LANG = "ch"


def discover_files(course_dir: Path) -> list[Path]:
    """发现课程目录中的 PDF 和 PPTX 源文件。

    搜索路径（按优先级）：
    - 课件/           PPTX 源文件（数值分析）
    - PDF/             PDF 源文件（马克思主义原理）
    - PPT课件/PDF/     PDF 课件（概率论）
    - 最优化方法PPT课件/PDF/  PDF 课件（最优化方法）
    - 一级目录下的 PDF/PPTX
    """
    files = []

    # 常见的课件源文件位置
    search_dirs = [
        course_dir / "课件",
        course_dir / "PDF",
        course_dir / "PPT课件" / "PDF",
        course_dir / "最优化方法PPT课件" / "PDF",
    ]

    # 也搜索课程根目录一级的 PDF/PPTX
    search_dirs.append(course_dir)

    for search_dir in search_dirs:
        if not search_dir.is_dir():
            continue
        for ext in ["pdf", "pptx", "PPTX", "PDF"]:
            for f in search_dir.glob(f"*.{ext}"):
                # 跳过非课件文件（复习纲要等）
                name = f.stem
                if any(kw in name for kw in ["复习纲要", "概念辨析", "材料分析", "模板"]):
                    continue
                if f not in files:
                    files.append(f)

    # 按文件名排序
    files.sort(key=lambda p: p.name)
    return files


def find_existing_md(course_dir: Path, source_file: Path) -> Path | None:
    """检查是否已有对应的 MD 输出。"""
    md_dir = course_dir / "课件" / "MD"
    if not md_dir.is_dir():
        return None

    # 匹配文件名（前缀匹配，如 01-xxx.pdf → 01-xxx.md）
    stem = source_file.stem
    for md_file in md_dir.glob("*.md"):
        if md_file.stem == stem or md_file.stem.startswith(stem[:5]):
            return md_file
    return None


def run_mineru(
    source: Path,
    output_dir: Path,
    backend: str = DEFAULT_BACKEND,
    lang: str = DEFAULT_LANG,
    dry_run: bool = False,
) -> bool:
    """运行 MinerU 处理单个文件。"""
    cmd = [
        MINERU_CMD,
        "-p", str(source),
        "-o", str(output_dir),
        "-b", backend,
        "-l", lang,
    ]

    print(f"\n{'[DRY RUN] ' if dry_run else ''}处理: {source.name}")
    print(f"  命令: {' '.join(cmd)}")

    if dry_run:
        return True

    try:
        result = subprocess.run(cmd, capture_output=False, text=True, timeout=1800)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] 超时（30分钟）: {source.name}")
        return False
    except Exception as e:
        print(f"  [FAIL]异常: {e}")
        return False


def find_mineru_md(output_dir: Path) -> Path | None:
    """在 MinerU 输出目录中查找生成的 MD 文件。

    MinerU 在输出目录中创建以源文件名命名的子文件夹，
    其中包含 .md 文件。
    """
    if not output_dir.is_dir():
        return None
    for md_file in output_dir.glob("**/*.md"):
        return md_file
    return None


def add_frontmatter(
    md_file: Path,
    source_name: str,
    subject: str,
) -> None:
    """在 MD 文件顶部添加 YAML frontmatter。"""
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已有 frontmatter
    if content.startswith("---"):
        return

    frontmatter = f"""---
raw_title: {source_name.split('.')[0]}
subject: {subject}
source: {source_name}
status: mineru解析
parser: mineru
---

"""
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(frontmatter + content)

    print(f"  [OK]已添加 frontmatter → {md_file.name}")


def collect_images(md_file: Path, course_dir: Path) -> None:
    """将 MinerU 生成的图片收集到课程的 _images/ 目录。

    MinerU 将图片放在 MD 同目录下的 images/ 文件夹中。
    统一收集到 course_dir/_images/ 下，与 数值分析 现有模式一致。
    """
    images_dir = md_file.parent / "images"
    if not images_dir.is_dir():
        return

    target_dir = course_dir / "_images"
    target_dir.mkdir(exist_ok=True)

    count = 0
    for img in images_dir.iterdir():
        if img.is_file():
            dest = target_dir / img.name
            if not dest.exists():
                shutil.copy2(img, dest)
                count += 1

    if count > 0:
        print(f"  [IMG]已收集 {count} 张图片 → {target_dir.relative_to(VAULT_ROOT)}")


def main():
    parser = argparse.ArgumentParser(
        description="MinerU 批处理 — 串行处理课程的 PDF/PPTX 文件"
    )
    parser.add_argument(
        "--course", required=True,
        help="课程名称（如 '马克思主义原理', '概率论', '数值分析'）"
    )
    parser.add_argument(
        "--backend", default=DEFAULT_BACKEND,
        choices=["pipeline", "vlm-auto-engine", "hybrid-auto-engine",
                 "vlm-http-client", "hybrid-http-client"],
        help=f"MinerU 后端（默认: {DEFAULT_BACKEND}）"
    )
    parser.add_argument(
        "--lang", default=DEFAULT_LANG,
        help=f"OCR 语言（默认: {DEFAULT_LANG}）"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="仅列出待处理文件，不实际运行"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="强制重新处理已有 MD 输出的文件"
    )
    parser.add_argument(
        "--skip-missing-source", action="store_true",
        help="跳过找不到源文件的情况"
    )

    args = parser.parse_args()

    # 定位课程目录
    course_dir = VAULT_ROOT / "课程" / args.course
    if not course_dir.is_dir():
        print(f"[FAIL]课程目录不存在: {course_dir}")
        # 尝试模糊匹配
        for d in (VAULT_ROOT / "课程").iterdir():
            if d.is_dir() and args.course in d.name:
                course_dir = d
                print(f"[DIR]模糊匹配到: {course_dir.name}")
                break
        else:
            sys.exit(1)

    print(f"[DIR]课程: {course_dir.relative_to(VAULT_ROOT)}")
    print(f"[CFG]后端: {args.backend} | 语言: {args.lang}")

    # 发现源文件
    files = discover_files(course_dir)
    if not files:
        print("[FAIL]未找到 PDF/PPTX 源文件")
        sys.exit(1)

    print(f"\n[FILE]发现 {len(files)} 个文件:")

    # 过滤已有 MD 的文件
    to_process = []
    for f in files:
        existing = find_existing_md(course_dir, f)
        status = "[SKIP]已有 MD" if existing and not args.force else ""
        if existing and not args.force:
            print(f"  {f.name}  {status}")
        else:
            print(f"  {f.name}")
            to_process.append(f)

    if not to_process:
        print("\n[OK]所有文件已处理完毕")
        return

    # 创建临时输出目录
    temp_dir = course_dir / "_mineru_temp"
    temp_dir.mkdir(exist_ok=True)

    # 目标 MD 目录
    md_dir = course_dir / "课件" / "MD"
    md_dir.mkdir(parents=True, exist_ok=True)

    # 串行处理
    success = 0
    fail = 0
    start_time = time.time()

    for i, source in enumerate(to_process, 1):
        print(f"\n[{i}/{len(to_process)}] ", end="")
        file_output_dir = temp_dir / source.stem

        ok = run_mineru(source, temp_dir, backend=args.backend, lang=args.lang, dry_run=args.dry_run)

        if args.dry_run:
            continue

        if not ok:
            fail += 1
            continue

        # 查找 MinerU 生成的 MD 文件
        mineru_md = find_mineru_md(file_output_dir)
        if not mineru_md:
            print(f"  [WARN]MinerU 未生成 MD 文件，尝试搜索...")
            # 搜索整个 temp_dir
            for md in temp_dir.glob("**/*.md"):
                mineru_md = md
                break

        if mineru_md:
            # 复制到课件/MD/
            dest_md = md_dir / f"{source.stem}.md"
            shutil.copy2(mineru_md, dest_md)

            # 添加 frontmatter
            add_frontmatter(dest_md, source.name, args.course)

            # 收集图片
            collect_images(mineru_md, course_dir)

            success += 1
            print(f"  [OK]{dest_md.name}")
        else:
            fail += 1
            print(f"  [FAIL]MD 文件未找到")

    elapsed = time.time() - start_time

    # 清理临时目录
    if not args.dry_run:
        shutil.rmtree(temp_dir, ignore_errors=True)

    print(f"\n{'='*50}")
    print(f"[OK]成功: {success} | [FAIL]失败: {fail} | [TIME]耗时: {elapsed:.0f}s")
    print(f"[DIR]输出目录: {md_dir.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()
