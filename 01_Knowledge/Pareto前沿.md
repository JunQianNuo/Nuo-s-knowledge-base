---
schema_version: 2
type: concept
source:
- '[[03_Sources/Reviews/归档/最优化方法/知识点解析梳理/24-多目标优化-知识梳理]]'
legacy_topics:
- Pareto前沿
- 多目标优化
- Pareto最优
- 支配关系
tags:
- Pareto前沿
- 多目标优化
- Pareto最优
- 支配关系
topics:
- '[[02_Maps/MOC-最优化]]'
legacy_topic_links:
- '[[01_Knowledge/Pareto最优]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Pareto 前沿

## 一句话

Pareto 前沿是所有 Pareto 最优解在目标函数值空间中的集合——它表示多目标问题中"无法再改善任何目标而不损害其他目标"的边界。

## 严格定义

**Pareto 最优解**：$x^*\in\Omega$ 不存在 $x\in\Omega$ 使得 $f_i(x)\leq f_i(x^*),\forall i$ 且 $\exists j:f_j(x)<f_j(x^*)$。

**Pareto 前沿**：所有 Pareto 最优解在像空间中对应的目标函数值集合。

## 关键区分

| 概念 | 所在空间 | 内容 |
|------|----------|------|
| Pareto 最优解 $x^*$ | 变量空间 | 决策变量取值 |
| Pareto 前沿 | 像空间 | 所有 Pareto 解对应 $f(x^*)$ 值的集合（曲线/曲面） |

## 支配关系

$x$ 支配 $x^*$ $\iff$ $f_i(x)\leq f_i(x^*),\forall i$ 且 $\exists j:f_j(x)<f_j(x^*)$。

## Pareto 前沿的遍历算法

对候选解两两比较，删除被支配的解，最终剩下 Pareto 前沿的近似：

```
对每个候选点 x^j:
  1. 若 x^j 支配某候选解 x^{*r}：删掉 x^{*r}，x^j 进入候选集
  2. 若 x^j 被某候选解支配：丢弃 x^j
  3. 若 x^j 与所有候选解互不支配：加入候选集
```

## 直观理解

对于两目标极小化问题，Pareto 前沿位于像空间的"左下角"边界。每一个 Pareto 最优解意味着"想改善某个目标就必须牺牲另一个"。

## 相关概念
- [[01_Knowledge/Pareto最优]]
- [[01_Knowledge/凸函数]]

- [[01_Knowledge/对偶间隙]]

## 习题

- [[03_Sources/Courses/归档/最优化方法/习题库/24-多目标优化/README|第24章习题库]]
