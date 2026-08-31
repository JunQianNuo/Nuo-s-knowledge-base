Gauss 求积公式的定义与最高代数精度？

---

**定义**：若 $n+1$ 个节点的求积公式代数精度达到 **$2n+1$**，则称为 **Gauss 求积公式**，节点称为 **Gauss 点**。

**最高代数精度**：$n+1$ 个节点最高可达 $2n+1$。

**Gauss 点充要条件**：$\omega_{n+1}(x) = \prod_{k=0}^n (x-x_k)$ 与任意 $\leq n$ 次多项式正交：
$$\int_a^b P(x) \omega_{n+1}(x) dx = 0, \quad \forall P \in \mathbb{P}_n$$

即 Gauss 点 = 正交多项式的零点！

**截断误差**（$f \in C^{2n+2}$）：
$$R[f] = \frac{f^{(2n+2)}(\xi)}{(2n+2)!} \int_a^b \omega_{n+1}^2(x) dx$$

**三种常见 Gauss 型公式**：
| 类型 | 区间 | 权函数 | 正交多项式 |
|------|------|--------|-----------|
| Gauss-Legendre | $[-1,1]$ | $\rho=1$ | Legendre $P_k$ |
| Gauss-Laguerre | $[0,+\infty)$ | $e^{-x}$ | Laguerre $L_k$ |
| Gauss-Hermite | $(-\infty,+\infty)$ | $e^{-x^2}$ | Hermite $H_k$ |