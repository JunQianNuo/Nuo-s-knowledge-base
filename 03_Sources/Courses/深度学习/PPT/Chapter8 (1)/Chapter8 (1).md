---
raw_title: Chapter8 (1)
subject: Chapter8 (1)
source: Chapter8 (1).pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](images/cd1c48829bd29288a9b28622d6036575abad20a2a807911bec5d63cdf0f025b2.jpg)

## 八、循环神经网络

## 离散型动态系统在许多实际应用中, 我们会遇到如下形式的递推关系:

$$
y _ {t} = f (y _ {t - 1}, x _ {t}), \quad t = 1, 2, \ldots
$$

其中, $\{ x _ { t } \} _ { t > 1 }$ 和 $\{ y _ { t } \} _ { t > 0 }$ 分别是某种数据类型(如向量、矩阵等)形成的序列. 这样的关系式称为(离散型)动态系统(dynamical system), 函数 f 称为动态系统的控制函数(governing function). 一般, 会给定一个初始值 $_ { y _ { 0 } }$ 作为系统的起点. 当 $t \geq 1$ 时, $x _ { t }$ 是第 t 步的输入, $_ { y _ { t } }$ 是第 t 步的输出.

## 离散型动态系统在许多实际应用中, 我们会遇到如下形式的递推关系:

$$
y _ {t} = f (y _ {t - 1}, x _ {t}), \quad t = 1, 2, \ldots
$$

其中, $\{ x _ { t } \} _ { t > 1 }$ 和 $\{ y _ { t } \} _ { t > 0 }$ 分别是某种数据类型(如向量、矩阵等)形成的序列. 这样的关系式称为(离散型)动态系统(dynamical system), 函数 f 称为动态系统的控制函数(governing function). 一般, 会给定一个初始值 $_ { y _ { 0 } }$ 作为系统的起点. 当 $t \geq 1$ 时, $x _ { t }$ 是第 t 步的输入, $_ { y _ { t } }$ 是第 t 步的输出.

可以看到, 系统在第 t 步时, 接收上一步 (即 t−1 步) 的输出 $_ { y _ { t - 1 } }$ 的信息和当前步的输入 $x _ { t }$ 的信息, 在控制函数作用下, 得到当前步的输出 y . 之后, $y _ { t }$ $_ { y _ { t } }$ 的信息继续传向系统的下一步. 具体过程如下图描述:

![](images/3cd7e23d2336dc0c885bb0eb3655acdf35046f98458685fcb559bb42ac256ff5.jpg)

例常微分方程的离散给定如下常微分方程初值问题

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = F (y, x), \quad x \geq 0; \quad y (0) = y _ {0}.
$$

其中, $y ( x )$ 是关于 x 的函数.

例常微分方程的离散给定如下常微分方程初值问题

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = F (y, x), \quad x \geq 0; \quad y (0) = y _ {0}.
$$

其中, $y ( x )$ 是关于 x 的函数.

对 x 所属区间 $[ 0 , + \infty )$ 进行等距剖分: 设 $h > 0$ 是固定步长, 并令 $x _ { t } = t h$ $t = 0 , 1 , 2 , \ldots .$ 于是, 该常微分方程在每个剖分点 $x _ { t }$ 上满足

$$
\frac {\mathrm{d} y}{\mathrm{d} x} (x _ {t}) = F (y (x _ {t}), x _ {t}), \quad t = 0, 1, 2, \ldots
$$

例常微分方程的离散给定如下常微分方程初值问题

$$
\frac {\mathrm{d} y}{\mathrm{d} x} = F (y, x), \quad x \geq 0; \quad y (0) = y _ {0}.
$$

其中, $y ( x )$ 是关于 x 的函数.

对 x 所属区间 $[ 0 , + \infty )$ 进行等距剖分: 设 $h > 0$ 是固定步长, 并令 $x _ { t } = t h$ $t = 0 , 1 , 2 , \ldots .$ 于是, 该常微分方程在每个剖分点 $x _ { t }$ 上满足

$$
\frac {\mathrm{d} y}{\mathrm{d} x} (x _ {t}) = F (y (x _ {t}), x _ {t}), \quad t = 0, 1, 2, \ldots
$$

用 $y _ { t }$ 作为 $y ( x _ { t } )$ 的近似值, 并以有限差分格式 $\frac { y _ { t + 1 } - y _ { t } } { h }$ 近似 $\frac { \mathrm { d } y } { \mathrm { d } x } \left( x _ { t } \right)$ . 于是, 上述方程转化为

$$
\frac {y _ {t + 1} - y _ {t}}{h} = F (y _ {t}, x _ {t}), \quad t = 0, 1, 2, \ldots
$$

即

$$
y _ {t + 1} = y _ {t} + h F (y _ {t}, x _ {t}), \quad t = 0, 1, 2, \ldots
$$

这就是一个离散的动态系统.

另一类动态系统更为复杂其递推关系如下

$$
h _ {t} = f (h _ {t - 1}, x _ {t}),
$$

$$
y _ {t} = g (h _ {t}), \quad t = 1, 2, \ldots
$$

另一类动态系统更为复杂其递推关系如下

$$
\begin{array}{l} h _ {t} = f (h _ {t - 1}, x _ {t}), \\ y _ {t} = g (h _ {t}), \quad t = 1, 2, \ldots \end{array}
$$

可以看到在每个阶段该系统向后一步传递的并非当前的输出 $y _ { t }$ 而是一个隐藏态(hidden state) $h _ { t }$ . 而 $h _ { t }$ 是由上一步的隐藏态 $h _ { t - 1 }$ 和当前输入 $x t$ 通过控制函数计算而来. 当前的输出 $_ { y _ { t } }$ , 则由 $h _ { t }$ 通过另一个函数 $g$ 直接计算得到. 具体过程如下图描述:

![](images/41fb1c9ee7cf7246e50a693797fec7b85ce4af63d9036772e0d15b2f16d88ece.jpg)

另一类动态系统更为复杂, 其递推关系如下:

$$
\begin{array}{l} h _ {t} = f (h _ {t - 1}, x _ {t}), \\ y _ {t} = g (h _ {t}), \quad t = 1, 2, \ldots \end{array}
$$

可以看到在每个阶段该系统向后一步传递的并非当前的输出 $y _ { t }$ 而是一个隐藏态(hidden state) $h _ { t }$ . 而 $h _ { t }$ 是由上一步的隐藏态 $h _ { t - 1 }$ 和当前输入 $x t$ 通过控制函数计算而来. 当前的输出 $_ { y _ { t } }$ , 则由 $h _ { t }$ 通过另一个函数 $g$ 直接计算得到. 具体过程如下图描述:

![](images/6550caf052ec263498be5b0a82e850bed448e24055b8a4847fc76fe595863e46.jpg)

一般, 会给定一个隐藏态初始值 $h _ { \mathrm { 0 } }$ 作为系统的起点. 在实际应用中, $h _ { t }$ 的规模往往远大于 $_ { y _ { t } }$ , 因为它需要携带大量信息传递到下一步.

例2: 自然语言序列. 一个由自然语言描述的文本可以看作是一个动态系统输出的结果.例如, 教材引言中的一段话:

在人工智能的早期那些对人类智力来说非常困难但对计算机来说相对简单的问题得到迅速解决比如那些可以通过一系列形式化的数学规则来描述的问题它可以视为由如下的一个动态系统生成:

![](images/176200880a39421d19a88c377e845ecb79253e5579eb84494ed6082cde2b8780.jpg)

## RNN的架构循环神经网络(recurrent neural network/RNN)是专门用于逼近上述含隐藏态的动态系统的一类神经网络.

## RNN的架构循环神经网络(recurrent neural network/RNN)是专门用于逼近上述含隐藏态的动态系统的一类神经网络. 其中, Elman 循环神经网络(以下简称循环神经网络)是一种常用的网络架构, 其数学表达式如下:

$$
h _ {t} = \sigma (W h _ {t - 1} + U x _ {t} + b),\tag{1}
$$

$$
y _ {t} = V h _ {t} + c, \quad t = 1, 2, \ldots\tag{2}
$$

其中, 列向量 $\boldsymbol { x } _ { t } \in \mathbb { R } ^ { d }$ 是第步的输入 $y _ { t } \in \mathbb { R } ^ { d ^ { \prime } }$ 是第 t 步的输出(这里 d 和 $d ^ { \prime }$ 分别表示输入维度和输出维度) 列向量 $h _ { t } \in \mathbb { R } ^ { M }$ 是第步的隐藏态(这里表示隐藏态向量的长度矩阵 $W \in \mathbb { R } ^ { M \times M } , U \in \mathbb { R } ^ { M \times d } , V \in \mathbb { R } ^ { d ^ { \prime } \times M }$ 和列向量 $b \in \mathbb { R } ^ { M } , c \in \mathbb { R } ^ { d ^ { \prime } }$ 是网络的参数, 需要通过训练优化予以确定. σ 是某个激活函数, 在循环神经网络架构中通常取函数

## RNN的架构循环神经网络(recurrent neural network/RNN)是专门用于逼近上述含隐藏态的动态系统的一类神经网络. 其中, Elman 循环神经网络(以下简称循环神经网络)是一种常用的网络架构, 其数学表达式如下:

$$
h _ {t} = \sigma (W h _ {t - 1} + U x _ {t} + b),\tag{1}
$$

$$
y _ {t} = V h _ {t} + c, \quad t = 1, 2, \ldots\tag{2}
$$

其中列向量 $\boldsymbol { x } _ { t } \in \mathbb { R } ^ { d }$ 是第 t 步的输入, $y _ { t } \in \mathbb { R } ^ { d ^ { \prime } }$ 是第 t 步的输出(这里 d 和 $d ^ { \prime }$ 分别表示输入维度和输出维度) 列向量 $h _ { t } \in \mathbb { R } ^ { M }$ 是第 t 步的隐藏态(这里 M 表示隐藏态向量的长度); 矩阵 $W \in \mathbb { R } ^ { M \times M } , U \in \mathbb { R } ^ { M \times d } , V \in \mathbb { R } ^ { d ^ { \prime } \times M }$ 和列向量 $b \in \mathbb { R } ^ { M } , c \in \mathbb { R } ^ { d ^ { \prime } }$ 是网络的参数, 需要通过训练优化予以确定. σ 是某个激活函数, 在循环神经网络架构中通常取 tanh 函数.

需要注意的是, 权重矩阵 W, U, V 和偏置向量 b, c 均与当前步数 t 无关, 即每一步的递推都共享这些权重矩阵和偏置向量循环神经网络中的隐藏态 $h _ { t }$ 是通过递推关系计算的我们可以试着将上述递推关系展开, 即

$$
\begin{array}{l} h _ {1} = \sigma (W h _ {0} + U x _ {1} + b), \\ h _ {2} = \sigma (W h _ {1} + U x _ {2} + b) = \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b), \\ h _ {3} = \sigma (W h _ {2} + U x _ {3} + b) = \sigma (W \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + U x _ {3} + b), \end{array}
$$

循环神经网络中的隐藏态 $h _ { t }$ 是通过递推关系计算的我们可以试着将上述递推关系展开, 即

$$
\begin{array}{l} h _ {1} = \sigma (W h _ {0} + U x _ {1} + b), \\ h _ {2} = \sigma (W h _ {1} + U x _ {2} + b) = \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b), \\ h _ {3} = \sigma (W h _ {2} + U x _ {3} + b) = \sigma (W \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + U x _ {3} + b), \\ \dots \end{array}
$$

## 以及计算输出

$$
\begin{array}{r l} & y _ {1} = V \sigma (W h _ {0} + U x _ {1} + b) + c, \\ & y _ {2} = V \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + c, \\ & y _ {3} = V \sigma (W \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + U x _ {3} + b) + c, \end{array}
$$

循环神经网络中的隐藏态 $h _ { t }$ 是通过递推关系计算的我们可以试着将上述递推关系展开, 即

$$
\begin{array}{l} h _ {1} = \sigma (W h _ {0} + U x _ {1} + b), \\ h _ {2} = \sigma (W h _ {1} + U x _ {2} + b) = \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b), \\ h _ {3} = \sigma (W h _ {2} + U x _ {3} + b) = \sigma (W \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + U x _ {3} + b), \\ \dots \end{array}
$$

以及计算输出

$$
\begin{array}{r l} & y _ {1} = V \sigma (W h _ {0} + U x _ {1} + b) + c, \\ & y _ {2} = V \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + c, \\ & y _ {3} = V \sigma (W \sigma (W \sigma (W h _ {0} + U x _ {1} + b) + U x _ {2} + b) + U x _ {3} + b) + c, \end{array}
$$

可以看到, 计算 $h _ { t }$ 和 $y _ { t }$ 时需要经过 t 次激活函数 $\sigma ( \cdot )$ 的复合计算. 因此, 一个走了 t步的循环神经网络的架构类似于一个层的深度神经网络然而循环神经网络与层全连接神经网络的区别在于前者共享每层的参数 (即 W, U, V, b, c).

记 $h _ { t , i } , x _ { t , i } , y _ { t , i }$ 和 $c _ { i }$ 分别为 ${ { h } _ { t } } , \ x _ { t } , \ y _ { t }$ 和 c 的第 i 个分量. 则上述循环神经网络的架构如下图所示:

![](images/d0f4c0a8e25e06fc8c6003e20c3150ea05b88788af53e6b69619c812782994a4.jpg)  
图循环神经网络的架构图中 $d = d ^ { \prime } = 2 , M = 3 )$

## 计算RNN关于参数的导数与全连接神经网络类似, 我们需要导出 RNN 各步的输出 {y } 关于全体参数$\{ W , U , V , b , c \}$ 的导数, 以便在学习模型中对网络进行训练

## 计算RNN关于参数的导数与全连接神经网络类似, 我们需要导出 RNN 各步的输出 $\{ y _ { t } \}$ 关于全体参数$\{ W , U , V , b , c \}$ 的导数, 以便在学习模型中对网络进行训练鉴于RNN的特殊架构, 我们只需要随着 t 的不断增大, 依次计算 $y _ { 1 } , y _ { 2 } , . . .$ . 的值以及它们关于各参数的导数注意初始隐藏态 $h _ { \mathrm { 0 } }$ 和每一步的输入 $x _ { 1 } , x _ { 2 } , . . .$ . 都是预先给定的.

## 计算RNN关于参数的导数与全连接神经网络类似, 我们需要导出 RNN 各步的输出 $\{ y _ { t } \}$ 关于全体参数$\{ W , U , V , b , c \}$ 的导数, 以便在学习模型中对网络进行训练鉴于RNN的特殊架构, 我们只需要随着 t 的不断增大, 依次计算 $y _ { 1 } , y _ { 2 } , . . .$ . 的值以及它们关于各参数的导数注意初始隐藏态 $h _ { \mathrm { 0 } }$ 和每一步的输入 $x _ { 1 } , x _ { 2 } , . . .$ . 都是预先给定的.

为方便, 记

$$
h _ {t} = [ h _ {t, 1} \dots h _ {t, M} ] ^ {\top}, \quad x _ {t} = [ x _ {t, 1} \dots x _ {t, d} ] ^ {\top}, \quad y _ {t} = [ y _ {t, 1} \dots y _ {t, d ^ {\prime}} ] ^ {\top}.
$$

## 计算RNN关于参数的导数与全连接神经网络类似, 我们需要导出 RNN 各步的输出 $\{ y _ { t } \}$ 关于全体参数$\{ W , U , V , b , c \}$ 的导数, 以便在学习模型中对网络进行训练鉴于RNN的特殊架构, 我们只需要随着 t 的不断增大, 依次计算 $y _ { 1 } , y _ { 2 } , . . .$ . 的值以及它们关于各参数的导数注意初始隐藏态 $h _ { \mathrm { 0 } }$ 和每一步的输入 $x _ { 1 } , x _ { 2 } , . . .$ . 都是预先给定的.

为方便, 记

$$
h _ {t} = [ h _ {t, 1} \dots h _ {t, M} ] ^ {\top}, \quad x _ {t} = [ x _ {t, 1} \dots x _ {t, d} ] ^ {\top}, \quad y _ {t} = [ y _ {t, 1} \dots y _ {t, d ^ {\prime}} ] ^ {\top}.
$$

引入中间变量 $q _ { t } = [ q _ { t , 1 } ~ . . . ~ q _ { t , M } ] ^ { \top }$ , 并记参数

$$
\begin{array}{c} W = [ w _ {i j} ] _ {M \times M}, U = [ u _ {i j} ] _ {M \times d}, V = [ v _ {i j} ] _ {d ^ {\prime} \times M}, \\ b = [ b _ {1} \ldots b _ {M} ] ^ {\top}, c = [ c _ {1} \ldots c _ {d ^ {\prime}} ] ^ {\top}. \end{array}
$$

(这里用蓝色表示给定常数、红色表示网络的参数、绿色表示在先前计算中得到的中间变量)

首先, 在第一步 (t = 1), 做以下计算:

$$
\begin{array}{l} {q _ {1} = W h _ {0} + U x _ {1} + b,} \\ {h _ {1} = \sigma (q _ {1}).} \end{array}
$$

首先, 在第一步 (t = 1), 做以下计算:

$$
\begin{array}{l} q _ {1} = W h _ {0} + U x _ {1} + b, \\ h _ {1} = \sigma (q _ {1}). \end{array}
$$

由链式法则, 可以计算 $h _ { 1 , k } \ ( 1 \leq k \leq M )$ 关于各参数的导数:

$$
\begin{array}{r l} & {\frac {\partial h _ {1 , k}}{\partial w _ {i j}} = \sigma^ {\prime} (q _ {1, k}) h _ {0, j} \delta_ {i k},} \\ & {\frac {\partial h _ {1 , k}}{\partial u _ {i j}} = \sigma^ {\prime} (q _ {1, k}) x _ {1, j} \delta_ {i k},} \\ & {\frac {\partial h _ {1 , k}}{\partial b _ {i}} = \sigma^ {\prime} (q _ {1, k}) \delta_ {i k},} \end{array}
$$

这里 $\delta _ { i k } = { \left\{ \begin{array} { l l } { 1 , ~ i = k } \\ { 0 , ~ i \neq k } \end{array} \right. }$ . 由于 $h _ { 1 }$ 不依赖于 V 和 $^ { c , }$ 因此无需考虑 $h _ { 1 }$ 关于它们的导数.

在之前的结果基础上, 可以计算 $y _ { 1 } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {1} = V h _ {1} + c,
$$

$$
\frac {\partial y _ {1 , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {1 , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {1 , i}}{\partial w _ {i j}},
$$

$$
\frac {\partial y _ {1 , k}}{\partial u _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {1 , s}}{\partial u _ {i j}} = v _ {k i} \frac {\partial h _ {1 , i}}{\partial u _ {i j}},
$$

$$
\frac {\partial y _ {1 , k}}{\partial b _ {i}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {1 , s}}{\partial b _ {i}} = v _ {k i} \frac {\partial h _ {1 , i}}{\partial b _ {i}},
$$

$$
\frac {\partial y _ {1 , k}}{\partial v _ {i j}} = h _ {1, j} \delta_ {i k},
$$

$$
\frac {\partial y _ {1 , k}}{\partial c _ {i}} = \delta_ {i k}.
$$

第一步计算完成后, 保存上述结果以供后续使用.

之后, 在第 t 步 (t = 2, 3, . . . ), 做以下计算:

$$
\begin{array}{l} q _ {t} = W h _ {t - 1} + U x _ {t} + b, \\ h _ {t} = \sigma (q _ {t}). \end{array}
$$

之后, 在第 t 步 (t = 2, 3, . . . ), 做以下计算:

$$
\begin{array}{l} q _ {t} = W h _ {t - 1} + U x _ {t} + b, \\ h _ {t} = \sigma (q _ {t}). \end{array}
$$

继续使用链式法则计算 $h _ { t , k } \ ( 1 \leq k \leq M )$ 关于各参数的导数

$$
\begin{array}{r l} & {\frac {\partial h _ {t , k}}{\partial w _ {i j}} = \sigma^ {\prime} (q _ {t, k}) \left(h _ {t - 1, j} \delta_ {i k} + w _ {k i} \frac {\partial h _ {t - 1 , k}}{\partial w _ {i j}}\right),} \\ & {\frac {\partial h _ {t , k}}{\partial u _ {i j}} = \sigma^ {\prime} (q _ {t, k}) \left(x _ {t, j} \delta_ {i k} + w _ {k i} \frac {\partial h _ {t - 1 , k}}{\partial u _ {i j}}\right),} \\ & {\frac {\partial h _ {t , k}}{\partial b _ {i}} = \sigma^ {\prime} (q _ {t, k}) \left(\delta_ {i k} + w _ {k i} \frac {\partial h _ {t - 1 , k}}{\partial b _ {i}}\right),} \end{array}
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

$$
\frac {\partial y _ {t , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial w _ {i j}},
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

$$
\frac {\partial y _ {t , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial w _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial u _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial u _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial u _ {i j}},
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

$$
\frac {\partial y _ {t , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial w _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial u _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial u _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial u _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial b _ {i}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial b _ {i}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial b _ {i}},
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

$$
\frac {\partial y _ {t , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial w _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial u _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial u _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial u _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial b _ {i}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial b _ {i}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial b _ {i}},
$$

$$
\frac {\partial y _ {t , k}}{\partial v _ {i j}} = h _ {t, j} \delta_ {i k},
$$

在之前的结果基础上, 计算 $y _ { t } \ ( 1 \leq k \leq d ^ { \prime } )$ 和它关于各参数的导数:

$$
y _ {t} = V h _ {t} + c,
$$

$$
\frac {\partial y _ {t , k}}{\partial w _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial w _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial w _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial u _ {i j}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial u _ {i j}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial u _ {i j}},
$$

$$
\frac {\partial y _ {t , k}}{\partial b _ {i}} = \sum_ {s = 1} ^ {M} v _ {k s} \frac {\partial h _ {t , s}}{\partial b _ {i}} = v _ {k i} \frac {\partial h _ {t , i}}{\partial b _ {i}},
$$

$$
\frac {\partial y _ {t , k}}{\partial v _ {i j}} = h _ {t, j} \delta_ {i k},
$$

$$
\frac {\partial y _ {t , k}}{\partial c _ {i}} = \delta_ {i k}.
$$

同样地, 保存上述结果以供后续使用

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入输出序列组合

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入-输出序列组合. 例如:

$$
\left\{ \begin{array}{l} \left(x _ {1} ^ {(1)}, x _ {2} ^ {(1)}, \ldots , x _ {s _ {1}} ^ {(1)}; y _ {1} ^ {(1)}, y _ {2} ^ {(1)}, \ldots , y _ {s _ {1}} ^ {(1)}\right) \\ \left(x _ {1} ^ {(2)}, x _ {2} ^ {(2)}, \ldots , x _ {s _ {2}} ^ {(2)}; y _ {1} ^ {(2)}, y _ {2} ^ {(2)}, \ldots , y _ {s _ {2}} ^ {(2)}\right) \\ \ldots \\ \left(x _ {1} ^ {(N)}, x _ {2} ^ {(N)}, \ldots , x _ {s _ {N}} ^ {(N)}; y _ {1} ^ {(N)}, y _ {2} ^ {(N)}, \ldots , y _ {s _ {N}} ^ {(N)}\right) \end{array} \right\}
$$

是一个由个数据点形成的数据集

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入-输出序列组合. 例如:

$$
\left\{ \begin{array}{l} \left(x _ {1} ^ {(1)}, x _ {2} ^ {(1)}, \ldots , x _ {s _ {1}} ^ {(1)}; y _ {1} ^ {(1)}, y _ {2} ^ {(1)}, \ldots , y _ {s _ {1}} ^ {(1)}\right) \\ \left(x _ {1} ^ {(2)}, x _ {2} ^ {(2)}, \ldots , x _ {s _ {2}} ^ {(2)}; y _ {1} ^ {(2)}, y _ {2} ^ {(2)}, \ldots , y _ {s _ {2}} ^ {(2)}\right) \\ \dots \\ \left(x _ {1} ^ {(N)}, x _ {2} ^ {(N)}, \ldots , x _ {s _ {N}} ^ {(N)}; y _ {1} ^ {(N)}, y _ {2} ^ {(N)}, \ldots , y _ {s _ {N}} ^ {(N)}\right) \end{array} \right\}
$$

是一个由个数据点形成的数据集

▶ 每一个 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ 表示一个数据点.

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入-输出序列组合. 例如:

$$
\left\{ \begin{array}{l} \left(x _ {1} ^ {(1)}, x _ {2} ^ {(1)}, \ldots , x _ {s _ {1}} ^ {(1)}; y _ {1} ^ {(1)}, y _ {2} ^ {(1)}, \ldots , y _ {s _ {1}} ^ {(1)}\right) \\ \left(x _ {1} ^ {(2)}, x _ {2} ^ {(2)}, \ldots , x _ {s _ {2}} ^ {(2)}; y _ {1} ^ {(2)}, y _ {2} ^ {(2)}, \ldots , y _ {s _ {2}} ^ {(2)}\right) \\ \dots \\ \left(x _ {1} ^ {(N)}, x _ {2} ^ {(N)}, \ldots , x _ {s _ {N}} ^ {(N)}; y _ {1} ^ {(N)}, y _ {2} ^ {(N)}, \ldots , y _ {s _ {N}} ^ {(N)}\right) \end{array} \right\}
$$

是一个由个数据点形成的数据集

▶ 每一个 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ 表示一个数据点.

▶ $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为整体是该数据点的样本特征向量

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入-输出序列组合. 例如:

$$
\left\{ \begin{array}{l} \left(x _ {1} ^ {(1)}, x _ {2} ^ {(1)}, \ldots , x _ {s _ {1}} ^ {(1)}; y _ {1} ^ {(1)}, y _ {2} ^ {(1)}, \ldots , y _ {s _ {1}} ^ {(1)}\right) \\ \left(x _ {1} ^ {(2)}, x _ {2} ^ {(2)}, \ldots , x _ {s _ {2}} ^ {(2)}; y _ {1} ^ {(2)}, y _ {2} ^ {(2)}, \ldots , y _ {s _ {2}} ^ {(2)}\right) \\ \dots \\ \left(x _ {1} ^ {(N)}, x _ {2} ^ {(N)}, \ldots , x _ {s _ {N}} ^ {(N)}; y _ {1} ^ {(N)}, y _ {2} ^ {(N)}, \ldots , y _ {s _ {N}} ^ {(N)}\right) \end{array} \right\}
$$

## 是一个由个数据点形成的数据集

▶ 每一个 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ 表示一个数据点.

▶ $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为整体是该数据点的样本特征向量

▶ $y _ { 1 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) }$ 是该动态系统输入 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 后的输出序列; 它作为整体, 是该数据点的标签.

## 训练RNN的数据集当我们用一个RNN去学习某个动态系统时, 用于训练RNN的数据集通常是关于该动态系统的一些已知的输入-输出序列组合. 例如:

$$
\left\{ \begin{array}{l} \left(x _ {1} ^ {(1)}, x _ {2} ^ {(1)}, \ldots , x _ {s _ {1}} ^ {(1)}; y _ {1} ^ {(1)}, y _ {2} ^ {(1)}, \ldots , y _ {s _ {1}} ^ {(1)}\right) \\ \left(x _ {1} ^ {(2)}, x _ {2} ^ {(2)}, \ldots , x _ {s _ {2}} ^ {(2)}; y _ {1} ^ {(2)}, y _ {2} ^ {(2)}, \ldots , y _ {s _ {2}} ^ {(2)}\right) \\ \dots \\ \left(x _ {1} ^ {(N)}, x _ {2} ^ {(N)}, \ldots , x _ {s _ {N}} ^ {(N)}; y _ {1} ^ {(N)}, y _ {2} ^ {(N)}, \ldots , y _ {s _ {N}} ^ {(N)}\right) \end{array} \right\}
$$

## 是一个由个数据点形成的数据集

▶ 每一个 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ 表示一个数据点.

▶ $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为整体是该数据点的样本特征向量

▶ $y _ { 1 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) }$ 是该动态系统输入 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 后的输出序列; 它作为整体, 是该数据点的标签.

▶ $s _ { n }$ 是该数据点对应序列的长度. 一般为了方便, 可以将所有数据点的序列长度 $s _ { n }$ 设置为相同值. 但理论上, $s _ { n }$ 也可以为随 n 不同的值.

有时, 我们已知某动态系统的一长串输入和输出序列 $\{ x _ { 1 } , x _ { 2 } , \ldots , \}$ 和 $\{ y _ { 1 } , y _ { 2 } , \ldots , \}$ (例如: 一本书中的所有文字按顺序排列). 然而, 将很长的输入-输出序列直接作为一个数据点用于训练会遇到困难有时, 我们已知某动态系统的一长串输入和输出序列 $\{ x _ { 1 } , x _ { 2 } , \ldots , \}$ 和 $\{ y _ { 1 } , y _ { 2 } , \ldots , \}$ (例如: 一本书中的所有文字按顺序排列). 然而, 将很长的输入-输出序列直接作为一个数据点用于训练会遇到困难首先每增加一步就需要增加一次激活函数的作用导致其非线性性质越来越强最终整体损失函数的非凸性越来越强. 其次, 随着步数增多, 梯度消失/爆炸出现的可能性越来越大.

有时, 我们已知某动态系统的一长串输入和输出序列 $\{ x _ { 1 } , x _ { 2 } , \ldots , \}$ 和 $\{ y _ { 1 } , y _ { 2 } , \ldots , \}$ (例如: 一本书中的所有文字按顺序排列). 然而, 将很长的输入-输出序列直接作为一个数据点用于训练会遇到困难首先每增加一步就需要增加一次激活函数的作用导致其非线性性质越来越强最终整体损失函数的非凸性越来越强. 其次, 随着步数增多, 梯度消失/爆炸出现的可能性越来越大.

因此我们可以在长序列上采样多个短序列片段形成多个数据点有时我们已知某动态系统的一长串输入和输出序列 $\{ x _ { 1 } , x _ { 2 } , \ldots , \}$ 和 $\{ y _ { 1 } , y _ { 2 } , \ldots , \}$ (例如: 一本书中的所有文字按顺序排列). 然而, 将很长的输入-输出序列直接作为一个数据点用于训练会遇到困难首先每增加一步就需要增加一次激活函数的作用导致其非线性性质越来越强最终整体损失函数的非凸性越来越强其次随着步数增多梯度消失爆炸出现的可能性越来越大.

因此我们可以在长序列上采样多个短序列片段形成多个数据点例如相邻采样(长度为10)

$$
\left\{ \begin{array}{l} (x _ {1}, x _ {2}, \ldots , x _ {1 0}; y _ {1}, y _ {2}, \ldots , y _ {1 0}) \\ (x _ {1 1}, x _ {1 2}, \ldots , x _ {2 0}; y _ {1 1}, y _ {1 2}, \ldots , y _ {2 0}) \\ (x _ {2 1}, x _ {2 2}, \ldots , x _ {3 0}; y _ {2 1}, y _ {2 2}, \ldots , y _ {3 0}) \\ \dots \end{array} \right\}
$$

有时我们已知某动态系统的一长串输入和输出序列 $\{ x _ { 1 } , x _ { 2 } , \ldots , \}$ 和 $\{ y _ { 1 } , y _ { 2 } , \ldots , \}$ (例如: 一本书中的所有文字按顺序排列). 然而, 将很长的输入-输出序列直接作为一个数据点用于训练会遇到困难首先每增加一步就需要增加一次激活函数的作用导致其非线性性质越来越强最终整体损失函数的非凸性越来越强其次随着步数增多梯度消失爆炸出现的可能性越来越大.

因此我们可以在长序列上采样多个短序列片段形成多个数据点例如相邻采样(长度为10)

$$
\left\{ \begin{array}{l} (x _ {1}, x _ {2}, \ldots , x _ {1 0}; y _ {1}, y _ {2}, \ldots , y _ {1 0}) \\ (x _ {1 1}, x _ {1 2}, \ldots , x _ {2 0}; y _ {1 1}, y _ {1 2}, \ldots , y _ {2 0}) \\ (x _ {2 1}, x _ {2 2}, \ldots , x _ {3 0}; y _ {2 1}, y _ {2 2}, \ldots , y _ {3 0}) \\ \dots \end{array} \right\}
$$

或随机采样(长度为10)

$$
\left\{ \begin{array}{l} (x _ {3}, x _ {4}, \ldots , x _ {1 2}; y _ {3}, y _ {4}, \ldots , y _ {1 2}) \\ (x _ {1 6}, x _ {1 7}, \ldots , x _ {2 5}; y _ {1 6}, y _ {1 7}, \ldots , y _ {2 5}) \\ (x _ {3 5}, x _ {3 6}, \ldots , x _ {4 4}; y _ {3 5}, y _ {3 6}, \ldots , y _ {4 4}) \\ \dots \end{array} \right\}
$$

## RNN学习模型

## RNN学习模型现给定一个数据点 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ . 对于一个参数为$\theta = \{ W , U , V , b , c \}$ 的 RNN, 我们可以将 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为输入 (以及搭配某个初始隐藏态 $h _ { 0 } )$ , 得到一组输出值 $y _ { 1 } , \ldots , y _ { s _ { n } }$

## RNN学习模型现给定一个数据点 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ . 对于一个参数为$\theta = \{ W , U , V , b , c \}$ 的 RNN, 我们可以将 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为输入 (以及搭配某个初始隐藏态 $h _ { 0 } )$ , 得到一组输出值 $y _ { 1 } , \ldots , y _ { s _ { n } }$

之后, 选定一类损失函数 $l ( \cdot , \cdot )$ , 则该数据点上的损失值可定义为

$$
L ^ {(n)} (\theta) = \sum_ {i = 1} ^ {s _ {n}} l (y _ {i}, y _ {i} ^ {(n)}).
$$

## RNN学习模型现给定一个数据点 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ . 对于一个参数为$\theta = \{ W , U , V , b , c \}$ 的 RNN, 我们可以将 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为输入 (以及搭配某个初始隐藏态 $h _ { 0 } )$ , 得到一组输出值 $y _ { 1 } , \ldots , y _ { s _ { n } }$

之后, 选定一类损失函数 $l ( \cdot , \cdot )$ , 则该数据点上的损失值可定义为

$$
L ^ {(n)} (\theta) = \sum_ {i = 1} ^ {s _ {n}} l (y _ {i}, y _ {i} ^ {(n)}).
$$

最后, 将所有数据点对应的损失值求平均数, 就是总损失函数, 即

$$
L (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} L ^ {(n)} (\theta).
$$

## RNN学习模型现给定一个数据点 $\left( x _ { 1 } ^ { ( n ) } , x _ { 2 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) } ; y _ { 1 } ^ { ( n ) } , y _ { 2 } ^ { ( n ) } , \ldots , y _ { s _ { n } } ^ { ( n ) } \right)$ . 对于一个参数为$\theta = \{ W , U , V , b , c \}$ 的 RNN, 我们可以将 $x _ { 1 } ^ { ( n ) } , \ldots , x _ { s _ { n } } ^ { ( n ) }$ 作为输入 (以及搭配某个初始隐藏态 $h _ { 0 } )$ , 得到一组输出值 $y _ { 1 } , \ldots , y _ { s _ { n } }$

之后, 选定一类损失函数 $l ( \cdot , \cdot )$ , 则该数据点上的损失值可定义为

$$
L ^ {(n)} (\theta) = \sum_ {i = 1} ^ {s _ {n}} l (y _ {i}, y _ {i} ^ {(n)}).
$$

最后, 将所有数据点对应的损失值求平均数, 就是总损失函数, 即

$$
L (\theta) = \frac {1}{N} \sum_ {n = 1} ^ {N} L ^ {(n)} (\theta).
$$

我们求解以下优化问题以训练 RNN:

$$
\min _ {\theta} L (\theta).
$$

对回归问题, 目标动态系统的输出类型通常是一个列向量, 而 RNN 的输出类型也必须设置成与之长度相同的列向量此时数据集中的 $y _ { i } ^ { ( n ) }$ 和 RNN 的输出 $y _ { i }$ 都是列向量, 损失函数 $l ( \cdot , \cdot )$ 可以选择为 $\ell ^ { 2 }$ 损失即

$$
l (y _ {i}, y _ {i} ^ {(n)}) = \| y _ {i} - y _ {i} ^ {(n)} \| _ {2} ^ {2},
$$

其中, $\| \cdot \| _ { 2 }$ 表示向量的欧式范数.

对分类问题若一共有个类则目标动态系统的输出类型通常是一个长度为的概率向量. 而由公式(1)-(2)定义的RNN的输出类型是一个一般的列向量. 此时, 概率向量 $y _ { i } ^ { ( n ) }$ 与 RNN 的输出 $y _ { i }$ 直接相减没有意义对分类问题若一共有个类则目标动态系统的输出类型通常是一个长度为的概率向量而由公式定义的的输出类型是一个一般的列向量此时概率向量 $y _ { i } ^ { ( n ) }$ 与 RNN 的输出 $y _ { i }$ 直接相减没有意义.

我们可以先对 $y _ { i }$ 作用一次 softmax 激活函数进行归一化, 将其转化为概率向量后, 再与$y _ { i } ^ { ( n ) }$ 一同在交叉熵下进行计算损失, 即

$$
\begin{array}{c} l (y _ {i}, y _ {i} ^ {(n)}) = - \sum_ {j = 1} ^ {J} \left(y _ {i} ^ {(n)}\right) _ {j} \ln \left(\operatorname{softmax} (y _ {i})\right) _ {j} \\ = - \left\langle y _ {i} ^ {(n)}, \ln \left(\operatorname{softmax} (y _ {i})\right) \right\rangle , \end{array}
$$

其中 $( \cdot ) _ { j }$ 表示向量的第 $j$ 个分量.

## 门控循环单元之前已经提到, 当RNN的计算步数 t 过长时, 很容易出现梯度消失/爆炸的现象. 具体地说, 在计算 $y _ { t }$ 对最初几步(如 t = 1,2)中的参数的导数时, 由于链式法则过长, 出现多项连乘导致数值计算的上溢或下溢这种现象也称为长期依赖

## 门控循环单元之前已经提到, 当RNN的计算步数 t 过长时, 很容易出现梯度消失/爆炸的现象. 具体地说, 在计算 $y _ { t }$ 对最初几步(如 t = 1,2)中的参数的导数时, 由于链式法则过长, 出现多项连乘, 导致数值计算的上溢或下溢. 这种现象也称为长期依赖.

为克服长期依赖带来的困难, 一种思路是在RNN的表达式(1)中对上一步隐藏态 $h _ { t - 1 }$ 逐元素乘一个取值在 (0,1) 上权向量 $r _ { t }$ , 从而减弱 $h _ { t - 1 }$ 在计算 $h _ { t }$ 时的影响, 即

$$
h _ {t} = \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b),
$$

这里 ∗ 表示同规模向量的逐元素相乘.

## 门控循环单元之前已经提到, 当RNN的计算步数 t 过长时, 很容易出现梯度消失/爆炸的现象. 具体地说, 在计算 $y _ { t }$ 对最初几步(如 t = 1,2)中的参数的导数时, 由于链式法则过长, 出现多项连乘, 导致数值计算的上溢或下溢. 这种现象也称为长期依赖.

为克服长期依赖带来的困难, 一种思路是在RNN的表达式(1)中对上一步隐藏态 $h _ { t - 1 }$ 逐元素乘一个取值在 (0,1) 上权向量 $r _ { t }$ , 从而减弱 $h _ { t - 1 }$ 在计算 $h _ { t }$ 时的影响, 即

$$
h _ {t} = \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b),
$$

这里 ∗ 表示同规模向量的逐元素相乘.

另一种思路则正好相反它不将 $h _ { t }$ 定义为 $\sigma ( W h _ { t - 1 } + U x _ { t } + b )$ 而是定义为$\sigma ( W h _ { t - 1 } + U x _ { t } + b )$ 与上一步隐藏态 $h _ { t - 1 }$ 的加权组合, 从而加强 $h _ { t - 1 }$ 在计算 $h _ { t }$ 时的影响, 即

$$
h _ {t} = u _ {t} * h _ {t - 1} + (1 - u _ {t}) * \sigma \left(W h _ {t - 1} + U x _ {t} + b\right),
$$

这里 $u _ { t }$ 也是一个与 $h _ { t }$ 同规模的权向量.

结合上述两种思路, 就可以导出如下表达式

$$
h _ {t} = u _ {t} * h _ {t - 1} + (1 - u _ {t}) * \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b).\tag{3}
$$

其中, 权向量 $r _ { t }$ 和 $u _ { t }$ 分别称为复位门和更新门, 起到一种逻辑计算中“门控”的作用. 表达式(3)也称为门控循环单元(gated recurrent unit, GRU).

结合上述两种思路, 就可以导出如下表达式

$$
h _ {t} = u _ {t} * h _ {t - 1} + (1 - u _ {t}) * \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b).\tag{3}
$$

其中, 权向量 $r _ { t }$ 和 $u _ { t }$ 分别称为复位门和更新门, 起到一种逻辑计算中“门控”的作用. 表达式(3)也称为门控循环单元(gated recurrent unit, GRU).

通常, $r _ { t }$ 和 $u t$ 可以用类似原始RNN中 $h _ { t }$ 的表达式计算, 即

$$
\begin{array}{l} r _ {t} = \sigma^ {r} (W ^ {r} h _ {t - 1} + U ^ {r} x _ {t} + b ^ {r}), \\ u _ {t} = \sigma^ {u} (W ^ {u} h _ {t - 1} + U ^ {u} x _ {t} + b ^ {u}). \end{array}\tag{4}
$$

结合上述两种思路, 就可以导出如下表达式

$$
h _ {t} = u _ {t} * h _ {t - 1} + (1 - u _ {t}) * \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b).\tag{3}
$$

其中, 权向量 $r _ { t }$ 和 $u _ { t }$ 分别称为复位门和更新门, 起到一种逻辑计算中“门控”的作用. 表达式(3)也称为门控循环单元(gated recurrent unit, GRU).

通常, $r _ { t }$ 和 $u t$ 可以用类似原始RNN中 $h _ { t }$ 的表达式计算, 即

$$
\begin{array}{l} r _ {t} = \sigma^ {r} (W ^ {r} h _ {t - 1} + U ^ {r} x _ {t} + b ^ {r}), \\ u _ {t} = \sigma^ {u} (W ^ {u} h _ {t - 1} + U ^ {u} x _ {t} + b ^ {u}). \end{array}\tag{4}
$$

为了保证 $r _ { t }$ 和 $u _ { t }$ 每个元素取值在 (0,1) 上, 相应的 $\sigma ^ { r }$ 和 $\sigma ^ { u }$ 可以选取 logisticsigmoid 型的激活函数. 此时, (4) 中的权重矩阵 $W ^ { r } , W ^ { u } , U ^ { r } , U ^ { u }$ 和偏置向量 $b ^ { r }$ $b ^ { u }$ 都是可训练的参数.

结合上述两种思路, 就可以导出如下表达式

$$
h _ {t} = u _ {t} * h _ {t - 1} + (1 - u _ {t}) * \sigma (W (r _ {t} * h _ {t - 1}) + U x _ {t} + b).\tag{3}
$$

其中, 权向量 $r _ { t }$ 和 $u _ { t }$ 分别称为复位门和更新门, 起到一种逻辑计算中“门控”的作用. 表达式(3)也称为门控循环单元(gated recurrent unit, GRU).

通常, $r _ { t }$ 和 $u t$ 可以用类似原始RNN中 $h _ { t }$ 的表达式计算, 即

$$
\begin{array}{l} r _ {t} = \sigma^ {r} (W ^ {r} h _ {t - 1} + U ^ {r} x _ {t} + b ^ {r}), \\ u _ {t} = \sigma^ {u} (W ^ {u} h _ {t - 1} + U ^ {u} x _ {t} + b ^ {u}). \end{array}\tag{4}
$$

为了保证 $r _ { t }$ 和 $u _ { t }$ 每个元素取值在 (0,1) 上, 相应的 $\sigma ^ { r }$ 和 $\sigma ^ { u }$ 可以选取 logisticsigmoid 型的激活函数. 此时, (4) 中的权重矩阵 $W ^ { r } , W ^ { u } , U ^ { r } , U ^ { u }$ 和偏置向量 $b ^ { r }$ $b ^ { u }$ 都是可训练的参数.

于是, 式(2),(3)和(4)定义了一个带门控循环单元的RNN

## 长短期记忆网络可以定义一类更复杂的基于门控循环单元的RNN. 首先, 在每一步引入一个新的状态 $s _ { t }$ 称为记忆元(memory cell). 在第 t 步时, 网络作如下计算

$$
\begin{array}{r l} & f _ {t} = \sigma^ {f} (W ^ {f} h _ {t - 1} + U ^ {f} x _ {t} + b ^ {f}), \\ & g _ {t} = \sigma^ {g} (W ^ {g} h _ {t - 1} + U ^ {g} x _ {t} + b ^ {g}), \\ & q _ {t} = \sigma^ {q} (W ^ {q} h _ {t - 1} + U ^ {q} x _ {t} + b ^ {q}), \\ & s _ {t} = f _ {t} * s _ {t - 1} + g _ {t} * \sigma^ {s} (W h _ {t - 1} + U x _ {t} + b), \\ & h _ {t} = q _ {t} * \sigma^ {h} (s _ {t}). \end{array}
$$

## 长短期记忆网络可以定义一类更复杂的基于门控循环单元的RNN. 首先, 在每一步引入一个新的状态 $s _ { t }$ 称为记忆元(memory cell). 在第 t 步时, 网络作如下计算

$$
\begin{array}{r l} & f _ {t} = \sigma^ {f} (W ^ {f} h _ {t - 1} + U ^ {f} x _ {t} + b ^ {f}), \\ & g _ {t} = \sigma^ {g} (W ^ {g} h _ {t - 1} + U ^ {g} x _ {t} + b ^ {g}), \\ & q _ {t} = \sigma^ {q} (W ^ {q} h _ {t - 1} + U ^ {q} x _ {t} + b ^ {q}), \\ & s _ {t} = f _ {t} * s _ {t - 1} + g _ {t} * \sigma^ {s} (W h _ {t - 1} + U x _ {t} + b), \\ & h _ {t} = q _ {t} * \sigma^ {h} (s _ {t}). \end{array}
$$

这里, $f _ { t }$ 称为遗忘门, g 称为输入门, q 称为输出门, 它们相应的激活函数 $g _ { t }$ $q _ { t }$ $\sigma ^ { f } , \sigma ^ { g } , \sigma ^ { q }$ 通常设定为 logistic sigmoid 型. 记忆元 $^ { s _ { t } }$ 和隐藏态 $h _ { t }$ 对应的激活函数 $\sigma ^ { s }$ 和 $\sigma ^ { h }$ 通常设定为 tanh 函数.

## 长短期记忆网络可以定义一类更复杂的基于门控循环单元的RNN. 首先, 在每一步引入一个新的状态 $s _ { t }$ 称为记忆元(memory cell). 在第 t 步时, 网络作如下计算

$$
\begin{array}{r l} & f _ {t} = \sigma^ {f} (W ^ {f} h _ {t - 1} + U ^ {f} x _ {t} + b ^ {f}), \\ & g _ {t} = \sigma^ {g} (W ^ {g} h _ {t - 1} + U ^ {g} x _ {t} + b ^ {g}), \\ & q _ {t} = \sigma^ {q} (W ^ {q} h _ {t - 1} + U ^ {q} x _ {t} + b ^ {q}), \\ & s _ {t} = f _ {t} * s _ {t - 1} + g _ {t} * \sigma^ {s} (W h _ {t - 1} + U x _ {t} + b), \\ & h _ {t} = q _ {t} * \sigma^ {h} (s _ {t}). \end{array}
$$

这里, $f _ { t }$ 称为遗忘门, $g _ { t }$ 称为输入门, $q _ { t }$ 称为输出门, 它们相应的激活函数 $\sigma ^ { f } , \sigma ^ { g } , \sigma ^ { q }$ 通常设定为 logistic sigmoid 型. 记忆元 $^ { s _ { t } }$ 和隐藏态 $h _ { t }$ 对应的激活函数 $\sigma ^ { s }$ 和 $\sigma ^ { h }$ 通常设定为 tanh 函数.

由上式定义的网络称为长短期记忆(long short-term memory, LSTM)网络. LSTM网络比简单的RNN更易于处理长期依赖, 并且在实际应用上有更好的整体表现.

# PyTorch 中的RNN实现

## RNN

class torch.nn.RNN(input\_size, hidden\_size, num\_layers=1, nonlinearity='tanh', bias=True batch first=False, dropout=0.0, bidirectional=False, device=None, dtype=None) [source]

Apply a multi-layer Elman RNN with tanh or ReLU non-linearity to an input sequence. For each element in the inpu sequence, each layer computes the following function

$$
h _ {t} = \tanh (x _ {t} W _ {i h} ^ {T} + b _ {i h} + h _ {t - 1} W _ {h h} ^ {T} + b _ {h h})
$$

where $h _ { t }$ is the hidden state at time $t , x _ { t }$ is the input at time t. and $h _ { ( t - 1 ) }$ is the hidden state of the previous layer at time t-1 or the initial hidden state at time 0. If nonlinearityis relu', then ReLU is used instead of tanh

图循环神经网络类的具体用法

## PyTorch 中的RNN实现

## RNN

class torch.nn.RNN(input\_size, hidden\_size, num\_layers=1, nonlinearity='tanh', bias=True batch first=False, dropout=0.0, bidirectional=False, device=None, dtype=None) [source]

Apply a multi-layer Elman RNN with tanh or ReLU non-linearity to an input sequence. For each element in the inpu sequence, each layer computes the following function

$$
h _ {t} = \tanh (x _ {t} W _ {i h} ^ {T} + b _ {i h} + h _ {t - 1} W _ {h h} ^ {T} + b _ {h h})
$$

where $h _ { t }$ is the hidden state at time $t , x _ { t }$ is the input at time t, and $h _ { ( t - 1 ) }$ is the hidden state of the previous layer at time t-1 or the initial hidden state at time 0. If nonlinearityis relu', then ReLU is used instead of tanh

图循环神经网络类的具体用法

Pytorch自带基本的 RNN 类 torch.nn.RNN. 可以直接建立一个RNN类的对象. 例如,rnn1 = torch.nn.RNN(10, 20)

定义了一个的默认激活函数为函数注意该命令只定义了 $h _ { t }$ 的计算及相应的参数不涉及 $y _ { t }$ 的计算若想定义完整的循环神经网络需手动添加一个 Linear 层以实现 $y _ { t } = V h _ { t } + c .$

下面, 用随机数产生一个数据集, 包含 N = 3 个数据点, 每个数据点总步数为 $s _ { n } = 5$ 其中每个 $x _ { t }$ 的维度 $d = 1 0 !$

```python
x_batch = torch.randn(5, 3, 10)
```

下面, 用随机数产生一个数据集, 包含 N = 3 个数据点, 每个数据点总步数为 $s _ { n } = 5$ 其中每个 $x _ { t }$ 的维度 $d = 1 0 \colon$

```python
x_batch = torch.randn(5, 3, 10)
```

再用随机数产生一批初始的隐藏态 $h _ { \mathrm { 0 } }$ , 数量为3 (对应3个数据点), 向量长度为20:

```python
h0_batch = torch.randn(1, 3, 20)
```

其中, <sub>randn</sub>的第一个输入参数 1 表示 $h _ { t }$ 的层数, 这里不深入介绍.

下面, 用随机数产生一个数据集, 包含 N = 3 个数据点, 每个数据点总步数为 $s _ { n } = 5$ 其中每个 $x _ { t }$ 的维度 d = 10:

```python
x_batch = torch.randn(5, 3, 10)
```

再用随机数产生一批初始的隐藏态 $h _ { \mathrm { 0 } }$ , 数量为3 (对应3个数据点), 向量长度为20:

```python
h0_batch = torch.randn(1, 3, 20)
```

其中, <sub>randn</sub>的第一个输入参数 1 表示 $h _ { t }$ 的层数, 这里不深入介绍.

输入上述定义的数据集和初始隐藏态, 计算rnn1每一步的 $h _ { t }$ (总步数为5):

```txt
all_ht, final_ht = rnn1(x_batch, h0_batch)
```

这里 <sub>all\_ht</sub> 是一个尺寸为(5, 3, 20)的tensor变量. 其中, <sub>all\_ht</sub>[<sub>t-1,n,:</sub>] 表示关于第 <sub>n</sub> 个数据点的 $h _ { t }$ 的值(t = 1, ..., 5); <sub>final\_ht</sub> 是一个尺寸为(1, 3, 20)的tensor变量,表示最后一步隐藏态 $h _ { 5 }$ 的值, 即 <sub>all\_ht</sub>[<sub>-1,:,:</sub>].

调用 <sub>rnn1.weight\_ih\_l0</sub>, <sub>rnn1.weight\_hh\_l0</sub>, <sub>rnn1.bias\_ih\_l0</sub>, <sub>rnn1.bias\_hh\_l0</sub>可以获取rnn1的各参数. (对多层RNN, 可用weight ih l1, weight ih l2, ... 等命令读取相应参数的第二层、第三层等, 这里不深入介绍)

调用 <sub>rnn1.weight\_ih\_l0</sub>, <sub>rnn1.weight\_hh\_l0</sub>, <sub>rnn1.bias\_ih\_l0</sub>, <sub>rnn1.bias\_hh\_l0</sub>可以获取rnn1的各参数. (对多层RNN, 可用weight ih l1, weight ih l2, ... 等命令读取相应参数的第二层、第三层等, 这里不深入介绍)

类似地, Pytorch 中自带的 torch.nn.GRU 和 torch.nn.LSTM 这两个类分别实现门控循环单元和长短期记忆网络.

## 演示: 用 RNN 生成平面上的光滑曲线给定一个原始数据集其中每个数据点是一串个平面上的点列且其围成一条封闭的光滑曲线. 现在以 D 为基础, 建立一个 RNN 模型并训练, 从而该模型能够生成新的光滑曲线.

1. 对 D 的每个数据点 $p _ { 1 } , \ldots , p _ { 1 2 0 }$ “裁剪”成小片段, 形成一个训练数据点

$$
\left(\left(p _ {k + 1}, p _ {k + 2}, \dots , p _ {k + s}\right), \left(p _ {k + 2}, p _ {k + 3}, \dots , p _ {k + s + 1}\right)\right),
$$

这里 s 是给定的正整数, 表示片段长度; $k \in [ 1 , 1 1 9 - s ]$ 是随机选取的一个整数表示片段的起始位置. 将所有上述训练数据点合并形成训练数据集 $D ^ { \prime }$

2. 定义 RNN 类并建立一个它的对象;

3. 用 $D ^ { \prime }$ 训练上述 RNN;

从一个随机起始点出发生成二维曲线并图示

## 本章总结

▶ 动态系统、隐藏态、循环神经网络、适用于RNN的数据集、RNN学习模型、门控循环单元、长短期记忆网络.(参考: 教材10.1, 10.2, 10.10)

▶ Pytorch 库有关RNN的常用命令 (参考: 官方文档 https://pytorch.org/docs/main/nn.html#)