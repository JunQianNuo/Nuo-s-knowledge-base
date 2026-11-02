# 知识库 v2 重构验收记录（2026-10-28）

实际数据位于 `D:/知识库`，入口为 [[Home]]。架构与属性约定见 [[docs/KNOWLEDGE_ARCHITECTURE]]，日常操作见 [[docs/KNOWLEDGE_DAILY_GUIDE]]。开发 worktree 只用于代码隔离，不是资料库的数据根。

## 实际结果

| 项目 | 验收快照 |
|---|---:|
| 原子笔记 | 196：concept 82、proposition 45、method 69 |
| 主题 MOC | 11 |
| 来源笔记 | 612：lecture 96、review 120、homework 396 |
| 来源提炼状态 | done 1、not done 611 |
| 有效实体合计 | 819（不含 System、原始资料和 Inbox） |
| 标准标签 | 1,349（同义名称另存 tag_aliases） |
| Inbox Markdown | 251 |

主要目录已落地：原子平铺 Knowledge，MOC 使用可多父的主题层级；课程及其 PPT/PDF 在 Sources/Courses，跨课程复习在 Sources/Reviews；图片进入 Assets。MOC/标签/课程/来源/待处理均有原生 Bases 入口。主题新增自动进入主题数据库；MOC 层级变化后由 views 更新递归闭包。

完成原始迁移计划全部 12,290 项。原 PDF 阅读器占用解除后，已核对两份文件的相同 SHA-256 并完成最后一项移动；没有遗留旧 PDF 路径。课程采集脚本与 exe 均已适配，status 与 polish_status 分离；索引刷新保留人工题注、表格链接、补充行和自定义说明。本轮没有新增定时提炼、修改采集计划或主动联网采集。

## 验证证据

- 知识管理回归：`python -B -m unittest discover -s 99_System/knowledge/tests -p "test_*.py"`，214 项通过。
- 课程脚本回归：`python -B -m unittest discover -s scripts/tests -p "test_*.py"`，30 项通过。
- 真实数据 v2 audit：0 个错误；验证原子属性、真实来源角色、MOC 归属与主题无环。
- 9,370 份迁移资源文件全部与计划中的 SHA-256 一致。最终事务覆盖 12,372 个路径，旧移动路径均已移除；并行编辑的索引通过单独快照保留，没有强行回写。
- 对 3,672 份内容与导航文件检查可识别的 Wiki/Markdown/reference/HTML/Canvas 引用，没有剩余可确定改写的旧迁移目标；表格的转义别名分隔符也已修复。这不等于历史库所有缺失、歧义或正文锚点问题已经解决。
- 录音程序以 PyInstaller 6.22.2 重新构建，实际部署 exe 的离线 `--help` 通过。Bases 结构已生成并验证；本轮未在 Obsidian GUI 内逐个渲染验收。

真实提炼使用 [[03_Sources/Courses/归档/实变函数/作业/01-集合论与点集拓扑基础/作业1.2-可列集平移后不相交-习题]]，建立 [[01_Knowledge/集合的平移]] 与 [[01_Knowledge/可数集存在不相交的平移]]。原来源正文逐字节保留，完整覆盖后才置 done；再次 prepare 的 needs_extraction=false。没有跳过任何内容，没有创建人工豁免审批。

[[03_Sources/Reviews/概率论/专题复习/概率密度函数-专题复习]] 因同时展开定义、性质、方法与例题，完整保留为 review，维持 not done；概念入口复用 [[01_Knowledge/概率密度]]，增加同义别名，标签也统一标准名。被合并的旧标签记录保留审计信息。

## 保留与待处理边界

迁移产生的 249 篇 Inbox 分为 36 篇待核实核心内容、213 篇待核实来源内容；另外 2 篇是并行工作新增的缺失录音记录。混合职责、缺乏足够来源或无法可靠判型的内容均完整保留，未硬塞进原子类型。611 篇来源保持 not done，不能将本次目录迁移等同于全库内容提炼完成。

历史语义审查对 66 篇边界条目记录了逐文件判断与证据，其中 27 篇方法笔记的新增来源是本次确实查阅、用于核对整合的课程资料，不宣称这些就是笔记最初创作时的历史来源。审查记录见 [[docs/superpowers/plans/legacy-semantic-decisions.json]]。

time 优先保留已有创建字段；可追溯的历史条目使用跨 Git 重命名的首次记录时间，850 篇修正了复制导致的偏晚时间；仍无可靠记录的使用文件系统创建时间并保留来源依据，不能断言等于最初创作时刻。

原有用户修改与独立项目边界保留。AI、语言、考研、每日疑惑、闪卡、数学建模只修复确定的受迁移影响引用。清理仅调用非递归空目录删除：移除 373 个空目录，并在新课程位置保留未处理项目录。旧 `课程/概率论/知识点解析梳理` 中 43 个隐藏调试文件及其 3 层目录未删除。未定位旧 Formatter，不声称已经集成。

## 备份与恢复

所有批次的计划、逐文件 diff、原件、载荷、日志和计划哈希保存在 Vault 外：

[备份及恢复说明](C:/Users/Nuo/.codex/backups/knowledge-v2-20261028/README.md)

完整机器证据位于同目录：`final-byte-verification.json`、`final-moved-link-verification.json`、`real-extraction-verification.json`、`migration-001/migration-report.json`、`time-history-details.json`、`concurrent-generated-updates.json`、目录清理计划与结果。恢复按批次逆序执行，遇到之后的用户编辑必须停下核对，不覆盖；PDF 临时复制批次不能再次恢复。详见备份说明。


## 2026-11-01 用户修正

课程源资料附件集中迁移已撤回，8,910 份配套图片回到源资料相对目录；原日期的验收记录保留，当前附件规则和实际还原证据见 [[docs/COURSE_ASSET_RESTORE_2026-11-01]]。
