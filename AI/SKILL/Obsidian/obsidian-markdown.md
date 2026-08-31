---
title: obsidian-markdown
type: Skill
status: 已安装
source:
  - github: "kepano/obsidian-skills"
date: 2026-06-12
---

# obsidian-markdown

创建和编辑 Obsidian Flavored Markdown（`.md`），含 wikilinks、embeds、callouts、properties 等 Obsidian 特有语法。

## 完整功能

### 工作流

1. 添加 YAML frontmatter（title、tags、aliases）
2. 用标准 Markdown + Obsidian 扩展语法写正文
3. 用 wikilinks `[[Note]]` 链接内部笔记
4. 用 `![[embed]]` 嵌入内容
5. 用 `> [!type]` 添加 callout
6. 验证阅读视图渲染

### 内部链接 (Wikilinks)

```
[[Note Name]]                  → 链接笔记
[[Note Name|Display Text]]     → 自定义显示文字
[[Note Name#Heading]]          → 链接到标题
[[Note Name#^block-id]]        → 链接到块
[[#Heading in same note]]      → 同笔记内标题链接
```

### 嵌入

```
![[Note Name]]                 → 嵌入完整笔记
![[Note Name#Heading]]         → 嵌入章节
![[image.png|300]]             → 嵌入图片（设宽度）
![[document.pdf#page=3]]       → 嵌入 PDF 页面
```

### Callout

```
> [!note]                      基本 callout
> [!warning] Custom Title      自定义标题
> [!faq]- Collapsed            可折叠（- 折叠/+ 展开）
```

类型：`note`、`tip`、`warning`、`info`、`example`、`quote`、`bug`、`danger`、`success`、`failure`、`question`、`abstract`、`todo`

### Properties (Frontmatter)

```yaml
---
title: My Note
date: 2024-01-15
tags: [project, active]
aliases: [Alternative Name]
cssclasses: [custom-class]
---
```

### 其他语法

- **标签**：`#tag`、`#nested/tag`
- **注释**：`%%hidden%%`
- **高亮**：`==highlighted==`
- **数学**：`$e^{i\pi}+1=0$`、`$$...$$`
- **Mermaid 图表**：```` ```mermaid ````
- **脚注**：`[^1]`、`^[inline]`
