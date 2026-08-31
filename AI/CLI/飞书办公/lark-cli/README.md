---
title: lark-cli
type: CLI
status: 已安装
source:
  - feishu: "lark-cli"
date: 2026-06-12
---

# lark-cli

飞书命令行工具，通过 Shortcuts（`+` 命令）操作飞书各项服务。

## 核心结构

```bash
lark-cli <service> +<shortcut> [flags]
# 例：
lark-cli im +messages-send --chat-id oc_xxx --text "Hello"
lark-cli docs +fetch --api-version v2 --doc "URL"
lark-cli base +record-list --base-token xxx --table-id tblxxx
lark-cli calendar +agenda
```

## 服务列表

`im` / `docs` / `base` / `sheets` / `slides` / `calendar` / `vc` / `minutes` / `mail` / `contact` / `drive` / `wiki` / `approval` / `task` / `okr` / `attendance` / `event` / `markdown` / `whiteboard` / `apps`

## 身份

- `--as user`：用户身份（user_access_token）
- `--as bot`：应用身份（tenant_access_token）

## 关联

- [[AI/Skill/飞书办公/lark/README|lark skills]]
