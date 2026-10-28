---
subject:
- 数值分析
chapter: 6
source_context:
- file: 06-矩阵特征值的数值解法-知识梳理.md
  line: 96
  text: 用这个 λ 做位移逆幂法，收敛速度变为立方
- file: 06-矩阵特征值的数值解法-知识梳理.md
  line: 100
  text: 对实对称矩阵，Rayleigh 商迭代的收敛是立方的
related_notes:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]]'
tags:
- Rayleigh商迭代
- 位移逆幂法
- 立方收敛
aliases:
- 第06章 答疑 — Rayleigh商迭代的本质与收敛
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- Rayleigh商迭代
- 位移逆幂法
- 立方收敛
source: []
status: not done
legacy_type: review
legacy_schema_version: 2
migration_reason: Missing traceable source in legacy source note
---

# Rayleigh 商迭代的本质与收敛速度

> 问题：Rayleigh 商迭代就是每步用 Rayleigh 商做位移的位移逆幂法？收敛为什么是立方不是平方？

> 来源：[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] §4

---

## 本质：确实就是动态位移的逆幂法

**Rayleigh 商迭代 = 每步用最新向量的 Rayleigh 商做位移的位移逆幂法。**

| | 普通位移逆幂法 | Rayleigh 商迭代 |
|------|------|------|
| 位移 $\mu$ | **固定**，事先选好 | **每步更新**：$\mu_k = x_k^T A x_k / x_k^T x_k$ |
| 收敛 | 线性，常数由 $\mu$ 离目标特征值多远决定 | 立方（对称时）/ 平方（非对称时） |

算法：

1. 有当前近似特征向量 $x_k$
2. 算 $\mu_k = x_k^T A x_k / x_k^T x_k$
3. 解 $(A - \mu_k I) y = x_k$（一步位移逆幂法）
4. 归一化 $x_{k+1} = y / \|y\|_2$，回到 2

---

## 收敛速度：线性 vs 平方 vs 立方

三个不同概念，容易混淆：

| 概念 | 收敛率 | 笔记位置 |
|------|:---:|------|
| **普通幂法**中向量方向收敛 | 线性：$e_{k+1} \approx \|\lambda_2/\lambda_1\| \cdot e_k$ | §3.1 |
| **普通幂法**中 Rayleigh 商估 $\lambda$ 的收敛 | **平方**：$\|\lambda_2/\lambda_1\|^2$ | — |
| **Rayleigh 商迭代**（全流程） | **立方**（对称）：$e_{k+1} \approx C e_k^3$ | §4 |

---

## 为什么是立方

Rayleigh 商有一个关键性质：在特征向量附近，它是**二阶平稳**的——$x$ 偏离真特征向量的误差是 $O(\varepsilon)$ 时，Rayleigh 商偏离真特征值的误差仅为 $O(\varepsilon^2)$。

然后拿这么精确的 $\mu$ 做位移逆幂法，逆幂法本身又是一阶放大——新向量的误差 = $O(\varepsilon^2 \times \varepsilon) = O(\varepsilon^3)$。

实际效果：

| 当前误差 | 下步误差 |
|:---:|:---:|
| $10^{-3}$ | $(10^{-3})^3 = 10^{-9}$ |
| $10^{-9}$ | $(10^{-9})^3 = 10^{-27}$（机器精度） |

两步就从 $10^{-3}$ 到机器精度。这就是"一步精确到机器精度"那句话的来源。

---

## 相关链接

- [[03_Sources/Reviews/归档/数值分析/知识点解析梳理/06-矩阵特征值的数值解法-知识梳理]] — §4 Rayleigh 商迭代
- [[00_Inbox/待核实来源/归档/数值分析/答疑/06-矩阵特征值的数值解法/06-幂法公式推导与收敛率]] — 幂法线性收敛
