---
title: 正交基与Fourier展开
type: 知识点
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - 标准正交基
  - Fourier展开
  - Parseval等式
  - Bessel不等式
  - L^2空间
  - Hilbert空间
exam: 考试重点
---

# 正交基与Fourier展开

## 一句话

$L^2$ 空间中，标准正交基将任意函数展开为基函数的无穷线性组合（Fourier 展开），展开系数由内积给出，Parseval 等式保证范数守恒——这是 Hilbert 空间几何在函数空间中的完整体现。

## 严格定义

设 $L^2(E)$ 为 $E \subset \mathbb{R}^n$ 上平方可积函数的 Hilbert 空间，内积定义为

$$
\langle f, g \rangle = \int_E f(x)g(x)\,dm(x)
$$

**标准正交系** $\{\varphi_k\}_{k=1}^\infty \subset L^2(E)$ 满足

$$
\langle \varphi_i, \varphi_j \rangle = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}
$$

**定理 4.2.14（标准正交基的四个等价条件）**：$\{\varphi_k\}$ 是标准正交基当且仅当以下任一条成立：

$$
\boxed{\|\varphi_k\|_2 = 1,\; \langle\varphi_i,\varphi_j\rangle = 0\;(i \neq j),\;\text{且 }\{\varphi_k\}\text{ 是极大标准正交系}}
$$

> [!important] 等价判定（四条择一即可）
>
> 1. **极大性**：$\{\varphi_k\}$ 是标准正交基（无法再添加非零函数使扩充后仍为标准正交系）
> 2. **稠密性**：$\operatorname{span}\{\varphi_k\}$ 在 $L^2(E)$ 中稠密，即有限线性组合 $\sum_{k=1}^{N} c_k \varphi_k$ 可逼近任意 $f \in L^2$
> 3. **完全性**：若 $f \in L^2(E)$ 满足 $\langle f, \varphi_k \rangle = 0$（$\forall k$），则 $f = 0$ a.e.
> 4. **Parseval 等式**：$\forall f \in L^2(E)$，有
>    $$
>    \boxed{\|f\|_2^2 = \sum_{k=1}^\infty |\langle f, \varphi_k \rangle|^2}
>    $$

当 $\{\varphi_k\}$ 为标准正交基时，$f$ 的 **Fourier 展开**为

$$
f = \sum_{k=1}^\infty \langle f, \varphi_k \rangle \, \varphi_k
$$

该级数在 $L^2$ 范数下收敛（即 $\|f - \sum_{k=1}^{N} \langle f, \varphi_k \rangle \varphi_k\|_2 \to 0$，$N \to \infty$）。

> [!important] Bessel 不等式（对任意标准正交系成立）
> 对任意标准正交系 $\{\varphi_k\}$（不要求是完全的）和任意 $f \in L^2(E)$，
> $$
> \sum_{k=1}^\infty |\langle f, \varphi_k \rangle|^2 \leq \|f\|_2^2
> $$
> **等号成立当且仅当 $\{\varphi_k\}$ 是完全的**（即 Parseval 等式成立）。

## 推导：Parseval 等式 $\Leftrightarrow$ 完全性

> [!proof]- 推导
> **思路**：利用 $L^2$ 中的正交投影性质——任意 $f$ 到 $\operatorname{span}\{\varphi_1,\ldots,\varphi_n\}$ 的最佳逼近由 Fourier 系数给出。
>
> **第一步：正交投影与最佳逼近**。令 $S_N = \sum_{k=1}^{N} \langle f, \varphi_k \rangle \varphi_k$。由正交性，
> $$
> \langle f - S_N, \varphi_k \rangle = 0 \quad (k = 1,\ldots,N)
> $$
> 因此 $S_N$ 是 $f$ 在 $\operatorname{span}\{\varphi_1,\ldots,\varphi_N\}$ 上的正交投影。由勾股定理，
> $$
> \|f\|_2^2 = \|S_N\|_2^2 + \|f - S_N\|_2^2
> = \sum_{k=1}^{N} |\langle f, \varphi_k \rangle|^2 + \|f - S_N\|_2^2
> $$
>
> **第二步：Bessel 不等式**。由 $\|f - S_N\|_2^2 \geq 0$ 得 $\sum_{k=1}^{N} |\langle f, \varphi_k \rangle|^2 \leq \|f\|_2^2$。令 $N \to \infty$ 即得 Bessel 不等式。
>
> **第三步：Parseval $\Leftrightarrow$ 完全性**。
> - ($\Rightarrow$) 若 Parseval 成立，则 $\|f - S_N\|_2^2 = \|f\|_2^2 - \sum_{k=1}^{N}|\langle f,\varphi_k\rangle|^2 \to 0$。故 $\operatorname{span}\{\varphi_k\}$ 稠密，$\{\varphi_k\}$ 为基。
> - ($\Leftarrow$) 若 $\{\varphi_k\}$ 完全（稠密），由最佳逼近性质，$\|f - S_N\|_2 \to \inf_{g \in \operatorname{span}\{\varphi_k\}} \|f - g\|_2 = 0$，代入勾股关系即得 Parseval。
>
> **核心技巧**：$L^2$ 的 Hilbert 结构将线性无关性化为正交性，将逼近问题化为投影问题——这是泛函分析标准范式的经典案例。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 标准正交系 | $\langle\varphi_i,\varphi_j\rangle = \delta_{ij}$，范数均为 1 且两两正交 |
| Bessel 不等式 | $\sum |\langle f,\varphi_k\rangle|^2 \leq \|f\|_2^2$，对**任意**标准正交系成立 |
| Parseval 等式 | $\sum |\langle f,\varphi_k\rangle|^2 = \|f\|_2^2$，$\{\varphi_k\}$ 为**完全**标准正交系时取等 |
| 四个等价条件 | 极大正交系 $\Leftrightarrow$ 稠密生成 $\Leftrightarrow$ 完全性 $\Leftrightarrow$ Parseval（证其一即知全部） |
| Fourier 收敛 | 级数在 $L^2$ 范数下收敛；**不保证逐点收敛** |
| 三角基 | $L^2[-\pi,\pi]$ 上 $\{1/\sqrt{2\pi},\cos(nx)/\sqrt{\pi},\sin(nx)/\sqrt{\pi}\}$ → 经典 Fourier 级数 |
| Legendre 基 | $L^2[-1,1]$ 上 $\{1,x,x^2,\ldots\}$ 的 Gram-Schmidt 正交化结果 |
| Hermite 基 | $L^2(\mathbb{R})$ 上 Hermite 函数 $\{h_n\}$，量子谐振子本征函数 |

## 典型例题

> **题目**：证明 $L^2[-\pi,\pi]$ 中三角函数系 $\{1/\sqrt{2\pi},\;\cos(nx)/\sqrt{\pi},\;\sin(nx)/\sqrt{\pi}\}_{n=1}^\infty$ 是完全标准正交系，并写出 Fourier 级数的 Parseval 等式。

> [!example]- 解答
> **（1）验证标准正交性**：
> - $\frac{1}{\pi}\int_{-\pi}^{\pi} \cos(mx)\cos(nx)\,dx = \delta_{mn}$（$m,n \geq 1$）
> - $\frac{1}{\pi}\int_{-\pi}^{\pi} \sin(mx)\sin(nx)\,dx = \delta_{mn}$
> - $\int_{-\pi}^{\pi} \cos(mx)\sin(nx)\,dx = 0$（奇偶性）
> - $\int_{-\pi}^{\pi} \frac{1}{\sqrt{2\pi}} \cdot \frac{\cos(nx)}{\sqrt{\pi}} \,dx = 0$，同理 $\sin$
>
> 归一化：$\int_{-\pi}^{\pi} (\frac{1}{\sqrt{2\pi}})^2 dx = 1$，$\int_{-\pi}^{\pi} (\frac{\cos(nx)}{\sqrt{\pi}})^2 dx = 1$，$\int_{-\pi}^{\pi} (\frac{\sin(nx)}{\sqrt{\pi}})^2 dx = 1$。
>
> **（2）验证完全性（稠密性路径）**：利用 Weierstrass 逼近定理——$[-\pi,\pi]$ 上的连续周期函数可被三角多项式一致逼近。而连续函数在 $L^2$ 中稠密，故三角多项式的集合（即 $\operatorname{span}\{\text{三角函数系}\}$）在 $L^2[-\pi,\pi]$ 中稠密。由等价条件 2，该三角函数系是标准正交基。
>
> **（3）Parseval 等式**：对任意 $f \in L^2[-\pi,\pi]$，令
> $$
> a_0 = \frac{1}{\sqrt{2\pi}}\langle f, 1 \rangle,\quad a_n = \frac{1}{\sqrt{\pi}}\langle f, \cos(nx) \rangle,\quad b_n = \frac{1}{\sqrt{\pi}}\langle f, \sin(nx) \rangle
> $$
> 则 Parseval 等式为
> $$
> \frac{1}{\pi}\int_{-\pi}^{\pi} |f(x)|^2\,dx = 2a_0^2 + \sum_{n=1}^{\infty} (a_n^2 + b_n^2)
> $$
>
> **点评**：完全性的验证避开了直接计算 $\langle f,\varphi_k\rangle = 0 \Rightarrow f = 0$ 的困难，转而利用已知的稠密性结果（Weierstrass 逼近定理）——这是验证完全性的常用策略。

## 易错点

> [!warning] 易错点 1：$L^2$ 收敛不等于逐点收敛
> Fourier 展开在 $L^2$ 范数下收敛（$\|f - S_N\|_2 \to 0$），但**不能推出对几乎所有 $x$ 有 $S_N(x) \to f(x)$**。逐点几乎处处收敛需要更强的条件（如 Carleson 定理：$L^2$ 函数的 Fourier 级数 a.e. 收敛，但这已是深刻结果，不在实变函数基本要求范围内）。

> [!warning] 易错点 2：完全性与 Parseval 等式等价——证其一即可
> 四个等价条件中任证一条即知 $\{\varphi_k\}$ 是标准正交基。通常**稠密性**（条件 2）或**Parseval**（条件 4）更容易验证——直接证明"零内积必为零函数"往往较困难。

> [!warning] 易错点 3：不同区间、不同权函数对应不同正交多项式
> Legendre 多项式对应 $[-1,1]$ 上权函数 $w(x) = 1$；Chebyshev 多项式对应 $(-1,1)$ 上权函数 $w(x) = 1/\sqrt{1-x^2}$；Hermite 多项式对应 $\mathbb{R}$ 上权函数 $w(x) = e^{-x^2}$。不能混用——勾股定理和 Parseval 等式中的内积必须带正确的权函数。

## 相关概念

- [[概念/实变函数/L^p空间]] — $L^2$ 是唯一具内积结构的 $L^p$ 空间，正交基理论建基于此
- [[概念/实变函数/Lebesgue积分]] — Fourier 系数由 Lebesgue 积分定义，极限定理保障级数分析
- [[概念/实变函数/Hölder不等式]] — $p=q=2$ 时退化为 Cauchy-Schwarz 不等式：$|\langle f,g\rangle| \leq \|f\|_2\|g\|_2$
- [[概念/实变函数/Fourier变换]] — Fourier 级数（离散谱）到 Fourier 变换（连续谱）的泛化
- [[知识点/实变函数/Riesz定理]] — Riesz-Fischer 定理确立 $L^2$ 与 $\ell^2$ 等距同构，是标准正交基理论的前置

## 习题

- [[课程/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — 习题 5.12（$L^p$ 完备性 / Riesz-Fischer）、习题 5.13（简单函数在 $L^p$ 中稠密）与正交基的完备性/稠密性条件一脉相承
