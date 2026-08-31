---
title: drawio-skill
type: Skill
status: 已安装
date: 2026-06-12
---

# drawio-skill

Draw.io 图表，生成 `.drawio` XML 并本地导出 PNG/SVG/PDF/JPG。

## 完整功能

### 前提

需安装 draw.io 桌面版。macOS: `brew install --cask drawio`；Windows: 下载安装包。

### 工作流（7步）

1. **检查依赖** — `draw.io --version`
2. **规划** — 形状、关系、布局方向（LR/TB）
3. **生成** — 写 `.drawio` XML
4. **导出草稿** — 预览 PNG（不带 `-e`，避免视觉 API 400错误）
5. **自检** — 用视觉能力读 PNG，检查重叠/截断/缺失连接/越界，最多 2 轮自动修复
6. **评审循环** — 展示给用户，收集反馈，精确 XML 编辑，循环至批准（最多 5 轮）
7. **最终导出** — 所有格式，PNG 带 `-e`（嵌入 XML 保持可编辑），运行 `repair_png.py` 修复 IEND

### 形状类型

| Style | 用途 |
|-------|------|
| `rounded=0` | 普通矩形 |
| `rounded=1` | 圆角矩形（服务、模块） |
| `ellipse;` | 椭圆（起止、数据库） |
| `rhombus;` | 菱形（决策点） |
| `shape=cylinder3;` | 圆柱（数据库） |
| `swimlane;` | 泳道容器 |

### 容器规则

- **Group**（不可见）：`group;pointerEvents=0;`
- **Swimlane**（有标题栏）：`swimlane;startSize=30;`
- **自定义容器**：加 `container=1;pointerEvents=0;`
- 子元素 `parent="containerId"`，坐标相对容器

### 连线要点

- 每条边必须有 `<mxGeometry relative="1" as="geometry" />`（不能自闭标签）
- 始终含 `rounded=1;orthogonalLoop=1;jettySize=auto`
- 多连接分配不同出入点（exitX/entryX 均匀分布）
- 最后直线段 ≥20px，否则箭头与弯折重叠
- 支持 `flowAnimation=1` 动画箭头、L形弯折、曲线

### 色板

| 颜色 | fillColor | strokeColor | 用途 |
|------|-----------|-------------|------|
| Blue | `#dae8fc` | `#6c8ebf` | 服务、客户端 |
| Green | `#d5e8d4` | `#82b366` | 成功、数据库 |
| Yellow | `#fff2cc` | `#d6b656` | 队列、决策 |
| Orange | `#ffe6cc` | `#d79b00` | 网关、API |
| Red | `#f8cecc` | `#b85450` | 错误、告警 |
| Grey | `#f5f5f5` | `#666666` | 外部/中性 |
| Purple | `#e1d5e7` | `#9673a6` | 安全、认证 |

### 间距参考

| 复杂度 | 节点数 | 水平间距 | 垂直间距 |
|--------|--------|----------|----------|
| 简单 | ≤5 | 200px | 150px |
| 中等 | 6–10 | 280px | 200px |
| 复杂 | >10 | 350px | 250px |

### 样式预设

支持用户自定义样式预设（`~/.drawio-skill/styles/`），覆盖颜色/形状/边/字体

### 降级链

CLI 不可用→浏览器 fallback（`encode_drawio_url.py`）→仅交付 XML
