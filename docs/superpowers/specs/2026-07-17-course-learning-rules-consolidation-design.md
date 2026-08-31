---
title: course-learning 规范整理与内置化设计
status: approved
created: 2026-07-17
scope:
  - 规范整理
  - course-learning skill
  - Obsidian vault
---

# course-learning 规范整理与内置化设计

## 背景

当前 `course-learning` skill 位于 `C:/Users/Nuo/.agents/skills/course-learning/`，其 `SKILL.md` 仍大量引用 vault 内的 `规范/*.md`。这在当前 vault 中可用，但换环境后 skill 无法独立调用这些规范。

同时，`规范/` 中存在职责相近的文档：`文档转MD规范` 与 `PPTX处理规范` 都包含转换方案、OCR、验证检查；`知识点解析梳理规范` 与 `知识点汇集规范` 是同一类章节笔记的两个输出模式；`概念卡规范`、`知识点卡规范`、`方法卡规范` 属于同一套原子知识体系。

## 目标

1. 减少 `规范/` 中的重复文档，让 active 规范更少、更清晰。
2. 保留课程学习工作流必需的关键规则，不因合并而丢失细节。
3. 让 `course-learning` 在离开当前 vault 后仍能读取自己的本地规范。
4. 避免一次性硬删除造成 wikilink 断裂；先归档或留跳转，再视情况删除。

## 新 active 规范

| 新 active 规范 | 合并来源 | 职责 |
|---|---|---|
| `规范/课程资料转MD规范.md` | `文档转MD规范` + `PPTX处理规范` | PDF/PPTX/图片转 Markdown；MinerU/OCR/xparse 方案决策；PPTX OMML 兜底；源 MD frontmatter；转换质量验证 |
| `规范/课程笔记生成规范.md` | `知识点解析梳理规范` + `知识点汇集规范` | 从源 MD 生成初学版“知识梳理”和复习版“知识汇集” |
| `规范/知识原子卡规范.md` | `概念卡规范` + `知识点卡规范` + `方法卡规范` | 概念卡、知识点卡、方法卡的边界、模板、链接规则和质量检查 |
| `规范/Obsidian写作规范.md` | `表格规范` + `tag规范` + Mermaid/Wiki-link 通用规则 | 全局 Markdown 表格、tag、Mermaid、Wiki-link、frontmatter 写作约束 |
| `规范/质量审查规范.md` | `审查规范` + 各规范验证清单 | 新增/修改内容后的格式检查、内容检查、链接检查和验收清单 |
| `规范/考试复习规范.md` | `考试纲要规范` + course-learning 中复习资料/考题生成规则 | 考试纲要、重点图谱、复习文件夹、考题生成 |

## 保持独立的 active 规范

- `规范/习题库规范.md`：单题文件、章节 README、提示/解析 callout、未处理项清理规则完整且独立。
- `规范/答疑规范.md`：强调 `source_context`、补充修改、章节索引。
- `规范/闪卡规范.md`：Yanki/Anki 专项流程。
- `规范/PDF导出规范.md`：Markdown 到 PDF 的工具型输出流程。
- `规范/AI工具规范.md`：AI 工具索引管理，和 course-learning 无直接依赖。

## 归档策略

旧规范全文保存到 `规范/已归档/2026-07-17/`。旧路径保留短跳转文件，避免旧 wikilink 立即断裂。`单纯形表规范` 是“最优化方法”专项规则，迁移到 `课程/最优化方法/专项规范/单纯形表规范.md`，原路径保留跳转。

## course-learning skill 内置化

新增：

```text
C:/Users/Nuo/.agents/skills/course-learning/references/
├── index.md
├── courseware-to-md.md
├── course-notes.md
├── exercises-and-qa.md
├── exam-review.md
├── atomic-cards.md
└── obsidian-style-quality.md
```

`SKILL.md` 保持轻量，只做触发、意图判断、读取 `references/index.md`、再读取对应 reference 的路由。详细规则不再塞进主文件。

## 验证计划

1. 确认新 active 规范、归档目录、跳转文件、skill references 均存在。
2. 搜索旧规范名，确保不会出现悬空引用。
3. 确认合并后仍包含关键规则：OCR 不超过 3 次调参、`未处理项/` 处理完即删、Mermaid 特殊符号避坑、表格裸 `|` 禁止、答疑 `source_context` 必填。
4. 确认 `course-learning/SKILL.md` 引用 `references/*.md`，而不是只能依赖 vault `规范/`。
