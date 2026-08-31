"""Embed exercise images by position in source MD - much more accurate."""
import re, shutil
from pathlib import Path

VAULT = Path("D:/知识库/课程/大学物理")
MD_DIR = VAULT / "课件" / "MD"
IMG_SRC = MD_DIR / "images"
EX_DIR = VAULT / "习题库"

CONFIG = [
    ("大学物理II-热学-热力学.md", "08-热力学基础"),
    ("大学物理II-热学-统计物理初步.md", "07-统计物理初步"),
    ("大学物理_16量子光学基础.md", "16-早期量子论"),
    ("大学物理_17量子力学基础.md", "17-量子力学基础"),
]

EX_NUM_MAP = {
    # 热力学: map exercise filename number → source label patterns
    "08-热力学基础": {
        "8-1": "例题 8-1", "8-2": "例题8-2", "8-3": "例题8-3",
        "8-4": "例题8-4", "8-5": "例题8-5", "8-6": "例题 8-7" if False else "例题8-6",
        "8-7": "例题 8-7", "8-8": "例8-8", "8-9": "例8-9",
        "8-10": "例8-10",
    },
}

def find_exercise_images(source_path: Path, ex_num: str) -> list:
    """Find images between this exercise and the next in source MD."""
    content = source_path.read_text(encoding="utf-8")
    lines = content.split('\n')

    # Find all headings and labeled sections
    # Pattern: 例题X-Y or 例X-Y (with optional spaces)
    ex_pattern = re.compile(r'(例题?\s*' + re.escape(ex_num).replace('-', r'\s*[-−]\s*') + r')')

    # Find this exercise's start
    start_idx = None
    for i, line in enumerate(lines):
        if ex_pattern.search(line):
            start_idx = i
            break

    if start_idx is None:
        # Try broader: find "例8-8" type
        broad = re.compile(r'例\s*' + re.escape(ex_num.replace('-循环','').replace('-喷气','')).replace('-', r'\s*[-−]\s*'))
        for i, line in enumerate(lines):
            if broad.search(line):
                start_idx = i
                break

    if start_idx is None:
        # Try with "例题" prefix
        for i, line in enumerate(lines):
            if f'例题{ex_num}' in line.replace(' ','') or f'例{ex_num}' in line.replace(' ',''):
                start_idx = i
                break

    if start_idx is None:
        return []

    # Find next exercise boundary (next 例题/例, or next ## section, or EOF)
    end_idx = len(lines)
    next_pattern = re.compile(r'(例题\s*\d+|例\s*\d+)')
    for i in range(start_idx + 1, len(lines)):
        if next_pattern.search(lines[i]) and '例题' in lines[i] or '例 ' in lines[i] or '例\n' in lines[i-1:i+2]:
            # Make sure it's a real exercise, not just "例如"
            if not lines[i].strip().startswith('例') or re.match(r'例\s*\d', lines[i].strip()):
                if '例如' not in lines[i] and '比例' not in lines[i]:
                    end_idx = i
                    break

    # If no next exercise found, stop at next ## section
    if end_idx == len(lines):
        for i in range(start_idx + 1, len(lines)):
            if re.match(r'^##\s', lines[i]) and i > start_idx + 3:
                end_idx = i
                break

    # Collect images in range
    img_pattern = re.compile(r'!\[\]\(images/([^)]+)\)')
    imgs = []
    for i in range(start_idx, end_idx):
        m = img_pattern.search(lines[i])
        if m:
            imgs.append(m.group(0))

    return imgs

def main():
    # First pass: count exercises needing images
    for src_name, chapter in CONFIG:
        src = MD_DIR / src_name
        ex_dir = EX_DIR / chapter
        if not src.exists() or not ex_dir.exists():
            continue

        print(f"\n{'='*60}")
        print(f"[{chapter}]")

        updated = 0
        for ex_file in sorted(ex_dir.glob("习题*.md")):
            # Check if already has images embedded
            content = ex_file.read_text(encoding="utf-8")
            if content.count('![[') > 0:
                continue  # already has embedded images

            # Extract exercise number from filename
            name = ex_file.stem  # e.g. "习题8-1" or "习题8-8-循环"
            ex_num = name.replace('习题', '')  # e.g. "8-1" or "8-8-循环"

            # Find images from source MD
            imgs = find_exercise_images(src, ex_num)

            if not imgs:
                # print(f"  [--] {ex_file.name}")
                continue

            # Insert images into exercise file before the hint section
            hint_match = re.search(r'\n> \[!hint\]', content)
            if hint_match:
                insert_pos = hint_match.start()
            else:
                # After frontmatter
                parts = content.split('---\n', 2)
                insert_pos = len(parts[0]) + len(parts[1]) + 8 if len(parts) >= 3 else 0

            # Copy images to exercise dir
            img_dir = ex_dir / "images"
            img_dir.mkdir(exist_ok=True)

            embed_lines = []
            for ref in imgs:
                m = re.search(r'images/([^)]+)', ref)
                if m:
                    fname = m.group(1)
                    src_img = IMG_SRC / fname
                    dst_img = img_dir / fname
                    if src_img.exists():
                        if not dst_img.exists():
                            shutil.copy2(src_img, dst_img)
                        embed_lines.append(f'![[images/{fname}]]')

            if embed_lines:
                embed_block = '\n' + '\n'.join(embed_lines) + '\n'
                new_content = content[:insert_pos] + embed_block + content[insert_pos:]
                ex_file.write_text(new_content, encoding="utf-8")
                print(f"  [OK] {ex_file.name}: +{len(embed_lines)} images")
                updated += 1
            else:
                print(f"  [--] {ex_file.name}: 0 images copied")

        print(f"  Done: {updated} updated")

if __name__ == "__main__":
    main()
