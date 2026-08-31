KKT条件的四个组成部分？

---

$$\begin{aligned}
\text{1. 驻点: } & \nabla f + \sum\mu_j\nabla g_j + \sum\lambda_i\nabla h_i = 0 \\
\text{2. 原始可行: } & g_j(x)\leq 0,\; h_i(x)=0 \\
\text{3. 对偶可行: } & \mu_j \geq 0 \\
\text{4. 互补松弛: } & \mu_j g_j(x) = 0
\end{aligned}$$

(1)+(3)+(4) = 对偶可行 + 驻点 + 互补松弛 = KKT核心。

助记: **"驻原对互"** → 驻点 + 原始可行 + 对偶可行 + 互补松弛。口诀: KKT 就像住院(**驻原**)对照护(**对互**)的四项检查。
