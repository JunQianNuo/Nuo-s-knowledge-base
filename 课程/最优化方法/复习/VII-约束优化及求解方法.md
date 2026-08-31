---
title: 复习VII — 约束优化及求解方法
subject: 最优化方法
type: 复习
source: 复习纲要-数学.md
topics:
  - 等式约束优化
  - 不等式约束优化
  - KKT条件
  - 拉格朗日对偶
  - 凸优化
  - 投影梯度法
  - 罚函数法
  - 增广拉格朗日法
---

# 复习VII — 约束优化及求解方法（第20-23章）

> 对应复习纲要 Section VII。涵盖：Lagrange乘子法、KKT条件、对偶理论、约束优化数值方法。

---

## 一、核心定义速查

### 1.1 约束优化问题标准形式

$$
\min_{x \in \mathbb{R}^n} f(x), \quad \text{s.t.} \quad h(x) = 0, \quad g(x) \leq 0
$$

其中 $h: \mathbb{R}^n \to \mathbb{R}^m$（等式约束），$g: \mathbb{R}^n \to \mathbb{R}^p$（不等式约束）。

| 符号 | 名称 | 说明 |
|------|------|------|
| $f$ | 目标函数 | 需最小化 |
| $h_i(x) = 0$ | 等式约束 | 共 $m$ 个 |
| $g_j(x) \leq 0$ | 不等式约束 | 共 $p$ 个 |
| $\Omega$ | 可行域 | $\{x \mid h(x) = 0, g(x) \leq 0\}$ |

### 1.2 等式约束的核心概念

**正则点**：$x^* \in \Omega$ 是正则点 $\iff$ $\{\nabla h_i(x^*)\}_{i=1}^m$ 线性无关 $\iff$ $\operatorname{rank}(Dh(x^*)) = m$。

**切空间**：

$$
\mathcal{T}(x^*) = \{d \in \mathbb{R}^n \mid Dh(x^*) d = 0\} = \mathcal{N}(Dh(x^*))
$$

维数为 $n - m$。

**法空间**：

$$
\mathcal{N}(x^*) = \mathcal{T}(x^*)^\perp = \mathcal{R}(Dh(x^*)^T) = \operatorname{span}\{\nabla h_1(x^*), \ldots, \nabla h_m(x^*)\}
$$

**关系**：$\mathbb{R}^n = \mathcal{N}(x^*) \oplus \mathcal{T}(x^*)$（正交直和分解）。

### 1.3 不等式约束的核心概念

**积极约束集**：

$$
J(x^*) = \{j \mid g_j(x^*) = 0, \; j = 1, \ldots, p\}
$$

**正则点（不等式约束版）**：$\{\nabla h_i(x^*)\}_{i=1}^m \cup \{\nabla g_j(x^*)\}_{j \in J(x^*)}$ 线性无关。

**线性化可行方向锥**：

$$
F(x^*) = \{d \mid \nabla h_i(x^*)^T d = 0 \; (\forall i), \; \nabla g_j(x^*)^T d \leq 0 \; (\forall j \in J(x^*))\}
$$

**临界锥**（用于二阶条件）：

$$
\mathcal{C}(x^*, \mu^*) = \left\{d \in \mathbb{R}^n \mid
\begin{aligned}
&\nabla h_i(x^*)^T d = 0, && \forall i \\
&\nabla g_j(x^*)^T d = 0, && \forall j \in J_+(x^*, \mu^*) \\
&\nabla g_j(x^*)^T d \leq 0, && \forall j \in J(x^*) \setminus J_+(x^*, \mu^*)
\end{aligned}\right\}
$$

其中 $J_+(x^*, \mu^*) = \{j \in J(x^*) \mid \mu_j^* > 0\}$（强积极约束）。

> 包含关系：$\mathcal{C}(x^*, \mu^*) \subseteq F(x^*)$。$\mu_j > 0$ 的约束在临界锥中表现得像等式约束（要求正交），$\mu_j = 0$ 的约束只要求不等式。

### 1.4 拉格朗日函数

**等式约束**：

$$
l(x, \lambda) = f(x) + \lambda^T h(x) = f(x) + \sum_{i=1}^m \lambda_i h_i(x)
$$

**不等式约束**：

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \lambda^T h(x) + \mu^T g(x)
$$

其中 $\mu \geq 0$（不等式乘子必须非负），$\lambda$ 无符号限制。

**拉格朗日 Hessian**：

$$
\nabla_{xx}^2 \mathcal{L}(x, \lambda, \mu) = \nabla^2 f(x) + \sum_{i=1}^m \lambda_i \nabla^2 h_i(x) + \sum_{j=1}^p \mu_j \nabla^2 g_j(x)
$$

### 1.5 鞍点的定义

> **定义**：$(x^*, z^*) \in X \times Z$ 是 $\phi: X \times Z \to \mathbb{R}$ 的**鞍点**，若：
> $$\phi(x^*, z) \leq \phi(x^*, z^*) \leq \phi(x, z^*), \quad \forall x \in X, \forall z \in Z$$

对约束优化问题，拉格朗日函数的鞍点 $(x^*, \lambda^*, \mu^*)$ 满足：
$$L(x^*, \lambda, \mu) \leq L(x^*, \lambda^*, \mu^*) \leq L(x, \lambda^*, \mu^*)$$

### 1.6 约束优化的对偶

**对偶函数**：$q(\lambda, \mu) = \min_{x} \mathcal{L}(x, \lambda, \mu)$

**对偶问题**：$\max_{\lambda, \mu \geq 0} q(\lambda, \mu)$

|           | 原始问题                                                     | 对偶问题                                              |
| --------- | -------------------------------------------------------- | ------------------------------------------------- |
| 表达式       | $\min_{x} \max_{\lambda, \mu \geq 0} \mathcal{L}$        | $\max_{\lambda, \mu \geq 0} \min_{x} \mathcal{L}$ |
| 对偶间隙      | $\text{dual gap} = w^* - q^* \geq 0$                     | —                                                 |
| 强对偶       | $w^* = q^*$（间隙为零）                                        | —                                                 |
| Slater 条件 | 存在严格内点 $\tilde{x}$：$h(\tilde{x}) = 0$，$g(\tilde{x}) < 0$ | 强对偶的充分条件                                          |

---

## 二、核心定理

### 2.1 等式约束的拉格朗日定理（FONC）

> **定理**：设 $x^*$ 是局部极小点且是正则点，则存在唯一的 $\lambda^* \in \mathbb{R}^m$ 使得：
> $$\nabla f(x^*) + Dh(x^*)^T \lambda^* = 0, \quad h(x^*) = 0$$
>
> 等价地：$\nabla_x l(x^*, \lambda^*) = 0$，$\nabla_\lambda l(x^*, \lambda^*) = 0$

> 直观理解：在极小点处，$\nabla f$ 落在法空间中——即 $\nabla f$ 可以被约束梯度的线性组合表示。沿任何切空间方向一阶变化为零。

### 2.2 KKT 条件（不等式约束，FONC）

> **定理**：设 $x^*$ 是正则的局部极小点，则存在 $\lambda^* \in \mathbb{R}^m$，$\mu^* \in \mathbb{R}^p$ 使得：

1. **原始可行性**：$h(x^*) = 0$，$g(x^*) \leq 0$
2. **对偶可行性**：$\mu^* \geq 0$
3. **驻点条件**：$\nabla f(x^*) + \sum_{i=1}^m \lambda_i^* \nabla h_i(x^*) + \sum_{j=1}^p \mu_j^* \nabla g_j(x^*) = 0$
4. **互补松弛**：$\mu_j^* \cdot g_j(x^*) = 0$，$j = 1, \ldots, p$

> 注意：KKT 是**必要条件**（需正则性）。若问题是凸的，KKT 升格为**充分条件**（不需正则性）。

### 2.3 等式约束的二阶条件

**SONC**（必要条件）：若 $x^*$ 是正则局部极小点，则存在 $\lambda^*$ 满足 FONC，且：

$$d^T L(x^*, \lambda^*) d \geq 0, \quad \forall d \in \mathcal{T}(x^*)$$

**SOSC**（充分条件）：若 $x^*$ 和 $\lambda^*$ 满足 FONC，且：

$$d^T L(x^*, \lambda^*) d > 0, \quad \forall d \neq 0, d \in \mathcal{T}(x^*)$$

则 $x^*$ 是严格局部极小点。

> 关键：二阶条件只在**切空间**上判定，不在全空间。

### 2.4 不等式约束的二阶条件

**SONC**：若 $x^*$ 是正则局部极小点，则存在 $\lambda^*, \mu^*$ 满足 KKT，且：

$$d^T \nabla_{xx}^2 \mathcal{L}(x^*, \lambda^*, \mu^*) d \geq 0, \quad \forall d \in \mathcal{C}(x^*, \mu^*)$$

**SOSC**：若存在 $(x^*, \lambda^*, \mu^*)$ 满足 KKT，且：

$$d^T \nabla_{xx}^2 \mathcal{L}(x^*, \lambda^*, \mu^*) d > 0, \quad \forall d \neq 0, d \in \mathcal{C}(x^*, \mu^*)$$

则 $x^*$ 是严格局部极小点。

> [!hint] 不等式约束的 SOSC 不需要正则性条件（与等式约束的关键区别）。

### 2.5 极小极大不等式与弱对偶

> **定理**：$\min_x \max_z \phi(x, z) \geq \max_z \min_x \phi(x, z)$

应用于约束优化：$w^* = \min_{x \in \Omega} f(x) \geq \max_{\lambda, \mu \geq 0} q(\lambda, \mu) = q^*$

### 2.6 强对偶定理（凸优化）

> **定理**：对于凸优化问题（$f$ 凸，$g_j$ 凸，$h_i$ 仿射），若 Slater 条件成立，则：
> $$w^* = q^*$$
>
> 且 KKT 点、鞍点、全局极小点三者等价。

### 2.7 凸优化的核心性质

- 局部极小 $\iff$ **全局极小**
- KKT 条件既是必要条件也是**充分条件**（且不需要正则性）
- 拉格朗日函数驻点条件 $\Rightarrow$ 全局最优（等式约束凸优化）

---

## 三、计算要点

### 3.1 KKT 条件的求解（三种典型例题类型）

**类型一：含绝对值的非光滑 KKT**

$$
\begin{aligned}
\min \quad & f(x) = |x_1| + x_2 \\
\text{s.t.} \quad & x_1 \leq 0 \\
& x_2 \geq 0
\end{aligned}
$$

> [!note]- 展开解答
> **第一步：化为标准形式**
>
> $$
> g_1(x) = x_1 \leq 0, \qquad g_2(x) = -x_2 \leq 0
> $$
>
> **第二步：处理非光滑项**。$|x_1|$ 在 $x_1 = 0$ 处不可微，需要用**次梯度**。在可行域内 $x_1 \leq 0$，分两种情形。
>
> **情形 A：$x_1 < 0$**（$g_1$ 非积极，$\mu_1 = 0$）
>
> 此时 $|x_1| = -x_1$，$f(x) = -x_1 + x_2$，$\nabla f = (-1, 1)$。
>
> 拉格朗日函数：$\mathcal{L} = -x_1 + x_2 + \mu_1 x_1 + \mu_2(-x_2)$
>
> 驻点条件：
> $$\frac{\partial\mathcal{L}}{\partial x_1} = -1 + \mu_1 = 0 \;\Rightarrow\; \mu_1 = 1$$
>
> 但 $g_1(x) = x_1 < 0$ 非积极 $\Rightarrow$ 互补松弛要求 $\mu_1 = 0$，矛盾。❌
>
> **情形 B：$x_1 = 0$**（$g_1$ 积极，使用次梯度）
>
> $f(x) = 0 + x_2 = x_2$，但 $\partial |x_1|(0) = [-1, 1]$。由于 $x_2 \geq 0$ 且 $f = x_2$，显然 $x_2 = 0$ 时目标最小。猜测 $x^* = (0, 0)$。
>
> 用次梯度 KKT 验证。拉格朗日函数（在不可微点用次梯度）：
>
> 存在 $g \in \partial f(0,0) = ([-1,1], 1)$ 使得：
> $$g + \mu_1 \nabla g_1 + \mu_2 \nabla g_2 = 0$$
>
> 即：$(g, 1) + \mu_1(1, 0) + \mu_2(0, -1) = (0, 0)$
>
> 分量展开：
> $$\begin{cases} g + \mu_1 = 0 \\ 1 - \mu_2 = 0 \end{cases} \;\Rightarrow\; \mu_2 = 1,\; \mu_1 = -g$$
>
> 由 $g \in [-1, 1]$ 且 $\mu_1 \geq 0$（对偶可行）：$\mu_1 = -g \in [0, 1]$。
>
> 互补松弛：$\mu_1 x_1 = 0$ ✓（$x_1 = 0$），$\mu_2(-x_2) = 0 \Rightarrow x_2 = 0$ ✓。
>
> > ✅ **KKT 解**：$x^* = (0, 0)^T$，$\mu_1^* \in [0, 1]$，$\mu_2^* = 1$。注意 $\mu_1^*$ 不唯一——这是非光滑 KKT 的典型特征（次微分是集合而非单点）。

**类型二：线性规划的 KKT**

$$
\begin{aligned}
\min \quad & c^T x \\
\text{s.t.} \quad & Ex = d \\
& x \geq 0
\end{aligned}
$$

> [!note]- 展开解答
> **第一步：化为标准形式**
>
> 不等式约束 $x \geq 0$ 改写为 $g(x) = -x \leq 0$（$p = n$ 个不等式）。
>
> **第二步：拉格朗日函数**
>
> $$\mathcal{L}(x, \lambda, \mu) = c^T x + \lambda^T(d - Ex) + \mu^T(-x), \quad \mu \geq 0$$
>
> **第三步：KKT 条件**
>
> | 条件 | 表达式 |
> |:---|:---|
> | ① 原始可行 | $Ex = d$，$x \geq 0$ |
> | ② 对偶可行 | $\mu \geq 0$ |
> | ③ 驻点条件 | $\nabla_x \mathcal{L} = c - E^T \lambda - \mu = 0$ |
> | ④ 互补松弛 | $\mu_i x_i = 0$，$i = 1, \ldots, n$ |
>
> **第四步：与单纯形法判别数的联系**
>
> 由 ③ 得 $\mu = c - E^T \lambda$。由 ② 得 $c - E^T \lambda \geq 0$，即 $E^T \lambda \leq c$。
>
> 互补松弛 ④ 即 $\mu_i x_i = (c_i - (E^T \lambda)_i) \cdot x_i = 0$。
>
> > 这正是 LP 对偶理论的核心：$\lambda$ 是对偶变量，$\mu = c - E^T \lambda$ 是**判别数（reduced cost）**。单纯形法的终止条件（所有判别数 $\geq 0$）恰好就是 KKT 的驻点条件 + 对偶可行性。
>
> **第五步：对偶问题**
>
> KKT 条件自然导出对偶问题：
> $$\max_{\lambda} \; d^T \lambda, \quad \text{s.t.} \quad E^T \lambda \leq c$$
>
> 其中 $\lambda$ 无符号限制（对应等式约束），$\mu = c - E^T \lambda \geq 0$ 是对偶可行性约束。

**类型三：二次规划的 KKT**

$$
\begin{aligned}
\min \quad & \frac{1}{2}x^T Q x + c^T x \\
\text{s.t.} \quad & Ax \leq b
\end{aligned}
$$

其中 $Q \in \mathbb{S}_+^n$（对称半正定），$A \in \mathbb{R}^{p \times n}$，$b \in \mathbb{R}^p$。

> [!note]- 展开解答
> **第一步：拉格朗日函数**
>
> $$\mathcal{L}(x, \mu) = \frac{1}{2}x^T Q x + c^T x + \mu^T(Ax - b), \quad \mu \geq 0$$
>
> **第二步：KKT 条件**
>
> | 条件 | 表达式 |
> |:---|:---|
> | ① 原始可行 | $Ax \leq b$ |
> | ② 对偶可行 | $\mu \geq 0$ |
> | ③ 驻点条件 | $\nabla_x \mathcal{L} = Qx + c + A^T \mu = 0$ |
> | ④ 互补松弛 | $\mu_i (A_i x - b_i) = 0$，$i = 1, \ldots, p$ |
>
> **第三步：求解策略**
>
> 由 ③ 解出 $x$（$Q \succ 0$ 时可逆）：
> $$x = -Q^{-1}(c + A^T \mu)$$
>
> 代入互补松弛条件 ④ 进行分类讨论（$2^p$ 种 $\mu_i = 0$ / $\mu_i > 0$ 的组合）：
>
> - $\mu_i = 0$：该约束非积极，$A_i x < b_i$
> - $\mu_i > 0$：该约束积极，$A_i x = b_i$
>
> > $Q \succ 0$ 时问题是**严格凸**的，KKT 条件既是必要条件也是**充分条件**——找到的 KKT 点直接是全局极小点，无需验证二阶条件。

### 3.2 用 Lagrange 函数求解约束优化（三种典型例题类型）

**类型一：目标为凸二次，单个线性不等式约束**

$$
\begin{aligned}
\min \quad & f(x) = \frac{1}{2}(x_1^2 + x_2^2) \\
\text{s.t.} \quad & g(x) = x_1 - 1 \leq 0
\end{aligned}
$$

**求解**：$\mathcal{L} = \frac{1}{2}(x_1^2 + x_2^2) + \mu(x_1 - 1)$。驻点条件：$x_1 + \mu = 0$，$x_2 = 0$。分类讨论 $\mu = 0$ 和 $\mu > 0$：
- $\mu = 0 \Rightarrow x_1 = 0$，但 $x_1 - 1 \leq 0$ 满足 → KKT 候选
- $\mu > 0 \Rightarrow x_1 = -\mu < 0$，$x_1 - 1 < 0$ 但 $\mu > 0$ 要求 $x_1 = 1$，矛盾

无约束极小点在 $x = (0, 0)$，满足约束，故 $\mu^* = 0$，$x^* = (0, 0)$。

**类型二：目标线性，单个非线性不等式约束**

$$
\begin{aligned}
\min \quad & f = -x_2 \\
\text{s.t.} \quad & x_1^2 + x_2^2 - 9 \leq 0 \\
& x_1 \geq 0, x_2 \geq 0
\end{aligned}
$$

**求解**：$\mathcal{L} = -x_2 + \mu(x_1^2 + x_2^2 - 9) - \mu_1 x_1 - \mu_2 x_2$。驻点条件加互补松弛，分类讨论得最优解在边界上：$x_1 = 0, x_2 = 3$，$\mu = 1/6$。

**类型三：线性目标，非线性约束**

$$
\begin{aligned}
\min \quad & f(x) = c^T x \\
\text{s.t.} \quad & g(x) = (x - \bar{x})^T A (x - \bar{x}) \leq b
\end{aligned}
$$

其中 $A \succ 0$。这是带椭球约束的线性规划。若无约束极小（线性函数无下界），最优解必在椭球边界上（约束积极）。用 KKT 条件求解。

### 3.3 等式约束 QP 的闭式解

$$
\min \frac{1}{2} x^T Q x, \quad \text{s.t.} \; Ax = b
$$

其中 $Q \succ 0$，$\operatorname{rank}(A) = m$。解为：

$$x^* = Q^{-1} A^T (A Q^{-1} A^T)^{-1} b, \qquad \lambda^* = (A Q^{-1} A^T)^{-1} b$$

### 3.4 写对偶问题并分析原始解与对偶解

**三步法**：
1. 写出拉格朗日函数：$\mathcal{L} = f(x) + \lambda^T h(x) + \mu^T g(x)$，$\mu \geq 0$
2. 求对偶函数：$q(\lambda, \mu) = \min_x \mathcal{L}(x, \lambda, \mu)$（令 $\nabla_x \mathcal{L} = 0$，解 $x^*(\lambda, \mu)$，回代）
3. 写出对偶问题：$\max_{\lambda, \mu \geq 0} q(\lambda, \mu)$

**对偶的三个重要特例**：

| 原问题         | 对偶问题                                      | 说明                                                           |
| ----------- | ----------------------------------------- | ------------------------------------------------------------ |
| 二次规划 + 等式约束 | 无约束二次规划（维数降低）                             | $q(\lambda) = -\frac{1}{2}\lambda^T P \lambda + d^T \lambda$ |
| 线性规划        | $\max b^T \lambda, \; A^T \lambda \leq c$ | LP对偶经典形式                                                     |
| 一般凸优化       | 强对偶成立（Slater条件）                           | 可解对偶代替原问题                                                    |

### 3.5 数值方法总览

| 方法 | 迭代格式 | 关键参数 | 使用条件 |
|------|----------|----------|----------|
| **投影梯度法** | $x^{(k+1)} = \Pi_\Omega[x^{(k)} - \alpha_k \nabla f(x^{(k)})]$ | 步长 $\alpha_k$ | 投影好算（盒子/球/仿射集） |
| **拉格朗日乘子法（等式）** | $x^{(k+1)} = x^{(k)} - \alpha_k(\nabla f + \nabla h^T \lambda^{(k)})$ <br> $\lambda^{(k+1)} = \lambda^{(k)} + \beta_k h(x^{(k)})$ | $\alpha_k, \beta_k$ | 中小规模 |
| **拉格朗日乘子法（不等式）** | $\mu^{(k+1)} = [\mu^{(k)} + g(x^{(k)})]_+$ | — | 乘子非负投影 |
| **$\ell_2$ 罚函数法** | $\min_x f(x) + \gamma(\|h\|^2 + \|[g]_+\|^2)$ | $\gamma \to \infty$ | 灵活、实现简单 |
| **增广拉格朗日法** | $x^{(k+1)} = \arg\min_x L_\gamma(x, \lambda^{(k)}, \mu^{(k)})$ <br> $\lambda^{(k+1)} = \lambda^{(k)} + \gamma h(x^{(k+1)})$ | 固定 $\gamma$ | 稳健（不需 $\gamma \to \infty$） |

### 3.6 投影梯度法详解

**投影定义**：$\Pi_\Omega[x] = \arg\min_{z \in \Omega} \|z - x\|$（$\Omega$ 是非空闭凸集时存在且唯一）。

**线性等式约束 $Ax = b$ 的投影矩阵**：

$$P = I - A^T (A A^T)^{-1} A, \quad \operatorname{rank}(A) = m$$

投影梯度迭代：$x^{(k+1)} = x^{(k)} - \alpha_k P \nabla f(x^{(k)})$

若 $x^{(0)}$ 可行则所有迭代点自动可行（$AP = 0$）。一阶必要条件：$P \nabla f(x^*) = 0$。

### 3.7 简单集合上的投影计算

| 约束集 | 投影公式 |
|--------|----------|
| 盒子 $\{x \mid a \leq x \leq b\}$ | $[\Pi_\Omega(x)]_i = \operatorname{median}\{a_i, x_i, b_i\}$ |
| 球 $\{x \mid \|x\| \leq r\}$ | $\Pi_\Omega(x) = \min(1, \frac{r}{\|x\|}) \cdot x$ |
| 仿射集 $\{x \mid Ax = b\}$ | $\Pi_\Omega(x) = x - A^\dagger(Ax - b)$ |
| 超平面 $\{x \mid a^T x = b\}$ | $\Pi_\Omega(x) = x - \frac{a^T x - b}{\|a\|^2} a$ |

### 3.8 罚函数法详解

**罚函数类型**：

| 类型         | 形式                                             | 可微性 |     |     |
| ---------- | ---------------------------------------------- | :-: | --- | --- |
| $\ell_1$ 罚 | $\gamma(\sum h_i+ \sum \max\{0, g_j\})$        | 不可微 |     |     |
| $\ell_2$ 罚 | $\gamma(\sum h_i^2 + \sum [\max\{0, g_j\}]^2)$ | 可微  |     |     |
| 对数罚（内点）    | $-\gamma \sum \ln(-g_j(x))$                    | 可微  |     |     |

**收敛性**：若 $\gamma_k \to \infty$，$\{x^{(k)}\}$ 的任意极限点都是原约束问题的极小点。

**引理链**（$\gamma_k$ 非减）：
1. 罚函数目标值 $\Phi(\gamma_k, x^{(k)})$ 随 $k$ 非减
2. $f(x^{(k)})$ 随 $k$ 非减（逼近最优值）
3. $P(x^{(k)})$ 随 $k$ 非增（可行性越来越好）
4. $f(x^*) \geq \Phi(\gamma_k, x^{(k)}) \geq f(x^{(k)})$

### 3.9 增广拉格朗日函数法

**增广拉格朗日函数**：

$$
L_\gamma(x, \lambda, \mu) = f(x) + \lambda^T h(x) + \mu^T g(x) + \frac{\gamma}{2}(\|h(x)\|^2 + \|[g(x)]_+\|^2)
$$

**迭代**：固定 $\gamma$，交替更新 $x$（精确极小化 $L_\gamma$）和乘子。

**优势**：$\gamma$ 不需要趋于无穷，取适度固定值即可。乘子更新比罚函数法更精确。

---

## 四、典型易错点

> [!warning] FONC vs SOSC 的角色
> - FONC 是**必要条件**（正则假设下），满足 FONC 只是候选点
> - SOSC 是**充分条件**，但需要 Hessian 在切空间/临界锥上严格正定
> - 只满足 FONC 不满足 SOSC 的点可能是鞍点

> [!warning] 二阶条件只在切空间/临界锥上判定
> 等式约束：在 $\mathcal{T}(x^*)$（$(n-m)$ 维）上判定。不等式约束：在 $\mathcal{C}(x^*, \mu^*)$ 上判定。**不要错误地在全空间 $\mathbb{R}^n$ 上判定。**

> [!warning] KKT 乘子的符号
> - $\lambda$（等式乘子）：**无符号限制**，可正可负可零
> - $\mu$（不等式乘子）：**必须非负**（$\mu_j \geq 0$）
> - 写 $g(x) \geq 0$ 时拉格朗日项应为 $-\mu^T g(x)$（$\mu \geq 0$）

> [!warning] 临界锥 $\neq$ 可行方向锥
> - $F(x^*)$：用于一阶条件（$\mu_j \geq 0$ 的积极约束只需 $\nabla g_j^T d \leq 0$）
> - $\mathcal{C}(x^*, \mu^*)$：用于二阶条件（$\mu_j > 0$ 的约束要求 $\nabla g_j^T d = 0$）
> - 在 $F(x^*)$ 上做二阶判定会漏判或误判

> [!warning] 正则性是拉格朗日定理/KKT 的前提
> 若 $x^*$ 不是正则点，拉格朗日定理可能不成立。但不等式约束 SOSC 不要求正则性——只需 KKT 成立。

> [!warning] KKT 分类讨论的完整性
> $p$ 个不等式乘子有 $2^p$ 种组合。必须逐一检查，遗漏任何一种都可能丢掉真正的 KKT 点。配合互补松弛可以有效剪枝。

> [!warning] 凸优化中 KKT 的角色翻转
> - 一般非凸：KKT 是**必要条件**（需正则性）
> - 凸优化：KKT 是**充分条件**（不需正则性），且 KKT 点 = 全局极小点

> [!warning] 等式约束必须是仿射函数才能保证约束集凸
> $h(x) = 0$ 中的 $h$ 必须是一次函数 $Ax - b$ 的形式，否则 $\{x \mid h(x) = 0\}$ 通常不是凸集。

> [!warning] 罚函数法 $\gamma$ 不能无限增大
> $\gamma$ 太大导致罚函数子问题 Hessian 条件数爆炸，难以求解。实践中采用逐步增大 $\gamma$ 的策略，以前一轮解为初始点。

> [!warning] 投影梯度法需要投影好算
> 投影梯度法对盒子、球、超平面等有闭式投影的约束集高效。对于复杂约束集（如非线性等式约束），投影本身难以计算。

> [!warning] 弱对偶永远成立，强对偶需要凸性 + Slater
> 弱对偶性 $w^* \geq q^*$ 不需任何条件。强对偶 $w^* = q^*$ 需凸优化 + Slater 条件保证。非凸问题可能也有强对偶，但不保证。

> [!warning] 对偶函数的定义域可能受限
> 当 $\min_x L(x, \lambda, \mu) = -\infty$ 时，对应的 $(\lambda, \mu)$ 不是对偶可行解。这在 LP 对偶推导中尤其重要——需要通过 "$q = -\infty$ 除非..." 来隐式定义对偶约束。

---

## 五、相关知识点梳理

| 知识点 | 链接 | 关联说明 |
|--------|------|----------|
| 等式约束优化 | [[../知识点解析梳理/20-等式约束优化问题-知识梳理\|第20章 知识梳理]] | 拉格朗日乘子、切空间/法空间、二阶条件、灵敏性 |
| 不等式约束优化 | [[../知识点解析梳理/21-不等式约束优化问题-知识梳理\|第21章 知识梳理]] | KKT条件、临界锥、SOSC |
| 凸优化 | [[../知识点解析梳理/22a-凸优化问题-知识梳理\|第22a章 知识梳理]] | 凸性判别、KKT升格、SDP/LMI |
| 拉格朗日对偶 | [[../知识点解析梳理/22b-拉格朗日对偶-知识梳理\|第22b章 知识梳理]] | 鞍点、极小极大不等式、对偶推导、弱/强对偶、Slater条件 |
| 约束优化方法 | [[../知识点解析梳理/23-约束优化方法-知识梳理\|第23章 知识梳理]] | 投影法、拉格朗日法、罚函数法、增广Lagrange法 |
| 最优性条件 | [[../知识点解析梳理/06-最优性条件\|第6章]] | FONC/SONC/SOSC框架是无约束版本，第20-21章是有约束版本 |
| 线性规划 | [[复习/V-线性规划\|V-线性规划]] | LP对偶是拉格朗日对偶在LP上的特例 |

---

## 六、典型考题速览

1. **写 Lagrange 函数**：给定约束优化问题，正确写出 $\mathcal{L}$（注意不等式乘子符号 $\mu \geq 0$）
2. **KKT 条件求解**：分类讨论 $\mu_j = 0$ / $\mu_j > 0$，配合互补松弛求解（见三种典型例题）
3. **二阶条件验证**：求 Hessian $\nabla_{xx}^2 \mathcal{L}$，确定切空间/临界锥，验证正定性
4. **写对偶问题**：三步法（Lagrange 函数 $\to$ 对偶函数 $\to$ 对偶问题）
5. **投影计算**：盒子截断、球归一化、超平面修正（三大闭式公式）
6. **投影梯度法**：线性等式约束下 $P = I - A^T(AA^T)^{-1}A$，验证可行性保持
7. **罚函数转化**：将约束问题写为 $\min f + \gamma P$ 的无约束形式（$\ell_2$ 罚函数）
8. **拉格朗日乘子法迭代**：写出一/两步迭代（$x$ 下降 + $\lambda$ 上升）
9. **判断强对偶是否成立**：验证凸性 + Slater 条件
10. **凸优化判定**：用 Hessian 半正定或保凸运算判断目标函数凸性
 