---
title: mmdc (Mermaid CLI)
type: CLI
status: 已安装
source:
  - npm: "@mermaid-js/mermaid-cli"
date: 2026-06-12
---

# mmdc (Mermaid CLI)

Mermaid 官方命令行渲染工具，将 `.mmd` 文件导出为 PNG/SVG/PDF。

## 安装

```bash
npm install -g @mermaid-js/mermaid-cli
mmdc --version
```

## 核心用法

```bash
# PNG（推荐 2048px 宽，白色背景）
mmdc -i diagram.mmd -o diagram.png -w 2048 --backgroundColor white

# SVG
mmdc -i diagram.mmd -o diagram.svg

# PDF
mmdc -i diagram.mmd -o diagram.pdf
```

## 关联

- [[AI/Skill/图表绘制/creating-mermaid-diagrams/README|creating-mermaid-diagrams]]
