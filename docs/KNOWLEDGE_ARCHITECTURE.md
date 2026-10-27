# 知识库架构 v1（Phase 1 + Phase 2A）

本文件描述用户批准的独立属性验证体系。既有文件保持原状；本规范不会因文档落盘而自动迁移旧笔记、替换旧模板或改变插件。系统入口见 [[99_System/knowledge/README]]，实施边界见 [[docs/REFACTOR_PLAN]]，决策见 [[docs/DECISIONS]]。

## 意图与实体职责

长期目标是以知识实体和语义关系形成可复用网络，以主题和 MOC 提供导航。文件夹只负责物理存储。本阶段不搬动文件，不把课程章节、习题、项目、原始资料和管理记录强行改成原子实体。

| 类型 | 中心问题 | 必须讲清的内容 |
|---|---|---|
| concept | 对象是什么？ | 定义、符号、含义、边界和必要例子 |
| proposition | 什么条件下什么成立？ | 假设、量词、结论、依据或证明、限制 |
| method | 怎样执行？ | 输入、条件、步骤、输出、检查与失败边界 |

三类并列；独立理解、复用和链接价值是拆分依据。概念内可以有例子，命题内可以有应用，方法内可以有原理，不为符合模板机械拆分。

MOC 采用 role: moc，编排主题问题、阅读路线和聚合结果。它是导航视图，不是第四类原子实体。历史 type: MOC 暂兼容；新模板不填写 type。

## 属性与关系

| 字段 | v1 规则 |
|---|---|
| type | 三类原子实体必填，取 concept/proposition/method |
| role | 新 MOC 必填 moc；不能与原子 type 并用 |
| title | 可省略；存在时为非空字符串；默认展示标题是文件名，不回写元数据 |
| schema_version | 可选整数 1；四个新模板默认带入 |
| topics | 主题归属，允许多个主题；整篇笔记链接列表 |
| prerequisites | 学习该内容需要的先修知识；链接列表 |
| about | 该内容讨论的对象；链接列表 |
| uses | 方法或推导直接使用的知识；链接列表 |
| related | 其他具有明确关联的笔记；链接列表，关系含义仍需正文解释 |
| source | 字符串列表，允许来源笔记链接、URL、书目和定位信息；不伪造来源 |
| aliases | Obsidian 原生别名，字符串列表 |
| tags | 少量辅助检索标签，字符串列表；不替代 topics 与关系 |
| status | 可选非空字符串；本阶段不新增统一状态枚举 |

示例仅演示语法，不创建或确认链接目标：

```yaml
schema_version: 1
type: method
topics:
  - "[[积分与极限]]"
uses:
  - "[[知识点/Lebesgue控制收敛定理]]"
```

topics 和四类语义关系字段允许省略或空列表。非空项只能是整篇笔记 Wiki-link，允许有路径或无路径；暂不接受嵌入、显示别名、标题或块锚点、前后空白及重复的相同字符串。文件名中的数学字符如 L^p 不被当作块锚点。不得把 source_context 等位置说明机械并入 source。

不维护冗余逆向属性。Phase 1 不判断目标是否存在、是否唯一、先修关系是否成环或语义关系是否真实，这些属于未来链接与内容审查。

## 注册表、Schema 与验证器

registry.yaml 是类型到模板、Schema 和历史识别策略的机器映射。六份 Schema 使用 Draft 2020-12：公共 Schema 定义属性与链接列表，四种配置通过本地 URN 引用公共定义，注册表 Schema 约束机器映射。

Schema 是字段结构约束的依据；原属性库继续保存用途和历史依赖说明。Validator 只读取属性条目的文件名作为已登记字段名，不将原属性说明中的旧 topics 定义覆盖 v1，也不修改属性库。新增的 v1 字段由公共 Schema 登记；未登记扩展字段警告并保留。允许合理扩展，不能因低频或空值自动删字段。

Validator 的流程是读取指定输入、解析 YAML、检查重复键和版本、选择配置、验证结构并输出诊断。没有全库默认扫描、写入、修复、迁移或格式化接口。日期保留为字符串；不接受递归 YAML 别名和非 JSON 兼容值，避免静默丢弃或改变元数据。

所有 Schema 资源从本地明确注册，解析引用时不允许网络获取。Phase 2A 进一步确认引用目标本身是合法 Schema、配置强制复用公共约束、历史“知识点”人工审查标记不可关闭；拒绝本 v1 家族未使用的嵌套资源 ID、动态引用及无条件引用环。此限制不更改笔记类型或字段约束，不扩展成通用 Schema 引擎。Formatter 尚未定位、专项审计未完成，没有集成。

## 版本识别与兼容

schema_version 声明的是笔记选择的约束版本，不是创建日期或历史来源证明。注册表版本另由 registry_version 标记。

| 情形 | 自动识别结果 |
|---|---|
| schema_version: 1 | 按 v1 严格检查；非法历史 type 仍报错 |
| 无版本，但英文原子 type 或 role: moc | 尝试 v1 兼容检查；version_status 为 undeclared，发出 W_VERSION_UNDECLARED |
| 无版本，只有中文概念、知识点、方法或 type: MOC | legacy；不赋予新的 canonical type |
| 已登记的课程、习题、项目等类型 | out_of_scope，未接受原子 Schema 验证 |
| 其他或没有类别信息 | unclassified，不能当作通过 |
| 版本值不是支持的整数 1 | invalid，不回退或猜测 |

显式 --profile v1 可检查没有版本的输入，仍标记 undeclared。compatible_shape 只说明当前结构兼容，不声称按 v1 创建。“知识点”始终需要人工内容审查，不存在无条件 proposition 映射。

## 系统文件隔离（所有未来消费者的前置条件）

知识实体扫描、MOC 动态查询和知识图谱构建必须先应用系统文件排除策略，再判断 type、role 或关系。系统模板即使完全符合原子 Schema，也不是实际知识实体。

当前注册表排除以下范围及其子目录：99_System、docs、scripts、模板、规范、总览/标签库、总览/属性库；排除隐藏路径及 AGENTS.md、CLAUDE.md。路径匹配按完整目录段判断，99_Systematic 不会被误排除。99_System 和 docs 是不可从注册表移除的最低排除要求。测试资料使用 JSON，不生成真实学习笔记。

未来扫描器应复用 is_system_path 或实现等价规则，且不得沿联接路径将系统文件重新纳入；未来 Bases/Dataview 查询与图谱构建必须实现相同排除条件。完整图谱还需排除系统文件发出的边，不能只隐藏节点。本阶段仅规定及测试排除规则，没有修改现有 Base、Dataview、图谱或插件，因此现有界面不因此自动改变。

验证报告把 validation_counts 与 knowledge_entities 分开。四个模板可作为验证对象全部通过，但 knowledge_entities 必须为 0；MOC 本身也不计入三类原子实体数量。历史未验证笔记不因目录位置被算作已通过的 v1 实体。

## 新旧 topics 与标签工具边界

新 topics 不能被直接视为标签名，标签、属性记录也不自动变为主题节点。按照用户 Phase 2A 验收 B，旧工具停止从 topics、标题、文件名及语义字段生成新标签；只对已有显式 tags 规划无歧义标准名归一。未知或歧义值保留，不使用上下文猜测其含义。

Phase 1 曾发现路径或链接文字中的 Lebesgue 会影响已有 DCT 标签的归一。Phase 2A 已移除这种上下文推断，并在规划与执行两处跳过版本标记、英文类型、MOC 角色、新语义字段及链接/混合 topics。执行还按当前 Registry 重算候选字节，拒绝旧推断计划、非标签变更和并发修改；单文件替换仍不是整批事务。

新系统存储路径不属于旧工具 SCOPES。执行类回归仅对临时数据调用 apply_changes，真实笔记没有标签写入。Maintenance 只读复用现有 Validator 和标签策略，不暴露执行接口。新格式 tags 仍由用户显式填写；隔离通过不等于新格式会被自动维护或真实笔记写入已获授权。

## Phase 2A 维护审计层

maintenance.py 要求显式 Vault 根和源范围，复用现有属性验证，不重复实现 Validator。link_validator.py 建立只读目标索引，源文件先排除系统、联接和独立仓库；系统规范仍可作为来源链接的目标，不能把“非知识实体”误解为“链接不能指向它”。实际命令和接口见系统 README。

标准 Markdown 与 Wiki-link 分别解析。Markdown 相对 URI 以来源目录为基准，不使用 Wiki-link 的全库短名回退；空 URI 是当前文档。Wiki-link 报告使用原文，含百分号编码时保守标记 unchecked，保留字面与解码候选。链接报告保留静态判断范围、候选和依据，区分 resolved、ambiguous、unresolved、unchecked、invalid_syntax，不声称等价于 Obsidian 的实际解析。无法可靠映射原文时不输出行列号；复杂锚点、外部 URI 和受排除目标标记 unchecked。没有自动修复链接或生成知识图谱。

## 存储与后续边界

Phase 1 建立独立系统；Phase 2A 仅修改批准的 16 个路径并新增 5 个文件。00_Inbox、01_Knowledge、02_Maps、03_Sources、04_Assets 和 Home.md 仍是后续候选，不创建、不迁入旧文件。课程来源、整理笔记、附件、闪卡和独立仓库保持原语境。Phase 2B 及 Phase 3–6 未授权。

参考：[Obsidian Properties](https://obsidian.md/help/properties)、[JSON Schema 对象](https://json-schema.org/understanding-json-schema/reference/object)、[jsonschema 本地引用](https://python-jsonschema.readthedocs.io/en/stable/referencing/)。
