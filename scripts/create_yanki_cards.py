#!/usr/bin/env python3
"""Generate Yanki flashcard .md files for Unconstrained Optimization."""
import os

DIR = r"D:\知识库\课程\最优化方法\闪卡\无约束优化"
os.makedirs(DIR, exist_ok=True)

def write_card(filename, front, back):
    path = os.path.join(DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(front + "\n\n---\n\n" + back + "\n")
    return path

cards = []

# ========== 收敛阶 ==========
cards.append(("01-收敛阶-定义.md",
    "收敛阶的数学定义是什么？",
    r"$\displaystyle\lim_{k\to\infty}\frac{\|x_{k+1}-x^*\|}{\|x_k-x^*\|^p}=L\in(0,\infty)$，$p$ 为收敛阶。"))

cards.append(("02-收敛阶-四种类型.md",
    "四种收敛类型及其 $p, L$ 取值？",
    r"""| 类型 | $p$ | $L$ | 表现 |
|------|:---:|:---:|------|
| 次线性 | $1$ | $1$ | 越来越慢，如 $1/k$ |
| 线性 | $1$ | $(0,1)$ | 每步按固定比例缩小 |
| 超线性 | $1$ | $0$（或 $p>1$） | 比线性快 |
| 二次 | $2$ | — | 每步误差平方缩小 |

助记: "次线=1/1, 线=1/分数, 超线=1/0, 二次=2" → $p$ 逐级升高。"""))

cards.append(("03-收敛阶-数值表现.md",
    "线性收敛 vs 二次收敛的数值表现差异？",
    r"""- 线性: $10^{-1} \to 10^{-2} \to 10^{-3} \to 10^{-4}$（每步减少一个数量级）
- 二次: $10^{-1} \to 10^{-2} \to 10^{-4} \to 10^{-8}$（有效数字翻倍）"""))

# ========== 梯度下降法 ==========
cards.append(("04-梯度-迭代格式.md",
    "梯度下降法和最速下降法的区别？",
    r"""梯度下降法: $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$（步长可固定、衰减、精确搜索）

最速下降法: 梯度下降 + 精确线搜索 $\alpha_k=\arg\min_{\alpha\geq 0}f(x_k-\alpha\nabla f(x_k))$

区别仅在步长选取方式，搜索方向相同。"""))

cards.append(("05-梯度-锯齿现象.md",
    "最速下降法的锯齿现象是什么？",
    r"""相邻梯度正交: $\nabla f(x_{k+1})\perp\nabla f(x_k)$

令 $\phi(\alpha)=f(x_k-\alpha\nabla f(x_k))$，$\alpha_k$ 是极小点 ⇒ $\phi'(\alpha_k)=0$，链式法则得 $-\nabla f(x_{k+1})^T\nabla f(x_k)=0$。"""))

cards.append(("06-梯度-收敛率.md",
    "最速下降法在二次函数上的收敛率公式？",
    r"""$V(x_{k+1})\leq\left(\frac{\lambda_{\max}-\lambda_{\min}}{\lambda_{\max}+\lambda_{\min}}\right)^2 V(x_k)$

记 $c=\left(\frac{\kappa-1}{\kappa+1}\right)^2$，$\kappa=\frac{\lambda_{\max}}{\lambda_{\min}}$ 是条件数。
- $\kappa=1$: $c=0$，一步收敛
- $\kappa=100$: $c\approx 0.96$，极慢（病态）"""))

cards.append(("07-梯度-定步长条件.md",
    "定步长梯度法收敛的充要条件？",
    r"$\alpha\in\left(0,\frac{2}{\lambda_{\max}(Q)}\right)$，区间内保证收敛，区间外存在发散反例。"))

# ========== 牛顿法 ==========
cards.append(("08-牛顿-迭代格式.md",
    "牛顿法的迭代格式？",
    r"$x_{k+1}=x_k-[\nabla^2 f(x_k)]^{-1}\nabla f(x_k)$，记 $H_k=\nabla^2 f(x_k)$，$g_k=\nabla f(x_k)$。实践中解 $H_k d_k=-g_k$。"))

cards.append(("09-牛顿-推导理解.md",
    "如何一句话理解牛顿法的推导？",
    r"在 $x_k$ 处做二阶 Taylor 展开构造二次模型，直接取该模型的极小点为 $x_{k+1}$。若 $f$ 是二次函数，一步到位。"))

cards.append(("10-牛顿-局部二阶收敛.md",
    "牛顿法局部二阶收敛定理的条件？",
    r"""$f\in C^3$，$\nabla f(x^*)=0$，$\nabla^2 f(x^*)$ 可逆，$x_0$ 充分靠近 $x^*$。

此时 $\|x_{k+1}-x^*\|\leq c_1 c_2\|x_k-x^*\|^2$（至少 2 阶收敛）。

关键词: **至少 2 阶**、**局部**（需要近解）。"""))

cards.append(("11-牛顿-下降方向条件.md",
    "牛顿方向什么时候是 / 不是下降方向？",
    r"""- 是下降方向: 当 $H_k\succ 0$（Hessian 正定），$\phi'(0)=-g_k^T H_k^{-1}g_k<0$
- 不是下降方向: 当 $H_k$ 非正定时 → 牛顿法需要修正的根本原因"""))

cards.append(("12-牛顿-LM修正.md",
    "Levenberg-Marquardt 修正的迭代格式和参数含义？",
    r"""$x_{k+1}=x_k-[H_k+\lambda I]^{-1}g_k$

- $\lambda\to 0$: 趋近牛顿法（二次收敛）
- $\lambda\to\infty$: 趋近梯度法（线性收敛）"""))

cards.append(("13-牛顿-高斯牛顿法.md",
    "高斯-牛顿法用于什么问题？迭代格式？",
    r"""非线性最小二乘 $\min_x\frac12\sum_{i=1}^m[r_i(x)]^2$

$x_{k+1}=x_k-[J(x_k)^T J(x_k)]^{-1}J(x_k)^T r(x_k)$

核心: 用 $J^T J$ 近似 Hessian，省略含 $r$ 二阶导的 $S(x)$ 项。真实 Hessian: $\nabla^2 f=J^T J+S(x)$。"""))

# ========== 共轭梯度法 ==========
cards.append(("14-CG-Q共轭定义.md",
    "$Q$-共轭向量的定义？",
    r"设 $Q\in S_{++}^n$，非零向量组 $\{p_0,\dots,p_m\}$ 满足 $p_i^T Q p_j=0$（$\forall i\neq j$）。$Q=I$ 时退化为普通正交。$n$ 个 $n$ 维 $Q$-共轭非零向量构成 $\mathbb{R}^n$ 的一组基。"))

cards.append(("15-CG-n步收敛.md",
    "共轭方向法的 $n$ 步收敛定理？",
    r"$x_n=x^*$。前提: $f(x)=\frac12 x^T Q x-b^T x$，$\{p_i\}$ 是 $Q$-共轭方向组，精确线搜索。对任意初始点至多 $n$ 次迭代得精确极小点。"))

cards.append(("16-CG-扩展子空间.md",
    "扩展子空间定理的内容和含义？",
    r"""$x_{k+1}=\arg\min_{x\in V_k}f(x)$，$V_k=x_0+\text{span}\{p_0,\dots,p_k\}$

每步得到逐渐扩大的子空间上的全局最优解——步子不浪费。$k=n-1$ 时覆盖全空间。

推论: $g_{k+1}^T p_i=0$（$\forall 0\leq i\leq k$），梯度与历史方向正交。"""))

cards.append(("17-CG-四种beta公式.md",
    "共轭梯度法的四种 $\\beta$ 公式？哪种最稳定？",
    r"""| 名称 | 公式 | 特点 |
|------|------|------|
| HS | $\frac{g_{k+1}^T[g_{k+1}-g_k]}{p_k^T[g_{k+1}-g_k]}$ | 直接推导 |
| PR | $\frac{g_{k+1}^T[g_{k+1}-g_k]}{g_k^T g_k}$ | 分母 $\|g_k\|^2$ |
| **FR** | $\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$ | **最稳定** |
| DY | $\frac{g_{k+1}^T g_{k+1}}{p_k^T[g_{k+1}-g_k]}$ | 近年变体 |

对二次函数等价，非线性时 **FR 首选**。助记: FR = "Fully Reciprocal"。"""))

cards.append(("18-CG-非线性区别.md",
    "非线性 CG 与线性 CG 的四个关键区别？",
    r"""1. 使用不含 $Q$ 的 $\beta$ 公式（FR/PR/HS/DY）
2. 线搜索用非精确线搜索
3. 共轭性和正交性不再精确成立
4. 需要 restart（通常每 $n$ 步或连续梯度不够正交时）"""))

# ========== 拟牛顿法 ==========
cards.append(("19-QN-动机.md",
    "拟牛顿法的核心动机？",
    r"避免牛顿法每步 $O(n^3)$ 计算 Hessian 并求逆。用一阶信息迭代更新矩阵逼近 Hessian（或其逆），实现超线性收敛，每步仅 $O(n^2)$。"))

cards.append(("20-QN-割线方程.md",
    "拟牛顿方程（割线方程）的两种版本？$s_k, y_k$ 的定义？",
    r"""$s_k=x_k-x_{k+1}$，$y_k=g_k-g_{k+1}$

| 版本 | 方程 |
|------|------|
| 版本1（近似 $[\nabla^2 f]^{-1}$） | $H_{k+1}y_k=s_k$ |
| 版本2（近似 $\nabla^2 f$） | $B_{k+1}s_k=y_k$ |

$n$ 个方程、$n(n+1)/2$ 个未知数 → 无数解。"""))

cards.append(("21-QN-曲率条件.md",
    "曲率条件是什么？如何保证？",
    r"$s_k^T y_k>0$。保证拟牛顿更新后矩阵保持正定。使用强 Wolfe 线搜索时恒成立。"))

cards.append(("22-QN-秩1校正.md",
    "秩1校正公式及其缺陷？",
    r"""$H_{k+1}=H_k+\frac{(s_k-H_k y_k)(s_k-H_k y_k)^T}{y_k^T(s_k-H_k y_k)}$

缺陷: 不保证正定性，分母可能接近零。实践中已被秩2公式取代。"""))

cards.append(("23-QN-DFP.md",
    "DFP 公式及其结构？",
    r"""$H_{k+1}^{\text{DFP}}=H_k+\frac{s_k s_k^T}{s_k^T y_k}-\frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}$

结构: 1) $H_k$ 上一步近似 2) $+\frac{s s^T}{s^T y}$ 正贡献项 3) $-\frac{H_k y y^T H_k}{y^T H_k y}$ 负修正项

秩2校正，近似 Hessian 逆。性质: 正定性遗传。"""))

cards.append(("24-QN-BFGS.md",
    "BFGS 公式（Hessian 版）？为什么是首选？",
    r"""$B_{k+1}^{\text{BFGS}}=B_k+\frac{y_k y_k^T}{y_k^T s_k}-\frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$

秩2校正，近似 Hessian（非逆）。对 Rosenbrock 只需 34 步（vs SD 的 5264 步），接近牛顿法的 21 步。

公认表现最好的拟牛顿公式。"""))

cards.append(("25-QN-共轭特征定理.md",
    "拟牛顿法的共轭特征定理？",
    r"""在强凸二次函数上，若 $H_{k+1}y_k=s_k$ 每步成立且步长非零，则 $\{d_k=-H_k g_k\}$ 是 $Q$-共轭向量组。

推论: 拟牛顿法在二次函数上至多 $n$ 步收敛。

拟牛顿法本质上是"隐式"的共轭梯度法——不需显式构造共轭方向，通过拟牛顿方程自动实现。"""))

cards.append(("26-QN-DFPvsBFGS.md",
    "DFP vs BFGS 的核心区别？",
    r"""| 维度 | DFP | BFGS |
|------|-----|------|
| 近似对象 | $H_k\approx[\nabla^2 f]^{-1}$ | $B_k\approx\nabla^2 f$ |
| 方向计算 | $d_k=-H_k g_k$ 直接 | 需解 $B_k d_k=-g_k$ |
| 对偶关系 | $H\leftrightarrow B$, $s\leftrightarrow y$ 互换 | |
| 数值表现 | 大规模可能停滞 | 更稳健，首选 |

实践中首选 BFGS（或 L-BFGS 有限内存版）。"""))

# ========== 对比与决策 ==========
cards.append(("27-对比-Rosenbrock.md",
    "Rosenbrock 函数上各方法分别需要多少步？",
    r"""$f(x_1,x_2)=100(x_2-x_1^2)^2+(1-x_1)^2$，收敛到 $\|g\|_\infty<10^{-5}$:

| 方法 | 步数 | 每步计算量 |
|------|:---:|:---:|
| 最速下降法 | 5264 | $O(n)$ |
| 非线性 CG (FR) | ~50-100 | $O(n)$ |
| BFGS | 34 | $O(n^2)$ |
| 牛顿法 | 21 | $O(n^3)$ |

BFGS 以 $O(n^2)$ 实现接近 $O(n^3)$ 牛顿法的速度。"""))

cards.append(("28-对比-决策流程.md",
    "无约束优化方法选择的决策流程？",
    r"""1. $n$ 很大 + 低精度: BB 方法或 SGD（$O(n)$）
2. $n$ 很大 + 需精度: 非线性 CG（FR + restart）
3. $n$ 中等: BFGS（首选，超线性收敛）
4. $n$ 小 + Hessian 可计算 + 近解: 牛顿法（二次收敛）
5. $n$ 小 + Hessian 不正定: L-M 修正
6. 非线性最小二乘: 高斯-牛顿法或 L-M 修正"""))

# ========== 易错点 ==========
cards.append(("29-易错-梯度vs最速下降.md",
    "梯度下降法 = 最速下降法 吗？",
    "≠。梯度下降法是方法族，最速下降法是采用精确线搜索的特例。区别仅在步长选取方式。"))

cards.append(("30-易错-最速是局部的.md",
    "最速下降法中的最速是全局还是局部概念？",
    "局部概念。仅指在当前点沿负梯度方向一阶下降速率最快。全局收敛速度是线性的，远不如牛顿法（二次收敛）。"))

cards.append(("31-易错-牛顿是局部的.md",
    "牛顿法的二次收敛是全局性质吗？",
    "不是，是局部性质。需要 $x_0$ 充分靠近 $x^*$。远离解时可能发散。这是阻尼牛顿法和 L-M 修正的设计动机。"))

cards.append(("32-易错-牛顿方向不总下降.md",
    "牛顿方向一定是下降方向吗？",
    r"不一定。仅当 Hessian 对称正定时才是下降方向。非正定时 $d_k=-H_k^{-1}g_k$ 可能指向上升方向或鞍点方向。"))

cards.append(("33-易错-共轭不意味着正交.md",
    "$Q$-共轭 = 正交 吗？",
    r"≠。$p_i^T Q p_j=0$ 不意味着 $p_i^T p_j=0$。仅 $Q=I$ 时两者重合。"))

cards.append(("34-易错-n步收敛仅二次.md",
    r"共轭方向法的 $n$ 步收敛对一般非线性函数成立吗？",
    r"不成立。前提是 $f(x)=\frac12 x^T Q x-b^T x$ 且精确线搜索。非线性时不能保证。"))

cards.append(("35-易错-beta不等价.md",
    r"非线性 CG 中四种 $\beta$ 公式始终等价吗？",
    "不等价。对二次函数等价，对非线性函数不等价。FR 数值最稳定，推荐默认使用。"))

cards.append(("36-易错-曲率条件不可忽略.md",
    "拟牛顿法中 $s_k^T y_k>0$ 可以忽略吗？",
    "不可忽略。否则矩阵可能不正定。用强 Wolfe 线搜索保证。"))

cards.append(("37-易错-秩1不可用.md",
    "秩1校正可以用于生产代码吗？",
    r"不可以。即使极小化二次函数也可能 $H_{k+1}\not\succ 0$。用 DFP 或 BFGS 等秩2校正。"))

# Write all cards
for filename, front, back in cards:
    write_card(filename, front, back)
    print(f"  OK  {filename}")

print(f"\nDone! {len(cards)} cards -> {DIR}")
