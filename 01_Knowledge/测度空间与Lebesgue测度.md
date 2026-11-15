---
schema_version: 2
type: concept
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/02-Lebesgue测度/习题2.2-Lebesgue测度空间示例-例题]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-09-22-第3节-数学分析课程讲座]]'
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-10-20-第7节-泛函分析课程授课]]'
tags:
- 测度空间
- Lebesgue测度
---
# 测度空间与Lebesgue测度

## 严格定义与核心内容

测度空间为三元组 $(X,\mathcal F,\mu)$：$X$ 为非空集合，$\mathcal F$ 为其上的 $\sigma$-代数，$\mu:\mathcal F\to[0,\infty]$ 满足 $\mu(\varnothing)=0$ 和两两不交可测集列的可数可加性。

在 $\mathbb R^n$ 上，全体Lebesgue可测集 $\mathfrak M_n$ 对补、可数并封闭，Lebesgue测度 $m$ 满足上述公理，所以 $(\mathbb R^n,\mathfrak M_n,m)$ 为测度空间。

它是完备的：零测集的任意子集仍可测；也 $\sigma$ 有限：$\mathbb R^n=\bigcup_k[-k,k]^n$，每块有限测度。

完备与 $\sigma$ 有限是不同性质。

结构基础见 [[01_Knowledge/σ代数]]，极限性质见 [[01_Knowledge/测度对单调集合列的连续性]]。




## 概率、可列可加与$\sigma$有限的区分

概率测度满足$\mu(X)=1$；一般测度不要求总质量为1。$\sigma$有限指$X=\bigcup_jE_j$且各$\mu(E_j)<\infty$；可列可加指对两两不交可测集$A_j$有$\mu(\bigcup_jA_j)=\sum_j\mu(A_j)$，二者不是同一性质。$\mathbb N$上计数测度总质量无限，却由有限前缀覆盖而$\sigma$有限。讨论高斯等随机元素前，须明确可测空间和概率测度；9月22日只作动机，未给高斯测度构造。

## 本次补充来源

- [[03_Sources/Courses/泛函分析/课堂笔记/2026-09-22-第3节-数学分析课程讲座]]
- [[03_Sources/Courses/泛函分析/课堂笔记/2026-10-20-第7节-泛函分析课程授课]]

证明展开、自测、教材补足仍按原来源标记其整理性质，不冒充教师逐字讲授。
