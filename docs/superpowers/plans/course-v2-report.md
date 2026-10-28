# Task 3 课程录音 v2 兼容报告

实施位置：`C:/Users/Nuo/.codex/worktrees/knowledge-v2/知识库`。未提交 Git；未写入真实 `D:/知识库`，未调用腾讯会议网络接口，未更改课表或计划任务，未打包 exe。

## 变更文件

- `scripts/pull_tmeet_recordings.py`：v2 课程目录与 Inbox 目录、课堂笔记模板、真实来源追加、润色状态兼容、保守占位合并。
- `scripts/tests/test_recording_v2.py`：14 项离线新旧兼容测试；所有归档写入均限临时目录，网络/下载边界使用固定夹具。
- 本报告。`scripts/recording_ui.py` 无须修改；其现有核心模块导入及 `--vault` 传递继续生效。

## 行为与兼容裁定

1. 新课程进入 `03_Sources/Courses/<课程>/课堂笔记/`；未匹配会议只保存原始资源到 `00_Inbox/课堂录音/raw/`。完整课程层级可保留 `归档/课程`；单独课程名复用唯一的已有课程目录，有多个候选则拒绝自动归并。课程 subject 使用名称，不将 `归档/` 当作课程名称的一部分。
2. 新课堂笔记使用 `schema_version: 2`、`type: lecture`、创建时的 `time`（ISO、`+08:00`）、课程名称列表 `subject`、真实 `lecture_date`、`status: not done`、`polish_status: not done`。不生成 YAML title 或占位 topics；原始转写/纪要仍为资源，不加 lecture 身份。
3. `source` 只链接实际存在的原始逐字稿/纪要，使用完整 Vault Wiki-link 路径。不添加虚构纪要链接或泛化的“腾讯会议录制”来源说明。追加片段同时补齐 YAML 来源和正文素材链接；重复运行保持幂等。
4. 保留现有笔记的 title、创建时间、旧日期、课程信息、自定义字段和正文，包括 CRLF、尾随空白与块 ID。旧来源说明转为列表时原值保留；不自动给旧笔记添加 v2 身份。新采集片段保留完整 `record_file_ids` 和 `recording_segments`（包含会议/录制 ID、原始时间、会议信息及分段信息）。会议号以字符串保存，保留前导零。
5. 新素材加入已有 v2 笔记时，独立把 `status` 和 `polish_status` 重新置为 `not done`，原 `time` 不变。完全重复的素材不重开状态；旧笔记沿用其旧状态，不声称旧“已完成”等价于 v2 提炼完成。
6. `_read_status`、README 和合并只消费 v2 的 `polish_status`；`done` 显示“已润色”，`not done` 或缺省显示“待润色”。历史笔记继续显示原 status。正文中的同名字段不参与状态判断。README 明确区分润色与知识提炼。
7. 同课重复占位仅在润色待处理、其他元数据一致、正文除素材行外一致时合并；来源/录制段列表合并去重后先写主文件，再删除兼容的副本。存在独有自定义数据、不同创建时间或人工正文时保持各文件。顶层重复 YAML 属性拒绝自动改写。
8. 原未匹配副本清理原先可能在部分下载后删除唯一素材。按本轮明确的禁止自动清理要求，导入器不再调用该函数，兼容入口保持不执行删除；包括字节一致的 Inbox raw 副本也完整保留。迁移阶段不依赖此函数处理旧目录。

## TDD 与验证

已先运行失败测试，再实现对应修复：最初 7 项因旧路径、旧模板、来源不完整和状态混淆失败；追加 CRLF/无缩进 YAML、手工正文保护、归档课程复用、新素材重开状态、重复属性拒绝、部分下载及字节相同副本保留原始素材的回归测试也分别先复现失败再通过。

最终验证：

| 命令 | 结果 |
|---|---|
| `python -B -m pytest scripts/tests/test_pull_tmeet_recordings.py scripts/tests/test_recording_v2.py -q` | 16 passed |
| `python -B -m pytest scripts/tests -q` | 30 passed, 10 subtests passed |
| `python -B scripts/pull_tmeet_recordings.py --help` | exit 0；显示新 Inbox 路径；不触发采集 |
| `python -B scripts/recording_ui.py --help` | exit 0；不启动 UI 服务 |
| `git diff --check -- scripts/pull_tmeet_recordings.py scripts/tests/test_recording_v2.py` | exit 0 |
| `python -B -m pytest -q` | 收集阶段失败；原因见下 |

全仓库 pytest 的既有范围外阻塞：`数学建模/tests/test_math_modeling_solver_promotion.py` 在导入时 `sys.exit(1)`，报告 3 项 promotion contract violation：缺少 `.agents/skills/math-modeling-solver/skill.md`、active skill frontmatter name 不为 `math-modeling-solver`、缺少 training-enhanced references。未修改数学建模项目，不能声称全仓库测试通过。

## 部署注意

- 核心录音脚本新增显式依赖 `PyYAML`，本机测试环境已有；PyInstaller 重打包须包含 `yaml`（普通显式导入应可自动发现）。旧 exe 仍未更新，由主 agent 在部署时保留旧字节并重建，仅验证帮助/导入路径。
- 文件命名继续保留既有录制 ID 后六位策略；本任务不改腾讯会议匹配、调课/停课规则、采集定时或正文润色流程。正文润色应只更新 `polish_status`；完整知识提炼由独立协议决定 `status`。
- 新笔记刻意省略缺失素材链接；下载缺失的部分继续由原有重试流程处理。保守合并可能保留多份历史占位，以保护用户的独有时间、字段和批注；不把此类保留报告为已合并。
