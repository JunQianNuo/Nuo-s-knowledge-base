---
title: 考题-01 - FONC/SONC应用：判断驻点是否为极小点
subject: 最优化方法
chapter: 6
section: 最优性条件
source: 复习纲要补充
status: 已校对
type: 考题
topics:
  - FONC
  - SONC
  - SOSC
  - 鞍点
  - Hessian矩阵
  - 高阶分析
---

# 考题 01

已知二元函数：

$$f(x_1, x_2) = x_1^3 + x_2^3 - 3x_1 x_2$$

**(a)** 求 $f$ 的所有驻点（即满足 $\nabla f(x) = 0$ 的点）。

**(b)** 对每个驻点，计算 Hessian 矩阵，并利用 SONC / SOSC 判断该点是局部极小点、局部极大点还是鞍点。

**(c)** 判断是否存在需要高阶分析的驻点（即二阶条件无法定性的情况），并说明理由。

---

## 💡 提示

> [!hint]- 点击展开提示
> - (a) $\frac{\partial f}{\partial x_1} = 3x_1^2 - 3x_2$，$\frac{\partial f}{\partial x_2} = 3x_2^2 - 3x_1$。联立求解时注意 $x_1 = x_2^2$ 代入第一式。
> - (b) Hessian 为 $\nabla^2 f = \begin{bmatrix} 6x_1 & -3 \\ -3 & 6x_2 \end{bmatrix}$。对 $2 \times 2$ 对称矩阵，可用主子式或特征值判断正定性。
> - (c) 高阶分析仅在 Hessian 半正定（或半负定）但不定时才是必要的——即 Hessian 奇异且二阶条件不矛盾的情况。

---

## 📝 详细解析

> [!solution]- 点击展开详细解析
> ### (a) 求所有驻点
>
> 令梯度为零：
>
> $$\begin{cases}
> \dfrac{\partial f}{\partial x_1} = 3x_1^2 - 3x_2 = 0 \\[8pt]
> \dfrac{\partial f}{\partial x_2} = 3x_2^2 - 3x_1 = 0
> \end{cases}$$
>
> 化简得：
>
> $$\begin{cases}
> x_2 = x_1^2 \quad \text{(1)} \\
> x_1 = x_2^2 \quad \text{(2)}
> \end{cases}$$
>
> 将 (1) 代入 (2)：
>
> $$x_1 = (x_1^2)^2 = x_1^4$$
>
> $$x_1^4 - x_1 = 0 \;\Longrightarrow\; x_1(x_1^3 - 1) = 0$$
>
> 在实数域中：
> - $x_1 = 0 \;\Longrightarrow\; x_2 = 0^2 = 0$
> - $x_1^3 = 1 \;\Longrightarrow\; x_1 = 1 \;\Longrightarrow\; x_2 = 1^2 = 1$
>
> 因此共有 **两个驻点**：$x^{(1)} = [0, 0]^\top$，$x^{(2)} = [1, 1]^\top$。
>
> ### (b) Hessian 矩阵与二阶条件
>
> 梯度再求导得 Hessian：
>
> $$\nabla^2 f(x) = \begin{bmatrix} \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} \\[8pt] \dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} \end{bmatrix} = \begin{bmatrix} 6x_1 & -3 \\ -3 & 6x_2 \end{bmatrix}$$
>
> **驻点 $x^{(1)} = [0, 0]^\top$：**
>
> $$\nabla^2 f(0, 0) = \begin{bmatrix} 0 & -3 \\ -3 & 0 \end{bmatrix}$$
>
> 判断正定性——求特征值：
>
> $$\det\begin{bmatrix} -\lambda & -3 \\ -3 & -\lambda \end{bmatrix} = \lambda^2 - 9 = 0 \;\Longrightarrow\; \lambda = \pm 3$$
>
> 特征值为 $3$ 和 $-3$，一正一负，Hessian 是**不定矩阵**（既非半正定也非半负定）。
>
> - **FONC 验证**：$\nabla f(0,0) = 0$ 成立，是一阶必要条件，无法排除。
> - **SONC 验证**：局部极小点的二阶必要条件是 $\nabla^2 f \succeq 0$。此处 Hessian 有负特征值 $-3$，**不满足 SONC**。因此 $(0, 0)$ **不是局部极小点**。
> - **局部极大点检查**：局部极大点的二阶必要条件是 $\nabla^2 f \preceq 0$。Hessian 有正特征值 $3$，也不满足。因此 $(0, 0)$ 也不是局部极大点。
>
> **结论：$(0, 0)$ 是鞍点。**
>
> **驻点 $x^{(2)} = [1, 1]^\top$：**
>
> $$\nabla^2 f(1, 1) = \begin{bmatrix} 6 & -3 \\ -3 & 6 \end{bmatrix}$$
>
> 判断正定性——用顺序主子式：
>
> - 一阶主子式：$\Delta_1 = 6 > 0$
> - 二阶主子式：$\Delta_2 = \det\begin{bmatrix} 6 & -3 \\ -3 & 6 \end{bmatrix} = 36 - 9 = 27 > 0$
>
> 所有顺序主子式 $> 0$，故 Hessian **正定**（$\nabla^2 f(1,1) \succ 0$）。
>
> 由 **SOSC（二阶充分条件）**：$\nabla f = 0$ 且 $\nabla^2 f \succ 0$ $\;\Longrightarrow\;$ **$(1, 1)$ 是严格局部极小点**。
>
> （特征值验证：$(6-\lambda)^2 - 9 = 0 \;\Longrightarrow\; \lambda = 3, 9$，均为正。）
>
> ### (c) 是否存在需要高阶分析的驻点？
>
> **不需要。** 两个驻点的 Hessian 矩阵均非奇异（行列式均不为 0），二阶条件已经给出定性结论：
>
> - $(0, 0)$ 的 Hessian 是不定矩阵（特征值一正一负），**二阶条件已定性**——必为鞍点。
> - $(1, 1)$ 的 Hessian 是正定矩阵，**二阶条件已定性**——必为严格局部极小点。
>
> 高阶分析（三阶及以上 Taylor 项）仅在以下情形才必要：Hessian 矩阵**半正定**（$\nabla^2 f \succeq 0$）但**不正定**（$\nabla^2 f \nsucc 0$），即 Hessian 有零特征值（奇异）且其余特征值非负。此时 SONC 满足但 SOSC 不满足，仅凭二阶信息无法判定。例如 $f(x_1, x_2) = x_1^2 + x_2^4$ 在 $(0, 0)$ 处 Hessian = $\operatorname{diag}(2, 0)$，半正定但不正定，需利用四阶信息才能确认其为局部极小点。$\square$
>
> **点评：** 本题完整展示了最优化方法中「一阶找候选点 → 二阶定性」的标准流程。关键思想：
>
> 1. **FONC（一阶必要条件）**：$\nabla f = 0$ 筛选出候选点，但本身不足以定性。
> 2. **SONC（二阶必要条件）**：若 $\nabla^2 f$ 非半正定，可直接排除局部极小点的可能性（如 $(0,0)$）。
> 3. **SOSC（二阶充分条件）**：$\nabla^2 f \succ 0$ 可直接确认严格局部极小点（如 $(1,1)$）。
> 4. **SONC 满足但 SOSC 不满足**（Hessian 半正定但非正定）是无法由二阶信息定性的灰色地带，需要高阶分析。
>
> 判断 $2 \times 2$ 对称矩阵正定性的快捷方法：顺序主子式全正（$\Delta_1 > 0$，$\Delta_2 > 0$）。

---

## 相关知识点

- [[06-最优性条件]] — FONC、SONC、SOSC 的定义与关系
- [[06-最优性条件#一阶必要条件 FONC|FONC 一阶必要条件]]
- [[06-最优性条件#二阶条件 SONC 和 SOSC|二阶条件 SONC 与 SOSC]]
- [[../知识点解析梳理/06-最优性条件-知识梳理|第6章 知识梳理]] — 最优性条件的详细推导与应用
- [[../05-微积分基础/考题-梯度-Hessian-Jacobi与方向导数|梯度/Hessian/Jacobi]] — 梯度与 Hessian 计算基础
- [[../05-微积分基础/考题-二阶Taylor展开|Taylor展开]] — Taylor 展开与最优性条件的关系
