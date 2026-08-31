---
title: asta-skill
type: Skill
status: 已安装
date: 2026-06-12
---

# asta-skill

Ai2 Asta MCP — Semantic Scholar 学术图谱的 MCP 接口。

## 完整功能

### MCP 端点

- 端点：`https://asta-tools.allen.ai/mcp/v1`
- 认证：`x-api-key` header
- 传输：streamable HTTP

### 工具映射

| 用户意图 | Asta 工具 |
|----------|-----------|
| 广泛主题搜索 | `search_papers_by_relevance`（支持 venue + date 过滤） |
| 已知论文标题 | `search_paper_by_title` |
| 已知 DOI/arXiv/PMID 等 | `get_paper` |
| 多个已知 ID | `get_paper_batch`（批量，优于 N 次 `get_paper`） |
| 谁引用了论文 X | `get_citations`（分页，含过滤） |
| 按名找作者 | `search_authors_by_name` |
| 作者发表列表 | `get_author_papers` |
| 找提及 X 的段落 | `snippet_search`（~500词摘录） |

### 过滤器

`publication_date_range`（`YYYY-MM-DD:YYYY-MM-DD`，支持简写 `"2021:"`/`":2015"`）、`venues`（逗号分隔）

### `fields` 参数注意事项

- **禁止**通过 `fields` 请求 `citations` 或 `references`（高引论文会溢出上下文窗口）
- 安全默认：`title,year,authors,venue,tldr,url,abstract`
- `externalIds` 非官方支持但可用（获取 DOI/arXiv/PubMed ID）

### 工作流模式

| 模式 | 步骤 |
|------|------|
| **主题发现** | `search_papers_by_relevance` → 按引用+时效排序 → 提供 `get_citations`/`snippet_search` 后续 |
| **种子扩展** | `get_paper` → `get_citations` → `search_papers_by_relevance` |
| **作者深挖** | `search_authors_by_name` → `get_author_papers` → 客户端按主题过滤 |
| **证据检索** | `snippet_search` → `get_paper` 获取元数据 |

### 关键规则

- 优先批量：独立查询并行 MCP 调用
- 不猜测 ID：模糊标题先用 `search_paper_by_title`
- 不编造字段：null 就说 null
