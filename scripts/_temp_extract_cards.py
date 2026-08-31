"""Extract front/back from all Marx flashcard .md files, output as Markdown table."""
import os
import re
import glob

BASE = r"D:\知识库\闪卡\马克思主义原理"
PATTERN = os.path.join(BASE, "**", "*.md")

files = sorted(glob.glob(PATTERN, recursive=True))

def extract_front_back(filepath):
    """Extract front question and back core answer from a flashcard .md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    rel_path = os.path.relpath(filepath, BASE)
    folder = os.path.dirname(rel_path) or os.path.basename(BASE)
    filename = os.path.basename(rel_path)

    has_sep = '---' in content

    if has_sep:
        # Basic Q&A card: split at first --- (must be on its own line)
        # Find --- on its own line
        parts = re.split(r'\n---\n', content, maxsplit=1)
        front = parts[0].strip() if len(parts) >= 1 else ''
        back_raw = parts[1].strip() if len(parts) >= 2 else ''

        # Strip ~~ marks from front (in case there are any)
        front = re.sub(r'~~.*?~~', '', front).strip()

        # Extract first meaningful sentence from back
        back_core = ''
        for line in back_raw.split('\n'):
            line = line.strip()
            if not line:
                continue
            # Skip lines that are just LaTeX formulas
            if line.startswith('**') or line.startswith('$') or line.startswith('|'):
                back_core = line
                break
            if line and not line.startswith('>'):
                back_core = line
                break

        # If back_core is empty, use first non-empty line
        if not back_core:
            for line in back_raw.split('\n'):
                line = line.strip()
                if line:
                    back_core = line
                    break

        return folder, filename, front, back_core

    else:
        # Cloze card (only ~~, no ---)
        # Front: text with ~~...~~ removed
        front = re.sub(r'~~.*?~~', '', content).strip()
        # Back core: content inside the first ~~...~~
        m = re.search(r'~~(.+?)~~', content)
        back_core = m.group(1).strip() if m else ''

        return folder, filename, front, back_core

# Process all files
rows = []
for fp in files:
    folder, fname, front, back = extract_front_back(fp)
    # Clean front: take first line or first meaningful part (limit length)
    front_display = front.replace('\n', ' ').strip()
    # Truncate if too long
    if len(front_display) > 120:
        front_display = front_display[:117] + '...'

    back_display = back.replace('\n', ' ').strip()
    if len(back_display) > 150:
        back_display = back_display[:147] + '...'

    rows.append((folder, fname, front_display, back_display))

# Write output to UTF-8 file (avoid GBK terminal issues)
output_path = r"D:\知识库\scripts\_temp_cards_output.md"
with open(output_path, 'w', encoding='utf-8') as out:
    out.write(f"共 {len(rows)} 张闪卡\n\n")
    out.write("| 文件夹 | 文件名 | 正面问题 | 反面核心答案 |\n")
    out.write("|---|---|---|---|\n")
    for folder, fname, front, back in rows:
        # Escape pipe characters for markdown table
        front_esc = front.replace('|', '\\|')
        back_esc = back.replace('|', '\\|')
        out.write(f"| {folder} | {fname} | {front_esc} | {back_esc} |\n")

print(f"Done. {len(rows)} cards written to {output_path}")