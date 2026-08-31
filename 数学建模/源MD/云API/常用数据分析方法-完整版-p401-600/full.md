## 回归分析概述

## 什么是回归分析？

研究一个因变量 (Y) 与一个或多个自变量 $( X _ { 1 } , X _ { 2 } , . . . , X _ { k } )$ 之间的定量关系，建立数学模型用于预测、控制和解释。

## 回归分析概述

## 什么是回归分析？

研究一个因变量 (Y) 与一个或多个自变量 $( X _ { 1 } , X _ { 2 } , . . . , X _ { k } )$ 之间的定量关系，建立数学模型用于预测、控制和解释。

回归分析的分类

<table><tr><td>分类依据</td><td>类型</td><td>说明</td></tr><tr><td>自变量个数</td><td>一元回归多元回归</td><td>只有一个自变量两个或以上自变量</td></tr><tr><td>回归函数形式</td><td>线性回归非线性回归</td><td>参数线性 $(Y = \beta_0 + \beta_1 X + \varepsilon)$ 参数非线性(如指数、Logistic等)</td></tr><tr><td>因变量类型</td><td>经典回归广义线性模型</td><td>因变量是连续型因变量可以是离散型(如0-1、计数)</td></tr></table>

## 一元线性回归模型假设

## 一元线性回归模型假设

模型形式

$$
Y = \beta_ {0} + \beta_ {1} X + \varepsilon
$$

其中： $\beta _ { 0 }$ 是截距， $\beta _ { 1 }$ 是斜率（回归系数），ε 是随机误差项。

## 一元线性回归模型假设

模型形式

$$
Y = \beta_ {0} + \beta_ {1} X + \varepsilon
$$

其中： $\beta _ { 0 }$ 是截距， $\beta _ { 1 }$ 是斜率（回归系数），ε 是随机误差项。

经典假设（高斯-马尔可夫假设）

• 线性性： $E ( Y | X ) = \beta _ { 0 } + \beta _ { 1 } X$ ，即 Y 的均值是X 的线性函数

• 零均值： $E ( \varepsilon | X ) = 0$ ，误差项的条件均值为0

• 同方差： $V a r ( \varepsilon | X ) = \sigma ^ { 2 }$ ，误差方差不随X 变化

• 无自相关： $C o v ( \varepsilon _ { i } , \varepsilon _ { j } ) = 0$ ，不同观测的误差不相关

• 正态性（可选）： $\varepsilon \sim N ( 0 , \sigma ^ { 2 } )$ ，用于假设检验和区间估计

## 一元线性回归模型假设

模型形式

$$
Y = \beta_ {0} + \beta_ {1} X + \varepsilon
$$

其中： $\beta _ { 0 }$ 是截距， $\beta _ { 1 }$ 是斜率（回归系数），ε 是随机误差项。

经典假设（高斯-马尔可夫假设）

• 线性性： $E ( Y | X ) = \beta _ { 0 } + \beta _ { 1 } X$ ，即 Y 的均值是X 的线性函数

• 零均值： $E ( \varepsilon | X ) = 0$ ，误差项的条件均值为0

• 同方差： $V a r ( \varepsilon | X ) = \sigma ^ { 2 }$ ，误差方差不随X 变化

• 无自相关： $C o v ( \varepsilon _ { i } , \varepsilon _ { j } ) = 0$ ，不同观测的误差不相关

• 正态性（可选）： $\varepsilon \sim N ( 0 , \sigma ^ { 2 } )$ ，用于假设检验和区间估计

高斯-马尔可夫定理

• 在满足前4 个假设下，OLS 估计量是最佳线性无偏估计 (BLUE)

最小二乘估计（OLS）

## 最小二乘估计（OLS）

估计思想

选择 $\beta _ { 0 }$ 和 $\beta _ { 1 }$ ，使残差平方和最小：

$$
\min Q = \sum_ {i = 1 \rightarrow n} e _ {i} ^ {2} = \sum (Y _ {i} - _ {i}) ^ {2} = \sum (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) ^ {2}
$$

## 最小二乘估计（OLS）

估计思想

选择 $\beta _ { 0 }$ 和 $\beta _ { 1 }$ ，使残差平方和最小：

$$
\min Q = \sum_ {i = 1 \rightarrow n} e _ {i} ^ {2} = \sum (Y _ {i} - _ {i}) ^ {2} = \sum (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) ^ {2}
$$

求解（对 $\beta _ { 0 }$ 和 $\beta _ { 1 }$ 求偏导并令其为 0）

$$
\text { 正规方程: } \left\{ \begin{array}{l} \sum (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) = 0 \\ \sum X _ {i} (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) = 0 \end{array} \right.
$$

解得： ${ \begin{array} { r } { { \hat { \beta } } _ { 1 } = \sum ( X _ { i } - X ) ( Y _ { i } - { \bar { Y } } ) / \sum ( X _ { i } - { \bar { X } } ) ^ { 2 } = S _ { x y } / S _ { x x } , \quad { \hat { \beta } } _ { 0 } = { \bar { Y } } - { \hat { \beta } } _ { 1 } \cdot { \bar { X } } } \end{array} }$

## 最小二乘估计（OLS）

估计思想

选择 $\beta _ { 0 }$ 和 $\beta _ { 1 }$ ，使残差平方和最小：

$$
\min Q = \sum_ {i = 1 \rightarrow n} e _ {i} ^ {2} = \sum (Y _ {i} - _ {i}) ^ {2} = \sum (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) ^ {2}
$$

求解（对 $\beta _ { 0 }$ 和 $\beta _ { 1 }$ 求偏导并令其为 0）

$$
\text { 正规方程: } \left\{ \begin{array}{l} \sum (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) = 0 \\ \sum X _ {i} (Y _ {i} - \beta_ {0} - \beta_ {1} X _ {i}) = 0 \end{array} \right.
$$

解得： ${ \begin{array} { r } { { \hat { \beta } } _ { 1 } = \sum ( X _ { i } - X ) ( Y _ { i } - { \bar { Y } } ) / \sum ( X _ { i } - { \bar { X } } ) ^ { 2 } = S _ { x y } / S _ { x x } , \quad { \hat { \beta } } _ { 0 } = { \bar { Y } } - { \hat { \beta } } _ { 1 } \cdot { \bar { X } } } \end{array} }$

几何意义：投影

$\hat { Y }$ 是 Y 在自变量张成的子空间上的正交投影。

残差 $e = Y - { \hat { Y } }$ 与 $\hat { Y }$ 正交（垂直），即 $\hat { Y } \cdot e = 0$ 。

这保证了残差平方和是最小的距离。

## 回归方程的显著性检验

## 回归方程的显著性检验

为什么需要检验？

即使 X 和Y 毫无关系，也能拟合出一条回归直线。需要检验回归关系是否真正存在。

## 回归方程的显著性检验

为什么需要检验？

即使 X 和Y 毫无关系，也能拟合出一条回归直线。需要检验回归关系是否真正存在。

## 三种等价的检验

<table><tr><td>检验方法</td><td>检验内容</td><td>统计量</td><td>一元/多元关系</td></tr><tr><td> $F$ 检验</td><td>整体显著性:所有  $\beta = 0$ ?</td><td> $F = \frac{MSR}{MSE} \sim F(1, n - 2)$ </td><td>一元中等价于  $t$  检验</td></tr><tr><td> $t$ 检验</td><td>单个系数 $\beta_1 = 0$ ?</td><td> $t = \frac{\hat{\beta}_1}{se(\hat{\beta}_1)} / \sim t(n - 2)$ </td><td>一元中与  $F$  检验等价</td></tr><tr><td>相关系数检验</td><td>相关系数 $\rho = 0$ ?</td><td> $t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}} \sim t(n - 2)$ </td><td>一元中等价</td></tr></table>

## 回归方程的显著性检验

为什么需要检验？

即使 X 和Y 毫无关系，也能拟合出一条回归直线。需要检验回归关系是否真正存在。

## 三种等价的检验

<table><tr><td>检验方法</td><td>检验内容</td><td>统计量</td><td>一元/多元关系</td></tr><tr><td> $F$ 检验</td><td>整体显著性:所有  $\beta = 0$ ?</td><td> $F = \frac{MSR}{MSE} \sim F(1, n - 2)$ </td><td>一元中等价于  $t$  检验</td></tr><tr><td> $t$ 检验</td><td>单个系数 $\beta_1 = 0$ ?</td><td> $t = \frac{\hat{\beta}_1}{se(\hat{\beta}_1)} / \sim t(n - 2)$ </td><td>一元中与  $F$  检验等价</td></tr><tr><td>相关系数检验</td><td>相关系数 $\rho = 0$ ?</td><td> $t = \frac{r\sqrt{n-2}}{\sqrt{1-r^2}} \sim t(n - 2)$ </td><td>一元中等价</td></tr></table>

## 一元线性回归中三者完全等价

$F = t ^ { 2 }$ ，F 检验的 p 值 = t 检验的 p 值 = 相关系数检验的p 值

$R ^ { 2 } = r ^ { 2 }$ （一元中，决定系数等于相关系数的平方）

• 多元回归中，F 检验整体，t 检验单个系数，不再等价

## 预测与控制

## 预测与控制

预测 (Prediction) 给定 $X = X _ { 0 }$ ，估计对应的 $Y _ { 0 }$ 或 $E ( Y _ { 0 } | X _ { 0 } )$ )。

点预测： $\hat { Y } _ { 0 } = \hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { 0 }$

## 预测与控制

预测 (Prediction) 给定 $X = X _ { 0 }$ ，估计对应的 $Y _ { 0 }$ 或 $E ( Y _ { 0 } | X _ { 0 } )$ )。

点预测： $\hat { Y } _ { 0 } = \hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { 0 }$

两种区间：

• 均值的置信区间： $E ( { Y _ { 0 } } | X _ { 0 } )$ 的区间估计（估计的是平均值）

• 个体的预测区间： $Y _ { 0 }$ 的区间估计（预测的是单个值）

注意：预测区间比置信区间更宽（因为个体波动更大）； $X _ { 0 }$ 离 $\bar { X }$ 越远，区间越宽（外推风险大）。

## 预测与控制

预测 (Prediction) 给定 $X = X _ { 0 }$ ，估计对应的 $Y _ { 0 }$ 或 $E ( Y _ { 0 } | X _ { 0 } )$ )。

点预测： $\hat { Y } _ { 0 } = \hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { 0 }$

两种区间：

• 均值的置信区间： $E ( { Y _ { 0 } } | X _ { 0 } )$ 的区间估计（估计的是平均值）

• 个体的预测区间： $Y _ { 0 }$ 的区间估计（预测的是单个值）

注意：预测区间比置信区间更宽（因为个体波动更大）； $X _ { 0 }$ 离 $\bar { X }$ 越远，区间越宽（外推风险大）。控制 (Control)

预测的反问题：要使Y 在指定范围内，X 应控制在什么范围？

## 预测与控制

预测 (Prediction) 给定 $X = X _ { 0 }$ ，估计对应的 $Y _ { 0 }$ 或 $E ( Y _ { 0 } | X _ { 0 } )$ )。

点预测： $\hat { Y } _ { 0 } = \hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { 0 }$

两种区间：

• 均值的置信区间： $E ( { Y _ { 0 } } | X _ { 0 } )$ 的区间估计（估计的是平均值）

• 个体的预测区间： $Y _ { 0 }$ 的区间估计（预测的是单个值）

注意：预测区间比置信区间更宽（因为个体波动更大）； $X _ { 0 }$ 离 $\bar { X }$ 越远，区间越宽（外推风险大）。

控制 (Control)

预测的反问题：要使Y 在指定范围内，X 应控制在什么范围？

例：要使产量Y 在 (100, 120) 之间，温度 X 应控制在多少度？求解思路：

Y 的下限： $\hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { l o w e r } \approx Y _ { l o w e r }$

Y 的上限： $\hat { \beta } _ { 0 } + \hat { \beta } _ { 1 } X _ { u p p e r } \approx Y _ { u p p e r }$

解得 X 的控制区间。

## 实例：身高与体重的回归分析

## 实例：身高与体重的回归分析

## 数据

随机抽取10名学生，测量身高 (cm) 和体重(kg).

身高：160, 165, 170, 175, 180, 158, 168, 172, 178, 162;

体重：50, 55, 60, 65, 70, 48, 56, 62, 68, 52.

## 实例：身高与体重的回归分析

## 数据

随机抽取10名学生，测量身高 (cm) 和体重(kg).

身高：160, 165, 170, 175, 180, 158, 168, 172, 178, 162;

体重：50, 55, 60, 65, 70, 48, 56, 62, 68, 52.

## 计算结果

$$
\bar {x} = 1 6 8. 8, \bar {y} = 5 8. 6, S _ {x x} = \sum (x _ {i} - \bar {x}) ^ {2} = 4 5 7. 6, S _ {x y} = \sum (x _ {i} - \bar {x}) (y _ {i} - \bar {y}) = 4 0 5. 8
$$

$$
\hat {\beta} _ {1} = 4 0 5. 8 / 4 5 7. 6 = 0. 8 8 7, \hat {\beta} _ {0} = 5 8. 6 - 0. 8 8 7 \times 1 6 8. 8 = 5 8. 6 - 1 4 9. 7 = - 9 1. 1
$$

回归方程： $\hat { Y } = - 9 1 . 1 + 0 . 8 8 7 X$

## 实例：身高与体重的回归分析

## 数据

随机抽取10名学生，测量身高 (cm) 和体重(kg).

身高：160, 165, 170, 175, 180, 158, 168, 172, 178, 162;

体重：50, 55, 60, 65, 70, 48, 56, 62, 68, 52.

## 计算结果

$$
\bar {x} = 1 6 8. 8, \bar {y} = 5 8. 6, S _ {x x} = \sum (x _ {i} - \bar {x}) ^ {2} = 4 5 7. 6, S _ {x y} = \sum (x _ {i} - \bar {x}) (y _ {i} - \bar {y}) = 4 0 5. 8
$$

$$
\hat {\beta} _ {1} = 4 0 5. 8 / 4 5 7. 6 = 0. 8 8 7, \hat {\beta} _ {0} = 5 8. 6 - 0. 8 8 7 \times 1 6 8. 8 = 5 8. 6 - 1 4 9. 7 = - 9 1. 1
$$

回归方程： $\hat { Y } = - 9 1 . 1 + 0 . 8 8 7 X$

含义：身高每增加1cm，体重平均增加约 0.887kg。

## 实例：身高与体重的回归分析

## 数据

随机抽取10名学生，测量身高 (cm) 和体重(kg).

身高：160, 165, 170, 175, 180, 158, 168, 172, 178, 162;

体重：50, 55, 60, 65, 70, 48, 56, 62, 68, 52.

## 计算结果

$$
\bar {x} = 1 6 8. 8, \bar {y} = 5 8. 6, S _ {x x} = \sum (x _ {i} - \bar {x}) ^ {2} = 4 5 7. 6, S _ {x y} = \sum (x _ {i} - \bar {x}) (y _ {i} - \bar {y}) = 4 0 5. 8
$$

$$
\hat {\beta} _ {1} = 4 0 5. 8 / 4 5 7. 6 = 0. 8 8 7, \hat {\beta} _ {0} = 5 8. 6 - 0. 8 8 7 \times 1 6 8. 8 = 5 8. 6 - 1 4 9. 7 = - 9 1. 1
$$

回归方程： $\hat { Y } = - 9 1 . 1 + 0 . 8 8 7 X$

含义：身高每增加1cm，体重平均增加约 0.887kg。

$R ^ { 2 } = 0 . 9 8$ （拟合程度很高）

## 实例：身高与体重的回归分析

## 数据

随机抽取10名学生，测量身高 (cm) 和体重(kg).

身高：160, 165, 170, 175, 180, 158, 168, 172, 178, 162;

体重：50, 55, 60, 65, 70, 48, 56, 62, 68, 52.

## 计算结果

$$
\bar {x} = 1 6 8. 8, \bar {y} = 5 8. 6, S _ {x x} = \sum (x _ {i} - \bar {x}) ^ {2} = 4 5 7. 6, S _ {x y} = \sum (x _ {i} - \bar {x}) (y _ {i} - \bar {y}) = 4 0 5. 8
$$

$$
\hat {\beta} _ {1} = 4 0 5. 8 / 4 5 7. 6 = 0. 8 8 7, \hat {\beta} _ {0} = 5 8. 6 - 0. 8 8 7 \times 1 6 8. 8 = 5 8. 6 - 1 4 9. 7 = - 9 1. 1
$$

回归方程： $\hat { Y } = - 9 1 . 1 + 0 . 8 8 7 X$

含义：身高每增加1cm，体重平均增加约 0.887kg。

$R ^ { 2 } = 0 . 9 8$ （拟合程度很高）

$F$ 检验 $p < 0 . 0 0 1$ （回归关系高度显著）

## 多元线性回归：模型的矩阵形式

## 多元线性回归：模型的矩阵形式

模型

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \ldots + \beta_ {k} X _ {k} + \varepsilon
$$

n 个观测写成矩阵形式： $Y = X \beta + \varepsilon$

## 多元线性回归：模型的矩阵形式

模型

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \ldots + \beta_ {k} X _ {k} + \varepsilon
$$

n 个观测写成矩阵形式： $Y = X \beta + \varepsilon$

各矩阵维度

$Y : n \times 1$ 的因变量向量

$X : n \times ( k + 1 )$ 的设计矩阵（第一列全为1，对应截距项）

$\beta : ( k + 1 ) \times 1$ 的参数向量

$\varepsilon : n \times 1$ 的误差向量

## 多元线性回归：模型的矩阵形式

模型

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \ldots + \beta_ {k} X _ {k} + \varepsilon
$$

n 个观测写成矩阵形式： $Y = X \beta + \varepsilon$

各矩阵维度

$Y : n \times 1$ 的因变量向量

X $: n \times ( k + 1 )$ 的设计矩阵（第一列全为1，对应截距项）

$\beta : ( k + 1 ) \times 1$ 的参数向量

$\varepsilon : n \times 1$ 的误差向量

最小二乘估计的矩阵形式

假设： $E ( \varepsilon ) = 0 , C o v ( \varepsilon ) = \sigma ^ { 2 } I$ （零均值、同方差、无自相关）

$$
\hat {\beta} = (X ^ {\prime} X) ^ {- 1} X ^ {\prime} Y
$$

## 多元线性回归：模型的矩阵形式

模型

$$
Y = \beta_ {0} + \beta_ {1} X _ {1} + \beta_ {2} X _ {2} + \ldots + \beta_ {k} X _ {k} + \varepsilon
$$

n 个观测写成矩阵形式： $Y = X \beta + \varepsilon$

各矩阵维度

$Y : n \times 1$ 的因变量向量

$X : n \times ( k + 1 )$ 的设计矩阵（第一列全为1，对应截距项）

$\beta : ( k + 1 ) \times 1$ 的参数向量

$\varepsilon : n \times 1$ 的误差向量

最小二乘估计的矩阵形式

假设： $E ( \varepsilon ) = 0 , C o v ( \varepsilon ) = \sigma ^ { 2 } I$ （零均值、同方差、无自相关）

$$
\hat {\beta} = (X ^ {\prime} X) ^ {- 1} X ^ {\prime} Y
$$

这是一个统一的公式，一元回归是它的特例 $\left( k = 1 \right)$ ）。

## 多元回归的显著性检验

## 多元回归的显著性检验

整体显著性检验（F 检验）

$H _ { 0 } : \beta _ { 1 } = \beta _ { 2 } = . . . = \beta _ { k } = 0$ （所有自变量都没有解释力）

$H _ { 1 }$ : 至少有一个 $\beta _ { j } \neq 0$

$$
F = \frac {S S R / k}{S S E / (n - k - 1)} = \frac {M S R}{M S E} \sim F (k, n - k - 1)
$$

若 $F > F \alpha ( k , n - k - 1 )$ ，则拒绝 $H _ { 0 }$ ，认为回归方程整体显著。

## 多元回归的显著性检验

整体显著性检验（F 检验）

$H _ { 0 } : \beta _ { 1 } = \beta _ { 2 } = . . . = \beta _ { k } = 0$ （所有自变量都没有解释力）

$H _ { 1 }$ : 至少有一个 $\beta _ { j } \neq 0$

$$
F = \frac {S S R / k}{S S E / (n - k - 1)} = \frac {M S R}{M S E} \sim F (k, n - k - 1)
$$

若 $F > F \alpha ( k , n - k - 1 )$ ，则拒绝 $H _ { 0 }$ ，认为回归方程整体显著。

单个系数的显著性检验（t 检验）

$$
H _ {0}: \beta_ {j} = 0 \text { vs } H _ {1}: \beta_ {j} \neq 0
$$

$$
t _ {j} = \hat {\beta} _ {j} / s e (\hat {\beta} _ {j}) \sim t (n - k - 1)
$$

## 多元回归的显著性检验

整体显著性检验（F 检验）

$H _ { 0 } : \beta _ { 1 } = \beta _ { 2 } = . . . = \beta _ { k } = 0$ （所有自变量都没有解释力）

$H _ { 1 }$ : 至少有一个 $\beta _ { j } \neq 0$

$$
F = \frac {S S R / k}{S S E / (n - k - 1)} = \frac {M S R}{M S E} \sim F (k, n - k - 1)
$$

若 $F > F \alpha ( k , n - k - 1 )$ ，则拒绝 $H _ { 0 }$ ，认为回归方程整体显著。

单个系数的显著性检验（t 检验）

$$
H _ {0}: \beta_ {j} = 0 \text { vs } H _ {1}: \beta_ {j} \neq 0
$$

$$
t _ {j} = \hat {\beta} _ {j} / s e (\hat {\beta} _ {j}) \sim t (n - k - 1)
$$

检验的是：在控制其他变量后，第j个变量是否还有显著的解释力。

## 多元回归的显著性检验

整体显著性检验（F 检验）

$H _ { 0 } : \beta _ { 1 } = \beta _ { 2 } = . . . = \beta _ { k } = 0$ （所有自变量都没有解释力）

$H _ { 1 }$ : 至少有一个 $\beta _ { j } \neq 0$

$$
F = \frac {S S R / k}{S S E / (n - k - 1)} = \frac {M S R}{M S E} \sim F (k, n - k - 1)
$$

若 $F > F \alpha ( k , n - k - 1 )$ ，则拒绝 $H _ { 0 }$ ，认为回归方程整体显著。

单个系数的显著性检验（t 检验）

$$
H _ {0}: \beta_ {j} = 0 \text { vs } H _ {1}: \beta_ {j} \neq 0
$$

$$
t _ {j} = \hat {\beta} _ {j} / s e (\hat {\beta} _ {j}) \sim t (n - k - 1)
$$

检验的是：在控制其他变量后，第j个变量是否还有显著的解释力。

多元回归中的注意事项

• $F$ 显著不代表每个变量都显著，可能是少数变量在起作用

• t 检验是”控制其他变量后”的边际效应，不是变量单独的作用

• 变量之间可能存在共线性，影响系数估计的稳定性

回归诊断：残差分析

## 回归诊断：残差分析

为什么做残差分析？

检验模型假设是否满足，发现异常值和影响点。

## 回归诊断：残差分析

为什么做残差分析？

检验模型假设是否满足，发现异常值和影响点。

## 残差图及其作用

<table><tr><td>残差图类型</td><td>检验什么</td><td>理想形态</td><td>问题信号</td></tr><tr><td>残差 vs 拟合值</td><td>线性性,同方差</td><td>随机散布在 0 附近</td><td>有曲线趋势=非线性;喇叭形=异方差</td></tr><tr><td>残差的正态概率图</td><td>正态性</td><td>点沿对角线分布</td><td>严重偏离直线=非正态</td></tr><tr><td>残差 vs 自变量</td><td>函数形式</td><td>随机散布</td><td>有趋势=需变换变量</td></tr><tr><td>时间序列残差图</td><td>自相关</td><td>无规律波动</td><td>有规律的循环=自相关</td></tr></table>

## 回归诊断：残差分析

## 为什么做残差分析？

检验模型假设是否满足，发现异常值和影响点。

## 残差图及其作用

<table><tr><td>残差图类型</td><td>检验什么</td><td>理想形态</td><td>问题信号</td></tr><tr><td>残差 vs 拟合值</td><td>线性性,同方差</td><td>随机散布在 0 附近</td><td>有曲线趋势=非线性;喇叭形=异方差</td></tr><tr><td>残差的正态概率图</td><td>正态性</td><td>点沿对角线分布</td><td>严重偏离直线=非正态</td></tr><tr><td>残差 vs 自变量</td><td>函数形式</td><td>随机散布</td><td>有趋势=需变换变量</td></tr><tr><td>时间序列残差图</td><td>自相关</td><td>无规律波动</td><td>有规律的循环=自相关</td></tr></table>

## 异常值检测

• 标准化残差、Cook距离、杠杆值等指标；异常值可能严重影响回归结果，需谨慎处理

回归诊断：共线性与 VIF

## 回归诊断：共线性与 VIF

什么是多重共线性？

自变量之间存在较强的线性相关关系。

## 回归诊断：共线性与 VIF

## 什么是多重共线性？

自变量之间存在较强的线性相关关系。

## 共线性的危害

• 系数估计不稳定，符号可能与预期相反

• 系数标准误变大，t 检验不显著（明明重要的变量却不显著）

• 模型整体F显著，但单个变量都不显著

• 变量的重要性无法准确判断

## 回归诊断：共线性与 VIF

## 什么是多重共线性？

自变量之间存在较强的线性相关关系。

共线性的危害

• 系数估计不稳定，符号可能与预期相反

• 系数标准误变大，t 检验不显著（明明重要的变量却不显著）

• 模型整体F显著，但单个变量都不显著

• 变量的重要性无法准确判断

VIF（方差膨胀因子）诊断

$$
V I F _ {j} = 1 / (1 - R _ {j} ^ {2})
$$

其中 $R _ { j } ^ { 2 }$ 是第 j 个自变量对其他所有自变量回归的决定系数。

## 回归诊断：共线性与 VIF

## 什么是多重共线性？

自变量之间存在较强的线性相关关系。

## 共线性的危害

• 系数估计不稳定，符号可能与预期相反

• 系数标准误变大，t 检验不显著（明明重要的变量却不显著）

• 模型整体F显著，但单个变量都不显著

• 变量的重要性无法准确判断

## VIF（方差膨胀因子）诊断

$$
V I F _ {j} = 1 / (1 - R _ {j} ^ {2})
$$

其中 $R _ { j } ^ { 2 }$ 是第 j 个自变量对其他所有自变量回归的决定系数。

判断标准：

• VIF > 5：存在中等程度共线性

• VIF > 10：存在严重共线性（需要处理）

## 回归诊断：共线性与 VIF

## 什么是多重共线性？

自变量之间存在较强的线性相关关系。

## 共线性的危害

• 系数估计不稳定，符号可能与预期相反

• 系数标准误变大，t 检验不显著（明明重要的变量却不显著）

• 模型整体F显著，但单个变量都不显著

• 变量的重要性无法准确判断

## VIF（方差膨胀因子）诊断

$$
V I F _ {j} = 1 / (1 - R _ {j} ^ {2})
$$

其中 $R _ { j } ^ { 2 }$ 是第 j 个自变量对其他所有自变量回归的决定系数。

判断标准：

• VIF > 5：存在中等程度共线性

• VIF > 10：存在严重共线性（需要处理）

处理方法：删除变量、合并变量、主成分回归、岭回归等。

变量选择：逐步回归、AIC/BIC

## 变量选择：逐步回归、AIC/BIC

逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

## 变量选择：逐步回归、AIC/BIC

## 逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

信息准则：AIC 与 BIC

## 变量选择：逐步回归、AIC/BIC

逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

信息准则：AIC 与 BIC

AIC (赤池信息准则)： $A I C = - 2 l n ( L ) + 2 k$

## 变量选择：逐步回归、AIC/BIC

逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

## 信息准则：AIC 与 BIC

AIC (赤池信息准则)： $A I C = - 2 l n ( L ) + 2 k$

BIC (贝叶斯信息准则)： $B I C = - 2 l n ( L ) + k \cdot l n ( n )$

## 变量选择：逐步回归、AIC/BIC

## 逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

## 信息准则：AIC 与 BIC

AIC (赤池信息准则)： $A I C = - 2 l n ( L ) + 2 k$

BIC (贝叶斯信息准则)： $B I C = - 2 l n ( L ) + k \cdot l n ( n )$

• L 是似然函数值，k 是参数个数，n 是样本量

• 准则：AIC/BIC 越小越好

• 平衡拟合优度和模型简洁性（惩罚复杂模型）

• BIC 对复杂模型的惩罚更重，倾向于选择更简洁的模型

## 变量选择：逐步回归、AIC/BIC

## 逐步回归 (Stepwise Regression)

• 向前选择：从无到有，逐个加入最显著的变量

• 向后剔除：从全模型开始，逐个剔除最不显著的变量

• 逐步回归：向前+向后，每步既可加入也可剔除（最常用）

• 共同特点：基于显著性检验（p 值）选择变量

## 信息准则：AIC 与 BIC

AIC (赤池信息准则)：AI C = −2ln(L) + 2k

BIC (贝叶斯信息准则)：BI C = −2ln(L) + k · ln(n)

• L 是似然函数值，k 是参数个数，n 是样本量

• 准则：AIC/BIC 越小越好

• 平衡拟合优度和模型简洁性（惩罚复杂模型）

• BIC 对复杂模型的惩罚更重，倾向于选择更简洁的模型

## 核心原则

• ”如无必要，勿增实体”——奥卡姆剃刀原则：能用简单模型就不用复杂模型

Logistic 回归

## Logistic 回归

适用场景

因变量Y 是二分类变量（0/1，如是否患病、是否购买、是否成功）。

## Logistic 回归

## 适用场景

因变量Y 是二分类变量（0/1，如是否患病、是否购买、是否成功）。

## 为什么不用线性回归？

• Y 只能取 0 和1，但线性回归预测值可能超出 [0,1] 范围

• 误差项不满足正态性和同方差假设

• 需要用 S 形曲线连接 X 和 $P ( Y = 1 | X )$

## Logistic 回归

## 适用场景

因变量Y 是二分类变量（0/1，如是否患病、是否购买、是否成功）。

## 为什么不用线性回归？

• Y 只能取 0 和1，但线性回归预测值可能超出 [0,1] 范围

• 误差项不满足正态性和同方差假设

• 需要用 S 形曲线连接 X 和 $P ( Y = 1 | X )$

## Logit 变换

设 $p = P ( Y = 1 | X )$ ，定义 $l o g i t ( p ) = l n ( p / ( 1 - p ) )$

模型： $l o g i t ( p ) = \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k }$

等价地： $p = e x p ( \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k } ) / ( 1 + e x p ( \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k } ) )$

## Logistic 回归

## 适用场景

因变量Y 是二分类变量（0/1，如是否患病、是否购买、是否成功）。

## 为什么不用线性回归？

• Y 只能取 0 和1，但线性回归预测值可能超出 [0,1] 范围

• 误差项不满足正态性和同方差假设

• 需要用 S 形曲线连接 X 和 $P ( Y = 1 | X )$

## Logit 变换

设 $p = P ( Y = 1 | X )$ ，定义 $l o g i t ( p ) = l n ( p / ( 1 - p ) )$

模型： $l o g i t ( p ) = \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k }$

等价地： $p = e x p ( \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k } ) / ( 1 + e x p ( \beta _ { 0 } + \beta _ { 1 } X _ { 1 } + . . . + \beta _ { k } X _ { k } ) )$

OR 值（优势比）解释：

$X _ { j }$ 增加 1 个单位，优势比变为原来的 $e x p ( \beta _ { j } )$ 倍。

若 $e x p ( \beta _ { j } ) > 1 $ 该因素是危险因素；若< 1 → 保护因素。

## 本章小结

## 本章小结

一元线性回归

• 模型： $Y = \beta _ { 0 } + \beta _ { 1 } X + \varepsilon$ ，高斯-马尔可夫假设

• OLS估计：最小化残差平方和，几何上是正交投影

• F 检验、t 检验、相关系数检验三者等价

## 本章小结

## 一元线性回归

• 模型： $Y = \beta _ { 0 } + \beta _ { 1 } X + \varepsilon$ ，高斯-马尔可夫假设

• OLS估计：最小化残差平方和，几何上是正交投影

• F 检验、t 检验、相关系数检验三者等价

## 多元线性回归

• 矩阵形式： $\boldsymbol { Y } = \boldsymbol { X } \beta + \boldsymbol { \varepsilon } , \boldsymbol { \hat { \beta } } = ( \boldsymbol { X } ^ { \prime } \boldsymbol { X } ) ^ { - 1 } \boldsymbol { X } ^ { \prime } \boldsymbol { Y }$

• F 检验整体显著性，t 检验单个系数（边际效应）

• 回归诊断：残差分析检验假设，VIF 诊断共线性

## 本章小结

## 一元线性回归

• 模型： $Y = \beta _ { 0 } + \beta _ { 1 } X + \varepsilon$ ，高斯-马尔可夫假设

• OLS估计：最小化残差平方和，几何上是正交投影

• F 检验、t 检验、相关系数检验三者等价

## 多元线性回归

• 矩阵形式： $\boldsymbol { Y } = \boldsymbol { X } \beta + \boldsymbol { \varepsilon } , \boldsymbol { \hat { \beta } } = ( \boldsymbol { X } ^ { \prime } \boldsymbol { X } ) ^ { - 1 } \boldsymbol { X } ^ { \prime } \boldsymbol { Y }$

• F 检验整体显著性，t 检验单个系数（边际效应）

• 回归诊断：残差分析检验假设，VIF 诊断共线性

## 广义线性模型

• 变量选择：逐步回归、 $\mathrm { A I C / B I C }$ ，遵循简洁原则

• Logistic 回归：二分类因变量，logit 变换，OR 值解释

• 是经典线性回归的推广，适用更广泛的数据类型

## 本章小结

## 一元线性回归

• 模型： $Y = \beta _ { 0 } + \beta _ { 1 } X + \varepsilon$ ，高斯-马尔可夫假设

• OLS估计：最小化残差平方和，几何上是正交投影

• F 检验、t 检验、相关系数检验三者等价

## 多元线性回归

• 矩阵形式： $\boldsymbol { Y } = \boldsymbol { X } \beta + \boldsymbol { \varepsilon } , \boldsymbol { \hat { \beta } } = ( \boldsymbol { X } ^ { \prime } \boldsymbol { X } ) ^ { - 1 } \boldsymbol { X } ^ { \prime } \boldsymbol { Y }$

• F 检验整体显著性，t 检验单个系数（边际效应）

• 回归诊断：残差分析检验假设，VIF 诊断共线性

## 广义线性模型

• 变量选择：逐步回归、AIC/BIC，遵循简洁原则

• Logistic 回归：二分类因变量，logit 变换，OR 值解释

• 是经典线性回归的推广，适用更广泛的数据类型

## 下章预告

• 第6 章：多元统计分析——处理多变量数据的降维与分类方法

## 第 6 章 多元统计分析

Multivariate Statistical Analysis

## 多元正态分布简述

## 多元正态分布简述

## 定义

$p$ 维随机向量 $X = ( X _ { 1 } , X _ { 2 } , . . . , X _ { p } ) ^ { \prime }$ 服从多元正态分布，记为 $X \sim N _ { p } ( \mu , \Sigma )$ 其中 $\mu$ 是 $p \times 1$ 均值向量，Σ 是 $p \times p$ 协方差矩阵（对称正定）。

## 多元正态分布简述

定义

$p$ 维随机向量 $X = ( X _ { 1 } , X _ { 2 } , . . . , X _ { p } ) ^ { \prime }$ 服从多元正态分布，记为 $X \sim N _ { p } ( \mu , \Sigma )$ 其中 $\mu$ 是 $p \times 1$ 均值向量， $\Sigma$ 是 $p \times p$ 协方差矩阵（对称正定）。

概率密度函数：

$$
f (x) = (2 \pi) ^ {- \frac {p}{2}} | \Sigma | ^ {- \frac {1}{2}} \cdot e x p (- \frac {1}{2} (x - \mu) ^ {\prime} \Sigma^ {- 1} (x - \mu))
$$

## 多元正态分布简述

定义

$p$ 维随机向量 $X = ( X _ { 1 } , X _ { 2 } , . . . , X _ { p } ) ^ { \prime }$ 服从多元正态分布，记为 $X \sim N _ { p } ( \mu , \Sigma )$ 其中 $\mu$ 是 $p \times 1$ 均值向量，Σ 是 $p \times p$ 协方差矩阵（对称正定）。

概率密度函数：

$$
f (x) = (2 \pi) ^ {- \frac {p}{2}} | \Sigma | ^ {- \frac {1}{2}} \cdot e x p (- \frac {1}{2} (x - \mu) ^ {\prime} \Sigma^ {- 1} (x - \mu))
$$

重要性质

• 多元正态的任意线性组合仍为正态分布

• 多元正态的边缘分布仍是正态分布

• 不相关 ⇐⇒独立（对正态分布而言）

• 条件分布也是正态分布

• 马氏距离： $D ^ { 2 } = ( x - \mu ) ^ { \prime } \Sigma ^ { - 1 } ( x - \mu )$ 服从 $\chi ^ { 2 } ( p )$

主成分分析：几何意义

## 主成分分析：几何意义

## PCA 是什么？

Principal Component Analysis：在损失很少信息的前提下，将多个相关变量转化为少数几个互不相关的综合指标（主成分）。想象p 维空间中的数据点云：

## 主成分分析：几何意义

## PCA 是什么？

Principal Component Analysis：在损失很少信息的前提下，将多个相关变量转化为少数几个互不相关的综合指标（主成分）。想象p 维空间中的数据点云：

• 第一主成分：数据变异最大的方向（最长轴）

• 第二主成分：与第一主成分正交的方向中变异最大的

• 第三主成分：与前两个正交，依此类推...

## 主成分分析：几何意义

## PCA 是什么？

Principal Component Analysis：在损失很少信息的前提下，将多个相关变量转化为少数几个互不相关的综合指标（主成分）。想象p 维空间中的数据点云：

• 第一主成分：数据变异最大的方向（最长轴）

• 第二主成分：与第一主成分正交的方向中变异最大的

• 第三主成分：与前两个正交，依此类推...

## 几何意义：坐标系旋转

相当于把坐标系旋转到与数据的” 自然坐标轴” 对齐。

新的坐标轴（主成分）互不相关，且按方差从大到小排列。

## 主成分分析：几何意义

## PCA 是什么？

Principal Component Analysis：在损失很少信息的前提下，将多个相关变量转化为少数几个互不相关的综合指标（主成分）。想象p 维空间中的数据点云：

• 第一主成分：数据变异最大的方向（最长轴）

• 第二主成分：与第一主成分正交的方向中变异最大的

• 第三主成分：与前两个正交，依此类推...

## 几何意义：坐标系旋转

相当于把坐标系旋转到与数据的” 自然坐标轴” 对齐。

新的坐标轴（主成分）互不相关，且按方差从大到小排列。

目的：用前几个主成分代替原始变量，实现降维。

## 主成分分析：几何意义

## PCA 是什么？

Principal Component Analysis：在损失很少信息的前提下，将多个相关变量转化为少数几个互不相关的综合指标（主成分）。想象p 维空间中的数据点云：

• 第一主成分：数据变异最大的方向（最长轴）

• 第二主成分：与第一主成分正交的方向中变异最大的

• 第三主成分：与前两个正交，依此类推...

## 几何意义：坐标系旋转

相当于把坐标系旋转到与数据的” 自然坐标轴” 对齐。

新的坐标轴（主成分）互不相关，且按方差从大到小排列。

目的：用前几个主成分代替原始变量，实现降维。

## 核心思想

• ”用最少的维度，保留最多的信息（方差）”

主成分分析：代数推导

## 主成分分析：代数推导

## 数学问题

找系数向量 $a _ { 1 }$ ，使 $Y _ { 1 } = a _ { 1 } ^ { \prime } X$ 的方差最大，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

$$
V a r (Y _ {1}) = V a r (a _ {1} ^ {\prime} X) = a _ {1} ^ {\prime} \Sigma a _ {1}
$$

用拉格朗日乘数法最大化 $a _ { 1 } ^ { \prime } \Sigma a _ { 1 }$ ，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

## 主成分分析：代数推导

## 数学问题

找系数向量 $a _ { 1 }$ ，使 $Y _ { 1 } = a _ { 1 } ^ { \prime } X$ 的方差最大，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

$$
V a r (Y _ {1}) = V a r (a _ {1} ^ {\prime} X) = a _ {1} ^ {\prime} \Sigma a _ {1}
$$

用拉格朗日乘数法最大化 $a _ { 1 } ^ { \prime } \Sigma a _ { 1 }$ ，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

转化为特征值问题

对 $\Sigma$ 做特征值分解： $\Sigma = U \Lambda U ^ { \prime }$

其中 $\Lambda = d i a g ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { p } ) , \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { p } \geq 0$

$U = ( u _ { 1 } , u _ { 2 } , . . . , u _ { p } )$ 是正交矩阵，列是特征向量。

第 $i$ 主成分： $Y _ { i } = u _ { i } ^ { \prime } X$ ，方差为 $\lambda _ { i }$ 。

## 主成分分析：代数推导

## 数学问题

找系数向量 $a _ { 1 }$ ，使 $Y _ { 1 } = a _ { 1 } ^ { \prime } X$ 的方差最大，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

$$
V a r (Y _ {1}) = V a r (a _ {1} ^ {\prime} X) = a _ {1} ^ {\prime} \Sigma a _ {1}
$$

用拉格朗日乘数法最大化 $a _ { 1 } ^ { \prime } \Sigma a _ { 1 }$ ，约束 $a _ { 1 } ^ { \prime } a _ { 1 } = 1$ 。

转化为特征值问题

对 $\Sigma$ 做特征值分解： $\Sigma = U \Lambda U ^ { \prime }$

其中 $\Lambda = d i a g ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { p } ) , \lambda _ { 1 } \geq \lambda _ { 2 } \geq . . . \geq \lambda _ { p } \geq 0$

$U = ( u _ { 1 } , u _ { 2 } , . . . , u _ { p } )$ 是正交矩阵，列是特征向量。

第i 主成分： $Y _ { i } = u _ { i } ^ { \prime } X$ ，方差为 $\lambda _ { i }$ 。

关键结论

• 主成分是协方差矩阵特征向量对应的线性组合

• 主成分的方差等于对应的特征值

• 主成分之间互不相关（特征向量正交）

主成分分析：方差贡献率与选取原则

## 主成分分析：方差贡献率与选取原则

## 方差贡献率

第 k 个主成分的方差贡献率 $= \lambda _ { k } / \sum _ { i = 1  p } \lambda _ { i }$

前 m 个主成分的累计贡献率 $= \sum _ { i = 1  m } \lambda _ { i } / \sum _ { i = 1  p } \lambda _ { i }$

累计贡献率表示前m 个主成分总共保留了多少原始信息

## 主成分分析：方差贡献率与选取原则

## 方差贡献率

第 k 个主成分的方差贡献率 $= \lambda _ { k } / \sum _ { i = 1  p } \lambda _ { i }$

前 m 个主成分的累计贡献率= $\sum _ { i = 1 \to m } \lambda _ { i } { \Big / } \sum _ { i = 1 \to p } \lambda _ { i }$

累计贡献率表示前m 个主成分总共保留了多少原始信息

## 主成分个数的选取原则

• 累计贡献率法：达到70% ˜ 85% 以上即可

• 特征值大于 1 法（Kaiser 准则）：保留特征值 > 1 的主成分

• 碎石图 (Scree Plot)：看特征值下降的” 肘部”

• 根据实际意义：选取的主成分要有可解释的含义

## 主成分分析：方差贡献率与选取原则

## 方差贡献率

第 k 个主成分的方差贡献率 $= \lambda _ { k } / \sum _ { i = 1  p } \lambda _ { i }$

前 m 个主成分的累计贡献率 $= \sum _ { i = 1  m } \lambda _ { i } / \sum _ { i = 1  p } \lambda _ { i }$

累计贡献率表示前m 个主成分总共保留了多少原始信息

## 主成分个数的选取原则

• 累计贡献率法：达到70% ˜ 85% 以上即可

• 特征值大于 1 法（Kaiser 准则）：保留特征值 > 1 的主成分

• 碎石图 (Scree Plot)：看特征值下降的” 肘部”

• 根据实际意义：选取的主成分要有可解释的含义

## 注意事项

• 变量量纲差异大时，应先标准化再做 PCA（用相关矩阵代替协方差矩阵）

• PCA 是无监督方法，不考虑因变量，只看自变量自身的变异

因子分析：因子模型与因子载荷

## 因子分析：因子模型与因子载荷

因子分析模型

$\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是可观测的随机向量

$F = ( F _ { 1 } , . . . , F _ { m } ) ^ { \prime }$ 是不可观测的公共因子 $( m < p )$

$\boldsymbol \varepsilon = ( \varepsilon _ { 1 } , . . . , \varepsilon _ { p } ) ^ { \prime }$ 是特殊因子（每个变量独有）

## 因子分析：因子模型与因子载荷

因子分析模型

$\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是可观测的随机向量

$F = ( F _ { 1 } , . . . , F _ { m } ) ^ { \prime }$ 是不可观测的公共因子 $( m < p )$

$\boldsymbol \varepsilon = ( \varepsilon _ { 1 } , . . . , \varepsilon _ { p } ) ^ { \prime }$ 是特殊因子（每个变量独有）

模型： $X _ { i } = \mu _ { i } + a _ { i 1 } F _ { 1 } + a _ { i 2 } F _ { 2 } + . . . + a _ { i m } F _ { m } + \varepsilon _ { i }$

## 因子分析：因子模型与因子载荷

因子分析模型

$\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是可观测的随机向量

$F = ( F _ { 1 } , . . . , F _ { m } ) ^ { \prime }$ 是不可观测的公共因子 $( m < p )$

$\boldsymbol \varepsilon = ( \varepsilon _ { 1 } , . . . , \varepsilon _ { p } ) ^ { \prime }$ 是特殊因子（每个变量独有）

模型： $X _ { i } = \mu _ { i } + a _ { i 1 } F _ { 1 } + a _ { i 2 } F _ { 2 } + . . . + a _ { i m } F _ { m } + \varepsilon _ { i }$

因子载荷矩阵 $A = \left( a _ { i j } \right)$

## 因子分析：因子模型与因子载荷

## 因子分析模型

$\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是可观测的随机向量

$F = ( F _ { 1 } , . . . , F _ { m } ) ^ { \prime }$ 是不可观测的公共因子 $( m < p )$

$\boldsymbol \varepsilon = ( \varepsilon _ { 1 } , . . . , \varepsilon _ { p } ) ^ { \prime }$ 是特殊因子（每个变量独有）

模型： $X _ { i } = \mu _ { i } + a _ { i 1 } F _ { 1 } + a _ { i 2 } F _ { 2 } + . . . + a _ { i m } F _ { m } + \varepsilon _ { i }$

因子载荷矩阵 $A = \left( a _ { i j } \right)$

矩阵形式： $X - \mu = A F + \varepsilon$

$a _ { i j }$ ：第 i 个变量在第j 个因子上的载荷（权重）。

$a _ { i j }$ 的意义： $X _ { i }$ 与 $F _ { j }$ 的相关系数。

绝对值越大，表示 $X _ { i }$ 与 $F _ { j }$ 的关系越密切。

## 因子分析：因子模型与因子载荷

因子分析模型

$\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是可观测的随机向量

$F = ( F _ { 1 } , . . . , F _ { m } ) ^ { \prime }$ 是不可观测的公共因子 $( m < p )$

$\boldsymbol \varepsilon = ( \varepsilon _ { 1 } , . . . , \varepsilon _ { p } ) ^ { \prime }$ 是特殊因子（每个变量独有）

模型： $X _ { i } = \mu _ { i } + a _ { i 1 } F _ { 1 } + a _ { i 2 } F _ { 2 } + . . . + a _ { i m } F _ { m } + \varepsilon _ { i }$

因子载荷矩阵 $A = \left( a _ { i j } \right)$

矩阵形式： $X - \mu = A F + \varepsilon$

$a _ { i j } :$ ：第 i 个变量在第j 个因子上的载荷（权重）。

$a _ { i j }$ 的意义： $X _ { i }$ 与 $F _ { j }$ 的相关系数。

绝对值越大，表示 $X _ { i }$ 与 $F _ { j }$ 的关系越密切。

公因子方差（共性方差） $h _ { i } ^ { 2 } = \sum _ { j = 1  m } a _ { i j } ^ { 2 }$

表示 $X _ { i }$ 的方差中能被m 个公共因子解释的比例。

特殊方差： $\psi _ { i } = V a r ( \varepsilon _ { i } ) = V a r ( X _ { i } ) - h _ { i } ^ { 2 }$

因子分析：因子旋转与因子得分

## 因子分析：因子旋转与因子得分

为什么要旋转？

初始因子载荷矩阵往往难以解释，旋转后使每个变量在少数因子上有高载荷。

## 因子分析：因子旋转与因子得分

## 为什么要旋转？

初始因子载荷矩阵往往难以解释，旋转后使每个变量在少数因子上有高载荷。

## 旋转方法

• 正交旋转（如 varimax）：因子仍保持不相关，载荷两极分化

• 斜交旋转：允许因子相关，拟合更好但解释更复杂

• 方差最大正交旋转 (Varimax)：最常用，使每个因子上高载荷变量越少越好

## 因子分析：因子旋转与因子得分

## 为什么要旋转？

初始因子载荷矩阵往往难以解释，旋转后使每个变量在少数因子上有高载荷。

## 旋转方法

• 正交旋转（如 varimax）：因子仍保持不相关，载荷两极分化

• 斜交旋转：允许因子相关，拟合更好但解释更复杂

• 方差最大正交旋转 (Varimax)：最常用，使每个因子上高载荷变量越少越好

## 因子得分

因子得分：每个样品在公共因子上的得分值。

即反过来用原始变量估计因子值： $\hat { F } _ { j } = \Sigma ( b _ { j i } X _ { i } )$

## 因子分析：因子旋转与因子得分

## 为什么要旋转？

初始因子载荷矩阵往往难以解释，旋转后使每个变量在少数因子上有高载荷。

## 旋转方法

• 正交旋转（如 varimax）：因子仍保持不相关，载荷两极分化

• 斜交旋转：允许因子相关，拟合更好但解释更复杂

• 方差最大正交旋转 (Varimax)：最常用，使每个因子上高载荷变量越少越好

## 因子得分

因子得分：每个样品在公共因子上的得分值。

即反过来用原始变量估计因子值： $\hat { F } _ { j } = \Sigma ( b _ { j i } X _ { i } )$

估计方法：

• 回归法（Thomson 法）

• Bartlett 法

## 因子分析：因子旋转与因子得分

为什么要旋转？

初始因子载荷矩阵往往难以解释，旋转后使每个变量在少数因子上有高载荷。

## 旋转方法

• 正交旋转（如 varimax）：因子仍保持不相关，载荷两极分化

• 斜交旋转：允许因子相关，拟合更好但解释更复杂

• 方差最大正交旋转 (Varimax)：最常用，使每个因子上高载荷变量越少越好

## 因子得分

因子得分：每个样品在公共因子上的得分值。

即反过来用原始变量估计因子值： $\hat { F } _ { j } = \Sigma ( b _ { j i } X _ { i } )$

估计方法：

• 回归法（Thomson 法）

• Bartlett 法

用途：将因子得分作为新变量，用于后续的回归、聚类等分析。

## PCA vs 因子分析对比

## PCA vs 因子分析对比

<table><tr><td>对比维度</td><td>主成分分析 (PCA)</td><td>因子分析 (FA)</td></tr><tr><td>本质</td><td>变量的线性组合(变换)</td><td>潜变量模型</td></tr><tr><td>目标</td><td>方差最大、降维</td><td>寻找公共因子、解释变量结构</td></tr><tr><td>模型假设</td><td>无(纯数学变换)</td><td>有(公共因子+特殊因子模型)</td></tr><tr><td>因子/成分</td><td>主成分是精确的线性组合</td><td>因子是不可观测的潜变量</td></tr><tr><td>个数确定</td><td>累计贡献率、碎石图</td><td>特征值、似然比检验</td></tr><tr><td>可旋转性</td><td>一般不旋转(旋转后还是同样的成分)</td><td>常用旋转(便于解释)</td></tr><tr><td>变量标准化</td><td>量纲不同时必须标准化</td><td>通常基于相关矩阵</td></tr><tr><td>应用</td><td>数据压缩、可视化</td><td>结构探索、量表构建</td></tr></table>

## PCA vs 因子分析对比

<table><tr><td>对比维度</td><td>主成分分析 (PCA)</td><td>因子分析 (FA)</td></tr><tr><td>本质</td><td>变量的线性组合(变换)</td><td>潜变量模型</td></tr><tr><td>目标</td><td>方差最大、降维</td><td>寻找公共因子、解释变量结构</td></tr><tr><td>模型假设</td><td>无(纯数学变换)</td><td>有(公共因子+特殊因子模型)</td></tr><tr><td>因子/成分</td><td>主成分是精确的线性组合</td><td>因子是不可观测的潜变量</td></tr><tr><td>个数确定</td><td>累计贡献率、碎石图</td><td>特征值、似然比检验</td></tr><tr><td>可旋转性</td><td>一般不旋转(旋转后还是同样的成分)</td><td>常用旋转(便于解释)</td></tr><tr><td>变量标准化</td><td>量纲不同时必须标准化</td><td>通常基于相关矩阵</td></tr><tr><td>应用</td><td>数据压缩、可视化</td><td>结构探索、量表构建</td></tr></table>

## 一句话区别

• PCA是”把变量重新组合”，FA 是”找出变量背后的原因”

## 判别分析

## 判别分析

什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

## 判别分析

## 什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

基本思想（投影）：将高维数据投影到低维（通常一维），使组间差异最大、组内差异最小。

Fisher 判别（线性判别）

## 判别分析

什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

基本思想（投影）：将高维数据投影到低维（通常一维），使组间差异最大、组内差异最小。

Fisher 判别（线性判别）

Fisher 准则：最大化

λ = (组间平方和) / (组内平方和). 相当于找到一个方向，使得投影后各类尽可能分开。得到判别函数后，设定一个分界点来判别归属。

## 判别分析

什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

基本思想（投影）：将高维数据投影到低维（通常一维），使组间差异最大、组内差异最小。

## Fisher 判别（线性判别）

Fisher 准则：最大化

λ = (组间平方和) / (组内平方和). 相当于找到一个方向，使得投影后各类尽可能分开。得到判别函数后，设定一个分界点来判别归属。

Bayes 判别

基于贝叶斯公式，计算新样品属于各类的后验概率，将其判归后验概率最大的类。

## 判别分析

## 什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

基本思想（投影）：将高维数据投影到低维（通常一维），使组间差异最大、组内差异最小。

## Fisher 判别（线性判别）

Fisher 准则：最大化

λ = (组间平方和) / (组内平方和). 相当于找到一个方向，使得投影后各类尽可能分开。得到判别函数后，设定一个分界点来判别归属。

Bayes 判别

基于贝叶斯公式，计算新样品属于各类的后验概率，将其判归后验概率最大的类。

优点：考虑了先验概率和错判损失，更全面。

## 判别分析

什么是判别分析？

已知分类的情况下，建立判别函数，判断新样品属于哪一类。

基本思想（投影）：将高维数据投影到低维（通常一维），使组间差异最大、组内差异最小。

Fisher 判别（线性判别）

Fisher 准则：最大化

λ = (组间平方和) / (组内平方和). 相当于找到一个方向，使得投影后各类尽可能分开。得到判别函数后，设定一个分界点来判别归属。

Bayes 判别

基于贝叶斯公式，计算新样品属于各类的后验概率，将其判归后验概率最大的类。

优点：考虑了先验概率和错判损失，更全面。

Fisher 判别 vs Bayes 判别：

• 两类正态且协方差相等时，两者等价

• Fisher不要求正态分布，更稳健；Bayes需要分布假设

Fisher 判别（线性判别） Fisher 准则

## Fisher 判别（线性判别） Fisher 准则

Fisher准则的数学表达

寻找投影方向 a，使得投影后组间平方和与组内平方和之比最大：

$$
\lambda (\mathbf {a}) = \frac {\mathbf {a} ^ {\prime} B \mathbf {a}}{\mathbf {a} ^ {\prime} W \mathbf {a}}
$$

其中：

• B：组间离差阵（Between-group scatter matrix）

• W：组内离差阵（Within-group scatter matrix）

## Fisher 判别（线性判别） Fisher 准则

Fisher准则的数学表达

寻找投影方向 a，使得投影后组间平方和与组内平方和之比最大：

$$
\lambda (\mathbf {a}) = \frac {\mathbf {a} ^ {\prime} B \mathbf {a}}{\mathbf {a} ^ {\prime} W \mathbf {a}}
$$

其中：

• B：组间离差阵（Between-group scatter matrix）

$W$ ：组内离差阵（Within-group scatter matrix）

两类情形的直观理解：

• 设两组样本： $\begin{array} { l l } { { G _ { 1 } } } & { { ( n _ { 1 } } } \end{array}$ 个）、 $\mathrm { ~ \textit ~ { ~ G ~ } ~ } ( n _ { 2 }$ 个），均值分别为 $\bar { \mathbf { x } } _ { 1 } , \bar { \mathbf { x } } _ { 2 }$

• 投影后均值差： $\bar { y } _ { 1 } - \bar { y } _ { 2 } = { \pmb a } ^ { \prime } ( \bar { { \pmb x } } _ { 1 } - \bar { { \pmb x } } _ { 2 } )$

• 投影后组内方差： $s _ { i } ^ { 2 } = \mathbf { a } ^ { \prime } S _ { i } \mathbf { a }$ ，其中 $\mathbf { } _ { S _ { i } }$ 为组内协方差阵

• Fisher准则等价于最大化： $\frac { ( \bar { y } _ { 1 } - \bar { y } _ { 2 } ) ^ { 2 } } { s _ { 1 } ^ { 2 } + s _ { 2 } ^ { 2 } }$

## 两类 Fisher 判别函数的推导

## 两类 Fisher 判别函数的推导

推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

## 两类 Fisher 判别函数的推导

## 推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$ 由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = 0
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

## 两类 Fisher 判别函数的推导

推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = \mathbf {0}
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

化简得： $W a \propto d$ ，即：

$$
\boldsymbol {a} = c \boldsymbol {W} ^ {- 1} (\bar {\boldsymbol {x}} _ {1} - \bar {\boldsymbol {x}} _ {2})
$$

## 两类 Fisher 判别函数的推导

## 推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = \mathbf {0}
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

化简得： $W a \propto d$ ，即：

$$
\mathbf {a} = c \mathbf {W} ^ {- 1} (\bar {\mathbf {x}} _ {1} - \bar {\mathbf {x}} _ {2})
$$

常数 c 不影响判别，取 c = 1 得Fisher判别系数。

## 两类 Fisher 判别函数的推导

## 推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = \mathbf {0}
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

化简得： $W a \propto d$ ，即：

$$
\mathbf {a} = c \mathbf {W} ^ {- 1} (\bar {\mathbf {x}} _ {1} - \bar {\mathbf {x}} _ {2})
$$

常数 c 不影响判别，取 c = 1 得Fisher判别系数。

结论：

## 两类 Fisher 判别函数的推导

推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = \mathbf {0}
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

化简得： $W a \propto d$ ，即：

$$
\boldsymbol {a} = c \boldsymbol {W} ^ {- 1} (\bar {\boldsymbol {x}} _ {1} - \bar {\boldsymbol {x}} _ {2})
$$

常数 c 不影响判别，取 c = 1 得Fisher判别系数。

结论：

最优投影方向为 $\pmb { a } = \pmb { W } ^ { - 1 } \big ( \bar { \pmb { x } } _ { 1 } - \bar { \pmb { x } } _ { 2 } \big )$

## 两类 Fisher 判别函数的推导

推导过程

目标：最大化 $\lambda ( { \bf a } ) = \frac { [ { \bf a ^ { \prime } } ( \bar { \bf x } _ { 1 } - \bar { \bf x } _ { 2 } ) ] ^ { 2 } } { { \bf a ^ { \prime } } W { \bf a } }$

由极值条件，对 a 求导并令其为零：

$$
\frac {\partial \lambda}{\partial \mathbf {a}} = \frac {2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} - 2 \mathbf {a} ^ {\prime} \mathbf {d} \cdot \mathbf {a} ^ {\prime} \mathbf {W a} \cdot \mathbf {W a}}{(\mathbf {a} ^ {\prime} \mathbf {W a}) ^ {2}} = 0
$$

其中 $d = \bar { \mathbf { x } } _ { 1 } - \bar { \mathbf { x } } _ { 2 }$ 。

化简得： $W a \propto d$ ，即：

$$
\boldsymbol {a} = c \boldsymbol {W} ^ {- 1} (\bar {\boldsymbol {x}} _ {1} - \bar {\boldsymbol {x}} _ {2})
$$

常数 c 不影响判别，取 c = 1 得Fisher判别系数。

结论：

最优投影方向为 $\pmb { a } = \pmb { W } ^ { - 1 } \big ( \bar { \pmb { x } } _ { 1 } - \bar { \pmb { x } } _ { 2 } \big )$

判别函数为： $y = { \pmb a } ^ { \prime } { \pmb x } = ( { \bar { \pmb x } } _ { 1 } - { \bar { \pmb x } } _ { 2 } ) ^ { \prime } { \pmb W } ^ { - 1 } { \pmb x }$

## 6判别规则与分界点确定

## 6判别规则与分界点确定

两类 Fisher 判别规则

设判别函数为 $y ( x ) = a ^ { \prime } x$ ，两组均值投影为 ${ \bar { y } } _ { 1 } , { \bar { y } } _ { 2 }$ 。

分界点（阈值）取两组均值的加权平均：

$$
y _ {0} = \frac {n _ {1} \bar {y} _ {1} + n _ {2} \bar {y} _ {2}}{n _ {1} + n _ {2}}
$$

若两组样本量相等，则 $y _ { 0 } = \frac { \bar { y } _ { 1 } + \bar { y } _ { 2 } } { 2 }$ 。

## 6判别规则与分界点确定

两类 Fisher 判别规则

设判别函数为 $y ( x ) = a ^ { \prime } x$ ，两组均值投影为 ${ \bar { y } } _ { 1 } , { \bar { y } } _ { 2 }$ 。

分界点（阈值）取两组均值的加权平均：

若两组样本量相等，则 $y _ { 0 } = \frac { \bar { y } _ { 1 } + \bar { y } _ { 2 } } { 2 }$ 判别规则（不妨设 $\bar { y } _ { 1 } > \bar { y } _ { 2 } )$ ：

$$
y _ {0} = \frac {n _ {1} \bar {y} _ {1} + n _ {2} \bar {y} _ {2}}{n _ {1} + n _ {2}}
$$

$$
\mathbf {x} \in \left\{ \begin{array}{l l} G _ {1}, & \text {若} y (\mathbf {x}) > y _ {0} \\ G _ {2}, & \text {若} y (\mathbf {x}) <   y _ {0} \\ \text {待判}, & \text {若} y (\mathbf {x}) = y _ {0} \end{array} \right.
$$

## 6判别规则与分界点确定

两类 Fisher 判别规则

设判别函数为 $y ( x ) = a ^ { \prime } x$ ，两组均值投影为 ${ \bar { y } } _ { 1 } , { \bar { y } } _ { 2 }$ 。

分界点（阈值）取两组均值的加权平均：

$$
y _ {0} = \frac {n _ {1} \bar {y} _ {1} + n _ {2} \bar {y} _ {2}}{n _ {1} + n _ {2}}
$$

若两组样本量相等，则 $y _ { 0 } = \frac { \bar { y } _ { 1 } + \bar { y } _ { 2 } } { 2 }$ 。

判别规则（不妨设 $\bar { y } _ { 1 } > \bar { y } _ { 2 } )$ ）：

$$
\mathbf {x} \in \left\{ \begin{array}{l l} G _ {1}, & \text {若} y (\mathbf {x}) > y _ {0} \\ G _ {2}, & \text {若} y (\mathbf {x}) <   y _ {0} \\ \text {待判}, & \text {若} y (\mathbf {x}) = y _ {0} \end{array} \right.
$$

多类 Fisher 判别（LDA）

k 类问题，找 k −1 个判别函数，使得组间/组内比最大。

等价于求解广义特征值问题： $B a = \lambda W a$

取前 k −1 个最大特征值对应的特征向量作为判别轴。

## Fisher 判别实例 男女身高体重判别

## Fisher 判别实例— 男女身高体重判别

问题：用身高(X )和体重 (X )判别性别。训练数据：

## Fisher 判别实例 男女身高体重判别

问题：

用身高 $( X _ { 1 } )$ 和体重 $( X _ { 2 } )$ 判别性别。训练数据：

<table><tr><td colspan="3">男性组( $G_1$ , $n_1 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>175</td><td>70</td></tr><tr><td>2</td><td>180</td><td>75</td></tr><tr><td>3</td><td>170</td><td>65</td></tr><tr><td>4</td><td>178</td><td>72</td></tr><tr><td>5</td><td>172</td><td>68</td></tr><tr><td colspan="3"> $\bar{x}_1 = (175,70)'$ </td></tr></table>

<table><tr><td colspan="3">女性组( $G_2$ ,  $n_2 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>160</td><td>50</td></tr><tr><td>2</td><td>165</td><td>55</td></tr><tr><td>3</td><td>158</td><td>48</td></tr><tr><td>4</td><td>162</td><td>52</td></tr><tr><td>5</td><td>168</td><td>58</td></tr><tr><td colspan="3"> $\bar{x}_2 = (162.6, 52.6)'$ </td></tr></table>

## Fisher 判别实例 男女身高体重判别

问题：

用身高 $( X _ { 1 } )$ 和体重 $( X _ { 2 } )$ 判别性别。训练数据：

<table><tr><td colspan="3">男性组( $G_1$ , $n_1 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>175</td><td>70</td></tr><tr><td>2</td><td>180</td><td>75</td></tr><tr><td>3</td><td>170</td><td>65</td></tr><tr><td>4</td><td>178</td><td>72</td></tr><tr><td>5</td><td>172</td><td>68</td></tr><tr><td colspan="3"> $\bar{x}_1 = (175, 70)'$ </td></tr></table>

计算过程：

• 均值差： $d = { \bar { x } } _ { 1 } - { \bar { x } } _ { 2 } = ( 1 2 . 4 , 1 7 . 4 ) ^ { \prime }$

• 组内离差阵： $\pmb { W } = \pmb { W } _ { 1 } + \pmb { W } _ { 2 }$

• 判别系数： $\ b { a } = \ b { W } ^ { - 1 } \ b { d }$

<table><tr><td colspan="3">女性组( $G_2$ ,  $n_2 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>160</td><td>50</td></tr><tr><td>2</td><td>165</td><td>55</td></tr><tr><td>3</td><td>158</td><td>48</td></tr><tr><td>4</td><td>162</td><td>52</td></tr><tr><td>5</td><td>168</td><td>58</td></tr><tr><td colspan="3"> $\bar{x}_2 = (162.6, 52.6)'$ </td></tr></table>

## Fisher 判别实例 男女身高体重判别

问题：

用身高 $( X _ { 1 } )$ 和体重 $( X _ { 2 } )$ 判别性别。训练数据：

<table><tr><td colspan="3">男性组( $G_1$ , $n_1 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>175</td><td>70</td></tr><tr><td>2</td><td>180</td><td>75</td></tr><tr><td>3</td><td>170</td><td>65</td></tr><tr><td>4</td><td>178</td><td>72</td></tr><tr><td>5</td><td>172</td><td>68</td></tr><tr><td colspan="3"> $\bar{x}_1 = (175, 70)'$ </td></tr></table>

计算过程：

• 均值差： $d = { \bar { x } } _ { 1 } - { \bar { x } } _ { 2 } = ( 1 2 . 4 , 1 7 . 4 ) ^ { \prime }$

• 组内离差阵： $\pmb { W } = \pmb { W } _ { 1 } + \pmb { W } _ { 2 }$

• 判别系数： $\ b { a } = \ b { W } ^ { - 1 } \ b { d }$

假设计算得 $\pmb { a } = ( 0 . 0 3 2 , 0 . 0 8 5 ) ^ { \prime }$ ，则判别函数： $y = 0 . 0 3 2 x _ { 1 } + 0 . 0 8 5 x _ { 2 }$

<table><tr><td colspan="3">女性组( $G_2$ ,  $n_2 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>160</td><td>50</td></tr><tr><td>2</td><td>165</td><td>55</td></tr><tr><td>3</td><td>158</td><td>48</td></tr><tr><td>4</td><td>162</td><td>52</td></tr><tr><td>5</td><td>168</td><td>58</td></tr><tr><td colspan="3"> $\bar{x}_2 = (162.6, 52.6)'$ </td></tr></table>

## Fisher 判别实例 男女身高体重判别

问题：

用身高 $( X _ { 1 } )$ 和体重 $( X _ { 2 } )$ 判别性别。训练数据：

<table><tr><td colspan="3">男性组( $G_1$ , $n_1 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>175</td><td>70</td></tr><tr><td>2</td><td>180</td><td>75</td></tr><tr><td>3</td><td>170</td><td>65</td></tr><tr><td>4</td><td>178</td><td>72</td></tr><tr><td>5</td><td>172</td><td>68</td></tr><tr><td colspan="3"> $\bar{x}_1 = (175, 70)'$ </td></tr></table>

计算过程：

• 均值差： $d = { \bar { x } } _ { 1 } - { \bar { x } } _ { 2 } = ( 1 2 . 4 , 1 7 . 4 ) ^ { \prime }$

• 组内离差阵： $\pmb { W } = \pmb { W } _ { 1 } + \pmb { W } _ { 2 }$

• 判别系数： $\ b { a } = \ b { W } ^ { - 1 } \ b { d }$

<table><tr><td colspan="3">女性组( $G_2$ ,  $n_2 = 5$ )</td></tr><tr><td>编号</td><td>身高(cm)</td><td>体重(kg)</td></tr><tr><td>1</td><td>160</td><td>50</td></tr><tr><td>2</td><td>165</td><td>55</td></tr><tr><td>3</td><td>158</td><td>48</td></tr><tr><td>4</td><td>162</td><td>52</td></tr><tr><td>5</td><td>168</td><td>58</td></tr><tr><td colspan="3"> $\bar{x}_2 = (162.6, 52.6)'$ </td></tr></table>

假设计算得 $\pmb { a } = ( 0 . 0 3 2 , 0 . 0 8 5 ) ^ { \prime }$ ，则判别函数： $y = 0 . 0 3 2 x _ { 1 } + 0 . 0 8 5 x _ { 2 }$

对新样本 (170, 62)： $y = 0 . 0 3 2 \times 1 7 0 + 0 . 0 8 5 \times 6 2 = 1 0 . 7 1$ ，与阈值比较后判别。

## Bayes 判别 基本思想

## Bayes 判别 基本思想

## Bayes 判别准则

设有 k 个总体 $G _ { 1 } , G _ { 2 } , \ldots , G _ { k }$ ，各总体的先验概率为 $q _ { 1 } , q _ { 2 } , \ldots , q _ { k }$ ，概率密度为$f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { k } ( \mathbf { x } )$ 。

## Bayes 判别 基本思想

## Bayes 判别准则

设有 k 个总体 $G _ { 1 } , G _ { 2 } , \ldots , G _ { k }$ ，各总体的先验概率为 $q _ { 1 } , q _ { 2 } , \ldots , q _ { k }$ ，概率密度为$f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { k } ( \mathbf { x } )$ 。

对新样本 x，计算其属于第 i 类的后验概率：

$$
P (G _ {i} | \mathbf {x}) = \frac {q _ {i} f _ {i} (\mathbf {x})}{\sum_ {j = 1} ^ {k} q _ {j} f _ {j} (\mathbf {x})}
$$

## Bayes 判别 基本思想

## Bayes 判别准则

设有 k 个总体 $G _ { 1 } , G _ { 2 } , \ldots , G _ { k }$ 各总体的先验概率为 $q _ { 1 } , q _ { 2 } , \ldots , q _ { k }$ ，概率密度为$f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { k } ( \mathbf { x } )$ 0

对新样本 x，计算其属于第 i 类的后验概率：

$$
P (G _ {i} | \mathbf {x}) = \frac {q _ {i} f _ {i} (\mathbf {x})}{\sum_ {j = 1} ^ {k} q _ {j} f _ {j} (\mathbf {x})}
$$

判别规则：将 x 判归后验概率最大的类，即

$$
\mathbf {x} \in G _ {l} \quad {\text {若}} \quad P (G _ {l} | \mathbf {x}) = \max _ {1 \leq i \leq k} P (G _ {i} | \mathbf {x})
$$

## Bayes 判别 基本思想

## Bayes 判别准则

设有 k 个总体 $G _ { 1 } , G _ { 2 } , \ldots , G _ { k }$ 各总体的先验概率为 $q _ { 1 } , q _ { 2 } , \ldots , q _ { k }$ ，概率密度为$f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { k } ( \mathbf { x } )$ 。

对新样本 x，计算其属于第 i 类的后验概率：

$$
P (G _ {i} | \mathbf {x}) = \frac {q _ {i} f _ {i} (\mathbf {x})}{\sum_ {j = 1} ^ {k} q _ {j} f _ {j} (\mathbf {x})}
$$

判别规则：将 x 判归后验概率最大的类，即

$$
\mathbf {x} \in G _ {l} \quad {\text {若}} \quad P (G _ {l} | \mathbf {x}) = \max _ {1 \leq i \leq k} P (G _ {i} | \mathbf {x})
$$

等价表述：

最小化期望错判损失（当先验概率均匀、错判损失相等时，等价于最小化错判概率）

## Bayes 判别 基本思想

Bayes 判别准则

设有 k 个总体 $G _ { 1 } , G _ { 2 } , \ldots , G _ { k }$ 各总体的先验概率为 $q _ { 1 } , q _ { 2 } , \ldots , q _ { k }$ ，概率密度为$f _ { 1 } ( \mathbf { x } ) , f _ { 2 } ( \mathbf { x } ) , \ldots , f _ { k } ( \mathbf { x } )$ 0

对新样本 x，计算其属于第 i 类的后验概率：

$$
P (G _ {i} | \mathbf {x}) = \frac {q _ {i} f _ {i} (\mathbf {x})}{\sum_ {j = 1} ^ {k} q _ {j} f _ {j} (\mathbf {x})}
$$

判别规则：将 x 判归后验概率最大的类，即

$$
\mathbf {x} \in G _ {l} \quad {\text {若}} \quad P (G _ {l} | \mathbf {x}) = \max _ {1 \leq i \leq k} P (G _ {i} | \mathbf {x})
$$

等价表述：

最小化期望错判损失（当先验概率均匀、错判损失相等时，等价于最小化错判概率）

错判损失的考虑

设 $C ( j | i )$ 为将 $G _ { i }$ 错判为 $G _ { j }$ 的损失，则期望损失最小化准则：

$$
\mathbf {x} \in G _ {l} \quad \text {若} \quad \sum_ {i = 1} ^ {k} q _ {i} f _ {i} (\mathbf {x}) C (l | i) = \min _ {j} \sum_ {i = 1} ^ {k} q _ {i} f _ {i} (\mathbf {x}) C (j | i)
$$

## 正态总体下的 Bayes判别函数

## 正态总体下的 Bayes判别函数

多元正态总体的Bayes 判别

设 $G _ { i } \sim N _ { p } ( \pmb { \mu } _ { i } , \pmb { \Sigma } _ { i } ) , i = 1 , 2 , . . . , k$ 。

取对数后验概率（忽略公共项），得到判别函数：

$$
y _ {i} (\mathbf {x}) = \ln q _ {i} - \frac {1}{2} \ln | \boldsymbol {\Sigma} _ {i} | - \frac {1}{2} (\mathbf {x} - \boldsymbol {\mu} _ {i}) ^ {\prime} \boldsymbol {\Sigma} _ {i} ^ {- 1} (\mathbf {x} - \boldsymbol {\mu} _ {i})
$$

判别规则： $\mathbf { \boldsymbol { x } } \in G _ { l }$ 若 $y _ { l } ( \mathbf { x } ) = \operatorname* { m a x } _ { i } y _ { i } ( \mathbf { x } )$

## 正态总体下的 Bayes判别函数

多元正态总体的Bayes 判别

设 $G _ { i } \sim N _ { p } ( \pmb { \mu } _ { i } , \pmb { \Sigma } _ { i } ) , i = 1 , 2 , . . . , k$ 。

取对数后验概率（忽略公共项），得到判别函数：

$$
y _ {i} (\mathbf {x}) = \ln q _ {i} - \frac {1}{2} \ln | \pmb {\Sigma} _ {i} | - \frac {1}{2} (\mathbf {x} - \pmb {\mu} _ {i}) ^ {\prime} \pmb {\Sigma} _ {i} ^ {- 1} (\mathbf {x} - \pmb {\mu} _ {i})
$$

判别规则： $\mathbf { \boldsymbol { x } } \in G _ { l }$ 若 $y _ { l } ( \mathbf { x } ) = \operatorname* { m a x } _ { i } y _ { i } ( \mathbf { x } )$

协方差阵相等的情形 $\left( \Sigma _ { 1 } = \cdot \cdot \cdot = \Sigma _ { k } = \Sigma \right)$

此时二次项抵消，判别函数简化为线性函数：

$$
y _ {i} (\mathbf {x}) = \ln q _ {i} + \pmb {\mu} _ {i} ^ {\prime} \pmb {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \pmb {\mu} _ {i} ^ {\prime} \pmb {\Sigma} ^ {- 1} \pmb {\mu} _ {i}
$$

## 正态总体下的 Bayes判别函数

多元正态总体的Bayes 判别

设 $G _ { i } \sim N _ { p } ( \pmb { \mu } _ { i } , \pmb { \Sigma } _ { i } ) , i = 1 , 2 , . . . , k$ 。

取对数后验概率（忽略公共项），得到判别函数：

$$
y _ {i} (\mathbf {x}) = \ln q _ {i} - \frac {1}{2} \ln | \pmb {\Sigma} _ {i} | - \frac {1}{2} (\mathbf {x} - \pmb {\mu} _ {i}) ^ {\prime} \pmb {\Sigma} _ {i} ^ {- 1} (\mathbf {x} - \pmb {\mu} _ {i})
$$

判别规则： $\mathbf { \boldsymbol { x } } \in G _ { l }$ 若 $y _ { l } ( \mathbf { x } ) = \operatorname* { m a x } _ { i } y _ { i } ( \mathbf { x } )$

协方差阵相等的情形 $\left( \Sigma _ { 1 } = \cdot \cdot \cdot = \Sigma _ { k } = \Sigma \right)$

此时二次项抵消，判别函数简化为线性函数：

$$
y _ {i} (\mathbf {x}) = \ln q _ {i} + \pmb {\mu} _ {i} ^ {\prime} \pmb {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \pmb {\mu} _ {i} ^ {\prime} \pmb {\Sigma} ^ {- 1} \pmb {\mu} _ {i}
$$

重要结论：

当先验概率相等 $\left( q _ { i } = 1 / k \right)$ 且协方差阵相等时，Bayes 判别与Fisher判别等价！

## Bayes 判别实例

## Bayes 判别实例

问题：

某公司根据两个指标 $X _ { 1 } , X _ { 2 }$ 判断产品是否合格。已知：

• 合格组 $G _ { 1 } \colon \mu _ { 1 } = ( 5 , 8 ) ^ { \prime } , \ \Sigma _ { 1 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 不合格组 $G _ { 2 } \colon \mu _ { 2 } = ( 2 , 3 ) ^ { \prime } , \ \Sigma _ { 2 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 先验概率： $q _ { 1 } = 0 . 7 , q _ { 2 } = 0 . 3$ （合格率约 70%）

• 协方差阵相等，使用线性判别函数

## Bayes 判别实例

问题：

某公司根据两个指标 $X _ { 1 } , X _ { 2 }$ 判断产品是否合格。已知：

• 合格组 $G _ { 1 } \colon \mu _ { 1 } = ( 5 , 8 ) ^ { \prime } , \ \Sigma _ { 1 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 不合格组 $G _ { 2 } \colon \mu _ { 2 } = ( 2 , 3 ) ^ { \prime } , \ \Sigma _ { 2 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 先验概率： $q _ { 1 } = 0 . 7 , q _ { 2 } = 0 . 3$ （合格率约 70%）

• 协方差阵相等，使用线性判别函数

计算：

$$
\boldsymbol {\Sigma} ^ {- 1} = \frac {4}{3} \left( \begin{array}{c c} 1 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right)
$$

$$
y _ {1} (\mathbf {x}) = \ln 0. 7 + \pmb {\mu} _ {1} ^ {\prime} \pmb {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \pmb {\mu} _ {1} ^ {\prime} \pmb {\Sigma} ^ {- 1} \pmb {\mu} _ {1}, y _ {2} (\mathbf {x}) = \ln 0. 3 + \pmb {\mu} _ {2} ^ {\prime} \pmb {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \pmb {\mu} _ {2} ^ {\prime} \pmb {\Sigma} ^ {- 1} \pmb {\mu} _ {2}
$$

## Bayes 判别实例

问题：

某公司根据两个指标 $X _ { 1 } , X _ { 2 }$ 判断产品是否合格。已知：

• 合格组 $G _ { 1 } \colon \mu _ { 1 } = ( 5 , 8 ) ^ { \prime } , \ \Sigma _ { 1 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 不合格组 $G _ { 2 } \colon \mu _ { 2 } = ( 2 , 3 ) ^ { \prime } , \ \Sigma _ { 2 } = \left( \begin{array} { c c } { { 1 } } & { { 0 . 5 } } \\ { { 0 . 5 } } & { { 1 } } \end{array} \right)$

• 先验概率： $q _ { 1 } = 0 . 7 , q _ { 2 } = 0 . 3$ （合格率约 70%）

• 协方差阵相等，使用线性判别函数

计算：

$$
\boldsymbol {\Sigma} ^ {- 1} = \frac {4}{3} \left( \begin{array}{c c} 1 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right)
$$

$$
y _ {1} (\mathbf {x}) = \ln 0. 7 + \boldsymbol {\mu} _ {1} ^ {\prime} \boldsymbol {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \boldsymbol {\mu} _ {1} ^ {\prime} \boldsymbol {\Sigma} ^ {- 1} \boldsymbol {\mu} _ {1}, y _ {2} (\mathbf {x}) = \ln 0. 3 + \boldsymbol {\mu} _ {2} ^ {\prime} \boldsymbol {\Sigma} ^ {- 1} \mathbf {x} - \frac {1}{2} \boldsymbol {\mu} _ {2} ^ {\prime} \boldsymbol {\Sigma} ^ {- 1} \boldsymbol {\mu} _ {2}
$$

对新样本 $\mathbf { x } = ( 4 , 6 ) ^ { \prime }$ ，计算得 $y _ { 1 } = - 2 . 7 8 , y _ { 2 } = - 5 . 4 7$

$\because y _ { 1 } > y _ { 2 } \quad . . .$ 判为合格组 $G _ { 1 }$

## 判别 vs Bayes 判别 总结对比

## 判别 vs Bayes 判别 总结对比

<table><tr><td>对比维度</td><td>Fisher 判别</td><td>Bayes 判别</td></tr><tr><td>基本思想</td><td>组间分离最大化</td><td>后验概率最大化</td></tr><tr><td>分布假设</td><td>无严格分布假设</td><td>需要知道总体分布(通常假设正态)</td></tr><tr><td>先验概率</td><td>不直接使用</td><td>显式考虑先验概率</td></tr><tr><td>错判损失</td><td>不直接考虑</td><td>可纳入错判损失</td></tr><tr><td>判别函数形式</td><td>线性判别函数</td><td>正态等方差时为线性,否则二次</td></tr><tr><td>多类问题</td><td>降维到 k-1 维空间</td><td>直接计算各类后验概率</td></tr><tr><td>适用场景</td><td>探索性分析、分布未知</td><td>有先验信息、需考虑损失</td></tr><tr><td>稳健性</td><td>对非正态更稳健</td><td>依赖分布假设</td></tr></table>

## 判别 vs Bayes 判别 总结对比

<table><tr><td>对比维度</td><td>Fisher 判别</td><td>Bayes 判别</td></tr><tr><td>基本思想</td><td>组间分离最大化</td><td>后验概率最大化</td></tr><tr><td>分布假设</td><td>无严格分布假设</td><td>需要知道总体分布(通常假设正态)</td></tr><tr><td>先验概率</td><td>不直接使用</td><td>显式考虑先验概率</td></tr><tr><td>错判损失</td><td>不直接考虑</td><td>可纳入错判损失</td></tr><tr><td>判别函数形式</td><td>线性判别函数</td><td>正态等方差时为线性,否则二次</td></tr><tr><td>多类问题</td><td>降维到 k-1 维空间</td><td>直接计算各类后验概率</td></tr><tr><td>适用场景</td><td>探索性分析、分布未知</td><td>有先验信息、需考虑损失</td></tr><tr><td>稳健性</td><td>对非正态更稳健</td><td>依赖分布假设</td></tr></table>

何时两者等价？

当满足以下全部条件时，Fisher 判别与 Bayes 判别完全等价：

## 判别 vs Bayes 判别 总结对比

<table><tr><td>对比维度</td><td>Fisher 判别</td><td>Bayes 判别</td></tr><tr><td>基本思想</td><td>组间分离最大化</td><td>后验概率最大化</td></tr><tr><td>分布假设</td><td>无严格分布假设</td><td>需要知道总体分布(通常假设正态)</td></tr><tr><td>先验概率</td><td>不直接使用</td><td>显式考虑先验概率</td></tr><tr><td>错判损失</td><td>不直接考虑</td><td>可纳入错判损失</td></tr><tr><td>判别函数形式</td><td>线性判别函数</td><td>正态等方差时为线性,否则二次</td></tr><tr><td>多类问题</td><td>降维到 k-1 维空间</td><td>直接计算各类后验概率</td></tr><tr><td>适用场景</td><td>探索性分析、分布未知</td><td>有先验信息、需考虑损失</td></tr><tr><td>稳健性</td><td>对非正态更稳健</td><td>依赖分布假设</td></tr></table>

## 何时两者等价？

当满足以下全部条件时，Fisher判别与Bayes 判别完全等价：

1 总体服从多元正态分布

2 各总体协方差阵相等

3 各类先验概率相等

4 错判损失相等

## 聚类分析

聚类分析

聚类 vs 判别

## 聚类分析

聚类 vs 判别

判别分析：类已知 → 给新样本分类（有监督）

## 聚类分析

聚类 vs 判别

判别分析：类已知 → 给新样本分类（有监督）

聚类分析：类未知→ 探索性地将样本分组（无监督）

## 聚类分析

聚类 vs 判别

判别分析：类已知 → 给新样本分类（有监督）

聚类分析：类未知→ 探索性地将样本分组（无监督）

系统聚类法（层次聚类）

## 聚类分析

聚类 vs 判别

判别分析：类已知 → 给新样本分类（有监督）

聚类分析：类未知→ 探索性地将样本分组（无监督）

系统聚类法（层次聚类）

基本步骤：

• 每个样本自成一类

• 计算各类之间的距离，将距离最近的两类合并

• 重新计算新类与其他类的距离

• 重复 2-3，直到所有样本归为一类

## 聚类分析

## 聚类 vs 判别

判别分析：类已知 → 给新样本分类（有监督）

聚类分析：类未知→ 探索性地将样本分组（无监督）

系统聚类法（层次聚类）

基本步骤：

• 每个样本自成一类

• 计算各类之间的距离，将距离最近的两类合并

• 重新计算新类与其他类的距离

• 重复 2-3，直到所有样本归为一类

类间距离定义不同，方法不同：

• 最短距离法（单链接）• 最长距离法（全链接）• 类平均法 • Ward 法

## 聚类分析 续

## 聚类分析 续

K 均值法（快速聚类）

## 聚类分析 续

K 均值法（快速聚类）基本步骤：

• 指定类别数 K，随机选K 个初始中心

• 将每个样本分配给最近的中心

• 重新计算各类的中心（均值）

• 重复 2-3，直到中心不再变化

## 聚类分析 续

K 均值法（快速聚类）基本步骤：

• 指定类别数 K，随机选K 个初始中心

• 将每个样本分配给最近的中心

• 重新计算各类的中心（均值）

• 重复 2-3，直到中心不再变化

优点：计算快，适合大样本；缺点：需要预先指定K，对初始值敏感。

## 层次聚类详解— 类间距离定义

## 层次聚类详解— 类间距离定义

## 四种常用类间距离

设两类 $G _ { p }$ （含 $n _ { p }$ 个样本）和 $G _ { q }$ （含 $n _ { q }$ 个样本），样本间距离为 $d _ { i j }$ 。

## 层次聚类详解— 类间距离定义

## 四种常用类间距离

设两类 $G _ { p }$ （含 $n _ { p }$ 个样本）和 $G _ { q }$ （含 $n _ { q }$ 个样本），样本间距离为 $d _ { i j }$ 。

1 最短距离法（单链接）： $D ( p , q ) = \operatorname* { m i n } _ { i \in G _ { p } , j \in G _ { q } } d _ { i j }$

2 最长距离法（全链接）： $D ( p , q ) = \operatorname* { m a x } _ { i \in G _ { p } , j \in G _ { q } } d _ { i j }$

3 类平均法： $\begin{array} { r } { D ( p , q ) = \frac { 1 } { n _ { p } n _ { q } } \sum _ { i \in G _ { p } } \sum _ { j \in G _ { q } } d _ { i j } } \end{array}$

4 Ward法（离差平方和法）： $D ( p , q ) = S _ { p q } - S _ { p } - S _ { q }$ ，其中 S 为类内离差平方和

## 层次聚类详解— 类间距离定义

## 四种常用类间距离

设两类 $G _ { p }$ （含 $n _ { p }$ 个样本）和 $G _ { q }$ （含 $n _ { q }$ 个样本），样本间距离为 $d _ { i j }$ 。

1 最短距离法（单链接）： $D ( p , q ) = \operatorname* { m i n } _ { i \in G _ { p } , j \in G _ { q } } d _ { i j }$

2 最长距离法（全链接）： $D ( p , q ) = \operatorname* { m a x } _ { i \in G _ { p } , j \in G _ { q } } d _ { i j }$

3 类平均法： $\begin{array} { r } { D ( p , q ) = \frac { 1 } { n _ { p } n _ { q } } \sum _ { i \in G _ { p } } \sum _ { j \in G _ { q } } d _ { i j } } \end{array}$

4 Ward法（离差平方和法）： $D ( p , q ) = S _ { p q } - S _ { p } - S _ { q }$ ，其中 S 为类内离差平方和

<table><tr><td>方法</td><td>特点</td><td>倾向</td><td>对异常值</td></tr><tr><td>最短距离</td><td>链状效应明显</td><td>长条形聚类</td><td>敏感</td></tr><tr><td>最长距离</td><td>紧凑类球形</td><td>类大小相近</td><td>不敏感</td></tr><tr><td>类平均</td><td>综合考虑所有点</td><td>适中</td><td>中等</td></tr><tr><td>Ward法</td><td>最小化类内方差</td><td>类内同质性</td><td>中等</td></tr></table>

## 层次聚类— 树状图与实例

## 层次聚类— 树状图与实例

实例：5 个样本的距离矩阵如下，进行系统聚类：

$$
\begin{array}{c c c c c c} & 1 & 2 & 3 & 4 & 5 \\ \hline 1 & 0 & & & & \\ 2 & 2 & 0 & & & \\ 3 & 6 & 5 & 0 & & \\ 4 & 7 & 6 & 1 & 0 & \\ 5 & 9 & 8 & 3 & 4 & 0 \end{array}
$$

## 层次聚类— 树状图与实例

实例：5 个样本的距离矩阵如下，进行系统聚类：

$$
\begin{array}{c c c c c c} & 1 & 2 & 3 & 4 & 5 \\ \hline 1 & 0 & & & & \\ 2 & 2 & 0 & & & \\ 3 & 6 & 5 & 0 & & \\ 4 & 7 & 6 & 1 & 0 & \\ 5 & 9 & 8 & 3 & 4 & 0 \end{array}
$$

最短距离法聚类过程：

1 最小距离 $D _ { 3 4 } = 1$ ，合并 G3 和 G4 为新类 G6

2 计算 G6 与其他类的最短距离： $D _ { 6 1 } = \operatorname* { m i n } ( 6 , 7 ) = 6 , D _ { 6 2 } = \operatorname* { m i n } ( 5 , 6 ) = 5 , D _ { 6 5 } = \operatorname* { m i n } ( 3 , 4 ) = 3$

3 最小距离 $D _ { 1 2 } = 2$ ，合并 G1 和 G2 为新类 G7

4 最小距离 $D _ { 6 5 } = 3$ ，合并 G6 和 G5 为新类 G8

5 最后合并 G7 和 G8，距离为 $\operatorname* { m i n } ( 6 , 5 ) = 5$

## 层次聚类— 树状图与实例

实例：5 个样本的距离矩阵如下，进行系统聚类：

$$
\begin{array}{c c c c c c} & 1 & 2 & 3 & 4 & 5 \\ \hline 1 & 0 & & & & \\ 2 & 2 & 0 & & & \\ 3 & 6 & 5 & 0 & & \\ 4 & 7 & 6 & 1 & 0 & \\ 5 & 9 & 8 & 3 & 4 & 0 \end{array}
$$

最短距离法聚类过程：

1 最小距离 $D _ { 3 4 } = 1$ ，合并 G3 和 G4 为新类 G6

2 计算 G6 与其他类的最短距离： $D _ { 6 1 } = \operatorname* { m i n } ( 6 , 7 ) = 6 , D _ { 6 2 } = \operatorname* { m i n } ( 5 , 6 ) = 5 , D _ { 6 5 } = \operatorname* { m i n } ( 3 , 4 ) = 3$

3 最小距离 $D _ { 1 2 } = 2$ ，合并 G1 和 G2 为新类 G7

4 最小距离 $D _ { 6 5 } = 3$ ，合并 G6 和 G5 为新类 G8

5 最后合并 G7 和 G8，距离为 $\operatorname* { m i n } ( 6 , 5 ) = 5$

树状图（系统聚类图）解读：

• 横坐标：样本编号；纵坐标：合并距离（高度）

• 水平线高度表示两类合并时的距离

• 切分位置决定聚类数目：切得越高，类越少；切得越低，类越多

## DBSCAN 密度聚类 基本概念

## DBSCAN 密度聚类 基本概念

## DBSCAN 核心思想

聚类是由”高密度区域”构成的，被低密度区域分隔开。无需指定聚类数目，可以发现任意形状的簇，能识别噪声点。

## DBSCAN 密度聚类 基本概念

DBSCAN 核心思想

聚类是由”高密度区域”构成的，被低密度区域分隔开。无需指定聚类数目，可以发现任意形状的簇，能识别噪声点。

核心概念（参数：ε 邻域半径，MinPts 最小点数）：

• ε 邻域：以某点为中心、ε 为半径的区域内的样本集合

• 核心点（Core Point）：ε 邻域内样本数 $\geq \mathrm { M i n P t s }$ 的点

• 边界点（Border Point）：不是核心点，但落在某个核心点的ε 邻域内

• 噪声点（Noise Point）：既不是核心点也不是边界点

## DBSCAN 密度聚类 基本概念

## DBSCAN 核心思想

聚类是由”高密度区域”构成的，被低密度区域分隔开。无需指定聚类数目，可以发现任意形状的簇，能识别噪声点。

## 核心概念（参数：ε 邻域半径，MinPts 最小点数）：

• ε 邻域：以某点为中心、ε 为半径的区域内的样本集合

• 核心点（Core Point）：ε 邻域内样本数 $\geq \mathrm { M i n P t s }$ 的点

• 边界点（Border Point）：不是核心点，但落在某个核心点的ε 邻域内

• 噪声点（Noise Point）：既不是核心点也不是边界点

## 密度可达与密度相连

• 直接密度可达：若 p 是核心点且 q 在 p 的 ε 邻域内，则 q 从 p 直接密度可达

• 密度可达：存在点链 $p _ { 1 } \to p _ { 2 } \to \cdots \to p _ { n }$ ，每步直接密度可达

• 密度相连：存在核心点 o，使得 p 和 q 都从 o 密度可达

## DBSCAN 密度聚类 基本概念

DBSCAN 核心思想

聚类是由”高密度区域”构成的，被低密度区域分隔开。无需指定聚类数目，可以发现任意形状的簇，能识别噪声点。

核心概念（参数：ε 邻域半径，MinPts 最小点数）：

• ε 邻域：以某点为中心、ε 为半径的区域内的样本集合

• 核心点（Core Point）：ε 邻域内样本数 $\geq \mathrm { M i n P t s }$ 的点

• 边界点（Border Point）：不是核心点，但落在某个核心点的ε 邻域内

• 噪声点（Noise Point）：既不是核心点也不是边界点

## 密度可达与密度相连

• 直接密度可达：若 p 是核心点且 q 在 p 的 ε 邻域内，则 q 从 p 直接密度可达

• 密度可达：存在点链 $p _ { 1 } \to p _ { 2 } \to \cdots \to p _ { n }$ ，每步直接密度可达

• 密度相连：存在核心点 o，使得 p 和 q 都从 o 密度可达

一个簇 = 所有互相密度相连的点的最大集合

## DBSCAN 算法步骤与实例

## DBSCAN 算法步骤与实例

## DBSCAN 算法步骤

1 从数据集中随机选择一个未访问的点 p

2 检查 p 的ε邻域：

<sup>•</sup> 若点数 $\geq \mathrm { M i n P t s }$ ，则 p 是核心点，创建新簇

<sup>•</sup> 否则，标记为噪声点（可能后续被其他核心点”收编”为边界点）

3 对新簇中的每个核心点，将其 ε 邻域内的所有点加入该簇

4 递归扩展：若新加入的点也是核心点，继续扩展其邻域

5 重复步骤1-4，直到所有点都被访问

## DBSCAN 算法步骤与实例

## DBSCAN 算法步骤

1 从数据集中随机选择一个未访问的点 p

2 检查 p 的ε邻域：

<sup>•</sup> 若点数 $\geq \mathrm { M i n P t s }$ ，则 p 是核心点，创建新簇

<sup>•</sup> 否则，标记为噪声点（可能后续被其他核心点”收编”为边界点）

3 对新簇中的每个核心点，将其 ε 邻域内的所有点加入该簇

4 递归扩展：若新加入的点也是核心点，继续扩展其邻域

5 重复步骤1-4，直到所有点都被访问

DBSCAN 实例 $( \varepsilon = 2 , \mathbf { M i n P t s } { = } 3 )$ ）：

• 10个二维点，分布为两个簇 + 一个孤立点

• 核心点：邻域内至少3 个点的点

• 算法从第一个核心点开始扩展，通过密度可达连接所有属于同一簇的点

• 孤立点因为不满足密度条件，被标记为噪声

## K-means++初始化策略

## K-means++初始化策略

K-means 的问题：对初始中心敏感

## K-means++初始化策略

K-means 的问题：对初始中心敏感随机初始化可能导致：

• 收敛到局部最优而非全局最优

• 初始中心可能落在同一簇中，导致聚类结果不稳定

• 需要多次运行取最优结果

## K-means++初始化策略

K-means 的问题：对初始中心敏感随机初始化可能导致：

• 收敛到局部最优而非全局最优

• 初始中心可能落在同一簇中，导致聚类结果不稳定

• 需要多次运行取最优结果

K-means++ 初始化策略

核心思想：初始中心之间应该尽可能相距较远。

## K-means++初始化策略

## K-means 的问题：对初始中心敏感

随机初始化可能导致：

• 收敛到局部最优而非全局最优

• 初始中心可能落在同一簇中，导致聚类结果不稳定

• 需要多次运行取最优结果

## K-means++ 初始化策略

核心思想：初始中心之间应该尽可能相距较远。

步骤：

1 从数据集中随机选择第一个中心 $c _ { 1 }$

2 对每个样本 $x _ { i }$ ，计算其到最近已有中心的距离 $d ( x _ { i } )$

以概率 $P ( c _ { k + 1 } = x _ { i } ) = \frac { d ( x _ { i } ) ^ { 2 } } { \sum _ { j } d ( x _ { j } ) ^ { 2 } }$ 选择下一个中心

4 重复步骤2-3，直到选出 K 个初始中心

5 之后按标准 K-means 算法迭代

## K-means++优势分析

## K-means++优势分析

为什么 K-means++更好？

• 距离已有中心越远的点，被选为新中心的概率越大

• 理论保证：K-means++解的期望代价不超过最优解的 O(logK) 倍

• 实际效果：通常只需运行一次即可获得较好结果，而标准 K-means需要多次运行取最优

## K-means++优势分析

## 为什么 K-means++更好？

• 距离已有中心越远的点，被选为新中心的概率越大

• 理论保证：K-means++解的期望代价不超过最优解的 O(logK) 倍

• 实际效果：通常只需运行一次即可获得较好结果，而标准 K-means需要多次运行取最优

K-means++ vs 标准 K-means 对比

<table><tr><td></td><td>K-means(随机初始化)</td><td>K-means++</td></tr><tr><td>初始化策略</td><td>随机选择K个中心</td><td>分散选择初始中心</td></tr><tr><td>稳定性</td><td>多次运行结果差异大</td><td>结果相对稳定</td></tr><tr><td>计算开销</td><td>O(nK)(初始化快)</td><td>O(nK)(初始化稍慢)</td></tr><tr><td>推荐运行次数</td><td>10-50次取最优</td><td>1-3次即可</td></tr></table>

## 聚类有效性评价指标

## 聚类有效性评价指标

外部指标（有真实标签时）

• Rand 指数（RI）：衡量聚类结果与真实分类的一致性

• 调整兰德指数（ARI）：对随机聚类做校正，取值[-1, 1]，越大越好

• FMI（Fowlkes-Mallows Index）：精确率和召回率的几何平均

## 聚类有效性评价指标

## 外部指标（有真实标签时）

• Rand 指数（RI）：衡量聚类结果与真实分类的一致性

• 调整兰德指数（ARI）：对随机聚类做校正，取值[-1, 1]，越大越好

• FMI（Fowlkes-Mallows Index）：精确率和召回率的几何平均内部指标（无真实标签时）

轮廓系数（Silhouette Coeficient）： $s ( i ) = \frac { b ( i ) - a ( i ) } { \operatorname* { m a x } ( a ( i ) , b ( i ) ) }$ ，取值 [-1, 1]

<sup>•</sup> a(i)：样本 i 到同类其他样本的平均距离（凝聚度）

<sup>•</sup> b(i)：样本 i 到最近异类所有样本的平均距离（分离度）

越接近 1越好，接近 0 说明重叠，负值说明分类错误

CH 指数（Calinski-Harabasz）： $\mathrm { C H } = { \frac { { \underline { { \xi } } } \mathrm { H } | \mathrm { \bar { H } } | \mathrm { \underline { { \xi } } } \mathrm { \bar { H } } } { \underline { { \xi } } \mathrm { H } | \mathrm { H } \mathrm { H } \mathrm { H } \mathrm { H } \mathrm { \bar { H } } } }$ 越大越好

• DB 指数（Davies-Bouldin）：衡量类间相似度，越小越好

## 肘部法则与实例

## 肘部法则与实例

肘部法则（Elbow Method）——确定 K 值

思想：随着 K增大，类内离差平方和（SSE）单调递减。

当K 小于真实聚类数时，SSE 下降很快；当K 超过真实聚类数后，SSE下降变缓。

”肘部”对应的 K值即为推荐的聚类数目。

## 肘部法则与实例

肘部法则（Elbow Method）——确定 K 值

思想：随着 K增大，类内离差平方和（SSE）单调递减。

当K 小于真实聚类数时，SSE 下降很快；当K 超过真实聚类数后，SSE下降变缓。

”肘部”对应的 K值即为推荐的聚类数目。

实例：

某数据集不同K 对应的SSE：

<table><tr><td>K</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>SSE</td><td>5000</td><td>2500</td><td>1200</td><td>800</td><td>650</td><td>550</td><td>500</td><td>460</td><td>430</td></tr><tr><td>下降幅度</td><td>-</td><td>2500</td><td>1300</td><td>400</td><td>150</td><td>100</td><td>50</td><td>40</td><td>30</td></tr></table>

## 肘部法则与实例

## 肘部法则（Elbow Method）——确定 K 值

思想：随着 K增大，类内离差平方和（SSE）单调递减。

当K 小于真实聚类数时，SSE 下降很快；当K 超过真实聚类数后，SSE下降变缓。

”肘部”对应的 K值即为推荐的聚类数目。

## 实例：

某数据集不同K 对应的SSE：

<table><tr><td>K</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>SSE</td><td>5000</td><td>2500</td><td>1200</td><td>800</td><td>650</td><td>550</td><td>500</td><td>460</td><td>430</td></tr><tr><td>下降幅度</td><td>-</td><td>2500</td><td>1300</td><td>400</td><td>150</td><td>100</td><td>50</td><td>40</td><td>30</td></tr></table>

## 分析：

K 从 2 到 3 时 SSE 从 2500 降到 1200（下降 1300），K 从 3 到 4 时只降了 400。在 K=3 处形成明显的”肘部”，因此推荐 K=3。

## 肘部法则与实例

肘部法则（Elbow Method）——确定 K 值

思想：随着 K增大，类内离差平方和（SSE）单调递减。

当K 小于真实聚类数时，SSE 下降很快；当K 超过真实聚类数后，SSE下降变缓。

”肘部”对应的 K值即为推荐的聚类数目。

实例：

某数据集不同K 对应的SSE：

<table><tr><td>K</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>SSE</td><td>5000</td><td>2500</td><td>1200</td><td>800</td><td>650</td><td>550</td><td>500</td><td>460</td><td>430</td></tr><tr><td>下降幅度</td><td>-</td><td>2500</td><td>1300</td><td>400</td><td>150</td><td>100</td><td>50</td><td>40</td><td>30</td></tr></table>

## 分析：

K 从 2 到 3 时 SSE 从 2500 降到 1200（下降 1300），K 从 3 到 4 时只降了 400。在 K=3 处形成明显的”肘部”，因此推荐 K=3。

综合选择建议

结合多种方法确定K：肘部法则 + 轮廓系数 + CH指数 + 业务理解。没有绝对”正确”的K，选择最适合业务解释的结果。

## 各聚类方法对比总结

## 各聚类方法对比总结

<table><tr><td>方法</td><td>原理</td><td>聚类形状</td><td>参数</td><td>适用场景</td></tr><tr><td>K-means</td><td>最小化类内距离和</td><td>凸形/球形簇</td><td>K值</td><td>大数据、球状簇</td></tr><tr><td>K-means++</td><td>K-means改进初始化</td><td>凸形/球形簇</td><td>K值</td><td>需要稳定结果</td></tr><tr><td>层次聚类</td><td>逐层合并/分裂</td><td>任意形状</td><td>距离定义、K</td><td>小数据、层次结构</td></tr><tr><td>DBSCAN</td><td>密度连通</td><td>任意形状</td><td> $\varepsilon, \text{MinPts}$ </td><td>噪声数据、不规则簇</td></tr><tr><td>方法</td><td>优点</td><td>缺点</td><td>对异常值</td><td>时间复杂度</td></tr><tr><td>K-means</td><td>快、简单、可解释</td><td>需指定K、对初值敏感</td><td>敏感</td><td> $O(nKt)$ </td></tr><tr><td>K-means++层次聚类</td><td>更稳定、效果更好无需指定K、可视化</td><td>仍需指定K计算慢、不能重分配</td><td>敏感视方法而定</td><td> $O(nKt)$  $O(n^{2}\log n)$ </td></tr><tr><td>DBSCAN</td><td>自动确定簇数、去噪</td><td>难选参数、高维失效</td><td>稳健</td><td> $O(n\log n)$ </td></tr></table>

## 典型相关分析基本思想

## 典型相关分析基本思想

问题

研究两组变量之间的相关关系。

（不是单个变量之间，而是两组变量整体之间）

## 典型相关分析基本思想

## 问题

研究两组变量之间的相关关系。

（不是单个变量之间，而是两组变量整体之间）

## 基本思想

设 $\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是第一组变量， $\boldsymbol { Y } = ( Y _ { 1 } , . . . , Y _ { q } ) ^ { \prime }$ 是第二组变量。找 X 的线性组合 $U = a ^ { \prime } X$ 和Y 的线性组合 $V = b ^ { \prime } Y$ ，使得U 和 V 的相关系数最大。

(U,V) 称为第一对典型变量，其相关系数称为第一典型相关系数。

类似主成分，可以继续找第二对、第三对...（与已有的不相关），直到相关系数不再显著。

## 典型相关分析基本思想

## 问题

研究两组变量之间的相关关系。

（不是单个变量之间，而是两组变量整体之间）

## 基本思想

设 $\boldsymbol { X } = ( X _ { 1 } , . . . , X _ { p } ) ^ { \prime }$ 是第一组变量， $\boldsymbol { Y } = ( Y _ { 1 } , . . . , Y _ { q } ) ^ { \prime }$ 是第二组变量。找 X 的线性组合 $U = a ^ { \prime } X$ 和Y 的线性组合 $V = b ^ { \prime } Y$ ，使得U 和 V 的相关系数最大。

(U,V) 称为第一对典型变量，其相关系数称为第一典型相关系数。

类似主成分，可以继续找第二对、第三对...（与已有的不相关），直到相关系数不再显著。

## 与其他方法的联系

• 相关分析 →两个单变量的关系

• 多元回归→ 一个因变量与多个自变量的关系

• 典型相关→两组多变量之间的整体关系

• 特例：一组只有1 个变量时，就是复相关系数

## 典型相关分析— 数学原理

## 典型相关分析 数学原理

## 数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

## 典型相关分析 数学原理

## 数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

## 典型相关分析 数学原理

## 数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

此时的 (U,V) 称为第一对典型变量， $\rho _ { 1 } = \rho ( U , V )$ 为第一典型相关系数。

## 典型相关分析 数学原理

## 数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

此时的 (U,V) 称为第一对典型变量， $\rho _ { 1 } = \rho ( U , V )$ 为第一典型相关系数。

求解：

## 典型相关分析 数学原理

数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

此时的 (U,V) 称为第一对典型变量， $\rho _ { 1 } = \rho ( U , V )$ 为第一典型相关系数。

求解：

等价于求解矩阵 $\pmb { \Sigma } _ { 1 1 } ^ { - 1 } \pmb { \Sigma } _ { 1 2 } \pmb { \Sigma } _ { 2 2 } ^ { - 1 } \pmb { \Sigma } _ { 2 1 }$ 的特征值问题。

## 典型相关分析 数学原理

数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

此时的 (U,V) 称为第一对典型变量， $\rho _ { 1 } = \rho ( U , V )$ 为第一典型相关系数。

求解：

等价于求解矩阵 $\pmb { \Sigma } _ { 1 1 } ^ { - 1 } \pmb { \Sigma } _ { 1 2 } \pmb { \Sigma } _ { 2 2 } ^ { - 1 } \pmb { \Sigma } _ { 2 1 }$ 的特征值问题。

典型相关系数 $\rho _ { i } = \sqrt { \lambda _ { i } }$ ，其中 $\lambda _ { i }$ 为特征值，按从大到小排列。

## 典型相关分析 数学原理

数学表述

设两组变量 $\pmb { X } = ( X _ { 1 } , \ldots , X _ { p } ) ^ { \prime }$ 和 $\pmb { Y } = ( Y _ { 1 } , \ldots , Y _ { q } ) ^ { \prime }$ ，协方差阵分块为：

$$
\boldsymbol {\Sigma} = \left( \begin{array}{c c} \boldsymbol {\Sigma} _ {1 1} & \boldsymbol {\Sigma} _ {1 2} \\ \boldsymbol {\Sigma} _ {2 1} & \boldsymbol {\Sigma} _ {2 2} \end{array} \right)
$$

找线性组合 $U = \mathbf { a } ^ { \prime } X$ 和 $V = \pmb { b } ^ { \prime } \pmb { Y }$ ，使得：

$$
\rho (U, V) = \frac {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 2} \boldsymbol {b}}{\sqrt {\boldsymbol {a} ^ {\prime} \boldsymbol {\Sigma} _ {1 1} \boldsymbol {a}} \sqrt {\boldsymbol {b} ^ {\prime} \boldsymbol {\Sigma} _ {2 2} \boldsymbol {b}}} = \max
$$

此时的 (U,V) 称为第一对典型变量， $\rho _ { 1 } = \rho ( U , V )$ 为第一典型相关系数。

求解：

等价于求解矩阵 $\pmb { \Sigma } _ { 1 1 } ^ { - 1 } \pmb { \Sigma } _ { 1 2 } \pmb { \Sigma } _ { 2 2 } ^ { - 1 } \pmb { \Sigma } _ { 2 1 }$ 的特征值问题。

典型相关系数 $\rho _ { i } = \sqrt { \lambda _ { i } }$ ，其中 $\lambda _ { i }$ 为特征值，按从大到小排列。

最多有 $\operatorname* { m i n } ( p , q )$ 对典型变量。

## 显著性检验与典型载荷