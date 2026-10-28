# topics → MOC 架构修正验收（2026-10-28）

本报告记录用户新增规则的实际实施结果，替代此前以普通原子笔记充当主题锚点的做法；早期验收报告保留为历史快照。

## 已确定的架构与已完成实现

- concept / proposition / method 并列；topics 仅表示主题归属，目标必须实际存在、唯一解析、非系统、属性合法并显式声明 role: moc。
- prerequisites / about / uses / related 表达原子之间的语义关系。此次未新增或改写这四类关系，也未将旧锚点机械转换为 related。
- 历史 type: MOC 仍兼容读取，但不能仅凭这个旧值成为新 topics 目标。知识网络总览现已显式声明 role: moc；旧主题关键词原样保存。
- 复用 Registry、四类模板、六份本地 Draft 2020-12 Schema、Validator、Link Validator、Maintenance。公共 Schema 只补充字段语义说明，链接格式和 schema_version: 1 保持兼容。
- 新增 topic_policy.py，以已有属性验证及链接解析检查目标角色。knowledge new、批量 plan、apply、Maintenance、Advisory 均接入；apply 重核角色，失效时 policy_skipped，不写原文件。
- 只生成整篇目标检查时使用 Link Validator 的全库文件名索引，仍保留完整命名空间、排除范围与歧义判断；不读取无关正文，不把这个模式用于标题/块锚点验收。
- Advisory navigation 仅代表合法且显式 role: moc 的导航；topics 的 selected 和 multiple 分支均拒绝原子候选。新 Prompt 为 advisory_v1_2.md，输出协议仍为 v1。没有启动独立模型运行器、读取凭据或调用外部 API。
- 当前 Codex 任务仅按用户授权的核心笔记范围检查内容；Advisory 的来源、检索与模型可见范围未被隐式扩大。
- 新主题 MOC 先创建，再生成引用它的笔记计划；不隐式接受同批尚不存在的目标。Schema-only check 继续只检查属性，完整上下文检查使用 audit。

## 实际笔记与主题数量

核心目录仍为 234 篇 Markdown：215 个已维护实体（concept 81、proposition 42、method 92），16 篇待分类内容保留，3 篇历史目录 README 导航保留。本轮修改 215 篇原子的 YAML，分类不变，不移动、不重命名、不拆卡。

| 主题 MOC | 实际归属原子数 |
|---|---:|
| [[总览/收敛性与积分理论-MOC]] | 43 |
| [[总览/集合与空间-MOC]] | 12 |
| [[总览/概率与随机结构-MOC]] | 51 |
| [[总览/数值计算-MOC]] | 65 |
| [[总览/最优化-MOC]] | 24 |
| [[总览/热学与量子-MOC]] | 26 |

合计 221 项原子 topics 归属；一篇可归属多个主题。主题选择保留逐文件正文证据、既有来源和判断记录，未按旧目录或名称直接推断。

原有 136 项原子主题锚点保存到 legacy_topic_links；原有 legacy_topics、source、tags、自定义字段及四类语义关系保留。legacy_topic_links 是历史追溯字段，不参与动态主题查询，不代表新增的已审查语义关系，允许未登记扩展字段警告。

Phase 3 三篇原子 topics 现均为 [[总览/收敛性与积分理论-MOC]]；MOC 自身归属核心知识工作台。归档主题索引原件保持原样，三个已知数学问题继续登记，未修改原子正文。

## 导航与界面验收

新增五个 MOC（集合与空间、概率与随机结构、数值计算、最优化、热学与量子），每页均包含人工问题路线、动态主题表格及跨主题入口。原收敛 MOC、核心工作台和知识网络总览同步更新。

总览/核心知识.base 新增六个主题视图；Phase 3 内联 Bases 的筛选已改为 topics 指向该 MOC，自身不再使用 Lebesgue 积分概念作主题锚点。系统、模板、测试、管理目录继续排除。

Obsidian 原生 base:query 对六个主题和全部原子视图逐文件核对，结果完全一致（43/12/51/65/24/26，全体 215）。Phase 3 MOC 已在实际阅读视图显示“43 个结果”，并保存渲染与截图证据；不是仅通过 YAML 静态解析宣称界面正常。

## 测试与保护结果

- 全系统隔离回归：119 项通过，其中新增 topics 相关机械测试 17 项；标签隔离测试 11 项通过，合计 130 项。
- 六份 Schema 加载通过；四个模板全部有效，系统实体计数为 0。
- 非 MOC 概念、仅有历史 type: MOC、系统目标、缺失目标、多候选错误目标及计划后目标角色改变均有回归覆盖；合法无显式版本 role: moc 仍可兼容验证。
- 215 / 215 原子正文逐字节一致；215 / 215 的四类语义字段不变；215 / 215 的其他既有 YAML 值保持不变。
- 核心完整审计：valid 215、legacy 19、标签隔离 skip 215，topics 目标错误从 136 降为 0。
- 静态链接 resolved 从 2055 增至 2276；历史 unresolved 31 项保持相同，无新增问题，ambiguous / unchecked / invalid_syntax 均为 0。此为静态审计，不直接宣称 Obsidian 全库断链结论。
- 实施各批均先生成 dry-run、逐文件 diff、原始字节和恢复计划；写入前重核 SHA-256，实际写入冲突为 0。
- 汇总恢复在隔离临时 Vault 完整还原 238 个既有文件原始字节；模拟的并发修改被保留并跳过。没有在真实 Vault 执行恢复测试。

可复跑命令：

~~~~powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" check-system --format json
python -B -m unittest discover -s "D:/知识库/99_System/knowledge/tests"
python -B -m unittest discover -s "D:/知识库/scripts/tests" -p test_tag_maintenance.py
python -B "D:/知识库/99_System/knowledge/knowledge.py" audit --vault-root "D:/知识库" --scope "概念" --scope "知识点" --scope "方法"
~~~~

## 实际文件与基线范围

本轮修改 238 个既有文件（215 篇原子 YAML + 23 个系统、文档与导航文件），新增 9 个文件（包含本报告）。逐文件 SHA-256、完整原始字节及 diff 位于 D:/KnowledgeRefactorBackups/20261028-topics-moc；完整核心路径见 topic-decisions.json 和 recovery/plan.json。

既有原子 215 篇的精确清单见备份的 topic-decisions.json（含变更前后哈希、旧值、新值和证据）。其他实际修改文件如下：

- 99_System/knowledge/ADVISORY_README.md
- 99_System/knowledge/README.md
- 99_System/knowledge/advisory.py
- 99_System/knowledge/advisory_retrieval.py
- 99_System/knowledge/change_control.py
- 99_System/knowledge/knowledge.py
- 99_System/knowledge/link_validator.py
- 99_System/knowledge/maintenance.py
- 99_System/knowledge/schemas/common.schema.json
- 99_System/knowledge/templates/concept.md
- 99_System/knowledge/templates/method.md
- 99_System/knowledge/templates/moc.md
- 99_System/knowledge/templates/proposition.md
- 99_System/knowledge/tests/test_maintenance.py
- docs/DECISIONS.md
- docs/KNOWLEDGE_ACCEPTANCE_2026-10-28.md
- docs/KNOWLEDGE_ARCHITECTURE.md
- docs/KNOWLEDGE_DAILY_GUIDE.md
- docs/REFACTOR_PLAN.md
- 总览/收敛性与积分理论-MOC.md
- 总览/核心知识.base
- 总览/核心知识工作台.md
- 总览/知识网络-MOC.md

实际新增文件：

- 99_System/knowledge/prompts/advisory_v1_2.md
- 99_System/knowledge/tests/test_topic_policy.py
- 99_System/knowledge/topic_policy.py
- 总览/数值计算-MOC.md
- 总览/最优化-MOC.md
- 总览/概率与随机结构-MOC.md
- 总览/热学与量子-MOC.md
- 总览/集合与空间-MOC.md
- docs/TOPICS_MOC_ACCEPTANCE_2026-10-28.md

基线 HEAD 为 fae8e4b8c8d22899e6c51912fe60db5023540837，分支 main。根仓库及两个独立数学建模仓库的 HEAD、分支、index 哈希保持不变；独立仓库 status 也相同。没有提交、推送、切分支、删除、移动或重命名；没有修改插件配置、旧标签脚本、Registry、独立数学建模工程及 AGENTS/CLAUDE。

范围外对照发现 2 个 Obsidian 运行态文件变化（workspace.json 与 cursor-positions.json，对应界面验证）及 719 个并发导入的深度学习资料/图片新增，均保留，不纳入本次修改或恢复。最终复核还发现总览/核心知识.base 在写入后出现仅移除空行和引号的格式变化；解析后的 YAML 对象完全相同。已保留当前字节、保存单独快照和 diff，没有覆盖。这属于范围内的并发/运行态格式例外，完整记录见 base-format-observation.json。未发现既有文件丢失。一个数学建模历史 .pytest_cache 目录仍因权限无法读取，已记录，没有尝试处理。

早期导航批次在索引期间超时，未写入笔记；其 dry-run 被后续成功批次替代并保留为放弃记录，不应再次应用。中文输出编码问题已修正，实际写入、日志路径和哈希均重新核对，没有覆盖用户改动。

## 日常使用

1. 从 Registry 模板或 knowledge.py new 创建三类原子及 role: moc 导航；topics 可空，只选择已有的合法 MOC。
2. 主题导航先写问题、阅读顺序和有价值的入口，再配置 topics 精确聚合；不以普通概念代替主题 MOC。
3. 使用 audit 检查属性、链接、topic_policy 和标签隔离；普通 check 不负责读取目标角色。
4. 新的原子关系填写 prerequisites/about/uses/related，核对双方内容、方向和目标，不从 topics 自动推导关系或标签。
5. AI 建议使用明确来源、检索、模型可见范围的授权证据包及 v1.2 Prompt；check 后人工审查，不能把本地通过当作数学正确性证明。
6. 批量修改通过 plan → 阅读 change.diff → 核对计划哈希 → apply；角色变化、内容并发改动或异常跳过并登记。新建 MOC 与引用它的原子分开规划。

完整命令与数据边界见 [[docs/KNOWLEDGE_DAILY_GUIDE]]。

## 恢复说明

汇总计划：D:/KnowledgeRefactorBackups/20261028-topics-moc/recovery/plan.json

SHA-256：178aaac42441552d96b036a1b29a8b0376694123c3533acdce1de45fac77c095

~~~~powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" restore --plan "D:/KnowledgeRefactorBackups/20261028-topics-moc/recovery/plan.json" --approve-plan-sha256 "178aaac42441552d96b036a1b29a8b0376694123c3533acdce1de45fac77c095"
~~~~

执行恢复前再次审查计划。它只在当前文件仍匹配本轮 after 哈希时恢复 238 个既有文件；后来用户修改会跳过。核心知识.base 当前已有上述等价格式变化，因此该文件在真实恢复时会安全跳过；若需要连同它还原，应先人工审阅额外格式 diff，再单独生成恢复计划，不改变本计划的旧 after 哈希。8 个新增系统/导航文件保留，不自动删除；本报告也是保留的新增文件，不在该恢复计划内。若要恢复此前最终实施轮次，先恢复本轮，再使用 20261028-0050 的原计划。原始备份不可覆盖，按逆时间顺序逐轮恢复。

## 尚未处理的历史事项与能力边界

16 篇语义不确定内容、3 篇旧目录导航、31 项核心历史 unresolved 及此前记录的数学正文问题仍保留，详见 [[docs/KNOWLEDGE_EXCEPTIONS]]；全 Vault 其他历史链接问题未纳入本次全量修复。课程、习题及并发导入资料没有被强制原子化。

Formatter Phase 2B 仍未定位、未集成。未启动独立 Advisory 推理任务或外部模型调用，也未开展独立性能评测、gold 标注或 Macro-F1 实验；Prompt、关系推荐质量及笔记数学正确性不能由这次机械测试推定。没有替换 Formatter、修改图谱插件过滤或引入额外付费依赖。
