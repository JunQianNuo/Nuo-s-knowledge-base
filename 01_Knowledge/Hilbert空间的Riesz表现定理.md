---
schema_version: 2
type: proposition
time: '2026-11-15T09:08:24+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-10-第13节-泛函分析与PDE基础讲座]]'
---

# Hilbert空间的Riesz表现定理

## 条件、结论与约定

设$H$为实或复Hilbert空间，内积第一变量线性、第二变量共轭线性。记$H^*$为有界线性泛函空间。每个$l\in H^*$都有唯一$z_l\in H$使

$$
l(x)=(x,z_l)\quad(x\in H),\qquad \|l\|=\|z_l\|.
$$

非零$z$对应泛函$x\mapsto(x,z)$；Cauchy–Schwarz给范数上界$\|z\|$，取$x=z/\|z\|$得到等号，$z=0$显然成立。若两个向量表示同一个泛函，则$(x,z-w)=0$对所有$x$成立，取$x=z-w$得到唯一性。

存在性依赖Hilbert空间的完备性及正交投影。对非零$l$，其核为闭真子空间；选$e\in(\ker l)^\perp$且$\|e\|=1$。$l(e)\ne0$，否则$e$同时属于核与其正交补。令$c=l(x)/l(e)$，则$m=x-ce\in\ker l$，所以每个$x$可写成$x=m+ce$，于是$l(x)=cl(e)$，取$z_l=\overline{l(e)}e$便有$(x,z_l)=cl(e)$。这一段是对来源所用定理的解释性证明，不是课堂逐字记录。

## 复数情形的边界

$l\mapsto z_l$共轭线性：$z_{\alpha l+\beta k}=\overline\alpha z_l+\overline\beta z_k$。不能把这个映射误写成复线性。此处的表现定理也不同于实变函数中“依测度收敛可抽取几乎处处收敛子列”的[[01_Knowledge/Riesz定理]]。

## 后续用途

以[[01_Knowledge/内积空间与Hilbert空间]]和[[01_Knowledge/Hilbert闭子空间的正交投影定理]]为基础，通过固定变量把泛函表示成内积，可构造[[01_Knowledge/Hilbert空间有界算子的伴随]]和[[01_Knowledge/有界共轭双线性形式的算子表示]]。

## 本次来源

[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-10-第13节-泛函分析与PDE基础讲座]]。本文按已整理来源提炼；来源中的证明补足、教材校核及新编自测保留其整理属性，不作为教师逐字发言。
