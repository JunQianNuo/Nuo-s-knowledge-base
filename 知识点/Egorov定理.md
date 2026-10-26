---
title: Egorov定理
type: 知识点
source:
- 课程/实变函数/知识点解析梳理/03-可测函数-知识梳理.md
topics:
- Egorov定理
- 几乎处处收敛
- 几乎一致收敛
- 有限测度
- 测度上连续性
- 降列
exam: 考试重点
status: 已整理
---

# Egorov定理

## 一句话

在有限测度集上，几乎处处收敛可加强为「去掉一个任意小测度的子集后一致收敛」——测度论用集合运算把逐点收敛的不一致部分"切除"掉。

## 严格定义

设 $m(E) < \infty$，$f_n, f$ 在 $E$ 上几乎处处有限且可测。若

$$
f_n \xrightarrow{\text{a.e.}} f \quad \text{on } E,
$$

则 $f_n \xrightarrow{\text{a.u.}} f$，即：

$$
\boxed{\forall \delta > 0,\; \exists\, \text{可测子集 } E_\delta \subset E,\; m(E \setminus E_\delta) < \delta,\; \text{且在 } E_\delta \text{ 上 } f_n \rightrightarrows f}
$$

> [!important] 关键条件
> - **有限测度** $m(E) < \infty$ 是必要条件——无穷测度时结论不成立（见反例）。
> - 可测子集 $E_\delta$ 依赖于 $\delta$：$\delta$ 越小，需要切除的"坏点"集合越大（但仍然小于 $\delta$）。
> - $f_n \rightrightarrows f$ 仅在 $E_\delta$ 上成立，不是在原集合 $E$ 上。

## 推导：降列与测度上连续性

> [!proof]- 推导
> **核心思路**：用集合论语言刻画「不一致收敛」的坏点集，证其为降列后用测度上连续性控制其测度。
>
> **Step 1** — 刻画收敛点集。
> $$
> \{f_k \to f\} = \bigcap_{i=1}^{\infty} \bigcup_{J=1}^{\infty} \bigcap_{j=J}^{\infty} E\!\left(|f_j - f| < \frac{1}{i}\right)
> $$
> 记 $A_J^{(i)} = \bigcup_{j \ge J} E\!\left(|f_j - f| \ge \frac{1}{i}\right)$。固定 $i$，$A_J^{(i)}$ 关于 $J$ 是**降列**：$A_1^{(i)} \supset A_2^{(i)} \supset \cdots$。
>
> **Step 2** — 利用 a.e. 收敛。$\{f_k \not\to f\}$ 为零测集，故 $\bigcap_{J=1}^\infty A_J^{(i)}$ 均包含于零测集内，从而也为零测集。由测度的**上连续性**（降列且 $m(A_1^{(i)}) \le m(E) < \infty$）：
> $$
> \lim_{J \to \infty} m\!\left(A_J^{(i)}\right) = m\!\left(\bigcap_{J} A_J^{(i)}\right) = 0
> $$
>
> **Step 3** — 构造 $\delta$-切除。对 $\delta > 0$ 及每个 $i$，因 $m(A_J^{(i)}) \to 0$，可取 $J_i$ 使 $m(A_{J_i}^{(i)}) < \delta / 2^i$。令
> $$
> A = \bigcup_{i=1}^{\infty} A_{J_i}^{(i)},\qquad m(A) \le \sum_{i=1}^{\infty} \frac{\delta}{2^i} = \delta
> $$
>
> **Step 4** — 验证一致收敛。取 $E_\delta = E \setminus A$。任取 $x \in E_\delta$ 及 $\varepsilon > 0$，取 $i > 1/\varepsilon$。因 $x \notin A_{J_i}^{(i)}$，对所有 $j \ge J_i$ 有 $|f_j(x) - f(x)| < 1/i < \varepsilon$。$\square$
>
> **方法论**：这是分析中"截断法"的测度论版本——降列 + 测度上连续性构造出可控制的坏点集，余下集合上自动得到一致收敛。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 方向 | $\text{a.e.} \Rightarrow \text{a.u.}$（有限测度下）；反向 $\text{a.u.} \Rightarrow \text{a.e.}$ 无条件成立 |
| 有限测度的必要性 | $E = (0, \infty)$ 上 $f_n = \chi_{(0,n)} \xrightarrow{\text{a.e.}} 1$，但任意去掉有限测度子集后无穷远处仍不收敛 |
| 与依测度收敛的关系 | 有限测度下：$\text{a.e.}$ $\xRightarrow{\text{Egorov}}$ $\text{a.u.}$ $\Rightarrow$ $\text{依测度}$ |
| 核心工具 | 降列 + 测度上连续性（$m(A_J) \searrow 0$） |
| 与 Lusin 定理的类比 | Lusin：可测函数近似连续（切除小测度集）；Egorov：收敛近似一致（切除小测度集的"反极限"） |

## 典型例题

> **题目**：设 $m(E) < \infty$，$f_n, f$ 在 $E$ 上可测且 a.e. 有限。用 Egorov 定理证明：若 $f_n \xrightarrow{\text{a.e.}} f$，则 $f_n$ 依测度收敛于 $f$。

> [!example]- 解答
> **分析**：依测度收敛要求 $\forall \varepsilon > 0$，$m(E(|f_n - f| \ge \varepsilon)) \to 0$。Egorov 给出切除小测度集后一致收敛——一致收敛足够强，能直接推出依测度收敛。
>
> **证明**：任取 $\varepsilon > 0, \delta > 0$。由 Egorov 定理，存在 $E_\delta \subset E$，$m(E \setminus E_\delta) < \delta$，且在 $E_\delta$ 上 $f_n \rightrightarrows f$。
>
> 由一致收敛，$\exists N$ 使 $n \ge N$ 时 $\sup_{x \in E_\delta} |f_n(x) - f(x)| < \varepsilon$。于是
> $$
> E(|f_n - f| \ge \varepsilon) \subset E \setminus E_\delta
> $$
> 故 $m(E(|f_n - f| \ge \varepsilon)) \le m(E \setminus E_\delta) < \delta$。由 $\delta$ 任意性得证。$\square$
>
> **评论**：这是 Egorov 定理最典型的应用——把"几乎处处"升级为"几乎一致"，再降级为"依测度"。关键步骤是一致收敛子集上 $|f_n - f| \ge \varepsilon$ 为空集（$n$ 充分大后），因此坏点只能落在被切除的小测度集上。

## 易错点

> [!warning] 易错点 1：无限测度下的反例
> $f_n = \chi_{(0,n)}$ 在 $(0, \infty)$ 上几乎处处收敛于 $1$，但**不几乎一致收敛**。原因：任意测度有限的子集 $E_\delta$ 外总有 $x > \sup E_\delta$ 使 $|f_n(x) - 1| = 1$ 对无穷多个 $n$ 成立。

> [!warning] 易错点 2：一致收敛仅在子集上
> Egorov 定理结论是"存在子集 $E_\delta$ 使一致收敛成立"，不是在原集合 $E$ 上一致收敛。误读为 $f_n \rightrightarrows f$ on $E$ 是常见错误。

> [!warning] 易错点 3：$\delta$ 与 $J_i$ 的依赖关系
> 证明中取 $J_i$ 使 $m(A_{J_i}^{(i)}) < \delta / 2^i$。$\delta$ 越小，每个 $J_i$ 需要越大（收敛"慢"的方向需要更靠后才达标），$E_\delta$ 也越小——但总能找到。

## 相关概念

- [[几乎一致收敛]]
- [[几乎处处收敛]]
- [[一致收敛]]
- [[依测度收敛]]
- [[概念/实变函数/可测函数]]
- [[概念/实变函数/零测集]]
- [[知识点/实变函数/依测度收敛]]
- [[知识点/实变函数/Riesz定理]]
- [[知识点/实变函数/Lusin定理]]

## 习题

- [[课程/实变函数/习题库/03-可测函数/README|第3章习题库]]
- [[课程/实变函数/习题库/03-可测函数/习题3.21-Egorov定理-习题|习题3.21]] — Egorov 定理完整证明
- [[课程/实变函数/习题库/03-可测函数/习题3.16-几乎一致收敛的判定-习题|习题3.16]] — 几乎一致收敛的判定与反例
- [[课程/实变函数/习题库/03-可测函数/习题3.20-有限测度集上几乎处处收敛蕴含依测度收敛-习题|习题3.20]] — Egorov 推依测度收敛
