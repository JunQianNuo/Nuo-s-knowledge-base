---
schema_version: 2
type: proposition
time: '2026-08-31T11:44:20+08:00'
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理]]'
- '[[03_Sources/Reviews/归档/实变函数/复习/IV-Lp空间]]'
- '[[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/考题-正交基与Fourier展开]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-03-第11节-希尔伯特空间定理授课]]'
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-泛函分析]]'
aliases:
- 正交基与Fourier展开
tags:
- Fourier展开
- Parseval等式
- 正交基与Fourier展开
- L2空间
exam: 考试重点
---

# Hilbert空间正交基与Parseval等式

## 一句话

$L^2$ 空间中，标准正交基将任意函数展开为基函数的无穷线性组合（Fourier 展开），展开系数由内积给出，Parseval 等式保证范数守恒——这是 Hilbert 空间几何在函数空间中的完整体现。

## 严格定义

设 $L^2(E)$ 为 $E \subset \mathbb{R}^n$ 上平方可积函数的 Hilbert 空间，内积定义为

$$
\langle f, g \rangle = \int_E f(x)\overline{g(x)}\,dm(x)
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
> 对固定 $f$，等号当且仅当 $f\in\overline{\operatorname{span}}\{\varphi_k\}$；只有对所有 $f\in L^2(E)$ 都取等号，才等价于该正交系完全。

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
> **（2）验证完全性（稠密性路径）**：利用 Weierstrass 逼近定理——$[-\pi,\pi]$ 上的连续周期函数可被三角多项式一致逼近。而连续周期函数在 $L^2[-\pi,\pi]$ 中稠密（可在端点附近小区间修正连续逼近函数使其周期化），故三角多项式的集合（即 $\operatorname{span}\{\text{三角函数系}\}$）在 $L^2[-\pi,\pi]$ 中稠密。由等价条件 2，该三角函数系是标准正交基。
>
> **（3）Parseval 等式**：对任意 $f \in L^2[-\pi,\pi]$，令
> $$
> a_0 = \frac{1}{\sqrt{2\pi}}\langle f, 1 \rangle,\quad a_n = \frac{1}{\sqrt{\pi}}\langle f, \cos(nx) \rangle,\quad b_n = \frac{1}{\sqrt{\pi}}\langle f, \sin(nx) \rangle
> $$
> 则 Parseval 等式为
> $$
> \int_{-\pi}^{\pi} |f(x)|^2\,dx = |a_0|^2 + \sum_{n=1}^{\infty} (|a_n|^2 + |b_n|^2)
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

- [[01_Knowledge/L^p空间]] — $L^2$ 是唯一具内积结构的 $L^p$ 空间，正交基理论建基于此
- [[01_Knowledge/Lebesgue积分]] — Fourier 系数由 Lebesgue 积分定义，极限定理保障级数分析
- [[01_Knowledge/Hölder不等式]] — $p=q=2$ 时退化为 Cauchy-Schwarz 不等式：$|\langle f,g\rangle| \leq \|f\|_2\|g\|_2$
- [[01_Knowledge/Fourier变换]] — Fourier 级数（离散谱）到 Fourier 变换（连续谱）的泛化
- [[01_Knowledge/Riesz定理]] — Riesz-Fischer 定理确立 $L^2$ 与 $\ell^2$ 等距同构，是标准正交基理论的前置

## 习题

- [[03_Sources/Courses/归档/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — 习题 5.12（$L^p$ 完备性 / Riesz-Fischer）、习题 5.13（简单函数在 $L^p$ 中稠密）与正交基的完备性/稠密性条件一脉相承


## 本轮习题补充与边界核对

对f(x)=x于[-π,π]，标准三角正交基为 $1/√(2π)$、cos(nx)/√π、sin(nx)/√π。奇偶性使常数和余弦系数0；积分分部给
$$\langle f,\sin(nx)/\sqrtπ\rangle=\frac{2\sqrtπ(-1)^{n+1}}n.$$
Parseval与 $\|f\|_2²=2π³/3$ 联立，得 $2π³/3=4π\sum_{n≥1}n^{-2}$，所以 $\sum_{n≥1}n^{-2}=π²/6$。这是范数等式的应用，a.e.或逐点收敛不由这一计算本身证明。对复空间内积须保留共轭。


## 本次来源核对与适用范围

一般Hilbert空间可有不可数正规正交基；对固定x，令A_n={α:|(x,e_α)|≥1/n}，Bessel使各A_n有限，故非零系数支撑至多可数。平方尾和保证正交部分和Cauchy，完备性给极限，基的稠密张成认出极限为x，并得Parseval与无条件收敛。单个向量可数支撑不推出整个空间可分；无限维可分H才对应ℓ²，有限维对应同标量域Fᵈ。




## 不可数基、尾和及坐标同构的详细核验

设$H$为Hilbert空间，$\{e_\alpha\}_{\alpha\in A}$为正规正交基，$c_\alpha=(x,e_\alpha)$。则

$$
x=\sum_{\alpha\in A}c_\alpha e_\alpha,\qquad
\|x\|^2=\sum_{\alpha\in A}|c_\alpha|^2.
$$

求和具有范数意义，非零项至多可数，级数无条件收敛。$A$本身可以不可数；每个固定$x$使用一个可数支撑，换$x$时支撑可以变，不能因此认定整个空间可分。

> 一句话来说：单个向量只需要可数多个非零正交坐标，整个空间却可能需要不可数多个基向量。

### 1. 非零系数为什么可数

**按课堂思路补全严格证明**：对每个正整数$n$，令$A_n=\{\alpha:|c_\alpha|\ge1/n\}$。若它有任意多不同元素，取其中$N$个，由Bessel不等式

$$
N/n^2\le\sum_{\alpha\in F}|c_\alpha|^2\le\|x\|^2
$$

得到$N\le n^2\|x\|^2$，故$A_n$有限。非零系数支撑恰为$\bigcup_{n\ge1}A_n$，所以至多可数；$x=0$情形直接成立。

### 2. 收敛存在不等于已经知道极限是谁

枚举非零系数为$c_{\alpha_j}$，令$s_N=\sum_{j=1}^N c_{\alpha_j}e_{\alpha_j}$。正交性给出

$$
\|s_N-s_M\|^2=\sum_{j=M+1}^N|c_{\alpha_j}|^2\to0.
$$

平方和由Bessel控制，故是Cauchy列；$H$完备，存在$y\in H$使$s_N\to y$。接下来分别检查：若$e_\alpha$出现在枚举中，内积连续性给$(y,e_\alpha)=c_\alpha$；若未出现，则每个部分和与它正交，且$c_\alpha=0$，仍有$(y,e_\alpha)=0$。因此$x-y$与全部基向量正交，基的完备性迫使$x-y=0$。

**无条件收敛的补充说明**：选有限集合$F$使其外系数平方和小于$\varepsilon^2$。任何有限尾项的范数平方均不超过这份尾和，因此重排后仍收敛到$x$；不是直接把实数级数的绝对收敛判据照搬到向量级数。

### 3. Parseval及能量解释

由正交分解

$$
\|x\|^2=\sum_{j=1}^N|c_{\alpha_j}|^2+\|x-s_N\|^2
$$

令$N\to\infty$得到等式。它把有限维“长度平方等于坐标平方和”推广到Hilbert空间；信号范数可解释为能量，但抽象向量不等于一个脱离基选择的坐标表。

> [!warning] 等式成立的关键是完整基
> 任意正规正交集一般只保证Bessel不等式。Parseval不限于可分空间；可分性只是使整组基可用自然数枚举。坐标依赖所选的基。

**补足维数条件**：无限维可分Hilbert空间$H$与同一标量域上的$\ell^2$线性等距、保内积同构；$d$维空间对应$\mathbb F^d$，不能把有限维也说成与无限维$\ell^2$双射同构。

取可数正规正交基，定义$Ux=((x,e_n))_{n\ge1}$。证明依次是：

1. Parseval保证$Ux\in\ell^2$，内积对第一变量线性保证$U$线性。
2. 将$x,y$都按基展开，先对有限部分和计算，再由连续性取极限：

$$
(Ux,Uy)_{\ell^2}=\sum_n(x,e_n)\overline{(y,e_n)}=(x,y)_H.
$$

该数项级数的绝对收敛由Cauchy–Schwarz保证。由此$\|Ux\|_2=\|x\|$，$Ux=0$推出$x=0$，故单射。

3. 满射不能仅凭“系数看起来像序列”认定。给定$a=(a_n)\in\ell^2$，有限和$x_N=\sum_{n=1}^N a_ne_n$满足

$$
\|x_N-x_M\|^2=\sum_{n=M+1}^N|a_n|^2\to0.
$$

完备性给$x_N\to x$，内积连续性给$(x,e_n)=a_n$，所以$Ux=a$。

> 一句话来说：抽象空间中的一个元素与它的一串坐标不是同一对象，但通过选基可建立保持全部内积结构的对应。

## 截断误差自测（来源新编）

1. 在$\ell^2$中，设$a_n=2^{-n}$。计算$\|a\|^2$、前$N$个坐标截断的误差平方，并说明为何截断序列的极限在$\ell^2$中存在。

> [!hint]- 提示
> 使用等比级数与尾和，不要把误差范数和其平方混同。

> [!solution]- 解析
> $\|a\|^2=\sum_{n\ge1}4^{-n}=1/3$，尾和$\sum_{n>N}4^{-n}=4^{-N}/3$。截断序列是Cauchy列，完备性保证收敛，极限即$a$。


## 正规正交基存在性的回顾边界

11月3日开头明确回顾此前讲过正规正交基存在性及Zorn证明。其关键步骤是将正规正交集按包含排序，链的并仍正规正交，Zorn给极大正规正交集；若闭线性张成$M$不是整个$H$，可独立用最近点论证给非零正交方向：取$x\notin M$及极小化列$m_k\in M$，令$d=\operatorname{dist}(x,M)>0$。平行四边形恒等式给

$$\|m_k-m_l\|^2\le2\|x-m_k\|^2+2\|x-m_l\|^2-4d^2\to0.$$

完备与闭性给$m_k\to m\in M$，且$\|x-m\|=d$。沿$M$中任一方向作实参数微扰（复数情形再乘$i$），最小性分别给$\operatorname{Re}(x-m,v)=0$与$\operatorname{Im}(x-m,v)=0$，故$x-m\perp M$。将非零$x-m$正规化后可再加入，矛盾。这样不依赖本节借正交基证明的投影定理，避免循环论证。这是依据可核实回顾作的原理展开，不表示10月30日缺失课堂的其他例题、证明和作业已经恢复。

## 本次补充来源

- [[03_Sources/Courses/泛函分析/课堂笔记/2026-11-03-第11节-希尔伯特空间定理授课]]

证明展开、自测、教材补足仍按原来源标记其整理性质，不冒充教师逐字讲授。
