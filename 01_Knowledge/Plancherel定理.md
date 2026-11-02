---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理]]'
legacy_topics:
- Fourier变换
- L^2空间
- 酉算子
- 等距延拓
- Parseval恒等式
exam: 考试重点
tags:
- 傅里叶变换
- Parseval恒等式
- Plancherel定理
- L2空间
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
about:
- '[[01_Knowledge/Fourier变换]]'
legacy_topic_links:
- '[[01_Knowledge/Fourier变换]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Plancherel定理

## 一句话

Plancherel 定理将 Fourier 变换从速降函数空间 $S(\mathbb{R}^n)$ 唯一等距延拓到整个 $L^2(\mathbb{R}^n)$ 上，使 Fourier 变换成为 $L^2$ 上的酉算子，且保持 $L^2$ 范数不变——即 Parseval 恒等式在 $L^2$ 中的推广。

## 严格定义

设 $\mathcal{F}$ 为 Schwartz 速降函数空间 $S(\mathbb{R}^n)$ 上的 Fourier 变换：

$$
\mathcal{F}f(t) = \hat{f}(t) := \int_{\mathbb{R}^n} f(x) e^{-2\pi i x \cdot t} \, dx \quad (f \in S(\mathbb{R}^n))
$$

则 $\mathcal{F}: S(\mathbb{R}^n) \to S(\mathbb{R}^n)$ 可**唯一延拓**为 $L^2(\mathbb{R}^n)$ 上的酉算子（仍记为 $\mathcal{F}$），满足

$$
\boxed{\|\hat{f}\|_2 = \|f\|_2 \quad (\forall f \in L^2(\mathbb{R}^n))}
$$

即

$$
\int_{\mathbb{R}^n} |\hat{f}(t)|^2 \, dt = \int_{\mathbb{R}^n} |f(x)|^2 \, dx
$$

> [!important] 延拓过程三步走
> 1. **在 $S$ 上定义**：先验证 $\mathcal{F}: S \to S$ 是良定的，且 $\mathcal{F}^4 = I$（四次作用回到自身）
> 2. **在 $S$ 上证明等距性**：利用 Fourier 反转公式证明 $\langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle$，从而 $\|\hat{f}\|_2 = \|f\|_2$
> 3. **稠密延拓**：$S(\mathbb{R}^n)$ 在 $L^2(\mathbb{R}^n)$ 中稠密，故等距算子 $\mathcal{F}$ 可唯一延拓到 $L^2$ 上，保内积且为双射（酉算子）

## 推导：等距延拓

> [!proof]- 推导
> **第一步：$S$ 上 Fourier 变换的封闭性**。对 $f \in S(\mathbb{R}^n)$，$\hat{f}$ 仍属于 $S$（速降函数 Fourier 变换后仍速降），且 $\mathcal{F}^4 f(x) = f(-x)$，从而 $\mathcal{F}^4 = I$。由此知 $\mathcal{F}$ 在 $S$ 上为双射。
>
> **第二步：证明 $S$ 上的等距性**。利用 Fourier 反转公式 $\check{g}(x) = \hat{g}(-x)$，对任意 $f, g \in S$：
> $$
> \langle \hat{f}, \hat{g} \rangle = \int \hat{f}(t) \overline{\hat{g}(t)} \, dt = \int f(x) \overline{g(x)} \, dx = \langle f, g \rangle
> $$
> （利用 Fubini 定理交换积分次序及 $\hat{\overline{g}}(-x) = \overline{g(x)}$）。取 $f = g$ 即得 $\|\hat{f}\|_2 = \|f\|_2$。
>
> **第三步：稠密延拓**。$S(\mathbb{R}^n) \subset L^2(\mathbb{R}^n)$ 稠密。对任意 $f \in L^2$，取 $f_n \in S$ 使 $\|f_n - f\|_2 \to 0$。由等距性 $\|\hat{f}_n - \hat{f}_m\|_2 = \|f_n - f_m\|_2 \to 0$，故 $\{\hat{f}_n\}$ 为 $L^2$ 中的 Cauchy 列，由 $L^2$ 完备性存在极限 $\hat{f} \in L^2$。该极限与逼近序列的选取无关，因此 $\mathcal{F}$ 在 $L^2$ 上良定，且等距性由极限保持。$\square$

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 等距性（Plancherel 恒等式） | $\|\hat{f}\|_2 = \|f\|_2$，即 Fourier 变换保 $L^2$ 范数 |
| 保内积 | $\langle \hat{f}, \hat{g} \rangle = \langle f, g \rangle$（极化恒等式推出） |
| 酉性 | $\mathcal{F}: L^2 \to L^2$ 为双射，且 $\mathcal{F}^* = \mathcal{F}^{-1} = \mathcal{F}^3$ |
| 延拓方式 | $f \in L^1 \cap L^2$ 时 $\hat{f}$ 仍由积分公式给出；纯 $L^2$ 中需通过 $S$ 中逼近序列的 $L^2$ 极限定义 |
| 与 $L^1$ 对比 | $L^1$ 中 $\hat{f} \in C_0$（Riemann-Lebesgue），不一定回 $L^1$；$L^2$ 中 $\hat{f} \in L^2$（自反） |
| Gauss 函数特征 | $G(x) = e^{-\pi|x|^2}$ 满足 $\hat{G} = G$，是 Fourier 变换在 $L^2$ 中的唯一（归一化后）特征函数 |

## 典型例题

> **题目**：证明 Gauss 函数 $G(x) = e^{-\pi |x|^2}$（$x \in \mathbb{R}^n$）是 Fourier 变换的特征函数，即 $\hat{G}(t) = G(t)$。

> [!example]- 解答
> **方法一（一维，利用微分方程）**：$G(x) = e^{-\pi x^2}$ 满足 $G'(x) = -2\pi x \, G(x)$。Fourier 变换后：
> $$
> \widehat{G'}(t) = 2\pi i t \, \hat{G}(t)
> $$
> 左边由分部积分：$\widehat{G'}(t) = \int G'(x) e^{-2\pi i x t} dx = 2\pi i t \int G(x) e^{-2\pi i x t} dx = 2\pi i t \, \hat{G}(t)$。
> 另一方面，$\widehat{-2\pi x G(x)}(t) = -2\pi \cdot \frac{i}{2\pi} \hat{G}'(t) = -i \hat{G}'(t)$。由原方程得 $2\pi i t \, \hat{G}(t) = -i \hat{G}'(t)$，即 $\hat{G}'(t) = -2\pi t \, \hat{G}(t)$。
> 解得 $\hat{G}(t) = \hat{G}(0) e^{-\pi t^2}$。而 $\hat{G}(0) = \int_{\mathbb{R}} e^{-\pi x^2} dx = 1$（Gauss 积分），故 $\hat{G}(t) = e^{-\pi t^2} = G(t)$。
>
> **方法二（高维，分离变量）**：$G(x) = \prod_{j=1}^{n} e^{-\pi x_j^2}$，一维结果相乘得 $\hat{G}(t) = \prod_{j=1}^{n} e^{-\pi t_j^2} = G(t)$。
>
> **点评**：Gauss 函数是唯一在 Fourier 变换下不变的 $L^2$ 函数（至多差常因子），这一性质在热核方程、不确定性原理和调和分析中至关重要。

## 易错点

> [!warning] 易错点 1：$L^2$ 中积分公式不一定逐点成立
> 对一般 $f \in L^2(\mathbb{R}^n)$（不在 $L^1$ 中），$\hat{f}(t) = \int f(x) e^{-2\pi i x t} dx$ 这个积分可能发散。$\hat{f}$ 需理解为 $S$ 中逼近序列 $\hat{f}_n$ 的 $L^2$ 极限，而非逐点积分。

> [!warning] 易错点 2：$L^1$ 与 $L^2$ 的 Fourier 变换不可混淆
> $f \in L^1$ 时 $\hat{f}$ 由积分定义且 $\hat{f} \in C_0$，但 $\hat{f}$ 不一定属于 $L^1$；$f \in L^2$ 时 $\hat{f}$ 由延拓定义且 $\hat{f} \in L^2$，但 $\hat{f}$ 不一定属于 $C_0$（虽然实际上 $L^2$ 的 Fourier 变换也属于 $C_0$，这是 Riemann-Lebesgue 引理的推广）。

> [!warning] 易错点 3：Plancherel 定理 $\neq$ Parseval 恒等式
> Parseval 恒等式通常指正交基展开的系数平方和等于范数平方（如 Fourier 级数）。Plancherel 定理是 Parseval 在 $L^2(\mathbb{R}^n)$ 上的连续推广——将离散求和换为连续积分。教学中两者常混用，但严格区分：Parseval 是级数形式，Plancherel 是积分形式。

## 相关概念

- [[01_Knowledge/Fourier变换]]
- [[01_Knowledge/L^p空间]]
- [[01_Knowledge/Lebesgue积分]]
- [[01_Knowledge/卷积]]
- [[01_Knowledge/Riesz定理]]

## 习题

- [[03_Sources/Courses/归档/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — Plancherel 定理相关习题（L^p 空间完备性与 Fourier 变换）
