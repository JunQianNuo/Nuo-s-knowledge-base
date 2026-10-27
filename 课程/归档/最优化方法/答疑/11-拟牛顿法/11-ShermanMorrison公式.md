---
title: 第11章 答疑 — Sherman-Morrison 公式与 BFGS 的逆矩阵困境
subject: 最优化方法
chapter: 11
type: 答疑
topics:
  - Sherman-Morrison公式
  - Woodbury恒等式
  - BFGS
  - 矩阵求逆
  - 秩2更新
source_context:
  - file: "11-拟牛顿法-知识梳理.md"
    line: 256
    text: "两次应用 Sherman-Morrison 公式即可递推地从 H_k 得到 H_{k+1}，无需每次求解"
related_notes:
  - "[[11-拟牛顿法-知识梳理]]"
tags:
- Sherman-Morrison公式
- BFGS
- 矩阵求逆
---

# 第11章 答疑 — Sherman-Morrison 公式与 BFGS

> 问题：**为什么要学 Sherman-Morrison 公式？它解决了 BFGS 的什么困境？实际怎么用？**

> 来源：`11-拟牛顿法-知识梳理.md` 第 256 行

---

## 一、为什么需要它

### 核心矛盾

BFGS 维护的是 $B_k$（近似 Hessian $F$），但算方向需要的是**它的逆**：

$$d^{(k)} = -B_k^{-1} g^{(k)}$$

没有 Sherman-Morrison 的话，只有两条路：

| 方案 | 做法 | 代价 |
|------|------|:--:|
| 每步求解 $B_k d = -g_k$ | 直接解线性方程组 | $O(n^3)$ — 拟牛顿法的优势没了 |
| 换用 DFP，直接维护 $H_k$ | 用 DFP 公式更新 $H_k$ | 数值表现差，可能**停滞** |

BFGS 数值好但更新的是 $B$ 而非 $H$。Sherman-Morrison 正是破局关键：用 $O(n^2)$ 从 $H_k$ 递推出 $H_{k+1}$，不碰 $O(n^3)$。

---

## 二、实际计算过程（Woodbury 一步到位）

BFGS 更新 $B_{k+1} = B_k + \text{秩2修正}$。直接对秩2用 Woodbury 恒等式（Sherman-Morrison 的推广）：

$$(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}$$

把 $B_{k+1} = B_k + U M U^T$ 代入，其中 $U = [B_k s, y]_{n \times 2}$，$M$ 是对角 $2 \times 2$ 矩阵。**括号内只是一个 $2 \times 2$ 矩阵求逆**——代价 $O(1)$。

经过推导（完整手算过程见下方补充），最终得到笔记中 $H_{k+1}$ 的直接更新式：

$$H_{k+1} = (I - \rho s y^T) H_k (I - \rho y s^T) + \rho s s^T, \quad \rho = \frac{1}{y^T s}$$

---

## 三、代码实现：三步出结果

不需要推公式，已知 $H_k$、$s$、$y$，直接：

```
ρ  = 1 / (yᵀs)              ← 标量，O(n)
Hy = H_k * y                 ← 矩阵乘向量，O(n²)
H_{k+1} = H_k - ρ*Hy*sᵀ - ρ*s*Hyᵀ + (ρ + ρ²*yᵀHy)*s*sᵀ
```

全程最贵的操作是矩阵-向量乘和几次外积，$O(n^2)$。

---

## 四、更一般的价值

Sherman-Morrison / Woodbury 回答了一个通用问题：

> **给一个矩阵加低秩扰动，它的逆如何高效更新？**

答案：不需要重新求逆——用原逆矩阵加一个同样低秩的修正就行。这在 Kalman 滤波、在线岭回归、高斯过程回归等场景中反复出现。

> **Sherman-Morrison 就是"矩阵求逆版的递推公式"——已知 $A^{-1}$，$A$ 只变了低秩一点点，新逆矩阵不用重算。**

---

## 五、完整推导（追问补充）

> 补充：笔记中说"两次应用 Sherman-Morrison"包含了省略的细节。正确做法是用 **Woodbury 恒等式**一次搞定秩2。

### Step 1：把秩2校正写成 $U M U^T$

令 $\alpha = s^T B_k s$，$\beta = y^T s$，$\gamma = y^T H_k y$：

$$U = [B_k s, \; y]_{n \times 2}, \qquad M = \begin{bmatrix} -\frac{1}{\alpha} & 0 \\ 0 & \frac{1}{\beta} \end{bmatrix}$$

则 $B_{k+1} = B_k + U M U^T$。

### Step 2：Woodbury

$$H_{k+1} = B_{k+1}^{-1} = H_k - H_k U \, (M^{-1} + U^T H_k U)^{-1} \, U^T H_k$$

### Step 3：算 $2 \times 2$ 矩阵

$$U^T H_k U = \begin{bmatrix} \alpha & \beta \\ \beta & \gamma \end{bmatrix}, \quad M^{-1} = \begin{bmatrix} -\alpha & 0 \\ 0 & \beta \end{bmatrix}$$

$$M^{-1} + U^T H_k U = \begin{bmatrix} 0 & \beta \\ \beta & \beta+\gamma \end{bmatrix}$$

其逆为 $\frac{1}{-\beta^2} \begin{bmatrix} \beta+\gamma & -\beta \\ -\beta & 0 \end{bmatrix}$。

### Step 4：代回得最终式

$$H_{k+1} = H_k - \rho H_k y s^T - \rho s y^T H_k + (\rho + \rho^2 \gamma) s s^T$$

与笔记公式 $(I - \rho s y^T) H_k (I - \rho y s^T) + \rho s s^T$ 展开后一致 ✅。

---

## 相关链接

- [[11-拟牛顿法-知识梳理#八、Sherman-Morrison 公式|Sherman-Morrison 公式]]
- [[课程/归档/最优化方法/知识点解析梳理/11-拟牛顿法-知识梳理#七、BFGS 公式（秩2校正，近似 Hessian，本章核心）|BFGS 秩2校正]]
- [[11-拟牛顿法/11-秩1矫正|秩1矫正（问一）]]
