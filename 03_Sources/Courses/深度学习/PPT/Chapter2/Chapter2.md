---
raw_title: Chapter2
subject: Chapter2
source: Chapter2.pdf
status: mineru解析
parser: mineru
---

## 深度学习 Deep Learning

授课人：顾亦奇

yiqigu@uestc.edu.cn

# 电子科技大学数学科学学院

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/e771b16d615ba74e74070c52b016098d27a10db54187ae5c8ea199d41299c3f3.jpg)

## 二、机器学习基础

## 复杂函数世界上存在着非常多的函数/映射关系. 有些函数较简单, 可以用简单的数学表达式描述,例如

▶ 以速度 $v _ { 0 }$ 进行匀速直线运动: $s = v _ { 0 } t$

▶ 质量为 $m _ { 1 }$ 和 $m _ { 2 }$ 的两个物体之间的万有引力: $\begin{array} { r } { F = \frac { G m _ { 1 } m _ { 2 } } { r ^ { 2 } } } \end{array}$

▶ 质能方程 $E = m c ^ { 2 }$

## 复杂函数世界上存在着非常多的函数/映射关系. 有些函数较简单, 可以用简单的数学表达式描述,例如

▶ 以速度 $v _ { 0 }$ 进行匀速直线运动: $s = v _ { 0 } t ;$

▶ 质量为 $m _ { 1 }$ 和 $m _ { 2 }$ 的两个物体之间的万有引力: $\begin{array} { r } { F = \frac { G m _ { 1 } m _ { 2 } } { r ^ { 2 } } } \end{array}$

▶ 质能方程 $E = m c ^ { 2 }$

而更多的函数则以复杂的隐式方式存在, 例如

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/39abd56cb3295893a0a848961aea8991ad58a5cde5a9dde06da53589ff694090.jpg)

手写数字分类函数将一张手写数字图片映射到中的某个类别

## Ai智能回答

## 地球是圆的吗?

地球的形状并不是完美的球体，而是稍微扁平的椭球体。科学家通过精密的测量发现，地球的两极部位略扁，赤道稍鼓，因此地球的形状更接近于一个不规则的椭圆球体，有时被套张地比喻为“梨形体”。这种形状是由于地球自转所产生的离心力和引力的共同作用造成的。此外，月食时观察到的月面黑影的圆弧形状，也是地球不是完美球体的一个证据

(d) 问答函数: 将一句话语(提问)映射到另一句话语(回答)

## 复杂函数这些”复杂”函数 y = f(x) 的特点:

▶ 变量(x和y)的形式复杂, 不仅可以是实数、向量、矩阵, 还可以是图片、声音、视频等等;

▶ 函数关系复杂, 无法用简单的数学表达式表示;

▶ 可能不连续, x 的小扰动可能导致 y 的突变.

## 复杂函数这些”复杂”函数 y = f(x) 的特点:

▶ 变量(x和y)的形式复杂, 不仅可以是实数、向量、矩阵, 还可以是图片、声音、视频等等;

▶ 函数关系复杂, 无法用简单的数学表达式表示;

▶ 可能不连续, x 的小扰动可能导致 y 的突变.

在实际应用中我们虽无法用数学表达式简单表达这些函数但可以用数学模型来模拟这些函数的效果. 机器学习, 就是用一个数学模型来近似(也称学习) 某个函数 f. 此时, f可称为目标函数(target function).

## 复杂函数这些”复杂”函数 y = f(x) 的特点:

▶ 变量(x和y)的形式复杂, 不仅可以是实数、向量、矩阵, 还可以是图片、声音、视频等等;

▶ 函数关系复杂, 无法用简单的数学表达式表示;

▶ 可能不连续, x 的小扰动可能导致 y 的突变.

在实际应用中我们虽无法用数学表达式简单表达这些函数但可以用数学模型来模拟这些函数的效果. 机器学习, 就是用一个数学模型来近似(也称学习) 某个函数 f. 此时, f可称为目标函数(target function).

当 f 的值域是离散分布时(例如上述数字图片分类问题, f 只有10种不同的取值), 该函数近似问题称为分类问题(classification); 当 f 的值域是连续分布时(例如R), 该问题称为回归问题(regression);

## 样本与数据集对某个函数 $f ,$ , 给定一个具体的变量 $x _ { n }$ , 就有一个对应的 $y _ { n } = f ( x _ { n } )$ 与之对应. 这里,$x _ { n }$ 称为一个样本(example)或特征向量(feature vector), 它的每个分量称为特征(feature); $y _ { n }$ 称为 $x _ { n }$ 的标签(label).

## 样本与数据集对某个函数 $f ,$ , 给定一个具体的变量 $x _ { n }$ , 就有一个对应的 $y _ { n } = f ( x _ { n } )$ 与之对应. 这里,$x _ { n }$ 称为一个样本(example)或特征向量(feature vector), 它的每个分量称为特征(feature); $y _ { n }$ 称为 $x _ { n }$ 的标签(label).

一定数量的二元组 $( x _ { n } , y _ { n } )$ 可以形成一个集合, 称为数据集(data set), 表示为$\{ ( x _ { n } , y _ { n } ) \}$ . 数据集中的每一个二元组 $( x _ { n } , y _ { n } )$ 称为一个数据点(data point). 机器学习通常是基于数据的, 因此机器学习方法也属于由数据驱动的方法.

## 样本与数据集对某个函数 $f ,$ , 给定一个具体的变量 $x _ { n }$ , 就有一个对应的 $y _ { n } = f ( x _ { n } )$ 与之对应. 这里,$x _ { n }$ 称为一个样本(example)或特征向量(feature vector), 它的每个分量称为特征(feature); $y _ { n }$ 称为 $x _ { n }$ 的标签(label).

一定数量的二元组 $( x _ { n } , y _ { n } )$ 可以形成一个集合, 称为数据集(data set), 表示为$\{ ( x _ { n } , y _ { n } ) \}$ . 数据集中的每一个二元组 $( x _ { n } , y _ { n } )$ 称为一个数据点(data point). 机器学习通常是基于数据的, 因此机器学习方法也属于由数据驱动的方法.

有一些机器学习任务只涉及特征向量 $x ,$ 不涉及标签 y, 它们一般称为无监督学习(unsupervised learning), 相应的数据集也只包含 $x _ { n }$ 的信息. 对应的, 既涉及特征向量又涉及标签的机器学习称为监督学习(supervised learning).

## 学习器在参数化机器学习模型(parametric model)中, 可以用一类已知具体结构的带参函数 f<sup>ˆ</sup>来对目标函数作近似. 此时, f<sup>ˆ</sup> 称为学习器(learner)或估计器(estimator). 例如, 在线性回归中的一次函数以及多项式回归中的多项式都是学习器而它们待确定的系数称为参数. 这类带参函数形成的函数集合有时也称为假设空间(hypothesis space).

## 学习器在参数化机器学习模型(parametric model)中, 可以用一类已知具体结构的带参函数 f<sup>ˆ</sup>来对目标函数作近似. 此时, f<sup>ˆ</sup> 称为学习器(learner)或估计器(estimator). 例如, 在线性回归中的一次函数, 以及多项式回归中的多项式都是学习器, 而它们待确定的系数称为参数. 这类带参函数形成的函数集合有时也称为假设空间(hypothesis space).

一个带参函数若关于它的参数向量是线性关系或仿射关系, 则称为线性结构; 否则, 称为非线性结构.

## 学习器在参数化机器学习模型(parametric model)中, 可以用一类已知具体结构的带参函数 $\hat { f }$ 来对目标函数作近似. 此时, $\hat { f }$ 称为学习器(learner)或估计器(estimator). 例如, 在线性回归中的一次函数以及多项式回归中的多项式都是学习器而它们待确定的系数称为参数. 这类带参函数形成的函数集合有时也称为假设空间(hypothesis space).

一个带参函数若关于它的参数向量是线性关系或仿射关系, 则称为线性结构; 否则, 称为非线性结构例如线性结构

▶ 多项式如 $\hat { f } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + \cdot \cdot \cdot + a _ { P } x ^ { P }$ 参数为 $\{ a _ { 0 } , a _ { 1 } , . . . , a _ { P } \}$

▶ 傅里叶级数如

$$
\hat {f} (x) = a _ {0} + a _ {1} \cos (x) + b _ {1} \sin (x) + \dots + a _ {M} \cos (M x) + b _ {M} \sin (M x).
$$

参数为 $\{ a _ { 0 } , a _ { 1 } , b _ { 1 } , . . . , a _ { P } , b _ { P } \}$ ;

▶ 有限元函数如 $\hat { f } ( x ) = a _ { 0 } \phi _ { 0 } ( x ) + \cdot \cdot \cdot + a _ { M } \phi _ { M } ( x )$ , 其中 $\phi _ { m } ( x )$ 是已知的有限元形函数.参数为 $\{ a _ { 0 } , a _ { 1 } , \dotsc , a _ { M } \}$ ;

## 学习器在参数化机器学习模型(parametric model)中, 可以用一类已知具体结构的带参函数 $\hat { f }$ 来对目标函数作近似. 此时, $\hat { f }$ 称为学习器(learner)或估计器(estimator). 例如, 在线性回归中的一次函数以及多项式回归中的多项式都是学习器而它们待确定的系数称为参数. 这类带参函数形成的函数集合有时也称为假设空间(hypothesis space).

一个带参函数若关于它的参数向量是线性关系或仿射关系, 则称为线性结构; 否则, 称为非线性结构例如

## 线性结构

▶ 多项式如 $\hat { f } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 } + \cdot \cdot \cdot + a _ { P } x ^ { P }$ 参数为 $\{ a _ { 0 } , a _ { 1 } , . . . , a _ { P } \}$

▶ 傅里叶级数如

$$
\hat {f} (x) = a _ {0} + a _ {1} \cos (x) + b _ {1} \sin (x) + \dots + a _ {M} \cos (M x) + b _ {M} \sin (M x).
$$

参数为 $\{ a _ { 0 } , a _ { 1 } , b _ { 1 } , . . . , a _ { P } , b _ { P } \}$ ;

▶ 有限元函数如 $\hat { f } ( x ) = a _ { 0 } \phi _ { 0 } ( x ) + \cdot \cdot \cdot + a _ { M } \phi _ { M } ( x )$ , 其中 $\phi _ { m } ( x )$ 是已知的有限元形函数.

参数为 $\{ a _ { 0 } , a _ { 1 } , \dotsc , a _ { M } \}$ ;

非线性结构

▶ 深度神经网络.

## 学习器的容量粗略的说, 一个函数类的容量(capacity)是指能被它有效拟合的函数的范围大小. 例如,全体五次多项式比全体三次多项式能够拟合更多的函数, 因此全体五次多项式具有更大的容量. 然而, 数学上对容量的严格定义则比较复杂, 常用的有 Vapnik–Chervonenkis 维数和 Rademacher 复杂度.

## 学习器的容量粗略的说, 一个函数类的容量(capacity)是指能被它有效拟合的函数的范围大小. 例如,全体五次多项式比全体三次多项式能够拟合更多的函数, 因此全体五次多项式具有更大的容量. 然而, 数学上对容量的严格定义则比较复杂, 常用的有 Vapnik–Chervonenkis 维数和 Rademacher 复杂度.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/b6fb29949cc761c6c6fbb3329a64029a6b4736d9b593f74d355b6f736f49f86e.jpg)  
图函数空间的包含关系其容量也由小到大

## 1-D 问题设函数 $f : [ a , b ]  \mathbb { R }$ 为一个目标函数. 设 $x _ { n } \in [ a , b ] , y _ { n } = f ( x _ { n } ) , n = 1 , \ldots , N$ , 并形成数据集 $\{ ( \stackrel { \cdot } { x } _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$

## 1-D 问题设函数 $f : [ a , b ]  \mathbb { R }$ 为一个目标函数. 设 $x _ { n } \in [ a , b ] , y _ { n } = f ( x _ { n } ) , n = 1 , \ldots , N$ , 并形成数据集 $\{ ( \stackrel { \cdot } { x } _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$

我们选取某类函数 ${ \hat { f } } ( x )$ 来对 f 作近似, 即需要减小 ${ \hat { f } } ( x _ { n } )$ 与 $y _ { n }$ 的差距为描述这种差距, 引进某个损失函数 $l ( t _ { 1 } , t _ { 2 } ) : \mathbb { R } ^ { 2 }  \mathbb { R }$ . 常见的损失函数如下

▶ $\ell ^ { p } .$ -损失(常用 $p = 2 ) \colon l ( t _ { 1 } , t _ { 2 } ) = | t _ { 1 } - t _ { 2 } | ^ { p } ;$

▶ 交叉熵(cross-entropy)损失: $l ( t _ { 1 } , t _ { 2 } ) = - t _ { 2 } \ln t _ { 1 }$

<sup>▶</sup> Jefrey distance: $\begin{array} { r } { l ( t _ { 1 } , t _ { 2 } ) = \frac { 1 } { 2 } ( t _ { 1 } - t _ { 2 } ) ( \ln t _ { 1 } - \ln t _ { 2 } ) } \end{array}$

## 1-D 问题设函数 $f : [ a , b ]  \mathbb { R }$ 为一个目标函数. 设 $x _ { n } \in [ a , b ] , y _ { n } = f ( x _ { n } ) , n = 1 , \ldots , N$ , 并形成数据集 $\{ ( \stackrel { \cdot } { x } _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$

我们选取某类函数 ${ \hat { f } } ( x )$ 来对 f 作近似, 即需要减小 ${ \hat { f } } ( x _ { n } )$ 与 $y _ { n }$ 的差距为描述这种差距, 引进某个损失函数 $l ( t _ { 1 } , t _ { 2 } ) : \mathbb { R } ^ { 2 }  \mathbb { R }$ . 常见的损失函数如下

▶ $\ell ^ { p } .$ -损失(常用 $p = 2 ) \colon l ( t _ { 1 } , t _ { 2 } ) = | t _ { 1 } - t _ { 2 } | ^ { p } ;$

▶ 交叉熵(cross-entropy)损失: $l ( t _ { 1 } , t _ { 2 } ) = - t _ { 2 } \ln t _ { 1 }$

<sup>▶</sup> Jefrey distance: $\begin{array} { r } { l ( t _ { 1 } , t _ { 2 } ) = \frac { 1 } { 2 } ( t _ { 1 } - t _ { 2 } ) ( \ln t _ { 1 } - \ln t _ { 2 } ) } \end{array}$

对每个数据点作用一次损失函数, 并求平均数, 就得到整个平均损失:

$$
L [ \hat {f} ] = \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}), y _ {n}).
$$

## 1-D 问题设函数 $f : [ a , b ]  \mathbb { R }$ 为一个目标函数. 设 $x _ { n } \in [ a , b ] , y _ { n } = f ( x _ { n } ) , n = 1 , \ldots , N$ , 并形成数据集 $\{ ( \stackrel { \cdot } { x } _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$

我们选取某类函数 ${ \hat { f } } ( x )$ 来对 f 作近似, 即需要减小 ${ \hat { f } } ( x _ { n } )$ 与 $y _ { n }$ 的差距为描述这种差距, 引进某个损失函数 $l ( t _ { 1 } , t _ { 2 } ) : \mathbb { R } ^ { 2 }  \mathbb { R }$ . 常见的损失函数如下

▶ $\ell ^ { p } .$ -损失(常用 $p = 2 ) \colon l ( t _ { 1 } , t _ { 2 } ) = | t _ { 1 } - t _ { 2 } | ^ { p } ;$

▶ 交叉熵(cross-entropy)损失: $l ( t _ { 1 } , t _ { 2 } ) = - t _ { 2 } \ln t _ { 1 }$

<sup>▶</sup> Jefrey distance: $\begin{array} { r } { l ( t _ { 1 } , t _ { 2 } ) = \frac { 1 } { 2 } ( t _ { 1 } - t _ { 2 } ) ( \ln t _ { 1 } - \ln t _ { 2 } ) } \end{array}$

对每个数据点作用一次损失函数, 并求平均数, 就得到整个平均损失:

$$
L [ \hat {f} ] = \frac {1}{N} \sum_ {n = 1} ^ {N} l (\hat {f} (x _ {n}), y _ {n}).
$$

之后, 需要对 $L [ \hat { f } ]$ 作最小化, 即

$$
\min _ {\hat {f}} L [ \hat {f} ].
$$

有时, 在不混淆的情况下, 我们也称 $L [ \hat { f } ]$ 为损失函数.

## 训练与训练误差

## 训练与训练误差上述最小化问题可使用各种优化算法(也称优化器(optimizer))进行求解, 如梯度下降法、L-BFGS拟牛顿法. 而这个优化的计算过程, 称为训练(training). 而数据集$\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 也称为训练集(training set)

## 训练与训练误差上述最小化问题可使用各种优化算法(也称优化器(optimizer))进行求解, 如梯度下降法、L-BFGS拟牛顿法. 而这个优化的计算过程, 称为训练(training). 而数据集$\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 也称为训练集(training set)

特例当 $\hat { f }$ 是线性结构且 $l ( t _ { 1 } , t _ { 2 } ) = ( t _ { 1 } - t _ { 2 } ) ^ { 2 }$ 为平方函数时该优化问题是凸优化只需求解线性方程组的最小二乘解即可

## 训练与训练误差上述最小化问题可使用各种优化算法(也称优化器(optimizer))进行求解, 如梯度下降法、L-BFGS拟牛顿法. 而这个优化的计算过程, 称为训练(training). 而数据集$\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ 也称为训练集(training set)

特例当 $\hat { f }$ 是线性结构且 $l ( t _ { 1 } , t _ { 2 } ) = ( t _ { 1 } - t _ { 2 } ) ^ { 2 }$ 为平方函数时该优化问题是凸优化只需求解线性方程组的最小二乘解即可通过训练, 可得到上述最小化问题的一个解, 仍然记作 ${ \hat { f } } .$ 此时, 我们称损失函数 $L [ \hat { f } ]$ 的值为训练损失（training loss). 进一步, 可以计算 $\hat { f }$ 与真正的目标函数 f 在训练集上的误差, 如 $\ell ^ { 2 }$ 误差

$$
\sqrt {\frac {1}{N} \sum_ {n = 1} ^ {N} \left(\hat {f} (x _ {n}) - f (x _ {n})\right) ^ {2}} = \sqrt {\frac {1}{N} \sum_ {n = 1} ^ {N} \left(\hat {f} (x _ {n}) - y _ {n}\right) ^ {2}}.
$$

这类误差称为训练误差(training error).

注: 训练损失有时也称为经验风险(empirical risk).

## 测试集、泛化误差与泛化差距得到 $\hat { f }$ 后, 需要对 $\hat { f }$ 进行测试, 以检查模型及训练的好坏. 重新生成一个新的数据集(称为测试集 $( \mathsf { t e s t ~ s e t } ) ) \ \{ ( x _ { n } ^ { \prime } , y _ { n } ^ { \prime } ) \} _ { n = 1 } ^ { N ^ { \prime } }$ , 并计算 $\hat { f }$ 与真正的目标函数 f 在测试集上的误差,如 $\ell ^ { 2 }$ 误差

$$
\sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - f (x _ {n} ^ {\prime})\right) ^ {2}} = \sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - y _ {n} ^ {\prime}\right) ^ {2}}.
$$

这类误差称为泛化误差(generalization error)或测试误差(test error).

## 测试集、泛化误差与泛化差距得到 $\hat { f }$ 后, 需要对 $\hat { f }$ 进行测试, 以检查模型及训练的好坏. 重新生成一个新的数据集(称为测试集 $( \mathsf { t e s t ~ s e t } ) ) \ \{ ( x _ { n } ^ { \prime } , y _ { n } ^ { \prime } ) \} _ { n = 1 } ^ { N ^ { \prime } }$ , 并计算 $\hat { f }$ 与真正的目标函数 f 在测试集上的误差,如 $\ell ^ { 2 }$ 误差

$$
\sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - f (x _ {n} ^ {\prime})\right) ^ {2}} = \sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - y _ {n} ^ {\prime}\right) ^ {2}}.
$$

这类误差称为泛化误差(generalization error)或测试误差(test error).

一个训练后的学习器应用于未参与训练的新样本, 这一过程称为泛化(generalization). 在多数情况下泛化误差会大于训练误差但也有相反的情况它们两者差的绝对值称为泛化差距(generalization gap). 有时, 也会将泛化损失(generalization loss), 即学习器在测试集上的损失函数值与训练损失的差称为泛化差距

## 测试集、泛化误差与泛化差距得到 $\hat { f }$ 后, 需要对 $\hat { f }$ 进行测试, 以检查模型及训练的好坏. 重新生成一个新的数据集(称为测试集 $( \mathsf { t e s t ~ s e t } ) ) \ \{ ( x _ { n } ^ { \prime } , y _ { n } ^ { \prime } ) \} _ { n = 1 } ^ { N ^ { \prime } }$ , 并计算 $\hat { f }$ 与真正的目标函数 f 在测试集上的误差,如 $\ell ^ { 2 }$ 误差

$$
\sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - f (x _ {n} ^ {\prime})\right) ^ {2}} = \sqrt {\frac {1}{N ^ {\prime}} \sum_ {n = 1} ^ {N ^ {\prime}} \left(\hat {f} (x _ {n} ^ {\prime}) - y _ {n} ^ {\prime}\right) ^ {2}}.
$$

这类误差称为泛化误差(generalization error)或测试误差(test error).

一个训练后的学习器应用于未参与训练的新样本, 这一过程称为泛化(generalization). 在多数情况下, 泛化误差会大于训练误差, 但也有相反的情况. 它们两者差的绝对值称为泛化差距(generalization gap). 有时, 也会将泛化损失(generalization loss), 即学习器在测试集上的损失函数值与训练损失的差称为泛化差距注意:

▶ 测试集与训练集都来源于同一个目标函数 $f ,$ 但它们的数据点不应有重叠

▶ 学习器的训练仅依赖于训练集, 与测试集无关;

## 例1 (1-D)

给定一元目标函数 $f ( x ) = 1 / ( x ^ { 2 } + x + 1 )$ . 生成9个训练数据点 $\{ ( x _ { n } , f ( x _ { n } ) ) \}$ }, 其中$x _ { 1 } , \ldots , x _ { 9 } = - 0 . 9 2 , - 0 . 7 8 , - 0 . 3 4 , - 0 . 3 3 , - 0 . 1 6 , 0 . 0 6 , 0 . 1 9 , 0 . 6 4 , 0 . 7 9$ 用二次多项式为学习器, $\therefore L \ell ^ { 2 } .$ -损失函数进行拟合(即最小二乘回归).生成个测试数据点 $\{ ( x _ { n } ^ { \prime } , f ( x _ { n } ^ { \prime } ) ) \}$ , 其中 $x _ { 1 } ^ { \prime } , \ldots , x _ { 5 } ^ { \prime } = - 0 . 8 , - 0 . 4 , 0 , 0 . 4 , 0 . 8 .$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/923300c26df4ece8bfb7dc8b96956eb2b59dbd5e965d174e644e86eca2a0f6d7.jpg)

(红色实线: 目标函数; 黑色实线: 学习器; 蓝点: 训练集; 红点: 测试集.)

## 例1 (1-D)

给定一元目标函数 $f ( x ) = 1 / ( x ^ { 2 } + x + 1 )$ . 生成9个训练数据点 $\{ ( x _ { n } , f ( x _ { n } ) ) \}$ }, 其中$x _ { 1 } , \ldots , x _ { 9 } = - 0 . 9 2 , - 0 . 7 8 , - 0 . 3 4 , - 0 . 3 3 , - 0 . 1 6 , 0 . 0 6 , 0 . 1 9 , 0 . 6 4 , 0 . 7 9$ 用二次多项式为学习器, $\therefore L \ell ^ { 2 } .$ -损失函数进行拟合(即最小二乘回归).生成个测试数据点 $\{ ( x _ { n } ^ { \prime } , f ( x _ { n } ^ { \prime } ) ) \}$ , 其中 $x _ { 1 } ^ { \prime } , \ldots , x _ { 5 } ^ { \prime } = - 0 . 8 , - 0 . 4 , 0 , 0 . 4 , 0 . 8 .$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/11fef4da1279abf5de905a33273765e6f9681ce21d3e93487f2df06171ed0826.jpg)

(红色实线: 目标函数; 黑色实线: 学习器; 蓝点: 训练集; 红点: 测试集.)可计算得到, 训练误差 $\phantom { 0 } { = 7 . 7 8 } \times 1 0 ^ { - 2 }$ , 泛化误差 $= 9 . 0 1 \times 1 0 ^ { - 2 }$ . 因此,泛化差距 $= | 9 . 0 1 \times 1 0 ^ { - 2 } - 7 . 7 8 \times 1 0 ^ { - 2 } | = 1 . 2 3 \times 1 0 ^ { - 2 }$

## 欠拟合/过拟合在例1中, 用不同次数 P 的多项式进行最小二乘回归. (相应的线性方程组有9个方程和 $P + 1$ 个未知数. 当 $P \geq 9$ 时, 为欠定方程组, 有无穷多个解. 这里只演示其中一个特解)

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/839ca23bc94afc5f86236efaac5f06fc3b3aafe01dce51e2970bfcfad5defac2.jpg)  
(a) $P = 2$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/ad934cbf9c7836e6fb4c01e9cac47394b20b9b870a3a0f6fef46412c79484881.jpg)  
(b) $P = 4$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/6cd11472ca7903b554411e627f76b0d0271d340d6b76d1f8728bb6bb80b3b441.jpg)  
(c) $P = 6$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/f84235769664904907f2fc1e94bd574508a13b1c1a9917978e05a090ff3113c4.jpg)  
(d) $P = 9$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/52f9e389cb934a200b05b21f2cf0f1f827df2aca0ea07bbd608dfb9d4270fc77.jpg)  
(e) $P = 1 0$  
随着 P 增大(即容量的增大), 欠拟合 $( \mathsf { U n d e r f i t t i n g } )$ ⇒ 过拟合(Overfitting)

<table><tr><td>P</td><td>训练误差</td><td>泛化误差</td><td>泛化差距</td></tr><tr><td>P=1</td><td>1.60e-01</td><td>1.29e-01</td><td>3.12e-02</td></tr><tr><td>P=2</td><td>7.78e-02</td><td>9.01e-02</td><td>1.23e-02</td></tr><tr><td>P=3</td><td>1.40e-02</td><td>1.62e-02</td><td>2.15e-03</td></tr><tr><td>P=4</td><td>1.39e-02</td><td>1.52e-02</td><td>1.32e-03</td></tr><tr><td>P=5</td><td>2.93e-03</td><td>6.29e-03</td><td>3.36e-03</td></tr><tr><td>P=6</td><td>1.15e-04</td><td>6.95e-04</td><td>5.80e-04</td></tr><tr><td>P=7</td><td>1.16e-05</td><td>9.97e-04</td><td>9.86e-04</td></tr><tr><td>P=8</td><td>1.11e-16</td><td>8.22e-04</td><td>8.22e-04</td></tr><tr><td>P=9</td><td>3.19e-16</td><td>2.82e-02</td><td>2.82e-02</td></tr><tr><td>P=10</td><td>5.27e-16</td><td>2.20e-02</td><td>2.20e-02</td></tr></table>

表训练误差、泛化误差和泛化差距随的变化

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/4dac528718c320b96d3b1e65c67b1ed4512c6dfbdb4dac007c64de5e67831a37.jpg)  
图通常随着学习器容量的增大训练误差不断下降泛化误差先降后升学习器参数的个数大于训练数据点的个数时, 问题通常是欠定的, 例如这里 P = 9,10 的情形. 此时, 该学习器被称为是过度参数化的(over-parameterized). 过拟合现象往往发生在学习器过度参数化时.

<table><tr><td>P</td><td>训练误差</td><td>泛化误差</td><td>泛化差距</td></tr><tr><td>P=1</td><td>1.60e-01</td><td>1.29e-01</td><td>3.12e-02</td></tr><tr><td>P=2</td><td>7.78e-02</td><td>9.01e-02</td><td>1.23e-02</td></tr><tr><td>P=3</td><td>1.40e-02</td><td>1.62e-02</td><td>2.15e-03</td></tr><tr><td>P=4</td><td>1.39e-02</td><td>1.52e-02</td><td>1.32e-03</td></tr><tr><td>P=5</td><td>2.93e-03</td><td>6.29e-03</td><td>3.36e-03</td></tr><tr><td>P=6</td><td>1.15e-04</td><td>6.95e-04</td><td>5.80e-04</td></tr><tr><td>P=7</td><td>1.16e-05</td><td>9.97e-04</td><td>9.86e-04</td></tr><tr><td>P=8</td><td>1.11e-16</td><td>8.22e-04</td><td>8.22e-04</td></tr><tr><td>P=9</td><td>3.19e-16</td><td>2.82e-02</td><td>2.82e-02</td></tr><tr><td>P=10</td><td>5.27e-16</td><td>2.20e-02</td><td>2.20e-02</td></tr></table>

表训练误差、泛化误差和泛化差距随的变化

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/fe0981e59d8a579bc9784c305c805a2ebde19fbffd47590b819ba440f2ff45a9.jpg)  
图通常随着学习器容量的增大训练误差不断下降泛化误差先降后升学习器参数的个数大于训练数据点的个数时, 问题通常是欠定的, 例如这里 P = 9,10 的情形. 此时, 该学习器被称为是过度参数化的(over-parameterized). 过拟合现象往往发生在学习器过度参数化时.

一个学习器在训练后要在实际应用中有好的效果才算是好的学习器而学习器的实际应用, 就是进行泛化 (因为每一次实际应用都可以看作学习器在测试点 $x _ { n } ^ { \prime }$ 上进行取值).因此我们一般认为当某个容量使得学习器的泛化误差达到最小时该容量是最优的最优容量与训练集大小的关系:

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/bc86697bf2db770b28cc45d62b4dedf7b1af5b9cbbde61c5e4c3ec8c3724969e.jpg)

图: 设目标函数 f(x) 是一个五次多项式. 令学习器是一个 N 次多项式, 对 f 进行拟合. 最优次数 N (即容量) 与训练集大小的关系如图. 蓝色竖线表示 40 次随机重复实验下的 95% 置信区间. 当训练集大小增大时, 最优次数也随之增大而在达到足够捕捉目标函数的复杂度之后就不再增长了

## 正则化在例1中, P = 9,10 时出现了过拟合现象. 我们输出训练后的学习器函数:

▶ $P = 9 \colon { \hat { f } } ( x ) = 1 . 0 0 - 1 . 0 1 x - 0 . 1 3 x ^ { 2 } + 1 . 2 1 x ^ { 3 } + 2 . 2 1 x ^ { 4 } + 3 . 0 1 x ^ { 5 } - 1 0 . 9 0 x ^ { 6 } - 1 . 0 0 3 x ^ { 7 } - 1 . 0 0 3 x ^ { 8 } - 2 . 0 1 x ^ { 8 } - 3 . 0 1 ( x - 0 . 0 0 3 x - 0 . 0 0 3 x - 0 . 0 0 3 x ^ { 9 } )$ $1 4 . 4 7 x ^ { 7 } + 1 1 . 0 9 x ^ { 8 } + 1 3 . 8 8 x ^ { 9 }$

▶ $P = 1 0 : { \hat { f } } ( x ) = 1 . 0 0 - 1 . 0 0 x - 0 . 0 2 x ^ { 2 } + 0 . 8 8 x ^ { 3 } - 0 . 4 7 x ^ { 4 } + 3 . 6 5 x ^ { 5 } + 3 . 1 6 x ^ { 6 } - 1 . 0 0 0 x ^ { 7 } + 3 . 1 4 x ^ { 8 } + 0 . 4 7 x ^ { 7 } + 3 . 1 4 x ^ { 8 }$ $1 4 . 6 9 x ^ { 7 } - { 1 3 . 9 4 x ^ { 8 } } + 1 3 . 9 0 x ^ { 9 } + 1 4 . 3 2 x ^ { 1 0 }$

## 正则化在例1中, $P = 9 , 1 0$ 时出现了过拟合现象. 我们输出训练后的学习器函数:

$$
\begin{array}{l} \triangleright P = 9 \colon \hat {f} (x) = 1. 0 0 - 1. 0 1 x - 0. 1 3 x ^ {2} + 1. 2 1 x ^ {3} + 2. 2 1 x ^ {4} + 3. 0 1 x ^ {5} - 1 0. 9 0 x ^ {6} - \\ 1 4. 4 7 x ^ {7} + 1 1. 0 9 x ^ {8} + 1 3. 8 8 x ^ {9}; \end{array}
$$

$$
\begin{array}{l} \triangleright P = 1 0 \colon \hat {f} (x) = 1. 0 0 - 1. 0 0 x - 0. 0 2 x ^ {2} + 0. 8 8 x ^ {3} - 0. 4 7 x ^ {4} + 3. 6 5 x ^ {5} + 3. 1 6 x ^ {6} - \\ 1 4. 6 9 x ^ {7} - 1 3. 9 4 x ^ {8} + 1 3. 9 0 x ^ {9} + 1 4. 3 2 x ^ {1 0}. \end{array}
$$

注意到, 这两个多项式 $\hat { f }$ 的系数(的绝对值)没有随次数的增大而减小. 然而, 数学上可以证明, 对平缓的解析函数, 其泰勒展式的系数(的绝对值)往往随次数增大而快速递减. 因此, 这两个多项式必然不会很平缓, 而是有一定的震荡, 导致其泛化能力较弱.

用高次多项式作学习器时为限制其系数不至于过大可以在损失函数中加入关于系数的惩罚项.

用高次多项式作学习器时, 为”限制”其系数不至于过大, 可以在损失函数中, 加入关于系数的惩罚项.

例如, 用P 次多项式 $\hat { f } ( x ) = w _ { 0 } + w _ { 1 } x + \cdot \cdot \cdot + w _ { P } x ^ { P }$ 对 f 进行最小二乘回归时, 加入关于系数 $w _ { p }$ 的平方项, 以保证 $w _ { p }$ 不至于过大, 即

$$
\min _ {w _ {0}, \ldots , w _ {P}} \frac {1}{N} \sum_ {n = 1} ^ {N} \left(w _ {0} + w _ {1} x _ {n} + \dots + w _ {P} x _ {n} ^ {P} - y _ {n}\right) ^ {2} + \lambda \sum_ {p = 0} ^ {P} w _ {p} ^ {2},
$$

或矩阵形式

$$
\min _ {\boldsymbol {w}} \frac {1}{N} \| \boldsymbol {A} \boldsymbol {w} - \boldsymbol {y} \| _ {2} ^ {2} + \lambda \| \boldsymbol {w} \| _ {2} ^ {2},
$$

其中 $\lambda > 0$ 是一个给定的常数. 这些用于限制参数大小的惩罚项(红色部分)称为正则项(regularization term).

## 例2 (1-D正则化模型)

对例1中的问题, 用九、十次多项式进行最小二乘回归, 并引入平方正则项 $\lambda \| \pmb { w } \| _ { 2 } ^ { 2 }$ . λ 设定为 $1 0 ^ { - 4 }$ . 训练后的学习器如下:

▶ $P = 9 ; { \hat { f } } ( x ) = 1 . 0 0 - 0 . 9 7 x - 0 . 1 1 x ^ { 2 } + 0 . 7 5 x ^ { 3 } - 0 . 3 2 x ^ { 4 } + 0 . 2 2 x ^ { 5 } - 0 . 0 7 x ^ { 6 } - 0 . 0 7 x ^ { 7 } + 0 . 0 7 x ^ { 8 }$ $0 . 1 3 x ^ { 7 } + 0 . 1 3 x ^ { 8 } - 0 . 2 9 x ^ { 9 }$

1 $P = 1 0 : { \hat { f } } ( x ) = 1 . 0 0 - 0 . 9 7 x - 0 . 1 0 x ^ { 2 } + 0 . 7 3 x ^ { 3 } - 0 . 3 3 x ^ { 4 } + 0 . 2 1 x ^ { 5 } - 0 . 1 2 x ^ { 6 } - 0 . 0 9 7 x - 0 . 0 9 7 x ^ { 7 } + 0 . 0 9 7 x ^ { 8 }$ $0 . 1 1 x ^ { 7 } + 0 . 0 6 x ^ { 8 } - 0 . 2 5 x ^ { 9 } + 0 . 1 7 x ^ { 1 0 }$

## 例2 (1-D正则化模型)

对例1中的问题, 用九、十次多项式进行最小二乘回归, 并引入平方正则项 $\lambda \| \pmb { w } \| _ { 2 } ^ { 2 }$ . λ 设定为 $1 0 ^ { - 4 }$ . 训练后的学习器如下:

▶ $P = 9 ; { \hat { f } } ( x ) = 1 . 0 0 - 0 . 9 7 x - 0 . 1 1 x ^ { 2 } + 0 . 7 5 x ^ { 3 } - 0 . 3 2 x ^ { 4 } + 0 . 2 2 x ^ { 5 } - 0 . 0 7 x ^ { 6 } - 0 . 0 7 x ^ { 7 } + 0 . 0 7 x ^ { 8 }$ $0 . 1 3 x ^ { 7 } + 0 . 1 3 x ^ { 8 } - 0 . 2 9 x ^ { 9 }$

▶ $P = 1 0 : { \hat { f } } ( x ) = 1 . 0 0 - 0 . 9 7 x - 0 . 1 0 x ^ { 2 } + 0 . 7 3 x ^ { 3 } - 0 . 3 3 x ^ { 4 } + 0 . 2 1 x ^ { 5 } - 0 . 1 2 x ^ { 6 } - 0 . 0 9 7 x - 0 . 0 9 7 x ^ { 7 } + 0 . 0 9 7 x ^ { 8 }$ $0 . 1 1 x ^ { 7 } + 0 . 0 6 x ^ { 8 } - 0 . 2 5 x ^ { 9 } + 0 . 1 7 x ^ { 1 0 }$

这两个多项式 $\hat { f }$ 的系数随次数增大保持在较小水平.

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/4e2cc708a93d657d30915c6ce5c61030bfbf2f88b16475d6efcdb096f9f451a5.jpg)  
(c) $P = 9$

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/a0696ec57153bad98a37a7180a83545b70a3df761f07a0fffca6d3df71b95ee9.jpg)  
(d) $P = 1 0$

<table><tr><td>P</td><td>训练误差</td><td>泛化误差</td><td>泛化差距</td></tr><tr><td>P=9</td><td>2.84e-03</td><td>2.64e-03</td><td>2.02e-04</td></tr><tr><td>P=10</td><td>2.81e-03</td><td>1.88e-03</td><td>9.36e-04</td></tr></table>

表正则化模型的泛化误差和泛化差距比无正则化时明显降低

## 验证集很多时候, 我们只拥有一个单纯的数据集, 并没有专门定义成训练集或测试集. 此时, 我们可以手动将数据集分为两部分, 分别作为训练集和测试集, 用于训练和测试学习器. 这里的测试集一般称为验证集(validation set). 验证集的选取应保证”均匀性”, 即验证集与训练集应满足相同的概率分布从而避免偏差例如

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/1352898227666b4e1b021d9e1a53ca9b3bb87d0fc4b6f4fe801df0ccf726eff2.jpg)  
(e) 不合适的选取

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/df6823b8cba181aa5fa814f97faed30555c37c7c66b15157f58955ca231cdef2.jpg)  
(f) 合适的选取

## 数据集大小对误差的影响一般来说, 随着数据集的增大, 总损失函数 $L [ \hat { f } ]$ 中的项 $l ( \hat { f } ( x _ { n } ) , y _ { n } )$ 随之增多, 对它进行最小化 (即训练) 也会越来越难. 因此, 在同一个优化器下, 训练误差往往随数据集的增大而增大.

## 数据集大小对误差的影响一般来说, 随着数据集的增大, 总损失函数 $L [ \hat { f } ]$ 中的项 $l ( \hat { f } ( x _ { n } ) , y _ { n } )$ 随之增多, 对它进行最小化 (即训练) 也会越来越难. 因此, 在同一个优化器下, 训练误差往往随数据集的增大而增大.

然而随着数据集的增大更多的数据点会分布在整个样本空间即目标函数的定义域上), 使得最终训练而成的学习器具有更好的泛化能力. 因此, 在同一个优化器下, 泛化误差往往随数据集的增大而减小

![](../../../../../04_Assets/Images/Courses/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/PPT/Chapter2/images/77534f152537f0f04719891f9d47fed581f4ae041f7562089d60cbedc814bec8.jpg)  
图: 设目标函数 f(x) 是一个五次多项式. 将学习器设定为为二次多项式或当前数据集规模下的最优次数多项式. 竖线表示次随机重复实验下的置信区间对每一个学习器当训练集大小增大时训练误差随之增大泛化误差随之减小

## 本章 Python 实践

## Python 常用库:

▶ <sub>numpy</sub>: 常用的数值计算库, 提供多维数组对象(array)及相应操作, 包括数组生成: <sub>ones</sub>, <sub>zeros</sub>, <sub>linspace</sub>, <sub>arange</sub>

数组操作: <sub>array</sub>[<sub>m,n</sub>], <sub>arange</sub>, <sub>reshape</sub>, <sub>transpose</sub>, <sub>split</sub>

数学函数:, <sub>sin</sub>, <sub>cos</sub>, <sub>tan</sub>, <sub>arcsin</sub>, <sub>arccos</sub>, <sub>arctan</sub>, <sub>around</sub>, <sub>floor</sub>, <sub>ceil</sub>

统计函数:, <sub>amin</sub>, <sub>amax</sub>, <sub>median</sub>, <sub>mean</sub>, <sub>average</sub>, <sub>std</sub>, <sub>var</sub>

线性代数:, <sub>inner</sub>, <sub>matmul</sub>, <sub>@</sub>, <sub>kron</sub>

▶ <sub>numpy.linalg</sub>: numpy的数值代数库, 提供求解线性方程组、矩阵分解、求解特征值等命令, 包括det, inv, norm, cond, solve, lstsq, qr, svd, eig

▶ <sub>numpy.random</sub>: numpy的随机数库, 提供随机数生成等命令, 包括randint, rand, choice, uniform, normal

▶ <sub>matplotlib.pyplot</sub>: 常用的2D绘图库, 命令包括plot, show, xlabel, ylabel, title, legend, clf

## 演示给定函数 f : [−1,1] → R, f(x) = sin(2πx). 用不同次数的多项式学习器进行多项式回归.

1. 生成训练集与测试集;

2. 建立模型参数;

3. 通过求解线性方程组计算模型参数, 并计算训练误差和测试误差;

4. 画图演示结果.

## 本章总结

▶ 数据集、学习器、假设空间、容量、泛化、欠拟合、过拟合、正则化、验证集 (参考: 教材5.2)

▶ NumPy 与 Matplotlib 库的使用

(参考: 官方文档 https://numpy.org/doc/stable/

线上中文教程: https://m.runoob.com/numpy/)