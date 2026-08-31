Simpson（抛物形）公式及其余项？代数精度是多少？

---

**Simpson 公式**（$n=2$ 的 Newton-Cotes）：
$$\int_a^b f(x) dx \approx \frac{b-a}{6}\left[f(a) + 4f\left(\frac{a+b}{2}\right) + f(b)\right]$$

或写作（$h = \frac{b-a}{2}$）：
$$\int_a^b f(x) dx \approx \frac{h}{3}[f(a) + 4f(a+h) + f(b)]$$

**求积系数**：$A_0 = h/3$，$A_1 = 4h/3$，$A_2 = h/3$

**余项**：
$$R_2[f] = -\frac{(b-a)^5}{2880} f^{(4)}(\xi) = -\frac{b-a}{180}h^4 f^{(4)}(\xi), \quad \xi \in (a,b)$$

**代数精度**：3（$n=2$ 是偶数 → 精度达 $n+1=3$）

**记忆**：分数分子 1,4,1 → 精度 3。