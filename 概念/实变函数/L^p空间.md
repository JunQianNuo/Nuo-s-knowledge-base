---
title: L^p空间
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - L^p空间
  - L^p范数
  - 本性有界
  - Riesz-Fisher定理
  - 完备性
exam: 考试重点
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

- [[概念/实变函数/Lebesgue积分]] — $L^1(E) = L(E)$ 即 Lebesgue 可积函数空间。
- [[概念/实变函数/几乎处处]] — $L^p$ 中的元素是 a.e. 等价类。
- [[概念/实变函数/Hölder不等式]] — $L^p$ 与 $L^q$ 函数乘积的积分不等式。
- [[概念/实变函数/Minkowski不等式]] — $L^p$ 范数的三角不等式。
- [[概念/实变函数/卷积]] — 卷积是 $L^p$ 空间上的重要运算，Young 不等式刻画其有界性。
