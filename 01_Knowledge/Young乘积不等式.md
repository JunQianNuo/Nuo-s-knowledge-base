---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-收敛性与积分理论]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/05-重积分与Lp空间/习题5.5-Young不等式-习题]]'
tags:
- Young不等式
---
# Young乘积不等式

## 适用条件与结论

若 $p,q>1$、$1/p+1/q=1$，则对a,b≥0，

$$
a^{1/p}b^{1/q}\le a/p+b/q.
$$

正值情形由ln凹性：$\ln(a/p+b/q)\ge p^{-1}\ln a+q^{-1}\ln b$，指数化即得；含0情形由连续性。

ln严格凹使等号当且仅当a=b。

写a=u^p、b=v^q，得到 $uv\le u^p/p+v^q/q$，等号当且仅当 $u^p=v^q$。

把函数按其Lp范数归一化后逐点应用，再积分，即为 [[01_Knowledge/Hölder不等式]] 的核心证明。

这是代数乘积版Young，不是 [[01_Knowledge/Young不等式(卷积版)]]。
