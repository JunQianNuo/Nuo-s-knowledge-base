---
schema_version: 2
type: concept
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/02-非线性方程求根-知识梳理]]'
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/10-常微分方程初值问题-知识梳理]]'
legacy_topics:
- Lipschitz条件
- Lipschitz常数
- 存在唯一性
- 收缩映射
tags:
- Lipschitz条件
- 收缩映射
topics:
- '[[02_Maps/MOC-数值计算]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Lipschitz条件

## 一句话

Lipschitz 条件给函数的变化率加了一个全局上界——$|f(x_1)-f(x_2)| \le L|x_1-x_2|$，是不动点迭代全局收敛和 ODE 解存在唯一的理论基础。

## 严格定义

函数 $f$ 在区域 $D$ 上满足 **Lipschitz 条件**，若存在常数 $L \geq 0$ 使得：

$$\|f(x_1) - f(x_2)\| \leq L\|x_1 - x_2\|,\quad \forall x_1, x_2 \in D$$

$L$ 称为 **Lipschitz 常数**。

- 若 $L < 1$，$f$ 称为**收缩映射**（contraction mapping），由 **Banach 不动点定理**保证存在唯一不动点
- 若 $f$ 可微，则 $L = \sup\|f'(x)\|$（用范数替代绝对值推广到多元）
- Lipschitz 条件比连续性更强，比可微性更弱——连续但不可微的函数也可满足 Lipschitz

> [!important] $L < 1$ 是收缩映射不动点迭代 $\mathbf{x}_{k+1}=f(\mathbf{x}_k)$ **全局收敛**的充分条件——这是数值分析中最重要的收敛性定理之一。

## 由来与作用

- 以德国数学家 Rudolf Lipschitz（1832-1903）命名
- 两大核心应用：(1) 不动点迭代的全局收敛性分析（解方程求根）；(2) ODE 初值问题解的存在唯一性定理（Picard-Lindelöf）
- 在数值分析中提供了一种"无需计算导数"的收敛保证方式——只需验证 $L < 1$
- 关键性质：收缩映射序列是 Cauchy 序列；误差衰减 $e_{n+1} \leq L e_n$（线性收敛）

## 相关概念

- [[01_Knowledge/收敛性]]
- [[01_Knowledge/不动点]]
- [[01_Knowledge/步长与离散化]]
