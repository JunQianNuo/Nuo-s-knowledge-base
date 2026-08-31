---
title: course-learning
type: Skill
status: 已更新
date: 2026-06-15
topics:
  - 课程学习
  - skill 路由
  - 学习流程
  - 知识组织
---

# course-learning

课程学习总控 / 路由层。用于判断课程学习任务的类型，并把任务路由到最合适的专项 skill。

## 完整功能

### 1. 任务识别

当用户提出泛化的课程学习需求时，先判断任务属于哪一类：

| 任务类型 | 典型表述 | 推荐路由 |
|----------|----------|----------|
| 资料处理 | “处理这个 PPT”“PDF 转 MD”“清洗课件 OCR” | [[AI/SKILL/学习考试/courseware-processing]] |
| 知识组织 | “梳理这一章”“整理知识点”“做知识图谱” | [[AI/SKILL/学习考试/knowledge-structuring]] |
| 学习计划 | “安排学习计划”“这周怎么复习”“制定 7 天复习计划” | [[AI/SKILL/学习考试/learning-plan]] |
| 备考策略 | “期末考试怎么复习”“怎么押题”“冲刺计划” | [[AI/SKILL/学习考试/exam-prep]] |
| 章节测试 | “出章节测试”“交互式练习” | [[AI/SKILL/学习考试/exampass]] |
| 闪卡制作 | “做 Anki”“生成闪卡”“间隔重复卡片” | [[AI/SKILL/学习考试/flashcard-creator]] |
| 学习习惯 | “怎么坚持学习”“主动回忆习惯”“时间管理” | [[AI/SKILL/学习考试/study-habits]] |

### 2. 跨阶段流程拆解

对于跨阶段任务，先拆成顺序流程，再逐段交给专项 skill。

**示例：从课件到期末复习**

```text
课件资料处理 → 知识组织 → 学习计划 → 章节测试 / 闪卡 → 备考策略
```

对应 skill：

1. `courseware-processing`：处理 PDF / PPTX / 图片 / 网页资料
2. `knowledge-structuring`：整理章节主线、知识点、重难点
3. `learning-plan`：安排学习节奏和复习节点
4. `exampass` / `flashcard-creator`：生成练习或闪卡
5. `exam-prep`：制定考前策略和冲刺安排

### 3. 路由输出模板

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

### 4. 质量检查清单

- 是否正确识别任务类型
- 是否避免越权处理专项任务
- 是否给出清晰执行顺序
- 是否引用相邻 skill 或 vault 规范
- 是否把资料处理、知识组织、学习计划、备考、闪卡、学习习惯区分清楚

## 不处理范围

`course-learning` 只做总控 / 路由，不直接执行以下专项任务：

- 不直接做 OCR / PDF / PPTX / 图片清洗
- 不直接写完整知识点梳理或知识图谱
- 不直接制定详细学习计划
- 不直接生成闪卡
- 不直接做备考排程或押题
- 不直接处理学习习惯训练

## 关联

- [[AI/SKILL/学习考试/courseware-processing]]
- [[AI/SKILL/学习考试/knowledge-structuring]]
- [[AI/SKILL/学习考试/learning-plan]]
- [[AI/SKILL/学习考试/exam-prep]]
- [[AI/SKILL/学习考试/exampass]]
- [[AI/SKILL/学习考试/flashcard-creator]]
- [[AI/SKILL/学习考试/study-habits]]
