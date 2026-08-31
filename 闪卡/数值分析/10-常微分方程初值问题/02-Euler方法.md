Euler 显式公式的两种推导方式？公式与局部截断误差？

---

**问题**：$y' = f(x,y)$，$y(x_0) = y_0$

**Euler 公式**（显式，一阶）：
$$y_{i+1} = y_i + h \cdot f(x_i, y_i)$$

**推导方式1——积分形式**：
$$y(x_{i+1}) - y(x_i) = \int_{x_i}^{x_{i+1}} f(x, y(x)) dx$$
右端用**左矩形公式** $\int_a^b g \approx (b-a)g(a)$ → Euler 公式。

**推导方式2——Taylor 展开**：
$$y(x_{i+1}) = y(x_i) + h y'(x_i) + \frac{h^2}{2} y''(\xi)$$
舍去 $h^2$ 项，$y'(x_i) = f(x_i, y_i)$ → Euler 公式。

**局部截断误差**（一阶方法）：
$$LTE = \frac{y''(\xi)}{2} h^2 = O(h^2)$$

**全局误差**：$O(h)$（积 $n = (b-a)/h$ 步）