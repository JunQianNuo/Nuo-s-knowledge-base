---
title: 第06章 答疑 — A_j为何落在前j个q张成的空间
subject: 数值分析
chapter: 6
type: 答疑
topics:
  - QR分解
  - Gram-Schmidt
  - 上三角
  - 张成空间
source_context:
  - file: "06-矩阵特征值的数值解法-知识梳理.md"
    line: 123
    text: "因为第 j 个原列向量 A_j 只由前 j 个正交方向表示"
related_notes:
  - "[[06-矩阵特征值的数值解法-知识梳理]]"
---

# $A_j$ 为何落在前 $j$ 个 $q$ 张成的空间中

> 问题：凭什么 $A_j$ 恰好能被 $q_1,\dots,q_j$ 线性表示，而不是所有 $n$ 个 $q$？

> 来源：[[课程/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] 5.1 节

---

## 这不是巧合——是 Gram-Schmidt 刻意保证的

Gram-Schmidt 最核心的不变量：

$$\text{span}\{q_1,\dots,q_j\} = \text{span}\{A_1,\dots,A_j\} \qquad (\forall j)$$

两个集合张成**完全同一个空间**。所以 $A_j$ 当然落在 $\text{span}\{q_1,\dots,q_j\}$ 里——它本身就是这个空间的生成元之一。

---

## 归纳法证明

**$j=1$**：$q_1 = A_1 / \|A_1\|$，$\text{span}\{q_1\} = \text{span}\{A_1\}$ ✓

**归纳假设**：$\text{span}\{q_1,\dots,q_{j-1}\} = \text{span}\{A_1,\dots,A_{j-1}\}$

**第 $j$ 步**：构造

$$y_j = A_j - \sum_{i=1}^{j-1} (q_i^T A_j) q_i$$

$$q_j = y_j / \|y_j\|_2$$

右边两项的方向：
- $A_j \in \text{span}\{A_1,\dots,A_j\}$（显然）
- $\sum(\cdots)q_i \in \text{span}\{q_1,\dots,q_{j-1}\} = \text{span}\{A_1,\dots,A_{j-1}\}$（归纳假设）

所以 $y_j \in \text{span}\{A_1,\dots,A_j\}$，从而 $\text{span}\{q_1,\dots,q_j\} \subseteq \text{span}\{A_1,\dots,A_j\}$。

**反过来**：$A_j = y_j + \sum_{i=1}^{j-1} (q_i^T A_j) q_i \in \text{span}\{q_1,\dots,q_j\}$

所以 $\text{span}\{A_1,\dots,A_j\} \subseteq \text{span}\{q_1,\dots,q_j\}$。两者相等 ✓

---

## 这就是 $R$ 上三角的根本原因

$A_j \in \text{span}\{q_1,\dots,q_j\}$ 意味着写成 $q$ 的线性组合时，$q_{j+1}$ 及以后的系数全为 $0$：

```
A₁ = r₁₁ q₁
A₂ = r₁₂ q₁ + r₂₂ q₂
A₃ = r₁₃ q₁ + r₂₃ q₂ + r₃₃ q₃
```

把每个 $A_j$ 的系数写成矩阵的列：

$$R = \begin{pmatrix}
r_{11} & r_{12} & r_{13}\\
0 & r_{22} & r_{23}\\
0 & 0 & r_{33}
\end{pmatrix}$$

从上往下看，第 $j+1$ 行开始全是 $0$——这就是上三角。

---

## 相关链接

- [[课程/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] — QR 分解
