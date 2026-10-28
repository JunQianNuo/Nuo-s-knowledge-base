---
raw_title: Chapter6
subject: Chapter6
source: Chapter6.pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter6/images/e771b16d615ba74e74070c52b016098d27a10db54187ae5c8ea199d41299c3f3.jpg)

六、分类模型

## 基本性质上一章提到, 用特定的机器学习模型去学习一个目标函数 f, 如果 f 的值域是连续分布的我们称这样的模型是回归模型相对应的如果的值域是离散分布的我们称这样的模型是分类模型.

## 基本性质上一章提到, 用特定的机器学习模型去学习一个目标函数 f, 如果 f 的值域是连续分布的我们称这样的模型是回归模型相对应的如果的值域是离散分布的我们称这样的模型是分类模型.

实际上在通常的分类模型中目标函数的值域只包含有限多个不同的值例如分类问题, 目标函数的取值只包含 0 和 1 两个数; 或图片分类问题, 一共有多少种可能的类别, 目标函数的值域就包含多少个不同的值.

## 与回归问题的差别出于分类问题中目标函数取值有限这一特殊性质, 针对分类问题的机器学习模型和上一章介绍的回归模型有着比较明显的差异

## 与回归问题的差别出于分类问题中目标函数取值有限这一特殊性质, 针对分类问题的机器学习模型和上一章介绍的回归模型有着比较明显的差异首先, 学习器并不直接用于逼近潜在的目标函数 $f ,$ 而是去逼近一个概率向量映射 ${ \hat { f } } .$ . 设所有类别的总数是 J, 则 $\hat { f }$ 接收一个特征(例如一张图片)作为输入, 然后输出一个 J 维概率向量

$$
[ p _ {1}, p _ {2}, \dots , p _ {J} ],
$$

满足

$$
p _ {i} \geq 0 \quad \forall i = 1, \ldots , J, \quad \sum_ {i = 1} ^ {J} p _ {i} = 1.
$$

## 与回归问题的差别出于分类问题中目标函数取值有限这一特殊性质, 针对分类问题的机器学习模型和上一章介绍的回归模型有着比较明显的差异首先, 学习器并不直接用于逼近潜在的目标函数 $f ,$ 而是去逼近一个概率向量映射 ${ \hat { f } } .$ . 设所有类别的总数是 J, 则 $\hat { f }$ 接收一个特征(例如一张图片)作为输入, 然后输出一个 J 维概率向量

$$
[ p _ {1}, p _ {2}, \dots , p _ {J} ],
$$

满足

$$
p _ {i} \geq 0 \quad \forall i = 1, \dots , J, \quad \sum_ {i = 1} ^ {J} p _ {i} = 1.
$$

这里, $p _ { i }$ 表示此特征属于第 i 个类别的概率. 因此, 若指标 $i _ { 0 }$ 满足 $p _ { i _ { 0 } } > p _ { i } \forall i \neq i _ { 0 }$ , 即$p _ { i _ { 0 } }$ 是所有 $p _ { i }$ 中唯一最大的, 则我们可以认为此特征属于第 $i _ { 0 }$ 个类别.

其次回归问题的损失函数根据不同场合可以有多种选择而分类问题的损失函数通常采用交叉熵损失函数 $l ( t _ { 1 } , t _ { 2 } ) = - t _ { 2 } \ln t _ { 1 }$ . 当 $t _ { 1 } , \ t _ { 2 }$ 为(列)向量时, 则交叉熵损失函数$l ( t _ { 1 } , t _ { 2 } ) = - t _ { 2 } ^ { \top } ( \ln t _ { 1 } )$ . (注意: 这里 $t _ { 1 }$ 表示学习器的输出, $t _ { 2 }$ 表示数据集的标签)

具体地说, 设分类问题的所有类别为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 现在, 假设某个数据特征 x 对应的标签为 $y = k \ ( k \in \mathcal { C } )$ , 即 x 所属的类别是第 k 类. 此时, 数据点 $( x , y )$ 对应的标签概率向量为 $\boldsymbol { e } _ { k } = [ 0 , \dots , 0 , 1 , 0 , \dots , 0 ] \in \mathbb { R } ^ { J }$ 即第个元素为其余元素为的维向量 (这种类型的向量也称作 one-hot 向量).

具体地说, 设分类问题的所有类别为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 现在, 假设某个数据特征 x 对应的标签为 $y = k \ ( k \in \mathcal { C } )$ , 即 x 所属的类别是第 k 类. 此时, 数据点 $( x , y )$ 对应的标签概率向量为 $\boldsymbol { e } _ { k } = [ 0 , \dots , 0 , 1 , 0 , \dots , 0 ] \in \mathbb { R } ^ { J }$ 即第个元素为其余元素为的维向量 (这种类型的向量也称作 one-hot 向量).

设所采用的学习器为 $\phi ,$ 其逼近的是一个概率向量. 因此, 对任意特征向量 $x ,$ 其输出$\phi ( x )$ 为一个维向量记作 $\boldsymbol { \phi } ( x ) = [ \phi _ { 1 } ( x ) , \phi _ { 2 } ( x ) , \dots , \phi _ { J } ( x ) ]$ 此时对于数据点$( x , y )$ 的交叉熵损失函数为

$$
l (\phi (x), e _ {k}) = - e _ {k} ^ {\top} (\ln \phi (x)) = - \ln \phi_ {k} (x).
$$

具体地说, 设分类问题的所有类别为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 现在, 假设某个数据特征 x 对应的标签为 $y = k \ ( k \in \mathcal { C } )$ , 即 x 所属的类别是第 k 类. 此时, 数据点 $( x , y )$ 对应的标签概率向量为 $\boldsymbol { e } _ { k } = [ 0 , \dots , 0 , 1 , 0 , \dots , 0 ] \in \mathbb { R } ^ { J }$ , 即第 k 个元素为 1, 其余元素为 0 的 J维向量 (这种类型的向量也称作 one-hot 向量).

设所采用的学习器为 $\phi ,$ 其逼近的是一个概率向量. 因此, 对任意特征向量 $x ,$ 其输出$\phi ( x )$ 为一个维向量记作 $\boldsymbol { \phi } ( x ) = [ \phi _ { 1 } ( x ) , \phi _ { 2 } ( x ) , \dots , \phi _ { J } ( x ) ]$ 此时对于数据点$( x , y )$ 的交叉熵损失函数为

$$
l (\phi (x), e _ {k}) = - e _ {k} ^ {\top} (\ln \phi (x)) = - \ln \phi_ {k} (x).
$$

由于 $- \ln ( \cdot )$ 是递减函数, 我们要降低该损失函数的值, 就需要增大 $\phi _ { k } ( x )$ . 考虑到$\phi _ { i } ( x ) \in [ 0 , 1 ] \forall i = 1 , . . . , J$ 我们的目标实际上是让 $\phi _ { k } ( x )$ 尽可能的接近 1 (相应的, 其余 $\phi _ { i } ( x )$ 就会接近 0). 所以, 降低交叉熵损失函数本质上就是在让 $\phi ( x )$ 尽量接近真正的标签概率向量 $e _ { k }$

## 一般的分类模型设分类问题的类别集合为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 给定数据集 $\{ ( x ^ { ( n ) } , v ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ , 其中$x ^ { ( n ) } \in \mathbb { R } ^ { d }$ 表示特征, $v ^ { ( n ) } = [ v _ { 1 } ^ { ( n ) } , \ldots , v _ { J } ^ { ( n ) } ] \in \mathbb { R } ^ { J }$ 表示 $x ^ { ( n ) }$ 对应的标签概率向量

## 一般的分类模型设分类问题的类别集合为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 给定数据集 $\{ ( x ^ { ( n ) } , v ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ , 其中$x ^ { ( n ) } \in \mathbb { R } ^ { d }$ 表示特征, $v ^ { ( n ) } = [ v _ { 1 } ^ { ( n ) } , \ldots , v _ { J } ^ { ( n ) } ] \in \mathbb { R } ^ { J }$ 表示 $x ^ { ( n ) }$ 对应的标签概率向量设 $\phi : \mathbb { R } ^ { d }  \mathbb { R } ^ { J }$ 是一个学习器且对任意 $x \in \mathbb { R } ^ { d } , \ \phi ( x ) = [ \phi _ { 1 } ( x ) , \ldots , \phi _ { J } ( x ) ]$ 是一个概率向量. 于是, 相应的分类模型为

$$
\begin{array}{c} \min _ {\phi} L [ \phi ] = - \frac {1}{N} \sum_ {n = 1} ^ {N} v ^ {(n) ^ {\top}} \ln \phi (x ^ {(n)}) \\ = - \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {J} v _ {j} ^ {(n)} \ln \phi_ {j} (x ^ {(n)}). \end{array}
$$

## 一般的分类模型设分类问题的类别集合为 $\mathcal { C } = \{ 1 , 2 , \dots , J \}$ . 给定数据集 $\{ ( x ^ { ( n ) } , v ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ , 其中$x ^ { ( n ) } \in \mathbb { R } ^ { d }$ 表示特征, $v ^ { ( n ) } = [ v _ { 1 } ^ { ( n ) } , \ldots , v _ { J } ^ { ( n ) } ] \in \mathbb { R } ^ { J }$ 表示 $x ^ { ( n ) }$ 对应的标签概率向量设 $\phi : \mathbb { R } ^ { d }  \mathbb { R } ^ { J }$ 是一个学习器, 且对任意 $x \in \mathbb { R } ^ { d } , \ \phi ( x ) = [ \phi _ { 1 } ( x ) , \ldots , \phi _ { J } ( x ) ]$ 是一个概率向量. 于是, 相应的分类模型为

$$
\begin{array}{c} \min _ {\phi} L [ \phi ] = - \frac {1}{N} \sum_ {n = 1} ^ {N} v ^ {(n) ^ {\top}} \ln \phi (x ^ {(n)}) \\ = - \frac {1}{N} \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {J} v _ {j} ^ {(n)} \ln \phi_ {j} (x ^ {(n)}). \end{array}
$$

如果 $v ^ { ( n ) }$ 是 one-hot 向量, 设 $v ^ { ( n ) } = e _ { y ^ { ( n ) } }$ , 其中 $y ^ { ( n ) } \in { \mathcal { C } }$ 是 $x ^ { ( n ) }$ 所属的类, 则上述模型可以改写为

$$
\min _ {\phi} L [ \phi ] = - \frac {1}{N} \sum_ {n = 1} ^ {N} \ln \phi_ {y ^ {(n)}} (x ^ {(n)}).
$$

## 为什么使用交叉熵?

给定特征 x, 则概率向量 $\phi ( x )$ 中最大元素所对应的类可视作 x 所属的类, 即“赢者通吃” 因此不同概率向量对应的分类结果可能是相同的例如当时概率向量和对应的结果都是第类假设真实的标签概率向量是[0,1,0], 则它们的交叉熵损失函数均为 $- \ln 0 . 6 = 0 . 5 1 0 8 .$

然而, 它们的 $\ell ^ { 2 }$ 损失函数则不相同, 分别为 $( 0 . 2 - 0 ) ^ { 2 } + ( 0 . 6 - 1 ) ^ { 2 } + ( 0 . 2 - 0 ) ^ { 2 } = 0 . 2 4$ 和 $( 0 - 0 ) ^ { 2 } + ( 0 . 6 - 1 ) ^ { 2 } + ( 0 . 4 - 0 ) ^ { 2 } = 0 . 3 \dot { 2 }$ 因此用 $\ell ^ { 2 }$ 损失函数来衡量并不合适

## Softmax函数为保证学习器 $\phi ( x )$ 的输出是一个概率向量, 我们可以引进 softmax 函数. 给定 $\boldsymbol { x } \in \mathbb { R } ^ { d }$ 定义

$$
\mathrm{softmax} _ {c} (x) = \mathrm{softmax} _ {c} ([ x _ {1} \dots x _ {d} ]) = \frac {[ e ^ {c x _ {1}} \cdots e ^ {c x _ {d}} ]}{\sum_ {i = 1} ^ {d} e ^ {c x _ {d}}},
$$

其中 $c > 0$ 是一个常数. 显然, $\operatorname { s o f t m a x } _ { c }$ 的输出是一个概率向量.

## Softmax神经网络用深度学习求解分类问题时, 作为学习器的深度神经网络通常用 softmax 函数为输出层的激活函数以保证最终输出的是一个概率向量

## Softmax神经网络用深度学习求解分类问题时作为学习器的深度神经网络通常用函数为输出层的激活函数, 以保证最终输出的是一个概率向量.

对 $\mathbb { R } ^ { d }$ 上的分类问题, 如果一共有 J 个类别, 则可以设立如下的 softmax 全连接神经网络作为学习器:

ϕ : $\mathbb { R } ^ { d } \to \mathbb { R } ^ { J } .$

$$
\phi (x) = \sigma^ {L + 1} \left(W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b ^ {L + 1}\right),
$$

其中 $\sigma ^ { L + 1 } ( \cdot )$ 为 softmax 激活函数.

## Softmax神经网络用深度学习求解分类问题时作为学习器的深度神经网络通常用函数为输出层的激活函数, 以保证最终输出的是一个概率向量.

对 $\mathbb { R } ^ { d }$ 上的分类问题, 如果一共有 J 个类别, 则可以设立如下的 softmax 全连接神经网络作为学习器:

$$
\begin{array}{l} \phi : \mathbb {R} ^ {d} \to \mathbb {R} ^ {J}, \\ \phi (x) = \sigma^ {L + 1} \bigg (W ^ {L + 1} \sigma^ {L} \Big (W ^ {L} \sigma^ {L - 1} \big (\ldots \sigma^ {1} (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1} \bigg), \end{array}
$$

其中 $\sigma ^ { L + 1 } ( \cdot )$ 为 softmax 激活函数.

当然, 也可以选用其它类型的神经网络甚至其它类型的带参函数作为学习器, 来求解分类问题只要保证输出端进行一次操作即可

## Softmax深度学习分类模型对有 J 个类别的分类问题, 设采用的学习器为 $\phi = \mathrm { s o f t m a x } _ { c } ( \psi ( x ) )$ ), 其中$\psi : \mathbb { R } ^ { d }  \mathbb { R } ^ { J }$ 是一个神经网络. 记 $\phi _ { j }$ 和 $\psi _ { j }$ 分别为 $\phi$ 和 $\psi$ 的第 $j$ 个输出分量.

## Softmax深度学习分类模型对有 J 个类别的分类问题, 设采用的学习器为 $\phi = \mathrm { s o f t m a x } _ { c } ( \psi ( x ) )$ ), 其中$\psi : \mathbb { R } ^ { d }  \mathbb { R } ^ { J }$ 是一个神经网络. 记 $\phi _ { j }$ 和 $\psi _ { j }$ 分别为 $\phi$ 和 $\psi$ 的第 $j$ 个输出分量.

给定数据集 $\{ ( x ^ { ( n ) } , y ^ { ( n ) } ) \} _ { n = 1 } ^ { N }$ , 其中 $y ^ { ( n ) } \in \{ 1 , 2 , \ldots , J \}$ 是 $x ^ { ( n ) }$ 所属的类, 于是相应的深度学习模型为

$$
\min _ {\phi} L [ \phi ] = - \frac {1}{N} \sum_ {n = 1} ^ {N} \ln \phi_ {y ^ {(n)}} (x ^ {(n)})
$$

$$
\text {或} \min _ {\psi} L [ \psi ] = - \frac {1}{N} \sum_ {n = 1} ^ {N} \ln \frac {e ^ {c \psi_ {y (n)} (x ^ {(n)})}}{\sum_ {j = 1} ^ {J} e ^ {c \psi_ {j} (x ^ {(n)})}}.
$$

## Softmax结合交叉熵的计算在上述损失函数中, 需要计算形如

$$
\ln {\frac {e ^ {t _ {j ^ {\prime}}}}{\sum_ {j = 1} ^ {J} e ^ {t _ {j}}}}, \quad j ^ {\prime} \in \{1, 2, \ldots , J \}
$$

的项在计算机的数值计算中当较大时 $e ^ { t }$ 可能是一个非常大的数从而造成数值溢出.

## Softmax结合交叉熵的计算在上述损失函数中, 需要计算形如

$$
\ln {\frac {e ^ {t _ {j ^ {\prime}}}}{\sum_ {j = 1} ^ {J} e ^ {t _ {j}}}}, \quad j ^ {\prime} \in \{1, 2, \ldots , J \}
$$

的项在计算机的数值计算中当较大时 $e ^ { t }$ 可能是一个非常大的数从而造成数值溢出.

为保持数值的稳定性, 可以将上式改写. 不妨设 $t _ { 1 } \leq t _ { 2 } \leq \dots \leq t _ { J }$ , 于是

$$
\begin{array}{c} \ln \frac {e ^ {t _ {j ^ {\prime}}}}{\sum_ {j = 1} ^ {J} e ^ {t _ {j}}} = \ln \frac {e ^ {t _ {j ^ {\prime}} - t _ {J}}}{\sum_ {j = 1} ^ {J} e ^ {t _ {j} - t _ {J}}} \\ = (t _ {j ^ {\prime}} - t _ {J}) - \ln \left(\sum_ {j = 1} ^ {J} e ^ {t _ {j} - t _ {J}}\right). \end{array}
$$

而对每个 $j ,$ 有 $t _ { j } - t _ { J } \leq 0$ . 因此计算 $e ^ { t _ { j } - t _ { J } }$ 不会造成数值溢出

## 测试和准确率对一个训练好的学习器 $\phi ,$ 给一个新的特征 $x ^ { \prime }$ , 它会输出关于 $x ^ { \prime }$ 的概率向量, 即

$$
\phi (x ^ {\prime}) = [ \phi_ {1} (x ^ {\prime}) \dots \phi_ {J} (x ^ {\prime}) ].
$$

于是,

$$
y ^ {\prime} = \arg \max _ {j} \phi_ {j} (x ^ {\prime})
$$

就是由 $\phi$ 预测的 $x ^ { \prime }$ 属于的类别.

## 测试和准确率对一个训练好的学习器 $\phi ,$ 给一个新的特征 $x ^ { \prime }$ , 它会输出关于 $x ^ { \prime }$ 的概率向量, 即

$$
\phi (x ^ {\prime}) = [ \phi_ {1} (x ^ {\prime}) \dots \phi_ {J} (x ^ {\prime}) ].
$$

于是,

$$
y ^ {\prime} = \arg \max _ {j} \phi_ {j} (x ^ {\prime})
$$

就是由 $\phi$ 预测的 $x ^ { \prime }$ 属于的类别.

对分类问题我们通常不用误差来衡量一个学习器的好坏而是用准确率给定一个测试数据集 $\{ ( \hat { x } ^ { ( n ) } , \hat { y } ^ { ( n ) } ) \}$ , 用学习器预测每一个 $\hat { x } ^ { ( n ) }$ 所属的类别, 并用真实标签 $\hat { y } ^ { ( n ) }$ 判断分类是否正确准确率即为预测正确的数量与数据点总数之比

```python
Softmax 函数
softmax 函数的 Pytorch 命令为 torch.nn.functional.softmax(), 或者变量自身 .Softmax()
对一个 Tensor 变量 a 进行 softmax 操作:
import torch
import torch.nn.functional as F

a = torch.Tensor([1.0, 2.0, 3.0])
softmax_a = F.softmax(a, dim=0)
softmax_a2 = a Wheatmax(dim=0)

(当 a 是二维 tensor 时, dim=0 表示逐列应用 softmax 函数, dim=1 表示逐行应用 softmax 函数)
```

## PyTorch 中的分类模型实现

## 交叉熵损失函数交叉熵损失函数的 Pytorch 命令为 <sub>torch.nn.functional.cross\_entropy</sub>()

对学习器的输出变量 p 和标签概率向量 q 进行交叉熵损失函数的计算, 并进行反向传播:

```txt
import torch.nn.functional as F
```

```julia
loss = F.cross_entropy(p, q)
loss.backward()
```

## 演示对二维平面上的点 $( x _ { 1 } , x _ { 2 } )$ 进行分类. 设真实的分类准则如下:

如果 $x _ { 1 } \geq 0 , x _ { 2 } \geq 0$ , 则属于类别 1;

如果 $x _ { 1 } < 0 , x _ { 2 } \geq 0$ , 则属于类别 2;

如果 $x _ { 1 } < 0 , x _ { 2 } < 0$ , 则属于类别 3;

如果 $x _ { 1 } \geq 0 , x _ { 2 } < 0$ , 则属于类别 4.

在 $R ^ { 2 }$ 上以标准正态分布 $\mathcal { N } ( 0 , I )$ 生成训练集/测试集, 并用Softmax全连接神经网络+交叉熵损失函数建立分类模型

1. 生成训练集/测试集;

2. 定义Softmax全连接神经网络;

3. 定义损失函数;

4. 用常见优化器进行训练并测试.

## 本章总结

▶ 概率向量、交叉熵损失函数、Softmax函数、Softmax神经网络、Softmax交叉熵稳定计算(参考: 教材)

▶ Pytorch 库有关分类模型命令的使用(参考: 官方文档 https://pytorch.org/docs/main/nn.html#)