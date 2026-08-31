---
title: Tesseract OCR
type: CLI
status: 已安装
source:
  - url: "https://github.com/tesseract-ocr/tesseract"
  - path: "C:/Program Files/Tesseract-OCR/tesseract.exe"
date: 2026-06-12
---

# Tesseract OCR

> **注意**：[[AI/CLI/文档处理/mineru/README|MinerU]] 已成为本仓库的主要文档解析方案。本工具保留为备用（MinerU 不可用时使用）。

开源 OCR 引擎，用于将 PDF/图片中的文字提取为文本。

## 安装/配置

- 安装路径：`C:/Program Files/Tesseract-OCR/tesseract.exe`
- 中文语言包：`tessdata/chi_sim.traineddata`（手动下载）
- 使用参数：`--psm 4`（假设单列文本），语言 `chi_sim+eng`

## 使用说明

本仓库主要用于 PDF 课件 OCR：
```
tesseract input.png output -l chi_sim+eng --psm 4
```

后处理规则：
- 移除 CJK 字符间多余空格
- 修复常见 OCR 错误：矩防→矩阵、刑技大学→科技大学、孔→子

## 相关

- [[AI/CLI/pdftocairo/README|pdftocairo]]（PDF → PNG 预处理）
