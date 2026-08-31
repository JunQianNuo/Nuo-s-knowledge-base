Lagrange 插值基函数的构造？插值多项式公式？

---

**Lagrange 基函数**（满足 $l_i(x_j) = \delta_{ij}$）：
$$l_i(x) = \frac{(x-x_0)\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_n)}{(x_i-x_0)\cdots(x_i-x_{i-1})(x_i-x_{i+1})\cdots(x_i-x_n)}$$

**插值多项式**：
$$P_n(x) = \sum_{i=0}^n f(x_i) \cdot l_i(x)$$

**优点**：构造简单直接，系数即函数值（$a_i = f(x_i)$）。

**缺点**：每增加一个节点需重算所有基函数。