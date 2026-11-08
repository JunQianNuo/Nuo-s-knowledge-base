---
type: concept
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-09-18-第2节-偏微分方程课程讲授]]'
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-10-23-第9节-偏微分方程初值问题授课]]'
- '[[03_Sources/Courses/数学物理方程/作业/10月9日作业]]'
- '[[03_Sources/Courses/数学物理方程/作业/9月21日数学作业]]'
schema_version: 2
time: '2026-11-08T09:10:48+08:00'
aliases: []
tags: []
---
# Dirac分布与集中冲量初速度

Dirac 分布 $\delta_{x_0}$ 由 $\langle\delta_{x_0},\phi\rangle=\phi(x_0)$ 定义，不是“某点无穷大而别处为零”的普通函数。阶跃 $H$ 的分布导数为 $\delta$。

冲量 $I$ 给线密度 $\rho$ 的弦带来初速度 $(I/\rho)\delta_{x_0}$，初位移可仍为0；由短段质量 $\rho\varepsilon$、速度 $I/(\rho\varepsilon)$ 的极限得到。杆截面积1时同理，击打结束后不把瞬时冲量当长期边界力。端点集中量须说明单侧约定，如 $\int_0^L\delta_L\phi=\phi(L)$。

两端固定弦冲量的正弦速度投影为 $2I\sin(n\pi x_0/L)/(\rho L)$；时间正弦系数再除以 $an\pi/L$。敲击点位于某模态节点时该模态不激发。整线冲量的达朗贝尔解为 $I[H(x-x_0+at)-H(x-x_0-at)]/(2a\rho)$。以上按分布/弱解理解，不满足普通光滑初速度假设。