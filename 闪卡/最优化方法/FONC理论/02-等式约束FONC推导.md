等式约束FONC → Lagrange乘子定理的推导关键步骤？

---

1. 切锥 $\mathcal{T} = \ker(Dh(x^*))$（等式约束的线性化）
2. FONC: $\nabla f(x^*)^T d = 0$（$\forall d\in\mathcal{T}$）
3. $\nabla f(x^*) \perp \mathcal{T}$ → $\nabla f(x^*)\in\mathcal{T}^\perp = \mathcal{R}(Dh(x^*)^T)$
4. $\exists\lambda^*$ 使 $\nabla f(x^*) = \sum\lambda_i^*\nabla h_i(x^*)$

核心: 目标梯度必落在约束梯度的张成空间内。
