# 当前入口：知识库 v2

新内容和迁移后的知识使用 [[99_System/knowledge/v2/README]] 与 `knowledge.py v2`。下文为 v1 历史实现说明，不覆盖 v2 已确认规则。

---

# 知识体系验证与维护审计（Phase 1 + Phase 2A）

## 2026-10-28 topics 目标规则

topics 只表示主题归属，目标必须显式声明 role: moc，并通过本地属性与目标解析检查；普通原子和仅有历史 type: MOC 的文件均不能充当新主题锚点。原子之间使用 prerequisites/about/uses/related。旧值保留，不自动转成其他关系。Maintenance 报告 topic_policy；新建、plan/apply 与 Advisory 均检查此规则。详见 [[docs/KNOWLEDGE_ARCHITECTURE]]、[[docs/KNOWLEDGE_DAILY_GUIDE]] 及 [[docs/TOPICS_MOC_ACCEPTANCE_2026-10-28]]。

## 2026-10-28 当前系统

最终实施授权已覆盖核心整理与长期维护；下方 Phase 1/2A 清单和未授权文字仅为历史记录，不构成当前阶段边界。日常入口为 knowledge.py；新建使用 Registry 模板并只生成计划，审查、apply/restore 由独立 change_control 完成，Maintenance 继续只读。当前范围与命令以 [[docs/KNOWLEDGE_DAILY_GUIDE]]、综合验收报告为准。Formatter 仍未定位、未集成。

这是独立的属性验证和只读维护审计工具。Maintenance 不迁移笔记、不写属性、标签、附件或插件，不运行 Formatter，不默认扫描 Vault。用户已批准 Phase 2A；Formatter 仍未定位、专项审计未完成、没有集成，Phase 2B 与 Phase 3–6 未授权。

架构见 [[docs/KNOWLEDGE_ARCHITECTURE]]，实施和验收记录见 [[docs/REFACTOR_PLAN]]，决策见 [[docs/DECISIONS]]。[[docs/AGENTS_PHASE1_PROPOSAL|根指令建议稿]] 尚未生效。

## 运行环境

已验证环境为 Python 3.13、PyYAML 6.0.3、jsonschema 4.26.0、referencing 0.37.0、markdown-it-py 4.2.0。requirements.txt 只声明已在本机具备的依赖，没有执行安装。命令使用 -B，避免生成字节码缓存。所有 Schema 及其引用本地加载，不获取网络资源。

## 可执行命令

检查注册表、六份 Schema 及四个模板：

```powershell
python -B "D:/知识库/99_System/knowledge/validator.py" check-system --format json
```

执行全部隔离测试：

```powershell
python -B -m unittest discover -s "D:/知识库/99_System/knowledge/tests" -p "test_*.py" -v
python -B -m unittest discover -s "D:/知识库/scripts/tests" -p "test_tag_maintenance.py" -v
```

检查指定文件的命令形式为 `check --file 绝对文件路径 --vault-root 所属Vault根目录 --profile auto`，可重复 --file；使用 --profile v1 执行严格结构检查。文件必须处于指定根目录内，输入目录不会被递归扫描。默认 Vault 根目录由工具位置推导。只接受 json/text 终端输出，没有 --apply、--fix、报告路径或迁移接口。

退出码：0 表示没有验证错误，允许有警告、legacy、unclassified 和 out_of_scope；1 表示输入不合规范；2 表示命令、读取或系统配置错误。必须查看分类覆盖和诊断，不能把退出码 0 称为全库规范通过。

## 报告与公开接口

validate_note(raw, path, system, profile) 只接受原始字节和相对 Vault 的逻辑路径，返回新报告，不改变原字节。load_system(root) 加载明确的本地系统目录；parse_frontmatter 只解析开头 YAML；is_system_path 是未来消费者必须遵循的排除规则；check_system 检查四个模板与映射。

报告包含 classification、selected_profile、version_status、validation_basis、display_title、semantic_review_required、is_system_file、is_knowledge_entity 和 diagnostics。诊断提供 code、severity、field 和 message；字段路径以斜杠分隔。summary 的 validation_counts 是输入验证分类，knowledge_entities 才是非系统、合法三类原子实体数量。

主要诊断：E_ENCODING、E_FRONTMATTER、E_YAML、E_DUPLICATE_KEY、E_VERSION、E_TYPE、E_SCHEMA、E_ROLE_TYPE_CONFLICT、E_TEMPLATE_PROFILE、E_TEMPLATE_VERSION 为错误；W_VERSION_UNDECLARED、W_UNKNOWN_FIELD、W_UNCLASSIFIED、W_LEGACY_MOC_TYPE、W_LEGACY_TAG_CONTEXT 为警告。I_LEGACY_TYPE 与 I_SEMANTIC_REVIEW 仅说明兼容识别。

四个模板在系统内可以通过 Schema，但不能计入真实实体。复制模板成为新笔记才进入新笔记工作流；本阶段未注册 Obsidian 模板位置，也不自动创建或复制笔记。YAML title 可省略，schema_version 默认 1；无版本仅能证明当前结构兼容，不能证明历史按 v1 创建。

## 系统隔离与旧标签脚本

未来知识扫描、MOC 查询和图谱构建必须先排除系统文件；范围见 registry.yaml 和架构文档。系统检查预期 knowledge_entities 为 0、system_files 为 4。本阶段没有更新既有 Base 或插件，不能认为现有查询自动具备该排除条件。

Phase 2A 的 tag_maintenance.py 在规划和执行时都跳过新版本、英文原子类型、MOC 角色、新语义字段及链接/混合 topics，明确报告原因。不再从任何 topics、标题、文件名或关系字段生成标签；只可规划显式 tags 的无歧义标准名归一，未知与歧义标签保留。执行前及备份后重新检查字节、隔离策略，并按当前 Registry 重算规划；旧计划不能绕过新规则，任意正文或其他元数据变更也不会被接受。

原标签 CLI 保留显式 --apply 和字节备份接口，但本阶段没有对真实笔记调用它；执行类测试仅在系统临时目录中进行。Maintenance 不暴露此接口，只读报告显式标签及建议；新/混合笔记整篇跳过旧推断。Validator 的 W_LEGACY_TAG_CONTEXT 表示需要隔离，不表示已获准补标。

## Phase 2A 统一审计入口

命令形式（示例展示参数，不表示已对这些真实笔记执行审计或写入）：

```powershell
python -B "D:/知识库/99_System/knowledge/maintenance.py" audit --vault-root "D:/知识库" --scope "课程/概率论" --format json
```

--vault-root 和至少一个 --scope 必填；范围可为文件或目录，可重复指定。只有范围内非系统 Markdown 作为源文件审计，目标索引覆盖可见命名空间，跳过隐藏/运行目录、符号链接/联接和嵌套独立仓库；每项报告保留范围、排除原因、候选及判断依据。来源可链接系统规范文件，它们可作为目标定位，但不计知识实体。此区分不改变既有 MOC 或图谱插件。

报告包含 attributes、links、tags、source_sha256，以及 dry_run: true、writes: 0、空 proposed_changes 和 formatter.status: not_located。入口没有 --apply、--fix、报告文件或 Formatter 替代接口。退出码 0 表示无结构/语法/读取错误，不表示所有静态链接已定位；1 是输入错误，2 是命令或配置错误。

链接状态为 resolved、ambiguous、unresolved、unchecked、invalid_syntax。resolved 只表示本次静态规则找到目标，不是 Obsidian 运行时断链结论。无路径同名项保守报告多候选，Markdown 与 PDF 区分；别名只能提供候选，不自动当成文件目标。PDF 页码、外部 URI、排除范围、复杂嵌套标题等不可靠判定项为 unchecked。

CommonMark 由 markdown-it-py 解析；Wiki-link 由独立扫描器解析，并非假设前者原生支持后者。先排除代码块、行内代码、注释和数学片段，再分别处理两种语法；保留数学文件名中的 ^，排除转义假链接及脚注误识别。正文 Wiki-link 在可直接映射原文时提供 1 基行列，列按 Unicode 字符计数，不是字节或制表符视觉列；Markdown 链接和 YAML 属性链接没有可靠字符映射时 line/column 为 null，并保留来源字段路径，不虚构位置。不获取外部 URI，不渲染任何媒体。

Markdown URI 按源文档所在目录解析相对路径，显式 / 前缀按本次 Vault 根规则处理，不回退到全库同名文件；空 URI 指向当前文档。Wiki-link 的短名、路径和候选逻辑独立处理，原始链接和目标从原文提取，遮罩内容不会进入报告。含百分号编码的 Wiki-link 因运行时语义未确认，报告 unchecked 并保留字面与解码候选；Markdown URI 正常解码。

实现依据：[markdown-it-py 官方文档](https://markdown-it-py.readthedocs.io/en/latest/using.html)。

## 实际新增文件清单

以下为 Phase 1 当时批准的 20 个新增文件，保留历史清单；Phase 2A 的 21 文件变更范围和逐文件基线对照见 [[docs/REFACTOR_PLAN]]。

| 绝对路径 | 用途 |
|---|---|
| D:/知识库/docs/AGENTS_PHASE1_PROPOSAL.md | 待审根指令建议稿 |
| D:/知识库/docs/KNOWLEDGE_ARCHITECTURE.md | 架构和隔离规则 |
| D:/知识库/docs/REFACTOR_PLAN.md | 实施与验收记录 |
| D:/知识库/docs/DECISIONS.md | 决策及未解决问题 |
| D:/知识库/99_System/knowledge/README.md | 使用与验收说明 |
| D:/知识库/99_System/knowledge/requirements.txt | 直接依赖版本 |
| D:/知识库/99_System/knowledge/registry.yaml | 类型注册表 |
| D:/知识库/99_System/knowledge/schemas/registry.schema.json | 注册表约束 |
| D:/知识库/99_System/knowledge/schemas/common.schema.json | 公共字段和链接约束 |
| D:/知识库/99_System/knowledge/schemas/concept.schema.json | 概念约束 |
| D:/知识库/99_System/knowledge/schemas/proposition.schema.json | 命题约束 |
| D:/知识库/99_System/knowledge/schemas/method.schema.json | 方法约束 |
| D:/知识库/99_System/knowledge/schemas/moc.schema.json | MOC 约束 |
| D:/知识库/99_System/knowledge/templates/concept.md | 概念模板 |
| D:/知识库/99_System/knowledge/templates/proposition.md | 命题模板 |
| D:/知识库/99_System/knowledge/templates/method.md | 方法模板 |
| D:/知识库/99_System/knowledge/templates/moc.md | 导航模板 |
| D:/知识库/99_System/knowledge/validator.py | 只读验证器 |
| D:/知识库/99_System/knowledge/tests/test_validator.py | 隔离测试 |
| D:/知识库/99_System/knowledge/tests/cases.json | 合成输入与预期诊断 |

## 验收与限制

Phase 1 的历史验证结果为 18 项 unittest 通过。Phase 2A 的检查点、最终测试数量及逐文件基线结果统一记录于 [[docs/REFACTOR_PLAN]]；配置损坏回归现覆盖非 Schema 引用、无条件环、嵌套资源 ID、公共约束丢失和关闭人工审查标记。约 4 KB 的大整数错误诊断也返回输入错误，不改变 Python 全局限制。

Phase 1 历史保护核验（本次 Phase 2A 的逐文件结果见实施记录）：Git 当时恰好列出上述 20 个未跟踪新增文件；既有跟踪文件没有新增修改，原有数学建模/2026国赛与数学建模/AutoMM 两个 dirty gitlink 标记保留，HEAD 未变。未执行 add、commit、push、reset 或 stash。既有文件全量摘要在实施期间发生变化，时间窗口复核仅检出被 Git 忽略的 .obsidian/workspace.json 更新；没有写入或回滚该运行时文件，不能将汇总摘要表述为全体既有文件逐字一致的证明。基线口径与复核说明见实施记录。

独立代码审查的最终结论及任何后续修订记录见 [[docs/REFACTOR_PLAN]]。所有结果仅覆盖获准的系统行为，不代表全库链接或数学内容通过。六处治理入口已按批准的最小补丁统一适用范围；旧属性库记录和旧模板保留原状。Formatter 仍未定位，Phase 2B 及真实笔记迁移没有实施。
