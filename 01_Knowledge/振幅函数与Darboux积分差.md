---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.26-振幅函数与黎曼上下积分的关系-习题]]'
tags:
- 振幅函数
- 黎曼上下积分
---
# 振幅函数与Darboux积分差

## 适用条件与结论

对有界实函数 $f:[a,b]\to\mathbb R$，定义相对邻域振幅

$$
\omega_f(x)=\inf_{\delta>0}\sup_{u,v\in[a,b]\cap B(x,\delta)}|f(u)-f(v)|.
$$

它非负有界，且 $\omega_f(x)=0$ 当且仅当f在x相对连续。

振幅是上半连续函数：若某点振幅小于c，可取邻域振幅小于c，再对附近点取更小邻域，所以 $\{\omega_f<c\}$ 相对开，因而可测。

取加细且网格趋0的分割，子区间振幅阶梯函数 $\omega_n=M_{nj}-m_{nj}$，在所有分点上任取0。

除所有分点组成的可数集外，包含x的子区间是x邻域且直径趋0，故 $\omega_n(x)\to\omega_f(x)$。

统一有界及有限区间允许BCT，得到

$$
\int_a^b\omega_f=\lim_n\sum_j(M_{nj}-m_{nj})\Delta x_{nj}=\overline{\int_a^b}f-\underline{\int_a^b}f.
$$

此式把Darboux积分差表达为非负振幅的Lebesgue积分，是 [[01_Knowledge/黎曼可积充要条件]] 的直接证明工具。
