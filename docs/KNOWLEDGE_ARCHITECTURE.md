# 知识库架构 v2

状态：用户于 2026-10-28 确认完整设计；当前重构结果见验收报告。完整需求见 [[docs/superpowers/specs/2026-10-28-knowledge-vault-restructure-design]]，原 v1 规则保存在 [[docs/history/2026-10-28-v1/docs/KNOWLEDGE_ARCHITECTURE]]。

## 组织原则

- `00_Inbox`：待整理和待核实内容。
- `01_Knowledge`：concept / proposition / method 平铺存放，不按课程、学科或类型分目录。
- `02_Maps`：`type: moc` 学科与主题导航，可多上层，拒绝主题环，上层递归汇集下层原子并去重。
- `03_Sources`：课堂、复习、作业、阅读、论文、网页、自主想法等来源记录；记录完整保留。
- `03_Sources/Courses/<课程>`：课堂笔记、课件、作业、习题。归档课程保留归档语境。
- `03_Sources/Reviews/<课程>`：复习与综合整理；跨课程复习使用 subject 列表。
- `04_Assets`：独立、共享附件；课程源资料的配套附件保留在原资料目录。
- `99_System`：模板、Schema、标签词表、工具、查询、维护报告，不计知识实体。
- `Home.md`：总入口。

当前非课程 AI/语言/考研/每日疑惑/闪卡/数学建模内容不重新归类；独立仓库不进入扫描。范围外仅定点修复受迁移影响的确定性路径链接。

## 属性规则

单值 type。省略笔记 title，文件名作标题；time 是带时区的创建时间，后续编辑不覆盖。新规则由 schema_version: 2 标识，系统负责填写。

| 类型 | 属性 |
|---|---|
| concept / proposition / method | 必填 type/time/topics/source；topics、source 非空整篇笔记链接列表；可选 aliases/tags/prerequisites/uses |
| moc | 必填 type/time/topics；topics 为上层 MOC，顶层空列表；aliases/tags 可选 |
| lecture / review / homework | 必填 type/time/status/source；课程相关 subject 为课程名列表；aliases/tags 可选 |
| book / paper / web | 必填 type/time/status/source/source_title；可选 authors 列表、year 整数、url、aliases/tags；与课程有关可填 subject |
| book | 另可填 publisher/edition/isbn |
| paper | 另可填 venue/doi |
| web | 另可填 site |
| idea | 用户自行填写属性；有 type 与待处理状态时才参与提炼 |

lecture 可选 lecture_date（上课日期）；homework 可选 due_date（截止日期）。日期格式 YYYY-MM-DD。录音生成的 lecture 使用独立 polish_status 管理润色，status 只管理原子提炼，两者均为 not done / done。

原子 source 至少指向一份真实、合法的 Sources 笔记；不只指向原始 PDF/转换课件。非原子 source 支持真实课件/PDF 链接、URL、书目与定位信息。同一知识只保留一篇原子，多个实际来源进入同一 source 列表。

concept 回答是什么；proposition 回答条件下什么成立、为何成立；method 回答如何执行。综合展开定义、性质、求解步骤的内容保留为来源笔记，不按主次硬塞原子类型。

习题归 homework；知识梳理和答疑不设独立 type，按内容归类为 review/homework 等。课件及转换产物是资料，原始转写和课程目录索引不是普通内容实体。

## 数据库与提炼

MOC 数据库自动识别 MOC 笔记。标签数据库自动读取 `99_System/knowledge/tags` 的 canonical_tag/tag_aliases 记录；AI 先复用标准名，可自主登记新标签。标签不需要完整层级，不替代主题。

收到用户指令后，AI 读取指定 Sources，查已有知识与同义名称，自主提炼/复用原子、确定类型、关联主题与有依据的知识关系。程序只负责准备上下文、验证、计划、应用和恢复，不冒充模型语义生成。不增设提炼自动调度。

来源全部承接为原子，或其中无需提炼的内容经过人工审查后，才标 done；其余保持 not done。不要求来源维护额外归档清单，原子 source 提供追溯；内部运行报告保存证据。

新模板与真实笔记必填值分开验证。系统、原始资料、Inbox、旧版兼容条目与知识实体分开统计。历史缺失时间依据在迁移报告中注明；缺少可核实来源或语义待审的条目保留在 Inbox，不伪造来源。

## 日常入口

[[Home]] · [[docs/KNOWLEDGE_DAILY_GUIDE]] · [[99_System/knowledge/v2/README]]

v1 工具保留历史兼容，新规则使用 knowledge.py v2 入口。旧 Formatter 仍未定位；新实现仅有明确的属性渲染和定点链接处理，不宣称旧 Formatter 已集成。


## 2026-11-01 课程附件位置修正

课程源资料及其附件作为完整资料包保存：教材/课件转换的 images、assets 等目录保留在源文件原有相对位置，不集中迁入 04_Assets；引用优先保留原有相对路径。04_Assets 仅用于独立或确需共享的附件。
