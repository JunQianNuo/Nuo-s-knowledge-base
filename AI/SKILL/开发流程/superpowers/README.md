---
title: Superpowers Skills
type: Skill
status: 已安装
source:
  - plugin: superpowers
date: 2026-06-12
---

# Superpowers Skills

开发流程方法论 Skills，覆盖计划→实现→调试→审查→验证全流程。

## 子 Skills 一览

### brainstorming — 创意前先探索

在任何创意工作（创建功能、构建组件、添加功能、修改行为）**之前**必须使用。探索用户意图、需求和设计方案。

### writing-plans — 编写实现计划

当有 spec 或需求涉及多步骤任务时，在写代码之前先产出计划。计划供用户审核批准后执行。

### executing-plans — 在独立 session 中执行计划

按已批准的计划在独立 session 中执行实现，带 review 检查点。适合需要代码审查的多步骤任务。

### subagent-driven-development — 子 agent 驱动开发

在当前 session 中执行包含多个独立任务的实现计划。每个独立任务派发给一个子 agent 并行执行。

### dispatching-parallel-agents — 并行派发子 agent

当有 2+ 个独立任务（无共享状态、无顺序依赖）时，并行派发多个子 agent。

### test-driven-development — 测试驱动开发

先写测试再写代码：红→绿→重构循环。确保每个改动有测试覆盖。

### systematic-debugging — 系统性调试

遇到 bug/测试失败/意外行为时，先系统性分析根因再提出修复方案，不跳步猜测。

### verification-before-completion — 完成前验证

通过运行应用观察行为来确认改动真正生效。用于验证 PR、确认修复、测试改动。

### requesting-code-review — 请求代码审查

完成任务/实现大功能/合并前请求代码审查，验证工作满足需求。

### receiving-code-review — 接收代码审查

接收并处理代码审查意见，逐条回应修改或说明理由。

### finishing-a-development-branch — 完成开发分支

开发分支收尾：清理、合并、推送的标准流程。

### using-git-worktrees — Git Worktree 隔离

创建隔离的 git worktree 进行开发，避免干扰主工作区，自动清理未变更的 worktree。

### using-superpowers — Superpowers 使用入门

建立如何发现和使用 skills 的规范。任何对话开始时使用，确保按流程先检查 skill。

### writing-skills — 编写 Skills

创建新 skill、编辑现有 skill、部署前验证。含 skill 命名/描述/触发优化的最佳实践。
