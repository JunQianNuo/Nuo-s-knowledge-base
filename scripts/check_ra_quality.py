"""Quality check for converted 实变函数 MD files."""
import os, re

md_dir = r'D:\知识库\课程\实变函数\课件\MD'
files = sorted(f for f in os.listdir(md_dir) if f.endswith('.md') and 'backup' not in f and 'xparse' not in f)

issues = []
for f in files:
    path = os.path.join(md_dir, f)
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()

    checks = []
    size_kb = len(text) / 1024

    # Check 1: Unicode math italic
    math_italic = re.findall(r'[\U0001D400-\U0001D7FF]', text)
    if math_italic:
        checks.append(f'Math italic: {len(math_italic)} chars')

    # Check 2: Damaged LaTeX
    if r'\c\dots' in text:
        checks.append(r'Has \c\dots')
    if r'\v\dots' in text:
        checks.append(r'Has \v\dots')

    # Check 3: Section headers
    h2_count = text.count('\n## ')
    if h2_count == 0:
        checks.append('No ## headers')

    # Check 4: Size
    if size_kb < 5:
        checks.append(f'Small: {size_kb:.1f}KB')

    # Check 5: Garbled lines
    garbled_lines = []
    for i, line in enumerate(text.split('\n'), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('!') or stripped.startswith('---') or stripped.startswith('$'):
            continue
        non_alpha = len(re.findall(r'[!"#$%&\'()*+,./:;<=>?@[\\\]^_`{|}~]', stripped))
        alpha = len(re.findall(r'[a-zA-Z0-9一-鿿぀-ヿ]', stripped))
        if non_alpha > 10 and alpha < 5 and len(stripped) > 15:
            garbled_lines.append((i, stripped[:80]))

    if garbled_lines:
        checks.append(f'Garbled: {len(garbled_lines)} lines')

    status = 'OK' if not checks else 'ISSUES: ' + ', '.join(checks)
    print(f'{f:30s} {size_kb:6.1f}KB  h2={h2_count}  mitalic={len(math_italic)}  {status}')

    if checks:
        issues.append((f, size_kb, checks, garbled_lines[:5]))

print(f'\n{"="*60}')
print(f'ISSUE DETAILS ({len(issues)} files with issues)')
for fname, size, checks, garbled in issues:
    print(f'\n--- {fname} ---')
    for c in checks:
        print(f'  {c}')
    if garbled:
        for ln, txt in garbled:
            print(f'  L{ln}: {txt}')

print(f'\nSummary: {len(files)} files checked, {len(issues)} with issues')
