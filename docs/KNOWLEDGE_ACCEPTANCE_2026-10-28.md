# 知识库最终重构综合验收报告

> 本报告保留此前实施时的验收快照。用户随后修正 topics 的目标规则：现统一指向显式 role: moc 导航；最新现状、测试与恢复记录见 [[docs/TOPICS_MOC_ACCEPTANCE_2026-10-28]]。下文旧主题锚点与数量不代表修正后的当前状态。

实施日期：2026-10-28；按北京时间 00:50 启动。以本次用户最终授权为依据，自主分批完成，不改变 Git 历史，不迁移物理目录。下列“已完成”限于有实际代码、文件或验证证据的部分；遗留内容单独列出。

## 1. 最终架构与入口

- 并列实体：concept / proposition / method；目录保留概念、知识点、方法的历史存储位置，类型依据中心内容判断。
- 关系：topics、prerequisites、about、uses、related 为整篇笔记 Wiki-link；不维护冗余逆向关系。
- 导航：[[总览/核心知识工作台]] 提供问题驱动的人工路线，[[总览/核心知识.base]] 按类型和显式版本动态聚合，复用 [[总览/收敛性与积分理论-MOC]]、[[总览/跨主题联系-MOC]]。
- 原有 Registry、四种笔记 Schema、公共 Schema、Validator、Link Validator、Maintenance 和标签隔离继续复用。笔记约束未放宽，Registry 与原验证工具实现未改。
- knowledge.py 是日常入口；change_control.py 是独立的计划、diff、执行和恢复层；Advisory 保持无写入、无 provider。
- 系统文件、模板、文档、测试和管理记录不计入原子实体；新 Bases 与扫描遵循系统排除。未修改插件配置或全局图谱过滤，不把现有 Extended Graph 的系统节点显示宣称为已统一。

日常完整用法见 [[docs/KNOWLEDGE_DAILY_GUIDE]]；字段架构见 [[docs/KNOWLEDGE_ARCHITECTURE]]。

## 2. 实际处理数量

核心范围为三个根目录中的 234 篇 Markdown，原始分布为概念 72、知识点 72、方法 90。

| 结果 | 数量 |
|---|---:|
| 本次实际修改 YAML 的原有笔记 | 212 |
| 先前已经是 v1、此次保持字节不变的试点原子笔记 | 3 |
| 最终通过 v1 的 concept | 81 |
| 最终通过 v1 的 proposition | 42 |
| 最终通过 v1 的 method | 92 |
| 最终原子实体总数 | 215 |
| 内容职责仍需人工裁定、保持原样 | 16 |
| 三类目录 README 导航、保持原样且不计实体 | 3 |
| 现有核心正文损失 | 0 |

这不是把旧 type 或目录批量翻译。实际跨目录调整包括：概念/KKT条件为 proposition；知识点/协方差、Pareto前沿、对偶间隙等为 concept；知识点/一维随机变量函数的分布、Newton-Cotes公式等为 method。定义、证明和例题服务同一中心的笔记没有机械拆分。

16 篇待裁定内容及原因见 [[docs/KNOWLEDGE_EXCEPTIONS]]。课程、习题、日记、管理记录、数学建模工程和旧归档主题索引未强制转换。

## 3. 属性与语义关系

旧主题值完整保存在 legacy_topics，新 topics 只使用已存在目标的内部链接。原 source、tags、所有未授权改变的自定义字段和原有语义值完整保留；扩展警告不触发删除。

本次新增属性关系按（来源、字段、目标）计数：

| 字段 | 新增数 |
|---|---:|
| topics | 133 |
| prerequisites | 10 |
| about | 12 |
| uses | 9 |
| related | 1 |
| 合计 | 165 |

其中非 topics 语义关系 32 条。topics 的依据是原有显式主题注记、正文对象和唯一真实目标；不将名称相似当作数学依赖。其他关系逐项保留双方内容证据，不从普通链接自动猜测方向，不添加不存在的节点。

所有 165 个新增目标均通过本地 Schema 格式和 Link Validator 的实际唯一目标解析。没有自动修复旧正文链接。完整来源、目标、字段和证据在备份根目录 relation-evidence.json；逐篇分类依据在 classification-decisions.json。这些是本次迁移决策记录，不是人工 gold 或模型成绩。

## 4. MOC 与 Bases

| 文件 | 实际工作 |
|---|---|
| 总览/核心知识工作台.md | 新增一个有内容的 MOC，含积分、概率、数值误差、迭代、优化和跨主题阅读路线 |
| 总览/核心知识.base | 新增共享 Bases，提供全部原子、概念、命题、方法和尚无主题视图 |
| 总览/知识网络-MOC.md | 保留旧正文，追加工作台和维护入口 |
| 总览/收敛性与积分理论-MOC.md | 保留人工路线、三项数学待复核和原 Base 配置，更新试点说明并接入工作台 |
| 总览/跨主题联系-MOC.md | 复用原件，未修改 |
| 归档主题索引 | 原样保留 |

Obsidian 1.14.5 中已实际看到核心工作台的 Bases 表格显示 **215 个结果**。原生 base:query 分别返回概念 81、命题 42、方法 92，路径集合与磁盘验证结果完全一致，没有系统模板混入。

最初应用只显示 202 条，核查发现 13 个 TFile 的 mtime/size 与磁盘不同，仍缓存旧类型。仅更新这些文件的应用内状态并重算元数据后恢复为 215；没有再次改写笔记或配置。此问题不是通过放宽筛选解决。

后续桌面锁定，停止了 GUI 操作；积分主题 MOC 本次更新后的额外界面复查未完成，原 Base 配置未改。一次额外的全量运行时逐边查询未完成，已停止本次创建的只读 CLI 辅助进程；不将这项查询列为通过。165 新目标的静态实际解析检查已通过。

## 5. Advisory 与维护工具

已完成：

1. **检索与身份消歧分开**：unique 保留原严格规则；selected 允许从有证据的实际可见候选选择一个已定位 ID，但不宣称检索、全库或数学关系唯一。隐藏命中、不完整证据和人工复核标记继续保留。
2. **最小推理封装**：inference 仅包含协议、request_id、阶段、可见正文和受限检索说明；不包含 audit、gold、隐藏候选正文。
3. **精确范围授权**：manifest 明确来源、检索、可见清单；authorize 绑定清单、根目录、阶段和冻结文件哈希，CLI 还要求授权文件的 SHA-256。pending 默认保持禁止真实正文导出，synthetic 根不得与真实 Vault 存在祖先或后代交集。
4. **模型与本地程序解耦**：没有新 API、凭据读取、自动推理、收费依赖或付费额度购买。日常可导出经审核的最小包，在没有 Vault/工具读取权限的独立普通聊天中获取建议，再本地 check 与人工审查。不能验证隔离的自动运行方式未启用。
5. **独立可恢复写入**：计划中必须有路径、预期哈希、目标字节和理由；先保存 diff、原字节、目标 payload 与计划摘要，再明确批准该摘要。现有核心正文修改拒绝，冲突逐文件跳过。Advisory 本身仍没有 apply/fix/migrate/split。
6. **Windows 写入保护**：独占句柄内比较并写入，验证最终路径，拒绝重解析、多硬链接和 Windows 路径别名；journal 同样保护。已验证的 plan/payload/original 字节保存在内存复用，不校验后重读。非 Windows 写入失败关闭。

实际 CLI 示例工件位于备份根目录 advisory-example/：本地检索 2 篇，模型可见 2 个 ID，导出为 1 篇来源和 1 篇候选，隐藏匹配数保留为 1；inference 为 27,295 字节且不含 audit，绑定 request_id。只生成本地包，没有调用外部模型。

不做独立模型性能测评，不创建 gold，不报告 Macro-F1。历史 30 样本与空标注原件保留；其哈希因本次真实整理而过期，不能继续充当当前授权清单。日常应重新生成范围与摘要。

Formatter 仍未定位、未集成，没有用新工具冒充 Formatter。

## 6. 文件修改及备份范围

主动修改 **223 个既有文件**：核心 YAML 212；其余 11 个系统、治理或导航文件如下：

- 99_System/knowledge/advisory.py
- 99_System/knowledge/advisory_retrieval.py
- 99_System/knowledge/advisory_schemas/response.schema.json
- 99_System/knowledge/README.md
- 99_System/knowledge/ADVISORY_README.md
- 99_System/knowledge/templates/moc.md
- docs/KNOWLEDGE_ARCHITECTURE.md
- docs/REFACTOR_PLAN.md
- docs/DECISIONS.md
- 总览/知识网络-MOC.md
- 总览/收敛性与积分理论-MOC.md

实际新增 **12 个文件**：

- 99_System/knowledge/advisory_schemas/inference.schema.json
- 99_System/knowledge/change_control.py
- 99_System/knowledge/knowledge.py
- 99_System/knowledge/prompts/advisory_v1_1.md
- 99_System/knowledge/tests/test_advisory_runtime.py
- 99_System/knowledge/tests/test_change_control.py
- 99_System/knowledge/tests/test_knowledge.py
- 总览/核心知识.base
- 总览/核心知识工作台.md
- docs/KNOWLEDGE_DAILY_GUIDE.md
- docs/KNOWLEDGE_EXCEPTIONS.md
- docs/KNOWLEDGE_ACCEPTANCE_2026-10-28.md（本报告）

原 Registry、四类笔记 Schema、公共/Registry Schema、Validator、Link Validator、Maintenance、旧标签脚本、AGENTS.md、CLAUDE.md 和插件配置均未主动修改。

备份根目录：D:/KnowledgeRefactorBackups/20261028-0050。包含全量基线、三个仓库状态、287 个初始原字节副本、每批计划/diff、212 篇核心批次、分类和关系证据、前后审计、恢复包及测试记录。最终逐文件变更清单与摘要位于 final-file-manifest.json。

全量基线 29,673 文件记录。范围外仅观察到 .obsidian/workspace.json 和 remember-cursor-position/cursor-positions.json 两项运行记录变化；没有向它们写入或回滚。没有删除或移动文件，没有范围外新增。凭据文件只记录元数据；数学建模/第一次训练/代码/.pytest_cache 无权限项保持排除，未改权限，不将排除项声称为逐字节核验通过。

根仓库 HEAD 保持 fae8e4b8c8d22899e6c51912fe60db5023540837，分支 main、index 摘要与空暂存差异不变；工作区 status 的预期变化来自本次文件修改。数学建模/2026国赛与 AutoMM 的 HEAD、分支、status、index 和暂存状态全部与开始基线一致。没有提交、推送或改变分支。

## 7. 自动化验收

| 检查 | 实际结果 |
|---|---|
| 知识系统 unittest | 102 项通过，包含本次新增 20 项 |
| 旧标签回归 | 11 项通过 |
| 合计 | 113 项通过 |
| 原 Registry/Schema/模板 | 6 份 Schema、4 个模板通过，零错误、零警告 |
| 系统模板实体统计 | 0 |
| 234 篇原正文 | 全部逐字节一致 |
| 原 source、tags、自定义字段、既有语义值 | 全部保留，旧 topics 原值保留 |
| 未转换 19 文件 | 全部保持原始字节 |
| 核心属性 | valid 215、legacy 19、invalid 0 |
| 核心 resolved 链接 | 1,890 → 2,055 |
| 核心历史 unresolved | 31 → 31 |
| 核心 ambiguous / invalid_syntax | 均为 0，无新增 |
| 新语义/主题目标 | 165 项静态实际唯一解析通过 |
| 标签隔离 | 215 篇新规范实体全部跳过旧推断，无真实标签写入 |
| 真实变更恢复演练 | 隔离副本恢复 223 个既有文件，原字节全部匹配；保留 11 个新增文件，零冲突、零失败 |
| 核心 Bases 运行时 | 215 条，三个类型数量与路径均匹配 |
| 三个导航文件静态审计 | resolved 55、复杂 Base 视图引用 unchecked 1；无 unresolved、ambiguous 或 invalid_syntax |

独立只读代码审查发现 5 个 P1 安全问题：Windows 别名正文绕过、校验后重读、journal 链接写入、并发比较/写入窗口、synthetic 子根越权。均已补充失败回归后修复；最终新安全子集为变更工具 11 项、Advisory 运行 7 项通过，完整套件再通过。没有把作者自审冒充独立复核。

整批不是数据库事务。写入意图和原字节先持久化；极端中断造成部分写入时，不满足当前摘要的自动恢复会停止，需人工对照备份，不强制覆盖。

## 8. 尚需人工处理的事项

- 16 篇职责混合或边界不清的内容，原样保留；不因篇幅或章节数机械拆分。
- 31 项核心历史 unresolved，以及原 Phase 3 归档范围的四项方括号语法问题，未自动修复。
- DCT 量词、控制函数有界要求、最大值公式三项数学问题，正文未修订；未开展全库数学正确性审查。
- Formatter 专项仍未完成。
- 自动外部模型运行器没有启用；严格包外隔离必须由实际运行环境提供，不以 Prompt 禁止工具冒充。
- 未改全局/Extended Graph 插件过滤，系统节点仍可能出现；新 Bases 和维护扫描的排除已实现。
- 后续锁屏后的额外界面复查未完成，不能将未完成检查称为通过。

逐文件明细与历史/新增区分见 [[docs/KNOWLEDGE_EXCEPTIONS]]。本次未产生新增已确认断链、正文损失或强制类型转换遗留；保留项不描述为已完成。

## 9. 日常使用

1. 从 [[总览/核心知识工作台]] 进入，按实际问题阅读；用 [[总览/核心知识.base]] 切换类型视图。
2. 复制 Registry 模板，或 knowledge.py new 生成审查计划；审查后显式 apply，不覆盖已有文件。
3. knowledge.py check 检查 YAML；audit 显式指定范围，查看链接状态、候选、字段警告与标签隔离。
4. advisory manifest → authorize → prepare --view inference；只把审查后的最小包提供给独立无工具聊天，随后 check 与人工审核。
5. 不直接执行模型输出。批量变更先 plan、检查 diff 与摘要，再 apply；并发冲突跳过。
6. 维护显式 topics 与有证据的语义属性，保留人工路线，不创建大量空 MOC，不从主题补 tags。

全部参数与复制可用的命令见 [[docs/KNOWLEDGE_DAILY_GUIDE]]。

## 10. 恢复说明

整次恢复包覆盖本次 223 个既有修改及 11 个新增系统/导航文件；新增验收报告作为恢复记录保留，不进入撤销目标。没有收录或回滚 Obsidian 运行记录、独立仓库和用户其他文件。

恢复计划：D:/KnowledgeRefactorBackups/20261028-0050/recovery/plan.json

完整 SHA-256：

c37247af5056b49a640703024baf861180255cc9eb88ec99bcc0730f892cd476

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" restore --plan "D:/KnowledgeRefactorBackups/20261028-0050/recovery/plan.json" --approve-plan-sha256 "c37247af5056b49a640703024baf861180255cc9eb88ec99bcc0730f892cd476"
```

恢复前先阅读 recovery/README.md 和计划。只将当前仍匹配本次结果的既有文件恢复为原始字节；后续用户修改会跳过。新增文件返回 preserved_addition，不自动删除。本恢复已在隔离副本真实执行验证，未对真实 Vault 执行回滚。需要局部撤销时可使用 core-batch/ 的原核心计划；不同计划格式按日常指南区分，不将引导记录直接交给恢复 CLI。

保留 baseline.json、original/、batches/、core-batch/、recovery/ 及其摘要。不要运行 reset --hard、clean 或覆盖整库来撤销本次改动。
