---
schema_version: 2
type: method
related:
- '[[01_Knowledge/Euler方法]]'
- '[[01_Knowledge/Runge-Kutta方法]]'
tags:
- EulerRK迭代流程
topics:
- '[[02_Maps/MOC-数值计算]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
source:
- '[[03_Sources/Reviews/归档/数值分析/复习/IX-常微分方程初值问题]]'
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/10-常微分方程初值问题-知识梳理]]'
---

# EulerRK迭代流程

## 适用场景
求解 ODE 初值问题 $y'=f(x,y)$, $y(x_0)=y_0$，根据精度需求选择 Euler（简单低精度）或 Runge-Kutta（高精度多阶段）。

## 核心公式/步骤

| 方法 | 公式 | 阶数 | 每步求值 |
|:--|:--|:--|:--|
| Euler 显式 | $\boxed{y_{i+1}=y_i+hf(x_i,y_i)}$ | 1 | 1 |
| 中点法 | $\boxed{y_{i+1}=y_i+hf(x_i+\frac{h}{2},y_i+\frac{h}{2}f_i)}$ | 2 | 2 |
| 经典 RK4 | $\boxed{\begin{aligned}&k_1=hf(x_i,y_i),\ k_2=hf(x_i+\frac{h}{2},y_i+\frac{k_1}{2})\\&k_3=hf(x_i+\frac{h}{2},y_i+\frac{k_2}{2}),\ k_4=hf(x_i+h,y_i+k_3)\\&y_{i+1}=y_i+\frac{1}{6}(k_1+2k_2+2k_3+k_4)\end{aligned}}$ | 4 | 4 |

```mermaid
flowchart TD
    A["给定 ODE\n y'=f(x,y), y(x0)=y0"] --> B{"精度需求 ?"}
    B -->|"低精度/快速试算"| C["Euler 显式\n y_{i+1}=y_i+hf_i\n 1阶，1次求值"]
    B -->|"中等精度"| D["中点法\n 2阶段\n 2阶，2次求值"]
    B -->|"高精度"| E["经典 RK4\n 4阶段\n 4阶，4次求值"]
    C --> F["计算一步"]
    D --> F
    E --> F
    F --> G{"到达终点 ?"}
    G -->|"否"| B
    G -->|"是"| H["输出数值解序列"]
```

## 典型例题

> **题目**：用 Euler 和 RK4 解 $y'=-y$, $y(0)=1$，步长 $h=0.2$，求 $y(1)$。

> [!example]- 解答
> 精确解 $y=e^{-x}$，$y(1)=e^{-1}\approx0.3679$。
> Euler：$y_1=0.8$, $y_2=0.64$, ..., $y_5=0.3277$，误差 $0.040$
> RK4：$y_5\approx0.3679$，误差极小。点评：RK4 的局部截断误差为 $O(h^5)$，在光滑问题上远优于 Euler。

## 链接的知识点
- [[01_Knowledge/Euler方法]]
- [[01_Knowledge/Runge-Kutta方法]]

## 链接的习题
- [[03_Sources/Courses/归档/数值分析/习题库/10-常微分方程初值问题的数值解法/README|第10章习题库]]
