---
title: 考题 - Fourier变换的核心性质
subject: 实变函数
chapter: 5
section: 重积分与L^p空间
source: 2023-RA-28.md
status: 已校对
type: 考题
topics:
  - Fourier变换
  - 卷积定理
  - Plancherel定理
knowledge_tags:
  - Plancherel定理
method_tags:
  - 
tags:
- 傅里叶变换
- 卷积定理
- Plancherel定理
---

# 考题：Fourier 变换的核心性质

## 题目

(1) 写出 $f \in L^1(\mathbb{R}^n)$ 的 Fourier 变换定义，并证明卷积定理：$(f * g)^\wedge = \hat{f} \cdot \hat{g}$。

(2) 写出 Gauss 函数 $G(x) = e^{-|x|^2/2}$（$x \in \mathbb{R}$）的 Fourier 变换，并验证 $\hat{G} = G$。

(3) 陈述 Plancherel 定理，并说明其与 Parseval 等式的关系。

---

> [!hint]- 点击展开提示
> (1) 卷积定理的证明关键是 Fubini 定理交换积分次序。(2) 利用 $G'(x) = -xG(x)$ 的 Fourier 变换关系。(3) Plancherel 是 Parseval 的 $L^2$ 推广。

> [!solution]- 点击展开详细解析
> **解**：
>
> **(1)** Fourier 变换定义（$L^1$ 中）：
> $$\hat{f}(t) = (2\pi)^{-n/2} \int_{\mathbb{R}^n} f(x) e^{-i t \cdot x} \, dx$$
>
> 卷积定理证明：
> $$\begin{aligned}
> (f*g)^\wedge(t) &= (2\pi)^{-n/2} \int_{\mathbb{R}^n} (f*g)(x) e^{-i t \cdot x} \, dx \\
> &= (2\pi)^{-n/2} \int_{\mathbb{R}^n} \left(\int_{\mathbb{R}^n} f(x-y)g(y) \, dy\right) e^{-i t \cdot x} \, dx \\
> &= (2\pi)^{-n/2} \int_{\mathbb{R}^n} g(y) e^{-i t \cdot y} \left(\int_{\mathbb{R}^n} f(x-y) e^{-i t \cdot (x-y)} \, dx\right) dy \quad \text{(Fubini)} \\
> &= (2\pi)^{-n/2} \int_{\mathbb{R}^n} g(y) e^{-i t \cdot y} \, dy \cdot \int_{\mathbb{R}^n} f(u) e^{-i t \cdot u} \, du \quad (u=x-y) \\
> &= \hat{f}(t) \cdot \hat{g}(t)
> \end{aligned}$$
>
> **(2)** Gauss 函数 $G(x) = e^{-x^2/2}$。由 $G'(x) = -xG(x)$ 得：
> $$\widehat{G'}(t) = it \hat{G}(t) = -\widehat{xG}(t) = i\hat{G}'(t)$$
> 故 $\hat{G}'(t) = -t \hat{G}(t)$。解微分方程得 $\hat{G}(t) = C e^{-t^2/2}$。
> 由 $\hat{G}(0) = (2\pi)^{-1/2} \int e^{-x^2/2}dx = 1$ 得 $C = 1$。故 $\hat{G} = G$。
>
> **(3)** Plancherel 定理：Fourier 变换可唯一延拓为 $L^2(\mathbb{R}^n)$ 上的酉算子，
> $$\|\hat{f}\|_2 = \|f\|_2 \quad (\forall f \in L^2)$$
> 即 $\int |\hat{f}|^2 = \int |f|^2$。这与 Parseval 等式 $\|f\|_2^2 = \sum |\langle f, \varphi_k \rangle|^2$ 本质一致——两者都表达"能量守恒"。Parseval 是离散版本（相对于可数正交基），Plancherel 是连续版本（相对于 Fourier 变换的"连续基" $e^{i t \cdot x}$）。
>
> **答案**：(1) 见上；(2) $\hat{G}=G$；(3) 见上。
>
> **点评**：这三问覆盖了 Fourier 变换理论的核心链条——定义 → 卷积定理 → 特征函数（Gauss）→ Plancherel。考试中卷积定理的证明（Fubini 交换）和 Gauss 的证明（微分方程法）都是经典题型。
