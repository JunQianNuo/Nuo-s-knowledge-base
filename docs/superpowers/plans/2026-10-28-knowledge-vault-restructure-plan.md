# Knowledge Vault V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** 落实已批准的 v2 属性、来源/原子/MOC 架构，并将本轮资料安全迁入新位置。

**Architecture:** 保留可识别的 v1 工具，新增 `99_System/knowledge/v2/` 实现明确的 v2 协议；复用严格 YAML 解析及 Windows 独占文件保护。模型/视图、课程采集适配、提炼协议可按明确文件所有权并行实现，迁移事务与真实数据执行由主 agent 负责。

**Tech Stack:** Python 3.13、PyYAML、jsonschema、本机 Obsidian Bases、Windows 独占文件句柄、unittest。

**Spec:** `docs/superpowers/specs/2026-10-28-knowledge-vault-restructure-design.md`

## Global Constraints

- 一篇原子笔记只承担一种核心职责；三类共用属性，单值 type。
- time 是创建时间；省略 title；原子 topics/source 非空且指向实际合规对象。
- 原子 source 至少链接一份 Sources 来源笔记；不猜测取材关系。
- 来源 status 只用 not done/done；polish_status 独立；无需提炼须人工审查。
- MOC 使用 type: moc，多上层、递归聚合、去重、拒绝环；系统记录排除。
- 其他内容不重组；仅受影响的确定性路径引用可定点修复；独立工程/联接不遍历。
- 重要批量变更先生成 dry-run、逐文件 diff、SHA-256、备份和恢复入口。
- 保留当前工作区字节、用户扩展字段和正文；不自动删除未处理项。
- 原始课件和转换 MD 不自动变成 lecture；不虚构来源或书目信息。

## Review Focus

1. Windows 大小写/重名、目标碰撞、联接、硬链接与独立仓库：写入前拒绝。
2. 事务中断和源/目标并发编辑：保留用户字节，日志可恢复，不覆盖新编辑。
3. 旧 status/title/date/source 的语义不等价：保留证据，不能机械当作 v2 完成。
4. 多父 MOC 的菱形路径和环：去重、拒绝循环、不能混入课件或系统笔记。
5. 部分提炼与待人工批准的跳过：保持 not done，不能伪报完整归档。

## Task 1: V2 属性、模板、主题索引与视图

**Files:** Create `99_System/knowledge/v2/{__init__,model,views}.py`、`v2/schemas/`、`v2/templates/`；tests `test_v2_model.py`、`test_v2_views.py`。

**Interfaces:**
- `model.read_note(raw: bytes) -> tuple[dict, bytes]`：复用 v1 严格 YAML，返回原字节正文。
- `model.render_note(data: dict, body: bytes) -> bytes`：UTF-8 属性和原字节正文。
- `model.validate(data: dict) -> list[dict]`：code/field/message 诊断，显式 v2 类型及字段。
- `model.scan(root: Path) -> dict[str, dict]`：只扫描新内容区；值至少含 data，排除系统、资源、独立工程。
- `model.audit(root: Path) -> dict`：包含 errors、counts、diagnostics，关系目标解析与角色核查。
- `views.build(root: Path) -> dict[str, bytes]`：生成数据库、课程资料视图、递归 MOC 嵌入结果/辅助索引；不直接落盘。
- `views.descendants(notes: dict, moc: str) -> set[str]`：与 scan 相同的逻辑路径，拒绝环。

- [x] 先写并运行失败测试：11 种类型、空来源/主题、非法时间、subject 列表、idea 手工模式、系统隔离、未知扩展保留。
- [x] 实现模型与本地 Schema；模板占位检查与真实笔记必填检查分开；发布模板正文职责。
- [x] 先写并运行失败测试：多父菱形、循环、非 MOC topics、来源非原子笔记角色和资源排除。
- [x] 实现递归与可用 Bases/辅助视图；不能只生成顶层过滤冒充递归。
- [x] `python -B -m unittest discover -s 99_System/knowledge/tests -p "test_v2_*.py" -v` 通过。

## Task 2: 可恢复迁移事务与分类计划

**Files:** Create `v2/transaction.py`、`v2/migration.py`、`test_v2_transaction.py`、`test_v2_migration.py`；必要时给旧 `_safe_stream` 增加向后兼容的 DELETE 访问参数。

**Interfaces:**
- 操作：`{source: str|None, target: str, content: bytes|None, reason: str}`；content 为 None 表示原字节移动。
- `transaction.plan(root: Path, operations: list[dict], backup: Path) -> dict`：返回 plan、plan_sha256、planned；原件/载荷/逐文件 diff 在 Vault 外。
- `transaction.apply(plan_path: Path, approved: str) -> dict`、`restore(...) -> dict`：整批预检，逐项独占、哈希与持久日志；拒绝目标碰撞、重复和路径越界。
- `migration.build(root: Path) -> tuple[list[dict], dict]`：返回全部路径映射操作和解释报告；从旧核心/课程/主题索引/标签资料生成计划，不直接写笔记。

- [x] 先写失败测试：原字节移动/改写、备份恢复、并发改变、目标已有、联接/路径越界、重复操作和只恢复实际应用的操作。
- [x] 实现事务；复用 Windows 文件保护，不能先删除源再写目标；恢复也保护之后的用户改动。
- [x] 先写失败测试：作业与习题归 homework、课件/原始录制/索引不是课堂笔记、跨课程 review、缺 source 进入 Inbox、确定性链接修复、来源证据保留。
- [x] 实现显式类型/位置规则，需语义判断的例外逐个核实；不根据相近概念伪造 source。
- [x] 在完整副本或隔离夹具中 apply/restore，验证内容与附件哈希。

## Task 3: 课程采集与润色协议

**Files:** Modify `scripts/pull_tmeet_recordings.py`、必要时 `scripts/recording_ui.py`；create `scripts/tests/test_recording_v2.py`。

**Interfaces:** 课程根为 `03_Sources/Courses`，未匹配录制进入 Inbox；生成 lecture 的 time/subject/source/lecture_date/status/polish_status 符合设计；原始转写仍是素材。

- [x] 先写失败测试：新目录和归档、占位状态分离、多段来源保留、README 展示润色状态而非误用提炼 done。
- [x] 修改必要路径、模板与状态读取，保留录制 ID/会议信息/缺失素材边界等扩展数据。
- [x] 运行课程脚本相关全套测试；CLI 帮助命令不触发网络采集。
- [x] 正式部署后重打包旧 exe，保留旧字节备份；只在本地帮助/导入路径上验证，不自动加入会议或发送消息。

## Task 4: 按指令提炼协议

**Files:** Create `v2/extraction.py`、`test_v2_extraction.py`；主 agent 集成 `v2/cli.py` 与旧 `knowledge.py` 的 v2 分发。

**Interfaces:**
- `extraction.prepare(root: Path, scopes: list[str]) -> dict`：指定 Sources 范围、完整来源正文、哈希、同义候选、主题与标签词表；只读。
- `extraction.propose(root: Path, packet: dict, response: dict) -> list[dict]`：返回 Task 2 操作；响应含 notes（path、metadata、body）、coverage（source、complete、atoms、skip_candidates、human_approved_skips）。
- 响应必须核对原 packet 的来源哈希；原子引用真实来源和已存在/同响应创建的有效 MOC；复用笔记只做有依据增补。
- complete 只在有原子承接且没有待人工批准的跳过时允许；不完整就保持 not done。来源正文和非 status 人工字段不被提炼过程无故改写。

- [x] 先写失败测试：旧包拒绝、source 变更、原子缺来源/主题、未批准跳过、不完整 coverage、已整理与原子归档状态分离、重复提炼。
- [x] 实现严格提炼提案验证与归档状态控制；note 内容生成由 Agent 完成，程序不冒充语义理解。
- [x] 通过事务计划应用并验收；入口提供 audit/new/prepare/propose/apply/restore/views，不增调度。

## Task 5: 正式部署、dry-run、迁移与真实验收

**Files:** Home、相关 AGENTS/CLAUDE 及规范、更新版 architecture/daily guide、迁移报告、主题与课程 Bases；本轮全部数据位置。

- [x] 将通过测试的自有代码从隔离开发区按基线哈希部署到真实 Vault，不覆盖开发期间的新用户编辑。
- [x] 产生完整只读迁移计划、逐文件 diff、哈希、恢复命令；在范围内核对并保存解释报告。
- [x] 先应用已核对迁移；并发冲突重新规划，不能覆盖用户改动。
- [x] 根据迁移后的实际类型和路径生成视图、MOC 递归内容与 Home，校验主题身份和来源。
- [x] 同步课程采集、标签维护和有效文档入口；用户未选的外部/独立内容不重组。
- [x] 用真实来源做一次受限提炼演示；未完整覆盖则保持 not done，报告实际新增/复用实体。
- [x] 运行 v1 回归、v2 测试、实际审计、附件校验与逐章抽检；修复新产生的断链。
- [x] 独立完整代码审阅，修复重要问题后复测；报告待核实来源/历史时间和全部恢复位置。

## Execution record

持续记录在 `docs/superpowers/plans/2026-10-28-knowledge-vault-restructure-progress.md`，每项记录验证命令、结果、实际变更和裁定。完整设计已由用户于本会话明确批准，执行过程中不重复请求继续许可。
