---
title: paper-fetch
type: Skill
status: 已安装
date: 2026-06-12
---

# paper-fetch

论文 PDF 下载引擎，多源自动解析。

## 完整功能

### 解析优先级链

1. **Unpaywall** — `api.unpaywall.org`（需 `UNPAYWALL_EMAIL`）
2. **Semantic Scholar** — `openAccessPdf` 字段
3. **arXiv** — 如果有 arXiv ID
4. **PubMed Central OA** — 如果有 PMCID
5. **bioRxiv / medRxiv** — DOI 前缀 `10.1101`
6. **出版商直连**（机构模式）— Nature/Science/Wiley/Springer/ACS/PNAS/NEJM 等
7. **Sci-Hub 镜像**（默认开启，可通过 `PAPER_FETCH_NO_SCIHUB=1` 关闭）

### URL 解析流程

标题 → DOI 的解析链：
1. **Crossref** `query.title` — 主解析器
2. **Semantic Scholar** `match_title` — 备选（处理 arXiv-only 论文）
3. **Crossref 低置信度** — 最后手段，标记 `low_confidence: true`

### 用法

```bash
python scripts/fetch.py <DOI>
python scripts/fetch.py --title "<标题>"
python scripts/fetch.py --batch <文件>        # 批量
python scripts/fetch.py schema                # 机器可读自描述
```

### 关键参数

| 参数 | 默认 | 用途 |
|------|------|------|
| `--out DIR` | `pdfs` | 输出目录 |
| `--format` | auto | `json`（agent）/ `text`（人） |
| `--idempotency-key KEY` | — | 安全重试，重跑回放原始结果不网络IO |
| `--dry-run` | — | 只解析不下载 |
| `--stream` | — | 流式输出，每 DOI 一行 |
| `--batch FILE` | — | 批量文件，用 `-` 读 stdin |
| `--overwrite` | — | 覆盖已有文件 |

### 输出结构

**成功**：`ok: true`，含 `doi`、`source`、`pdf_url`、`file`、`meta`（标题/年份/作者）、`sources_tried`

**部分成功**：`ok: "partial"`，`data.next` 列出失败 DOI 的重试命令

**失败**：`ok: false`，含 `error.code`（`not_found` / `download_network_error` / `download_not_a_pdf` 等）

### stderr 进度事件

`session` → `start` → `source_try` → `source_hit`/`source_miss` → `download_ok`/`download_error`

### 退出码

| 码 | 含义 | 可重试 |
|----|------|--------|
| 0 | 全部成功 | — |
| 1 | 无 OA 副本 | 7天后 |
| 3 | 参数错误 | 否 |
| 4 | 网络/IO 错误 | 是 |

### 环境变量

| 变量 | 用途 |
|------|------|
| `UNPAYWALL_EMAIL` | Unpaywall API 邮箱（可选但推荐） |
| `PAPER_FETCH_INSTITUTIONAL` | 启用机构模式（出版商直连 + 1req/s 限速） |
| `PAPER_FETCH_NO_SCIHUB` | 禁用 Sci-Hub 后备 |
| `PAPER_FETCH_SCIHUB_MIRRORS` | 自定义 Sci-Hub 镜像列表 |

### 安全

- SSRF 防御：阻止私有 IP / 非 http(s) / 云元数据
- `%PDF` 魔术字节校验 + 50MB 上限
- 不自动登录，不破解 CAPTCHA
- 机构模式需操作者设置环境变量（agent 不能自启）
