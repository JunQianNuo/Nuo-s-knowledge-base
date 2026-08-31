"""Fix <br/> tags in Mermaid diagrams across all 知识点解析梳理 files."""
import re, os, glob, sys

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DIR = r'D:\知识库\课程\概率论\知识点解析梳理'

files = sorted(glob.glob(os.path.join(DIR, '*.md')))
total_fixes = 0

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    in_mermaid = False
    new_lines = []
    changed = False
    file_fixes = 0

    for line in lines:
        stripped = line.strip()
        if stripped == '```mermaid':
            in_mermaid = True
            new_lines.append(line)
            continue
        if in_mermaid and stripped == '```':
            in_mermaid = False
            new_lines.append(line)
            continue

        if in_mermaid and ('<br' in line):
            old = line
            line = line.replace('<br/>', ' ').replace('<br\\>', ' ').replace('<br>', ' ')
            line = re.sub(r'  +', ' ', line)
            if line != old:
                changed = True
                file_fixes += 1

        new_lines.append(line)

    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        total_fixes += file_fixes
        print(f'[OK] {os.path.basename(fp)}: {file_fixes} fixes')

print(f'\nDone! {total_fixes} total fixes across all files')
