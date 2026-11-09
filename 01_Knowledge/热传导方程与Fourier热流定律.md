---
type: concept
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-09-18-第2节-偏微分方程课程讲授]]'
- '[[03_Sources/Courses/数学物理方程/作业/9月21日数学作业]]'
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-09-16-第1节-数理方程课程导论与基础知识回顾]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-11-02-第18节-热方程求解与调试培训]]'
schema_version: 2
time: '2026-11-08T09:10:48+08:00'
aliases: []
tags: []
---
# 热传导方程与Fourier热流定律

## 一句话

热流沿温度下降方向，局部能量守恒把热流散度与温度变化联系起来。

## 严格定义与核心内容

温度 $u$、导热率 $k>0$ 下，热流矢量 $\boldsymbol q=-k\nabla u$；沿外法向 $n$ 的向外通量 $q_{out}=-k\partial_nu$。

负号表示由高温流向低温。

局部能量守恒为 $c\rho u_t=\nabla\cdot(k\nabla u)+Q$，$Q$ 是单位体积单位时间热源；常参数时为 $u_t=a^2\Delta u+Q/(c\rho)$、$a^2=k/(c\rho)$。

梯度给方向导数，散度累计流出，$\Delta=\nabla\cdot\nabla$；三维可用散度定理将边界通量转体积分。

变系数不能把 $k$ 无条件提出散度。

一阶时间方程只给一个初温。

稳态无源时 $\Delta u=0$（Laplace），有稳态源时 $-k\Delta u=Q$（Poisson）。

热扩散率 $a^2$ 不是波速；本笔记不把扩散与无阻尼波动的传播性质混同。
