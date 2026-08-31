import os, json

BASE = r"D:\知识库\闪卡"
folders = []
for root, dirs, files in os.walk(BASE):
    if any(f.endswith('.md') for f in files):
        rel = os.path.relpath(root, BASE).replace("\\", "/")
        full = "闪卡/" + rel.rstrip("/") if rel != "." else "闪卡"
        folders.append(full)

config_path = r"D:\知识库\.obsidian\plugins\yanki\data.json"
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

old = config['folders']
config['folders'] = sorted(folders)

with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print(f"Changed: {len(old)} parent -> {len(folders)} individual folders")
for f in sorted(folders):
    print(f"  {f}")
