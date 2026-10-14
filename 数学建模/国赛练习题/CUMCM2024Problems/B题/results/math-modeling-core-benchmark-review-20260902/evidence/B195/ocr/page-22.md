（3）算法：本文模型是一个线性进程，有多个步骤，每个步骤都是一个循环。于是可以无限循环迭代。而且使用了非传统的线性模拟退火。筛选出最优解以及几个备用决策，把备用的决策再验算，便得出正确的解。

# 7.2 模型缺点

（1）迭代过程中有部分决策过程不合适，但是最终结果正确。

（2）通过模型，整个仿真过程转化成不断迭代的线性进程。但该模型忽视了一种情况，一般在生产中会优先使用检测出来的正品，但模型中存在检测到的是正品，又对其拆解的情况。但最后迭代得出的结果表明该现象为算法区域机制，对于最终结果不存在任何影响。

（3）生产规模很小的情况下，决策不一定最好，因为模型建立在10000套的基础上，更适用于常规规模。

# 8 参考文献

# 参考文献

［1］孙小素，尚书钰．计数标准型一次抽样检验方案设计方法探讨 兼议 GB/T 132622008改进问题［J]．山东工商学院学报，2024,38(01):69-76．

# 9 附录

## 9.1 程序结果汇总

## 9.2 代码汇总

from scipy,stats import norm

import math

import random

import matplotlib.pyplot asplt

import numpy as np

plt.rcParams['font,sans-serif']=[ $'KaiTi'$ 

plt.rcParams['axes.unicodeminus $']=Fals$ 

10def $quantile\_value(p):$ 

＃计算标准正态分布的第p分位数值

12

$$\text {value}=\text {norm.ppf(p)}$$

13

return value

14

15def $get\_n(p0,$ $,p1$ ,alpha,belta)

16

$\text {swap_{n}=quantile_{value}(1-alpha)*math.sqrt(p0*(1-p0))-}$ $quantil$  (belta)

math. $\text {sqrt}(\mathrm {p}1*(1-\mathrm {p}1))$ 

17

sWn $\mathrm {p}\_\mathrm {n}/=\mathrm {p}1-\mathrm {p}0$ 

18

returnswap $\_n**$  ~ if $\text {swap_{n}**}2<100$ else100

dxs.moe.g

10

<!-- 22 -->

