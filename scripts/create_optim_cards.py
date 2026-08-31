#!/usr/bin/env python3
"""Generate Yanki flashcards for 最优化方法 (remaining chapters)."""
import os

DIR = r"D:\知识库\闪卡\最优化方法"
os.makedirs(DIR, exist_ok=True)

def card(subfolder, filename, front, back):
    d = os.path.join(DIR, subfolder)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, filename), 'w', encoding='utf-8') as f:
        f.write(front + "\n\n---\n\n" + back + "\n")

# ===== I-预备知识 (8 cards) =====
sf = lambda f, front, back: card("预备知识", f, front, back)

sf("01-线性无关.md",
    "线性无关与线性相关的定义？",
    """线性无关: $\\sum \\alpha_i a_i = 0 \\Rightarrow \\alpha_i = 0$（只有零解），无冗余方向。

线性相关: 存在不全为零的 $\\alpha_i$ 使 $\\sum \\alpha_i a_i = 0$，至少一个向量可被其余表示。

一句话: 线性无关 = 每个向量都提供了新方向；线性相关 = 有冗余。""")

sf("02-四大子空间.md",
    "矩阵的四大基本子空间及其维数？",
    """| 空间 | 记法 | 定义 | 维数 |
|------|------|------|:---:|
| 值域（列空间） | $\\mathcal{R}(A)$ | $\\{Ax \\mid x\\in\\mathbb{R}^n\\}$ | $\\text{rank}(A)$ |
| 零空间 | $\\mathcal{N}(A)$ | $\\{x \\mid Ax=0\\}$ | $n-\\text{rank}(A)$ |
| 行空间 | $\\mathcal{R}(A^T)$ | $\\{A^T y \\mid y\\in\\mathbb{R}^m\\}$ | $\\text{rank}(A)$ |
| 左零空间 | $\\mathcal{N}(A^T)$ | $\\{y \\mid A^T y=0\\}$ | $m-\\text{rank}(A)$ |

对偶: $\\mathcal{R}(A)^\\perp = \\mathcal{N}(A^T)$，$\\mathcal{N}(A)^\\perp = \\mathcal{R}(A^T)$""")

sf("03-基与维数.md",
    "基的定义？维数由什么决定？",
    """**基:** 线性无关 + 张成整个空间 = 最少向量、完整表达空间的坐标系。

**维数:** 基中向量的个数，**唯一确定**。

**坐标:** $\\forall a\\in V$，存在唯一的系数使 $a = \\sum \\alpha_i a_i$。""")

sf("04-秩.md",
    "矩阵的秩的定义？哪些运算保秩？",
    """$\\text{rank}(A)$ = 线性无关列的最大个数 = 线性无关行的最大个数 = $\\dim\\mathcal{R}(A)$。

**保秩运算:** 列乘非零标量、交换列、乘以可逆矩阵 $PAQ$、加入现有列的线性组合。""")

sf("05-特征值与正定性.md",
    "特征值与矩阵正定性/半正定性的关系？",
    """$A \\in S^n$（对称矩阵）:

- $A \\succ 0$（正定） $\\iff$ 所有特征值 $> 0$
- $A \\succeq 0$（半正定） $\\iff$ 所有特征值 $\\geq 0$
- $A \\prec 0$（负定） $\\iff$ 所有特征值 $< 0$
- 不定 $\\iff$ 同时有正和负的特征值""")

sf("06-Rayleigh不等式.md",
    "Rayleigh商和Rayleigh不等式？",
    """Rayleigh商: $R_A(x) = \\frac{x^T A x}{x^T x}$（$x \\neq 0$，$A$ 对称）

Rayleigh不等式: $\\lambda_{\\min}(A) \\leq R_A(x) \\leq \\lambda_{\\max}(A)$

边界可达: $x$ 为对应特征向量时取等号。""")

sf("07-范数.md",
    "常见向量范数和矩阵范数？",
    """向量范数: $\\ell_1$（绝对值和）、$\\ell_2$（欧氏距离）、$\\ell_\\infty$（最大绝对值）

矩阵范数（诱导范数）: $\\|A\\|_p = \\max_{\\|x\\|_p=1}\\|Ax\\|_p$

- $\\|A\\|_1$ = 最大列绝对值和
- $\\|A\\|_\\infty$ = 最大行绝对值和
- $\\|A\\|_2$ = 最大奇异值 = $\\sqrt{\\lambda_{\\max}(A^T A)}$""")

sf("08-正交投影.md",
    "正交投影的定义和公式？",
    """$x$ 在子空间 $V$ 上的正交投影 $\\hat{x}$ 满足: $(x - \\hat{x}) \\perp V$

若 $V = \\mathcal{R}(A)$（$A$ 列满秩）: $\\hat{x} = A(A^T A)^{-1}A^T x$

投影矩阵 $P = A(A^T A)^{-1}A^T$ 满足 $P^2 = P = P^T$。""")

# ===== II-凸集与凸函数 (8 cards) =====
sf2 = lambda f, front, back: card("凸集与凸函数", f, front, back)

sf2("01-凸集定义.md",
    "凸集的定义？常见凸集有哪些？",
    """**定义:** $S$ 是凸集 $\\iff$ $\\forall x,y\\in S$，$ax+(1-a)y\\in S$（$\\forall a\\in(0,1)$）。

一句话: 连线上没有洞——任取两点，连线全程在集合内。

**常见凸集:** 空集、单点集、直线、线段、子空间、超平面、半空间、多面体 $\\{x\\mid Ax\\leq b\\}$、二阶锥、正半定锥。""")

sf2("02-超平面与半空间.md",
    "超平面、半空间、线性簇的定义？",
    """**超平面:** $H = \\{x \\mid v^T(x-a)=0\\}$（$v\\neq 0$）。$a=0$ 时过原点（子空间），$a\\neq 0$ 时是仿射集。

**半空间:** $H^+ = \\{x\\mid v^T(x-a)\\geq 0\\}$，$H^- = \\{x\\mid v^T(x-a)\\leq 0\\}$。

**线性簇:** $L = \\{x\\mid Ax=b\\}$，多个超平面的交集，维数 $= \\dim\\mathcal{N}(A)$。

不等式约束 $Ax\\leq b$ = 要求 $x$ 落在若干半空间交集内。""")

sf2("03-凸函数定义.md",
    "凸函数的两种等价定义？",
    """**定义1（Jensen不等式）:** $f(ax+(1-a)y) \\leq af(x)+(1-a)f(y)$，$\\forall a\\in(0,1)$

**定义2（一阶条件）:** $f(y) \\geq f(x) + \\nabla f(x)^T(y-x)$，$\\forall x,y$

两个定义等价。定义2的几何含义: 函数图像在任意点的切线**上方**。

**严格凸:** 不等式严格取 $<$（$x\\neq y$）。""")

sf2("04-凸函数二阶条件.md",
    "凸函数的二阶判定条件？",
    """$f\\in C^2$:

- $f$ 是凸函数 $\\iff$ $\\nabla^2 f(x) \\succeq 0$（Hessian处处半正定）
- $f$ 是严格凸函数 $\\Leftarrow$ $\\nabla^2 f(x) \\succ 0$（处处正定，充分非必要）

注意: 严格凸 $\\Leftarrow$ Hessian正定，但反向不成立（例: $f(x)=x^4$ 严格凸但 $f''(0)=0$）。""")

sf2("05-保凸运算.md",
    "常见保凸运算有哪些？",
    """1. 非负加权和: $\\sum w_i f_i$（$w_i\\geq 0$，$f_i$ 凸）
2. 与仿射函数的复合: $f(Ax+b)$（$f$ 凸）
3. 逐点最大: $\\max\\{f_1,\\dots,f_m\\}$（各 $f_i$ 凸）
4. 上确界: $\\sup_{y\\in\\mathcal{A}} f(x,y)$（$f(\\cdot,y)$ 凸）""")

sf2("06-极点多面体.md",
    "极点（顶点）的定义？多面体极点与BFS的关系？",
    """**极点:** 不能表示为集合中另外两点的严格凸组合的点。

**多面体:** $\\{x\\mid Ax\\leq b\\}$（有界多面体 = 多胞形）。

**极点与BFS:** 对于标准形LP $\\{x\\mid Ax=b, x\\geq 0\\}$，极点和基本可行解(BFS)一一对应。线性规划最优解必在极点上达到。""")

sf2("07-FONC无约束.md",
    "无约束优化的 FONC、SONC、SOSC？",
    """**FONC（一阶必要条件）:** $\\nabla f(x^*)=0$

**SONC（二阶必要条件）:** $\\nabla^2 f(x^*) \\succeq 0$（Hessian半正定）

**SOSC（二阶充分条件）:** $\\nabla f(x^*)=0$ 且 $\\nabla^2 f(x^*) \\succ 0$（Hessian正定）$\\Rightarrow$ $x^*$ 是严格局部极小点""")

sf2("08-Taylor展开.md",
    "一阶和二阶 Taylor 展开公式？",
    """一阶: $f(x+d) \\approx f(x) + \\nabla f(x)^T d$

二阶: $f(x+d) \\approx f(x) + \\nabla f(x)^T d + \\frac{1}{2}d^T\\nabla^2 f(x)d$

带余项形式（一阶）: $f(x+d) = f(x) + \\nabla f(x+\\theta d)^T d$（$\\theta\\in(0,1)$）。""")

# ===== III-线搜索 (8 cards) =====
sf3 = lambda f, front, back: card("线搜索", f, front, back)

sf3("01-黄金分割法.md",
    "黄金分割法的两个关键参数？推导关键？",
    """$\\lambda = \\frac{3-\\sqrt{5}}{2} \\approx 0.382$，$\\mu = \\frac{\\sqrt{5}-1}{2} \\approx 0.618$

**推导关键:** 对称性 $\\lambda = 1-\\mu$ + 自相似性 $\\lambda = \\mu^2$ → $\\lambda^2-3\\lambda+1=0$。

**核心优势:** 每轮只需计算1个新函数值（旧内点自动复用），区间压缩比 $\\mu$。""")

sf3("02-二分法.md",
    "二分法的原理和收敛速度？与黄金分割的区别？",
    """**原理:** 利用 $f'(x^*)=0$，在中点检查导数符号决定删哪一半。

**收敛:** 线性，压缩比 $0.5$（每步算1次导数）。

**与黄金分割区别:** 黄金分割只需 $f$ 值（零阶），二分法需要 $f'$（一阶）。二分法理论压缩比更优($0.5$ vs $0.618$)，但需要导数信息。""")

sf3("03-一元牛顿法.md",
    "一元牛顿法的迭代格式和收敛阶？",
    """$x_{k+1} = x_k - f'(x_k)/f''(x_k)$

**收敛:** **二次收敛**（局部），需要 $f\\in C^2$ 且 $f''>0$。

用曲率来校准步长——曲率大处步长小，曲率小处步长大。""")

sf3("04-割线法.md",
    "割线法的迭代格式和收敛阶？与牛顿法的区别？",
    """$x_{k+1} = x_k - \\frac{f'(x_k)(x_k-x_{k-1})}{f'(x_k)-f'(x_{k-1})}$

**收敛:** **超线性**（约1.618阶），只需 $f\\in C^1$。

用差商代替 $f''$，避免计算二阶导数。需要两个初始点。""")

sf3("05-方法对比表.md",
    "一维搜索六种方法的所需信息与收敛速度？",
    """| 方法 | 所需信息 | 收敛速度 |
|------|:---:|:---:|
| 黄金分割法 | $f$ | 线性，$\\mu\\approx 0.618$ |
| 斐波那契法 | $f$ | 线性，前期更快 |
| 二分法 | $f'$ | 线性，$0.5$ |
| 牛顿法（一元） | $f',f''$ | **二次** |
| 割线法 | $f'$（两点） | **超线性**(1.618) |
| 插值法 | $f$/$f'$ | 取决于插值次数 |""")

sf3("06-Wolfe条件.md",
    "Armijo条件和Wolfe条件的区别？",
    """**Armijo条件（充分下降）:** $f(x_k+\\alpha d_k) \\leq f(x_k)+c_1\\alpha\\nabla f(x_k)^T d_k$，$c_1\\in(0,1)$

**Wolfe条件:** Armijo + 曲率条件: $\\nabla f(x_k+\\alpha d_k)^T d_k \\geq c_2\\nabla f(x_k)^T d_k$，$0<c_1<c_2<1$

**强Wolfe条件:** 曲率条件改为 $|\\nabla f(x_k+\\alpha d_k)^T d_k| \\leq c_2|\\nabla f(x_k)^T d_k|$

强Wolfe保证 $s_k^T y_k > 0$，对拟牛顿法至关重要。""")

sf3("07-信赖域.md",
    "信赖域方法与线搜索方法的根本区别？",
    """| | 线搜索 | 信赖域 |
|------|--------|--------|
| 策略 | 先定方向，再选步长 | 先定区域，再在区域内找最优方向+步长 |
| 模型 | 方向固定 | 在信赖域半径内二次模型近似 |

信赖域半径根据模型与实际下降的比值动态调整。""")

sf3("08-单峰函数.md",
    "单峰函数的定义和作用？",
    """区间 $[a,b]$ 上有唯一极小点 $x^*$，且 $f$ 在左侧严格递减、右侧严格递增。

这是一维搜索方法的核心假设——保证只保留一个含极小点的子区间。""")

# ===== V-线性规划 (10 cards) =====
sf4 = lambda f, front, back: card("线性规划", f, front, back)

sf4("01-LP标准形.md",
    "LP标准形的要求和标准化四步？",
    """标准形: $\\min\\;c^Tx$，s.t. $Ax=b,\\;x\\geq 0$，$\\text{rank}(A)=m<n$，$b\\geq 0$。

标准化四步:
1. $\\max$ → $\\min(-c)^Tx$
2. $\\leq$ 约束 $+s_i$（松弛）；$\\geq$ 约束 $-s_i$（剩余）
3. 自由变量 $x_i = x_i^+ - x_i^-$
4. $b_i<0$ → 方程乘 $-1$""")

sf4("02-基本可行解.md",
    "基本解、基本可行解(BFS)、退化BFS的定义？",
    """| 术语 | 定义 |
|------|------|
| 基本解 | 令 $x_N=0$，$x_B = B^{-1}b$ |
| 基本可行解(BFS) | 基本解 + $x_B\\geq 0$ |
| 退化BFS | BFS且某基变量=0（正分量数<$m$） |

BFS个数 $\\leq \\binom{n}{m}$。极点和BFS一一对应。""")

sf4("03-单纯形法核心.md",
    "单纯形法的核心思想和判别数？",
    """**核心思想:** 从一个BFS出发，沿使目标下降的方向移动到相邻BFS，直到无法改进。

**判别数:** $r_j = c_j - c_B^T B^{-1}A_j$

$\\min$ 问题: $r_j\\geq 0$（所有非基）→ 最优；最负$r_j$ → 入基。

$\\max$ 问题: 判据相反（非基$r_j\\leq 0$时最优）。""")

sf4("04-大M法.md",
    "大M法的核心思想和步骤？",
    """为 $\\geq$ 和 $=$ 约束引入人工变量，目标函数加 $M\\cdot$(人工变量和)（$\\min$ 时 $+M$，$\\max$ 时 $-M$）。

$M$ 是很大的正数，确保优先赶走人工变量。若最优解中人工变量非零 → 原问题不可行。""")

sf4("05-两阶段法.md",
    "两阶段法的两个阶段分别做什么？",
    """**Phase I:** 目标 $\\min\\;\\sum a_i$（人工变量和），检验原问题可行性。若最优值=0 → 可行，获得初始BFS；若>0 → 不可行。

**Phase II:** 以Phase I的BFS为起点，用原目标函数继续单纯形法。

两阶段法数值上比大M法更稳健。""")

sf4("06-对偶LP.md",
    "如何从原始LP构造对偶LP？",
    """| 原始 ($\\min$) | 对偶 ($\\max$) |
|------|------|
| $c^Tx$ | $b^T\\lambda$ |
| $Ax \\geq b$ | $\\lambda \\geq 0$ |
| $Ax \\leq b$ | $\\lambda \\leq 0$ |
| $Ax = b$ | $\\lambda$ 自由 |
| $x \\geq 0$ | $A^T\\lambda \\leq c$ |

规则: 原始$\\min$ → 对偶$\\max$；不等号方向翻转。""")

sf4("07-对偶定理.md",
    "弱对偶定理和强对偶定理的内容？",
    """**弱对偶:** 若$x$是(P)可行解，$\\lambda$是(D)可行解，则 $c^Tx \\geq b^T\\lambda$（对$\\min$问题）。

**强对偶:** 若(P)有有限最优解$x^*$，则(D)也有最优解$\\lambda^*$，且 $c^Tx^* = b^T\\lambda^*$。

对偶间隙 = $c^Tx - b^T\\lambda \\geq 0$，最优时为零。""")

sf4("08-互补松弛.md",
    "互补松弛条件及其含义？",
    """$(c_j - \\lambda^T a_j)\\cdot x_j = 0$，$\\forall j$

含义:
- $x_j > 0 \\Rightarrow c_j - \\lambda^T a_j = 0$（正变量对应的对偶约束取等号）
- $c_j - \\lambda^T a_j > 0 \\Rightarrow x_j = 0$（非紧对偶约束对应原变量为零）

用于从对偶最优解恢复原始最优解。""")

sf4("09-对偶单纯形法.md",
    "对偶单纯形法与原始单纯形法的区别？",
    """| | 原始单纯形 | 对偶单纯形 |
|------|----------|----------|
| 保持 | 原始可行性($x_B\\geq 0$) | 对偶可行性($r_j\\geq 0$) |
| 迭代 | 追求对偶可行性 | 追求原始可行性 |
| 适用场景 | 标准求解 | 添加约束后的重优化、$b$含负分量 |

出基: RHS最负者；入基: 比值最小者。""")

sf4("10-影子价格.md",
    "影子价格的含义和来源？",
    """**影子价格:** $\\lambda_i$（对偶变量）表示第$i$个资源的边际价值。

对$\\min$问题: $b_i$增加一单位 → 最优值变化 $-\\lambda_i$。

直接从最优表的判别行读出: $\\lambda^T = c_B^T B^{-1}$。""")

# ===== VI-整数规划 (4 cards) =====
sf5 = lambda f, front, back: card("整数规划", f, front, back)

sf5("01-IP类型.md",
    "整数规划的三种类型？与连续LP的关键区别？",
    """| 类型 | 条件 |
|------|------|
| 纯整数规划(Pure IP) | 全部变量 $\\in\\mathbb{Z}$ |
| 混合整数规划(Mixed IP) | 部分整数、部分连续 |
| 0-1整数规划 | $x_i\\in\\{0,1\\}$ |

与连续LP区别: IP可行域是离散格点（非凸），求解是**NP-hard**。IP最优值 $\\geq$ LP松弛最优值（$\\min$问题）。""")

sf5("02-LP松弛.md",
    "LP松弛的定义和性质？",
    """去掉整数约束 $x_i\\in\\mathbb{Z}$ 得LP松弛。

性质: LP松弛最优值 = IP最优值的**下界**（$\\min$问题）。若LP松弛最优解恰好是整数 → 也是IP最优解。""")

sf5("03-割平面法.md",
    "割平面法的核心思想？",
    """在LP松弛最优解非整数时，添加一个线性不等式（割平面），割掉当前分数解但**不割掉任何整数可行解**。

反复求解LP松弛+添加割线，直到得到整数解。Gomory割是最经典的割平面。""")

sf5("04-分支定界法.md",
    "分支定界法的核心步骤？",
    """1. **分支:** 选一个分数变量 $x_i$，分为 $x_i\\leq\\lfloor v\\rfloor$ 和 $x_i\\geq\\lceil v\\rceil$ 两个子问题
2. **定界:** 每个子问题求解LP松弛得下界
3. **剪枝:** 下界 $\\geq$ 当前最优整数值 → 不再分支

通过不断分支和剪枝，最终找到整数最优解。""")

# ===== VII-约束优化 (8 cards) =====
sf6 = lambda f, front, back: card("约束优化", f, front, back)

sf6("01-正则点.md",
    "正则点的定义？意义？",
    """$x^*$是正则点 $\\iff$ $\\{\\nabla h_i(x^*)\\}_{i=1}^m$ 线性无关 $\\iff$ $\\text{rank}(Dh(x^*))=m$。

**意义:** 保证约束梯度的线性无关性 → 切空间维数 = $n-m$（满秩），Lagrange乘子唯一。

对于含不等式约束: LICQ = 积极约束梯度线性无关。""")

sf6("02-Lagrange乘子法.md",
    "Lagrange乘子定理（等式约束FONC）的内容？",
    """**定理:** $x^*$ 是正则局部极小点 $\\Rightarrow$ 存在唯一 $\\lambda^*\\in\\mathbb{R}^m$ 使:
$$\\nabla f(x^*) = \\sum_{i=1}^m \\lambda_i^* \\nabla h_i(x^*)$$

即 $\\nabla f(x^*)$ 落在约束梯度张成的法空间内。

等价于 Lagrange函数 $L(x,\\lambda)=f(x)+\\lambda^T h(x)$ 的驻点条件 $\\nabla_x L=0$。""")

sf6("03-KKT条件.md",
    "KKT条件的四个组成部分？",
    """$$\\begin{aligned}
\\text{1. 驻点: } & \\nabla f + \\sum\\mu_j\\nabla g_j + \\sum\\lambda_i\\nabla h_i = 0 \\\\
\\text{2. 原始可行: } & g_j(x)\\leq 0,\\; h_i(x)=0 \\\\
\\text{3. 对偶可行: } & \\mu_j \\geq 0 \\\\
\\text{4. 互补松弛: } & \\mu_j g_j(x) = 0
\\end{aligned}$$

(1)+(3)+(4) = 对偶可行 + 驻点 + 互补松弛 = KKT核心。""")

sf6("04-积极约束集.md",
    "积极不等式约束集的定义？为什么只关注它？",
    """$\\mathcal{J}(x^*) = \\{j \\mid g_j(x^*)=0\\}$（恰好取等的约束）。

**为什么:** 非积极约束($g_j(x^*)<0$)在$x^*$邻域内自动满足，对局部可行方向不构成限制。只有积极约束影响切锥。""")

sf6("05-对偶问题.md",
    "Lagrange对偶问题的构造和弱/强对偶？",
    """Lagrange函数: $L(x,\\lambda,\\mu) = f(x) + \\sum\\mu_j g_j(x) + \\sum\\lambda_i h_i(x)$

对偶函数: $q(\\lambda,\\mu) = \\inf_x L(x,\\lambda,\\mu)$

对偶问题: $\\max_{\\lambda,\\mu\\geq 0} q(\\lambda,\\mu)$

**弱对偶:** $q^* \\leq f^*$（对偶最优值 $\\leq$ 原始最优值）
**强对偶:** 凸问题+Slater条件 → $q^* = f^*$（零对偶间隙）""")

sf6("06-罚函数法.md",
    "罚函数法的基本思想？",
    """将约束优化转为无约束优化: $\\min_x f(x) + \\rho\\cdot P(x)$

$P(x)$ 惩罚约束违反: 等式 $h_i^2$，不等式 $\\max(0,g_j)^2$。$\\rho\\to\\infty$ 时逼近原问题。

缺点: $\\rho$ 过大导致 Hessian 病态。""")

sf6("07-增广Lagrange.md",
    "增广Lagrange法相比罚函数法的优势？",
    """$L_A(x,\\lambda,\\rho) = f(x) + \\lambda^T h(x) + \\frac{\\rho}{2}\\|h(x)\\|^2$

**优势:** 结合 Lagrange乘子（对偶信息）和二次罚项。不需要 $\\rho\\to\\infty$（乘子自动逼近最优乘子），避免了罚函数法的病态问题。""")

sf6("08-投影梯度法.md",
    "投影梯度法的迭代格式？",
    """$x_{k+1} = P_\\Omega(x_k - \\alpha_k\\nabla f(x_k))$

$P_\\Omega$: 投影到可行域 $\\Omega$ 的算子。

沿负梯度走一步，若跑出可行域就投影回来。适用于约束简单（投影易算）的问题。""")

# ===== VIII-多目标规划 (5 cards) =====
sf7 = lambda f, front, back: card("多目标规划", f, front, back)

sf7("01-多目标定义.md",
    "多目标优化与单目标的关键区别？",
    """| | 单目标 | 多目标 |
|------|--------|------|
| 目标 | $f(x)\\in\\mathbb{R}$ | $f(x)\\in\\mathbb{R}^l$ |
| 比较 | 全序（任意两数可比较） | **偏序**（向量无法直接比大小） |
| 最优解 | $f(x^*)\\leq f(x)$ | **Pareto最优**（非支配解） |

核心困难: 向量没有全序——无法直接说 $[1,2]^T$ 和 $[2,1]^T$ 谁更好。""")

sf7("02-Pareto最优.md",
    "Pareto最优解（非支配解）的定义？",
    """$x^*$是Pareto最优解 $\\iff$ 不存在$x$使:
1. $\\forall i,\\; f_i(x)\\leq f_i(x^*)$
2. 且 $\\exists i,\\; f_i(x) < f_i(x^*)$

一句话: 无法在不损害其他目标的前提下改进任一目标——改进已经穷尽。""")

sf7("03-Pareto前沿.md",
    "Pareto前沿是什么？",
    """所有Pareto最优解在**像空间**（目标函数值空间）中的像构成的集合。

Pareto前沿 = 目标函数空间中"最优折中"的边界——前沿上的点无法同时改进所有目标。""")

sf7("04-求解方法.md",
    "多目标优化的四种主要求解方法？",
    """1. **加权凸组合法:** $\\min\\sum w_i f_i(x)$（$w_i\\geq 0,\\sum w_i=1$），改变权重得不同Pareto解
2. **极大极小法:** $\\min\\max_i\\{f_i(x)\\}$，最小化最大损失
3. **范数法:** $\\min\\|f(x)-f^*\\|$（$f^*$为理想点）
4. **约束集法:** 选一个为主目标，其余转为约束

加权法仅对凸问题能获得完整Pareto前沿。""")

sf7("05-三类多目标.md",
    "多目标规划的三类形式？",
    """| 类型 | 描述 | 标准化 |
|------|------|--------|
| 全极小化 | 所有$f_i$求$\\min$ | 标准形式 |
| 全极大化 | 所有$f_i$求$\\max$ | $\\min -f_i$ |
| 混合型 | 部分$\\min$，部分$\\max$ | $\\max$目标取负 |""")

# ===== FONC理论 (6 cards) =====
sf8 = lambda f, front, back: card("FONC理论", f, front, back)

sf8("01-无约束FONC.md",
    "无约束优化FONC的推导思路？",
    """$\\nabla f(x^*)=0$

若 $\\nabla f(x^*)\\neq 0$，取 $d=-\\nabla f(x^*)$，由Taylor展开:
$f(x^*+\\alpha d) = f(x^*) - \\alpha\\|\\nabla f(x^*)\\|^2 + o(\\alpha) < f(x^*)$（$\\alpha$充分小）

矛盾于$x^*$是局部极小点。""")

sf8("02-等式约束FONC推导.md",
    "等式约束FONC → Lagrange乘子定理的推导关键步骤？",
    """1. 切锥 $\\mathcal{T} = \\ker(Dh(x^*))$（等式约束的线性化）
2. FONC: $\\nabla f(x^*)^T d = 0$（$\\forall d\\in\\mathcal{T}$）
3. $\\nabla f(x^*) \\perp \\mathcal{T}$ → $\\nabla f(x^*)\\in\\mathcal{T}^\\perp = \\mathcal{R}(Dh(x^*)^T)$
4. $\\exists\\lambda^*$ 使 $\\nabla f(x^*) = \\sum\\lambda_i^*\\nabla h_i(x^*)$

核心: 目标梯度必落在约束梯度的张成空间内。""")

sf8("03-切锥.md",
    "等式约束下切锥与法空间的关系？",
    """切锥: $\\mathcal{T} = \\{d\\mid Dh(x^*)d=0\\} = \\mathcal{N}(Dh(x^*))$，维数$n-m$。

法空间: $\\mathcal{N} = \\mathcal{T}^\\perp = \\mathcal{R}(Dh(x^*)^T) = \\text{span}\\{\\nabla h_i(x^*)\\}$

$\\mathbb{R}^n = \\mathcal{N}\\oplus\\mathcal{T}$（正交直和分解）。

直观: 切锥是曲面在$x^*$处的切平面，法空间是各约束梯度的张成空间。""")

sf8("04-KKT推导.md",
    "不等式约束下KKT条件的推导关键？",
    """1. 积极约束集 $\\mathcal{J}(x^*)=\\{j\\mid g_j(x^*)=0\\}$
2. 线性化切锥: $d$满足 $Dh d=0$ 且 $\\nabla g_j^T d\\leq 0$（$j\\in\\mathcal{J}$）
3. FONC + Farkas引理 → $\\nabla f \\in -\\text{cone}\\{\\nabla g_j\\} + \\text{span}\\{\\nabla h_i\\}$
4. 即存在 $\\mu_j\\geq 0$ 和 $\\lambda_i$ 使 $\\nabla f + \\sum\\mu_j\\nabla g_j + \\sum\\lambda_i\\nabla h_i = 0$
5. 互补松弛: 非积极约束 $\\mu_j=0$$""")

sf8("05-Farkas引理.md",
    "Farkas引理在KKT推导中的作用？",
    """Farkas引理: $Ax\\leq 0,\\; c^Tx>0$ 无解 $\\iff$ $\\exists y\\geq 0$ 使 $A^Ty=c$。

在KKT推导中: 将 $-\\nabla f$ 表示为积极约束梯度的非负组合 + 等式约束梯度的线性组合。Farkas引理保证这一表示的存在性。""")

sf8("06-LICQ.md",
    "LICQ（线性无关约束规格）的条件和作用？",
    """LICQ: 积极约束的梯度 $\\{\\nabla h_i(x^*)\\} \\cup \\{\\nabla g_j(x^*): j\\in\\mathcal{J}(x^*)\\}$ 线性无关。

**作用:** 保证Lagrange乘子唯一存在；保证线性化切锥 = 实际切锥。是最常用的约束规格之一。""")

# ===== 常考查的证明 (6 cards) =====
sf9 = lambda f, front, back: card("常考证明", f, front, back)

sf9("01-锯齿现象证明.md",
    "最速下降法锯齿现象的证明关键步骤？",
    """1. $x_{k+1} = x_k - \\alpha_k\\nabla f(x_k)$，$\\alpha_k$ 精确线搜索
2. 定义 $\\varphi(\\alpha)=f(x_k-\\alpha\\nabla f(x_k))$
3. $\\varphi'(\\alpha_k)=0$（极小点一阶必要条件）
4. 链式法则: $\\varphi'(\\alpha) = -\\nabla f(x_k-\\alpha\\nabla f(x_k))^T\\nabla f(x_k)$
5. 代入 $\\alpha=\\alpha_k$: $\\nabla f(x_{k+1})^T\\nabla f(x_k)=0$

核心洞察: 精确线搜索使新梯度在旧方向上分量为零 → 正交 → 锯齿。""")

sf9("02-凸函数全局最优.md",
    "凸函数FONC → 全局最优的证明关键？",
    """**定理:** $f$凸，$\\nabla f(x^*)=0$ $\\Rightarrow$ $x^*$是全局极小点。

**证明:** $\\forall x$，由凸函数一阶条件:
$f(x)\\geq f(x^*) + \\nabla f(x^*)^T(x-x^*) = f(x^*)$（因为$\\nabla f(x^*)=0$）

因此 $f(x)\\geq f(x^*)$对所有$x$成立，$x^*$是全局极小点。""")

sf9("03-牛顿法二阶收敛.md",
    "牛顿法局部二阶收敛的证明框架？",
    """**定理:** $f\\in C^3$，$\\nabla f(x^*)=0$，$\\nabla^2 f(x^*)$ 可逆 → $x_0$ 近$x^*$时二阶收敛。

**证明框架:**
1. 对 $\\nabla f$ 在 $x_k$ 处 Taylor 展开，在 $x^*$ 处取值
2. 牛顿步: $x_{k+1}=x_k-H_k^{-1}g_k$
3. 误差递推: $\\|x_{k+1}-x^*\\|\\leq c_1c_2\\|x_k-x^*\\|^2$

$f\\in C^3$ 保证 Hessian 的 Lipschitz 连续，$H(x^*)$ 可逆保证 $H_k^{-1}$ 一致有界。""")

sf9("04-共轭方向n步终止.md",
    "共轭方向法n步终止的证明关键？",
    """**定理:** 对 $f(x)=\\frac12 x^TQx-b^Tx$（$Q\\succ 0$），使用 $Q$-共轭方向组 $\\{p_i\\}$ 和精确线搜索，至多$n$步终止。

**证明关键:**
1. $\\{p_i\\}$ 是 $\\mathbb{R}^n$ 的基 → $x^*-x_0=\\sum\\beta_i p_i$
2. 由共轭性和精确线搜索 → $g_k^T p_i=0$（$i<k$）
3. 展开得 $\\beta_k = \\alpha_k$ → $x_n=x^*$

每一步恰好消除了对应方向上的误差，$n$步扫完整个空间。""")

sf9("05-BFGS正定性.md",
    "BFGS更新保持正定性需要什么条件？",
    """BFGS更新: $B_{k+1}=B_k+\\frac{y_k y_k^T}{y_k^T s_k}-\\frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$

**正定性遗传:** 若 $B_k\\succ 0$ 且 $s_k^T y_k>0$ → $B_{k+1}\\succ 0$

$s_k^T y_k>0$ 由强Wolfe线搜索保证。DFP同样有此性质。这就是曲率条件在拟牛顿法中的核心作用。""")

sf9("06-对偶间隙零条件.md",
    "强对偶定理（对偶间隙为零）的条件？",
    """对凸问题，若满足 Slater 条件（存在严格可行内点: $g_j(x)<0$ 对所有$j$），则强对偶成立: $p^* = d^*$。

对 LP（天然的凸问题）: 只要原问题或对偶问题可行且有限，强对偶必然成立。""")

print(f"Done! 63 cards created.")
