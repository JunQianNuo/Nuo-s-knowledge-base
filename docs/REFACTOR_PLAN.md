# Phase 1 与 Phase 2A 实施及验收记录

前文保留 Phase 1 当时的权限与结果；本次生效的增量授权、检查点和逐文件对照见后文“Phase 2A 执行记录”。

## 目标与权限

用户于 2026-10-27 批准精确清单中的 20 个新增文件，构建独立 Type Registry、四种模板、Draft 2020-12 Schema 及只读 Validator。YAML title 非必填，schema_version 可选；新模板默认声明版本。新旧规范并存，不进行实际迁移。

本文件也是本阶段实施记录，不另建日志、工作树、依赖缓存或过程文件。没有修改根 AGENTS.md、CLAUDE.md、旧规范、旧脚本、插件、真实笔记或数学建模子项目的权限；不自动提交或推送 Git。若必须改变清单外文件，停止该动作并另行申请。

完整清单见 [[99_System/knowledge/README#实际新增文件清单]]。架构见 [[docs/KNOWLEDGE_ARCHITECTURE]]；根指令更新仅有 [[docs/AGENTS_PHASE1_PROPOSAL|建议稿]]，尚未生效。

## 工作步骤与接口

1. 建立基线：检查 20 个路径均不存在，记录现有文件元数据、文本与配置哈希汇总、HEAD 和未提交状态。
2. 先写隔离测试和 cases.json，确认尚无实现时测试失败。
3. 新增注册表、六份 Schema 和四个模板；四种配置引用同一 common Schema。
4. 实现 load_system、parse_frontmatter、validate_note、is_system_path、check_system 以及只读 CLI。
5. 测试模板、版本、历史类型、扩展字段、YAML、只读、离线及旧标签工具隔离。
6. 完成文档、独立代码审查、针对问题的回归和最终白名单核对。

## 验收命令

```powershell
python -B -m unittest discover -s "D:/知识库/99_System/knowledge/tests" -p "test_*.py" -v
python -B "D:/知识库/99_System/knowledge/validator.py" check-system --format json
```

预期所有测试通过；系统检查报告六份 Schema、四份有效模板、0 个错误、0 个知识实体及 4 个系统文件。报告不落盘；-B 禁止生成字节码缓存。需要文件输入的测试只在系统临时目录建立合成 Vault。

## 验收标准

- type 与 role 分类明确；原子最小输入无需 YAML title。
- 未声明版本可以兼容验证，但必须报告 undeclared；不声称历史创建规范。
- 未登记字段警告并保留；历史“知识点”没有自动命题映射。
- 关系只检查整篇链接格式，不判断存在性、唯一性或内容正确性。
- Schema 复用有效；未知版本、远程引用、重复或失效映射能检测。
- 模板、测试和治理文件不计入知识实体；未来扫描、MOC 和图谱排除要求明确。
- Validator 的执行不写输入、不创建输出文件、不获取网络 Schema；原标签工具只做合成数据规划测试。
- 新增文件严格属于批准清单；既有文件与开始状态核对，原有两个 dirty gitlink 不被处理。

## 实施记录

- 基线：HEAD 21b792d67e39dc730e4f7512292f6886c2df58e5；29,582 个既有文件的路径/大小/mtime 汇总，11,894 个文本及配置文件内容哈希汇总；扫描无错误。排除 Git 内部数据、依赖与常见缓存，不跟随目录联接。
- 原未提交状态：数学建模/2026国赛、数学建模/AutoMM 两个 gitlink 标记为修改；未对其实施操作。
- TDD：先建立测试，观察到 validator.py 尚未存在导致失败；初始实现后 16 项测试通过。
- 边界回归：先观察到末尾换行链接被接受、隔离前缀可被移除及 bootstrap 远程引用尝试联网三项失败；随后禁止链接中的换行、约束最低隔离前缀、给 bootstrap 使用仅含本地资源的引用注册表，17 项测试通过。
- 执行选择：按用户白名单在原工作区仅新增文件，不采用技能默认的额外工作树、过程文件或自动提交；批准的本文件保存过程记录。
- 本轮最终验收运行：18 项 unittest 测试通过；check-system 为 6 份 Schema、4 个有效模板、0 个错误/警告、4 个系统文件、0 个知识实体。24 组合成样例与多组公共字段、配置损坏和 CLI 子用例纳入测试。
- 白名单核验：Git 仅多出清单中的 20 个未跟踪文件，无既有跟踪文件的新增修改；HEAD 和原有两个 dirty gitlink 标记保持。20 文件语法及空白检查通过，没有新字节码缓存。
- 保护复核边界：既有文件汇总摘要前后不同；按首次新增文件的创建时间窗口检查，仅发现 .obsidian/workspace.json 更新。该文件是 Git 忽略的运行时会话状态，未由本工具写入，当前状态保留，未回滚。初始快照仅保存汇总哈希而非逐文件清单，因此不能用它证明所有既有文件逐字一致；Git 核对与时间窗口检查分别提供各自范围内的证据，不夸大为附件完整性审计。
- 独立只读代码审查复跑原 17 项测试通过，无 Critical/Important，发现 1 项被评为 Minor 的非法 YAML 标量异常。实施者按公开 API 会抛异常及 CLI 误分类的实际影响，将其提升为需修复项；先用 int/float/bool/timestamp 显式标签和 CLI 回归观察失败，再在 YAML 解析边界归一构造异常，最终 18 项测试通过，没有遗留该问题。该取舍只增加输入诊断，不回写数据；若归类错误的代价是错误诊断，已用回归限定为非法标量输入。
- 审查中明确搁置 Formatter 集成、链接存在性与语义检查、旧标签工具适配：均属未授权后续阶段，不能因本轮审查而扩范围；保留未完成状态及兼容警告。

## 风险与恢复

Formatter 未定位、专项审计未完成、未集成。旧标签工具的链接上下文风险通过测试和诊断显式暴露，不在本阶段修复。结构验证不能证明数学内容正确。

本阶段只有新增文件，不需要覆盖恢复旧笔记。若未来撤销，应先核对实际新增清单和文件是否有用户后续修改，再单独批准清理；本工具没有自动删除或恢复接口，不用 reset、clean 或 stash 处理用户工作区。

未来批量变更须另行批准：记录范围、规则版本、前后哈希、逐文件 diff、路径映射和原始字节备份，审批绑定具体计划；执行及恢复时都检查并发修改。单文件 os.replace 不等于整批事务。独立仓库和 Git LFS 实际对象需分别核验。

## 未授权后续阶段

Phase 2 为 Formatter 专项定位与工具集成、链接检查；Phase 3 为四篇实变函数候选的实际试点；Phase 4 为 AI 分类与语义建议；Phase 5 为渐进迁移；Phase 6 为自动化维护与长期回归。这里只保留路线，不实施这些阶段，不自动修复历史链接，也不修改 Base 或插件。

## Phase 2A 执行记录（2026-10-27）

用户另行批准 16 个既有文件修改和 5 个新增文件，分为 2A-1 与 2A-2；下列记录覆盖本次授权，前述 Phase 1 记录保留原语境。Phase 2B 未批准，Formatter 未定位，不能创建替代实现或宣称集成。

- 基线在进程内保存逐文件 SHA-256、大小和 mtime，覆盖 29,602 个现有文件；不落盘额外清单。批准范围的前后对照和受保护范围核验在最终验收时记录于此。
- 2A-1：先加入大整数诊断、非 Schema 引用目标、无条件引用环、嵌套 ID、缺失公共引用及人工审查标记损坏的回归；观察到失败，再加固解析器及注册表约束。六个治理入口按已审阅补丁更新，保留原行尾。
- 2A-1 检查点通过：20 项 unittest 全部通过；check-system 为 6 份 Schema、4 个有效模板、0 错误、0 警告、0 个知识实体。随后才进入 2A-2。
- 执行选择：以用户最新验收 B 为准，旧工具也不从 topics、标题、文件名或语义关系生成标签；仅可规划显式 tags 的无歧义标准名归一，未知与歧义值保留。真实笔记不执行标签写入。该选择替代先前方案中保留旧 topics 补标的设想；代价是旧自动补标行为停止，相关旧测试改为明确验证不补标。
- 仅使用批准路径保存代码、测试及本记录；不另建工作树、过程文件或 Git 提交。隔离测试可使用系统临时目录。

## Phase 2A 实际变更与逐文件基线

本轮实际范围为 16 个既有文件修改、5 个文件新增，清单如下。哈希算法为 SHA-256，基线取自写入前逐文件快照；未改变 Phase 1 其他文件。本文不嵌入自身最终哈希，交付消息另给出该值。若后续又改动批准文件，应重新计算本表。

| 操作 | 相对 D:/知识库 的路径 | 基线 SHA-256 | 当前 SHA-256 |
|---|---|---|---|
| 修改 | AGENTS.md | 8e85a502be3ffe8415cd89731fb18c3ed517881a4f4ce99d77881ba215192c81 | 1c8b884b76a0c47878c248194670af5a31b215cc884ca6a193f1c7b65ca02b7a |
| 修改 | CLAUDE.md | a013a6742109af4dc1809b12d004c1d528cead6e29f99e1460877dbc145dc6c9 | db4d31fd911ceac2bfdecbb8e1f1d8a2e6d8abee58d544a405d6e9d5054905ae |
| 修改 | 规范/知识库元数据规范.md | bc8901119c9fa5f48161e219caca739b6c60b32828eed6e5ae1476cf8527d7ad | c16ea9a71150b6c2ead89a198b69a75f3c828fd2a66b551d7ce7e233c504ae8c |
| 修改 | 规范/知识原子卡规范.md | 63c015b893f401b13f8f166e58bad16ffd1a92f4951a76cc3a8658f200469f53 | 888a061b789c98df3a7f670d04946da10ace2c2f30ff490687681cb2742a8266 |
| 修改 | 规范/Obsidian写作规范.md | 66e7efcb06ea888e9bf51fd7745853c2432c8b8a7e6ba9582f2dc4781e8600fb | 839e4fdb75b119ede05c91d8a2722ef57a07bf3aac2a0e19e0ad04c95fb7e8ca |
| 修改 | 规范/质量审查规范.md | 9e3b82479d7922fa1ed7c74ec25b3a4a9ea78b346850cdc12d42463cbd28b82f | 495c9d91276d088427998dbf38ab11e94115d6d6b317d3d91f0d47814cac2deb |
| 修改 | 99_System/knowledge/validator.py | 46d6ef3414a01497f96ce92e2dd5219482bc1807ac4b4a2c3d543b56cd088fdb | 1127a68756d44d2524039618172449658667f63fe74bec1ed6c14c6b0e7a2503 |
| 修改 | 99_System/knowledge/schemas/registry.schema.json | b5dc239155a65072991579eaac2d99846a3ce9d037beecc04c6467424832c9a9 | 5889b5381131e56c940954da3f4e2b396cd8cbf6066dfeace1e240b644d8010e |
| 修改 | 99_System/knowledge/tests/test_validator.py | 4cd92caed7f3729d75df2d1de94f8500e8223cbe05d51578d33cc326b79223fa | ba2c3b413e9275ea12c8d4615bcc25eebe2300e22a1cd43ac417609438dd2862 |
| 修改 | 99_System/knowledge/requirements.txt | e443c9296c83477edc659d344a3a38e2ab768f70d1ea42fa0989bc1bed830aca | c599cffcd29ecbd07adbc8f4fa0c3fc8f9b9400059e834d5b9332b8dde50a7c9 |
| 修改 | 99_System/knowledge/README.md | 47545539171ab477de6699d1a035cf0e0eaa530fd05cb9eb960df7d339ac6053 | 90eba4f7c3bcb5b01ffafef2676bf24677656f26e5663b6985e3173c31a3b3aa |
| 修改 | docs/KNOWLEDGE_ARCHITECTURE.md | 01aa082c3dfc5bd0fee1ea146c0ef690103661e685584a4d7e5de72f1c128c4a | e2a613da015300128e912fc1a0c5f0eea058cd674c9659f6ce52e939ad007d0a |
| 修改 | docs/REFACTOR_PLAN.md | fa2f5489c2667b38bf95362071fd08691fe949d7244260cf04bb9dbd515c749c | 本文最终 SHA-256 在交付消息单独提供，避免自引用 |
| 修改 | docs/DECISIONS.md | 3ac46ce9dcea7d5343bbb525fb7184f39cd8f346be40343f3b0d4822703879a0 | a9fa6a3f14b6a548986e43e50b8c4bd9cb975854329bb3d6dc6bee9fea62521f |
| 修改 | scripts/tag_maintenance.py | b9b54ba1d01327a35b0f76ec227d3ecdacd38d1ba08138cf3926d2348a8164e6 | 962493be73f150f6ece4001c697fd1b0538df86798e5c3f75e37eed5f4deb4b2 |
| 修改 | scripts/tests/test_tag_maintenance.py | f4975ab4605611512d41f9d1f3a6fb979b4461b2541b49fcdd5f4101360e70ff | 2ec668cd216d2be6ff8dc4fb93f0ce8d222d65276667c332e64cb3c335c913c0 |
| 新增 | 99_System/knowledge/link_validator.py | 新增，无原文件 | 75cac010843839442f07810d0cbff65619e459ae057c51621ad9931437bd0861 |
| 新增 | 99_System/knowledge/maintenance.py | 新增，无原文件 | f60f5d3747eb0ff2a6b68677c6ce29cb806374dfcf952a26a0dc5e959b8c89a3 |
| 新增 | 99_System/knowledge/tests/test_link_validator.py | 新增，无原文件 | b4b86d45cb8c296dc9eaf2ae9a0b8580ebf0965a02b526d43dbe86a4f749e3d7 |
| 新增 | 99_System/knowledge/tests/test_maintenance.py | 新增，无原文件 | 6aa8c1614055adaa7fd5bfb955113de7011a223bc8c66e548d6e2206910d93bb |
| 新增 | 99_System/knowledge/tests/link_cases.json | 新增，无原文件 | 395ef46a8db33f2bdf09d185e89ee3f109052b097bcbb31f86749773beb8b800 |

### 阶段结果与剩余边界

- 2A-1 在进入下一步前通过 20 项测试及四模板检查。
- 2A-2 最终完整回归：系统 43 项、旧标签 11 项，合计 54 项 unittest 全部通过；check-system 为 6 份 Schema、4 个有效模板、0 错误、0 警告、4 个系统文件、0 个知识实体。输入使用内存或隔离临时数据，未调用真实笔记标签执行。
- 独立只读审查复跑最初 39 + 11 项测试，发现四项 P2：Markdown 相对 URI 误用 Wiki 候选规则、Wiki 原文被遮罩替换、anyOf 等同实例引用环未被拒绝、合法空 Markdown URI 被判错。已先加入失败回归再逐项修复；配置回归重新通过 2A-1 后才继续链接修复，最终 43 + 11 项通过。没有将修复后的自测表述为审查者再次批准。
- 新增保守边界：百分号编码 Wiki-link 为 unchecked，报告原始目标及字面/解码候选；Markdown URI 正常解码。相对 Markdown 路径只按来源目录定位，空 URI 定位自身。Schema 的循环检查覆盖 allOf/anyOf/oneOf、not/if/then/else 与 dependentSchemas 的同实例路径。
- 审查非阻断边界保留：复杂标题、PDF、别名及外部 URI 不猜测；单文件替换不构成整批事务，最后一次校验与替换之间也不提供文件系统锁保证。真实批量执行仍须另行审批并评估并发写入。
- Maintenance 默认只读且要求显式范围，报告五类链接状态和范围、候选、依据；无可靠字符映射的行列为 null，正文可定位 Wiki-link 提供字符行列，不声称等价于 Obsidian 运行时。
- 字符位置按解码后 Unicode 字符计数，不是 UTF-8 字节或制表符视觉列；复杂嵌套标题、PDF 页码、外部 URI、别名独立目标和排除命名空间为 unchecked。
- 真实笔记没有标签执行、链接修复或迁移。测试写入/备份仅发生在临时目录。没有自动安装依赖、插件修改、Git 提交、推送或分支切换。
- 保护核验：21 个授权路径全部符合预定的 16 改、5 新；范围外无新增和删除。29,586 个范围外基线文件中，29,583 个内容、大小、mtime 均未变化；三个 Obsidian 文件在运行期间发生变化，不能声称所有范围外文件完全一致。
- 范围外变化为 `.obsidian/workspace.json`、`.obsidian/plugins/remember-cursor-position/cursor-positions.json`、`.obsidian/plugins/extended-graph/data.json`。本次实施工具没有写入这些路径，也没有回滚它们；仅凭最终状态不能确定写入来源。Git 相对 HEAD 的图谱差异是 scale 值，另外两项涉及工作区/光标运行记录。它们单列为环境并发变化，不能作为本次代码获准修改插件配置的依据。
- 根仓库：HEAD、分支相同，暂存 diff 仍为空；最终核验发现 .git/index 字节摘要不同于初始值，不能宣称 index 字节未变。期间执行过 git status，可能涉及索引 stat 缓存刷新；没有执行 add/reset/stash/commit，也没有回滚索引。工作区 status 不同，包含获准文件变更及上述两个已跟踪运行数据变化。数学建模/2026国赛、数学建模/AutoMM 的 HEAD、分支、index 及完整 status 均与基线相同，原未提交状态保留。真实学习笔记、附件和 Phase 1 清单中本次未授权文件未检出变化。
- 语法核验：批准路径内 Python 均能 AST 解析，JSON 均可加载；AGENTS.md/CLAUDE.md 原有空白行不顺带清理。没有生成字节码缓存或依赖安装产物。
- Formatter 仍未定位，不创建替代系统。Phase 2B 与 Phase 3–6 未授权。
