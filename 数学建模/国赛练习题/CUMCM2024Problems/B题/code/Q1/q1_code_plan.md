# Q1 第三轮代码规划

状态：`PLANNED`。实现目标为 Python，输出轮次为 `round3`。有效方法选择仍为 `q1_method_choice_v2`：B1 为主方法，M1 为可用基线；实验调整来自人类结果裁决 `q1_final_result_verdict`，原文理由为“真实次品率设置的组数不够多，不足以表现我们模型与方法的能力”。本轮只扩展参数覆盖，不改变判定公式、错误预算、检查点规则、上限未决语义或方法角色。

## 目标与变更边界

第二轮的 77 个非均匀参数点继续作为风险探针与历史一致性样本，但不足以形成提交阶段的连续工作特性曲线。第三轮在闭区间 ([0,1]) 上采用步长 0.001 的均匀真实次品率网格

\[
\Theta_3=\{0,0.001,0.002,\ldots,0.999,1\},\qquad |\Theta_3|=1001.
\]

该网格包含 (p_0=0.10)，并在 8%--12% 区间提供 41 个点。0.001 是本轮固定的实验分辨率，不是题给精度或通过结果调优所得。三种检测上限仍为 900、1000、1100；预计产生 (2\times3\times1001=6006) 行工作特性。不得把更密网格解释为新增真实数据或全参数数学证明。

第二轮代码、结果、审查、稳健性总结及提交报告保持只读。第三轮入口为 `code/Q1/q1_run_round3.py`，测试为 `code/Q1/test_q1_round3.py`，输出根目录为 `results/Q1/experiments/round3/`。原第二轮计划原样保存在 `code/Q1/q1_code_plan_round2.md`。

## 输入合同

| 来源 | 必需内容与校验 |
|---|---|
| `workspace/data_clean/q1_statement_parameters.csv` | 一行 (p_0=0.10,\alpha_R=0.05,\alpha_A=0.10)，概率为无量纲小数 |
| `methods/Q1/q1_decisions.jsonl` | 最新方法选择为 B1/main、M1/usable_baseline；存在 `q1_final_result_verdict` 且 `round_action=adjust` |
| `methods/Q1/q1_method_card.md` | B1、M1 的严格判定规则与限制 |
| `methods/Q1/probes/probe_config.json` | 原 77 点构造及 900/1000/1100 上限，用于历史子网格核对，不作为第三轮密网格来源 |
| `planning/model_assumptions.md`、`workspace/data/data_profile.json` | A1、A2 仍为适用条件；实测抽样行为数仍为 0 |
| `results/Q1/experiments/round2/` | 只读；密网格与原 77 点交集上的数值必须逐字段一致 |

输入哈希应写入第三轮 `run_summary.json`。旧运行摘要引用的旧版 `q1_code_plan.md` 内容已按其哈希原样保存为 `q1_code_plan_round2.md`；不得回写旧结果以迁就新路径。

## 数学与计算合同

### B1 主方法

对每个上限在抽样前固定“从 10 开始倍增并以该上限作为末次检查”的完整检查表。主预算 1000 的检查点为 (10,20,40,80,160,320,640,1000)，共 (K=8) 次，每次分别使用 (alpha_A/K=0.0125) 和 (alpha_R/K=0.00625)。在检查点 (k_\ell)，若

\[
\Pr_{p_0}\{\operatorname{Bin}(k_\ell,p_0)\le X_{k_\ell}\}<\alpha_A/K
\]

则接收；若

\[
\Pr_{p_0}\{\operatorname{Bin}(k_\ell,p_0)\ge X_{k_\ell}\}<\alpha_R/K
\]

则拒收，否则继续。非检查点不判定；到上限仍未越界则未决。900、1000、1100 三张表均有 8 次检查和相同逐次错误分配，只是末次检查点不同，因而彼此不嵌套。

### M1 可用基线

沿用固定 Beta(1,1) 均匀混合置信序列，每检测一件检查一次。使用稳定对数形式计算 (E_k(p_0))，并按样本比例相对 (p_0) 的方向严格越过 (1/\alpha_A) 或 (1/\alpha_R) 后接收或拒收。M1 必须输出与 B1 同单位、同参数网格、同上限的 ASN、(P_A,P_R,P_U)，不能降格为只提供单个参考数的诊断方法。

### 公共递推与指标

复用已审查的 `code/Q1/q1_run.py` 数值核心，以尚未停止的状态概率质量作精确递推。首次判定后概率质量吸收；以观测前存活概率计算

\[
\operatorname{ASN}(\theta)=\mathbb E_\theta[T^*],\qquad T^*=\min(T,N_{\max}),
\]

并独立用停止时刻的一、二阶矩复核 ASN 和 `SD_T_star`。每个情景满足 (P_A+P_R+P_U=1)。计算使用 `float64` 与稳定对数公式，写文件前不舍入。

## 输出合同

```text
results/Q1/experiments/round3/
├── figures/                         # 本轮允许为空，正式图由 figure-table-planner 决定
├── tables/
│   ├── decision_boundaries.csv
│   ├── operating_characteristics.csv
│   ├── comparison.csv
│   └── near_threshold_dense.csv
├── metrics/
│   ├── dense_grid_summary.json
│   └── validation.json
└── run_summary.json
```

`operating_characteristics.csv` 保留 `method_id,role,cap,theta,ASN,SD_T_star,P_A,P_R,P_U`。`comparison.csv` 按 B1 减 M1 给出 ASN 与未决率差。`near_threshold_dense.csv` 保存 (0.08\le\theta\le0.12) 的主预算逐点结果，共 41 行，不再只保留 8%、10%、12% 三点。

`dense_grid_summary.json` 至少报告：网格规模与步长；B1/M1 在主预算下 ASN 和未决率的逐点优劣计数；优势与劣势最大的参数位置；(P_U\ge0.5) 和 (P_U\ge0.9) 的参数区间（仅作描述性集中范围，不作为人类性能阈值）；最大相邻网格概率变化；原 77 点与 round2 的最大一致性误差。不得计算带隐含真实次品率权重的综合期望或据此声称全局最优。

`run_summary.json` 除标准字段外必须记录：

- `round="round3"`、`implementation_target="python"`；
- `approved_decision_id="q1_method_choice_v2"`；
- `experiment_adjustment_decision_id="q1_final_result_verdict"`；
- `change_from_round2="theta_grid_density_only"`、`mathematical_rule_change=false`；
- `theta_grid={start:0,end:1,step:0.001,count:1001}`；
- B1/main 与 M1/usable_baseline；
- `randomness="none"`、`seed_used=false`；
- A1/A2、近阈值集中、非嵌套上限和不得全局优越性外推等风险；
- `fallback_id=null`、`observed=false`。

## 验证合同

1. `input_contract`：题给参数、方法选择、调整裁决、网格端点/步长/数量均准确。
2. `method_alignment`：两法判定边界与第二轮一致，接收和拒收区域不重叠。
3. `probability_and_moments`：最大概率质量误差不超过 (10^{-10})，ASN 双路径误差不超过 (10^{-8}) 件。
4. `dense_error_grid`：在 1001 点和三个上限上，错拒不超过 0.05、错收不超过 0.10；同时注明有限网格不是全参数证明。
5. `directional_monotonicity`：随 (	heta) 增大，接收概率不增加、拒收概率不减少，容差 (10^{-10})。
6. `round2_overlap`：第三轮与第二轮 77 点交集上 ASN、`SD_T_star`、(P_A,P_R,P_U) 最大差不超过 (10^{-10})。
7. `schedule_check`：三个 B1 方案均恰为 8 次检查、共享前七点、逐次错误分配相同，末次检查点不同。
8. `reproducibility`：独立小状态路径枚举误差不超过 (10^{-10})，`--verify-existing` 全量重算与保存文件一致。
9. `scale`：目标为每种方法 60 秒以内、跟踪内存 256 MB 以内；若超限应失败并保留诊断，不得降低网格密度后静默宣称成功。

## 风险、fallback 与下一步

扩大网格只提高曲线分辨率，不能验证 A1/A2，也不能消除阈值附近高未决率。1001 点仍是有限离散网格；错误控制的统一理论依据仍须单独陈述。描述 (P_U\ge0.5) 或 (P_U\ge0.9) 的区间不等于把 50% 或 90% 设为可接受阈值。

当前无条件性备用方法，`fallback_id=null`。若密网格暴露错误控制超限、方向反常、数值不复现或资源超限，则停止并返回代码审查/实验设计，不自动改变检查点、错误预算或方法选择。若只出现与既有结论一致的高未决集中，则如实报告，交由新的提交级结果裁决处理。

下一 skill 为 `python-model-code-generator`，只实现上述 round3 密网格证据；随后重新进入 `code-reviewer`、`result-report-generator` 与 `robustness-checker`。现有 `q1_final_result_analysis.md` 因人类要求扩大证据覆盖而不再作为可冻结终稿，待 round3 通过后重建。
