"""Fix Mermaid {} in node labels: replace {...} → (...) inside [...] or "..." only."""
import re, os, glob, sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DIR = r'D:\知识库\课程\概率论\知识点解析梳理'
files = sorted(glob.glob(os.path.join(DIR, '*.md')))
total_fixes = 0

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find ```mermaid ... ``` blocks and fix them
    fixes_in_file = [0]
    def fix_mermaid_block(match):
        block = match.group(0)
        old_block = block
        lines = block.split('\n')
        new_lines = []

        for line in lines:
            # Only fix {...} that appears INSIDE [...] or "..." labels
            # Preserve rhombus syntax: id{text} where id is alphanumeric and immediately followed by {
            # Rhombus pattern: \w+{...}  at the start of a node definition

            # Find [...] groups and fix {} inside them
            def fix_bracket_content(m):
                inner = m.group(1)
                if '{' in inner or '}' in inner:
                    return '[' + inner.replace('{', '(').replace('}', ')') + ']'
                return m.group(0)

            def fix_quote_content(m):
                inner = m.group(1)
                if '{' in inner or '}' in inner:
                    return '"' + inner.replace('{', '(').replace('}', ')') + '"'
                return m.group(0)

            # Only fix inside brackets (not rhombus)
            line = re.sub(r'\[([^\]]*)\]', fix_bracket_content, line)
            line = re.sub(r'"([^"]*)"', fix_quote_content, line)

            new_lines.append(line)

        new_block = '\n'.join(new_lines)
        if new_block != old_block:
            fixes = old_block.count('{') - new_block.count('{')
            fixes_in_file[0] += fixes
            print(f'  Fixed {fixes} braces in block')
        return new_block

    new_content = re.sub(
        r'```mermaid\n.*?```',
        fix_mermaid_block,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        total_fixes += fixes_in_file[0]
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[OK] {os.path.basename(fp)}: {fixes_in_file[0]} fixes')

print(f'\nDone! {total_fixes} braces fixed')
