---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/04-Lebesgue积分/习题4.10-黎曼可积函数必为Lebesgue可积且积分值相等-习题]]'
---
# 黎曼积分与Lebesgue积分的一致性

## 适用条件与结论

若有界实函数f在 $[a,b]$ 黎曼可积，则它Lebesgue可积且两种积分相等。

取加细、网格趋0的分割，按每个子区间下确界、上确界构造阶梯函数 $\varphi_n\le f\le\psi_n$。

除可数分点外，$\varphi_n$ 递增、$\psi_n$ 递减；极限 $u,v$ 均可测且 $u\le f\le v$。

各阶梯积分恰为Darboux下和、上和。

有限区间上统一有界，用有界收敛得 $\int u=\int v=R\int f$。

由于 $v-u\ge0$ 且积分0，有 $v=u$ a.e.，所以 $f=u$ a.e.。

完备性给f可测，有界性给可积，两积分相同。

反向不成立，见 [[01_Knowledge/Dirichlet函数的两种积分行为]]。
