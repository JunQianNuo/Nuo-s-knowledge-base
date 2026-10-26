---
title: Minkowski不等式
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - Minkowski不等式
  - L^p三角不等式
  - 范数公理
exam: 考试重点
---

# Minkowski不等式

## 一句话

Minkowski 不等式就是 $L^p$ 范数的三角不等式——"和的 $L^p$ 范数不超过各自 $L^p$ 范数之和"。它与 Hölder 不等式共同确立 $\|\cdot\|_p$ 是真正的范数，使 $L^p$ 成为赋范向量空间。

## 严格定义

设 $1 \leq p \leq \infty$，$f, g \in L^p(E)$。则

$$\|f + g\|_p \leq \|f\|_p + \|g\|_p.$$

写成积分形式（$1 \leq p < \infty$）：

$$\left(\int_E |f(x) + g(x)|^p dx\right)^{1/p} \leq \left(\int_E |f(x)|^p dx\right)^{1/p} + \left(\int_E |g(x)|^p dx\right)^{1/p}.$$

**$L^p$ 范数的三条公理**（定理 4.1.4）：
1. **齐次性**：$\|\alpha f\|_p = |\alpha| \|f\|_p$（$\forall \alpha \in \mathbb{R}$）；
2. **三角不等式**：$\|f+g\|_p \leq \|f\|_p + \|g\|_p$（即 Minkowski 不等式）；
3. **正定性**：$\|f\|_p \geq 0$，且 $\|f\|_p = 0 \iff f = 0$ a.e. $[E]$。

> [!important] 核心要点
> - **证明核心**：将 $\|f+g\|_p^p$ 拆为 $\int |f+g|^{p-1}|f+g| \leq \int |f+g|^{p-1}|f| + \int |f+g|^{p-1}|g|$，对每一项用 Hölder 不等式（利用 $(p-1)q = p$），合并即得 $\|f+g\|_p^p \leq \|f+g\|_p^{p-1}(\|f\|_p + \|g\|_p)$，约去公因子证毕。
> - **$p=1$ 时是平凡的**：$\|f+g\|_1 \leq \|f\|_1 + \|g\|_1$ 来自 $|f+g| \leq |f| + |g|$ 逐点积分。
> - **等号成立条件**（$1 < p < \infty$）：存在非负常数 $c$ 使 $f = c g$ a.e.（即两个函数成比例）。

## 由来与作用

- **历史起源**：由 Hermann Minkowski（约 1900）在研究凸体几何和数论中发现。他将欧几里得空间中的三角不等式推广到函数空间，为后来的 Banach 空间理论奠定了基础。
- **解决的问题**：没有三角不等式，$L^p$ 只是一个带半度量的集合，无法做收敛分析和逼近理论。Minkowski 不等式确立了 $L^p$ 的赋范结构。
- **在实变函数中的角色**：与 Hölder 不等式组成不可分割的"不等式对"——Hölder 给 Minkowski 提供证明技术，Minkowski 给 $L^p$ 提供赋范结构。两者共同使 $L^p$ 成为 Banach 空间。
- **关键性质**：Minkowski 不等式对 $1 \leq p \leq \infty$ 均成立；$p<1$ 时不成立（此时 $\|\cdot\|_p$ 不是范数）。

## 相关概念

- [[L^p空间]] — Minkowski 不等式使 $L^p$ 成为赋范空间。
- [[概念/实变函数/Hölder不等式]] — Minkowski 不等式的证明依赖 Hölder 不等式。
- [[概念/实变函数/卷积]] — 卷积的 Young 不等式是 Minkowski 与 Hölder 的综合推广。
