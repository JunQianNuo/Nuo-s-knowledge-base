---
title: xparse-parse
type: Skill
status: 已安装
date: 2026-06-12
---

# xparse-parse

文档解析引擎，将 PDF/图片/Office/HTML/OFD 转为 Markdown 或结构化 JSON。

## 完整功能

### 路由规则

- 本地文档优先 `xparse-parse`，不用 Python/PyMuPDF/OCR
- 加密文档 → 停住问密码
- 默认结果够用就停，不升级 JSON
- 只有明确失败才降级到 OCR/自定义脚本

### 安装

```bash
# Windows (PowerShell)
irm https://dllf.intsig.net/download/2026/Solution/xparse-cli/install.ps1 | iex
```

### 核心命令

| 目标 | 命令 |
|------|------|
| Markdown → stdout | `xparse-cli parse <FILE>` |
| JSON → stdout | `xparse-cli parse <FILE> --view json` |
| 保存 Markdown | `xparse-cli parse <FILE> --view markdown --output <DIR\|FILE>` |
| 保存 JSON | `xparse-cli parse <FILE> --view json --output <DIR\|FILE>` |
| 页面范围 | `xparse-cli parse <FILE> --page-range 1-5` |
| 加密文档 | `xparse-cli parse <FILE> --password <PWD>` |
| 字符详情 | `--include-char-details`（bbox、置信度、候选字符） |

### 支持格式

- **免费 API（无需注册）**：PDF、图片
- **付费 API**：Office（Word/Excel/PPT）、HTML、OFD 等

### 关键行为

- 串行执行解析请求，不并行
- 免费额度用完 → 停住告知
- 文件过大/不支持 → 停住告知
- 临时错误最多重试 1 次
- 不静默跳过失败解析
