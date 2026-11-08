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

对 $-X''=\lambda X,X(0)=0,X'(L)+hX(L)=0$，先声明 $h$ 的取值，再按 $\lambda$ 的正、零、负分支求非零解。

- $\lambda=\beta^2>0$：$X=\sin\beta x$，条件 $\beta\cos\beta L+h\sin\beta L=0$。保留这一不除以 $h$ 的式子可涵盖 $h=0$；在可除时写 $\tan\beta L=-\beta/h$。
- $\lambda=0$：$X=Cx$，存在非零解当且仅当 $h=-1/L$。
- $\lambda=-\kappa^2<0$：$X=\sinh\kappa x$，条件 $h=-\kappa\coth(\kappa L)$，只可能在 $h<-1/L$。

若 $h\ge0$，积分得 $\lambda\int X^2=\int(X')^2+hX(L)^2>0$，才可保证所有非平凡特征值为正。来源10月9日作业未在题面写明 $h\ge0$，其“非正特征值只有平凡解”的结论必须附此符号条件，不能当任意实 $h$ 的结论。