---
title: obsidian-bases
type: Skill
status: 已安装
source:
  - github: "kepano/obsidian-skills"
date: 2026-06-12
---

# obsidian-bases

创建和编辑 Obsidian Bases（`.base`），含视图、筛选器、公式和汇总。

## 完整功能

### 工作流

1. 创建 `.base` 文件（合法 YAML）
2. 定义 `filters` 选择笔记范围（按标签/文件夹/property/日期）
3. 添加 `formulas` 定义计算属性
4. 配置 `views`（table/cards/list/map）
5. 验证 YAML 合法 + 引用的属性和公式存在

### 三种属性类型

| 类型 | 来源 | 示例 |
|------|------|------|
| Note properties | Frontmatter | `author`、`status` |
| File properties | 文件元数据 | `file.name`、`file.mtime`、`file.tags` |
| Formula properties | 计算值 | `formula.total` |

### 筛选器语法

```yaml
# 单一
filters: 'status == "done"'
# AND / OR / NOT（支持嵌套）
filters:
  and:
    - 'status == "active"'
    - not: ['file.hasTag("archived")']
```

运算符：`==`、`!=`、`>`、`<`、`>=`、`<=`、`&&`、`||`、`!`

### 公式语法

```yaml
formulas:
  total: "price * quantity"
  status_icon: 'if(done, "✅", "⏳")'
  days_old: '(now() - file.ctime).days'
  formatted: 'if(price, price.toFixed(2) + " dollars")'
```

**关键函数**：`date()`、`now()`、`today()`、`if()`、`duration()`、`file()`、`link()`

**Duration 注意**：日期相减返回 Duration 类型，必须访问 `.days`/`.hours` 等字段后才能用数字函数

### 视图类型

| 类型 | 用途 |
|------|------|
| `table` | 表格视图，支持 summaries（Average/Min/Max/Sum 等） |
| `cards` | 卡片画廊视图 |
| `list` | 简单列表 |
| `map` | 地图视图（需经纬度属性和 Maps 插件） |

### 默认汇总公式

`Average`、`Min`、`Max`、`Sum`、`Range`、`Median`、`Stddev`、`Earliest`、`Latest`、`Checked`、`Unchecked`、`Empty`、`Filled`、`Unique`

### YAML 引号规则

- 公式含双引号用单引号包裹：`'if(done, "Yes", "No")'`
- 含特殊字符（`:{}[],#?|`等）的字符串必须引号
