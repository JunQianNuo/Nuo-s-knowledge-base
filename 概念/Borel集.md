---
title: Borel集
type: 概念
source:
- "[[课程/归档/实变函数/知识点解析梳理/01-集合论与点集拓扑基础-知识梳理]]"
topics:
- Borel集
- Borel $\sigma$ 代数
- Borel分层
- $G_\delta$ 集
- $F_\sigma$ 集
- Lebesgue可测集
exam: 不考
status: 已整理
tags:
- Borel集
- Lebesgue可测集
- Gδ集
- Fσ集
---

# Borel集

## 一句话

Borel 集是从开集出发、通过可数次交并补运算所能生成的一切集合——它是 Lebesgue 可测集的"构造性内核"，也是概率论中随机变量的定义域。

## 严格定义

设 $\mathcal{O}$ 为 $\mathbb{R}^n$ 中全体开集构成的集族。由 $\mathcal{O}$ 生成的**最小 $\sigma$ 代数**称为 **Borel $\sigma$ 代数**，记作 $\mathcal{B}(\mathbb{R}^n)$ 或 $\mathcal{B}^n$。$\mathcal{B}^n$ 中的元素称为 **Borel 集**。

具体地，$\mathcal{B}^n$ 是满足以下条件的最小集族：

1. $\mathcal{O} \subset \mathcal{B}^n$（包含全体开集）；
2. 对可数并封闭：$A_k \in \mathcal{B}^n \Rightarrow \bigcup_{k=1}^{\infty} A_k \in \mathcal{B}^n$；
3. 对补集封闭：$A \in \mathcal{B}^n \Rightarrow \mathbb{R}^n \setminus A \in \mathcal{B}^n$。

**Borel 分层**（Borel hierarchy）——按构造复杂度递进：

| 层级 | 记号 | 定义 |
|:--|:--|:--|
| $G_\delta$ 集 | $\mathbf{\Pi}_2^0$ | 可数个开集的交 $\bigcap_{k=1}^{\infty} G_k$，$G_k$ 开 |
| $F_\sigma$ 集 | $\mathbf{\Sigma}_2^0$ | 可数个闭集的并 $\bigcup_{k=1}^{\infty} F_k$，$F_k$ 闭 |
| $G_{\delta\sigma}$ 集 | $\mathbf{\Sigma}_3^0$ | 可数个 $G_\delta$ 集的并 |
| $F_{\sigma\delta}$ 集 | $\mathbf{\Pi}_3^0$ | 可数个 $F_\sigma$ 集的交 |
| $\cdots$ | | 可超限归纳至 $\omega_1$ 层 |

$G_\delta$ 与 $F_\sigma$ 互为对偶（取余集互换）。例如：$\mathbb{Q}$ 是 $F_\sigma$ 集（单点可数个的并），$\mathbb{R} \setminus \mathbb{Q}$ 是 $G_\delta$ 集。

**等价生成族**：$\mathcal{B}^n$ 也可由以下任一集族生成（结果相同）——

- 全体闭集；
- 全体半开区间 $\prod_{i=1}^{n}[a_i, b_i)$；
- 全体紧集；
- 全体开球。

> [!important] 核心要点
> - **Borel 集是"可构造的"**：每一层 Borel 集都可通过不超过可数次交并补从开/闭集得到。这与"选择公理构造的非构造性集合"形成根本对立。
> - **$\mathcal{B} \subset \mathcal{L}$ 且严格包含**：所有 Borel 集都是 Lebesgue 可测集，但存在 Lebesgue 可测而**非 Borel** 的集合（例如 Cantor 集的某些子集）。也就是说，$\mathcal{B} \subsetneq \mathcal{L}$。
> - **$\mathcal{L}$ 是 $\mathcal{B}$ 的完备化**：Lebesgue 可测集 = Borel 集 $\cup$ 零测集的子集。任何 Lebesgue 可测集 $A$ 可表为 $A = B \cup N$，其中 $B \in \mathcal{B}$ 且 $N$ 是零测集。
> - **$\mathcal{B}$ 与拓扑深度绑定**：Borel $\sigma$ 代数是拓扑空间上最自然的 $\sigma$ 代数——它仅用拓扑结构（开集）定义，不依赖测度。
> - **概率论基础**：随机变量 $X: (\Omega, \mathcal{F}) \to \mathbb{R}$ 定义为 $\mathcal{F}/\mathcal{B}(\mathbb{R})$-可测函数；事件 $\{X \in B\}$（$B \in \mathcal{B}$）是随机变量分布的核心语言。

## 由来与作用

**历史背景**：Emile Borel 在 1898 年的测度论工作中首次系统研究了从开集出发构造的集族。Borel $\sigma$ 代数的概念后来由 Lebesgue（1902）和 Hausdorff 等人完善，成为现代测度论和概率论的骨架语言。

**解决的问题**：并非所有 $\mathbb{R}^n$ 的子集都能被赋予"合理的"测度（Vitali 集是不可测的经典例子）。Borel 集的构造方式确保所有 Borel 集都能被精确定义测度，且这个测度与我们的几何直觉一致。更进一步，Borel $\sigma$ 代数抓住了"通过可数运算可构造的所有集合"——它既足够丰富（包含几乎所有日常遇到的集合），又足够约束（排除了选择公理带来的病态构造）。

**在实变函数中的角色**：

- **测度论的语言基础**：测度是定义在 $\sigma$ 代数上的集函数。Borel $\sigma$ 代数是 $\mathbb{R}^n$ 上的**典范 $\sigma$ 代数**——Caratheodory 外测度构造的起点正是开覆盖，自然地引向 Borel 集。
- **连通拓扑与测度的桥梁**：Borel $\sigma$ 代数仅依赖拓扑（开集）定义，而测度是在它上面定义的集函数。这一框架使拓扑结构（开/闭/紧/连续）与测度结构（可测/测度/积分）得以对话——这正是 Lusin 定理和 Egorov 定理的哲学根基。
- **完备化的必要性**：$\mathcal{B} \subsetneq \mathcal{L}$ 的事实说明"构造性"（Borel）不足以覆盖所有可测集。Lebesgue 测度的完备化（添加零测集的子集）是技术上必要的——它保证了 a.e. 收敛的极限仍是可测的。
- **概率论的核心概念**：随机变量、分布函数、期望——所有这些概念都依赖于 Borel $\sigma$ 代数。$(\mathbb{R}, \mathcal{B})$ 是概率论的"默认可测空间"。

**关键性质回顾**：对可数并/交/补/差封闭；对 Borel 可测函数的原像封闭（若 $f$ Borel 可测，则 $f^{-1}(B) \in \mathcal{B}$）；基数为 $\mathfrak{c}$（连续统）；包含所有开集、闭集、$G_\delta$ 集、$F_\sigma$ 集及其所有可数层级组合。

## 相关概念

- [[概念/零测集]] — $\mathcal{L}$ 是 $\mathcal{B}$ 的完备化：任何 Lebesgue 可测集 = Borel 集 + 零测集子集
- [[概念/可测函数]] — 随机变量定义为 Borel 可测函数；Borel $\sigma$ 代数保证了可测函数与连续函数间的深刻联系（Lusin/Egorov）
- [[概念/Lebesgue积分]] — Lebesgue 积分的定义以 Borel/Lebesgue 可测空间为前提
- [[概念/不可数集]] — Cantor 集是零测 Borel 集（$G_\delta$ 集）且不可数；其某些子集 Lebesgue 可测但非 Borel
