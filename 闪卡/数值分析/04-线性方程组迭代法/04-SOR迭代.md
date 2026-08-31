SOR（连续超松弛）迭代的思想与公式？$\omega$ 的取值含义？

---

**核心思想**：对 Gauss-Seidel 迭代进行外推（松弛），加速收敛。

**外推公式**：
$$x_{k+1} = \gamma (G x_k + c) + (1-\gamma) x_k$$

**SOR 迭代公式**（分量形式）：
$$x_i^{(k+1)} = (1-\omega) x_i^{(k)} + \omega \cdot \frac{b_i - \sum_{j<i} a_{ij} x_j^{(k+1)} - \sum_{j>i} a_{ij} x_j^{(k)}}{a_{ii}}$$

**$\omega$ 取值**：
| $\omega$ | 含义 |
|-----------|------|
| $\omega = 1$ | **Gauss-Seidel** |
| $\omega > 1$ | **超松弛**（加速） |
| $\omega < 1$ | **欠松弛**（稳定） |

**迭代矩阵**：$G_\omega = (D + \omega L)^{-1}[(1-\omega)D - \omega U]$

**收敛条件**：$\rho(G_\omega) < 1$，且 $\omega$ 有最优值（通常 $0 < \omega < 2$）。