---
title: QR分解求最小二乘
type: 知识点
subject: 数值分析
source:
  - 课程/数值分析/知识点解析梳理/08-数据拟合与最小二乘-知识梳理.md
topics:
  - QR分解
  - 最小二乘
  - 数值稳定性
  - Householder变换
---

# QR分解求最小二乘

## 一句话

用 QR 分解代替法方程——$\min\|Rx-Q^T b\|$ 更稳定，因为 $\kappa(R)=\kappa(A)$ 而非 $\kappa(A)^2$。

## 严格定义

设 $A=QR$（$Q\in\mathbb{R}^{m\times m}$ 正交，$R\in\mathbb{R}^{m\times n}$ 上三角）。

正交矩阵保 2-范数，故：

$$
\boxed{\|Ax-b\|_2=\|QRx-b\|_2=\|Rx-Q^T b\|_2}
$$

将 $R$ 和 $Q^T b$ 分块：

$$
R=\begin{pmatrix}R_1\\0\end{pmatrix},\; Q^T b=\begin{pmatrix}c_1\\c_2\end{pmatrix}
$$

其中 $R_1\in\mathbb{R}^{n\times n}$ 非奇异（$A$ 满秩时）。

**最小二乘解**：

$$
\boxed{R_1 x=c_1}
$$

残差范数为 $\|c_2\|_2$。

> [!important] $\kappa_2(R_1)=\kappa_2(A)$——不放大条件数！

## 推导：正交不变性

> [!proof]- 推导
> QR 分解 $A=QR$（$Q$ 正交→$Q^T Q=I$）。
>
> 由正交矩阵保 2-范数：
>
> $$
> \|Ax-b\|_2=\|Q^T(Ax-b)\|_2=\|Q^T QRx-Q^T b\|_2=\|Rx-Q^T b\|_2
> $$
>
> 分块后：
>
> $$
> \|Rx-Q^T b\|^2=\|R_1 x-c_1\|^2+\|c_2\|^2
> $$
>
> 第二项与 $x$ 无关→要使总范数最小，只需 $R_1 x=c_1$。
>
> **数值优势**：$R_1$ 直接来自 $A$ 的 QR 分解（条件数为 $\kappa(A)$），而非法方程（条件数 $\kappa^2(A)$）。

## 算法步骤

1. $A$ 的 QR 分解（推荐 Householder 或 Givens）
2. 计算 $c=Q^T b$
3. 取 $R_1$（$R$ 的前 $n$ 行）、$c_1$（$c$ 的前 $n$ 个分量）
4. 回代解 $R_1 x=c_1$
5. 残差 $\|r\|_2=\|c_2\|_2$

## 关键性质

| 性质 | 数值 |
|------|------|
| 条件数 | $\kappa(R_1)=\kappa(A)$ |
| vs 法方程 | $\kappa(R_1)\ll\kappa(A^T A)$（稳定得多） |
| 计算量 | $\frac{4}{3}n^3$（Householder QR） |
| vs 法方程计算量 | 约 2 倍（$\frac23 n^3$ vs $\frac43 n^3$） |
| 残差 | 直接可从 $c_2$ 获得 |

## 易错点

> [!warning] QR 分解选对算法
> Gram-Schmidt 正交化最直观但数值不稳定——要用 Householder 或修改版 Gram-Schmidt（MGS）。Householder 是生产级代码的标准选择。

> [!warning] QR 分解比法方程慢但值得
> QR 约是法方程计算量的 2 倍——对 $A$ 良态的问题似乎浪费，但对中等病态问题避免了 $10^{16}$ 的条件数平方——这个稳定性优势是无价的。

> [!warning] 残差从 $c_2$ 获取而非重算
> $\|r\|_2=\|c_2\|_2$ 是通过正交变换直接获取的——重算 $b-Ax$ 会引入额外的舍入误差。

## 相关概念

- [[概念/数值分析/QR分解]]
- [[概念/数值分析/数值稳定性]]
- [[知识点/数值分析/最小二乘法(法方程)]]

## 习题

- [[课程/数值分析/习题库/08-数据拟合与最小二乘/README|第8章习题库]]
