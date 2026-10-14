# -*- coding: utf-8 -*-
"""临时脚本：按列重建课表全文（TSV 坐标精确聚类）"""
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

TSV = r'D:\知识库\tmp\kebiao_tsv2.tsv'
COLUMNS = [('节次', 0, 130), ('周一', 130, 380), ('周二', 380, 620),
           ('周三', 620, 870), ('周四', 870, 1120), ('周五', 1120, 1400)]

words = []
with open(TSV, encoding='utf-8') as f:
    for row in csv.DictReader(f, delimiter='\t'):
        if row.get('level') != '5' or not row.get('text', '').strip():
            continue
        try:
            conf = float(row['conf'])
        except (ValueError, KeyError):
            continue
        if conf < 30:
            continue
        words.append((int(row['top']), int(row['left']),
                      int(row['width']), int(row['height']), row['text'].strip()))

# 每列内按 top 聚类成行（行距 ~18px 内的词合并）
for cname, x0, x1 in COLUMNS:
    col = [w for w in words if x0 <= w[1] < x1]
    col.sort(key=lambda w: w[0])
    rows = []  # (center, [ (left,text) ])
    for top, left, w, h, text in col:
        placed = False
        for r in rows:
            if abs(r[0] - (top + h / 2)) < 12:
                r[1].append((left, text))
                placed = True
                break
        if not placed:
            rows.append([top + h / 2, [(left, text)]])
    rows.sort(key=lambda r: r[0])
    print(f'\n===== {cname}（{x0}-{x1}px，{len(col)} 词）=====')
    for center, ws in rows:
        ws.sort(key=lambda x: x[0])
        print(f'  y={int(center):4d} | {"".join(t for _, t in ws)}')
