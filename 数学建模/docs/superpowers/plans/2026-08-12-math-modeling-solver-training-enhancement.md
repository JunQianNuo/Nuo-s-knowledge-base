# Math Modeling Solver Training Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将三次数模培训中的数据审计、基准模型、条件化算法检查、求解器诊断、复现、团队协同和 AI 核验规则落实到 `math-modeling-solver-copy`，且不改变原版 Skill。

**Architecture:** 保留现有阶段0—8与全部文件路径，在主 `skill.md` 增加三种工作模式和阶段门禁；新增三个单一职责参考文件，并对七个既有参考文件做局部增强。使用一个独立的 Python 契约测试脚本验证静态结构、关键行为规则、相对链接和原版隔离。

**Tech Stack:** Markdown、YAML frontmatter、Python 3 标准库、Skill `quick_validate.py`

## Global Constraints

- 只修改 `.agents/skills/math-modeling-solver-copy/` 及本计划所需测试文件。
- 不修改 `.agents/skills/math-modeling-solver/` 原版。
- 不移动或重命名既有 Cookbook、Playbook 和代码模板。
- 不批量修改 29 个代码模板和 12 个 Playbook。
- 阶段3采用“通用算法契约 → 算法专项检查 → 求解器专项检查”；非求解器算法不得虚构求解状态或最优间隙。
- 局部协助模式不得强制创建完整竞赛目录。

---

### Task 1: 建立失败的规格契约测试

**Files:**
- Create: `.agents/skills/math-modeling-solver-copy/tests/test_training_enhancement_contract.py`
- Read: `docs/superpowers/specs/2026-08-12-math-modeling-solver-training-enhancement-design.md`

**Interfaces:**
- Consumes: 副本 Skill 目录与原版 Skill 目录。
- Produces: 一个返回非零或零状态的标准库测试程序，覆盖新增文件、模式、阶段3分支、阶段增强、相对引用和原版隔离。

- [ ] **Step 1: 写入契约测试**

测试必须检查：三个新增参考文件存在；主 Skill 包含三种模式、数据审计、基准模型和三级阶段3；七个既有参考文件包含各自新增契约；B1—B14行为要求具有对应文字规则；原版文件与实施前基线清单一致。

- [ ] **Step 2: 运行测试确认 RED**

Run: `python .agents/skills/math-modeling-solver-copy/tests/test_training_enhancement_contract.py`

Expected: FAIL，至少指出三个新增参考文件不存在，以及主 Skill 缺少三种工作模式。

### Task 2: 新增培训方法参考文件

**Files:**
- Create: `.agents/skills/math-modeling-solver-copy/references/data-audit-and-baseline.md`
- Create: `.agents/skills/math-modeling-solver-copy/references/algorithm-and-solver-engineering.md`
- Create: `.agents/skills/math-modeling-solver-copy/references/competition-execution.md`
- Test: `.agents/skills/math-modeling-solver-copy/tests/test_training_enhancement_contract.py`

**Interfaces:**
- Consumes: 设计规格第3、5、6、7、9节。
- Produces: 数据审计与模型阶梯模板；通用/专项/求解器三级算法契约；团队、复现及AI治理模板。

- [ ] **Step 1: 编写三个参考文件**

内容使用可直接执行的表格、门禁和输出模板；不复制现有 Cookbook 的算法原理。

- [ ] **Step 2: 运行契约测试**

Expected: 新文件存在性通过，主流程及既有参考文件相关检查仍失败。

### Task 3: 增强主 Skill 路由和阶段门禁

**Files:**
- Modify: `.agents/skills/math-modeling-solver-copy/skill.md`
- Test: `.agents/skills/math-modeling-solver-copy/tests/test_training_enhancement_contract.py`

**Interfaces:**
- Consumes: Task 2 的三个参考文件路径。
- Produces: 三种模式路由、阶段0—8增强入口、三级阶段3规则、横向协同和AI治理规则。

- [ ] **Step 1: 添加工作模式路由**

将全流程、局部协助、方案审查模式放在阶段入口之前，并明确局部协助不创建完整目录。

- [ ] **Step 2: 修改阶段0—8**

在相应阶段引用 Task 2 文件，添加数据审计、模型阶梯、条件化算法检查、分类型验证、图表证据、复现、求解诊断和 Claim—Evidence 交接。

- [ ] **Step 3: 更新阶段间规则和参考资源**

明确不适用项、失败回退、AI核验和三个新参考入口。

- [ ] **Step 4: 运行契约测试**

Expected: 主 Skill 合约通过；既有参考文件增强检查仍失败。

### Task 4: 增强问题拆解、模型选择与优化手册

**Files:**
- Modify: `.agents/skills/math-modeling-solver-copy/references/problem-decomposition.md`
- Modify: `.agents/skills/math-modeling-solver-copy/references/model-selection-matrix.md`
- Modify: `.agents/skills/math-modeling-solver-copy/references/cookbook-optimization.md`

**Interfaces:**
- Consumes: 数据审计、模型阶梯和求解器专项规则。
- Produces: 数据结构指纹检查、基准/升级裁决、求解状态与不可行诊断说明。

- [ ] **Step 1: 增强问题拆解**

添加观测单位、独立性、分组/重复测量、时间/空间、截尾、类别不平衡、单位和泄漏检查。

- [ ] **Step 2: 增强模型选择矩阵**

添加常识基线、数学基准、升级证据、复杂度代价和回退裁决。

- [ ] **Step 3: 增强优化 Cookbook**

添加求解状态、incumbent/bound/gap、不可行/无界诊断、松弛和结果解释；明确启发式算法不能虚构 gap。

- [ ] **Step 4: 运行契约测试**

Expected: 本任务对应检查通过。

### Task 5: 增强检验、图表、结果与论文桥接

**Files:**
- Modify: `.agents/skills/math-modeling-solver-copy/references/validation-planning.md`
- Modify: `.agents/skills/math-modeling-solver-copy/references/figure-planning.md`
- Modify: `.agents/skills/math-modeling-solver-copy/references/result-analysis.md`
- Modify: `.agents/skills/math-modeling-solver-copy/references/paper-bridge.md`

**Interfaces:**
- Consumes: 阶段1—3产出的数据审计、模型阶梯和算法契约。
- Produces: 分类型最低检验、扩展 Figure Contract、算法条件化结果报告与 Claim—Evidence 表。

- [ ] **Step 1: 增强检验规划**

加入回归、分类、聚类、优化、机理和评价模型的最低检验集合，以及不确定性表达。

- [ ] **Step 2: 增强图表规划**

加入数据处理前后、基准/升级、残差/区间、收敛/gap、现实方案等图表类型。

- [ ] **Step 3: 增强结果分析**

区分所有模型、随机算法、数学规划求解器、不可行模型和预测—决策模型的报告字段。

- [ ] **Step 4: 增强论文桥接**

加入 Claim—Evidence 表及变量、参数、公式、代码、结果、图表一致性门禁。

- [ ] **Step 5: 运行契约测试**

Expected: 全部契约检查通过。

### Task 6: 完整验证与清理

**Files:**
- Verify: `.agents/skills/math-modeling-solver-copy/`
- Verify unchanged: `.agents/skills/math-modeling-solver/`

**Interfaces:**
- Consumes: 所有实现文件。
- Produces: 可复核的测试、Skill 校验、链接检查与原版隔离证据。

- [ ] **Step 1: 运行契约测试**

Run: `python .agents/skills/math-modeling-solver-copy/tests/test_training_enhancement_contract.py`

Expected: PASS，0 failures。

- [ ] **Step 2: 运行 Skill 校验**

Run: `$env:PYTHONUTF8=1; python C:\Users\Nuo\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\math-modeling-solver-copy`

Expected: `Skill is valid!`

- [ ] **Step 3: 检查相对引用和占位符**

运行测试脚本中的链接及占位符检查，确认无失效相对引用和未完成字段。

- [ ] **Step 4: 检查原版隔离**

比较实施前记录的原版文件路径、大小和 SHA-256，必须完全一致。

- [ ] **Step 5: 检查变更范围**

确认未修改 Playbook、代码模板、LICENSE 和原版目录；输出最终文件清单。
