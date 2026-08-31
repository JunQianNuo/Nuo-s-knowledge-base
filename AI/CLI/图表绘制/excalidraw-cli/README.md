---
title: excalidraw-brute-export-cli
type: CLI
status: 已安装
source:
  - npm: "excalidraw-brute-export-cli"
date: 2026-06-12
---

# excalidraw-brute-export-cli

Excalidraw 图表命令行导出工具，基于 Firefox（Playwright），将 `.excalidraw` JSON 导出为 PNG/SVG。

## 安装

```bash
npm install -g excalidraw-brute-export-cli
npx playwright install firefox
```

**macOS 需额外打补丁**（替换 Ctrl 为 Meta 快捷键）。

## 核心用法

```bash
# PNG（2x 缩放推荐）
excalidraw-brute-export-cli -i diagram.excalidraw -o diagram.png -f png -s 2

# SVG
excalidraw-brute-export-cli -i diagram.excalidraw -o diagram.svg -f svg -s 1
```

**备选**：Kroki API 零安装导出 SVG（仅需 curl）。

## 关联

- [[AI/Skill/图表绘制/excalidraw/README|excalidraw]]
