---
title: json-canvas
type: Skill
status: 已安装
source:
  - github: "kepano/obsidian-skills"
date: 2026-06-12
---

# json-canvas

创建和编辑 JSON Canvas 文件（`.canvas`），含节点、边、分组和连接。

## 完整功能

### 文件结构

```json
{
  "nodes": [],
  "edges": []
}
```

遵循 [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)

### 节点类型

| 类型 | 专属字段 | 用途 |
|------|---------|------|
| `text` | `text` | Markdown 文本节点 |
| `file` | `file`, `subpath` | 链接到 vault 内文件 |
| `link` | `url` | 外部 URL |
| `group` | `label`, `background`, `backgroundStyle` | 可视化分组容器 |

### 通用节点属性

`id`（16 字符 hex）、`type`、`x`、`y`、`width`、`height`、`color`（预设 `"1"`-`"6"` 或 hex `"#FF0000"`）

### z-order

数组顺序决定层级：第一个节点最底层，最后一个最顶层

### 边（Edges）

| 属性 | 说明 |
|------|------|
| `fromNode`/`toNode` | 源/目标节点 ID |
| `fromSide`/`toSide` | `top`/`right`/`bottom`/`left` |
| `fromEnd`/`toEnd` | `none` 或 `arrow`（默认 `toEnd: "arrow"`） |
| `label` | 边上的描述文字 |
| `color` | 线条颜色 |

### 色板预设

| 预设 | 颜色 |
|------|------|
| `"1"` | Red |
| `"2"` | Orange |
| `"3"` | Yellow |
| `"4"` | Green |
| `"5"` | Cyan |
| `"6"` | Purple |

### 布局指南

- 节点间距 50-100px，组内 padding 20-50px
- 对齐到 10 或 20 的倍数额网格
- 建议宽度：小文本 200-300、中文本 300-450、大文本 400-600

### 验证清单

1. 所有 ID 唯一（节点+边）
2. 边引用的 `fromNode`/`toNode` 存在
3. 必填字段完整
4. type/side/end 值合法
5. JSON 可解析
