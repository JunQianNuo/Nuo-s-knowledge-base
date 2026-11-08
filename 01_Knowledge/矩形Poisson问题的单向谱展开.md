---
type: method
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/作业/10月23日作业]]'
schema_version: 2
time: '2026-11-08T09:10:48+08:00'
aliases: []
tags: []
---
# 矩形Poisson问题的单向谱展开

在 $(0,a)\times(0,b)$ 求 $\Delta u=f$，左右值 $\varphi_1,\varphi_2$，上下值 $\psi_1,\psi_2$。先取 $h=(1-x/a)\varphi_1(y)+(x/a)\varphi_2(y)$，令 $v=u-h$，则左右齐次、源为 $g=f-h_{yy}$，上下为 $p=\psi_1-h(\cdot,0),q=\psi_2-h(\cdot,b)$。

沿 $x$ 作正弦投影，$k_n=n\pi/a$、系数用 $2/a$ 归一化，各模态解 $V_n''-k_n^2V_n=g_n,V_n(0)=p_n,V_n(b)=q_n$。齐次边值部分为 $p_n\sinh(k_n(b-y))/\sinh(k_nb)+q_n\sinh(k_ny)/\sinh(k_nb)$；加 $\int_0^bG_n(y,s)g_n(s)ds$，其中
$$G_n=-\frac{\sinh(k_n\min(y,s))\sinh(k_n(b-\max(y,s)))}{k_n\sinh(k_nb)}.$$
用端点零值、函数连续及 $G_y(s^+,s)-G_y(s^-,s)=1$ 核对符号。最后 $u=h+\sum V_n\sin k_nx$，核查级数正则性、四边值与四角相容；角点冲突时不声称闭域连续。唯一性可对零边界调和差用最大值原理。