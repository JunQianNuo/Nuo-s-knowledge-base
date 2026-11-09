---
type: method
source:
- '[[03_Sources/Courses/归档/最优化方法/作业/11-拟牛顿法/考题-DFP-BFGS公式推导]]'
topics:
- '[[02_Maps/MOC-最优化]]'
schema_version: 2
time: '2026-11-08T17:59:22+08:00'
aliases: []
tags: []
---
# 拟牛顿逆更新的DFP与BFGS

## 适用场景与操作步骤

任务：用梯度差代替精确 Hessian 逆求下降方向。

给定 $H=H^T\succ0$，作下降线搜索 $s=x_+-x$，$y=\nabla f(x_+)-\nabla f(x)$。

先检查曲率 $s^Ty>0$，否则不能照套正定更新，需阻尼/跳过或调整线搜索。

DFP：$H_+=H+ss^T/(s^Ty)-Hyy^TH/(y^THy)$。

BFGS逆更新：$H_+=(I-\rho sy^T)H(I-\rho ys^T)+\rho ss^T$，$\rho=1/(y^Ts)$。

两者直接乘 $y$ 可验 $H_+y=s$，对称性显然；在曲率条件下正定性由非负平方项及不可能同时为0证明。

计算后检查对称性、割线残差 $H_+y-s$、正定性，再用 $d_+=-H_+g_+$。

精确线搜索的曲率保证还依赖下降方向/相应光滑性；不能对任意非凸任意步长宣称正曲率。

Wolfe 条件在下降步中可保证曲率。

SPD 二次函数且精确算术、精确线搜索等条件下有有限步性质，不作为浮点任意函数保证。

## 例子与核对

来源例 $Q=\operatorname{diag}(4,2),s=(10/9,5/9),y=(40/9,10/9)$：$y=Qs$，但不是标量比例（分量比为4、2）。

得到 $H_{DFP}=\begin{pmatrix}43/153&-19/153\\-19/153&305/306\end{pmatrix}$、$H_{BFGS}=\begin{pmatrix}23/81&-11/81\\-11/81&169/162\end{pmatrix}$，两者割线残差0。

来源提示“恰成比例”须勘误。
