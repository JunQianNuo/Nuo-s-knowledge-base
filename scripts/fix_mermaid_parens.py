"""Fix: wrap [...] and {...} labels containing () in "" quotes for Mermaid."""
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
        lines = block.split('\n')
        new_lines = []

        for line in lines:
            # Skip non-content lines
            s = line.strip()
            if s in ('```mermaid', '```') or s.startswith('flowchart'):
                new_lines.append(line)
                continue

            # Fix 1: [...(...)...] where label contains (, not already in quotes
            # Pattern: X[...] where ... contains ( or )
            def fix_bracket(m):
                full = m.group(0)
                inner = m.group(1)
                if ('(' in inner or ')' in inner):
                    # Don't double-wrap
                    if inner.startswith('"') and inner.endswith('"'):
                        return full
                    return '["' + inner + '"]'
                return full

            line = re.sub(r'\[([^\]]*)\]', fix_bracket, line)

            # Fix 2: {...(...)...} same treatment
            def fix_diamond(m):
                full = m.group(0)
                inner = m.group(1)
                if ('(' in inner or ')' in inner):
                    if inner.startswith('"') and inner.endswith('"'):
                        return full
                    return '{"' + inner + '"}'
                return full

            line = re.sub(r'\{([^}]*)\}', fix_diamond, line)

            new_lines.append(line)

        new_block = '\n'.join(new_lines)
        if new_block != old:
            total += 1
        return new_block

    new_content = re.sub(r'```mermaid\n.*?```', fix_block, content, flags=re.DOTALL)

    if new_content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[FIXED] {os.path.basename(fp)}')

print(f'\nDone! {total} blocks fixed')
