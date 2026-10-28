---
schema_version: 2
type: method
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理]]'
legacy_topics:
- Newton-Cotes公式
- 数值积分
- 代数精度
- 梯形公式
- Simpson公式
tags:
- Newton-Cotes公式
- 数值积分
- 代数精度
- 梯形公式
topics:
- '[[02_Maps/MOC-数值计算]]'
legacy_topic_links:
- '[[01_Knowledge/代数精度]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Newton-Cotes公式

## 一句话

等距节点 + 内插求积——梯形（$n=1$）、Simpson（$n=2$）、Cotes（$n=4$），最简单的求积公式但有 Runge 式缺陷。

## 严格定义

将 $[a,b]$ 等分 $n$ 份，节点 $x_k=a+kh$，$h=(b-a)/n$。

**Newton-Cotes 求积公式**：

$$
\boxed{\int_a^b f(x)dx\approx\sum_{k=0}^{n}A_k f(x_k)}
$$

其中系数 $A_k=\int_a^b \ell_k(x)dx$（$\ell_k$ 为 Lagrange 基函数）。

**常用公式**（$n=1,2,4$）：

- 梯形（$n=1$）：$\int_a^b f\approx\frac{h}{2}[f(a)+f(b)]$，精度=1
- Simpson（$n=2$）：$\int_a^b f\approx\frac{h}{3}[f(a)+4f(\frac{a+b}{2})+f(b)]$，精度=3
- Cotes（$n=4$）：$\int_a^b f\approx\frac{2h}{45}[7f_0+32f_1+12f_2+32f_3+7f_4]$，精度=5

> [!important] 偶数阶 NC 精度额外+1（Simpson $n=2$ 精度为 3 而非 2）；$n\ge8$ 时系数有负值→数值不稳定

## 推导：Lagrange 内插求积

> [!proof]- 推导
> 用过 $n+1$ 个等距节点的 Lagrange 插值多项式 $P_n(x)$ 近似 $f(x)$：
>
> $$
> \int_a^b f(x)dx\approx\int_a^b P_n(x)dx=\int_a^b\sum_{k=0}^n f(x_k)\ell_k(x)dx=\sum_{k=0}^n\left(\int_a^b\ell_k(x)dx\right)f(x_k)
> $$
>
> 系数 $A_k=\int_a^b\ell_k(x)dx$ 只依赖于节点分布（不依赖 $f$），可预制。
>
> **误差公式**（$n$ 为偶数时精度+1）：$\int_a^b f-P_n=\frac{h^{n+3}f^{(n+2)}(\xi)}{(n+2)!}\int_0^n t^2(t-1)\cdots(t-n)dt$

## 算法步骤

1. 选择 NC 阶数 $n$（推荐 $n=1,2,4$）
2. 计算等距节点和对应函数值
3. 代入 NC 系数加权求和
4. 验证结果（特别是 $n\ge5$ 时检查系数是否出现负数）

## 关键性质

| 性质 | 数值 |
|------|------|
| 梯形（$n=1$） | 精度=1，$O(h^2)$ 局部误差 |
| Simpson（$n=2$） | 精度=3，$O(h^4)$ 局部误差 |
| Cotes（$n=4$） | 精度=5，$O(h^6)$ 局部误差 |
| $n\ge8$ | 系数出现负数→不稳定 |
| 优缺点 | 简单直观，但高阶不稳定 |

## 典型例题

> **题目**：对 $\int_0^1 e^x dx$（精确值 $e-1\approx1.718282$），分别用梯形、Simpson、Cotes 计算。

> [!example]- 解答
> **梯形**（$n=1$，$h=1$）：$T=\frac12[e^0+e^1]=1.859141$，误差 $0.141$。
>
> **Simpson**（$n=2$，$h=0.5$）：$S=\frac{0.5}{3}[1+4e^{0.5}+e^1]=1.718861$，误差 $0.00058$。
>
> **Cotes**（$n=4$，$h=0.25$）：$C=\frac{0.5}{45}[7\cdot1+32e^{0.25}+12e^{0.5}+32e^{0.75}+7e^1]$
>
> $=\frac{0.5}{45}[7+44.91+19.78+62.61+19.03]=1.718283$，误差 $10^{-6}$。
>
> **点评**：$n$ 从 1 到 4，误差从 $10^{-1}$ 降到 $10^{-6}$——"多算几个点"在低阶 NC 中效果显著。

## 易错点

> [!warning] 高阶 NC 系数出现负数
> $n=8$ 时部分系数为负且绝对值大——正负抵消时极大舍入误差（类似于 Runge 现象在积分中的对应）。

> [!warning] 不要盲目追求高阶
> NC 阶数过高时节点数激增但精度不一定大幅提升——复化低阶（分段 Simpson）通常是更好的策略。

> [!warning] 奇偶阶精度差
> 偶数阶 NC 比奇数阶多一阶精度（这是余项积分中 $t$ 的奇偶性导致的）——因此 Simpson（$n=2$）比 $n=3$ 更常用。

## 相关概念

- [[01_Knowledge/代数精度]]
- [[01_Knowledge/插值与拟合]]
- [[01_Knowledge/复化求积法]]
- [[01_Knowledge/Gauss求积]]

## 习题

- [[03_Sources/Courses/归档/数值分析/习题库/09-数值积分与数值微分/README|第9章习题库]]
