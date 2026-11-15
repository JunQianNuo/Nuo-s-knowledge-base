---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-09-18-第2节-线性空间与拓扑结构课程]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-09-22-第3节-数学分析课程讲座]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-10-20-第7节-泛函分析课程授课]]'
- '[[03_Sources/Courses/泛函分析/作业/10.27]]'
---
# lp序列空间与包含关系

## 一句话

$\ell^p$ 用所有坐标的可和性约束整个序列；逐坐标收敛不等于范数收敛。

## 严格定义

对 $1\le p<\infty$，
$$
\ell^p=\left\{x=(x_j)_{j\ge1}:\sum_{j=1}^{\infty}|x_j|^p<\infty\right\},\qquad
\|x\|_p=\left(\sum_{j=1}^{\infty}|x_j|^p\right)^{1/p}.
$$
有界序列空间及其范数为
$$
\ell^\infty=\{x:\sup_j|x_j|<\infty\},\qquad\|x\|_\infty=\sup_j|x_j|.
$$

## 包含关系及依据

若 $1\le p<q<\infty$，则 $\ell^p\subset\ell^q$。因为可和序列的坐标趋于零，尾部满足 $|x_j|\le1$，从而 $|x_j|^q\le|x_j|^p$；有限个首项不影响可和性。

## 边界与辨析

- 范数收敛控制整体误差，不能仅由逐坐标误差趋零推出。
- $\ell^p$ 是计数测度上的 $L^p$。计数测度不是有限测度，不能照搬有限测度函数空间中方向相反的包含关系。




## 上确界端点与线性运算

$p<\infty$时，$\sup_j|x_j|\le(\sum_j|x_j|^p)^{1/p}$，所以$\ell^p\subset\ell^\infty$。$\ell^\infty$中$\sup_j|ax_j+by_j|\le |a|\|x\|_\infty+|b|\|y\|_\infty$，同时证明线性组合仍有界及三角估计。其距离$\|x-y\|_\infty$与加法、数乘相容。不要混同序列的逐项上确界与$L^\infty$函数等价类的本质上确界。

## 本次补充来源

- [[03_Sources/Courses/泛函分析/课堂笔记/2026-09-18-第2节-线性空间与拓扑结构课程]]
- [[03_Sources/Courses/泛函分析/课堂笔记/2026-09-22-第3节-数学分析课程讲座]]

证明展开、自测、教材补足仍按原来源标记其整理性质，不冒充教师逐字讲授。
