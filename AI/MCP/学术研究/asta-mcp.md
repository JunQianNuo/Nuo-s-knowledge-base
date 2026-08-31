---
title: Asta MCP
type: MCP
status: 已安装
source:
  - endpoint: "https://asta-tools.allen.ai/mcp/v1"
  - provider: "Ai2 (Allen Institute for AI)"
date: 2026-06-12
---

# Asta MCP

Ai2 的 Semantic Scholar 学术图谱 MCP 接口，streamable HTTP 传输。

## 端点

- **URL**: `https://asta-tools.allen.ai/mcp/v1`
- **认证**: `x-api-key` header
- **传输**: streamable HTTP

## 工具

| 工具 | 用途 |
|------|------|
| `search_papers_by_relevance` | 广泛主题搜索，支持 venue + date 过滤 |
| `search_paper_by_title` | 已知论文标题精确匹配 |
| `get_paper` | 按 DOI/arXiv/PMID/CorpusId 查找 |
| `get_paper_batch` | 批量查找（优于 N 次 `get_paper`） |
| `get_citations` | 引用遍历，分页含过滤 |
| `search_authors_by_name` | 按名找作者 |
| `get_author_papers` | 作者发表列表 |
| `snippet_search` | 全文段落搜索（~500 词摘录） |

## 关联

- [[AI/Skill/学术研究/asta-skill/README|asta-skill]]
