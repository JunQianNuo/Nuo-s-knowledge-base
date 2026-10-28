---
raw_title: Chapter4
subject: Chapter4
source: Chapter4.pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/e771b16d615ba74e74070c52b016098d27a10db54187ae5c8ea199d41299c3f3.jpg)

四、深度学习中的优化

## 最小化损失函数在机器学习中, 我们通常需要最小化一个总损失函数. 设训练数据集为 $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 所用的学习器为 $\hat { f } ( x ; \theta )$ (这里 θ 表示学习器的参数). 设 $l ( t _ { 1 } , t _ { 2 } )$ 为损失函数用来刻画每个数据点上学习器 $\hat { f }$ 与标签 $y _ { n }$ 的差距. 于是, 总损失函数可以写成

$$
\mathcal {L} (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

## 最小化损失函数在机器学习中, 我们通常需要最小化一个总损失函数. 设训练数据集为 $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 所用的学习器为 $\hat { f } ( x ; \theta )$ (这里 θ 表示学习器的参数). 设 $l ( t _ { 1 } , t _ { 2 } )$ 为损失函数用来刻画每个数据点上学习器 $\hat { f }$ 与标签 $y _ { n }$ 的差距. 于是, 总损失函数可以写成

$$
\mathcal {L} (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

而机器学习的训练过程就是在最小化 $\mathcal { L } ( \boldsymbol { \theta } )$ , 即求解

$$
\min _ {\theta} \mathcal {L} (\theta)
$$

的过程.

## 最小化损失函数在机器学习中, 我们通常需要最小化一个总损失函数. 设训练数据集为 $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 所用的学习器为 $\hat { f } ( x ; \theta )$ (这里 θ 表示学习器的参数). 设 $l ( t _ { 1 } , t _ { 2 } )$ 为损失函数用来刻画每个数据点上学习器 $\hat { f }$ 与标签 $y _ { n }$ 的差距. 于是, 总损失函数可以写成

$$
\mathcal {L} (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

而机器学习的训练过程就是在最小化 $\mathcal { L } ( \boldsymbol { \theta } )$ , 即求解

$$
\min _ {\theta} \mathcal {L} (\theta)
$$

的过程.

在实际应用中我们不需要也无法精确求出 $\mathcal { L } ( \boldsymbol { \theta } )$ 的最小值及相应的最小值点但我们会通过某些优化算法, 尽可能的降低 $\mathcal { L } ( \boldsymbol { \theta } )$ 的值, 以达到可接受的程度

## 优化问题的基本概念给定一个损失函数 $\mathcal { L } ( \boldsymbol { \theta } )$ . 记变量 $\theta$ 的取值范围为 $\mathcal { D } .$

对 $\mathcal { D }$ 中的一点 $\theta ^ { * }$ , 如果存在它的某个领域 $\mathcal { N } \subset \mathcal { D }$ , 使得

$$
\mathcal {L} (\theta^ {*}) \leq \mathcal {L} (\theta), \quad \forall \theta \in \mathcal {N},
$$

则称 $\theta ^ { * }$ 是 $\mathcal { L } ( \boldsymbol { \theta } )$ 的一个局部极小点(local minimum point). 类似也可定义局部极大点(local maximum point).

## 优化问题的基本概念给定一个损失函数 $\mathcal { L } ( \boldsymbol { \theta } )$ . 记变量 $\theta$ 的取值范围为 $\mathcal { D }$

对 $\mathcal { D }$ 中的一点 $\theta ^ { * }$ , 如果存在它的某个领域 $\mathcal { N } \subset \mathcal { D }$ , 使得

$$
\mathcal {L} (\theta^ {*}) \leq \mathcal {L} (\theta), \quad \forall \theta \in \mathcal {N},
$$

则称 $\theta ^ { * }$ 是 $\mathcal { L } ( \boldsymbol { \theta } )$ 的一个局部极小点(local minimum point). 类似也可定义局部极大点(local maximum point).

对 $\mathcal { D }$ 中的一点 $\theta ^ { * }$ , 如果成立

$$
\mathcal {L} (\theta^ {*}) \leq \mathcal {L} (\theta), \quad \forall \theta \in \mathcal {D},
$$

则称 $\theta ^ { * }$ 是 $\mathcal { L } ( \boldsymbol { \theta } )$ 的一个全局极小点(global minimum point). 类似也可定义全局极大点(global maximum point).

在优化 L(θ) 时, 算法常常会找到一个局部极小点并徘徊在该点附近, 而不去寻找真正的全局极小点或者取值更低的其它局部极小点这是机器学习训练中的一个主要困难在优化 $\mathcal { L } ( \boldsymbol { \theta } )$ 时, 算法常常会找到一个局部极小点并徘徊在该点附近, 而不去寻找真正的全局极小点或者取值更低的其它局部极小点这是机器学习训练中的一个主要困难然而, 并不是所有局部极小点都是“不好”的. 设 $\theta ^ { * }$ 是一个局部极小点, 如果

$$
\mathcal {L} (\theta^ {*}) \approx \min _ {\theta} \mathcal {L} (\theta),
$$

即 $\theta ^ { * }$ 处的损失与全局最小损失比较接近, 那么我们认为 $\theta ^ { * }$ 是一个“好”的局部极小点.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/0f3f7215d9ef37e65573ce546f9ea047a36befcea9969e77649e3e949e580a53.jpg)

在优化 $\mathcal { L } ( \boldsymbol { \theta } )$ 时, 算法常常会找到一个局部极小点并徘徊在该点附近, 而不去寻找真正的全局极小点或者取值更低的其它局部极小点这是机器学习训练中的一个主要困难然而, 并不是所有局部极小点都是“不好”的. 设 $\theta ^ { * }$ 是一个局部极小点, 如果

$$
\mathcal {L} (\theta^ {*}) \approx \min _ {\theta} \mathcal {L} (\theta),
$$

即 $\theta ^ { * }$ 处的损失与全局最小损失比较接近, 那么我们认为 $\theta ^ { * }$ 是一个“好”的局部极小点.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/4d1007d6b144819ad781a6409eddb38d1e494160578fe44796075b813b76df72.jpg)

当使用全连接神经网络作为学习器时损失函数可能存在非常多的局部极小点其主要原因是全连接神经网络对参数的可辨识性较差 (教材P.174). 然而, 最新研究表明, 只要网络的宽度非常大相应损失函数的局部极小点大多数都会是好的当 L(θ) 连续可导时, 它的局部极小/大点处的偏导数一定为零. 但若某点处的偏导数为零, 该点未必是局部极值点, 还有可能是鞍点(saddel point). 对一个连续可导的高维函数, 偏导数为零的点大概率都是鞍点.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/f402a6f144a77011e9fcb6f22a0c64dfc8ea1eb73c41347a01284078e782fb4a.jpg)  
图维函数的鞍点相对于局部极小点带来的优化困难, 鞍点更加容易被克服, 尤其是沿负梯度方向进行优化时, 优化器总是能逃离鞍点某些损失函数, 可能不存在局部或全局极小点, 例如交叉熵损失函数 −lnf(x;θ), 或形如下图的函数

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/fb0f36a0f095754343a06518df1ba2dea8968e2b6f0b7c43f0526f2e55a952d6.jpg)

图: 当 L(θ) 的定义域 D 是开集时, 它在 D 上可能不存在全局极小点, 因为使得 L(θ) 取值最小的点趋近于 D 的边界使用优化器对损失函数进行优化时选取合适的初值十分重要在下图中我们试图沿负梯度方向下降搜索全局极小点如果初值选取在橙色点则优化器容易收敛到较差的局部极小点(绿色点).

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/21371c12ae97c88cea6dc4cc48f23d1acadcbb2da03af86bf6618e2143befa9d.jpg)

## 优化算法: 最速下降法由多元微积分的知识, 一个多元函数的图像, 沿着梯度方向上升最快, 沿着梯度相反方向(负梯度方向)下降最快. 而最速下降法(steepest descent method), 俗称梯度法, 即沿着损失函数的负梯度方向对变量进行迭代更新从而较快地降低损失函数的值

## 优化算法: 最速下降法由多元微积分的知识一个多元函数的图像沿着梯度方向上升最快沿着梯度相反方向(负梯度方向)下降最快. 而最速下降法(steepest descent method), 俗称梯度法, 即沿着损失函数的负梯度方向对变量进行迭代更新从而较快地降低损失函数的值具体地, 假设损失函数 $\mathcal { L } ( \boldsymbol { \theta } )$ 存在一阶偏导数. 给定变量 $\theta$ 的一个初始值 $\theta ^ { ( 0 ) }$ , 我们按以下公式对 $\theta$ 进行迭代更新

$$
\theta^ {(k + 1)} = \theta^ {(k)} - \eta_ {k} \nabla \mathcal {L} (\theta^ {(k)}), \quad k = 0, 1, \ldots
$$

其中正实数 $\eta _ { k }$ 是沿负梯度 $- \nabla \mathcal { L } ( \theta ^ { ( k ) } )$ 更新时所用的步长, 也称为学习率(learningrate).

即便是对同一个优化问题, 不同的学习率也可能造成完全不同的优化行为. 例如, 对函数$f ( x ) = x _ { 1 } ^ { 2 } + 4 x _ { 2 } ^ { 2 }$ 进行最小化(全局极小点为 $( 0 , 0 ) )$ , 且选择初始点 $x _ { 1 } ^ { ( 0 ) } > 0 , x _ { 2 } ^ { ( 0 ) } > 0$ 假设每次迭代的学习率都是 $\eta > 0$ , 则最速下降法的迭代格式为

$$
\begin{array}{r} x _ {1} ^ {(k + 1)} = (1 - 2 \eta) x _ {1} ^ {(k)}, \\ x _ {2} ^ {(k + 1)} = (1 - 8 \eta) x _ {2} ^ {(k)}. \end{array}
$$

即便是对同一个优化问题, 不同的学习率也可能造成完全不同的优化行为. 例如, 对函数$f ( x ) = x _ { 1 } ^ { 2 } + 4 x _ { 2 } ^ { 2 }$ 进行最小化(全局极小点为 $( 0 , 0 ) )$ , 且选择初始点 $x _ { 1 } ^ { ( 0 ) } > 0 , x _ { 2 } ^ { ( 0 ) } > 0 .$ 假设每次迭代的学习率都是 $\eta > 0$ , 则最速下降法的迭代格式为

$$
\begin{array}{r} x _ {1} ^ {(k + 1)} = (1 - 2 \eta) x _ {1} ^ {(k)}, \\ x _ {2} ^ {(k + 1)} = (1 - 8 \eta) x _ {2} ^ {(k)}. \end{array}
$$

对 $0 < \eta < 1 / 8$ 和 $1 / 8 < \eta < 1 / 4$ 两种情形, 优化行为分别如下图所示

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/95e6cab298a8df1da66f4216dd7e68e2e48df6d39818dd92afe552ba680828cc.jpg)  
(c) $0 < \eta < 1 / 8$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/2faf6295da1805cf894da3a528588e57b2e5fb3a2b3bddc4fb39ce1f91041cf3.jpg)  
(d) $1 / 8 < \eta < 1 / 4$

而当 $\eta > 1 / 4$ 时上述迭代格式中的 $x _ { 2 } ^ { ( k ) }$ 是发散的即最速下降法不收敛

## 选择最优学习率: 线搜索(line search)

在最速下降法的每一次迭代中, 通常存在着最优步长(即最优学习率), 使得在当前的负梯度方向上损失函数能够达到最小.

## 选择最优学习率: 线搜索(line search)

在最速下降法的每一次迭代中, 通常存在着最优步长(即最优学习率), 使得在当前的负梯度方向上损失函数能够达到最小.

具体地, 当前迭代步的最优学习率 $\eta _ { k } ^ { * }$ (如果存在) 可定义为

$$
\eta_ {k} ^ {*} := \arg \min _ {\eta > 0} \mathcal {L} (\theta^ {(k)} - \eta \nabla \mathcal {L} (\theta^ {(k)})).
$$

定义 $g ( \eta ) = \mathcal { L } ( \theta ^ { ( k ) } - \eta \nabla \mathcal { L } ( \theta ^ { ( k ) } ) )$ . 则 $\eta _ { k } ^ { * }$ 必然满足 $g ^ { \prime } ( \eta _ { k } ^ { * } ) = 0$

因此, 在每一步迭代时, 可以通过求解 $g ^ { \prime } ( \eta _ { k } ^ { * } ) = 0$ 来获得最优学习率, 或近似求解它来获得较优的学习率

## 选择最优学习率: 线搜索(line search)

在最速下降法的每一次迭代中, 通常存在着最优步长(即最优学习率), 使得在当前的负梯度方向上损失函数能够达到最小.

具体地, 当前迭代步的最优学习率 $\eta _ { k } ^ { * }$ (如果存在) 可定义为

$$
\eta_ {k} ^ {*} := \arg \min _ {\eta > 0} \mathcal {L} (\theta^ {(k)} - \eta \nabla \mathcal {L} (\theta^ {(k)})).
$$

定义 $g ( \eta ) = \mathcal { L } ( \theta ^ { ( k ) } - \eta \nabla \mathcal { L } ( \theta ^ { ( k ) } ) )$ . 则 $\eta _ { k } ^ { * }$ 必然满足 $g ^ { \prime } ( \eta _ { k } ^ { * } ) = 0$

因此, 在每一步迭代时, 可以通过求解 $g ^ { \prime } ( \eta _ { k } ^ { * } ) = 0$ 来获得最优学习率, 或近似求解它来获得较优的学习率然而, $g ^ { \prime }$ 可能没有显式表达式, 或表达式可能十分复杂, 故求解 $g ^ { \prime } = 0$ 计算量较大, 需要综合考虑是否使用线搜索寻找最优学习率

## 动量法(Momentum method)

虽然在理论上, 负梯度方向是多元函数下降最快的方向. 但每次都朝负梯度方向进行更新未必是最好的选择.

## 动量法(Momentum method)

虽然在理论上, 负梯度方向是多元函数下降最快的方向. 但每次都朝负梯度方向进行更新未必是最好的选择动量法引入了一个“速度”向量 v, 与原始变量 θ 一起进行迭代更新. 经典动量法的迭代公式如下:

$$
\begin{array}{l} v ^ {(k + 1)} = \mu v ^ {(k)} - \eta \nabla \mathcal {L} (\theta^ {(k)}), \\ \theta^ {(k + 1)} = \theta^ {(k)} + v ^ {(k + 1)}, \end{array}
$$

其中实数 $\mu \in ( 0 , 1 ]$ 称为动量系数.

## 动量法(Momentum method)

虽然在理论上, 负梯度方向是多元函数下降最快的方向. 但每次都朝负梯度方向进行更新未必是最好的选择.

动量法引入了一个“速度”向量 v, 与原始变量 θ 一起进行迭代更新. 经典动量法的迭代公式如下:

$$
\begin{array}{l} v ^ {(k + 1)} = \mu v ^ {(k)} - \eta \nabla \mathcal {L} (\theta^ {(k)}), \\ \theta^ {(k + 1)} = \theta^ {(k)} + v ^ {(k + 1)}, \end{array}
$$

其中实数 $\mu \in ( 0 , 1 ]$ 称为动量系数.

动量法的一个改进版本如下:

$$
\begin{array}{l} v ^ {(k + 1)} = \mu v ^ {(k)} - \eta \nabla \mathcal {L} (\theta^ {(k)} + \mu v ^ {(k)}), \\ \theta^ {(k + 1)} = \theta^ {(k)} + v ^ {(k + 1)}, \end{array}
$$

它也称作 NAG (Nesterov Accelerated Gradient) 方法.

## AdaGrad算法

Adaptive Gradient (AdaGrad) 是另一种基于梯度的优化算法. 它的迭代公式如下:

$$
G ^ {(k)} = \sum_ {i = 0} ^ {k} \nabla f (x ^ {(i)}) \nabla f (x ^ {(i)}) ^ {\top},
$$

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta (G ^ {(k)}) ^ {- 1 / 2} \nabla f (x ^ {(k)}).
$$

其中, $\left( G ^ { ( k ) } \right) ^ { 1 / 2 }$ 是将对称非负定矩阵 $G ^ { ( k ) }$ 进行矩阵分解

$G ^ { ( k ) } = \left( G ^ { ( k ) } \right) ^ { 1 / 2 } \left( G ^ { ( k ) } \right) ^ { 1 / 2 }$ 的结果, 而 $\left( G ^ { ( k ) } \right) ^ { - 1 / 2 }$ 表示 $\left( G ^ { ( k ) } \right) ^ { 1 / 2 }$ 的逆矩阵(当$\left( G ^ { ( k ) } \right) ^ { 1 / 2 }$ 不可逆时, 表示伪逆矩阵).

## RMSProp算法

Root Mean Square Propagation (RMSProp) 算法是一种自适应学习率的方法. 它的迭代公式如下:

$$
v ^ {(k + 1)} = \gamma v ^ {(k)} + (1 - \gamma) (\nabla f (x ^ {(k)})) ^ {2},
$$

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \frac {\nabla f (x ^ {(k)})}{\sqrt {| v ^ {(k + 1)} |}}.
$$

其中常数 $\eta > 0 , \gamma \in ( 0 , 1 )$ ; 向量 $\left( \nabla f ( x ^ { ( k + 1 ) } ) \right) ^ { 2 }$ 表示梯度 $\nabla f ( x ^ { ( k + 1 ) } )$ 逐元素平方后得到的向量; $\sqrt { | v ^ { ( k + 1 ) } | }$ 表示对 $\boldsymbol { v } ^ { ( k + 1 ) }$ 逐元素取绝对值后开根号; 除法 $\frac { \nabla f ( x ^ { ( k ) } ) } { \sqrt { | v ^ { ( k + 1 ) } | } }$ 表示两个向量逐元素相除.

## Adam 算法

Adaptive moment estimation (Adam) 可以看作是 AdaGrad 和 RMSProp 算法的结合.在迭代格式中引入向量 $m ^ { ( k ) } \mathsf { \bar { a } n d } v ^ { ( k ) }$ , 分别表示两个动量向量. 具体的迭代格式为:

$$
\begin{array}{l} m ^ {(k + 1)} = \beta_ {1} m ^ {(k)} + (1 - \beta_ {1}) \nabla f (x ^ {(k)}), \\ v ^ {(k + 1)} = \beta_ {2} v ^ {(k)} + (1 - \beta_ {2}) \left(\nabla f (x ^ {(k)})\right) ^ {2}, \\ x ^ {(k + 1)} = x ^ {(k)} - \eta \frac {m ^ {(k + 1)}}{(1 - \beta_ {1} ^ {k + 1}) \left(\sqrt {| v ^ {(k + 1)} | / (1 - \beta_ {2} ^ {k + 1})} + \epsilon\right)}, \end{array}
$$

其中小常数 ϵ > 0 用于避免分母为零; 常数 $\beta _ { 1 } , \beta _ { 2 } \in [ 0 , 1 )$ 表示动量随 k 的指数衰减率类似于 RMSProp 算法, $\frac { m ^ { ( k + 1 ) } } { ( 1 - \beta _ { 1 } ^ { k + 1 } ) \left( \sqrt { | v ^ { ( k + 1 ) } | / ( 1 - \beta _ { 2 } ^ { k + 1 } ) } + \epsilon \right) }$ 表示两个向量逐元素相除.

## AdaMax 算法另一种类似的方法 Adaptive Maximum (AdaMax), 格式如下:

$$
m ^ {(k + 1)} = \beta_ {1} m ^ {(k)} + (1 - \beta_ {1}) \nabla f (x ^ {(k)}),
$$

$$
u ^ {(k + 1)} = \max \{\beta_ {2} u ^ {(k)}, | \nabla f (x ^ {(k)}) | \},
$$

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \frac {m ^ {(k + 1)}}{(1 - \beta_ {1} ^ {k + 1}) u ^ {(k + 1)}},
$$

其中 $\operatorname* { m a x } \{ \beta _ { 2 } u ^ { ( k ) } , | \nabla f ( x ^ { ( k ) } ) | \}$ 表示对两个向量 $\beta _ { 2 } u ^ { ( k ) }$ 和 $| \nabla f ( x ^ { ( k ) } ) |$ 相同位置的元素取最大值, 最终返回一个同规模的向量.

## 小批量随机优化在机器学习中, 我们往往需要求解如下优化问题:

$$
\min _ {\theta} \mathcal {L} (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

## 小批量随机优化在机器学习中, 我们往往需要求解如下优化问题:

$$
\min _ {\theta} \mathcal {L} (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

若使用基于梯度的方法, 则在每一次迭代时, 都需要计算损失函数 L 关于 $\theta$ 的梯度

$$
\nabla_ {\theta} \mathcal {L} (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} l ^ {\prime} (\hat {f} (x _ {n}; \theta), y _ {n}) \cdot \nabla_ {\theta} \hat {f} (x _ {n}; \theta),
$$

其中 $l ^ { \prime } ( \cdot , \cdot )$ 表示对第一个变量的偏导数

## 小批量随机优化在机器学习中, 我们往往需要求解如下优化问题:

$$
\min _ {\theta} \mathcal {L} (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}; \theta), y _ {n}).
$$

若使用基于梯度的方法, 则在每一次迭代时, 都需要计算损失函数 L 关于 θ 的梯度

$$
\nabla_ {\theta} \mathcal {L} (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} l ^ {\prime} (\hat {f} (x _ {n}; \theta), y _ {n}) \cdot \nabla_ {\theta} \hat {f} (x _ {n}; \theta),
$$

其中 $l ^ { \prime } ( \cdot , \cdot )$ 表示对第一个变量的偏导数在实际问题中数据集规模可能非常大计算整个梯度 $\nabla _ { \boldsymbol { \theta } } \mathcal { L } ( \boldsymbol { \theta } )$ 代价过大. 另一方面,数据点之间的相似度有时候会很高, 这意味着将全部数据点都参与计算梯度意义不大.

因此, 在每一次迭代时我们可以选取整个数据集中的一个小批量子集, 在该子集上计算上述梯度. 记 $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 为原始数据集在优化算法的每次迭代时可选取它的一个小批量子集 $\{ ( x _ { n } , y _ { n } ) \} _ { n \in I }$ , 其中指标集 I 是 {1,2,...,N} 的一个子集 $( S : = | I | )$ ), 并计算“随机”梯度

$$
\frac {1}{S} \sum_ {n \in I} l ^ {\prime} (\hat {f} (x _ {n}; \theta), y _ {n}) \cdot \nabla_ {\theta} \hat {f} (x _ {n}; \theta)
$$

用于近似真正的梯度 $\begin{array} { r } { \nabla _ { \boldsymbol { \theta } } \mathcal { L } ( \boldsymbol { \theta } ) = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } l ^ { \prime } ( \boldsymbol { \hat { f } } ( \boldsymbol { x } _ { n } ; \boldsymbol { \theta } ) , y _ { n } ) \cdot \nabla _ { \boldsymbol { \theta } } \boldsymbol { \hat { f } } ( \boldsymbol { x } _ { n } ; \boldsymbol { \theta } ) } \end{array}$ 虽然每次迭代仅有个数据点参与计算但每次迭代的小批量子集都可以不同随着迭代次数增多, 最终整个数据集都有可能参与计算.

虽然每次迭代仅有个数据点参与计算但每次迭代的小批量子集都可以不同随着迭代次数增多, 最终整个数据集都有可能参与计算.

I 的选取可以是随机的, 如每次迭代时在 1,2,...,N 中按均匀分布选取 S 个互不相同的整数; 也可以是确定的, 如每次迭代时依次按先后顺序选取 S 个整数形成 I (如图所示)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/f08c00f724525eabc93b505e070453cdc644f1b657d6d37c4fc9ba573097e959.jpg)

图: 将训练集均分为 $N / S$ 批, 每次迭代用其中的一批计算“随机”梯度. 在 N/S 次迭代完毕后, 整个训练集被完整用过一次, 之后可以重复前面步骤继续迭代. 每完整地遍历一次训练集称为一轮(epoch).

虽然每次迭代仅有个数据点参与计算但每次迭代的小批量子集都可以不同随着迭代次数增多, 最终整个数据集都有可能参与计算.

I 的选取可以是随机的, 如每次迭代时在 1,2,...,N 中按均匀分布选取 S 个互不相同的整数; 也可以是确定的, 如每次迭代时依次按先后顺序选取 S 个整数形成 I (如图所示)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter4/images/70aad796f6260e014315ad7fbd7d250eb82e3b2010dede077476932c8b090fe7.jpg)

图: 将训练集均分为 $N / S$ 批, 每次迭代用其中的一批计算“随机”梯度. 在 $N / S$ 次迭代完毕后整个训练集被完整用过一次, 之后可以重复前面步骤继续迭代. 每完整地遍历一次训练集称为一轮(epoch).

批量的大小 S 可以根据实际情况而定若 $S = 1$ 则每次迭代仅有一个数据点参与计算“随机”梯度. 若 $S = N$ , 则为原始的最速下降法. 当 $S < N$ 时该方法称为随机梯度下降(stochastic gradient descent) 方法.

## 深度学习中的梯度爆炸与梯度消失神经网络对参数求导时往往涉及多项连乘当网络较深时就会出现大量的项连乘一个简单的例子, 考虑 R 上深度为 L+1, 宽度为 1 的全连接网络

$$
f (x) = w _ {L + 1} \sigma \left(w _ {L} \sigma \left(w _ {L - 1} \left(\dots \sigma \left(w _ {1} x + b _ {1}\right) \dots\right) + b _ {L - 1}\right) + b _ {L}\right) + b
$$

对参数 $w _ { 1 }$ 的偏导数.

## 深度学习中的梯度爆炸与梯度消失神经网络对参数求导时, 往往涉及多项连乘. 当网络较深时, 就会出现大量的项连乘. 一个简单的例子, 考虑 R 上深度为 L+1, 宽度为 1 的全连接网络

$$
f (x) = w _ {L + 1} \sigma \left(w _ {L} \sigma \left(w _ {L - 1} \left(\dots \sigma \left(w _ {1} x + b _ {1}\right) \dots\right) + b _ {L - 1}\right) + b _ {L}\right) + b
$$

对参数 $w _ { 1 }$ 的偏导数.

当 $L = 1$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x;
$$

## 深度学习中的梯度爆炸与梯度消失神经网络对参数求导时往往涉及多项连乘当网络较深时就会出现大量的项连乘一个简单的例子, 考虑 R 上深度为 L+1, 宽度为 1 的全连接网络

$$
f (x) = w _ {L + 1} \sigma \left(w _ {L} \sigma \left(w _ {L - 1} \left(\dots \sigma \left(w _ {1} x + b _ {1}\right) \dots\right) + b _ {L - 1}\right) + b _ {L}\right) + b
$$

对参数 $w _ { 1 }$ 的偏导数.

当 $L = 1$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x;
$$

当 $L = 2$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {3} \sigma^ {\prime} (w _ {2} \sigma (w _ {1} x + b _ {1}) + b _ {2}) \cdot w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x;
$$

## 深度学习中的梯度爆炸与梯度消失神经网络对参数求导时, 往往涉及多项连乘. 当网络较深时, 就会出现大量的项连乘. 一个简单的例子, 考虑 R 上深度为 L+1, 宽度为 1 的全连接网络

$$
f (x) = w _ {L + 1} \sigma \left(w _ {L} \sigma \left(w _ {L - 1} \left(\dots \sigma \left(w _ {1} x + b _ {1}\right) \dots\right) + b _ {L - 1}\right) + b _ {L}\right) + b
$$

对参数 $w _ { 1 }$ 的偏导数.

当 $L = 1$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x;
$$

当 $L = 2$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {3} \sigma^ {\prime} (w _ {2} \sigma (w _ {1} x + b _ {1}) + b _ {2}) \cdot w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x;
$$

当 $L = 3$ 时,

$$
\frac {\partial f}{\partial w _ {1}} = w _ {4} \sigma^ {\prime} (w _ {3} \sigma (w _ {2} \sigma (w _ {1} x + b _ {1}) + b _ {2}) + b _ {3}) \cdot w _ {3} \sigma^ {\prime} (w _ {2} \sigma (w _ {1} x + b _ {1}) + b _ {2}) \cdot w _ {2} \sigma^ {\prime} (w _ {1} x + b _ {1}) \cdot x.
$$

从该例子中可以看出, 对 $w _ { 1 }$ 的偏导数涉及 L 个形如 $w _ { \ell } \sigma ^ { \prime } ( \dots )$ 的项连乘.

在实际应用中 $w _ { \ell }$ 的值可能较接近例如对神经网络的初始化通常会设置 $w _ { \ell }$ 在0的附近). 同时, 选取的 $\sigma ^ { \prime }$ 可能一致有界 (例如, 选取 $\sigma$ 为 logistic sigmoid 函数). 此时,大量形如 $w _ { \ell } \sigma ^ { \prime } ( \dots )$ 的项相乘会导致乘积十分接近甚至因低于机器精度而数值向下溢出. 最终, 导致损失函数对参数的导数十分接近0, 即梯度消失(vanishing gradient).

从该例子中可以看出, 对 $w _ { 1 }$ 的偏导数涉及 L 个形如 $w _ { \ell } \sigma ^ { \prime } ( \dots )$ 的项连乘.

在实际应用中 $w _ { \ell }$ 的值可能较接近例如对神经网络的初始化通常会设置 $w _ { \ell }$ 在0的附近). 同时, 选取的 $\sigma ^ { \prime }$ 可能一致有界 (例如, 选取 $\sigma$ 为 logistic sigmoid 函数). 此时大量形如 $w _ { \ell } \sigma ^ { \prime } ( \dots )$ 的项相乘会导致乘积十分接近甚至因低于机器精度而数值向下溢出. 最终, 导致损失函数对参数的导数十分接近0, 即梯度消失(vanishing gradient).

另一方面, 在神经网络的训练过程中, $| w _ { \ell } |$ 的值可能会变得较大 (如使用了过大的学习率). 此时, 大量形如 $w _ { \ell } \sigma ^ { \prime } ( \dots )$ 的项相乘会导致乘积的绝对值非常大. 最终, 导致损失函数对参数的导数非常大, 即梯度爆炸(exploding gradient).

## PyTorch 中的优化器实现

PyTorch 自带的优化命令库为 <sub>torch.optim</sub>.

## PyTorch 中的优化器实现

PyTorch 自带的优化命令库为 <sub>torch.optim</sub>.

## 定义变量能够被优化器优化的变量必须是 Tensor 数据类型, 并且可以被优化器计算梯度. 因此,可如下定义

parameters=torch.zeros((10,)) parameters.requires\_grad = True

## PyTorch 中的优化器实现

PyTorch 自带的优化命令库为 <sub>torch.optim</sub>.

## 定义变量能够被优化器优化的变量必须是 Tensor 数据类型, 并且可以被优化器计算梯度. 因此,可如下定义

```python
parameters=torch.zeros((10,))
parameters.requires_grad = True
```

## 建立优化器为已定义的参数 <sub>parameters</sub> 建立一个最速下降法的优化器, 并设置学习率为 0.01:

```txt
optimizer = torch.optim.SGD([parameters], lr=0.01)
```

这里的 <sub>SGD</sub> 可以替换成其它的优化算法, 如 <sub>Adagrad</sub>, <sub>Adam</sub>, <sub>Adamax</sub>, <sub>LBFGS</sub>, <sub>RMSprop</sub>等.

## 定义损失函数可以用直接赋值的方式, 定义一个损失函数变量. 它一般是包含了待优化参数的某个表达式. 例如, 定义如下的均方误差损失函数

```python
loss = torch.Tensor([0])
for n in range(N):
    loss = loss + (torch.dot(parameters, data_X[n]) - data_Y[n]) ** 2
loss = loss/N
```

## 定义损失函数可以用直接赋值的方式, 定义一个损失函数变量. 它一般是包含了待优化参数的某个表达式. 例如, 定义如下的均方误差损失函数

```python
loss = torch.Tensor([0])
for n in range(N):
    loss = loss + (torch.dot(parameters, data_X[n]) - data_Y[n]) ** 2
loss = loss/N
```

## 计算损失函数关于参数的梯度在每次计算梯度之前, 一般要先将之前计算的梯度信息清零: <sub>optimizer.zero\_grad</sub>()

计算梯度: <sub>loss.backward</sub>()

## 定义损失函数可以用直接赋值的方式, 定义一个损失函数变量. 它一般是包含了待优化参数的某个表达式. 例如, 定义如下的均方误差损失函数

```python
loss = torch.Tensor([0])
for n in range(N):
    loss = loss + (torch.dot(parameters, data_X[n]) - data_Y[n]) ** 2
loss = loss/N
```

## 计算损失函数关于参数的梯度在每次计算梯度之前, 一般要先将之前计算的梯度信息清零: <sub>optimizer.zero\_grad</sub>()

计算梯度: <sub>loss.backward</sub>()

## 执行一次优化执行一次优化, 即对参数进行更新: <sub>optimizer.step</sub>()

演示给定函数

$$
f (x) = \frac {1}{d - 3} \sum_ {i = 1} ^ {d - 3} (x _ {i} x _ {i + 1} + x _ {i + 1} x _ {i + 2} + x _ {i + 2} x _ {i + 3} - a _ {i}) ^ {2},
$$

其中 $\boldsymbol { x } = ( x _ { 1 } , \dots , x _ { d } )$ 为变量, $\begin{array} { r } { a _ { i } = \frac { i } { d - 3 } } \end{array}$ 为给定的数. 求解 $\operatorname* { m i n } _ { x } f ( x )$

1. 定义待优化的变量 $x ;$

2. 定义优化器;

3. 输入损失函数 $f ( x )$

4. 进行优化计算并演示.

## 本章总结

▶ 损失函数、极值、优化算法、随机梯度下降法、梯度爆炸与梯度消失(参考: 教材8.1, 8.2, 8.3, 8.5)

▶ torch.optim 库的使用(参考: 官方文档 https://pytorch.org/docs/stable/optim.html)