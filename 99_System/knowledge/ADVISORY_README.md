# AI Advisory：Phase 4A-1 工程基础

## 2026-10-28 topics 目标规则

topics 只表示主题归属，目标必须显式声明 role: moc，并通过本地属性与目标解析检查；普通原子和仅有历史 type: MOC 的文件均不能充当新主题锚点。原子之间使用 prerequisites/about/uses/related。旧值保留，不自动转成其他关系。Maintenance 报告 topic_policy；新建、plan/apply 与 Advisory 均检查此规则。详见 [[docs/KNOWLEDGE_ARCHITECTURE]]、[[docs/KNOWLEDGE_DAILY_GUIDE]] 及 [[docs/TOPICS_MOC_ACCEPTANCE_2026-10-28]]。

## 2026-10-28 当前只读建议接口

本文件下方为 Phase 4A-1 历史说明。当前新增 manifest、authorize 与 prepare --view inference；真实正文只接受绑定清单、根目录、阶段及文件哈希的授权，CLI 还需授权文件摘要。selected 区分候选身份定位与检索唯一，原 unique 保持严格拒绝规则；旧 30 候选仍为空可见且不运行评测。使用 [[docs/KNOWLEDGE_DAILY_GUIDE]] 与 prompts/advisory_v1_2.md，不向模型提供 bundle 的 audit。没有网络、provider、自动推理或写入操作；不新增独立 API。

这是只读、离线的建议协议与机械检查工具，不是 AI 分类器或 Formatter。没有 provider、API、凭据读取、模型子进程或联网代码，没有 apply、fix、migrate、split 写入命令。Phase 4A-2 真实模型测试未授权。

## 当前状态

30 篇真实候选只保存路径、SHA-256、候选层及分组；人工标注模板全部 pending、gold 为 null。真实样本 source=30、retrieval=30、model_visible=0；pending_phase4a2 下不能加入模型可见 ID。把真实 Vault 改称 synthetic 也会被拒绝。

机械测试只在系统临时目录建立合成 Vault；测试内的合成答案是计分器样例，不是人工 gold，也不是模型成绩。evaluate 不会通过输入中自称的 model 名称或 origin 放开语义验收，metrics 始终为 null。

## CLI

程序从标准输出返回 JSON；没有报告路径、缓存或输出文件选项。所有涉及笔记读取的命令必须显式给出 Vault 根和操作者指定的 manifest。未知命令/参数退出 2；输入、读取、协议或检查错误退出 1；机械操作成功退出 0。evaluate 退出 0 不代表语义验收通过。

检查真实候选的分组和空标注状态（不生成正文包，不启动模型）：

```powershell
python -B "D:/知识库/99_System/knowledge/advisory.py" evaluate --manifest "D:/知识库/99_System/knowledge/benchmarks/phase4a/sample_manifest.json" --annotations "D:/知识库/99_System/knowledge/benchmarks/phase4a/annotation_template.jsonl"
```

prepare 生成本地 bundle：audit 是本地侧车，model_input 才是唯一可导出的模型视图。真实清单的模型视图为空；本阶段不把真实正文提供给模型。下面命令当前只得到空模型正文清单：

```powershell
python -B "D:/知识库/99_System/knowledge/advisory.py" prepare --vault-root "D:/知识库" --manifest "D:/知识库/99_System/knowledge/benchmarks/phase4a/sample_manifest.json" --stage classify --view model
```

其余命令形式（路径占位符指向用户另行准备的隔离合成样例，不表示已存在文件）：

```text
advisory.py search --vault-root <隔离样例根> --manifest <合成清单.json> --query Fatou
advisory.py prepare --vault-root <隔离样例根> --manifest <合成清单.json> --stage relations --query Fatou
advisory.py check --vault-root <隔离样例根> --manifest <合成清单.json> --request <本地请求.json> --response <合成响应.json>
```

操作者可在批准后自行把 stdout 保存到 Vault 外；不要把 bundle 整体当作模型输入，audit 含路径、旧元数据报告与检索范围，可能泄漏分类代理线索。

## 接口与现有系统复用

- advisory_retrieval.validate_manifest：验证清单结构、相对路径、哈希格式、三范围、分组及阶段权限。
- build_catalog(root, manifest)：只读取清单 source/retrieval 并集的 Markdown，不递归扩范围；复用 Maintenance 中的同一 Validator、Link Validator 模块。
- retrieve(catalog, query, k=8)：别名/标题与中文二元词项、英文词项的 TF-IDF 排序；返回 unique/multiple/not_found，分数不是置信概率。候选只含元数据，不返回正文。
- advisory.prepare：创建绑定 manifest/内容哈希的确定性请求与三个范围的请求、实际纳入、排除记录。
- check_response：重新准备并逐项比对原请求，验证来源与候选 ID、双方精确引文/位置、当前哈希、允许字段、既有链接格式及解析结果；任何错误导致整份响应拒收。
- advisory_evaluation.audit_manifest/content_leakage：清单机械检查及启发式跨集合相似度检查。
- classification_metrics/retrieval_metrics/relation_metrics：纯计分数学函数。evaluate 始终不报告真实语义指标。

使用现有 load_system、parse_frontmatter、is_system_path、validate_note、protected_reason、Index、audit_links；内部适配器还调用 Link Validator 的 _record 和 Maintenance 的 _tag_report。不复制它们的链接解析、标签隔离或笔记 Schema。私有接口耦合是已知风险，受合成回归测试保护。没有调用 Maintenance.audit 的隐式全库目标索引，以免超出清单范围；原入口仍保持原状。

新建议协议 Schema 独立加载，复用现有本地 Schema 引用预检；不写入原 Registry，不把 mixed 等分类结果登记成笔记 type，不安装新依赖。

## 输出语义

classification 区分 atomic/mixed/non_atomic/undetermined；只有 atomic 分类才允许三种 primary_type。关系使用 topics/prerequisites/about/uses/related，不建议 status、tags、个人掌握程度。split_review 只有来源片段、用途和候选类型，没有创建、移动或拆卡动作。new_entity_review 只给普通名称与理由，不生成悬空链接，并核对已读范围内标题、文件名和显式别名。abstain 必须保持 undetermined。

每项建议必须有来源证据、理由、目标状态、候选、置信等级及不确定性。关系还要有目标证据。confidence.calibrated 固定 false，requires_human_review 固定 true。check 的 ok 只表示机械准入，semantic_verified 始终 false。

名称多候选即使仅一个获准给模型看，也不能被模型改称 unique；可在全部候选获准且有证据时提交 multiple、不作选择，或者弃权。现有短链接与全路径链接通过原链接解析器按目标去重；先修循环仅标为人工复核，不改动任何原关系。有限范围内没有结果不证明全库不存在。

来源位置以 UTF-8/BOM 解码后的原始行计数；列为 1 基 Unicode 字符，不是字节或视觉制表列，end_column 为开区间。正文行包括公式与算法代码，均视为不可信数据。每篇最多 80,000 字符、2,000 非空行，单行最多保留前 8,192 字符；超限保留可定位前缀并标记 coverage=partial，不允许据此确认整篇原子类型。整个正文包最多 160,000 字符，超限要求缩小已批准范围，不自动扩权或静默截去候选。

## 测试与边界

```powershell
python -B -m unittest discover -s "D:/知识库/99_System/knowledge/tests" -p "test_*.py" -v
python -B -m unittest discover -s "D:/知识库/scripts/tests" -p "test_tag_maintenance.py" -v
python -B "D:/知识库/99_System/knowledge/validator.py" check-system --format json
```

JSON 输入限制 4 MiB，重复键与非有限数拒收；读取前检查大小并有界读取。没有默认递归扫描、模型自动调用或写入接口。清单是操作者指定的本地授权工件；响应不能修改它。没有加密签名或操作系统文件锁，哈希不是身份认证；准备后原文件变化会使检查失败，未来仍需避免并发编辑。

真实语义能力、置信校准、全库召回、数学正确性、模型提示注入抵抗效果均未测。正文中的数学错误、历史断链、归档四处方括号链接问题不在本阶段修复。Formatter Phase 2B 未定位、未集成。

完整设计、实施记录和最终机械验收见 docs/AI_ADVISORY_DESIGN.md；真实模型与正文范围须按其中 Phase 4A-2 清单另行审批。
