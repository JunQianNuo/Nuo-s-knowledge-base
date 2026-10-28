# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 仓库概述

这是一个 **Obsidian 中文知识库**，使用 Codex Agent（claudian 插件）进行知识管理。主要语言为中文，数学内容使用 LaTeX 标记。

## v2 当前执行规则（2026-10-28 用户已批准）

实际数据根为 `D:/知识库`；Codex worktree 仅用于代码开发，处理课程或知识内容时显式使用真实数据根。验收见 [[docs/KNOWLEDGE_ACCEPTANCE_V2_2026-10-28]]。

本节覆盖下文旧目录与 v1 示例。依据 [[docs/KNOWLEDGE_ARCHITECTURE]] 和已批准设计，使用 `99_System/knowledge/v2/` 的模板、Schema 和 `knowledge.py v2`。

- 原子 concept/proposition/method 单一职责、单值 type，平铺 `01_Knowledge`；必填 time、非空 topics 和真实 Sources 笔记 source，不填 title/subject。
- MOC 为 type:moc，放 `02_Maps`，topics 指上层主题，可多父、拒绝环；上层递归汇集原子并去重。主题库自动读取 MOC。
- 来源类型 lecture/review/homework/book/paper/web；idea 属性由用户手填。习题归 homework，不设知识梳理/答疑独立类型；课件和原始转写是资料。
- 课程目录在 `03_Sources/Courses`，复习在 `03_Sources/Reviews`；subject 是课程名列表。课程 PDF/PPT 跟课程走，配套图片放 `04_Assets/Images`。
- time 为创建时间；lecture_date/due_date 为上课/截止日期。status 只用 not done/done 表示原子归档；polish_status 独立管理录音笔记润色。
- 用户发出整理指令后，AI 在指定 Sources 范围自主提炼、检索复用、建立主题与关系、登记标签并应用哈希绑定事务。不增自动提炼调度。
- 无需提炼的内容必须先经人类明确审查，Agent 不得自行调用批准入口或伪造审批记录；待审则保持 not done。
- tags 可灵活，但先查 `99_System/knowledge/tags` 标准名和同义词；允许自主登记真实新标签，不从 MOC 或文件名机械补标。
- 遵守 dry-run、逐文件 diff、SHA-256、Vault 外备份和恢复要求；保留并发编辑与独立工程边界。来源不足或类型待核实进入 Inbox，不伪造数据。
- 本轮不重组 AI/语言/考研/每日疑惑/闪卡/数学建模；仅定点修复移动影响的引用。旧清理规则不触发本轮自动删除。
- 不宣称未定位的旧 Formatter 已集成；v2 新属性渲染保留正文。

## 知识体系规则与维护边界

知识模型与 v1 属性规则统一以 [[docs/KNOWLEDGE_ARCHITECTURE]] 为准，机器约束见 `99_System/knowledge/registry.yaml`；与本文件下述旧约定冲突时，新建或明确按 v1 维护的笔记采用新规，历史笔记保持兼容，不自动升级。

新建笔记的 topics 使用内部链接；现阶段 v1 Schema 只严格覆盖原子笔记和 MOC，其他内容类型不硬套三类枚举。

三类原子类型为 `concept/proposition/method`；MOC 用 `role: moc`，暂兼容历史 `type: MOC`。YAML `title` 可省略；无版本但通过兼容检查不证明历史创建规范。历史“知识点”必须语义审查，不能无条件映射。

旧目录描述、课程样例与附件约定不构成迁移授权。新 v1 模板使用 `99_System/knowledge/templates/`，不切换插件配置；旧标签工具适配验收前，不对新格式或链接 topics 笔记执行标签写入。

重要批量变更先提供 dry-run、逐文件 diff、哈希与恢复方案；现有清理规则不触发本重构的自动删除。实体统计、MOC 查询与图谱构建必须排除系统文件，且保留用户修改及独立仓库边界。阶段权限以用户最新明确授权为准，Formatter 未定位时不得声称已集成。

## 目录结构

```
规范/                          # 各类型内容规范（独立于课程）
scripts/                       # Python 脚本（OCR、闪卡生成、PPTX 处理等）
闪卡/                          # Anki/Yanki 闪卡导出（按课程分文件夹）
未命名/                        # 待整理的临时笔记
AI/                            # AI 工具索引（Skills、MCP、CLI、Prompt模板）
  AI-总览.md                   # MOC：按分类索引全部AI工具
  Skill/                       # Agent Skills（按功能分类）
    Obsidian/                  # Obsidian 原生（markdown/bases/canvas/cli/defuddle）
    图表绘制/                  # Mermaid/Excalidraw/Draw.io/PlantUML/Tldraw
    学习考试/                  # course-learning/exam-prep/exampass/flashcard/study-habits
    文档处理/                  # xparse-parse/kimi
    学术研究/                  # semanticscholar/asta/paper-fetch/nature-skills/journal-abbrev
    开发流程/                  # superpowers/code-review/verify/context7 等
    搜索与数据/                # web-search/deep-research/target-prioritization
    AI开发/                    # Codex-api/skill-creator/find-skills
    飞书办公/                  # lark（25子skill）
    多媒体/                    # video-podcast-maker
    数学建模/                  # math-modeling
    未归档/                    # playwright-cli
  CLI/                         # 命令行工具（按功能分类）
  MCP/                         # MCP 服务端（按功能分类）
  Prompt模板/                  # 沉淀的 prompt 模板

概念/                          # 共享个人概念：定义与边界，无课程子目录
知识点/                        # 共享个人知识点：条件与结论，无课程子目录
方法/                          # 共享个人方法：操作流程，无课程子目录
课程/                          # 在学课程与按原目录保存的归档
  专业写作基础/、习近平新时代中国特色社会主义思想概论/
  并行与分布式计算/、数学物理方程/、数理统计/
  概率论/（PPT课件/、习题库/、知识点解析梳理/、答疑/、复习/）
  泛函分析/、深度学习/、英语/
  归档/
    最优化方法/                 # 成熟课程结构，可供参考
      最优化方法-知识图谱.md
      最优化方法PPT课件/（PDF/、MD/）
      习题库/
      答疑/
      知识点解析梳理/
      复习/
      未处理项/
    大学物理/、实变函数/、数值分析/
    控制理论基础/、控制理论基础 1/、马克思主义原理/
```

 
## 课程规范文件（索引）

各内容类型的详细规范存于独立文件，需要时读取：

| 规范 | 文件 | 用途 |
|:--|:--|:--|
| 课程资料转 MD | [[规范/课程资料转MD规范\|课程资料转MD规范]] | PDF/PPTX/图片 → Markdown，MinerU/OCR/xparse 方案、PPTX 兜底、验证 |
| 课堂录音归档 | [[规范/课堂录音归档规范\|课堂录音归档规范]] | 腾讯会议录制自动拉取（逐字稿/纪要）→ 课表匹配 → 归档课堂笔记/raw → Agent 润色梳理 |
| 课程笔记生成 | [[规范/课程笔记生成规范\|课程笔记生成规范]] | 知识梳理、按目标复习资料与共享原子条目的职责规范 |
| 习题库 | [[规范/习题库规范\|习题库规范]] | 习题录入流程、callout、回链、OCR 注意事项 |
| 答疑 | [[规范/答疑规范\|答疑规范]] | 答疑文件结构、frontmatter、修改规则 |
| 考试复习 | [[规范/考试复习规范\|考试复习规范]] | 考试纲要、重点图谱、复习文件夹、考题生成 |
| 知识原子卡 | [[规范/知识原子卡规范\|知识原子卡规范]] | 概念卡、知识点卡、方法卡的边界、模板和链接规则 |
| Obsidian 写作 | [[规范/Obsidian写作规范\|Obsidian写作规范]] | 表格、tag、Mermaid、Wiki-link、frontmatter 通用规则 |
| 质量审查 | [[规范/质量审查规范\|质量审查规范]] | 新增/修改内容后的格式、内容、链接验证 |
| 闪卡 | [[规范/闪卡规范\|闪卡规范]] | 闪卡文件夹结构、Yanki 语法、制作流程、同步维护 |
| PDF 导出 | [[规范/PDF导出规范\|PDF导出规范]] | 课程笔记导出为 PDF 的格式与流程 |
| AI 工具 | [[规范/AI工具规范\|AI工具规范]] | AI 工具（Skill/MCP/CLI）的录入模板、分类规则、维护流程 |

> 旧规范如 `文档转MD规范`、`PPTX处理规范`、`知识点解析梳理规范` 等已保留为跳转文件，原文归档在 [[规范/已归档/2026-07-17/_manifest|2026-07-17 规范归档清单]]。

**使用规则**：仅在任务确实涉及上述内容类型时，才按需读取对应规范文件（不要预读所有规范）。**规范已有方案时直接执行，不要向用户提问“选A还是B”。**

## Obsidian 配置

- **已安装插件**：claudian（Codex Agent）、obsidian-git、terminal、excalidraw（绘图）、obsidian-excalidraw-plugin（.excalidraw 支持）、flashcard-sync（闪卡同步）、surfing（内嵌浏览器）、yanki（闪卡制作）、pdf-plus（PDF 阅读增强）、obsidian-html-plugin（HTML 嵌入）、remember-cursor-position、realclaudian
- **闪卡同步**：使用 `python scripts/sync_flashcards.py`（不依赖 Obsidian 插件），详见[[规范/闪卡规范]]
- **Mermaid 图表**：Obsidian 原生支持，用 ````mermaid` 代码块
  - **铁律**：节点标签含数学符号（`()`、`{}`、`[]`、`|`、`:`）时，统一用 `"..."` 包裹，如 `B["分布律 p_n = P(ξ=x_n)"]`
  - **禁止**：`<br/>` 换行（用空格替代）、`:` 半角冒号（换全角 `：`）、`{"..."}` 双重引号（去内引号）、`{}` 在未加引号的 `[...]` 内（会误解析为菱形语法）、`[...]` 数学方括号在标签内（会提前闭合标签，统一换 `(...)`）
  - **允许**：`→` Unicode 箭头、`\n` 换行、`"..."` 内任意字符
- **Wiki-links**：文件名唯一时可用 `[[filename]]`，否则用 `[[path/filename]]`
- **媒体文件**：图片嵌入用 `![[image.png]]`，图片存放在 vault 根目录

## Frontmatter 基础

课程笔记使用以下 YAML frontmatter（各类型详细字段见对应规范文件）：

```yaml
---
title: 第X章 章节名
subject: 最优化方法
source: 源文件名.pdf
status: OCR转换（待校对）
topics:
  - 关键词1
  - 关键词2
---
```

MOC 文件额外使用 `type: MOC`。

共享个人原子条目直接放在根目录 `概念/`、`知识点/`、`方法/`，不设课程子目录，不填写课程归属 `subject`。三类分别负责定义与边界、条件与结论、操作流程；课程只作 `source` 溯源或正文中的实际应用链接，不要求每个条目都有习题。

## 文件命名

课程笔记：`XX-中文描述.md`（如 `02-向量空间与矩阵.md`、`22a-凸优化问题.md`）

## 编码注意事项

- Windows 文件系统使用 UTF-8，但 Git Bash（MinGW）终端使用 GBK
- 处理中文文件名时优先用绝对路径 `/d/知识库/...` 或 glob 匹配
- Python 脚本处理中文路径时需 `sys.stdout.reconfigure(encoding='utf-8')` 或写文件后读取
- PowerShell 对本仓库的中文路径支持不稳定，优先使用 Bash + Python


## 未处理项清理规则

- **处理完毕即删除**：`未处理项/` 中的文件在完成处理后必须删除
- OCR 临时产物（tessdata/、.txt）一并清理
- **`未处理项/` 目录本身保留**，不删除（即使为空）

## 行为反模式（禁止）

| 反模式               | 正确做法                                      |
| ----------------- | ----------------------------------------- |
| 跳过规范直接生成内容        | 先 `Read 规范/xxx规范.md`                      |
| 脚本输出"差不多"就交付      | 逐章抽检：打开文件看前 50 行，搜索残留问题                   |
| 文本提取不到 = 没有内容     | 检查源文件中是否有图片引用（PPTX: `<a:blip>`，PDF: 嵌入图片） |
| OCR 反复调参 ≥3 次     | 停止，将图片放 vault 根目录，告诉用户需要协助                |
| 同一问题修复后不验证        | 修复一种模式后，全局搜索确认是否还有残留                      |
| 规范已有方案时问用户"选A还是B" | 按规范直接执行                                   |
| 源 MD 质量差就直接交付     | 必须走完整清理流程（Unicode → LaTeX修复 → 孤儿删除 → 验证）  |
