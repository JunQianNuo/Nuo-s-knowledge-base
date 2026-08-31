"""Generate probability exercise files from MinerU extracted content - v2 with correct boundaries."""
import json, re, os, shutil

OUT = r'D:\知识库\课程\概率论\习题库'

# Timestamp-based chapter boundaries (verified against content)
CHAPTER_BOUNDARIES = [
    ('01-概率基础', 1, 0, 21),    # items 0-20: 概率基础(生日/球/牌/σ代数/条件概率/全概率/贝叶斯)
    ('02-随机变量', 2, 21, 35),   # items 21-34: 离散型/连续型/分布函数/常见分布
    ('03-多维随机变量', 3, 35, 57), # items 35-56: 联合分布/独立性/条件分布/函数分布
    ('04-数字特征', 4, 57, 78),   # items 57-77: 期望/方差/协方差/相关系数/条件期望
    ('05-极限定理', 5, 78, 97),   # items 78-96: CLT/大数定律/特征函数/收敛性
]

with open(r'D:\知识库\课程\概率论\未处理\mineru_output\all_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Clean and recreate
for d in os.listdir(OUT):
    dp = os.path.join(OUT, d)
    if os.path.isdir(dp):
        shutil.rmtree(dp)

total = 0
for dirname, ch_num, start, end in CHAPTER_BOUNDARIES:
    ch_name = dirname.split('-', 1)[1]
    ch_dir = os.path.join(OUT, dirname)
    os.makedirs(ch_dir, exist_ok=True)
    items = data[start:end]

    # Generate README
    readme = f'''---
title: 第{ch_num}章 习题库 - {ch_name}
subject: 概率论
chapter: {ch_num}
type: MOC
---

# 习题库：第{ch_num}章 {ch_name}

> 本章共 {len(items)} 道习题，MinerU 云 API 提取自答题平台截图。印刷题目已提取，手写答案/解析待校对补充。

## 习题列表

| 编号 | 题目简述 | 类型 |
|:--|:--|:--|
'''
    for i, item in enumerate(items, 1):
        md = item['md']
        lines = [l.strip() for l in md.split('\n') if l.strip() and not l.startswith('![')]
        title_line = ''
        for l in lines:
            clean = re.sub(r'^##\s*.*?页\s*$', '', l)
            clean = re.sub(r'^\d+/\d+\s*(单选题|证明/计算/分析题|选择题|判断题)?\s*', '', clean).strip()
            clean = re.sub(r'^<\s*.*?页\s*$', '', clean)
            if clean and len(clean) > 5 and not clean.startswith('#'):
                title_line = clean[:70]
                break
        if not title_line:
            title_line = '(见原文)'
        qtype = '选择题' if re.search(r'A\s*\$', md) else ('判断题' if '判断' in md else '计算/证明')
        readme += f'| 习题{ch_num}.{i} | {title_line} | {qtype} |\n'

    readme += f'''
## 知识点覆盖

待补充（对照 [[../../知识点解析梳理/|知识梳理]] 标注）。

## 回链

- 课件：[[../../PPT课件/MD/|PPT课件]]
- 知识梳理：[[../../知识点解析梳理/|知识点解析梳理]]
- 复习纲要：[[../../复习/README|复习纲要]]
'''
    with open(os.path.join(ch_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)

    # Generate individual exercise files
    for i, item in enumerate(items, 1):
        md = item['md']
        fn = item['file']

        lines = [l.strip() for l in md.split('\n') if l.strip() and not l.startswith('![')]
        title_line = ''
        for l in lines:
            clean = re.sub(r'^##\s*.*?页\s*$', '', l)
            clean = re.sub(r'^\d+/\d+\s*(单选题|证明/计算/分析题|选择题|判断题)?\s*', '', clean).strip()
            clean = re.sub(r'^<\s*.*?页\s*$', '', clean)
            if clean and len(clean) > 5 and not clean.startswith('#'):
                title_line = clean[:60]
                break
        if not title_line:
            title_line = f'第{ch_num}章习题{i}'

        qtype = '选择题' if re.search(r'A\s*\$', md) else ('判断题' if '判断' in md else '计算/证明')

        # Clean body
        body_lines = []
        seen = set()
        for l in lines:
            clean = re.sub(r'^##\s*.*?页\s*$', '', l)
            clean = re.sub(r'^\d+/\d+\s*(单选题|证明/计算/分析题|选择题|判断题)?\s*', '', clean).strip()
            clean = re.sub(r'^<\s*.*?页\s*$', '', clean)
            skip_words = ['回答正确','+1分','本题得分','+3分','参考答案','请作答','请输入您的答案',
                         '上传图片','下一题','答题卡','参考']
            if clean and len(clean) > 2 and clean not in seen and not any(w in clean for w in skip_words):
                seen.add(clean)
                body_lines.append(clean)

        body = '\n\n'.join(body_lines)

        fm = f'''---
title: 习题{ch_num}.{i} - {title_line[:35]}
subject: 概率论
chapter: {ch_num}
section: {ch_name}
source: {fn}
status: MinerU提取（待校对）
type: 习题
type_tag: {qtype}
topics:
  - {ch_name}
---

'''
        hint = '\n\n> [!hint]- 点击展开提示\n> 待补充\n'
        sol = '\n\n> [!solution]- 点击展开详细解析\n> 待补充（需对照原始截图手写答案）\n'
        links = f'\n\n---\n\n## 相关知识点\n\n- [[../../知识点解析梳理/|知识梳理]]\n- [[../../复习/README|复习纲要]]\n'

        full = fm + body + hint + sol + links
        full = re.sub(r'!\[.*?\]\(.*?\)', '', full)
        full = re.sub(r'image_\d+\.jpg', '', full)
        full = re.sub(r'\n{3,}', '\n\n', full)

        fname = f'习题{ch_num}.{i}.md'
        with open(os.path.join(ch_dir, fname), 'w', encoding='utf-8') as f:
            f.write(full)
        total += 1

print(f'Done! {total} exercise files in 5 chapter folders')
for dirname, ch_num, start, end in CHAPTER_BOUNDARIES:
    print(f'  {dirname}: {end-start} 题 (items {start}-{end-1})')
