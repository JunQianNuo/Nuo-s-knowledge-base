---
title: context7
type: Skill
status: 已安装
source:
  - github: "upstash/context7"
date: 2026-06-12
---

# context7

实时拉取库/框架最新官方文档注入 LLM 上下文，解决训练数据过时导致的 API 幻觉。

## 核心能力

- 按库名解析 → 匹配最佳文档源 → 拉取版本特定文档和代码示例
- 支持 `ctx7` CLI 和 MCP 两种模式
- 比 WebSearch 精准（直连官方文档源，非全网搜索）

## 使用方式

```
# 提示词中加上 use context7
"用 Next.js 14 写个中间件，检查 JWT cookie。use context7"

# 指定库 ID 跳过匹配步骤
"实现 Supabase 认证。use library /supabase/supabase"
```

## 在你的 vault

主要用于开发脚本、插件时的 API 文档查询。
