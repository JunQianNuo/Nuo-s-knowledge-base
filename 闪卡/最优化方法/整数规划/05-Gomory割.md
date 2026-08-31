Gomory割平面如何从单纯形表生成？

---

在LP松弛最优表中，选一个基变量行（值为分数）:
$x_i + \sum_{j\in N}\bar{a}_{ij}x_j = \bar{b}_i$

Gomory割: $\sum_{j\in N}(\bar{a}_{ij}-\lfloor\bar{a}_{ij}\rfloor)x_j \geq \bar{b}_i-\lfloor\bar{b}_i\rfloor$

含义: 小数部分的和 $\geq$ 小数部分的值——割掉当前分数解但不割整数解。
