---
title: defuddle
type: Skill
status: 已安装
source:
  - github: "kepano/obsidian-skills"
date: 2026-06-12
---

# defuddle

从网页提取纯净 Markdown 内容，去除导航/广告/杂讯以节省 token。

## 完整功能

### 安装

```bash
npm install -g defuddle
```

### 核心用法

```bash
defuddle parse <url> --md             # Markdown 输出
defuddle parse <url> --md -o out.md   # 保存到文件
```

### 元数据提取

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

### 输出格式

| Flag | 格式 |
|------|------|
| `--md` | Markdown（默认推荐） |
| `--json` | JSON（含 HTML + Markdown） |
| (无) | HTML |
| `-p <name>` | 指定元数据属性 |

### 使用规则

- 标准网页优先用 defuddle，不用 WebFetch
- `.md` 结尾的 URL 直接用 WebFetch（已经是 Markdown）
