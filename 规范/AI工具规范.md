---
title: AI工具规范
type: 规范
---

# AI 工具规范

记录已安装的 MCP 服务、Agent Skills、CLI 工具的说明与使用实例。

## 目录结构

```
AI/
├── AI-总览.md                  ← MOC：按分类 Dataview 索引
├── Skill/                      ← Agent Skills（按功能分类）
│   ├── 文档处理/               # xparse-parse, kimi 等
│   ├── 图表绘制/               # mermaid, excalidraw, drawio 等
│   ├── 学术研究/               # semanticscholar, paper-fetch, nature-skills 等
│   ├── 学习考试/               # course-learning, exam-prep, flashcard 等
│   ├── Obsidian/               # obsidian-markdown, bases, canvas, cli, defuddle
│   ├── 飞书办公/               # lark（25 子 skill）
│   ├── 开发流程/               # superpowers, code-review, context7 等
│   ├── AI开发/                 # claude-api, skill-creator, find-skills
│   ├── 搜索与数据/             # web-search, deep-research, target-prioritization
│   ├── 多媒体/                 # video-podcast-maker
│   ├── 数学建模/               # math-modeling
│   └── 未归档/                 # 不好归类的工具
│       └── 工具名.md
├── CLI/                        ← 命令行工具（按功能分类，同 Skill 分类体系）
│   └── 分类/
│       └── 工具名.md
├── MCP/                        ← MCP 服务端（按功能分类，同 Skill 分类体系）
│   └── 分类/
│       └── 服务名.md
└── Prompt模板/                 ← 沉淀的 prompt 模板
    └── 场景-模板名.md
```

## 分类规则

1. 按工具**主要功能**归类，不强行分类
2. 不好归类的放 `未归档/`
3. 同属一个插件族的 skill（如 lark 的 25 子 skill、superpowers 的 14 子 skill）整合为一个 README，不拆分
4. Skill/CLI/MCP 三个顶层文件夹使用**相同的分类体系**

## 工具文件夹命名

- Skill：单个 skill 用原名（如 `course-learning.md`），skill 族用族名（如 `lark/README.md`）
- CLI：用命令行工具名（如 `tesseract.md`、`ant.md`）
- MCP：用服务名（如 `bio-research.md`、`asta-mcp.md`）

## README.md 模板

每个工具的 `README.md` 按以下板块编写：

```markdown
---
title: 工具名
type: MCP                     # MCP | Skill | CLI
status: 已安装                # 已安装 | 待配置 | 已废弃
source:                       # 安装来源
  - url: "https://..."
date: YYYY-MM-DD
---

# 工具名

## 简介

一句话描述这个工具是什么、能干什么。

## 安装/配置

- 安装方式
- 配置要点（关键参数、环境变量等）

## 使用说明

- 核心功能列表
- 触发条件（Skill 适用）或调用方式

## 我的实例

使用案例汇总：

| 日期 | 场景 | 实例链接 |
|------|------|----------|
| YYYY-MM-DD | 简要描述 | [[实例/实例文件]] |
```

## 实例文件规范

实例文件放在 `实例/` 子文件夹，命名：`YYYY-MM-DD-简短描述.md`

```markdown
---
title: 实例 — 简短描述
type: 实例
tool: 工具名
date: YYYY-MM-DD
---

# 实例：简短描述

## 背景

为什么要用这个工具。

## 操作过程

具体怎么用的（命令、参数、截图等）。

## 结果与总结

效果如何，有什么经验。
```

## 总览表维护

每次新增工具后，同步更新 `AI/AI-总览.md` 中的 Dataview 链接或手动添加索引。
