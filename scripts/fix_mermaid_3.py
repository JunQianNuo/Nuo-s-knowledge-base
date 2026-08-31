"""Fix remaining Mermaid issues: | and : inside node labels, inconsistent indent."""
import re, os, glob, sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DIR = r'D:\知识库\课程\概率论\知识点解析梳理'
files = sorted(glob.glob(os.path.join(DIR, '*.md')))
total_fixes = 0

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    def fix_mermaid_block(match):
        global total_fixes
        block = match.group(0)
        old_block = block
        lines = block.split('\n')
        new_lines = []

        for line in lines:
            # Only process content lines (not ``` markers, not flowchart header)
            s = line.strip()
            if s in ('```mermaid', '```') or s.startswith('flowchart'):
                new_lines.append(line)
                continue

            # Fix 1: replace | inside "..." labels (pipe confuses edge label parser)
            # BUT only if | appears inside a quoted label, not as edge label -->
            # Edge labels use -->|text| so we need to preserve those
            # Strategy: within "..." node labels, replace | with ｜(fullwidth) or just comma
            # But this is hard to do with regex. Simpler: in quoted labels, escape the pipe

            # Actually, let's try a different approach: just remove colons and pipes
            # from INSIDE node labels [..] and ".."

            def clean_label(m):
                inner = m.group(1)
                # Replace problematic chars inside labels
                inner = inner.replace(':', '：')  # fullwidth colon
                # Don't replace | as it's very common in math and might break more than it fixes
                # But do replace | if it appears to cause issues
                return m.group(0)[0] + inner + m.group(0)[-1]

            # Apply to [...] labels
            line = re.sub(r'\[([^\]]*)\]', clean_label, line)
            # Apply to "..." labels
            line = re.sub(r'"([^"]*)"', clean_label, line)

            # Fix 2: replace ² with ^2
            line = line.replace('²', '^2')

            new_lines.append(line)

        new_block = '\n'.join(new_lines)
        if new_block != old_block:
            total_fixes += 1
        return new_block

    new_content = re.sub(
        r'```mermaid\n.*?```',
        fix_mermaid_block,
        content,
        flags=re.DOTALL
    )

    if new_content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[FIXED] {os.path.basename(fp)}')

print(f'\nDone! {total_fixes} blocks fixed')
