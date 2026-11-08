---
type: proposition
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-10-28-第10节-偏微分方程考前复习宣讲]]'
- '[[03_Sources/Courses/数学物理方程/作业/10月14日数学作业]]'
schema_version: 2
time: '2026-11-08T09:10:48+08:00'
aliases: []
tags: []
---
# 热方程总量平衡与Neumann稳态相容

对 $u_t=a^2u_{xx}+f$、$u_x(0,t)=h_1(t),u_x(L,t)=h_2(t)$，积分得到
$$\frac d{dt}\int_0^Lu\,dx=a^2(h_2-h_1)+\int_0^Lf\,dx.$$
这是零模态/平均温度的演化。稳态常数据必须满足 $a^2(h_2-h_1)+\int f=0$；满足时纯 Neumann 稳态仍差一个任意常数，额外平均值可确定它。

例 $L=2,a=1,f=x,h_1=1,h_2=0$，总量导数为1，无稳态；改 $h_2=-1$ 则可用 $U=x-x^3/6+C$。相容性失败不能推出随时间变化的热解不存在。带 $-bu$ 时总量另有 $-b\int u$；两端绝热且无源时均值按 $e^{-bt}$ 衰减，$b=0$ 才守恒。