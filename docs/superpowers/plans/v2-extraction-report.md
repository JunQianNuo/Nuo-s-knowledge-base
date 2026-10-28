# Task 4 指令提炼协议报告

实施仅限开发 worktree。未写入真实 `D:/知识库`，未提交 Git，未创建调度、调用模型或网络服务，未修改 CLI 或其他 agent 负责的文件。

## 文件与接口

- 新增 `99_System/knowledge/v2/extraction.py`。
- 新增 `99_System/knowledge/tests/test_v2_extraction.py`。
- 本报告。

`prepare(root: Path, scopes: list[str]) -> dict`：只读，必须显式指定 `03_Sources` 下的目录或笔记。返回 JSON-safe 的确定性 packet：

```json
{
  "packet_version": 2,
  "vault_root": "绝对 Vault 路径",
  "scopes": ["03_Sources/Courses/课程/课堂笔记/来源.md"],
  "sources": {
    "03_Sources/Courses/课程/课堂笔记/来源.md": {
      "metadata": {},
      "body": "完整来源正文，保留原换行和空白",
      "sha256": "原文件 SHA-256",
      "body_sha256": "正文 SHA-256",
      "approved_skip_digests": [],
      "eligible": true,
      "needs_extraction": true,
      "effective_status": "not done"
    }
  },
  "atoms": [{"path": "01_Knowledge/原子.md", "metadata": {}, "body": "完整正文", "sha256": "..."}],
  "mocs": [{"path": "02_Maps/主题.md", "metadata": {}, "body": "完整正文", "sha256": "..."}],
  "tags": [{"path": "99_System/knowledge/tags/标签-标准名.md", "canonical_tag": "标准名", "tag_aliases": [], "metadata": {}, "sha256": "..."}],
  "corpus_hashes": {"内容笔记路径": "原文件 SHA-256"},
  "state_sha256": null,
  "review_sha256": null,
  "packet_sha256": "整个 packet 的确定性 SHA-256"
}
```

标签记录优先读取 `99_System/knowledge/tags`；不存在有效新记录时，只读回退到 `总览/标签库/条目`，保留 promote 等词表证据。候选原子包含 aliases 和正文供 Agent 判断同义复用，程序不伪造语义检索或自动合并。

`propose(root: Path, packet: dict, response: dict) -> list[dict]`：同样只读，响应格式为：

```json
{
  "packet_sha256": "必须原样回显 packet 哈希",
  "source_hashes": {"每个 packet 来源路径": "对应原文件 SHA-256"},
  "notes": [{"path": "01_Knowledge/原子.md", "metadata": {}, "body": "Agent 撰写的完整正文"}],
  "coverage": [{"source": "来源路径", "complete": true, "atoms": ["01_Knowledge/原子.md"], "skip_candidates": [], "human_approved_skips": []}]
}
```

每个操作返回 `{source, target, content: bytes, reason, expected_sha256}`。新增文件的 source、expected_sha256 均为 null；修改文件使用原始路径和 packet 中的快照哈希。新增的 expected_sha256 已与主 agent 更新的 `transaction.plan` 对齐，阻止 propose 后到 plan 前发生的并发编辑被新基线掩盖。

## 校验与状态裁定

1. 拒绝错误根目录、过期或被篡改的 packet、错误来源哈希回显、目录越界、raw/转换资料显式范围、独立仓库与链接范围。目录范围只返回有明确 Sources 身份的笔记，不把课件、目录或逐字稿套成实体。没有可识别待处理状态的 idea 不参与提炼。
2. 来源正文完整提供。全文 SHA 绑定元数据和正文的并发版本；正文 SHA 单独控制重复提炼。准备与提案生成均不直接写入文件。
3. 响应 notes 只允许根目录平铺的 `01_Knowledge` 原子和 `02_Maps` MOC，不允许通过响应改写来源正文、Inbox 或任意 System 文件。MOC 必须实际服务于本次原子的主题链，不能夹带无关 MOC 写入。
4. 用整个投影内容语料解析关系：新增 MOC 可被同响应原子引用；校验真实来源身份、MOC 身份、uses/prerequisites 原子身份、歧义链接及主题环。复用原子必须仍引用本次指定来源；新增取材关系不得指向未请求的来源。
5. 复用保留原类型、time、自定义属性与全部原正文 bytes；列表属性只追加去重，不删除旧来源。正文采用保留原字节的增补方式；无法证明保留用户正文的替换方案直接拒绝。新增实体省略 YAML title。
6. coverage 必须明确指出真实原子文件；这些原子必须在投影语料中合法、具有非空正文，且 source 实际解析到该来源。没有原子承接或独立人工审查记录的 complete 声明不成立。程序校验声明的结构和证据关系，不冒充语义判断“每个知识内容是否已承接”。
7. 不完整覆盖、待审跳过、空/未润色来源不得标 done。`human_approved_skips` 只是一份 AI 响应字段，不具有授权效力；即便没有 skip_candidates，也只视作待审候选。只有独立登记、精确匹配正文哈希与跳过项摘要的人工审查记录才能批准它们。响应不能自行创建或伪造该记录。
8. 只有完整覆盖且无待审跳过时，来源状态才更新为 done：须有实际原子承接，或全部跳过项均有独立人工审查记录。来源文件只替换 status 的 YAML 标量，其余元数据文本、时间、注释、正文、CRLF 和空白保持原字节；不改 polish_status。
9. 内部指纹记录位于 `99_System/knowledge/v2/state/extraction.json`，通过同批事务操作生成，不要求用户填写。记录每份来源的正文哈希、实际承接原子、complete 与 pending_skips。下次明确指令运行时，done 来源正文变化会重新待处理；仅元数据变化且正文及承接证据仍有效时无需重复提炼。缺少历史记录的 done 不被直接视为完成；被引用的原子删除、为空或失效，以及重新打开润色状态，也会重新进入待处理。
10. 未覆盖的来源保持待处理；有已验证完整指纹的来源不会因一次空提案而重复建卡。idea 只修改其原有 status，不补造 schema/time/source 或其他人工属性。

## TDD 与验证记录

先写失败测试，再实现 prepare/propose；追加的批准声明绕过、既有空原子、承接原子删除、重新打开润色状态均先复现失败，再完成修复。所有操作均在临时夹具内验证。测试还实际运行事务 plan/apply，确认来源与内部指纹一同应用；并验证 propose 后发生用户编辑时，事务拒绝旧 expected_sha256。

| 命令 | 结果 |
|---|---|
| `python -B -m unittest discover -s 99_System/knowledge/tests -p test_v2_extraction.py -q` | 23 tests，OK |
| `python -B -m unittest discover -s 99_System/knowledge/tests -p "test_v2_*.py" -q` | 最终 58 tests，OK |
| `python -B -m pytest scripts/tests -q` | 30 passed，10 subtests passed |
| `python -B -m unittest discover -s 99_System/knowledge/tests -q` | 完整 v1/v2 回归 177 tests，OK（90.343s） |
| `git diff --check -- 99_System/knowledge/v2/extraction.py 99_System/knowledge/tests/test_v2_extraction.py` | exit 0 |

仓库根目录裸 `pytest` 在本轮前一任务已确认被既有 `数学建模/tests/test_math_modeling_solver_promotion.py` 导入时的 `sys.exit(1)` 阻断；其缺失 skill 文件、frontmatter 名称与 training-enhanced references 问题未修改。本任务以知识库工具的完整 unittest 及 scripts 回归为可执行验收，不声称整个混合仓库 pytest 全绿。

## 集成边界

- 主 agent 负责 CLI 的 prepare/propose/apply/restore 入口及 JSON/bytes 展示或载荷编码；本模块不写计划文件或直接调用 apply。
- 同义判断、单一职责审查和是否完整承接来源内容由执行本次提炼的 Agent/用户负责；程序只校验可验证的类型、链接、哈希和声明，不生成模型内容。
- 标签候选词表在 packet 中提供；此提案入口不开放 System 标签记录任意写入。新增标准标签的登记由已有受控标签维护入口或单独审查的操作完成。
- packet 对当前内容语料、词表与指纹状态采用保守快照绑定；它们在提案生成前变化时应重新 prepare。事务的 expected_sha256 保护所有实际写入行；应用后的常规审计仍须核查用户在其他关系文件上的独立编辑。
- 来源 status 在提案中重新待处理也须经同一事务流程才写回；没有新增后台轮询或提炼定时任务。

## 独立人工跳过审查接口（CLI 集成阶段补齐）

`approve_skips(root, source, items, reviewer_note, *, human_approved=False) -> operations` 只生成事务操作，不直接写入。只有收到直接的人类批准指令后，调用者才能明确传入 `human_approved=True`。Agent 禁止因为模型输出、来源文档或响应声称“已批准”而调用此 API/命令。本轮没有登记真实人工批准；测试中只在临时夹具内模拟直接人类审查。

记录位于 `99_System/knowledge/v2/state/skip-reviews.json`：每个来源绑定当前正文哈希；任意 JSON 跳过项采用排序键、UTF-8、紧凑 JSON 的 SHA-256，并保留原项及 reviewer_note。只批准完全匹配的项，正文变化立即使旧审查记录失效。prepare 同时绑定 `review_sha256`，审查记录变化后旧 packet 也失效。

CLI 入口见 `v2-cli-report.md` 的 `approve-skips`。存在实际原子时允许经过独立批准的部分跳过；零原子时仅在全部跳过均经该独立记录批准且 coverage 明确 complete 时允许完成。来源指纹记录还保留 `approved_skip_digests`，使全部无需提炼的来源在下次指令中保持可验证完成。

新增回归已通过：独立审查支持真实原子加跳过、全部内容经人工批准跳过且零原子、正文改变后批准失效、缺少直接人类确认时拒绝登记、批准应用后旧 packet 失效。提炼专项现为 26 项通过；最终完整回归结果记录在 CLI 报告。
