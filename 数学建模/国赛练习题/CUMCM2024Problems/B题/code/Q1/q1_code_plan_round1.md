# Q1 第一轮代码规划

状态：PLANNED；尚未生成或运行正式求解代码。人类决策：q1_method_choice，主方法M1，理由原文“更加灵活”；B1为可用对照，无备用方法。保持learning + lean。

## 目标与工程范围

实现方法卡已定义的M1均匀混合置信序列与B1预定分批精确二项检验，输出整数判定边界及参数化ASN、接收/拒收/未决概率。公式与符号以 methods/Q1/q1_method_card.md、planning/symbol_table.md 为准，不改变混合权重、错误预算或停止语义，不开展新候选搜索。

采用Python、round1。语言是AI沿用仓库默认Python路径和现有探针运行环境的工程安排，不记录成人类偏好；若用户指定MATLAB则迁移实现合同，不重选数学方法。本轮只做理论性能计算，不生成实测序列、论文、冻结数字或MATLAB副本。

## 输入与配置合同

| 来源 | 必需内容 | 校验、单位和边界 |
|---|---|---|
| workspace/data_clean/q1_statement_parameters.csv | nominal_defect_rate、reject_confidence、accept_confidence | 恰一行；本题0.10、0.95、0.90；无量纲小数，拒绝缺失、非有限和越界值 |
| methods/Q1/probes/probe_config.json | M1固定Beta(1,1)混合，B1首检查点10、倍增规则、参数网格 | 沿用筛选配置，不修改探针文件，不将设计参数称作题给值 |
| methods/Q1/q1_decisions.jsonl | DECIDED q1_method_choice，M1主方法和B1对照 | 运行前核对人类记录与证据存在 |
| workspace/data/data_profile.json、planning/model_assumptions.md | Q1数据画像、A1/A2 | iid Bernoulli及无误检测属于适用条件，实测独立性未验证 |

主预算1000件，预算敏感性900、1100件；这些只是首轮理论性能切片，不是题给上限、优化目标或最终采购约束。真实次品率网格沿用probe_config的theta_base及0.9/1.1相对乘数，截到[0,1]、12位小数去重，得到与探针一致的77点。theta是情景参数而非估计或真实观测。保持题给p0、95%/90%不变，不基于结果挑选有利网格。

B1每种预算下先确定从10倍增并补上限的全部检查点，再分配每侧错误预算；检测开始后不得改表。M1每件均查看，早期边界不随上限改变。两法均首次判定即停止，上限未越界输出未决，不强制二分。

标准摘要保留random_seed=2026作为运行合同字段，同时写randomness="none"、seed_used=false；本轮是确定性概率递推，无需为使用种子而产生模拟样本。

## 计算合同

使用单一入口 code/Q1/q1_run.py 和测试 code/Q1/test_q1_model.py 即可。可复用探针经复核的数值核心，但必须重新运行生成正式结果，不能复制探针JSON充当新实验。

M1用对数阶乘或lgamma计算方法卡的log E_k(p0)，同时核对X_k/k位于p0哪一侧，再按相应1/alpha严格越界判定。导出每个k的最大接收次品数及最小拒收次品数；边界不存在写null，不用合法计数0替代。少量边界邻点通过独立二分反演置信集检查L/U与整数判定一致，端点按连续延拓处理，不必对全部状态重复求根。

B1在预定检查点计算精确二项上下尾，分别与alpha_A/K和alpha_R/K严格比较。非检查点写is_look=false、无判定边界；不得反复使用未经错误分配的单次95%/90%置信界。

公共求值器按“累计件数、累计次品数、尚未停止概率质量”递推，接收和拒收质量吸收。每次观测前的存活概率之和给出ASN；另外以吸收时刻及最终未决质量独立累计停止时间的一阶和二阶矩，核对ASN并得到SD_T_star。使用float64及稳定对数公式，判定前不舍入。

## 输出合同

以下为未来运行产物，当前不代表存在；基目录为 results/Q1/experiments/round1/。

| 输出 | 必需字段或内容 |
|---|---|
| tables/decision_boundaries.csv | method_id、cap、k、is_look、accept_max_defects、reject_min_defects；仅适用于尚未停止路径 |
| tables/operating_characteristics.csv | method_id、cap、theta、ASN、SD_T_star、P_A、P_R、P_U |
| tables/comparison.csv | cap、theta、两法ASN和P_U、M1减B1差值；不得只按ASN写全面胜负 |
| metrics/sensitivity.json | 参数相对±10%下三态概率分布TV、ASN变化、是否跨越p0，以及预算变化效果 |
| metrics/validation.json | 数值核验、边界互斥、独立核算、概率单调性、错误概率网格检查、耗时和失败项 |
| run_summary.json | 实际执行状态、角色、完整配置、输入/代码哈希、环境、指标、风险和输出清单 |

检测数和ASN单位为件，概率为[0,1]小数；P_U表示未决概率，不能与上置信界U混淆。figures/留给后续图表规划，本轮figure_files=[]，不得登记不存在的图表。logs/仅在失败或复现异常需要时创建，不写成功长日志或重复README。

run_summary.json必含schema_version、question="Q1"、round="round1"、implementation_target="python"、random_seed、approved_decision_id="q1_method_choice"、methods、comparison、fallback_trigger、environment。methods分别记录M1/main和B1/usable_baseline；可共用脚本，但各自有status、execution_time_seconds、input_files、output_files、figure_files、metrics_summary、warnings和errors。无备用，fallback_id=null、observed=false。在risk_conditions单列仍未解决的适用性/稳定性限制，不伪装成备用激活。

正式输出写入前核对目录是否已有内容；遇到来源不明的既有结果不得读取历史作答或覆盖。原始数据、探针及决策历史只读。

## 风险条件和调整触发

方法选择只授权首轮验证，不将探针CONDITIONAL自动改成PASS。持续保留A1/A2适用范围、阈值附近未决集中和敏感区间。TV是三态概率分布变化，不是同一批次的方案翻转率；概率单调也不等于变化足够小。

必须成对报告ASN和未决概率。不得新增人类未给定的TV上限、最低判定率或真实次品率权重，也不能声称全局最少、普遍稳定或任意批次有限次必能判定。数据仍缺失时，只输出理论情景结果。

数值核验失败、判定重叠、错误概率超界或每方法超过60秒/跟踪分配内存256MB预算，记录失败并停止正常交付，不静默换法。真实抽样假设变化则退回假设审查；使用者不接受性能曲线则进入decision-prompt-builder讨论调整，不自动扩展复杂模型。

## 验证及后续审查合同

- syntax：入口及测试可解析，无导入即运行副作用。
- input_contract：校验CSV字段/行数、概率域、整数预算和人类方法记录；缺少实测输入时不虚构记录。
- method_alignment：两法公式、置信方向、严格比较、检查时点、吸收逻辑与方法卡一致；接收为低端、拒收为高端，边界不重叠。
- reproducibility：12件全部二进制路径独立枚举核对（B1包含10、12两次检查），误差不超过1e-10；核对正式整数边界及邻点；固定配置结果与原探针对齐，保存代码/输入哈希。重新运行的数值需一致，耗时不要求一致。
- output_contract：概率和误差不超过1e-10；概率在容差内属于[0,1]，ASN在[1,cap]；双重ASN核算误差不超过1e-8；theta=0/1未决为0；接收率随theta非增、拒收率非减。网格上错拒/错收分别不超过5%/10%，但网格检查不替代理论保证。

生成器自检不能替代python-code-reviewer独立审查；正式执行前不得写success或PASS产物。原探针对照不一致时先定位原因，不修改旧证据迁就新结果。

## 环境和交接

已知可用Python 3.12.13、NumPy 2.3.5；实际执行时复核版本。不依赖SciPy，不下载新库。解释器：
C:/Users/Nuo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe。

预期在既有每方法60秒预算内，实际耗时待验证。下一skill为python-model-code-generator，只实现M1与B1；然后code-reviewer → python-code-reviewer。当前仅完成决策与规划，不进入正式结果分析或论文阶段。

