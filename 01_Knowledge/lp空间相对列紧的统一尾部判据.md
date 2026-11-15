---
schema_version: 2
type: proposition
time: '2026-11-15T09:35:21+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/作业/10.27]]'
---


# lp空间相对列紧的统一尾部判据



## 条件、双向证明与边界

**题目**：证明：$\ell^p$（$1\le p<\infty$）中子集 $S$ 是列紧的充要条件是：

1. 存在常数 $M>0$，使对一切 $x=\{\xi_n\}_{n=1}^{\infty}\in S$，都有 $\sum_{n=1}^{\infty}|\xi_n|^p\le M$。
2. 任给 $\varepsilon>0$，存在正整数 $N$，使当 $k\ge N$ 时，对一切 $x=\{\xi_n\}_{n=1}^{\infty}\in S$ 有 $\sum_{n=k}^{\infty}|\xi_n|^p\le\varepsilon$。

> [!hint]- 点击展开提示
> 必要性：列紧推出存在有限网，先控制有限个网点的尾部，再用三角不等式传给整个 $S$。充分性：逐坐标抽共同收敛子列，用条件2统一控制尾部，证明该子列在 $\ell^p$ 中为 Cauchy。

> [!solution]- 点击展开详细解析
> ```mermaid
> flowchart TD
>   A["证明充要条件"] --> B["必要性用有限网"]
>   B --> C["有界网点与统一小尾部"]
>   A --> D["充分性逐坐标抽子列"]
>   D --> E["有限头部和统一尾部控制差值"]
>   E --> F["子列为Cauchy并由完备性收敛"]
> ```
>
> **证明**：空集情形两边均成立，以下设 $S\ne\varnothing$。记尾投影
> $$
> R_kx=(0,\ldots,0,\xi_k,\xi_{k+1},\ldots),\qquad
> \|R_kx\|_p^p=\sum_{j=k}^{\infty}|\xi_j|^p.
> $$
> 它满足 $\|R_k(x-y)\|_p\le\|x-y\|_p$。
>
> **必要性。** 设 $S$ 列紧。由教材定理6.1，$S$ 完全有界，故有有限 $1$-网 $\{z^1,\ldots,z^m\}\subset\ell^p$。对任意 $x\in S$，选 $i$ 使 $\|x-z^i\|_p<1$，则
> $$
> \|x\|_p\le1+\max_{1\le i\le m}\|z^i\|_p=:C.
> $$
> 取 $M=C^p>0$，即得条件1。
>
> 任给 $\varepsilon>0$，置 $\delta=\varepsilon^{1/p}/3$，再取 $S$ 的有限 $\delta$-网 $\{y^1,\ldots,y^l\}\subset\ell^p$。每个 $y^i\in\ell^p$，故其尾部范数趋零。因网点只有有限个，可选同一个 $N$，使
> $$
> \|R_Ny^i\|_p<\delta\qquad(i=1,\ldots,l).
> $$
> 对任意 $x\in S$，选 $i$ 使 $\|x-y^i\|_p<\delta$，则当 $k\ge N$ 时，
> $$
> \begin{aligned}
> \|R_kx\|_p
> &\le\|R_k(x-y^i)\|_p+\|R_ky^i\|_p\\
> &\le\|x-y^i\|_p+\|R_Ny^i\|_p<2\delta<\varepsilon^{1/p}.
> \end{aligned}
> $$
> 取 $p$ 次方即得条件2，且 $N$ 对所有 $x\in S$ 统一有效。
>
> **充分性。** 设条件1、2成立。任取序列 $\{x_m\}\subset S$，写 $x_m=(\xi_j^{(m)})$。由条件1，对每个 $j,m$ 有 $|\xi_j^{(m)}|\le M^{1/p}$。对第1坐标抽收敛子列，再从中对第2坐标抽子列，依次进行，并取对角线子列 $\{x_{m_l}\}$。于是对于每个固定 $j$，$\{\xi_j^{(m_l)}\}_{l\ge1}$ 都收敛，特别是 Cauchy。
>
> 下面证明这条共同子列在 $\ell^p$ 中是 Cauchy。任给 $\eta>0$，由条件2，选 $N$，使
> $$
> \|R_Nx\|_p\le\eta/4\qquad(\forall x\in S).
> $$
> 前 $N-1$ 个坐标只有有限个，各坐标列为 Cauchy，故存在 $L$，使 $l,h\ge L$ 时
> $$
> \left(\sum_{j=1}^{N-1}|\xi_j^{(m_l)}-\xi_j^{(m_h)}|^p\right)^{1/p}<\eta/2.
> $$
> （若 $N=1$，此有限和为零。）把差向量分为头部和尾部，利用 Minkowski 不等式，得
> $$
> \begin{aligned}
> \|x_{m_l}-x_{m_h}\|_p
> &\le\left(\sum_{j=1}^{N-1}|\xi_j^{(m_l)}-\xi_j^{(m_h)}|^p\right)^{1/p}
>   +\|R_Nx_{m_l}\|_p+\|R_Nx_{m_h}\|_p\\
> &<\eta/2+\eta/4+\eta/4=\eta.
> \end{aligned}
> $$
> 因而该子列为 Cauchy。由第9题 $\ell^p$ 完备，子列收敛于某个 $x\in\ell^p$。由于原序列任意，$S$ 列紧。$\square$
>
> **答案**：$S$ 列紧当且仅当它在 $\ell^p$ 中有界，且 $p$ 次幂尾和对 $S$ 一致趋于零。不需要 $S$ 闭。
>
> **点评**：“对每个 $x$ 尾部趋零”本来就是 $x\in\ell^p$ 的性质；条件2强在同一个 $N$ 对所有 $x\in S$ 有效。单位向量族 $\{e_n\}$ 有界却不满足统一尾部条件；它逐坐标趋零，但范数恒为1。



先修：[[01_Knowledge/完全有界与相对列紧]]、[[01_Knowledge/嵌套子列的对角线抽取]]、[[01_Knowledge/Lp空间完备性的子列证明法]]。

## 本次补充来源

- [[03_Sources/Courses/泛函分析/作业/10.27]]

证明展开、自测、教材补足仍按原来源标记其整理性质，不冒充教师逐字讲授。
