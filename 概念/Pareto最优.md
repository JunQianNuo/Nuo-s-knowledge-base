---
title: Pareto最优
type: 概念
source:
- 课程/最优化方法/知识点解析梳理/24-多目标优化-知识梳理.md
topics:
- Pareto最优
- 多目标优化
- Pareto前沿
- 支配关系
status: 已整理
---

# Pareto 最优

## 一句话

Pareto 最优解是指不存在另一个可行解能在所有目标上都不差、且至少一个目标更好的解——你想改善某个目标，就必须牺牲其他目标。

## 严格定义

对于多目标极小化问题 $\min [f_1(x),\dots,f_l(x)]^T$，s.t. $x\in\Omega$，$x^*$ 是 **Pareto 最优解**，若**不存在** $y\in\Omega$ 使得

$$
f_i(y)\leq f_i(x^*),\;\forall i\quad\text{且}\quad\exists j:f_j(y)<f_j(x^*)
$$

> [!important] 等价表述：$x^*$ 是 Pareto 最优 $\iff$ 不存在任何可行的"Pareto 改进"——要改善任何目标都必须以损害其他目标为代价。这与经济学中"帕累托有效"的概念完全一致。

**支配关系**：$y$ **支配** $x^*$，若 $f_i(y)\leq f_i(x^*),\forall i$ 且 $\exists j:f_j(y)<f_j(x^*)$。Pareto 最优 = 不被任何可行解支配。

## 由来与作用

Pareto 最优由意大利经济学家 Vilfredo Pareto 在 1906 年提出。在优化中：

- **多目标优化的"最优"定义**：向量无法直接比较大小，Pareto 最优取代了标量优化中的"全局极小点"概念
- **Pareto 前沿**：所有 Pareto 最优解在像空间中的集合形成一条边界——它表示问题可达的"最佳权衡"
- **转化为单目标**：加权和法、$\varepsilon$-约束法、极大极小法等都是通过不同方式"逼近"Pareto 前沿

## 相关概念

- [[对偶]]
