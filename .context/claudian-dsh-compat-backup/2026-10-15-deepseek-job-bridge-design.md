---
title: DeepSeek 后台任务桥接补充设计
date: 2026-10-15
status: 待桥接授权
tags:
  - debugging
  - claudian
---

# DeepSeek 后台任务桥接补充设计

## 为什么触发本次审阅

用户已确认原对话修复设计与实施计划，并选择本会话顺序实施。实施计划 Task 0 要求：原生后台停止没有 Remote 出口时，新增桥接必须先审阅。

实际启动当前 dsh 后，网关报告 `job/list`、`job/kill`、`session/projections` 和 `permissionPresets/catalog` 均未注册；活跃原生 Remote 中也没有 job/job(s) 命名空间的导出。`commands/execute`、`session/control`、`session/cancel`、`session/updateQueue` 和子代理中断仍可用。

原生 jobs 服务仍有公开的 `get/list/kill` 方法；kill 会校验调用 Agent，返回 requested 或 already-finished。requested 不是任务已停止，不能凭回执发布成功。

旧权限目录不需要新增桥接：当前 permissions 投影已带 options/currentValue，原生 `/permission` 命令仍存在。实测当前原生 preset 名为 read-only、workspace-write、danger-full-access；保留原生预设，不重写配置。

## 建议桥接：复用原生已认证命令通道

只增加一个限于 Claudian 启动组合的任务控制命令，不新增 HTTP 端口，不向原生配置文件写入插件，也不恢复整套旧 RPC。现有兼容、生命周期和临时会话插件保持各自职责；桥接源码单独成模块。

命令使用每次 Host 启动唯一的名称，由 Host 传给 adapter；只接受 JSON 格式的两类请求：

```json
{"action":"list"}
```

```json
{"action":"stop","jobId":"opaque-native-job-id"}
```

- 通过现有 `commands/execute` 发送；沿用原生 loopback 认证和 Agent 参数解析，不提供新的匿名入口。
- 命令只注册到 Claudian 的 Agent 组合中，不注册为所有原生会话的全局命令，不向模型添加新工具，不加入面向用户的 slash-command 目录。
- 只在明确已被本视图拥有、已跟随且已激活的 Agent 上调用，不为查询任务激活冷子代理。
- list 只返回 ownerSession 与当前 Agent 身份完全相同的任务。不包含聊天正文、工具输出、凭据或全局任务。
- stop 先通过原生 jobs.get 取得快照，要求 ownerSession 与当前 Agent 身份完全相同，再调用 jobs.kill。即使原生服务允许调用者访问无主任务，桥接也拒绝停止无主任务。
- provider 在调用前检查当前视图的最近 claimed ancestor；原生侧再次按 Agent 和 ownerSession 检查。不跨独立 fork，不处理其他根会话任务。
- job ID 是不透明数据，仅作为 JSON 字符串传递，不拼接进 shell，不 eval，不允许方法名或服务名由请求指定。
- 回执只代表停止已请求。只有收到原生 terminal 状态并完成控制重整，界面才能报告工作已停止；失败、取消或超时必须可见。

## 控制状态如何保持单一来源

仍由 Roster 独占全局控制订阅和归一化状态。原生 control 的 jobs 行不暴露 ownerSession，且底层 jobs.list 可能包含无主任务，不能简单把每个 bucket 内所有任务都认作当前会话所有。

对已跟随 Agent，使用上述只读 list 动作核对任务身份，将结果归入 Roster 自己的控制状态；不在 Observer 再保留另一套 jobs map。相关控制更新、重新建立基线与命令读取必须有同代/请求序号隔离，旧结果不能覆盖较新结果。读取期间状态未知，不能伪装为空任务。

原生命令通道会正常追加 command/run 和 command/done 元数据；这是本次桥接明确新增的可见副作用。不会伪造用户或 assistant 消息，不直接修改会话文件，也不调用全局清理或删除接口。桥接读取不得因这些日志产生递归的任务刷新循环。

## 通过授权后纳入原实施计划

1. 增加单独的任务桥接模块及 invocation-only 启动文件；由 Host 封装命令能力，其他 provider 不可见。
2. 先写红测试，覆盖：外来根任务、无主任务、未知 ID、无效 JSON、取消、已完成任务、stopping 非 terminal，以及旧代迟到响应。
3. 对原生 jobs 公开服务做真实小任务的 list/stop 验证；不仅测试 fake command handler。确认子代理的已激活身份可用后才纳入停止循环。
4. Roster/Observer/Execution 按原计划迁移；权限目录改用原生 permissions 投影，保留实际 sandbox/approval 日志核验。
5. 原实施计划的真实问答、连续消息、工具、取消、冷读、完整测试、独立审查和最终产物验证全部保留，不因增加桥接而跳过。

## 当前工作状态

- 已完成实机注册契约探测。
- 两项新集成测试已观察到预期失败：当前任务流导致初始化失败、queue/jobs 更新导致控制订阅被关闭；其余 10 项原有测试通过。
- 本次尚未修改生产源码或运行中的插件；活动 main.js 哈希仍为原计划的预期值。
- 新增桥接属于原计划明确要求先授权的能力扩展，因此等待本补充设计确认后再实施，不以“忽略后台任务”绕过门槛。
