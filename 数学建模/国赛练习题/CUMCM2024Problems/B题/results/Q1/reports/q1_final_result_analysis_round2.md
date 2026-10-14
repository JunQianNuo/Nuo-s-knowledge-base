# Q1 最终结果分析

状态：`AWAITING_HUMAN_RESULT_VERDICT`  
模式：`submission`  
生成时间：2026-09-08T14:57:08+08:00

## 1. 证据范围与比较口径

本报告汇总 Q1 第二轮已审查结果。主方法为 B1（预定分批精确二项检验），可用基线为 M1（均匀 Beta--二项混合置信序列），对应人类方法选择 `q1_method_choice_v2`；建模者随后在 `q1_round2_stability_scope` 中决定保留 B1。两种方法均采用标称次品率 (p_0=0.10)、拒收侧错误上限 (alpha_R=0.05)、接收侧错误上限 (alpha_A=0.10)，并允许达到检测上限后仍输出“未决”。

比较使用相同的 77 个真实次品率情景和 (N_{\max}=900,1000,1100) 三个预算切片。核心数值由有限状态概率递推确定性计算，不含蒙特卡洛随机误差；`random_seed=2026` 仅为统一输出字段，实际 `seed_used=false`。题目没有提供真实抽检序列，因此下列结果是 A1“检测无误”和 A2“近似独立同分布 Bernoulli 抽样”条件下的理论工作特性，不是实测性能。

主要来源：

- `results/Q1/experiments/round2/run_summary.json`
- `results/Q1/experiments/round2/tables/operating_characteristics.csv`
- `results/Q1/experiments/round2/tables/comparison.csv`
- `results/Q1/experiments/round2/tables/near_threshold_summary.csv`
- `results/Q1/experiments/round2/metrics/validation.json`
- `results/Q1/experiments/round2/metrics/sensitivity.json`
- `robustness/Q1/q1_robustness_summary.json`
- `code/Q1/reviews/q1_python_review.json`

## 2. 数值正确性与错误控制

第二轮运行状态为 `success`，独立代码审查结论为 `PASSED`。主动测试 6 项通过，重新执行 `python -B code/Q1/q1_run_round2.py --verify-existing` 后保存结果完全复现。六个“方法--上限”组合中的最大概率质量误差为 (4.952\times10^{-14})，两种方式计算 ASN 的最大差为 (4.138\times10^{-11}) 件；第二轮与第一轮同一方法、上限和参数组合的最大数值差为 0。这些检查支持实现与既定公式一致，但不等价于验证 A1、A2 在真实生产中的成立。

在已检查网格上，B1 的最大错误拒收概率为 0.02504，小于 0.05；含边界的最大错误接收概率为 0.03920，小于 0.10。M1 对应最大值分别为 0.02823 和 0.00702，也未超过规定水平。有限网格检查提供数值佐证；全参数错误控制仍来自精确二项尾检验、随机单调性和 Bonferroni 联合界的理论论证，而不是由这 77 个点“证明”。

上述数值分别来自 `metrics/validation.json` 和 `robustness/Q1/q1_robustness_summary.json`。

## 3. 主方法与基线的核心比较

在主要预算 (N_{\max}=1000) 下，阈值附近结果如下。ASN 单位为件，概率保留为百分比以便解释。

| 真实次品率 | B1 ASN | M1 ASN | B1 未决率 | M1 未决率 | 证据含义 |
|---:|---:|---:|---:|---:|---|
| 8% | 797.06 | 908.90 | 48.46% | 81.08% | B1 同时减少平均检测量和未决概率 |
| 10% | 959.33 | 967.74 | 93.64% | 96.49% | B1 仅相对改善；两者大多未决 |
| 12% | 859.39 | 896.18 | 61.18% | 82.77% | B1 同时减少平均检测量和未决概率 |

数据来自 `tables/near_threshold_summary.csv`。在 (	heta=0.10) 时，B1 的接收、拒收、未决概率分别为 0.03855、0.02504、0.93641，实际在上限前作出接收或拒收结论的概率仅为 0.06359。因此，结果只支持“B1 在相同条件下比 M1 少一些未决”，不支持“B1 已解决临界次品率附近的判定问题”。

在 (N_{\max}=1000) 的全部 77 个网格点中，B1 的 ASN 在 51 点低于 M1，未决概率在 72 点低于 M1，两项同时更低的有 51 点。B1 并非全面支配 M1：在 (	heta=0.20) 时，B1 与 M1 的 ASN 分别为 121.32 件和 105.35 件，M1 更快；两者未决概率都已接近 0。故不能声称 B1 全局最省检测量，也不能把有限网格计数解释成真实次品率分布下的平均优势，因为没有给定各 (	heta) 的权重。

全网格计数和反例来自 `robustness/Q1/q1_robustness_summary.json`，逐点原始值来自 `tables/comparison.csv` 与 `tables/operating_characteristics.csv`。

## 4. 参数敏感性与输出集中

对真实次品率作相对正负 10% 扰动时，B1 最大三态分布总变差距离为 0.44464，出现在 (0.13\rightarrow0.117)；ASN 相对增加 24.89%。M1 最大总变差距离为 0.43900，出现在 (0.14\rightarrow0.126)；ASN 相对增加 40.39%。两组扰动都没有跨越 (p_0=0.10)，说明变化不能全部归因于穿过标称阈值。概率质量主要在“拒收”和“未决”之间转移，反映的是靠近阈值时检出能力迅速下降，而不是数值递推不稳定。

从 (	heta=0.10) 到 0.09 和 0.11 的 B1 总变差距离分别为 0.12819 和 0.09254，对应 ASN 相对变化分别为 -4.04% 和 -1.96%。目前没有人为规定可接受的总变差或最低判定概率，因此只能将其报告为敏感区，不能据此自动否决或宣称稳定。

两种方法在端点情景的未决概率均为 0，且三类输出均曾出现，所以不存在全局“永远未决”的退化；但 B1 在 (p_0) 处 93.64% 的未决概率构成明显的局部输出集中。敏感性数值来自 `metrics/sensitivity.json`，解释及集中检查来自 `robustness/Q1/q1_robustness_summary.json`。

## 5. 检测上限与检查表风险

B1 在三个预算下均设置 8 次检查，共享前七个检查点 (10,20,40,80,160,320,640)，第八个检查点分别替换为 900、1000 或 1100。因检查次数相同，每次接收侧和拒收侧错误预算始终分别为 0.0125 和 0.00625；三张检查表的差异来自末次检查点，不是 Bonferroni 分配改变。

三张方案并不嵌套，所以增加上限不保证未决概率逐点下降。例如 (	heta=0.105) 时，(N_{\max}=1000) 和 1100 对应的未决概率分别为 0.92615 和 0.92740，增加 0.00125；ASN 则由 956.75 件增至 1050.92 件。该现象说明上限必须与完整预定检查表一起说明，不能把 1100 简单理解为在 1000 方案之后“多检查一次”，也不能把上限作为脱离未决率的单独优化指标。证据来自 `tables/decision_boundaries.csv`、`tables/operating_characteristics.csv` 和 `robustness/Q1/q1_robustness_summary.json`。

## 6. 不确定性、适用范围与不能支持的结论

本轮数值误差已被控制到远小于展示精度，但模型不确定性仍然存在。B1 的理论保证适用于抽样前固定检查表、近似独立同分布 Bernoulli 抽样且检测无误的情形；检查表不能根据中途结果临时修改。若批量有限且抽样占比不可忽略、缺陷存在聚集或相关、检测存在误判，则当前概率保证和工作特性不能直接外推，必须重新建模或校准。

(N_{\max}=900,1000,1100) 是实验预算切片，并非题目给出的最大检测量，也不是优化得到的唯一最优上限。当前结果不能支持以下表述：B1 对所有真实次品率都优于 M1；B1 给出了所有合法抽样规则中的全局最少检测次数；任意批次都能在有限次数内得到二元结论；95% 和 90% 是对当前批次合格概率的后验陈述；模型已由真实生产数据验证。

可支持的结论限于：在上述假设、固定检查规则、相同错误约束和已计算参数网格内，B1 满足数值错误控制检查，并在大多数已检查点降低未决概率；其主要代价是阈值附近仍高度未决，且检查上限变化具有离散、非嵌套效应。

## 7. Fallback 与提交裁决状态

当前没有条件性备用方法，`fallback_id=null`，也没有触发归档或自动换模。M1 保留为可用统计基线。人类已通过 `q1_round2_stability_scope` 决定保留 B1，但尚未针对本提交级最终结果分析记录独立的 `result_verdict`。在该裁决写入 `methods/Q1/q1_decisions.jsonl` 前，本报告中的数字不冻结，且不得据此进入最终方法详解或论文材料包。

## 8. 证据快照

| Artifact | SHA-256 |
|---|---|
| `results/Q1/experiments/round2/run_summary.json` | `86ab5e08780de41472c0ee47b68516c90a70a9093a79ee29905c30152dd40b38` |
| `results/Q1/experiments/round2/tables/near_threshold_summary.csv` | `b8dd34732382d8df3c8bbd3a6fd65596fbbd6413e89a800837a3fe620505e92e` |
| `results/Q1/experiments/round2/tables/comparison.csv` | `a9e43ab407249b92632a1bf22ba4326aebeb8f37c3145929370e4ddecc72ebc8` |
| `results/Q1/experiments/round2/tables/operating_characteristics.csv` | `594a28988925111add06b2c626c70e448a818c752d93c1735eca880ac41330d2` |
| `results/Q1/experiments/round2/metrics/validation.json` | `fc2727845cf74e0c24d645a1507ecb630cc9926a61d46a655633994d1e67b830` |
| `results/Q1/experiments/round2/metrics/sensitivity.json` | `531cece6d0bfcd72f4647d85b341e88f0f3be488d4895c7cae17c5b0f253090a` |
| `robustness/Q1/q1_robustness_summary.json` | `ee455fa6d3a8a6d9d508fd89953b3035ffd381627345552e761ea99c14f0b410` |
| `code/Q1/reviews/q1_python_review.json` | `32d67a5e20b564f68ab904f466620627526d825b3bf7ffdd3aa659e81e75df5f` |
| `methods/Q1/q1_decisions.jsonl`（报告生成前） | `43dd768e06540f36a2a6e74e2d7ecff1a960dfa573b009fa4aa20664b61411e3` |
