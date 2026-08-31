---
title: draw.io CLI
type: CLI
status: 已安装
source:
  - github: "https://github.com/jgraph/drawio-desktop"
date: 2026-06-12
---

# draw.io CLI

Draw.io 桌面版命令行导出工具，将 `.drawio` XML 导出为 PNG/SVG/PDF/JPG。

## 安装

```bash
brew install --cask drawio    # macOS
# Windows: 下载安装包 https://github.com/jgraph/drawio-desktop/releases
```

## 核心用法

```bash
# 预览 PNG（不带 -e）
draw.io -x -f png -s 2 -o diagram.png input.drawio

# 最终导出（带 -e 嵌入 XML，保持可编辑）
draw.io -x -f png -e -s 2 -o diagram.drawio.png input.drawio

# SVG / PDF
draw.io -x -f svg -e -o diagram.svg input.drawio
draw.io -x -f pdf -e -o diagram.pdf input.drawio
```

**注意**：`-e` 导出的 PNG 需运行 `repair_png.py` 修复 IEND chunk。

## 关联

- [[AI/Skill/图表绘制/drawio-skill/README|drawio-skill]]
