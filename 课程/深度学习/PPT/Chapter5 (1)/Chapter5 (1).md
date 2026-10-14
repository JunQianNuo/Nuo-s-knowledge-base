---
raw_title: Chapter5 (1)
subject: Chapter5 (1)
source: Chapter5 (1).pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](images/e771b16d615ba74e74070c52b016098d27a10db54187ae5c8ea199d41299c3f3.jpg)

## 五、回归模型

## 以全连接神经网络作为学习器机器学习模型中最常见的一类, 就是用某种学习器直接学习(逼近)目标函数 (如在第2章提到的1-D例子中, 用多项式去逼近目标函数).

## 以全连接神经网络作为学习器机器学习模型中最常见的一类, 就是用某种学习器直接学习(逼近)目标函数 (如在第2章提到的1-D例子中, 用多项式去逼近目标函数).

由神经网络逼近理论(如万能近似定理), 全连接神经网络对常见的函数具有一定的逼近能力. 因此, 全连接神经网络也是一种可行的学习器.

## 学习 d 维目标函数令 $K \subset \mathbb { R } ^ { d }$ 是一个有界闭集, f : K → R 是定义在 K 上的未知目标函数. 设$\{ ( x ^ { ( n ) } , y ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ 是已知的训练数据集其中 $x ^ { ( n ) } \in K , y ^ { ( n ) } = f ( x ^ { ( n ) } )$

## 学习 d 维目标函数令 $K \subset \mathbb { R } ^ { d }$ 是一个有界闭集, f : K → R 是定义在 K 上的未知目标函数. 设$\{ ( x ^ { ( n ) } , y ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ 是已知的训练数据集其中 $x ^ { ( n ) } \in K , y ^ { ( n ) } = f ( x ^ { ( n ) } )$

此时, 给定一个全连接神经网络的架构 (深度、宽度、激活函数), 并令具有该架构的神经网络为学习器去学习 f (即在训练数据集上逼近 f), 就可以导出常见的深度学习模型.

## 学习 d 维目标函数令 $K \subset \mathbb { R } ^ { d }$ 是一个有界闭集, f : K → R 是定义在 K 上的未知目标函数. 设$\{ ( x ^ { ( n ) } , y ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ 是已知的训练数据集其中 $x ^ { ( n ) } \in K , y ^ { ( n ) } = f ( x ^ { ( n ) } )$

此时, 给定一个全连接神经网络的架构 (深度、宽度、激活函数), 并令具有该架构的神经网络为学习器去学习 f (即在训练数据集上逼近 f), 就可以导出常见的深度学习模型.

当函数的值域是连续分布时一般称这样的学习模型为回归模型例如, 记 $\mathcal { F } _ { L , M , \sigma }$ 为所有从 K 映射到 R, 深度为 L+1, 宽度为 M, 隐藏层激活函数为$\sigma$ 的全连接神经网络形成的集合, 即

$$
\begin{array}{c} \mathcal {F} _ {L, M, \sigma} := \Big \{\phi (x) = W ^ {L + 1} \sigma \Big (W ^ {L} \sigma \big (\ldots \sigma (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1}: \\ W ^ {L + 1} \in \mathbb {R} ^ {1 \times M}, \quad W ^ {\ell} \in \mathbb {R} ^ {M \times M},   \ell = 2, \ldots , L, \quad W ^ {1} \in \mathbb {R} ^ {M \times d}, \\ b ^ {L + 1} \in \mathbb {R}, \quad b ^ {\ell} \in \mathbb {R} ^ {M \times 1},   \ell = 1, \ldots , L \Big \}. \end{array}
$$

例如, 记 $\mathcal { F } _ { L , M , \sigma }$ 为所有从 K 映射到 R, 深度为 L+1, 宽度为 M, 隐藏层激活函数为$\sigma$ 的全连接神经网络形成的集合, 即

$$
\begin{array}{c} \mathcal {F} _ {L, M, \sigma} := \Big \{\phi (x) = W ^ {L + 1} \sigma \Big (W ^ {L} \sigma \big (\ldots \sigma (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1}: \\ W ^ {L + 1} \in \mathbb {R} ^ {1 \times M}, \quad W ^ {\ell} \in \mathbb {R} ^ {M \times M},   \ell = 2, \ldots , L, \quad W ^ {1} \in \mathbb {R} ^ {M \times d}, \\ b ^ {L + 1} \in \mathbb {R}, \quad b ^ {\ell} \in \mathbb {R} ^ {M \times 1},   \ell = 1, \ldots , L \Big \}. \end{array}
$$

于是, 相应的学习模型可写成:

$$
\min _ {\phi \in \mathcal {F} _ {L, M, \sigma}} L [ \phi ] := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\phi (x ^ {(n)}), y ^ {(n)}),
$$

其中, $l ( t , y ) : \mathbb { R } ^ { 2 } \to$ R 是某类损失函数.

有时, 为了强调模型的变量是神经网络的参数(即所有权重和偏置), 会引进符号$\theta = \{ W ^ { \ell } , b ^ { \ell } \} _ { \ell = 1 } ^ { L + 1 }$ , 表示网络全体参数形成的集合. 于是, 神经网络 $\phi ( x )$ 也可写成$\phi ( x ; \theta )$ , 相应的学习模型可写成

$$
\min _ {\theta} L (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\phi (x ^ {(n)}; \theta), y ^ {(n)}).
$$

## 例: 用二层ReLU网络学习连续函数给定二维目标函数 f : $K : = [ - 1 , 1 ] \times [ - 1 , 1 ] \to \mathbb { R } , \ f ( x ) = 1 / ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 1 )$ . 在 K 上生成 N 个均匀随机分布的点 $\{ x ^ { ( n ) } \}$ 作为训练数据的特征(如下图所示), 并令$y ^ { ( n ) } = f ( x ^ { ( n ) } )$ 作为训练数据的标签.

![](images/ed92b85bb06d2588db633ad0745e6198489b99f6d89bf6eee336fa0368baa496.jpg)  
图: 均匀分布的随机点(N = 100)

## 例: 用二层ReLU网络学习连续函数给定二维目标函数 f : $K : = [ - 1 , 1 ] \times [ - 1 , 1 ] \to \mathbb { R } , \ f ( x ) = 1 / ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + 1 )$ . 在 K 上生成 N 个均匀随机分布的点 $\{ x ^ { ( n ) } \}$ 作为训练数据的特征(如下图所示), 并令$y ^ { ( n ) } = f ( x ^ { ( n ) } )$ 作为训练数据的标签.

![](images/7d5fb117f3b1e027533efd00aad3fedd6f221bb1a1fd1c640412fd8ba8e66161.jpg)  
图: 均匀分布的随机点(N = 100)

令假设空间为全体深度为2、宽度为M的ReLU全连接神经网络, 即

$$
\mathcal {F} _ {2, M, \mathrm{ReLU}} := \left\{\phi (x) = \sum_ {m = 1} ^ {M} a _ {m} \mathrm{ReLU} (w _ {m} ^ {\top} x + b _ {m}) + b: \right.
$$

$$
\left. a _ {m}, b _ {m}, b \in \mathbb {R}, w _ {m} \in \mathbb {R} ^ {2 \times 1} \right\}.
$$

我们选用均方误差, 即 $\ell ^ { 2 } .$ -损失作为损失函数, 于是就有如下模型:

$$
\min _ {\phi \in \mathcal {F} _ {2, M, \mathrm{ReLU}}} \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\phi (x ^ {(n)}) - y ^ {(n)}\right) ^ {2},
$$

或

$$
\begin{array}{l} \min _ {a _ {m}, b _ {m}, b, w _ {m}} L (a _ {m}, b _ {m}, b, w _ {m}) \\ := \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\sum_ {m = 1} ^ {M} a _ {m} \text {ReLU} (w _ {m} ^ {\top} x ^ {(n)} + b _ {m}) + b - y ^ {(n)}\right) ^ {2}. \end{array}
$$

我们选用均方误差, 即 $\ell ^ { 2 } .$ -损失作为损失函数, 于是就有如下模型:

$$
\min _ {\phi \in \mathcal {F} _ {2, M, \mathrm{ReLU}}} \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\phi (x ^ {(n)}) - y ^ {(n)}\right) ^ {2},
$$

或

$$
\begin{array}{l} \min _ {a _ {m}, b _ {m}, b, w _ {m}} L (a _ {m}, b _ {m}, b, w _ {m}) \\ := \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\sum_ {m = 1} ^ {M} a _ {m} \mathrm{ReLU} (w _ {m} ^ {\top} x ^ {(n)} + b _ {m}) + b - y ^ {(n)}\right) ^ {2}. \end{array}
$$

由于 ReLU 激活函数的存在, 上述总损失函数 L 通常不是一个凸函数, 即上述优化问题并不是一个凸优化这也是深度学习模型与多项式回归线性回归的主要不同之处

## 变量(网络参数)初始化当我们用优化算法如最速下降法求解上述优化问题时首先要对变量 $\{ a _ { m } , b _ { m } , b , w _ { m } \}$ 进行初始化, 即赋予初值. 学习理论表明, 在深度学习模型中, 不同的变量初始化方式对优化算法的收敛性有着很大的影响

## 变量(网络参数)初始化当我们用优化算法如最速下降法求解上述优化问题时首先要对变量 $\{ a _ { m } , b _ { m } , b , w _ { m } \}$ 进行初始化, 即赋予初值. 学习理论表明, 在深度学习模型中, 不同的变量初始化方式对优化算法的收敛性有着很大的影响在一些其它的迭代算法中人们往往倾向于将变量初始化为固定常数如用迭代法求解线性方程组 Ax = b, 可以将 x 初始化为零向量). 然而, 理论和实践均表明, 在机器学习中,对变量初始化为固定常数不是一个好的选择, 因为这可能会导致优化算法收敛到一个较差的鞍点.

## 变量(网络参数)初始化当我们用优化算法如最速下降法求解上述优化问题时首先要对变量 $\{ a _ { m } , b _ { m } , b , w _ { m } \}$ 进行初始化, 即赋予初值. 学习理论表明, 在深度学习模型中, 不同的变量初始化方式对优化算法的收敛性有着很大的影响在一些其它的迭代算法中人们往往倾向于将变量初始化为固定常数如用迭代法求解线性方程组 Ax = b, 可以将 x 初始化为零向量). 然而, 理论和实践均表明, 在机器学习中,对变量初始化为固定常数不是一个好的选择, 因为这可能会导致优化算法收敛到一个较差的鞍点.

对于一个神经网络, 若每一层的所有权重都初始化成相同的数值, 可能会导致这些权重在优化算法下始终被同等对待从而在多次迭代后仍然保持相同的数值这样这一层的全体神经元都可以等价于一个神经元失去了宽度的意义

## 变量(网络参数)初始化当我们用优化算法如最速下降法求解上述优化问题时首先要对变量 $\{ a _ { m } , b _ { m } , b , w _ { m } \}$ 进行初始化, 即赋予初值. 学习理论表明, 在深度学习模型中, 不同的变量初始化方式对优化算法的收敛性有着很大的影响在一些其它的迭代算法中人们往往倾向于将变量初始化为固定常数如用迭代法求解线性方程组 Ax = b, 可以将 x 初始化为零向量). 然而, 理论和实践均表明, 在机器学习中,对变量初始化为固定常数不是一个好的选择, 因为这可能会导致优化算法收敛到一个较差的鞍点.

对于一个神经网络若每一层的所有权重都初始化成相同的数值可能会导致这些权重在优化算法下始终被同等对待从而在多次迭代后仍然保持相同的数值这样这一层的全体神经元都可以等价于一个神经元, 失去了宽度的意义.

因此, 大多数情况下, 我们都会将网络参数按某种概率分布(如正态分布、均匀分布)进行随机初始化(random initialization).

考虑从 $\mathbb { R } ^ { d }$ 映射到 $\mathbb { R } ^ { d ^ { \prime } }$ 的全连接神经网络

$$
\phi (x; \theta) = W ^ {L + 1} \sigma^ {L} \Big (W ^ {L} \sigma^ {L - 1} \big (\ldots \sigma^ {1} (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1},
$$

其中 $W _ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times M _ { \ell - 1 } } ( \ell = 1 , \dots , L + 1 )$ . 这里 $M _ { 0 } = d$ 是输入维度; 对 $\ell = 1 , \ldots , L$ $M _ { \ell }$ 是第 ℓ 个隐藏层的宽度; $M _ { L + 1 } = d ^ { \prime }$ 是输出维度.

考虑从 $\mathbb { R } ^ { d }$ 映射到 $\mathbb { R } ^ { d ^ { \prime } }$ 的全连接神经网络

$$
\phi (x; \theta) = W ^ {L + 1} \sigma^ {L} \Big (W ^ {L} \sigma^ {L - 1} \big (\ldots \sigma^ {1} (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1},
$$

其中 $W _ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times M _ { \ell - 1 } } ( \ell = 1 , \dots , L + 1 )$ . 这里 $M _ { 0 } = d$ 是输入维度; 对 $\ell = 1 , \ldots , L$ $M _ { \ell }$ 是第 ℓ 个隐藏层的宽度; $M _ { L + 1 } = d ^ { \prime }$ 是输出维度.

对于上述全连接网络, 有以下几种较好的初始化方式:

<sup>▶</sup> Lecun initialization: $\begin{array} { r } { w _ { i j } ^ { \ell } \sim \mathcal N ( 0 , \frac { 1 } { M _ { \ell - 1 } } ) } \end{array}$

<sup>▶</sup> Xavier initialization:

正态分布 $\begin{array} { r } { w _ { i j } ^ { \ell } \sim \mathcal N ( 0 , \frac { 2 } { M _ { \ell - 1 } + M _ { \ell } } ) } \end{array}$

均匀分布 $\begin{array} { r } { w _ { i j } ^ { \ell } \sim \mathcal { U } ( - \sqrt { \frac { 6 } { M _ { \ell - 1 } + M _ { \ell } } } , \sqrt { \frac { 6 } { M _ { \ell - 1 } + M _ { \ell } } } ) } \end{array}$ ;

He initialization: $\begin{array} { r } { w _ { i j } ^ { \ell } \sim \mathcal N ( 0 , \frac { 2 } { M _ { \ell - 1 } } ) } \end{array}$ 或 $\begin{array} { r } { w _ { i j } ^ { \ell } \sim \mathcal N ( 0 , \frac { 2 } { M _ { \ell } } ) } \end{array}$ ;

这里 $w _ { i j } ^ { \ell }$ 表示权重矩阵 $W ^ { \ell }$ 的任一元素. 对每个矩阵 $W ^ { \ell }$ , 它的元素进行随机初始化时是独立同分布的.

## 优化过程(训练)

在变量完成初始化后, 便可使用优化算法对深度学习模型的损失函数进行优化记神经网络学习器为 $\phi ( x ; \theta )$ , 则回归模型为

$$
\min _ {\theta} L (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\phi (x ^ {(n)}; \theta), y ^ {(n)}).
$$

## 优化过程(训练)

在变量完成初始化后, 便可使用优化算法对深度学习模型的损失函数进行优化记神经网络学习器为 $\phi ( x ; \theta )$ , 则回归模型为

$$
\min _ {\theta} L (\theta) := \frac {1}{N} \sum_ {n = 1} ^ {N} l (\phi (x ^ {(n)}; \theta), y ^ {(n)}).
$$

使用基于梯度的算法进行优化时需要计算梯度

$$
\nabla_ {\theta} L (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} \partial_ {t} l (\phi (x ^ {(n)}; \theta), y ^ {(n)}) \cdot \nabla_ {\theta} \phi (x ^ {(n)}; \theta).
$$

## 测试在经过若干次优化迭代(即训练)后, 我们得到上述优化问题的某个可行解 $\theta ^ { * }$ . 此时, 如果优化损失 $L ( \theta ^ { * } )$ 的值已经比较小(如小于某个我们设定的阈值), 就可以停止优化, 并接受$\theta ^ { * }$ 作为最终的数值解. 此时, $\phi ( x ; \theta ^ { * } )$ 可以看作是训练后的神经网络.

## 测试在经过若干次优化迭代即训练后我们得到上述优化问题的某个可行解 $\theta ^ { * }$ 此时如果优化损失 $L ( \theta ^ { * } )$ 的值已经比较小(如小于某个我们设定的阈值), 就可以停止优化, 并接受$\theta ^ { * }$ 作为最终的数值解. 此时, $\phi ( x ; \theta ^ { * } )$ 可以看作是训练后的神经网络.

之后, 需要在某个测试集上检测 $\phi ( x ; \theta ^ { * } )$ 的泛化性能. 令 $\{ ( \hat { x } ^ { ( n ) } , \hat { y } ^ { ( n ) } ) \} _ { n = 1 } ^ { \hat { N } }$ 为给定的测试集. 我们可以计算泛化损失

$$
\hat {L} (\theta^ {*}) = \frac {1}{\hat {N}} \sum_ {n = 1} ^ {\hat {N}} l (\phi (\hat {x} ^ {(n)}; \theta^ {*}), \hat {y} ^ {(n)}).
$$

如果泛化损失也比较小, 则可以认为该网络 $\phi ( x ; \theta ^ { * } )$ 具有较好的泛化性能

## 预测在工业应用中训练完成的神经网络往往要参与各种实际用途例如某实际问题中有一个数据特征 ${ \tilde { x } } ,$ 需要用训练后的网络 $\phi ( x ; \theta ^ { * } )$ 去预测相应的数据标签此时只需要直接求值即计算

$$
\tilde {y} = \phi (\tilde {x}; \theta^ {*}).
$$

计算后的 $\tilde { y }$ 便是我们预测的特征 $\tilde { x }$ 的标签.

## 预测在工业应用中训练完成的神经网络往往要参与各种实际用途例如某实际问题中有一个数据特征 ${ \tilde { x } } ,$ 需要用训练后的网络 $\phi ( x ; \theta ^ { * } )$ 去预测相应的数据标签此时只需要直接求值即计算

$$
\tilde {y} = \phi (\tilde {x}; \theta^ {*}).
$$

计算后的 $\tilde { y }$ 便是我们预测的特征 $\tilde { x }$ 的标签.

以图像识别为例, 假设某个用于识别的神经网络已经在某个数据集下训练完成. 之后, 我们为网络输入一张新的图片(即x˜), 计算网络的输出值(即y˜). 该输出值就是对该图片进行识别的结果.

![](images/47db6b5bd1c53098e116c51d92a9fc2137fe38d820fdfbbaa8ea3bb886c65861.jpg)

## 正则化为防止可能出现的过拟合现象, 在深度学习模型的损失函数中也可以加入正则项记 θ 是神经网络所有可训练的参数形成的集合(可以视为由参数排列而成的一个向量).则正则项就是一个关于 θ 的范数惩罚项, 记作 Ω(θ).

## 正则化为防止可能出现的过拟合现象, 在深度学习模型的损失函数中也可以加入正则项记 θ 是神经网络所有可训练的参数形成的集合(可以视为由参数排列而成的一个向量).则正则项就是一个关于 $\theta$ 的范数惩罚项, 记作 Ω(θ).

假设原始的损失函数是 L(θ), 则加入正则项后的新损失函数为

$$
\tilde {L} (\theta) = L (\theta) + \lambda \Omega (\theta),
$$

其中 λ > 0 为给定的常数, 表示正则项的影响强度

## 正则化为防止可能出现的过拟合现象, 在深度学习模型的损失函数中也可以加入正则项记 $\theta$ 是神经网络所有可训练的参数形成的集合(可以视为由参数排列而成的一个向量).则正则项就是一个关于 $\theta$ 的范数惩罚项, 记作 Ω(θ).

假设原始的损失函数是 L(θ), 则加入正则项后的新损失函数为

$$
\tilde {L} (\theta) = L (\theta) + \lambda \Omega (\theta),
$$

其中 λ > 0 为给定的常数, 表示正则项的影响强度一般地, 记 $\theta = ( \theta _ { 1 } , \dots , \theta _ { K } )$ . 常用的正则化方式有

▶ $L ^ { 2 }$ 正则化: $\begin{array} { r } { \Omega ( { \boldsymbol { \theta } } ) = \| { \boldsymbol { \theta } } \| _ { 2 } ^ { 2 } = \sum _ { k = 1 } ^ { K } | \theta _ { k } | ^ { 2 } } \end{array}$

▶ $L ^ { 1 }$ 正则化: $\begin{array} { r } { \Omega ( { \boldsymbol { \theta } } ) = \| { \boldsymbol { \theta } } \| _ { 1 } = \sum _ { k = 1 } ^ { K } | \theta _ { k } | } \end{array}$

## $L ^ { 2 }$ 正则化带 $L ^ { 2 }$ 正则化项的目标函数为 $\tilde { L } ( \theta ) = L ( \theta ) + \lambda \| \theta \| _ { 2 } ^ { 2 }$

## $L ^ { 2 }$ 正则化带 $L ^ { 2 }$ 正则化项的目标函数为 $\tilde { L } ( \theta ) = L ( \theta ) + \lambda \| \theta \| _ { 2 } ^ { 2 }$

记 $L ( \theta )$ 的全局极小点为 $\theta ^ { * }$ . 而正则项 $\| \theta \| _ { 2 } ^ { 2 }$ 的全局极小点显然为 $\theta = 0$ . 于是, $\tilde { L } ( \theta )$ 的全局极小点 $\tilde { \theta }$ 其实是 $\theta ^ { * }$ 和之间的某个平衡点

![](images/ee1cea35b642408c5291eabfd52fd27e26514815abb1eda3e0b2afbcf9f5551c.jpg)

图: 以 $\theta = ( \theta _ { 1 } , \theta _ { 2 } )$ 为例. 实线表示 $L ( \theta )$ 的等值线; 虚线表示正则项 $\| \theta \| _ { 2 } ^ { 2 }$ 的等值线. 则 $\tilde { \theta }$ 位于 $\theta ^ { * }$ 和 0 之间.随着 λ 从 0 不断增大, $\tilde { \theta }$ 的位置从 $\theta ^ { * }$ 不断地变化到 0

## $L ^ { 1 }$ 正则化带 $L ^ { 1 }$ 正则化项的目标函数为 $\tilde { L } ( \theta ) = L ( \theta ) + \lambda \| \theta \| _ { 1 }$

## $L ^ { 1 }$ 正则化带 $L ^ { 1 }$ 正则化项的目标函数为 $\tilde { L } ( \theta ) = L ( \theta ) + \lambda \| \theta \| _ { 1 }$

$L ^ { 2 }$ 正则项 $\| \theta \| _ { 2 } ^ { 2 }$ 对 $\theta$ 的梯度为 $\nabla _ { \theta } \| \theta \| _ { 2 } ^ { 2 } = 2 \theta$ , 仍然是一个连续函数; 而 $L ^ { 1 }$ 正则项$\| \theta \| 1$ 对 $\theta$ 的梯度为 $\nabla _ { \theta } \| \theta \| _ { 1 } = \mathrm { s i g n } ( \theta )$ , 即对 $\theta$ 的每一个元素取符号, 并不是一个连续函数.

相比 $L ^ { 2 }$ 正则化, $L ^ { 1 }$ 正则化容易产生更稀疏的解, 即全局极小点容易有更多的0元素

## 提前终止

![](images/aa65787621f55ad21fb8f29fb00995576544f7d1f2034993d12ebc3fe9452ea9.jpg)  
图: 随着训练进行训练损失(蓝色)总体呈下降趋势而泛化损失(绿色)总体呈先下降后缓慢上升的趋势因此, 可以在训练前设立一个交叉验证集, 并在训练过程中计算验证集上的泛化损失. 当发现泛化损失开始慢慢增大时, 就可以提前终止训练. 这种正则化的方式称作提前终止(early stopping)

## 深度学习的隐式正则性近几年研究发现常见的神经网络架构其本身就自带某种正则性当用某个神经网络去学习某些目标函数时, 在基于梯度的优化算法下, 网络会优先学习目标函数的低频率成分, 之后才渐渐学习高频率成分. 这种现象被称为频率原则(F-Principle).

图红色虚线表示目标函数 $f$ 的离散傅里叶变换 $\hat { f }$ 横坐标越接近表示频率越低蓝色实线表示神经网络学习器 $\phi$ 的离散傅里叶变换 $\hat { \phi } .$ 可以看到, $\hat { \phi }$ 先逼近 $\hat { f }$ 的低频成分, 后逼近高频成分.

## 深度学习的隐式正则性近几年研究发现常见的神经网络架构其本身就自带某种正则性当用某个神经网络去学习某些目标函数时, 在基于梯度的优化算法下, 网络会优先学习目标函数的低频率成分, 之后才渐渐学习高频率成分. 这种现象被称为频率原则(F-Principle).

图: 红色虚线表示目标函数 f 的离散傅里叶变换 $\hat { f }$ (横坐标越接近0表示频率越低); 蓝色实线表示神经网络学习器 $\phi$ 的离散傅里叶变换 $\hat { \phi } .$ 可以看到, $\hat { \phi }$ 先逼近 $\hat { f }$ 的低频成分, 后逼近高频成分.

因此在通常的深度学习中神经网络随着训练会优先收敛到一个平缓的函数之后才可能渐渐变得震荡. 也就是说, 即使在损失函数中不加入正则项, 深度学习本身也具有一定正则性. 这种正则性也称为隐式正则性(implicit regularization).

## PyTorch 中的神经网络实现

PyTorch 自带的神经网络命令库为 <sub>torch.nn</sub>.PyTorch 自带的神经网络相关函数命令库为 <sub>torch.nn.functional</sub>.

定义神经网络的一个线性层(即仿射变换)

以下代码可以定义一个形如 $y = W x + b$ 的仿射变换, 其中 $x \in \mathbb { R } ^ { n } , W \in \mathbb { R } ^ { m \times n }$ $b \in \mathbb { R } ^ { m }$ :

```txt
my_affine = nn.Linear(n, m)
```

将该仿射变换作用于Tensor类型的向量x:

```txt
y = my_affine(x)
```

## 激活函数作用于Tensor变量直接对Tensor类型的变量a作用ReLU激活函数:

```python
ReLU_a = torch.nn.functional.relu(a)
```

```txt
这里relu可以替换成其它常见的激活函数类型, 如hardtanh、elu、selu、leaky_relu、logsigmoid、softsign、softplus、tanh等.
```

```txt
激活函数作用于Tensor变量直接对Tensor类型的变量a作用ReLU激活函数:
ReLU_a = torch.nn.functional.relu(a)
这里relu可以替换成其它常见的激活函数类型, 如hardtanh、elu、selu、leaky_relu、logsigmoid、softsign、softplus、tanh等.
或者, 定义一个ReLU激活函数my_relu, 再对Tensor变量a作用:
my_relu = torch.nn.ReLU()
ReLU_a = my_relu(a)
这里ReLU()可以替换成其它常见的激活函数类型, 如Hardtanh()、Elu()、SELU()、Leaky_ReLU()、LogSigmoid()、Softsign()、Softplus()、Tanh()等.
```

## 用nn.Module定义一个神经网络类(class)

以下代码定义了一个从 $\mathbb { R } ^ { 2 }$ 到 R, 包含2个ReLU隐藏层且每层宽度为10的全连接神经网络类, 即

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\{\phi : \mathbb{R}^2 \to \mathbb{R} : \phi(x) = a^\top \sigma(W_2 \sigma(W_1 x + b_1) + b_2) + b\}$ 其中，$a \in \mathbb{R}^{10}$，$b \in \mathbb{R}$，$W_1 \in \mathbb{R}^{10 \times 2}$，$b_1 \in \mathbb{R}^{10}$，$W_2 \in \mathbb{R}^{10 \times 10}$，$b_2 \in \mathbb{R}^{10}$，$\sigma(\cdot)$ 为ReLU激活函数.
</div>

```python
import torch.nn as nn
import torch.nn.functional as F

class my_net_class(nn.Module):
    def __init__(self) -> None:
    super().__init__()
    self.linear1 = nn.Linear(2, 10)
    self.linear2 = nn.Linear(10, 10)
    self.linear3 = nn.Linear(10, 1)

    def forward(self, x):
    x = F.relu(self.linear1(x))
    x = F.relu(self.linear2(x))
    x = self.linear3(x)
    return x
```

## 创建一个神经网络类的实例以下代码创建了一个上述类 my net class 的实例, 即创建了一个具体的神经网络.

my\_net = my\_net\_class()

## 创建一个神经网络类的实例以下代码创建了一个上述类 my net class 的实例, 即创建了一个具体的神经网络.

```python
my_net = my_net_class()
```

## 用nn.Sequential快速创建一个神经网络以下代码也可以快速创建一个从 R<sup>2</sup> 到 R, 包含2个ReLU隐藏层且每层宽度为10的全连接神经网络.

```python
my_net = nn.Sequential(
    nn.Linaer(2,10),
    nn.ReLU(),
    nn.Linaer(10,10),
    nn.ReLU()
    nn.Linaer(10,1),
)
```

## 神经网络参数的初始化用<sub>torch.nn.init</sub> 下的子命令可以对神经网络参数进行初始化, 例如将每个参数按均匀分布 U(−0.1,0.1) 初始化:torch.nn.init.uniform\_(my\_net.linear1.weight, a=-0.1, b=0.1)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
将每个参数按正态分布  $\mathcal{N}(0.0,0.1^{2})$  初始化:
torch.nn.init.normal_(my_net.linear1.weight, mean=0.0, std=0.1)
</div>

```javascript
将每个参数初始化为常数 0.1:
torch.nn.init.constant_(my_net.linear1.weight, 0.1)
```

将每个参数按 Xavier 均匀分布进行初始化: torch.nn.init.xavier\_uniform\_(my\_net.linear1.weight)

将每个参数按 Xavier 正态分布进行初始化:torch.nn.init.xavier\_normal\_(my\_net.linear1.weight)

## 演示假设 d 维目标函数 f : $K : = [ - 1 , 1 ] ^ { d } \to \mathbb { R } , f ( x ) = 1 / ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + \cdot \cdot \cdot + x _ { d } ^ { 2 } + 1 )$ . 在 K上以均匀分布生成训练集/测试集, 并用全连接神经网络 $+ { \hat { \ell } } ^ { 2 }$ 损失函数进行回归.

1. 生成训练集/测试集;

2. 定义全连接神经网络;

3. 定义损失函数;

4. 用常见优化器进行训练并测试.

## 本章总结

▶ 回归模型、参数初始化、训练、测试、预测、正则化 (参考: 教材7.1, 7.2, 7.3, 7.8, 8.4)

▶ torch.nn 库的使用(参考: 官方文档 https://pytorch.org/docs/main/nn.html#)