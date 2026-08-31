BFGS 公式（Hessian 版）？为什么是首选？

---

$B_{k+1}^{\text{BFGS}}=B_k+\frac{y_k y_k^T}{y_k^T s_k}-\frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$

秩2校正，近似 Hessian（非逆）。对 Rosenbrock 只需 34 步（vs SD 的 5264 步），接近牛顿法的 21 步。

公认表现最好的拟牛顿公式。
