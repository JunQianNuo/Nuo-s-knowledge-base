Gauss-Seidel 迭代的分裂矩阵 $Q$ 和迭代矩阵 $G_{GS}$？相比 Jacobi 有何改进？

---

**分裂**：$Q = D + L$（对角 + 严格下三角）

$$(D+L)x_{k+1} = -U x_k + b$$

**迭代矩阵**：$G_{GS} = -(D+L)^{-1}U$

**分量形式**：
$$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij} x_j^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)}}{a_{ii}}$$

**相比 Jacobi 的改进**：计算 $x_i^{(k+1)}$ 时使用**已更新**的 $x_j^{(k+1)}$（$j < i$），而非全部用旧值。

**收敛条件**：$A$ 严格行对角占优 $\implies$ Gauss-Seidel 收敛。

**通常比 Jacobi 更快收敛**。