---
title: 第06章 答疑 — QR算法中A_j与A的关系
subject: 数值分析
chapter: 6
type: 答疑
topics:
  - QR算法
  - 正交相似变换
source_context:
  - file: "06-矩阵特征值的数值解法-知识梳理.md"
    section: "6.2 QR 算法的标准形式"
related_notes:
  - "[[06-矩阵特征值的数值解法-知识梳理]]"
tags:
- QR算法
- 正交相似变换
---

# QR 算法中 $A_j$ 与 $A$ 的关系

> 问题：$A_j$ 和 $A$ 有什么关系？为什么特征值相同但形状在变？

> 来源：[[课程/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] 6.2 节

---

## 核心一句话

**$A_j$ 和 $A$ 是同一个线性变换在不同正交基底下的表示——特征值全同，但 $A_j$ 更靠近上三角。**

---

## 关系链

$$A = A_0 \xrightarrow{QR} A_1 \xrightarrow{QR} A_2 \xrightarrow{QR} \cdots \xrightarrow{QR} A_{\infty} \text{（上三角）}$$

每一步：$A_{j+1} = Q_j^T A_j Q_j$（正交相似变换）。

---

## 展开看

$$
\begin{aligned}
A_1 &= Q_0^T A Q_0 \\[2pt]
A_2 &= Q_1^T A_1 Q_1 = Q_1^T Q_0^T A Q_0 Q_1 = (Q_0 Q_1)^T A (Q_0 Q_1) \\[2pt]
A_j &= (Q_0 Q_1 \cdots Q_{j-1})^T \;A\; (Q_0 Q_1 \cdots Q_{j-1})
\end{aligned}
$$

所以 $A_j = \widehat{Q}_{j-1}^T A \,\widehat{Q}_{j-1}$，其中 $\widehat{Q}_{j-1}$ 是累积正交矩阵。

---

## 为什么特征值相同

$\widehat{Q}^T A \,\widehat{Q}$ 和 $A$ 是相似矩阵。相似矩阵有相同的特征多项式：

$$\det(\widehat{Q}^T A \,\widehat{Q} - \lambda I) = \det(\widehat{Q}^T) \det(A - \lambda I) \det(\widehat{Q}) = \det(A - \lambda I)$$

因为 $\det(\widehat{Q}^T)\det(\widehat{Q})=1$。

---

## 为什么形状在变

基底一直在变——每步 QR 分解构造出的 $Q_j$ 由当前 $A_j$ 的列向量正交化得到，天然"偏袒"按特征值大小排序的方向。越迭代，基底越接近特征向量基底，矩阵越接近上三角。

```
A₀: [4  3]       A₁: [6.16 0.12]      A∞: [5.541  0  ]
     [3  2]            [0.12 -0.16]          [  0   0.459]

  满矩阵              左下角在缩小              对角元=特征值
```

---

## 相关链接

- [[课程/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] — QR 算法
- [[课程/归档/数值分析/答疑/06-矩阵特征值的数值解法/06-幂法到QR算法的演进]]
