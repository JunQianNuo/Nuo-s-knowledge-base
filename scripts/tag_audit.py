"""Scan vault for all Obsidian tags and generate audit report.
Outputs to a UTF-8 file for reliable reading."""
import re, os, sys
from collections import Counter, defaultdict
import yaml

vault = r'D:\知识库'
outfile = os.path.join(vault, 'scripts', 'tag_audit_report.txt')

# Files/dirs to exclude
exclude_dirs = {'.git', '.obsidian', '.claude', '.trash', 'node_modules', '__pycache__', 'scripts'}
exclude_files = {'.DS_Store'}

tag_counter = Counter()
tag_files = defaultdict(list)
file_tags = defaultdict(set)
all_tags_set = set()

tag_fields = ['tags', 'knowledge_tags', 'method_tags', 'topic_tags', 'concept_tags']

def extract_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except:
        return None

def extract_inline_tags(content):
    content = re.sub(r'^---[\s\S]*?---', '', content, flags=re.MULTILINE)
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`[^`]+`', '', content)
    tags = set()
    pattern = re.compile(r'(?:^|\s)(#[^\s\[\]()#.,;:!?`"\'{}=~|\\/<>]+)')
    for m in pattern.finditer(content):
        tag = m.group(1)
        if re.match(r'^#[0-9a-fA-F]{3,8}$', tag):
            continue
        if re.match(r'^#\d+$', tag):
            continue
        if len(tag) > 1:
            tags.add(tag)
    return tags

total_files = 0
files_with_tags = 0

for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
    for f in files:
        if not f.endswith('.md') or f in exclude_files:
            continue
        fpath = os.path.join(root, f)
        try:
            with open(fpath, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except:
            continue
        total_files += 1
        rel = os.path.relpath(fpath, vault)
        tags = set()

        fm = extract_frontmatter(content)
        if fm and isinstance(fm, dict):
            for field in tag_fields:
                val = fm.get(field)
                if val is None:
                    continue
                if isinstance(val, list):
                    for t in val:
                        if isinstance(t, str) and t.strip():
                            tags.add(t.strip())
                elif isinstance(val, str) and val.strip():
                    tags.add(val.strip())

        inline = extract_inline_tags(content)
        tags.update(inline)

        if tags:
            files_with_tags += 1
            file_tags[rel] = tags
            for tag in tags:
                tag_counter[tag] += 1
                tag_files[tag].append(rel)
            all_tags_set.update(tags)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write('=' * 70 + '\n')
    f.write('TAG AUDIT REPORT\n')
    f.write('=' * 70 + '\n')
    f.write(f'Total .md files scanned: {total_files}\n')
    f.write(f'Files with tags:         {files_with_tags}\n')
    f.write(f'Unique tags:             {len(all_tags_set)}\n')
    f.write(f'Total tag occurrences:   {sum(tag_counter.values())}\n')
    f.write('\n')

    f.write('=' * 70 + '\n')
    f.write('TOP 80 TAGS BY FREQUENCY\n')
    f.write('=' * 70 + '\n')
    for tag, count in tag_counter.most_common(80):
        files_sample = tag_files[tag][:2]
        f.write(f'  {count:4d}  {tag:30s}  {", ".join(files_sample)}\n')

    f.write('\n' + '=' * 70 + '\n')
    f.write('ALL TAGS SORTED ALPHABETICALLY\n')
    f.write('=' * 70 + '\n')
    for tag in sorted(all_tags_set, key=str.lower):
        f.write(f'  {tag_counter[tag]:4d}  {tag}\n')

    orphans = [(tag, tag_files[tag][0]) for tag in all_tags_set if tag_counter[tag] == 1]
    f.write('\n' + '=' * 70 + '\n')
    f.write(f'ORPHAN TAGS (used only once): {len(orphans)}\n')
    f.write('=' * 70 + '\n')
    for tag, fpath in sorted(orphans):
        f.write(f'  {tag:40s}  {fpath}\n')

    f.write('\n' + '=' * 70 + '\n')
    f.write('FILES WITH MOST TAGS\n')
    f.write('=' * 70 + '\n')
    for fpath, tags in sorted(file_tags.items(), key=lambda x: -len(x[1]))[:20]:
        f.write(f'  {len(tags):3d} tags  {fpath}\n')
        f.write(f'         {" | ".join(sorted(tags))}\n')

    # Potential duplicates
    f.write('\n' + '=' * 70 + '\n')
    f.write('POTENTIAL DUPLICATES / SIMILAR TAGS\n')
    f.write('=' * 70 + '\n')
    sorted_tags_list = sorted(all_tags_set, key=str.lower)
    for i, t1 in enumerate(sorted_tags_list):
        for t2 in sorted_tags_list[i+1:]:
            if t1.lower() == t2.lower() and t1 != t2:
                f.write(f'  CASE MISMATCH: "{t1}" ({tag_counter[t1]}) vs "{t2}" ({tag_counter[t2]})\n')
            elif (t1 in t2 or t2 in t1) and abs(len(t2) - len(t1)) <= 3 and len(t1) > 1:
                if tag_counter[t1] <= 3 or tag_counter[t2] <= 3:
                    f.write(f'  SIMILAR: "{t1}" ({tag_counter[t1]}) vs "{t2}" ({tag_counter[t2]})\n')

    # Tag statistics by category
    f.write('\n' + '=' * 70 + '\n')
    f.write('TAG STATISTICS\n')
    f.write('=' * 70 + '\n')
    f.write(f'Tags used in 5+ files: {sum(1 for t in all_tags_set if tag_counter[t] >= 5)}\n')
    f.write(f'Tags used in 3-4 files: {sum(1 for t in all_tags_set if 3 <= tag_counter[t] <= 4)}\n')
    f.write(f'Tags used in 2 files:   {sum(1 for t in all_tags_set if tag_counter[t] == 2)}\n')
    f.write(f'Tags used in 1 file:    {sum(1 for t in all_tags_set if tag_counter[t] == 1)}\n')

print(f'Report written to: {outfile}')
print(f'Total files: {total_files}, files with tags: {files_with_tags}')
print(f'Unique tags: {len(all_tags_set)}, occurrences: {sum(tag_counter.values())}')
