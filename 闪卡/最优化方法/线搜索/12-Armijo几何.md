Armijo条件的几何理解？为什么不能单独使用？

---

$f(x_k+\alpha p_k)\leq f(x_k)+c\cdot\alpha\cdot p_k^T\nabla f(x_k)$

右端是过$(0,f(x_k))$、斜率为$c\cdot p_k^T\nabla f(x_k)$的直线——要求$\phi(\alpha)$在线下方。

$c$越小 → 条件越松。$c$越大 → 要求更显著下降。

**不能单独使用:** 允许$\alpha\to 0$（Taylor展开下总是成立）。必须配合回溯或Wolfe曲率条件。
