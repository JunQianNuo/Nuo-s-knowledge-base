不等式约束下KKT条件的推导关键？

---

1. 积极约束集 $\mathcal{J}(x^*)=\{j\mid g_j(x^*)=0\}$
2. 线性化切锥: $d$满足 $Dh d=0$ 且 $\nabla g_j^T d\leq 0$（$j\in\mathcal{J}$）
3. FONC + Farkas引理 → $\nabla f \in -\text{cone}\{\nabla g_j\} + \text{span}\{\nabla h_i\}$
4. 即存在 $\mu_j\geq 0$ 和 $\lambda_i$ 使 $\nabla f + \sum\mu_j\nabla g_j + \sum\lambda_i\nabla h_i = 0$
5. 互补松弛: 非积极约束 $\mu_j=0$$
