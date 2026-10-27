---
title: 第22b章 答疑 — Lagrangian无下界的例子
subject: 最优化方法
chapter: 22b
type: 答疑
topics:
  - 对偶函数
  - Lagrangian
  - 拉格朗日对偶
  - 无下界
source_context:
  - file: "知识点解析梳理/22b-拉格朗日对偶-知识梳理.md"
    line: 387
    text: "若L关于x无下界（如线性函数），则q=-∞（此时对偶问题需加约束排除此情况）"
related_notes:
  - "[[../复习/VII-约束优化及求解方法]]"
  - "[[22b-拉格朗日对偶-知识梳理]]"
tags:
- 对偶函数
- Lagrangian
- Lagrange对偶
---

# 第22b章 答疑 — Lagrangian 无下界的例子

> 问题：**什么情况下 Lagrangian 无下界导致 $q = -\infty$？举例说明。**

---

## 例子：线性规划

$$\min\; 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + x_2 \geq 1,\; x_1, x_2 \geq 0$$

标准形 $g \leq 0$：$g_1 = 1-x_1-x_2 \leq 0$，$g_2 = -x_1 \leq 0$，$g_3 = -x_2 \leq 0$。

---

## Lagrangian 展开

$$\mathcal{L} = 2x_1 + 3x_2 + \mu_1(1-x_1-x_2) + \mu_2(-x_1) + \mu_3(-x_2)$$

合并 $x$ 的系数：

$$\mathcal{L} = \underbrace{(2 - \mu_1 - \mu_2)}_{x_1 \text{ 系数}} x_1 + \underbrace{(3 - \mu_1 - \mu_3)}_{x_2 \text{ 系数}} x_2 + \mu_1$$

---

## 何时无下界

$\mathcal{L}$ 是 $x$ 的**线性函数**。只要 $x$ 的系数非零，令 $x \to \pm\infty$ 就能让 $\mathcal{L} \to -\infty$。

$q(\mu) = \inf_x \mathcal{L} = -\infty$，**除非**系数全部为零：

$$\begin{cases} 2 - \mu_1 - \mu_2 = 0 \\ 3 - \mu_1 - \mu_3 = 0 \end{cases}$$

---

## 这对偶约束的来源

这两条就是排除无下界情形的约束——只有满足它们的 $\mu$ 才能参与最大化：

$$\begin{aligned}
\max \quad & q(\mu) = \mu_1 \\
\text{s.t.} \quad & \mu_1 + \mu_2 = 2,\; \mu_1 + \mu_3 = 3,\; \mu \geq 0
\end{aligned}$$

---

## 相关链接

- [[答疑/22b-拉格朗日对偶/22b-对偶函数定义|对偶函数定义]]
- [[22b-拉格朗日对偶-知识梳理|第22b章：拉格朗日对偶]]
