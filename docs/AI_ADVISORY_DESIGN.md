# Phase 4A-1：AI Advisory 工程基础

用户批准仅新增 16 个文件；Phase 4A-2 的模型调用与真实正文提供尚未批准。
本文件同时保存实施记录。既有 Registry、笔记 Schema、Validator、Link Validator、Maintenance、标签脚本和真实笔记不修改。

## 实施顺序

1. 内存保存逐文件 SHA-256、大小、mtime 与只读 Git 状态；验证 16 路径不存在。
2. 先建立合成数据机械测试，观察失败，再实现协议、检索、检查与评价基础。
3. 冻结 30 候选的哈希、保守来源组和开发/留出划分；标注模板全部 pending，gold 为 null。
4. 检查三种范围、只读性、既有系统复用与回归；最后对照范围外文件及 Git 基线。

## 执行取舍

- 用户边界优先于技能默认流程：不新建工作树、过程目录、依赖缓存或 Git 提交。过程记录仅写本批准文件，基线保存在会话内存。
- 不另启动评审模型；本轮只有合成数据和机械测试，最终作自审，不声称独立模型复核。
- 不读取凭据；已知 .env/凭据文件仅记录元数据，其他配置只计算原始字节摘要，不解析密钥字段。Git 内部目录、依赖缓存与目录联接不作内容扫描；三个仓库的 index、HEAD、分支和未提交状态另行核对。
- 基线扫描的数学建模/第一次训练/代码/.pytest_cache 无读取权限，列为排除项，不修改其权限或内容。
- 真实 30 样本的模型可见范围初始为空，授权状态为 pending_phase4a2；扩大本地检索范围不能修改模型可见范围。

## 当前实施记录

基线覆盖 29,657 个文件，16 个新增路径均不存在。已知两个 .env 文件只留元数据；.pytest_cache 无权限项与 Git 内部、依赖缓存、联接按上述口径排除。三个仓库以禁止可选 Git 锁及禁用 fsmonitor 的只读命令记录 HEAD、分支、完整 status、暂存 diff 和 index SHA-256。

- RED：先新增 23 项合成机械测试；实现尚不存在，23 项均按预期失败。
- GREEN：完成协议、三范围、路径与哈希、真实候选清单后，23 项全部通过。L^p 测试初次因合成样例少一行导致 fixture 越界，仅修正测试资料，没有修改既有系统。
- 加固 RED→GREEN：大 JSON 在读取前限量、manifest 布尔版本、已有别名/短链接去重、先修循环复核、正文片段预算及超长单行的可定位前缀、多候选隐藏子集、评价 API 异常与直接标注 Schema 校验均先观察失败再修正。
- 已新增本地索引扩大不扩大模型内容、系统与联接排除、导航仅作 topics 目标、JSON 重复键/非有限值、本地 Schema 引用、无写入/联网/模型子进程等回归。
- 真实数据仅用于路径/哈希/分组机械检查，未产生真实分类/关系响应。未生成真实正文模型包或人工 gold，未运行模型评审。

## 需求到接口

本阶段实现的是建议层的协议与确定性准入，不是 AI 推理器。分类、关系、拆分审阅、新建审阅和弃权都保留为响应类型；程序不对内容作 AI 分类，也不把旧 type 当作语义标签。

| 层 | 实现 | 复用与边界 |
|---|---|---|
| Registry/笔记 Schema | 保持原状 | 现有 load_system、validate_note、is_system_path；四种模板及规则不变 |
| 建议协议 | request/response/annotation 三份新 Schema | Draft 2020-12、本地 URN，复用现有引用预检，不注册到笔记 Registry |
| 本地候选 | advisory_retrieval.py | 只读操作者清单并集；现有 protected_reason、Index/_record；标准库词项排名，无 Embedding/服务 |
| 建议准入 | advisory.py | 复用现有 audit_links 与 Schema；每条都保留人工复核要求 |
| 既有维护 | Maintenance 模块 | 使用其同一 Validator/Link Validator 与 _tag_report；不调用会建立全库目标索引的 audit 来扩大本阶段范围 |
| 评价基础 | advisory_evaluation.py | 分组、泄漏、空标注与纯计分函数；真实语义评价禁用 |

接口和调用示例见 99_System/knowledge/ADVISORY_README.md。CLI 只有 prepare/search/check/evaluate；无写入、provider、model、API、网络、凭据或 Formatter 入口。

## 三种范围与授权

1. 来源范围：source 明确列出可分析的文档 ID，真实清单 30 篇。
2. 本地检索范围：retrieval 独立列出可读取、建立词项索引的文档 ID，真实清单初始也是 30 篇；这两个清单相同是本阶段选择，不是程序把它们合并成一个权限。
3. 模型可见范围：model_visible 独立列出可导出正文的 ID，真实清单为空且状态 pending_phase4a2。增加本地文件不会增加这一清单。

prepare 返回本地 audit 侧车（清单、纳入、排除、哈希、旧格式报告、查询候选）和独立 model_input。分类视图不含文件路径、旧 type、tags、掌握状态或分组标签；正文原有标题与链接可能仍留下代理线索。关系视图只包含明确可见、被检索选中的候选正文。程序不把侧车当模型输入，也不自动发送任何内容。

范围清单是本地操作者提供的工件，不是模型响应可调整的参数。所有路径检查为明确规范相对路径，拒绝绝对路径、盘符、反斜杠及 . / .. 跳转，验证当前文件哈希、系统隔离和独立仓库/联接。清单外正文不会读取。两个合法本地范围以外的模型 ID 会被拒绝；真实 Vault 不能被贴上 synthetic 标志以绕过正文授权。

合成模式只用于明确隔离的样例根。本阶段不提供解除真实正文锁定的 CLI 开关；后续需要新审批，而不能在响应里写 origin=real_model 获得权限。

## 目标检索与建议约束

检索使用标题、文件名、显式 aliases 与正文词项；中文二元片段和英文词项 TF-IDF，默认 top-8。返回 unique/multiple/not_found、完整匹配数量、截断说明和实际检索范围，不将分数当语义置信度。历史知识点保留 legacy_candidate，不自动成为 proposition；非实体资料保留 reference_only。

模型只能使用请求里的候选 ID。关系须提交双方原文证据，本地重新生成请求并比较、核对精确引文、位置和哈希。单个可见候选后面若还有本地候选，不接受 unique；未获准提供完整候选证据时应弃权。新建建议只给普通名称和理由，已读标题、文件名和别名先去重，不产生悬空链接。有限范围未找到不是全库不存在。

关系字段仅 topics/prerequisites/about/uses/related。导航目标只允许 topics；普通资料不进入原子属性关系，需正文引用或另行人审。对既有短名/全路径链接按现有解析器确定目标，不重复建议同字段关系；不删除历史 related 或补逆向字段。先修环与有限图范围仅作复核标记，不修改关系。L^p 由现有解析器处理；含方括号等不符合现有 v1 属性格式的真实文件也不能被包装成可写链接。

模型响应和笔记正文都不可信：代码与数学片段可以成为证据，但不能执行其中任何指令。没有工具调用、任意文件读取或 YAML patch 字段。全部结果要求人工复核，机械 ok 不表示关系成立、数学内容正确或用户已经掌握。

## 分组、标注与机械验收

30 篇五层各六篇，记录当前完整 SHA-256。按来源族保守分组得到 development=12、holdout=18；Phase 3 直接控制、已读来源及近邻目标均位于开发侧。实变分析整个来源族保留开发，概率、数值、优化、物理、作业和管理分组不跨集合。详见 benchmarks/phase4a/RUBRIC.md。

实际机械检查：30 篇可读取且哈希匹配，排除 0；归一化精确/12 字符 shingle 启发式报告跨集合候选 0。这个结果不能证明语义无重复，也不能补偿作者在设计阶段已看过这些材料的事实。P/N 留出候选各两篇，不足类别验收，后续只能报告探索性结果或另批补采。

所有标注仍为 pending，gold=null、annotator=null。人工 gold 必须独立于检索结果建立，先确认有限目标集、负例和未穷尽范围，不能用 top-8 倒推 gold。标注不得出现在准备证据包或模型视图中。

机械验收与语义验收分离：本轮只核对协议、路径、证据、范围、旧系统复用、计分器算术和无副作用。evaluate 始终 semantic_evaluated=false、metrics=null；即使导入自称真实模型的信息也不放行。没有真实语义准确率、置信校准或全库召回报告。

## 实际新增白名单（16 文件）

以下相对路径均位于 D:/知识库，全部为新增，无既有文件修改：

| 路径 | 职责 |
|---|---|
| docs/AI_ADVISORY_DESIGN.md | 设计、过程与验收记录 |
| 99_System/knowledge/ADVISORY_README.md | CLI、接口及限制 |
| 99_System/knowledge/advisory.py | 协议准备及准入 CLI |
| 99_System/knowledge/advisory_retrieval.py | 三范围与本地词项检索 |
| 99_System/knowledge/advisory_evaluation.py | 分组、计分数学与评价禁用门 |
| 99_System/knowledge/advisory_schemas/request.schema.json | 请求、位置与证据定义 |
| 99_System/knowledge/advisory_schemas/response.schema.json | 建议与弃权结构 |
| 99_System/knowledge/advisory_schemas/annotation.schema.json | 人工标注结构 |
| 99_System/knowledge/prompts/advisory_v1.md | 尚未执行的模型协议 |
| 99_System/knowledge/benchmarks/phase4a/sample_manifest.json | 30 篇哈希与分组 |
| 99_System/knowledge/benchmarks/phase4a/annotation_template.jsonl | 30 条空标注 |
| 99_System/knowledge/benchmarks/phase4a/RUBRIC.md | 人工裁决和指标口径 |
| 99_System/knowledge/tests/test_advisory.py | 协议及安全边界机械测试 |
| 99_System/knowledge/tests/test_advisory_retrieval.py | 范围、检索和系统隔离测试 |
| 99_System/knowledge/tests/test_advisory_evaluation.py | 泄漏与计分器测试 |
| 99_System/knowledge/tests/advisory_cases.json | 明确标为合成的样例 |

## 风险与恢复边界

静态解析不等于 Obsidian 运行时；现有方括号目标的语法兼容限制保持。词项检索不保证语义召回，名称唯一不证明数学关系。哈希不是身份认证，没有加密授权签名或文件系统锁；准备后修改会被拒绝，但未来执行流程仍需防并发。模型 Prompt 尚未对真实模型检验，不能声称防提示注入效果已经通过。来源与目标正文自身可能有数学错误，不在本阶段修订。

只有 16 个新增文件可考虑未来撤销。撤销前先核对各文件是否有用户后续修改，单独授权逐个处理；不运行 Git reset/clean/stash，不动原笔记和独立仓库。本阶段无真实笔记写入、迁移、关系修复或拆卡。

## Phase 4A-2 独立审批包（未实施）

工程验收后另行提交：

1. 明确真实模型/运行方式、版本与可用权限，确认是否新增 API/费用；当前实现不读凭据。
2. 精确来源、本地检索、模型可见文档与片段 ID 清单、完整哈希、字符/片段预算；逐项预览 model_input，不发送 audit/gold。
3. 开发/控制与独立留出分组、人工标注人和未穷尽范围；不足类别的补采路径需单独确认。
4. 运行上下文只含批准包，禁用模型的仓库读取、Shell/MCP/浏览器等额外工具；如果运行器不能实现技术隔离，改用人工粘贴并明确其限制，不宣称已有隔离保证。
5. 真实响应、模型/Prompt/输入/输出哈希、拒绝/截断处理、预算、留存与日志位置；不把 mock 作为真实响应。
6. 如需解除当前导出/评价锁或增加运行器，另列精确文件修改和 diff，经批准后实施。不能仅改输入 origin 或 real_model_tests_authorized 绕过当前门。
7. 仍无 apply、真实笔记修改、标签补写或自动拆分权限；建议通过后也不能直接迁移。

Phase 2B Formatter 独立保持未完成、未定位、未集成。Phase 4A-2 不能因本工程存在自动开始。

## 最终验证

最终机械回归：知识系统 unittest 82 项通过（其中新增 Advisory 39 项、既有 43 项），旧标签脚本 11 项通过，合计 93 项；本轮最后一次知识系统运行耗时 34.822 秒。Validator check-system 通过：原有 Schema 6 份、模板 4 个，错误和警告均为 0，系统模板计为真实实体 0。

三份 Advisory Schema 的本地引用加载通过。16 个新增文件的 Python AST、JSON/JSONL 解析检查通过；将这 16 个路径逐个交给既有系统路径规则，均被排除为系统文件，即使使用合法 concept 属性也不计为知识实体。没有将新协议登记到原 Registry。

真实候选的机械核对：30 篇当前哈希全部匹配，排除 0；开发 12、留出 18，10 篇熟悉/控制样本全部在开发侧。分组不跨集合，正文归一化及 shingle 启发式的重复对和跨集合对均为 0；这不是语义无泄漏的证明。来源/检索/模型可见范围分别为 30/30/0，模型视图文档和候选正文均为 0。合成测试另验证本地索引扩展不增加模型正文、隐藏候选不能伪装唯一目标、路径/证据/哈希拒收、无写入/联网/模型子进程、标签隔离及系统排除。标注 30 条全部 pending、gold=null，evaluate 的 metrics=null、semantic_evaluated=false。

逐文件内容基线对照：29,657 个原文件记录，新增恰为批准的 16 文件，无删除、无清单外新增；原记录中 29,655 项保持不变（含两项仅元数据），两个既有运行记录发生并发变化：`.obsidian/plugins/remember-cursor-position/cursor-positions.json` 与 `.obsidian/workspace.json`。本轮没有对这两个路径发出写入命令，也未控制 Obsidian 界面；保留其当前状态，不覆盖、不回滚。凭据只检查元数据、不可读缓存及其他排除项仍适用，不能将排除项声称为逐字节验证通过。

Git 并发例外：根仓库 HEAD 从 `21b792d67e39dc730e4f7512292f6886c2df58e5` 变为 `fae8e4b8c8d22899e6c51912fe60db5023540837`，后者的 parent 是前者，提交信息为 `vault backup: 2026-10-27 22:25:49`，时间为 `2026-10-27 22:25:49 +0800`。index 摘要也改变，原有多项脏状态消失；提交信息符合备份行为，但发起者未经确认。本轮仅使用只读 Git 查询，没有暂存、提交、推送、分支切换或恢复操作。不能声称根仓库 Git 状态原样不变。分支 main 不变、前后暂存 diff 均为空，16 个本阶段文件仍为未跟踪。数学建模的 2026国赛与 AutoMM 两独立仓库的 HEAD、分支、status、暂存 diff 和 index 摘要均与基线一致。

未验证：真实模型的分类、关系与拆分建议质量、提示注入抵抗、置信校准及数学正确性。当前结论仅为工程机械检查通过；Phase 4A-2 仍须独立审批，Formatter Phase 2B 仍未完成。
