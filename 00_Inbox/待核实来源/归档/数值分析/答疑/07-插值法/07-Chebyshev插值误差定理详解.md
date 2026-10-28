---
subject:
- 数值分析
chapter: 7
source_context:
- file: 07-插值法-知识梳理.md
  line: 195
  text: 2^{1-n}T_n(x) 是所有 n 次首一多项式中 ∞-范数最小的那个
- file: 07-插值法-知识梳理.md
  line: 200
  text: ω(x) = ∏(x-x_i) = 2^{-n} T_{n+1}(x)
- file: 07-插值法-知识梳理.md
  line: 201
  text: '|f(x)-P_n(x)| ≤ (1/(2^n (n+1)!)) max|f^{(n+1)}|'
related_notes:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理]]'
tags:
- Chebyshev插值
- 插值误差
aliases:
- 第7章 答疑 — Chebyshev插值误差定理详解
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- Chebyshev多项式
- Chebyshev插值
- 插值误差
- 首一多项式定理
- minimax性质
source: []
status: not done
legacy_type: review
legacy_schema_version: 2
migration_reason: Missing traceable source in legacy source note
---

# 第7章 答疑 — Chebyshev 插值误差定理详解

---

## 一、为什么 $\omega(x) = 2^{-n} T_{n+1}(x)$？

> 问题：$\omega(x)=\prod_{i=0}^n(x-x_i) = 2^{-n}\,T_{n+1}(x)$ —— 这怎么来的？
>
> 来源：[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理|07-知识梳理]] 第 200 行

### 核心

**$\omega$ 和 $T_{n+1}$ 的根完全相同 → 它们成比例 → 对齐最高次项系数即得比例常数。**

**第一步——同根**：插值节点 $x_0,\ldots,x_n$ 选为 $T_{n+1}$ 的 $n+1$ 个零点。所以 $\omega$ 和 $T_{n+1}$ 是**次数相同、根完全相同**的两个多项式 → $\omega(x) = c \cdot T_{n+1}(x)$。

**第二步——对齐系数**：$\omega$ 是 $n+1$ 个 $(x-x_i)$ 的乘积，$x^{n+1}$ 系数为 $1$（首一）；$T_{n+1}$ 的 $x^{n+1}$ 系数为 $2^n$（递推 $T_{n+1}=2xT_n-T_{n-1}$，每次乘 $2x$）。

$$c \cdot 2^n = 1 \quad\Rightarrow\quad c = 2^{-n}$$

因此 $\omega(x) = 2^{-n} T_{n+1}(x)$，且 $\max\vert\omega(x)\vert = 2^{-n} \cdot \max\vert T_{n+1}\vert = 1/2^n$。

> **全局误差 = $(f^{(n+1)}$的界$)/(2^n (n+1)!)$——分母的 $2^n$ 是压制 Runge 的关键。**

---

## 二、首一多项式定理（minimax 性质）

> 问题：$2^{1-n}T_n(x)$ 是所有 $n$ 次首一多项式中 $\infty$-范数最小的那个 —— 怎么看出来的？
>
> 来源：[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理|07-知识梳理]] 第 195 行

### 核心：反证法 + 符号交替

设 $q(x) = 2^{1-n}T_n(x)$。已知 $T_n$ 在 $n+1$ 个点上轮流触及 $\pm 1$：

$$T_n\!\left(\cos\frac{k\pi}{n}\right) = (-1)^k, \quad k=0,1,\ldots,n$$

所以 $q$ 在这 $n+1$ 个点 $x_k = \cos\frac{k\pi}{n}$ 上轮流取 $\pm 2^{1-n}$：

$$+2^{1-n} \xrightarrow{x_1} -2^{1-n} \xrightarrow{x_2} +2^{1-n} \xrightarrow{x_3} -2^{1-n} \cdots$$

假设存在另一个 $n$ 次首一多项式 $p$ 满足 $\max\vert p\vert < 2^{1-n}$。

**为什么 $\max\vert p\vert < 2^{1-n}$ 意味着 $p(x_k)$ 在 $\pm 2^{1-n}$ 之内？**

范数取的是整个区间上的 sup：$\max\vert p\vert = \sup_{x\in[-1,1]}\vert p(x)\vert$。既然这个上界严格小于 $2^{1-n}$，那么**任何单个点**的 $\vert p(x_k)\vert$ 当然也小于 $2^{1-n}$（单点值 ≤ 全局 max）。

考虑差值 $r(x) = q(x) - p(x)$。在每个 $x_k$：
- $q(x_k) = +2^{1-n}$，而 $p(x_k) < 2^{1-n}$ → $r(x_k) > 0$
- $q(x_{k+1}) = -2^{1-n}$，而 $p(x_{k+1}) > -2^{1-n}$ → $r(x_{k+1}) < 0$

$r$ 的正负号跟着 $q$ 一起交替 → 相邻 $x_k$ 之间必过零 → **$r$ 至少有 $n$ 个根**。

但 $q$ 和 $p$ 都是 $n$ 次首一多项式 → $r = q-p$ 最高 $n-1$ 次 → 最多 $n-1$ 个根（除非恒为零）。

**矛盾。** 所以不存在振幅更小的首一多项式。

> **一句话**：$T_n$ 的等振荡性就是它最小化 max-norm 的"基因"——交替符号压出 $n$ 个零点，差值次数吃不下 → 证明其最优。

---

## 三、误差定理汇总

### 标准区间 $[-1,1]$

节点取 $T_{n+1}$ 的根 $x_k = \cos\frac{(2k+1)\pi}{2(n+1)}$：

$$\vert f(x)-P_n(x)\vert \leq \frac{1}{2^n (n+1)!}\;\max_{c\in[-1,1]}\vert f^{(n+1)}(c)\vert$$

### 任意区间 $[a,b]$

通过线性映射 $x \mapsto \frac{2x-(b+a)}{b-a}$ 变换节点：

$$x_k = \frac{b-a}{2}\cos\frac{(2k+1)\pi}{2(n+1)} + \frac{b+a}{2}$$

$$\vert f(x)-P_n(x)\vert \leq \frac{\left(\frac{b-a}{2}\right)^{n+1}}{2^n (n+1)!}\;\max_{c\in[a,b]}\vert f^{(n+1)}(c)\vert$$

> **对比 Runge**：均匀节点下 $\max\vert\omega\vert$ 随 $n$ 指数增长；Chebyshev 节点下分母有 $2^n$ 压制 → 只要 $f^{(n+1)}$ 增长不太快，误差随 $n\to\infty$ 趋于零。

---

## 相关链接

- [[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理|07-插值法 知识梳理]]
- [[03_Sources/Courses/归档/数值分析/课件/MD/07-插值法|07-插值法 课件笔记]]
- [[03_Sources/Courses/归档/数值分析/数值分析-知识图谱|数值分析 知识图谱]]
