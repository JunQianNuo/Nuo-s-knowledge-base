---
schema_version: 2
type: proposition
time: '2026-11-15T09:35:21+08:00'
topics:
- '[[02_Maps/MOC-数理统计]]'
source:
- '[[03_Sources/Courses/数理统计/课堂笔记/2026-10-27-第15节-数理统计期末复习与新课讲授]]'
---


# 正态样本均值方差的MLE与无偏修正

> 一句话：正态方差的极大似然分母是n，无偏修正分母是n减1，二者服务不同准则。

独立同分布正态样本 $N(\mu,\sigma^2)$，$\sigma^2>0,n\ge2$，令 $Q=\sum(X_i-\bar X)^2$。非退化观测 $Q>0$ 时，对数似然
$$\ell=-\frac n2\log(2\pi\sigma^2)-\frac{Q+n(\bar X-\mu)^2}{2\sigma^2}$$
先在 $\mu=\bar X$ 最大，再对正方差优化得 $\hat\sigma^2_{MLE}=Q/n$。这与无偏估计 $S^2=Q/(n-1)$ 不同，因为 $Q/\sigma^2\sim\chi^2(n-1)$，从而 $E(Q/n)=(n-1)\sigma^2/n$ 而 $ES^2=\sigma^2$。

若所有观测完全相同，$Q=0$，在限制 $\sigma^2>0$ 的模型里似然随方差趋零而无界，不存在正方差内部的MLE；不能无条件把0写成合法正方差参数。

未知方差时 $(\bar X-\mu)/(S/\sqrt n)\sim t(n-1)$，反解得到双侧中心置信区间 $\bar X\pm t_{\alpha/2}(n-1)S/\sqrt n$，此处采用上侧分位数。若原课件将分母n的方差记为 $V_n$，相同标准误写成 $\sqrt{V_n}/\sqrt{n-1}$，符号名称相同也不能混用分母。已知方差则改用正态枢轴量，见 [[01_Knowledge/已知方差正态均值区间的长度与样本量设计]]。
