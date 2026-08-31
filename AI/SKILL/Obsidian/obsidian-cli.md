---
title: obsidian-cli
type: Skill + CLI
status: 已安装
source:
  - github: "kepano/obsidian-skills"
date: 2026-06-12
---

# obsidian-cli

与运行中的 Obsidian 实例交互的 CLI，管理笔记、搜索、属性、任务、插件/主题开发。

## 完整功能

### 笔记管理

```bash
obsidian read file="My Note"                        # 读取笔记
obsidian create name="New Note" content="# Hello"    # 创建笔记
obsidian append file="My Note" content="New line"    # 追加内容
obsidian search query="term" limit=10                # 搜索
obsidian daily:read                                  # 读今日日记
obsidian daily:append content="- [ ] task"           # 追加到今日日记
```

### 属性与元数据

```bash
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

### 文件定位

- `file=<name>` — 按 wikilink 解析
- `path=<path>` — vault 根目录精确路径
- 无 file/path 默认用当前活动文件
- `vault=<name>` 指定 vault

### 常用标志

`--copy` 复制到剪贴板、`silent` 不打开文件、`total` 返回计数

### 插件/主题开发

```bash
obsidian plugin:reload id=my-plugin     # 重载插件
obsidian dev:errors                     # 检查错误
obsidian dev:console level=error        # 控制台输出
obsidian dev:screenshot path=ss.png     # 截图
obsidian dev:dom selector=".class" text # DOM 检查
obsidian eval code="app.vault..."       # 执行 JS
obsidian dev:css selector="x" prop=bg   # 查 CSS 值
obsidian dev:mobile on                  # 移动端模拟
```
