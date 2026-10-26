---
title: Lebesgue控制收敛定理
type: 知识点
source:
- 课程/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理.md
topics:
- Lebesgue控制收敛定理
- DCT
- 积分与极限交换
- 控制函数
- Fatou引理
exam: 考试重点
status: 已整理
---

# Lebesgue控制收敛定理

## 一句话

控制收敛定理（DCT）给出积分与极限可交换的充分条件——存在一个可积函数"压制"整个函数列，则极限可穿过积分号，且收敛是 $L^1$ 范数意义下的强收敛。

## 严格定义

设 $\{f_n\}$ 是可测集 $E$ 上的一列可测函数，满足：

1. $f_n \to f$ a.e. 于 $E$（几乎处处逐点收敛）；
2. 存在控制函数 $F \in L(E)$（即 $F$ 在 $E$ 上 Lebesgue 可积），使得对几乎所有 $n$，
   $$|f_n(x)| \leq F(x) \quad \text{a.e. } x \in E$$

则 $f \in L(E)$，且积分与极限可交换：

$$
\boxed{\lim_{n\to\infty} \int_E f_n = \int_E f = \int_E \lim_{n\to\infty} f_n}
$$

此外还有更强的结论：**$L^1$ 收敛**

$$
\int_E |f_n - f| \to 0 \quad (n \to \infty)
$$

> [!important] DCT 核心判定要点
> - 控制函数必须**可积**（$\int_E F < \infty$），仅有界不够（除非 $m(E) < \infty$ 时用有界收敛定理）
> - 逐点收敛只需 **a.e.** 成立——这是 DCT 最强大的地方，远比一致收敛宽松
> - $L^1$ 收敛是"白送的"：不仅积分值收敛，被积函数本身也按 $L^1$ 范数收敛

## 推导：Fatou 双向夹逼

> [!proof]- 推导
> 核心思路：将 Fatou 引理分别应用于 $F + f_n$ 和 $F - f_n$（二者均非负），从两个方向夹逼积分。
>
> **第一步（下界）**：$F + f_n \geq 0$，由 Fatou 引理
> $$\int_E (F + f) = \int_E \lim_{n\to\infty} (F + f_n) \leq \varliminf_{n\to\infty} \int_E (F + f_n)$$
> 两边消去 $\int_E F$（有限），得
> $$\int_E f \leq \varliminf_{n\to\infty} \int_E f_n$$
>
> **第二步（上界）**：$F - f_n \geq 0$，同理
> $$\int_E (F - f) \leq \varliminf_{n\to\infty} \int_E (F - f_n)$$
> 消去 $\int_E F$ 并整理符号，得
> $$\int_E f \geq \varlimsup_{n\to\infty} \int_E f_n$$
>
> **第三步（夹逼）**：两步结合
> $$\varlimsup_{n\to\infty} \int_E f_n \leq \int_E f \leq \varliminf_{n\to\infty} \int_E f_n$$
> 而下极限必然 $\leq$ 上极限，故上下极限相等且等于 $\int_E f$，即
> $$\lim_{n\to\infty} \int_E f_n = \int_E f$$
>
> **第四步（$L^1$ 收敛）**：对 $|f_n - f| \leq 2F$ 再次应用 DCT，即得 $\int_E |f_n - f| \to 0$。
>
> **技巧点评**：Fatou 引理天然给出 $\leq$ 方向（下极限）。DCT 的巧妙之处在于通过构造 $F \pm f_n$ 两个非负辅助列，分别得到积分关于下极限的上界和关于上极限的下界，完成双向夹逼。

## 关键性质

| 性质 | 说明 |
|:--|:--|
| 积分与极限交换 | $\lim \int f_n = \int \lim f_n$（条件：存在可积控制函数） |
| $L^1$ 收敛 | $\int \vert f_n - f \vert \to 0$，比积分值收敛更强 |
| 控制函数可积是关键 | $F \in L(E)$ 不可替代为仅有界（除非 $m(E) < \infty$） |
| 逐点收敛只需 a.e. | 不要求一致收敛、不要求处处收敛——适用范围极广 |

### 控制函数构造套路（考试高频）

| 函数类型 | 控制思路 | 典型示例 |
|:--|:--|:--|
| 三角函数 | $\vert \sin x \vert, \vert \cos x \vert \leq 1$ | $\frac{\sin(nx)}{n}$ 控制在 $\frac{1}{n}$ 内 |
| 指数衰减 | $e^{-x}$ 在 $(0,\infty)$ 上可积 | $e^{-nx}$ 控制在 $e^{-x}$ 内 |
| 幂函数（靠近 0） | $x^{-\alpha}$ 在 $(0,1)$ 可积当 $\alpha < 1$ | $\frac{1}{\sqrt{x}+nx^2}$ |
| 幂函数（靠近 $\infty$） | $x^{-\alpha}$ 在 $(1,\infty)$ 可积当 $\alpha > 1$ | $\frac{\ln x}{1+x^2}$ |
| 对数控制 | $\frac{\ln t}{t} \leq e^{-1}\;(t>0)$，故 $\ln(1+x) \leq x$ | $\frac{\ln(1+nx)}{n^2 x}$ |
| 分式构造（均值不等式） | $\frac{nx}{1+n^2x^2} \leq \frac{1}{2}$ | 控制函数取常值 $\frac{1}{2}$（需有限测度集） |

## 典型例题

> **题目**：计算 $\displaystyle \lim_{n\to\infty} \int_0^\infty \frac{\sin(nx)}{n(1+x^2)} \, dx$。

> [!example]- 解答
> **分析**：被积函数含振荡因子 $\sin(nx)$，直接积分困难。考虑用 DCT 将极限移入积分号内。
>
> **步骤 1**：验证逐点收敛。
> $$f_n(x) = \frac{\sin(nx)}{n(1+x^2)} \to 0 = f(x) \quad (\forall x \in [0,\infty))$$
> 因为 $\vert \sin(nx) \vert \leq 1$，分子有界而分母 $n \to \infty$。
>
> **步骤 2**：构造控制函数。
> $$\vert f_n(x) \vert = \frac{\vert \sin(nx) \vert}{n(1+x^2)} \leq \frac{1}{1+x^2} \triangleq F(x)$$
>
> **步骤 3**：验证 $F \in L(\mathbb{R})$。
> $$\int_{-\infty}^\infty \frac{1}{1+x^2} \, dx = \pi < \infty$$
> 故 $F$ 在 $[0,\infty)$ 上可积。
>
> **步骤 4**：应用 DCT。
> $$\lim_{n\to\infty} \int_0^\infty f_n(x) \, dx = \int_0^\infty \lim_{n\to\infty} f_n(x) \, dx = \int_0^\infty 0 \, dx = 0$$
>
> **点评**：此题关键在于找到控制函数 $\frac{1}{1+x^2}$——它同时压制了振荡因子 $\sin(nx)$（以 1 为界）和分母的 $n$（含在系数 $\frac{1}{n}$ 中）。注意控制函数与 $n$ 无关！

## 易错点

> [!warning] 易错点 1：控制函数必须可积
> $F$ 必须有界且 $\int_E F < \infty$。仅 $F$ 有界不能使用 DCT——除非 $m(E) < \infty$，此时请用**有界收敛定理**（BCT）。例如 $E = \mathbb{R}$ 上 $f_n = \chi_{[0,n]}$ 有共同界 $1$，但极限与积分不可交换，因为控制函数 $\chi_{[0,\infty)}$ 在 $\mathbb{R}$ 上不可积。

> [!warning] 易错点 2：控制函数是 $F(x)$，不是常数 $M$
> 常数控制 $M$ 是有界收敛定理的假设，比 DCT 更强。DCT 的强大之处在于 $F$ 可以随 $x$ 变化（如 $e^{-x}$），只要整体可积即可。区分两者的适用场景：BCT 要求 $m(E) < \infty$，DCT 无此限制。

> [!warning] 易错点 3：DCT 只要求 a.e. 逐点收敛，不要求一致收敛
> 这是 DCT 对比 Riemann 积分理论的巨大优势。许多函数列不一致收敛（如 $f_n = n\chi_{(0,1/n]}$），但只要存在可积控制函数，DCT 仍然保证积分与极限可交换。

## 相关概念

- [[Lebesgue积分]]
- [[概念/实变函数/可测函数]]
- [[几乎处处收敛]]
- [[L^p空间]]
- [[知识点/实变函数/Fatou引理]]
- [[知识点/实变函数/逐项积分定理]]
- [[知识点/实变函数/有界收敛定理]]

## 习题

- [[课程/实变函数/习题库/04-Lebesgue积分/README|第4章习题库]] — DCT 相关习题：
  - 习题 4.16：控制收敛定理（基础验证）
  - 习题 4.17：指数衰减型控制函数
  - 习题 4.18：幂次型控制函数
  - 习题 4.19：经典极限定义 $e$（DCT 应用）
  - 习题 4.20：依测度收敛下的控制收敛定理
  - 习题 4.21：有界收敛定理（BCT）
