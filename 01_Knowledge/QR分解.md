---
schema_version: 2
type: concept
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]]'
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/08-数据拟合与最小二乘-知识梳理]]'
- '[[03_Sources/Courses/归档/数值分析/作业/06-矩阵特征值的数值解法/习题6.2]]'
legacy_topics:
- QR分解
- 正交矩阵
- Gram-Schmidt
- Householder
- QR算法
tags:
- QR分解
- 正交矩阵
- Gram-Schmidt
- Householder变换
- QR算法
topics:
- '[[02_Maps/MOC-数值计算]]'
- '[[02_Maps/MOC-数值分析]]'
time: '2026-08-31T11:44:20+08:00'
aliases: []
legacy_status: 已整理
---

# QR分解

## 一句话

$A=QR$（$Q$ 正交保长度，$R$ 上三角）——QR 分解是特征值 QR 算法的基础，也是最小二乘问题的稳定解法（比法方程更优）。

## 严格定义

对任意 $A \in \mathbb{R}^{m \times n}$（$m \geq n$），存在**QR 分解**：

$$A = QR$$

其中：
- $Q \in \mathbb{R}^{m \times m}$ 是**正交矩阵**（$Q^T Q = I$）
- $R \in \mathbb{R}^{m \times n}$ 是**上三角矩阵**（$R = \begin{bmatrix} R_1 \\ 0 \end{bmatrix}$，$R_1$ 为 $n \times n$ 上三角）

正交矩阵保长度：$\|Qx\|_2 = \|x\|_2$（保 2-范数），$\operatorname{cond}_2(Q)=1$。

计算方式：
- **经典 Gram-Schmidt**：直观但数值不稳定（正交性因舍入误差快速退化）
- **修正 Gram-Schmidt**：改进正交性，但仍不如 Householder
- **Householder 反射子**：$H = I - 2vv^T$（$v$ 为单位向量），最稳定的 QR 分解方法

> [!important] QR 分解解最小二乘 $\min\|Ax-b\|_2$ 只需解 $R_1 x = Q_1^T b$——避免了法方程 $\operatorname{cond}(A^T A) = [\operatorname{cond}(A)]^2$ 的条件数放大问题。计算量虽比法方程大，但稳定性远优于法方程。

## 由来与作用

- QR 算法（Francis, 1961; Kublanovskaya, 1961）是计算所有特征值的标准方法——通过反复 QR 分解实现矩阵的 Schur 型
- 最小二乘的标准解法：Householder QR 是求解 $\min\|Ax-b\|$ 的最稳定通用方法
- 在数值分析中的核心优势：正交变换保条件数（$\operatorname{cond}(QA)=\operatorname{cond}(A)$），不引入额外误差放大
- 关键性质：QR 分解对列满秩矩阵唯一（若要求 $R$ 的对角元为正）

## 相关概念

- [[01_Knowledge/范数]]
- [[01_Knowledge/对称正定矩阵]]
- [[01_Knowledge/数值稳定性]]
- [[01_Knowledge/插值与拟合]]

## 与投影和拟合的联系

[[01_Knowledge/QR分解求最小二乘]] 用正交变换把拟合问题化为三角方程；其几何核心是向列空间作正交投影。[[01_Knowledge/Hilbert空间正交基与Parseval等式]] 将同样的正交展开与投影思想用于函数空间，有限维矩阵情形和无限维函数情形要分别检查维数与完备性条件。


## 2026-11-08 来源复核补充

完全QR的Q为$m\times m$正交阵；薄QR的Q1只有n列，满足$Q_1^TQ_1=I_n$。源3×2例的两列$q_1=(-2,-1,2)^T/3$、$q_2=(-2,2,-1)^T/3$，可补$q_3=(1,2,2)^T/3$，R为首两行$(6,-3),(0,9)$及末行零。检验$Q^TQ=I$与$QR=A$；补齐列可变，因此满列秩且R对角正只使薄QR唯一，不能声称所有完全Q都唯一。
