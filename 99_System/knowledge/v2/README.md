# Knowledge v2 维护入口

从 [[Home]] 进入学科主题、课程资料、来源提炼状态与待处理视图。属性与目录规则见 [[docs/KNOWLEDGE_ARCHITECTURE]]。

## 给 Agent 的日常指令

> 按知识库 v2 规则整理 Sources 中尚未完成提炼的笔记。先检索已有原子、MOC 和标签，复用已有知识，自主创建必要原子、主题和标签；保留真实来源。无需提炼的候选交给我审查，未完成或待审的来源保持 not done。使用哈希绑定的迁移事务保存 diff、备份和恢复记录。

也可限定某门课程或某一篇笔记。指令是执行授权，正常流程自主完成，不逐篇重复确认。不要自己批准无需提炼，也不要伪造作者、创建时间、出处或完整覆盖。

## 工具入口

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" v2 audit --vault-root "D:/知识库"
python -B "D:/知识库/99_System/knowledge/knowledge.py" v2 prepare --vault-root "D:/知识库" --scope "03_Sources/Courses/数理统计/课堂笔记" --output "C:/Users/Nuo/.codex/backups/knowledge-v2-20261028/数理统计提炼包.json"
python -B "D:/知识库/99_System/knowledge/knowledge.py" v2 --help
```

prepare 生成明确范围、全文、源哈希、已有知识与词表上下文。Agent 读完整来源后生成提案，propose 验证提案、来源快照、主题和来源角色；apply 应用精确哈希绑定的事务；restore 按备份恢复并保留之后的用户编辑。完整参数以各命令 --help 为准。

- 新笔记使用 `99_System/knowledge/v2/templates`，从 v2 new/propose 入口补齐实际 time、来源、主题，不将占位模板当成完整知识。
- 原子笔记只有一个职责，topics/source 必填；不设置 subject 或学习掌握状态。
- 课程来源笔记 subject 使用统一课程名列表；time 为创建时间，lecture_date 和 due_date 分别记录上课与截止日期。
- status=done 仅代表原子归档完成。课堂笔记是否润色完成由 polish_status 表示。
- idea 属性用户自填，Agent 不擅自补写个人思考的出处。
- 书籍/论文/网页每篇以一份主要资料为中心；作者等字段描述主要资料，补充资料进入 source。
- 新标签先查标准名和同义词；确需新增可由 Agent 登记，不按主题名批量补标签。
- 来源正文变化后在下次指令中重新检查；元数据调整不无条件重复提炼。

## 数据库刷新

MOC、来源和课程数据库动态读取文件属性。原子新增后会进入匹配主题的视图；修改 MOC 上层关系后，通过 v2 views 刷新递归闭包。视图辅助数据放在 System，不让用户手填全部祖先 topics。

课程 PPT/PDF 放在课程目录，配套图片进入 Assets。复习笔记在 Reviews 中，课程资料视图通过 subject 找到跨目录、跨课程内容。

## 恢复与历史

每个应用批次在 Vault 外保存 plan.json、original、payload、diffs、journal.jsonl 和计划 SHA-256。恢复命令：

```powershell
python -B "D:/知识库/99_System/knowledge/knowledge.py" v2 restore --plan "批次目录/plan.json" --approve-plan-sha256 "该计划的SHA256"
```

恢复也会检查当前字节，不能覆盖新编辑。历史迁移例外与本次实际统计见验收报告；Inbox 中的条目不算通过 v2 的知识实体。不要把旧已完成/已整理状态直接转换为新 done。
