---
title: SOR迭代
type: 知识点
subject: 数值分析
source:
  - 课程/数值分析/知识点解析梳理/04-线性方程组的迭代法-知识梳理.md
topics:
  - SOR迭代
  - 超松弛
  - 迭代法
  - 最优松弛因子
---

# SOR迭代

## 一句话

Gauss-Seidel 的松弛推广——$x^{(k+1)}=(1-\omega)x^{(k)}+\omega x_{GS}^{(k+1)}$，通过松弛因子 $\omega$ 调节收敛速度。

## 严格定义

**SOR（Successive Over-Relaxation）迭代**：

令 $x_i^{GS}$ 为 Gauss-Seidel 算出的临时值，则：

$$
\boxed{x_i^{(k+1)}=(1-\omega)x_i^{(k)}+\omega\,x_i^{GS}}
$$

**迭代矩阵**：

$$
\boxed{G_{SOR}=(D+\omega L)^{-1}\big((1-\omega)D-\omega U\big)}
$$

- $\omega=1$：退化为 Gauss-Seidel
- $1<\omega<2$：超松弛（通常加速收敛）
- $0<\omega<1$：亚松弛（某些非收敛迭代收敛化）

收敛必要条件：$0<\omega<2$（Ostrowski-Reich 定理）。

> [!important] $\omega_{opt}$ 由 $\rho(G_J)$ 决定——对于一致性排序矩阵，$\omega_{opt}=1+\big(\frac{\rho(G_J)}{1+\sqrt{1-\rho^2(G_J)}}\big)^2$

## 推导：松弛思想

> [!proof]- 推导
> G-S 的更新方向为 $\Delta=x_i^{GS}-x_i^{(k)}$。
>
> SOR 沿此方向做加权步：
>
> $$
> x_i^{(k+1)}=x_i^{(k)}+\omega(x_i^{GS}-x_i^{(k)})=(1-\omega)x_i^{(k)}+\omega x_i^{GS}
> $$
>
> 当 $\omega>1$ 时"越过" GS 步（超松弛加速收敛），$\omega<1$ 时"退缩"（稳定化发散迭代）。
>
> 最优 $\omega$ 的导出依赖于矩阵拥有一致性排序（Consistently Ordered）——Poisson 方程离散矩阵满足此性质。

## 算法步骤

1. 选定松弛因子 $\omega\in(0,2)$
2. 给定 $x^{(0)}$，容差 $\varepsilon$
3. 对 $k=0,1,\ldots$
   - 对 $i=1,\ldots,n$：
     $$x_i^{GS}=\frac{1}{a_{ii}}\left(b_i-\sum_{j=1}^{i-1}a_{ij}x_j^{(k+1)}-\sum_{j=i+1}^{n}a_{ij}x_j^{(k)}\right)$$
     $$x_i^{(k+1)}=(1-\omega)x_i^{(k)}+\omega\,x_i^{GS}$$
4. 检查停机准则

## 关键性质

| 性质 | 数值 |
|------|------|
| $\omega=1$ | G-S（退化） |
| $\omega>1$ | 超松弛（加速） |
| $\omega<1$ | 亚松弛（稳定化） |
| 收敛必要条件 | $0<\omega<2$ |
| SPD 充分条件 | $0<\omega<2$ |
| 最优 $\omega$ | 需 $\rho(G_J)$ 估算 |

## 典型例题

> **题目**：对 Poisson 方程 5 点差分离散矩阵（$n=3$），Jacobi 迭代矩阵的谱半径 $\rho(G_J)=\cos(\pi h)\approx0.951$。求最优 SOR 松弛因子。

> [!example]- 解答
> 该矩阵满足一致性排序，最优 $\omega$ 公式：
>
> $$
> \omega_{opt}=\frac{2}{1+\sqrt{1-\rho^2(G_J)}}=\frac{2}{1+\sqrt{1-0.951^2}}=\frac{2}{1+\sqrt{0.0956}}=\frac{2}{1+0.309}=1.528
> $$
>
> 对照 $\rho(G_{SOR})=\omega_{opt}-1=0.528$，而 G-S 的 $\rho(G_G)=\rho^2(G_J)=0.904$。
>
> 收敛率对比：
> - Jacobi：$-\log\rho=0.050$
> - G-S：$-\log\rho=0.101$（约 2 倍于 Jacobi）
> - SOR($1.528$)：$-\log\rho=0.639$（约 13 倍于 Jacobi！）
>
> **点评**：选对 $\omega$ 的 SOR 迭代带来数量级别的加速——是迭代法工程实践中的标准技巧。

## 易错点

> [!warning] $\omega$ 选错比 G-S 还慢
> 若 $\omega$ 过高（接近 2），可能振荡发散；若 $\omega$ 太低（接近 0），几乎原地踏步。最优 $\omega$ 需要估算 $\rho(G_J)$——不精确的 $\omega$ 可能比 G-S 更差。

> [!warning] $\omega$ 对问题强依赖
> 没有万能的 $\omega$——矩阵的不同离散化（$h$ 不同）对应不同的最优 $\omega$。对每种网格都需要单独估算。

> [!warning] $0<\omega<2$ 只是必要条件
> 即使 $A$ 是对称正定且 $0<\omega<2$，若矩阵不满足其他条件（如一致性排序），SOR 的收敛行为无法用 $\rho(G_J)$ 简单表达。

## 相关概念

- [[概念/数值分析/谱半径]]
- [[知识点/数值分析/Gauss-Seidel迭代]]
- [[知识点/数值分析/迭代收敛定理(谱半径)]]

## 习题

- [[课程/数值分析/习题库/04-线性方程组的迭代法/README|第4章习题库]]
