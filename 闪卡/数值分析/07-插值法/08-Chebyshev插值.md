Chebyshev 插值节点的选取与误差界？区间变换公式？

---

**Chebyshev 节点**（$[-1,1]$ 区间）：取 $T_{n+1}(x)$ 的 $n+1$ 个零点：
$$x_i = \cos\frac{(2i+1)\pi}{2(n+1)}, \quad i = 0,1,\ldots,n$$

**误差界**：
$$|f(x) - P_n(x)| \leq \frac{1}{2^n (n+1)!} \max_{-1 \leq x \leq 1} |f^{(n+1)}(x)|$$

**区间变换**：$x \in [a,b] \rightarrow \tilde{x} \in [-1,1]$
$$\tilde{x} = \frac{2(x - \frac{b+a}{2})}{b-a}$$
逆变换：$x = \frac{b-a}{2}\tilde{x} + \frac{b+a}{2}$

**任意区间 $[a,b]$ 的 Chebyshev 节点**：
$$x_i = \frac{b-a}{2} \cos\frac{(2i+1)\pi}{2(n+1)} + \frac{b+a}{2}$$

**误差界**：
$$|f(x) - P_n(x)| \leq \frac{(\frac{b-a}{2})^{n+1}}{2^n (n+1)!} \max |f^{(n+1)}|$$

**记忆**：Chebyshev 节点 = $T_{n+1}$ 的零点，两端密集布局。