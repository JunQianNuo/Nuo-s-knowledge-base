---
raw_title: Homework02
subject: Homework02
source: Homework02.pdf
status: mineru解析
parser: mineru
---

# 《深度学习》课程作业02

# (请同学们课后自行完成，不需提交)

## Exercise 1 (8pts)

一、构造一个全连接神经网络 $\phi (  { \boldsymbol { { x } } } ) : \mathbb { R } ^ { 2 } \to$ R, 使其满足如下条件:

(1) ϕ 具有两个隐藏层, 每层的激活函数均为 ReLU, 且宽度均为 2. 输出层激活函数为恒等函数;

(2) ϕ 的所有自由参数均不等于零;

(3) $\phi ( 1 , - 1 ) = 1 , \phi ( 1 , 1 ) = 2 , \phi ( - 1 , - 1 ) = - 1 , \phi ( - 1 , 1 ) = 1 .$

二、构造一个全连接神经网络 $\phi ( x )$ : R → R, 使其满足如下条件:

(1) ϕ 具有一个隐藏层, 其激活函数为 $\sigma ( t ) = | t | ,$ , 且宽度不大于 10. 输出层激活函数为恒等函数;

(2) $\phi ( 1 ) = \phi ( 3 ) = \phi ( 5 ) = \phi ( 7 ) = 1 , \phi ( 2 ) = \phi ( 4 ) = \phi ( 6 ) = \phi ( 8 ) = - 1 .$

Exercise 2 (6pts)

证明: 一个深度为 $L + 1$ , 宽度为 $M ,$ 从 $\mathbb { R } ^ { d }$ 到 $\mathbb { R } ^ { d ^ { \prime } }$ 的全连接神经网络, 作一次前向传播所需的计算复杂度(即加减乘除的次数)为 $O ( ( L - 1 ) M ^ { 2 } + d M + d ^ { \prime } M )$

Exercise 3 (6pts)

给定全连接神经网络

$$
\phi (x) = \left[ \begin{array}{c c c} 1 & 1 & 2 \end{array} \right] \sigma_ {2} \left(\left[ \begin{array}{c c} 1 & - 2 \\ 2 & - 1 \\ 0 & 1 \end{array} \right] \sigma_ {1} \left(\left[ \begin{array}{c c c} 2 & 1 & - 1 \\ - 2 & 1 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]\right) + \left[ \begin{array}{c} 1 \\ 2 \\ 3 \end{array} \right]\right),
$$

其中 $\sigma _ { 1 } ( t ) = \mathrm { m a x } ( 0 , t ) , \sigma _ { 2 } ( t ) = t ^ { 2 }$ . 设 $x ^ { * } = ( 1 , 2 , 3 )$ . 用前向传播和反向传播计算 $\phi ( x ^ { * } ) , \ \frac { \partial \phi } { \partial x _ { i } }$ $( i = 1 , 2 )$ 及 $\phi$ 对所有参数的导数.

Exercise 4 (8pts)

非全连接的一般神经网络也可以用类似的前向传播和反向传播来计算函数值和函数对参数的导数.给定如下图所示的前馈神经网络 $y = \phi ( x )$ :

设 $\sigma _ { 1 } ( t ) = \operatorname { R e L U } ( t ) , \sigma _ { 2 } ( t ) = \sigma _ { 3 } ( t ) = t ^ { 2 } , \sigma _ { 4 } ( t ) = | t |$ , 并设权重 $w _ { 1 } , \ldots , w _ { 8 } = ( 1 , 2 , 1 , 2 , 3 , - 1 , - 2 , - 3 )$ 偏置 $b _ { 1 } , \dots , b _ { 4 } = ( - 2 , 4 , 4 , 2 )$ . 令 $x ^ { * } = ( 1 , - 1 )$

(1) 计算 $f ( x ^ { * } )$ 的值;

(2) 在上述给定的权重和偏置下, 用链式法则计算 $\begin{array} { r } { \frac { \partial y } { \partial w _ { i } } \ ( i = 1 , 2 , 3 , 4 ) } \end{array}$ 和 $\begin{array} { r } { \frac { \partial y } { \partial x _ { i } } \ ( i = 1 , 2 ) } \end{array}$ 在 $x ^ { * }$ 处的值.

Exercise 5 (6pts)

证明: 函数 $f ( x ) = 8 x _ { 1 } + 1 2 x _ { 2 } + x _ { 1 } ^ { 2 } - 2 x _ { 2 } ^ { 2 }$ 只有一个驻点, 且是鞍点.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/%E4%BD%9C%E4%B8%9A/Homework02/images/fc7e86cef3532a65fe4e4e948c999f523426a9381b96df55f5d5a6384ac9b47d.jpg)

Exercise 6 (6pts)

设函数 $f ( x ) = ( x _ { 1 } + x _ { 2 } ^ { 2 } ) ^ { 2 }$ . 在 (0, 1) 点处对 f 作最速下降线搜索, 求最优的步长 $\eta ^ { * }$ .

Exercise 7 (30pts)

用 Python + numpy 命令库编程完成以下任务. (要求手动实现神经网络架构及前向/反向传播, 不能使用 PyTorch 等深度学习命令库直接实现)

(1) 编写函数, 以实现全连接神经网络 $f : \mathbb { R } ^ { d } $ R,

$$
f (x) = W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b ^ {L + 1}
$$

的前向和反向传播. 其中, 所有隐藏层的激活函数均为 $\sigma ( \cdot ) ;$ ; 输出层的激活函数为恒等函数. 可参考如下模版:

def propagation(x, W\_list, b\_list, activation\_type):

<sub>#</sub> 设定<sub>,</sub> 初始化等

<sub>#</sub> 前向传播

<sub>#</sub> 反向传播

return fx, DfDx, DfDW, DfDb

• 输入参数中, x 表示输入的向量 $x ^ { * } i$ <sub>W\_list</sub> 是一个列表(list), 储存神经网络各层的权重矩阵$W ^ { 1 } , W ^ { 2 } , \dots , W ^ { L + 1 }$ ; 类似地, <sub>b\_list</sub> 储存神经网络各层的偏置向量 $b ^ { 1 } , b ^ { 2 } , \dots , b ^ { L + 1 }$ ;<sub>activation\_type</sub> 是一个字符串, 表示激活函数 σ 的类型, 例如 $" \mathrm { R e L U " } , \ " \mathrm { t a n h " }$ 等.

• 输入维数 d 可以通过读取 $x ^ { * }$ 的长度或 $W ^ { 1 }$ 的列数得到, 如 $\mathtt { d } { = } \mathtt { l e n } ( \mathtt { x } )$ 或 $\mathtt { d } { = } \mathtt { W } _ { - } \mathtt { l i s t } [ 0 ]$ .shape[1].

• 输出参数中, fx 表示 f(x<sup>∗</sup>); DfDx 是一个 1D-array, 表示 $\left( \frac { \partial f ( x ^ { * } ) } { \partial x _ { 1 } } , \ldots , \frac { \partial f ( x ^ { * } ) } { \partial x _ { d } } \right)$ ; <sub>DfDW</sub> 是一个3D-array, 其中 DfDW[l][i][j] 表示 $\frac { \partial f ( \boldsymbol { x } ^ { * } ) } { \partial w _ { i j } ^ { \ell } }$ ; <sub>DfDb</sub> 是一个 $2 \mathrm { D - a r r a y } ,$ 其中 DfDb[l][i] 表示

$$
\frac {\partial f (x ^ {*})}{\partial b _ {i} ^ {\ell}}.
$$

(2) 对(1)中的函数进行测试: 令 $d = 3 , L = 5$ , 各隐藏层宽度分别为 2,4,6,8,10. 自定义一组网络参数 $\{ W ^ { \ell } , b ^ { \ell } \} _ { \ell = 1 } ^ { L + 1 }$ (例如, 用 <sub>numpy.random.uniform</sub> 生成随机矩阵), 以及 5 个输入向量 $x ^ { ( 1 ) } , \cdots , x ^ { ( 5 ) }$ 输出相应的 $\begin{array} { r } { \bar { f } ( x ^ { ( k ) } ) , \frac { \partial f ( x ^ { ( k ) } ) } { \partial x _ { i } } , \frac { \partial f ( x ^ { ( k ) } ) } { \partial w _ { i j } ^ { \ell } } } \end{array}$ 和 $\frac { \partial f ( \boldsymbol { x } ^ { ( k ) } ) } { \partial b _ { i } ^ { \ell } } \ ( k = 1 , \cdot \cdot \cdot , 5 )$

(3) 已知有限差分公式 $\begin{array} { r } { g ^ { \prime } ( t ) \approx \frac { g ( t + h ) - g ( t - h ) } { 2 h } } \end{array}$ , 其中 g 是一个光滑的可微函数, 近似误差为 $O ( h ^ { 2 } )$ . 用前向传播配合上述公式再次计算 $\begin{array} { r } { \frac { \partial f ( \overline { { \boldsymbol { x } } ^ { ( k ) } } ) } { \partial x _ { 1 } } , \frac { \partial f ( \boldsymbol { x } ^ { ( k ) } ) } { \partial w _ { 1 1 } ^ { 1 } } , \frac { \partial f ( \boldsymbol { x } ^ { ( k ) } ) } { \partial w _ { 2 2 } ^ { 2 } } } \end{array}$ 和 $\frac { \partial f ( x ^ { ( k ) } ) } { \partial b _ { 3 } ^ { 3 } } \ ( k = 1 , \cdots , 5 )$ 的近似值, 并与(2) 中的结果作比较.

(4) 从计算复杂度上讨论前向/反向传播和有限差分公式计算 $\big \{ \frac { \partial f } { \partial x _ { i } } , \frac { \partial f } { \partial w _ { i j } ^ { \ell } } , \frac { \partial f } { \partial b _ { i } ^ { \ell } } \big \}$ 的优劣性.

## Exercise 8 (30pts)

用 Python + numpy/matplotlib 等命令库编程完成以下任务. (要求手动实现各优化算法的迭代格式, 不能使用 torch.optim 下的优化算法命令直接实现)

已知 Rosenbrock 函数 $f ( x ) = 1 0 0 ( x _ { 2 } - x _ { 1 } ^ { 2 } ) ^ { 2 } + ( 1 - x _ { 1 } ) ^ { 2 }$ . 分别用最速下降法 $( \eta = 0 . 0 1 )$ , 动量法 $( \mu = 0 . 1 , \ \eta = 0 . 0 1 )$ , AdaGrad算法 $( \eta = 0 . 0 1 )$ , RMSProp算法 $( \gamma = 0 . 1 , \ \eta = 0 . 0 1 )$ , Adam算法 $( \beta _ { 1 } = 0 . 9 , \beta _ { 2 } = 0 . 9 9 9 , \eta = 0 . 0 1 , \epsilon = 0 . 0 0 1 ) , \mathrm { { A d a M a x } }$ 算法 $( \beta _ { 1 } = 0 . 9 , \beta _ { 2 } = 0 . 9 9 9 , \eta = 0 . 0 1 )$ 对f(x) 进行优化. 迭代总次数为 1000. 分别尝试使用初值 (1, 0), (0, 1), (−1, −1) 和 (3, 3). 将每种方法的数值解与全局最小值 (1,1) 比较并计算误差, 并用合理的图表进行展示.