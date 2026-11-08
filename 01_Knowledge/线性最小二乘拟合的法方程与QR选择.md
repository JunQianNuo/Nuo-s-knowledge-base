---
schema_version: 2
type: method
time: '2026-08-31T11:44:20+08:00'
source:
- '[[03_Sources/Reviews/归档/数值分析/复习/VII-数据拟合与最小二乘]]'
- '[[03_Sources/Courses/归档/数值分析/作业/08-数据拟合与最小二乘/习题8.1]]'
- '[[03_Sources/Courses/归档/数值分析/作业/08-数据拟合与最小二乘/习题8.2]]'
topics:
- '[[02_Maps/MOC-数值计算]]'
- '[[02_Maps/MOC-数值分析]]'
aliases:
- 最小二乘拟合流程(法方程vsQR)
tags:
- 最小二乘拟合流程-法方程与QR
related:
- '[[01_Knowledge/最小二乘法(法方程)]]'
- '[[01_Knowledge/QR分解求最小二乘]]'
---

# 线性最小二乘拟合的法方程与QR选择

## 适用场景
给定含噪声的观测数据 $(x_i,y_i)$，求最佳拟合曲线 $\phi(x;c_1,\ldots,c_m)$，需在法方程（快速）和 QR（稳定）间选择。

## 核心公式/步骤

1. 构造设计矩阵 $A$（$n\times m$，$n>m$）和观测向量 $\mathbf{b}$
2. 先检查 $\operatorname{rank}(A)=m$；下列唯一解及可逆三角方程均要求满列秩。若秩亏，用带列主元 QR 或 SVD，需最小范数解时使用伪逆。再判断矩阵条件：
   - **法方程法**（条件好时）：$\boxed{A^T A\mathbf{c}=A^T\mathbf{b}}$，解出 $\mathbf{c}$
   - **QR 法**（条件差时）：QR 分解 $\boxed{A=QR=Q\begin{bmatrix}R_1\\0\end{bmatrix}}$，解 $\boxed{R_1\mathbf{c}=Q_1^T\mathbf{b}}$
3. 法方程条件数被平方放大：$\boxed{\kappa_2(A^T A)=\kappa_2(A)^2}$，所以 QR 更稳定
4. 拟合残差：$\boxed{\|\mathbf{r}\|_2^2=\|\mathbf{b}-A\mathbf{c}\|_2^2}$

```mermaid
flowchart TD
    A["构造设计矩阵 A 和观测向量 b"] --> B["先查满列秩 秩亏用 SVD 否则估计 κ2(A)"]
    B --> C{"cond(A) 适中 ?\n（结合机器精度和误差要求）"}
    C -->|"是"| D["法方程法\nA^T A c = A^T b"]
    C -->|"否（病态）"| E["QR 分解法\nA = QR"]
    D --> F["Cholesky 解 A^T A c = A^T b"]
    E --> G["解 R1 c = Q1^T b"]
    F --> H["输出拟合参数 c"]
    G --> H
    H --> I["计算残差 ||b - A c||²"]
```

## 典型例题

> **题目**：用最小二乘法拟合直线 $y=c_1+c_2 x$ 到数据 $(1,2),(2,3),(3,4),(4,5)$。

> [!example]- 解答
> $A=\begin{bmatrix}1&1\\1&2\\1&3\\1&4\end{bmatrix}$, $b=[2,3,4,5]^T$
> 法方程 $A^T A=\begin{bmatrix}4&10\\10&30\end{bmatrix}$, $A^T b=[14,40]^T$
> 解 $\begin{bmatrix}4&10\\10&30\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix}=\begin{bmatrix}14\\40\end{bmatrix}$ → $c_1=1$, $c_2=1$
> 拟合直线 $y=1+x$，残差为零（数据共线）。点评：本题数据完美共线，实际数据需比较两种方法。

## 链接的知识点
- [[01_Knowledge/最小二乘法(法方程)]]
- [[01_Knowledge/QR分解求最小二乘]]

## 链接的习题
- [[03_Sources/Courses/归档/数值分析/习题库/08-数据拟合与最小二乘/README|第8章习题库]]


## 2026-11-08 来源复核补充

周期模型按基函数1、cos、sin逐行构造设计矩阵，等距一周期的离散正交性可直接给薄QR：$Q_1$为A三列分别除以$\sqrt6,\sqrt3,\sqrt3$，$R_1=\mathrm{diag}(\sqrt6,\sqrt3,\sqrt3)$。以$R_1c=Q_1^Tb$仍得$(1/2,2/3,0)$。

3×2拟合例复用完全QR时，$Q^Tb=(-5,4,7)^T$，R1为$(6,-3；0,9)$，回代$x=(-11/18,4/9)$，剩余分量7直接给残差范数；独立检验$A^T(b-Ax)=0$。
