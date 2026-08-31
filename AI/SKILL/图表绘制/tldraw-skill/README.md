---
title: tldraw-skill
type: Skill
status: 已安装
date: 2026-06-12
---

# tldraw-skill

白板风格图表，生成 `.tldr` JSON 并通过 `@kitschpatrol/tldraw-cli` 导出 PNG/SVG。

## 完整功能

### 安装

```bash
npm install -g @kitschpatrol/tldraw-cli
```

### 工作流（7步）

1. 检查依赖（`tldraw --version`）
2. 规划（形状类型、布局方向 TB/LR）
3. 生成 `.tldr` JSON
4. 导出草稿 PNG
5. 自检（视觉检查重叠/截断/缺失连接/越界，最多 2 轮自动修复）
6. 评审循环（用户反馈 → 精确 JSON 编辑 → 重新导出，最多 5 轮）
7. 最终导出所有格式

### Geo 形状类型

| geo | 用途 |
|-----|------|
| `rectangle` | 服务、模块、组件 |
| `ellipse` | 数据库、起止节点 |
| `diamond` | 决策点 |
| `cloud` | 外部服务、基础设施 |
| `hexagon` | 事件枢纽、消息总线 |
| `triangle` | 网关、负载均衡器 |
| `star` | 亮点、关键特性 |

### 色板

| color | 用途 |
|-------|------|
| `blue` | 客户端、核心服务 |
| `green` | 成功、数据库、存储 |
| `orange` | 队列、事件总线、警告 |
| `red` | 外部 API、错误、告警 |
| `violet` | 网关、安全、认证 |
| `yellow` | 决策、缓存 |
| `grey` | 中性、背景 |
| `light-blue` | 次要服务、元数据 |
| `light-red` | 软告警 |
| `black` | 标题、强调 |

### 样式选项

`fill`: `semi`（推荐）/ `solid` / `none` / `pattern`
`dash`: `draw`（手绘默认）/ `solid` / `dashed` / `dotted`
`size`: `s` / `m` / `l` / `xl`
`font`: `draw`（白板默认）/ `sans` / `serif` / `mono`

### 箭头连接规则

- `normalizedAnchor` 指定连接点（0-1 范围）：`{x: 0.5, y: 0}` 顶部中央、`{x: 1, y: 0.5}` 右侧中央 等
- 多连接时均匀分布 anchor
- `bend: 20` 弯曲线避开重叠
- `dash: "dashed"` 异步流虚线

### 图表预设

**架构图**：Client(blue rect) → Gateway(violet triangle) → Services(blue rect) → DB(green ellipse) → Queue(orange hexagon)
**流程图**：Start/End(green ellipse) → Process(blue rect) → Decision(yellow diamond) 分支标注
**时序图**：Actor header(blue rect) → 灰色 lifeline → 实线消息/虚线异步
**ML/DL 模型图**：Input(green) → Conv/Pooling(blue) → Attention(violet) → FC(orange) → Loss(red)，skip connection 虚线弯箭
**ER 图**：Entity(light-blue 实心 rect)+多行文字标注 PK/FK
**UML 类图**：Class(light-blue 实心 rect)含标题+属性+方法

### 索引规则

z-order 序列：`a1, a2, ..., a9, aA, aB, ..., aZ`。Geo 形状先用，箭头后用。每个形状唯一索引。

### 导出

```bash
tldraw export diagram.tldr -f png --scale 2 -o ./
tldraw export diagram.tldr -f svg -o ./
tldraw export diagram.tldr -f png --scale 2 --transparent -o ./
tldraw export diagram.tldr -f png --scale 2 --dark -o ./
```

`-o` 是输出目录（非文件名），文件名自动匹配输入名。

### 降级链

tldraw-cli 缺失 → 仅生成 `.tldr` JSON → 拖入 tldraw.com 或安装 CLI
