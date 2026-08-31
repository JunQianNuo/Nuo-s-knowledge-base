Gauss-Legendre 求积公式的节点怎么确定？两点公式的节点和系数？

---

**节点**：$(n+1)$ 阶 Legendre 多项式 $P_{n+1}(x)$ 的 $n+1$ 个零点。

**Legendre 多项式**：$P_k(x) = \frac{1}{2^k k!} \frac{d^k}{dx^k}(x^2-1)^k$

**两点 Gauss-Legendre 公式**（$n=1$，精度 $2n+1=3$）：
$$\int_{-1}^1 f(x) dx \approx f\left(-\frac{\sqrt{3}}{3}\right) + f\left(\frac{\sqrt{3}}{3}\right)$$
节点：$x_0 = -\sqrt{3}/3 \approx -0.57735$，$x_1 = \sqrt{3}/3 \approx 0.57735$
系数：$A_0 = A_1 = 1$

**一般区间 $[a,b]$ → $[-1,1]$ 变换**：
$$x = \frac{a+b}{2} + \frac{b-a}{2}t \implies \int_a^b f(x)dx = \frac{b-a}{2}\int_{-1}^1 f\left(\frac{a+b}{2} + \frac{b-a}{2}t\right)dt$$

**截断误差**：$R[f] = \frac{f^{(2n+2)}(\xi)}{(2n+2)!} \frac{2^{2n+3}[(n+1)!]^4}{(2n+3)[(2n+2)!]^3}$