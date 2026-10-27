---
title: Riesz-Fisher定理
type: 知识点
source:
- "[[课程/归档/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理]]"
topics:
- Riesz-Fisher定理
- L^p空间
- Banach空间
- 完备性
- Cauchy列
- 依测度收敛
- Fatou引理
exam: 考试重点
status: 已整理
tags:
- Riesz-Fisher定理
- Lp空间
- Banach空间
- 完备性
- Cauchy列
- 依测度收敛
- Fatou引理
---

# Riesz-Fisher定理

## 一句话

$L^p(E)$（$1 \leq p \leq \infty$）在 $L^p$ 范数下完备——每个 Cauchy 列都收敛于某个 $L^p$ 函数，这是 $L^p$ 空间成为 Banach 空间的基石，也是泛函分析工具得以在实变函数论中施展的前提。

## 严格定义

设 $(E, \mathcal{M}, m)$ 为测度空间（通常 $E \subset \mathbb{R}^n$，$m$ 为 Lebesgue 测度），$1 \leq p \leq \infty$。若 $\{f_n\} \subset L^p(E)$ 为 **Cauchy 列**，即

$$
\|f_n - f_m\|_p \to 0 \quad (n, m \to \infty),
$$

则存在 $f \in L^p(E)$ 使得

$$
\boxed{\|f_n - f\|_p \to 0 \quad (n \to \infty)}
$$

换言之：**$L^p(E)$ 是 Banach 空间**。

> [!important] 关键点
> - **核心结论**：$L^p$ 范数下的 Cauchy 列必有 $L^p$ 极限——不会"漏出" $L^p$ 空间。这与 Riemann 可积函数空间形成鲜明对比：后者在 $L^1$ 范数下不完备。
> - **$p < \infty$ 的证明核心**：Cauchy 列 $\to$ 依测度 Cauchy $\to$ 子列 a.e. 收敛（Riesz 定理） $\to$ Fatou 引理控制范数 $\to$ 原列 $L^p$ 收敛。
> - **$p = \infty$ 的证明核心**：Cauchy 条件直接给出 a.e. 一致 Cauchy（逐点），无需子列技巧。
> - **与 $\ell^p$ 的类比**：$\ell^p$（序列空间）也是 Banach 空间，$L^2$ 与 $\ell^2$ 等距同构（Riesz-Fisher 定理的原始形式，1907）。

## 推导：$1 \leq p < \infty$ 的完备性证明

> [!proof]- 推导
> **思路总览**：$L^p$ 中 Cauchy 列不必然 a.e. 收敛（打字机序列的 $L^p$ 版本），必须通过子列技巧：先构造快速 Cauchy 子列（几何衰减），再利用 Chebyshev → 依测度 Cauchy → Riesz 子列 a.e. 收敛 → Fatou 引理完成。
>
> ---
>
> **Step 0 — 构造快速 Cauchy 子列**。由 $\|f_n - f_m\|_p \to 0$，可逐层选取子列 $\{f_{n_k}\}$ 满足
> $$
> \|f_{n_{k+1}} - f_{n_k}\|_p < \frac{1}{2^k}, \qquad k = 1, 2, \dots
> $$
>
> **Step 1 — Cauchy 列 $\Rightarrow$ 依测度 Cauchy 列**。由 Chebyshev 不等式，对任意 $\varepsilon > 0$：
> $$
> m\bigl(|f_n - f_m| > \varepsilon\bigr) \leq \varepsilon^{-p}\, \|f_n - f_m\|_p^p \to 0
> $$
> 故 $\{f_n\}$ 依测度为 Cauchy 列。
>
> **Step 2 — 依测度 Cauchy 列 $\Rightarrow$ 依测度收敛**。依测度 Cauchy 性等价于依测度收敛——这是测度收敛空间的完备性（与 $\mathbb{R}$ 中 Cauchy 准则类似）。故存在 $f$（a.e. 有限的可测函数）使 $f_{n_k} \xrightarrow{m} f$。
>
> **Step 3 — 依测度收敛 $\Rightarrow$ 存在子列 a.e. 收敛**。对 $\{f_{n_k}\}$ 应用 **Riesz 定理**：存在子子列（仍记作 $\{f_{n_k}\}$，不影响一般性）使得
> $$
> f_{n_k} \xrightarrow{\text{a.e.}} f
> $$
>
> **Step 4 — Fatou 引理 $\Rightarrow$ $L^p$ 收敛**。对每个固定的 $k$，考虑 $\{f_{n_j}\}_{j \geq k}$：
> $$
> \begin{aligned}
> \int_E |f_{n_k} - f|^p
> &= \int_E \varliminf_{j \to \infty} |f_{n_k} - f_{n_j}|^p \quad (\text{子列 a.e. 收敛于 } f) \\
> &\leq \varliminf_{j \to \infty} \int_E |f_{n_k} - f_{n_j}|^p \quad (\text{Fatou 引理}) \\
> &\leq \varliminf_{j \to \infty} \|f_{n_k} - f_{n_j}\|_p^p
> \end{aligned}
> $$
> 由 Step 0 的构造，当 $j > k$ 时 $\|f_{n_k} - f_{n_j}\|_p \leq \sum_{i=k}^{j-1} \|f_{n_{i+1}} - f_{n_i}\|_p < \sum_{i=k}^{\infty} 1/2^i = 1/2^{k-1}$。故右侧 $\to 0$（$k \to \infty$），即 $f_{n_k} \xrightarrow{L^p} f$。
>
> **Step 5 — 原列收敛**。对任意 $n \geq n_k$，
> $$
> \|f_n - f\|_p \leq \|f_n - f_{n_k}\|_p + \|f_{n_k} - f\|_p
> $$
> 第一项 $\to 0$（原列为 Cauchy 列），第二项 $\to 0$（Step 4）。故 $\|f_n - f\|_p \to 0$。$\square$
>
> ---
>
> **为什么必须用子列？** $L^p$ 中的 Cauchy 列不必然 a.e. 收敛。反例：将打字机序列的区间长度替换为 $1/k^{p+1}$ 后归一化，可构造 $L^p$ Cauchy 列但处处不收敛。子列技巧是绕开这一障碍的唯一途径。

## 推导：$p = \infty$ 的完备性证明

> [!proof]- 推导（$p = \infty$）
> **$L^\infty$ 的完备性证明远简单于 $p < \infty$ 的情形，无需子列和 Fatou 引理。**
>
> 设 $\{f_n\} \subset L^\infty(E)$ 为 Cauchy 列：$\forall \varepsilon > 0$，$\exists N$ 使 $n, m \geq N$ 时
> $$
> \|f_n - f_m\|_\infty < \varepsilon
> $$
> 即对每对 $(n, m) \geq N$，存在零测集 $Z_{n,m}$ 使
> $$
> |f_n(x) - f_m(x)| \leq \varepsilon, \quad \forall x \in E \setminus Z_{n,m}
> $$
>
> 令 $Z = \bigcup_{n,m \geq 1} Z_{n,m} \cup \bigcup_{n \geq 1} \{x : |f_n(x)| = \infty\}$。$Z$ 仍为零测集（可数个零测集的并）。在 $E \setminus Z$ 上，$\{f_n(x)\}$ 是对每个 $x$ 的 **一致 Cauchy 数列**，故存在逐点极限
> $$
> f(x) = \lim_{n \to \infty} f_n(x), \quad x \in E \setminus Z
> $$
> （在 $Z$ 上定义 $f = 0$）。由一致 Cauchy 性，$\|f_n - f\|_\infty \to 0$，且 $f \in L^\infty(E)$。$\square$

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 完备性的意义 | $L^p$ 是 Banach 空间——极限运算不会"漏出"空间，这是泛函分析工具（对偶、弱收敛、Hahn-Banach）的前提 |
| $p < \infty$ 的证明工具链 | Chebyshev $\to$ 依测度 Cauchy $\to$ Riesz 子列 $\to$ Fatou 引理；每一步不可省略 |
| $p = \infty$ 的特殊性 | 证明极简（逐点一致 Cauchy），无需子列技巧；$L^\infty$ 完备但**不可分** |
| 子列的必要性 | $L^p$ Cauchy 列不必然 a.e. 收敛（打字机序列的 $L^p$ 版本），子列是唯一出路 |
| Fatou 的应用方向 | $\int \liminf \leq \liminf \int$，方向不能反——需要下极限在外、积分在内 |
| 与 Riemann 可积函数的对比 | Riemann 可积函数空间在 $L^1$ 范数下**不完备**，这正是引入 Lebesgue 积分的根本动机之一 |
| 与 $\ell^p$ 的等距同构 | 原始 Riesz-Fisher 定理（1907）：$L^2[-\pi,\pi] \cong \ell^2$（通过 Fourier 系数），奠定了泛函分析的基石 |

## 典型例题

> **题目**：完整写出 $L^p(E)$（$1 \leq p < \infty$）完备性（Riesz-Fisher 定理）的证明链，并逐一解释每一步的作用：
> - 为什么从 Cauchy 列构造快速子列？
> - Chebyshev 不等式如何将 $L^p$ 范数条件转化为测度条件？
> - 为什么需要 Riesz 定理（依测度收敛 $\to$ 子列 a.e. 收敛）而不能直接用原列 a.e. 收敛？
> - Fatou 引理的方向为什么是 $\int \liminf \leq \liminf \int$ 而非反向？
> - 最后如何从子列收敛回到原列收敛？

> [!example]- 解答
> **完整证明链与每一步的作用**：
>
> ---
>
> **（1）构造快速子列**：取 $\|f_{n_{k+1}} - f_{n_k}\|_p < 2^{-k}$。
>
> *作用*：保证子列的相邻项差在 $L^p$ 范数下几何衰减。这是后续利用 Fatou 引理控制 $\|f_{n_k} - f\|_p$ 的关键——$\sum \|f_{n_{k+1}} - f_{n_k}\|_p$ 收敛性通过三角不等式传递给 $\|f_{n_k} - f_{n_j}\|_p$。
>
> ---
>
> **（2）Chebyshev 不等式**：$m(|f_n - f_m| > \varepsilon) \leq \varepsilon^{-p} \|f_n - f_m\|_p^p$。
>
> *作用*：将 $L^p$ 范数（积分量）转化为测度（集合大小）。这是从"度量收敛"进入"测度收敛"的唯一桥梁——只有测度条件才能触发 Borel-Cantelli 和 Riesz 定理。
>
> ---
>
> **（3）Riesz 定理**：依测度收敛 $\Rightarrow$ 存在子列 a.e. 收敛。
>
> *为什么不能用原列？* $L^p$ Cauchy 列不保证 a.e. 收敛。反例思路：打字机序列的 $L^p$ 版本——构造闭区间列使每个区间的 $L^p$ 贡献递减（$1/k^{1+\delta}$），同时保留遍历性使每点被无穷多区间覆盖。原列处处不收敛，但快速子列可以选出互不相交的区间从而 a.e. 收敛。
>
> *Riesz 定理的作用*：它是依测度收敛与 a.e. 收敛之间唯一的桥梁，将"概率意义上接近"转化为"逐点意义上接近"。
>
> ---
>
> **（4）Fatou 引理**：$\int \liminf |f_{n_k} - f_{n_j}|^p \leq \liminf \int |f_{n_k} - f_{n_j}|^p$。
>
> *为什么方向是 $\leq$？* 因为积分与极限交换的条件太强（需要控制收敛定理意义上的控制函数），而 Fatou 只要求被积函数非负。这里 $|f_{n_k} - f_{n_j}|^p \geq 0$ 满足条件。方向不能反——$\liminf \int \leq \int \liminf$ 不成立（反例：打字机序列，积分恒为常值但逐点极限为 $0$）。
>
> *为什么应用在这个方向？* 我们需要上界控制：$\|f_{n_k} - f\|_p^p = \int \liminf_j |f_{n_k} - f_{n_j}|^p \leq \liminf_j \|f_{n_k} - f_{n_j}\|_p^p$。右侧由 Step 0 的几何衰减可知 $\to 0$。
>
> ---
>
> **（5）从子列回到原列**：$\|f_n - f\|_p \leq \|f_n - f_{n_k}\|_p + \|f_{n_k} - f\|_p$。
>
> *作用*：Cauchy 条件保证第一项小（$n, n_k$ 充分大），Step 4 保证第二项小（$k$ 充分大）。这是度量空间中 Cauchy 列有收敛子列 $\Rightarrow$ 原列收敛的标准论证——这是 Riesz-Fisher 证明中唯一一歩纯属度量空间理论的推理。
>
> ---
>
> **整体逻辑链回顾**：
> $$
> \begin{aligned}
> \text{Cauchy 列 } \{f_n\}
> &\xrightarrow{\text{Step 0}} \text{快速子列 } \{f_{n_k}\} \\
> &\xrightarrow{\text{Chebyshev}} \text{依测度 Cauchy} \\
> &\xrightarrow{\text{完备性}} \text{依测度收敛于 } f \\
> &\xrightarrow{\text{Riesz}} \text{子子列 a.e. 收敛于 } f \\
> &\xrightarrow{\text{Fatou}} f_{n_k} \xrightarrow{L^p} f \\
> &\xrightarrow{\text{Cauchy 性质}} f_n \xrightarrow{L^p} f
> \end{aligned}
> $$
>
> **点评**：Riesz-Fisher 定理是实变函数论中证明链最长的定理之一——它串联了 Chebyshev、Riesz、Fatou 三大工具，每一步都有明确的数学动机和不可替代性。掌握这一证明链意味着理解 $L^p$ 空间完备性的深层原因：不是"碰巧"完备，而是 Lebesgue 积分的 Fatou 性质和 Riesz 子列定理共同保证的必然结果。

## 易错点

> [!warning] 易错点 1：必须取子列——不能直接对原 Cauchy 列使用 a.e. 收敛
> 证明中先取子列 $\{f_{n_k}\}$ 再使用 Riesz 定理，**不能**直接用原序列 a.e. 收敛。$L^p$ 中的 Cauchy 列不必然 a.e. 收敛——打字机序列经 $L^p$ 归一化后仍是 Cauchy 列但处处不收敛。子列技巧不可跳过。

> [!warning] 易错点 2：Fatou 引理的方向正确性
> 证明中写的是 $\int \varliminf |f_{n_k} - f_{n_j}|^p \leq \varliminf \int |f_{n_k} - f_{n_j}|^p$。常见错误：(a) 写反不等号方向（$\geq$ 不成立）；(b) 将 $\varliminf$ 误写成 $\varlimsup$（虽两者在此等号可达，但逻辑上 $\varliminf$ 是正确的出发点）。

> [!warning] 易错点 3：$L^\infty$ 的完备性证明比 $p < \infty$ 简单得多
> $L^\infty$ 中 Cauchy 条件直接给出 a.e. 逐点一致 Cauchy——去掉可数个零测集的并后，在剩余集上 $\{f_n\}$ 是 $\mathbb{R}$ 中的 Cauchy 列，完备性自动继承自 $\mathbb{R}$。不需要 Chebyshev、Riesz、Fatou 的任何工具。混淆两种情形的证明结构是常见错误。

> [!warning] 易错点 4：Riemann 可积函数空间不完备
> Riesz-Fisher 定理说 $L^p$ **是**完备的，但 Riemann 可积函数空间在 $L^1$ 范数下**不是**完备的。反例：取 $[0,1]$ 上有理数集的特征函数序列（每步只取有限个有理数）——该序列在 $L^1$ 范数下是 Cauchy 列，但极限 Dirichlet 函数不是 Riemann 可积的。正是这种不完备性驱动了 Lebesgue 积分理论的诞生。

## 相关概念

- [[概念/L^p空间]] — Riesz-Fisher 定理是 $L^p$ 空间成为 Banach 空间的完备性保证
- [[概念/依测度收敛]] — 证明链的核心中转站：$L^p$ 收敛 $\Rightarrow$ 依测度收敛（Chebyshev）
- [[概念/几乎处处收敛]] — Riesz 定理将依测度收敛的子列升级为 a.e. 收敛
- [[概念/Lebesgue积分]] — $L^p$ 范数通过 Lebesgue 积分定义，Fatou 引理是完备性证明的收官工具
- [[知识点/Minkowski不等式]] — 三角不等式保证了 $\|\cdot\|_p$ 是范数（完备性讨论的前提）
- [[概念/度量空间]] — Banach 空间 = 完备的赋范空间；完备性是度量空间理论的核心概念
- [[知识点/Riesz定理]] — 依测度收敛 $\Rightarrow$ 存在子列 a.e. 收敛，是 Riesz-Fisher 证明链的关键环节

## 习题

- [[课程/归档/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — 重积分与 $L^p$ 空间
- [[课程/归档/实变函数/习题库/05-重积分与Lp空间/习题5.12-L^p空间的完备性（Riesz-Fischer定理）-习题|习题5.12]] — $L^p$ 空间完备性（Riesz-Fischer）的完整证明
- [[课程/归档/实变函数/习题库/05-重积分与Lp空间/习题5.10-L^p收敛蕴含依测度收敛（定理4.1.9）-习题|习题5.10]] — $L^p$ 收敛 $\Rightarrow$ 依测度收敛（证明链第一步）
- [[课程/归档/实变函数/习题库/05-重积分与Lp空间/习题5.18-Riemann可积函数空间在L^1范数下不完备-习题|习题5.18]] — Riemann 可积函数空间不完备（对照 Riesz-Fisher 完备性）
