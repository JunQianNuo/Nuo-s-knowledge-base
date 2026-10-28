---
raw_title: Chapter7
subject: Chapter7
source: Chapter7.pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/e771b16d615ba74e74070c52b016098d27a10db54187ae5c8ea199d41299c3f3.jpg)

## 七、卷积神经网络

## 基本介绍卷积神经网络(convolutional neural network)是一类特殊的神经网络. 它与全连接神经网络在架构上存在一些差别卷积神经网络最初来自于计算机视觉中的图像处理问题. 图像/图片通常是以矩阵的形式表示, 如一张分辨率 720×480 的灰度图片可以用一个规模为 720×480 的矩阵来表示因此, 最初的卷积神经网络, 其输入变量类型是矩阵(即2D张量). 相比之下, 全连接神经网络的输入变量类型是列向量(即1D张量).

而经简单推广后, 卷积神经网络可以接收任意维的张量作为输入变量卷积神经网络架构中有两类特殊的隐藏层: 卷积层和池化层.

## 互相关运算以2D情形为例. 首先, 给定一个卷积核(convolutional layer) $K = ( k _ { i j } )$ , 它是一个 $. s _ { 1 } \times s _ { 2 }$ 的矩阵. 再输入一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵 $X = ( x _ { i j } )$ (其中 $m _ { 1 } \geq s _ { 1 } , m _ { 2 } \geq s _ { 2 } )$ 于是, 可以将 X 在卷积核 K 下作互相关运算(cross-correlation)

$$
Y = X * K.
$$

这里的输出 $Y = ( y _ { i j } )$ 是一个 $( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的矩阵, 称为特征映射或特征图(feature map), 其每个元素按如下公式计算:

$$
y _ {p q} = \sum_ {i = 1} ^ {s _ {1}} \sum_ {j = 1} ^ {s _ {2}} x _ {p + i - 1, q + j - 1} k _ {i j},
$$

$$
1 \leq p \leq m _ {1} - s _ {1} + 1, \quad 1 \leq q \leq m _ {2} - s _ {2} + 1.
$$

图 1. 一个 3 × 3 的卷积核作用在一个 $^ \textrm { \scriptsize 5 } \times 5$ 的矩阵上, 得到一个 3 × 3 的特征映射

## 互相关运算将 $Y = X * K$ 写成如下的逐元素形式

$$
\begin{array}{c} \left[ \begin{array}{c c c c} x _ {1 1} & x _ {1 2} & \dots & x _ {1, m _ {2}} \\ x _ {2 1} & x _ {2 2} & \dots & x _ {2, m _ {2}} \\ \vdots & \vdots & \ddots & \vdots \\ x _ {m _ {1}, 1} & x _ {m _ {1}, 2} & \dots & x _ {m _ {1}, m _ {2}} \end{array} \right] * \left[ \begin{array}{c c c c} k _ {1 1} & k _ {1 2} & \dots & k _ {1, s _ {2}} \\ k _ {2 1} & k _ {2 2} & \dots & k _ {2, s _ {2}} \\ \vdots & \vdots & \ddots & \vdots \\ k _ {s _ {1}, 1} & k _ {s _ {1}, 2} & \dots & k _ {s _ {1}, s _ {2}} \end{array} \right] \\ = \left[ \begin{array}{c c c c} y _ {1 1} & y _ {1 2} & \dots & y _ {1, m _ {2} - s _ {2} + 1} \\ y _ {2 1} & y _ {2 2} & \dots & y _ {2, m _ {2} - s _ {2} + 1} \\ \vdots & \vdots & \ddots & \vdots \\ y _ {m _ {1} - s _ {1} + 1, 1} & y _ {s _ {1}, 2} & \dots & y _ {m _ {1} - s _ {1} + 1, m _ {2} - s _ {2} + 1} \end{array} \right]. \end{array}
$$

对于 Y 的任一元素 $y _ { p q }$ , 它等于矩阵

$$
X _ {p q} := \left[ \begin{array}{c c c} x _ {p q} & \dots & x _ {p, q + s _ {2} - 1} \\ \vdots & \ddots & \vdots \\ x _ {p + s _ {1} - 1, q} & \dots & x _ {p + s _ {1} - 1, q + s _ {2} - 1} \end{array} \right]
$$

和 K 逐元素相乘后再所有元素相加得到. 因此, 矩阵 $X _ { p q }$ 也称作 $y _ { p q }$ 的接收域或感受野(receptive field).

## 互相关运算互相关运算实际上是一个线性运算, 因此可以用矩阵-向量乘法进行表示.例1: 设

$$
X = \left[ \begin{array}{c c c} 3 & 2 & - 2 \\ 1 & 0 & - 1 \\ 2 & - 1 & 4 \end{array} \right], K = \left[ \begin{array}{c c} 1 & - 2 \\ - 1 & 3 \end{array} \right],
$$

则

$$
Y = X * K = \left[ \begin{array}{c c} - 2 & 3 \\ - 4 & 1 5 \end{array} \right].
$$

## 互相关运算互相关运算实际上是一个线性运算因此可以用矩阵向量乘法进行表示例1: 设

$$
X = \left[ \begin{array}{c c c} 3 & 2 & - 2 \\ 1 & 0 & - 1 \\ 2 & - 1 & 4 \end{array} \right], K = \left[ \begin{array}{c c} 1 & - 2 \\ - 1 & 3 \end{array} \right],
$$

则

$$
Y = X * K = \left[ \begin{array}{c c} - 2 & 3 \\ - 4 & 1 5 \end{array} \right].
$$

若将 X 和 Y 分别拉长为列向量, 则满足 $\mathsf { v e c } ( Y ) = \hat { K } \mathsf { v e c } ( X )$ , 其中

$$
\operatorname{vec} (Y) = \left[ \begin{array}{c} - 2 \\ 3 \\ - 4 \\ 1 5 \end{array} \right],   \hat {K} = \left[ \begin{array}{c c c c c c c c c} 1 & - 2 & 0 & - 1 & 3 & 0 & 0 & 0 & 0 \\ 0 & 1 & - 2 & 0 & - 1 & 3 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & - 2 & 0 & - 1 & 3 & 0 \\ 0 & 0 & 0 & 0 & 1 & - 2 & 0 & - 1 & 3 \end{array} \right],   \operatorname{vec} (X) = \left[ \begin{array}{c} 3 \\ 2 \\ - 2 \\ 1 \\ 0 \\ - 1 \\ 2 \\ - 1 \\ 4 \end{array} \right]
$$

这里, $\hat { K }$ 是由卷积核 K 导出的一个矩阵.

## 互相关运算的性质首先, 可以看到 $\hat { K }$ 是一个稀疏矩阵, 即它的大部分元素都是 0. (当 X 的规模相较 K 的规模更大时, $\hat { K }$ 的稀疏度会更高). 这反映了互相关运算的一个特性: 稀疏交互(sparseinteraction).

## 互相关运算的性质首先, 可以看到 $\hat { K }$ 是一个稀疏矩阵, 即它的大部分元素都是 0. (当 X 的规模相较 K 的规模更大时, $\hat { K }$ 的稀疏度会更高). 这反映了互相关运算的一个特性: 稀疏交互(sparseinteraction).

实际上如果我们用神经网络图示法来表示互相关运算则会发现大部分输入神经元和输出神经元之间并不存在连接. 例如, 例1可以表示成下图:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/61cc35307f0db37467efd4a4a657c6d763105f7bf8a253b75d3bbda36243e990.jpg)  
图 2. 互相关运算示意图(红色: 权重为 1; 绿色: 权重为 −2; 黄色: 权重为 −1; 蓝色: 权重为 3).

## 互相关运算的性质其次, 可以看到 Kˆ 每一行的非零元素都是相同的, 即 K 中的元素 1、−2、−1、3. 这反映了互相关运算的另一个特性: 参数共享(parameter sharing).

在图2中可以看到, 同一种颜色的所有连接, 共享同一个权重.

## 互相关运算的性质其次, 可以看到 $\hat { K }$ 每一行的非零元素都是相同的, 即 K 中的元素 1、−2、−1、3. 这反映了互相关运算的另一个特性: 参数共享(parameter sharing).

在图2中可以看到, 同一种颜色的所有连接, 共享同一个权重.

另外, 互相关运算还具有等变表示(equivariant representations)的性质. 以平移等变为例,

1. 一方面, 将输入矩阵 X 的每个元素向右平移 $n \left( n \leq m _ { 2 } - s _ { 2 } \right)$ )个单位, 得到 $X ^ { \prime }$ (此时空出的前 n 列可用 0 填充). 然后作互相关运算, 得到 $X ^ { \prime } * K$

2. 另一方面, 先对 X 作互相关运算, 得到 $X * K$ , 再将其每个元素向右平移 n 个单位, 得到 $( X * K ) ^ { \prime }$

显然, $X ^ { \prime } * K$ 与 $( X * K ) ^ { \prime }$ 从第 $n + 1$ 列开始, 右边部分是相等的.

## 互相关运算的意义从本质上说, 互相关运算是将一个表示某种特征的卷积核 K 在输入变量 X (如一张图片) 上滑动, 寻找 X 上带有该特征的部分. 通过 K 与 X 的局部区域作内积, 当内积值较大时意味着的该区域与的特征较相似

## 填充上述互相关运算将一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵转化为 $( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的特征映射矩阵即矩阵的行数和列数分别减小了 $s _ { 1 } - 1$ 和 $s _ { 2 } - 1$ 而在卷积神经网络中可能会复合多次互相关运算这将导致输出矩阵的规模不断减小从而丢失较多信息

## 填充上述互相关运算将一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵转化为 $( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的特征映射矩阵即矩阵的行数和列数分别减小了 $s _ { 1 } - 1$ 和 $s _ { 2 } - 1$ 而在卷积神经网络中可能会复合多次互相关运算这将导致输出矩阵的规模不断减小从而丢失较多信息为避免这种情况, 可以在每次进行互相关运算前, 对输入矩阵进行一定填充. 例如, 在例1中, 可以将 X 的左侧和上方各增加一列 0 和一行 0, 得到一个新矩阵 $\tilde { X }$ , 即

$$
\tilde {X} = \left[ \begin{array}{c c c c} 0 & 0 & 0 & 0 \\ 0 & 3 & 2 & - 2 \\ 0 & 1 & 0 & - 1 \\ 0 & 2 & - 1 & 4 \end{array} \right],
$$

然后再与 K 作互相关运算, 得到

$$
\tilde {X} * K = \left[ \begin{array}{c c c} 9 & 3 & - 8 \\ - 3 & - 2 & 3 \\ 4 & - 4 & 1 5 \end{array} \right].
$$

此时特征映射 $\tilde { X } * K$ 与原始输入矩阵 X 具有相同的规模.

## 填充上述互相关运算将一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵转化为 $( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的特征映射矩阵即矩阵的行数和列数分别减小了 $s _ { 1 } - 1$ 和 $s _ { 2 } - 1$ 而在卷积神经网络中可能会复合多次互相关运算这将导致输出矩阵的规模不断减小从而丢失较多信息为避免这种情况, 可以在每次进行互相关运算前, 对输入矩阵进行一定填充. 例如, 在例1中, 可以将 X 的左侧和上方各增加一列 0 和一行 0, 得到一个新矩阵 $\tilde { X }$ , 即

$$
\tilde {X} = \left[ \begin{array}{c c c c} 0 & 0 & 0 & 0 \\ 0 & 3 & 2 & - 2 \\ 0 & 1 & 0 & - 1 \\ 0 & 2 & - 1 & 4 \end{array} \right],
$$

然后再与 K 作互相关运算, 得到

$$
\tilde {X} * K = \left[ \begin{array}{c c c} 9 & 3 & - 8 \\ - 3 & - 2 & 3 \\ 4 & - 4 & 1 5 \end{array} \right].
$$

此时特征映射 $\tilde { X } * K$ 与原始输入矩阵 X 具有相同的规模.

一般地, 可以在矩阵 X 的上下左右各个方向增加新的行或列, 从而使互相关运算后的特征映射保持较大的规模. 这种对 X 的操作称为填充(padding).

## 步幅在互相关运算中, 卷积核矩阵 K 每次从输入矩阵 X 的左上方开始, 从左往右、从上往下依次滑动. 我们将每次滑动的行数或列数称为步幅(stride).

## 步幅在互相关运算中, 卷积核矩阵 K 每次从输入矩阵 X 的左上方开始, 从左往右、从上往下依次滑动. 我们将每次滑动的行数或列数称为步幅(stride).

在先前例子中, 卷积核横向和纵向移动的步幅均为 1. 而一般地, 我们可以根据需要设置更大的步幅例如设

$$
X = \left[ \begin{array}{c c c c} 1 & 3 & 2 & - 2 \\ 0 & 1 & 0 & - 1 \\ - 2 & 2 & - 1 & 4 \\ - 1 & 0 & 1 & 2 \end{array} \right], K = \left[ \begin{array}{c c} 1 & - 2 \\ - 1 & 3 \end{array} \right],
$$

则当横向和纵向步幅均为 2 时,

$$
X * K = \left[ \begin{array}{c c} - 2 & 3 \\ - 5 & - 4 \end{array} \right].
$$

## 卷积层设对于某个神经网络如果它的一个隐藏层执行的是一次互相关运算可能再加上一个标量偏置), 再进行一次激活函数操作, 则这样的隐藏层称为卷积层.

## 卷积层设对于某个神经网络如果它的一个隐藏层执行的是一次互相关运算可能再加上一个标量偏置), 再进行一次激活函数操作, 则这样的隐藏层称为卷积层.

设神经网络的第 l 层是卷积核为 K, 标量偏置为 b 的卷积层. 如果网络的第 l−1 层传递给第 l 层一个矩阵 $X _ { l }$ , 则第 l 层将执行如下操作

$$
X _ {l + 1} = \sigma ((X _ {l} * K) + b),
$$

其中, $X _ { l + 1 }$ 是第 l 层的输出; $\sigma ( \cdot )$ 是某个激活函数; “+” 表示矩阵的每个元素均加上 b.对一个卷积层, 它的卷积核 K 的每个元素以及标量偏置 b 是可训练的参数.

## 池化操作池化(pooling)操作是将某一位置附近的总体统计特征作为该位置的值进行输出. 池化操作的方式与互相关运算类似, 即用一个“核矩阵”从输入矩阵的左上角开始, 从左往右、从上往下平移, 每次计算一个输出矩阵的元素.

## 池化操作池化(pooling)操作是将某一位置附近的总体统计特征作为该位置的值进行输出. 池化操作的方式与互相关运算类似, 即用一个“核矩阵”从输入矩阵的左上角开始, 从左往右、从上往下平移每次计算一个输出矩阵的元素以2D为例, 对一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵 X 进行 $s _ { 1 } \times s _ { 2 }$ 最大池化操作, 将输出一个$( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的矩阵 $Y = ( y _ { p q } )$ 其每个元素按如下公式计算

$$
y _ {p q} = \max \{x _ {p + i - 1, q + j - 1} \} _ {i = 1, \ldots , s _ {1}} ^ {j = 1, \ldots , s _ {2}},
$$

## 池化操作池化(pooling)操作是将某一位置附近的总体统计特征作为该位置的值进行输出. 池化操作的方式与互相关运算类似, 即用一个“核矩阵”从输入矩阵的左上角开始, 从左往右、从上往下平移每次计算一个输出矩阵的元素以2D为例, 对一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵 X 进行 $s _ { 1 } \times s _ { 2 }$ 最大池化操作, 将输出一个$( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的矩阵 $Y = ( y _ { p q } )$ 其每个元素按如下公式计算

$$
y _ {p q} = \max \{x _ {p + i - 1, q + j - 1} \} _ {i = 1, \ldots , s _ {1}} ^ {j = 1, \ldots , s _ {2}},
$$

类似地, 可定义平均池化操作:

$$
y _ {p q} = \frac {1}{s _ {1} s _ {2}} \sum_ {i = 1} ^ {s _ {1}} \sum_ {j = 1} ^ {s _ {2}} x _ {p + i - 1, q + j - 1},
$$

显然, 平均池化操作等价于用每个元素均为 $\frac { 1 } { s _ { 1 } s _ { 2 } }$ 的卷积核进行互相关运算.

## 池化操作池化(pooling)操作是将某一位置附近的总体统计特征作为该位置的值进行输出. 池化操作的方式与互相关运算类似, 即用一个“核矩阵”从输入矩阵的左上角开始, 从左往右、从上往下平移每次计算一个输出矩阵的元素以2D为例, 对一个 $m _ { 1 } \times m _ { 2 }$ 的矩阵 X 进行 $s _ { 1 } \times s _ { 2 }$ 最大池化操作, 将输出一个$( m _ { 1 } - s _ { 1 } + 1 ) \times ( m _ { 2 } - s _ { 2 } + 1 )$ 的矩阵 $Y = ( y _ { p q } )$ 其每个元素按如下公式计算

$$
y _ {p q} = \max \{x _ {p + i - 1, q + j - 1} \} _ {i = 1, \ldots , s _ {1}} ^ {j = 1, \ldots , s _ {2}},
$$

类似地, 可定义平均池化操作:

$$
y _ {p q} = \frac {1}{s _ {1} s _ {2}} \sum_ {i = 1} ^ {s _ {1}} \sum_ {j = 1} ^ {s _ {2}} x _ {p + i - 1, q + j - 1},
$$

显然, 平均池化操作等价于用每个元素均为 $\frac { 1 } { s _ { 1 } s _ { 2 } }$ 的卷积核进行互相关运算.

同样地也可以定义池化操作在各个方向上的步幅上面两式中横向和纵横步幅均为

## 池化操作图 3. 一个 2 × 2 的池化核以步幅 2 作用在一个 4 × 4 的矩阵上, 得到一个 2 × 2 的输出矩阵. 左为最大池化, 右为平均池化.

## 池化操作对少量平移的不变性当池化操作作用于原始的输入矩阵 X 时, 相当于对 X 进行降采样. 如果 X 表示一张图片则相当于对进行简单的图片压缩但一般情况下, 我们不直接对 X 作池化操作, 而是先进行一次互相关运算后再进行池化操作. 此时, 池化操作对 X 的少量平移具有输出的稳定性(在不严格的情况下, 也可称为不变性).

例如:

$$
X = \left[ \begin{array}{c c c c c c} 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right], \quad K = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right], \quad X * K = \left[ \begin{array}{c c c c} 6 & 4 & 3 & 2 \\ 4 & 4 & 4 & 2 \\ 3 & 4 & 3 & 0 \\ 2 & 2 & 0 & 0 \end{array} \right].
$$

此时对 ∗ 作 × 步幅为的最大池化得到 $\left[ { \begin{array} { l l } { 6 } & { 4 } \\ { 4 } & { 3 } \end{array} } \right]$

例如:

$$
X = \left[ \begin{array}{c c c c c c} 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 0 & 0 & 0 \\ 1 & 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right], \quad K = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right], \quad X * K = \left[ \begin{array}{c c c c} 6 & 4 & 3 & 2 \\ 4 & 4 & 4 & 2 \\ 3 & 4 & 3 & 0 \\ 2 & 2 & 0 & 0 \end{array} \right].
$$

此时, 对 $X * K$ 作 2×2 步幅为 2 的最大池化, 得到 $\left[ { \begin{array} { l l } { 6 } & { 4 } \\ { 4 } & { 3 } \end{array} } \right]$ . 假如将 X 中的元素向下和向右各平移一个单位, 得到

0 0 0 0 0 0 0 0 0 1 0 0 $X ^ { \prime } * K = { \left[ \begin{array} { l l l l } { 1 } & { 3 } & { 3 } & { 1 } \\ { 3 } & { 6 } & { 4 } & { 3 } \\ { 3 } & { 4 } & { 4 } & { 4 } \\ { 1 } & { 3 } & { 4 } & { 3 } \end{array} \right] }$ 0 0 1 1 0 0 ′ 则 0 1 1 1 1 1 , 0 0 0 1 1 0 <sub>0</sub> 0 0 1 0 0

此时, 对 $X ^ { \prime } * K$ 作 2×2 步幅为 2 的最大池化, 得到 $\left[ { \begin{array} { l l } { 6 } & { 4 } \\ { 4 } & { 4 } \end{array} } \right]$ , 与平移前的结果是几乎相同的.

## 池化层与卷积层类似对于神经网络的一个隐藏层可以对输入矩阵执行一次池化操作输出的结果传递到下一层这样的神经网络隐藏层称为池化层池化层一般不设置激活函数然而, 池化操作一般是既定的, 通常不包含可变参数, 因此在训练过程中池化层始终保持不变.

## 多通道输入/输出有时候卷积层的输入不仅仅有一个矩阵而是有多个规模相同的矩阵比如一张彩色图片, 它有RGB(红、绿、蓝)三个颜色通道, 因此对应三个相同规模的矩阵.

除了输入矩阵的长和宽外, 我们可以将矩阵的数量也视作一个维度(如彩色图片的3), 称为通道(channel).

## 多通道输入/输出有时候卷积层的输入不仅仅有一个矩阵而是有多个规模相同的矩阵比如一张彩色图片, 它有RGB(红、绿、蓝)三个颜色通道, 因此对应三个相同规模的矩阵.

除了输入矩阵的长和宽外, 我们可以将矩阵的数量也视作一个维度(如彩色图片的3), 称为通道(channel).

类似地, 卷积层的输出也可以不止一个矩阵, 而是多个规模相同的矩阵, 即多通道输出多通道输入/输出的计算方式并没有约定的固定公式, 而是十分灵活的, 因具体应用而异.这里仅举一个例子作为演示当输入的通道数为时我们可以在卷积层定义个规模相同的卷积核. 此时的多通道互相关运算, 可以定义为将每个输入矩阵与对应的卷积核作互相关运算最后将得到的多个矩阵逐元素相加例如: 设一组双通道的输入为

$$
X _ {1} = \left[ \begin{array}{c c c} 1 & 2 & 3 \\ 2 & 1 & 1 \\ 1 & 3 & 1 \end{array} \right], X _ {2} = \left[ \begin{array}{c c c} 2 & 2 & 1 \\ 0 & 1 & 2 \\ 3 & 2 & 1 \end{array} \right].
$$

而卷积层的核为

$$
K _ {1} = \left[ \begin{array}{c c} 0 & 1 \\ 1 & 2 \end{array} \right], K _ {2} = \left[ \begin{array}{c c} 3 & 1 \\ 1 & 0 \end{array} \right].
$$

则双通道的互相关运算可以如下进行:

$$
\{X _ {1}, X _ {2} \} * \{K _ {1}, K _ {2} \} = X _ {1} * K _ {1} + X _ {2} * K _ {2} = \left[ \begin{array}{c c} 6 & 6 \\ 8 & 6 \end{array} \right] + \left[ \begin{array}{c c} 8 & 8 \\ 4 & 7 \end{array} \right] = \left[ \begin{array}{c c} 1 4 & 1 4 \\ 1 2 & 1 3 \end{array} \right].
$$

对多通道输入, 我们也可以将多个输入矩阵及对应的多个卷积核视为一个三维输入张量及一个三维卷积张量设输入矩阵的规模为 $m _ { 1 } \times m _ { 2 }$ 通道数为 $^ { c , }$ 则所有这些输入矩阵可以视为一个规模为 $c \times m _ { 1 } \times m _ { 2 }$ 的三维输入张量. 同样地, 设每个卷积核矩阵的规模为 $s _ { 1 } \times s _ { 2 }$ , 则所有这些卷积核矩阵可以视为一个规模为 $c \times s _ { 1 } \times s _ { 2 }$ 的三维卷积核张量.

对多通道输入, 我们也可以将多个输入矩阵及对应的多个卷积核视为一个三维输入张量及一个三维卷积张量设输入矩阵的规模为 $m _ { 1 } \times m _ { 2 }$ 通道数为 $^ { c , }$ 则所有这些输入矩阵可以视为一个规模为 $c \times m _ { 1 } \times m _ { 2 }$ 的三维输入张量. 同样地, 设每个卷积核矩阵的规模为 $s _ { 1 } \times s _ { 2 }$ , 则所有这些卷积核矩阵可以视为一个规模为 $c \times s _ { 1 } \times s _ { 2 }$ 的三维卷积核张量.

在上例中, 我们可以视输入张量为 $X = \{ X _ { 1 } , X _ { 2 } \}$ , 其规模为 $2 \times 3 \times 3$ ; 卷积核张量为$K = \{ K _ { 1 } , K _ { 2 } \}$ , 其规模为 $2 \times 2 \times 2$ . 于是,

$$
X * K = \left[ \begin{array}{c c} 1 4 & 1 4 \\ 1 2 & 1 3 \end{array} \right].
$$

类似地我们也可以为多通道输出定义其它的计算方式对多通道输入, 我们也可以将多个输入矩阵及对应的多个卷积核视为一个三维输入张量及一个三维卷积张量设输入矩阵的规模为 $m _ { 1 } \times m _ { 2 }$ 通道数为 $^ { c , }$ 则所有这些输入矩阵可以视为一个规模为 $c \times m _ { 1 } \times m _ { 2 }$ 的三维输入张量. 同样地, 设每个卷积核矩阵的规模为 $s _ { 1 } \times s _ { 2 }$ , 则所有这些卷积核矩阵可以视为一个规模为 $c \times s _ { 1 } \times s _ { 2 }$ 的三维卷积核张量.

在上例中, 我们可以视输入张量为 $X = \{ X _ { 1 } , X _ { 2 } \}$ , 其规模为 $2 \times 3 \times 3$ ; 卷积核张量为$K = \{ K _ { 1 } , K _ { 2 } \}$ , 其规模为 $2 \times 2 \times 2$ . 于是,

$$
X * K = \left[ \begin{array}{c c} 1 4 & 1 4 \\ 1 2 & 1 3 \end{array} \right].
$$

类似地我们也可以为多通道输出定义其它的计算方式在实际计算中, 若想增加卷积层的自由参数, 无法通过不断增大卷积核的尺寸来实现. 因为卷积核的尺寸不能超过输入张量的尺寸, 而且卷积核一旦过大也会失去其本身“寻找局部特征”这一功能.

对多通道输入, 我们也可以将多个输入矩阵及对应的多个卷积核视为一个三维输入张量及一个三维卷积张量设输入矩阵的规模为 $m _ { 1 } \times m _ { 2 }$ 通道数为 $^ { c , }$ 则所有这些输入矩阵可以视为一个规模为 $c \times m _ { 1 } \times m _ { 2 }$ 的三维输入张量. 同样地, 设每个卷积核矩阵的规模为 $s _ { 1 } \times s _ { 2 }$ , 则所有这些卷积核矩阵可以视为一个规模为 $c \times s _ { 1 } \times s _ { 2 }$ 的三维卷积核张量.

在上例中, 我们可以视输入张量为 $X = \{ X _ { 1 } , X _ { 2 } \}$ , 其规模为 $2 \times 3 \times 3$ ; 卷积核张量为$K = \{ K _ { 1 } , K _ { 2 } \}$ , 其规模为 $2 \times 2 \times 2$ . 于是,

$$
X * K = \left[ \begin{array}{c c} 1 4 & 1 4 \\ 1 2 & 1 3 \end{array} \right].
$$

类似地我们也可以为多通道输出定义其它的计算方式在实际计算中, 若想增加卷积层的自由参数, 无法通过不断增大卷积核的尺寸来实现. 因为卷积核的尺寸不能超过输入张量的尺寸, 而且卷积核一旦过大也会失去其本身“寻找局部特征”这一功能.

因此, 对卷积层, 我们一般通过增加通道的数量来增加自由参数 (相比之下, 对全连接层我们一般通过增大宽度来增加自由参数)

## 卷积神经网络的架构含有卷积层的神经网络都可以称为卷积神经网络(convolutional neural network/CNN).经典卷积神经网络的架构包含两个模块: 卷积层块和全连接层块.

## 卷积神经网络的架构含有卷积层的神经网络都可以称为卷积神经网络(convolutional neural network/CNN).经典卷积神经网络的架构包含两个模块: 卷积层块和全连接层块.

第一步由卷积层块接收原始的多个通道输入矩阵并重复进行若干轮卷积层和池化层的操作. 第二步, 将卷积层块输出的结果(一般仍然是多个通道的矩阵)整体拉长成一个列向量并用若干个全连接层进行操作最终输出一个实数或向量

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/78b3fbae8729316be99dc542a2a9b24aa56150fcf1117f5a03add60da6af18ae.jpg)  
图 4. 1990年由Yann LeCun等人提出的卷积神经网络LeNet-5. 用于识别手写体或打印体的字符

## 高维推广互相关运算不仅仅局限在矩阵(即二维张量)的计算上, 还可以向更高维的张量计算进行推广. 例如, 三维互相关运算可以按如下示意图进行

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/11d561bda6236588084963056f0c4d3c8e476541cf7420bc045cedac1b995831.jpg)

图 5. 三维互相关运算示意图(三维卷积核从输入张量的顶角开始, 从上往下、从左往右、从前往后依次滑动, 每经过一个位置便逐元素相乘后再相加得到一个值作为输出张量的一个元素

## 卷积网络接收数据类型

<table><tr><td></td><td>单通道</td><td>多通道</td></tr><tr><td>一维</td><td>音频波形</td><td>骨架动画(每一个通道表示一个关节的信息)</td></tr><tr><td>二维</td><td>灰度图像</td><td>彩色图像(每一个通道表示RGB中的一个颜色)</td></tr><tr><td>三维</td><td>体积数据,如CT扫描后的立体图像</td><td>彩色视频(三维分别是高度、宽度、时间轴;每一个通道表示RGB中的一个颜色)</td></tr></table>

表用于卷积网络的不同数据类型实例

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/e38920b2e1a3c14735ab14e0f93c9465019d284908842eb5fc46cf63412458b6.jpg)  
图音频波形

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/62060ab8eba80bc1737f0819a86d81a23390af9614dc973f064a989200d85f0a.jpg)  
图 7. 骨架动画

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter7/images/d548837f50828ad3b29edf29958e296d1e8b52c87316e150123c9b54c65afcfd.jpg)  
图 8. 三维体积图像

## PyTorch 中的CNN实现

## 卷积层

▶ 定义1维卷积层 <sub>C 1</sub> ( )

▶ 定义2维卷积层 <sub>torch.nn.Conv2d</sub>(<sub>...</sub>)

▶ 定义3维卷积层 <sub>torch.nn.Conv3d</sub>(<sub>...</sub>)

## Conv2d

class torch.nn.Conv2d(in\_channels, out\_channels, kernel\_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding\_mode='zeros', device=None, dtype=None [source]

Applies a 2D convolution over an input signal composed of several input planes

In the simplest case, the output value of the layer with input size $( N , C _ { \mathrm { i n } } , H , W )$ and output $( N , C _ { \mathrm { o u t } } , H _ { \mathrm { o u t } } , W _ { \mathrm { o u t } } )$ can be precisely described as

$$
\operatorname{out} \left(N _ {i}, C _ {\text { out } _ {j}}\right) = \operatorname{bias} \left(C _ {\text { out } _ {j}}\right) + \sum_ {k = 0} ^ {C _ {\text { in }} - 1} \operatorname{weight} \left(C _ {\text { out } _ {j}}, k\right) \star \operatorname{input} \left(N _ {i}, k\right)
$$

where \* is the valid 2D cross-correlation operator, N is a batch size, C denotes a number of channels, H is a heigh of input planes in pixels, and W is width in pixels

图维卷积层命令的具体用法

## 池化层

▶ 定义1维最大池化层 ( )

▶ 定义2维最大池化层 <sub>torch.nn.MaxPool2d</sub>(<sub>...</sub>)

▶ 定义3维最大池化层 <sub>torch.nn.MaxPool3d</sub>(<sub>...</sub>)

▶ 定义1维平均池化层 <sub>torch.nn.AvgPool1d</sub>(<sub>...</sub>)

▶ 定义2维平均池化层 <sub>torch.nn.AvgPool2d</sub>(<sub>...</sub>)

▶ 定义3维平均池化层 <sub>torch.nn.AvgPool3d</sub>(<sub>...</sub>)

## AvgPool2d

class torch.nn.AvgPool2d(kernel\_size, stride=None, padding=0, ceil\_mode=False count include pad=True, divisor override=None

[source]

Applies a 2D average pooling over an input signal composed of several input planes

In the simplest case, the output value of the layer with input size $( N , C , H , W )$ , output $( N , C , H _ { o u t } , W _ { o u t } )$ ) and kernel\_size (kH, kW) can be precisely described as

$$
\operatorname{out} \left(N _ {i}, C _ {j}, h, w\right) = \frac {1}{k H * k W} \sum_ {m = 0} ^ {k H - 1} \sum_ {n = 0} ^ {k W - 1} \text { input } \left(N _ {i}, C _ {j}, \text { stride } [ 0 ] \times h + m, \text { stride } [ 1 ] \times w + n\right)
$$

If padding is non-zero, then the input is implicitly zero-padded on both sides for padding number of points

图 10. 2维平均池化层命令AvgPool2d的具体用法

## 演示: 任务一对规模为 $8 \times 8$ 的实矩阵按是否对称进行分类. 具体如下

▶ 类别1: 对称矩阵 $A + A ^ { \top }$ , 其中 A 的每个元素属于 [−1,1];

▶ 类别2: 一般矩阵, 其中每个元素属于 [−1,1].

1. 生成训练集/测试集(用rand随机生成矩阵的元素):

2. 定义如下卷积神经网络:

$$
1 @ 8 \times 8 \xrightarrow {\text {填充} + 3 \times 3 \text {卷积核} + \mathrm{ReLU}} 1 0 @ 8 \times 8 \xrightarrow {\text {平均池化(核} 2 \times 2 , \text {步幅} 2)}
$$

$$
1 0 @ 4 \times 4 \xrightarrow {\text {填充} + 2 \times 2 \text {卷积核} + \mathrm{ReLU}} 1 0 @ 4 \times 4 \xrightarrow {\text {拉长成列向量}}
$$

$$
1 6 0 \times 1 \xrightarrow {\text {ReLU全连接层}} 2 0 \times 1 \xrightarrow {\text {softmax全连接层}} 2 \times 1.
$$

定义标签概率向量和交叉熵损失函数

4. 用常见优化器进行训练并测试.

## 演示: 任务二对规模为 8×8 的实对称矩阵, 按其最小特征值是否大于 −1.8 进行分类. 具体如下

▶ 类别1: 对称矩阵 $A + A ^ { \top }$ , 其中 A 的每个元素属于 [0,1], 且其最小特征值大于−1.8;

▶ 类别2: 对称矩阵 $A + A ^ { \top }$ , 其中 A 的每个元素属于 [0,1], 且其最小特征值小于或等于 −1.8;

其余设定同上一个任务.

## 本章总结

▶ 互相关运算、卷积核、接收域、稀疏交互、参数共享、等变表示、填充、步幅、池化、通道(参考: 教材9.1-9.7)

▶ Pytorch 库有关CNN的常用命令 (参考: 官方文档 https://pytorch.org/docs/main/nn.html#)