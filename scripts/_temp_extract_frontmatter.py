"""Extract frontmatter from all 马克思主义原理 knowledge point files."""
import os
import sys
import json

# Fix encoding
sys.stdout.reconfigure(encoding='utf-8')

base = r'课程\马克思主义原理\知识点'
results = []

# Folders in order
folders = [
    '导论', '唯物论', '唯物辩证法', '认识论', '历史唯物主义',
    '科学社会主义', '商品经济理论', '剩余价值生产', '剩余价值分配',
    '资本积累与再生产', '资本主义上层建筑', '概念辨析'
]

for folder in folders:
    folder_path = os.path.join(base, folder)
    if not os.path.isdir(folder_path):
        continue
    for fname in sorted(os.listdir(folder_path)):
        if not fname.endswith('.md'):
            continue
        if '知识图谱' in fname:
            continue
        fpath = os.path.join(folder_path, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except Exception as e:
            print(f"ERROR reading {fpath}: {e}")
            continue

        if not content.startswith('---'):
            continue

        end = content.find('---', 3)
        if end <= 0:
            continue

        fm_text = content[3:end].strip()
        lines = fm_text.split('\n')

        entry = {
            'path': fpath,
            'title': '',
            'exam_types': [],
            'flashcards': []
        }

        # Simple YAML parsing
        in_flashcards = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('title:'):
                entry['title'] = stripped.split(':', 1)[1].strip().strip('"').strip("'")
            elif stripped.startswith('exam_types:'):
                types_str = stripped.split(':', 1)[1].strip()
                # Parse [选择, 判断] or [选择, 判断, 简答]
                for t in ['选择', '判断', '简答', '材料分析', '材料']:
                    if t in types_str:
                        entry['exam_types'].append(t)
            elif stripped.startswith('flashcards:'):
                in_flashcards = True
            elif in_flashcards and stripped.startswith('-'):
                card_link = stripped[1:].strip()
                entry['flashcards'].append(card_link)
            elif in_flashcards and not stripped.startswith('-') and not stripped.startswith('#'):
                in_flashcards = False

        # Convert exam_types for classification
        if '简答' in entry['exam_types'] or '材料分析' in entry['exam_types'] or '材料' in entry['exam_types']:
            entry['test_type'] = '简答'  # Keep Q&A
        else:
            entry['test_type'] = '选择判断'  # Convert to Cloze

        results.append(entry)

# Output as JSON for easy parsing
output_path = r'scripts\_temp_fm_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(results)} knowledge points to {output_path}")

# Also print summary
answer_count = sum(1 for r in results if r['test_type'] == '简答')
choice_count = sum(1 for r in results if r['test_type'] == '选择判断')
print(f"Keep as Q&A (简答): {answer_count}")
print(f"Convert to Cloze (选择判断): {choice_count}")
print()

for r in results:
    print(f"[{r['test_type']}] {r['path']}")
    print(f"  title: {r['title']}")
    print(f"  exam_types: {r['exam_types']}")
    for fc in r['flashcards']:
        print(f"  flashcard: {fc}")
    print()
