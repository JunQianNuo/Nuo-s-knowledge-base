---
title: 考题-01 - DFP/BFGS公式推导计算
subject: 最优化方法
chapter: 11
section: 拟牛顿法
source: 复习纲要补充
status: 已校对
type: 考题
topics:
  - DFP公式
  - BFGS公式
  - 拟牛顿方程
  - 秩2校正
  - 对称正定性
  - 精确线搜索
tags:
- DFP公式
- BFGS公式
- 拟牛顿方程
- 秩2校正
- 精确线搜索
---

# 考题 01

考虑二次函数

$$f(x) = \frac{1}{2}x^\top \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} x - \begin{bmatrix} 4 & 2 \end{bmatrix} x$$

从初始点 $x^{(0)} = [0, 0]^\top$ 出发，初始 Hessian 逆近似取 $H_0 = I$（单位阵）。

**a.** 以方向 $d_0 = -H_0 g_0$ 进行一步精确线搜索，步长取 $\alpha_0 = -\dfrac{g_0^\top d_0}{d_0^\top Q d_0}$。计算 $x^{(1)}$。

**b.** 计算 $s_0 = x^{(1)} - x^{(0)}$ 和 $y_0 = g_1 - g_0$（其中 $g_k = \nabla f(x^{(k)})$）。

**c.** 使用 **DFP 公式**计算 $H_1^{\text{DFP}}$：

$$H_1 = H_0 + \frac{s_0 s_0^\top}{s_0^\top y_0} - \frac{H_0 y_0 y_0^\top H_0}{y_0^\top H_0 y_0}$$

**d.** 使用 **BFGS 逆更新公式**计算 $H_1^{\text{BFGS}}$：

$$H_1 = (I - \rho s_0 y_0^\top) H_0 (I - \rho y_0 s_0^\top) + \rho s_0 s_0^\top, \qquad \rho = \frac{1}{y_0^\top s_0}$$

**e.** 验证 $H_1^{\text{DFP}}$ 和 $H_1^{\text{BFGS}}$ 均满足**拟牛顿方程**（割线方程）$H_1 y_0 = s_0$。

**f.** 验证 $H_1^{\text{BFGS}}$ 是对称正定矩阵。

---

## 💡 提示

> [!hint]- 点击展开提示
> **(a)** 梯度公式：$g(x) = Qx - b$，其中 $Q = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}$，$b = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$。
>
> 初始：$g_0 = \begin{bmatrix} -4 \\ -2 \end{bmatrix}$，$d_0 = -H_0 g_0 = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$。
>
> 步长：
> $$g_0^\top d_0 = -20, \quad d_0^\top Q d_0 = 72, \quad \alpha_0 = \frac{20}{72} = \frac{5}{18}$$
>
> $x^{(1)} = \frac{5}{18}\begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} 10/9 \\ 5/9 \end{bmatrix}$。
>
> **(b)** $g_1 = \begin{bmatrix} 4/9 \\ -8/9 \end{bmatrix}$，因此 $y_0 = g_1 - g_0 = \begin{bmatrix} 40/9 \\ 10/9 \end{bmatrix}$。
>
> 注意：$y_0$ 与 $s_0$ 恰成比例——这是因为 $f$ 是二次函数且 $\nabla f(x) = Qx - b$，所以 $y_0 = Q s_0$。验证 $Q s_0 = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 10/9 \\ 5/9 \end{bmatrix} = \begin{bmatrix} 40/9 \\ 10/9 \end{bmatrix} = y_0$。$\checkmark$
>
> **(c)** DFP 公式中由于 $H_0 = I$，可以简化：
> $$H_1^{\text{DFP}} = I + \frac{s s^\top}{s^\top y} - \frac{y y^\top}{y^\top y}$$
>
> 关键计算：
> - $s^\top y = \frac{50}{9}$
> - $y^\top y = \frac{1700}{81}$
>
> **(d)** BFGS 公式中同样 $H_0 = I$，注意 $\rho = 1/(y^\top s) = 9/50$。
>
> **(e)** 拟牛顿方程 $H_1 y_0 = s_0$ 是拟牛顿法的核心约束——替代牛顿法中 Hessian 逆的真实行为。
>
> **(f)** 正定性验证：检查所有顺序主子式为正。注意 BFGS 公式设计上保证 $H_k \succ 0$ 的遗传性（若 $H_{k-1} \succ 0$ 且 $s^\top y > 0$）。

---

## 📝 详细解析

> [!solution]- 点击展开详细解析
>
> ### (a) 第一步迭代
>
> 梯度：
>
> $$g(x) = \nabla f(x) = Qx - b = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} - \begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} 4x_1 - 4 \\ 2x_2 - 2 \end{bmatrix}$$
>
> 在 $x^{(0)} = [0, 0]^\top$ 处：
>
> $$g_0 = \begin{bmatrix} -4 \\ -2 \end{bmatrix}$$
>
> 搜索方向：
>
> $$d_0 = -H_0 g_0 = -\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} -4 \\ -2 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$$
>
> 精确步长：
>
> $$g_0^\top d_0 = [-4, -2] \begin{bmatrix} 4 \\ 2 \end{bmatrix} = -16 - 4 = -20$$
>
> $$Q d_0 = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} 16 \\ 4 \end{bmatrix}$$
>
> $$d_0^\top Q d_0 = [4, 2] \begin{bmatrix} 16 \\ 4 \end{bmatrix} = 64 + 8 = 72$$
>
> $$\alpha_0 = -\frac{g_0^\top d_0}{d_0^\top Q d_0} = \frac{20}{72} = \frac{5}{18}$$
>
> 更新：
>
> $$x^{(1)} = x^{(0)} + \alpha_0 d_0 = \frac{5}{18} \begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} \dfrac{10}{9} \\[8pt] \dfrac{5}{9} \end{bmatrix}$$
>
> ---
>
> ### (b) 计算 $s_0$ 和 $y_0$
>
> $$s_0 = x^{(1)} - x^{(0)} = \begin{bmatrix} \dfrac{10}{9} \\[8pt] \dfrac{5}{9} \end{bmatrix}$$
>
> 在新点处的梯度：
>
> $$g_1 = \nabla f(x^{(1)}) = \begin{bmatrix} 4 \cdot \dfrac{10}{9} - 4 \\[8pt] 2 \cdot \dfrac{5}{9} - 2 \end{bmatrix} = \begin{bmatrix} \dfrac{40}{9} - \dfrac{36}{9} \\[8pt] \dfrac{10}{9} - \dfrac{18}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{4}{9} \\[8pt] -\dfrac{8}{9} \end{bmatrix}$$
>
> $$y_0 = g_1 - g_0 = \begin{bmatrix} \dfrac{4}{9} \\[8pt] -\dfrac{8}{9} \end{bmatrix} - \begin{bmatrix} -4 \\ -2 \end{bmatrix} = \begin{bmatrix} \dfrac{4}{9} + \dfrac{36}{9} \\[8pt] -\dfrac{8}{9} + \dfrac{18}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{40}{9} \\[8pt] \dfrac{10}{9} \end{bmatrix}$$
>
> 验证（二次函数性质）：$Q s_0 = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 10/9 \\ 5/9 \end{bmatrix} = \begin{bmatrix} 40/9 \\ 10/9 \end{bmatrix} = y_0$。$\checkmark$
>
> 预备标量：
>
> $$s_0^\top y_0 = \frac{10}{9} \cdot \frac{40}{9} + \frac{5}{9} \cdot \frac{10}{9} = \frac{400}{81} + \frac{50}{81} = \frac{450}{81} = \frac{50}{9}$$
>
> $$y_0^\top y_0 = \left(\frac{40}{9}\right)^2 + \left(\frac{10}{9}\right)^2 = \frac{1600}{81} + \frac{100}{81} = \frac{1700}{81}$$
>
> ---
>
> ### (c) DFP 更新
>
> 由于 $H_0 = I$，DFP 公式简化为：
>
> $$H_1^{\text{DFP}} = I + \frac{s_0 s_0^\top}{s_0^\top y_0} - \frac{y_0 y_0^\top}{y_0^\top y_0}$$
>
> **第一项：** $\dfrac{s_0 s_0^\top}{s_0^\top y_0}$
>
> $$s_0 s_0^\top = \begin{bmatrix} \dfrac{10}{9} \\[4pt] \dfrac{5}{9} \end{bmatrix} \begin{bmatrix} \dfrac{10}{9} & \dfrac{5}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{100}{81} & \dfrac{50}{81} \\[8pt] \dfrac{50}{81} & \dfrac{25}{81} \end{bmatrix}$$
>
> $$\frac{s_0 s_0^\top}{s_0^\top y_0} = \frac{1}{50/9} \begin{bmatrix} 100/81 & 50/81 \\ 50/81 & 25/81 \end{bmatrix} = \frac{9}{50} \cdot \frac{1}{81} \begin{bmatrix} 100 & 50 \\ 50 & 25 \end{bmatrix} = \frac{1}{450} \begin{bmatrix} 100 & 50 \\ 50 & 25 \end{bmatrix} = \begin{bmatrix} \dfrac{2}{9} & \dfrac{1}{9} \\[8pt] \dfrac{1}{9} & \dfrac{1}{18} \end{bmatrix}$$
>
> **第二项：** $\dfrac{y_0 y_0^\top}{y_0^\top y_0}$
>
> $$y_0 y_0^\top = \begin{bmatrix} \dfrac{40}{9} \\[4pt] \dfrac{10}{9} \end{bmatrix} \begin{bmatrix} \dfrac{40}{9} & \dfrac{10}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{1600}{81} & \dfrac{400}{81} \\[8pt] \dfrac{400}{81} & \dfrac{100}{81} \end{bmatrix}$$
>
> $$\frac{y_0 y_0^\top}{y_0^\top y_0} = \frac{1}{1700/81} \begin{bmatrix} 1600/81 & 400/81 \\ 400/81 & 100/81 \end{bmatrix} = \frac{81}{1700} \cdot \frac{1}{81} \begin{bmatrix} 1600 & 400 \\ 400 & 100 \end{bmatrix} = \begin{bmatrix} \dfrac{16}{17} & \dfrac{4}{17} \\[8pt] \dfrac{4}{17} & \dfrac{1}{17} \end{bmatrix}$$
>
> **合并：**
>
> $$H_1^{\text{DFP}} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} \dfrac{2}{9} & \dfrac{1}{9} \\[4pt] \dfrac{1}{9} & \dfrac{1}{18} \end{bmatrix} - \begin{bmatrix} \dfrac{16}{17} & \dfrac{4}{17} \\[4pt] \dfrac{4}{17} & \dfrac{1}{17} \end{bmatrix}$$
>
> 逐元素计算：
>
> - $H_{11} = 1 + \dfrac{2}{9} - \dfrac{16}{17} = 1 + \dfrac{34}{153} - \dfrac{144}{153} = \dfrac{43}{153}$
> - $H_{12} = H_{21} = 0 + \dfrac{1}{9} - \dfrac{4}{17} = \dfrac{17}{153} - \dfrac{36}{153} = -\dfrac{19}{153}$
> - $H_{22} = 1 + \dfrac{1}{18} - \dfrac{1}{17} = 1 + \dfrac{17}{306} - \dfrac{18}{306} = \dfrac{305}{306}$
>
> $$\boxed{H_1^{\text{DFP}} = \begin{bmatrix} \dfrac{43}{153} & -\dfrac{19}{153} \\[8pt] -\dfrac{19}{153} & \dfrac{305}{306} \end{bmatrix}}$$
>
> ---
>
> ### (d) BFGS 逆更新
>
> $\rho = \dfrac{1}{y_0^\top s_0} = \dfrac{9}{50}$。
>
> 先计算 $I - \rho s_0 y_0^\top$ 和 $I - \rho y_0 s_0^\top$（注意 $H_0 = I$）：
>
> $$\rho s_0 y_0^\top = \frac{9}{50} \begin{bmatrix} \dfrac{10}{9} \\[4pt] \dfrac{5}{9} \end{bmatrix} \begin{bmatrix} \dfrac{40}{9} & \dfrac{10}{9} \end{bmatrix} = \frac{1}{450} \begin{bmatrix} 400 & 100 \\ 200 & 50 \end{bmatrix} = \begin{bmatrix} \dfrac{8}{9} & \dfrac{2}{9} \\[8pt] \dfrac{4}{9} & \dfrac{1}{9} \end{bmatrix}$$
>
> $$\rho y_0 s_0^\top = \frac{9}{50} \begin{bmatrix} \dfrac{40}{9} \\[4pt] \dfrac{10}{9} \end{bmatrix} \begin{bmatrix} \dfrac{10}{9} & \dfrac{5}{9} \end{bmatrix} = \frac{1}{450} \begin{bmatrix} 400 & 200 \\ 100 & 50 \end{bmatrix} = \begin{bmatrix} \dfrac{8}{9} & \dfrac{4}{9} \\[8pt] \dfrac{2}{9} & \dfrac{1}{9} \end{bmatrix}$$
>
> 因此：
>
> $$I - \rho s_0 y_0^\top = \begin{bmatrix} 1 - \dfrac{8}{9} & -\dfrac{2}{9} \\[8pt] -\dfrac{4}{9} & 1 - \dfrac{1}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{1}{9} & -\dfrac{2}{9} \\[8pt] -\dfrac{4}{9} & \dfrac{8}{9} \end{bmatrix}$$
>
> $$I - \rho y_0 s_0^\top = \begin{bmatrix} 1 - \dfrac{8}{9} & -\dfrac{4}{9} \\[8pt] -\dfrac{2}{9} & 1 - \dfrac{1}{9} \end{bmatrix} = \begin{bmatrix} \dfrac{1}{9} & -\dfrac{4}{9} \\[8pt] -\dfrac{2}{9} & \dfrac{8}{9} \end{bmatrix}$$
>
> 中间乘积：
>
> $$(I - \rho s y^\top)(I)(I - \rho y s^\top) = \begin{bmatrix} \dfrac{1}{9} & -\dfrac{2}{9} \\[8pt] -\dfrac{4}{9} & \dfrac{8}{9} \end{bmatrix} \begin{bmatrix} \dfrac{1}{9} & -\dfrac{4}{9} \\[8pt] -\dfrac{2}{9} & \dfrac{8}{9} \end{bmatrix}$$
>
> $$= \frac{1}{81} \begin{bmatrix} 1 & -2 \\ -4 & 8 \end{bmatrix} \begin{bmatrix} 1 & -4 \\ -2 & 8 \end{bmatrix}$$
>
> $$= \frac{1}{81} \begin{bmatrix} 1 \cdot 1 + (-2)(-2) & 1 \cdot (-4) + (-2) \cdot 8 \\ (-4) \cdot 1 + 8 \cdot (-2) & (-4)(-4) + 8 \cdot 8 \end{bmatrix}$$
>
> $$= \frac{1}{81} \begin{bmatrix} 5 & -20 \\ -20 & 80 \end{bmatrix} = \begin{bmatrix} \dfrac{5}{81} & -\dfrac{20}{81} \\[8pt] -\dfrac{20}{81} & \dfrac{80}{81} \end{bmatrix}$$
>
> 加上 $\rho s_0 s_0^\top$：
>
> $$\rho s_0 s_0^\top = \frac{9}{50} \cdot \frac{1}{81} \begin{bmatrix} 100 & 50 \\ 50 & 25 \end{bmatrix} = \frac{1}{450} \begin{bmatrix} 100 & 50 \\ 50 & 25 \end{bmatrix} = \begin{bmatrix} \dfrac{2}{9} & \dfrac{1}{9} \\[8pt] \dfrac{1}{9} & \dfrac{1}{18} \end{bmatrix}$$
>
> 合并：
>
> $$H_1^{\text{BFGS}} = \begin{bmatrix} \dfrac{5}{81} & -\dfrac{20}{81} \\[8pt] -\dfrac{20}{81} & \dfrac{80}{81} \end{bmatrix} + \begin{bmatrix} \dfrac{2}{9} & \dfrac{1}{9} \\[8pt] \dfrac{1}{9} & \dfrac{1}{18} \end{bmatrix}$$
>
> 化为分母 $81$（$\dfrac{1}{9} = \dfrac{9}{81}$，$\dfrac{1}{18} = \dfrac{4.5}{81}$）：
>
> $$H_1^{\text{BFGS}} = \begin{bmatrix} \dfrac{5 + 18}{81} & \dfrac{-20 + 9}{81} \\[8pt] \dfrac{-20 + 9}{81} & \dfrac{80 + 4.5}{81} \end{bmatrix} = \begin{bmatrix} \dfrac{23}{81} & -\dfrac{11}{81} \\[8pt] -\dfrac{11}{81} & \dfrac{84.5}{81} \end{bmatrix} = \begin{bmatrix} \dfrac{23}{81} & -\dfrac{11}{81} \\[8pt] -\dfrac{11}{81} & \dfrac{169}{162} \end{bmatrix}$$
>
> $$\boxed{H_1^{\text{BFGS}} = \begin{bmatrix} \dfrac{23}{81} & -\dfrac{11}{81} \\[8pt] -\dfrac{11}{81} & \dfrac{169}{162} \end{bmatrix}}$$
>
> ---
>
> ### (e) 验证拟牛顿方程 $H_1 y_0 = s_0$
>
> **DFP 验证：**
>
> $$H_1^{\text{DFP}} y_0 = \begin{bmatrix} \dfrac{43}{153} & -\dfrac{19}{153} \\[8pt] -\dfrac{19}{153} & \dfrac{305}{306} \end{bmatrix} \begin{bmatrix} \dfrac{40}{9} \\[8pt] \dfrac{10}{9} \end{bmatrix}$$
>
> 第一分量：
> $$\frac{43}{153} \cdot \frac{40}{9} + \left(-\frac{19}{153}\right) \cdot \frac{10}{9} = \frac{1720 - 190}{1377} = \frac{1530}{1377} = \frac{170}{153} = \frac{10}{9}$$
>
> 第二分量：
> $$-\frac{19}{153} \cdot \frac{40}{9} + \frac{305}{306} \cdot \frac{10}{9} = -\frac{760}{1377} + \frac{3050}{2754} = \frac{-1520 + 3050}{2754} = \frac{1530}{2754} = \frac{5}{9}$$
>
> $$H_1^{\text{DFP}} y_0 = \begin{bmatrix} \dfrac{10}{9} \\[8pt] \dfrac{5}{9} \end{bmatrix} = s_0 \quad \checkmark$$
>
> **BFGS 验证：**
>
> $$H_1^{\text{BFGS}} y_0 = \begin{bmatrix} \dfrac{23}{81} & -\dfrac{11}{81} \\[8pt] -\dfrac{11}{81} & \dfrac{169}{162} \end{bmatrix} \begin{bmatrix} \dfrac{40}{9} \\[8pt] \dfrac{10}{9} \end{bmatrix}$$
>
> 第一分量：
> $$\frac{23 \cdot 40}{81 \cdot 9} + \frac{-11 \cdot 10}{81 \cdot 9} = \frac{920 - 110}{729} = \frac{810}{729} = \frac{10}{9}$$
>
> 第二分量：
> $$-\frac{11 \cdot 40}{81 \cdot 9} + \frac{169 \cdot 10}{162 \cdot 9} = -\frac{440}{729} + \frac{1690}{1458} = \frac{-880 + 1690}{1458} = \frac{810}{1458} = \frac{5}{9}$$
>
> $$H_1^{\text{BFGS}} y_0 = \begin{bmatrix} \dfrac{10}{9} \\[8pt] \dfrac{5}{9} \end{bmatrix} = s_0 \quad \checkmark$$
>
> 两种更新均满足拟牛顿方程。
>
> ---
>
> ### (f) 验证 $H_1^{\text{BFGS}}$ 对称正定
>
> **对称性：** $H_{12} = H_{21} = -\dfrac{11}{81}$。$\checkmark$
>
> **正定性**（顺序主子式法）：
>
> 一阶顺序主子式：
> $$H_{11} = \frac{23}{81} > 0 \quad \checkmark$$
>
> 二阶顺序主子式（行列式）：
>
> $$\det(H_1^{\text{BFGS}}) = \frac{23}{81} \cdot \frac{169}{162} - \left(-\frac{11}{81}\right)^2 = \frac{3887}{13122} - \frac{121}{6561}$$
>
> $$= \frac{3887}{13122} - \frac{242}{13122} = \frac{3645}{13122} > 0 \quad \checkmark$$
>
> 两顺序主子式均大于零，故 $H_1^{\text{BFGS}} \succ 0$（对称正定）。$\checkmark$
>
> ---
>
> **点评：** 本题完整呈现了拟牛顿法的核心操作流程。关键观察：
> 1. 对于二次函数，$y_0 = Q s_0$ 精确成立——这是二次函数特有的性质，拟牛顿法的有限步收敛证明即依赖于此。
> 2. DFP 和 BFGS 均是对称秩 2 校正公式，都满足拟牛顿方程 $H_1 y_0 = s_0$，但 BFGS 具有更好的数值稳定性（对非精确线搜索也更鲁棒），实际应用中 BFGS 更受欢迎。
> 3. 两种更新均保持 $H_k$ 的对称正定性（只要 $H_{k-1} \succ 0$ 且 $s^\top y > 0$，后者由精确线搜索或 Wolfe 条件保证）。
> 4. 对于 $n = 2$ 的二次函数，拟牛顿法配合精确线搜索最多 $n = 2$ 步收敛到极小点（即 $H_2 = Q^{-1}$，且 $x^{(2)} = x^*$）。本题只进行了一步后的 Hessian 近似更新。
>
> $\square$

---

## 相关知识点

- [[11-拟牛顿法#拟牛顿法的基本思想|拟牛顿法的基本思想]] — 割线方程与 Hessian 近似
- [[11-拟牛顿法#DFP校正|DFP 公式]] — 秩 2 校正公式及推导
- [[11-拟牛顿法#BFGS校正|BFGS 公式]] — 逆更新公式及推导
- [[../知识点解析梳理/11-拟牛顿法-知识梳理|第11章 知识梳理]] — 拟牛顿法系统梳理
- [[../复习/IV-无约束优化|IV-无约束优化]] — 无约束优化复习纲要
- [[09-牛顿法]] — 拟牛顿法是对牛顿法的改进（避免 Hessian 计算与求逆）
- [[08-梯度方法]] — 拟牛顿法在最速下降方向（$H_0 = I$ 时）与牛顿方向之间插值
