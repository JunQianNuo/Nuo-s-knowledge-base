---
schema_version: 2
type: proposition
time: '2026-11-15T09:35:21+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/作业/10.27]]'
---


# Riesz引理



## 条件与结论

设$X$为赋范空间，$M\subsetneq X$为真闭线性子空间，$0<\theta<1$。存在$u\in X$满足$\|u\|=1$，且$\operatorname{dist}(u,M)>\theta$。不要求$X$完备，也不保证取$\theta=1$时仍存在这样的向量。

## 证明与使用步骤

取$z\notin M$。闭性给$d=\operatorname{dist}(z,M)>0$。由下确界定义可选$y\in M$使$\|z-y\|<d/\theta$。令$u=(z-y)/\|z-y\|$。对任意$m\in M$，因为$y+\|z-y\|m\in M$，有

$$\|u-m\|=\frac{\|z-(y+\|z-y\|m)\|}{\|z-y\|}\ge\frac d{\|z-y\|}>\theta.$$

取下确界即得结论。应用时先核实子空间真且闭，再固定同一$\theta$递归选向量；作业第11题由此得到球中固定分离列，见[[01_Knowledge/球的相对列紧性刻画有限维]]。这是教材习题所调用引理的解释性证明。

## 本次补充来源

- [[03_Sources/Courses/泛函分析/作业/10.27]]

证明展开、自测、教材补足仍按原来源标记其整理性质，不冒充教师逐字讲授。
