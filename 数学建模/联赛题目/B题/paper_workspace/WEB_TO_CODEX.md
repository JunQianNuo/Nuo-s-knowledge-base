# WEB_TO_CODEX — 正式论文 sections 合并执行单（2026-08-16）

> Handoff type: Web → Codex  
> Project: 2026线上集训 Practice01 / 策联杯 B题  
> Source Commit: `871e3c1c25ef6d47af4ef1caa3f62bb5d84c906b`  
> Execution mode: **只执行文件合并、LaTeX 工程与 QA；不要重新分析或改写论文内容**  
> PAPER_SYNC_POINT: 本任务暂不创建，待全文编译与人工确认后再处理。

## 1. 当前冻结状态

`.paper_workspace/DECISIONS.md` 已同步到 Stage B 160 人正式认证口径：

- Q1：`\widehat T_{1,\Omega}=14759 min`，validated feasible；
- Q2：`\widehat T_{2,\Omega}=18963 min`，validated feasible；
- Q3 Stage A：`\widehat T_{0,\Omega}=35114 min`，作为 `B_0=35114 min`；
- Q3 Stage B：160/160，incumbent = best bound = 160，gap=0，`OPTIMAL`，允许写 `N_{\mathrm{temp},\Omega}^{*}=160`，仅限当前有限 TimedColumn 池与固定 `B_0`；
- Q3 Stage C：`T_air=34033`、`T_pax=246808`、fuel=`273629.0`、flights=`204`、utilization=`47.77%`；C1—C4 FEASIBLE，C5 UNKNOWN，final source = C4 incumbent，`full_certified=false`。

历史 143/160 与17人瓶颈只保留为历史实验，不得回写当前正文。

## 2. 本地论文目录合同

当前正式目录统一为：

- 已确认 MD 输入：`E:\数模策联杯\论文书写\md文件分析`
- 正式 LaTeX 权威目录：`E:\数模策联杯\论文书写\正式论文`
- 里程碑/历史快照：`E:\数模策联杯\论文书写\版本记录`

不要再使用旧的“正式论文记录”目录名。

当前正式主文件：

`E:\数模策联杯\论文书写\正式论文\main.tex`

正式正文目录：

`E:\数模策联杯\论文书写\正式论文\sections`

图片目录：

`E:\数模策联杯\论文书写\正式论文\figures`

## 3. 最新 TeX 文件包

Web 已完成最新版 MD→TeX 转换，并已实际联合 XeLaTeX 试编译通过。

最新包名：

`正式论文_sections_最新版Tex_2026-08-16.zip`

包内 `sections/` 共13个文件：

- `00_abstract.tex` — 保持 Codex 原版
- `01_problem_restatement.tex` — **最新版，替换**
- `02_problem_analysis.tex` — 保持 Codex 原版
- `03_assumptions.tex` — 保持 Codex 原版
- `04_notation.tex` — 保持 Codex 原版
- `05_data_foundation.tex` — **最新版，替换**
- `06_q1.tex` — **最新版，替换**
- `07_q2.tex` — **最新版，替换**
- `08_q3.tex` — **最新版，替换**
- `09_validation.tex` — **最新版，替换**
- `10_evaluation.tex` — **最新版，新增/替换**
- `11_references.tex` — 保持 Codex 原版
- `12_appendix.tex` — 保持 Codex 原版

如果本地已经存在用户刚放入/解压的这个 ZIP，直接使用，不要重新生成 TeX；如果已经直接覆盖到 `sections/`，只做内容/时间戳确认后继续。

## 4. 图片引用合同

最新版 TeX 已统一使用 `figures/*.png`，不要改回 SVG，也不要重做图片。

当前正式图片文件包括：

- `figures/05_Fig1_三问统一建模框架与目标层级.png`
- `figures/05_Fig2_运输网络与三问数据规模概览 (1).png`
- `figures/06_Fig4_求解过程及飞机使用时间变化.png`
- `figures/06_Fig5_五级目标的求解状态与相对差距.png`
- `figures/06_Fig6_逐航段载客量与距离加权座位利用率.png`
- `figures/07_Fig7_Q2联合运输与独立OD运输基线对比.png`
- `figures/07_Fig8_人员在途时间的结构性权衡.png`
- `figures/07_Fig9_五级词典序求解状态与计算代价.png`
- `figures/07_Fig10_半开区间动态容量与座位即时复用.png`
- `figures/08_Fig11_Q3三阶段递进.png`
- `figures/08_Fig12_Q3七天机队排班甘特图.png`
- `figures/08_Fig13_Q3临时任务全接纳与兼容性画像.png`
- `figures/09_Fig14_Q3时间列密度敏感性.png`

本轮**不要统一或重命名图号**；用户将在图片齐全后集中处理编号与命名。

## 5. Required Operations — 直接执行，不要展开分析

### Step 1 — 同步与备份

1. 在仓库根目录执行 `git status`，确认无不明本地冲突。
2. `git fetch` / `git pull --ff-only`，确保至少包含 `871e3c1c25ef6d47af4ef1caa3f62bb5d84c906b`。
3. 在覆盖正式论文前，将当前 `E:\数模策联杯\论文书写\正式论文` 做一次里程碑快照到：
   `E:\数模策联杯\论文书写\版本记录\2026-08-16_sections最新版合并前\`
   或等价 ZIP 快照。

### Step 2 — 覆盖 sections

直接把最新版包中的 `sections/*.tex` 覆盖/合并到：

`E:\数模策联杯\论文书写\正式论文\sections\`

**不要重新生成正文，不要润色，不要调整公式，不要改表格内容。**

### Step 3 — main.tex 只做工程检查

检查 `main.tex` 是否按顺序输入：

`00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12`

若 `10_evaluation.tex` 尚未 `\input`，只补这一条；其他排版宏、页边距、标题格式不主动修改。

### Step 4 — 编译

在 `E:\数模策联杯\论文书写\正式论文` 下使用现有 XeLaTeX 工程方式完整编译，至少执行两遍 XeLaTeX（如当前工程有既定 latexmk 命令则沿用）。

不得因为编译警告而自行重写正文；只允许修复明确的 LaTeX 工程错误，例如：

- 文件路径错误；
- `\input` 缺失；
- 图片文件名/转义导致的找不到文件；
- 明确的环境未闭合；
- 明确的宏包/命令依赖问题。

### Step 5 — QA

只检查并记录：

1. `main.pdf` 是否成功生成；
2. 总页数；
3. 05—09 大致页码范围与总页数；
4. 是否存在 Missing file / Undefined control sequence / Fatal error；
5. 是否存在明显 Overfull hbox（尤其模型大括号与表格）；
6. 13张最新版图片是否全部被正确载入；
7. 06/07/08 的 `min / s.t. / 大括号` 模型是否正常显示；
8. 08 式(8-1)～(8-9)是否连续；
9. 10“模型评价与改进”是否出现在参考文献之前。

不要在本轮做图号统一、图片重绘、内容重写或参考文献扩充。

### Step 6 — 回传

更新 `.paper_workspace/CODEX_TO_WEB.md`，只写精简结果：

- 合并是否成功；
- 实际使用的 Source Commit；
- `main.tex` 是否修改以及修改了什么；
- 编译命令；
- PDF总页数；
- 05—09页码范围；
- warnings/errors 摘要；
- `main.tex` / `main.pdf` SHA256；
- 新快照路径与 SHA256（若为 ZIP）；
- 尚需人工处理事项。

不需要再次解释模型原理。

## 6. Do Not

- 不重新阅读全部模型材料后重写正文；
- 不修改已确认的01、05—10文字内容；
- 不把Stage B从160改回143；
- 不把Q1/Q2/Stage A FEASIBLE结果写成OPTIMAL；
- 不把Q2算法改称经典ALNS；
- 不重命名图片或统一图号；
- 不重绘05图片；
- 不新增Q2敏感性实验；
- 不调整用户已冻结的页面与标题层级规范；
- 不创建PAPER_SYNC_POINT；
- 不提交与本任务无关的代码、模型或结果文件修改。

## 7. Acceptance Criteria

本任务完成当且仅当：

1. 最新 `sections/` 已进入正式论文目录；
2. `main.tex` 正确包含 `10_evaluation.tex`；
3. XeLaTeX 全文编译成功并生成 `main.pdf`；
4. 所有最新图片成功加载；
5. 无 Fatal LaTeX 错误；
6. 05—09页面范围已记录，可据此判断是否满足20页预算；
7. `.paper_workspace/CODEX_TO_WEB.md` 已回传精简执行结果。
