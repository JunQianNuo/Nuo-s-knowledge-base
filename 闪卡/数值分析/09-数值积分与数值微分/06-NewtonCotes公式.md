Newton-Cotes 公式的求积系数表达式？偶数阶 N-C 公式为何精度多 1？

---

**Newton-Cotes 公式**（等距节点）：
$$A_k = (b-a) C_k^{(n)}$$

Newton-Cotes 系数：
$$C_k^{(n)} = \frac{(-1)^{n-k}}{n \cdot (n-k)! \cdot k!} \int_0^n t(t-1)\cdots(t-n)/(t-k) \, dt$$

**余项**（$f \in C^{n+1}$）：
$$R_n[f] = \int_a^b \frac{f^{(n+1)}(\xi)}{(n+1)!} \omega(x) dx$$

**偶数阶精度 +1**：$n$ 为偶数时，代数精度 = $n+1$

**证明关键**：$n=2k$，对 $n+1$ 次多项式 $q$：
$$R[q] = a_{n+1} \int_0^{2k} h^{n+2} \, t(t-1)\cdots(t-2k) \, dt$$
作变换 $u = t-k$ → 被积函数 $\psi(u)$ 为**奇函数** → 积分 = 0

**实用**：$n=2k$ 和 $n=2k+1$ 代数精度相同 → 只用偶数阶（如 $n=2$ Simpson）。