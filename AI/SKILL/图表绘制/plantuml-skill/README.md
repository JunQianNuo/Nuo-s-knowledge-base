---
title: plantuml-skill
type: Skill
status: 已安装
date: 2026-06-12
---

# plantuml-skill

PlantUML 图表，生成 `.puml` 并通过 Kroki API 导出 PNG/SVG（无需本地 Java）。

## 完整功能

### 导出

```bash
# PNG
curl -X POST https://kroki.io/plantuml/png --data-binary @diagram.puml -o diagram.png
# SVG
curl -X POST https://kroki.io/plantuml/svg --data-binary @diagram.puml -o diagram.svg
# 本地 Docker
curl -X POST http://localhost:8000/plantuml/png --data-binary @diagram.puml -o diagram.png
```

### 图表类型

| 类型 | 语法 | 用途 |
|------|------|------|
| Sequence | `A -> B : msg` | API 调用、协议流 |
| Component | `component "Name"` | 服务架构、模块依赖 |
| Class | `class Name { }` | OOP 模型 |
| ER | `entity "Name" { }` | 数据库模式 |
| Activity | `start → if → stop` | 工作流、业务流程 |
| Use Case | `actor → usecase` | 系统需求 |
| State | `[*] --> State` | 状态机 |
| C4 | `!include C4_Context` | 系统上下文 |
| Mind Map | `@startmindmap` | 主题分解 |
| Gantt | `@startgantt` | 时间线 |

### 形状速查

| 形状 | 语法 |
|------|------|
| Actor | `actor "Name" as id` |
| Component | `component "Name" as id` |
| Rectangle | `rectangle "Name" as id` |
| Database | `database "Name" as id` |
| Queue | `queue "Name" as id` |
| Cloud | `cloud "Name" as id` |
| Node | `node "Name" as id` |
| Frame | `frame "Name" { }` |
| Package | `package "Name" { }` |

### 箭头语法

| 语法 | 含义 |
|------|------|
| `A --> B` | 实线箭头 |
| `A -> B` | 细箭头 |
| `A ..> B` | 虚线箭头 |
| `A --> B : label` | 带标签 |
| `A <--> B` | 双向 |
| `A ->> B` | 异步消息（时序图） |
| `A -[#red]-> B` | 彩色箭头 |

### 关系（类图）

`--|>` 继承、`..|>` 实现接口、`*--` 组合、`o--` 聚合、`"1" --> "*" : label` 多重性

### 主题

`!theme plain`（推荐）、`cerulean`、`blueprint`、`aws-orange`、`vibrant`；或用 `skinparam` 完全自定义
