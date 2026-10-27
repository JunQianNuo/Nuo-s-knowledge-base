---
title: III. 积分与极限交换 — 复习
subject: 实变函数
type: 复习
source: 考试范围.txt, 知识图谱.png
topics:
  - Levi定理
  - Fatou引理
  - 控制收敛定理
  - 有界收敛定理
  - Lebesgue积分定义
  - 黎曼可积充要条件
tags:
- Levi定理
- Fatou引理
- 控制收敛定理
- 有界收敛定理
- Lebesgue积分定义
- 黎曼可积充要条件
---

# III. 积分与极限交换

> 一句说清：Lebesgue 积分最大的优势——极限和积分交换的条件比黎曼积分宽松得多。Levi 处理单调列，Fatou 给下界估计，DCT（控制收敛）是最强、最常用的工具。

> [!important] 考试重点
> **主要考积分与极限交换顺序**。积分定义（vs. 黎曼）仅需了解；重积分/Fubini 仅作了解。

---

## 一、核心定义速查

### 1.1 Lebesgue 积分定义（了解）

| 层次 | 定义 | 关键 |
|:--|:--|:--|
| 非负简单函数 | $\int_E \sum a_j\chi_{E_j} = \sum a_j\cdot m(E_j)$ | 柱体体积之和 |
| 非负可测函数 | $\int_E f = \sup\{\int_E h: 0\leq h\leq f, h\text{ 简单}\}$ | 用简单函数逼近取上确界 |
| 一般可测函数 | $\int_E f = \int_E f^+ - \int_E f^-$ | 正部/负部分解 |

**Lebesgue 可积 $\iff$ 绝对可积**（$|f|\in L(E)$），这与黎曼积分截然不同。

### 1.2 Lebesgue vs Riemann

| | Riemann | Lebesgue |
|:--|:--|:--|
| 划分方式 | 定义域划分 | 值域划分 |
| 可积条件 | 不连续点零测 | 可测 + $\int|f|<\infty$ |
| 绝对可积 | 条件收敛可能存在 | 可积 $\iff$ 绝对可积 |
| Dirichlet 函数 | 不可积 | 可积（= 0） |

### 1.3 黎曼可积的充要条件（定理 3.2.10）

$f$ 在 $[a,b]$ 上有界 → $f$ 黎曼可积 $\iff$ $f$ 的不连续点集是零测集。

---

## 二、极限定理速查表（核心）

| 定理 | 条件 | 结论 | 用途 |
|:--|:--|:--|:--|
| **Levi** (3.1.3) | $f_n\geq 0$，$f_n\uparrow f$ | $\lim\int f_n=\int f$ | 单调递增列 |
| **Fatou** (3.2.3) | $f_n\geq 0$ | $\int\varliminf f_n \leq \varliminf\int f_n$ | 下界估计 |
| **DCT** (3.2.4) | $\lvert f_n\rvert\leq F\in L$，$f_n\to f$ a.e. | $\lim\int f_n=\int f$ | **最常用** |
| **有界收敛** (3.2.6) | $m(E)<\infty$，$\lvert f_n\rvert\leq M$ | $\lim\int f_n=\int f$ | DCT 的最简情形 |
| **基本定理** (3.2.1) | $f_n\geq 0$，$f=\sum f_n$ | $\int\sum f_n = \sum\int f_n$ | 非负级数逐项积分 |

---

## 三、核心定理详解

### 3.1 Levi 单调收敛定理 ★★

**定理**：$\{f_k\}\subset\mathfrak{M}(E)$，$f_1\leq f_2\leq\cdots$，$\lim f_k = f$ → $\lim\int_E f_k = \int_E f$。

**证明要点**：取 $\alpha\in(0,1)$，用简单函数 $h\leq f$ 构造 $E_k=E(f_k\geq\alpha h)$，$E_k\uparrow E$，则
$$\int_E f_k \geq \int_{E_k} f_k \geq \alpha\int_{E_k} h \to \alpha\int_E h$$
令 $\alpha\to 1$，再对所有 $h\leq f$ 取上确界。

### 3.2 Fatou 引理 ★★

**定理**：$f_n\geq 0$ → $\int\varliminf f_n \leq \varliminf\int f_n$。

> 不等号方向：极限跑进积分号里，积分值"缩水"了。

**经典反例**：
$f_n(x)=\frac{\sqrt{n}}{\sqrt{2\pi}}e^{-nx^2/2}$（$\int f_n=1$，$\lim f_n=0$ a.e.） → $0=\int\lim f_n < \lim\int f_n = 1$

**证明**：令 $g_n=\inf_{j\geq n}f_j$，$g_n\uparrow\varliminf f_n$，用 Levi。

### 3.3 Lebesgue 控制收敛定理（DCT）★★★

**定理**：$\lvert f_n\rvert\leq F\in L(E)$，$f_n\to f$ a.e. → $\lim\int_E f_n = \int_E f$。

**证明技巧**：$g_n=|f_n-f|\leq 2F$，对 $\{2F-g_n\}$ 用 Fatou 引理。

> [!tip] 构造控制函数是 DCT 解题的核心技能

**例**：求 $\lim\int_0^1 \frac{n^{3/2}x}{1+n^2x^2}dx$。
控制函数：$\frac{n^{3/2}x}{1+n^2x^2}\leq x^{-1/2}\in L([0,1])$。逐点极限 $0$，由 DCT 得积分为 $0$。

### 3.4 有界收敛定理 ★

**定理**：$m(E)<\infty$，$\lvert f_n\rvert\leq M$，$f_n\to f$ a.e.（或依测度） → $\lim\int f_n=\int f$。

> DCT 的最简版本——控制函数取常值 $F(x)\equiv M$（有限测度上必可积）。

---

## 四、典型考题

### 4.1 构造控制函数

**核心技能**：找到公共的可积上界 $F(x)$。

**常见套路**：
- 利用 $\lvert\sin x\rvert,\lvert\cos x\rvert\leq 1$
- 利用 $e^{-x}$ 的衰减性
- 利用幂函数 $x^{-\alpha}$ 在 $0$ 或 $\infty$ 处的可积性
- 利用 $\frac{\ln t}{t}\leq e^{-1}$

### 4.2 判断极限与积分能否交换

**流程**：
1. 求逐点极限 $f(x)=\lim f_n(x)$
2. 尝试找控制函数 $F(x)$（$\lvert f_n\rvert\leq F$，$\int F<\infty$）
3. 找到 → DCT；找不到 → 尝试 Fatou/Levi/有界收敛

### 4.3 判断黎曼可积性

用定理 3.2.10：分析不连续点集是否零测。例：
- Dirichlet 函数：处处不连续 → 不连续点集测度 $1$ → 非黎曼可积
- 仅在有理点间断的函数：有理点集可数 → 零测 → 黎曼可积

---

## 五、易错点

> [!warning] Fatou 不等号方向
> $\int\varliminf f_n \leq \varliminf\int f_n$，极限跑进积分"缩水"。只有加控制函数（DCT）才有等号。

> [!warning] DCT 中 $F$ 必须可积
> $F$ 仅逐点有限不够，必须 $\int F<\infty$。

> [!warning] Lebesgue 可积 = 绝对可积
> 黎曼积分有"条件收敛"的广义积分（如 $\int_0^1\frac{1}{x}\sin(\frac{1}{x})dx$），但不是 Lebesgue 可积的。

> [!warning] 黎曼可积 $\Rightarrow$ Lebesgue 可积，反之不成立
> Dirichlet 函数是反例。

---

## 六、相关知识点梳理

| 链接 | 内容 |
|:--|:--|
| [[课程/归档/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理#六、Lebesgue 积分的极限定理（**本章核心 + 难点**）]] | 极限定理详解 |
| [[课程/归档/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理#八、黎曼可积性的 Lebesgue 刻画（**核心**）]] | 黎曼可积充要条件 |

## 七、作业回顾

- 直接用定义计算简单函数的 Lebesgue 积分
- 构造控制函数 + DCT 求极限
- 用 Fatou 引理估计下界
- 判断函数的黎曼可积性（不连续点零测）
