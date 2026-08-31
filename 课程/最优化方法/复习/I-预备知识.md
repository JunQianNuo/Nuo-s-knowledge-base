---
title: I. 预备知识 — 复习
subject: 最优化方法
type: 复习
source: 复习纲要-数学.md
topics:
  - 向量空间
  - 矩阵与秩
  - 线性方程组
  - 内积与范数
  - 特征值
  - 正交投影
  - 二次型
  - 矩阵范数
  - Rayleigh不等式
---

# I. 预备知识（第2-3章）

> 覆盖：第2章（向量空间与矩阵）和第3章（线性代数基础）。这些是整个最优化课程的数学语言——梯度是向量，Hessian 是矩阵，收敛性用范数描述，正定性用特征值判定。

---

## 一、核心定义速查

### 1.1 线性代数基础（第2章）

#### 向量与线性组合

| 概念 | 定义 | 关键条件 |
|------|------|----------|
| **线性组合** | $\sum_{i=1}^k \alpha_i a_i$ | $\alpha_i \in \mathbb{R}$ |
| **线性无关** | $\sum \alpha_i a_i = 0 \Rightarrow \alpha_i = 0$（只有零解） | 无冗余方向 |
| **线性相关** | 存在不全为零的 $\alpha_i$ 使 $\sum \alpha_i a_i = 0$ | 至少一个向量可被其余表示 |
| **张成子空间** | $\operatorname{span}[a_1, \ldots, a_k] = \left\{ \sum \alpha_i a_i \mid \alpha_i \in \mathbb{R} \right\}$ | 所有线性组合的集合 |

> 一句说清：线性无关 = 向量组中每个向量都提供了新方向；线性相关 = 有冗余。

#### 基与维数

- **基**：线性无关 + 张成整个空间。一句话：最少向量、完整表达空间的"坐标系"。
- **维数** $\dim V$：基中向量的个数，唯一确定。
- **坐标**：$\forall a \in V$，$\exists!$ 系数使 $a = \sum \alpha_i a_i$。
- **标准基**：$\mathbb{R}^n$ 的标准基 = $I_n$ 的列向量组。

#### 子空间与仿射集

| 概念 | 定义 | 必过原点？ |
|------|------|:---:|
| **子空间** | 非空集 $V$，$\forall x,y \in V, \forall a,b \in \mathbb{R}: ax+by \in V$ | 是 |
| **仿射集** | $X = \bar{x} + V$（子空间的平移） | 不一定 |

> 优化中的应用：线性等式约束 $Ax=b$ 的可行集是仿射集，对应子空间为 $\mathcal{N}(A)$。

#### 矩阵的四大空间

对于 $A \in \mathbb{R}^{m \times n}$：

| 空间 | 记法 | 定义 | 维数 |
|------|------|------|:---:|
| **值域（列空间）** | $\mathcal{R}(A)$ | $\{Ax \mid x \in \mathbb{R}^n\}$ | $\operatorname{rank}(A)$ |
| **零空间（核）** | $\mathcal{N}(A)$ | $\{x \mid Ax = 0\}$ | $n - \operatorname{rank}(A)$ |
| **行空间** | $\mathcal{R}(A^\top)$ | $\{A^\top y \mid y \in \mathbb{R}^m\}$ | $\operatorname{rank}(A)$ |
| **左零空间** | $\mathcal{N}(A^\top)$ | $\{y \mid A^\top y = 0\}$ | $m - \operatorname{rank}(A)$ |

> 空间对偶关系：$\mathcal{R}(A)^\perp = \mathcal{N}(A^\top)$，$\mathcal{N}(A)^\perp = \mathcal{R}(A^\top)$

#### 矩阵的秩

$$\operatorname{rank}(A) = \text{线性无关列的最大个数} = \text{线性无关行的最大个数} = \dim \mathcal{R}(A)$$

**保秩运算**（不改变秩的操作）：

| 运算 | 说明 |
|------|------|
| 列乘以非零标量 | 缩放不改变线性无关性 |
| 交换列 | 顺序不影响秩 |
| 加入一列（是现有列的线性组合） | 冗余不增秩 |
| 乘以可逆矩阵 | $A \to PAQ$（$P,Q$ 可逆） |
| 刚体变换 | 翻转、镜像、对称等 |

**秩与子式**：最高阶非零子式的阶数 = 秩。

#### 迹

$$\operatorname{tr}(A) = \sum_{i=1}^n a_{ii} = \sum_{i=1}^n \lambda_i$$

> 一句说清：迹 = 对角元和 = 特征值之和，是矩阵的"总缩放量"。

---

### 1.2 线性方程组（第2章核心）

#### 问题形式

$$Ax = b \quad \iff \quad x_1 a_1 + x_2 a_2 + \cdots + x_n a_n = b$$

即 $b$ 表示为 $A$ 的列向量的线性组合。

#### 解的存在性与唯一性

| 秩条件 | 解的情况 |
|--------|----------|
| $\operatorname{rank}(A) = \operatorname{rank}[A, b] = n$ | **唯一解** |
| $\operatorname{rank}(A) = \operatorname{rank}[A, b] < n$ | **无穷多解** |
| $\operatorname{rank}(A) \neq \operatorname{rank}[A, b]$ | **无解** |

> 判定口诀：有解靠秩相等，唯一靠秩等于列数。

#### 通解的结构

$$x = x_0 + \mathcal{N}(A)$$

三种等价表示：
1. $x = x_0 + \sum_{i=1}^{n-r} k_i \xi_i$（特解 + 基础解系）
2. $x = x_0 + \mathcal{N}(A)$（特解 + 零空间）
3. $x = A^\dagger b$（广义逆表示）

> $Ax = b$ 有解 $\iff$ $b \in \mathcal{R}(A)$。零空间中的向量不改变 $Ax$ 的结果——它们是自由变量对应的自由度。

---

### 1.3 内积与范数（第2章核心）

#### 欧式内积

$$(x, y) = \sum_{i=1}^n x_i y_i = x^\top y$$

内积公理：非负性、对称性、双线性。

#### 正交

$\cos\theta = \frac{(x, y)}{\|x\| \|y\|}$。正交 $\iff$ $(x, y) = 0$。

> 正交向量组一定是线性无关组（线性无关不一定正交）。

#### 范数的三条性质

| 性质    | 内容                                  |     |     |
| ----- | ----------------------------------- | --- | --- |
| 非负性   | $\|x\| > 0$（$x \neq 0$），$\|0\| = 0$ |     |     |
| 齐次性   | $\|\alpha x\| =\alpha\|x\|$         |     |     |
| 三角不等式 | $\|x + y\| \leq \|x\| + \|y\|$      |     |     |

#### $p$-范数

$$\|x\|_p = \begin{cases}
\left( \sum_{i=1}^n |x_i|^p \right)^{1/p}, & 1 \leq p < \infty \\[4pt]
\max\{|x_1|,\ldots,|x_n|\}, & p = \infty
\end{cases}$$

| $\|x\|_1$ | $\|x\|_2$ | $\|x\|_\infty$ |
|-----------|-----------|----------------|
| 曼哈顿距离（分量绝对值之和） | 欧式距离 | 最大分量绝对值 |

#### 范数等价性

在 $\mathbb{R}^n$ 中所有范数等价。$\forall \|\cdot\|_\alpha, \|\cdot\|_\beta$，$\exists c_1, c_2 > 0$：

$$c_1 \|x\|_\alpha \leq \|x\|_\beta \leq c_2 \|x\|_\alpha$$

**常用等价关系**（$p > q \geq 0$）：

$$\|x\|_p \leq \|x\|_q \leq n^{\frac{1}{q} - \frac{1}{p}} \|x\|_p$$

> 核心意义：在有限维空间中，用哪个范数定义收敛都可以——只差常数因子。这是收敛性分析选最方便范数（通常是 $\ell_2$）的理论基础。

---

### 1.4 线性变换与特征值（第3章）

#### 线性变换

$L: \mathbb{R}^n \to \mathbb{R}^m$ 是线性变换 $\iff$ $L(\alpha x) = \alpha L(x)$ 且 $L(x+y) = L(x) + L(y)$。

| 例子 | 是线性变换？ |
|------|:---:|
| $L(x) = Ax$ | 是 |
| $L(x) = Ax + b$ | 否（仿射变换） |
| $L(x) = x^\top x + c$ | 否（二次） |

> 选定基后，线性变换 = 矩阵乘法。

#### 相似变换

同一线性变换在不同基下的矩阵 $A$ 和 $B$ 满足：$B = T^{-1} A T$（相似变换）。

#### 特征值与特征向量

$$Av = \lambda v$$

- 特征向量：被矩阵变换后方向不变的"特权方向"
- 特征值：该方向上的缩放倍数
- 互异特征值的特征向量线性无关

#### 实对称矩阵的三条黄金性质

| 性质 | 内容 | 优化中的意义 |
|------|------|-------------|
| 特征值全实数 | $\lambda_i \in \mathbb{R}$ | 正定性判定 |
| 互异特征值对应的特征向量正交 | $v_i^\top v_j = 0$ | 保证正交对角化 |
| 可正交对角化 | $A = Q \Lambda Q^\top$，$Q^\top = Q^{-1}$ | 二次型化简为标准形 |

---

### 1.5 正交投影（第3章核心）

#### 正交补

$$V^{\perp} = \{x \in \mathbb{R}^n \mid v^\top x = 0, \forall v \in V\}$$

$\mathbb{R}^n = V \oplus V^{\perp}$（正交直和）。

#### 正交投影算子

$P$ 是子空间 $V$ 上的正交投影算子 $\iff$ $Px \in V$ 且 $x - Px \in V^{\perp}$。

**判定定理**：$P$ 是某子空间的正交投影算子 $\iff$ $P = P^\top = P^2$（**对称且幂等**）。

#### 空间对偶关系

$$\mathcal{R}(A)^{\perp} = \mathcal{N}(A^\top), \qquad \mathcal{N}(A)^{\perp} = \mathcal{R}(A^\top)$$

> 这是 Ch20 中"约束的切空间 = 法空间的补"的代数根源。

---

### 1.6 二次型与正定性（第3章核心）

#### 二次型

$f(x) = x^\top Q x$，$Q \in \mathbb{R}^{n \times n}$。不失一般性总假设 $Q$ 对称（用 $\frac{Q+Q^\top}{2}$ 替代）。

#### 正定性分类（$Q \in S^n$，对称）

| 类型 | 记号 | 条件 | 优化中的含义 |
|------|------|------|-------------|
| **正定** | $Q \succ 0$ | $x^\top Q x > 0, \forall x \neq 0$ | SOSC（严格局部极小） |
| **半正定** | $Q \succeq 0$ | $x^\top Q x \geq 0, \forall x$ | SONC + 凸性 |
| **负定** | $Q \prec 0$ | $x^\top Q x < 0, \forall x \neq 0$ | 严格局部极大 |
| **半负定** | $Q \preceq 0$ | $x^\top Q x \leq 0, \forall x$ | 非严格极大 |
| **不定** | — | 存在正和负 | 鞍点 |

#### Sylvester 准则（仅适用于对称矩阵）

$$Q \succ 0 \iff \text{所有顺序主子式 } \Delta_k > 0 \; (k=1,\ldots,n) \iff \text{所有特征值 } \lambda_i > 0$$

> [!warning] 注意：顺序主子式非负 $\neq$ 半正定！半正定需要**所有**主子式（而非仅顺序主子式）非负，或特征值全非负。
> 
> > 澄清：正定（$\Delta_k > 0$）当然是半正定的充分条件——从定义 $x^\top Q x > 0 \Rightarrow x^\top Q x \geq 0$ 直接推出。这个 warning 说的是顺序主子式**全非负**（允许等号）不够——允许出现零时 Sylvester 的充分性不再成立。更强的条件「顺序主子式全正」当然能推出半正定，因为你已经证出了更强的结论。

#### 主子式 vs 顺序主子式

| 概念 | 定义 | 数量 |
|------|------|:---:|
| **顺序主子式** | 取前 $k$ 行和前 $k$ 列 | $n$ 个 |
| **主子式** | 取任意相同行/列索引 | $C_n^k$ 个（$k$ 阶） |

---

### 1.7 矩阵范数与谱分析（第3章）

#### 矩阵范数的四条公理

$\|A\|$ 需满足：非负性、齐次性、三角不等式、**相容性（次乘性）** $\|AB\| \leq \|A\| \cdot \|B\|$。

#### 常用矩阵范数

| 范数                  | 公式                                                                    | 含义        |
| ------------------- | --------------------------------------------------------------------- | --------- |
| **Frobenius（F-范数）** | $\|A\|_F = \sqrt{\sum a_{ij}^2} = \sqrt{\operatorname{Tr}(A^\top A)}$ | 矩阵的"欧式长度" |
| **谱范数** $\|A\|_2$   | $\sqrt{\lambda_{\max}(A^\top A)}$                                     | 矩阵的最大拉伸倍数 |
| **$\|A\|_1$**       | $\max_{j} \sum_{i} a_{ij}$                                            | 最大列和      |
| **$\|A\|_\infty$**  | $\max_{i} \sum_{j} a_{ij}$                                            | 最大行和      |

#### 谱范数 vs 谱半径

| 概念                | 定义                                | 适用对象 |
| ----------------- | --------------------------------- | :--: |
| **谱范数** $\|A\|_2$ | $\sqrt{\lambda_{\max}(A^\top A)}$ | 任意矩阵 |
| **谱半径** $\rho(A)$ | $\max_i \lambda_i(A)$             | 仅方阵  |

**关系**：$\rho(A) \leq \|A\|_2$。若 $A \in S^n$（对称），则 $\rho(A) = \|A\|_2$。

> [!warning] 关键区分：$A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$，$\rho(A) = 0$ 但 $\|A\|_2 = 1$。非对称时两者差距可以很大。

#### 导出范数（诱导范数）

$$\|A\|_{\alpha,\beta} = \max_{x \neq 0} \frac{\|Ax\|_\beta}{\|x\|_\alpha} = \max_{\|x\|_\alpha = 1} \|Ax\|_\beta$$

> 一句说清：导出范数 = 矩阵作为线性变换时对向量的"最大拉伸倍数"。

---

## 二、核心定理

### 2.1 Rank-Nullity 定理

对于 $A \in \mathbb{R}^{m \times n}$：

$$\dim \mathcal{R}(A) + \dim \mathcal{N}(A) = n$$

即 $\operatorname{rank}(A) + \operatorname{nullity}(A) = n$。

### 2.2 Cauchy-Schwarz 不等式

$$|x^\top y| \leq \|x\|_2 \cdot \|y\|_2$$

等号成立 $\iff$ $x$ 与 $y$ 共线（$x = \alpha y$）。

> 在优化中：$|\nabla f^\top d| \leq \|\nabla f\| \cdot \|d\|$，取等时梯度方向与搜索方向平行——这是负梯度是最速下降方向的数学证明。

### 2.3 范数等价性定理

在 $\mathbb{R}^n$ 中，所有范数等价。即 $\exists c_1, c_2 > 0$：

$$c_1 \|x\|_\alpha \leq \|x\|_\beta \leq c_2 \|x\|_\alpha$$

> 仅在**有限维**空间成立。无穷维空间中不成立。

### 2.4 Rayleigh 不等式

设 $Q \in S^n$（对称矩阵），$\lambda_{\min}$ 和 $\lambda_{\max}$ 为最小和最大特征值：

$$\lambda_{\min}(Q) \, \|x\|_2^2 \leq x^\top Q x \leq \lambda_{\max}(Q) \, \|x\|_2^2$$

> 证明：将 $Q$ 正交对角化 $Q = V \Lambda V^\top$，令 $y = V^\top x$，则 $x^\top Q x = \sum \lambda_i y_i^2$，由 $\lambda_{\min} \sum y_i^2 \leq \sum \lambda_i y_i^2 \leq \lambda_{\max} \sum y_i^2$ 即得。

> 优化意义：梯度法的收敛率 $\displaystyle\left(\frac{\lambda_{\max} - \lambda_{\min}}{\lambda_{\max} + \lambda_{\min}}\right)^2$ 直接来自 Rayleigh 不等式。条件数 $\kappa = \lambda_{\max}/\lambda_{\min}$ 越大，收敛越慢。

### 2.5 Sylvester 准则

对 $Q \in S^n$（对称矩阵）：

$$Q \succ 0 \iff \Delta_k > 0, \; k = 1, \ldots, n \quad (\Delta_k \text{ 为顺序主子式})$$

> [!warning] Sylvester 必须对称！非对称时失效。

### 2.6 谱半径与矩阵幂收敛

$$\lim_{k \to \infty} A^k = 0 \iff \rho(A) = \max_i |\lambda_i(A)| < 1$$

### 2.7 von Neumann 引理

$$\sum_{k=0}^{\infty} A^k = (I - A)^{-1}, \quad \text{当 } \rho(A) < 1$$

> 这是几何级数的矩阵版本。推论：若 $\|A^{-1}\| \cdot \|A - B\| < 1$，则 $B$ 也可逆——可逆性在扰动下稳定。

### 2.8 Gerschgorin 圆盘定理

$A \in \mathbb{R}^{n \times n}$ 的所有特征值落在 $n$ 个圆盘的并集中：

$$D_i = \left\{ \lambda \in \mathbb{C} \;\middle|\; |\lambda - a_{ii}| \leq \sum_{j \neq i} |a_{ij}| \right\}$$

> 特征值范围估计：$\lambda_{\min} \geq \min_i \{a_{ii} - \sum_{j \neq i} |a_{ij}|\}$，$\lambda_{\max} \leq \max_i \{a_{ii} + \sum_{j \neq i} |a_{ij}|\}$。

---

## 三、计算要点

### 3.1 判断线性方程组解的情况

**步骤**：
1. 写出系数矩阵 $A$ 和增广矩阵 $[A, b]$
2. 计算 $\operatorname{rank}(A)$ 和 $\operatorname{rank}([A, b])$
3. 将两个秩与 $n$（列数）比较

**判定表**：

| 条件 | 结论 |
|------|------|
| $\operatorname{rank}(A) \neq \operatorname{rank}([A,b])$ | 无解 |
| $\operatorname{rank}(A) = \operatorname{rank}([A,b]) = n$ | 唯一解 |
| $\operatorname{rank}(A) = \operatorname{rank}([A,b]) < n$ | 无穷多解 |

**通解**：找特解 + 求基础解系（通过解齐次方程组 $Ax = 0$ 得到）。

### 3.2 判定矩阵的正定性

**方法一：特征值法**（最可靠）

计算所有特征值：
- 全正 $\Rightarrow$ 正定
- 全非负 $\Rightarrow$ 半正定
- 有正有负 $\Rightarrow$ 不定

**方法二：Sylvester 准则**（仅对称矩阵有效）

计算顺序主子式 $\Delta_k$：
- 全正 $\Rightarrow$ 正定

**方法三：主子式法**（半正定）

计算**所有**主子式（注意不是顺序主子式）：
- 全非负 $\Rightarrow$ 半正定

### 3.3 计算特征值

解特征多项式 $\det(\lambda I - A) = 0$。

**自检方法**：$\sum \lambda_i = \operatorname{tr}(A)$，$\prod \lambda_i = \det(A)$。

### 3.4 验证正交投影算子

检查两个条件：
1. $P = P^\top$（对称）
2. $P^2 = P$（幂等）

### 3.5 计算矩阵的谱范数

1. 计算 $A^\top A$
2. 求 $A^\top A$ 的特征值
3. $\|A\|_2 = \sqrt{\lambda_{\max}(A^\top A)}$

> 若 $A$ 对称，则 $\|A\|_2 = \rho(A) = \max_i |\lambda_i(A)|$。

### 3.6 计算 $p$-范数

| $\|x\|_1$ | $\|x\|_2$ | $\|x\|_\infty$ |
|-----------|-----------|----------------|
| $\sum_{i=1}^n \|x_i\|$ | $\sqrt{\sum x_i^2}$ | $\max_i \|x_i\|$ |

---

## 四、典型易错点

> [!warning] 子空间必须过原点
> 验证子空间时必须检查零向量是否在集合中。仿射集不一定过原点——不要混淆。

> [!warning] 零空间维数 $= n - \operatorname{rank}(A)$，不是 $m - \operatorname{rank}(A)$
> $\mathcal{N}(A)$ 是 $\mathbb{R}^n$ 的子空间，维数由列数决定。

> [!warning] 线性无关 vs 正交
> 正交 $\Rightarrow$ 线性无关，但线性无关 $\nRightarrow$ 正交。

> [!warning] 范数等价性仅在有限维
> 在无穷维函数空间中 $\ell_1$ 和 $\ell_2$ 不等价。

> [!warning] Sylvester 准则只对对称矩阵有效
> 使用前必须确认 $Q = Q^\top$。非对称矩阵的正定性没有简洁的行列式判据。

> [!warning] 顺序主子式非负 $\neq$ 半正定
> 半正定需要**所有**主子式非负（不仅顺序主子式）或特征值全非负。考试最容易在此设陷阱。

> [!warning] 谱半径 vs 谱范数
> $\rho(A)$ 仅对方阵有定义。非对称时 $\rho(A)$ 可能远小于 $\|A\|_2$。

> [!warning] 投影算子需同时验证对称和幂等
> 仅幂等 $P^2 = P$ 是斜投影算子，还需对称才是**正交**投影。

> [!warning] 并非所有矩阵范数都满足相容性
> $\|A\| = \max_{i,j} |a_{ij}|$ 不满足 $\|AB\| \leq \|A\| \cdot \|B\|$。

> [!warning] 二次型要求 $Q$ 对称
> 若 $Q$ 不对称，用 $\frac{Q + Q^\top}{2}$ 替代。因为 $x^\top Q x = x^\top (\frac{Q+Q^\top}{2})x$。

---

## 五、相关知识点梳理

| 链接 | 内容 | 为什么看 |
|------|------|----------|
| [[../知识点解析梳理/02-向量空间与矩阵-知识梳理]] | 向量空间、子空间、秩、线性方程组、内积、范数 | 预备知识第一部分：结构链与度量链 |
| [[../知识点解析梳理/03-线性代数基础-知识梳理]] | 线性变换、特征值与对角化、正交投影、二次型、矩阵范数 | 预备知识第二部分：工具链 |
| [[../知识点解析梳理/04-几何概念-知识梳理]] | 超平面、凸集 | 子空间和仿射集是超平面的特例 |
| [[../知识点解析梳理/05-微积分基础-知识梳理]] | 梯度、方向导数 | 梯度是向量、方向导数是内积——本章的内积/范数是微分学的基础语言 |
| [[../知识点解析梳理/06-最优性条件-知识梳理]] | FONC/SONC/SOSC | Sylvester 准则和特征值法直接用于 Hessian 正定性判定 |
| [[../知识点解析梳理/08-梯度方法-知识梳理]] | 收敛率分析 | Rayleigh 不等式决定梯度法的收敛率 |

---

## 六、作业回顾

- [[../习题库/02-向量空间与矩阵/README|第2章习题库]] — 重点：线性无关判定（习题2.3）、子空间验证（2.5）、范数计算（2.10）
- [[../习题库/03-线性代数基础/README|第3章习题库]] — 重点：特征值与正定性（3.17）、矩阵范数计算（3.21）、正交投影验证（3.22）
