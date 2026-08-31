---
title: semanticscholar-skill
type: Skill
status: 已安装
date: 2026-06-12
---

# semanticscholar-skill

Semantic Scholar 学术搜索，结构化 4 阶段工作流。

## 完整功能

### 搜索策略决策树

| 用户意图 | 策略 | 函数 |
|----------|------|------|
| 广泛主题探索 | 批量搜索（推荐） | `search_bulk()` + `build_bool_query()` |
| 需要 TLDR/作者详情 | 相关性搜索 | `search_relevance()` |
| 精确术语/短语 | 布尔批量搜索 | `search_bulk()` + 运算符 |
| 特定段落/方法 | 片段搜索 | `search_snippets()` |
| 已知论文标题 | 标题匹配 | `match_title()` |
| 已知 DOI/PMID/arXiv | 直接查找 | `get_paper()` |
| 引用某论文的 | 引文遍历 | `get_citations()` |
| 相似论文 | 单种子推荐 | `find_similar()` |
| 多篇相关 | 多种子推荐 | `recommend()` |
| 找研究者 | 作者搜索 | `search_authors()` |
| 研究者详情 | 作者信息 | `get_author()` |
| 研究者发表 | 作者论文 | `get_author_papers()` |

### 布尔查询语法

| 语法 | 示例 | 含义 |
|------|------|------|
| `"..."` | `"deep learning"` | 精确短语 |
| `+` | `+transformer` | 必须包含 |
| `-` | `-survey` | 排除 |
| `\|` | `CNN \| RNN` | OR |
| `*` | `neuro*` | 前缀通配 |
| `()` | `(CNN \| RNN) +attention` | 分组 |
| `term~N` | `bugs~3` | 模糊匹配 N 编辑距离内 |
| `"phrase"~N` | `"blue lake"~3` | 邻近匹配 N 词内 |

### 过滤器

`year`、`publication_date`（YYYY-MM-DD 范围）、`venue`、`fields_of_study`、`min_citations`、`pub_types`（Review/JournalArticle/Conference/ClinicalTrial 等）、`open_access`

### 输出函数

| 函数 | 用途 |
|------|------|
| `format_results()` | 综合：摘要表 + Top-10 详情 |
| `format_table()` | Markdown 摘要表（最多30行） |
| `format_details()` | 详细条目含 TLDR/摘要 |
| `format_citations()` | 引文信封含意图标签+上下文 |
| `format_authors()` | 作者表（姓名/机构/h-index） |
| `export_bibtex()` | BibTeX 导出 |
| `export_markdown()` | Markdown 报告保存 |
| `export_json()` | JSON 导出 |
| `deduplicate()` | 按 paperId 去重 |

### 数据集 API

批量下载 S2 全量数据集：`papers`、`abstracts`、`authors`、`citations`、`embeddings-specter_v1`、`s2orc`、`tldrs`。支持增量 diff。

### 速率限制

| 模式 | 间隔 | 上限 |
|------|------|------|
| 有 API Key | 1.1s | 1 req/s（专属配额） |
| 无 Key | 5.0s | 1000 req/s（全局共享） |

### 支持的 ID 格式

DOI、ARXIV、PMID、PMCID、CorpusId、ACL、DBLP、MAG、URL
