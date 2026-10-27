---
title: 考题-01 - 多元函数梯度、Hessian、Jacobian与方向导数
subject: 最优化方法
chapter: 5
section: 微积分基础
source: 复习纲要补充
status: 已校对
type: 考题
topics:
  - 梯度
  - Hessian矩阵
  - Jacobian矩阵
  - 方向导数
  - 向量值函数求导
tags:
- 梯度
- Hessian矩阵
- Jacobian矩阵
- 方向导数
---

# 考题 01

已知标量函数和向量值函数：

$$f(x_1, x_2, x_3) = x_1^2 e^{x_2} + x_2 \ln(1 + x_3^2)$$

$$g(x_1, x_2, x_3) = \begin{bmatrix} x_1 x_2 \\ x_2^2 + x_3 \end{bmatrix}$$

给定方向 $d = [1, -1, 2]^\top$ 和点 $x_0 = [1, 0, 1]^\top$。

**(a)** 计算 $f$ 在 $x_0$ 处的梯度 $\nabla f(x_0)$。

**(b)** 计算 $f$ 在 $x_0$ 处的 Hessian 矩阵 $\nabla^2 f(x_0)$。

**(c)** 计算 $g$ 在 $x_0$ 处的 Jacobian 矩阵 $Dg(x_0)$。

**(d)** 计算 $f$ 在 $x_0$ 处沿方向 $d$ 的方向导数 $\frac{\partial f}{\partial d}\big|_{x_0}$。

---

## 💡 提示

> [!hint]- 点击展开提示
> - (a) 求梯度时逐分量求偏导。注意 $\frac{\partial}{\partial x_3}\ln(1+x_3^2) = \frac{2x_3}{1+x_3^2}$。
> - (b) Hessian 是梯度的 Jacobian，即对梯度每个分量再求一次偏导。注意 Hessian 的对称性可作为检查依据。
> - (c) Jacobian 矩阵的行对应 $g$ 的分量，列对应 $x$ 的分量（$Dg_{ij} = \frac{\partial g_i}{\partial x_j}$）。
> - (d) 方向导数 $\frac{\partial f}{\partial d} = \nabla f^\top \cdot d$（使用给定的 $d$ 不做归一化）。

---

## 📝 详细解析

> [!solution]- 点击展开详细解析
> ### (a) 梯度 $\nabla f(x_0)$
>
> 逐分量求偏导数：
>
> $$\begin{aligned}
> \frac{\partial f}{\partial x_1} &= 2x_1 e^{x_2} \\[4pt]
> \frac{\partial f}{\partial x_2} &= x_1^2 e^{x_2} + \ln(1 + x_3^2) \\[4pt]
> \frac{\partial f}{\partial x_3} &= x_2 \cdot \frac{2x_3}{1 + x_3^2}
> \end{aligned}$$
>
> 代入 $x_0 = [1, 0, 1]^\top$：
>
> $$\begin{aligned}
> \left.\frac{\partial f}{\partial x_1}\right|_{x_0} &= 2 \cdot 1 \cdot e^0 = 2 \\[4pt]
> \left.\frac{\partial f}{\partial x_2}\right|_{x_0} &= 1^2 \cdot e^0 + \ln(1 + 1^2) = 1 + \ln 2 \\[4pt]
> \left.\frac{\partial f}{\partial x_3}\right|_{x_0} &= 0 \cdot \frac{2}{1 + 1} = 0
> \end{aligned}$$
>
> $$\nabla f(x_0) = \begin{bmatrix} 2 \\ 1 + \ln 2 \\ 0 \end{bmatrix}$$
>
> ### (b) Hessian 矩阵 $\nabla^2 f(x_0)$
>
> 对梯度的每个分量再求偏导：
>
> $$\begin{aligned}
> \frac{\partial^2 f}{\partial x_1^2} &= 2e^{x_2} &
> \frac{\partial^2 f}{\partial x_1 \partial x_2} &= 2x_1 e^{x_2} &
> \frac{\partial^2 f}{\partial x_1 \partial x_3} &= 0 \\[4pt]
> \frac{\partial^2 f}{\partial x_2 \partial x_1} &= 2x_1 e^{x_2} &
> \frac{\partial^2 f}{\partial x_2^2} &= x_1^2 e^{x_2} &
> \frac{\partial^2 f}{\partial x_2 \partial x_3} &= \frac{2x_3}{1 + x_3^2} \\[4pt]
> \frac{\partial^2 f}{\partial x_3 \partial x_1} &= 0 &
> \frac{\partial^2 f}{\partial x_3 \partial x_2} &= \frac{2x_3}{1 + x_3^2} &
> \frac{\partial^2 f}{\partial x_3^2} &= x_2 \cdot \frac{2(1 - x_3^2)}{(1 + x_3^2)^2}
> \end{aligned}$$
>
> 代入 $x_0 = [1, 0, 1]^\top$：
>
> $$e^{x_2}\big|_{x_0} = e^0 = 1,\quad \ln(1+x_3^2)\big|_{x_0} = \ln 2$$
>
> $$\nabla^2 f(x_0) = \begin{bmatrix}
> 2 & 2 & 0 \\
> 2 & 1 & 1 \\
> 0 & 1 & 0
> \end{bmatrix}$$
>
> 检验：矩阵对称（$\frac{\partial^2 f}{\partial x_2 \partial x_3} = \frac{\partial^2 f}{\partial x_3 \partial x_2} = 1$），符合 Schwartz 定理。
>
> ### (c) Jacobian 矩阵 $Dg(x_0)$
>
> $g: \mathbb{R}^3 \to \mathbb{R}^2$，Jacobian 为 $2 \times 3$ 矩阵：
>
> $$Dg(x) = \begin{bmatrix}
> \frac{\partial g_1}{\partial x_1} & \frac{\partial g_1}{\partial x_2} & \frac{\partial g_1}{\partial x_3} \\[6pt]
> \frac{\partial g_2}{\partial x_1} & \frac{\partial g_2}{\partial x_2} & \frac{\partial g_2}{\partial x_3}
> \end{bmatrix} = \begin{bmatrix}
> x_2 & x_1 & 0 \\
> 0 & 2x_2 & 1
> \end{bmatrix}$$
>
> 代入 $x_0 = [1, 0, 1]^\top$：
>
> $$Dg(x_0) = \begin{bmatrix}
> 0 & 1 & 0 \\
> 0 & 0 & 1
> \end{bmatrix}$$
>
> ### (d) 方向导数 $\frac{\partial f}{\partial d}\big|_{x_0}$
>
> 方向导数定义为梯度与方向的点积（此处 $d$ 即为给定的方向向量，无需归一化）：
>
> $$\begin{aligned}
> \left.\frac{\partial f}{\partial d}\right|_{x_0} &= \nabla f(x_0)^\top d \\
> &= \begin{bmatrix} 2 & 1+\ln 2 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix} \\
> &= 2 \times 1 + (1+\ln 2) \times (-1) + 0 \times 2 \\
> &= 2 - 1 - \ln 2 \\
> &= 1 - \ln 2
> \end{aligned}$$
>
> 若要求沿单位方向的方向导数，则需除以 $\|d\|_2 = \sqrt{1^2 + (-1)^2 + 2^2} = \sqrt{6}$，结果为 $\frac{1 - \ln 2}{\sqrt{6}}$。本课程中方向导数一般指 $\nabla f^\top d$ 形式。$\square$
>
> **点评：** 本题综合考察了最优化方法中最基础的微积分计算技能——梯度、Hessian、Jacobian 和方向导数是 FONC/SONC 判断、Taylor 展开、梯度下降法等后续内容的计算基础。其中 Hessian 矩阵的对称性（混合偏导可交换）是重要的检查手段；Jacobian 矩阵的行列维度须与映射的输入输出维度一致。注意 $\ln(1+x_3^2)$ 在 $x_3=1$ 时不是特殊值，需保留 $\ln 2$。

---

## 相关知识点

- [[05-微积分基础]] — 梯度、Hessian、Jacobian、方向导数定义
- [[05-微积分基础#Jacobian矩阵与Hessian矩阵|Jacobian 与 Hessian]]
- [[../知识点解析梳理/05-微积分基础-知识梳理|第5章 知识梳理]] — 多元函数微分学方法总结
- [[../04-几何概念/考题-判断凸集|判断凸集]] — 凸集判断题（章节关联）
