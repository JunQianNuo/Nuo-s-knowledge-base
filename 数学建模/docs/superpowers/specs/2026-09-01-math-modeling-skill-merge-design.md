# 数学建模 Skill 合并设计

日期：2026-09-01

## 目标

把 `XiaoMaColtAI/math-modeling-skill` 与 `Lupynow/math-modeling-skills` 中的解题能力合并进本地现有的 `math-modeling-solver`，供个人工作区使用。合并后的 Skill 聚焦“读题、拆题、模型选择、算法实现、验证、比较和复现”，论文写作继续由现有 `math-modeling-paper` 独立承担。

本次不建设可发布仓库，不处理开源许可证、第三方声明、社区治理或发布兼容性。两个下载仓库保留为只读上游快照，活动 Skill 不依赖其运行时路径。

## 选定方案

直接升级 `.agents/skills/math-modeling-solver`，不新建会与它争抢触发词的第三个建模 Skill。

选择该方案的原因：

- 当前活动目录已经包含 Lupynow 的问题分类、模型矩阵、Cookbook、Playbook 和代码模板，是最小迁移基线。
- XiaoMa 的主要增量是模型合同、角色化工程流程、环境检查、最小可运行切片、阶段门禁和复现约束，适合作为控制层合并进现有 solver。
- 保留 `math-modeling-paper` 为独立写作 Skill，避免主入口继续膨胀，也避免与本次“建模与算法设计”目标混杂。

## 分层架构

### 1. Skill 路由层

根入口统一为大写 `SKILL.md`，并提供三种模式：

- 全流程：题目接收 → 数据审计 → 问题合同 → 候选模型 → 最小实例 → 全量求解 → 验证比较 → 复现交付。
- 局部协助：直接进入模型选择、算法实现、验证或结果诊断，仅补齐当前结论所必需的前置检查。
- 方案审查：审查用户已有模型、代码与结果，不无理由推翻已有方案。

入口只保留路由、硬约束、阶段产物和失败回退。详细规则按需进入 `references/`，避免一次加载整个知识库。

### 2. Reasoning / Knowledge 层

以 Lupynow 内容为主体：

- `problem-decomposition.md`：12 类问题本质与混合问题拆解。
- `model-selection-matrix.md`：候选模型生成和场景判断。
- 8 本 Cookbook：模型和算法知识。
- Playbook：仅作为案例参考，不作为强制路径。
- 29 个代码模板：保留为 `experimental/reference`，不得因脚本可运行就宣称算法可信。

吸收 XiaoMa 内容：

- 模型合同、变量/参数/约束字典和阶段交付约束。
- 数值稳定性、尺度、条件数、多初值、多随机种子、收敛与边界检查。
- `SKILL_ROOT` 只读、题目附件只读、所有结果写入 `PROJECT_ROOT`。
- 动态依赖检查、唯一复现命令和输入哈希。

两套算法索引不并行保留为两个路由器。统一使用：

`问题本质 taxonomy → required_capabilities → Algorithm Registry`。

### 3. Typed Runtime 层

在 Skill 内新增可直接调用的 Python 包：

```text
scripts/mathmodel_core/
├── contracts.py
├── registry.py
├── selector.py
├── validation.py
├── reproducibility.py
└── algorithms/
```

核心契约：

- `ProblemSpec`：题目标识、问题类型、目标、约束、能力、指标和假设。
- `DataBundle`：原始数据、特征、目标和元数据。
- `SolveConfig`：随机种子、超时、容差和最大迭代数。
- `SolveResult`：解、目标值、指标、诊断和产物。
- `ValidationReport`：状态、检查项、失败证据和建议回退阶段。
- `AlgorithmPlugin`：`supports`、`solve`、`validate` 统一协议。

首版实现两个跨领域、依赖轻且可构造数学 oracle 的 stable 插件：

- TOPSIS：代表综合评价；验证权重、归一化、贴近度范围和已知排序。
- Dijkstra shortest path：代表图论；验证路径连续性、端点、边权和、不可达状态及已知最短路。

其余上游模板全部进入 Registry 的 `experimental` 清单或仅保留为知识参考。NSGA-II、CVaR 等已知有缺陷的模板不得注册为 stable。

### 4. Validation Runtime 层

统一验证流水线包含：

1. 数据完整性与 Schema 检查。
2. 问题约束和数学不变量。
3. 数值有限性、范围和稳定性。
4. 算法专项 oracle/property 检验。
5. 多随机种子、灵敏度或 baseline 比较（适用时）。

`ValidationReport.status` 只能为 `PASS`、`FAIL` 或 `BLOCKED`。只有 `PASS` 候选可以进入最终比较；失败必须携带机器可读检查项和回退阶段，不能由文字解释覆盖。

### 5. Reproducibility 层

每次运行生成 JSON manifest，至少记录：

- Skill/API/算法版本。
- 输入文件 SHA-256。
- seed、参数、Python 和依赖版本。
- 验证状态。
- 唯一复现命令。

manifest 写入用户项目的 `results/`，不得写回 Skill 目录。

## 数据流

```text
题目与附件
  → 数据审计 + 问题拆解
  → ProblemSpec / DataBundle
  → 候选模型与能力标签
  → Registry 匹配（最多 1 个主模型 + 1 个独立对照）
  → 最小结构等价实例
  → 全量求解
  → Validation Pipeline
  → 通过验证的模型比较
  → SolveResult + manifest
  → 可选交给 math-modeling-paper
```

## 文件迁移规则

- 保留现有 Lupynow references、Cookbook、Playbook 和模板。
- 从 XiaoMa 复制建模手/编程手中与论文无关的工程规则，并重组为短小、条件化 references。
- 复用或改造 XiaoMa 的环境检查与复现脚本；输出接口适配本设计的 JSON 契约。
- 不合并论文手、DOCX、LaTeX、论文搜索以及 Office 生成工具；需要时继续调用已有独立 Skills。
- 修正根入口文件名为 `SKILL.md`，添加 `agents/openai.yaml`，并使描述只陈述触发条件。
- 保留旧 Skill 的可恢复快照；活动路径中只存在一个 `math-modeling-solver`。

## 错误处理

- 输入不完整：返回 `BLOCKED` 并列出缺少字段，不猜测硬约束。
- 无候选插件：回退知识层给出人工实现方案，不虚构 Registry 命中。
- 依赖缺失：报告缺少的 feature/package，不自动安装。
- 最小实例失败：禁止进入全量计算，回退模型合同或算法实现。
- 验证失败：保留原始结果和失败报告，禁止把目标值最优等同于模型合格。
- 超时：报告当前可行解和已有诊断；不把超时表述为无解。

## 测试与验收

### RED / GREEN 范围

实施前先编写会失败的契约测试，覆盖：

- 规范入口与必要 references 尚不存在或未路由。
- 未注册/experimental 算法不能作为 stable 选择。
- 无效 `ProblemSpec`、非有限结果和违反不变量的结果被拒绝。
- TOPSIS 与 shortest-path 的已知答案和边界 case。
- manifest 对相同输入和 seed 保持确定性。

随后实现最小代码使测试通过，再整理重复内容。

### 完成交付门槛

- `SKILL.md` 和 `agents/openai.yaml` 通过 skill validator。
- 所有新增 Python 文件通过编译。
- 所有单元、oracle、property、回归和集成测试通过。
- 两个 stable 插件均使用同一契约，并各有 oracle/property test。
- 任何未验证上游模板均未注册为 stable。
- 上游仓库快照不被修改。
- 现有 `math-modeling-paper` 和 `mathmodel-skill` 测试不因本次修改失败。

## 明确不做

- 不实现报告中的 15 个 stable 算法目标；首版先验证架构和质量门禁。
- 不合并或重写论文生成链。
- 不发布、不推送上游、不创建 PR。
- 不自动安装第三方 Python/MATLAB 依赖。
- 不把 Playbook 或模型矩阵当成唯一决策规则。
