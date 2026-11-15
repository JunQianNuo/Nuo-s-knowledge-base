---
schema_version: 2
type: concept
time: '2026-11-15T09:08:24+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-10-第13节-泛函分析与PDE基础讲座]]'
---

# Hilbert空间有界算子的伴随

设$T\in L(H_1,H_2)$，即$T:H_1\to H_2$有界且线性。固定$y\in H_2$，定义

$$
f_y(x)=(Tx,y)_{H_2},\qquad x\in H_1.
$$

它关于$x$线性，并由Cauchy–Schwarz和算子有界性满足

$$
|f_y(x)|\le\|Tx\|\|y\|\le\|T\|\|x\|\|y\|.
$$

Riesz定理给唯一$\widehat y\in H_1$使$f_y(x)=(x,\widehat y)_{H_1}$。定义$T^*y=\widehat y$，得到

$$
\boxed{(Tx,y)_{H_2}=(x,T^*y)_{H_1}},\qquad T^*:H_2\to H_1.
$$

这就是Hilbert共轭算子，也称伴随算子。注意映射方向反过来。课堂要求掌握“固定第二变量 → 有界线性泛函 → Riesz唯一表示 → 定义新算子”的流程，不只背最后公式。

**补全线性与有界性的验证**：将$\alpha y+\beta z$代入公式，两边第二变量都共轭线性，得到

$$
(x,T^*(\alpha y+\beta z))=(x,\alpha T^*y+\beta T^*z).
$$

唯一性给$T^*(\alpha y+\beta z)=\alpha T^*y+\beta T^*z$。又$\|T^*y\|=\|f_y\|\le\|T\|\|y\|$，故它确实有界。

> 一句话来说：伴随算子把内积一侧的作用转移到另一侧，同时反转定义域和值域。

有限维核对：在正规正交坐标下，$T^*$的矩阵是$\overline A^{\mathsf T}$；实数情形退化为转置。这里必须保留“正规正交坐标”和复共轭，不能泛称任意基下都是普通转置。

## 复矩阵核对（来源新编自测1）

1. 在$\mathbb C^2$的标准内积下，取$A=\begin{pmatrix}1&i\\0&2\end{pmatrix}$。求$A^*$与$(iA)^*$，并对$x=(0,1),y=(1,0)$检验伴随定义。

> [!hint]- 提示
> 矩阵先共轭再转置，标量$i$也要共轭。

> [!solution]- 解析
> $A^*=\begin{pmatrix}1&0\\-i&2\end{pmatrix}$，$(iA)^*=-iA^*$。$Ax=(i,2)$，所以$(Ax,y)=i$；$A^*y=(1,-i)$，故$(x,A^*y)=\overline{-i}=i$。

参见[[01_Knowledge/Hilbert空间的Riesz表现定理]]与[[01_Knowledge/伴随算子的运算与范数等式]]。

## 本次来源

[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-10-第13节-泛函分析与PDE基础讲座]]。本文按已整理来源提炼；来源中的证明补足、教材校核及新编自测保留其整理属性，不作为教师逐字发言。
