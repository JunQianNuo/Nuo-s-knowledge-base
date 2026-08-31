# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 仓库概述

这是一个 **Obsidian 中文知识库**，使用 Codex Agent（claudian 插件）进行知识管理。主要语言为中文，数学内容使用 LaTeX 标记。

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

课程/                          # 所有学习笔记
  最优化方法/                   # 最完整的课程结构，作为参考模板
    最优化方法-知识图谱.md       # MOC：课程知识图谱
    最优化方法PPT课件/
      PDF/                     
      MD/                      
    习题库/                    
    答疑/                       # 答疑记录（按章节分文件夹）
    知识点汇集/                 # 复习用（固定9板块，清单式）
    知识点解析梳理/              # 初学用（重组织、有因果、有轻重）
    复习/                       # 期末复习资料
    未处理项/                   # 待处理的图片/PDF/临时文件
  实变函数/（课件/MD/、习题库/、知识点解析梳理/、答疑/）
  数值分析/（课件/MD/、习题库/、知识点汇集/、知识点解析梳理/、复习/）
  概率论/（PPT课件/MD/及PDF/、习题库/、知识点汇集/、知识点解析梳理/、答疑/）
  马克思主义原理/（PDF/、课件/复习纲要(jpg)/、复习/、知识点解析梳理/）
```

 
## 课程规范文件（索引）

各内容类型的详细规范存于独立文件，需要时读取：

| 规范 | 文件 | 用途 |
|:--|:--|:--|
| 课程资料转 MD | [[规范/课程资料转MD规范\|课程资料转MD规范]] | PDF/PPTX/图片 → Markdown，MinerU/OCR/xparse 方案、PPTX 兜底、验证 |
| 课程笔记生成 | [[规范/课程笔记生成规范\|课程笔记生成规范]] | 知识梳理（初学）与知识点汇集（复习）的统一规范 |
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
