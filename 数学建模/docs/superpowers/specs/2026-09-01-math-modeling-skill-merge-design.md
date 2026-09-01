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

## 四层架构

### 1. Reasoning Layer：问题理解与模型设计

职责：

- 读取题目与附件，建立数据结构指纹。
- 将子问题映射到 Lupynow 的 12 类问题本质，允许混合类型与级联数据流。
- 形成 `ProblemSpec` 和 `ModelContract`，明确目标、约束、输入输出、假设、指标、风险和回退条件。
- 从问题结构生成中英文检索式，检索相似问题、候选算法、参数依据和验证方法，形成结构化 `EvidenceRecord`。
- 从知识层产生多个候选，但进入计算阶段时最多保留一个主模型和一个结构独立的对照模型。
- 使用数据结构、约束、文献适用性、验证可行性、依赖和复杂度评分候选，不把场景矩阵或论文数量当成模型名称查表器。

### 2. Algorithm Layer：可执行算法插件

职责：

- 所有算法通过统一 `AlgorithmPlugin` 协议注册。
- 插件声明名称、算法版本、API 版本、状态、能力标签、依赖、约束支持和随机性。
- `stable` 算法必须拥有 unit test 和数学 oracle/property test。
- 未审计模板只能标记为 `experimental` 或保留为知识示例。
- 第三方扩展通过 Registry 注册，不修改主 `SKILL.md`。

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
│   ├── problem-decomposition.md
│   ├── model-contract.md
│   ├── model-selection.md
│   ├── literature-evidence.md
│   ├── data-and-solver-engineering.md
│   ├── validation-runtime.md
│   ├── reproducibility.md
│   ├── cookbooks/
│   ├── playbooks/
│   └── algorithm-notes/
├── src/
│   └── mathmodel/
│       ├── contracts/
│       │   ├── problem.py
│       │   ├── data.py
│       │   ├── result.py
│       │   └── validation.py
│       ├── reasoning/
│       │   ├── taxonomy.py
│       │   ├── selector.py
│       │   └── evidence_mapper.py
│       ├── evidence/
│       │   ├── records.py
│       │   ├── providers.py
│       │   ├── retrieval.py
│       │   ├── deduplication.py
│       │   └── cache.py
│       ├── algorithms/
│       │   ├── base.py
│       │   ├── registry.py
│       │   ├── optimization/
│       │   ├── evaluation/
│       │   ├── forecasting/
│       │   ├── statistics/
│       │   ├── graph/
│       │   ├── mechanistic/
│       │   └── simulation/
│       ├── validation/
│       │   ├── invariants.py
│       │   ├── numerical.py
│       │   ├── statistical.py
│       │   ├── constraints.py
│       │   └── comparison.py
│       └── runtime/
│           ├── executor.py
│           ├── dependencies.py
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
│   └── fixtures/
└── pyproject.toml
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

- `ProblemSpec`：题目标识、问题类型、目标、约束、能力、指标和假设。
- `DataBundle`：特征、目标、原始数据和数据元信息。
- `SolveConfig`：seed、timeout、tolerance、max_iterations 和算法参数。
- `SolveResult`：解、目标值、指标、诊断、状态和 artifacts。
- `ValidationCheck`：检查名称、状态、观测值、阈值和证据。
- `ValidationReport`：`PASS`、`FAIL` 或 `BLOCKED`，并给出回退阶段。
- `AlgorithmMetadata`：名称、版本、状态、能力、依赖和支持范围。
- `AlgorithmPlugin`：`supports`、`solve`、`validate` 协议。
- `EvidenceRecord`：题名、作者、年份、期刊、DOI/稳定标识、检索源、使用模型、适用条件、参数依据、验证方法、局限和访问日期。
- `EvidenceBundle`：检索式、检索预算、去重结果、核验状态以及与子问题和候选算法的映射。

## Literature Evidence Pipeline

论文检索位于“问题拆解”之后、“候选模型定榜”之前：

1. 从 `ProblemSpec` 为每个子问题生成中文和英文检索式。
2. 默认最多执行 5 次外部检索；找到 5–8 篇高度相关且来源可核验的论文后停止。
3. 优先使用 OpenAlex，并在可用时用 Semantic Scholar、出版方页面或第二检索源交叉核验题名、年份和 DOI。
4. 支持读取用户已下载的本地 PDF/Markdown 文献，纳入同一 `EvidenceRecord` 契约。
5. 按 DOI 优先、规范化题名其次去重；同一论文的多个来源合并为一个记录。
6. 提取“论文解决的问题、实际使用的模型、适用条件、参数依据、验证方法、量化结果和局限”，禁止仅凭摘要关键词推荐模型。
7. 将证据映射到子问题、模型合同和候选算法，输出支持、反对或条件性证据。

核验状态：

- `VERIFIED`：题名/年份/DOI 或稳定标识已由权威页面或两个独立来源核对。
- `PARTIAL`：论文存在已确认，但方法细节、参数或全文尚未核验。
- `UNVERIFIED`：仅有搜索片段或用户未要求检索；不得作为确定性事实进入最终结论。

检索是默认步骤，但不是硬阻塞。用户明确跳过、网络不可用或时间受限时可以继续模型设计，同时在候选表、验证报告和 manifest 中保留 `evidence_status=UNVERIFIED`。不得伪造 DOI、期刊级别、参数来源或论文结论。

## Registry 与模型选择

Registry 依据能力标签而不是文件名匹配算法。Selector 对候选计算：

```text
结构匹配
+ 数据匹配
+ 约束匹配
+ 文献适用性与证据质量
+ 可验证性
+ 依赖可用性
- 复杂度风险
```

规则：

- 知识层可以返回多个候选。
- 计算阶段最多选择一个主模型和一个结构独立的对照模型。
- `experimental` 不得在没有用户明确选择的情况下胜出。
- `stable` 但依赖缺失的插件返回 `BLOCKED`，不得静默替换算法。
- 最终最佳模型是“通过预定义门禁后的综合最优”，不是目标函数数值最优。
- 文献数量不直接决定排序；一篇适用条件匹配的强证据可以高于多篇场景不匹配的弱证据。
- 文献与本题数据结构或约束冲突时，记录反对证据并降低候选得分，不得只保留支持性论文。

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

NSGA-II 与 CVaR 保留为 P1 修复对象。必须先修复上游已知错误并通过 ZDT/独立 LP oracle，之后才能从 `experimental` 晋级 `stable`。

## 数据流与阶段门禁

```text
题目 / 附件
  → Intake 与数据审计
  → 问题拆解和 taxonomy
  → ProblemSpec / ModelContract
  → Literature Evidence Pipeline
      VERIFIED/PARTIAL → 提取适用条件、参数与验证方法
      UNVERIFIED → 显式标记后继续
  → 候选生成与 Registry 匹配
  → 主模型 + 独立对照模型
  → P1 最小结构等价实例
      FAIL → 回退合同或候选选择
      PASS → 全量求解
  → Validation Pipeline
      FAIL → 保留证据并回退
      PASS → Model Comparator
  → SolveResult + Artifacts + Manifest
  → 可选交给 math-modeling-paper
```

Skill 根目录和题目附件只读；产物只写入 `PROJECT_ROOT`。门禁失败不能由文字解释覆盖。

## 验证体系

五类测试：

1. Unit：公式和局部实现。
2. Oracle：与手工解析解、独立 formulation 或已知答案一致。
3. Property：概率和、流守恒、边界、排序、可行性等数学不变量。
4. Benchmark：标准数据或标准问题上的合理表现。
5. Regression：固定 seed 和容差下的关键指标稳定。

运行时验证包含：

- 数据类型、维度、缺失、异常、单位和泄漏检查。
- 约束可行性和结果有限性。
- 条件数、尺度、收敛与边界检查。
- 预测任务的时间顺序或交叉验证。
- 随机算法的多 seed 与稳定性检查。
- baseline、替代模型和灵敏度比较。
- DOI/题名去重、证据适用条件和参数来源核验。

证据管线测试包含：

- 5 次检索预算与 5–8 篇提前停止规则。
- DOI 优先、题名回退的确定性去重。
- 多来源记录合并且不丢失冲突信息。
- `VERIFIED`、`PARTIAL`、`UNVERIFIED` 状态转换。
- 离线、超时、空结果和只有本地文献时的回退。
- 候选排序不会因论文数量多而覆盖结构或适用条件冲突。
- manifest 能重放检索式、来源标识、访问日期和证据映射。

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
- 文献检索式、检索源、记录标识、访问日期、核验状态和本地文献哈希。

旧算法版本不能被同号覆盖。算法回归失败时禁止晋级；稳定别名继续指向上一个通过版本。

## 错误处理

- 输入不完整：`BLOCKED`，列出缺少字段，不猜测硬约束。
- 无候选插件：回退知识层给出人工方案，不虚构 Registry 命中。
- 检索源不可用：使用其他已配置源或本地文献；都不可用时标记 `UNVERIFIED` 后继续，不编造结果。
- DOI/题名冲突：保留冲突记录并标记 `PARTIAL`，在核验前不引用争议字段。
- 文献适用条件不匹配：作为反对证据进入候选评分，不把“检索到论文”解释为“模型适合本题”。
- 依赖缺失：`BLOCKED` 并列出缺失依赖，不自动安装。
- 最小实例失败：禁止全量计算，返回模型合同或算法实现。
- 数学规划不可行：诊断冲突约束、最小松弛或无界原因。
- 超时：报告 incumbent、bound、gap 或当前诊断，不把超时表述为无解。
- 验证失败：保存原始结果与失败证据，不把目标函数更优等同于模型合格。

## 实施顺序

1. 建立契约测试和失败基线。
2. 创建第三个 Skill 目录与四层骨架。
3. 合并、去重并重路由两仓库知识资料。
4. 实现 `EvidenceRecord`、检索 providers、去重、核验、缓存和候选证据映射。
5. 实现 contracts、Registry、Selector 和 Validation Runtime。
6. 逐个以 RED-GREEN-REFACTOR 实现 15 个 stable 插件。
7. 修复并验证 NSGA-II、CVaR，仍不满足门槛时保持 experimental。
8. 实现 doctor、runner 和 reproducibility manifest。
9. 运行 Skill、证据管线、算法、集成和现有工作区回归测试。
10. 禁用旧 solver，验证新 Skill 能被发现且无入口冲突。

## v1.0 验收门槛

- Stable 算法插件不少于 15。
- stable 插件 unit test 覆盖率 100%。
- stable 插件 oracle/property test 覆盖率 100%。
- 未测试模板进入 stable 的数量为 0。
- 固定 seed 的随机算法可复现率 100%。
- 算法依赖 metadata 完整率 100%。
- 算法输入输出统一契约覆盖率 100%。
- 所有进入最终结论的文献记录均具有稳定标识和非 `UNVERIFIED` 状态。
- 检索预算、去重、离线回退和证据映射测试通过率 100%。
- manifest 对检索式、来源、访问日期、核验状态和本地文献哈希的记录完整率 100%。
- Critical 测试失败数为 0。
- `SKILL.md` 与 `agents/openai.yaml` 通过 Skill validator。
- 新增 Python 代码编译通过，测试分支覆盖率目标不低于 85%。
- 两个上游源码快照保持未修改。
- 旧 solver 已移出自动发现目录且可恢复。
- 现有 `math-modeling-paper` 与 `mathmodel-skill` 回归测试通过。

## 明确不做

- 不发布、不推送上游、不创建 PR。
- 不处理许可证、来源声明或 clean-room 重写。
- 不把论文生成链合并进核心 Skill。
- 不自动安装第三方 Python/MATLAB 依赖。
- 不把 Playbook 或模型矩阵当成唯一决策规则。
