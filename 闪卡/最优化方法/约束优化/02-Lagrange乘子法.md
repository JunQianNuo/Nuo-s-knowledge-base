Lagrange乘子定理（等式约束FONC）的内容？

---

**定理:** $x^*$ 是正则局部极小点 $\Rightarrow$ 存在唯一 $\lambda^*\in\mathbb{R}^m$ 使:
$$\nabla f(x^*) = \sum_{i=1}^m \lambda_i^* \nabla h_i(x^*)$$

即 $\nabla f(x^*)$ 落在约束梯度张成的法空间内。

等价于 Lagrange函数 $L(x,\lambda)=f(x)+\lambda^T h(x)$ 的驻点条件 $\nabla_x L=0$。
