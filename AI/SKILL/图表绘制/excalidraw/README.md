---
title: excalidraw
type: Skill
status: 已安装
date: 2026-06-12
---

# excalidraw

手绘风格图表，生成 `.excalidraw` JSON 并导出 PNG/SVG。

## 完整功能

### 导出方式

| 方式 | 输出 | 依赖 |
|------|------|------|
| Kroki API | SVG only | 仅需 curl |
| excalidraw-brute-export-cli | PNG + SVG | Node + Firefox（Playwright） |

### 元素类型

| type | 用途 |
|------|------|
| `rectangle` | 框、组件、模块 |
| `ellipse` | 起止节点、数据库 |
| `diamond` | 决策点 |
| `arrow` | 有向连接 |
| `line` | 无向连接 |
| `text` | 独立标签（可绑定到形状内） |

### 设计系统

**字体层级**：Title 28px → Header 24px → Label 20px → Description 16px → Note 14px

**语义色板**（60-30-10 规则）：

| 类别 | Fill | Stroke | 用途 |
|------|------|--------|------|
| Primary | `#dbeafe` | `#1e40af` | 入口、API |
| Success | `#dcfce7` | `#166534` | 数据存储 |
| Warning | `#fef9c3` | `#854d0e` | 决策点 |
| Error | `#fee2e2` | `#991b1b` | 错误/告警 |
| External | `#f3e8ff` | `#6b21a8` | 外部服务、AI/ML |
| Process | `#e0f2fe` | `#0369a1` | 标准流程 |
| Trigger | `#fed7aa` | `#c2410c` | 起点/触发器 |
| Neutral | `#f1f5f9` | `#475569` | 分组/容器 |

**箭头语义**：实线=主流程、虚线=异步/回调、点线=可选/弱依赖

### 布局模式

- **Flowchart**：椭圆起止→菱形决策→矩形流程，200×150px 间距
- **Architecture**：列间距 340-400px，关联服务用 Neutral 虚线容器（opacity:30）
- **Sequence**：participant 间距 200px，实线请求/虚线响应
- **Mind Map**：中心最大→逐级缩小，4-6 分支
- **Swimlane**：大透明矩形作泳道，标签 28px 独立定位

### 大图分段构建

10+ 元素的图分节写入 JSON，种子按节命名空间（100xxx, 200xxx, 300xxx）

### 反模式

- 禁用 `boundElements: []`，用 `null`
- 不在大背景矩形上绑定文本（会居中到图形中间）
- 文本元素必须显式设置 `strokeColor`（即文本颜色）
- 容器用 `opacity: 25-40`
