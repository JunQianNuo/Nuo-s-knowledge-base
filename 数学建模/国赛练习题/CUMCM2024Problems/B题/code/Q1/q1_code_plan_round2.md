# Q1 第二轮代码规划

状态：PLANNED；尚未生成或运行第二轮代码。有效人类决策为 `q1_method_choice_v2`：B1 为主方法，M1 为可用基线，理由原文为“B1方案在接近10%时的未决率较小”。无条件性备用方法。保持 `interaction_mode: learning` 与 `rigor_profile: lean`。

## 目标与变更边界

第二轮只落实已批准的角色调整，不重选或改写数学方法：主方法采用 B1 预定分批精确二项检验，基线采用 M1 均匀 Beta-Binomial 混合置信序列。两者继续输出整数判定边界，以及参数化的平均检测数（ASN）、接收概率、拒收概率和未决概率，以便在同一参数网格与预算下直接比较。

本轮相对第一轮的变化类型为 `method_roles_only`，`mathematical_rule_change=false`。第一轮代码、结果、审查和稳健性证据保持只读；第二轮不得覆盖它们。B1 在已测近阈值情景中的未决率相对 M1 较低，但在真实次品率恰为 10% 时仍约为 93.64%，所以此次选择表示相对偏好，不表示近阈值未决问题已经解决，也不支持“全局最少检测次数”或“普遍稳定”的结论。

实现语言为 Python，实验轮次为 `round2`，结果根目录为 `results/Q1/experiments/round2/`。本轮只生成理论性能证据，不生成实测序列、论文、冻结数字、图表成品或 MATLAB 副本。

## 输入与配置合同

| 来源 | 必需内容 | 校验、单位和边界 |
|---|---|---|
| `workspace/data_clean/q1_statement_parameters.csv` | `nominal_defect_rate`、`reject_confidence`、`accept_confidence` | 恰一行；本题为 0.10、0.95、0.90；无量纲小数；拒绝缺失、非有限及越界值 |
| `methods/Q1/q1_decisions.jsonl` | 最新有效记录 `q1_method_choice_v2`，B1/main，M1/usable_baseline | 运行前确认状态为 DECIDED、替代关系明确，不把第一轮角色当成当前角色 |
| `methods/Q1/q1_method_card.md` | B1、M1 的公式、严格判定语义、风险和适用边界 | 不修改错误预算、混合权重或上限未决语义 |
| `methods/Q1/probes/probe_config.json`、`methods/Q1/probes/risk_probe_summary.json` | 固定参数网格、检查点生成规则、风险条件 | 复用筛选时的预注册配置，不根据第一轮结果重新挑选有利参数 |
| `workspace/data/data_profile.json`、`planning/model_assumptions.md` | 数据状态以及 A1/A2 | iid Bernoulli 与无误检测只是适用条件；当前无实测记录可验证它们 |
| `results/Q1/experiments/round1/tables/operating_characteristics.csv` | 第一轮按 `method_id/cap/theta` 的历史数值 | 只读，用于核对数学规则未变；不得直接复制成第二轮证据 |

题给阈值与两项错误预算保持为

\[
p_0=0.10,\qquad \alpha_R=0.05,\qquad \alpha_A=0.10.
\]

主预算为 1000 件，预算敏感性切片为 900、1100 件；它们是当前实验设计，不是题给上限或优化所得上限。真实次品率网格继续由探针中的基础网格与 0.9/1.1 相对扰动生成，截到 `[0,1]` 后按 12 位小数去重，预期共 77 点。`theta` 是理论情景参数，不是观测估计。

B1 在主预算 1000 下的预定检查点为 `[10,20,40,80,160,320,640,1000]`，每侧按实际检查次数 `K` 使用 Bonferroni 预算 `alpha_A/K`、`alpha_R/K`。预算为 900 或 1100 时，从 10 起倍增并补入各自的最终上限；三张检查表因此分别预注册、并不嵌套。上限变化可能改变检查次数和单次错误预算，不能预设更大上限一定降低未决率。

M1 基线每检一件均检查一次，沿用固定 `Beta(1,1)` 均匀混合与时间一致阈值。两法均首次越界即停止；到达上限仍未越界时输出未决，不强制接收或拒收。

## 文件与复用边界

第二轮新入口为 `code/Q1/q1_run_round2.py`，测试为 `code/Q1/test_q1_round2.py`。第一轮的 `code/Q1/q1_run.py` 与 `code/Q1/test_q1_model.py` 不得改写。

允许从经审查的第一轮模块导入纯数值核心，例如规则构建、概率递推、混合置信集反演及边界见证检查；不得调用其第一轮 `main`、输入装载器或输出常量，因为这些包含旧决策编号、旧角色和 `round1` 路径。第二轮入口负责独立校验当前决策、建立当前角色、重新计算并写入新目录。`run_summary.json` 必须记录复用模块的 SHA-256 哈希，使依赖可追踪。

若旧模块接口不足以安全复用，可在第二轮文件中抽取最小适配层，但不得借机调整数学规则或篡改第一轮文件。不得实现未获批准的备用方法。

## 计算合同

### B1 主方法

仅在预定检查点计算精确二项分布上下尾。低端尾概率严格小于 `alpha_A/K` 时接收，高端尾概率严格小于 `alpha_R/K` 时拒收；非检查点不判定。导出的边界必须标记 `is_look`，不存在的边界写 `null`，不得用 0 冒充。两侧判定必须互斥，检测开始后不得改检查表或错误分配。

### M1 可用基线

用稳定的对数阶乘或 `lgamma` 计算方法卡中的 `log E_k(p0)`，并结合 `X_k/k` 位于 `p0` 的方向，按对应的 `1/alpha_A` 或 `1/alpha_R` 严格越界。每个 `k` 导出最大可接收次品数及最小可拒收次品数；少量边界邻点用独立二分反演混合置信集，核对 `L/U` 与整数判定一致。

### 公共概率递推

公共求值器按“累计检测数、累计次品数、尚未停止概率质量”递推，接收和拒收概率质量在首次判定后吸收。以每次观测前的存活概率求 ASN；另以吸收时刻及最终未决质量独立累计停止时间一、二阶矩，核对 ASN 并求 `SD_T_star`。使用 `float64` 与稳定对数公式，判定前不舍入。

标准摘要保留 `random_seed=2026`，同时写 `randomness="none"`、`seed_used=false`；本轮为确定性概率计算，不通过伪造模拟来“使用”种子。

## 输出合同

以下均为未来运行产物，当前不表示已经存在：

| 输出 | 必需字段或内容 |
|---|---|
| `tables/decision_boundaries.csv` | `method_id,cap,k,is_look,accept_max_defects,reject_min_defects`；B1 仅预定检查点可有边界 |
| `tables/operating_characteristics.csv` | `method_id,role,cap,theta,ASN,SD_T_star,P_A,P_R,P_U` |
| `tables/comparison.csv` | `cap,theta,B1_ASN,M1_ASN,ASN_B1_minus_M1,B1_P_U,M1_P_U,P_U_B1_minus_M1`；差值方向以当前主方法 B1 减基线 M1 为准 |
| `tables/near_threshold_summary.csv` | `theta` 为 0.08、0.10、0.12 时两法的 ASN、三态概率和差值；用于核对本次人类选择的依据，不代替全网格结果 |
| `metrics/sensitivity.json` | 参数相对 ±10% 时三态分布 TV、ASN 变化、是否跨越 `p0`，以及不同上限的效果；不得把 TV 称作单批方案翻转率 |
| `metrics/validation.json` | 输入、边界、独立枚举、概率守恒与单调性、错误控制网格、第一轮数值一致性、耗时及失败项 |
| `run_summary.json` | 实际执行状态、决策编号、当前角色、变更类型、配置、输入/代码哈希、环境、指标、风险和输出清单 |

检测数与 ASN 的单位为件，概率以 `[0,1]` 小数保存。`P_U` 是未决概率，不得与上置信界 `U` 混淆。`figures/` 可以为空，摘要中 `figure_files=[]`；成功运行不写长日志或重复 README。

`run_summary.json` 至少包含：`schema_version`、`question="Q1"`、`round="round2"`、`implementation_target="python"`、`approved_decision_id="q1_method_choice_v2"`、`change_from_round1="method_roles_only"`、`mathematical_rule_change=false`、`random_seed`、`randomness`、`seed_used`、`methods`、`comparison`、`risk_conditions`、`fallback_trigger`、`environment`。`methods` 中 B1 记为 `main`，M1 记为 `usable_baseline`；无备用方案，故 `fallback_id=null`、`observed=false`。

第二轮重新计算的同一 `method_id/cap/theta` 数值应与第一轮在 `1e-10` 容差内一致；当前角色、比较差值方向和决策编号则必须不同。若数学数值不一致，运行应标记失败并保留诊断，不得修改历史结果迁就新结果。

## 风险条件与可支持结论

持续保留 A1/A2、敏感区间、近阈值未决集中及上限影响。正式报告必须成对展示 ASN 与未决概率，不能只用较小 ASN 宣称更优。尤其应明确：

- B1 在已检查的 8%、10%、12% 附近相对 M1 未决率较低，是主方案选择的经验依据；
- `theta=0.10` 时两法均大量未决，B1 约 93.64%，因而不存在“稳定解决临界点”的证据；
- B1 的 900/1000/1100 检查表不同，增大上限可能因 Bonferroni 分配变化而局部放大未决概率；
- 参数化结果只描述规则在假设情景下的工作特性，不能证明真实批次独立、检测无误、全局最优或任意有限样本必有结论。

不得新增人类未给定的 TV 阈值、最低判定率或真实 `theta` 权重。若使用者以后要求绝对近阈值判定率目标，必须返回决策与方法筛选，不自动调检查点。

## 验证及审查合同

- `syntax`：新入口与测试可解析，无导入即执行副作用；旧文件哈希保持不变。
- `input_contract`：严格校验 CSV、概率域、预算、探针配置与最新有效决策；发现角色不匹配立即失败。
- `method_alignment`：B1 只在预定检查点判定并使用正确 Bonferroni 分配；M1 方向、严格阈值与混合公式一致；两法均无上限强制决策。
- `reproducibility`：对 12 件的全部二进制路径作独立枚举核对，B1 包含 10、12 两个检查点；误差不超过 `1e-10`。固定配置重复运行数值一致，耗时可以不同。
- `historical_equivalence`：按 `method_id/cap/theta` 与第一轮正式表逐项比较，ASN、`SD_T_star`、`P_A/P_R/P_U` 最大绝对误差不超过 `1e-10`；只允许角色字段和比较方向改变。
- `output_contract`：概率和误差不超过 `1e-10`，概率在容差内属于 `[0,1]`，ASN 属于 `[1,cap]`；双重 ASN 核算误差不超过 `1e-8`；`theta=0/1` 未决为 0；接收率随 `theta` 非增、拒收率非减。
- `risk_reporting`：近阈值表必须包含 0.08、0.10、0.12；摘要必须显式保留 B1 在 10% 仍高未决和上限非单调风险。
- `no_clobber`：若 `round2` 已存在来源不明或非空产物，停止并报告，不覆盖；不得写入 `workspace/data_raw/`、`round1/` 或既有审查文件。

数值核验失败、边界重叠、错误概率超界或任一方法超过 60 秒/跟踪分配内存 256 MB 时，保存失败摘要并停止正常交付，不静默换方法。生成器自检不能替代 `python-code-reviewer` 的独立审查。

## 环境与交接

已知可用 Python 3.12.13、NumPy 2.3.5；执行时重新记录真实版本。不依赖 SciPy，不下载新库。解释器预期为 `C:/Users/Nuo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`。

下一 skill 为 `python-model-code-generator`：只实现已批准的 B1 主方法、M1 基线及共享验证逻辑，生成 `round2` 证据；随后依次进入 `code-reviewer` 与 `python-code-reviewer`。当前仍不允许结果定稿、论文写作或最终组装。
