---
schema_version: 2
type: method
time: '2026-11-15T09:08:24+08:00'
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/作业/11月9日作业]]'
---

# 三维波动方程的Poisson球面公式

## 问题、记号与公式

解 $u_{tt}=a^2\Delta_3u+f(M,t)$，$M=(x,y,z)\in\mathbb R^3$、$t>0$，$a>0$，初位移 $\varphi$、初速度 $\psi$。设数据足够光滑，例如 $\varphi\in C^3$、$\psi\in C^2$，$f$ 各变量局部 $C^2$，以允许下述求导与积分交换。定义
$$
S_3(t)g(M)=t\mathcal M_{at}g(M)=\frac1{4\pi a^2t}\iint_{|Q-M|=at}g(Q)dS_Q,\quad t>0,
$$
其中 $\mathcal M$ 是 [[01_Knowledge/球面平均]]，$S_3(0)g=0$ 按极限。解为
$$
u=\partial_t[S_3(t)\varphi]+S_3(t)\psi+\int_0^tS_3(t-\tau)f(\cdot,\tau)d\tau.
$$
前两项分别处理初位移、初速度；第三项由 [[01_Knowledge/波动方程的Duhamel时间叠加]] 处理源。线性叠加要求分量初值、源和边界的和等于原数据。位移项对整个 $t\mathcal M_{at}\varphi$ 求导，不能直接照搬速度项。

## 两个多项式例子

1. $\varphi=yz,\psi=xz,f=0$。球面交叉矩消失，故 $S_3(t)\varphi=tyz$、$S_3(t)\psi=txz$，得 $u=yz+txz$。两项初值均满足，且 $u_{tt}=\Delta_3u=0$；没有波速 $a$ 是因为初值调和。
2. $\varphi=0,\psi=x^2+yz,f=2(y-t)$。初值解为 $v=t(x^2+yz)+a^2t^3/3$。固定激励时刻 $\tau$，源在球面上平均为 $2(y-\tau)$，所以
$$p=\int_0^t(t-\tau)2(y-\tau)d\tau=yt^2-t^3/3.$$
合并得 $u=t(x^2+yz)+yt^2+(a^2-1)t^3/3$。验算 $u_{tt}=2y+2(a^2-1)t$、$\Delta_3u=2t$，因此 $u_{tt}=a^2\Delta_3u+2(y-t)$，初速度亦正确。

平方矩产生 $a^2t^3/3$，源的时间积分产生 $-t^3/3$，不能混为一个来源。源函数必须代 $f(Q,\tau)$ 而非 $f(Q,t)$。本公式只积分有限传播范围，不要求全空间多项式可积或趋零；单次三维响应在球面上，降至二维后是整个圆盘，见 [[01_Knowledge/指数升维与二维波动方程的双曲余弦核]]。
