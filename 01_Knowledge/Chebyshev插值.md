---
schema_version: 2
type: method
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理]]'
legacy_topics:
- Chebyshev插值
- 插值节点
- 最优逼近
- Runge现象
tags:
- Chebyshev插值
- Runge现象
topics:
- '[[02_Maps/MOC-数值计算]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Chebyshev插值

## 一句话

将插值节点选为 Chebyshev 多项式的零点——最小化最大误差（最优误差界），彻底避免 Runge 现象。

## 严格定义

**Chebyshev 多项式**（第一类）：

$$
\boxed{T_n(x)=\cos(n\cos^{-1}x)},\quad x\in[-1,1]
$$

递推式：$T_0=1,\;T_1=x,\;T_{n+1}=2xT_n-T_{n-1}$。

**Chebyshev 节点**（$T_{n+1}$ 的零点）：

$$
\boxed{x_k=\cos\frac{(2k+1)\pi}{2n+2}},\quad k=0,1,\ldots,n
$$

节点在 $[-1,1]$ 两端密集分布（不是均匀的）。

**误差界**（在 $[-1,1]$ 上 $n+1$ 个节点）：

$$
\boxed{\max_{x\in[-1,1]}|f(x)-P_n(x)|\le\frac{1}{2^n(n+1)!}\max_{\xi\in[-1,1]}|f^{(n+1)}(\xi)|}
$$

> [!important] Chebyshev 节点使 $\max\prod|x-x_i|$ 最小化——将 Runge 现象的产生根源（乘积最大项）降到最低

## 推导：最小化 $\|\prod(x-x_i)\|_\infty$

> [!proof]- 推导
> 插值余项主导因子为 $\prod_{i=0}^{n}|x-x_i|$。在所有首一多项式 $x^{n+1}+\cdots$ 中，$T_{n+1}(x)/2^n$ 在 $[-1,1]$ 上的最大绝对值最小。
>
> 将 $T_{n+1}$ 的零点作为插值节点（此时 $\prod(x-x_i)=T_{n+1}(x)/2^n$），恰好实现余项因子的最小化。
>
> 对一般区间 $[a,b]$，需做线性变换：
>
> $$
> x_k'=\frac{a+b}{2}+\frac{b-a}{2}\cos\frac{(2k+1)\pi}{2n+2}
> $$

## 算法步骤

1. 区间映射：$x\in[a,b]\mapsto t=\frac{2x-a-b}{b-a}\in[-1,1]$
2. 计算 Chebyshev 节点 $t_k=\cos\frac{(2k+1)\pi}{2n+2}$
3. 映射回原区间 $x_k=\frac{a+b}{2}+\frac{b-a}{2}t_k$
4. 计算 $f(x_k)$，用 Lagrange 或 Newton 构造插值多项式

## 关键性质

| 性质 | 数值 |
|------|------|
| 节点分布 | $[-1,1]$ 两端密集 |
| 误差上界 | $\frac{1}{2^n(n+1)!}\max|f^{(n+1)}|$ |
| Runge 现象 | 避免 |
| 需要函数值 | 在 Chebyshev 节点处 |
| 一般区间 | 需线性变换映射 |

## 易错点

> [!warning] 节点仅在 $[-1,1]$ 上定义
> 对一般区间 $[a,b]$ 必须做线性变换 $x_k=\frac{a+b}{2}+\frac{b-a}{2}t_k$——直接用 $[-1,1]$ 的节点在 $[a,b]$ 上毫无意义。

> [!warning] Chebyshev 节点≠均匀节点
> 均匀节点在区间中点比两端密，而 Chebyshev 节点恰恰相反（两端密）——这是压制 Runge 现象的关键。

> [!warning] 需要能在 Chebyshev 节点处计算函数值
> Chebyshev 节点的纵坐标不是有理数——若 $f(x)$ 只能通过实验/离散数据获得（而非公式），Chebyshev 插值不可行。

## 相关概念

- [[01_Knowledge/插值与拟合]]
- [[01_Knowledge/数值稳定性]]
- [[01_Knowledge/Lagrange插值]]

## 习题

- [[03_Sources/Courses/归档/数值分析/习题库/07-插值法/README|第7章习题库]]
