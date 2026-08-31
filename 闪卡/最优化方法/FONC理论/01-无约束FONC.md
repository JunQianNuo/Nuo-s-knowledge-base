无约束优化FONC的推导思路？

---

$\nabla f(x^*)=0$

若 $\nabla f(x^*)\neq 0$，取 $d=-\nabla f(x^*)$，由Taylor展开:
$f(x^*+\alpha d) = f(x^*) - \alpha\|\nabla f(x^*)\|^2 + o(\alpha) < f(x^*)$（$\alpha$充分小）

矛盾于$x^*$是局部极小点。
