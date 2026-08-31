---
title: course-learning skills 拆分重组设计
type: Spec
status: 已实现
date: 2026-06-15
topics:
  - course-learning
  - skill design
  - Obsidian
  - 课程学习
---

# course-learning skills 拆分重组设计

## 1. 背景

当前 [[AI/SKILL/学习考试/course-learning/README.md]] 是一个泛化的课程学习 skill，覆盖触发场景较多，包括课件处理、知识梳理、复习、答疑、闪卡等。与此同时，vault 中已经存在多个相邻 skill：

- [[AI/SKILL/学习考试/study-habits/README.md]]
- [[AI/SKILL/学习考试/exam-prep/README.md]]
- [[AI/SKILL/学习考试/exampass/README.md]]
- [[AI/SKILL/学习考试/flashcard-creator/README.md]]

这些相邻 skill 各自负责学习习惯、备考、章节测试、闪卡制作等专项任务。当前 `course-learning` 的职责边界不够清晰，容易与相邻 skill 的职责重叠。

## 2. 目标

将 `course-learning` 从“泛化课程学习 skill”重构为“课程学习总控 / 路由层”，并新增 3 个更聚焦的子 skill：

1. `courseware-processing`：课程资料处理
2. `knowledge-structuring`：课程知识组织
3. `learning-plan`：学习节奏与计划

目标是让每个 skill 的职责边界清晰、触发规则准确、维护成本降低，并减少与现有 `exam-prep`、`exampass`、`flashcard-creator`、`study-habits` 的重叠。

## 3. 设计原则

### 3.1 单一职责

每个 skill 只负责一类清晰任务。若一个 skill 同时覆盖资料处理、知识梳理、复习计划、闪卡制作和备考，则职责过大，触发规则会失真。

### 3.2 总控与执行分离

`course-learning` 只做判断和路由，不直接执行所有课程学习任务。具体执行交给子 skill 或已有专项 skill。

### 3.3 复用现有能力

不重复实现已有专项 skill 的功能：

- 学习习惯交给 `study-habits`
- 备考策略交给 `exam-prep`
- 章节测试交给 `exampass`
- 闪卡制作交给 `flashcard-creator`

### 3.4 符合 vault 风格

Skill 文档采用当前 vault 的 README 风格：frontmatter、标题、适用场景、完整功能、模板、质量检查清单、关联规范。

## 4. 目标结构

```text
AI/SKILL/学习考试/
  course-learning/
    README.md              # 总控 / 路由层
  courseware-processing/
    README.md              # 资料处理层
  knowledge-structuring/
    README.md              # 知识组织层
  learning-plan/
    README.md              # 学习节奏层
  exam-prep/
    README.md              # 保留现状
  exampass/
    README.md              # 保留现状
  flashcard-creator/
    README.md              # 保留现状
  study-habits/
    README.md              # 保留现状
```

## 5. Skill 职责定义

### 5.1 `course-learning`：总控 / 路由层

**职责**：

- 识别用户任务属于哪类课程学习场景
- 判断是否需要资料处理、知识组织、学习计划、备考、章节测试或闪卡制作
- 路由到最合适的 skill
- 对跨阶段任务给出执行顺序

**典型触发**：

- “帮我学这一章”
- “这门课怎么学”
- “帮我整理课程学习流程”
- “这个任务应该用哪个 skill”
- “从课件到复习材料怎么走流程”

**不处理**：

- 不直接做 OCR / PDF / PPTX 清洗
- 不直接写完整知识点梳理
- 不直接制定详细学习计划
- 不直接生成闪卡
- 不直接做备考排程

### 5.2 `courseware-processing`：资料处理层

**职责**：

- 处理 PDF、PPTX、图片、网页等课程资料
- 判断是否需要 OCR、MinerU、xparse 或手工校对
- 将资料转换为可编辑 Markdown
- 输出 frontmatter 和基础清洗结果

**典型触发**：

- “处理这个 PPT”
- “把课件转 Markdown”
- “PDF 转 MD”
- “整理课件 OCR 结果”
- “清洗这份资料”

**不处理**：

- 不做知识图谱
- 不做复习计划
- 不做闪卡
- 不做考试策略

### 5.3 `knowledge-structuring`：知识组织层

**职责**：

- 对课程资料进行知识梳理
- 生成知识点清单、知识图谱、章节梳理
- 区分初学版“解析梳理”和复习版“知识点汇集”
- 标注重难点、因果链、易错点、回链关系

**典型触发**：

- “梳理这一章”
- “整理知识点”
- “做知识图谱”
- “帮我理解这一节”
- “把资料整理成复习笔记”

**不处理**：

- 不处理 OCR 和图片清洗
- 不制定每日学习计划
- 不生成闪卡
- 不做完整备考计划

### 5.4 `learning-plan`：学习节奏层

**职责**：

- 制定课程学习计划
- 安排复习节奏
- 设计主动回忆、间隔重复、阶段检测
- 跟踪学习进度和学习反馈

**典型触发**：

- “帮我安排学习计划”
- “这周怎么复习”
- “制定 7 天复习计划”
- “怎么安排主动回忆”
- “帮我追踪学习进度”

**不处理**：

- 不处理资料 OCR
- 不直接梳理知识点
- 不生成闪卡
- 不做考试策略

## 6. 路由矩阵

| 用户意图 | 路由目标 | 说明 |
|----------|----------|------|
| 不知道用什么 skill / 需要整体流程 | `course-learning` | 先判断任务类型，再拆分执行 |
| PDF / PPTX / 图片 / 网页转 Markdown | `courseware-processing` | 资料处理优先 |
| 章节理解、知识点清单、知识图谱 | `knowledge-structuring` | 知识组织优先 |
| 学习计划、复习节奏、进度安排 | `learning-plan` | 学习过程管理优先 |
| 期末考试、复习策略、押题 | `exam-prep` | 已有专项 skill |
| 章节测试、交互式练习 | `exampass` | 已有专项 skill |
| 闪卡 / Anki / 间隔重复卡片 | `flashcard-creator` | 已有专项 skill |
| 学习习惯、主动回忆习惯、时间管理 | `study-habits` | 已有专项 skill |

## 7. 文档更新范围

本次实现需要更新或新增以下文件：

1. 修改 [[AI/SKILL/学习考试/course-learning/README.md]]
   - 将内容改为总控 / 路由层说明
   - 明确触发条件、不处理范围、路由矩阵

2. 新增 [[AI/SKILL/学习考试/courseware-processing/README.md]]
   - 资料处理职责、工作流、输出模板、质量检查

3. 新增 [[AI/SKILL/学习考试/knowledge-structuring/README.md]]
   - 知识组织职责、初学/复习两种输出、质量检查

4. 新增 [[AI/SKILL/学习考试/learning-plan/README.md]]
   - 学习计划职责、节奏模板、进度跟踪、质量检查

5. 可选更新 [[AI/AI-总览.md]]
   - 若 Dataview 能自动列出新增文件，则不需要手动更新正文
   - 若需要补充描述，可在“学习考试”区域增加一行说明

## 8. 输出模板

### 8.1 `course-learning` 路由输出模板

```markdown
## 任务判断

- 任务类型：资料处理 / 知识组织 / 学习计划 / 备考 / 闪卡 / 学习习惯
- 推荐 skill：...
- 执行顺序：...

## 建议流程

1. ...
2. ...
3. ...

## 下一步

建议先执行：...
```

### 8.2 `courseware-processing` 输出模板

```markdown
## 资料处理结果

- 源文件：...
- 处理方式：MinerU / OCR / xparse / 手工校对
- 输出目录：...
- 状态：待校对 / 已清洗 / 需人工确认

## 待处理问题

- ...
```

### 8.3 `knowledge-structuring` 输出模板

```markdown
## 章节主线

...

## 核心知识点

1. ...
2. ...
3. ...

## 重难点与易错点

- 重难点：...
- 易错点：...

## 回链建议

- [[...]]
```

### 8.4 `learning-plan` 输出模板

```markdown
## 学习目标

...

## 阶段安排

| 阶段 | 时间 | 任务 | 验收标准 |
|------|------|------|----------|
| ...  | ...  | ...  | ...      |

## 复习节奏

- 首次学习后：...
- 第 2 天：...
- 第 7 天：...
```

## 9. 质量检查清单

### `course-learning`

- 是否正确识别任务类型
- 是否避免越权处理专项任务
- 是否给出清晰执行顺序
- 是否引用相邻 skill 或规范

### `courseware-processing`

- 是否明确源文件和输出位置
- 是否说明处理方式
- 是否标注待校对问题
- 是否避免把 OCR 结果当作最终知识梳理

### `knowledge-structuring`

- 是否有章节主线
- 是否区分重难点和易错点
- 是否有回链建议
- 是否避免堆砌资料原文

### `learning-plan`

- 是否有明确学习目标
- 是否有阶段安排
- 是否有验收标准
- 是否包含复习节奏或反馈机制

## 10. 验收标准

完成后应满足：

1. `course-learning` 不再承担过宽的课程学习任务，而是明确作为总控 / 路由层
2. 新增 3 个 skill 文档，职责边界清晰
3. 每个 skill 都有触发条件、工作流、输出模板、质量检查清单
4. 路由矩阵能覆盖常见课程学习场景
5. 与 `exam-prep`、`exampass`、`flashcard-creator`、`study-habits` 的职责不重复
6. README 风格与当前 vault 中其他 skill 文档一致

## 11. 风险与规避

### 风险 1：拆分后用户不知道用哪个 skill

规避：`course-learning` 作为总入口，提供清晰路由矩阵。

### 风险 2：新 skill 与现有专项 skill 重叠

规避：文档中明确“不处理”范围，并把备考、闪卡、学习习惯继续交给现有专项 skill。

### 风险 3：索引过多导致维护困难

规避：优先依赖 Dataview 自动列出文件，正文只保留分类说明，不维护冗长手工列表。

## 12. 后续实现计划

设计批准后，下一步进入实现阶段：

1. 修改 `course-learning/README.md`
2. 新增 `courseware-processing/README.md`
3. 新增 `knowledge-structuring/README.md`
4. 新增 `learning-plan/README.md`
5. 检查相邻 skill 的交叉引用
6. 验证文件路径、frontmatter、Dataview 索引和链接可点击性
