Armijo条件和Wolfe条件的区别？

---

**Armijo条件（充分下降）:** $f(x_k+\alpha d_k) \leq f(x_k)+c_1\alpha\nabla f(x_k)^T d_k$，$c_1\in(0,1)$

**Wolfe条件:** Armijo + 曲率条件: $\nabla f(x_k+\alpha d_k)^T d_k \geq c_2\nabla f(x_k)^T d_k$，$0<c_1<c_2<1$

**强Wolfe条件:** 曲率条件改为 $|\nabla f(x_k+\alpha d_k)^T d_k| \leq c_2|\nabla f(x_k)^T d_k|$

强Wolfe保证 $s_k^T y_k > 0$，对拟牛顿法至关重要。
