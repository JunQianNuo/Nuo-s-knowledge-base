---
title: claude-api
type: Skill
status: 已安装
date: 2026-06-12
---

# claude-api

Claude API / Anthropic SDK 完整参考。

## 完整功能

### 当前模型

| 模型 | ID | 上下文 | Input $/1M | Output $/1M |
|------|-----|--------|-----------|-------------|
| Opus 4.8 | `claude-opus-4-8` | 1M | $5.00 | $25.00 |
| Opus 4.7 | `claude-opus-4-7` | 1M | $5.00 | $25.00 |
| Opus 4.6 | `claude-opus-4-6` | 1M | $5.00 | $25.00 |
| Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3.00 | $15.00 |
| Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 |

### Thinking 模式速查

- **Opus 4.8/4.7**：仅 `thinking: {type: "adaptive"}`，`budget_tokens` 返回 400
- **Opus 4.6/Sonnet 4.6**：推荐自适应，`budget_tokens` 已弃用
- **Effort**：`output_config: {effort: "low"|"medium"|"high"|"xhigh"|"max"}`（Opus 4.6+）

### 核心功能

- **Messages API**：单一端点 `POST /v1/messages`，含 tools/output_config
- **Streaming**：`client.messages.stream()` + `.get_final_message()`
- **Tool Use**：Tool Runner（推荐）/ Manual Loop，支持 MCP 转换
- **Structured Outputs**：`client.messages.parse()` 自动验证，或用 `output_config.format`
- **Prompt Caching**：前缀匹配，最多 4 断点，~90% 成本节省
- **Compaction**（Beta）：长对话自动摘要，Opus 4.6/Sonnet 4.6
- **Batches API**：50% 折扣异步处理，最多 100K 请求
- **Files API**（Beta）：上传文件引用，最大 500MB
- **Code Execution**：服务端沙箱执行代码（Python 3.11 + 数据科学库）
- **Vision**：Base64/URL 图片，Opus 4.7+ 支持 2576px 高分辨率
- **Managed Agents**（Beta）：持久化、版本化 Agent，SSE 事件流
- **Task Budgets**（Beta, Opus 4.7+）：模型感知的令牌预算计数

### 模型迁移

`/claude-api migrate` — 含 Step 0（确认范围）→ Step 1（分类文件）→ 各版本 breaking changes → 验证

### SDK 覆盖

Python / TypeScript / Java / Go / Ruby / C# / PHP，7 种语言完整 SDK 参考

### 子命令

| 命令 | 用途 |
|------|------|
| `migrate` | 迁移到新模型 |
| `managed-agents-onboard` | 从零搭建 Managed Agent |
