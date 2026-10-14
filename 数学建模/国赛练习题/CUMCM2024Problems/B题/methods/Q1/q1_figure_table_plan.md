# Q1 图表计划

状态：`FIGURES_RENDER_VERIFIED_TABLES_PENDING`  
模式：`submission`  
批准依据：使用者于 2026-09-09 确认“正文3项＋附录2项”的精简设计  
核心方法决策：`q1_method_choice_v2`  
核心结果裁决：`q1_final_result_verdict_v2`

## 1. 规划边界

本计划只使用 Q1 round3 已审查的确定性概率递推结果，不读取 B 题已有作答，不新增数据、不插值构造额外观测，也不改变 B1、M1、检测上限或真实次品率网格。当前尚无已渲染图形，`paper/` 目录也尚未建立；现有 CSV 和 JSON 是所有后续图表的唯一数值来源。

本阶段尚未生成 `frozen_numbers.json`，因此不手填 frozen claim ID。Type 3 图表先绑定人工裁决、源文件路径和 SHA-256；`solution-package-builder` 后续根据同一证据生成冻结编号。冻结前不得把计划状态误写成论文成品。

## 2. 需要图表支持的已验证结论

| Claim ID | 已验证结论 | 人工/证据追溯 | 是否需要视觉或精确表格 |
|---|---|---|---|
| C-Q1-01 | B1 在主预算1000下使用8个预定检查点，并以明确的累计次品数边界接收、拒收或继续 | `q1_method_choice_v2`；`decision_boundaries.csv` | 需要精确表格，便于直接实施 |
| C-Q1-02 | 在8%--12%的41个密网格点上，B1 的 ASN 和未决率均低于 M1；但全区间仅145点具有较低 ASN | `q1_final_result_verdict_v2`；`comparison.csv`；`dense_grid_summary.json` | 需要相对差值曲线，同时显示局部优势与全局代价 |
| C-Q1-03 | B1 缩窄高未决带，但在 \(\theta=0.10\) 时未决率仍为0.93641 | `q1_final_result_verdict_v2`；`operating_characteristics.csv` | 需要绝对未决率曲线，防止只展示相对优势 |
| C-Q1-04 | 三种 B1 上限方案不嵌套；从1000增至1100可在 \(\theta=0.107\) 处使未决率增加0.001337 | `q1_robustness_summary.json`；`q1_robustness_report.md` | 作为附录限制图，不占正文主图 |
| C-Q1-05 | 数值误差、错误控制、方向单调性和 round2 重合检查均通过 | `validation.json`；`q1_python_review.json` | 适合紧凑附录表，不需要诊断图 |

## 3. 最小交付集合

| ID | Qx | 类型 | 形式 | 一个核心结论 | 主要数据源 | 目标位置 | 当前状态 |
|---|---|---|---|---|---|---|---|
| Q1-T3-T01 | Q1 | Type 3 paper | 8行决策表 | B1 是可直接执行的预定分批验收规则 | `decision_boundaries.csv` | 方法与求解 | `PLANNED_FROM_VALIDATED_SOURCE` |
| Q1-T3-F01 | Q1 | Type 3 paper | 双面板差值折线图 | B1 的优势集中在阈值附近，不能外推为全局 ASN 优势 | `comparison.csv` | 结果分析 | `RENDER_VERIFIED` |
| Q1-T3-F02 | Q1 | Type 3 paper | 绝对未决率对比曲线 | B1 缩窄高未决带，但没有解决10%附近的高未决 | `operating_characteristics.csv` | 结果分析与局限性 | `RENDER_VERIFIED` |
| Q1-T4-F01 | Q1 | Type 4 appendix | 上限差值折线图 | 非嵌套末次检查导致上限增加时未决率可能局部上升 | `operating_characteristics.csv` | 附录稳健性 | `RENDER_VERIFIED` |
| Q1-T4-T01 | Q1 | Type 4 appendix | 验证摘要表 | 程序错误控制和数值核验达到预定阈值 | `validation.json`、`q1_python_review.json` | 附录验证 | `PLANNED_FROM_VALIDATED_SOURCE` |

正文只保留两幅图和一张表；附录保留一幅限制图和一张验证表。没有 Type 1 图，因为现有 JSON 已足够完成内部数值诊断；没有 Type 2 备选图，因为 M1 的比较已经是论文主结论不可缺少的组成部分。

## 4. Q1-T3-T01：B1 主预算决策表

数据筛选固定为 `method_id=B1`、`cap=1000`、`is_look=True`，只读取 `k,accept_max_defects,reject_min_defects`。表中使用“累计检测数”“接收所允许的最大累计次品数”“拒收所需的最小累计次品数”“继续区间”四列；字符串 `null` 必须显示为“无接收边界”，不能显示成0。

源表给出的8行边界为：

| 累计检测数 \(k\) | 接收上界 | 拒收下界 |
|---:|---:|---:|
| 10 | 无 | 5 |
| 20 | 无 | 7 |
| 40 | 无 | 10 |
| 80 | 2 | 16 |
| 160 | 7 | 27 |
| 320 | 20 | 47 |
| 640 | 47 | 85 |
| 1000 | 78 | 125 |

表下注明：累计次品数不高于接收上界则接收，不低于拒收下界则拒收，中间区域继续；1000件处的继续状态转为未决。该表只对应主预算1000，不能和900或1100的末次边界混用。

计划中的结构化派生表路径为 `results/Q1/reports/tables/q1_b1_decision_rule.csv`。它由源 CSV 机械筛选生成，随后由解决方案包写入正文表格；不把表格渲染成图片。

## 5. Q1-T3-F01：B1 相对 M1 的效率—未决权衡

采用上下两个共享横轴的面板，横轴均为完整 \(\theta\in[0,1]\)，数据仅取 `cap=1000`：

- 上面板绘制 \(\Delta\operatorname{ASN}=\operatorname{ASN}_{B1}-\operatorname{ASN}_{M1}\)；
- 下面板绘制 \(\Delta P_U=P_{U,B1}-P_{U,M1}\)；
- 两面板均绘制零基线、\(p_0=0.10\) 竖线，并淡色标出8%--12%窗口；
- 使用5%--15%局部嵌入视图呈现阈值附近变化，但主坐标必须保留完整0--1范围，避免只截取优势区间。

负值表示 B1 指标较低。图注必须同时陈述：8%--12%的41点两项差值均为负；全网格只有145点的 ASN 差值为负。网格点不带真实 \(\theta\) 权重，曲线不能解释成现实总体平均收益。

计划输出为 `paper/figures/q1_main_baseline_tradeoff.pdf` 和同名 PNG 预览。核心 claim 为 C-Q1-02，决策追溯为 `q1_final_result_verdict_v2`。

## 6. Q1-T3-F02：阈值附近绝对未决概率

横轴限定为 \(\theta\in[0.05,0.15]\)，纵轴为 \(P_U(\theta)\)，只使用 `cap=1000`。B1 使用主方法实线，M1 使用基线虚线；绘制 \(p_0=0.10\) 竖线。可绘制 \(P_U=0.9\) 的细水平参考线，但图注必须写明0.9仅为描述性集中阈值，不是人工验收标准。

图中标注 \(\theta=0.10\) 的两点：B1 为0.93641，M1 为0.96492；同时在图注说明 B1 的 \(P_U\ge0.9\) 网格区间为9.5%--10.7%，M1 为8.5%--11.5%。该图必须呈现绝对概率，不能只画相对改善，以免掩盖主方法仍有较高未决率。

计划输出为 `paper/figures/q1_undecided_probability_near_threshold.pdf` 和同名 PNG 预览。核心 claim 为 C-Q1-03，决策追溯为 `q1_final_result_verdict_v2`。

## 7. Q1-T4-F01：检测上限非嵌套效应

只绘制 B1，横轴取 \(\theta\in[0.08,0.13]\)。以 `cap=1000` 为参照，画出

\[
P_U^{(900)}-P_U^{(1000)},
\qquad
P_U^{(1100)}-P_U^{(1000)}.
\]

绘制零基线，并标注 \(\theta=0.107\) 处后一个差值为正0.001337。图注必须说明三种方案都有8次检查和相同逐次错误预算，但末次检查点分别为900、1000、1100，因此方案不嵌套；图形不能表述成“增加上限一般会增加未决率”。

计划输出为 `paper/figures/q1_cap_nonnesting_sensitivity.pdf` 和同名 PNG 预览。该图只进入附录，正文局限性段落引用即可。

## 8. Q1-T4-T01：验证摘要表

表格机械提取以下五项，不引入新的合格阈值：

| 检查 | round3观测值 | 已有判据 |
|---|---:|---:|
| 最大概率质量误差 | \(4.3743\times10^{-14}\) | \(\le10^{-10}\) |
| ASN 双路径最大误差 | \(3.7289\times10^{-11}\) 件 | \(\le10^{-8}\) 件 |
| 最大错拒概率 | 0.02823 | \(\le0.05\) |
| 最大错收概率 | 0.03920 | \(\le0.10\) |
| round2重合情景最大差 | 0 | \(\le10^{-10}\) |

另在表注中报告最大方向单调性误差 \(2.5535\times10^{-15}\)，并注明有限网格核验不能替代理论上的全参数错误控制证明。计划中的结构化派生表路径为 `results/Q1/reports/tables/q1_validation_summary.csv`，由解决方案包或表格生成步骤直接读取 JSON 字段。

## 9. 统一视觉规范与渲染检查

B1 在所有图中固定使用蓝色实线，M1 作为 baseline 使用灰色虚线；同一语义不得跨图换色。中文标签使用可嵌入字体，数学符号用一致的 \(\theta\)、ASN、\(P_U\)。白底、浅灰辅助线，禁止渐变、3D效果、装饰图标和双纵轴。

每幅图同时输出矢量 PDF 和 PNG 预览。渲染后必须检查：字体嵌入或可替代、图例不遮挡曲线、坐标和负号清晰、标注不越界、完整0--1与局部窗口的范围符合计划、源数据行数和筛选条件可复核。PNG 仅用于检查和预览，论文优先引用 PDF。

三幅图已按计划生成并通过上述检查；机器清单见 `paper/figures/q1_figure_manifest.json`，独立渲染记录见 `paper/figures/q1_render_check.json`。两张结构化派生表仍由后续 `solution-package-builder` 机械生成。

## 10. 明确排除项

不制作模型流程装饰图、3D曲面、1001行全量正文表、单独的运行时间图或概率质量误差曲线。它们不会比公式、紧凑验证表或现有运行摘要增加新的论证价值。代表性参数值不再另做一张正文性能表，避免与两幅主图及正文数值重复。

## 11. 源证据快照

| Source artifact | SHA-256 |
|---|---|
| `results/Q1/experiments/round3/tables/decision_boundaries.csv` | `14cec7775680212b86ac58c73e782681b293dbb25ea1c110ca0b40141640caaf` |
| `results/Q1/experiments/round3/tables/operating_characteristics.csv` | `95e5e297f5118fb06a1529727303a48875a5cd2553f0c3e6bba26aa6a05166c8` |
| `results/Q1/experiments/round3/tables/comparison.csv` | `ce4fd627464e3f366fff7da408fc45238f277c53e96dcd61fdc38fd7b8af9074` |
| `results/Q1/experiments/round3/tables/near_threshold_dense.csv` | `9e62b0cb7d56c311f81bef34836977845f51241b74392c92d270534eb1168722` |
| `results/Q1/experiments/round3/metrics/validation.json` | `1464f1140b7959049122c9aaf18f107855d541a485903f4949f3ce02a32982a5` |
| `results/Q1/experiments/round3/metrics/dense_grid_summary.json` | `aa6b75eb8840be7958df83caa0b4ed0a609c053127b6872e4352771d3011dee9` |
| `results/Q1/reports/q1_final_result_analysis.md` | `2dc141f6c04f05798282a228b4d222bcae0de00cb8b3d393508b74a6a21e066c` |
| `robustness/Q1/q1_robustness_summary.json` | `49736fc3485ab1781cafa562f2d3211bfd04d3e4ddbf9f4d500e0e6b1afc9101` |
| `methods/Q1/q1_final_method_explanation.md` | `dfb77ee35d5e17f7481adf484de8c16448067a8435b5545bf9535fd06c4e5377` |
| `methods/Q1/q1_decisions.jsonl` | `246bf721b829deb3698444645020697ba782c43f19a6bd1e7f18e30860ee0447` |

## 12. 下一阶段

下一 skill 为 `math-figure-generator`。它只生成并渲染验证 Q1-T3-F01、Q1-T3-F02 和 Q1-T4-F01；两张表保持结构化表格，不转成图片。所有 Type 3 产物在 `solution-package-builder` 生成冻结编号前均标记为“已验证来源、尚未冻结”。
