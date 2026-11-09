---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.2-非负可测简单函数积分的线性性质-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.3-非负可测函数积分的四条基本性质-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.5-非负可测函数积分为零当且仅当函数几乎处处为零-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.6-可积即绝对可积-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.7-广义黎曼可积但非Lebesgue可积的例子-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.8-可积函数的基本性质(1)-(5)-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/作业4.2-与所有有界可测函数正交则a.e.为零-习题]]'
---
# Lebesgue积分的序性质与零积分判别

## 适用条件与结论

非负积分的上确界定义直接给保序性：$0\le f\le g\Rightarrow\int f\le\int g$；区域限制用零延拓给 $\int_Af=\int_Ef\chi_A$。

简单函数以共同细分块证明齐次、可加；递增区域上简单函数积分的连续性逐个分块用测度下连续性得到。

非负函数在零测集上的积分为0，因所有下方简单函数积分都为0；有限测度域上 $0\le f\le M$ 给 $\int f\le M m(E)<\infty$。

若f非负可测，则 $\int f=0\iff f=0$ a.e.。

正向对 $E_k=\{f\ge1/k\}$ 用 $0\ge k^{-1}m(E_k)$ 得各E_k零测，再取并；反向用零测集积分0。

因此a.e.相等不改积分。

对一般可测f，$f=f^+-f^-$、$|f|=f^++f^-$，所以

$$
f\in L^1\iff\int|f|<\infty,\qquad |\int f|\le\int|f|.
$$

可积函数a.e.有限；若正测集上 $|f|=\infty$，则 $\int|f|\ge N m(A)$ 对所有N，不可能有限。

可测f被非负可积g控制即也可积；可积f≤g则积分保序。

有界可测函数在有限测度集上可积。

条件收敛的广义黎曼积分不属于此可积概念。

## 例子与核对

例 $f(x)=x^{-1}\sin(1/x)$ 于 $(0,1)$，代换t=1/x得 $\int_1^\infty\sin t/t$，Dirichlet判别收敛；绝对值积分每段 $[k\pi,(k+1)\pi]$ 至少 $2/((k+1)\pi)$，故发散。

它不是Lebesgue可积。

若实 $f\in L^1$ 且对所有有界可测φ有 $\int fφ=0$，取 $φ=\operatorname{sgn}f$ 得 $\int|f|=0$，于是f=0 a.e.。

这把“所有检验函数正交”化为零积分判别。
