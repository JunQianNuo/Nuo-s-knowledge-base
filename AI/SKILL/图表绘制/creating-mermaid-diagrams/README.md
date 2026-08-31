---
title: creating-mermaid-diagrams
type: Skill
status: 已安装
date: 2026-06-12
---

# creating-mermaid-diagrams

Mermaid 图表生成，文本语法 + 自动布局，导出 PNG/SVG/PDF。

## 完整功能

### 支持的图表类型

| 类型 | 关键词 | 用途 |
|------|--------|------|
| Flowchart | `flowchart TD/LR` | 流程、管道、决策 |
| Sequence | `sequenceDiagram` | API 调用、消息传递 |
| Class | `classDiagram` | OOP 模型、数据结构 |
| ER | `erDiagram` | 数据库模式 |
| State | `stateDiagram-v2` | 状态机、生命周期 |
| Gantt | `gantt` | 项目时间线 |
| Pie | `pie` | 比例图 |
| Git Graph | `gitGraph` | 分支策略 |
| C4 Context | `C4Context` | 高层架构 |
| Mind Map | `mindmap` | 主题分解 |

### 工作流

1. 检查依赖（`mmdc --version` 或降级 Kroki）
2. 选择图表类型
3. 生成 `.mmd` 文件
4. **验证（导出前必须）** — 用 `mmdc` 或 Kroki 测试渲染
5. 导出 PNG/SVG/PDF

### 导出方式

**本地 (mmdc)**：
```bash
mmdc -i diagram.mmd -o diagram.png -w 2048 --backgroundColor white
```

**Kroki API（无需安装）**：
```bash
curl -X POST https://kroki.io/mermaid/svg --data-binary @diagram.mmd -o diagram.svg
```

### 常见错误速查

| 错误 | 修复 |
|------|------|
| 序列图箭头方向错 | 请求 `->>`，响应 `-->>` |
| 标签含特殊字符 | 引号包裹 `A["Label: value"]` |
| 输出空白/太小 | 加 `-w 2048` |
| participant 顺序错 | 顶部显式声明 |

### 参考文件

Skill 目录下含 `reference/FLOWCHART.md`、`reference/SEQUENCE.md`、`reference/CLASS-ER.md`、`reference/OTHER-TYPES.md`
