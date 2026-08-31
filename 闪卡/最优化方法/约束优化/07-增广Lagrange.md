增广Lagrange法相比罚函数法的优势？

---

$L_A(x,\lambda,\rho) = f(x) + \lambda^T h(x) + \frac{\rho}{2}\|h(x)\|^2$

**优势:** 结合 Lagrange乘子（对偶信息）和二次罚项。不需要 $\rho\to\infty$（乘子自动逼近最优乘子），避免了罚函数法的病态问题。
