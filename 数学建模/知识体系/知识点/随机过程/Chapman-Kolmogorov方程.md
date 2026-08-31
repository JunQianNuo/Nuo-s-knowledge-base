---
title: Chapman-Kolmogorov方程
type: 知识点
subject: 随机过程
source:
  - 知识点/源MD/随机过程16：9
topics:
  - Chapman-Kolmogorov方程
tags:
  - Chapman-Kolmogorov方程
---

# Chapman-Kolmogorov方程

## 一句话

初始分布满足 $\pi_n=\pi_0P^n$。

## 严格定义

$$
\boxed{p_{ij}^{(m+n)}=\sum_kp_{ik}^{(m)}p_{kj}^{(n)},\quad P^{m+n}=P^mP^n}
$$

## 推导：核心洞察

> [!proof]- 推导
> 按中间状态划分事件，再用马尔可夫性质组合条件概率。

## 算法步骤 / 关键性质

- 先核对定义和适用条件。
- 再构造统计量或关系式。
- 最后解释结论而不超出假设范围。

## 典型例题

> [!example]- 解答
> 使用上式识别已知量、代入计算，并检查条件；结果应同时给出统计含义。

## 易错点

- 忽略适用条件。
- 把数学关系直接解释成因果关系。

## 相关概念

- [[马尔可夫性质]]
- [[转移概率矩阵]]

## 相关方法

- [[马尔可夫链状态预测流程]]

## 习题

- 后续链接到对应课程习题库。
