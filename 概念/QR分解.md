---
title: QR分解
type: 概念
source:
- "[[课程/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]]"
- "[[课程/归档/数值分析/知识点解析梳理/08-数据拟合与最小二乘-知识梳理]]"
topics:
- QR分解
- 正交矩阵
- Gram-Schmidt
- Householder
- QR算法
status: 已整理
tags:
- QR分解
- 正交矩阵
- Gram-Schmidt
- Householder变换
- QR算法
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

- [[概念/范数]]
- [[概念/对称正定矩阵]]
- [[概念/数值稳定性]]
- [[概念/插值与拟合]]

## 与投影和拟合的联系

[[方法/QR分解求最小二乘]] 用正交变换把拟合问题化为三角方程；其几何核心是向列空间作正交投影。[[知识点/正交基与Fourier展开]] 将同样的正交展开与投影思想用于函数空间，有限维矩阵情形和无限维函数情形要分别检查维数与完备性条件。
