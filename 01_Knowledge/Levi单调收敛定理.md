---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/04-Lebesgue积分-知识梳理]]'
legacy_topics:
- Levi定理
- 单调收敛定理
- MCT
- Lebesgue积分
- 非负可测函数
- α技巧
exam: 考试重点
tags:
- Levi定理
- 单调收敛定理
- Lebesgue积分
- 非负可测函数
- Levi单调收敛定理
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
about:
- '[[01_Knowledge/Lebesgue积分]]'
legacy_topic_links:
- '[[01_Knowledge/Lebesgue积分]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Levi单调收敛定理

## 一句话

单调递增的非负可测函数列的积分极限等于极限函数的积分——Levi 定理用单调性绕过了控制收敛定理对可积控制函数的要求，是 Lebesgue 积分三大极限定理中条件最弱的一个。

## 严格定义

设 $f_n$ 是可测集 $E$ 上的非负可测函数列，满足

$$
0 \leq f_1(x) \leq f_2(x) \leq \cdots \quad \text{a.e. } x \in E
$$

且 $f_n \to f$ a.e. $x \in E$。则

$$
\boxed{\lim_{n\to\infty} \int_E f_n = \int_E f}
$$

其中允许 $\int_E f = \infty$（即积分值可以发散到无穷）。

> [!important] 核心条件与结论
> - **单调性**：$0 \leq f_1 \leq f_2 \leq \cdots$（逐点递增）——这是最关键的假设，不可省略
> - **非负性**：$f_n \geq 0$，保证 $\int f_n$ 为递增数列（允许 $\infty$）
> - **不要求**：有限测度（区别于 Egorov 定理）或可积控制函数（区别于控制收敛定理）
> - **结论**：积分与极限可交换，且等式两侧均允许取 $\infty$

## 推导：$\alpha$ 技巧

> [!proof]- 推导
> **第一步：$\lim \int f_n$ 存在且 $\leq \int f$**。由单调性 $f_n \leq f_{n+1} \leq f$，积分序列 $\int f_n$ 单调递增（允许 $\infty$），故 $\lim \int f_n$ 存在（视为广义实数）。又 $f_n \leq f$ 对每个 $n$ 成立，故 $\int f_n \leq \int f$，取极限得 $\lim \int f_n \leq \int f$。
>
> **第二步：反向不等号（$\alpha$ 技巧的核心）**。任取非负简单函数 $0 \leq \varphi \leq f$，取 $0 < \alpha < 1$，定义
> $$
> E_n := \bigl\{x \in E : f_n(x) \geq \alpha \varphi(x)\bigr\}
> $$
> 由 $f_n \uparrow f$ 且 $\alpha < 1$，有 $E_1 \subset E_2 \subset \cdots$ 且 $\bigcup_{n=1}^{\infty} E_n = E$（因为对任意 $x$，$f_n(x) \to f(x) \geq \varphi(x) > \alpha \varphi(x)$，故当 $n$ 充分大时 $f_n(x) \geq \alpha \varphi(x)$）。于是
> $$
> \int_E f_n \geq \int_{E_n} f_n \geq \int_{E_n} \alpha \varphi = \alpha \int_{E_n} \varphi
> $$
> 令 $n \to \infty$：由测度的下连续性，$E_n \uparrow E$，且 $\varphi$ 为简单函数，$\int_{E_n} \varphi \to \int_E \varphi$。故
> $$
> \lim_{n\to\infty} \int_E f_n \geq \alpha \int_E \varphi
> $$
> 令 $\alpha \to 1$，得 $\lim \int_E f_n \geq \int_E \varphi$。此式对所有 $\varphi \leq f$ 成立，对右侧取 supremum：
> $$
> \lim_{n\to\infty} \int_E f_n \geq \sup_{\varphi \leq f} \int_E \varphi = \int_E f
> $$
>
> **结论**：结合两步得 $\lim \int f_n = \int f$。$\square$
>
> **核心洞察**：$\alpha$ 技巧引入参数 $\alpha < 1$ 是为了构造 $E_n$ 的严格递增性（若 $\alpha = 1$，$f_n \geq \varphi$ 可能永远不成立）；取 sup 则回到 Lebesgue 积分定义为简单函数积分的上确界。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 非负性要求 | $f_n \geq 0$ 是必需的；对一般函数需先分解为正部 $f_n^+$ 和负部 $f_n^-$ 分别处理 |
| 单调性 | 最关键的假设——若无单调性，需改用 Fatou 引理或控制收敛定理 |
| 不要求有限测度 | $m(E)$ 可以是 $\infty$，结论仍成立（区别于有界收敛定理） |
| 不要求可积 | $f_n$ 和 $f$ 的积分均可为 $\infty$，只要单调性和非负性满足 |
| $\alpha$ 技巧 | Lebesgue 积分理论的标准证法模式：引入参数 $\alpha < 1$ 构造 $E_n$，取 sup 回到定义 |
| 与 Fatou 引理关系 | Fatou 引理仅要求非负（不要求单调），结论为 $\leq$；Levi 定理加强为 $=$（利用单调性） |
| 与级数关系 | Levi 定理可直接推出 Lebesgue 基本定理（非负项级数逐项积分） |

## 典型例题

> **题目**：计算 $\displaystyle \lim_{n\to\infty} \int_0^1 \frac{nx}{1 + n^2 x^2}\,dx$。验证函数列不满足单调性，通过变形或换元使 Levi 定理可用。

> [!example]- 解答
> **分析**：令 $f_n(x) = \frac{nx}{1 + n^2 x^2}$。$f_n$ 不单调（随 $n$ 增大，峰值移动且积分值变化），不能直接使用 Levi 定理。需先分析极限行为。
>
> **步骤 1：逐点极限**。对 $x \in (0,1]$，$f_n(x) = \frac{x/n}{1/n^2 + x^2} \to 0$（分子 $\sim x/n$，分母 $\to x^2$）。$x = 0$ 时 $f_n(0) = 0$。故 $f_n \to 0$ a.e.，极限积分为 $0$ 若积分号可取进。
>
> **步骤 2：直接积分**。$\int_0^1 f_n = \frac{1}{2n}\ln(1 + n^2) \to 0$（由 L'Hôpital 或直接估计 $\ln(1+n^2) \sim 2\ln n$，被 $n$ 除后趋于 $0$）。极限与逐点极限积分一致，但验证不能依赖 Levi 定理（函数列非单调）。
>
> **(变体)** 若考虑 $g_n(x) = \frac{n}{1 + n^2 x^2}$（去 $x$ 因子），可令 $t = nx$ 换元：$\int_0^1 g_n = \int_0^n \frac{dt}{1+t^2} \to \frac{\pi}{2}$。此时 $g_n$ 单调递增，Levi 定理直接适用。
>
> **点评**：原函数列不单调是典型陷阱——需先判断定理条件是否满足。原题直接积分即可得到 $0$，Levi 定理在此并非必要但变体展示了单调性如何触发定理。

## 易错点

> [!warning] 易错点 1：非负性不可忽略
> 若 $f_n$ 可取负值，即使单调递增，$\int f_n$ 的极限也可能不等于 $\int f$。一般函数须分解为正负部：$f_n = f_n^+ - f_n^-$，对 $f_n^+$ 和 $f_n^-$ 分别应用 Levi 定理。

> [!warning] 易错点 2：单调性不可省略
> $f_n(x) = nx/(1 + n^2 x^2)$ 在 $[0,1]$ 上收敛于 $0$ 但不单调——Levi 定理不适用。若错误套用，会掩盖条件缺失。
>
> 更严重的反例：$f_n(x) = n\chi_{(0, \frac{1}{n}]}$ 不单调，$\int f_n = 1$ 但逐点极限 $f = 0$，$\int f = 0 \neq 1$。

> [!warning] 易错点 3：$\alpha$ 技巧中 $\alpha < 1$ 的严格必要性
> 若取 $\alpha = 1$，则 $E_n = \{f_n \geq \varphi\}$ 可能恒为空集（例如 $f_n \uparrow f$ 但 $f_n$ 始终严格小于 $\varphi$ 在某正测集上不成立），无法保证 $E_n \uparrow E$。$\alpha < 1$ 确保对于每个 $x$，当 $n$ 充分大时 $f_n(x) \geq \alpha\varphi(x)$。

## 相关概念

- [[01_Knowledge/Lebesgue积分]]
- [[01_Knowledge/可测函数]]
- [[01_Knowledge/简单函数]]
- [[01_Knowledge/几乎处处]]
- [[01_Knowledge/零测集]]
- [[01_Knowledge/Riesz定理]]

## 习题

- [[03_Sources/Courses/归档/实变函数/习题库/04-Lebesgue积分/README|第4章习题库]] — 习题 4.4（Levi单调收敛定理）
- [[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.4-Levi单调收敛定理-习题|习题4.4]] — Levi 定理直接应用
- [[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.12-Lebesgue基本定理（级数逐项积分）-习题|习题4.12]] — 级数逐项积分（Levi 定理推论）
- [[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.14-Fatou引理-习题|习题4.14]] — Fatou 引理（对比）
- [[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.16-控制收敛定理-习题|习题4.16]] — 控制收敛定理（对比三大定理）
