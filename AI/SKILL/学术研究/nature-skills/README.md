---
title: Nature Skills
type: Skill
status: 已安装
source:
  - plugin: nature-skills
date: 2026-06-12
---

# Nature Skills

Nature 学术出版全套 Skills，覆盖文献检索、写作润色、图表制作、PPT 生成、论文精读等。

## 子 Skills 一览

### nature-academic-search — 多源文献检索

**MCP 工具矩阵**：

| 层级 | 工具 | 最佳用途 |
|------|------|----------|
| T1 核心 | `pubmed_search_articles` | 生物医学、MeSH、临床试验 |
| T1 核心 | `search_crossref` | 跨学科、引文计数 |
| T1 核心 | `search_arxiv` | 预印本（物理/数学/CS/生物） |
| T2 扩展 | `search_semantic_scholar` | 引文图谱、领域过滤 |
| T2 扩展 | `search_google_scholar` | 广泛学术搜索（抓取） |
| T2 扩展 | `search_biorxiv` / `search_medrxiv` | 生物/医学预印本 |
| T3 最后手段 | `search_webofscience` / `search_scopus` | 精选索引 |

**PubMed 工具**：`pubmed_fetch_articles`、`pubmed_find_related`、`pubmed_format_citations`（APA/MLA/BibTeX/RIS）、`pubmed_convert_ids`（DOI↔PMID↔PMCID）、`pubmed_lookup_mesh`（MeSH 词探索和层级）、`pubmed_lookup_citation`

**5 大工作流**：
1. 多源文献搜索（T1→T2→T3 后备链）
2. 引用验证（从文档提取引用 → 多源核对）
3. MeSH 搜索策略
4. 引文文件管理（.nbib/.ris/.bib 互转）
5. 参考文献管理（BibTeX、相关文章、ID 转换）

**共享模块**：去重引擎、引文解析器、搜索策略、RIS/BibTeX 格式规范、格式转换器（`scripts/format-converter.py`）

### nature-polishing — Nature 风格学术润色

**核心架构**：识别论文类型 → 读者导向写作 → 沙漏结构 → 正确写作顺序

**论文类型识别**：Research paper / Methods paper / Hypothesis-based / Algorithmic-device work

**读者心理序列**：相关性 → 新颖性 → 可信度 → 可复用性 → 意义与边界

**写作顺序（研究论文）**：Results → Introduction+Conclusion → Title → Discussion → Methods → Authors → Abstract

**各章节职责**：
- **Introduction**：为什么重要、填补什么空白、已知/未知/提问
- **Results**：观察到了什么（过去式为主、统计学适度）
- **Discussion**：怎么理解、何时失效
- **Conclusion**：三分法收尾——重申贡献+总结证据+声明边界
- **Title**：好奇+可信，不玩文字游戏

**AI 红绿灯边界**：Green（语法/清晰度/大纲/翻译）→ Yellow（方法解释需人类强控制）→ Red（禁止起草核心论点、编造引用/数据）

**引用伦理**：明确归属前人贡献、引用实际读过验证过的来源

**句子规则**：10-30 词范围、每句 ≤30 词、一句话一个核心命题、不用 em dash

### nature-reader — 论文全文精读

**核心输出**：中英对照 Markdown 全文解读 + `source_map.json` + `translation_notes.md` + `assets/`

**不妥协默认值**：段落级双语对照、保持原文结构/证据/术语/公式/引用标记

**源映射**：每个实质块有稳定锚点（S001/S002 正文、C001/C002 图注、F001/F002 图表、T001/T002 表格），含页码、块类型、原文、译文、置信度

**图表处理**：裁剪到内容区域 → 放在首次实质性提及处 → 保留原文+中文图注 → 后文提及同一图表时用链接而非重复

**翻译规则**：保守翻译，保持术语/基因名/蛋白名/公式/模型名不变，不塌缩方法细节为模糊散文，不确定处标记而非猜测

### nature-paper2ppt — 论文转 PPTX

**核心原则**：以论文学术论证为演示逻辑主线

**受众心理顺序**：问题为什么重要 → 什么空白/瓶颈 → 做了什么 → 关键证据 → 为什么可信 → 新颖/可复用 → 边界和开放问题

**精简模式**（默认）：
- 仅读取支持论点所需内容
- 仅提取实际入页的图表
- PPTX 为主要交付物
- 交叉平台 Python 优先工具链（PyMuPDF + Pillow + python-pptx）

**论文类型与演示逻辑**：
| 类型 | 逻辑 |
|------|------|
| 发现/机制论文 | question-to-evidence |
| 方法/工具/AI | problem-to-solution |
| 资源/数据集/图谱 | workflow-to-validation |
| 临床/人群 | design-to-inference |
| 综述 | evidence-map |

**默认结构**（12-16 张）：标题页 → 背景 → 知识缺口 → 核心问题 → 研究设计 → 关键证据×3 → 验证 → 机制/模型 → 创新点 → 局限 → 总结

**图表选择优先级**：设计/工作流 → 主要证据 → 验证 → 机制/模型 → 实践意义

**Nature 风格排版**：白色背景、暗色可读文字、一两个柔和强调色、图表优先、无装饰素材、无渐变

### nature-citation — Nature/CNS 引用匹配

为文稿段落自动匹配 Nature/CNS 系列引用，支持分段引用、Nature 系列/CNS 子刊过滤、EndNote/RIS/Zotero 导出

### nature-data — 数据可用性声明

Nature 格式数据声明、数据仓库选择、数据集引用、FAIR 元数据清单

### nature-figure — 论文图表

Nature 级 Python/R 科学图表（matplotlib/seaborn + ggplot2/patchwork/ComplexHeatmap），支持多面板图、SVG/PDF/TIFF 导出

### nature-response — 审稿回复

回复审稿意见的结构化框架

### nature-writing — 论文写作

Nature 风格学术写作全流程指导
