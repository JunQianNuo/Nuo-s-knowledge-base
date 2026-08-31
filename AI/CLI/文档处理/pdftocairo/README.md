---
title: pdftocairo
type: CLI
status: 已安装
source:
  - package: poppler-utils
date: 2026-06-12
---

# pdftocairo

> **注意**：[[AI/CLI/文档处理/mineru/README|MinerU]] 已成为本仓库的主要文档解析方案。本工具保留为备用（MinerU 不可用时使用）。

Poppler 工具集成员，将 PDF 页面渲染为 PNG/JPEG/PDF等格式。

## 安装/配置

属于 poppler-utils 包，通过系统包管理器安装。

## 使用说明

本仓库用于 PDF → 图片预处理，为 Tesseract OCR 准备输入：

```
pdftocairo -png -r 300 input.pdf output_prefix
```

参数：
- `-png`：输出 PNG 格式
- `-r 300`：300 DPI 分辨率（OCR 推荐）

## 相关

- [[AI/CLI/tesseract/README|Tesseract OCR]]（后续 OCR 步骤）
