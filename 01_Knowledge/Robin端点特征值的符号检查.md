---
type: method
topics:
- '[[02_Maps/MOC-数学物理方程]]'
source:
- '[[03_Sources/Courses/数学物理方程/作业/10月9日作业]]'
schema_version: 2
time: '2026-11-08T09:10:48+08:00'
aliases: []
tags: []
---
# Robin端点特征值的符号检查

## 一句话

先查 Robin 参数的符号，再分别处理正、零、负特征值，不能预先只保留正根。

## 适用场景与操作步骤

对 $-X''=\lambda X,X(0)=0,X'(L)+hX(L)=0$，先声明 $h$ 的取值，再按 $\lambda$ 的正、零、负分支求非零解。

- $\lambda=\beta^2>0$：$X=\sin\beta x$，条件 $\beta\cos\beta L+h\sin\beta L=0$。保留这一不除以 $h$ 的式子可涵盖 $h=0$；在可除时写 $\tan\beta L=-\beta/h$。
- $\lambda=0$：$X=Cx$，存在非零解当且仅当 $h=-1/L$。
- $\lambda=-\kappa^2<0$：$X=\sinh\kappa x$，条件 $h=-\kappa\coth(\kappa L)$，只可能在 $h<-1/L$。

若 $h\ge0$，积分得 $\lambda\int X^2=\int(X')^2+hX(L)^2>0$，才可保证所有非平凡特征值为正。

来源10月9日作业未在题面写明 $h\ge0$，其“非正特征值只有平凡解”的结论必须附此符号条件，不能当任意实 $h$ 的结论。


## 全实参数的完整分支与正根定位

设 $L>0,h\in\mathbb R$。题面未声明 $h$ 的符号时，不必擅自指定数值；将所有分支写清即可给出完整的条件性答案。乘方程 $-X''=\lambda X$ 以 $X$ 并分部积分，得
$$\lambda\int_0^LX^2dx=\int_0^L(X')^2dx+hX(L)^2.$$
由 $X(L)=\int_0^LX'dx$ 与Cauchy不等式，有 $X(L)^2\le L\int(X')^2$，故当 $h>-1/L$ 时所有特征值为正（$-1/L<h<0$ 也包括在内）。$h=-1/L$ 时出现零特征值和特征函数 $X=x$；$h<-1/L$ 时有一个负特征值，其余正谱仍由未除法的行列式条件确定。

负分支写为 $h=-\kappa\coth(\kappa L)$，$\kappa>0$。函数 $\kappa\coth(\kappa L)$ 从 $1/L$ 严格增至无穷：令 $z=\kappa L$，导数符号由 $\sinh z\cosh z-z>0$ 确定（其导数为 $2\sinh^2z>0$）。因此 $h<-1/L$ 时负特征值恰有一个。

若已知 $h>0$，每个区间 $((2k+1)\pi/(2L),(k+1)\pi/L)$，$k\ge0$，恰有一个正波数根：$\tan(\beta L)$ 由负无穷递增至0，而 $-\beta/h$ 递减。$h=0$ 单独得到 $\beta_n=(n-1/2)\pi/L$，不能用除以 $h$ 的公式。$h\to+\infty$ 时各根趋 $n\pi/L$，$h\downarrow0$ 时趋半整数谱。

因此10月9日来源中“不可能有非正特征值”及所列负半支根区间只在其适当参数范围成立；原题 $h$ 未限定时，应使用本卡全分支结果，不把未知符号当作无法求解的缺题面。
