---
title: tldraw CLI
type: CLI
status: 已安装
source:
  - npm: "@kitschpatrol/tldraw-cli"
date: 2026-06-12
---

# tldraw CLI

Tldraw 白板图表命令行导出工具，将 `.tldr` JSON 导出为 PNG/SVG。

## 安装

```bash
npm install -g @kitschpatrol/tldraw-cli
tldraw --version
```

## 核心用法

```bash
# PNG（2x 缩放推荐）
tldraw export diagram.tldr -f png --scale 2 -o ./

# SVG
tldraw export diagram.tldr -f svg -o ./

# 透明背景 / 深色主题
tldraw export diagram.tldr -f png --scale 2 --transparent -o ./
tldraw export diagram.tldr -f png --scale 2 --dark -o ./
```

`-o` 是输出目录（非文件名），文件名自动匹配输入名。

## 关联

- [[AI/Skill/图表绘制/tldraw-skill/README|tldraw-skill]]
