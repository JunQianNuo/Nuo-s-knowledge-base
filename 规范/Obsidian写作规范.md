---
title: Obsidian 写作规范
type: 规范
topics:
  - Markdown 表格
  - tag
  - Mermaid
  - Wiki-link
  - frontmatter
---

# Obsidian 写作规范

## Frontmatter

课程笔记尽量使用 YAML frontmatter 管理元数据：

```yaml
---
title: 标题
subject: 课程名
type: 知识梳理
topics:
  - 关键词
tags:
  - 概念名
---
```

内容类型用 `type` 字段，状态用 `status` 字段，不用 tag 表示。

## Wiki-link

- Vault 内部文件使用 `[[wikilink]]`。
- 文件名可能重复时使用带路径的链接，如 `[[课程/最优化方法/习题库/README]]`。
- 外部网页使用普通 Markdown 链接。

## Tag

Tag 是跨课程/跨章节的概念锚点，默认放在 frontmatter 的 `tags` 字段，不用正文内联 `#tag`。

原则：

- 用概念名，不带内容类型前缀。
- 中文为主，常用英文缩写可保留，如 `KKT条件`。
- 不用 `#知识点`、`#习题`、`#todo` 等类型/状态 tag。
- 新增 tag 前先搜索同义 tag。

## Markdown 表格

表格单元格禁止裸 `|`。在 LaTeX 中使用：

| 场景 | 表格内写法 |
|---|---|
| 绝对值 | `\vert x \vert` |
| 范数 | `\Vert x \Vert` |
| 条件概率/集合条件 | `\mid` |

验证表格：

- 表头、分隔行、数据行列数一致。
- 分隔行冒号紧贴横线，如 `|:--|`。
- 表格前后各空一行。

## Mermaid

- 节点标签含数学符号、括号、花括号、方括号、竖线、冒号时，用 `"..."` 包裹。
- 避免 `<br/>`，用短节点 + 图外解释。
- 避免在标签中使用未转义的 `|`、`{}`、`[]`。
- 可使用 Unicode 箭头 `→`，但复杂说明放图外。

## Callout

常用格式：

```markdown
> [!warning] 易错点
> 内容

> [!hint]- 点击展开提示
> 内容

> [!solution]- 点击展开详细解析
> 内容
```

折叠 callout 使用 `-`，展开 callout 使用 `+`。

## LaTeX

- 行内公式用 `$...$`。
- 块级公式用 `$$...$$`。
- 表格内避免裸 `|`，改用 `\vert`、`\Vert`、`\mid`。

## 验证清单

- Frontmatter 是否有必要字段？
- Wiki-link 是否可点击且无歧义？
- 表格是否无裸 `|` 且列数一致？
- Mermaid 是否避免 `<br/>` 和未加引号的特殊标签？
- Callout 是否每行都有 `>` 前缀？
