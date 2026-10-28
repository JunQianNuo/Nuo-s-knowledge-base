---
subject:
- 最优化方法
chapter: 9
source_context:
- file: 09-牛顿法-知识梳理.md
  line: 286
  text: Hessian：∇²f(x) = J(x)^T J(x) + S(x)
related_notes:
- '[[03_Sources/Reviews/归档/最优化方法/知识点解析梳理/09-牛顿法-知识梳理]]'
tags:
- Hessian矩阵
- 非线性最小二乘
- 高斯-牛顿法
aliases:
- 第9章 答疑 — Hessian 矩阵 J^T J + S 的推导
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- Hessian矩阵
- J^T J + S
- 非线性最小二乘
- 高斯牛顿法
- 乘积法则
source: []
status: not done
legacy_type: review
legacy_schema_version: 2
migration_reason: Missing traceable source in legacy source note
---

# 第9章 答疑 — Hessian 矩阵 $\nabla^2 f = J^T J + S$ 的推导

> 问题：**如何理解 Hessian 矩阵 $\nabla^2 f(x) = J(x)^T J(x) + S(x)$？**

> 来源：`09-牛顿法-知识梳理.md` 第 286–295 行

---

## 核心回答

这个形式来自对**非线性最小二乘**目标函数直接求二阶导——就是乘积法则的自然结果。

目标函数：$f(x) = \frac{1}{2} r(x)^T r(x) = \frac{1}{2} \sum_{i=1}^{m} [r_i(x)]^2$

### 第一步：梯度

$$\frac{\partial f}{\partial x_j} = \sum_{i=1}^{m} \frac{\partial r_i}{\partial x_j} \cdot r_i(x) \quad \Rightarrow \quad \nabla f = J(x)^T r(x)$$

### 第二步：Hessian（对梯度的第 $j$ 个分量再对 $x_k$ 求偏导）

$$\begin{aligned}
[\nabla^2 f]_{kj} &= \frac{\partial}{\partial x_k} \left( \sum_{i=1}^{m} \frac{\partial r_i}{\partial x_j} \cdot r_i(x) \right) \\
&= \sum_{i=1}^{m} \underbrace{\frac{\partial r_i}{\partial x_k} \cdot \frac{\partial r_i}{\partial x_j}}_{\text{第一项}} \;+\; \sum_{i=1}^{m} \underbrace{\frac{\partial^2 r_i}{\partial x_k \partial x_j} \cdot r_i(x)}_{\text{第二项}}
\end{aligned}$$

这就是**乘积法则** $\partial(uv) = (\partial u)v + u(\partial v)$ 的直接结果。

### 两项的矩阵解释

| 项 | 矩阵形式 | 含义 |
|---|---|---|
| 第一项 | $J^T J$ | Jacobian 各行外积求和——所有残差"一阶灵敏度"的聚合 |
| 第二项 | $S(x)$ | 残差值 $r_i(x)$ 与其 $n \times n$ 二阶导的加权和——残差的"曲率"信息 |

### 为什么可以省略 $S(x)$？

- **残差小 → $S$ 小**：$r_i(x) \to 0 \Rightarrow S(x) \to 0$
- **$S$ 贵**：需要 $m \times n \times n$ 个二阶偏导数，而 $J^T J$ 算完 $J$ 后只需一次矩阵乘法（几乎免费）

> 删掉 $S$ 就是高斯-牛顿法。

---

## 相关链接

- [[03_Sources/Reviews/归档/最优化方法/知识点解析梳理/09-牛顿法-知识梳理#七、高斯-牛顿法——非线性最小二乘|非线性最小二乘与高斯-牛顿法]]
