# 数学建模 Skill 合并设计

日期：2026-09-01

## 目标与范围

严格采用研究报告提出的架构合并方法，把 `XiaoMaColtAI/math-modeling-skill` 与 `Lupynow/math-modeling-skills` 合并为本地个人使用的第三个 Skill：`math-modeling-core`。

目标不是拼接两个目录，而是形成：

```text
Lupynow 的问题与算法知识
+ XiaoMa 的工程门禁与复现机制
+ 新增的统一算法 API、Registry 和 Validation Runtime
```

合并范围聚焦“数学建模与算法设计”：题目理解、问题拆解、数据审计、论文证据检索、模型选择、算法执行、验证、比较和复现。论文写作继续由现有 `math-modeling-paper` 独立承担。论文检索服务于模型选择、参数溯源和验证设计，不负责摘要、正文或排版。

本 Skill 只在个人工作区使用，不发布，因此不实施许可证清洗、clean-room 重写、来源登记、第三方声明、社区治理或发布流程。允许直接复用两个上游仓库中的相关文本和代码，并在合并时修正已知缺陷。

## 部署策略

新建 `.agents/skills/math-modeling-core/`，完整实现报告中的第三套架构。完成并通过验收后：

- 把当前 `.agents/skills/math-modeling-solver` 移到 `.agents/disabled-skills/` 作为可恢复旧版。
- 保留 `math-modeling-paper`，只承担论文写作。
- 保留 `mathmodel-skill` 竞赛全流程插件，不修改其内部文件；通过更窄的触发描述避免与新 Skill 重复路由。
- 两个下载仓库继续作为只读上游快照，不作为运行时依赖。

## 触发边界、运行模式与交接

`math-modeling-core` 保持默认可自动发现。`SKILL.md` 的 description 只描述触发条件，不概述完整工作流，拟定为：

```yaml
description: Use when solving or reviewing a mathematical-modeling problem, selecting mathematical models or algorithms, auditing modeling data, or validating and reproducing a model; excludes requests solely for contest-paper prose, formatting, or end-to-end contest project orchestration.
```

三个 Skill 的边界固定如下：

| 用户意图 | 主入口 | 交接规则 |
|---|---|---|
| 通用建模、拆题、变量设计、模型/算法选择、求解、验证或复现 | `math-modeling-core` | 在核心 Skill 内完成，不转给论文 Skill |
| CUMCM、MCM/ICM、电工杯等从选题到提交的完整竞赛项目管理 | `mathmodel-skill` | 它仍是项目编排入口；建模内核可由用户显式调用 `math-modeling-core`，两者不自动重复运行同一阶段 |
| 只写、改、检查或排版数学建模论文 | `math-modeling-paper` | 读取已经生成的 `PaperHandoff`；不得反向修改已验证的模型结果 |
| 既要求求解又要求成文 | 先 `math-modeling-core`，后 `math-modeling-paper` | 只有核心结果达到允许交接的验证状态后才生成 `PaperHandoff` |

核心 Skill 接受四种 `OperatingMode`：

- `analyze`：只完成领域理解、拆题、变量、模型合同和候选选择，不执行全量求解。
- `solve`：默认模式；执行分析、求解、验证、比较和 manifest。
- `review`：审查用户已有模型、代码、结果或证据，不擅自重写，除非用户同时要求修复。
- `evidence`：只执行 E0/E1 检索与证据结构化，不启动算法插件。

系统只在会改变数学问题或授权边界时暂停：目标/硬约束存在多种实质解释、关键业务规则无法核验、需要启用 experimental 插件、需要安装依赖、需要扩大外部检索预算，或用户要求论文交接但验证仍为 `FAIL/BLOCKED`。其他缺失信息按显式假设继续，并写入 `ProblemSpec.assumptions`；不得对每个普通参数重复请求确认。

`SKILL.md` 只保留触发边界、模式选择、不可绕过的门禁和 reference 路由。初始最多加载共享 `workflow.md` 加两个与当前模式最相关的 reference；taxonomy 确定后才加载对应 Cookbook/Playbook/algorithm note。禁止启动时批量读取全部知识库。

| 模式 | 初始 reference | 条件满足后再加载 |
|---|---|---|
| `analyze` | `domain-understanding.md`、`problem-decomposition.md` | 形成 taxonomy 后加载 `model-selection.md` 和一个对应 Cookbook |
| `solve` | `model-contract.md`、`data-and-solver-engineering.md` | 模型候选确定后加载对应 algorithm note；求解前加载 `validation-runtime.md` |
| `review` | `model-contract.md`、`validation-runtime.md` | 涉及复跑时加载 `reproducibility.md`，涉及证据时加载 `literature-evidence.md` |
| `evidence` | `literature-evidence.md`、`domain-understanding.md` | 只有 E1 方法审查需要时加载 `model-selection.md` |

## 四层架构

### 1. Reasoning Layer：问题理解与模型设计

职责：

- 读取题目与附件，先形成“已知、未知、歧义、领域术语”清单，而不是立即冻结数学问题。
- 执行 E0 领域理解检索，获取领域背景、物理/业务机制、业务规则、变量定义、单位和典型数量级。
- 建立 `DomainContext`、领域术语表、候选变量字典、机制关系图和业务规则表。
- 将子问题映射到 Lupynow 的 12 类问题本质，允许混合类型与级联数据流，并用领域证据修正初始拆题。
- 结合领域证据和附件数据建立数据结构指纹，形成 `ProblemSpec` 和 `ModelContract`，明确目标、约束、输入输出、假设、指标、风险和回退条件。
- 执行 E1 方法检索，检索相似问题、候选算法、参数依据和验证方法，形成结构化 `EvidenceRecord`。
- 先由 `ModelSelector` 选择数学抽象，再由 `AlgorithmSelector` 为入选模型选择求解算法；不得从某个现成算法反推题目必须采用的模型。
- 从知识层产生多个 `ModelCandidate`，但进入计算阶段时最多保留一个最小充分主模型和一个结构独立或能修复明确缺口的挑战者模型。
- 使用硬门禁、Pareto 支配和确定性并列规则选择候选，不使用论文篇数或默认主观权重把复杂模型推到经典充分模型之前。

### 2. Algorithm Layer：可执行算法插件

职责：

- 所有算法通过统一 `AlgorithmPlugin` 协议注册。
- 插件声明名称、算法版本、API/Schema 版本、输入输出 schema、状态、能力标签、依赖、约束支持、随机性和能力权限。
- `stable` 算法必须拥有 unit test 和数学 oracle/property test。
- 未审计模板只能标记为 `experimental` 或保留为知识示例。
- 内置插件由 allowlist 加载；个人扩展通过显式目录或 Python entry point 注册，不修改主 `SKILL.md`，也不扫描任意工作区代码。

### 3. Validation Runtime：执行、验证、比较和复现

职责：

- 环境与依赖检查。
- P1 最小结构等价实例执行。
- 全量求解、超时和失败状态管理。
- 五层验证：数据、数学不变量、数值稳定、统计/泛化、题目约束。
- 灵敏度、多初值、多随机种子、baseline 与 oracle 比较。
- 只在候选通过验证后进行模型比较。
- 输出结构化 `ValidationReport`、artifacts 和 reproducibility manifest。
- 核验进入最终结论的 DOI、题名、参数来源和文献适用条件；未核验内容不得伪装成已验证证据。

### 4. Knowledge Layer：知识增强

以 Lupynow 为知识主体：

- 12 类问题 taxonomy 和混合问题拆解。
- 95+ 场景模型选择矩阵。
- 8 本 Cookbook。
- 12 本 Playbook，降级为示例而非强制路线。
- 22 个 Python 与 7 个 MATLAB 模板，作为迁移 specification 或 experimental 资产。
- 文献检索策略、检索次数上限、适用条件审查和参数溯源方法。

补充 XiaoMa：

- 七类算法资料与算法适用条件索引。
- 建模手的模型合同、假设、验证与风险规则。
- 编程手的数值稳定、尺度、条件数、收敛、边界和资源降级规范。
- 动态依赖检查、最小可运行切片、输入只读、阶段回退和复现约束。
- OpenAlex 与可用第二检索源的交叉核验、去重和结果融合机制。

两套算法索引不并行承担路由。统一映射为：

```text
problem taxonomy → required capabilities → Algorithm Registry
```

## 目录结构

```text
.agents/skills/math-modeling-core/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow.md
│   ├── domain-understanding.md
│   ├── problem-decomposition.md
│   ├── model-contract.md
│   ├── model-selection.md
│   ├── plugin-contract.md
│   ├── literature-evidence.md
│   ├── data-and-solver-engineering.md
│   ├── validation-runtime.md
│   ├── reproducibility.md
│   ├── handoffs.md
│   ├── cookbooks/
│   ├── playbooks/
│   └── algorithm-notes/
├── src/
│   └── mathmodel/
│       ├── contracts/
│       │   ├── domain.py
│       │   ├── problem.py
│       │   ├── data.py
│       │   ├── model.py
│       │   ├── plugin.py
│       │   ├── result.py
│       │   └── validation.py
│       ├── reasoning/
│       │   ├── taxonomy.py
│       │   ├── model_candidates.py
│       │   ├── selector.py
│       │   ├── algorithm_selector.py
│       │   └── evidence_mapper.py
│       ├── evidence/
│       │   ├── records.py
│       │   ├── providers.py
│       │   ├── retrieval.py
│       │   ├── extraction.py
│       │   ├── deduplication.py
│       │   ├── conflicts.py
│       │   └── cache.py
│       ├── algorithms/
│       │   ├── base.py
│       │   ├── metadata.py
│       │   ├── loader.py
│       │   ├── registry.py
│       │   ├── optimization/
│       │   ├── evaluation/
│       │   ├── forecasting/
│       │   ├── statistics/
│       │   ├── graph/
│       │   ├── mechanistic/
│       │   └── simulation/
│       ├── validation/
│       │   ├── statuses.py
│       │   ├── invariants.py
│       │   ├── numerical.py
│       │   ├── statistical.py
│       │   ├── constraints.py
│       │   └── comparison.py
│       └── runtime/
│           ├── executor.py
│           ├── dependencies.py
│           ├── capabilities.py
│           ├── artifacts.py
│           └── reproducibility.py
├── scripts/
│   ├── doctor.py
│   └── run_model.py
├── tests/
│   ├── unit/
│   ├── algorithms/
│   ├── properties/
│   ├── regression/
│   ├── integration/
│   ├── behavior/
│   └── fixtures/
├── pyproject.toml
└── requirements.lock
```

## 统一契约

所有算法接受：

```text
ProblemSpec + DataBundle + SolveConfig
```

并返回：

```text
SolveResult + ValidationReport
```

核心类型：

- `ProblemSpec`：题目标识、问题类型、目标、约束、假设、评价协议和用户可接受的实用改进阈值。
- `ModelRequirements`：从 `ProblemSpec` 提取的强制覆盖项、结构、约束、随机/动态特征、数据和求解能力需求。
- `ComplexityProfile`：新增数据字段数、潜变量/待估参数数、未核验关键假设数、模型维度档位、求解保证要求、预计时间和内存档位。
- `ModelCandidate`：稳定 candidate id、数学抽象、覆盖声明、假设、方程/目标/约束、需要的数据、`ComplexityProfile`、已知缺口及证据。
- `ModelSelectionDecision`：被接受/拒绝的候选、每项硬门禁结果、支配关系、主模型、挑战者和可重放理由。
- `DataBundle`：原始数据引用、表/数组、字段 schema、特征、目标、单位、缺失/异常信息和切分计划；禁止只有一个无类型 `data` 字段。
- `SolveConfig`：seed、timeout、tolerance、max_iterations 和算法参数。
- `SolveResult`：解、目标值、指标、诊断、状态和 artifacts。
- `ValidationCheck`：检查名称、严重度、状态、观测值、阈值、证据和回退阶段。
- `ValidationReport`：聚合 `PASS`、`WARN`、`FAIL`、`BLOCKED` 或 `SKIPPED` 检查，并给出总状态和风险接受记录。
- `IOContract`：每个插件独立声明的 `input_schema`、`output_schema`、`config_schema`、schema 版本和自校验规则。
- `AlgorithmMetadata`：唯一 `plugin_id`、名称、版本、API/Schema 兼容范围、状态、能力、依赖、支持规模、求解保证、验证能力、确定性/随机性、资源估计器、权限和 `IOContract`。
- `SupportDecision`：插件 `supports` 的 `SUPPORTED`、`UNSUPPORTED` 或 `UNKNOWN` 结果及逐项理由；`UNKNOWN` 不得自动入选。
- `AlgorithmPlugin`：`metadata`、`supports`、`validate_input`、`solve`、`validate_result` 协议。
- `AlgorithmSelectionDecision`：入选插件、被拒插件、依赖状态、P1 结果、并列消解和回退信息。
- `EvidenceRecord`：题名、作者、年份、期刊、DOI/稳定标识、检索源、使用模型、适用条件、参数依据、验证方法、局限和访问日期。
- `EvidenceBundle`：检索式、检索预算、去重结果、核验状态以及与子问题和候选算法的映射。
- `DomainContext`：研究对象、场景边界、利益相关方、时间/空间尺度、领域术语、典型数量级和未解决歧义。
- `VariableSpec`：变量名称、符号、领域定义、角色、数据类型、单位、测量方法、合理范围、可观测性和证据链接。
- `MechanismSpec`：上游变量、下游变量、作用方向、数学关系候选、成立条件、适用尺度、证据和置信状态。
- `BusinessRuleSpec`：规则文本、官方/行业/论文来源、适用时间与地区、硬/软约束类型、形式化约束候选和冲突状态。
- `EvidenceClaim`：背景事实、变量定义、机制、业务规则、模型方法、参数依据或验证方法中的一种可追溯主张。
- `PaperHandoff`：题意与变量、模型方程、选择轨迹、参数、结果、验证、图表、证据和限制的只读论文交接包。

每个算法插件的 `IOContract` 在进入 `solve` 前执行 schema 校验；插件不得自行猜测缺失的目标、硬约束、单位或字段含义。通用 `DataBundle` 负责运输和审计数据，插件自己的 schema 负责说明“本算法实际需要什么”。

## Literature Evidence Pipeline

论文证据分为两个阶段，而不是只在模型选择前检索一次。

### E0：领域理解检索

E0 位于“初读题目”之后、“正式问题拆解和变量冻结”之前：

1. 从题面提取领域对象、专业术语、事件、参与方、时间/空间尺度和歧义点。
2. 分别生成四类查询：领域背景、机制/因果、业务规则、变量定义与测量。
3. 按证据类型路由来源：
   - 领域背景：综述论文、权威教材或机构报告。
   - 物理/生物机制：原始研究、综述、标准或教材。
   - 业务规则：当期官方规则、标准、监管文件或行业规范优先，论文只作解释补充。
   - 变量定义：标准、数据字典、领域论文和测量方法文献。
4. 从全文或可核验片段提取 `EvidenceClaim`，并分别写入 `DomainContext`、`VariableSpec`、`MechanismSpec` 和 `BusinessRuleSpec`。
5. 输出五个中间产物：领域术语表、候选变量字典、机制关系图、业务规则表、证据冲突表。
6. 用这些产物修正题意解释、问题边界和变量角色，再生成正式 `ProblemSpec`。

变量不能因为在论文中高频出现就自动进入模型。纳入变量必须同时评估：题目相关性、机制证据、数据可得性、可测量性、可辨识性、冗余/共线性和决策可作用性。变量角色统一标记为 `input`、`state`、`decision`、`output`、`latent` 或 `confounder`。

机制关系必须区分“相关性”“经验关系”“因果机制”“守恒/物理定律”和“业务约束”。论文提出的关系先作为候选机制，不直接当作本题必然成立的方程；需要核对尺度、边界条件和数据可辨识性。

业务规则必须记录适用时间、地区、组织和版本。规则如果来自可变的现实制度，必须优先核对当前官方来源；论文中的旧规则不能直接转成硬约束。

### E1：方法与验证检索

E1 位于正式 `ProblemSpec` 之后、“候选模型定榜”之前：

1. 从 `ProblemSpec`、机制关系和变量字典为每个子问题生成中文和英文检索式。
2. 检索相似问题的模型、求解算法、参数依据、验证方法、benchmark 和已知失败条件。
3. 优先使用 OpenAlex，并在可用时用 Semantic Scholar、出版方页面或第二检索源交叉核验题名、年份和 DOI。
4. 支持读取用户已下载的本地 PDF/Markdown 文献，纳入同一 `EvidenceRecord` 契约。
5. 按 DOI 优先、规范化题名其次去重；同一论文的多个来源合并为一个记录。
6. 提取“论文解决的问题、实际使用的模型、适用条件、参数依据、验证方法、量化结果和局限”，禁止仅凭摘要关键词推荐模型。
7. 将证据映射到子问题、模型合同和候选算法，输出支持、反对或条件性证据。

E1 的来源优先级按主张类型决定：数学性质和算法行为优先原始论文、官方文档或标准 benchmark；参数与领域适用性优先原始研究、系统综述和现行标准；竞赛获奖论文只能作为建模表达或候选启发，不能单独证明方法正确或适用于本题。

检索预算使用可机械计数的定义：

- 一个 `search_request` 是“一个规范化查询式发送给一个 provider 的一个结果页”。同一查询发给两个 provider 计两次；分页计新的请求。
- 网络失败后的同参数重试、按已知 DOI/标识获取元数据、打开已命中的权威页面不计新的搜索请求，但全部写入网络事件日志。
- 默认 `initial_search_budget=5`，未解决关键歧义时可自动扩展到 `hard_cap=8`；超过 8 次必须由用户明确批准新的上限。
- 领域陌生或题意歧义大时，初始预算通常分配 E0 约 3 次、E1 约 2 次；领域清晰时分配 E0 约 1–2 次、E1 约 3–4 次。分配是上限内的调度建议，不是每阶段最低消费量。
- 多个子问题共享总预算，不按子问题机械乘倍；优先覆盖会改变变量、硬约束或模型族的未决主张。若在 hard cap 内仍有关键主张未解决，相关项保持 `PARTIAL/UNVERIFIED`，不得用低优先级检索挤占关键问题。
- 提前停止同时要求：关键主张覆盖率达到预设门槛、没有未处理的高严重度冲突，并已获得通常 5–8 篇高度相关且可核验的论文。论文篇数只是停止信号之一，不是硬配额。
- 官方规则、标准和本地资料不计入“论文篇数”，但通过外部搜索寻找它们时仍消耗 `search_request`；直接读取用户本地文件不消耗外部预算。

核验状态：

- `EvidenceRecord.metadata_status=VERIFIED`：题名、年份、作者和 DOI/稳定标识已由权威页面或两个独立来源核对。
- `EvidenceClaim.status=VERIFIED`：可定位的原文、公式、表格、标准条款或官方页面直接支持该主张，且适用条件已经核对。
- `PARTIAL`：来源存在已确认，但只能核验部分字段、方法细节或适用条件。
- `UNVERIFIED`：只有搜索片段、二手转述，或者没有取得支撑该主张的可定位内容；不得作为确定性事实进入最终结论。

元数据核验不能自动提升其中所有主张。一个 DOI 正确的论文仍可能被误读；每个进入变量定义、硬约束、参数选择或最终结论的 `EvidenceClaim` 都要独立记录定位信息和状态。

检索是默认步骤，但不是硬阻塞。用户明确跳过、网络不可用或时间受限时可以继续模型设计，同时把相应的领域主张、变量定义或方法证据标记为 `UNVERIFIED`。未核验的业务规则不得进入硬约束；未核验的机制不得包装成确定性定律。候选表、验证报告和 manifest 必须保留证据状态。不得伪造 DOI、期刊级别、参数来源或论文结论。

为了可复现，每个 provider 响应保存规范化快照：provider 名称与版本、查询式、参数、页码、访问时间、返回记录顺序、稳定标识、可用摘要/片段、HTTP/工具状态和 SHA-256。提取后的 claim、定位信息与快照 hash 绑定。允许缓存元数据和依法可保存的片段；未授权全文只保存本地路径/hash 或远端稳定标识，不复制全文。重放默认使用快照，只有显式 `--refresh-evidence` 才重新联网并生成新的 evidence revision。

## Registry 与模型选择

Registry 只注册“如何求解”，`ModelSelector` 决定“问题应抽象成什么”，`AlgorithmSelector` 决定“入选模型由哪个插件求解”。两级选择器不得合并成按算法名称查表。

### 一级：ModelSelector

`ModelSelector` 从 taxonomy、机制、变量和模型知识生成多个 `ModelCandidate`，然后依次执行七个硬门禁：

1. `CoverageGate`：覆盖 `ProblemSpec` 的全部强制目标、输出和子问题。
2. `StructureGate`：连续/离散、静态/动态、确定/随机、单/多目标等结构一致。
3. `ConstraintGate`：能够表达全部硬约束；近似或遗漏必须在题目允许范围内。
4. `AssumptionGate`：线性、独立、平稳、无记忆、边界条件等关键假设未被题面、数据或证据否定。
5. `DataGate`：所需变量可获得、可测量、单位明确，或已有被批准的 proxy/latent 处理。
6. `IdentifiabilityGate`：参数和状态能由现有数据、先验或实验设计辨识。
7. `ValidationGate`：存在可执行的 oracle、baseline、留出验证、守恒律或其他证伪路径。

硬门禁结果只能是 `PASS`、`FAIL` 或 `UNKNOWN`。`FAIL` 候选被拒绝；`UNKNOWN` 候选不能自动成为主模型，必须先解决关键歧义或由用户明确接受其为 experimental challenger。文献只为门禁提供证据，不拥有独立投票权。

### 最小充分模型与论文候选准入

在所有硬门禁通过的模型中，默认主模型是**最小充分模型**：完整覆盖题目并具有满足预定义验证要求的可执行路径的候选中，优先使用附加数据需求更少、不可辨识参数更少、假设风险更低、模型维数和计算成本更低、解释更直接的模型。

采用 Pareto 支配而不是默认加权总分：若模型 A 的覆盖和验证能力不弱于 B，`ComplexityProfile` 至少一项更低且无一项更高，并且 B 没有修复 A 的明确缺口，则 A 支配 B。仍不可比的最小充分候选按“未核验 Critical 假设数、新增数据字段数、不可辨识参数数、资源档位、稳定 candidate id”进行字典序消解。权重只在用户明确给出多目标偏好时使用，并写入 `ProblemSpec.preference_weights`。

论文中的复杂模型只有填写完整的 `GapClosureClaim` 后才能作为挑战者：

```yaml
baseline_model: 经典充分模型
addresses_gap: 要修复的明确覆盖、假设、误差、稳健性或规模缺口
added_variables: 新增变量及其可测量性
added_assumptions: 新增假设及风险
added_data: 新增数据需求
expected_gain: 预期改善的预注册指标
minimum_practical_improvement: 足以抵偿复杂度的最小实用改进
validation_test: 在相同数据切分、seed 和约束下如何检验
```

`addresses_gap` 为空、适用条件与本题不一致，或只因“论文更新/模型更复杂/使用人数更多”而提出的候选直接拒绝。经典模型完全覆盖且通过验证时，论文的主要作用是核验假设、参数、验证方法和失效边界，不强制引入更复杂模型。

进入计算阶段最多保留：

- 主模型：最简单的完整充分候选。
- 挑战者：结构独立、能提供有效对照，或具有已登记 `GapClosureClaim` 的一个候选。

例如，静态、非负边权、单目标最短路由 Dijkstra 完整覆盖时，处理动态拥堵和多目标路由的蚁群论文不能成为主模型；只有题目确实包含动态、随机或多目标结构时才重新进入门禁。

### 二级：AlgorithmSelector

对每个入选模型，Registry 按能力标签和插件 schema 返回 `SupportDecision`。硬过滤顺序固定为：

```text
API/Schema 兼容
→ 模型结构和约束支持
→ 输入 schema 可满足
→ stable/experimental 状态
→ 依赖与权限可用
→ 规模、稀疏性、凸性/刚性等数值适用条件
→ P1 最小结构等价实例
```

`experimental` 不得在没有用户明确选择的情况下胜出。`stable` 但依赖缺失的插件返回 `BLOCKED`，不得静默安装依赖或用另一个算法替换。多个 stable 插件都满足时，先分别运行 P1，再按“求解保证与问题结构匹配度（可证明全局/精确优先于局部或启发式）、验证能力完整度、资源估计是否满足上限、确定性优先、插件 id、版本”进行字典序消解。所有枚举值和顺序在 Registry schema 中固定，不能由自然语言临时判断；最后两项保证相同输入得到确定的选择结果。

### 最终比较与挑战者晋级

主模型和挑战者必须使用同一份预注册 `EvaluationProtocol`：相同数据切分、指标定义、seed 集合、约束容差和资源上限。最终只比较没有 Critical `FAIL/BLOCKED` 的候选。

挑战者替换主模型必须同时满足：

1. 自身所有硬门禁和 P1 通过。
2. 在预注册指标上达到 `minimum_practical_improvement`，或修复主模型的 Critical 缺陷。
3. 改进在多 seed、重采样或敏感性测试下保持稳定。
4. 新增数据、假设、参数、依赖和计算成本没有超过 `ProblemSpec` 的限制。

如果性能差异落在不确定区间内，保留更简单的主模型。最终最佳模型是“通过门禁后有可验证净增益的模型”，不是目标函数数值最好或论文最多的模型。`ModelSelectionDecision` 与 `AlgorithmSelectionDecision` 必须记录每个拒绝原因、证据和并列消解过程。

`minimum_practical_improvement` 必须在查看挑战者结果前冻结，来源依次为题目阈值、业务/物理分辨率、观测噪声或用户偏好。若都无法定义，挑战者不能自动替换主模型，只能报告“结果不可判定/近似并列”。

完整选择决策图见 `assets/model-algorithm-selection.mmd` 及其导出的 SVG/PNG。

## v1.0 Stable 算法集合

首个完成版本实现不少于 15 个 stable 插件：

| 域 | 插件 |
|---|---|
| 精确优化 | Linear Programming、Mixed-Integer Linear Programming、连续非线性优化 |
| 图论 | Dijkstra Shortest Path、Max Flow |
| 综合评价 | AHP、Entropy Weight、TOPSIS |
| 预测 | Linear Regression、Ridge Regression、ARIMA |
| 统计/ML | PCA、Random Forest |
| 机理/仿真 | ODE Solver、Monte Carlo |

每个插件必须：

- 使用统一契约。
- 声明依赖和能力。
- 提供一个已知答案或标准 benchmark。
- 提供至少一个数学不变量或 property test。
- 对错误输入给出定义明确的 `FAIL` 或 `BLOCKED`。

v1.0 的最低验收 oracle 和 property 固定如下；所有 fixture 离线可用，外部 benchmark 只作附加验证，不能成为 CI 的网络依赖：

| 插件 | 最低 oracle / benchmark | 必验 property |
|---|---|---|
| Linear Programming | 二变量解析最优解与独立顶点枚举 | 原始可行、目标一致、弱对偶不被违反 |
| Mixed-Integer Linear Programming | 小型 0-1 knapsack 全枚举 | 整数性、约束满足、目标不劣于所有枚举可行解 |
| 连续非线性优化 | 有界凸二次函数解析解；Rosenbrock 仅作 benchmark | 边界满足、有限结果、凸例达到容差内全局解 |
| Dijkstra Shortest Path | 手工图并由 Floyd-Warshall 独立核对 | 路径连通、距离和一致、非负边条件受检 |
| Max Flow | 小网络手算并验证 max-flow=min-cut | 容量约束、源汇外流守恒、流值一致 |
| AHP | 完全一致互反矩阵的已知权重 | 权重非负和为 1、互反性、CR 对一致矩阵为 0 |
| Entropy Weight | 含常量列和差异列的手算 fixture | 权重非负和为 1、常量列处理确定、尺度约定一致 |
| TOPSIS | 单调合成样本手算排名 | 得分位于 [0,1]、收益/成本方向正确、无 NaN |
| Linear Regression | 无噪声合成数据的已知系数 | 维度一致、残差近零、预测不泄漏目标 |
| Ridge Regression | 正交设计的闭式 ridge 解 | `alpha>0` 时系数收缩、截距规则明确、结果有限 |
| ARIMA | 固定 seed 的 AR(1) 递推预测 fixture | 时间顺序无泄漏、预测长度正确、重复运行一致 |
| PCA | 对角协方差矩阵的已知特征值/方向 | 分量正交、解释方差非增、方差比和不超过 1 |
| Random Forest | 固定 seed 的简单可分数据与独立指标计算 | 同 seed 完全复现、输出形状/概率合法、训练测试隔离 |
| ODE Solver | `dy/dt=ky` 的解析指数解 | 时间单调、误差在容差内、事件/边界行为确定 |
| Monte Carlo | 已知积分或 Bernoulli 均值的解析期望 | 同 seed 复现、置信区间合法、样本增大时误差统计性收敛且测试不脆弱 |

NSGA-II 与 CVaR 保留为 P1 修复对象。必须先修复上游已知错误并通过 ZDT/独立 LP oracle，之后才能从 `experimental` 晋级 `stable`。

## 数据流与阶段门禁

```text
题目 / 附件
  → Intake：术语、歧义与未知清单
  → E0 领域理解检索
      → DomainContext
      → 变量字典
      → 机制关系图
      → 业务规则表
  → 领域证据支持的问题拆解和 taxonomy
  → 数据审计与可测量性检查
  → ProblemSpec / ModelContract
  → E1 方法与验证检索
      VERIFIED/PARTIAL → 提取适用条件、参数与验证方法
      UNVERIFIED → 显式标记后继续
  → ModelRequirements 与候选模型生成
  → 七项 ModelAdequacyGate
      FAIL → 拒绝候选并记录原因
      UNKNOWN → 解决歧义或仅作为 experimental challenger
      PASS → 最小充分模型筛选
  → 主模型 + 最多一个 GapClosure challenger
  → Algorithm Registry 与插件 IO/依赖/权限匹配
  → P1 最小结构等价实例
      FAIL → 回退合同或候选选择
      PASS → 全量求解
  → Validation Pipeline
      FAIL/BLOCKED → 保留证据并回退
      WARN/PASS → 在相同 EvaluationProtocol 下进入 Model Comparator
  → ChallengerPromotionRule
      未达到最小实用改进 → 保留简单主模型
      通过全部条件 → 挑战者晋级
  → SolveResult + Artifacts + Manifest
  → 验证状态允许时生成可选 PaperHandoff
  → 用户要求后交给 math-modeling-paper
```

Skill 根目录和题目附件只读；产物只写入 `PROJECT_ROOT/results/<run_id>/`。门禁失败不能由文字解释覆盖。用户可以记录接受风险，但 Critical `FAIL/BLOCKED` 的机器状态不会因此被改写为 `PASS`。

完整证据数据流图见 `assets/domain-evidence-pipeline.mmd` 及其导出的 SVG。

## 验证体系

单项检查包含 `severity=critical|major|minor` 与以下状态：

- `PASS`：检查已执行且满足阈值。
- `WARN`：结果可用但存在非 Critical 风险，必须展示并进入比较惩罚。
- `FAIL`：检查已执行且违反要求。
- `BLOCKED`：依赖、输入或先决条件不足，要求的检查无法执行。
- `SKIPPED`：仅允许用于 `ProblemSpec` 明确标记为不适用的可选检查，并记录理由。

总状态确定性聚合：存在 Critical `FAIL` 则为 `FAIL`；不存在 Critical `FAIL` 但存在必需检查 `BLOCKED` 则为 `BLOCKED`；其余存在任意 `WARN` 或 Major/Minor `FAIL` 则为 `WARN`；全部必需检查通过才为 `PASS`。风险接受记录只能附加 `accepted_risk`、接受人/时间和理由，不能改变原始状态。只有总状态 `PASS/WARN` 的结果可进入 Comparator；`WARN` 必须在最终选择和论文交接中可见。

五类测试：

1. Unit：公式和局部实现。
2. Oracle：与手工解析解、独立 formulation 或已知答案一致。
3. Property：概率和、流守恒、边界、排序、可行性等数学不变量。
4. Benchmark：标准数据或标准问题上的合理表现。
5. Regression：固定 seed 和容差下的关键指标稳定。

运行时验证包含：

- 数据类型、维度、缺失、异常、单位和泄漏检查。
- 变量定义、单位、合理范围、测量方法和数据字段的一致性检查。
- 机制关系的尺度、边界条件、方向性和可辨识性检查。
- 业务规则的适用时间、地区、版本以及硬/软约束映射检查。
- 约束可行性和结果有限性。
- 条件数、尺度、收敛与边界检查。
- 预测任务的时间顺序或交叉验证。
- 随机算法的多 seed 与稳定性检查。
- baseline、替代模型和灵敏度比较。
- DOI/题名去重、证据适用条件和参数来源核验。
- 所有候选使用同一 `EvaluationProtocol`；指标方向、数据切分、seed 集合、容差和资源上限必须在运行前冻结。

证据管线测试包含：

- `search_request` 计量、初始 5 次/hard cap 8 次、扩容授权与覆盖式提前停止规则。
- DOI 优先、题名回退的确定性去重。
- 多来源记录合并且不丢失冲突信息。
- `VERIFIED`、`PARTIAL`、`UNVERIFIED` 状态转换。
- 同一变量的多种定义、单位或测量口径冲突检测。
- 相关关系不会被自动升级为因果机制或物理定律。
- 过期或区域不匹配的业务规则不能进入硬约束。
- 缺乏数据可得性或可辨识性的变量不会被自动冻结进模型。
- 离线、超时、空结果和只有本地文献时的回退。
- 候选排序不会因论文数量多而覆盖结构或适用条件冲突。
- manifest 能重放检索式、来源标识、访问日期和证据映射。
- provider 结果顺序改变时，快照重放仍产生同一 evidence revision；`--refresh-evidence` 生成新 revision 而不覆盖旧快照。

模型/算法选择行为测试至少覆盖：

- 静态非负最短路选择 Dijkstra，拒绝无明确缺口的动态蚁群论文模型。
- 连续线性目标与约束选择 LP，不因“创新性”改用 GA/PSO。
- 负边权使 Dijkstra 在结构门禁失败，并路由到支持负边的候选或 `BLOCKED`。
- 非平稳或存在明显结构突变的序列不会在假设未知时自动冻结 ARIMA。
- 复杂挑战者只有达到预注册最小实用改进才晋级；差异落在不确定区间时保留简单模型。
- 论文篇数增加不能越过 Coverage/Assumption/Data 等硬门禁。

这些场景先作为无新 Skill 的行为基线，再用于新 `SKILL.md` 的 fresh-context 前向测试；同时把可机械检查的门禁转成 `tests/behavior/` 中的确定性 selector fixture，避免只测输出措辞。

## 复现与版本

分别记录：

- Skill 版本。
- API 版本。
- Schema 版本。
- 算法名称和算法版本。
- 输入 SHA-256。
- seed 和参数。
- Python、平台和依赖版本。
- 验证状态。
- 唯一复现命令。
- `ModelRequirements`、两级 SelectionDecision、EvaluationProtocol 和所有被拒候选理由。
- 文献检索式、预算计数、检索源/版本、规范化响应快照 hash、evidence revision、记录标识、访问日期、claim 级核验状态和本地文献哈希。
- 领域术语版本、变量字典、机制关系、业务规则及其证据链接和冲突状态。

旧算法版本不能被同号覆盖。算法回归失败时禁止晋级；稳定别名继续指向上一个通过版本。

单次运行的固定产物布局为：

```text
PROJECT_ROOT/results/<run_id>/
├── inputs/              # 输入清单、schema、hash；大文件只记录只读引用
├── domain/              # DomainContext、变量、机制和规则
├── evidence/            # 查询日志、provider 快照、claims 和 conflicts
├── selection/           # Model/Algorithm SelectionDecision 与 EvaluationProtocol
├── solve/               # 原始解、日志和中间 checkpoint
├── validation/          # 检查明细、比较和敏感性结果
├── figures/             # 可选图表
├── paper-handoff/       # 仅用户要求且状态允许时生成
└── manifest.json
```

## 插件加载与能力安全

内置插件由版本化 allowlist 加载。个人扩展必须来自用户显式配置的目录或 entry point，并具有通过 schema 校验的 `plugin.yaml`；loader 不递归扫描整个 `PROJECT_ROOT`，不 import 未登记的 `.py` 文件。插件 ID 与版本组合唯一，同 ID/版本内容 hash 不同则拒绝加载。

插件 manifest 至少声明：

```yaml
plugin_id: graph.dijkstra
algorithm_version: 1.0.0
api_version: 1
schema_version: 1
status: stable
entrypoint: mathmodel.algorithms.graph.dijkstra:DijkstraPlugin
dependencies: [core, graph]
permissions:
  filesystem_read: [declared_inputs]
  filesystem_write: [run_artifacts]
  network: false
  subprocess: false
  secrets: false
```

默认能力模型：

- 允许读取已声明的题目附件、输入数据和 Skill 内只读 reference。
- 只允许写当前 `PROJECT_ROOT/results/<run_id>/`；所有路径先 `resolve`，验证位于允许根目录内，再打开文件。
- 算法插件默认禁止网络、任意 shell、动态 `eval/exec`、读取 secrets 和动态安装依赖。
- 证据 provider 是独立受控组件，可以按检索预算访问网络，但不能写算法目录或读取 secrets。
- 必须调用外部 solver 时，插件声明 `subprocess=true` 和固定 executable allowlist；参数使用数组传递，不拼接 shell 字符串。
- `doctor.py` 只报告依赖和建议安装命令，绝不执行 `pip/conda/npm` 安装。
- 权限请求超出 manifest 时返回 `BLOCKED`；用户授权只对指定 run 和能力生效，不永久扩大其他插件权限。

## CLI、依赖与运行接口

唯一公开脚本入口：

```text
python scripts/doctor.py --profile <core|optimization|forecasting|ml|all>
python scripts/run_model.py --project-root <absolute-path> --problem <problem.yaml> [--data <data.yaml>] --mode <analyze|solve|review|evidence> [--output results/<run_id>] [--refresh-evidence]
```

规则：

- `run_model.py` 从自身已解析的 `SKILL_ROOT/src` 启动包，不依赖当前工作目录，也不修改全局 `PYTHONPATH`。
- `--project-root` 必须是显式绝对路径；`--output` 解析后必须仍位于该根目录。未给 run id 时使用 UTC 时间戳加输入 hash 前缀，避免覆盖。
- `pyproject.toml` 定义 `core`、`optimization`、`forecasting`、`ml`、`graph`、`dev` 可选依赖组；`requirements.lock` 固定已验收环境的解析版本。
- 启动时只检查当前候选需要的依赖组。缺失依赖返回 `BLOCKED` 和精确包列表，不自动安装，也不因环境缺包静默改变数学模型。
- 测试通过 `pyproject.toml` 将 `src` 加入测试导入路径；正式 runner 使用经过路径验证的本地包入口。直接运行零散上游模板不属于公开 API。
- CLI 成功退出码为 0；输入/schema 错误为 2；依赖/权限 `BLOCKED` 为 3；求解或 Critical 验证失败为 4；意外内部错误为 5。无论退出码如何，能建立 run 目录时都保存诊断和 manifest。

`PaperHandoff` 只在用户要求时生成。它引用 manifest 中已经冻结的题意、方程、变量、参数、结果、图表、证据、验证状态和限制；论文 Skill 可以改变叙述和排版，但不能覆盖核心 artifacts。若总状态为 `WARN`，handoff 必须带醒目的 warnings；`FAIL/BLOCKED` 默认拒绝交接，只能生成明确标为“诊断草稿、不得作为最终结果”的包。

## 上游资产迁移映射

两个上游快照始终只读。以下映射在实现前冻结，避免实现人员临时决定复制范围：

| 来源 | 目标 | 迁移动作 |
|---|---|---|
| XiaoMa 根 `SKILL.md`、`references/roles/建模手/` | `SKILL.md`、`workflow.md`、`model-contract.md` | 抽取模型合同、阶段门禁和回退规则；压缩入口，细节进入 reference |
| XiaoMa `references/roles/编程手/` 与 `check_env.py`、`repro_manifest.py` 思想 | `data-and-solver-engineering.md`、runtime、doctor | 转为插件级依赖、数值门禁和统一 manifest；旧脚本不作为公开运行入口 |
| XiaoMa `references/算法索引.md` 与七类算法说明 | capability tags、`algorithm-notes/` | 合并为二级算法知识，不保留平行模型路由 |
| XiaoMa `tools/paper_search/` | evidence providers | 审计后迁移查询、元数据核验与融合能力，改用统一 Evidence 契约和缓存 |
| XiaoMa 论文手、DOCX/PDF/LaTeX/figure/xlsx 工具、`dsh-plugin/` | 核心 Skill 不迁入 | 论文能力留给现有 paper Skill；通用文件工具按需调用现有独立 Skill |
| Lupynow `problem-decomposition.md` | `problem-decomposition.md`、taxonomy | 保留 12 类问题本质、混合问题和子问题数据流，并结构化为可测试 metadata |
| Lupynow `model-selection-matrix.md` | `model-selection.md` 加机器可读 metadata | 保留候选知识；矩阵只能生成候选，不能越过硬门禁 |
| Lupynow 8 个 Cookbook | `references/cookbooks/` | 去重后保留，按 taxonomy 渐进加载 |
| Lupynow 12 个 Playbook | `references/playbooks/` | 作为案例和反例，不参与强制路由 |
| Lupynow 29 个 Python/MATLAB 模板 | algorithm notes、experimental 或重写后的 plugin | 逐个审计；模板不直接晋级 stable，MATLAB 仅作知识/对照资产，v1.0 stable 以统一 Python API 为准 |
| Lupynow `paper-bridge.md` | `handoffs.md` | 重写为结构化 `PaperHandoff`，不合并论文写作链 |
| Lupynow `math-modeling-paper/` | 保持现有独立 Skill | 不复制到 core，不产生第二套论文入口 |

## 错误处理

- 输入不完整：`BLOCKED`，列出缺少字段，不猜测硬约束。
- 模型硬门禁为 `UNKNOWN`：列出未决假设/变量/规则；不能自动成为主模型，可在用户接受后仅作为 experimental challenger。
- 经典模型已完整覆盖：拒绝没有 `GapClosureClaim` 的复杂候选，不以“更创新”作为例外。
- 无候选插件：回退知识层给出人工方案，不虚构 Registry 命中。
- 插件 schema 不兼容或 `supports=UNKNOWN`：拒绝自动运行并保存逐项诊断。
- 插件 ID/版本相同但内容 hash 不同：拒绝加载，要求提升版本或恢复已登记内容。
- 插件越权访问文件、网络、subprocess 或 secrets：立即 `BLOCKED`，保留安全事件，不尝试放宽权限。
- 检索源不可用：使用其他已配置源或本地文献；都不可用时标记 `UNVERIFIED` 后继续，不编造结果。
- 领域证据冲突：同时保留冲突主张、来源和适用条件，在解析前不冻结相关变量或规则。
- 变量不可观测或不可辨识：降级为 latent、proxy 或删除候选，并记录对模型能力的影响。
- 业务规则版本不明：不得生成硬约束；先请求用户确认或核对当前官方来源。
- DOI/题名冲突：保留冲突记录并标记 `PARTIAL`，在核验前不引用争议字段。
- 文献适用条件不匹配：作为反对证据进入候选硬门禁或 Pareto 判定，不把“检索到论文”解释为“模型适合本题”。
- 依赖缺失：`BLOCKED` 并列出缺失依赖，不自动安装。
- 最小实例失败：禁止全量计算，返回模型合同或算法实现。
- 数学规划不可行：诊断冲突约束、最小松弛或无界原因。
- 超时：报告 incumbent、bound、gap 或当前诊断，不把超时表述为无解。
- 验证失败：保存原始结果与失败证据，不把目标函数更优等同于模型合格。
- 验证警告：总状态保持 `WARN`，允许比较但施加显式风险标记；风险接受不改写原始检查结果。
- 论文交接时为 `FAIL/BLOCKED`：拒绝生成可作为最终结论的 handoff，只能按用户明确要求生成诊断草稿。

## 实施顺序

1. 为经典充分模型、复杂论文模型、错误假设、离线检索和门禁绕过建立行为失败基线；先写 selector/contract/schema/status/security 的失败测试。
2. 创建第三个 Skill 目录、最小 `SKILL.md`、reference 路由和四层包骨架；此时不搬运全部知识资料。
3. 实现 `ProblemSpec`、`ModelRequirements`、`ModelCandidate`、IOContract、结果、验证和 handoff schema。
4. 实现 ModelSelector 的七项硬门禁、最小充分模型、GapClosure challenger 和确定性 SelectionDecision。
5. 实现插件 metadata schema、allowlist loader、Registry、AlgorithmSelector、依赖解析和 capability enforcement。
6. 按冻结的迁移表合并、去重并重路由两仓库知识资料；每类迁移建立 inventory 与引用测试。
7. 实现 E0 领域证据提取、领域上下文、变量/机制/业务规则契约与冲突解析。
8. 实现 E1 方法证据、provider 预算计数、去重、claim 级核验、响应快照、revision 和候选证据映射。
9. 实现 Validation Runtime、状态聚合、EvaluationProtocol、Comparator 和挑战者晋级规则。
10. 逐个以 RED-GREEN-REFACTOR 实现 15 个 stable 插件，并完成规定 oracle/property/benchmark。
11. 修复并验证 NSGA-II、CVaR；仍不满足门槛时保持 experimental。
12. 实现 doctor、runner、固定 artifact 布局、退出码和 reproducibility manifest。
13. 实现 `PaperHandoff` 和三个 Skill 的路由/交接回归测试。
14. 运行 Skill 前向行为测试、证据、算法、schema、安全、CLI、集成和现有工作区回归测试。
15. 只有全部验收通过后才禁用旧 solver，并验证新 Skill 可发现、旧版可恢复且无入口冲突。

## v1.0 验收门槛

- 触发测试能区分 core、contest orchestrator 和 paper-only 请求；四种 OperatingMode 路由正确率 100%。
- `SKILL.md` 初始加载不批量读取全部 Cookbook/Playbook/algorithm notes，所有 reference 均有明确按需入口。
- Stable 算法插件不少于 15。
- stable 插件 unit test 覆盖率 100%。
- stable 插件 oracle/property test 覆盖率 100%。
- 本设计规定的 15 个最低 oracle/property fixture 全部通过，CI 不依赖网络下载 benchmark。
- 未测试模板进入 stable 的数量为 0。
- 固定 seed 的随机算法可复现率 100%。
- 算法依赖 metadata 完整率 100%。
- 算法 input/output/config schema 覆盖率 100%；schema 不匹配在调用 solver 前被拒绝。
- 插件 allowlist、ID/版本/hash 冲突、路径 containment、网络/subprocess/secrets 越权测试通过率 100%。
- 七项 ModelAdequacyGate、最小充分模型、GapClosure 准入、复杂度支配和挑战者晋级行为 fixture 通过率 100%。
- Dijkstra/蚁群、LP/启发式、负边最短路、非平稳 ARIMA 等 fresh-context 场景不发生复杂度或论文数量越权。
- 相同输入、Registry 和 evidence snapshot 产生字节稳定的 SelectionDecision；并列时由插件 id/version 确定消解。
- 所有进入最终结论的文献记录均具有稳定标识和非 `UNVERIFIED` 状态。
- 所有进入最终结论的关键 claim 均具有可定位证据和非 `UNVERIFIED` 状态；record 元数据通过不能替代 claim 核验。
- 检索预算计数、hard cap、扩容授权、去重、离线回退、快照重放、refresh revision 和证据映射测试通过率 100%。
- 进入 `ProblemSpec` 的变量均具有定义、角色、单位/无量纲声明、可测量性状态和证据链接。
- 转成硬约束的业务规则均具有适用时间、地区/组织、版本和已核验来源。
- 机制关系均区分相关、经验、因果、物理定律或业务约束，并记录成立条件。
- manifest 对检索式、预算、provider 版本、响应 hash、evidence revision、访问日期、claim 核验状态和本地文献哈希的记录完整率 100%。
- ValidationReport 状态聚合、风险接受不改写原始状态、WARN 可见和 Critical FAIL/BLOCKED 禁止比较的测试通过率 100%。
- CLI 路径无关启动、输出 containment、退出码、缺依赖不安装和失败仍保存诊断的集成测试通过率 100%。
- `PaperHandoff` 不修改核心 artifacts；WARN 被保留，FAIL/BLOCKED 不生成可作为最终结论的 handoff。
- 上游迁移 inventory 覆盖映射表全部类别，未列入映射的文件不会意外进入核心 Skill。
- Critical 测试失败数为 0。
- `SKILL.md` 与 `agents/openai.yaml` 通过 Skill validator。
- 新增 Python 代码编译通过，mypy 或 pyright 对公开契约零错误，测试分支覆盖率目标不低于 85%。
- 两个上游源码快照保持未修改。
- 旧 solver 已移出自动发现目录且可恢复。
- 现有 `math-modeling-paper` 与 `mathmodel-skill` 回归测试通过。

## 明确不做

- 不发布、不推送上游、不创建 PR。
- 不处理许可证、来源声明或 clean-room 重写。
- 不把论文生成链合并进核心 Skill。
- 不自动安装第三方 Python/MATLAB 依赖。
- 不把 Playbook 或模型矩阵当成唯一决策规则。
