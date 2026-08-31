"""Fix {"..."} → {...} inside Mermaid blocks (remove unnecessary inner quotes)."""
import re, os, glob, sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DIR = r'D:\知识库\课程\概率论\知识点解析梳理'
files = sorted(glob.glob(os.path.join(DIR, '*.md')))
total = 0

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    def fix_block(match):
        global total
        block = match.group(0)
        old = block
        # Replace {"..."} with {...} (remove inner quotes around node text)
        block = re.sub(r'\{(".*?")\}', lambda m: '{' + m.group(1)[1:-1] + '}', block)
        if block != old:
            total += block.count('{')  # just counting for logging
        return block

    new_content = re.sub(r'```mermaid\n.*?```', fix_block, content, flags=re.DOTALL)

    if new_content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[FIXED] {os.path.basename(fp)}')

print(f'\nDone! {total} replacements')
