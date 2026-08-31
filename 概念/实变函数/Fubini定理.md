---
title: Fubini定理
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - Fubini定理
  - Tonelli定理
  - 重积分
  - 累次积分
  - 乘积测度
exam: 仅了解
---

# Fubini定理

## 一句话

Fubini 定理是连接重积分与累次积分的核心定理——在 Lebesgue 可积条件下，多重积分可化为逐次积分且积分次序可交换。

## 严格定义

设 $f(x,y) \in L^1(\mathbb{R}^{p+q})$（关于 Lebesgue 乘积测度可积），则：

(1) **截面可积性**：对 a.e. $x \in \mathbb{R}^p$，$f(x,\cdot) \in L^1(\mathbb{R}^q)$；对称地，对 a.e. $y \in \mathbb{R}^q$，$f(\cdot,y) \in L^1(\mathbb{R}^p)$。

(2) **部分积分的可积性**：函数 $x \mapsto \int_{\mathbb{R}^q} f(x,y)\,dy$ 属于 $L^1(\mathbb{R}^p)$，且函数 $y \mapsto \int_{\mathbb{R}^p} f(x,y)\,dx$ 属于 $L^1(\mathbb{R}^q)$。

(3) **积分次序可交换**：

$$\iint_{\mathbb{R}^{p+q}} f(x,y)\,dxdy = \int_{\mathbb{R}^p} \left[ \int_{\mathbb{R}^q} f(x,y)\,dy \right] dx = \int_{\mathbb{R}^q} \left[ \int_{\mathbb{R}^p} f(x,y)\,dx \right] dy$$

> [!important] 核心要点
> - **前提是 $f \in L^1$**（绝对可积）——没有这个前提，累次积分可能不等。这与黎曼积分中"两个累次积分相等 $\Rightarrow$ 重积分存在"的逻辑相反：在 Lebesgue 框架下是先有重积分可积，再推出累次积分相等。
> - **Tonelli 定理是配套工具**：对**非负可测**函数 $f \geq 0$，无需先验证 $f \in L^1$，累次积分自动相等（允许 $+\infty$）。标准工作流：先用 Tonelli 验证 $|f|$ 的重积分有限 $\Rightarrow$ $f \in L^1$，再用 Fubini 得到 $f$ 本身的等式。
> - **典型反例**：$f(x,y) = \frac{x^2-y^2}{(x^2+y^2)^2}$ 在 $(0,1)^2$ 上，两个累次积分分别得 $\pi/4$ 和 $-\pi/4$，不等。根因是 $f \notin L^1$（重积分发散），不满足 Fubini 的前提。

## 由来与作用

- **历史起源**：Guido Fubini（1879–1943，意大利数学家）于 1907 年发表该定理的原型。在 Lebesgue 积分论建立后，该定理被自然地推广到乘积测度空间，成为实分析积分理论的支柱成果之一。Leonida Tonelli 于 1909 年补充了非负可测函数版本。
- **解决的问题**：将高维积分分解为低维逐次积分——这是计算重积分的根本手段。在黎曼框架下，交换积分次序需要相当强的条件（如一致收敛）；Fubini 定理将其统一到简洁的 $L^1$ 条件。
- **在实变函数中的角色**：
  - 是重积分理论的**核心定理**——连接了一维积分与多维积分。
  - 与 Tonelli 定理构成**判定—计算二段式**：Tonelli 定可积性，Fubini 得等式。
  - 是 $L^p$ 空间中大量证明的技术基础（Young 不等式、卷积不等式、Minkowski 积分不等式等均依赖交换积分次序）。
- **关键性质与注意事项**：
  - $f \in L^1$ 是充分条件，也是必要条件（若两个累次积分存在且相等，能否推出 $f \in L^1$？不总是——反例即上述 $(0,1)^2$ 例子，两个累次积分存在但不等，故 $f \notin L^1$）。
  - 乘积测度的完备化是定理成立的技术前提。
  - Fubini 定理对 $\sigma$-有限的测度空间普遍成立，不限于 Lebesgue 测度。

## 相关概念

- [[概念/实变函数/Lebesgue积分]] — Fubini 定理是 Lebesgue 积分论中重积分的核心定理。
- [[概念/实变函数/可测函数]] — Fubini 定理要求被积函数在乘积空间上可测。
- [[概念/实变函数/L^p空间]] — $L^1$ 可积性是 Fubini 定理的核心前提；定理是 $L^p$ 中交换积分操作的技术基础。
- [[概念/实变函数/几乎处处]] — 截面可积性仅对 a.e. $x$ 和 a.e. $y$ 成立。
- [[概念/实变函数/卷积]] — 卷积不等式的证明中大量使用 Fubini/Tonelli 交换积分次序。
- [[知识点/实变函数/Young不等式(卷积版)]] — 证明中通过 Tonelli 定理交换积分次序，再经 Hölder 不等式完成估计。
- [[知识点/实变函数/Plancherel定理]] — 证明 $\|\hat{f}\|_2 = \|f\|_2$ 时利用 Fubini 定理交换累次积分。
