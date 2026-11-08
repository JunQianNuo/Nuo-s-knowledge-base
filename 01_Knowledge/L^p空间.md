---
schema_version: 2
type: concept
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理]]'
- '[[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.10-L^p收敛蕴含依测度收敛（定理4.1.9）-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.11-L^p控制收敛定理（定理4.1.10）-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.8-有限测度集上L^p空间的包含关系-习题]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-09-22-第3节-数学分析课程讲座]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-10-09-第5节-泛函分析空间完备性讲座]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-10-20-第7节-泛函分析课程授课]]'
legacy_topics:
- L^p空间
- L^p范数
- 本性有界
- Riesz-Fisher定理
- 完备性
exam: 考试重点
tags:
- Lp空间
- Riesz-Fisher定理
- 完备性
- Lp范数
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-泛函分析]]'
prerequisites:
- '[[01_Knowledge/Lebesgue积分]]'
time: '2026-08-31T11:44:20+08:00'
aliases: []
legacy_status: 已整理
---

# L^p空间

## 一句话

$L^p$ 空间是所有 $p$ 次幂 Lebesgue 可积（可测且 $|f|^p$ 积分有限）的函数构成的赋范向量空间——它是泛函分析中最基本的 Banach 空间之一，$p=2$ 时是 Hilbert 空间，在 PDE、概率论和信号处理中有核心地位。

## 严格定义

设 $E$ 是 $\mathbb{R}^n$ 中的可测集。

**(1) 对 $1 \leq p < \infty$**：定义

$$\|f\|_p = \left(\int_E |f(x)|^p \, dx\right)^{1/p},$$

$L^p(E) = \{f \in \mathfrak{M}(E) \mid \|f\|_p < \infty\}$。

**(2) $L^\infty(E)$**：若存在 $M > 0$ 使 $|f(x)| \leq M$ a.e. $[E]$，则称 $f$ **本性有界**。定义

$$\|f\|_\infty = \inf\{M > 0 \mid |f(x)| \leq M \text{ a.e. } [E]\},$$

$L^\infty(E) = \{f \in \mathfrak{M}(E) \mid \|f\|_\infty < \infty\}$。

**注意**：$L^p$ 空间中的元素是**函数的等价类**——两个 a.e. 相等的函数视为同一元素。因此 $\|\cdot\|_p$ 满足范数正定性（$\|f\|_p = 0 \iff f = 0$ a.e.）。

**共轭指数**：$p, q \in [1, \infty]$ 满足 $p^{-1} + q^{-1} = 1$，如 $(p,q) = (2,2), (1,\infty), (3,3/2)$。

> [!important] 核心要点
> - **$L^p$ 是 Banach 空间**（Riesz-Fisher 定理）：$L^p$ 对 $L^p$ 范数完备——每个 $L^p$ Cauchy 列在 $L^p$ 中收敛。
> - **$L^2$ 是 Hilbert 空间**：内积 $\langle f,g\rangle = \int_E f(x)g(x)\,dx$ 导出 $L^2$ 范数。
> - **有限测度集上的包含关系**：若 $m(E) < \infty$，则 $p_1 < p_2 \Rightarrow L^{p_2}(E) \subset L^{p_1}(E)$（高指数空间更"小"）。反例：$E = (0, \infty)$ 时包含关系不成立。
> - **稠密性**：$C_c^\infty(\mathbb{R}^n)$ 在 $L^p(\mathbb{R}^n)$ 中稠密（$1 \leq p < \infty$），$L^p$ 是可分的。

## 由来与作用

- **历史起源**：$L^p$ 空间由 F. Riesz（1910）系统研究，他将 Lebesgue 积分与泛函分析结合，证明了 $L^p$ 的完备性。Banach（1920s）将其纳入赋范空间的公理化框架。
- **解决的问题**：$L^p$ 空间统一了"可积性"和"收敛性"——$L^p$ 收敛比一致收敛弱，比 a.e. 收敛强，且具有完备性（a.e. 收敛没有完备性）。
- **在实变函数中的角色**：是课程的终点——从集合论到测度到积分到 $L^p$ 空间，构成了完整的知识链。在泛函分析、PDE、概率论中，$L^p$ 是最基础的函数空间。
- **关键性质**：$L^p$ 收敛 $\Rightarrow$ 依测度收敛 $\Rightarrow$ 存在 a.e. 收敛子列；Hölder 不等式和 Minkowski 不等式使 $L^p$ 成为赋范空间。

## 相关概念

- [[01_Knowledge/Lebesgue积分]] — $L^1(E) = L(E)$ 即 Lebesgue 可积函数空间。
- [[01_Knowledge/几乎处处]] — $L^p$ 中的元素是 a.e. 等价类。
- [[01_Knowledge/Hölder不等式]] — $L^p$ 与 $L^q$ 函数乘积的积分不等式。
- [[01_Knowledge/Minkowski不等式]] — $L^p$ 范数的三角不等式。
- [[01_Knowledge/卷积]] — 卷积是 $L^p$ 空间上的重要运算，Young 不等式刻画其有界性。

## 概率中的同一结构

把底层测度换成概率测度 $P$，$E|X|^p<\infty$ 就表示随机变量 $X$ 属于 $L^p(P)$（$1\le p<\infty$）。[[01_Knowledge/数学期望]] 与 [[03_Sources/Reviews/概率论/专题复习/方差、矩与切比雪夫概率界|二阶矩和方差]] 因而可以放在同一可积性框架下理解。


## 本轮习题补充与边界核对

Lp→依测度（1≤p<∞）由
$$m(|f_n-f|>ε)\le ε^{-p}\|f_n-f\|_p^p$$
直接得到。L∞收敛更强：可数个本性上界例外取并后，在同一满测集一致收敛。

Lp控制收敛：若 $|f_n|\le g∈Lp$ 且a.e.或依测度趋f，则先由a.e.收敛或Riesz子列得 $|f|\le g$ a.e.。$h_n=|f_n-f|^p$ 趋0（依测度时 $\{h_n>ε\}=\{|f_n-f|>ε^{1/p}\}$），并被 $2^pg^p∈L1$ 控制；用DCT相应版本得 $\|f_n-f\|_p\to0$。

有限测度0<m(E)<∞时，p1<p2有 $\|f\|_{p1}\le m(E)^{1/p1-1/p2}\|f\|_{p2}$，由对 $|f|^{p1}\cdot1$ 用Hölder得到；p2=∞直接估计。对f∈L∞，上界 $\|f\|_p\le\|f\|_∞m(E)^{1/p}$；对任意0<M'<\|f\|∞，正测集A={|f|>M'}给下界 $\|f\|_p\ge M'm(A)^{1/p}$。令p→∞再M'↑\|f\|∞，得Lp范数极限为本性上确界。零测E时各范数均为0，单独处理。

原文“Lp收敛比a.e.强”应订正：Lp收敛保证依测度收敛和某子列a.e.收敛，不保证原列a.e.收敛；有限区间的打字机指标函数即Lp趋0却处处不收敛。


## 本次来源核对与适用范围

本次课堂按几乎处处相等取函数等价类；有限测度下p<q有Lᑫ⊂Lᵖ及$\|f\|_p\le\mu(\Omega)^{1/p-1/q}\|f\|_q$。原文“Lᵖ收敛比a.e.收敛强”不能理解为原序列必逐点几乎处处收敛：一般只能保证存在a.e.收敛子列。复L²内积须写$\int f\overline g\,d\mu$；实值情形才可省共轭。一般测度空间的可分性需要额外可测结构条件，不能仅凭p有限概括所有空间。
