---
title: ant (Anthropic CLI)
type: CLI
status: 已安装
source:
  - github: "https://github.com/anthropics/anthropic-cli"
date: 2026-06-12
---

# ant (Anthropic CLI)

Anthropic 官方命令行工具，将 Claude API 所有资源暴露为 shell 子命令。

## 安装

```bash
brew install anthropics/tap/ant    # macOS
```

## 核心用法

```bash
# 模型列表
ant models list

# 发送消息
ant messages create --model claude-opus-4-8 --max-tokens 1024 \
  --message '{role: user, content: "Hello"}'

# Managed Agents 管理
ant beta:agents create < agent.yaml
ant beta:sessions create --agent "$AGENT_ID" --environment-id "$ENV_ID"

# Token 计数
ant messages count-tokens --model claude-opus-4-8 \
  --message '{role: user, content: "@./file.md"}' --transform input_tokens -r

# 认证
ant auth login
```

## 关键特性

- `--transform` 用 GJSON 路径提取字段
- `@path` 内联文件内容
- 列表端点自动分页
- `--format json|yaml|pretty|raw`

## 关联

- [[AI/Skill/AI开发/claude-api/README|claude-api]]
