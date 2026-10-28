# 日常知识库使用指南

当前主入口是 [[总览/核心知识工作台]]。概念、知识点、方法目录保留原位置；type 决定并列职责，不能用目录名判断新类型。topics 按需填写指向 role: moc 导航的整篇笔记 Wiki-link；原子之间使用 prerequisites/about/uses/related，目标必须真实存在。title 可省略，tags 由用户显式维护，旧主题保存在 legacy_topics 中。

下面的命令使用已有 Python 与本地依赖，不安装模型或插件。统一入口：D:/知识库/99_System/knowledge/knowledge.py。程序全部使用 -B；命令输出为 JSON。首次操作先阅读输出，错误、跳过和 legacy 不能当成全部通过。

## 新建笔记

可以手动复制 99_System/knowledge/templates/ 中的 Registry 模板，替换正文标题并填写实际内容。也可以使用只生成审查计划的入口：

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" new --vault-root "D:/知识库" --path "概念/示例对象.md" --type concept --backup-dir "D:/KnowledgeRefactorBackups/new-object-独立批次"
```

type 可选 concept、proposition、method、moc；路径不决定类型。可重复 --topic "总览/收敛性与积分理论-MOC.md" 指定已存在且合法的 role: moc 导航；普通概念和仅有历史 type: MOC 的笔记会被拒绝。备份目录必须在 Vault 外且尚不存在；示例名称是占位符，不表示已经创建真实示例笔记。命令只在备份目录生成 plan.json、change.diff 和 payload，不创建目标笔记。已有目标、缺失主题、受保护路径均拒绝。

审查 change.diff，核对返回的 plan_sha256 后：

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" apply --plan "D:/KnowledgeRefactorBackups/new-object-独立批次/plan.json" --approve-plan-sha256 "<该计划完整SHA-256>"
```

只创建有实际内容的条目，不为填满模板制造空卡。正文以后由正常写作维护；本次现有核心笔记的批量工具只允许 YAML 修改。

## 属性、链接与标签审计

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" check-system --format json
python -B "D:/知识库/99_System/knowledge/knowledge.py" check --vault-root "D:/知识库" --file "D:/知识库/概念/可测函数.md"
python -B "D:/知识库/99_System/knowledge/knowledge.py" audit --vault-root "D:/知识库" --scope "概念" --scope "知识点" --scope "方法"
```

审计入口只读：复用 Validator、Link Validator、topics 目标角色检查和标签隔离，不写笔记、不修链接。resolved/ambiguous/unresolved/unchecked/invalid_syntax 是静态结果，不能直接当作 Obsidian 实际断链结论。检查报告里的范围、候选和依据。legacy_topics、legacy_topic_links、exam 等扩展警告允许存在，不自动删除字段。历史中文类型保留 legacy，不能因退出码 0 认定已转换。

旧 tag_maintenance 在规划和执行两处跳过新规范或混合格式，不从 topics、文件名或关系推断 tags。不要对这批新实体运行旧标签写入。字段结构通过与数学正确性、个人掌握程度是三件不同的事。

## 获取 AI 分类和关系建议

程序没有自动模型调用器，不读取凭据，不接新 API。既有 Codex 工作流可以辅助分析；要做严格范围受限建议，应将最小包交给没有工作区、连接器、文件和其他工具权限的独立普通聊天。不要把能读整个 Vault 的 Agent 称为已隔离；不能验证该边界时保留本地包，不启动外部运行。

以下 Git Bash 命令只生成明确范围的本地工件。自行选择一个新的 Vault 外目录，先创建该目录，再执行；不同批次不要覆盖。示例只含一个来源和一个候选，扩大本地索引不会扩大模型可见正文。

```bash
RUN='D:/KnowledgeRefactorBackups/advisory-my-run'
python -B 'D:/知识库/99_System/knowledge/knowledge.py' advisory manifest \
  --vault-root 'D:/知识库' --source '方法/回溯线搜索.md' \
  --candidate '概念/Armijo准则.md' \
  --visible '方法/回溯线搜索.md' --visible '概念/Armijo准则.md' > "$RUN/manifest.json"

python -B 'D:/知识库/99_System/knowledge/knowledge.py' advisory authorize \
  --vault-root 'D:/知识库' --manifest "$RUN/manifest.json" --stage relations > "$RUN/authorization.json"
sha256sum "$RUN/authorization.json"
```

authorization 是操作者生成的本地范围记录，绑定当前清单、文件哈希、根目录和允许阶段；不是模型可提供的授权，也不是身份认证签名。记录授权文件的完整摘要，以下 AUTH_SHA 替换为该摘要：

```bash
AUTH_SHA='<authorization.json 的完整SHA-256>'
python -B 'D:/知识库/99_System/knowledge/knowledge.py' advisory prepare \
  --vault-root 'D:/知识库' --manifest "$RUN/manifest.json" \
  --authorization "$RUN/authorization.json" --authorization-sha256 "$AUTH_SHA" \
  --stage relations --query 'Armijo' --view bundle > "$RUN/request.json"

python -B 'D:/知识库/99_System/knowledge/knowledge.py' advisory prepare \
  --vault-root 'D:/知识库' --manifest "$RUN/manifest.json" \
  --authorization "$RUN/authorization.json" --authorization-sha256 "$AUTH_SHA" \
  --stage relations --query 'Armijo' --view inference > "$RUN/inference.json"
```

只提供 prompts/advisory_v1_2.md、响应协议说明及审查后的 inference.json。**不提供 request.json 的 audit、历史样本清单、人工标注或整个项目对话。** 分类使用 --stage classify，并在 authorize 时授权 classify。正文标题、已有链接仍可能带来线索，不宣称完全盲化。

将模型原始 JSON 响应存为该批次 response.json，再本地验证：

```bash
python -B 'D:/知识库/99_System/knowledge/knowledge.py' advisory check \
  --vault-root 'D:/知识库' --manifest "$RUN/manifest.json" \
  --authorization "$RUN/authorization.json" --authorization-sha256 "$AUTH_SHA" \
  --request "$RUN/request.json" --response "$RUN/response.json"
```

selected 表示已定位一个提供证据的候选 ID，不是检索或数学关系唯一。隐藏候选、截断、循环和旧类型目标仍须复核。伪造引文、路径、ID、过期哈希和越界目标拒收；机器通过仍不能直接写入。没有合适依据时允许弃权，不补虚构双链。

模型拒绝、响应截断、格式不符、文件变化或范围扩大时停止该批次；不自动重试、扩正文、切换服务或修补模型响应。30 篇历史候选及空标注保留为旧工程资料，已随真实迁移过期；不要当作当前授权或继续性能实验，日常使用应重新生成明确范围清单。evaluate 仍不报告真实语义成绩。

## 审查、执行和恢复批量变更

change_control.py 接收操作者审阅过的 changes JSON，顶层为 items；每项必须有 path、expected_sha256（新增为 null）、content_base64 和 reason。它不解释或执行模型输出。先用 plan --vault-root --changes --backup-dir 生成计划；审阅 change.diff、全部路径、原始和目标摘要，再按完整 plan_sha256 执行 apply。

备份必须在 Vault 外；系统与核心范围以外、隐藏路径、联接、独立仓库和任意上跳路径拒绝。现有核心 Markdown 的正文变化拒绝；其他自定义字段和来源由计划制定者核对，不能因验证器警告删除。写入前重核当前字节，冲突逐文件跳过；同一计划再执行不会强制覆盖。

恢复单批次：

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" restore --plan "<该批次plan.json绝对路径>" --approve-plan-sha256 "<该计划完整SHA-256>"
```

只有当前文件仍等于该计划写入结果时才恢复原字节；后续用户修改会产生 conflict_skipped。新增文件恢复时保留，报告 preserved_addition，不自动删除。恢复不是 Git reset，不改历史。备份目录中的 journal.jsonl 保存执行意图与结果；崩溃后可按当前摘要判断，不依赖一句“已执行”。

本次核心批次位于 D:/KnowledgeRefactorBackups/20261028-0050/core-batch/。完整原始快照、逐文件分类与关系依据也在该根目录。系统和导航的逐文件计划位于 batches/，恢复时可把该目录中的 plan.json 当作原始对照；这些引导阶段计划不是 change_control 的格式，不要直接交给其 CLI。整次撤销使用 D:/KnowledgeRefactorBackups/20261028-0050/recovery/plan.json 及其独立摘要，执行同一 restore 命令；该汇总计划兼容 change_control，不用 reset/clean。

## 维护 MOC

打开 [[总览/核心知识.base]] 切换全部原子、概念、命题、方法和“尚无主题”。[[总览/核心知识工作台]] 保留问题驱动路线，[[总览/收敛性与积分理论-MOC]] 按 topics 聚合。不要根据目录或标签强推主题，不要求每个主题创建 MOC。

动态筛选显式版本与类型，并排除系统范围。现有旧 MOC、课程归档和三类 README 保持历史内容；不把它们算原子实体。外部批量修改后若磁盘校验数量与 Bases 不一致，先核查 Obsidian 缓存，不重复改正文或放宽筛选。此次曾发现 13 个 TFile 状态过期，经只更新应用缓存恢复为 215 条，未改笔记。

## 长期检查

新建和关系修改后运行 check 与小范围 audit，定期运行完整 knowledge/tests 和旧标签回归。备份计划、diff、原字节和授权包应一起保留；不要将原字节备份作为真实知识实体导入 Vault。依赖已在 requirements.txt 声明，不自动升级环境。Formatter 仍未定位、未集成；本系统不创建替代 Formatter。

写入与恢复在 Windows 使用禁止共享的独占文件句柄，锁内核对字节并写入；拒绝重解析路径、多硬链接和 Windows 路径别名。被占用或变化的文件跳过，非 Windows 写入失败关闭。plan、payload、original 通过哈希校验的同一份内存字节被用于执行，不重新读取。journal 也采用同样的独占与链接保护。整批不是数据库事务；意外中断时保留原始备份，部分写入不满足恢复前置摘要时停止并由人工核对，不强制覆盖。

## 主题导航与迁移约束

topics 目标先满足显式 role: moc、非系统、Schema 合法和唯一实际解析，再由操作者确认主题是否合适。新建 MOC 使用对应模板，先审查并创建有内容的导航，再生成笔记的 topics 计划；同批尚不存在的导航不会被隐式认可。plan 和 apply 双重检查，目标角色在两次操作间改变时记录 policy_skipped，退出码为 1，原文件保持原状。

旧关键词 legacy_topics 与旧原子锚点 legacy_topic_links 仅供追溯，不用于 MOC 查询，也不据此推导 tags 或其他语义字段。Phase 3 的可测函数、控制收敛定理、控制函数构造法现统一归属收敛性与积分理论 MOC；归档主题索引保留原样。

本次修正备份位于 D:/KnowledgeRefactorBackups/20261028-topics-moc；需跨两轮恢复时，先恢复本轮，再恢复 20261028-0050 轮次。每次都核对恢复计划哈希；并发变化会跳过，新增文件保留，不删除。恢复说明及本轮验收见 [[docs/TOPICS_MOC_ACCEPTANCE_2026-10-28]]。
