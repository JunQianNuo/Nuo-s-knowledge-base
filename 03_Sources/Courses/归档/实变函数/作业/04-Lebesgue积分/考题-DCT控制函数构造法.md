---
subject:
- 实变函数
chapter: 4
section: Lebesgue积分
source:
- 考试纲要.md
type: homework
knowledge_tags:
- Lebesgue控制收敛定理
method_tags:
- DCT控制函数构造法
tags:
- 控制收敛定理
- 控制函数
- DCT控制函数构造法
aliases:
- 考题 - DCT控制函数构造法
schema_version: 2
time: "2026-08-31T11:44:20+08:00"
legacy_status: 已校对
legacy_topics:
- 控制收敛定理
- DCT
- 控制函数
- 积分与极限
status: not done
---

# 考题：构造 DCT 控制函数的典型方法

> 题目来源：考试纲要·第三块·解题核心。DCT 是考试最高频定理，控制函数的构造是得分关键。

## 题目

计算下列极限，要求构造适当的控制函数并说明其可积性：

(1) $\displaystyle \lim_{n\to\infty} \int_0^\infty \frac{\sin(nx)}{n(1+x^2)} \, dx$

(2) $\displaystyle \lim_{n\to\infty} \int_0^1 \frac{nx}{1+n^2x^2} \, dx$

(3) $\displaystyle \lim_{n\to\infty} \int_0^\infty \frac{\ln(1+x^n)}{1+x^n} \, e^{-x} \, dx$

(4) $\displaystyle \lim_{n\to\infty} \int_0^1 n x^n (1-x) \, dx$

---

> [!hint]- 点击展开提示
> (1) 分子有界分母保序：$|\sin(nx)| \leq 1$ → 用 $F(x)=\frac{1}{1+x^2}$
> (2) 均值不等式：$1+n^2x^2 \geq 2nx$ → $|f_n| \leq 1/2$
> (3) $\ln(1+t) \leq t$，$e^{-x}$ 天然可积
> (4) 需要找到与 $n$ 无关的界——考虑 $f_n$ 的最大值点

> [!solution]- 点击展开详细解析
> **解**：
>
> **(1)** $|f_n(x)| = \left|\frac{\sin(nx)}{n(1+x^2)}\right| \leq \frac{1}{1+x^2} = F(x)$。
> $F(x) = \frac{1}{1+x^2} \in L(0,\infty)$（$\int_0^\infty \frac{dx}{1+x^2} = \frac{\pi}{2} < \infty$）。
> 且 $f_n(x) \to 0$ 逐点。由 DCT，$\lim \int f_n = 0$。
>
> **(2)** 由均值不等式 $1+n^2x^2 \geq 2\sqrt{1 \cdot n^2x^2} = 2nx$，故
> $|f_n(x)| = \frac{nx}{1+n^2x^2} \leq \frac{nx}{2nx} = \frac{1}{2}$（$x>0$；$x=0$ 时 $f_n(0)=0$）。
> 控制函数 $F(x) = 1/2$ 在 $[0,1]$ 上可积（常数在有限测度集上可积）。
> 且 $f_n(x) \to 0$ a.e.（除 $x=0$ 外）。由 DCT（或有界收敛定理），极限为 0。
>
> **(3)** $|f_n(x)| \leq \frac{\ln(1+x^n)}{1+x^n}e^{-x}$。注意 $\frac{\ln(1+t)}{1+t} \leq \frac{t}{1+t} \leq 1$（$t \geq 0$），
> 故 $|f_n(x)| \leq e^{-x} = F(x) \in L(0,\infty)$。且 $f_n(x) \to 0$ 逐点。
> 由 DCT，极限为 0。
>
> **(4)** 令 $g_n(x) = nx^n(1-x)$。求最大值：$g_n'(x) = n^2x^{n-1}(1-x) - nx^n = nx^{n-1}(n(1-x)-x)$。
> 令导数为零：$n(1-x)=x$ → $x = \frac{n}{n+1}$。最大值：
> $g_n(\frac{n}{n+1}) = n\left(\frac{n}{n+1}\right)^n \cdot \frac{1}{n+1} = \frac{n}{n+1}\left(\frac{n}{n+1}\right)^n \to e^{-1}$。
> 故对几乎所有 $n$，$|g_n(x)| \leq 1$。且 $g_n(x) \to 0$ a.e.（$x<1$ 时 $nx^n \to 0$，$x=1$ 时 $1-x=0$）。
> 由有界收敛定理，极限为 0。
>
> **答案**：(1) $0$；(2) $0$；(3) $0$；(4) $0$。
>
> **点评**：控制函数构造是 DCT 应用的核心。四种套路分别对应三角有界、均值不等式、对数-幂比较、求最大值。记住：控制函数必须**不依赖于 $n$** 且**可积**。
