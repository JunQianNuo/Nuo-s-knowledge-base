Rayleigh 商的定义？Rayleigh 商迭代的收敛速度？

---

**定义**：已知近似特征向量 $x$，用 Rayleigh 商估计特征值：
$$\lambda \approx R(x) = \frac{x^T A x}{x^T x}$$

**原理**：$Ax \approx \lambda x$（超定方程）→ 最小化残差 $\|Ax - \lambda x\|_2$ → 得 Rayleigh 商。

**Rayleigh 商迭代算法**：
```
x ← x_0
for k = 0 to k_max:
    u ← x / ‖x‖₂    (归一化)
    λ ← uᵀAu         (Rayleigh商)
    x ← (A-λI)⁻¹u    (位移逆幂法一步)
```

**收敛速度**：**三次收敛**（$p=3$）！比幂法和逆幂法快得多。

**代价**：每步需解 $(A - \lambda I)x = u$。