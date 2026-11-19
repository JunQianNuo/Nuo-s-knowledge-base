---
raw_title: Homework05
subject: Homework05
source: Homework05.pdf
status: mineru解析
parser: mineru
---

## 《深度学习》课程作业05

Exercise 1

令 $[ a , b ] \subset \mathbb { R }$ . 证明对任意 $g \in C ( [ a , b ] )$ 和 $\epsilon > 0$ , 存在正整数 n, 实数 $\alpha _ { 1 } , \ldots , \alpha _ { n }$ 和非负整数$m _ { 1 } , \ldots , m _ { n }$ 使得对任意 $x \in [ a , b ]$ , 成立

$$
\left| g (x) - \sum_ {i = 1} ^ {n} \alpha_ {i} e ^ {m _ {i} x} \right| <   \epsilon .
$$

Exercise 2

令 $[ a , b ] \subset \mathbb { R }$ . 证明: 以下函数集

$$
\mathcal {N} = \left\{f: [ a, b ] \to \mathbb {R}, f (x) = a _ {0} + \alpha \sum_ {n = 1} ^ {N} \gamma_ {n} H (x + b _ {n}): a _ {0}, \alpha , b _ {n} \in \mathbb {R}, \gamma_ {n} \in \{1, - 1 \}, N \in \mathbb {Z} ^ {+} \right\}
$$

在 $C ( [ a , b ] )$ 上稠密.

Exercise 3

设 $g : [ 0 , 1 ] $ R 是一个 Lipschitz 连续函数, 即 g 满足

$$
| g (x) - g (y) | \leq c _ {L} | x - y |, \quad \forall x, y \in [ 0, 1 ],
$$

其中 $c _ { L } > 0$ 是 Lipschitz 常数. 证明: 对任意整数 $N > 0$ , 存在一个如下的两层神经网络

$$
f (x) = \sum_ {n = 1} ^ {N} a _ {n} \sigma (w _ {n} x + b _ {n}) + b,
$$

其中 $\sigma ( x ) = \operatorname* { m a x } ( 0 , x )$ 以及 $a _ { n } , w _ { n } , b _ { n } , b \in \mathbb { R }$ 使得

$$
\sup _ {x \in [ 0, 1 ]} | f (x) - g (x) | \leq \frac {c _ {L}}{N}.
$$

Exercise 4

找到一个从 $\mathbb { R } ^ { 2 }$ 到 R 的两层 ReLU 神经网络且宽度不超过 3, 使得它精确拟合数据集$\{ ( ( 0 , 1 ) , 0 ) , ( ( 0 , - 1 ) , 1 ) , ( ( 0 , 0 ) , 2 ) , ( ( 1 , 0 ) , 4 ) , ( ( - 1 , 0 ) , 5 ) \}$

Exercise 5

(1) 找到一个全连接神经网络 $f _ { 1 } ( x )$ 使其满足

• f<sub>1</sub>(x) = x<sup>4</sup> + 4x<sup>3</sup> + 10x<sup>2</sup> + 12x + 12, ∀x ∈ R;

$f _ { 1 }$ 正好包含两个隐藏层, 且每层激活函数均为 $\sigma ( x ) = x ^ { 2 }$

(2) 找到一个全连接神经网络 $f _ { 2 } ( x )$ 使其满足

$f _ { 2 } ( x ) = 8 \cos ^ { 4 } ( x ) + 2 \sin ^ { 2 } ( x ) , \forall x \in \mathbb { R } ;$

• $f _ { 2 }$ 正好包含一个隐藏层, 其激活函数为 $\sigma ( x ) = \cos ( x )$

## Exercise 6

(1) 将 $f ( x _ { 1 } , x _ { 2 } ) = \operatorname* { m i n } \{ x _ { 1 } , x _ { 2 } \}$ 表示成一个宽度为4的浅层全连接神经网络(矩阵-向量形式).

(2) 根据定理10.7, 将一个 $[ 0 , 1 ] ^ { 2 }$ 上的连续函数 $f ( x _ { 1 } , x _ { 2 } )$ 表示成一个前馈神经网络(矩阵-向量形式),其含两个隐藏层, 第一层激活函数是 $\psi ,$ 第二层激活函数是 $\chi .$ . 并画出网络连接示意图.

Exercise 7 令 $g \in C ^ { 1 } ( [ 0 , 1 ] )$ . 证明: 对任意 $\varepsilon > 0 ,$ , 存在一个神经网络

$$
f (x) = \sum_ {n = 1} ^ {N} a _ {n} \sigma \left(w _ {n} x + b _ {n}\right) + c _ {1} x + c _ {0},
$$

其中 $\sigma ( x ) = \ln ( 1 + e ^ { x } )$ 是 softplus 激活函数, $N \in \mathbb { N } ^ { + }$ 且 $a _ { n } , w _ { n } , b _ { n } , c _ { 1 } , c _ { 0 } \in \mathbb { R }$ , 使得对任意 $x \in [ 0 , 1 ]$ 成立 $| f ( x ) - g ( x ) | \leq \varepsilon x$

提示: $\begin{array} { r } { \sigma { ' } ( x ) = \frac { 1 } { 1 + e ^ { - x } } } \end{array}$ 是 logistic 激活函数.