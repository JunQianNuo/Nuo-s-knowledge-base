---
schema_version: 2
type: concept
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/02-Lebesgue测度/习题2.2-Lebesgue测度空间示例-例题]]'
tags:
- 测度空间
- Lebesgue测度
---

# 测度空间与Lebesgue测度

测度空间为三元组 $(X,\mathcal F,\mu)$：$X$ 为非空集合，$\mathcal F$ 为其上的 $\sigma$-代数，$\mu:\mathcal F\to[0,\infty]$ 满足 $\mu(\varnothing)=0$ 和两两不交可测集列的可数可加性。

在 $\mathbb R^n$ 上，全体Lebesgue可测集 $\mathfrak M_n$ 对补、可数并封闭，Lebesgue测度 $m$ 满足上述公理，所以 $(\mathbb R^n,\mathfrak M_n,m)$ 为测度空间。它是完备的：零测集的任意子集仍可测；也 $\sigma$ 有限：$\mathbb R^n=\bigcup_k[-k,k]^n$，每块有限测度。完备与 $\sigma$ 有限是不同性质。结构基础见 [[01_Knowledge/σ代数]]，极限性质见 [[01_Knowledge/测度对单调集合列的连续性]]。
