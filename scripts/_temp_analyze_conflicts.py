"""Analyze flashcard conflicts between 简答 and 选择判断 knowledge points."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'scripts\_temp_fm_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Resolve wikilinks to relative flashcard paths
def resolve_flashcard_path(wikilink):
    """[[../../../../闪卡/马克思主义原理/商品经济理论/01-商品定义|商品定义]] -> 闪卡/马克思主义原理/商品经济理论/01-商品定义.md"""
    # Strip the outer quotes and wikilink brackets
    wl = wikilink.strip('"')
    # Extract path part before |
    wl = wl.replace('[[', '').replace(']]', '')
    if '|' in wl:
        path_part = wl.split('|')[0]
    else:
        path_part = wl
    # Knowledge points are at: 课程/马克思主义原理/知识点/<subfolder>/XX.md
    # Wikilinks start with ../..
    # Simply strip leading ../.. patterns and get the rest
    parts = path_part.split('/')
    result_parts = []
    for p in parts:
        if p == '..':
            continue
        else:
            result_parts.append(p)
    return '/'.join(result_parts) + '.md'

# Build keep-as-QA set (from 简答 KPs)
qa_flashcards = set()
choice_flashcards = {}

for entry in data:
    for fl in entry['flashcards']:
        fc_path = resolve_flashcard_path(fl)
        if entry['test_type'] == '简答':
            qa_flashcards.add(fc_path)
        else:
            if fc_path not in choice_flashcards:
                choice_flashcards[fc_path] = []
            choice_flashcards[fc_path].append(entry['title'])

# Only-convert flashcards: in choice_flashcards but NOT in qa_flashcards
convert_fcs = {}
for fc_path, kp_titles in choice_flashcards.items():
    if fc_path not in qa_flashcards:
        convert_fcs[fc_path] = kp_titles

print("=== FLASHCARDS THAT MUST REMAIN AS Q&A (linked by 简答 KPs) ===")
for fc in sorted(qa_flashcards):
    print(f"  {fc}")
print(f"  Total: {len(qa_flashcards)}")

print()
print("=== FLASHCARDS THAT CAN BE CONVERTED TO CLOZE (only linked by 选择判断 KPs) ===")
for fc, titles in sorted(convert_fcs.items()):
    print(f"  {fc}")
    for t in titles:
        print(f"    <- {t}")
print(f"  Total unique flashcards to convert: {len(convert_fcs)}")

# Also identify shared flashcards (in both sets)
shared = set(choice_flashcards.keys()) & qa_flashcards
print()
print("=== SHARED FLASHCARDS (linked by both 简答 and 选择判断) - KEEP AS Q&A ===")
for fc in sorted(shared):
    print(f"  {fc}")
    # which choice KPs link to it
    for t in choice_flashcards.get(fc, []):
        print(f"    <- [选择判断] {t}")
print(f"  Total shared: {len(shared)}")

# Save the convert list
output = []
for fc_path, kp_titles in sorted(convert_fcs.items()):
    output.append({'flashcard': fc_path, 'source_kps': kp_titles})

with open(r'scripts\_temp_convert_list.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print()
print(f"Convert list saved. Total: {len(output)} flashcards to convert.")
