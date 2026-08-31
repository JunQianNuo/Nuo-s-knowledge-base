Gram-Schmidt 正交化如何实现 QR 分解？

---

**消减 QR 分解**（$A$ 为 $m \times n$，列满秩，$m \geq n$）：

1. $y_1 = A_1$，$r_{11} = \|y_1\|_2$，$q_1 = y_1 / r_{11}$
2. 对 $j = 2, \ldots, n$：
   - $r_{ij} = q_i^T A_j \quad (i < j)$
   - $y_j = A_j - \sum_{i=1}^{j-1} r_{ij} q_i$
   - $r_{jj} = \|y_j\|_2$，$q_j = y_j / r_{jj}$

**结果**：$A = QR$，$Q$ 列正交，$R$ 上三角

**完全 QR 分解**：任意添加 $m-n$ 个向量扩展为正交基，得 $m \times m$ 的 $Q$。

**注意**：经典 Gram-Schmidt 数值不稳定 → 实际用**修正 Gram-Schmidt**（MGS）。