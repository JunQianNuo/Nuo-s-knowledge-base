---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/05-重积分与Lp空间-知识梳理]]'
legacy_topics:
- Young不等式
- 卷积
- Lp空间
- Hölder不等式
- Fubini定理
- 磨光算子
exam: 考试重点
tags:
- Young不等式
- 卷积
- Lp空间
- Hölder不等式
- Fubini定理
- 磨光算子
- Young卷积不等式
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
about:
- '[[01_Knowledge/卷积]]'
legacy_topic_links:
- '[[01_Knowledge/卷积]]'
- '[[01_Knowledge/Hölder不等式]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Young不等式（卷积版）

## 一句话

Young 不等式（卷积版）断言：$L^p$ 函数与 $L^1$ 函数的卷积仍在 $L^p$ 中，且 $\|f*g\|_p \leq \|f\|_p \|g\|_1$——这是卷积在 $L^p$ 尺度上的基本连续性估计，也是磨光算子逼近理论（$C_c^\infty$ 在 $L^p$ 中稠密）的根基。

## 严格定义

**定理（Young 不等式，卷积版）**：设 $f \in L^p(\mathbb{R}^n)$（$1 \leq p \leq \infty$），$g \in L^1(\mathbb{R}^n)$。则 $f * g \in L^p(\mathbb{R}^n)$ 且

$$
\boxed{\|f * g\|_p \leq \|f\|_p \,\|g\|_1}
$$

> [!important] 关键条件与适用范围
> - **$g \in L^1$ 是关键前提**：若 $g$ 仅在 $L^q$（$q>1$）中而不在 $L^1$ 中，则本文不等式不成立，需替换为更一般的 Young 卷积不等式 $\|f*g\|_r \leq \|f\|_p \|g\|_q$（$\frac{1}{p}+\frac{1}{q}=1+\frac{1}{r}$）。本文是 $q=1$、$r=p$ 的特例。
> - **$p=1$**：$\|f*g\|_1 \leq \|f\|_1\|g\|_1$，即 $L^1$ 在卷积下封闭（构成无单位元的交换 Banach 代数）。
> - **$p=\infty$**：$\|f*g\|_\infty \leq \|f\|_\infty\|g\|_1$，由积分三角不等式直接得到，无需 Hölder 不等式。

## 推导：Hölder + Fubini

> [!proof]- 推导
> $p=1$ 或 $p=\infty$ 时直接由定义（或积分三角不等式）得到。以下设 $1 < p < \infty$，$q$ 为共轭指数（$\frac{1}{p}+\frac{1}{q}=1$）。
>
> **第 1 步：逐点估计。** 对任意 $x \in \mathbb{R}^n$，
> $$
> |(f*g)(x)| \leq \int_{\mathbb{R}^n} |f(x-y)|\,|g(y)| \, dy = \int_{\mathbb{R}^n} \big(|f(x-y)|\,|g(y)|^{1/p}\big) \cdot |g(y)|^{1/q} \, dy
> $$
>
> **第 2 步：Hölder 不等式**（对 $y$ 积分，$|f(x-y)||g|^{1/p}$ 承担 $L^p$ 角色，$|g|^{1/q}$ 承担 $L^q$ 角色）：
> $$
> |(f*g)(x)| \leq \Big(\int_{\mathbb{R}^n} |f(x-y)|^p\,|g(y)| \, dy\Big)^{1/p} \Big(\int_{\mathbb{R}^n} |g(y)| \, dy\Big)^{1/q}
> $$
>
> **第 3 步：取 $L^p$ 范数。** 两端 $p$ 次幂后在 $\mathbb{R}^n$ 上积分：
> $$
> \|f*g\|_p^p \leq \int_{\mathbb{R}^n}\!\Big(\int_{\mathbb{R}^n} |f(x-y)|^p\,|g(y)| \, dy\Big) dx \cdot \|g\|_1^{p/q}
> $$
>
> **第 4 步：Fubini 交换积分序。** 被积函数非负，由 Tonelli 定理：
> $$
> \begin{aligned}
> \iint_{\mathbb{R}^n\times\mathbb{R}^n} |f(x-y)|^p\,|g(y)| \, dy\,dx
> &= \int_{\mathbb{R}^n} |g(y)| \Big(\int_{\mathbb{R}^n} |f(x-y)|^p \, dx\Big) dy \\
> &= \int_{\mathbb{R}^n} |g(y)| \, dy \cdot \int_{\mathbb{R}^n} |f(x)|^p \, dx
> = \|f\|_p^p\,\|g\|_1
> \end{aligned}
> $$
> （其中 $\int_{\mathbb{R}^n} |f(x-y)|^p dx = \|f\|_p^p$ 由 Lebesgue 积分的平移不变性。）
>
> **第 5 步：合并。**
> $$
> \|f*g\|_p^p \leq \|f\|_p^p\,\|g\|_1 \cdot \|g\|_1^{p/q}
> = \|f\|_p^p\,\|g\|_1^{1 + p/q}
> = \|f\|_p^p\,\|g\|_1^p
> $$
> （因为 $1 + \frac{p}{q} = 1 + p(1-\frac{1}{p}) = p$。）
>
> **第 6 步：** 开 $p$ 次方得 $\|f*g\|_p \leq \|f\|_p\,\|g\|_1$。$\square$
>
> **核心技巧**：将 $|g|$ 拆为 $|g|^{1/p} \cdot |g|^{1/q}$ 是证明的"魔术因子"——使 Hölder 恰好产出 $\|g\|_1^{1/q}$ 余项，与 Fubini 交换积分序产出的 $\|g\|_1$ 合并为所需的 $\|g\|_1^p$。此拆分本质上利用了 $1/p + 1/q = 1$ 对指数和的约束。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| $L^p$ 封闭性 | $L^p * L^1 \subseteq L^p$：卷积不降低可积性层次 |
| 范数乘法估计 | $\|f*g\|_p \leq \|f\|_p \|g\|_1$，类比 Banach 代数的乘法不等式 |
| 磨光算子推论 | 取 $\varphi_\varepsilon(x) = \varepsilon^{-n}\varphi(x/\varepsilon)$（$\varphi \geq 0$，$\|\varphi\|_1 = 1$），则 $\|\varphi_\varepsilon * f\|_p \leq \|f\|_p$（一致有界），且可进一步证明 $\varphi_\varepsilon * f \xrightarrow{L^p} f$ |
| 稠密性推论 | $C_c^\infty(\mathbb{R}^n)$ 在 $L^p(\mathbb{R}^n)$ 中稠密（$1 \leq p < \infty$）；多项式在 $L^p[a,b]$ 中稠密 |
| 一般形式 | $\|f*g\|_r \leq \|f\|_p \|g\|_q$，$\frac{1}{p}+\frac{1}{q}=1+\frac{1}{r}$（Young 卷积不等式的完整版本），本文是 $q=1$、$r=p$ 的特例 |
| 证明核心工具 | Hölder 不等式（逐点拆分）+ Tonelli/Fubini（交换积分序）+ Lebesgue 平移不变性 |

## 典型例题

> **题目**：（1）验证 Young 不等式在 $p=2$、$n=1$ 时的特例：设 $f \in L^2(\mathbb{R})$，取 $g(x) = \frac{1}{2}\chi_{[-1,1]}(x)$，验证 $\|f*g\|_2 \leq \|f\|_2$。
>
> （2）利用 Young 不等式构造一列光滑函数，在 $L^p$ 范数下逼近给定的 $f \in L^p(\mathbb{R}^n)$。

> [!example]- 解答
> **（1）特例验证**：
> $g(x) = \frac{1}{2}\chi_{[-1,1]}(x)$，则 $\|g\|_1 = 1$。$(f*g)(x) = \frac{1}{2}\int_{-1}^{1} f(x-y)\,dy$ 是 $f$ 在 $[x-1,x+1]$ 上的**滑动平均**。由 Young 不等式：
> $$
> \|f*g\|_2 \leq \|f\|_2 \cdot \|g\|_1 = \|f\|_2
> $$
> 即滑动平均不增大 $L^2$ 能量——从频域看，局部平均滤去了高频分量，但总能量不增。
>
> **（2）磨光算子构造**：
> 取标准磨光子 $\varphi \in C_c^\infty(\mathbb{R}^n)$，满足 $\varphi \geq 0$，$\operatorname{supp}\varphi \subseteq \overline{B(0,1)}$，$\int_{\mathbb{R}^n} \varphi = 1$。令
> $$
> \varphi_\varepsilon(x) = \varepsilon^{-n}\, \varphi\!\left(\frac{x}{\varepsilon}\right),\quad \varepsilon > 0
> $$
> 则 $\|\varphi_\varepsilon\|_1 = 1$，$\operatorname{supp}\varphi_\varepsilon \subseteq \overline{B(0,\varepsilon)}$。对任意 $f \in L^p(\mathbb{R}^n)$，定义
> $$
> f_\varepsilon(x) := (\varphi_\varepsilon * f)(x) = \int_{\mathbb{R}^n} \varphi_\varepsilon(x-y)\,f(y)\,dy
> $$
> 由 Young 不等式：$\|f_\varepsilon\|_p \leq \|f\|_p$（一致有界）。由于 $\varphi_\varepsilon \in C_c^\infty$，$f_\varepsilon$ 也是 $C^\infty$ 的。进一步利用 $L^p$ 中平移连续性可证：
> $$
> \|f_\varepsilon - f\|_p \to 0 \quad (\varepsilon \to 0)
> $$
> 因此 $\{f_\varepsilon\}$ 是一列光滑函数，在 $L^p$ 范数下逼近 $f$。由此直接推出 **$C_c^\infty(\mathbb{R}^n)$ 在 $L^p(\mathbb{R}^n)$ 中稠密**。
>
> **点评**：这是 Young 不等式最深刻的应用——它不仅给出了卷积的范数控制，更使"用光滑函数逼近任意 $L^p$ 函数"这一抽象结论变得可操作。整个论证链为：Young 不等式 $\Rightarrow$ 磨光子一致有界 $\Rightarrow$ 平移连续性 $\Rightarrow$ $L^p$ 逼近 $\Rightarrow$ 稠密性。

## 易错点

> [!warning] 易错点 1：$g \in L^1$ 不可弱化为 $g \in L^q$（$q>1$）
> 若 $g$ 仅在 $L^q$ 中（$q>1$）而不在 $L^1$ 中，则本文给出的不等式 $\|f*g\|_p \leq \|f\|_p \|g\|_1$ 不成立（右边无定义或需重新解释）。此时须用一般 Young 卷积不等式 $\|f*g\|_r \leq \|f\|_p \|g\|_q$（$\frac{1}{p}+\frac{1}{q}=1+\frac{1}{r}$）。例如 $f, g \in L^2(\mathbb{R})$ 时，$\|f*g\|_\infty \leq \|f\|_2 \|g\|_2$（$p=q=2$，$r=\infty$）。

> [!warning] 易错点 2：Fubini 交换积分序需非负性保证
> 证明中 $\iint |f(x-y)|^p |g(y)|\,dy\,dx$ 的被积函数非负，故可直接用 **Tonelli 定理**交换积分序（无需先验证可积性）。若忘记取绝对值而对 $f(x-y)g(y)$ 直接用 Fubini，则须先证 $\iint |f(x-y)g(y)| < \infty$——这恰好需要 Young 不等式本身来保证，会造成循环论证。

> [!warning] 易错点 3：$p=\infty$ 的证明路径不同
> $p=\infty$ 时不经过 Hölder 不等式，直接由积分三角不等式：
> $$
> |(f*g)(x)| \leq \int |f(x-y)|\,|g(y)|\,dy \leq \|f\|_\infty \int |g(y)|\,dy = \|f\|_\infty \|g\|_1
> $$
> 对所有 $x$ 成立，取本质上确界即得结论。若生搬硬套 $1<p<\infty$ 的 Hölder 拆分反而会出错。

## 相关概念

- [[01_Knowledge/卷积]] — 卷积的定义与基本代数性质（交换、结合、双线性），Young 不等式是其 $L^p$ 分析支柱
- [[01_Knowledge/L^p空间]] — $L^p$ 空间的完备性（Banach）、包含关系与对偶理论
- [[01_Knowledge/Hölder不等式]] — 证明核心技术：逐点拆分 $|g|^{1/p}$ 与 $|g|^{1/q}$，是整个证明链的起点
- [[01_Knowledge/Minkowski不等式]] — 与 Young 不等式 + Hölder 不等式共同构成 $L^p$ 分析的三大不等式支柱

## 习题

- [[03_Sources/Courses/归档/实变函数/习题库/05-重积分与Lp空间/README|第5章习题库]] — 习题5.3（卷积可积性，$p=1$ 特例）、习题5.5（Young不等式，代数版）
- [[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.3-卷积的定义与可积性（定理3.3.7）-习题|习题5.3]] — 卷积在 $L^1$ 中的可积性（Young 不等式的 $p=1$ 特例，直接验证 $\|f*g\|_1 \leq \|f\|_1 \|g\|_1$）
- [[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.5-Young不等式-习题|习题5.5]] — Young 不等式（代数版：$a^{1/p}b^{1/q} \leq a/p + b/q$，由对数凹性或极值法证明，是 Hölder 不等式的代数基础）
