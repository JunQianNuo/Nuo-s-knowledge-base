---
title: 2024 CUMCM B题算法设计（math-modeling-core）
date: 2026-09-02
mode: solve / algorithm-design
status: WARN
source_model_review: ../math-modeling-core-analyze-20260902/analysis.md
solver_executed: false
---

# 0. 结论与版本关系

本阶段只冻结算法，不伪造题面没有给出的数据，也不发布最终数值策略。四问采用同一条可复核计算链：

$$
\text{二项抽样证据}
\rightarrow \text{质量参数/置信集合}
\rightarrow \text{闭环生产策略评价器}
\rightarrow \text{精确策略比较与稳定性审计}.
$$

| 问题 | 模型 | 主算法 | 最优性/状态口径 |
|---|---|---|---|
| Q1 | 两质量点、双风险截尾序贯验收 | 精确二项固定样本基线 + 截尾 SPRT + 精确路径 DP 校准 | 模型族已定；具体方案因 $p_1,N_{\max}$ 未由题面给定而 `BLOCKED_DATA` |
| Q2 | 两零件吸收 Markov 奖励模型 | 16 个固定策略全枚举 + 状态图生成 + 线性方程求解 | 对已声明的固定策略空间精确 |
| Q3 | 装配树吸收 Markov 奖励模型 | 后序局部核 + 65536 个固定策略全枚举 | 对题给 16 位固定策略空间精确 |
| Q4 | 联合置信集合传播与策略稳定性 | 同时区间 + Q2/Q3 评价器复用 + 数值筛选 + 区间分支定界认证 | 具体结果因缺少各节点 $(N_j,K_j)$ 而 `BLOCKED_DATA`；未完成区间认证时只称数值审计 |

本报告取代旧算法报告中把 Q4 的 Bayesian VOI、KG/rollout 作为主线的部分。它们只在企业另外提出“下一件检什么、检多少、何时停”，并提供先验、追加抽样成本、预算及切换成本后启用。现有 Q1–Q3 主干仍可复用。

# 1. 统一算法契约

## 1.1 冻结的业务解释

1. 计算单位是一笔订单最终交付一个合格品，不是一次装配，也不是单位时间。
2. 收入只计一次；市场次品会产生题给调换损失，并触发补产。
3. 节点次品率是“直接子件均合格条件下”的装配次品率。
4. 检测在主线中假定完美且无损；检出坏件后丢弃并补购。
5. 拆解不损坏子件，也不重置其真实质量；已获得的信息随回收件保留。
6. 题面未给库存、工时、误检率和缺陷相关性，因此不使用库存控制、SMDP 或复杂相关失效模型。

## 1.2 统一生产评价接口

```text
evaluate_policy(problem, policy, quality_parameters, assumptions)
    -> {
         status,
         expected_profit,
         expected_total_cost,
         cost_breakdown,
         event_counts,
         absorption_margin,
         linear_residual,
         diagnostics
       }
```

利润始终为

$$
\Pi(d;\mathbf p)
=S-\mathbb E_d[C_{\rm buy}+C_{\rm test}+C_{\rm assembly}
+C_{\rm disassembly}+C_{\rm replacement}].
$$

Q2、Q3 和 Q4 必须调用同一个评价接口。Q4 不得为了计算方便另写一个忽略回流或改变核算分母的利润公式。

## 1.3 统一状态码

| 状态码 | 含义 | 是否允许进入策略比较 |
|---|---|---|
| `SUCCESS_EXACT` | 状态、吸收性和线性方程均通过 | 是 |
| `SUCCESS_LOCAL_CALIBRATION` | Q1 只完成预声明边界邻域校准 | 是，但不能称族内全局最优 |
| `SUCCESS_GRID_OBJECTIVE` | 连续参数目标只在网格上评价 | 是，但必须保留限定词 |
| `BLOCKED_DATA` | 缺少 $p_1,N_{\max}$ 或 $(N_j,K_j)$ | 否；只输出参数化方案 |
| `NON_ABSORBING` | 存在可达闭合循环或 $\rho(P)\ge1$ | 否；期望成本不可作有限值发布 |
| `NEAR_NONABSORBING` | 吸收裕度很小、数值病态 | 高精度复核后决定 |
| `ILL_CONDITIONED` | 线性方程无法在容差内稳定求解 | 否 |
| `WARN_NUMERICAL_STABILITY` | Q4 只做场景/采样审计，未获区间证书 | 可报告，不可称稳健最优 |

# 2. Q1 算法：精确二项基线 + 截尾 SPRT + 路径 DP

## 2.1 输入与输出

输入：

- 可接受质量点 $p_0=0.10$；
- 不可接受质量点 $p_1>p_0$，必须由企业声明或做情景分析；
- 生产方风险 $\alpha=0.05$，使用方风险 $\beta=0.10$；
- 最大样本量规则，例如 $N_{\max}\le \kappa n_F$；
- 独立 Bernoulli 抽样、完美检测的主线假设。

输出：固定样本基线 $(n_F,c_F)$、每个时刻的接收/拒收边界、最大样本量、终端截断数、OC 曲线、两端点精确风险、ASN 曲线、停止时间分位数和最优性范围。

若 $p_1$ 或截尾规则未冻结，算法只运行 $p_1\in\{0.12,0.13,0.15,0.20\}$ 的敏感性，不把其中任一值伪装为题目事实。

## 2.2 固定样本精确基线

对 $n=1,2,\ldots$ 和整数 $c\in\{0,\ldots,n\}$ 搜索：

$$
P_{p_0}(X_n>c)\le\alpha,
\qquad
P_{p_1}(X_n\le c)\le\beta.
$$

首次可行的 $n$ 即最小固定样本量；使用 `binom.sf` 计算上尾，避免 `1-cdf` 的消减误差。以下值作为实现 oracle，而不是 Q1 最终答案：

| $p_1$ | $n_F$ | $c_F$ | $P_{0.10}(R)$ | $P_{p_1}(A)$ |
|---:|---:|---:|---:|---:|
| 0.12 | 2096 | 232 | 0.0493657550 | 0.0995398380 |
| 0.13 | 968 | 112 | 0.0486497073 | 0.0997558579 |
| 0.15 | 368 | 46 | 0.0496448526 | 0.0999328161 |
| 0.20 | 109 | 16 | 0.0432080762 | 0.0990770489 |

## 2.3 序贯边界初始化

累计次品数为 $K_t$，累计对数似然比为

$$
\ell_t=K_t\log\frac{p_1}{p_0}
+(t-K_t)\log\frac{1-p_1}{1-p_0}.
$$

Wald 初值为

$$
h_A^{(0)}=\log\frac{\beta}{1-\alpha},
\qquad
h_R^{(0)}=\log\frac{1-\beta}{\alpha}.
$$

当 $\ell_t\le h_A$ 时接收，当 $\ell_t\ge h_R$ 时拒收，否则继续。Wald 边界只用于生成候选；离散越界与有限截尾会改变真实风险，必须由精确 DP 重新校准。

## 2.4 精确路径递推

令 $q_t(k;p)$ 为时刻 $t$ 决策后仍继续、且累计 $k$ 个次品的概率质量。初始化 $q_0(0;p)=1$，逐层递推

$$
\widetilde q_{t+1}(k;p)
=(1-p)q_t(k;p)+p q_t(k-1;p).
$$

按整数边界把质量分流到接收、拒收或继续集合；在 $t=N_{\max}$ 用终端截断数 $c_N$ 强制二元终止。由递推直接得到

$$
P_p(A),\quad P_p(R),\quad
\operatorname{ASN}(p)=\sum_{t=0}^{N_{\max}-1}\sum_k q_t(k;p).
$$

概率守恒门为 $|P_p(A)+P_p(R)-1|\le10^{-10}$。有限状态递推是性能主计算；Monte Carlo 只允许作独立复核。

## 2.5 边界校准与目标

在可达 LLR 断点、$N_{\max}$ 和 $c_N$ 上搜索，而不是盲扫连续小数阈值：

```text
for p1 in declared_scenarios:
    fixed <- minimum_exact_binomial_plan(p0, p1, alpha, beta)
    candidate_set <- {fixed plan}
    for Nmax in declared_caps:
        for (hA, hR) in reachable_LLR_breakpoints_near_Wald:
            boundaries <- integer_boundaries(hA, hR, Nmax)
            for cN in feasible_terminal_cutoffs:
                risk0 <- exact_path_DP(plan, p0)
                risk1 <- exact_path_DP(plan, p1)
                if risk0.reject <= alpha and risk1.accept <= beta:
                    J <- sup_{p in [p0,p1]} ASN(plan,p)
                    retain(plan, J, Nmax, endpoint_ASN)
    choose lexicographically by (J, Nmax, endpoint_max_ASN, hash)
```

主目标为无差异区最坏 ASN：

$$
\min_\pi\sup_{p\in[p_0,p_1]}\operatorname{ASN}(p;\pi),
$$

同时满足双风险和最大样本量约束。若 ASN 上确界只在网格上取最大，状态必须是 `SUCCESS_GRID_OBJECTIVE`；若阈值只在 Wald 邻域搜索，则是 `SUCCESS_LOCAL_CALIBRATION`。只有完整覆盖预声明边界族且连续上确界得到认证时，才称“族内最优”。

## 2.6 复杂度与失败回退

一个候选、一个 $p$ 值的滚动 DP 时间上界为 $O(N_{\max}^2)$，工作内存为 $O(N_{\max})$。先在 $p_0,p_1$ 做风险剪枝，只对可行短名单计算完整 OC/ASN。

若企业拒绝声明 $p_1$，回退为双单侧任意停止有效置信序列，但报告必须写明：该方案控制任意停止错误，不保证检测次数最少。

# 3. Q2 算法：16 策略枚举 + 吸收 Markov 奖励求解

## 3.1 策略编码

固定策略

$$
d=(x_1,x_2,y,z)\in\{0,1\}^4,
$$

分别表示检测零件 1、检测零件 2、检测成品和拆解坏成品。共 16 个，不使用 GA、PSO 或 SA。

## 3.2 可达状态生成

状态至少记录

$$
s=(\text{phase},z_1,z_2,i_1,i_2,o_1,o_2),
$$

其中 $z_i\in\{\text{missing,good,bad}\}$ 是真实质量，$i_i$ 是未知/已知良/已知坏信息，$o_i$ 是新购/回收来源。流程阶段包括备料、两个零件检测、装配和已知坏成品处理。

从初始状态做 BFS，仅展开概率非零的可达状态。每条边同时记录：

- 转移概率；
- 采购、检测、装配、拆解、调换损失；
- 采购数、检测数、装配数、拆解数、调换数等事件奖励；
- 是否进入“最终交付合格品”的吸收态。

关键实现规则：坏成品拆解后，子件保持原真实质量和已获得的信息；不得重新独立抽样质量。若不拆解则丢弃，补产从缺失物料状态重新开始。

## 3.3 吸收性与线性求解

对每个策略构造瞬态转移矩阵 $P_d$、即时成本矩阵/向量。先做两层检查：

1. 图上寻找没有吸收泄漏的可达闭合强连通分量；
2. 数值计算 $\rho(P_d)$ 和吸收裕度 $1-\rho(P_d)$。

通过后求解

$$
(I-P_d)X_d=B_d,
$$

其中 $B_d$ 把总成本分项和事件计数拼成多右端矩阵。使用 LU/稀疏 LU 求解，不显式求逆。初始状态行给出一笔订单的期望成本和事件次数，利润为售价减总成本。

残差门为

$$
r_d=
\frac{\|(I-P_d)X_d-B_d\|_\infty}
{\|I-P_d\|_\infty\|X_d\|_\infty+\|B_d\|_\infty}
\le10^{-10}.
$$

近非吸收时依次使用缩放、迭代改进和高精度复核；不能人为截断循环来制造有限利润。

## 3.4 主伪代码

```text
results <- []
for policy in all_binary_vectors(length=4):
    graph <- build_reachable_state_graph(policy, case)
    if has_closed_nonabsorbing_SCC(graph):
        results.append(NON_ABSORBING)
        continue
    P, B <- assemble_transition_and_rewards(graph)
    if spectral_radius(P) >= 1:
        results.append(NON_ABSORBING)
        continue
    X <- solve(I-P, B)
    verify_probability_rows_and_linear_residual(P, X, B)
    results.append(profit_and_accounting(X, initial_state))
best <- all feasible policies within tie_tolerance of max(profit)
```

并列容差采用

$$
|\Pi_i-\Pi_j|\le10^{-8}\max(1,|\Pi_i|,|\Pi_j|).
$$

主目标保持利润最大；若并列，可把动作更少作为透明次级准则。

## 3.5 复杂度

若单策略瞬态状态数为 $S_2$，最坏稠密上界为 $O(16S_2^3)$；本题规模很小，正确性和对账优先于元启发式速度。

# 4. Q3 算法：装配树局部核 + 65536 精确搜索

## 4.1 决策位序

```text
bits 0..7   零件 1..8 是否检测
bits 8..10  半成品 1..3 是否检测
bit 11      成品是否检测
bits 12..14 半成品 1..3 是否拆解
bit 15      成品是否拆解
```

共 $2^{16}=65536$ 个固定策略。位序必须写入元数据，所有函数共享同一解码器。

## 4.2 后序局部核

对装配树做后序遍历。每个节点 $v$ 的核表示

$$
K_v^{\pi_v}:
(\text{子件质量与信息状态})
\mapsto
(\text{父件质量、成本、事件数、回流状态}).
$$

算法顺序：

1. 叶节点核：生成新购质量、执行检测、坏件补购，保留已知良件；
2. 半成品核：组合直接子件核，支付装配/检测/拆解成本，处理局部回流；
3. 根节点核：组合三个半成品核，加入市场退换和最终交付吸收态；
4. 对每个局部核执行概率守恒、吸收性和奖励方程校验；
5. 以 `(子树结构哈希, 参数哈希, 局部策略签名, 假设版本)` 缓存。

同一个物理状态只有在未来转移与奖励完全相同时才能合并。信息不同但期望恰好相同的状态不能合并。

## 4.3 全策略求解

```text
tree <- validate_and_topologically_sort(product_tree)
cache <- empty
for strategy_id in 0..65535:
    policy <- decode(strategy_id)
    root_kernel <- compose_postorder(tree, policy, cache)
    if any local/global closed nonabsorbing loop:
        record NON_ABSORBING
    else:
        solve local/global reward equations
        audit material balance and cost breakdown
        record exact profit
sort deterministically by strategy_id
select global profit maximum with tie tolerance
```

给定实例必须完成 65536 个策略的完整覆盖；运行慢不是改用 GA/SA 的理由。只有推广后策略位数使完整枚举不可承受时，才升级为分支定界或近似 DP，并降低最优性称谓。

## 4.4 物料守恒

每次父节点装配消耗每个直接子件各 1 件；拆解一次只返回每个直接子件各 1 件。对节点 $u$，应检查

$$
E[N_u^{\rm acquired}+N_u^{\rm returned}]
=E[N_u^{\rm consumed}+N_u^{\rm scrapped}+N_u^{\rm terminal\ inventory}].
$$

一笔订单终止后主线不保留期末库存，因此右侧期末库存为 0。若采用跨订单库存模型，必须新建模型版本，不能在当前公式中暗含库存价值。

## 4.5 复杂度

设策略数 $D=65536$、缓存后一次根核组合与求解成本为 $C_{\rm kernel}$，则

$$
T=O(D\,C_{\rm kernel}).
$$

按固定策略 ID 分片并行可以加速，但归并必须按 ID 排序，避免调度顺序改变结果。

# 5. Q4 算法：联合置信集合传播与策略稳定性

## 5.1 输入门禁

每个质量参数 $p_j$ 必须提供：

```text
parameter_name
N_j                 # 有效样本量
K_j                 # 次品数
sampling_unit       # component / all-inputs-good assembly
stopping_rule       # fixed_n / sequential
inspection_error    # 主线为 perfect，若非完美须另建观测模型
```

内部节点次品率必须来自“直接子件均确认合格”的条件试装数据。若把普通终检坏品率当作条件装配次品率，会与上游零件次品重复计算，直接返回 `INVALID_CONDITIONING`。

题面没有给具体 $(N_j,K_j)$，因此本阶段只冻结算法。只给点估计百分比而不给样本量时，不能计算区间宽度，也不能给唯一 Q4 策略。

## 5.2 同时置信集合

设质量参数个数为 $J$，总错误概率为 $\alpha_{\rm fam}$。采用 Bonferroni 分配

$$
\alpha_j=\alpha_{\rm fam}/J.
$$

- 固定样本：每个参数使用 Clopper–Pearson 精确二项区间；
- 数据依赖停止/持续查看：使用任意停止有效的 Bernoulli 置信序列；
- 构造联合矩形集合
  $$
  \mathcal U=\prod_{j=1}^J[L_j,U_j].
  $$

Bonferroni 可能保守，但覆盖解释透明；只有在有明确联合抽样结构时才改用更紧的同时区间。

## 5.3 第一层：点估计与场景筛选

先以 $\widehat p_j=K_j/N_j$ 调用 Q2/Q3 精确评价器，得到点估计最优策略。再生成：

- 中心点；
- 每个参数的一次单端扰动；
- Q2 的全部 $2^3=8$ 个角点；
- Q3 的全部低阶组合极端场景以及确定性 Sobol 点；
- 由局部最坏搜索发现的反例点。

每个场景都重新完成策略比较，形成候选集合 $\mathcal C$、策略切换图、利润经验包络和最大观测遗憾。此层只用于筛选和找反例，状态为 `WARN_NUMERICAL_STABILITY`，不能单独证明“整个置信集合内稳定”。

## 5.4 第二层：区间分支定界认证

对参数子盒 $B\subseteq\mathcal U$，用区间运算生成 $P_d(B)$、$c_d(B)$，并用区间线性求解/Krawczyk 算子包络

$$
V_d(B)\supseteq\{(I-P_d(\mathbf p))^{-1}c_d(\mathbf p):\mathbf p\in B\}.
$$

由此得到策略利润区间 $[L_d(B),U_d(B)]$。算法按以下规则递归：

1. 若某候选 $d^*$ 满足 $L_{d^*}(B)>\max_{d\ne d^*}U_d(B)$，则 $d^*$ 在该子盒稳定，停止细分；
2. 若目标是 max–min，且某策略在 $B$ 的利润上界低于当前最好最坏利润下界，则剪枝；
3. 否则按标准化区间宽度或利润梯度上界最大的参数二分；
4. 直到所有子盒获证、发现策略交叉反例，或达到宽度/节点预算。

固定策略的灵敏度可由

$$
\frac{\partial V}{\partial p_j}
=(I-P)^{-1}
\left(\frac{\partial c}{\partial p_j}
+\frac{\partial P}{\partial p_j}V\right)
$$

计算，用于选择分裂维度和构造 Lipschitz 上界，但点梯度本身不是全局证书。若运行环境没有可靠区间线性代数，允许退化为多起点连续优化与密集场景检查，但状态必须保持 `WARN_NUMERICAL_STABILITY`。

## 5.5 第三层：输出稳定性，而不是强行选择复杂模型

对每个策略报告

$$
\Pi_-(d)=\min_{\mathbf p\in\mathcal U}\Pi(d;\mathbf p),
\qquad
\Pi_+(d)=\max_{\mathbf p\in\mathcal U}\Pi(d;\mathbf p),
$$

并报告：

- 点估计最优策略及其利润区间；
- 在 $\mathcal U$ 内可能最优的策略集合；
- 策略切换反例和对应参数；
- 最大遗憾
  $$
  R(d)=\max_{\mathbf p\in\mathcal U}
  [\max_{d'}\Pi(d';\mathbf p)-\Pi(d;\mathbf p)];
  $$
- 稳定区域覆盖比例（数值量）和认证状态（逻辑量）。

决策规则按以下门禁使用：

1. 若同一策略在整个 $\mathcal U$ 内严格最优，直接推荐该稳定策略；
2. 若策略交叉，先报告不稳定性，不擅自把保守偏好塞进题意；
3. 企业声明“保底利润优先”后，才采用 $\arg\max_d\Pi_-(d)$；
4. 企业声明“避免选错损失”后，可采用最小最大遗憾；
5. 有可信先验时，Beta 后验期望利润可作为挑战者，但不能取代频率学主报告。

## 5.6 Q4 伪代码

```text
records <- validate_counts_and_conditioning(raw_evidence)
U <- simultaneous_confidence_box(records, family_error)

nominal <- solve_Q2_or_Q3(p_hat)              # 精确枚举
scenarios <- deterministic_screening_design(U)
scenario_results <- solve_all_scenarios(scenarios)
C <- policies_optimal_or_near_optimal_somewhere(scenario_results)

certificate <- interval_branch_and_bound(U, C, all_policies, evaluator)
if certificate.proves_one_policy_dominates:
    decision <- stable_policy
elif certificate.finds_crossing:
    decision <- report_candidate_set_and_regret
else:
    status <- WARN_NUMERICAL_STABILITY
    decision <- no_unique_certified_policy

if enterprise_risk_rule_is_declared:
    apply_the_declared_rule_using_certified_or_labeled_bounds
```

## 5.7 复杂度与可扩展路径

Q2 只有 3 个不确定参数和 16 个策略，角点筛选与区间细分都很轻。Q3 有 12 个参数和 65536 个策略，应先用场景评价筛出小候选集，再对候选做认证，同时用利润上界剪除其余策略。

若认证预算耗尽，输出未决子盒、当前利润上下界和最可能切换的参数，不把数值搜索包装成严格稳健结论。

# 6. 最小等价实例与验证门

## 6.1 Q1 P1

| 测试 | 预期 |
|---|---|
| 固定二项 oracle | 精确复现第 2.2 节四行，误差 $\le10^{-9}$ |
| 小 $N_{\max}$ 完全路径枚举 | 与 DP 的接收、拒收概率及 ASN 一致 |
| 概率守恒 | 所有 OC 点 $P(A)+P(R)=1\pm10^{-10}$ |
| OC 单调性 | $P_p(A)$ 随 $p$ 非增 |
| 截尾 | $N_{\max}$ 后继续质量严格为 0 |
| 风险 | $P_{p_0}(R)\le0.05$ 且 $P_{p_1}(A)\le0.10$ |

## 6.2 Q2 P1

| 测试 | 预期 |
|---|---|
| $p_1=p_2=p_f=0$ | 无检测时一次装配必成功，成本为两零件采购加一次装配 |
| 无检测一次良率 | 等于 $(1-p_1)(1-p_2)(1-p_f)$ |
| 无回流退化 | Markov 求解与几何更新闭式解一致 |
| 拆回坏件质量保留 | 不会被重新当作独立新购件 |
| 对账 | 分项成本之和等于总成本，事件数非负 |
| 非吸收反例 | 可达闭合坏件复装循环被标为 `NON_ABSORBING` |

## 6.3 Q3 P1

| 测试 | 预期 |
|---|---|
| 全不检测一次良率 | $0.9^{12}=0.282429536\ldots$ |
| 二零件子树退化 | 与 Q2 对应策略和成本一致 |
| 策略覆盖 | 唯一 ID 恰为 65536，无重复、无遗漏 |
| 物料守恒 | 每个叶/半成品的残差在容差内 |
| 边界概率 | $p=0$、$p\to1$ 时状态与吸收检查合理 |
| 近非吸收 | 触发高精度半径和奖励方程复核 |

## 6.4 Q4 P1

| 测试 | 预期 |
|---|---|
| 退化区间 $L_j=U_j=\hat p_j$ | 完全恢复 Q2/Q3 点估计结果 |
| Q2 三参数角点 | 场景层覆盖全部 8 个角点 |
| 固定样本覆盖 | 单参数 Clopper–Pearson 边界与独立库一致 |
| 序贯证据 | 不得错误调用固定样本区间 |
| 嵌套集合 | 对嵌套收缩的 $\mathcal U$，已证明稳定的策略不应变为不稳定 |
| 反例搜索 | 人工构造两策略切换时能输出交叉点而非伪称唯一稳健策略 |
| 无区间求解器 | 明确降级为 `WARN_NUMERICAL_STABILITY` |

# 7. 现有代码复用与缺口

| 现有模块 | 审计结论 | 新版处理 |
|---|---|---|
| `代码/q1/fixed_binomial_plan.py` | 可复用精确固定基线 | 保留 |
| `代码/q1/exact_path_dp.py` | 可复用有限截尾路径 DP | 保留 |
| `代码/q1/run_q1.py` | 当前是预声明局部阈值与网格 ASN 搜索 | 保留 `SUCCESS_LOCAL_CALIBRATION` 限定；不能写全局最优 |
| `代码/q2/model.py` | 状态、信息保留、吸收检查和奖励方程与主模型一致 | 作为 Q2/Q4 唯一点评价器 |
| `代码/q3/model.py` | 局部核、回流、全策略接口与主模型一致 | 作为 Q3/Q4 唯一点评价器 |
| `代码/q4/simultaneous_cs.py` | 固定样本区间和序贯 CS 可复用 | 保留并补覆盖测试 |
| `代码/q4/batch_evaluators.py` | 可用于场景筛选，但须与 Q2/Q3 精确评价器逐点交叉验证 | 作为加速层，不作独立真值源 |
| `代码/q4/run_q4.py::robust_audit` | 直接把“所有参数上端点”当最坏点，缺乏一般性证明 | 不作为新 Q4 主结果；由区间 BnB/有标签数值审计替代 |
| `代码/q4/exact_voi_dp.py`、`kg_rollout.py` | 回答追加抽样分配，需要额外先验和成本 | 降为可选企业扩展 |

不删除旧文件和旧结果；新版通过新 `run_id` 隔离，避免把既有演示结果冒充重算结果。

# 8. 运行产物规范

正式求解时写入新的

```text
results/<run_id>/
  inputs/
  q1/
    fixed_baseline.csv
    sequential_plan.csv
    operating_characteristics.csv
    calibration_audit.csv
  q2/
    all_policies.csv
    best_policies.csv
    state_audit.csv
  q3/
    all_policies.parquet
    best_policies.csv
    material_balance.csv
  q4/
    simultaneous_intervals.csv
    scenario_screen.csv
    stability_certificate.json
    regret_envelope.csv
  validation/
    review.json
  summary.json
```

每次运行保存输入哈希、策略位序、假设版本、随机设计种子（若使用 Sobol scramble）、依赖版本、容差和状态码。旧结果目录不得原地覆盖。

# 9. 下一步执行顺序

1. 先由企业/答题者冻结 Q1 的 $p_1$ 与 $N_{\max}$ 口径；否则只做四档敏感性。
2. 运行 Q2 的 6 情形 × 16 策略，并完成状态/成本/吸收性对账。
3. 运行 Q3 的 65536 策略，先通过 Q2 退化和 $0.9^{12}$ 基准。
4. 收集 Q4 每个节点的 $(N_j,K_j)$、抽样条件和停止规则。
5. 生成联合置信集合，先做场景筛选，再做区间认证；策略交叉时输出候选集与遗憾，不擅自选择风险偏好。

这一顺序已经满足“经典模型能完全覆盖时，不为追求复杂度而换模型”：Q1 用经典序贯验收，Q2/Q3 用有限状态 Markov 奖励与精确枚举，Q4 只把抽样不确定性传播进相同评价器。
