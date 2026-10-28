---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]]'
legacy_topics:
- Gershgorin圆盘定理
- 特征值定位
- 谱半径
- 正定性判定
tags:
- Gershgorin圆盘定理
- 谱半径
topics:
- '[[02_Maps/MOC-数值计算]]'
legacy_topic_links:
- '[[01_Knowledge/谱半径]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Gershgorin圆盘定理

## 一句话

每个特征值必落在某个 Gershgorin 圆盘内——无需计算就能定位特征值范围，快速判定正定性或可逆性。

## 严格定义

设 $A=(a_{ij})_{n\times n}$。对每个 $i=1,\ldots,n$，定义：

**圆盘**（行版本）：圆心 $a_{ii}$，半径 $R_i=\sum_{j\neq i}|a_{ij}|$。

$$
\boxed{D_i=\{z\in\mathbb{C}:|z-a_{ii}|\le R_i\}}
$$

**定理**：

1. $\sigma(A)\subseteq\bigcup_{i=1}^{n}D_i$（所有特征值落在圆盘的并集中）
2. 若 $k$ 个圆盘形成一个连通区域且与其他圆盘不相交，则该区域恰含 $k$ 个特征值

**列版本**（用 $A^T$）：圆心 $a_{ii}$，半径 $C_i=\sum_{j\neq i}|a_{ji}|$。

> [!important] 只需矩阵元素就能给出特征值范围——正定性（对角占优）、谱半径等可快速判断

## 推导：从 $Av=\lambda v$ 出发

> [!proof]- 推导
> 设 $(\lambda,v)$ 是 $A$ 的特征对，$\|v\|_\infty=1$，并设 $|v_i|=1$。
>
> 由特征方程 $(A-\lambda I)v=0$，考察第 $i$ 行：
>
> $$
> \sum_{j}a_{ij}v_j=\lambda v_i\quad\Rightarrow\quad(\lambda-a_{ii})v_i=\sum_{j\neq i}a_{ij}v_j
> $$
>
> 取模：
>
> $$
> |\lambda-a_{ii}|\le\sum_{j\neq i}|a_{ij}|\cdot|v_j|\le\sum_{j\neq i}|a_{ij}|=R_i
> $$
>
> 故 $\lambda\in D_i$——每个特征值都在某个圆盘中。

## 关键性质

| 性质 | 说明 |
|------|------|
| 特征值定位 | $\lambda\in\cup D_i$ |
| 圆盘互不相交 | 每个圆盘恰含 1 个特征值 |
| 对角占优判断 | 若 $|a_{ii}|>R_i\;\forall i\Rightarrow$ 所有圆盘不含原点 $\Rightarrow$ $A$ 可逆 |
| 正定性判断 | 对称 + 对角占优 + $a_{ii}>0\Rightarrow A$ 正定 |
| 谱半径估计 | $\rho(A)\le\max_i(|a_{ii}|+R_i)=\|A\|_\infty$ |

## 典型例题

> **题目**：用 Gershgorin 圆盘判定 $A=\begin{pmatrix}4&1&1\\1&3&0\\1&0&2\end{pmatrix}$ 的特征值范围和可逆性。

> [!example]- 解答
> **行圆盘**：
> - $D_1$：圆心 4，半径 $|1|+|1|=2$，区间 $[2,6]$
> - $D_2$：圆心 3，半径 $|1|+|0|=1$，区间 $[2,4]$
> - $D_3$：圆心 2，半径 $|1|+|0|=1$，区间 $[1,3]$
>
> 所有圆盘在正半轴（$\ge1$），严格不含 0→ $A$ 可逆。
>
> 圆盘 $D_1$ 与 $D_2$ 重叠，$D_2$ 与 $D_3$ 重叠→特征值确切割不明确。
>
> 谱半径 $\rho(A)\le\max(4+2,3+1,2+1)=6$。实际特征值约 $5.24,2.60,1.16$——全在估计范围内。
>
> **点评**：只看矩阵元素就能断言可逆性和特征值上下界——比求特征值快 $O(n^3)$ 倍。

## 易错点

> [!warning] 只是包含关系不是精确值
> Gershgorin 定理给出的是"圆盘包含特征值"——不能直接读出特征值的精确数值。圆盘之间重叠时，特征值的具体归属无法确定。

> [!warning] 行圆盘和列圆盘取交集最紧
> 特征值同时满足行版本和列版本的圆盘并集——$\sigma(A)\subseteq(\cup D_i^{\text{行}})\cap(\cup D_i^{\text{列}})$ 更紧。

> [!warning] 对角占优$\neq$ 正定
> 对角占优且 $a_{ii}>0$ 只能推断特征值*实部* >0（可逆），不能直接下结论正定——还需 $A$ 对称（或用各阶主子式判定）。

## 相关概念

- [[01_Knowledge/谱半径]]
- [[01_Knowledge/范数]]
- [[01_Knowledge/幂法]]

## 习题

- [[03_Sources/Courses/归档/数值分析/习题库/06-矩阵特征值的数值解法/README|第6章习题库]]
