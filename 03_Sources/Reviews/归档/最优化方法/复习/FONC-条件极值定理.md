---
subject:
- 最优化方法
type: review
source:
- 复习纲要-数学.md
tags:
- 一阶必要条件
- Lagrange乘子法
- 等式约束优化
- 切锥
- 正交补
aliases:
- FONC → 条件极值定理 — 最优化方法
schema_version: 2
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- FONC
- 条件极值定理
- Lagrange乘子法
- 等式约束优化
- 切锥
- 线性无关约束规格
- 正交补
status: not done
---

# FONC → 条件极值定理（Lagrange 乘子定理）

> 本文详细展示从一阶必要条件（FONC）到等式约束优化条件极值定理（Lagrange 乘子定理）的完整推导过程。

---

## 一、问题设定

考虑**仅含等式约束**的优化问题：

$$\min_{x \in \Omega} f(x), \qquad \Omega = \{x \in \mathbb{R}^n \mid h_i(x) = 0,\; i = 1, \ldots, m\}$$

其中 $f, h_1, \dots, h_m \in C^1$（连续可微）。

**目标**：从 FONC 出发，推导经典的条件极值定理——即存在 Lagrange 乘子 $\lambda_1^*, \dots, \lambda_m^*$ 使得

$$\nabla f(x^*) = \sum_{i=1}^{m} \lambda_i^* \nabla h_i(x^*)$$

---

## 二、第一步：切锥的表征

### 2.1 等式约束下切锥的定义

对于等式约束 $\Omega = \{x \mid h(x) = 0\}$（$h = (h_1, \dots, h_m)^T$），在点 $x^*$ 处的切锥为：

$$\mathcal{T}_\Omega(x^*) = \{d \in \mathbb{R}^n \mid Dh(x^*) \, d = 0\}$$

其中 $Dh(x^*) \in \mathbb{R}^{m \times n}$ 是 $h$ 在 $x^*$ 处的 Jacobian 矩阵：

$$Dh(x^*) = \begin{bmatrix}
\nabla h_1(x^*)^T \\
\nabla h_2(x^*)^T \\
\vdots \\
\nabla h_m(x^*)^T
\end{bmatrix}$$

> [!hint] 直观理解
> 等式约束定义了一个 $(n-m)$ 维的曲面（流形），切锥就是该曲面在 $x^*$ 处的切平面。条件 $Dh(x^*) d = 0$ 要求方向 $d$ 与所有约束梯度正交——即 $d$ 在曲面的切空间内。

### 2.2 切锥是一个线性子空间

$$T := \mathcal{T}_\Omega(x^*) = \ker(Dh(x^*))$$

这是 $Dh(x^*)$ 的零空间，是 $\mathbb{R}^n$ 的一个线性子空间。

---

## 三、第二步：FONC 给出正交条件

### 3.1 应用 FONC

由[[常考查的证明#证明 6：约束优化的一阶必要条件（FONC）|FONC]]：
$$d^T \nabla f(x^*) \geq 0, \quad \forall d \in T = \ker(Dh(x^*))$$

### 3.2 关键观察：从不等式到等式

因为 $T$ 是一个线性子空间（而不只是锥），如果 $d \in T$，则 $-d \in T$ 也成立。

分别对 $d$ 和 $-d$ 应用 FONC：
$$\begin{aligned}
d^T \nabla f(x^*) &\geq 0 \\
(-d)^T \nabla f(x^*) &\geq 0 \quad \Rightarrow \quad d^T \nabla f(x^*) \leq 0
\end{aligned}$$

两者同时成立意味着：
$$d^T \nabla f(x^*) = 0, \quad \forall d \in T$$

> [!hint] 核心洞察
> 对于等式约束，FONC 的不等式自动升级为等式，因为切锥是一个线性子空间——每个方向和它的反向都是可行方向。这意味着梯度必须与整个切空间正交。

---

## 四、第三步：从正交性到 Lagrange 乘子

### 4.1 FONC 的几何含义

条件 $d^T \nabla f(x^*) = 0$ 对所有 $d \in T$ 成立等价于：

$$\nabla f(x^*) \in T^\perp$$

即 $\nabla f(x^*)$ 属于切空间 $T$ 的正交补。

### 4.2 切空间正交补的代数刻画

因为 $T = \ker(Dh(x^*))$，由线性代数的基本定理（"行空间是零空间的正交补"）：

$$T^\perp = \ker(Dh(x^*))^\perp = \operatorname{range}\!\big(Dh(x^*)^T\big)$$

$Dh(x^*)^T \in \mathbb{R}^{n \times m}$ 的列空间由梯度向量 $\nabla h_1(x^*), \dots, \nabla h_m(x^*)$ 张成。

因此，$\nabla f(x^*) \in \operatorname{range}(Dh(x^*)^T)$ 意味着**存在系数 $\lambda_1^*, \dots, \lambda_m^* \in \mathbb{R}$ 使得**：

$$\nabla f(x^*) = \sum_{i=1}^{m} \lambda_i^* \nabla h_i(x^*)$$

### 4.3 用 Lagrange 函数表达

定义 **Lagrange 函数**：
$$L(x, \lambda) = f(x) - \sum_{i=1}^{m} \lambda_i h_i(x)$$

则一阶必要条件 $\nabla_x L(x^*, \lambda^*) = 0$ 恰好给出：
$$\nabla f(x^*) - \sum_{i=1}^{m} \lambda_i^* \nabla h_i(x^*) = 0$$

此即为**条件极值定理**（Lagrange 乘子定理）。

---

## 五、线性无关约束规格（LICQ）

### 5.1 LICQ 的必要性

上述推导中隐含了一个重要假设：$T^\perp = \operatorname{range}(Dh(x^*)^T)$ 是 $m$ 维的。这要求梯度向量组 $\{\nabla h_1(x^*), \dots, \nabla h_m(x^*)\}$ **线性无关**。

若约束梯度线性相关，则 $T^\perp$ 的维数小于 $m$，乘子 $\lambda_i^*$ 的选取不唯一——此时 FONC 仍然成立，但 Lagrange 乘子定理的表述需要调整。

### 5.2 LICQ 的定义

> **线性无关约束规格（LICQ）**：在 $x^*$ 处，积极约束的梯度向量组 $\{\nabla h_i(x^*)\}_{i=1}^{m}$ 线性无关。

等价于 Jacobian 矩阵 $Dh(x^*)$ 行满秩：$\operatorname{rank}(Dh(x^*)) = m$。

> [!hint] LICQ 的作用
> LICQ 保证乘子的唯一性，也是后续 KKT 条件推导中正则性条件的基础。在大多数实际应用中，LICQ 是一个合理且温和的假设。

---

## 六、完整证明流程总结

```
FONC: d^T ∇f(x*) ≥ 0, ∀d ∈ T
         │
         ▼ (T 是子空间⇒不等式升级为等式)
d^T ∇f(x*) = 0, ∀d ∈ T
         │
         ▼ (梯度正交于切空间)
∇f(x*) ∈ T^⊥
         │
         ▼ (T^⊥ = range(Dh^T) = span{∇h_i})
∇f(x*) = Σ λ_i* ∇h_i(x*)
         │
         ▼ (定义 Lagrange 函数)
条件极值定理 / Lagrange 乘子定理
```

每一步的逻辑关系：

| 步骤 | 从 | 到 | 依赖的工具 |
|------|----|----|-----------|
| 1 | 局部极小点 $x^*$ | $d^T \nabla f(x^*) \geq 0,\; \forall d \in T$ | FONC（第6章） |
| 2 | 不等式 | 等式 $d^T \nabla f(x^*) = 0$ | $T$ 是线性子空间 ⇒ $d \in T \Rightarrow -d \in T$ |
| 3 | 等式 | $\nabla f(x^*) \in T^\perp$ | 正交补的定义 |
| 4 | $\nabla f(x^*) \in T^\perp$ | $\nabla f(x^*) = \sum \lambda_i^* \nabla h_i(x^*)$ | 线性代数：$\ker(A)^\perp = \operatorname{range}(A^T)$ |
| 5 | — | 乘子唯一 | LICQ：$\nabla h_i(x^*)$ 线性无关 |

---

## 七、相关知识点链接

- [[常考查的证明#证明 6：约束优化的一阶必要条件（FONC）|FONC 的证明]]
- [[../知识点解析梳理/06-最优性条件-知识梳理|第6章：最优性条件与切锥]]
- [[../知识点解析梳理/06-最优性条件-知识梳理#三、可行方向与切锥|切锥的定义与计算]]
- [[03_Sources/Reviews/归档/最优化方法/复习/FONC-KKT条件|FONC → KKT 条件（含不等式约束）]]
- [[../复习纲要-数学|复习纲要]]
