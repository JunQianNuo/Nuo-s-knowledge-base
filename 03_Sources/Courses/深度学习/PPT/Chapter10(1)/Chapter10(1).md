---
raw_title: Chapter10(1)
subject: Chapter10(1)
source: Chapter10(1).pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](images/cd1c48829bd29288a9b28622d6036575abad20a2a807911bec5d63cdf0f025b2.jpg)

## 十、精确学习

## 精确学习对某些特殊的目标函数 $f ( x ) : D  \mathbb { R }$ (其中 $D \subset \mathbb { R } ^ { d }$ 是 f 的定义域), 我们可以通过对学习器 $\phi ( x ; \theta )$ 进行训练, 使得 $\phi ( x ; \theta )$ 与 $f ( x )$ 在 D 上完全相等, 即

$$
f (x) = \phi (x; \theta), \quad \forall x \in D,
$$

则称学习器 $\phi ( x ; \theta )$ 能够精确学习 $f ( x )$ , 或者称 $f ( x )$ 在定义域上能够被 $\phi ( x ; \theta )$ 表示.

## 精确学习对某些特殊的目标函数 $f ( x ) : D  \mathbb { R }$ (其中 $D \subset \mathbb { R } ^ { d }$ 是 $f$ 的定义域), 我们可以通过对学习器 $\phi ( x ; \theta )$ 进行训练, 使得 $\phi ( x ; \theta )$ 与 $f ( x )$ 在上完全相等即

$$
f (x) = \phi (x; \theta), \quad \forall x \in D,
$$

则称学习器 $\phi ( x ; \theta )$ 能够精确学习 $f ( x )$ , 或者称 $f ( x )$ 在定义域上能够被 $\phi ( x ; \theta )$ 表示.

有时, 不存在一个具体的 $\phi ( x ; \theta )$ 在 D 上与 $f ( x )$ 完全相等, 但是存在一系列 $\phi ( x ; \theta )$ 在$D$ 上无限逼近 $f ( x )$ (这里 $\phi ( x ; \theta )$ 的架构固定不变). 具体地, 对任意小的 $\epsilon > 0$ , 总是存在参数 $\theta _ { \epsilon }$ , 使得

$$
| f (x) - \phi (x; \theta_ {\epsilon}) | <   \epsilon , \quad \forall x \in D,
$$

则我们也称 $\phi ( x ; \theta )$ 能够对 f 进行精确学习.

## 学习有限点集上的函数设 $\Gamma = \{ x _ { 1 } , x _ { 2 } , \dots , x _ { N } \}$ 是 $\mathbb { R } ^ { d }$ 上的一个有限集. 可以定义 Γ 上的函数 $f : \Gamma \to \mathbb { R } .$ . 考虑用神经网络对这样的函数进行精确学习, 即找一个神经网络 $\phi ( x ; \theta )$ 使得

$$
\phi (x _ {n}; \theta) = f (x _ {n}), \quad n = 1, \ldots , N.\tag{1}
$$

## 学习有限点集上的函数设 $\Gamma = \{ x _ { 1 } , x _ { 2 } , \dots , x _ { N } \}$ 是 $\mathbb { R } ^ { d }$ 上的一个有限集. 可以定义 Γ 上的函数 f : Γ → R. 考虑用神经网络对这样的函数进行精确学习, 即找一个神经网络 $\phi ( x ; \theta )$ 使得

$$
\phi (x _ {n}; \theta) = f (x _ {n}), \quad n = 1, \dots , N.\tag{1}
$$

考虑宽度为 M 的浅层神经网络

$$
\phi (x; \theta) = \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}),\tag{2}
$$

其中 $\theta = \{ a _ { m } , w _ { m } , b _ { m } \} , w _ { m } \in \mathbb { R } ^ { d } , a _ { m } , b _ { m } \in \mathbb { R }$ ; M 是一个正整数.

记 $y _ { n } = f ( x _ { n } )$ , 并将(2)代入(1)得

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {1} + b _ {m}) = y _ {1},
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {2} + b _ {m}) = y _ {2},\tag{3}
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {N} + b _ {m}) = y _ {N}.
$$

记 $y _ { n } = f ( x _ { n } )$ , 并将(2)代入(1)得

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {1} + b _ {m}) = y _ {1},
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {2} + b _ {m}) = y _ {2},\tag{3}
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {N} + b _ {m}) = y _ {N}.
$$

这是一个关于 $\{ a _ { m } , w _ { m } , b _ { m } \}$ 的代数方程组. $\phi ( x ; \theta )$ 能否精确学习 f(x) 就取决于该方程组是否有解将方程组 (3) 写成矩阵和向量乘积的形式

$$
\boldsymbol {A} _ {w, b} \boldsymbol {a} = \boldsymbol {y},\tag{4}
$$

其中

$$
\begin{array}{c} \boldsymbol {A} _ {w, b} = \left[ \begin{array}{c c c c} \sigma (w _ {1} ^ {\top} x _ {1} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {1} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {1} + b _ {M}) \\ \sigma (w _ {1} ^ {\top} x _ {2} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {2} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {2} + b _ {M}) \\ \vdots & \vdots & \ddots & \vdots \\ \sigma (w _ {1} ^ {\top} x _ {N} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {N} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {N} + b _ {M}) \end{array} \right], \\ \boldsymbol {a} = \left[ \begin{array}{c} a _ {1} \\ a _ {2} \\ \vdots \\ a _ {M} \end{array} \right], \boldsymbol {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {N} \end{array} \right]. \end{array}
$$

将方程组 (3) 写成矩阵和向量乘积的形式

$$
\boldsymbol {A} _ {w, b} \boldsymbol {a} = \boldsymbol {y},\tag{4}
$$

其中

$$
\begin{array}{c} \boldsymbol {A} _ {w, b} = \left[ \begin{array}{c c c c} \sigma (w _ {1} ^ {\top} x _ {1} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {1} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {1} + b _ {M}) \\ \sigma (w _ {1} ^ {\top} x _ {2} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {2} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {2} + b _ {M}) \\ \vdots & \vdots & \ddots & \vdots \\ \sigma (w _ {1} ^ {\top} x _ {N} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {N} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {N} + b _ {M}) \end{array} \right], \\ \boldsymbol {a} = \left[ \begin{array}{c} a _ {1} \\ a _ {2} \\ \vdots \\ a _ {M} \end{array} \right], \boldsymbol {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {N} \end{array} \right]. \end{array}
$$

我们考虑 $M = N$ , 即网络宽度等于 Γ 的点数的简单情形, 此时矩阵 $A _ { w , b }$ 为方阵. 可以证明, 当 $\sigma$ 是 ReLU 激活函数时, 可以找到一组 $\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ , 使得矩阵 $A _ { w , b }$ 可逆.

将方程组 (3) 写成矩阵和向量乘积的形式

$$
\boldsymbol {A} _ {w, b} \boldsymbol {a} = \boldsymbol {y},\tag{4}
$$

其中

$$
\begin{array}{c} \boldsymbol {A} _ {w, b} = \left[ \begin{array}{c c c c} \sigma (w _ {1} ^ {\top} x _ {1} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {1} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {1} + b _ {M}) \\ \sigma (w _ {1} ^ {\top} x _ {2} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {2} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {2} + b _ {M}) \\ \vdots & \vdots & \ddots & \vdots \\ \sigma (w _ {1} ^ {\top} x _ {N} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {N} + b _ {2}) & \dots & \sigma (w _ {M} ^ {\top} x _ {N} + b _ {M}) \end{array} \right], \\ \boldsymbol {a} = \left[ \begin{array}{c} a _ {1} \\ a _ {2} \\ \vdots \\ a _ {M} \end{array} \right], \boldsymbol {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {N} \end{array} \right]. \end{array}
$$

我们考虑 $M = N$ , 即网络宽度等于 Γ 的点数的简单情形, 此时矩阵 $A _ { w , b }$ 为方阵. 可以证明, 当 $\sigma$ 是 ReLU 激活函数时, 可以找到一组 $\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ , 使得矩阵 $A _ { w , b }$ 可逆.

命题令 $x _ { 1 } , \ldots , x _ { N }$ 为 $\mathbb { R } ^ { d }$ 上互不相同的点设 $M = N$ 且 $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ . 则存在具体的 $w _ { m } \in \mathbb R ^ { d } , b _ { m } \in \mathbb R , m = 1 , \dots , N$ 使得相应的矩阵 $A _ { w , b }$ 是一个对角元非零的下三角矩阵, 从而 $A _ { w , b }$ 可逆.

于是, 只需要取命题 10.1中的 $\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ 代入 (4), 就可解出 $\pmb { a } = \pmb { A } _ { w , b } ^ { - 1 } \pmb { y }$ . 由这些$\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ 以及解出的 $\{ a _ { m } \} _ { m = 1 } ^ { M }$ 为参数的神经网络 $\phi ( x ; \theta )$ , 就对 f(x) 进行了精确学习. 总之, 有以下结论于是, 只需要取命题 10.1中的 $\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ 代入 (4), 就可解出 $\pmb { a } = \pmb { A } _ { w , b } ^ { - 1 } \pmb { y }$ . 由这些$\{ w _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ 以及解出的 $\{ a _ { m } \} _ { m = 1 } ^ { M }$ 为参数的神经网络 $\phi ( x ; \theta )$ , 就对 $f ( x )$ 进行了精确学习. 总之, 有以下结论定理10.2 设 $\Gamma = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { N } \} \subset \mathbb { R } ^ { d }$ 且 $x _ { n } \ ( n = 1 , \ldots , N )$ 互不相同. 令$f : \Gamma \to \mathbb { R }$ . 则存在一个浅层 ReLU 神经网络 $\begin{array} { r } { \phi ( x ) = \sum _ { m = 1 } ^ { N } a _ { m } \sigma ( w _ { m } ^ { \top } x + b _ { m } ) } \end{array}$ ), 其中$\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ , 满足

$$
\phi (x _ {n}) = f (x _ {n}), \quad \forall 1 \leq n \leq N.
$$

可以证明定理对其它许多类型的激活函数如函数也是成立的

## ReLU神经网络的精确学习考虑一个从 $\mathbb { R } ^ { d }$ 到 R 的多层 ReLU 神经网络

$$
\phi (x; \theta) = a ^ {\top} \sigma \Bigl (W ^ {L} \sigma \bigl (\dots \sigma (W ^ {1} x + b ^ {1}) \dots \bigr) + b ^ {L} \Bigr) + b,\tag{5}
$$

其中 $\sigma ( t ) = \mathrm { R e L U } ( t ) = \operatorname* { m a x } \{ 0 , t \} ; a \in \mathbb { R } ^ { M _ { L } \times 1 } , b \in \mathbb { R } , W ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times M _ { \ell - 1 } }$ $b ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times 1 } ~ ( M _ { \ell } \in \dot { \mathbb { Z } } ^ { + } ~ \vec { \mathbb { x } } \mathbf { \mathscr { t } } ~ \ell = 1 , \dots , L ; ~ M _ { 0 } : = d )$ 是所有参数.

## ReLU神经网络的精确学习考虑一个从 $\mathbb { R } ^ { d }$ 到 R 的多层 ReLU 神经网络

$$
\phi (x; \theta) = a ^ {\top} \sigma \Bigl (W ^ {L} \sigma \bigl (\dots \sigma (W ^ {1} x + b ^ {1}) \dots \bigr) + b ^ {L} \Bigr) + b,\tag{5}
$$

其中 $\sigma ( t ) = \mathrm { R e L U } ( t ) = \operatorname* { m a x } \{ 0 , t \} ; a \in \mathbb { R } ^ { M _ { L } \times 1 } , b \in \mathbb { R } , W ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times M _ { \ell - 1 } }$ $b ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times 1 } ~ ( M _ { \ell } \in \dot { \mathbb { Z } } ^ { + } ~ \vec { \mathbb { x } } \mathbf { \mathscr { t } } ~ \ell = 1 , \dots , L ; ~ M _ { 0 } : = d )$ 是所有参数.

容易证明 $\phi ( x ; \theta )$ 是 $\mathbb { R } ^ { d }$ 上的分片线性函数. 因此, 若目标函数 f(x) 也是分片线性函数,则 $\phi ( x ; \theta )$ 有可能对 f(x) 实现精确学习.

ReLU 激活函数 $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ 满足表达式

$$
t = \sigma (t) - \sigma (- t),
$$

$$
| t | = \sigma (t) + \sigma (- t).
$$

ReLU 激活函数 $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ 满足表达式

$$
t = \sigma (t) - \sigma (- t),
$$

$$
| t | = \sigma (t) + \sigma (- t).
$$

于是, 二元最大值函数 $\operatorname* { m a x } \{ x { x _ { 1 } , x _ { 2 } } \}$ 可以表示成

$$
\begin{array}{r l} \max \{x _ {1}, x _ {2} \} & = \frac {1}{2} (x _ {1} + x _ {2} + | x _ {1} - x _ {2} |) \\ & = \frac {1}{2} (\sigma (x _ {1} + x _ {2}) - \sigma (- x _ {1} - x _ {2}) + \sigma (x _ {1} - x _ {2}) + \sigma (- x _ {1} + x _ {2})) \\ & = \frac {1}{2} \sigma (x _ {1} + x _ {2}) - \frac {1}{2} \sigma (- x _ {1} - x _ {2}) + \frac {1}{2} \sigma (x _ {1} - x _ {2}) + \frac {1}{2} \sigma (- x _ {1} + x _ {2}), \end{array}
$$

即一个宽度为4的浅层ReLU神经网络.

对多元最大值函数可以用数学归纳法证明如下结论定理10.3 函数 $f ( x _ { 1 } , \dots , x _ { d } ) = \operatorname* { m a x } \{ x _ { 1 } , \dots , x _ { d } \}$ 能够被精确表示成一个深度为 $L + 1$ 的 ReLU 神经网络, 其中

$$
L = \left\{ \begin{array}{l l} {k,} & {\text {如果} d = 2 ^ {k}, k \text {是某个正整数},} \\ {\lfloor \log_ {2} d \rfloor + 1,} & {\text {如果} d \neq 2 ^ {k}, \text {对任意正整数} k.} \end{array} \right.
$$

证明: 讲义2.4.2.

对多元最大值函数, 可以用数学归纳法证明如下结论:

定理10.3 函数 $f ( x _ { 1 } , \dots , x _ { d } ) = \operatorname* { m a x } \{ x _ { 1 } , \dots , x _ { d } \}$ 能够被精确表示成一个深度为 $L + 1$ 的 ReLU 神经网络, 其中

$$
L = \left\{ \begin{array}{l l} {k,} & {\text {如果} d = 2 ^ {k}, k \text {是某个正整数},} \\ {\lfloor \log_ {2} d \rfloor + 1,} & {\text {如果} d \neq 2 ^ {k}, \text {对任意正整数} k.} \end{array} \right.
$$

证明: 讲义2.4.2.

上述关于函数的结论都可以类似推广到函数上只需利用关系式

$$
\min \{x _ {1}, x _ {2} \} = \frac {1}{2} \left(x _ {1} + x _ {2} - | x _ {1} - x _ {2} |\right).
$$

一个浅层而较宽的 ReLU 神经网络可以表示成一个深层而较窄的 ReLU 网络. 具体结论如下:

一个浅层而较宽的 ReLU 神经网络可以表示成一个深层而较窄的 ReLU 网络. 具体结论如下:

定理10.4 设 $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ . 令 $\phi : [ 0 , 1 ] ^ { d } $ R 是一个宽度为 M 的浅层 ReLU 神经网络, 即

$$
\phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}),
$$

其中 $a _ { 0 } , a _ { m } , b _ { m } \in \mathbb { R } \ \mathsf { a n d } \ w _ { m } \in \mathbb { R } ^ { d }$ . 则存在一个深层 ReLU 神经网络 $\hat { \phi } : [ 0 , 1 ] ^ { d } \to$ R,它恰好包含 $M + 1$ 个宽度为 $d + 2$ 的隐藏层, 即

$$
\hat {\phi} (x) = \hat {a} ^ {\top} \sigma \Big (\hat {W} ^ {M + 1} \sigma \big (\dots \sigma (\hat {W} ^ {1} x + \hat {b} ^ {1}) \dots \big) + \hat {b} ^ {M + 1} \Big) + \hat {b},
$$

其中 $\hat { a } , \hat { b } ^ { \ell } \in \mathbb { R } ^ { d + 2 } ( \ell = 1 , \dots , M + 1 ) , \hat { W } ^ { 1 } \in \mathbb { R } ^ { d \times ( d + 2 ) } , \hat { W } ^ { \ell } \in \mathbb { R } ^ { ( d + 2 ) \times ( d + 2 ) }$ $( \ell = 2 , \dots , M + 1 ) , \hat { b } \in \mathbb { R }$ , 且满足

$$
\phi (x) = \hat {\phi} (x), \quad \forall x \in [ 0, 1 ] ^ {d}.
$$

证明: 讲义2.4.2.

实际上, 一个连续的分片线性函数总能被表示成一个深层的 ReLU 神经网络. 具体如下实际上一个连续的分片线性函数总能被表示成一个深层的神经网络具体如下定理10.5 令 $f : \mathbb { R } ^ { d } $ R 是一个连续的分片线性函数. 则 f 能够被精确表示成一个深度不超过 $\lfloor \log _ { 2 } ( d + 1 ) \rfloor + 1$ 的 ReLU 神经网络.

证明: 讲义2.4.2.

## Kolmogorov-Arnold-Sprecher定理之前关于神经网络对目标函数进行精确学习的结论中网络的激活函数是确定的如ReLU), 但宽度不确定, 即网络可以任意宽. 与之相反的, 另一类关于精确学习的结论中,网络的深度和宽度均确定但激活函数的形式不确定

## Kolmogorov-Arnold-Sprecher定理之前关于神经网络对目标函数进行精确学习的结论中网络的激活函数是确定的如但宽度不确定即网络可以任意宽与之相反的另一类关于精确学习的结论中网络的深度和宽度均确定但激活函数的形式不确定

Arnold 和 Kolmogorov 在1959年证明了如下定理定理10.6 设 $d \geq 2$ 为整数. 则存在单调的单变量函数 $\psi _ { i j } ( \cdot )$

$( i = 1 , \ldots , d ; ~ j = 1 , \ldots , 2 d + 1 )$ 使得对任意 $f ( x _ { 1 } , \dots , x _ { d } ) \in C ( I _ { d } )$ , 它能够被精确表示成

$$
f (x _ {1}, \dots , x _ {d}) = \sum_ {j = 1} ^ {2 d + 1} \chi_ {j} \left(\sum_ {i = 1} ^ {d} \psi_ {i j} (x _ {i})\right),\tag{6}
$$

其中 $\chi _ { j } ( \cdot ) ~ ( j = 1 , \ldots , 2 d + 1 )$ 是单变量函数.

注意: 该定理中, 函数 $\chi _ { j } ( \cdot )$ 可能与 f 有关, 即随 f 的变化而变化; 但函数 $\psi _ { i j } ( \cdot )$ 是固定的, 即独立于 f.

特别的, 当 d = 2 时, $f ( x )$ 可以表示成

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}) = \chi_ {1} \left(\psi_ {1 1} (x _ {1}) + \psi_ {2 1} (x _ {2})\right) + \chi_ {2} \left(\psi_ {1 2} (x _ {1}) + \psi_ {2 2} (x _ {2})\right) \\ & \qquad + \chi_ {3} \left(\psi_ {1 3} (x _ {1}) + \psi_ {2 3} (x _ {2})\right) + \chi_ {4} \left(\psi_ {1 4} (x _ {1}) + \psi_ {2 4} (x _ {2})\right) \\ & \qquad + \chi_ {5} \left(\psi_ {1 5} (x _ {1}) + \psi_ {2 5} (x _ {2})\right). \end{array}
$$

特别的, 当 d = 2 时, $f ( x )$ 可以表示成

$$
\begin{array}{l} f (x _ {1}, x _ {2}) = \chi_ {1} \left(\psi_ {1 1} (x _ {1}) + \psi_ {2 1} (x _ {2})\right) + \chi_ {2} \left(\psi_ {1 2} (x _ {1}) + \psi_ {2 2} (x _ {2})\right) \\ \qquad + \chi_ {3} \left(\psi_ {1 3} (x _ {1}) + \psi_ {2 3} (x _ {2})\right) + \chi_ {4} \left(\psi_ {1 4} (x _ {1}) + \psi_ {2 4} (x _ {2})\right) \\ \qquad + \chi_ {5} \left(\psi_ {1 5} (x _ {1}) + \psi_ {2 5} (x _ {2})\right). \end{array}
$$

这是一个具有两个隐藏层的神经网络(如下图所示)

![](images/9838e4ea2796436552ebf55a622b657422b13f3573e7057454d1bce3ee4edd5c.jpg)  
图: 用于精确表示二维连续函数的神经网络(含有两个隐藏层; 其每一条边的权重均为1)

## Sprecher 将定理10.6改进为如下结果定理10.7 设 $d \geq 2$ 为整数. 则存在与 d 相关的单调递增的单变量函数 $\psi ( \cdot )$ , 满足$\psi ( [ 0 , 1 ] ) = [ 0 , 1 ]$ 及以下性质对任意 $\delta > 0$ 存在有理数 $\epsilon \left( 0 < \epsilon < \delta \right)$ 以及常数 $\rho$ 使得对任意 $f ( x _ { 1 } , \dots , x _ { d } ) \in C ( I _ { d } )$ , 它能够被精确表示成

$$
f (x _ {1}, \dots , x _ {d}) = \sum_ {j = 1} ^ {2 d + 1} \chi \left(\sum_ {i = 1} ^ {d} \rho^ {i} \psi (x _ {i} + (j - 1) \epsilon) + j - 1\right),\tag{7}
$$

其中 $\chi ( \cdot )$ 是一个单变量连续函数

Sprecher 将定理10.6改进为如下结果定理10.7 设 $d \geq 2$ 为整数. 则存在与 d 相关的单调递增的单变量函数 $\psi ( \cdot )$ , 满足$\psi ( [ 0 , 1 ] ) = [ 0 , 1 ]$ 及以下性质对任意 $\delta > 0 ,$ 存在有理数 $\epsilon \left( 0 < \epsilon < \delta \right)$ 以及常数 $\rho$ 使得对任意 $f ( x _ { 1 } , \dots , x _ { d } ) \in C ( I _ { d } )$ , 它能够被精确表示成

$$
f (x _ {1}, \dots , x _ {d}) = \sum_ {j = 1} ^ {2 d + 1} \chi \left(\sum_ {i = 1} ^ {d} \rho^ {i} \psi (x _ {i} + (j - 1) \epsilon) + j - 1\right),\tag{7}
$$

其中 $\chi ( \cdot )$ 是一个单变量连续函数注意: 类似地, 函数 χ(·) 可能与 f 有关, 但函数 $\psi ( \cdot )$ 独立于 f.

特别的, 当 d = 2 时, f(x) 可以表示成

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}) = \chi (\rho \psi (x _ {1}) + \rho^ {2} \psi (x _ {2})) \\ & \qquad + \chi (\rho \psi (x _ {1} + \epsilon) + \rho^ {2} \psi (x _ {2} + \epsilon) + 1) + \chi (\rho \psi (x _ {1} + 2 \epsilon) + \rho^ {2} \psi (x _ {2} + 2 \epsilon) + 2) \\ & \qquad + \chi (\rho \psi (x _ {1} + 3 \epsilon) + \rho^ {2} \psi (x _ {2} + 3 \epsilon) + 3) + \chi (\rho \psi (x _ {1} + 4 \epsilon) + \rho^ {2} \psi (x _ {2} + 4 \epsilon) + 4), \end{array}
$$

特别的, 当 d = 2 时, $f ( x )$ 可以表示成

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}) = \chi (\rho \psi (x _ {1}) + \rho^ {2} \psi (x _ {2})) \\ & \qquad + \chi (\rho \psi (x _ {1} + \epsilon) + \rho^ {2} \psi (x _ {2} + \epsilon) + 1) + \chi (\rho \psi (x _ {1} + 2 \epsilon) + \rho^ {2} \psi (x _ {2} + 2 \epsilon) + 2) \\ & \qquad + \chi (\rho \psi (x _ {1} + 3 \epsilon) + \rho^ {2} \psi (x _ {2} + 3 \epsilon) + 3) + \chi (\rho \psi (x _ {1} + 4 \epsilon) + \rho^ {2} \psi (x _ {2} + 4 \epsilon) + 4), \end{array}
$$

这是一个具有两个隐藏层的神经网络其第一层激活函数是 $\psi ,$ 第二层激活函数是 $\chi .$

上一章提到, 给定一个连续函数 $f : [ 0 , 1 ] \to \mathbb { R }$ , 对任意的 ϵ > 0, 总存在足够大的正整数$M > 0$ 及宽度为 M 的浅层 ReLU 神经网络 $\phi ,$ 使得 $\begin{array} { r } { \operatorname* { m a x } _ { x \in [ 0 , 1 ] } | \phi ( x ) - f ( x ) | < \epsilon } \end{array}$

上一章提到, 给定一个连续函数 $f : [ 0 , 1 ] \to \mathbb { R }$ , 对任意的 ϵ > 0, 总存在足够大的正整数M > 0 及宽度为 M 的浅层 ReLU 神经网络 $\phi ,$ 使得 $\begin{array} { r } { \operatorname* { m a x } _ { x \in [ 0 , 1 ] } | \phi ( x ) - f ( x ) | < \epsilon } \end{array}$

一般随着不断变小所需要的会不断变大这意味着当浅层神经网络能够对 f 有越来越高的逼近精度时, 所需要的宽度也会越来越大, 即所需自由参数的数量越来越多.

上一章提到, 给定一个连续函数 f : [0,1] → R, 对任意的 ϵ > 0, 总存在足够大的正整数M > 0 及宽度为 M 的浅层 ReLU 神经网络 $\phi ,$ 使得 $\mathrm { m a x } _ { x \in [ 0 , 1 ] } | \phi ( x ) - f ( x ) | < \epsilon$

一般随着不断变小所需要的会不断变大这意味着当浅层神经网络能够对 f 有越来越高的逼近精度时, 所需要的宽度也会越来越大, 即所需自由参数的数量越来越多.

而在定理10.7的精确逼近中, 网络的宽度和深度都是固定的, 但激活函数 χ(·) 随着目标函数的变化而不断变化上一章提到, 给定一个连续函数 f : [0,1] → R, 对任意的 ϵ > 0, 总存在足够大的正整数M > 0 及宽度为 M 的浅层 ReLU 神经网络 $\phi ,$ 使得 $\mathrm { m a x } _ { x \in [ 0 , 1 ] } | \phi ( x ) - f ( x ) | < \epsilon$

一般随着不断变小所需要的会不断变大这意味着当浅层神经网络能够对 f 有越来越高的逼近精度时, 所需要的宽度也会越来越大, 即所需自由参数的数量越来越多.

而在定理10.7的精确逼近中, 网络的宽度和深度都是固定的, 但激活函数 χ(·) 随着目标函数的变化而不断变化问题是否存在一种既固定了宽度和深度又固定了激活函数的全连接神经网络架构仅通过改变自由参数的值就可以以任意小的误差即逼近给定的连续函数

## 有限参数神经网络的精确学习如下定义 σ:

$$
\sigma (t) = \left\{ \begin{array}{l l} \sigma_ {1} (t), & t \geq 0, \\ \sigma_ {2} (t), & t <   0, \end{array} \right.
$$

$$
\text {其中} \sigma_ {1} (t) = {\left\{ \begin{array}{l l} {| t |,} & {t \in [ - 1, 1 ],} \\ {\sigma_ {1} (t \pm 2),} & {t \in (- \infty , \infty),} \end{array} \right.} \quad \sigma_ {2} (t) = {\frac {t}{| t | + 1}},   t \in \mathbb {R}.
$$

![](images/f32dacc829031258b44c6b700410e1855f0fa0d2de4e80c7eb2e27b2dcb038a5.jpg)  
图: σ(t) 在 [−10, 10] 上.

定理10.8 (Zhang, Shen & Yang, 2022) 给定问题维数 $d \geq 1$

(i) 给定 $f \in C ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ , 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
| \phi (x) - f (x) | <   \epsilon , \quad \forall x \in I _ {d};
$$

(ii) 给定 $f \in L ^ { p } ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ , 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
\| \phi - f \| _ {p, I _ {d}} = \left(\int_ {I _ {d}} | \phi (x) - f (x) | ^ {p} \mathrm{d} x\right) ^ {1 / p} <   \epsilon .
$$

定理10.8 (Zhang, Shen & Yang, 2022) 给定问题维数 $d \geq 1$

(i) 给定 $f \in C ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
| \phi (x) - f (x) | <   \epsilon , \quad \forall x \in I _ {d};
$$

(ii) 给定 $f \in L ^ { p } ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ , 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
\| \phi - f \| _ {p, I _ {d}} = \left(\int_ {I _ {d}} | \phi (x) - f (x) | ^ {p} \mathrm{d} x\right) ^ {1 / p} <   \epsilon .
$$

定理10.8中的全连接神经网络一共有

$$
(d \times M + M) + (M \times M + M) \times (L - 1) + M \times 1 + 1 \sim d ^ {4}
$$

个自由参数. 而在定理的证明中, 实际仅需要调整 $5 4 3 7 ( d + 1 ) ( 2 d + 1 ) = O ( d ^ { 2 } )$ 个自由参数即可满足条件.

定理10.8 (Zhang, Shen & Yang, 2022) 给定问题维数 $d \geq 1$

(i) 给定 $f \in C ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
| \phi (x) - f (x) | <   \epsilon , \quad \forall x \in I _ {d};
$$

(ii) 给定 $f \in L ^ { p } ( I _ { d } )$ . 对任意 $\epsilon > 0 ,$ , 存在一个宽度为 $3 6 d ( 2 d + 1 )$ , 深度为 12, 激活函数为 $\sigma ( t )$ 的全连接神经网络 $\phi ( x )$ , 使得

$$
\| \phi - f \| _ {p, I _ {d}} = \left(\int_ {I _ {d}} | \phi (x) - f (x) | ^ {p} \mathrm{d} x\right) ^ {1 / p} <   \epsilon .
$$

定理10.8中的全连接神经网络一共有

$$
(d \times M + M) + (M \times M + M) \times (L - 1) + M \times 1 + 1 \sim d ^ {4}
$$

个自由参数. 而在定理的证明中, 实际仅需要调整 $5 4 3 7 ( d + 1 ) ( 2 d + 1 ) = O ( d ^ { 2 } )$ 个自由参数即可满足条件.

定理表明仅仅需要调整固定个数的参数值就可以让固定架构的神经网络无限逼近任意连续函数或 $L ^ { p }$ 函数. 然而, 在实际计算中, 该架构的神经网络并不实用, 因为参数的值在逼近过程中往往会变得巨大

## 本章总结

▶ 有限点集上函数的精确学习, ReLU神经网络的精确学习, K-A-S定理, 有限参数网络的精确学习(参考: 自编讲义2.4)