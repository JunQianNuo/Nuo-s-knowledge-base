---
title: 考题-01 - Lagrange乘子法求解等式约束优化
subject: 最优化方法
chapter: 20
section: 等式约束优化问题
source: 复习纲要补充
status: 已校对
type: 考题
topics:
  - Lagrange乘子法
  - 一阶必要条件
  - 二阶充分条件
tags:
- Lagrange乘子法
- 一阶必要条件
- 二阶充分条件
---

# 考题 01 — Lagrange 函数求解等式约束

用 Lagrange 乘子法求解：

$$\begin{aligned}
\min \quad & f(x_1, x_2, x_3) = x_1^2 + x_2^2 + x_3^2 \\
\text{s.t.} \quad & x_1 + 2x_2 + 3x_3 = 6 \\
& x_1 - x_2 + x_3 = 2
\end{aligned}$$

**a.** 写出 Lagrangian 函数和一阶必要条件。

**b.** 求解驻点 $x^*$ 和乘子 $\lambda^*$。

**c.** 验证二阶充分条件（计算 Lagrangian 的 Hessian，在切空间上验证正定性）。

**d.** 目标函数的最优值是多少？

---

## 💡 提示

> [!hint]- 点击展开提示
> - Lagrangian：$\mathcal{L}(x, \lambda) = f(x) + \lambda_1 h_1(x) + \lambda_2 h_2(x)$，注意 $h_i(x) = 0$ 的符号约定。
> - 一阶条件：$\nabla_x \mathcal{L} = 0$（$n$ 个方程）加上 $h(x) = 0$（$m$ 个方程），共 $n+m$ 个方程解 $x$ 和 $\lambda$。
> - 二阶条件：$\nabla_{xx}^2 \mathcal{L}$ 在切空间 $T = \{d \mid \nabla h_i(x^*)^\top d = 0\}$ 上正定。
> - 切空间维度 $= n - m = 3 - 2 = 1$，只需找一个基向量 $d$ 验证 $d^\top (\nabla^2 \mathcal{L}) d > 0$。

---

## 📝 详细解析

> [!solution]- 点击展开详细解析
> ### (a) Lagrangian 与一阶必要条件
>
> **Lagrangian：**
>
> $$\mathcal{L}(x_1, x_2, x_3, \lambda_1, \lambda_2) = x_1^2 + x_2^2 + x_3^2 + \lambda_1(x_1 + 2x_2 + 3x_3 - 6) + \lambda_2(x_1 - x_2 + x_3 - 2)$$
>
> **一阶必要条件（驻点方程）：**
>
> $$\begin{aligned}
> \frac{\partial \mathcal{L}}{\partial x_1} &= 2x_1 + \lambda_1 + \lambda_2 = 0 \quad &(1) \\
> \frac{\partial \mathcal{L}}{\partial x_2} &= 2x_2 + 2\lambda_1 - \lambda_2 = 0 \quad &(2) \\
> \frac{\partial \mathcal{L}}{\partial x_3} &= 2x_3 + 3\lambda_1 + \lambda_2 = 0 \quad &(3) \\
> \frac{\partial \mathcal{L}}{\partial \lambda_1} &= x_1 + 2x_2 + 3x_3 - 6 = 0 \quad &(4) \\
> \frac{\partial \mathcal{L}}{\partial \lambda_2} &= x_1 - x_2 + x_3 - 2 = 0 \quad &(5)
> \end{aligned}$$
>
> ---
>
> ### (b) 求解 $x^*$ 和 $\lambda^*$
>
> 从 (1)–(3) 解出 $x$ 关于 $\lambda$ 的表达式：
>
> $$x_1 = -\frac{\lambda_1 + \lambda_2}{2},\quad x_2 = -\frac{2\lambda_1 - \lambda_2}{2},\quad x_3 = -\frac{3\lambda_1 + \lambda_2}{2}$$
>
> 代入约束 (4)：
>
> $$\begin{aligned}
> -\frac{\lambda_1 + \lambda_2}{2} - (2\lambda_1 - \lambda_2) - \frac{3(3\lambda_1 + \lambda_2)}{2} &= 6 \\[4pt]
> -\frac{\lambda_1 + \lambda_2}{2} - \frac{4\lambda_1 - 2\lambda_2}{1} - \frac{9\lambda_1 + 3\lambda_2}{2} &= 6 \\[4pt]
> \text{通分}\quad -14\lambda_1 - 2\lambda_2 &= 12 \\[4pt]
> -7\lambda_1 - \lambda_2 &= 6 \qquad\text{(A)}
> \end{aligned}$$
>
> 代入约束 (5)：
>
> $$\begin{aligned}
> -\frac{\lambda_1 + \lambda_2}{2} + \frac{2\lambda_1 - \lambda_2}{2} - \frac{3\lambda_1 + \lambda_2}{2} &= 2 \\[4pt]
> \frac{-\lambda_1 - \lambda_2 + 2\lambda_1 - \lambda_2 - 3\lambda_1 - \lambda_2}{2} &= 2 \\[4pt]
> \frac{-2\lambda_1 - 3\lambda_2}{2} &= 2 \\[4pt]
> -2\lambda_1 - 3\lambda_2 &= 4 \qquad\text{(B)}
> \end{aligned}$$
>
> 解线性方程组 (A)(B)：
>
> 由 (B)：$\lambda_1 = -2 - \frac{3}{2}\lambda_2$。代入 (A)：
>
> $$-7\left(-2 - \frac{3}{2}\lambda_2\right) - \lambda_2 = 6 \;\Longrightarrow\; 14 + \frac{21}{2}\lambda_2 - \lambda_2 = 6 \;\Longrightarrow\; \frac{19}{2}\lambda_2 = -8 \;\Longrightarrow\; \lambda_2 = -\frac{16}{19}$$
>
> $$\lambda_1 = -2 - \frac{3}{2}\left(-\frac{16}{19}\right) = -2 + \frac{24}{19} = \frac{-38 + 24}{19} = -\frac{14}{19}$$
>
> 回代求 $x^*$：
>
> $$\begin{aligned}
> x_1^* &= -\frac{-\frac{14}{19} - \frac{16}{19}}{2} = -\frac{-\frac{30}{19}}{2} = \frac{15}{19} \\[4pt]
> x_2^* &= -\frac{-\frac{28}{19} + \frac{16}{19}}{2} = -\frac{-\frac{12}{19}}{2} = \frac{6}{19} \\[4pt]
> x_3^* &= -\frac{-\frac{42}{19} - \frac{16}{19}}{2} = -\frac{-\frac{58}{19}}{2} = \frac{29}{19}
> \end{aligned}$$
>
> **验证约束：**
>
> $$x_1 + 2x_2 + 3x_3 = \frac{15 + 12 + 87}{19} = \frac{114}{19} = 6 \;\checkmark$$
>
> $$x_1 - x_2 + x_3 = \frac{15 - 6 + 29}{19} = \frac{38}{19} = 2 \;\checkmark$$
>
> ---
>
> ### (c) 二阶充分条件
>
> **Lagrangian 的 Hessian（关于 $x$）：**
>
> $$\nabla_{xx}^2 \mathcal{L} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix} = 2I$$
>
> 显然正定（$d^\top (2I) d = 2\|d\|^2 > 0$ 对所有 $d \neq 0$），因此在切空间 $T$ 上也正定。
>
> **切空间 $T$：** 约束 Jacobian：
>
> $$A = \begin{bmatrix} \nabla h_1^\top \\ \nabla h_2^\top \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 \\ 1 & -1 & 1 \end{bmatrix}$$
>
> $T = \{d \in \mathbb{R}^3 \mid Ad = 0\}$。求 $T$ 的一组基：
>
> $$Ad = 0 \;\Longrightarrow\; \begin{cases} d_1 + 2d_2 + 3d_3 = 0 \\ d_1 - d_2 + d_3 = 0 \end{cases}$$
>
> 相减第一式减第二式：$3d_2 + 2d_3 = 0 \;\Longrightarrow\; d_3 = -\frac{3}{2}d_2$。
>
> 代入第二式：$d_1 - d_2 - \frac{3}{2}d_2 = 0 \;\Longrightarrow\; d_1 = \frac{5}{2}d_2$。
>
> 取 $d_2 = 1$，得基向量 $d = \left(\frac{5}{2},\, 1,\, -\frac{3}{2}\right)^\top$。
>
> **验证：**
>
> $$d^\top (\nabla_{xx}^2 \mathcal{L}) d = 2 \cdot \left[\left(\frac{5}{2}\right)^2 + 1^2 + \left(-\frac{3}{2}\right)^2\right] = 2 \cdot \left[\frac{25}{4} + 1 + \frac{9}{4}\right] = 2 \cdot \frac{38}{4} = 19 > 0$$
>
> SOSC 成立，$x^*$ 是严格局部极小点。
>
> ---
>
> ### (d) 最优值
>
> $$f(x^*) = \left(\frac{15}{19}\right)^2 + \left(\frac{6}{19}\right)^2 + \left(\frac{29}{19}\right)^2 = \frac{225 + 36 + 841}{361} = \frac{1102}{361} \approx 3.0526$$
>
> 由于 $f$ 是凸函数（$\nabla^2 f = 2I \succ 0$）且约束为线性，KKT 点即为全局最优解。$\square$
>
> **点评：** 本题是等式约束优化的标准流程。值得注意：(1) 3 个变量 + 2 个约束，切空间维度为 1——二阶条件的验证只需在一个方向上检查；(2) Hessian 为 $2I$ 意味着在切空间上自动正定（全域正定 $\Rightarrow$ 任意子空间正定），但条件更弱的情况（Hessian 不定但仍可在切空间上正定）也常见，考试中务必在切空间上验证而非直接在 $\mathbb{R}^n$ 上验证；(3) $x^*$ 坐标均非整数，说明不必害怕分数结果。

---

## 相关知识点

- [[20-等式约束优化问题]] — 等式约束优化的基本理论
- [[../知识点解析梳理/20-等式约束优化问题-知识梳理|第20章 知识梳理]] — 一阶必要条件、二阶充分条件的详细推导
- [[../复习/VII-约束优化及求解方法|VII-约束优化]] — 复习纲要中约束优化综合
