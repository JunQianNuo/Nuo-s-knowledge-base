---
title: Minkowski不等式
type: 知识点
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理.md
topics:
  - Minkowski不等式
  - L^p三角不等式
  - 范数公理
  - Hölder不等式
  - 共轭指数
exam: 考试重点
---

# Minkowski不等式

## 一句话

Minkowski 不等式即 $L^p$ 范数的三角不等式——"和的 $L^p$ 范数不超过各自 $L^p$ 范数之和"。它与 Hölder 不等式并列为 $L^p$ 理论的两根支柱，共同确立 $\|\cdot\|_p$ 是真正的范数。

## 严格定义

设 $1 \leq p \leq \infty$，$f, g \in L^p(E)$。则 $f+g \in L^p(E)$ 且

$$
\boxed{\|f+g\|_p \leq \|f\|_p + \|g\|_p}
$$

写成积分形式（$1 \leq p < \infty$）：

$$
\left(\int_E |f+g|^p \, dx\right)^{1/p} \leq \left(\int_E |f|^p \, dx\right)^{1/p} + \left(\int_E |g|^p \, dx\right)^{1/p}
$$

> [!important] 关键解读
> - **范数意义**：Minkowski 不等式恰好是 $\|\cdot\|_p$ 满足范数公理中的**三角不等式**——没有它，$L^p$ 只是带半度量的集合，无法做收敛分析和逼近理论。
> - **证明核心**：将 $|f+g|^p = |f+g|^{p-1} \cdot |f+g|$ 拆分，利用 $|f+g| \leq |f| + |g|$，对每一项用 Hölder 不等式（取 $q = p/(p-1)$ 使得 $(p-1)q = p$），合并后约去公因子即得。
> - **等号成立条件**（$1 < p < \infty$）：存在非负常数 $c$ 使 $f = cg$ a.e.（即两函数成比例）。
> - **$p < 1$ 时不成立**：此时 $\|\cdot\|_p$ 不是范数，三角不等式反向或不成立。

## 推导：基于 Hölder 不等式的证明

> [!proof]- 推导
> **分三种情况证明**。
>
> ---
>
> **情形 1：$p = 1$（平凡）**
>
> $$
> \|f+g\|_1 = \int_E |f+g| \, dx \leq \int_E (|f| + |g|) \, dx = \|f\|_1 + \|g\|_1
> $$
>
> 直接来自逐点不等式 $|f+g| \leq |f| + |g|$。
>
> ---
>
> **情形 2：$1 < p < \infty$（核心，依赖 Hölder）**
>
> 若 $\|f+g\|_p = 0$，三角不等式平凡成立。下设 $\|f+g\|_p > 0$。
>
> 设 $q = p/(p-1)$ 为共轭指数，满足 $1/p + 1/q = 1$，且关键恒等式 $(p-1)q = p$ 成立。
>
> **Step 1 — 拆分**：
> $$
> \|f+g\|_p^p = \int_E |f+g|^p = \int_E |f+g|^{p-1} \cdot |f+g|
> $$
>
> **Step 2 — 三角不等式拆分**（逐点）：
> $$
> \int_E |f+g|^{p-1} |f+g| \leq \int_E |f+g|^{p-1} |f| + \int_E |f+g|^{p-1} |g|
> $$
>
> **Step 3 — 对第一项用 Hölder**（$|f+g|^{p-1} \in L^q$，$|f| \in L^p$）：
> $$
> \begin{aligned}
> \int_E |f+g|^{p-1} |f|
> &\leq \left( \int_E \bigl(|f+g|^{p-1}\bigr)^q \right)^{1/q} \left( \int_E |f|^p \right)^{1/p} \\
> &= \left( \int_E |f+g|^{(p-1)q} \right)^{1/q} \|f\|_p \\
> &= \|f+g\|_p^{p/q} \|f\|_p \qquad (\because (p-1)q = p) \\
> &= \|f+g\|_p^{p-1} \|f\|_p \qquad (\because p/q = p-1)
> \end{aligned}
> $$
>
> **Step 4 — 第二项同理**：$\int_E |f+g|^{p-1} |g| \leq \|f+g\|_p^{p-1} \|g\|_p$。
>
> **Step 5 — 合并**：
> $$
> \|f+g\|_p^p \leq \|f+g\|_p^{p-1} \bigl( \|f\|_p + \|g\|_p \bigr)
> $$
>
> **Step 6 — 约去公因子**：两边除以 $\|f+g\|_p^{p-1}$（因为 $\|f+g\|_p > 0$），得
> $$
> \|f+g\|_p \leq \|f\|_p + \|g\|_p
> $$
>
> ---
>
> **情形 3：$p = \infty$**
>
> 由本性确界的定义，存在零测集 $Z_1, Z_2$ 使
> $$
> |f(x)| \leq \|f\|_\infty \; (\forall x \notin Z_1), \qquad |g(x)| \leq \|g\|_\infty \; (\forall x \notin Z_2)
> $$
> 在 $E \setminus (Z_1 \cup Z_2)$ 上，
> $$
> |f(x) + g(x)| \leq |f(x)| + |g(x)| \leq \|f\|_\infty + \|g\|_\infty
> $$
> 取下确界即得 $\|f+g\|_\infty \leq \|f\|_\infty + \|g\|_\infty$。$\square$
>
> ---
>
> **证明链总结**：$p=1$ 依赖逐点积分 → $1<p<\infty$ 依赖 Hölder 的共轭指数配合 → $p=\infty$ 依赖本质确界定义。Hölder 是 Minkowski 证明中不可替代的核心工具。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 范数公理之三角不等式 | Minkowski 恰好满足 $\|\cdot\|_p$ 的三角不等式要求（公理 2/3），与齐次性、正定性共同构成范数 |
| 与 Hölder 的关系 | Hölder 是 Minkowski 证明的唯一非线性工具——两者组成不可分割的"不等式对" |
| $L^p$ 赋范结构 | Minkowski + Hölder → $L^p$ 是赋范线性空间；再加 Riesz-Fisher（完备性）→ Banach 空间 |
| $p=1$ 的特殊性 | 证明退化到逐点积分的线性性，无需 Hölder |
| $p=\infty$ 的特殊性 | 证明退化到本质确界的三角不等式，无需积分技巧 |
| $p < 1$ 失效 | 当 $0 < p < 1$ 时 $\|\cdot\|_p$ 不满足三角不等式（事实上三角不等式反向），不是范数 |
| 等号条件（$1<p<\infty$） | $f$ 与 $g$ 成比例（$f = cg$ a.e.，$c \geq 0$），等价于 Hölder 取等 + 三角不等式逐点取等 |
| 积分形式与离散形式的统一 | 离散版本 $\left(\sum |a_n + b_n|^p\right)^{1/p} \leq \left(\sum |a_n|^p\right)^{1/p} + \left(\sum |b_n|^p\right)^{1/p}$ 是完全平行的——只需将测度空间换为计数测度 |

## 典型例题

> **题目**：完整写出 Minkowski 不等式（$1 < p < \infty$）基于 Hölder 不等式的证明，并验证 $p = \infty$ 时的不等式。最后说明：为什么 Minkowski + Hölder + Riesz-Fisher 三者共同使 $L^p$ 成为 Banach 空间？

> [!example]- 解答
> **（1）$1 < p < \infty$ 的 Hölder 证明**
>
> 设 $q = p/(p-1)$ 为共轭指数。若 $\|f+g\|_p = 0$ 则平凡；下设 $>0$。
>
> $$
> \begin{aligned}
> \|f+g\|_p^p &= \int_E |f+g|^p = \int_E |f+g|^{p-1} \cdot |f+g| \\
> &\leq \int_E |f+g|^{p-1} |f| + \int_E |f+g|^{p-1} |g| \qquad (\because |f+g| \leq |f|+|g|) \\
> &\leq \|f+g\|_p^{p-1} \|f\|_p + \|f+g\|_p^{p-1} \|g\|_p \qquad (\text{Hölder，利用 }(p-1)q = p) \\
> &= \|f+g\|_p^{p-1} (\|f\|_p + \|g\|_p)
> \end{aligned}
> $$
>
> 两边除以 $\|f+g\|_p^{p-1} > 0$ 即得 $\|f+g\|_p \leq \|f\|_p + \|g\|_p$。
>
> ---
>
> **（2）$p = \infty$ 的验证**
>
> 由本性确界定义，$|f| \leq \|f\|_\infty$ a.e.，$|g| \leq \|g\|_\infty$ a.e.，故在除去一个零测集后
> $$
> |f+g| \leq |f| + |g| \leq \|f\|_\infty + \|g\|_\infty
> $$
> 取本质确界即得 $\|f+g\|_\infty \leq \|f\|_\infty + \|g\|_\infty$。
>
> ---
>
> **（3）三者如何共同使 $L^p$ 成为 Banach 空间**
>
> - **Hölder 不等式**：提供共轭指数 $p,q$ 的积分估计技术，是 Minkowski 证明的唯一非线性工具；
> - **Minkowski 不等式（三角不等式）**：确立 $\|\cdot\|_p$ 满足范数公理，使 $L^p$ 成为**赋范线性空间**；
> - **Riesz-Fisher 定理（完备性）**：$L^p$ 中每个 Cauchy 列都收敛于 $L^p$ 内——这是 Banach 空间的决定性条件。
>
> 三步递进：乘积估计（Hölder）→ 范数结构（Minkowski）→ 完备性（Riesz-Fisher），缺一不可。
>
> ---
>
> **点评**：Minkowski 证明中最精妙的一步是拆分 $|f+g|^p = |f+g|^{p-1} \cdot |f+g|$——这个看似平凡的操作将问题转化为两个仅含单函数的 Hölder 估计，完美利用了共轭指数 $(p-1)q = p$ 的代数巧合。这体现了 $L^p$ 理论中 $p$ 与 $q$ 深度耦合的设计美学。

## 易错点

> [!warning] 易错点 1：拆分 $|f+g|^p = |f+g| \cdot |f+g|^{p-1}$ 是关键技巧，容易遗漏
> 不拆分直接对 $|f+g|^p$ 用 Hölder 会走入死胡同——因为 Hölder 不等式的一对因子必须分属 $L^p$ 和 $L^q$，而 $|f+g|^p$ 只含一个函数无法拆对。拆分后 $|f+g|^{p-1} \in L^q$ 与 $|f| \in L^p$ 恰好配对，这是证明的核心洞察。

> [!warning] 易错点 2：Hölder 中的 $q$ 取为 $p/(p-1)$，不是 $p-1$
> 共轭指数由 $1/p + 1/q = 1$ 推出 $q = p/(p-1)$。常见错误是取 $q = p-1$，这会导致 $(p-1)q = (p-1)^2 \neq p$，后续 $\|f+g\|_p^{p/q}$ 无法化简为 $\|f+g\|_p^{p-1}$。代数上要始终牢记 $(p-1)q = p$ 是化简的关键恒等式。

> [!warning] 易错点 3：除以 $\|f+g\|_p^{p-1}$ 的前提是 $\|f+g\|_p > 0$，需显式处理零情形
> 当 $\|f+g\|_p = 0$ 时不能除以零，但此时三角不等式 $\|f+g\|_p \leq \|f\|_p + \|g\|_p$ 退化为 $0 \leq \|f\|_p + \|g\|_p$（因范数非负自动成立）。证明中必须分情况处理，不能在未声明 $\|f+g\|_p > 0$ 的情况下直接除。

## 相关概念

- [[概念/实变函数/Minkowski不等式]] — 概念层：Minkowski不等式的由来、作用与关系网
- [[概念/实变函数/L^p空间]] — Minkowski 不等式使 $L^p$ 成为赋范空间
- [[概念/实变函数/Hölder不等式]] — Minkowski 不等式的证明完全依赖 Hölder 不等式
- [[概念/实变函数/卷积]] — 卷积的 Young 不等式是 Minkowski 与 Hölder 的综合推广
- [[知识点/实变函数/Riesz-Fisher定理]] — Minkowski + Hölder + Riesz-Fisher → $L^p$ 是 Banach 空间
- [[知识点/实变函数/Young不等式(卷积版)]] — 卷积版 Young 不等式综合运用 Minkowski 与 Hölder

## 习题

- [[课程/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — 重积分与 $L^p$ 空间
- [[课程/实变函数/习题库/05-重积分与Lp空间/习题5.7-Minkowski不等式（L^p三角不等式）-习题|习题5.7]] — Minkowski 不等式（$L^p$ 三角不等式）的完整证明
- [[课程/实变函数/习题库/05-重积分与Lp空间/习题5.6-Hölder不等式-习题|习题5.6]] — Hölder 不等式（Minkowski 证明的前置工具）
- [[课程/实变函数/习题库/05-重积分与Lp空间/习题5.9-L^p范数的对偶表示（定理4.1.5）-习题|习题5.9]] — $L^p$ 范数的对偶表示（使用 Minkowski 与 Hölder）
