#!/usr/bin/env python3
"""Generate 马克思主义原理-知识图谱.canvas — beautified layout."""

import json
import os
import random

random.seed(2025)

VAULT = r"D:\知识库"
BASE = r"课程/马克思主义原理/知识点"

# Chapter definitions: (folder, label, emoji, group, color_hex, files)
CHAPTERS = [
    # === 哲学篇 ===
    ("导论", "导论", "📖", "哲学篇", "#3b7dd8", [
        ("01", "马克思主义定义与组成", "01-马克思主义定义与组成.md"),
        ("02", "创立与发展", "02-马克思主义创立与发展.md"),
        ("03", "基本特征", "03-马克思主义基本特征.md"),
        ("04", "当代价值 ⭐", "04-马克思主义当代价值.md"),
        ("05", "学习运用", "05-学习运用马克思主义.md"),
    ]),
    ("唯物论", "唯物论", "🌍", "哲学篇", "#3b7dd8", [
        ("01", "哲学基本问题", "01-哲学基本问题.md"),
        ("02", "列宁物质定义", "02-列宁物质定义.md"),
        ("03", "物质范畴理论意义 ⭐", "03-物质范畴理论意义.md"),
        ("04", "物质的存在方式", "04-物质的存在方式.md"),
        ("05", "物质世界二重化", "05-物质世界二重化.md"),
        ("06", "意识本质", "06-意识本质.md"),
        ("07", "意识能动作用 ⭐⭐⭐", "07-意识能动作用.md"),
        ("08", "主观能动性与客观规律 ⭐", "08-主观能动性与客观规律.md"),
        ("09", "AI与人智能 ⭐", "09-AI与人智能.md"),
        ("10", "物质统一性 ⭐", "10-物质统一性.md"),
    ]),
    ("唯物辩证法", "唯物辩证法", "⚡", "哲学篇", "#3b7dd8", [
        ("01", "两大总特征", "01-两大总特征.md"),
        ("02", "五对基本范畴", "02-五对基本范畴.md"),
        ("03", "联系特点 ⭐", "03-联系特点.md"),
        ("04", "新事物与旧事物", "04-新事物与旧事物.md"),
        ("05", "矛盾同一性与斗争性 ⭐", "05-矛盾同一性与斗争性.md"),
        ("06", "矛盾普遍性与特殊性", "06-矛盾普遍性与特殊性.md"),
        ("07", "两点论与重点论", "07-两点论与重点论.md"),
        ("08", "量变质变规律 ⭐", "08-量变质变规律.md"),
        ("09", "辩证否定观 ⭐", "09-辩证否定观.md"),
        ("10", "否定之否定规律", "10-否定之否定规律.md"),
        ("11", "六种思维能力", "11-六种思维能力.md"),
        ("12", "唯物辩证法认识功能", "12-唯物辩证法认识功能.md"),
    ]),
    ("认识论", "认识论", "🧠", "哲学篇", "#3b7dd8", [
        ("01", "科学实践观意义 ⭐", "01-科学实践观意义.md"),
        ("02", "实践本质", "02-实践本质.md"),
        ("03", "实践基本特征 ⭐⭐⭐", "03-实践基本特征.md"),
        ("04", "实践基本结构 ⭐", "04-实践基本结构.md"),
        ("05", "实践形式", "05-实践形式.md"),
        ("06", "实践决定认识 ⭐⭐⭐", "06-实践决定认识.md"),
        ("07", "认识本质", "07-认识本质.md"),
        ("08", "感性理性认识 ⭐", "08-感性理性认识.md"),
        ("09", "两次飞跃", "09-两次飞跃.md"),
        ("10", "非理性因素", "10-非理性因素.md"),
        ("11", "真理三大属性 ⭐", "11-真理三大属性.md"),
        ("12", "真理与谬误", "12-真理与谬误.md"),
        ("13", "实践检验真理 ⭐", "13-实践检验真理.md"),
        ("14", "真理与价值统一", "14-真理与价值统一.md"),
    ]),
    ("历史唯物主义", "历史唯物主义", "👥", "哲学篇", "#3b7dd8", [
        ("01", "社会存在与社会意识 ⭐", "01-社会存在与社会意识.md"),
        ("02", "生产方式决定力量", "02-生产方式决定力量.md"),
        ("03", "生产力与生产关系", "03-生产力与生产关系.md"),
        ("04", "经济基础与上层建筑", "04-经济基础与上层建筑.md"),
        ("05", "社会基本矛盾作用", "05-社会基本矛盾作用.md"),
        ("06", "科技作用", "06-科技作用.md"),
        ("07", "文化作用", "07-文化作用.md"),
        ("08", "交往作用", "08-交往作用.md"),
        ("09", "人民群众决定作用 ⭐", "09-人民群众决定作用.md"),
        ("10", "群众观点与群众路线", "10-群众观点与群众路线.md"),
        ("11", "社会革命作用", "11-社会革命作用.md"),
        ("12", "群众阶级政党领袖", "12-群众阶级政党领袖.md"),
    ]),
    # === 政治经济学篇 ===
    ("商品经济理论", "商品经济理论", "💰", "政治经济学篇", "#2ea043", [
        ("01", "商品二因素", "01-商品二因素.md"),
        ("02", "劳动二重性", "02-劳动二重性.md"),
        ("03", "价值量决定", "03-价值量决定.md"),
        ("04", "货币职能", "04-货币职能.md"),
        ("05", "价值规律", "05-价值规律.md"),
        ("06", "基本矛盾", "06-私有制商品经济基本矛盾.md"),
        ("07", "劳动价值论意义", "07-劳动价值论意义.md"),
        ("08", "深化劳动价值论", "08-深化劳动价值论.md"),
    ]),
    ("剩余价值生产", "剩余价值生产", "🏭", "政治经济学篇", "#2ea043", [
        ("01", "资本总公式", "01-资本总公式.md"),
        ("02", "劳动力商品条件", "02-劳动力商品条件.md"),
        ("03", "劳动力价值三部分", "03-劳动力价值三部分.md"),
        ("04", "生产过程二重性", "04-生产过程二重性.md"),
        ("05", "不变可变资本", "05-不变可变资本.md"),
        ("06", "资本有机构成", "06-资本有机构成.md"),
        ("07", "剩余价值率", "07-剩余价值率.md"),
        ("08", "剩余价值理论意义", "08-剩余价值理论意义.md"),
        ("09", "资本主义基本矛盾", "09-资本主义基本矛盾.md"),
        ("10", "经济危机", "10-经济危机.md"),
    ]),
    ("剩余价值分配", "剩余价值分配", "📊", "政治经济学篇", "#2ea043", [
        ("01", "绝对相对剩余价值 ⭐", "01-绝对相对剩余价值.md"),
        ("02", "超额剩余价值", "02-超额剩余价值.md"),
        ("03", "工资本质", "03-工资本质.md"),
        ("04", "利润与平均利润", "04-利润与平均利润.md"),
        ("05", "价值转生产价格", "05-价值转生产价格.md"),
        ("06", "商业利润等来源", "06-商业利润等来源.md"),
    ]),
    ("资本积累与再生产", "资本积累与再生产", "🔄", "政治经济学篇", "#2ea043", [
        ("01", "资本积累与再生产", "01-资本积累与再生产.md"),
        ("02", "资本循环", "02-资本循环.md"),
        ("03", "产业资本循环条件", "03-产业资本循环条件.md"),
        ("04", "固定资本与流动资本", "04-固定资本与流动资本.md"),
        ("05", "社会总产品", "05-社会总产品.md"),
        ("06", "社会再生产实现条件", "06-社会再生产实现条件.md"),
        ("07", "资本积聚与资本集中", "07-资本积聚与资本集中.md"),
        ("08", "相对过剩人口", "08-相对过剩人口.md"),
    ]),
    ("资本主义上层建筑", "资本主义上层建筑", "🏛️", "政治经济学篇", "#2ea043", [
        ("01", "国家本质", "01-国家本质.md"),
        ("02", "民主制度本质", "02-民主制度本质.md"),
        ("03", "政治制度局限性", "03-政治制度局限性.md"),
        ("04", "意识形态本质", "04-意识形态本质.md"),
    ]),
    # === 科学社会主义篇 ===
    ("科学社会主义", "科学社会主义", "🚩", "科学社会主义篇", "#8250df", [
        ("01", "诞生标志", "01-诞生标志.md"),
        ("02", "无产阶级革命", "02-无产阶级革命.md"),
        ("03", "马克思主义政党", "03-马克思主义政党.md"),
        ("04", "共产主义基本特征", "04-共产主义基本特征.md"),
        ("05", "两个必然与决不会", "05-两个必然与决不会.md"),
    ]),
    # === 概念辨析 ===
    ("概念辨析", "概念辨析", "⚖️", "概念辨析", "#cf222e", [
        ("01", "使用价值 vs 价值", "01-使用价值vs价值.md"),
        ("02", "具体劳动 vs 抽象劳动", "02-具体劳动vs抽象劳动.md"),
        ("03", "不变资本 vs 可变资本", "03-不变资本vs可变资本.md"),
        ("04", "绝对 vs 相对剩余价值", "04-绝对vs相对剩余价值.md"),
        ("05", "固定资本 vs 流动资本", "05-固定资本vs流动资本.md"),
        ("06", "资本循环 vs 资本周转", "06-资本循环vs资本周转.md"),
        ("07", "感性认识 vs 理性认识", "07-感性认识vs理性认识.md"),
        ("08", "社会存在 vs 社会意识", "08-社会存在vs社会意识.md"),
        ("09", "量变 vs 质变", "09-量变vs质变.md"),
        ("10", "矛盾同一性 vs 斗争性", "10-矛盾同一性vs斗争性.md"),
    ]),
]

GROUP_META = {
    "哲学篇": {
        "label": "📘 哲学篇 · 辩证唯物主义与历史唯物主义",
        "color": "5",   # cyan preset
        "bg_hex": "#ddf4ff",
    },
    "政治经济学篇": {
        "label": "📗 政治经济学篇 · 资本主义经济制度",
        "color": "4",   # green preset
        "bg_hex": "#dafbe1",
    },
    "科学社会主义篇": {
        "label": "📙 科学社会主义篇",
        "color": "6",   # purple preset
        "bg_hex": "#fbefff",
    },
    "概念辨析": {
        "label": "📕 概念辨析 · 易混淆概念对比",
        "color": "1",   # red preset
        "bg_hex": "#ffeef0",
    },
}

def gen_id():
    return ''.join(random.choice('0123456789abcdef') for _ in range(16))

def build_canvas():
    nodes = []
    edges = []
    node_ids = {}

    # === Layout constants ===
    CHAPTER_W = 280
    CHAPTER_H = 72
    FILE_W = 260
    FILE_H = 44
    FILE_GAP = 6
    ROOT_W = 380
    ROOT_H = 100
    COL_GAP = 40
    COL_WIDTH = CHAPTER_W + COL_GAP  # 320

    # === Root node ===
    root_id = gen_id()
    root_x = -190
    root_y = -420

    nodes.append({
        "id": root_id,
        "type": "text",
        "x": root_x,
        "y": root_y,
        "width": ROOT_W,
        "height": ROOT_H,
        "text": "# 🔴 马克思主义原理\n\n##### 知识图谱 · 点击节点跳转知识点\n\n*104 个知识点 · 12 个章节 · 4 大板块*",
        "color": "1",
    })

    # === Position chapters ===
    # Philosophy: 5 columns in one row
    philo_chapters = ["导论", "唯物论", "唯物辩证法", "认识论", "历史唯物主义"]
    PHILO_START_X = -1400
    PHILO_Y = -200

    # Economics: 5 columns in second row
    econ_chapters = ["商品经济理论", "剩余价值生产", "剩余价值分配", "资本积累与再生产", "资本主义上层建筑"]
    ECON_START_X = -1400
    # ECON_Y computed after philosophy row

    # Right side
    RIGHT_X = 500
    SS_Y = -200
    CB_Y = 280

    chapter_positions = {}
    for i, ch in enumerate(philo_chapters):
        chapter_positions[ch] = (PHILO_START_X + i * COL_WIDTH, PHILO_Y)
    for i, ch in enumerate(econ_chapters):
        chapter_positions[ch] = (ECON_START_X + i * COL_WIDTH, 0)  # temp, compute later
    chapter_positions["科学社会主义"] = (RIGHT_X, SS_Y)
    chapter_positions["概念辨析"] = (RIGHT_X, CB_Y)

    # First pass: compute file list heights
    chapter_heights = {}
    for folder, label, emoji, group, color, files in CHAPTERS:
        ch_h = CHAPTER_H + 24 + len(files) * (FILE_H + FILE_GAP)
        chapter_heights[folder] = ch_h

    # Compute ECON_Y based on max philosophy height
    max_philo_h = max(chapter_heights[ch] for ch in philo_chapters)
    ECON_Y = PHILO_Y + max_philo_h + 120

    for i, ch in enumerate(econ_chapters):
        chapter_positions[ch] = (ECON_START_X + i * COL_WIDTH, ECON_Y)

    max_econ_h = max(chapter_heights[ch] for ch in econ_chapters)

    # === Build nodes ===
    for folder, label, emoji, group, color, files in CHAPTERS:
        ch_x, ch_y = chapter_positions[folder]

        # Chapter header node
        ch_id = gen_id()
        # Count exam markers
        star_count = sum(1 for _, name, _ in files if '⭐' in name)
        triple_count = sum(1 for _, name, _ in files if '⭐⭐⭐' in name)
        stats = f"{len(files)} 个知识点"
        if star_count:
            stats += f" · {star_count} 简答"
        if triple_count:
            stats += f" · {triple_count} 真题"

        nodes.append({
            "id": ch_id,
            "type": "text",
            "x": ch_x,
            "y": ch_y,
            "width": CHAPTER_W,
            "height": CHAPTER_H,
            "text": f"## {emoji} {label}\n\n*{stats}*",
            "color": color,
        })

        # Edge: root → chapter
        edges.append({
            "id": gen_id(),
            "fromNode": root_id,
            "fromSide": "bottom",
            "toNode": ch_id,
            "toSide": "top",
            "toEnd": "arrow",
            "color": color,
        })

        # File nodes
        file_y_start = ch_y + CHAPTER_H + 24
        for nn, display, filename in files:
            fid = gen_id()
            node_ids[(folder, nn)] = fid

            # Display name with exam markers
            nodes.append({
                "id": fid,
                "type": "file",
                "x": ch_x + 10,
                "y": file_y_start,
                "width": FILE_W,
                "height": FILE_H,
                "file": f"{folder}/{filename}",
                "color": color,
            })

            # Edge: chapter → file
            edges.append({
                "id": gen_id(),
                "fromNode": ch_id,
                "fromSide": "bottom",
                "toNode": fid,
                "toSide": "left",
                "toEnd": "arrow",
                "color": color,
            })

            file_y_start += FILE_H + FILE_GAP

    # === Cross-group edges (概念辨析 → related chapters) ===
    cross_edges = [
        ("概念辨析", "01", "商品经济理论", "01"),
        ("概念辨析", "02", "商品经济理论", "02"),
        ("概念辨析", "03", "剩余价值生产", "05"),
        ("概念辨析", "04", "剩余价值分配", "01"),
        ("概念辨析", "05", "资本积累与再生产", "04"),
        ("概念辨析", "06", "资本积累与再生产", "02"),
        ("概念辨析", "07", "认识论", "08"),
        ("概念辨析", "08", "历史唯物主义", "01"),
        ("概念辨析", "09", "唯物辩证法", "08"),
        ("概念辨析", "10", "唯物辩证法", "05"),
    ]

    for from_ch, from_nn, to_ch, to_nn in cross_edges:
        from_id = node_ids.get((from_ch, from_nn))
        to_id = node_ids.get((to_ch, to_nn))
        if from_id and to_id:
            edges.append({
                "id": gen_id(),
                "fromNode": from_id,
                "fromSide": "right",
                "toNode": to_id,
                "toSide": "left",
                "toEnd": "arrow",
                "color": "#cf222e",
            })

    # === Group boxes ===
    # Philosophy group
    philo_group = nodes[0]
    philo_left = PHILO_START_X - 40
    philo_top = PHILO_Y - 80
    philo_right_edge = PHILO_START_X + 5 * COL_WIDTH + 10
    philo_bottom = PHILO_Y + max_philo_h + 40

    nodes.append({
        "id": gen_id(),
        "type": "group",
        "x": philo_left,
        "y": philo_top,
        "width": philo_right_edge - philo_left,
        "height": philo_bottom - philo_top,
        "label": GROUP_META["哲学篇"]["label"],
        "color": GROUP_META["哲学篇"]["color"],
    })

    # Economics group
    econ_left = ECON_START_X - 40
    econ_top = ECON_Y - 80
    econ_right_edge = ECON_START_X + 5 * COL_WIDTH + 10
    econ_bottom = ECON_Y + max_econ_h + 40

    nodes.append({
        "id": gen_id(),
        "type": "group",
        "x": econ_left,
        "y": econ_top,
        "width": econ_right_edge - econ_left,
        "height": econ_bottom - econ_top,
        "label": GROUP_META["政治经济学篇"]["label"],
        "color": GROUP_META["政治经济学篇"]["color"],
    })

    # Scientific socialism group
    ss_h = chapter_heights["科学社会主义"]
    nodes.append({
        "id": gen_id(),
        "type": "group",
        "x": RIGHT_X - 40,
        "y": SS_Y - 80,
        "width": 360,
        "height": ss_h + 120,
        "label": GROUP_META["科学社会主义篇"]["label"],
        "color": GROUP_META["科学社会主义篇"]["color"],
    })

    # 概念辨析 group
    cb_h = chapter_heights["概念辨析"]
    nodes.append({
        "id": gen_id(),
        "type": "group",
        "x": RIGHT_X - 40,
        "y": CB_Y - 80,
        "width": 360,
        "height": cb_h + 120,
        "label": GROUP_META["概念辨析"]["label"],
        "color": GROUP_META["概念辨析"]["color"],
    })

    # === Validation ===
    all_node_ids = {n["id"] for n in nodes}
    for e in edges:
        assert e["fromNode"] in all_node_ids, f"dangling fromNode: {e['fromNode']}"
        assert e["toNode"] in all_node_ids, f"dangling toNode: {e['toNode']}"

    all_ids = [n["id"] for n in nodes] + [e["id"] for e in edges]
    assert len(all_ids) == len(set(all_ids)), "Duplicate IDs"

    # === File path validation ===
    for n in nodes:
        if n["type"] == "file":
            full = os.path.join(VAULT, BASE, n["file"])
            assert os.path.exists(full), f"Missing: {n['file']}"

    canvas = {"nodes": nodes, "edges": edges}
    output_path = os.path.join(VAULT, BASE, "马克思主义原理-知识图谱.canvas")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)

    n_file = sum(1 for n in nodes if n["type"] == "file")
    n_text = sum(1 for n in nodes if n["type"] == "text")
    n_group = sum(1 for n in nodes if n["type"] == "group")
    print(f"Canvas: {output_path}")
    print(f"  Nodes: {len(nodes)} ({n_file} file, {n_text} text, {n_group} group)")
    print(f"  Edges: {len(edges)}")
    print(f"  All 104 file paths valid")
    print(f"  All edge references valid")

if __name__ == "__main__":
    build_canvas()
