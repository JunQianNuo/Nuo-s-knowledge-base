BFGS更新保持正定性需要什么条件？

---

BFGS更新: $B_{k+1}=B_k+\frac{y_k y_k^T}{y_k^T s_k}-\frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$

**正定性遗传:** 若 $B_k\succ 0$ 且 $s_k^T y_k>0$ → $B_{k+1}\succ 0$

$s_k^T y_k>0$ 由强Wolfe线搜索保证。DFP同样有此性质。这就是曲率条件在拟牛顿法中的核心作用。
