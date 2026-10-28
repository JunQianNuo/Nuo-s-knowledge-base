---
schema_version: 2
type: method
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理]]'
legacy_topics:
- Lagrange插值
- 插值多项项
- Lagrange基函数
- Runge现象
tags:
- Lagrange插值
- 插值多项项
- Runge现象
topics:
- '[[02_Maps/MOC-数值计算]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Lagrange插值

## 一句话

用 Lagrange 基函数 $\ell_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ 的线性组合直接构造过所有数据点的插值多项式。

## 严格定义

给定 $n+1$ 个互异节点 $(x_i,f(x_i)),\;i=0,1,\ldots,n$。

**Lagrange 基函数**：

$$
\boxed{\ell_i(x)=\prod_{\substack{j=0\\j\neq i}}^{n}\frac{x-x_j}{x_i-x_j}}
$$

满足 $\ell_i(x_j)=\delta_{ij}$（Kronecker delta）。

**Lagrange 插值多项式**：

$$
\boxed{P_n(x)=\sum_{i=0}^{n}f(x_i)\ell_i(x)}
$$

**存在唯一性**：过 $n+1$ 点存在唯一的不超过 $n$ 次多项式。

> [!important] 构造直观——不需解方程组，但增一个点需全部重算

## 推导：插值条件与基函数

> [!proof]- 推导
> 插值条件：$P_n(x_i)=f(x_i),\;i=0,\ldots,n$。
>
> 由于 $\ell_i(x_j)=\delta_{ij}$，$P_n(x_j)=\sum_i f(x_i)\delta_{ij}=f(x_j)$——自动满足所有插值条件。
>
> **存在唯一性**：Vandermonde 行列式 $\det(V)=\prod_{i<j}(x_i-x_j)\neq0$（节点互异）→插值矩阵可逆→解唯一。
>
> **插值余项**：$f(x)-P_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x-x_i)$。

## 算法步骤

1. 输入节点 $(x_i,f_i)$，$i=0,\ldots,n$
2. 对每个插值点 $x$：
   - 计算所有 $\ell_i(x)$：分子 $\prod_{j\neq i}(x-x_j)$，分母 $\prod_{j\neq i}(x_i-x_j)$
   - 加权求和 $P_n(x)=\sum f_i\ell_i(x)$

## 关键性质

| 性质 | 数值 |
|------|------|
| 构造方式 | 基函数线性组合 |
| 增节点 | 全部重算 |
| 存在唯一性 | 唯一（节点互异） |
| 最高效场景 | 节点固定、多点求值 |
| 缺点 | Runge 现象（均匀节点高次） |

## 典型例题

> **题目**：已知 $f(0)=1,\;f(1)=2,\;f(2)=3$，求 Lagrange 插值多项式。

> [!example]- 解答
> 三个节点，$n=2$。
>
> **基函数**：
>
> $\ell_0(x)=\frac{(x-1)(x-2)}{(0-1)(0-2)}=\frac{x^2-3x+2}{2}$
>
> $\ell_1(x)=\frac{(x-0)(x-2)}{(1-0)(1-2)}=-(x^2-2x)=2x-x^2$
>
> $\ell_2(x)=\frac{(x-0)(x-1)}{(2-0)(2-1)}=\frac{x^2-x}{2}$
>
> **插值多项式**：
>
> $P_2(x)=1\cdot\frac{x^2-3x+2}{2}+2\cdot(2x-x^2)+3\cdot\frac{x^2-x}{2}$
>
> $=\frac{x^2-3x+2}{2}+4x-2x^2+\frac{3x^2-3x}{2}=(\frac12-2+\frac32)x^2+(-\frac32+4-\frac32)x+1=x+1$
>
> $P_2(x)=x+1$——验证：$f(0)=1,f(1)=2,f(2)=3$。
>
> **点评**：数据点恰好在直线 $y=x+1$ 上，插值多项式退化到一次。

## 易错点

> [!warning] 增点需重算所有基函数
> Lagrange 形式的基函数依赖**全部**节点——加一个新点后所有 $\ell_i(x)$ 都要重新计算。对需要动态增点的场景，Newton 插值（差商表）更合适。

> [!warning] 均匀节点 + 高次 = Runge 现象
> 均匀分布的节点做高次 Lagrange 插值时，在区间两端出现剧烈振荡（即使原函数光滑）。这是插值节点选择的问题——用 Chebyshev 节点可避免。

> [!warning] 分母可能极小导致数值问题
> 当节点间距很密时，$\prod_{j\neq i}(x_i-x_j)$ 会很小——除法放大舍入误差。Lagrange 公式的直接实现不是数值最优的。

## 相关概念

- [[01_Knowledge/插值与拟合]]
- [[01_Knowledge/数值稳定性]]
- [[01_Knowledge/Newton插值(差商)]]
- [[01_Knowledge/Chebyshev插值]]

## 习题

- [[03_Sources/Courses/归档/数值分析/习题库/07-插值法/README|第7章习题库]]
