# Math Modeling 28-Skill 重建设计基线

日期：2026-09-02  
状态：架构已由用户确认；实现待按本设计执行  
上游基线：`zhnnky329/MathModeling-skills` commit `046a6e74814c2e5fef72b5ee56305509a8635e1d`

## 1. 目标

本次重建不再以“大幅精简”为目标。首要目标是降低数学建模过程中的事实、参数、文献、模型和结果幻觉。

本地套件完整保留上游 28 个 skill 的分类、职责边界、工作流关卡、人工决策边界和证据产物。现有 `math-modeling-core` 只保留为兼容入口，不再把 28 类职责压缩进一个超大 skill。

在上游机制之上仅增加四项本地要求：

1. `related-paper-analyzer` 支持主动检索论文，而不只分析用户已下载论文。
2. 题面事实、数据观察、文献证据、数学推导、建模假设和人工决定必须分开记录。
3. 用户可读阶段成果和最终交付物必须写入 Markdown；JSON/JSONL 仅承担机器状态、数值血缘和追加式决策记录。
4. 以失败关闭为默认策略：缺少高影响事实、参数来源、人工决定或可比 baseline 时停止，不使用默认真值继续。

## 2. 不可削弱的上游机制

### 2.1 权责边界

- AI 负责机械正确性、证据整理、风险检查、代码执行和一致性检查。
- 人负责建模取舍、方法选择、结果接受、物理或业务解释、置信范围和提交授权。
- AI 可以构造选择卡，但不得生成、润色或强化用户理由。

### 2.2 工作流关卡

- `G1 PROBLEM_FRAMED`：题意解析、分类、数据清单、成功标准和必要的人工框定完成。
- `G2 METHOD_SCREENED`：主候选、可用 baseline、条件备选及风险探针完成。
- `G2.5 METHOD_CHOSEN_BY_HUMAN`：用户基于证据选定方法；此前禁止生成模型代码。
- `G3 CODE_AND_EXPERIMENT_REVIEWED`：主方法和 baseline 均执行，运行摘要和语言审查通过。
- `G4 RESULTS_JUDGED_AND_FROZEN`：用户对结果、稳定性和声明范围作出决定；提交模式冻结数值。
- `G5 PAPER_SECTION_READY`：写作者只使用解决方案包、冻结数值和已确认解释。
- `G6 FINAL_AUDIT_PASSED`：一致性、完整性、质量保证三项审查分别通过。

### 2.3 方法选择约束

- 一个 `main_candidate`。
- 一个真正完成同一任务、输出可直接比较的 `usable_baseline`。
- 至多一个带明确触发条件的 `conditional_fallback`。
- 无真实备选时不凑数。
- 不能完成真实任务的简单参考只能标记为 `diagnostic_reference`。
- 经典模型完整覆盖题意、可识别、可执行且可验证时，不因论文模型更复杂而替换它。

### 2.4 人工决定

- 每个子问题使用一个追加式 `methods/Qx/qx_decisions.jsonl`。
- 全局框定决定使用 `planning/framing_decisions.jsonl`。
- 决定必须为人类作出、非空、引用证据且无占位符。
- 修改决定时追加 `supersedes` 记录，不能覆盖历史。
- 只有引用的实质证据变化才使决定过期；格式变化不得触发过期。

### 2.5 数值与声明血缘

数值流向固定为：

```text
代码与输入 → 实验结果 → run_summary → robustness → frozen_numbers → 论文
```

- 禁止在论文中手工输入无法定位来源的数值。
- 冻结值发生变化时必须执行“解冻—修改 canonical source—重跑—重冻结—范围一致性审查”。
- 最终论文中的物理意义、业务意义、贡献和声明范围必须引用人工决定。

## 3. 28 个 skill 的完整分类与职责

### A. 调度、题意和基础契约

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 1 | `workflow-orchestrator` | 读取状态、判断 G1–G6、分类变更影响、只路由一个下一动作 | `planning/manifests/Qx.json`、阶段 Markdown 摘要 |
| 2 | `problem-parser` | 模型中立地解析目标、对象、数据、约束、输出、变量、关系和歧义 | `planning/parse/problem_parse.json`、`problem_parse.md` |
| 3 | `problem-classifier` | 按要求输出和结构确定主/次任务类型，不选择算法 | `planning/classification/problem_classification.json`、分类摘要 MD |
| 4 | `data-auditor-cleaner` | 附件映射、只读原始数据、清洗、覆盖度与方法准备度 | `workspace/data/data_report.md`、`data_profile.json` |
| 5 | `symbol-table-builder` | 维护跨问题唯一的符号、类型、定义域和单位 | `planning/symbol_table.md` |
| 6 | `model-assumptions-builder` | 维护有来源、有必要性的假设及违反影响 | `planning/model_assumptions.md` |

### B. 论文证据、方法筛选和人工判断

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 7 | `related-paper-analyzer` | 检索/读取论文，提取机制、变量、假设、方法、验证和迁移边界 | `workspace/papers/related_paper_analysis.md`、检索清单 |
| 8 | `method-selector` | 生成主方法、可用 baseline、条件备选并执行方法特定风险探针 | `qx_method_card.md`、`risk_probe_summary.json` |
| 9 | `decision-prompt-builder` | 只在真实建模判断点构造互斥选择卡及后果 | 会话选择卡；必要时 MD 决策报告 |
| 10 | `modeler-decision-logger` | 忠实追加用户原始选择和理由，不代写 | `qx_decisions.jsonl` |

### C. 实现规划、代码生成和代码审查

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 11 | `model-code-analyzer` | 将已批准数学方法转换为语言中立实现与实验契约 | `qx_code_plan.md` |
| 12 | `python-model-code-generator` | 只实现批准的 Python 主方法和 baseline 并实际运行 | `.py`、`run_summary.json`、结果文件 |
| 13 | `matlab-model-code-generator` | 只实现批准的 MATLAB/北太天元主方法和 baseline 并实际运行 | `.m`、`run_summary.json`、结果文件 |
| 14 | `code-reviewer` | 按实现语言路由审查，不重复审查 | 路由结果 |
| 15 | `python-code-reviewer` | 检查语法、输入契约、方法对齐、复现性、输出契约 | `qx_python_review.json` |
| 16 | `matlab-code-reviewer` | 在上述检查外验证 MATLAB/北太天元兼容性 | `qx_matlab_review.json` |

### D. 结果、稳健性和可视化

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 17 | `result-report-generator` | 比较主方法和 baseline，暴露异常及 fallback 触发，不替人判断 | 决策点/最终结果分析 MD |
| 18 | `robustness-checker` | 针对承重假设和声明设计敏感性、误差及稳健性检查 | `qx_robustness_summary.json`、稳健性报告 MD |
| 19 | `figure-table-planner` | 规划最少且有证据价值的诊断、比较、论文和附录图表 | `qx_figure_table_plan.md` |
| 20 | `math-figure-generator` | 从保存的数据确定性生成并渲染审查图形 | 图形源码、PNG/SVG/PDF、渲染检查 |

### E. 最终解释、写作和参考文献

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 21 | `final-method-explainer` | 从决定、公式、代码、结果和稳健性证据生成权威方法说明 | `qx_final_method_explanation.md` |
| 22 | `solution-package-builder` | 汇总写作者单一来源并在人工签字后冻结数值 | 解决方案包 MD、`frozen_numbers.json` |
| 23 | `paper-section-writer` | 只从解决方案包、冻结值和人工解释写论文段落 | `paper/sections/*.md` 或 `.tex` |
| 24 | `paper-polisher` | 润色语言、校准声明、检查符号和公式，不修饰逻辑缺口 | 润色稿、变更说明 MD |
| 25 | `reference-manager` | 核验来源、引用与 BibTeX，阻断虚构文献 | `paper/refs.bib`、`reference_audit.md` |

### F. 三层独立终审

| # | Skill | 保留职责 | 主要输出 |
|---|---|---|---|
| 26 | `consistency-auditor` | 检查跨介质数值、符号、方法、决定、文件和声明一致性 | 范围/最终一致性审查 |
| 27 | `completeness-auditor` | 检查当前 profile 所需的语义证据是否完整且未过期 | `completeness_audit.md` |
| 28 | `quality-assurance-auditor` | 在前两审通过后检查工作流、证据、方法、论文和展示质量 | `paper/qa_report.md` |

三种审查不能合并为一个“全部通过”，也不能由同一项检查互相替代。

## 4. 本地安装与发现结构

28 个 skill 作为 `.agents/skills/` 下的同级、可独立触发 skill 安装，名称与上游一致：

```text
.agents/
├── AGENTS.md                         # 共享治理策略
└── skills/
    ├── workflow-orchestrator/
    ├── problem-parser/
    ├── ...其余 26 项...
    ├── quality-assurance-auditor/
    └── math-modeling-core/           # 兼容入口，只转交 orchestrator
```

每个 skill 必须拥有自己的 `SKILL.md`，能够在不依赖旧 Python runtime/registry 的情况下说明：

- 触发条件；
- 前置条件；
- 读取的 canonical artifacts；
- 允许写入的产物；
- 停止条件；
- 人工判断边界；
- 下一个 skill；
- 验证清单。

## 5. 主动论文检索的本地增强

上游 `related-paper-analyzer` 默认只分析用户提供的论文。本地版本扩展为两个阶段，但不新增第 29 个 skill：

1. **检索阶段**：根据题意、领域机制、变量候选和子问题检索论文、权威报告、标准或官方资料。
2. **原文分析阶段**：只对可访问原文或足以核实的权威摘要提取建模信号。

每条文献信号记录：来源、支持的机制/变量/关系、适用条件、所需数据、可迁移内容、不可直接迁移内容和置信等级。

文献不得：

- 覆盖题面明确要求；
- 将其他场景参数直接代入当前问题；
- 因方法复杂或新颖而自动成为主模型；
- 在无法验证作者、标题、年份或 DOI 时进入最终引用。

## 6. 防幻觉强制契约

### 6.1 六类陈述

任何承重陈述必须属于以下之一：

- `PROBLEM_FACT`：题面明确事实；
- `DATA_OBSERVATION`：从附件计算得到；
- `LITERATURE_EVIDENCE`：可核验外部来源；
- `DERIVATION`：从已列前提推导；
- `MODELING_ASSUMPTION`：为可解性引入且记录影响；
- `HUMAN_DECISION`：用户明确选择。

来源不明的陈述标记为 `UNRESOLVED`，不能转换为模型参数、硬约束或最终结论。

### 6.2 参数来源

每个固定参数必须记录：符号、值、单位、角色、来源定位、适用范围和敏感性计划。禁止通过变量名称相似、常识或论文案例值自动赋值。

### 6.3 模型必要性

复杂模型只有在经典模型不能覆盖目标、约束、非线性机制、不确定性或验证需求时，才能成为主候选。否则复杂模型仅作为 baseline、挑战方案或条件备选。

### 6.4 结果解释

- 计算结果和解释分开记录。
- AI 不得把相关性写成因果性。
- 异常、退化、过度集中和负结果必须保留。
- 结果是否可接受、物理/业务意义和声明范围由用户决定。

## 7. Markdown 输出约束

机器状态继续使用 JSON/JSONL，以保证关卡和血缘可验证；但每个用户决策点、最终方法、最终结果、稳健性、解决方案包、论文及审查都必须有 Markdown 输出。

用户要求“分析/建模/回答”且发生文件写入时，最终回复必须给出生成的 Markdown 文件绝对路径。不得只在聊天窗口输出长篇结论而不落盘。

## 8. 行为验收

实现至少通过以下回归场景：

1. **2024B 参数偷换**：题面中的 `0.13` 不得被自动绑定为未定义的模型概率；系统应给出证据缺口或选择卡。
2. **经典模型完整覆盖**：论文中的复杂模型不因更复杂而取代完整覆盖问题的经典模型。
3. **论文参数迁移**：外部论文参数未经适用性和单位核验不得进入计算。
4. **无可比 baseline**：不得用无法完成真实任务的玩具方法冒充 baseline。
5. **人工关卡**：无 `method_choice` 时禁止生成模型代码。
6. **结果异常**：退化输出或 fallback 触发后不得自动继续到最终结论。
7. **决定变更**：实质证据变化后旧决定标记 stale，并要求重新确认。
8. **数值血缘**：论文中的每个关键数值能定位到冻结值和实际结果文件。
9. **虚构引用**：无法核验的标题、作者、年份或 DOI 阻断最终参考文献。
10. **Markdown 交付**：每个人工决策点和最终阶段均生成规定的 Markdown 文件。

## 9. 非目标

- 不为了显示“高级”而扩充候选模型数量。
- 不要求每个 skill 每次都生成仪式性报告。
- 不把所有流程重新塞回单一 `math-modeling-core/SKILL.md`。
- 不在本次重建中自动修改现有 2024B 代码或结论；它只作为回归样例。
- 不发布或建立外部 marketplace。

## 10. 完成定义

只有满足以下条件才能称为完成：

- 28 个同名 skill 均安装并可被发现；
- 28 项职责和上游关卡没有缺项；
- 主动论文检索、防幻觉契约、人工判断和 Markdown 交付已嵌入对应 skill；
- 共享治理策略与每个 skill 的前置/输出/停止/验证契约一致；
- 结构检查和 10 类行为回归通过；
- 使用一个实际建模题完成至少到 G2.5 的端到端试运行，并保存 Markdown 产物。
