---
title: Claudian DeepSeek 对话协议适配实施计划
date: 2026-10-15
status: 待计划审阅与执行方式选择
tags:
  - debugging
  - claudian
---

# DeepSeek Chat Compatibility Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for native execution, or superpowers:subagent-driven-development if the user selects delegated execution. Execute task-by-task and retain red/green evidence.

**Goal:** 在当前安装上恢复经过真实问答、连续消息、受限工具和取消验证的 DeepSeek 对话，不把模型列表成功当作对话成功。

**Architecture:** `DeepSeekHost` 独占原生进程；`DeepSeekRoster` 独占进程级控制状态。Observer 读取 Roster 的任务、队列和投影，并通过 follow 处理消息。历史读取只使用原生冷读接口。没有公开对等能力时触发审阅门槛，不伪造成功。

**Tech Stack:** TypeScript、Node 24.16.0、Jest、esbuild、原生 dsh 0.1.5-rc.1、Windows Web profile。

**Spec:** [[2026-10-15-deepseek-chat-design]]，用户已在本对话回复“继续”确认设计范围。本文仍需审阅和执行方式选择。

## Global Constraints

- 工作源码根目录 `C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work`，下文源码相对路径均相对此目录；实际文件操作必须使用绝对路径。
- 资格验证仅针对 Claudian 2.3.20 + dsh 0.1.5-rc.1 的当前 Web 安装，不推广为所有版本或 Desktop 兼容。
- 不改密钥、模型默认值、MCP、原生配置、已有会话文件，不删除锁，不重启其他会话共享的 Host。
- 不修改其他 provider、课程笔记或聊天 UI，不升级或降级 dsh。
- 保留前两次启动补丁。活动产物预期 SHA-256 为 `69d90e7f211385bd24879623bdc0e6676fad6333ae51c69cb922824c9d0c8422`；不同则先核对，禁止覆盖外部更新。
- 源码目录来自压缩包，没有 `.git`。不初始化新仓库或提交 Vault；每项任务结束保留文件差异、测试日志和哈希，作为本次变更检查点。
- 实施前重读源码 `AGENTS.md`、`src/providers/deepseek/AGENTS.md`、`tests/AGENTS.md`；打包再读 `scripts/AGENTS.md`，检查 `.env.local` 是否会自动部署。
- 所有业务变化先观察预期失败，再实现并观察通过。完整测试仍须运行；原版已有失败按名称列入报告。
- 原生版本适配若影响临时会话契约，按 provider 指南验证不落盘矩阵；不能用普通对话通过替代隔离验证。
- 真模型测试只发送人工合成短提示，不发送 Vault 正文，不要求模型暴露凭据。测试脚本设置单次与总时限，遇到错误停止，不无限重试。
- 需要新增后台停止桥接、改变原生配置或扩大权限时停止并先审阅设计；这不是默认实施授权。
- 不热重载当前运行插件；最终 UI 验收由用户重启 Obsidian 后完成。

## File Structure

| 文件 | 职责与变更 |
|---|---|
| `src/providers/deepseek/runtime/DeepSeekRoster.ts` | 控制基线、队列和任务归一化、同代刷新及订阅清理 |
| `src/providers/deepseek/execution/DeepSeekSessionObserver.ts` | 移除旧 job/list 订阅；保持 follow、归属和工作状态判断 |
| `src/providers/deepseek/execution/DeepSeekExecutionSession.ts` | 对接任务刷新与已验证的取消契约，不替换整个执行器 |
| `src/providers/deepseek/history/DeepSeekJournal.ts` | 替换旧 projection RPC，保留固定切点分页 |
| `src/providers/deepseek/runtime/DeepSeekHost.ts` | 保持冷读白名单准确，禁止意外激活 |
| `tests/helpers/deepseek/NativeDefaults.ts` | 改成当前原生形状，不在 fixture 中代替业务归一化 |
| `tests/helpers/deepseek/NativePeer.ts` | 仅在退役旧 jobsOf helper 无剩余消费者时移除，不增加生产测试门面 |
| `tests/integration/providers/deepseek/runtime/DeepSeekRoster.test.ts` | 控制代、乱序、未知状态及格式验证 |
| `tests/integration/providers/deepseek/execution/DeepSeekSessionObserver.test.ts` | 当前协议下的任务/子代理/完成判断 |
| `tests/integration/providers/deepseek/execution/DeepSeekExecutionBackend.test.ts` | 完整执行、权限边界、连续消息及取消 |
| `tests/integration/providers/deepseek/execution/DeepSeekSharedHost.test.ts` | 多视图、断连和共享 Host 隔离 |
| `tests/integration/providers/deepseek/history/DeepSeekConversationHistoryService.test.ts` | 冷读、分页及缺失投影行为 |
| `tests/integration/providers/deepseek/execution/DeepSeekPermissions.test.ts` | 权限目录、命令回执与原生日志语义一致 |
| `.context/InspectNativeChatContract.ts` | 一次性、脱敏的安装契约探测，不随产品发布 |
| `.context/RealDeepSeekChatRegression.ts` | 通过真实执行会话运行问答与取消，不直连模型 API |
| `.context/DeepSeekCandidateArtifactCheck.cjs` | 最终产物对应类的回归及补丁边界检查 |

## Review Focus

1. 新格式 job 行没有 `owner`：归属必须来自 control 的 session bucket，不能过滤掉所有真实任务。任务 1、2 覆盖。
2. turn/end 与 jobs/queue 更新跨流乱序：不能短暂发布假空闲。任务 2、4 覆盖。
3. 冷会话缺少缓存 projection：不能当成会话已删除，也不能为了读取而激活它。任务 3 覆盖。
4. 多视图与外来任务：Stop 只影响当前拥有的任务，不能结束共享进程或其他视图。任务 4 覆盖。
5. 旧代迟到帧或断连后重放：旧状态不能覆盖新基线，已显示消息不能重复追加。任务 1、2、5 覆盖。

---

## Task 0：锁定当前原生契约与停止能力

**Files:** Create `.context/InspectNativeChatContract.ts` and `.context/native-chat-contract.json`；读取原生安装包，不改生产文件。

**Interfaces:** 输入为当前 Host 启动覆盖层和原生 `typertGateway.claimsEndpoint(endpoint)`；输出为 endpoint 是否注册、参数形状及来源文件位置的 JSON，不包含认证 token 或聊天正文。

- [ ] 基于已有 `.context/native-routes.ts` 的临时覆盖层探测以下候选能力，不发送业务命令：

```ts
const endpoints = [
  'session/list', 'session/control', 'session/create', 'session/follow',
  'session/page', 'session/projections', 'session/prompt', 'session/cancel',
  'session/updateQueue', 'job/list', 'job/kill', 'commands/list',
  'commands/execute', 'permissionPresets/catalog', 'skills/list',
  'subagents/interruptByParent',
];
const claims = endpoints.map(endpoint => ({
  endpoint, registered: ctx.typertGateway.claimsEndpoint(endpoint),
}));
```

这段代码置于诊断插件的 `ctx.inject(['typertGateway'], ctx => ...)` 内，仅写脱敏 JSON。原生入口、profile、cwd 与已有诊断保持一致，临时进程必须在 finally 中关闭并删除其覆盖层。

- [ ] 用当前已安装包的 generated Remote metadata 与实现交叉核对每个必要方法的参数，不从 TypeScript 方法是否存在推断它已公开。
- [ ] 核对已发现的当前形状：control jobs 行只有 `id/status/...`，没有 owner；session/list 的 projection 列可缺失，且可能为缓存。
- [ ] 重新运行已保存的 `.context/job-endpoint-diagnostic.ts`，记录完整错误仍可复现，且没有模型请求或用户会话访问。
- [ ] **停止门槛：** 若后台停止或权限选择没有公开对等能力，不编造替代路径，不进入部署。记录缺口，单独给出最小公开服务桥接设计供用户审阅；之后才可更新本计划对应任务。允许继续准备其他任务的红测试，但不把部分通过当作可发布。
- [ ] 保存契约 JSON、来源位置和探测退出码作为检查点。

诊断编译沿用工作目录现有 esbuild；从绝对工作目录执行：

```powershell
& $node "$work/node_modules/esbuild/bin/esbuild" "$work/.context/InspectNativeChatContract.ts" --bundle --platform=node --packages=external "--outfile=$work/.context/InspectNativeChatContract.cjs"
& $node "$work/.context/InspectNativeChatContract.cjs"
```

后续命令统一变量：

```powershell
$work = 'C:/Users/Nuo/AppData/Local/Temp/claudian-dsh-compat-work'
$node = 'C:/Users/Nuo/AppData/Local/Temp/claudian-node24/node-v24.16.0-win-x64/node.exe'
```

## Task 1：Roster 成为完整控制状态所有者

**Files:** Modify `DeepSeekRoster.ts`；extend `DeepSeekRoster.test.ts`。

**Interfaces produced:** 在 Roster 模块定义以下 provider 内部类型与只读 API；Observer 原有导出类型继续转导出，避免消费者循环依赖。

```ts
export interface DeepSeekJob {
  readonly id: string;
  readonly owner: string;
  readonly status: string;
}
export interface DeepSeekQueueItem {
  readonly id: string;
  readonly content: readonly unknown[];
  readonly source?: { readonly kind?: string; readonly rpcId?: string };
}
export interface DeepSeekControlState {
  readonly jobs?: readonly DeepSeekJob[];
  readonly queue?: readonly DeepSeekQueueItem[];
}
// Members of DeepSeekRoster:
// control(id: string): DeepSeekControlState | undefined
// refreshControl(signal?: AbortSignal): Promise<void>
```

- [ ] 在现有 NativePeer 测试中增加当前格式的基线与更新，并先运行观察失败。该错误必须是控制状态不被识别或任务丢失，不是 fixture 崩溃。

```ts
peer.send('session/control', {
  type: 'jobs', sessionId: 'root',
  jobs: [{ id: 'job-1', status: 'running' }],
});
peer.send('session/control', {
  type: 'queue', sessionId: 'root',
  items: [{ id: 'queued-1', content: [{ type: 'text', text: 'next' }] }],
});
// After the actual peer delivery has settled:
expect(roster.control('root')?.jobs).toEqual([
  { id: 'job-1', owner: 'root', status: 'running' },
]);
expect(roster.control('root')?.queue?.map(item => item.id)).toEqual(['queued-1']);
```

- [ ] 用单个 Roster 所有的控制状态集合安装完整基线；以 frame.sessionId 或基线 bucket key 归一化 job.owner。若收到显式冲突 owner，不采纳为当前 owner 的任务。未提供字段保留 undefined，不生成空数组。
- [ ] `refreshControl` 由同一个所有者重新开控制订阅：旧订阅先失效；基线未完成前 ready 为 false；收到同代有效完整基线才 resolve。取消、断连、格式错误必须 reject 并保留未知状态。
- [ ] 测试延迟基线、旧订阅迟到帧、缺失 jobs/queues、坏字段、重连及 dispose 后回调，保留之前 agentAvailable 和冷子代理的测试。
- [ ] 运行 Roster focused tests 至绿色，保存红绿日志及源码差异。

## Task 2：Observer 使用统一控制状态

**Files:** Modify `DeepSeekSessionObserver.ts`；extend `DeepSeekSessionObserver.test.ts`；migrate `NativeDefaults.ts`。

**Consumes:** Task 1 的 `control`、`refreshControl`、类型与现有 `onChange`；follow 与 claim 仍使用现有接口。

**Produces:** 现有 `isReady/hasWork/ownedJobs/queuedItems` 对调用者保持语义；新增 `rebaselineControl(signal?: AbortSignal): Promise<void>`，仅转交 Roster 刷新，用于执行边界显式等待。

- [ ] 把 Observer 的当前协议测试改成 NativePeer 拒绝旧 `job/list`。使用真实 Roster + Observer，control 基线带 jobs 和 queues，follow 返回 snapshot；先观察旧 Observer 无法 ready。
- [ ] 删除 Observer 的 offJobs 和重复 jobs 状态，改为读取 `roster.control(id)`；任务归属只由 Roster 给出；queuedItems 不再从旧 inbox projection 拼接。
- [ ] turn/end 后安排并等待同所有者的控制基线刷新，再允许发布空闲。一次性刷新请求期间一律 busy；已有回调必须 identity-fence，失败进入已有 onError 路径。
- [ ] 在原有 NativeDefaults 的 open 中直接发送原生形状，不做业务过滤或合成 owner：

```ts
send({
  type: 'baseline',
  value: {
    queues: Object.fromEntries(options.roster().map(id => [id, []])),
    jobs: Object.fromEntries(options.roster().map(id => [id, options.jobs?.(id) ?? []])),
    projections: Object.fromEntries(options.roster().map(id => [id, {
      asOfSeq: options.seq(), values: options.projections?.(id) ?? {},
    }])),
  },
});
```

- [ ] 更新被迁移行为的 fixtures，删除旧 job stream 推送，不把新生产逻辑写进 helper。现有 assertions 先列出并保留各自的覆盖归属。
- [ ] 测试 root idle 但 child job running、cold child 不 follow、未知控制状态忙、foreign owner 不归入当前 root、turn/end 先到而 job 仍运行、刷新失败、重连后旧跟随回调。
- [ ] 运行 Observer + Roster + SharedHost focused tests。每项既断言 busy/ready 等结果，也保留异常对调用者可见的验证。

## Task 3：移除历史与权限的旧 projection 依赖

**Files:** Modify `DeepSeekJournal.ts`、必要时 `DeepSeekHost.ts` 冷读白名单；extend `DeepSeekConversationHistoryService.test.ts`、`DeepSeekPermissions.test.ts`、`NativeDefaults.ts`。

**Interfaces:** `readDeepSeekProjection(client, sessionId): Promise<DeepSeekProjection>` 与 journal generator 的外部签名不变；不得增加 follow 激活作为冷读 fallback。

- [ ] 现有 history/permission 集成测试改用 session/list 行内 projection，旧 session/projections 返回 endpoint 不存在；先观察正确的红结果。
- [ ] 实现根据 session/list 的匹配行读取 projection，完整验证 asOfSeq 与 values。没有该行时才返回 session/missing；行存在但 projection 缺失则明确报不可用，不能伪装为空历史或会话丢失。

```ts
const listed = await client.call('session/list', { _request: {} });
if (!isRecord(listed) || !Array.isArray(listed.items)) {
  throw new Error('Malformed DeepSeek session roster.');
}
const row = listed.items.find(item => isRecord(item) && item.sessionId === sessionId);
if (!row) throw new DeepSeekRemoteError('DeepSeek native session is missing.', 'session/missing');
if (!isRecord(row) || !isRecord(row.projections)
  || !isCheckpoint(row.projections.asOfSeq) || !isRecord(row.projections.values)) {
  throw new Error('DeepSeek native projections are unavailable or malformed.');
}
return { asOfSeq: row.projections.asOfSeq, values: row.projections.values };
```

- [ ] 固定切点读取继续走 session/page；投影缓存不能证明足够新时不宣称完整恢复。测试检查 pending fork checkpoint 大于已有 cut 的拒绝、分页无进展及来自另一原生 store 的拒绝仍保留。
- [ ] NativeDefaults 的 session/list 返回 projection，退役 session/projections fixture 分支；维护权限日志与权限选择回执的现有独立断言。
- [ ] `session/projections` 从冷读白名单移除；新增方法只在 Task 0 明确证明冷读不激活后才可加入。测试确保 cold hydrate 不开 follow、不创建 session、不请求命令目录。
- [ ] 验证当前 permission catalog/command 真实能力。若 Task 0 发现不兼容，依照审阅门槛处理，不擅自放宽安全语义。
- [ ] 运行 history、permissions、Host 和 execution focused tests；保存红绿日志及差异。

## Task 4：执行、取消与多视图不相互干扰

**Files:** Modify `DeepSeekExecutionSession.ts`；extend `DeepSeekExecutionBackend.test.ts`、`DeepSeekSharedHost.test.ts`。

**Consumes:** Task 2 的 rebaselineControl；Task 0 通过审阅的停止契约；原有 requested/steer 和 ProviderExecutionEvent 类型不变。

- [ ] 扩展现有 execution 测试，用当前控制帧驱动真实 backend；验证请求关联、第二条消息和非当前请求的 wake turn 不被错误归因。预期最终事件仍是 turn_completed，不产生执行错误。
- [ ] 在完成与 Stop 的确认点调用已定义的 `observer.rebaselineControl(signal)`，而不是以 HTTP ack 或 turn/end 推断所有工作已停止。
- [ ] 使用已核对的原生停止出口替换遗留 job/kill；若公开能力不足，执行 Task 0 的桥接审阅门槛。没有已审阅出口时不部署此任务。
- [ ] 保留未领取 steer 的撤回、claim race、取消后 inbox 不自动丢弃、独立 child ownership 的既有逻辑；以 peer 的真实更新证明完成，不在 mock 内直接设置 observer 状态。
- [ ] 基于两条 claimed roots 的 SharedHost 测试增加：当前 root 停止后另一 root 的 follow 与 running job 仍存在，lifecycle.disposed 不增加。另测超时、取消请求失败、job 已结束的幂等性及旧代回执。
- [ ] 检查 rebaseline 失败时既有错误事件明确且可恢复，没有假 turn_completed，没有关闭其他 lease。
- [ ] 运行 DeepSeek 全部 focused suites，记录与原有失败基线的差异。保存源码快照，不改运行中的 main.js。

## Task 5：实机验证、独立审查与最终产物

**Files:** Create `.context/RealDeepSeekChatRegression.ts`、`.context/DeepSeekCandidateArtifactCheck.cjs`；产出脱敏验证日志和 JSON 报告。

**Consumes:** 当前 DeepSeekExecutionBackend、DeepSeekHostProcess、ProviderExecutionSession 公共执行接口，以及已完成的前四项任务。

- [ ] 基于已有 ExecutionBackend integration harness 的 ProviderHost/interactionPort 最小环境创建实机 harness，实例化真实 HostProcess 和 backend；不 mock Roster、Observer、RemoteClient 或执行状态机。测试工作目录由 fs.mkdtemp 创建，命令必须 windowsHide。
- [ ] 用真实临时 execution session 发送 `Reply with CHAT_COMPAT_OK only.`，收集整个 run.events，断言含非空 assistant 内容、请求对应完成事件、没有 execution_error；同会话再发 `Reply with SECOND_TURN_OK only.`。测试在收到所有完成状态后才结束，不只看标准输出出现文本。
- [ ] 在临时工作目录建立无敏感内容的小文本文件，使用 read-only permission 请求读取；确认有真实 tool/result 且内容与文件一致，不请求其他 Vault 文件。
- [ ] 用有界的长回答测试进行中取消，验证取消事件与状态恢复；后台任务停止通过原生实际任务生命周期验证，不能仅 mock kill 回执。停止失败或超时即不合格。
- [ ] 对专门创建的测试持久会话测试 page、冷读和重开继续。已有用户会话不纳入内容探测。临时根及其 forks 另外做 provider 指南要求的不落盘检查；测试产生的持久记录在报告中列明，不擅自删除原生记录或锁。
- [ ] 每次模型调用设置 timeout，任何异常停止本轮；只使用少量人工短提示。模型实际回复、密钥与 token 不写入公开诊断，只记录断言结果、事件类型和计数。
- [ ] 运行完整工程验证，在绝对工作目录中执行：

```powershell
npm.cmd run typecheck
npm.cmd run lint
npm.cmd run test
npm.cmd run build
npm.cmd run check:performance
```

每步单独记录退出码，测试失败不跳过剩余只读检查；build 前确认 `.env.local` 不会自动覆盖 Vault。与 `official-baseline-tests.log` 按失败测试全名比较，所有新增失败阻止发布。报告明确完整测试不是全绿时的每个失败名称。

- [ ] 依据 requesting-code-review 技能发起一次独立审查，提供明确设计、改动差异、实机结果，不把对话历史当作评审材料。Critical/Important 未解决不部署。
- [ ] 构建并解析最终候选产物。优先保留当前产物的所有无关字节，只替换本次实际变化的类/方法及必需依赖；对每个自由标识符核对所属依赖。无法证明映射和字节边界时不发布手工拼接产物，改为单独说明完整重建产物的差异供审阅。
- [ ] 使用候选产物中的实际类重跑实机 execution harness，而不是只验证源码；记录模型问答、工具、取消、历史的逐项结果与候选 SHA-256。
- [ ] 备份当前 main.js 并快照配置哈希，写入候选后重读校验哈希、解析语法、核对配置未改；只改 `.obsidian/plugins/realclaudian/main.js`。保留先前备份，不覆盖。
- [ ] 报告已验证/未验证/不支持项、完整测试失败清单、模型请求次数、备份位置与回退方法。请用户完全重启 Obsidian 后用新会话完成 UI 验收；用户确认前 UI 状态标记为待确认。

## Self-Review

- 已逐项覆盖设计中的控制所有权、消息与完成语义、历史冷读、取消、安全约束、真实测试、最终产物和用户 UI 验收。
- 后台停止和权限公开能力尚需探测，被明确建模为 Task 0 的发布阻断与单独审阅点，没有用未定义的替代 RPC 填补。
- Task 1 定义了 Task 2、4 引用的新类型及方法；生产状态仍只有 Roster 一处所有者。
- Review Focus 五类风险均已归入相应任务的红绿测试或实机验收。
- 原生历史缓存缺失、临时隔离矩阵、全量测试非全绿及源码目录无 git 的限制均已明确，不会被“问答成功”掩盖。

## Execution Handoff

推荐 **Native：本会话顺序实施，最后一次独立审查**。这些任务共享控制状态接口和生命周期边界，顺序实施比拆给多个实现代理更容易维持一致性。

也可选择 **Subagent-driven：每项独立实现与逐项审查**，但上下文和审查成本更高。无论选择哪种方式，都需先确认本文，且 Task 0 的安全门槛不因执行方式改变而取消。
