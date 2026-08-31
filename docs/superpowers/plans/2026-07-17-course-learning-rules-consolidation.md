# Course Learning Rules Consolidation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidate duplicated vault course-learning rules, preserve old wikilinks through redirect stubs, and embed the cleaned rules into `course-learning/references/` so the skill works outside this vault.

**Architecture:** Treat `规范/` as the vault-facing rule source and `C:/Users/Nuo/.agents/skills/course-learning/references/` as the portable skill-facing rule bundle. First create consolidated active rules, then archive old files with redirect stubs, then build skill references from the consolidated rules, and finally verify links and key constraints.

**Tech Stack:** Obsidian Markdown, YAML frontmatter, Wiki-links, PowerShell, Python 3 standard library, existing `course-learning` scripts.

## Global Constraints

- Vault root is `D:\知识库`; use relative vault paths for vault files such as `规范/课程资料转MD规范.md`.
- Installed skill path is `C:/Users/Nuo/.agents/skills/course-learning/`; use absolute paths for this external skill directory.
- Preserve old rule text by copying full originals to `规范/已归档/2026-07-17/` before replacing old paths with redirect stubs.
- Do not permanently delete old rule content in this implementation.
- Keep `course-learning/SKILL.md` lean: it routes to `references/*.md`; detailed rules live in references.
- Maintain Obsidian-native syntax: YAML frontmatter, `[[wikilinks]]`, callouts, Mermaid code blocks, and relative vault links.
- The current `.git` directory is invalid; do not run `git commit`. Use filesystem archives and verification logs instead.
- Preserve these key rules: OCR attempts stop after 3 failures; processed `未处理项/` files are deleted while the folder remains; Mermaid labels with math/special symbols are quoted; table cells contain no bare `|`; answer files require `source_context` when applicable.

---

## File Structure

### Create active vault rules

- `规范/课程资料转MD规范.md` — PDF/PPTX/image-to-Markdown decision tree, MinerU/OCR/xparse rules, PPTX OMML fallback, frontmatter, validation.
- `规范/课程笔记生成规范.md` — source-MD-to-note rules for 初学版“知识梳理”和复习版“知识汇集”.
- `规范/知识原子卡规范.md` — concept/knowledge/method card boundaries, templates, links, quality checks.
- `规范/Obsidian写作规范.md` — table, tag, Mermaid, wikilink, frontmatter writing rules.
- `规范/质量审查规范.md` — post-change format/content/link verification workflow.
- `规范/考试复习规范.md` — exam outline, highlighted graph, review folder, and exam question generation rules.

### Archive then redirect old vault rules

- `规范/文档转MD规范.md` → `规范/课程资料转MD规范.md`
- `规范/PPTX处理规范.md` → `规范/课程资料转MD规范.md`
- `规范/知识点解析梳理规范.md` → `规范/课程笔记生成规范.md`
- `规范/知识点汇集规范.md` → `规范/课程笔记生成规范.md`
- `规范/概念卡规范.md` → `规范/知识原子卡规范.md`
- `规范/知识点卡规范.md` → `规范/知识原子卡规范.md`
- `规范/方法卡规范.md` → `规范/知识原子卡规范.md`
- `规范/表格规范.md` → `规范/Obsidian写作规范.md`
- `规范/tag规范.md` → `规范/Obsidian写作规范.md`
- `规范/审查规范.md` → `规范/质量审查规范.md`
- `规范/考试纲要规范.md` → `规范/考试复习规范.md`
- `规范/单纯形表规范.md` → `课程/最优化方法/专项规范/单纯形表规范.md`

### Keep active without change

- `规范/习题库规范.md`
- `规范/答疑规范.md`
- `规范/闪卡规范.md`
- `规范/PDF导出规范.md`
- `规范/AI工具规范.md`
- `规范/export_pdfs.py`

### Create or modify skill files

- `C:/Users/Nuo/.agents/skills/course-learning/references/index.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/courseware-to-md.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/course-notes.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/exercises-and-qa.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/exam-review.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/atomic-cards.md`
- `C:/Users/Nuo/.agents/skills/course-learning/references/obsidian-style-quality.md`
- `C:/Users/Nuo/.agents/skills/course-learning/SKILL.md`

---

### Task 1: Snapshot Current Rule and Skill State

**Files:**
- Create: `规范/已归档/2026-07-17/_manifest.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/_backup_2026-07-17/SKILL.md`

**Interfaces:**
- Consumes: current `规范/*.md` and `C:/Users/Nuo/.agents/skills/course-learning/SKILL.md`.
- Produces: rollback archive and manifest.

- [ ] **Step 1: Create backup directories**

Run:
```powershell
New-Item -ItemType Directory -Force -Path '规范/已归档/2026-07-17' | Out-Null
New-Item -ItemType Directory -Force -Path 'C:/Users/Nuo/.agents/skills/course-learning/_backup_2026-07-17' | Out-Null
```
Expected: both directories exist.

- [ ] **Step 2: Back up the existing skill main file**

Run:
```powershell
Copy-Item -LiteralPath 'C:/Users/Nuo/.agents/skills/course-learning/SKILL.md' -Destination 'C:/Users/Nuo/.agents/skills/course-learning/_backup_2026-07-17/SKILL.md' -Force
```
Expected: backup file exists.

- [ ] **Step 3: Copy old rule files into the archive**

Run:
```powershell
$files = @('文档转MD规范.md','PPTX处理规范.md','知识点解析梳理规范.md','知识点汇集规范.md','概念卡规范.md','知识点卡规范.md','方法卡规范.md','表格规范.md','tag规范.md','审查规范.md','考试纲要规范.md','单纯形表规范.md')
foreach ($f in $files) { Copy-Item -LiteralPath (Join-Path '规范' $f) -Destination (Join-Path '规范/已归档/2026-07-17' $f) -Force }
```
Expected: all 12 old rule files exist under `规范/已归档/2026-07-17/`.

- [ ] **Step 4: Create archive manifest**

Create `规范/已归档/2026-07-17/_manifest.md` with a table mapping each old file to its new active entry exactly as listed in “Archive then redirect old vault rules”.
Expected: manifest includes 12 mappings.

- [ ] **Step 5: Verify snapshot count**

Run:
```powershell
(Get-ChildItem -LiteralPath '规范/已归档/2026-07-17' -Filter '*.md').Count
```
Expected: `13`.

---

### Task 2: Create Consolidated Vault-Facing Active Rules

**Files:**
- Create: `规范/课程资料转MD规范.md`
- Create: `规范/课程笔记生成规范.md`
- Create: `规范/知识原子卡规范.md`
- Create: `规范/Obsidian写作规范.md`
- Create: `规范/质量审查规范.md`
- Create: `规范/考试复习规范.md`

**Interfaces:**
- Consumes: archived originals.
- Produces: active consolidated rules referenced by redirect stubs and skill references.

- [ ] **Step 1: Create `规范/课程资料转MD规范.md`**

Include sections: 适用场景, 方案决策, MinerU 云 API, MinerU 本地, pdftocairo + Tesseract OCR, xparse-cli, PPTX 专项规则, 输出 frontmatter, 后处理清单, 验证检查点, 反模式, 相关规范.
Mandatory strings: `m:f`, `m:d`, `C:/Program Files/Tesseract-OCR/tesseract.exe`, `(?<=[一-鿿])\s+(?=[一-鿿])`, `3 次`, `<a:blip>`, `Unicode`, `\c\dots`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 2: Create `规范/课程笔记生成规范.md`**

Include sections: 两类输出的边界, 知识点解析梳理（初学导向）, 知识点汇集（复习导向）, Frontmatter 模板, 文件命名, Mermaid 与格式规则, 生成流程, 质量检查清单.
Mandatory strings: `知识梳理`, `知识点汇集`, `固定9板块`, `一句话来说`, `全量覆盖`, `<br/>`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 3: Create `规范/知识原子卡规范.md`**

Include sections: 四层体系与职责边界, 概念卡, 知识点卡, 方法卡, Frontmatter 模板, 链接规则, 生成流程, 质量检查清单.
Mandatory strings: `概念卡`, `知识点卡`, `方法卡`, `相关概念`, `习题链接`, `oxed{}`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 4: Create `规范/Obsidian写作规范.md`**

Include sections: Frontmatter, Wiki-link, Tag, Markdown 表格, Mermaid, Callout, LaTeX, 验证清单.
Mandatory strings: `禁止裸`, `ert`, `\Vert`, `\mid`, `Mermaid`, `Wiki-link`, `tags`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 5: Create `规范/质量审查规范.md`**

Include sections: 触发时机, 格式检查, 内容检查, Wiki-link 检查, 课程资料转换检查, 输出格式, 修复闭环.
Mandatory strings: `重新验证`, `Frontmatter`, `Callout`, `OCR`, `Mermaid`, `**答案**：`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 6: Create `规范/考试复习规范.md`**

Include sections: 适用场景, 考点提取, 考试纲要, 考试图谱-重点标注, 复习文件夹, 考题生成, 准确性验证清单.
Mandatory strings: `考试纲要`, `考试图谱-重点标注`, `复习/README.md`, `常考查的证明`, `考题不是课后习题`.
Expected: file exists and all mandatory strings are present.

- [ ] **Step 7: Verify new active rules**

Run a PowerShell `Select-String` check for the mandatory strings listed in Steps 1-6.
Expected: every mandatory string is found.

---

### Task 3: Replace Old Rule Paths with Redirect Stubs

**Files:**
- Modify: old rule files listed above.
- Create: `课程/最优化方法/专项规范/单纯形表规范.md`.

**Interfaces:**
- Consumes: archived originals and active rules.
- Produces: stable old wikilink targets and course-specific simplex rule location.

- [ ] **Step 1: Create the course-specific rule directory**

Run:
```powershell
New-Item -ItemType Directory -Force -Path '课程/最优化方法/专项规范' | Out-Null
```
Expected: directory exists.

- [ ] **Step 2: Copy simplex original to course-specific location**

Run:
```powershell
Copy-Item -LiteralPath '规范/已归档/2026-07-17/单纯形表规范.md' -Destination '课程/最优化方法/专项规范/单纯形表规范.md' -Force
```
Expected: the course-specific file contains the full simplex table rule.

- [ ] **Step 3: Replace old paths with redirect stubs**

For each old rule file, replace content with YAML frontmatter containing `type: 规范跳转`, `status: 已整合` or `status: 已迁移`, and `redirect_to`, followed by one paragraph linking to the new entry and one paragraph linking to the archived original.
Expected: 12 old paths are redirect stubs, not deleted files.

- [ ] **Step 4: Verify redirect count**

Run:
```powershell
(Get-ChildItem -LiteralPath '规范' -Filter '*.md' | Select-String -Pattern 'type: 规范跳转').Count
```
Expected: `12`.

---

### Task 4: Update Vault Instruction Index

**Files:**
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: new active rules.
- Produces: current rule index for future agents.

- [ ] **Step 1: Replace the course rule index table in `AGENTS.md`**

The table under `## 课程规范文件（索引）` must list these active rules: 课程资料转MD规范, 课程笔记生成规范, 习题库规范, 答疑规范, 考试复习规范, 知识原子卡规范, Obsidian写作规范, 质量审查规范, 闪卡规范, PDF导出规范, AI工具规范.
Expected: archived rules are not presented as primary active rules.

- [ ] **Step 2: Add archive note**

Add below the table:
```markdown
> 旧规范如 `文档转MD规范`、`PPTX处理规范`、`知识点解析梳理规范` 等已保留为跳转文件，原文归档在 [[规范/已归档/2026-07-17/_manifest|2026-07-17 规范归档清单]]。
```
Expected: future agents can find old texts and new active entries.

- [ ] **Step 3: Verify AGENTS index**

Run:
```powershell
Select-String -LiteralPath 'AGENTS.md' -Pattern '课程资料转MD规范|课程笔记生成规范|知识原子卡规范|Obsidian写作规范|质量审查规范|考试复习规范'
```
Expected: all six new active rule names appear.

---

### Task 5: Create Portable Skill References

**Files:**
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/index.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/courseware-to-md.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/course-notes.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/exercises-and-qa.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/exam-review.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/atomic-cards.md`
- Create: `C:/Users/Nuo/.agents/skills/course-learning/references/obsidian-style-quality.md`

**Interfaces:**
- Consumes: active vault rules plus `习题库规范.md` and `答疑规范.md`.
- Produces: portable rule bundle for `course-learning/SKILL.md`.

- [ ] **Step 1: Create references directory**

Run:
```powershell
New-Item -ItemType Directory -Force -Path 'C:/Users/Nuo/.agents/skills/course-learning/references' | Out-Null
```
Expected: references directory exists.

- [ ] **Step 2: Create `references/index.md`**

Create a route table mapping: courseware conversion → `courseware-to-md.md`; note generation → `course-notes.md`; exercises/Q&A → `exercises-and-qa.md`; exam review → `exam-review.md`; atomic cards → `atomic-cards.md`; all routes finish with `obsidian-style-quality.md`.
Expected: index exists and names all six route files.

- [ ] **Step 3: Create the six detail references**

Copy/adapt the active rules into these references:
- `courseware-to-md.md` from `规范/课程资料转MD规范.md`.
- `course-notes.md` from `规范/课程笔记生成规范.md`.
- `exercises-and-qa.md` from `规范/习题库规范.md` + `规范/答疑规范.md`.
- `exam-review.md` from `规范/考试复习规范.md`.
- `atomic-cards.md` from `规范/知识原子卡规范.md`.
- `obsidian-style-quality.md` from `规范/Obsidian写作规范.md` + `规范/质量审查规范.md`.
Expected: references are portable and do not require vault `规范/` paths to be useful.

- [ ] **Step 4: Verify reference count and key strings**

Run:
```powershell
(Get-ChildItem -LiteralPath 'C:/Users/Nuo/.agents/skills/course-learning/references' -Filter '*.md').Count
Select-String -LiteralPath 'C:/Users/Nuo/.agents/skills/course-learning/references/index.md' -Pattern 'courseware-to-md|course-notes|exercises-and-qa|exam-review|atomic-cards|obsidian-style-quality'
```
Expected: first command prints `7`; second command prints matches for all six route files.

---

### Task 6: Refactor `course-learning/SKILL.md` to Use References

**Files:**
- Modify: `C:/Users/Nuo/.agents/skills/course-learning/SKILL.md`

**Interfaces:**
- Consumes: `references/index.md` and six detail references.
- Produces: lean skill router that no longer depends on vault `规范/` files.

- [ ] **Step 1: Preserve frontmatter name and trigger-rich description**

Keep `name: course-learning` and the existing description about courseware processing, knowledge organization, exercise extraction, Q&A, exam review, and Chinese course-learning phrases.
Expected: skill identity and triggering behavior remain stable.

- [ ] **Step 2: Replace body with lean router**

Body must contain: core idea, first action after trigger, intent routing table, scripts list, and red lines. It must instruct the agent to read `references/index.md`, then matching reference files, then `references/obsidian-style-quality.md` before completion.
Expected: `SKILL.md` contains `references/index.md` and does not inline the old long duplicated rule bodies.

- [ ] **Step 3: Verify skill no longer hard-depends on vault rules**

Run:
```powershell
Select-String -LiteralPath 'C:/Users/Nuo/.agents/skills/course-learning/SKILL.md' -Pattern '规范/'
```
Expected: no matches, or only a sentence saying local `规范/` may be consulted when explicitly requested.

---

### Task 7: Verification and Completion Report

**Files:**
- Create: `docs/superpowers/plans/2026-07-17-course-learning-rules-consolidation-verification.md`

**Interfaces:**
- Consumes: all changes from Tasks 1-6.
- Produces: evidence that rule consolidation and skill embedding are complete.

- [ ] **Step 1: Verify active rule files exist**

Run a `Test-Path` check for all active rule files listed in File Structure.
Expected: every active rule file exists.

- [ ] **Step 2: Verify archived originals exist**

Run a `Test-Path` check for the 12 archived originals in `规范/已归档/2026-07-17/`.
Expected: every archived original exists.

- [ ] **Step 3: Verify redirect stubs exist and point somewhere**

Run a check that the 12 old paths contain `type: 规范跳转` and at least one `[[...]]` wikilink.
Expected: every old path is a redirect stub.

- [ ] **Step 4: Verify skill references exist**

Run a `Test-Path` check for all seven files in `C:/Users/Nuo/.agents/skills/course-learning/references/`.
Expected: every reference exists.

- [ ] **Step 5: Verify key constraints survived**

Search across active rules and skill references for: `3 次`, `m:d`, `m:f`, `一句话来说`, `固定9板块`, `禁止裸`, `Mermaid`, `重新验证`, `source_context`.
Expected: every key constraint appears at least once in the appropriate active rule/reference.

- [ ] **Step 6: Write verification log**

Create `docs/superpowers/plans/2026-07-17-course-learning-rules-consolidation-verification.md` with pass/fail rows for active rules, archives, redirects, skill references, key constraints, and Git skipped because `.git` is invalid.
Expected: verification log exists.

- [ ] **Step 7: Final user report**

Report new active rules, archived old rules, updated skill references, updated `SKILL.md`, verification log, and the fact that commit was skipped because the vault is not a valid Git repository.
Expected: user receives concise summary with clickable vault links.

---

## Self-Review

- Spec coverage: Tasks 1-3 cover consolidation and archiving; Task 4 covers `AGENTS.md`; Tasks 5-6 cover portable skill references and `SKILL.md`; Task 7 covers verification.
- Placeholder scan: the plan contains no open-ended markers requiring later invention.
- Path consistency: vault files use relative paths; skill files use `C:/Users/Nuo/.agents/skills/course-learning/` absolute paths.
- Git constraint: plan explicitly skips commits because this directory is not a valid Git repository.
