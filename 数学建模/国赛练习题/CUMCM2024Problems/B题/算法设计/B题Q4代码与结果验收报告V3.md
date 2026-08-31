---
title: B题 Q4 代码与结果验收报告 V3
problem: CUMCM 2024 B题 Q4
model_id: Q4-M4 + Q4-M2 + Q4-M3
algorithm_id: Q4-A3 + Q4-A1 + Q4-A2
source_version: Q4_v3.0
result_base_commit: ac9b71e868f2096ccb2c6d75eca13d06cae68d82
reviewed_at: 2026-08-30T15:10:41+08:00
status: PASS_WITH_REVIEW
verdict: pass_with_review
---

# B题 Q4 代码与结果验收报告 V3

## 1. 总结论

> [!success] Q4-M4/M2/M3 与 Q4-A3/A1/A2 实现通过验收
> 当前 `q4/` 代码确实实现 **Q4-M4 序贯价值信息联合抽样—生产决策主模型**（Q2 有限期精确 DP / Q3 成本敏感一步 KG），以 **Q4-M2 + Q4-A1** 提供后验终止价值，以 **Q4-M3 + Q4-A2** 提供频率学稳健审计；模型 ID、Belief 更新、Bellman/KG 动作值、成本分账、双先验、条件制样校验与最优性称谓均与阶段2/阶段3设计一致。

本报告为 Q4 首个验收报告（此前算法设计目录仅有 Q1/Q2/Q3 验收记录）。本轮未发现会改变 Q2 初始决策、Q3 停止决策或稳健策略的功能性错误。**必须重申：题面未给实际 $(N_j,K_j)$、先验强度和完整抽样成本，全部数值结果基于 `q4_demo_evidence.json`（`DEMO_ONLY_NOT_OFFICIAL_DATA`），任何"最优检测次数"都必须绑定保存的情景配置。**

剩余问题集中在三处：Q4-A2 内层最坏搜索未按设计实现（仅单点端点评价）、Q4-A3 的 rollout 未接入主流程、Q3 MC/RQMC 预算与收敛检查低于设计契约。三者均不改变当前已保存数值的正确性，但其中第 1 项影响稳健审计的称谓强度，须按第 7 节处理。

## 2. 验收依据

| 类别 | 文件 |
|---|---|
| 模型契约 | [[国赛练习题/CUMCM2024Problems/B题/模型设计/B题阶段2模型设计报告.md]] 第 7 节（Q4-M2/M3/M4） |
| 算法契约 | [[国赛练习题/CUMCM2024Problems/B题/算法设计/B题阶段3算法设计报告.md]] 第 7–9、13、14 节（Q4-A1/A2/A3） |
| 主程序 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/run_q4.py]] |
| Belief 状态 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/belief_state.py]] |
| 终止价值 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/terminal_value.py]] |
| 精确 VOI DP | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/exact_voi_dp.py]] |
| KG/rollout | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/kg_rollout.py]] |
| 联合置信集 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/simultaneous_cs.py]] |
| 生产评价器 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/batch_evaluators.py]] |
| 测试 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/test_q4.py]] |
| 参数/证据 | [[国赛练习题/CUMCM2024Problems/B题/代码/q4/config.json]]、[[国赛练习题/CUMCM2024Problems/B题/代码/q4/q4_demo_evidence.json]] |
| 摘要/复现 | [[国赛练习题/CUMCM2024Problems/B题/代码/results/q4/summary.json]]、[[国赛练习题/CUMCM2024Problems/B题/代码/results/q4/reproducibility.json]] |

复现清单记录提交号 `ac9b71e8`（`git_dirty=true`）、探索/确认种子 2024/12024、证据与 12 个 Q4 源文件 SHA-256；本轮核验与清单一致。

## 3. Q4-M4/M2/M3 模型符合性

| 模型要求 | 当前实现 | 判定 |
|---|---|---|
| Belief state $(a_j,b_j)=a_{j0}+K_j,\ b_{j0}+N_j-K_j$ | `from_records` 严格一致 | ✅ |
| 观测模型 $Y_{j,t}\mid p_j\sim\mathrm{Bernoulli}(p_j)$，独立 Beta 基准 | 一致；未引入相关模型（设计允许的基准） | ✅ |
| 条件制样语义（内部节点必须 `all_inputs_good`） | schema 强制校验，违规返回 `INVALID_CONDITIONING` | ✅ |
| 过去抽样成本为沉没成本，不改变策略排序 | `past_sampling_cost` 仅入总净利润 | ✅ |
| 未来抽样成本进入动作值，不与生产检测重复 | Bellman/KG 中扣除，分账审计通过 | ✅ |
| Q4-M2：$G(s)=\max_d\mathbb E_s[\Pi(d;\mathbf p)]$ | 确定性求积/全策略 RQMC 计算 | ✅ |
| Q4-M2 输出：最优概率、期望遗憾、负利润概率、分位数 | 全部输出 | ✅ |
| Uniform/Jeffreys 双先验透明基准 | `priors` 双组运行 | ✅ |
| Q4-M4：动作={停止, 检测 $j$}，Bellman 方程 (Q4-2)/(A3-1) | 精确 DP 与 KG 均按公式实现 | ✅ |
| 停止原则：净价值不为正即停止，不强制统一置信半宽 | `STOP_NO_POSITIVE_NET_VOI` 等状态码 | ✅ |
| EVSI/NVSI/EVPI 报告 | Q2 全量输出；Q3 输出 EVPI | ✅ |
| Q4-M3：$\mathcal U=\prod_j\mathcal C_j$，$d_R^*=\arg\max_d\min_{\mathbf p\in\mathcal U}\Pi(d;\mathbf p)$ | Bonferroni 联合集 + 全策略外层取最大 | ⚠️ 内层最小值仅取单端点，见 §4 |
| 稳健审计默认只作审计层，不冒充硬约束 | 一致 | ✅ |

## 4. Q4-A3/A1/A2 算法符合性

| 算法要求 | 当前实现 | 判定 |
|---|---|---|
| Q4-A1/Q2：Gauss–Jacobi 求积，多阶收敛判据（价值、前两名差、最优稳定） | 阶序列 [8,12,16,24,32,48]，三条件齐备，`VALUE_INTEGRATION_CONVERGED` | ✅ |
| Q4-A1/Q3：全策略共同随机数/RQMC，8 个独立 scramble | 8 scramble + Owen-scrambled Sobol + 独立确认种子 | ✅ |
| 禁止 nominal top-$K$ 预筛 | 每批覆盖全部 16/65536 策略 | ✅ |
| 探索/确认分离，确认推翻排序 → 近优集合/ambiguous | `AMBIGUOUS` / `VOI_MC_NOT_CONVERGED` 分支 | ✅ |
| Q4-A3/Q2：记忆化后向 DP，状态键、平局规则（停止>无切换>成本低>ID 小） | 一致；`VOI_DP_STATE_LIMIT` 保护 | ✅ |
| Q4-A3/Q2：EVPI 剪枝等有证据剪枝 | 未实现（H=4 状态数 210，未触发） | ⚠️ 设计列明但非当前瓶颈 |
| Q4-A3/Q3：成本敏感一步 KG（A3-2） | 按公式实现，配对 t 区间，`myopic-KG` 标签 | ✅ |
| Q4-A3/Q3：rollout 改善短视性（L 深度敏感性） | `rollout_with_oracle` 仅单测使用，主流程未接线；`rollout_depth/paths` 为死配置 | ⚠️ 未实现 |
| MC 误差控制（C6）：B0=1024/scramble、稳定 checkpoint×3、ε_prob=0.005 收敛循环 | 实际 16 draws/scramble、无 checkpoint 循环、无 SE 门禁 | ⚠️ 低于设计契约 |
| Q4-A2：固定样本 → Clopper–Pearson；自适应 → time-uniform CS | 按 `stopping_rule` 自动路由 | ✅ |
| Q4-A2：Bonferroni $\alpha_j=\alpha_{\mathrm{total}}/J$，90% 主、95% 敏感性 | `robust_coverages=[90,95]` | ✅ |
| Q4-A2：单调性三层认证（结构证明/JAX 反例/区间导数） | 未实现；仅断言 "structural monotonicity" | ⚠️ 未实现 |
| Q4-A2：无证书时 2^r 角点 + SHGO + ≥10 seed DE + 区间 BnB | 仅单点（全上端点）评价，`inner_gap=None` | ⚠️ 未实现，称谓需降级 |
| `ROBUST_CERTIFIED`/`ROBUST_NUMERICAL`/`ROBUST_UNCERTIFIED` 语义 | 使用 `ROBUST_NUMERICAL`，但按设计定义需角点/SHGO/DE 一致 | ⚠️ 当前证据弱于设计定义 |
| 策略称谓：exact-DP-to-tolerance / myopic-KG / ambiguous | 标签与状态码一致 | ✅ |

## 5. 本轮实测证据

### 5.1 单元测试

`q4.test_q4` 8 项全部通过：KG 多 scramble 门禁、schema 条件制样校验、fixed/sequential 区间覆盖、Q2 求积收敛、零期界退化、Q2 批量评价器 vs Markov 求解器（<1e-9）、Q3 批量评价器 vs 局部核（<1e-8）、rollout 微型 oracle。

### 5.2 独立复核（验收方另写实现）

| 检查 | 实测结果 |
|---|---|
| 独立 MC（2×10⁶ Beta 样本）复算情形1/Uniform 终止价值 | $G(s)=17.0123$ vs 保存 17.0111（MC 误差内）✅ |
| 独立 MC 复算 EVPI | 0.0436 vs 保存 0.0444 ✅ |
| 独立 MC 最优策略 | 1101，与保存一致 ✅ |
| Bellman 恒等式（$V\ge G$、$V-G\le\mathrm{EVPI}$、NVSI≥0） | summary checks 全 true ✅ |
| 成本分账（过去/追加/生产） | 情形1 过去成本 3600 = 100×(2+3+31) 核对一致 ✅ |
| 状态数 | 210 = $\sum_{h=0}^{4}\binom{4-h+5}{5}$ 理论一致 ✅ |
| Q2 输入 | `table1.json` 与题面表 1 六情形逐项一致 ✅ |

### 5.3 关键结果摘录（DEMO 情景）

- **Q2（6 情形 × 2 先验）**：初始动作全部 STOP，NVSI=0（EVPI≤0.36 < 最便宜边际检测成本 1），期望追加样本数 0；终止策略 1101/1101/1111/1111/0110(0100)/1000(0000)；$G(s)$ 10.14–20.97 元/件；扣除过去抽样成本（3200–3900 元）后净利润为负。
- **Q3**：STOP（全部净 KG 为负 ≈−边际成本），终止策略 63487，停止价值 55.31(Uniform)/56.34(Jeffreys)，EVPI 0.095/0.076。
- **稳健审计（90%/95%）**：情形1–4、6 稳健策略 = Bayesian 策略；情形5 切换为 1101（Bayesian 0110 最坏 −2.64/−5.04，稳健 1101 最坏 +1.45/+0.24）；Q3 切换为 65535（最坏 29.71 vs 63487 的 26.96）。

### 5.4 测试环境说明

验收在 Windows/Python 3.13 + NumPy 2.4.6 + SciPy 1.17.1 + pandas 2.3.3 完成；结果清单为 Linux/Python 3.14.7 容器运行（`generated_at_utc=2026-08-30T06:30:14Z`）。Q4 不依赖 `confseq`，本机可直接运行全部测试。

## 6. 尚存差异与优先级

1. **P1：Q4-A2 内层最坏搜索未按设计实现，且 `ROBUST_NUMERICAL` 称谓强于当前证据。** 设计 §8.2/8.3 要求先做三层单调性认证（结构耦合证明 + JAX 反例搜索 + 区间导数认证）；未获证书时执行 2^r 角点 + SHGO(n=8192) + ≥10 固定种子 DE + 区间分支定界（gap ≤ ε_robust）。当前实现只评价单点（全上端点）并断言 "supported by structural monotonicity"，未执行任何认证流程；按设计定义 `ROBUST_NUMERICAL` 需要"角点、SHGO、DE 一致"，当前证据不足。**修复前：论文引用稳健审计结果时必须原样保留 `claim_scope` 中 "no interval BnB certificate" 的限定，不得写成已认证最坏利润。** 利润对 p 单调递减的结构使单端点数值大概率正确，但设计契约要求先证明再固定端点。
2. **P2：Q3 rollout 未接入主流程。** 设计 §9.4 以 KG 为 base policy 做 L 步 rollout 与深度敏感性；当前 `run_q4.py` 只跑一步 KG（标签 myopic-KG 诚实），`config.json` 的 `rollout_depth/rollout_paths` 未使用。建议删除死配置或接入 rollout。
3. **P2：Q3 MC/RQMC 预算与收敛检查低于设计契约（C6、§7.3）。** 实际 16 draws/scramble vs 设计起步 1024、无"三个稳定 checkpoint"、无 ε_prob=0.005 最优概率容差循环、无 SE 达标门禁；后验最优概率 0.90625 仅为 128 样本粒度。数值当前正确，但误差控制未达设计标准。
4. **P2：Q4-M4 敏感性输出未实现（设计 §7.5.3 第 7 条）。** 无先验强度 τ 敏感性（§7.3 的 $a_{j0}=\tau\widetilde p_j$ 情景先验）、无 $H/B$ 稳定性、无检测成本/破坏性/切换成本变体；EVPI 剪枝（§9.2）也未使用。
5. **P3：稳健审计未输出 $d_R^*$ 相对 $d_B^*$ 的后验期望利润损失（§8.4）。** 可经 `simultaneous_intervals.csv` + 后验均值补算。

## 7. 最终判定

> [!important] 验收状态：PASS_WITH_REVIEW

- **模型与算法主线：通过；**
- **Q2 精确 VOI DP、Q3 myopic KG 与终止价值、联合置信构集与全策略外层：通过，可进入论文（按各自标签与 DEMO 情景口径）；**
- **独立复核（求积/DP/MC/分账/输入数据）：通过；**
- **P1 修复前：稳健审计只能按 §6.1 的限定称谓呈现，不得声称已认证最坏利润；**
- **P2/P3 项不改变当前保存数值，但建议在论文定稿前处理（rollout 接线或删除死配置、MC 预算与收敛检查、敏感性情景、$d_R^*$ 损失报告）。**
