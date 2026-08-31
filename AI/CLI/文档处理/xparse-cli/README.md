---
title: xparse-cli
type: CLI
status: 已安装
source:
  - url: "https://dllf.intsig.net/download/2026/Solution/xparse-cli/"
date: 2026-06-12
---

# xparse-cli

> **注意**：[[AI/CLI/文档处理/mineru/README|MinerU]] 已成为本仓库的主要文档解析方案。本工具保留为备用（需要远程解析或 JSON 输出时使用）。

文档解析命令行工具，将 PDF/图片/Office/HTML/OFD 转为 Markdown 或 JSON。

## 安装

```powershell
# Windows
irm https://dllf.intsig.net/download/2026/Solution/xparse-cli/install.ps1 | iex
```

## 核心用法

```bash
xparse-cli parse report.pdf                    # Markdown → stdout
xparse-cli parse file.pdf --view json          # JSON → stdout
xparse-cli parse file.pdf --output ./out/      # 保存到文件
xparse-cli parse file.pdf --page-range 1-5     # 指定页面
xparse-cli parse encrypted.pdf --password pwd  # 加密文档
```

## 关联

- [[AI/Skill/文档处理/xparse-parse/README|xparse-parse skill]]
