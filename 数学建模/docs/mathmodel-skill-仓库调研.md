---
title: mathmodel-skill 仓库调研
aliases:
  - mathmodel-skill 调研
  - handsomeZR-netizen mathmodel-skill
tags:
  - 数学建模
  - agent-skill
  - GitHub调研
source: https://github.com/handsomeZR-netizen/mathmodel-skill
reviewed_commit: d3941e14d8693fb4a79948e59afff3098734127e
reviewed_at: 2026-08-12
---

# mathmodel-skill 仓库调研

> [!summary] 结论
> 这是一个**“竞赛项目操作系统”型** Skill，而不是单纯的模型知识库或算法模板库。它最值得借鉴的是：持久状态、阶段门禁、局部回修、确定性脚本、竞赛合规和 AI 使用台账。它与本地 `math-modeling-solver-copy` 的关系是**流程治理层 vs. 解题知识与实现层**，适合选择性融合，不适合整仓覆盖。

## 1. 调研范围与版本

- 仓库：[handsomeZR-netizen/mathmodel-skill](https://github.com/handsomeZR-netizen/mathmodel-skill)
- 固定提交：[d3941e1](https://github.com/handsomeZR-netizen/mathmodel-skill/commit/d3941e14d8693fb4a79948e59afff3098734127e)，提交时间为 2026-07-22。
- 调研日期：2026-08-12。
- 固定版本包含 103 个受 Git 跟踪文件，约 672 KiB；其中 56 个 Markdown、17 个 Python、20 个 JSON、3 个 TeX 文件。
- 仓库采用 MIT License，可修改和再分发，但复制实质内容时必须保留版权和许可声明。[许可文件](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/LICENSE)

## 2. 产品定位

仓库自述的目标不是“一次生成整篇论文”，而是把 72–96 小时的数学建模竞赛组织成可恢复、可检查、可局部修改的十阶段项目。核心对象不是某个模型，而是整条决策链：

```text
题目与团队约束
  ↓
10 阶段主流程 ↔ decision_log.json
  ↓
模型 → 求解 → 验证 → 论文 → 合规终审
  ↑                     ↓
  └──── L1/L2/L3/L4 定向反馈 ────┘
```

它明确支持 CUMCM、MCM/ICM 和电工杯，提供 Codex Skill、Codex Plugin 和 Claude Code 的入口；触发边界也较清楚：仅面向这三类建模竞赛，不应被普通数据分析或一般论文评审触发。[主 Skill](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/SKILL.md)

## 3. 架构与核心组件

### 3.1 十阶段工作流

| 阶段 | 主要任务 | 主要产物 |
|---|---|---|
| 0 | 团队启动、工具与规则预检 | 角色、预算、规则基线、环境状态 |
| 1 | 多题比较与选题 | 选择理由、风险、题型 |
| 2 | 题目拆解 | 子问、变量、约束、依赖图、数据 schema |
| 3 | 模型选型 | 候选、否决理由、toy demo、red-team |
| 4 | Foundation | 假设、符号、术语 |
| 5 | 逐子问建模与求解 | 公式、代码、结果、图、per-Qi 状态 |
| 6 | 验证与稳健性 | 风险匹配的检验、区间、失败边界 |
| 7 | 模型评价 | 有证据的优点、局限、改进、迁移条件 |
| 8 | 论文装配 | 稳定的 Markdown 工作区、TeX/PDF、AI 台账 |
| 9 | 提交前终审 | 合规门、终稿 Panel、最终提交状态 |

各阶段细则被拆到 `references/stage_00_*` 至 `stage_09_*`，主 `SKILL.md` 负责调度并要求按阶段懒加载。这种“主文件短、细节按需读”的结构有利于控制上下文和减少规则漂移。[阶段目录](https://github.com/handsomeZR-netizen/mathmodel-skill/tree/d3941e14d8693fb4a79948e59afff3098734127e/references)

### 3.2 持久状态

`templates/shared/decision_log.json` 是整个方案的关键：保存竞赛、题型、当前阶段、各子问状态、评分、回退、合规和 AI 使用记录。它把“聊天记忆”变成“项目状态”，允许中断恢复、换 Agent、按 Qi 局部返工。[状态模板](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/templates/shared/decision_log.json)

### 3.3 四层反馈

- **L1**：每阶段/每子问结构化评分，低分触发局部补丁。
- **L2**：跨阶段一致性回检，例如结果是否推翻选型前提、符号和假设是否漂移。
- **L3**：终稿多视角 Panel，覆盖数学严谨性、建模贡献、代码复现、表达与赛制。
- **L4**：证据校准与反例/边界检查。

Stage 5 还实现了 `pass`、`pass_with_review`、`refine_partial`、`block` 等状态：单个子问失败时可以只回修该 Qi，未解决的高严重度问题不能被均分掩盖。[Stage 5](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/stage_05_subproblem_loop.md)

### 3.4 确定性脚本

| 脚本 | 用途 |
|---|---|
| `doctor.py` | 包结构、竞赛包、状态 schema、模板 marker、工具链预检 |
| `score_artifact.py` | 校验评分 JSON、重算 verdict、聚合 per-Qi |
| `extract_diff.py` | section-level patch 与 unified diff 应用 |
| `render_paper.py` | Markdown 工作区装配为竞赛 TeX/PDF |
| `render_ai_usage.py` | 从台账生成 CUMCM/MCM AI 披露产物 |
| `ingest_papers.py` | 维护期论文语料统计 |
| `download_cumcm_papers.py` | 维护期公开样本下载 |

这使模型负责判断，脚本负责可确定检查，减少“Agent 说通过但没有机械验证”的问题。[脚本文档](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/scripts/README.md)

### 3.5 三类竞赛包

`competitions/{cumcm,mcm,diangong}` 分别保存规则入口、题型路由、rubric overlay、反模式、论文骨架与模板素材。规则文件带核对日期，并明确要求 Stage 0、8、9 重新打开当届官方来源，仓库基线不得覆盖最新官方规则。[竞赛包](https://github.com/handsomeZR-netizen/mathmodel-skill/tree/d3941e14d8693fb4a79948e59afff3098734127e/competitions)

## 4. 建模与求解能力评价

### 4.1 做得好的部分

1. **选型不是只查模型表。** Stage 3 要求候选适配证据、否决理由、时间预算、可验证增益和最小可执行 demo；模型命名必须与公式、代码、消融证据一致。[Stage 3](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/stage_03_model_selection.md)
2. **求解有基本科学门禁。** Stage 5 包含求解状态、数量级、边界情形、同约束基线、随机种子、结果落盘和跨子问接口检查。[Stage 5](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/stage_05_subproblem_loop.md)
3. **验证按风险选择方法。** Stage 6 不强制所有题目做同一种“灵敏度分析”，而是区分参数不确定性、数据漂移、随机性、模型结构和离散边界，再匹配 OAT、LHS、滚动验证、多种子、压力测试等方法。[Stage 6](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/stage_06_robustness.md)
4. **支持不依赖数学规划求解器的算法。** 仓库虽然示例偏 `cvxpy`，但 Stage 3/6 的协议也覆盖统计、预测、仿真、启发式、图算法和数值算法；`model_catalog.md` 列出优化、预测、评价、分类、仿真、图论、统计、动力系统等模型族。[模型目录](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/model_catalog.md)

### 4.2 能力边界

- 代码起步模板只有 5 类：classification、evaluation、optimization、prediction、simulation；它不是完整算法库。
- 主流程偏“按竞赛阶段推进”，不擅长用户只想快速询问某个算法、某类模型或单段代码的场景。
- 对机理建模、ODE/PDE、几何/运动学、网络科学、博弈等领域，目录层有介绍，但可运行模板和专项 playbook 深度有限。
- Stage 5 的正文示例默认 `cvxpy + GLPK_MI`，容易让读者误以为“求解”等同于数学规划；实际使用时仍需根据算法类型条件化执行。

## 5. 工程质量与维护状态

### 5.1 正向证据

- 有自动化 CI，固定提交的 Python 3.10 和 3.12 两个任务均成功，包含编译、66 项测试、三类竞赛 preflight。[CI 运行](https://github.com/handsomeZR-netizen/mathmodel-skill/actions/runs/29925385834)
- 本地在 Windows/Python 3.13 上重新执行 `compileall` 成功；设置 `PYTHONUTF8=1` 后，三个 `doctor.py --skip-tools --json` 均通过。
- 测试覆盖评分边界、原子状态写入、模板 section marker、占位符 fail-closed、AI 披露、patch 安全和 code starter 的若干科研正确性边界。[CI 配置](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/.github/workflows/ci.yml)
- 运行时代码未发现 `eval`、`exec` 或 `shell=True`；网络访问集中在维护期下载脚本。渲染脚本通过参数数组调用 Pandoc/TeX，风险相对可控。
- 仓库声明第三方边界，未把论文 PDF 和外部模板二进制直接打包进仓库。[第三方声明](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/THIRD_PARTY_NOTICES.md)

### 5.2 风险与不足

> [!warning] Windows 编码兼容
> `doctor.py` 的人类可读输出使用 `✓/✗/↳`。在本机默认 GBK 控制台直接运行时触发 `UnicodeEncodeError`；使用 `--json` 且启用 UTF-8 后通过。这说明仓库官方 CI 成功不等于 Windows 默认终端无摩擦。[doctor.py](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/scripts/doctor.py)

> [!warning] 本地测试不能“零依赖即全过”
> 当前环境缺少 `seaborn` 与 `unidiff`，完整单元测试出现依赖错误；同时 Python 3.13/Windows 子进程输出还出现 UTF-8 解码问题。仓库 CI 按配置安装测试依赖后是绿色，因此这更准确地表明：README 所说的“核心流程无需完整科学栈”成立，但“完整回归测试”仍必须安装 CI 的测试依赖并处理 Windows 编码。

其他注意点：

1. **发布标记略滞后。** 主文件和 plugin manifest 已写 v6.1，但 Releases/Tags 页面当前只有 v6.0.0 与 v5.0.0；使用者若按“最新 Release”安装，拿不到仓库当前 v6.1 主线。[Releases](https://github.com/handsomeZR-netizen/mathmodel-skill/releases)
2. **样本统计不可当质量阈值。** CUMCM 的 91 份来源中只有 59 份进入文本统计，32 份图像型 PDF 未进入；自动计数也可能漏记或重复。仓库已明确声明这是观察锚点而非获奖预测，但二次集成时必须保留该限制。[样本报告](https://github.com/handsomeZR-netizen/mathmodel-skill/blob/d3941e14d8693fb4a79948e59afff3098734127e/references/papers/_DOWNLOAD_REPORT.md)
3. **赛制经验仍需审慎。** 电工杯 Issue #2 曾指出“工程类评审标准”的表述不够严谨；维护者已承认工程实施建议属于经验增强而非官方强制章节。当前版本已强化“官方规则优先”，但经验材料仍应标成启发式。[Issue #2](https://github.com/handsomeZR-netizen/mathmodel-skill/issues/2)
4. **维护节奏较集中。** 仓库目前只有 10 个提交，开发主要集中在 2026-05 与 2026-07；因此它有工程化基础，但长期维护稳定性仍需继续观察。[提交历史](https://github.com/handsomeZR-netizen/mathmodel-skill/commits/main/)
5. **测试不覆盖真实竞赛端到端效果。** CI 主要证明结构、脚本和若干模板行为正确，并不证明 10 阶段在真实 72–96 小时协作中一定优于更轻流程，也不证明模型质量或奖项结果。

## 6. 与本地 `math-modeling-solver-copy` 对比

本地对象：[[.agents/skills/math-modeling-solver-copy/skill.md]]。

| 维度 | `mathmodel-skill` | 本地 `math-modeling-solver-copy` | 判断 |
|---|---|---|---|
| 核心定位 | 长周期竞赛流程与状态治理 | 解题知识、模型选择、算法实现、结果分析 | 互补 |
| 主流程 | 10 阶段，强门禁、可回退 | 从理解、检索、设计、实现到论文衔接 | 本地更细于“技术解题”，外部更强于“项目控制” |
| 持久状态 | `decision_log.json` schema 3.1 | 主要依赖文件产物与阶段规则 | 外部明显更强 |
| 局部修复 | per-Qi、section patch、L2 回检 | 有阶段回退，但缺统一机器状态 | 外部更强 |
| 模型知识 | 一个通用 model catalog | 95+ 决策矩阵、8 类 cookbook、12 类 playbook | 本地更强 |
| 可运行模板 | 5 个 Python starter | 22 个 Python + 7 个 MATLAB 模板 | 本地更强 |
| 数据审计/基线 | schema 扫描、基线 sanity check | 数据结构指纹、泄漏检查、模型阶梯、升级证据 | 本地更系统 |
| 条件化算法/求解器工程 | 有求解状态与基本预算检查 | 明确区分通用算法、随机算法、数值算法、优化求解器 | 本地更符合“并非所有算法都用求解器” |
| 验证 | 风险驱动稳健性 + 跨阶段回检 | 分类型最低检验集 + Claim–Evidence + 结果门禁 | 两者互补 |
| 论文生成 | 自带三赛制 TeX/PDF 装配 | 只桥接到 `math-modeling-paper` | 取决于是否希望职责分离 |
| 合规/AI 披露 | 强，且有确定性脚本 | AI 治理有原则，缺自动生成披露 | 外部更强 |
| 触发边界 | 仅三类明确竞赛 | 覆盖更广的建模解题咨询 | 本地更灵活 |

### 关键判断

不建议用该仓库直接替换本地副本。外部仓库的强项恰好是本地副本尚弱的“状态、合规、局部回修、确定性验收”；而本地副本的强项是“模型知识深度、数据审计、条件化算法工程、代码模板”。整仓覆盖会丢掉后者，也会与现有 `math-modeling-paper` 的职责发生重叠。

## 7. 建议吸收的内容

### P0：优先吸收

1. **最小持久状态**：为每个项目保存 `current_stage`、题目/子问、关键假设、模型选择、结果路径、验证状态、未决问题和回退记录。
2. **阶段退出门禁**：每阶段必须有输入、产物、验证证据和退出条件，不能只凭“已写完”进入下一步。
3. **per-Qi 局部回修**：允许只修失败子问，并显式记录对下游结果、图表和论文的影响。
4. **确定性 preflight**：新增 doctor/contract 检查，验证目录、依赖、结果路径、图表、论文交接和关键占位符。
5. **规则与 AI 台账**：规则带 `last_verified` 和官方链接；AI 使用从过程开始记录，不到赛末才回忆。

### P1：选择性吸收

1. **fast / standard / championship 模式**，但根据剩余时间与风险动态裁剪，避免固定流程压垮短问答。
2. **L1/L2/L3 反馈分层**，只保留可改变决策的检查，不机械追求多轮评分。
3. **competition pack**：把 CUMCM/MCM/电工杯的规则、模板和提交要求与通用解题逻辑分离。
4. **fail-closed 论文装配**：缺章节、占位符、匿名或披露项未处理时不标记可提交。

### 不建议直接搬运

- CUMCM 经验分位、优秀论文短语库和反模式数量；除非同时搬运 provenance、局限说明与更新机制。
- 全套十阶段固定时长；应由题面、团队能力和 deadline 重新分配。
- 统一的数值评分作为绝对质量结论；评分只能用于发现薄弱点，不能替代事实核验。
- 把论文渲染全部塞回 solver；本地已有 `math-modeling-paper`，更适合保留“solver 输出结构化交接包 → paper 负责正式写作与排版”的边界。

## 8. 推荐整合架构

```text
math-modeling-solver-copy
├─ 主流程路由（保留现有灵活入口）
├─ solver-state.json / state.md（吸收最小状态机）
├─ problem → data audit → baseline ladder
├─ model → conditional algorithm/solver engineering
├─ validation → result gate
├─ per-Qi status + targeted rollback
├─ competition packs（只保存规则/提交差异）
└─ paper handoff package
      ↓
math-modeling-paper
└─ 正式论文写作、渲染、版式与提交检查
```

### 推荐落地顺序

1. 先定义最小状态 schema，不复制外部仓库的全部字段。
2. 给现有各阶段补 `entry / artifacts / checks / exit / rollback` 五项契约。
3. 把本地已有的 `data-audit-and-baseline.md`、`algorithm-and-solver-engineering.md`、`validation-planning.md` 映射到状态字段。
4. 新增 `doctor.py`，先检查路径、依赖、状态和关键产物，不急于实现评分系统。
5. 最后再评估 per-Qi 聚合、competition pack 和 AI 披露生成器。

## 9. 最终评价

| 项目 | 评价 |
|---|---|
| 流程设计 | 强 |
| 状态与可恢复性 | 很强 |
| 合规与交付 | 很强 |
| 模型知识深度 | 中等 |
| 可运行算法模板广度 | 中等偏弱 |
| 自动化测试 | 强，但偏结构/脚本层 |
| Windows 开箱体验 | 中等，存在编码摩擦 |
| 作为本地副本替代品 | 不推荐 |
| 作为架构参考与治理增强源 | 推荐 |

**一句话结论：借它的“骨架和神经系统”，保留本地副本的“模型大脑和算法肌肉”。**