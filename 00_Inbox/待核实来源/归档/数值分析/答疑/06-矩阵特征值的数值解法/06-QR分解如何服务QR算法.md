---
subject:
- 数值分析
chapter: 6
source_context:
- file: 06-矩阵特征值的数值解法-知识梳理.md
  section: 5.4 为什么 QR 分解能服务 QR 算法？
related_notes:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]]'
tags:
- QR分解
- QR算法
- 正交相似变换
aliases:
- 第06章 答疑 — QR分解如何服务QR算法
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- QR分解
- QR算法
- 正交相似变换
source: []
status: not done
legacy_type: review
legacy_schema_version: 2
migration_reason: Missing traceable source in legacy source note
---

# QR 分解如何服务 QR 算法

> 问题：$A_{j+1}=R_jQ_j=Q_j^T A_j Q_j$ 到底是什么意思？特征值不变我能理解，但为什么拆开再拼回去、左下角就会变成 $0$？

> 来源：[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] 5.4 节

---

## 两件独立的事

### 第一件：特征值为什么不变

因为 $A_{j+1}=Q_j^T A_j Q_j$ 是**正交相似变换**。相似矩阵有相同特征多项式——对任意方阵 $A$、可逆矩阵 $P$、任意 $\lambda$：

$$\det(P^{-1}AP - \lambda I)=\det(P^{-1})\det(A-\lambda I)\det(P)=\det(A-\lambda I)$$

这里 $P=Q_j$ 且 $Q_j^{-1}=Q_j^T$，所以 $Q_j^T A_j Q_j$ 和 $A_j$ 特征值相同。

### 第二件：为什么形状会变

这才是核心。用具体例子看——跑一轮 QR 迭代到底发生了什么。

$$A_0 = \begin{pmatrix}4 & 3 \\ 3 & 2\end{pmatrix},\quad \lambda_1\approx5.541,\;\lambda_2\approx0.459$$

**QR 分解**（Gram-Schmidt）：

$$Q_0 = \begin{pmatrix}0.8 & 0.6 \\ 0.6 & -0.8\end{pmatrix},\quad R_0 = \begin{pmatrix}5 & 3.6 \\ 0 & 0.2\end{pmatrix}$$

**重组** $A_1 = R_0 Q_0$：

$$A_1 = \begin{pmatrix}5 & 3.6 \\ 0 & 0.2\end{pmatrix}\begin{pmatrix}0.8 & 0.6 \\ 0.6 & -0.8\end{pmatrix}
= \begin{pmatrix}6.16 & 0.12 \\ 0.12 & -0.16\end{pmatrix}$$

**对比**：

$$A_0 = \begin{pmatrix}4 & 3 \\ \boxed{3} & 2\end{pmatrix}
\quad\longrightarrow\quad
A_1 = \begin{pmatrix}6.16 & 0.12 \\ \boxed{0.12} & -0.16\end{pmatrix}$$

左下角：**$3 \to 0.12$**，缩小了约 25 倍。对角元向真特征值靠拢。

再迭代一轮，左下角继续缩小。

## 直观理解：QR 迭代 = "把矩阵旋正"

每轮 QR 迭代等价于**换一个正交基底再看同一个线性变换**。这个新基底的选择不是任意的——QR 分解的 $Q$ 是基于当前矩阵列向量正交化得到的，它天然地"偏袒"按特征值模大小排序的方向。

反复换基底 $\to$ 矩阵逐渐被"挤压"成上三角 $\to$ 对角元 = 特征值。

## 和图解

```
A₀ = [4  3]    QR分解    拆成Q₀R₀    重组          [6.16  0.12]
     [3  2]  ──────────→            ───────→ A₁ =  [0.12 -0.16]
                 ↑                                ↓
              正交化抓方向                     逆序乘回去
              （相当于换基底）                  （在新基底下看A）
```

每步做的是同一个操作的循环——拆开→重组→拆开→重组。就像反复拧魔方，每一步都是合法转动（不改变魔方状态集），但目标是把颜色归到同一面上。

---

## 相关链接

- [[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] — QR 算法
- [[00_Inbox/待核实来源/归档/数值分析/答疑/06-矩阵特征值的数值解法/06-幂法到QR算法的演进]]
