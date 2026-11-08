---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.14-Fatou引理-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.15-Fatou引理严格不等式示例-习题]]'
legacy_topics:
- Fatou引理
- 下极限
- 非负可测函数
- 积分与极限交换
- Levi定理
- 控制收敛定理
exam: 考试重点
tags:
- Fatou引理
- 下极限
- 非负可测函数
- 积分与极限交换
- Levi定理
- 控制收敛定理
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
- '[[02_Maps/MOC-实变函数]]'
about:
- '[[01_Knowledge/Lebesgue积分]]'
time: '2026-08-31T11:44:20+08:00'
aliases: []
legacy_status: 已整理
---

# Fatou引理

## 一句话

非负可测函数列的下极限的积分，不超过积分的下极限——"极限跑进积分号里"积分值只会变小或不变。它是 Lebesgue 积分极限理论中条件最弱（仅需非负性）的工具，也是证明 Lebesgue 控制收敛定理的关键中间步骤。

## 严格定义

设 $\{f_n\}$ 是可测集 $E$ 上的**非负**可测函数列，则

$$
\boxed{\int_E \varliminf_{n\to\infty} f_n(x)\,dx \;\leq\; \varliminf_{n\to\infty} \int_E f_n(x)\,dx}
$$

左边是「下极限函数」的积分，右边是「积分的下极限」。不等号方向：**函数下极限的积分 $\leq$ 积分的下极限**。

> [!important] 关键条件与解读
> - **唯一条件**：$f_n \geq 0$（非负性）——不要求收敛、不要求控制函数、不要求有限测度
> - **不等号方向**：$\displaystyle\int \varliminf f_n \;\leq\; \varliminf \int f_n$（左边更小或相等）
> - **严格不等号可以成立**：典型反例见下方「典型例题」
> - **对比 Levi 定理**：Levi 要求单调递增 $\Rightarrow$ 等号成立；Fatou 仅要求非负 $\Rightarrow$ 只能保证 $\leq$
> - **对比 DCT**：DCT 给了控制函数 $\Rightarrow$ 等号成立；Fatou 是证明 DCT 的关键引理

## 推导：四步证明

> [!proof]- 推导
> **核心思路**：将下极限转化为单调递增列的极限，再用 Levi 定理。
>
> **步骤 1：构造单调递增列 $g_n$**。令
> $$
> g_n(x) = \inf_{j \geq n} f_j(x)
> $$
> 则 $0 \leq g_n \leq f_n$（逐点），且 $\{g_n\}$ 单调递增：$g_1 \leq g_2 \leq \cdots$。由下极限的定义，
> $$
> \lim_{n\to\infty} g_n(x) = \varliminf_{n\to\infty} f_n(x)
> $$
>
> **步骤 2：对 $g_n$ 应用 Levi 单调收敛定理**。因为 $\{g_n\}$ 是非负可测函数的单调递增列，Levi 定理保证极限与积分可交换：
> $$
> \int_E \varliminf_{n\to\infty} f_n = \int_E \lim_{n\to\infty} g_n = \lim_{n\to\infty} \int_E g_n
> $$
>
> **步骤 3：利用 $g_n \leq f_n$**。由积分的单调性，
> $$
> \int_E g_n \leq \int_E f_n \quad (\forall n)
> $$
> 取下极限得
> $$
> \varliminf_{n\to\infty} \int_E g_n \leq \varliminf_{n\to\infty} \int_E f_n
> $$
>
> **步骤 4：合龙**。由于 $\{g_n\}$ 单调递增，$\{\int_E g_n\}$ 也单调递增，故极限存在且等于下极限：
> $$
> \lim_{n\to\infty} \int_E g_n = \varliminf_{n\to\infty} \int_E g_n \leq \varliminf_{n\to\infty} \int_E f_n
> $$
> 结合步骤 2，得 $\displaystyle\int_E \varliminf f_n \leq \varliminf \int_E f_n$。

## 关键性质

| 性质 | 说明 |
|------|------|
| 条件 | **仅需非负性**（$f_n \geq 0$ on $E$），不要求有界、可积、收敛 |
| 不等号方向 | $\int \varliminf f_n \leq \varliminf \int f_n$（**左边 $\leq$ 右边**） |
| 严格不等号 | 可以成立——质量可以"逃逸到无穷"或"集中到零测集" |
| 与 Levi 的关系 | Levi $\Rightarrow$ Fatou（Levi 条件更强，结论也更强） |
| 与 DCT 的关系 | Fatou 是证明 DCT 的关键引理（对 $2F \pm f_n$ 应用 Fatou 推导 DCT） |
| 测度空间推广 | 对任意测度空间 $(X,\mathcal{F},\mu)$ 上非负 $\mu$-可测函数列同样成立 |

## 典型例题

> **题目**：验证 Fatou 引理中严格不等号可以成立。取 $f_n = \chi_{[n,n+1]}$ 在 $\mathbb{R}$ 上（Lebesgue 测度）。

> [!example]- 解答
> **逐点极限**：对任意 $x \in \mathbb{R}$，当 $n > |x|$ 后 $x \notin [n, n+1]$，故 $f_n(x) = 0$。因此
> $$
> \lim_{n\to\infty} f_n(x) = 0,\quad \forall x \in \mathbb{R}
> $$
> 从而 $\varliminf f_n = 0$。
>
> **逐点极限的积分**：
> $$
> \int_{\mathbb{R}} \varliminf f_n = \int_{\mathbb{R}} 0\,dx = 0
> $$
>
> **每个 $f_n$ 的积分**：$[n, n+1]$ 的 Lebesgue 测度为 $1$，故
> $$
> \int_{\mathbb{R}} f_n(x)\,dx = m([n, n+1]) = 1
> $$
>
> **积分的下极限**：
> $$
> \varliminf_{n\to\infty} \int_{\mathbb{R}} f_n(x)\,dx = \varliminf_{n\to\infty} 1 = 1
> $$
>
> **结论**：
> $$
> 0 = \int_{\mathbb{R}} \varliminf f_n \;<\; \varliminf \int_{\mathbb{R}} f_n = 1
> $$
> 即 Fatou 引理中的不等号可以严格成立。
>
> **点评**：此例中 $f_n$ 的"支撑集"（$[n, n+1]$）不断向右移动，导致逐点极限恒为 $0$，但每个 $f_n$ 的积分恒为 $1$。"质量"没有消失——它逃逸到了无穷远处，而 $\varliminf$ 无法捕捉到逃逸的质量。

---

> **题目（课件反例）**：取 $f_n(x) = \frac{\sqrt{n}}{\sqrt{2\pi}} e^{-nx^2/2}$（$x \in \mathbb{R}$）。

> [!example]- 解答
> **逐个积分**：每个 $f_n$ 是正态分布 $\mathcal{N}(0, 1/n)$ 的密度函数，故
> $$
> \int_{\mathbb{R}} f_n(x)\,dx = 1
> $$
>
> **逐点极限**：对 $x \neq 0$，$\lim_{n\to\infty} f_n(x) = 0$（$n$ 越大，指数衰减越快）；$x = 0$ 处 $f_n(0) \to \infty$（质量集中到原点）。因此
> $$
> \varliminf f_n = \lim f_n = 0 \quad \text{a.e.}
> $$
>
> **验证**：
> $$
> 0 = \int_{\mathbb{R}} \varliminf f_n \;<\; 1 = \varliminf \int_{\mathbb{R}} f_n
> $$
> 这是另一个严格不等号的例子——质量"集中到了零测集（原点）"，积分无法捕捉。
>
> **点评**：质量集中到零测集 $\Leftrightarrow$ 测度向 Dirac 测度弱收敛，是 Fatou 引理中"不等号严格成立"的另一典型机制。

## 易错点

> [!warning] 不等号方向记反
> 最常见错误：记成 $\varliminf \int f_n \leq \int \varliminf f_n$（不等号反了）。正确方向是 $\int \varliminf \leq \varliminf \int$。口诀："极限跑进积分号里，积分值只会变小"。

> [!warning] 忘记非负性条件
> Fatou 引理要求 $f_n \geq 0$。对非非负函数列，结论可能不成立——例如 $f_n = -\chi_{[n,n+1]}$ 时 $\int \varliminf f_n = 0$ 但 $\varliminf \int f_n = -1$，此时 $0 \not\leq -1$。若函数列有下界但不是非负，可考虑平移 $(f_n + C)$ 再应用 Fatou。

> [!warning] 误以为等号一定成立
> Fatou 引理只给出不等式。需要等号时，需检查条件是否加强到 Levi（单调）或 DCT（控制函数）。不能随意把 $\leq$ 改成 $=$。

## 相关概念

- [[01_Knowledge/Lebesgue积分]]
- [[01_Knowledge/可测函数]]
- [[01_Knowledge/几乎处处]]
- [[01_Knowledge/Levi单调收敛定理]]
- [[01_Knowledge/Lebesgue控制收敛定理]]
- [[01_Knowledge/Riesz定理]]

## 习题

- [[03_Sources/Courses/归档/实变函数/习题库/04-Lebesgue积分/README|第4章习题库]]
  - **习题 4.14** — Fatou 引理的证明
  - **习题 4.15** — Fatou 引理严格不等式示例（正态密度反例）
- [[03_Sources/Courses/归档/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]]
  - **习题 5.12** — $L^p$ 空间的完备性（Riesz-Fischer），证明中用 Fatou 引理完成最后估计


## 本轮习题补充与边界核对

正态尖峰 $f_n=\sqrt{n/(2\pi)}e^{-nx^2/2}$ 用 $t=\sqrt n x$ 得每项积分1；x≠0时指数压过 $\sqrt n$ 趋0，x=0时趋无穷。极限函数a.e.为0、积分0，故严格不等式 $0<1$。这是质量集中，不是积分质量凭空消失；相应概率测度弱收敛到Dirac质量，密度的a.e.极限无法描述该奇异极限。

对原文末尾“平移一个常数即可用Fatou”需限定该下界可积；无限测度空间上的正常数并不可积，不能随意消去两个无穷积分。
