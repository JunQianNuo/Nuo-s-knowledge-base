---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/01-集合论与点集拓扑基础/习题1.8-Dirichlet函数的积分-思考题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/03-可测函数/习题3.5-Dirichlet函数是Lebesgue可测的-习题]]'
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.1-Dirichlet函数的黎曼不可积性-习题]]'
tags:
- Dirichlet函数
- Lebesgue积分
---

# Dirichlet函数的两种积分行为

在任意非退化有界区间 $I$，$D=\chi_{\mathbb Q\cap I}$ 与 $1-D$ 均处处不连续。任意分割的每个子区间都有有理、无理点，故下Darboux和为0、上和为 $m(I)$，两者都不可黎曼积。

有理数可数、零测，所以 $D$ 可测且 a.e. 为0，Lebesgue积分0；$1-D$ 可测且 a.e. 为1，Lebesgue积分 $m(I)$。直接水平集判定中，$0\le t<1$ 时 $\{D>t\}=\mathbb Q\cap I$，其他阈值给全集或空集。在全 $\mathbb R$ 上，$1-\chi_\mathbb Q$ 的积分为无穷，不能称 $L^1(\mathbb R)$ 可积。
