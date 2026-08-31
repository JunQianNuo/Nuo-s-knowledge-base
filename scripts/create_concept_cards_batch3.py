#!/usr/bin/env python3
"""Batch create concept cards batch 3 for 实变函数."""
import os, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"D:\知识库\概念\实变函数"
os.makedirs(BASE, exist_ok=True)

cards = {}

# ============================================================
# Lebesgue积分
# ============================================================
cards['Lebesgue积分'] = r"""---
title: Lebesgue积分
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理.md
topics:
  - Lebesgue积分
  - 简单函数逼近
  - Levi单调收敛定理
  - Fatou引理
  - 控制收敛定理
---

# Lebesgue积分

## 一句话

Lebesgue 积分的核心思想是**对值域划分而非对定义域划分**——通过将函数用简单函数从下方逼近，再取积分的上确界来定义。这使得积分与极限运算的交换条件大大放宽，Dirichlet 函数也因此变得可积。

## 严格定义

**第一步：非负简单函数的积分**

设 $h(x) = \sum_{j=1}^{m} a_j \chi_{E_j}(x)$ 是 $E$ 上的非负可测简单函数（$E_j$ 互不相交、可测，$a_j \geq 0$），定义：

$$\int_E h(x)\,dx = \sum_{j=1}^{m} a_j \cdot m(E_j)$$

（几何意义：下方图的体积 = 各"柱体"体积之和。）

**第二步：非负可测函数的积分**

设 $f \geq 0$ 在 $E$ 上可测，定义：

$$\int_E f(x)\,dx = \sup\left\{ \int_E h(x)\,dx \;\middle|\; h \text{ 是 } E \text{ 上的非负简单可测函数}, \; h \leq f \right\}$$

若积分有限，称 $f$ 在 $E$ 上 **Lebesgue 可积**，记 $f \in L(E) = L^1(E)$。

**第三步：一般可测函数的积分**

分解 $f = f^+ - f^-$（$f^+ = \max(f,0), f^- = \max(-f,0)$）。若 $\int_E f^+$ 和 $\int_E f^-$ 至少有一个有限，定义：

$$\int_E f(x)\,dx = \int_E f^+(x)\,dx - \int_E f^-(x)\,dx$$

若两者都有限，则 $f \in L(E)$。

> [!important] 核心要点
> - **可积即绝对可积**：$f \in L(E) \iff |f| \in L(E)$。这与黎曼积分截然不同（黎曼积分中条件收敛可以不绝对收敛）。
> - **三大极限定理**：(1) Levi 单调收敛定理——单调增的非负函数列，极限与积分可交换；(2) Fatou 引理——$\int \liminf f_k \leq \liminf \int f_k$；(3) 控制收敛定理——若有控制函数 $g \in L^1$，则 $\lim \int f_k = \int \lim f_k$。
> - **零测集上积分为零**：$m(E)=0 \Rightarrow \int_E f = 0$。
> - **$f=0$ a.e. $\iff \int |f| = 0$**：积分具有正定性。

## 由来与作用

- **历史起源**：Henri Lebesgue 在其 1902 年博士论文《积分、长度与面积》中提出了这种全新的积分定义。他受到 Borel 测度论和 Jordan 容量理论的启发，天才地将划分从定义域转向值域。
- **解决的问题**：Dirichlet 函数（在有理点取 1、无理点取 0）在黎曼框架下不可积，但在 Lebesgue 框架下可积且积分为 0。更一般地，Lebesgue 积分使极限与积分交换的条件从"一致收敛"放宽到"控制函数存在"。
- **在实变函数中的角色**：是整个课程的核心——第 1-2 章为它准备集合论和测度基础，第 3 章为它建立可测函数理论，第 5 章将其推广到 $L^p$ 空间和重积分。
- **与黎曼积分的关系**：若 $f$ 在 $[a,b]$ 上黎曼可积，则 $f$ 必 Lebesgue 可积且积分值相等；反过来，Lebesgue 可积的广义可积函数不一定是黎曼可积的。有界函数黎曼可积 $\iff$ 不连续点为零测集。

## 相关概念

- [[概念/实变函数/简单函数]] — 简单函数的积分是 Lebesgue 积分定义的起点。
- [[概念/实变函数/可测函数]] — Lebesgue 积分的定义对象必须是可测函数。
- [[概念/实变函数/几乎处处]] — 积分值与零测集上的修改无关。
- [[概念/实变函数/零测集]] — 零测集上积分为零；黎曼可积性由此刻画。
- [[概念/实变函数/L^p空间]] — $L^1(E)$ 即 Lebesgue 可积函数空间；$L^p$ 是其自然推广。
"""

# ============================================================
# L^p空间
# ============================================================
cards['L^p空间'] = r"""---
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
"""

# ============================================================
# Hölder不等式
# ============================================================
cards['Hölder不等式'] = r"""---
title: Hölder不等式
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - Hölder不等式
  - 共轭指数
  - Young不等式
  - Schwarz不等式
---

# Hölder不等式

## 一句话

Hölder 不等式是 $L^p$ 空间理论的基石不等式——它表明乘积的 $L^1$ 范数不超过各自 $L^p$ 与 $L^q$ 范数的乘积，其中 $p, q$ 为共轭指数（$1/p + 1/q = 1$）。

## 严格定义

设 $E \in \mathfrak{M}_n$，$1 \leq p, q \leq \infty$ 满足 $p^{-1} + q^{-1} = 1$。若 $f \in L^p(E)$，$g \in L^q(E)$，则 $fg \in L^1(E)$，且

$$\|fg\|_1 \leq \|f\|_p \|g\|_q.$$

等价形式：

$$\int_E |f(x)g(x)| \, dx \leq \left(\int_E |f(x)|^p dx\right)^{1/p} \left(\int_E |g(x)|^q dx\right)^{1/q}.$$

**特殊情形**：
- $p = q = 2$：退化为 **Schwarz 不等式** $\left|\int_E fg\right| \leq \|f\|_2 \|g\|_2$。
- $p = 1, q = \infty$：$\|fg\|_1 \leq \|f\|_1 \|g\|_\infty$（几乎显然）。
- $p = \infty, q = 1$：$\|fg\|_1 \leq \|f\|_\infty \|g\|_1$。

> [!important] 核心要点
> - **证明核心（Young 不等式）**：由对数函数的上凸性导出 $a^{1/p} b^{1/q} \leq a/p + b/q$（$a,b > 0$）。取 $a = |f|^p / \|f\|_p^p$，$b = |g|^q / \|g\|_q^q$，积分即得。
> - **共轭指数的必备性**：$\frac{1}{p} + \frac{1}{q} = 1$ 保证了不等式是齐次的——若用其他指数对，不等式将不具有适当的尺度不变性。
> - **不可用于 $p,q$ 均为非共轭**：若 $1/p + 1/q > 1$，乘积 $fg$ 可能不可积。

## 由来与作用

- **历史起源**：由 Otto Hölder（1889）在研究 Fourier 级数收敛性时发现，后来由 F. Riesz 纳入 $L^p$ 空间理论体系。其离散形式（级数版本）更早出现。
- **解决的问题**：在没有逐点控制的情况下，如何约束乘积函数的积分？Hölder 不等式给出了最佳可能的范数估计，且当 $f$ 与 $g$ "对齐"时可以达到等号。
- **在实变函数中的角色**：
  - 是 $L^p$ 空间理论的第一块基石——没有它就无法证明 Minkowski 不等式（三角不等式）。
  - 广泛用于证明 $L^p$ 范数的对偶刻画、$L^p$ 空间的包含关系等。
  - 与 Young 不等式共同构成 $L^p$ 空间不等式体系的基础。
- **关键性质**：等号成立条件（对 $1<p,q<\infty$）：存在常数 $c$ 使 $|f|^p$ 与 $|g|^q$ 成比例 a.e.。

## 相关概念

- [[概念/实变函数/L^p空间]] — Hölder 不等式是 $L^p$ 理论的核心工具。
- [[概念/实变函数/Minkowski不等式]] — Minkowski 不等式的证明依赖于 Hölder 不等式。
- [[概念/实变函数/卷积]] — 卷积的 Young 不等式（$\|f*g\|_p \leq \|f\|_p \|g\|_1$）是 Hölder 不等式的推广。
"""

# ============================================================
# Minkowski不等式
# ============================================================
cards['Minkowski不等式'] = r"""---
title: Minkowski不等式
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - Minkowski不等式
  - L^p三角不等式
  - 范数公理
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

- [[概念/实变函数/L^p空间]] — Minkowski 不等式使 $L^p$ 成为赋范空间。
- [[概念/实变函数/Hölder不等式]] — Minkowski 不等式的证明依赖 Hölder 不等式。
- [[概念/实变函数/卷积]] — 卷积的 Young 不等式是 Minkowski 与 Hölder 的综合推广。
"""

# ============================================================
# 卷积
# ============================================================
cards['卷积'] = r"""---
title: 卷积
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - 卷积
  - Fubini定理
  - 磨光算子
  - Young不等式
---

# 卷积

## 一句话

卷积是两个函数的"平移加权平均"——$f*g(x) = \int f(x-y)g(y)\,dy$。它将两个函数的信息融合为一个新函数，是可积性保持、有磨光效果的核心运算，广泛应用于 PDE、信号处理和概率论。

## 严格定义

设 $f(x)$ 和 $g(x)$ 是 $\mathbb{R}^n$ 上的可测函数，若积分

$$\int_{\mathbb{R}^n} f(x-y)g(y)\,dy$$

存在，则称其为 $f$ 和 $g$ 的**卷积**，记为：

$$f*g(x) = \int_{\mathbb{R}^n} f(x-y)g(y)\,dy.$$

**基本性质**：
- **交换性**：$f*g = g*f$（通过平移 $z = x-y$ 变换可得）。
- **线性性**：$(\alpha f + h) * g = \alpha f*g + h*g$。

> [!important] 核心要点
> - **可积性定理**：若 $f, g \in L^1(\mathbb{R}^n)$，则 $f*g$ 对 a.e. $x$ 存在，且 $f*g \in L^1$，$\|f*g\|_1 \leq \|f\|_1 \|g\|_1$。证明用到 Tonelli 定理交换积分次序。
> - **Young 不等式**（卷积的 $L^p$ 有界性）：若 $f \in L^p$（$1 \leq p \leq \infty$），$g \in L^1$，则 $f*g \in L^p$，且 $\|f*g\|_p \leq \|f\|_p \|g\|_1$。
> - **磨光（Mollification）**：用光滑函数做卷积可以使粗糙函数变光滑——$C_c^\infty * L_{\text{loc}}^1 \to C^\infty$。
> - **$L^2$ 的特殊性**：$L^2 * L^2$ 得到有界连续函数（定理 4.3.3）。

## 由来与作用

- **历史起源**：卷积运算在 18 世纪已隐式出现（Laplace 变换、Euler），但直到 20 世纪初才由 Lebesgue 积分赋予严格基础。名称"convolution"由 von Neumann 等人在 1940s 推广。
- **解决的问题**：
  - 提供了函数的"平滑化"标准手段——任何 $L_{\text{loc}}^1$ 函数用磨光核卷积后变为 $C^\infty$ 函数。
  - 通过 Fubini 定理将重积分理论（交换积分次序）应用于具体运算。
  - 在 Fourier 分析中，"卷积的 Fourier 变换 = Fourier 变换的乘积"是核心恒等式。
- **在实变函数中的角色**：是 Fubini 定理的经典应用案例，连接了重积分理论与函数运算。也是证明 $C_c^\infty$ 在 $L^p$ 中稠密（$1 \leq p < \infty$）的技术工具。
- **关键性质**：$\|f*g\|_1 \leq \|f\|_1 \|g\|_1$；Young 不等式推广到 $L^p * L^q \to L^r$（$1/p + 1/q = 1 + 1/r$）。

## 相关概念

- [[概念/实变函数/Lebesgue积分]] — 卷积的存在性由 Lebesgue 积分保证。
- [[概念/实变函数/L^p空间]] — 卷积的 Young 不等式刻画了 $L^p$ 上的有界性。
- [[概念/实变函数/Fourier变换]] — $\widehat{f*g} = (2\pi)^{n/2} \hat{f} \cdot \hat{g}$，卷积与 Fourier 变换对偶。
- [[概念/实变函数/Hölder不等式]] — Young 不等式的证明基于 Hölder。
"""

# ============================================================
# Fourier变换
# ============================================================
cards['Fourier变换'] = r"""---
title: Fourier变换
type: 概念
subject: 实变函数
source:
  - 课程/实变函数/课件/MD/2023-RA-28.md
topics:
  - Fourier变换
  - L^1上的Fourier变换
  - L^2上的Fourier变换
  - Riemann-Lebesgue引理
---

# Fourier变换

## 一句话

Fourier 变换将函数从"时域"（或空域）转换到"频域"——$\hat{f}(t) = \frac{1}{(2\pi)^{n/2}} \int f(x) e^{-i t \cdot x} dx$，它在 $L^1$ 上产生有界连续函数、在 $L^2$ 上是等距同构，且将卷积变为乘积，是调和分析的核心工具。

## 严格定义

**$L^1(\mathbb{R}^n)$ 上的 Fourier 变换**：设 $f \in L^1(\mathbb{R}^n)$，定义

$$\hat{f}(t) = \frac{1}{(2\pi)^{n/2}} \int_{\mathbb{R}^n} f(x) e^{-i t \cdot x} \, dx, \quad t \in \mathbb{R}^n,$$

其中 $t \cdot x = \sum_{i=1}^n t_i x_i$。$\hat{f}(t)$ 是复值函数。

**基本性质（$L^1$）**：
- **有界性**：$|\hat{f}(t)| \leq (2\pi)^{-n/2} \|f\|_1$。
- **连续性**：由控制收敛定理，$\hat{f}(t)$ 在 $\mathbb{R}^n$ 上一致连续。
- **Riemann-Lebesgue 引理**：$\lim_{|t| \to \infty} \hat{f}(t) = 0$（Fourier 变换在无穷远处衰减到零）。

**$L^2(\mathbb{R}^n)$ 上的 Fourier 变换**：由于 $L^1 \cap L^2$ 在 $L^2$ 中稠密，可以将 Fourier 变换从 $L^1 \cap L^2$ 延拓到整个 $L^2$ 上，得到 $L^2$ 上的酉算子：

$$\|\hat{f}\|_2 = \|f\|_2 \quad (\text{Plancherel 定理}).$$

> [!important] 核心要点
> - **卷积与 Fourier 变换的对偶**：$\widehat{f*g} = (2\pi)^{n/2} \hat{f} \cdot \hat{g}$——卷积在频域变为乘积，乘积在频域变为卷积。
> - **导数与乘法**：Fourier 变换将求导变为乘以 $it$：$\widehat{\partial_j f}(t) = i t_j \hat{f}(t)$。
> - **Gauss 函数的不动性**：$f(x) = e^{-|x|^2/2}$ 的 Fourier 变换为 $\hat{f}(t) = e^{-|t|^2/2}$。
> - **$L^1$ 反演公式**：若 $\hat{f} \in L^1$，则 $f(x) = \frac{1}{(2\pi)^{n/2}} \int \hat{f}(t) e^{i x \cdot t} dt$ a.e.。

## 由来与作用

- **历史起源**：Joseph Fourier（1807-1822）在研究热传导方程时引入了以他命名的级数和变换。他声称"任意"周期函数都可展开为三角级数——这一大胆论断引发了 Cauchy、Dirichlet、Riemann 等一个世纪的严格化工作，最终在 Lebesgue 积分框架下得到圆满解决。
- **解决的问题**：Fourier 变换将微分方程变为代数方程（求导 $\leftrightarrow$ 乘以 $it$），将卷积变为乘积——大大简化了信号处理、PDE 和概率论中的计算。
- **在实变函数中的角色**：
  - 是 Lebesgue 积分理论在调和分析中的核心应用——Fourier 变换的严格定义依赖于 Lebesgue 可积性。
  - $L^2$ 上的 Plancherel 定理是 Hilbert 空间理论的标准例子。
  - 卷积与 Fourier 变换的对偶关系是分析学中最优美的结构之一。
- **关键性质**：$\mathcal{F}: L^2 \to L^2$ 是酉算子；Riemann-Lebesgue 引理；$\mathcal{F}$ 将速降函数空间 $\mathcal{S}$ 映到自身。

## 相关概念

- [[概念/实变函数/Lebesgue积分]] — Fourier 变换的严格定义需要 Lebesgue 积分。
- [[概念/实变函数/L^p空间]] — Fourier 变换在 $L^1$ 和 $L^2$ 上有定义，在其他 $L^p$ 上需用插值理论。
- [[概念/实变函数/卷积]] — $\widehat{f*g} = (2\pi)^{n/2} \hat{f} \hat{g}$，卷积与 Fourier 变换互为对偶。
- [[概念/实变函数/Minkowski不等式]] — 用于证明 Fourier 变换相关的积分不等式。
"""

# Write all cards
for name, content in cards.items():
    path = os.path.join(BASE, name + '.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.lstrip('\n'))
    print(f'Created: {path}')

print(f'\nDone. Created {len(cards)} cards.')
