---
subject:
- 数值分析
type: review
source:
- 复习纲要.md
tags:
- Lagrange插值
- Newton插值
- 差商
- Runge现象
- Chebyshev节点
- 样条插值
aliases:
- VI. 插值法 — 复习
schema_version: 2
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- Lagrange插值
- Newton插值
- 差商
- Runge现象
- Chebyshev节点
- 样条插值
status: not done
---

# VI. 插值法（第7章）

> 一句说清：给 $n+1$ 个点，找不超过 $n$ 次的多项式精确经过——Lagrange 显式表示、Newton 增量构造。高次均匀节点会爆炸（Runge），对策是 Chebyshev 节点或分段样条。

---

## 一、核心定义速查

### 1.1 插值问题的要素

| 概念 | 定义 |
|------|------|
| 基函数空间 | $\Phi = \text{span}\{\varphi_0,\ldots,\varphi_n\}$ |
| 插值条件 | $g(x_i) = f(x_i), i=0,\ldots,m$ |
| 唯一性条件 | $m=n$ 且 $M_{ij}=\varphi_j(x_i)$ 可逆 |

### 1.2 三种多项式插值

| 方法 | 基函数 | 系数求解 | 增点代价 |
|------|------|------|:---:|
| Vandermonde | $\{1,x,\ldots,x^n\}$ | 解 $Va=f$（病态） | 全重算 |
| Lagrange | $l_i(x)=\prod_{j\neq i}\frac{x-x_j}{x_i-x_j}$ | 直接：$a_i=f(x_i)$ | 全重算 |
| Newton | $N_k(x)=\prod_{i=0}^{k-1}(x-x_i)$ | 差商递推（前代） | 只加一项 |

### 1.3 差商

| 概念 | 公式/含义 |
|------|------|
| 一阶差商 | $f[x_i,x_j]=\frac{f(x_j)-f(x_i)}{x_j-x_i}$ |
| $k$ 阶差商 | $f[x_0,\ldots,x_k]=\frac{f[x_1,\ldots,x_k]-f[x_0,\ldots,x_{k-1}]}{x_k-x_0}$ |
| 差商对称性 | $f[x_{i_0},\ldots,x_{i_n}]$ 与节点排列顺序无关 |
| Newton 插值 | $P_n(x)=\sum_{k=0}^n f[x_0,\ldots,x_k]\prod_{i=0}^{k-1}(x-x_i)$ |

### 1.4 Runge 与 Chebyshev

| 概念 | 定义 |
|------|------|
| Runge 现象 | 均匀节点下 $n$ 增大 → 两端误差爆炸 |
| Chebyshev 多项式 | $T_n(x)=\cos(n\cos^{-1}x)$，递推 $T_{n+1}=2xT_n-T_{n-1}$ |
| Chebyshev 节点 | $x_k=\cos\frac{(2k+1)\pi}{2n+2}$，最小化 $\max\|\omega(x)\|$ |
| 首一多项式定理 | $\max_{x\in[-1,1]} |p(x)|$ 在首一 $n$ 次多项式中以 $2^{1-n}T_n(x)$ 最小 |
| 区间映射 | $[a,b]$ 上 Chebyshev 节点：$x_k = \frac{a+b}{2} + \frac{b-a}{2}\cos\frac{(2k+1)\pi}{2n+2}$ |

### 1.5 三次样条

分段三次多项式，整体 $C^2$ 连续。$4n$ 个未知数 = $2n + (n-1) + (n-1) + 2 = 4n$ 个方程。

---

## 二、核心定理

### 2.1 插值唯一性

过 $n+1$ 个不同点，存在唯一次数 $\leq n$ 的插值多项式。Vandermonde 行列式 $\prod_{i>j}(x_i-x_j) \neq 0$。

### 2.2 插值误差定理

$$f(x)-P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n (x-x_i), \quad \xi \in (a,b)$$

### 2.3 Chebyshev 插值误差

用 $T_{n+1}(x)$ 的根作节点：$\max_{-1\leq x \leq 1} |f-P_n| \leq \frac{1}{2^n (n+1)!} \max |f^{(n+1)}|$

---

## 三、计算要点

### 3.1 Lagrange 插值

写出 $l_i(x)$ → 线性组合。**例**：过 $(1,6),(2,1),(3,12)$，$P_2(x)=6\frac{(x-2)(x-3)}{(1-2)(1-3)}+1\frac{(x-1)(x-3)}{(2-1)(2-3)}+12\frac{(x-1)(x-2)}{(3-1)(3-2)}$

### 3.2 Newton 插值（差商表）

**例**（同上数据）：
$$\begin{array}{c|c} 1 & 6 \\ & & \frac{1-6}{2-1}=-5 \\ 2 & 1 & & \frac{11-(-5)}{3-1}=8 \\ & & \frac{12-1}{3-2}=11 \\ 3 & 12 \end{array}$$

$P_2(x) = 6 -5(x-1) + 8(x-1)(x-2) = 8x^2-29x+27$

### 3.3 Chebyshev 节点计算

**例**：在 $[-1,1]$ 上取 $n=3$（4个节点）：$x_k = \cos\frac{(2k+1)\pi}{8}, k=0,1,2,3$ → $x_0\approx0.924$, $x_1\approx0.383$, $x_2\approx-0.383$, $x_3\approx-0.924$（向两端集中——抑制 Runge 的机理）。

### 3.4 方法选择

| 场景 | 推荐 |
|------|------|
| 节点少（$\leq 10$） | Newton 插值（均匀节点即可） |
| 节点多 + 全局光滑 | Chebyshev 节点 + Newton 插值 |
| 节点多 + 分段光滑 | 三次样条插值 |
| 需要增量更新 | Newton 插值 |

---

## 四、典型易错点

> [!warning] **插值 ≠ 拟合**：插值精确经过所有点，拟合追求整体误差最小。

> [!warning] **高次 ≠ 高精度**：Runge 现象说明均匀节点下提高次数反而害事。

> [!warning] **Newton 优于 Lagrange 于实用**：增点只需加一项，Lagrange 需重算所有基函数。

> [!warning] **Vandermonde 矩阵是病态的经典例子**：理论可逆，数值上 $n \geq 10$ 就不可用。

---

## 五、相关知识点梳理

| 链接 | 内容 | 为什么看 |
|------|------|----------|
| [[../知识点解析梳理/07-插值法-知识梳理]] | 完整知识梳理 | 所有推导 + 方法对比 |
| [[../知识点解析梳理/08-数据拟合与最小二乘-知识梳理]] | 第8章 | 插值 vs 拟合对比 |
| [[../知识点解析梳理/09-数值积分与数值微分-知识梳理]] | 第9章 | 内插求积公式 |

---

## 六、作业回顾

- Lagrange/Newton 插值手算（差商表）
- Runge 函数验证：均匀节点 vs Chebyshev 节点
- 三次样条的自由度分析和边界条件选择

> 详见 [[../课件/MD/07-插值法#思考与练习|第7章课后思考题]]
