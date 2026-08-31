"""Fix [""..."..."...] patterns in Mermaid - remove double-quote wrapping."""
import re, os, glob, sys

DIR = r'D:\知识库\课程\概率论\知识点解析梳理'
for fp in glob.glob(os.path.join(DIR, '*.md')):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    def fix_block(match):
        block = match.group(0)
        # Fix [""... → ["
        block = block.replace('[""', '["')
        # Fix ..."]"] → ..."]" at end of labels
        block = block.replace('"]"]', '"]')
        # Fix ..."]| → ...]|
        block = block.replace('"]|', ']|')
        return block

    new_content = re.sub(r'```mermaid\n.*?```', fix_block, content, flags=re.DOTALL)
    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[FIXED] {os.path.basename(fp)}')

print('Done')
