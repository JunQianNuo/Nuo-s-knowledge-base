---
raw_title: Chapter3(1)
subject: Chapter3(1)
source: Chapter3(1).pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/cd1c48829bd29288a9b28622d6036575abad20a2a807911bec5d63cdf0f025b2.jpg)

## 三、前馈神经网络

## 神经元数学意义下的抽象神经元(neurons)是构成人工神经网络的基本单元, 它的数学形式借鉴了生物学中神经元的运行机制

## 神经元数学意义下的抽象神经元(neurons)是构成人工神经网络的基本单元, 它的数学形式借鉴了生物学中神经元的运行机制具体的说一个神经元定义为如下从 $\mathbb { R } ^ { n }$ 到 R 的函数

$$
y = \sigma (w _ {1} x _ {1} + \dots + w _ {n} x _ {n} + b),
$$

或

$$
y = \sigma (\boldsymbol {w} ^ {\top} \boldsymbol {x} + b).
$$

其中, 函数的自变量 $\pmb { x } = [ x _ { 1 } \dots x _ { n } ] ^ { \top }$ 是一个列向量; 列向量 $\pmb { w } = [ w _ { 1 } \ \dots \ w _ { n } ] ^ { \top }$ 和标量 b 是函数自身的参数, 分别称为权重(weight)和偏置(bias); σ 是一个既定的函数, 称为激活函数(activation function).

## 神经元数学意义下的抽象神经元(neurons)是构成人工神经网络的基本单元, 它的数学形式借鉴了生物学中神经元的运行机制具体的说一个神经元定义为如下从 R<sup>n</sup> 到 R 的函数

$$
y = \sigma (w _ {1} x _ {1} + \dots + w _ {n} x _ {n} + b),
$$

或

$$
y = \sigma (\boldsymbol {w} ^ {\top} \boldsymbol {x} + b).
$$

其中, 函数的自变量 $\pmb { x } = [ x _ { 1 } \dots x _ { n } ] ^ { \top }$ 是一个列向量; 列向量 $\pmb { w } = [ w _ { 1 } \ \dots \ w _ { n } ] ^ { \top }$ 和标量 b 是函数自身的参数, 分别称为权重(weight)和偏置(bias); σ 是一个既定的函数, 称为激活函数(activation function).

通常, 可以用下图表示一个神经元:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/9ac5cc8a34039e27f5df72fdcf81e50883258af04a2f85021c89637caa2bf411.jpg)  
图: 神经元的图示法有时, 神经元的定义域也可以限定为 $\mathbb { R } ^ { n }$ 的一个子集, 例如:

▶ 二元逻辑输入 $x _ { i } \in \{ 0 , 1 \} , i = 1 , \ldots , n ;$

▶ 符号输入 $x _ { i } \in \{ - 1 , 1 \} , i = 1 , \ldots , n ;$

▶ 整数输入 $x _ { i } \in S \subset \mathbb { I } , i = 1 , \dots , n ,$ , 其中 I 是全体整数集;

▶ 实数输入 $x _ { i } \in \Omega \subset \mathbb { R } , i = 1 , \dots , n ;$

## 常见激活函数

1. 阶梯型函数

## 常见激活函数

## 1. 阶梯型函数

▶ 线性函数 $l ( x ) = c x ,$ , 其中 $c > 0$

## 常见激活函数

## 1. 阶梯型函数

▶ 线性函数 $l ( x ) = c x ,$ , 其中 $c > 0$

▶ Heaviside 函数

$$
H (x) = {\left\{ \begin{array}{l l} {0,} & {{\text {如果}} x <   0,} \\ {1,} & {{\text {如果}} x \geq 0.} \end{array} \right.}
$$

$H ( x )$ 在形式上的导数是 Dirac 函数, i.e. $H ^ { \prime } ( x ) = \delta ( x )$

## 常见激活函数

1. 阶梯型函数

▶ 线性函数 $l ( x ) = c x ,$ , 其中 $c > 0$

▶ Heaviside 函数

$$
H (x) = {\left\{ \begin{array}{l l} {0,} & {{\text {如果}} x <   0,} \\ {1,} & {{\text {如果}} x \geq 0.} \end{array} \right.}
$$

$H ( x )$ 在形式上的导数是 Dirac 函数, i.e. $H ^ { \prime } ( x ) = \delta ( x )$

▶ 符号函数

$$
S (x) = {\left\{ \begin{array}{l l} {- 1,} & {{\text {如果}} x <   0,} \\ {1,} & {{\text {如果}} x \geq 0.} \end{array} \right.}
$$

它满足 $S ( x ) = 2 H ( x ) - 1$ ;

## 常见激活函数

## 1. 阶梯型函数

▶ 线性函数 $l ( x ) = c x ,$ , 其中 $c > 0 ;$

▶ Heaviside 函数

$$
H (x) = {\left\{ \begin{array}{l l} {0,} & {{\text {如果}} x <   0,} \\ {1,} & {{\text {如果}} x \geq 0.} \end{array} \right.}
$$

$H ( x )$ 在形式上的导数是 Dirac 函数, i.e. $H ^ { \prime } ( x ) = \delta ( x )$

▶ 符号函数

$$
S (x) = {\left\{ \begin{array}{l l} {- 1,} & {{\text {如果}} x <   0,} \\ {1,} & {{\text {如果}} x \geq 0.} \end{array} \right.}
$$

它满足 $S ( x ) = 2 H ( x ) - 1$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/d2cdbafe47995ad5a27ad56486ca635a94feefed2366c55028df807a8c734e66.jpg)  
(i) Heaviside 函数

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/52e95e89b71ca16ae32388bacdc2ea65731b198e26f8ea1c21027ee165c58881.jpg)  
(j) 符号函数

## 2. L型函数

## 2. L型函数

▶ 整流线性单元 $( { \mathsf { R e L U } } ) { \mathrm { ~ R e L U } } ( x ) = x H ( x ) = \operatorname* { m a x } ( x , 0 )$

ReLU 在 x = 0 连续但不可导, 而它的弱导数存在: $\mathrm { R e L U } ^ { \prime } ( x ) = H ( x )$

## 2. L型函数

▶ 整流线性单元 $( { \mathsf { R e L U } } ) { \mathrm { ~ R e L U } } ( x ) = x H ( x ) = \operatorname* { m a x } ( x , 0 )$

ReLU 在 $x = 0$ 连续但不可导, 而它的弱导数存在: $\mathrm { R e L U } ^ { \prime } ( x ) = H ( x )$

▶ 参数化整流线性单元 $( \mathsf { P R e L U } )$

$$
\operatorname{PReLU} (x; \alpha) = \left\{ \begin{array}{l l} \alpha x, & \text { if } x <   0, \\ x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha > 0$

2. L型函数

▶ 整流线性单元 $( { \mathsf { R e L U } } ) { \mathrm { ~ R e L U } } ( x ) = x H ( x ) = \operatorname* { m a x } ( x , 0 )$

${ \sf R e L U }$ 在 $x = 0$ 连续但不可导, 而它的弱导数存在: $\mathrm { R e L U } ^ { \prime } ( x ) = H ( x )$

▶ 参数化整流线性单元 $( \mathsf { P R e L U } )$

$$
\operatorname{PReLU} (x; \alpha) = \left\{ \begin{array}{l l} \alpha x, & \text { if } x <   0, \\ x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha > 0$

▶ 指数线性单元(ELU)

$$
\operatorname{ELU} (x; \alpha) = \left\{ \begin{array}{l l} \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha > 0$

▶ 缩放指数线性单元(SELU)

$$
\operatorname{SELU} (x; \alpha , \lambda) = \left\{ \begin{array}{l l} \lambda \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ \lambda x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha , \lambda > 0 ;$

▶ 缩放指数线性单元(SELU)

$$
\operatorname{SELU} (x; \alpha , \lambda) = \left\{ \begin{array}{l l} \lambda \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ \lambda x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha , \lambda > 0 ;$

<sup>▶</sup> Sigmoid线性单元(SLU)

$$
\operatorname{SLU} (x) = \frac {x}{1 + e ^ {- x}};
$$

▶ 缩放指数线性单元(SELU)

$$
\operatorname{SELU} (x; \alpha , \lambda) = \left\{ \begin{array}{l l} \lambda \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ \lambda x, & \text { if } x \geq 0, \end{array} \right.
$$

其中常数 $\alpha , \lambda > 0 ;$

<sup>▶</sup> Sigmoid线性单元(SLU)

$$
\operatorname{SLU} (x) = \frac {x}{1 + e ^ {- x}};
$$

▶ softplus函数

$$
\operatorname{sp} (x) = \ln (1 + e ^ {x}).
$$

它满足 $\operatorname { s p } ( x ) - \operatorname { s p } ( - x ) = x$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/815e1f7e7b94b8978449412429ff4f0c8f90694e99159071d16a9c24b818cdcf.jpg)  
(a) ReLU

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/0c3e897609bc9dd88aedb37a600f73eec191f72c736dab1a9dc969b9fb800668.jpg)  
(b) PReLU (α = 0.5)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/a52a7810eb1cb9cdb0a62ae5f6f60b12b845b63567ca46ec9367a8f38ce052c5.jpg)  
(d) SELU  
(α = 0.5, λ = 1.5)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/f4e10702fed5531e98b0bf1ff81d8eb33ea31f97130ca6f60cae344c5ee579a0.jpg)  
(e) SLU

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/5665f4fa8dc0860018c20e5d4db372331af33d9aca192fb963f9d8a75db8b581.jpg)  
(c) ELU (α = 0.5)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/6d7aa7dbbfbd864c5fb91dbd386ed0d9e08c756caeaaaf20c1da2d35a5925a09.jpg)  
(f) softplus函数

3. S型函数

## 3. S型函数

▶ Logistic sigmoid 函数

$$
\lg s (x) = \frac {1}{1 + e ^ {- x}}.
$$

它满足 $\operatorname { s p } ^ { \prime } ( x ) = \log \mathbf { s } ( x )$

## 3. S型函数

▶ Logistic sigmoid 函数

$$
\lg s (x) = \frac {1}{1 + e ^ {- x}}.
$$

它满足 $\operatorname { s p } ^ { \prime } ( x ) = \log \mathbf { s } ( x )$

▶ 参数化 logistic sigmoid 函数

$$
\mathrm{lg} \mathrm{s} _ {c} (x) = \frac {1}{1 + e ^ {- c x}},
$$

其中常数 $c > 0 , \ c$ 越大, $\mathrm { l g s } _ { c } ( x )$ 在 $x = 0$ 处从变为的斜率就越大即它越接近Heaviside 函数;

3. S型函数

▶ Logistic sigmoid 函数

$$
\lg s (x) = \frac {1}{1 + e ^ {- x}}.
$$

它满足 $\operatorname { s p } ^ { \prime } ( x ) = \log \mathbf { s } ( x )$

▶ 参数化 logistic sigmoid 函数

$$
\mathrm{lg} \mathrm{s} _ {c} (x) = \frac {1}{1 + e ^ {- c x}},
$$

其中常数 $c > 0 , \ c$ 越大, $\mathrm { l g s } _ { c } ( x )$ 在 $x = 0$ 处从0变为1的斜率就越大, 即它越接近Heaviside 函数;

▶ 双曲正切函数

$$
\tanh (x) = \frac {e ^ {x} - e ^ {- x}}{e ^ {x} + e ^ {- x}}.
$$

它满足 $\operatorname { t a n h } ( x ) = 2 \mathrm { l g s } _ { 2 } ( x ) - 1$

▶ Arctangent 函数

$$
h (x) = \frac {2}{\pi} \arctan (x).
$$

系数 $\textstyle { \frac { 2 } { \pi } }$ 用于将函数的值域限制在 (−1,1);

▶ Arctangent 函数

$$
h (x) = \frac {2}{\pi} \arctan (x).
$$

系数 $\textstyle { \frac { 2 } { \pi } }$ 用于将函数的值域限制在 (−1,1);

▶ Softsign 函数

$$
\operatorname{so} (x) = \frac {x}{1 + | x |}.
$$

它处处可导, 且当 $x \to \infty$ 时以 $O ( x ^ { - 1 } )$ 的速率收敛到渐近线;

▶ Arctangent 函数

$$
h (x) = \frac {2}{\pi} \arctan (x).
$$

系数 $\textstyle { \frac { 2 } { \pi } }$ 用于将函数的值域限制在 (−1,1);

▶ Softsign 函数

$$
\operatorname{so} (x) = \frac {x}{1 + | x |}.
$$

它处处可导, 且当 $x \to \infty$ 时以 $O ( x ^ { - 1 } )$ 的速率收敛到渐近线;

▶ 分段线性函数, 例如:

$$
f _ {\alpha} (x) = \left\{ \begin{array}{l l} - 1, & \text { if } x \leq - \alpha , \\ x / \alpha , & \text { if } - \alpha <   x <   \alpha , \\ 1, & \text { if } x \geq \alpha , \end{array} \right.
$$

其中常数 $\alpha > 0$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/93ef61274f64afe6a7759fbb74e90ce65a3375998205e27687845022f3afbb2b.jpg)  
(a) logistic sigmoid 函数

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/704b7d86f4b3d62bd020ada29847bb6c14dc489e257acece6aeb0f965ae08e94.jpg)  
(b) 参数化 logisticsigmoid 函数 (c = 2)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/1b45011ea80511abd25d40cd413879853ae1812657f278940d7ee335ea8c7f08.jpg)  
(d) arctangent 函数

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/149932964ba495e305717f30028ac9f811ed8321b14f04288076e71eb91993dd.jpg)  
(e) softsign 函数

(c) 双曲正切函数  
![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/cae5aba91d8497e84d3eb350f5f25333a0c01759e44dcef1ba6d725d8d877a93.jpg)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/db14f01756ce0bc59cfda1185420be6a9c85d592d80b460957b5cd62e8d40470.jpg)  
(f) 分段线性函数(α = 1)

上述阶梯型、L型和S型激活函数, 通常都是以”逐元素”的方式作用于标量、向量或矩阵上, 即它接收一个标量、向量或矩阵作为输入, 然后将运算法则作用在每一个元素(标量)上. 因此, 激活函数最终的输出结果与它的输入的尺寸规模是相同的. 例如:

$$
\operatorname{ReLU} (- 2) = \max \{- 2, 0 \} = 0,
$$

$$
\operatorname{ReLU} (\left[ \begin{array}{c} - 2 \\ 1 \\ 3 \end{array} \right]) = \left[ \begin{array}{c} \max \{- 2, 0 \} \\ \max \{1, 0 \} \\ \max \{3, 0 \} \end{array} \right] = \left[ \begin{array}{c} 0 \\ 1 \\ 3 \end{array} \right],
$$

$$
\mathrm{ReLU} (\left[ \begin{array}{c c} - 2 & 1. 5 \\ 1 & - 2. 5 \\ 3 & 0 \end{array} \right]) = \left[ \begin{array}{c c} \max \{- 2, 0 \} & \max \{1. 5, 0 \} \\ \max \{1, 0 \} & \max \{- 2. 5, 0 \} \\ \max \{3, 0 \} & \max \{0, 0 \} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1. 5 \\ 1 & 0 \\ 3 & 0 \end{array} \right].
$$

## 4. softmax函数

Softmax 激活函数的输入类型通常是一个向量, 但并不是以”逐元素”的方式进行作用的它的作用方式如下

$$
\mathrm{softmax} _ {c} (\left[ x _ {1} x _ {2} \dots x _ {n} \right]) = \frac {\left[ e ^ {c x _ {1}} e ^ {c x _ {2}} \cdots e ^ {c x _ {n}} \right]}{\sum_ {i = 1} ^ {n} e ^ {c x _ {n}}},
$$

其中 c > 0 是一个常数.

## 4. softmax函数

Softmax 激活函数的输入类型通常是一个向量, 但并不是以”逐元素”的方式进行作用的它的作用方式如下

$$
\mathrm{softmax} _ {c} (\left[ x _ {1} x _ {2} \dots x _ {n} \right]) = \frac {\left[ e ^ {c x _ {1}} e ^ {c x _ {2}} \cdots e ^ {c x _ {n}} \right]}{\sum_ {i = 1} ^ {n} e ^ {c x _ {n}}},
$$

其中 c > 0 是一个常数.

▶ Softmax 函数的输出向量与输入向量尺寸规模相同;

## 4. softmax函数

Softmax 激活函数的输入类型通常是一个向量, 但并不是以”逐元素”的方式进行作用的它的作用方式如下

$$
\mathrm{softmax} _ {c} (\left[ x _ {1} x _ {2} \dots x _ {n} \right]) = \frac {\left[ e ^ {c x _ {1}} e ^ {c x _ {2}} \cdots e ^ {c x _ {n}} \right]}{\sum_ {i = 1} ^ {n} e ^ {c x _ {n}}},
$$

其中 c > 0 是一个常数.

▶ Softmax 函数的输出向量与输入向量尺寸规模相同;

▶ Softmax 函数的输出向量每个元素均为正, 且和为1. 因此, softmax 函数的输出通常用来表示概率空间下各互斥事件的概率;

## 4. softmax函数

Softmax 激活函数的输入类型通常是一个向量, 但并不是以”逐元素”的方式进行作用的它的作用方式如下

$$
\mathrm{softmax} _ {c} (\left[ x _ {1} x _ {2} \dots x _ {n} \right]) = \frac {\left[ e ^ {c x _ {1}} e ^ {c x _ {2}} \cdots e ^ {c x _ {n}} \right]}{\sum_ {i = 1} ^ {n} e ^ {c x _ {n}}},
$$

其中 c > 0 是一个常数.

▶ Softmax 函数的输出向量与输入向量尺寸规模相同;

▶ Softmax 函数的输出向量每个元素均为正, 且和为1. 因此, softmax 函数的输出通常用来表示概率空间下各互斥事件的概率;

▶ Softmax 函数将输出入量的最大元进一步放大, 而其它元则缩小. 参数 c 表示这种放大缩小的程度

## 4. softmax函数

Softmax 激活函数的输入类型通常是一个向量, 但并不是以”逐元素”的方式进行作用的它的作用方式如下

$$
\mathrm{softmax} _ {c} (\left[ x _ {1} x _ {2} \dots x _ {n} \right]) = \frac {\left[ e ^ {c x _ {1}} e ^ {c x _ {2}} \cdots e ^ {c x _ {n}} \right]}{\sum_ {i = 1} ^ {n} e ^ {c x _ {n}}},
$$

其中 c > 0 是一个常数.

▶ Softmax 函数的输出向量与输入向量尺寸规模相同;

▶ Softmax 函数的输出向量每个元素均为正, 且和为1. 因此, softmax 函数的输出通常用来表示概率空间下各互斥事件的概率;

▶ Softmax 函数将输出入量的最大元进一步放大, 而其它元则缩小. 参数 c 表示这种放大/缩小的程度;

▶ $\begin{array} { r } { \operatorname* { l i m } _ { c \to \infty } \mathrm { s o f t m a x } _ { c } ( x ) = e _ { k } } \end{array}$ , 其中 $e _ { k } = \left[ 0 \ \cdot \cdot \cdot \ 0 \ 1 0 \ \cdot \cdot \cdot \ 0 \right]$  是单位向量, k 是向量中最大元的指标

## 例子: 用神经元学习二元逻辑函数常见的二元逻辑函数有和(AND), 或(OR), 异或(XOR) 等, 它们的定义域为 {0,1}<sup>2</sup>, 值域为 {0, 1}.

<table><tr><td> $x_1$ </td><td> $x_2$ </td><td> $y = x_1 \land x_2$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

(a) AND 函数 ∧

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \lor x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

(b) OR 函数 ∨

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \oplus x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

(c) XOR 函数 ⊕

(a) AND 函数 ∧

## 例子: 用神经元学习二元逻辑函数常见的二元逻辑函数有和(AND), 或(OR), 异或(XOR) 等, 它们的定义域为 {0,1}<sup>2</sup>, 值域为 {0, 1}.

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \land x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \lor x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

(b) OR 函数 ∨

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \oplus x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

(c) XOR 函数 ⊕  
问题能否用一个简单的神经元来精确地表示这些逻辑函数?

可以用一个 Heaviside 激活函数的神经元(也称为感知机(perceptron)) $y = H ( w ^ { \top } x + b )$ 来表示 AND 和 OR 函数.

可以用一个 Heaviside 激活函数的神经元(也称为感知机(perceptron)) $y = H ( w ^ { \top } x + b )$ 来表示 AND 和 OR 函数. 例如

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \land x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

AND 函数 ∧

$$
y = H (x _ {1} + x _ {2} - 1. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   1. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 1. 5. \end{array} \right.
$$

函数的神经元表示可以用一个 Heaviside 激活函数的神经元(也称为感知机(perceptron)) $y = H ( w ^ { \top } x + b )$ 来表示 AND 和 OR 函数. 例如

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \land x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

$$
y = H (x _ {1} + x _ {2} - 1. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   1. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 1. 5. \end{array} \right.
$$

AND 函数 ∧

函数的神经元表示

<table><tr><td> $x_1$ </td><td> $x_2$ </td><td> $y = x_1 \lor x_2$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

OR 函数 ∨

$$
y = H (x _ {1} + x _ {2} - 0. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   0. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 0. 5. \end{array} \right.
$$

函数的神经元表示可以用一个 Heaviside 激活函数的神经元(也称为感知机(perceptron)) $y = H ( w ^ { \top } x + b )$ 来表示 AND 和 OR 函数. 例如

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \land x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

AND 函数 ∧

$$
y = H (x _ {1} + x _ {2} - 1. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   1. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 1. 5. \end{array} \right.
$$

函数的神经元表示

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \lor x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

OR 函数 ∨

$$
y = H (x _ {1} + x _ {2} - 0. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   0. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 0. 5. \end{array} \right.
$$

函数的神经元表示但是, 用一个 Heaviside 神经元无法表示 XOR 函数. (线性函数 $y = w ^ { \top } x + b$ 也不能)

单个神经元难以表示 XOR 函数. 然而, 若使用两个 Heaviside 激活函数神经元“串联”的方式, 即将两个神经元通过 AND 相连的方式, 就可以表示 XOR 函数, 例如:

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \oplus x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

XOR 函数 ⊕

$$
y = H (x _ {1} + x _ {2} - 0. 5) \wedge H (- x _ {1} - x _ {2} + 1. 5) = \left\{ \begin{array}{l l} 0, & \text {if} x _ {1} + x _ {2} <   0. 5 \text {或} x _ {1} + x _ {2} > 1. 5, \\ 1, & \text {if} 0. 5 \leq x _ {1} + x _ {2} \leq 1. 5. \end{array} \right.
$$

用两个神经元“串联”来表示 XOR 函数单个神经元难以表示 XOR 函数. 然而, 若使用两个 Heaviside 激活函数神经元“串联”的方式, 即将两个神经元通过 AND 相连的方式, 就可以表示 XOR 函数, 例如:

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \oplus x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

XOR 函数 ⊕

$$
y = H (x _ {1} + x _ {2} - 0. 5) \wedge H (- x _ {1} - x _ {2} + 1. 5) = \left\{ \begin{array}{l l} 0, & \text {if} x _ {1} + x _ {2} <   0. 5 \text {或} x _ {1} + x _ {2} > 1. 5, \\ 1, & \text {if} 0. 5 \leq x _ {1} + x _ {2} \leq 1. 5. \end{array} \right.
$$

用两个神经元“串联”来表示 XOR 函数因此单个神经元往往表达能力有限而将多个神经元进行函数组合其表达能力可以大大增强.

单个神经元难以表示 XOR 函数. 然而, 若使用两个 Heaviside 激活函数神经元“串联”的方式, 即将两个神经元通过 AND 相连的方式, 就可以表示 XOR 函数, 例如:

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $y = x_{1} \oplus x_{2}$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

XOR 函数 ⊕

$$
y = H (x _ {1} + x _ {2} - 0. 5) \wedge H (- x _ {1} - x _ {2} + 1. 5) = \left\{ \begin{array}{l l} 0, & \text {if} x _ {1} + x _ {2} <   0. 5 \text {或} x _ {1} + x _ {2} > 1. 5, \\ 1, & \text {if} 0. 5 \leq x _ {1} + x _ {2} \leq 1. 5. \end{array} \right.
$$

用两个神经元“串联”来表示 XOR 函数因此单个神经元往往表达能力有限而将多个神经元进行函数组合其表达能力可以大大增强.

将多个神经元进行函数组合, 即形成了人工神经网络(artificial neural network), 简称神经网络.

## 向前传播的神经网络一种简单的组合神经元的方式, 就是将多个神经元首尾相连, 前一个神经元的输出作为后一个神经元的输入. 例如:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/5c07ca9decb826b10bb9cbc5e5b525c704317f18c16da70ed4343924235761b2.jpg)

图: 三个神经元首尾依次连接. 第一个神经元 $\mathbb { R } ^ { 2 } \to$ R, 第二、三个神经元 R → R.

## 向前传播的神经网络一种简单的组合神经元的方式, 就是将多个神经元首尾相连, 前一个神经元的输出作为后一个神经元的输入. 例如:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/d833bd98dce0902178ffa0c0645498c1aa6f578646e80cce3caf037d7fd1603d.jpg)  
图: 三个神经元首尾依次连接. 第一个神经元 $\mathbb { R } ^ { 2 } \to$ R, 第二、三个神经元 R → R.

上图中神经元依次连接所形成的函数可以用复合函数的数学表达式来描述即

$$
y = \sigma_ {3} (\sigma_ {2} (\sigma_ {1} (w _ {1} x _ {1} + w _ {2} x _ {2} + b _ {1}) + b _ {2}) + b _ {3}).
$$

它是一个从 $\mathbb { R } ^ { 2 }$ 到 R 的函数.

一个更复杂的例子如下图所示:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/12447a704533b4f1d51c9c3179ee5ef82aed4f4a93e974438a16b870a790be9c.jpg)  
图五个神经元的连接图将 $x _ { 1 } , x _ { 2 } , x _ { 3 }$ 三个输入标量从左向右传递最终以标量 $_ y$ 形式输出一个更复杂的例子如下图所示:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/2b64197a7dc19ab357872a0a96ced7d585b4b560d8bf044f7860e39ddf50255b.jpg)

图: 五个神经元的连接图, 将 $x _ { 1 } , x _ { 2 } , x _ { 3 }$ 三个输入标量从左向右传递, 最终以标量 $_ y$ 形式输出上图中的五个神经元其表达式分别如下

$$
\begin{array}{r l} & y _ {5} = \sigma_ {5} (w _ {5} ^ {1} y _ {4} + w _ {5} ^ {2} y _ {3} + b _ {5}), \\ & y _ {3} = \sigma_ {3} (w _ {3} ^ {1} y _ {1} + w _ {3} ^ {2} y _ {2} + b _ {3}), \\ & y _ {2} = \sigma_ {2} (w _ {2} ^ {1} x _ {1} + w _ {2} ^ {2} x _ {2} + w _ {2} ^ {3} x _ {3} + b _ {2}). \end{array}
$$

$$
y _ {4} = \sigma_ {4} (w _ {4} ^ {1} x _ {1} + w _ {4} ^ {2} y _ {1} + b _ {4}),
$$

$$
y _ {1} = \sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1}),
$$

一个更复杂的例子如下图所示:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/33afa840534d42571d5798bce1122dc52af823a50f6e426b2418eb80ba8f2ec7.jpg)

图: 五个神经元的连接图, 将 $x _ { 1 } , x _ { 2 } , x _ { 3 }$ 三个输入标量从左向右传递, 最终以标量 $_ y$ 形式输出上图中的五个神经元其表达式分别如下

$$
\begin{array}{r l} & y _ {5} = \sigma_ {5} (w _ {5} ^ {1} y _ {4} + w _ {5} ^ {2} y _ {3} + b _ {5}), \\ & y _ {3} = \sigma_ {3} (w _ {3} ^ {1} y _ {1} + w _ {3} ^ {2} y _ {2} + b _ {3}), \\ & y _ {2} = \sigma_ {2} (w _ {2} ^ {1} x _ {1} + w _ {2} ^ {2} x _ {2} + w _ {2} ^ {3} x _ {3} + b _ {2}). \end{array}
$$

$$
\begin{array}{r} y _ {4} = \sigma_ {4} (w _ {4} ^ {1} x _ {1} + w _ {4} ^ {2} y _ {1} + b _ {4}), \\ y _ {1} = \sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1}), \end{array}
$$

将它们复合后, 可写出整体函数的表达式:

$$
\begin{array}{l} y = \sigma_ {5} \Bigg [ \bigg (w _ {5} ^ {1} \Big (\sigma_ {4} (w _ {4} ^ {1} x _ {1} + w _ {4} ^ {2} (\sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1})) + b _ {4}) \Big) \\ \qquad + w _ {5} ^ {2} \Big (\sigma_ {3} \big (w _ {3} ^ {1} (\sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1})) + w _ {3} ^ {2} (\sigma_ {2} (w _ {2} ^ {1} x _ {1} + w _ {2} ^ {2} x _ {2} + w _ {2} ^ {3} x _ {3} + b _ {2})) \big) + b _ {3} \Big) \Bigg) + b _ {5} \Bigg ]. \end{array}
$$

## 前馈神经网络上述由多个神经元连接复合而成的函数就是神经网络对一个神经网络它的整体结构(即它所包含的神经元数量以及神经元的连接方式)称为架构(architecture). 神经网络的架构往往可以用图论中的有向图进行表示, 即每个输入标量和神经元用一个点表示, 它们之间的连接用一条边表示.

## 前馈神经网络上述由多个神经元连接(复合)而成的函数就是神经网络. 对一个神经网络, 它的整体结构(即它所包含的神经元数量以及神经元的连接方式)称为架构(architecture). 神经网络的架构往往可以用图论中的有向图进行表示, 即每个输入标量和神经元用一个点表示, 它们之间的连接用一条边表示.

在上述例子中, 最初的输入 $x _ { 1 } , \ldots , x _ { n }$ 通过一系列神经元的传递, 从前往后(在图中从左往右进行数值的传播最终输出结果具有这种架构的神经网络称为前馈神经网络(feedforward neural network).

## 全连接神经网络而在实际应用中人们倾向于使用排列规则的神经元架构以便进行数学表达和工程计算. 一种简单的方式是将所有神经元逐层排列, 并且将前一层的每个神经元与后一层的所有神经元都连接起来. 具有这种架构的前馈神经网络称为全连接神经网络(fully-connected neural network).

## 例如:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/5b4bcc940edb7076680da6d54e256784fe0c0077b84da0c220d2afb622fbcb13.jpg)

该全连接神经网络一共包括6层. 从左往右第一层是全体输入标量, 称为输入层(inputlayer); 最后一层由一组神经元形成, 它们的输出即为整个神经网络的输出, 因此称为输出层(output layer); 而其它各层也由一组神经元形成, 它们位于输入层和输出层之间, 称为隐藏层(hidden layer).

## 例如:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/cd13679354d8a726cd596bc7688356950308c5268dac7420fa7ed2259c5bee9a.jpg)

该全连接神经网络一共包括6层. 从左往右第一层是全体输入标量, 称为输入层(inputlayer); 最后一层由一组神经元形成, 它们的输出即为整个神经网络的输出, 因此称为输出层(output layer); 而其它各层也由一组神经元形成, 它们位于输入层和输出层之间, 称为隐藏层(hidden layer).

▶ 通常, 隐藏层和输出层的总数(即隐藏层数量+1)称为网络的深度(depth);

▶ 对每一个隐藏层, 其包含的神经元数量称为该层的宽度(width);

▶ 如果一个全连接神经网络的各隐藏层宽度均相同则称之为网络的宽度假设一个全连接神经网络包含个输入标量 $x _ { 1 } , \ldots , x _ { d }$ 和 $d ^ { \prime }$ 个输出标量 $y _ { 1 } , \ldots , y _ { d ^ { \prime } }$ 同时它包含个隐藏层且第个隐藏层的宽度为 $M _ { \ell } \ ( \ell = 1 , \ldots , L )$ . 另外, 记第 ℓ个隐藏层的神经元激活函数均为 $\sigma ^ { \ell }$ 输出层的神经元激活函数均为 $\sigma ^ { L + 1 }$ . 于是, 该网络的各层具有如下数学表达式第1个隐藏层: $y _ { j } ^ { 1 } = \sigma ^ { 1 } \left( \sum _ { i = 1 } ^ { d } w _ { j i } ^ { 1 } x _ { i } + b _ { j } ^ { 1 } \right) , \quad j = 1 , \ldots , M _ { 1 }$

第2至第L个隐藏层: $y _ { j } ^ { \ell } = \sigma ^ { \ell } \left( \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } + b _ { j } ^ { \ell } \right)$ $j = 1 , \ldots , M _ { \ell } , \quad \ell = 2 , \ldots , L ,$

输出层: $y _ { j } = \sigma ^ { L + 1 } \left( \sum _ { i = 1 } ^ { M _ { L } } w _ { j i } ^ { L + 1 } y _ { i } ^ { L } + b _ { j } ^ { L + 1 } \right)$ $j = 1 , \ldots , d ^ { \prime } .$

其中, $w _ { j i } ^ { \ell }$ 和 $b _ { j } ^ { \ell }$ 分别是各层的权重和偏置. 所有权重和偏置统称为神经网络的(自由)参数((free) parameters).

也可以用矩阵和向量的形式来简化上述表达. 记

$$
x = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \ldots \\ x _ {d} \end{array} \right]; \quad y ^ {\ell} = \left[ \begin{array}{c} y _ {1} ^ {\ell} \\ y _ {2} ^ {\ell} \\ \ldots \\ y _ {M _ {\ell}} ^ {\ell} \end{array} \right],   \ell = 1, \ldots , L; \quad y = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \ldots \\ y _ {d ^ {\prime}} \end{array} \right];
$$

$$
W ^ {1} = \left[ \begin{array}{c c c c} w _ {1 1} ^ {1} & w _ {1 2} ^ {1} & \dots & w _ {1 d} ^ {1} \\ w _ {2 1} ^ {1} & w _ {2 2} ^ {1} & \dots & w _ {2 d} ^ {1} \\ \dots & \dots & \dots & \dots \\ w _ {M _ {1}, 1} ^ {1} & w _ {M _ {1}, 2} ^ {1} & \dots & w _ {M _ {1}, d} ^ {1} \end{array} \right], b ^ {1} = \left[ \begin{array}{c} b _ {1} ^ {1} \\ b _ {2} ^ {1} \\ \dots \\ b _ {M _ {1}} ^ {1} \end{array} \right];
$$

$$
W ^ {\ell} = \left[ \begin{array}{c c c c} w _ {1 1} ^ {\ell} & w _ {1 2} ^ {\ell} & \ldots & w _ {1, M _ {\ell - 1}} ^ {\ell} \\ w _ {2 1} ^ {\ell} & w _ {2 2} ^ {\ell} & \ldots & w _ {2, M _ {\ell - 1}} ^ {\ell} \\ \ldots & \ldots & \ldots & \ldots \\ w _ {M _ {\ell}, 1} ^ {\ell} & w _ {M _ {\ell}, 2} ^ {\ell} & \ldots & w _ {M _ {\ell}, M _ {\ell - 1}} ^ {\ell} \end{array} \right], b ^ {\ell} = \left[ \begin{array}{c} b _ {1 1} ^ {\ell} \\ b _ {2 1} ^ {\ell} \\ \ldots \\ b _ {M _ {\ell}} ^ {\ell} \end{array} \right], \ell = 2, \ldots , L;
$$

$$
W ^ {L + 1} = \left[ \begin{array}{c c c c} w _ {1 1} ^ {L + 1} & w _ {1 2} ^ {L + 1} & \ldots & w _ {1, M _ {L}} ^ {L + 1} \\ w _ {2 1} ^ {L + 1} & w _ {2 2} ^ {L + 1} & \ldots & w _ {2, M _ {L}} ^ {L + 1} \\ \ldots & \ldots & \ldots & \ldots \\ w _ {d ^ {\prime}, 1} ^ {L + 1} & w _ {d ^ {\prime}, 2} ^ {L + 1} & \ldots & w _ {d ^ {\prime}, M _ {L}} ^ {L + 1} \end{array} \right],   b ^ {L + 1} = \left[ \begin{array}{c} b _ {1} ^ {L + 1} \\ b _ {2} ^ {L + 1} \\ \ldots \\ b _ {d ^ {\prime}} ^ {L + 1} \end{array} \right].
$$

则该网络的各层可以表示成第1个隐藏层: $\boldsymbol { y } ^ { 1 } = \boldsymbol { \sigma } ^ { 1 } ( \boldsymbol { W } ^ { 1 } \boldsymbol { x } + \boldsymbol { b } ^ { 1 } )$

第至第个隐藏层 $y ^ { \ell } = \sigma ^ { \ell } ( W ^ { \ell } y ^ { \ell - 1 } + b ^ { \ell } ) , \quad \ell = 2 , \dots , L ,$

输出层: $y = \sigma ^ { L + 1 } ( W ^ { L + 1 } y ^ { L } + b ^ { L + 1 } )$

将各层表达式写成复合函数, 就可以得到整个神经网络的表达式:

$$
y = \sigma^ {L + 1} \left(W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} (W ^ {1} x + b ^ {1}) \dots\right) + b ^ {L}\right) + b ^ {L + 1}\right).
$$

将各层表达式写成复合函数, 就可以得到整个神经网络的表达式:

$$
y = \sigma^ {L + 1} \left(W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} (W ^ {1} x + b ^ {1}) \dots\right) + b ^ {L}\right) + b ^ {L + 1}\right).
$$

在许多回归问题中, 输出层的激活函数 $\sigma ^ { L + 1 }$ 通常设置为恒等函数 $\sigma ^ { L + 1 } ( t ) = t .$ . 因此,网络可写成

$$
y = W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b ^ {L + 1}.
$$

将各层表达式写成复合函数, 就可以得到整个神经网络的表达式:

$$
y = \sigma^ {L + 1} \left(W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} (W ^ {1} x + b ^ {1}) \dots\right) + b ^ {L}\right) + b ^ {L + 1}\right).
$$

在许多回归问题中, 输出层的激活函数 $\sigma ^ { L + 1 }$ 通常设置为恒等函数 $\sigma ^ { L + 1 } ( t ) = t .$ . 因此,网络可写成

$$
y = W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b ^ {L + 1}.
$$

有时我们将一个神经网络记作 $f ( x ; \theta )$ , 其中 x 是输入向量, $\theta$ 是网络全体参数形成的集合. 对上述全连接神经网络, $\theta = \{ W ^ { \ell } , b ^ { \ell } \} _ { \ell = 1 } ^ { L + 1 }$ . 随着 $\theta$ 的不断变化, 函数 $f ( x ; \theta )$ 往往也在不断变化

## 神经网络求值(前向传播)

前馈神经网络接收输入 x, 通过各隐藏层的逐渐传递, 最终产生输出 y. 这个过程称为前向传播(forward propagation). 前向传播实质上就是对神经网络进行函数求值的过程.

## 神经网络求值(前向传播)

前馈神经网络接收输入 x, 通过各隐藏层的逐渐传递, 最终产生输出 y. 这个过程称为前向传播(forward propagation). 前向传播实质上就是对神经网络进行函数求值的过程.

可以估算前向传播的复杂度一个从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的具有简单激活函数如函数)的全连接神经网络, 设其深度为 L+1 (含 L 个隐藏层), 每个隐藏层宽度均为 M,则作一次前向传播所需的计算复杂度为 $O ( ( L - 1 ) M ^ { 2 } + d M + d ^ { \prime } M )$

## 神经网络对参数求导当使用基于梯度的优化器对前馈神经网络进行训练时通常需要计算网络对其参数的一阶导数, 从而形成梯度向量. 为了简便, 我们考虑一个从 $\mathbb { R } ^ { d }$ 到 R 的全连接神经网络, 并假设它具有如下的分层表达式

$$
y = \sigma^ {L + 1} (\sum_ {i = 1} ^ {M _ {L}} w _ {i} ^ {L + 1} y _ {i} ^ {L} + b ^ {L + 1}),\tag{1}
$$

$$
y _ {j} ^ {\ell} = \sigma^ {\ell} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}), \quad j = 1, \ldots , M _ {\ell}, \quad \ell = 2, \ldots , L,\tag{2}
$$

$$
y _ {j} ^ {1} = \sigma^ {1} (\sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}), \quad j = 1, \ldots , M _ {1}.\tag{3}
$$

这里, 神经网络的输入变量是 $x _ { 1 } , \ldots , x _ { d }$ , 输出变量是 y.

## 神经网络对参数求导当使用基于梯度的优化器对前馈神经网络进行训练时通常需要计算网络对其参数的一阶导数, 从而形成梯度向量. 为了简便, 我们考虑一个从 $\mathbb { R } ^ { d }$ 到 R 的全连接神经网络, 并假设它具有如下的分层表达式

$$
y = \sigma^ {L + 1} (\sum_ {i = 1} ^ {M _ {L}} w _ {i} ^ {L + 1} y _ {i} ^ {L} + b ^ {L + 1}),\tag{1}
$$

$$
y _ {j} ^ {\ell} = \sigma^ {\ell} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}), \quad j = 1, \ldots , M _ {\ell}, \quad \ell = 2, \ldots , L,\tag{2}
$$

$$
y _ {j} ^ {1} = \sigma^ {1} (\sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}), \quad j = 1, \ldots , M _ {1}.\tag{3}
$$

这里, 神经网络的输入变量是 $x _ { 1 } , \ldots , x _ { d }$ , 输出变量是 y.

目标: 给定输入变量 $x _ { 1 } , \ldots , x _ { d }$ 和参数 $\{ w _ { j i } ^ { \ell } , b _ { j } ^ { \ell } \} _ { \ell = 1 } ^ { L } \cup \{ w _ { i } ^ { L + 1 } , b ^ { L + 1 } \}$ 的一组具体值,计算该网络的输出变量 y 对各参数的偏导数的值.

直接计算 y 对各参数的偏导数, 需要反复对神经网络的表达式使用链式法则. 当 L 较大时偏导数的表达式将十分复杂不适合进行高效编程计算因此当前最主流的计算方法是引进辅助变量, 在符号上简化链式法则.

直接计算 $_ y$ 对各参数的偏导数需要反复对神经网络的表达式使用链式法则当较大时, 偏导数的表达式将十分复杂, 不适合进行高效编程计算. 因此, 当前最主流的计算方法是引进辅助变量, 在符号上简化链式法则. 具体地, 引入中间变量 $q _ { j } ^ { \ell } ,$ , 将 (1)-(3) 改写为

$$
y = \sigma^ {L + 1} (q ^ {L + 1}), \quad q ^ {L + 1} = \sum_ {i = 1} ^ {M _ {L}} w _ {i} ^ {L + 1} y _ {i} ^ {L} + b ^ {L + 1},\tag{4}
$$

$$
y _ {j} ^ {\ell} = \sigma^ {\ell} (q _ {j} ^ {\ell}), \quad q _ {j} ^ {\ell} = \sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}, \quad j = 1, \ldots , M _ {\ell}, \quad \ell = 2, \ldots , L,\tag{5}
$$

$$
y _ {j} ^ {1} = \sigma^ {1} (q _ {j} ^ {1}), \quad q _ {j} ^ {1} = \sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}, \quad j = 1, \ldots , M _ {1}.\tag{6}
$$

直接计算 y 对各参数的偏导数, 需要反复对神经网络的表达式使用链式法则. 当 L 较大时, 偏导数的表达式将十分复杂, 不适合进行高效编程计算. 因此, 当前最主流的计算方法是引进辅助变量, 在符号上简化链式法则. 具体地, 引入中间变量 $q _ { j } ^ { \ell } ,$ , 将 (1)-(3) 改写为

$$
y = \sigma^ {L + 1} (q ^ {L + 1}), \quad q ^ {L + 1} = \sum_ {i = 1} ^ {M _ {L}} w _ {i} ^ {L + 1} y _ {i} ^ {L} + b ^ {L + 1},\tag{4}
$$

$$
y _ {j} ^ {\ell} = \sigma^ {\ell} (q _ {j} ^ {\ell}), \quad q _ {j} ^ {\ell} = \sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}, \quad j = 1, \ldots , M _ {\ell}, \quad \ell = 2, \ldots , L,\tag{5}
$$

$$
y _ {j} ^ {1} = \sigma^ {1} (q _ {j} ^ {1}), \quad q _ {j} ^ {1} = \sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}, \quad j = 1, \ldots , M _ {1}.\tag{6}
$$

进一步, 引入辅助变量 $\begin{array} { r } { p _ { i } ^ { \ell } : = \frac { \partial y } { \partial q _ { i } ^ { \ell } } , i = 1 , \ldots , M _ { \ell } , \ell = 1 , \ldots , L } \end{array}$ 以及 $\begin{array} { r } { p ^ { L + 1 } : = \frac { \partial y } { \partial q ^ { L + 1 } } } \end{array}$ 直接计算 y 对各参数的偏导数, 需要反复对神经网络的表达式使用链式法则. 当 L 较大时, 偏导数的表达式将十分复杂, 不适合进行高效编程计算. 因此, 当前最主流的计算方法是引进辅助变量, 在符号上简化链式法则. 具体地, 引入中间变量 $q _ { j } ^ { \ell } ,$ , 将 (1)-(3) 改写为

$$
y = \sigma^ {L + 1} (q ^ {L + 1}), \quad q ^ {L + 1} = \sum_ {i = 1} ^ {M _ {L}} w _ {i} ^ {L + 1} y _ {i} ^ {L} + b ^ {L + 1},\tag{4}
$$

$$
y _ {j} ^ {\ell} = \sigma^ {\ell} (q _ {j} ^ {\ell}), \quad q _ {j} ^ {\ell} = \sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}, \quad j = 1, \ldots , M _ {\ell}, \quad \ell = 2, \ldots , L,\tag{5}
$$

$$
y _ {j} ^ {1} = \sigma^ {1} (q _ {j} ^ {1}), \quad q _ {j} ^ {1} = \sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}, \quad j = 1, \ldots , M _ {1}.\tag{6}
$$

进一步, 引入辅助变量 $\begin{array} { r } { p _ { i } ^ { \ell } : = \frac { \partial y } { \partial q _ { i } ^ { \ell } } , i = 1 , \ldots , M _ { \ell } , \ell = 1 , \ldots , L } \end{array}$ 以及 $\begin{array} { r } { p ^ { L + 1 } : = \frac { \partial y } { \partial q ^ { L + 1 } } } \end{array}$ 算法的第一步, 是执行一次前向传播, 即按 (4)-(6) 依次计算 $q _ { j } ^ { 1 } , y _ { j } ^ { 1 } , q _ { j } ^ { 2 } , y _ { j } ^ { 2 } , . . . , q _ { j } ^ { L }$ $y _ { j } ^ { L } , q ^ { L + 1 } , y$ , 并保存结果以后续使用.

下一步, 对输出层进行计算(蓝色变量):

输出层: $\begin{array} { r } { y = \sigma ^ { L + 1 } ( q ^ { L + 1 } ) , \quad q ^ { L + 1 } = \sum _ { i = 1 } ^ { M _ { L } } w _ { i } ^ { L + 1 } y _ { i } ^ { L } + b ^ { L + 1 } . } \end{array}$

下一步, 对输出层进行计算(蓝色变量):

输出层: $\begin{array} { r } { y = \sigma ^ { L + 1 } ( q ^ { L + 1 } ) , \quad q ^ { L + 1 } = \sum _ { i = 1 } ^ { M _ { L } } w _ { i } ^ { L + 1 } y _ { i } ^ { L } + b ^ { L + 1 } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p ^ {L + 1} := \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} = (\sigma^ {L + 1}) ^ {\prime} (q ^ {L + 1}), \\ \frac {\partial y}{\partial w _ {i} ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial w _ {i} ^ {L + 1}} = p ^ {L + 1} y _ {i} ^ {L}, \quad \frac {\partial y}{\partial b ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial b ^ {L + 1}} = p ^ {L + 1} \cdot 1 = p ^ {L + 1}. \end{array}
$$

下一步, 对输出层进行计算(蓝色变量):

输出层: $\begin{array} { r } { y = \sigma ^ { L + 1 } ( q ^ { L + 1 } ) , \quad q ^ { L + 1 } = \sum _ { i = 1 } ^ { M _ { L } } w _ { i } ^ { L + 1 } y _ { i } ^ { L } + b ^ { L + 1 } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p ^ {L + 1} := \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} = (\sigma^ {L + 1}) ^ {\prime} (q ^ {L + 1}), \\ \frac {\partial y}{\partial w _ {i} ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial w _ {i} ^ {L + 1}} = p ^ {L + 1} y _ {i} ^ {L}, \quad \frac {\partial y}{\partial b ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial b ^ {L + 1}} = p ^ {L + 1} \cdot 1 = p ^ {L + 1}. \end{array}
$$

下一步, 对最后一层隐藏层 (ℓ = L) 进行计算:

第L层: $\begin{array} { r } { y _ { j } ^ { L } = \sigma ^ { L } ( q _ { j } ^ { L } ) , \quad q _ { j } ^ { L } = \sum _ { i = 1 } ^ { M _ { L - 1 } } w _ { j i } ^ { L } y _ { i } ^ { L - 1 } + b _ { j } ^ { L } , \quad j = 1 , \dots , M _ { L } . } \end{array}$

下一步, 对输出层进行计算(蓝色变量):

输出层: $\begin{array} { r } { y = \sigma ^ { L + 1 } ( q ^ { L + 1 } ) , \quad q ^ { L + 1 } = \sum _ { i = 1 } ^ { M _ { L } } w _ { i } ^ { L + 1 } y _ { i } ^ { L } + b ^ { L + 1 } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p ^ {L + 1} := \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} = (\sigma^ {L + 1}) ^ {\prime} (q ^ {L + 1}), \\ \frac {\partial y}{\partial w _ {i} ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial w _ {i} ^ {L + 1}} = p ^ {L + 1} y _ {i} ^ {L}, \quad \frac {\partial y}{\partial b ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial b ^ {L + 1}} = p ^ {L + 1} \cdot 1 = p ^ {L + 1}. \end{array}
$$

下一步, 对最后一层隐藏层 $( \ell = L )$ 进行计算:

第L层: $\begin{array} { r } { y _ { j } ^ { L } = \sigma ^ { L } ( q _ { j } ^ { L } ) , \quad q _ { j } ^ { L } = \sum _ { i = 1 } ^ { M _ { L - 1 } } w _ { j i } ^ { L } y _ { i } ^ { L - 1 } + b _ { j } ^ { L } , \quad j = 1 , \dots , M _ { L } . } \end{array}$

由链式法则, 有

$$
p _ {i} ^ {L} := \frac {\partial y}{\partial q _ {i} ^ {L}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial y _ {i} ^ {L}} \cdot \frac {\mathrm{d} y _ {i} ^ {L}}{\mathrm{d} q _ {i} ^ {L}} = p ^ {L + 1} w _ {i} ^ {L + 1} \cdot (\sigma^ {L}) ^ {\prime} (q _ {i} ^ {L}),
$$

$$
\frac {\partial y}{\partial w _ {j i} ^ {L}} = \frac {\partial y}{\partial q _ {j} ^ {L}} \cdot \frac {\partial q _ {j} ^ {L}}{\partial w _ {j i} ^ {L}} = p _ {j} ^ {L} y _ {i} ^ {L - 1}, \quad \frac {\partial y}{\partial b _ {j} ^ {L}} = \frac {\partial y}{\partial q _ {j} ^ {L}} \cdot \frac {\partial q _ {j} ^ {L}}{\partial b _ {j} ^ {L}} = p _ {j} ^ {L} \cdot 1 = p _ {j} ^ {L}.
$$

之后, 对 $\ell = L - 1 , \ldots , 2$ 依次计算:

第ℓ层: $\begin{array} { r } { y _ { j } ^ { \ell } = \sigma ^ { \ell } ( q _ { j } ^ { \ell } ) , \quad q _ { j } ^ { \ell } = \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } + b _ { j } ^ { \ell } , \quad j = 1 , \ldots , M _ { \ell } . } \end{array}$

之后, 对 $\ell = L - 1 , \ldots , 2$ 依次计算:

第ℓ层: $\begin{array} { r } { y _ { j } ^ { \ell } = \sigma ^ { \ell } ( q _ { j } ^ { \ell } ) , \quad q _ { j } ^ { \ell } = \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } + b _ { j } ^ { \ell } , \quad j = 1 , \ldots , M _ { \ell } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p _ {i} ^ {\ell} := \frac {\partial y}{\partial q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} \frac {\partial y}{\partial q _ {j} ^ {\ell + 1}} \cdot \frac {\partial q _ {j} ^ {\ell + 1}}{\partial y _ {i} ^ {\ell}} \cdot \frac {\mathrm{d} y _ {i} ^ {\ell}}{\mathrm{d} q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} p _ {j} ^ {\ell + 1} w _ {j i} ^ {\ell + 1} \cdot (\sigma^ {\ell}) ^ {\prime} (q _ {i} ^ {\ell}), \\ \frac {\partial y}{\partial w _ {j i} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial w _ {j i} ^ {\ell}} = p _ {j} ^ {\ell} y _ {i} ^ {\ell - 1}, \quad \frac {\partial y}{\partial b _ {j} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial b _ {j} ^ {\ell}} = p _ {j} ^ {\ell} \cdot 1 = p _ {j} ^ {\ell}. \end{array}
$$

之后, 对 $\ell = L - 1 , \ldots , 2$ 依次计算:

第ℓ层: $\begin{array} { r } { y _ { j } ^ { \ell } = \sigma ^ { \ell } ( q _ { j } ^ { \ell } ) , \quad q _ { j } ^ { \ell } = \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } + b _ { j } ^ { \ell } , \quad j = 1 , \ldots , M _ { \ell } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p _ {i} ^ {\ell} := \frac {\partial y}{\partial q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} \frac {\partial y}{\partial q _ {j} ^ {\ell + 1}} \cdot \frac {\partial q _ {j} ^ {\ell + 1}}{\partial y _ {i} ^ {\ell}} \cdot \frac {\mathrm{d} y _ {i} ^ {\ell}}{\mathrm{d} q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} p _ {j} ^ {\ell + 1} w _ {j i} ^ {\ell + 1} \cdot (\sigma^ {\ell}) ^ {\prime} (q _ {i} ^ {\ell}), \\ \frac {\partial y}{\partial w _ {j i} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial w _ {j i} ^ {\ell}} = p _ {j} ^ {\ell} y _ {i} ^ {\ell - 1}, \quad \frac {\partial y}{\partial b _ {j} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial b _ {j} ^ {\ell}} = p _ {j} ^ {\ell} \cdot 1 = p _ {j} ^ {\ell}. \end{array}
$$

最后, 对第一层隐藏层 (ℓ = 1) 进行计算:

第1层: $\begin{array} { r } { y _ { j } ^ { 1 } = \sigma ^ { 1 } ( q _ { j } ^ { 1 } ) , \quad q _ { j } ^ { 1 } = \sum _ { i = 1 } ^ { d } w _ { j i } ^ { 1 } x _ { i } + b _ { j } ^ { 1 } , \quad j = 1 , \ldots , M _ { 1 } } \end{array}$

之后, 对 $\ell = L - 1 , \ldots , 2$ 依次计算:

第ℓ层: $\begin{array} { r } { y _ { j } ^ { \ell } = \sigma ^ { \ell } ( q _ { j } ^ { \ell } ) , \quad q _ { j } ^ { \ell } = \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } + b _ { j } ^ { \ell } , \quad j = 1 , \ldots , M _ { \ell } . } \end{array}$

由链式法则, 有

$$
\begin{array}{c} p _ {i} ^ {\ell} := \frac {\partial y}{\partial q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} \frac {\partial y}{\partial q _ {j} ^ {\ell + 1}} \cdot \frac {\partial q _ {j} ^ {\ell + 1}}{\partial y _ {i} ^ {\ell}} \cdot \frac {\mathrm{d} y _ {i} ^ {\ell}}{\mathrm{d} q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} p _ {j} ^ {\ell + 1} w _ {j i} ^ {\ell + 1} \cdot (\sigma^ {\ell}) ^ {\prime} (q _ {i} ^ {\ell}), \\ \frac {\partial y}{\partial w _ {j i} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial w _ {j i} ^ {\ell}} = p _ {j} ^ {\ell} y _ {i} ^ {\ell - 1}, \quad \frac {\partial y}{\partial b _ {j} ^ {\ell}} = \frac {\partial y}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial b _ {j} ^ {\ell}} = p _ {j} ^ {\ell} \cdot 1 = p _ {j} ^ {\ell}. \end{array}
$$

最后, 对第一层隐藏层 (ℓ = 1) 进行计算:

第1层: $\begin{array} { r } { y _ { j } ^ { 1 } = \sigma ^ { 1 } ( q _ { j } ^ { 1 } ) , \quad q _ { j } ^ { 1 } = \sum _ { i = 1 } ^ { d } w _ { j i } ^ { 1 } x _ { i } + b _ { j } ^ { 1 } , \quad j = 1 , \ldots , M _ { 1 } . } \end{array}$

由链式法则, 有

$$
p _ {i} ^ {1} := \frac {\partial y}{\partial q _ {i} ^ {1}} = \sum_ {j = 1} ^ {M _ {2}} \frac {\partial y}{\partial q _ {j} ^ {2}} \cdot \frac {\partial q _ {j} ^ {2}}{\partial y _ {i} ^ {1}} \cdot \frac {\mathrm{d} y _ {i} ^ {1}}{\mathrm{d} q _ {i} ^ {1}} = \sum_ {j = 1} ^ {M _ {2}} p _ {j} ^ {2} w _ {j i} ^ {2} \cdot (\sigma_ {i} ^ {1}) ^ {\prime} (q _ {i} ^ {1}),
$$

$$
\frac {\partial y}{\partial w _ {j i} ^ {1}} = \frac {\partial y}{\partial q _ {j} ^ {1}} \cdot \frac {\partial q _ {j} ^ {1}}{\partial w _ {j i} ^ {1}} = p _ {j} ^ {1} x _ {i}, \quad \frac {\partial y}{\partial b _ {j} ^ {1}} = \frac {\partial y}{\partial q _ {j} ^ {1}} \cdot \frac {\partial q _ {j} ^ {1}}{\partial b _ {j} ^ {1}} = p _ {j} ^ {1} \cdot 1 = p _ {j} ^ {1}.
$$

更进一步, 可以计算 y 对每个 $x _ { i }$ 的导数:

$$
\frac {\partial y}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} \frac {\partial y}{\partial q _ {j} ^ {1}} \cdot \frac {\partial q _ {j} ^ {1}}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} p _ {j} ^ {1} w _ {j i} ^ {1}, \quad i = 1, \ldots , d.
$$

更进一步, 可以计算 y 对每个 $x _ { i }$ 的导数:

$$
\frac {\partial y}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} \frac {\partial y}{\partial q _ {j} ^ {1}} \cdot \frac {\partial q _ {j} ^ {1}}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} p _ {j} ^ {1} w _ {j i} ^ {1}, \quad i = 1, \ldots , d.
$$

上述从输出层出发, 从后往前依次计算 $\begin{array} { r } { p ^ { L + 1 } , \frac { \partial y } { \partial w _ { i } ^ { L + 1 } } , \frac { \partial y } { \partial b ^ { L + 1 } } , p _ { i } ^ { L } , \frac { \partial y } { \partial w _ { j i } ^ { L } } , \frac { \partial y } { \partial b _ { j } ^ { L } } , \dots , } \end{array}$ $\begin{array} { r } { p _ { i } ^ { 1 } , \frac { \partial y } { \partial w _ { j i } ^ { 1 } } , \frac { \partial y } { \partial b _ { j } ^ { 1 } } , \frac { \partial y } { \partial x _ { i } } } \end{array}$ 的过程称为反向传播(backward propagation).

反向传播过程可以用矩阵-向量乘法的方式进行实现. 具体的算法流程可参考讲义1.2.3的 Algorithm 2.

## 一、前向传播，依次计算 qj, yj,qj,yj ., qj,yj $a ^ { n - 1 } - b ^ { n - 1 }$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter3%281%29/images/de914ff1c1882bad39714938470099b7fd48a377579d711a05b6a3dda00a21b9.jpg)

## $\frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } \times \frac { 1 } { 2 } = \frac { 1 } { 2 }$

图前向传播和反向传播首先进行一次前向传播计算各隐藏层的 $q _ { j } ^ { \ell } , y _ { j } ^ { \ell }$ 和输出层的 $q ^ { L + 1 } , y ;$ 之后进行一次反向传播, 计算输出层的 $\begin{array} { r } { p ^ { L + 1 } , \frac { \partial y } { \partial w _ { i } ^ { L + 1 } } , \frac { \partial y } { \partial b ^ { L + 1 } } } \end{array}$ 和各隐藏层的 $\begin{array} { r } { p _ { i } ^ { \ell } , \frac { \partial \bar { y } } { \partial w _ { j i } ^ { \ell } } , \frac { \partial y } { \partial b _ { j } ^ { \ell } } } \end{array}$ , 最终计算 $\textstyle { \frac { \partial y } { \partial x _ { i } } }$

可以估算反向传播算法的复杂度: 一个从 $\mathbb { R } ^ { d }$ 到 R 的具有简单激活函数(如 ReLU,logistic 函数)的全连接神经网络, 设其深度为 L+1 (含 L 个隐藏层), 每个隐藏层宽度均为则作一次反向传播所需的计算复杂度为 $O \left( ( L - 1 ) M ^ { 2 } + \dot { d } M \right)$

对非全连接的前馈神经网络, 也可以用类似的方式推导出相应的算法, 用于计算网络对各参数及输入变量的偏导数问题: 如果有一个从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的具有简单激活函数(如 ReLU, logistic 函数)的全连接神经网络, 我们要计算它的所有输出 $y _ { j } \ ( j = 1 , \ldots , d ^ { \prime } )$ 对所有参数的偏导数的值. 是否需要重复上述前向传播反向传播 <sup>′</sup> 次问题: 如果有一个从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的具有简单激活函数(如 ReLU, logistic 函数)的全连接神经网络, 我们要计算它的所有输出 $y _ { j } \ ( j = 1 , \ldots , d ^ { \prime } )$ 对所有参数的偏导数的值. 是否需要重复上述前向传播反向传播 <sup>′</sup> 次回答: “前向传播” 只需执行一次; 反向传播需要独立执行 $d ^ { \prime }$ 次 (从每个 $y _ { j }$ 出发各走一次).

问题: 如果有一个从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的具有简单激活函数(如 ReLU, logistic 函数)的全连接神经网络, 我们要计算它的所有输出 $y _ { j } \ ( j = 1 , \ldots , d ^ { \prime } )$ 对所有参数的偏导数的值. 是否需要重复上述“前向传播+反向传播” $\bar { d } ^ { \prime }$ 次?

回答: “前向传播” 只需执行一次; 反向传播需要独立执行 $d ^ { \prime }$ 次 (从每个 $y _ { j }$ 出发各走一次).

问题: 在实际应用中, $d ^ { \prime }$ 可能很大, 那么“计算神经网络对所有参数的导数”这件事, 计算量岂不是很大问题: 如果有一个从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的具有简单激活函数(如 ReLU, logistic 函数)的全连接神经网络, 我们要计算它的所有输出 $y _ { j } \ ( j = 1 , \ldots , d ^ { \prime } )$ 对所有参数的偏导数的值. 是否需要重复上述“前向传播+反向传播” $\bar { d } ^ { \prime }$ 次?

回答: “前向传播” 只需执行一次; 反向传播需要独立执行 $d ^ { \prime }$ 次 (从每个 $y _ { j }$ 出发各走一次).

问题: 在实际应用中, $d ^ { \prime }$ 可能很大, 那么“计算神经网络对所有参数的导数”这件事, 计算量岂不是很大回答: 在实际应用中, 我们不需要计算“神经网络对所有参数的导数”, 而是直接计算 “损失函数 L 对所有网络参数的导数”, 方法类似上述的“前向传播+反向传播”. 由于 ${ \mathcal { L } } -$ 定是一个标量因此只要走一次前向传播反向传播即可

## 逼近理论的表述方式我们时常会研究某些函数类的逼近理论. 以一元多项式为例, 用 Stone-Weierstrass 定理可以证明如下结论定理3.1 设 $f ( x )$ 是定义在 $[ a , b ] \subset$ R 上的连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及某个 N 次多项式 $p ( x ) = { a _ { 0 } } + a _ { 1 } x + \cdot \cdot \cdot + a _ { N } x ^ { N }$ 使得

$$
\| p - f \| _ {L ^ {\infty} ([ a, b ])} <   \varepsilon .
$$

## 逼近理论的表述方式我们时常会研究某些函数类的逼近理论. 以一元多项式为例, 用 Stone-Weierstrass 定理可以证明如下结论定理3.1 设 $f ( x )$ 是定义在 [a,b] ⊂ R 上的连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及某个 N 次多项式 $p ( x ) \dot { = } a _ { 0 } \dot { + } a _ { 1 } x + \cdot \cdot \cdot + a _ { N } x ^ { N }$ 使得

$$
\| p - f \| _ {L ^ {\infty} ([ a, b ])} <   \varepsilon .
$$

另一方面利用正交多项式的性质可以证明如下结论定理3.2 设 f(x) 是定义在 $[ a , b ] \subset \mathbb { R }$ 上的 s 阶连续可导函数. 则对任意正整数 N, 存在某个 N 次多项式 $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { N } x ^ { N }$ 使得

$$
\| p - f \| _ {L ^ {2} ([ a, b ])} \leq C \| f \| \cdot N ^ {- s},
$$

其中 C 是一个仅与 a,b 有关的常数; ∥f∥ 是 f 的某个范数(如Sobolev范数).

## 逼近理论的表述方式我们时常会研究某些函数类的逼近理论. 以一元多项式为例, 用 Stone-Weierstrass 定理可以证明如下结论定理3.1 设 f(x) 是定义在 [a,b] ⊂ R 上的连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及某个 N 次多项式 $p ( x ) \dot { = } a _ { 0 } \dot { + } a _ { 1 } x + \cdot \cdot \cdot + a _ { N } x ^ { N }$ 使得

$$
\| p - f \| _ {L ^ {\infty} ([ a, b ])} <   \varepsilon .
$$

另一方面利用正交多项式的性质可以证明如下结论定理3.2 设 f(x) 是定义在 $[ a , b ] \subset \mathbb { R }$ 上的 s 阶连续可导函数. 则对任意正整数 N, 存在某个 N 次多项式 $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { N } x ^ { N }$ 使得

$$
\| p - f \| _ {L ^ {2} ([ a, b ])} \leq C \| f \| \cdot N ^ {- s},
$$

其中 C 是一个仅与 a,b 有关的常数; ∥f∥ 是 f 的某个范数(如Sobolev范数).

这两个定理的描述在逻辑上有什么区别?

第一个定理, 只保证存在一个多项式可以达到指定的逼近精度 ε, 但没有指明所需多项式的次数与的关系第二个定理, 保证存在一个 N 次多项式, 可以达到 $C \| f \| \cdot N ^ { - s }$ 的逼近精度, 即指明了具体的误差界.

第一个定理, 只保证存在一个多项式可以达到指定的逼近精度 ε, 但没有指明所需多项式的次数与的关系第二个定理, 保证存在一个 N 次多项式, 可以达到 $C \| f \| \cdot N ^ { - s }$ 的逼近精度, 即指明了具体的误差界.

第二个定理的结论更强第一个定理, 只保证存在一个多项式可以达到指定的逼近精度 ε, 但没有指明所需多项式的次数与的关系第二个定理, 保证存在一个 N 次多项式, 可以达到 $C \| f \| \cdot N ^ { - s }$ 的逼近精度, 即指明了具体的误差界.

## 第二个定理的结论更强对多项式、分片多项式、傅里叶级数等经典函数结构, 已经有比较完善的逼近理论. 而对神经网络, 相关的逼近理论研究仍处在初步的探索阶段.

## 万能近似定理所谓的“万能近似定理”(Universal Approximation Theorem)是比较经典的神经网络逼近定理. 其中一个简单的版本如下:

定理设激活函数 $\sigma$ 是一个连续函数且不是多项式是正整数是 $\mathbb { R } ^ { d }$ 上的有界闭集. 设 $f : K \to \mathbb { R }$ 是一个连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及一个宽度为 N的二层全连接神经网络

$$
\phi (x) = W ^ {2} \sigma (W ^ {1} x + b ^ {1}), \quad W ^ {1} \in \mathbb {R} ^ {N \times d},   b ^ {1} \in \mathbb {R} ^ {N \times 1},   W ^ {2} \in \mathbb {R} ^ {1 \times N},
$$

使得

$$
| \phi (x) - f (x) | <   \varepsilon , \quad \forall x \in K.
$$

## 万能近似定理所谓的“万能近似定理”(Universal Approximation Theorem)是比较经典的神经网络逼近定理. 其中一个简单的版本如下:

定理设激活函数 $\sigma$ 是一个连续函数且不是多项式是正整数是 $\mathbb { R } ^ { d }$ 上的有界闭集. 设 f : K → R 是一个连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及一个宽度为 N的二层全连接神经网络

$$
\phi (x) = W ^ {2} \sigma (W ^ {1} x + b ^ {1}), \quad W ^ {1} \in \mathbb {R} ^ {N \times d},   b ^ {1} \in \mathbb {R} ^ {N \times 1},   W ^ {2} \in \mathbb {R} ^ {1 \times N},
$$

使得

$$
| \phi (x) - f (x) | <   \varepsilon , \quad \forall x \in K.
$$

在定理3.3中, 我们令 $\varepsilon = \varepsilon _ { n } \to 0$ , 则可推出存在一个神经网络序列 $( \phi _ { n } ) _ { n }$ , 它对 $f$ 的逼近误差收敛到零, 即 $( \phi _ { n } ) _ { n }$ 一致收敛到 $f .$

## 万能近似定理所谓的“万能近似定理”(Universal Approximation Theorem)是比较经典的神经网络逼近定理. 其中一个简单的版本如下:

定理设激活函数 $\sigma$ 是一个连续函数且不是多项式是正整数是 $\mathbb { R } ^ { d }$ 上的有界闭集. 设 f : K → R 是一个连续函数. 则对任意 $\varepsilon > 0$ , 存在正整数 N 以及一个宽度为 N的二层全连接神经网络

$$
\phi (x) = W ^ {2} \sigma (W ^ {1} x + b ^ {1}), \quad W ^ {1} \in \mathbb {R} ^ {N \times d},   b ^ {1} \in \mathbb {R} ^ {N \times 1},   W ^ {2} \in \mathbb {R} ^ {1 \times N},
$$

使得

$$
| \phi (x) - f (x) | <   \varepsilon , \quad \forall x \in K.
$$

在定理3.3中, 我们令 $\varepsilon = \varepsilon _ { n } \to 0$ , 则可推出存在一个神经网络序列 $( \phi _ { n } ) _ { n }$ , 它对 $f$ 的逼近误差收敛到零, 即 $( \phi _ { n } ) _ { n }$ 一致收敛到 $f$ .

然而定理只给出了达到逼近误差的神经网络的存在性并没有给出一个显式的误差界. 我们无法通过定理3.3知道一个宽度为 N 的二层神经网络, 对给定函数 f 的最佳逼近误差是多少全连接神经网络不仅可以逼近连续函数, 还可以逼近可测函数、可积函数、H¨older连续函数和其它一些特殊的函数具体的逼近性质将在后续章节介绍

## 本章总结

▶ 神经元、激活函数、前馈神经网络、前向传播、反向传播 (参考: 自编讲义1.1.1-1.2.4)

▶ 万能近似定理 (参考: https://en.wikipedia.org/wiki/Universal approximation theorem)