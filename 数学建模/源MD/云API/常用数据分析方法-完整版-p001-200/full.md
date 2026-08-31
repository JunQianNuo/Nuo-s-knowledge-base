# 常用的数据分析方法

# Mathematical Statistics: A Theoretical Framework

覃思义

Mathematical Science School

2026 年 7 月 15 日

## 目录

1 预备知识

2 统计量与抽样分布

3 参数估计

4 假设检验

5 方差分析

6 回归分析

7 多元统计分析

8 专题方法

9 方法选择与总结

10 感谢学习

## 第 0 章 预备知识

Prerequisites

## 概率空间与随机变量

1. 概率空间 (Probability Space)

定义：三元组 (Ω, F,P)

• Ω（样本空间）：随机试验所有可能结果的集合

• F（σ 代数）：Ω 的子集构成的集合，满足可测性要求

• P（概率测度）： $F  [ 0 , 1 ]$ 的映射，满足非负性、规范性、可列可加性

## 概率空间与随机变量

## 1. 概率空间 (Probability Space)

定义：三元组 $( \Omega , F , P )$

• Ω（样本空间）：随机试验所有可能结果的集合

• F（σ 代数）：Ω 的子集构成的集合，满足可测性要求

• P（概率测度）： $F  [ 0 , 1 ]$ 的映射，满足非负性、规范性、可列可加性

## 2. 随机变量 (Random Variable)

定义： $X : \Omega  R$ 是可测函数，即对任意 Borel 集 B，有 $\{ X \in B \} \in F$

• 累积分布函数 $( C D F ) : F ( x ) = P ( X \leq x )$

• 概率质量函数(PMF)：离散型， $P ( X = x )$

• 概率密度函数(PDF)：连续型， $f ( x ) = F ^ { \prime } ( x )$

## 常用离散分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望  $E(X)$ </td><td>方差  $Var(X)$ </td><td>典型应用</td></tr><tr><td>0-1 分布</td><td> $(0 - 1)$ </td><td> $p \in (0,1)$ </td><td> $p$ </td><td> $p(1 - p)$ </td><td>单次试验成功/失败</td></tr><tr><td>二项分布</td><td> $B(n,p)$ </td><td> $n,p$ </td><td> $np$ </td><td> $np(1 - p)$ </td><td> $n$  次独立重复试验成功次数</td></tr><tr><td>泊松分布</td><td> $P(\lambda)$ </td><td> $\lambda >0$ </td><td> $\lambda$ </td><td> $\lambda$ </td><td>单位时间内随机事件发生次数</td></tr><tr><td>几何分布</td><td> $Geo(p)$ </td><td> $p \in (0,1)$ </td><td> $1/p$ </td><td> $(1 - p)/p^{2}$ </td><td>首次成功所需试验次数</td></tr><tr><td>超几何分布</td><td> $H(N,M,n)$ </td><td>N,M,n</td><td> $nM/N$ </td><td> $n\frac{M}{N}\left(1 - \frac{M}{N}\right)\frac{N-n}{N-1}$ </td><td>不放回抽样成功次数</td></tr></table>

## 常用离散分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望  $E(X)$ </td><td>方差  $Var(X)$ </td><td>典型应用</td></tr><tr><td>0-1 分布</td><td> $(0 - 1)$ </td><td> $p \in (0,1)$ </td><td> $p$ </td><td> $p(1 - p)$ </td><td>单次试验成功/失败</td></tr><tr><td>二项分布</td><td> $B(n,p)$ </td><td> $n,p$ </td><td> $np$ </td><td> $np(1 - p)$ </td><td> $n$  次独立重复试验成功次数</td></tr><tr><td>泊松分布</td><td> $P(\lambda)$ </td><td> $\lambda >0$ </td><td> $\lambda$ </td><td> $\lambda$ </td><td>单位时间内随机事件发生次数</td></tr><tr><td>几何分布</td><td> $Geo(p)$ </td><td> $p \in (0,1)$ </td><td> $1/p$ </td><td> $(1 - p)/p^{2}$ </td><td>首次成功所需试验次数</td></tr><tr><td>超几何分布</td><td> $H(N,M,n)$ </td><td>N,M,n</td><td> $nM/N$ </td><td> $n^{\frac{M}{N}}\left(1 - \frac{M}{N}\right)\frac{N-n}{N-1}$ </td><td>不放回抽样成功次数</td></tr></table>

## 核心记忆技巧

• 二项分布 → 正态近似（n → +∞时）

## 常用离散分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望  $E(X)$ </td><td>方差  $Var(X)$ </td><td>典型应用</td></tr><tr><td>0-1 分布</td><td> $(0 - 1)$ </td><td> $p \in (0,1)$ </td><td> $p$ </td><td> $p(1 - p)$ </td><td>单次试验成功/失败</td></tr><tr><td>二项分布</td><td> $B(n,p)$ </td><td> $n,p$ </td><td> $np$ </td><td> $np(1 - p)$ </td><td> $n$  次独立重复试验成功次数</td></tr><tr><td>泊松分布</td><td> $P(\lambda)$ </td><td> $\lambda >0$ </td><td> $\lambda$ </td><td> $\lambda$ </td><td>单位时间内随机事件发生次数</td></tr><tr><td>几何分布</td><td> $Geo(p)$ </td><td> $p \in (0,1)$ </td><td> $1/p$ </td><td> $(1 - p)/p^{2}$ </td><td>首次成功所需试验次数</td></tr><tr><td>超几何分布</td><td> $H(N,M,n)$ </td><td>N,M,n</td><td> $nM/N$ </td><td> $n^{\frac{M}{N}}\left(1 - \frac{M}{N}\right)\frac{N-n}{N-1}$ </td><td>不放回抽样成功次数</td></tr></table>

## 核心记忆技巧

• 二项分布 → 正态近似（n → +∞时）

• 二项分布→泊松分布（稀有事件建模），λ 越大越对称

## 常用连续分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望 E(X)</td><td>方差 Var(X)</td><td>概率密度函数</td></tr><tr><td>均匀分布</td><td> $U(a,b)$ </td><td> $a < b$ </td><td> $\frac{a+b}{2}$ </td><td> $\frac{(b-a)^{2}}{12}$ </td><td> $f(x) = \frac{1}{b-a}, x \in (a,b)$ </td></tr><tr><td>正态分布</td><td> $N(\mu,\sigma^{2})$ </td><td> $\mu, \sigma^{2} > 0$ </td><td> $\mu$ </td><td> $\sigma^{2}$ </td><td> $f(x) = \frac{1}{\sqrt{2\pi}\sigma} \cdot exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})$ </td></tr><tr><td>指数分布</td><td> $Exp(\lambda)$ </td><td> $\lambda > 0$ </td><td> $\frac{1}{\lambda}$ </td><td> $\frac{1}{\lambda^{2}}$ </td><td> $f(x) = \lambda e^{-\lambda x}, x \geq 0$ </td></tr><tr><td>伽马分布</td><td> $\Gamma(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\alpha\beta$ </td><td> $\alpha\beta^{2}$ </td><td> $f(x) = \frac{x^{\alpha-1}e^{-x/\beta}}{\beta^{\alpha}\Gamma(\alpha)}, x \geq 0$ </td></tr><tr><td>贝塔分布</td><td> $B(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\frac{\alpha}{\alpha+\beta}$ </td><td> $\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ </td><td> $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, x \in [0,1]$ </td></tr></table>

## 常用连续分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望 E(X)</td><td>方差 Var(X)</td><td>概率密度函数</td></tr><tr><td>均匀分布</td><td> $U(a,b)$ </td><td> $a < b$ </td><td> $\frac{a+b}{2}$ </td><td> $\frac{(b-a)^{2}}{12}$ </td><td> $f(x) = \frac{1}{b-a}, x \in (a,b)$ </td></tr><tr><td>正态分布</td><td> $N(\mu,\sigma^{2})$ </td><td> $\mu, \sigma^{2} > 0$ </td><td> $\mu$ </td><td> $\sigma^{2}$ </td><td> $f(x) = \frac{1}{\sqrt{2\pi}\sigma} \cdot exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})$ </td></tr><tr><td>指数分布</td><td> $Exp(\lambda)$ </td><td> $\lambda > 0$ </td><td> $\frac{1}{\lambda}$ </td><td> $\frac{1}{\lambda^{2}}$ </td><td> $f(x) = \lambda e^{-\lambda x}, x \geq 0$ </td></tr><tr><td>伽马分布</td><td> $\Gamma(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\alpha\beta$ </td><td> $\alpha\beta^{2}$ </td><td> $f(x) = \frac{x^{\alpha-1}e^{-x/\beta}}{\beta^{\alpha}\Gamma(\alpha)}, x \geq 0$ </td></tr><tr><td>贝塔分布</td><td> $B(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\frac{\alpha}{\alpha+\beta}$ </td><td> $\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ </td><td> $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, x \in [0,1]$ </td></tr></table>

## 重要性质

• 正态分布的线性组合仍为正态分布

## 常用连续分布回顾

<table><tr><td>分布名称</td><td>记号</td><td>参数</td><td>期望 E(X)</td><td>方差 Var(X)</td><td>概率密度函数</td></tr><tr><td>均匀分布</td><td> $U(a,b)$ </td><td> $a < b$ </td><td> $\frac{a+b}{2}$ </td><td> $\frac{(b-a)^{2}}{12}$ </td><td> $f(x) = \frac{1}{b-a}, x \in (a,b)$ </td></tr><tr><td>正态分布</td><td> $N(\mu,\sigma^{2})$ </td><td> $\mu, \sigma^{2} > 0$ </td><td> $\mu$ </td><td> $\sigma^{2}$ </td><td> $f(x) = \frac{1}{\sqrt{2\pi}\sigma} \cdot exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})$ </td></tr><tr><td>指数分布</td><td> $Exp(\lambda)$ </td><td> $\lambda > 0$ </td><td> $\frac{1}{\lambda}$ </td><td> $\frac{1}{\lambda^{2}}$ </td><td> $f(x) = \lambda e^{-\lambda x}, x \geq 0$ </td></tr><tr><td>伽马分布</td><td> $\Gamma(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\alpha\beta$ </td><td> $\alpha\beta^{2}$ </td><td> $f(x) = \frac{x^{\alpha-1}e^{-x/\beta}}{\beta^{\alpha}\Gamma(\alpha)}, x \geq 0$ </td></tr><tr><td>贝塔分布</td><td> $B(\alpha,\beta)$ </td><td> $\alpha, \beta > 0$ </td><td> $\frac{\alpha}{\alpha+\beta}$ </td><td> $\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ </td><td> $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, x \in [0,1]$ </td></tr></table>

## 重要性质

• 正态分布的线性组合仍为正态分布

• 指数分布具有无记忆性： $P ( X > s + t | X > s ) = P ( X > t )$

## $\chi ^ { 2 }$ 分布的构造与性质

构造定义

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布于N(0,1)，则

$$
\chi^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + \ldots + X _ {n} ^ {2} \sim \chi^ {2} (n)
$$

称 $\chi ^ { 2 }$ 服从自由度为 n 的卡方分布，记为 $\chi ^ { 2 } \sim \chi ^ { 2 } ( n )$

## $\chi ^ { 2 }$ 分布的构造与性质

构造定义

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布于N(0,1)，则

$$
\chi^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + \dots + X _ {n} ^ {2} \sim \chi^ {2} (n)
$$

称 $\chi ^ { 2 }$ 服从自由度为 n 的卡方分布，记为 $\chi ^ { 2 } \sim \chi ^ { 2 } ( n )$

主要性质

• 期望与方差： $E [ \chi ^ { 2 } ( n ) ] = n , V a r [ \chi ^ { 2 } ( n ) ] = 2 n$

## $\chi ^ { 2 }$ 分布的构造与性质

构造定义

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布于N(0,1)，则

$$
\chi^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + \ldots + X _ {n} ^ {2} \sim \chi^ {2} (n)
$$

称 $\chi ^ { 2 }$ 服从自由度为 n 的卡方分布，记为 $\chi ^ { 2 } \sim \chi ^ { 2 } ( n )$

## 主要性质

• 期望与方差： $E [ \chi ^ { 2 } ( n ) ] = n , V a r [ \chi ^ { 2 } ( n ) ] = 2 n$

• 可加性：若 $\chi ^ { 2 } ( n _ { 1 } )$ 与 $\chi ^ { 2 } ( n _ { 2 } )$ 独立，则 $\chi ^ { 2 } ( n _ { 1 } ) + \chi ^ { 2 } ( n _ { 2 } ) \sim \chi ^ { 2 } ( n _ { 1 } + n _ { 2 } )$

## $\chi ^ { 2 }$ 分布的构造与性质

构造定义

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布于N(0,1)，则

$$
\chi^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + \ldots + X _ {n} ^ {2} \sim \chi^ {2} (n)
$$

称 $\chi ^ { 2 }$ 服从自由度为 n 的卡方分布，记为 $\chi ^ { 2 } \sim \chi ^ { 2 } ( n )$

主要性质

• 期望与方差： $E [ \chi ^ { 2 } ( n ) ] = n , V a r [ \chi ^ { 2 } ( n ) ] = 2 n$

• 可加性：若 $\chi ^ { 2 } ( n _ { 1 } )$ 与 $\chi ^ { 2 } ( n _ { 2 } )$ 独立，则 $\chi ^ { 2 } ( n _ { 1 } ) + \chi ^ { 2 } ( n _ { 2 } ) \sim \chi ^ { 2 } ( n _ { 1 } + n _ { 2 } )$

• 当 $n \to \infty$ 时， $\chi ^ { 2 } ( n )$ 渐近服从 $N ( n , 2 n )$

## $\chi ^ { 2 }$ 分布的构造与性质

构造定义

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布于N(0,1)，则

$$
\chi^ {2} = X _ {1} ^ {2} + X _ {2} ^ {2} + \dots + X _ {n} ^ {2} \sim \chi^ {2} (n)
$$

称 $\chi ^ { 2 }$ 服从自由度为 n 的卡方分布，记为 $\chi ^ { 2 } \sim \chi ^ { 2 } ( n )$

## 主要性质

• 期望与方差： $E [ \chi ^ { 2 } ( n ) ] = n , V a r [ \chi ^ { 2 } ( n ) ] = 2 n$

• 可加性：若 $\chi ^ { 2 } ( n _ { 1 } )$ 与 $\chi ^ { 2 } ( n _ { 2 } )$ 独立，则 $\chi ^ { 2 } ( n _ { 1 } ) + \chi ^ { 2 } ( n _ { 2 } ) \sim \chi ^ { 2 } ( n _ { 1 } + n _ { 2 } )$

• 当 $n \to \infty$ 时， $\chi ^ { 2 } ( n )$ 渐近服从 $N ( n , 2 n )$

• 取值范围： $( 0 , + \infty )$ ，右偏分布，自由度越大越对称

## t 分布的构造与性质

## 构造定义

设 $X \sim N ( 0 , 1 ) , Y \sim \chi ^ { 2 } ( n )$ ，且 X 与 Y 独立，则

$$
T = \frac {X}{\sqrt {Y / n}} \sim t (n)
$$

称 T 服从自由度为n 的t 分布 (也称为学生分布)，记为 $T \sim t ( n )$

## t 分布的构造与性质

## 构造定义

设 $X \sim N ( 0 , 1 ) , Y \sim \chi ^ { 2 } ( n )$ ，且 X 与 Y 独立，则

$$
T = \frac {X}{\sqrt {Y / n}} \sim t (n)
$$

称 T 服从自由度为n 的t 分布 (也称为学生分布)，记为 $T \sim t ( n )$

## 主要性质

• 关于 0 对称，形态类似正态分布但尾部更厚

## t 分布的构造与性质

构造定义

设 $X \sim N ( 0 , 1 ) , Y \sim \chi ^ { 2 } ( n )$ ，且 X 与Y 独立，则

$$
T = \frac {X}{\sqrt {Y / n}} \sim t (n)
$$

称 T 服从自由度为n 的t 分布 (也称为学生分布)，记为 $T \sim t ( n )$

## 主要性质

• 关于 0 对称，形态类似正态分布但尾部更厚

• 期望： $E [ T ] = 0 ( n > 1 )$ ，方差： $V a r [ T ] = n / ( n - 2 ) ( n > 2 )$

## t 分布的构造与性质

## 构造定义

设 $X \sim N ( 0 , 1 ) , Y \sim \chi ^ { 2 } ( n )$ ，且 X 与Y 独立，则

$$
T = \frac {X}{\sqrt {Y / n}} \sim t (n)
$$

称 T 服从自由度为n 的t 分布 (也称为学生分布)，记为 $T \sim t ( n )$

## 主要性质

• 关于 0 对称，形态类似正态分布但尾部更厚

• 期望： $E [ T ] = 0 ( n > 1 )$ ，方差： $V a r [ T ] = n / ( n - 2 ) ( n > 2 )$

• 当 $n \to \infty$ 时， $t ( n ) \to N ( 0 , 1 )$ （渐近标准正态）

## t 分布的构造与性质

## 构造定义

设 $X \sim N ( 0 , 1 ) , Y \sim \chi ^ { 2 } ( n )$ ，且 X 与Y 独立，则

$$
T = \frac {X}{\sqrt {Y / n}} \sim t (n)
$$

称 T 服从自由度为n 的t 分布 (也称为学生分布)，记为 $T \sim t ( n )$

## 主要性质

• 关于 0 对称，形态类似正态分布但尾部更厚

• 期望： $E [ T ] = 0 ( n > 1 )$ ，方差： $V a r [ T ] = n / ( n - 2 ) ( n > 2 )$

• 当 $n \to \infty$ 时， $t ( n ) \to N ( 0 , 1 )$ （渐近标准正态）

• 自由度越小，尾部越厚； $n \geq 3 0$ 时与正态分布非常接近

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$ 主要性质

• 取值范围： $( 0 , + \infty )$ ，右偏分布

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$

主要性质

• 取值范围： $( 0 , + \infty )$ ，右偏分布

• 倒数性质：若 $F \sim F ( n _ { 1 } , n _ { 2 } )$ ，则 $1 / F \sim F ( n _ { 2 } , n _ { 1 } )$

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$

## 主要性质

• 取值范围： $( 0 , + \infty )$ ，右偏分布

• 倒数性质：若 $F \sim F ( n _ { 1 } , n _ { 2 } )$ ，则 $1 / F \sim F ( n _ { 2 } , n _ { 1 } )$

• 与t 分布关系：若 $T \sim t ( n )$ ，则 $T ^ { 2 } \sim F ( 1 , n )$

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$

主要性质

• 取值范围： $( 0 , + \infty )$ ，右偏分布

• 倒数性质：若 $F \sim F ( n _ { 1 } , n _ { 2 } )$ ，则 $1 / F \sim F ( n _ { 2 } , n _ { 1 } )$

• 与t 分布关系：若 $T \sim t ( n )$ ，则 $T ^ { 2 } \sim F ( 1 , n )$

• $F ( n _ { 1 } , n _ { 2 } )$ 的上 α 分位数记为 $F _ { \alpha } ( n _ { 1 } , n _ { 2 } )$

## $F$ 分布的构造与性质

构造定义

设 $U \sim \chi ^ { 2 } ( n _ { 1 } ) , V \sim \chi ^ { 2 } ( n _ { 2 } )$ ，且 U 与V 独立，则

$$
F = \frac {U / n _ {1}}{V / n _ {2}} \sim F (n _ {1}, n _ {2})
$$

称 F 服从第一自由度为 $n _ { 1 }$ 、第二自由度为 $n _ { 2 }$ 的 F 分布，记为 $F \sim F ( n _ { 1 } , n _ { 2 } )$

## 主要性质

• 取值范围： $( 0 , + \infty )$ ，右偏分布

• 倒数性质：若 $F \sim F ( n _ { 1 } , n _ { 2 } )$ ，则 $1 / F \sim F ( n _ { 2 } , n _ { 1 } )$

• 与t 分布关系：若 $T \sim t ( n )$ ，则 $T ^ { 2 } \sim F ( 1 , n )$

• $F ( n _ { 1 } , n _ { 2 } )$ 的上 α 分位数记为 $F _ { \alpha } ( n _ { 1 } , n _ { 2 } )$

• $F _ { ( 1 - \alpha ) } ( n _ { 1 } , n _ { 2 } ) = 1 / F _ { \alpha } ( n _ { 2 } , n _ { 1 } )$ （下侧分位数换算公式）

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$ 加权平均，反映随机变量的平均水平

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

重要性质

• 期望线性性： $E ( a X + b Y ) = a E ( X ) + b E ( Y )$ （无需独立）

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

重要性质

• 期望线性性： $E ( a X + b Y ) = a E ( X ) + b E ( Y )$ （无需独立）

• 方差性质： $V a r ( a X + b ) = a ^ { 2 } V a r ( X ) , V a r ( X \pm Y ) = V a r ( X ) + V a r ( Y ) \pm 2 C o v ( X , Y )$

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

重要性质

• 期望线性性： $E ( a X + b Y ) = a E ( X ) + b E ( Y )$ （无需独立）

• 方差性质： $V a r ( a X + b ) = a ^ { 2 } V a r ( X ) , V a r ( X \pm Y ) = V a r ( X ) + V a r ( Y ) \pm 2 C o v ( X , Y )$

• $X , Y$ 独立 $\Rightarrow C o v ( X , Y ) = 0$ （反之不成立）

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

## 重要性质

• 期望线性性： $E ( a X + b Y ) = a E ( X ) + b E ( Y )$ （无需独立）

• 方差性质： $V a r ( a X + b ) = a ^ { 2 } V a r ( X ) , V a r ( X \pm Y ) = V a r ( X ) + V a r ( Y ) \pm 2 C o v ( X , Y )$

• X,Y 独立 $\Rightarrow C o v ( X , Y ) = 0$ （反之不成立）

• 相关系数： $\rho = C o v ( X , Y ) / ( \sigma _ { x } \cdot \sigma _ { y } )$ ，取值 [−1,1]，衡量线性相关程度

## 数字特征：期望、方差、协方差

期望 Expectation: $E ( X ) = \Sigma _ { i = 1 } ^ { + \infty } x _ { i } p _ { i }$ 或 $\textstyle \int _ { - \infty } ^ { + \infty } x f ( x ) d x$

加权平均，反映随机变量的平均水平

方差 Variance: $V a r ( X ) = E [ ( X - \mu ) ^ { 2 } ]$

反映随机变量取值的离散程度

协方差 Covariance: $C o v ( X , Y ) = E [ ( X - \mu _ { x } ) ( Y - \mu _ { y } ) ]$

反映两个随机变量的协同变化程度

重要性质

• 期望线性性： $E ( a X + b Y ) = a E ( X ) + b E ( Y )$ （无需独立）

• 方差性质： $V a r ( a X + b ) = a ^ { 2 } V a r ( X ) , V a r ( X \pm Y ) = V a r ( X ) + V a r ( Y ) \pm 2 C o v ( X , Y )$

• X,Y 独立 $\Rightarrow C o v ( X , Y ) = 0$ （反之不成立）

• 相关系数： $\rho = C o v ( X , Y ) / ( \sigma _ { x } \cdot \sigma _ { y } )$ ，取值 [−1,1]，衡量线性相关程度

• 柯西-施瓦茨不等式： $[ C o v ( X , Y ) ] ^ { 2 } \leq V a r ( X ) \cdot V a r ( Y )$

## 大数定律

定义

## 大数定律

定义

设 $X _ { n } , n = 1 , 2 , \cdots$ 是随机变量序列，其数学期望都存在，若对于任意的 $\varepsilon > 0$ ，有

$$
\lim _ {n \to + \infty} P \{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) \right| \geq \varepsilon \} = 0.
$$

$$
\text {或者} \lim _ {n \to + \infty} P \{| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) | <   \varepsilon \} = 1.
$$

称随机变量序列 $\{ X _ { n } \}$ 服从大数定律.

## 大数定律

定义

设 $X _ { n } , n = 1 , 2 , \cdots$ 是随机变量序列，其数学期望都存在，若对于任意的 $\varepsilon > 0$ ，有

$$
\lim _ {n \to + \infty} P \{| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) | \geq \varepsilon \} = 0.
$$

$$
\text {或者} \lim _ {n \to + \infty} P \{| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) | <   \varepsilon \} = 1.
$$

称随机变量序列 $\{ X _ { n } \}$ 服从大数定律.

![](2e0a563aa30f5f5f03c029d7e64a3236adf104f5c9d2d2a3f55bdf996edb4717.jpg)

1 服从大数定律不能说 $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i }$ 依概率收敛到 $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } E ( X _ { i } )$ 。

## 大数定律

定义

设 $X _ { n } , n = 1 , 2 , \cdots$ 是随机变量序列，其数学期望都存在，若对于任意的 $\varepsilon > 0$ ，有

$$
\lim _ {n \to + \infty} P \{\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) \right| \geq \varepsilon \} = 0.
$$

$$
\text {或者} \lim _ {n \to + \infty} P \{| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) | <   \varepsilon \} = 1.
$$

称随机变量序列 $\{ X _ { n } \}$ 服从大数定律.

1 服从大数定律不能说 $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } X _ { i }$ 依概率收敛到 $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } E ( X _ { i } )$ 。

2 服从大数定律的概率意义： $\{ X _ { k } \} , k = 1 , 2 , \cdots$ 的前 n 项算术平均将紧密地聚集在其数学期望的附近。

大数定律

切比雪夫大数定律

## 大数定律

## 切比雪夫大数定律

$X _ { k } , k = 1 , 2 , \cdots$ 是相互独立的随机变量序列,其数学期望和方差都存在，且方差有界，即存在常$\forall i \in N , D ( X _ { i } ) < C$ . 则

$$
\lim _ {n \rightarrow \infty} P \left(\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) \right| <   \varepsilon\right) = 1
$$

即随机变量序列 $X _ { k } , k = 1 , 2 , \cdots$ · 服从大数定律.

## 大数定律

切比雪夫大数定律

$X _ { k } , k = 1 , 2 , \cdots$ 是相互独立的随机变量序列,其数学期望和方差都存在，且方差有界，即存在常$\forall i \in N , D ( X _ { i } ) < C$ . 则

$$
\lim _ {n \rightarrow \infty} P \left(\left| \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} - \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) \right| <   \varepsilon\right) = 1
$$

即随机变量序列 $X _ { k } , k = 1 , 2 , \cdots$ · 服从大数定律.

独立同分布大数定律

设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 独立同分布， $E ( X _ { i } ) = \mu , V a r ( X _ { i } ) = \sigma ^ { 2 } < \infty$ ，则样本均值 ${ \bar { X } } = ( X _ { 1 } + \ldots + X _ { n } ) / n$ 依概率收敛于 $\mu .$

直观理解：试验次数足够多时，样本均值会越来越接近总体均值

中心极限定理 (Central Limit Theorem)

## 中心极限定理 (Central Limit Theorem)

定义

设随机变量 $X _ { k } , k = 1 , 2 , \cdots$ · 相互独立，有有限数学期望和方差.若随机变量序列

$$
Y _ {n} = \frac {\sum_ {k = 1} ^ {n} X _ {k} - \sum_ {k = 1} ^ {n} E (X _ {k})}{\sqrt {\sum_ {k = 1} ^ {n} D (X _ {k})}}
$$

对 $y \in R$ 一致地有 $\begin{array} { r } { \operatorname* { l i m } _ { n  + \infty } P \{ Y _ { n } \leq y \} = \int _ { - \infty } ^ { y } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } } d t = \Phi ( y ) } \end{array}$ 随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理.

## 中心极限定理 (Central Limit Theorem)

定义

设随机变量 $X _ { k } , k = 1 , 2 , \cdots$ · 相互独立，有有限数学期望和方差.若随机变量序列

$$
Y _ {n} = \frac {\sum_ {k = 1} ^ {n} X _ {k} - \sum_ {k = 1} ^ {n} E (X _ {k})}{\sqrt {\sum_ {k = 1} ^ {n} D (X _ {k})}}
$$

对 $y \in R$ 一致地有 $\begin{array} { r } { \operatorname* { l i m } _ { n  + \infty } P \{ Y _ { n } \leq y \} = \int _ { - \infty } ^ { y } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } } d t = \Phi ( y ) } \end{array}$

随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理.

1 随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理, 指其前 n 项和 $\scriptstyle \sum _ { k = 1 } ^ { n } X _ { k }$ 的标准化随机变量依分布收敛于标准正态分布随机变量 $X ,$

## 中心极限定理 (Central Limit Theorem)

定义

设随机变量 $X _ { k } , k = 1 , 2 , \cdots$ · 相互独立，有有限数学期望和方差.若随机变量序列

$$
Y _ {n} = \frac {\sum_ {k = 1} ^ {n} X _ {k} - \sum_ {k = 1} ^ {n} E (X _ {k})}{\sqrt {\sum_ {k = 1} ^ {n} D (X _ {k})}}
$$

对 $y \in R$ 一致地有 $\begin{array} { r } { \operatorname* { l i m } _ { n  + \infty } P \{ Y _ { n } \leq y \} = \int _ { - \infty } ^ { y } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } } d t = \Phi ( y ) } \end{array}$

随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理.

1 随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理, 指其前 n 项和 $\scriptstyle \sum _ { k = 1 } ^ { n } X _ { k }$ 的标准化随机变量依分布收敛于标准正态分布随机变量 $X ,$

2 解释了现实中哪些随机变量可看服从正态分布。

## 中心极限定理 (Central Limit Theorem)

定义

设随机变量 $X _ { k } , k = 1 , 2 , \cdots$ · 相互独立，有有限数学期望和方差.若随机变量序列

$$
Y _ {n} = \frac {\sum_ {k = 1} ^ {n} X _ {k} - \sum_ {k = 1} ^ {n} E (X _ {k})}{\sqrt {\sum_ {k = 1} ^ {n} D (X _ {k})}}
$$

对 $y \in R$ 一致地有 $\begin{array} { r } { \operatorname* { l i m } _ { n  + \infty } P \{ Y _ { n } \leq y \} = \int _ { - \infty } ^ { y } \frac { 1 } { \sqrt { 2 \pi } } e ^ { - \frac { 1 } { 2 } t ^ { 2 } } d t = \Phi ( y ) } \end{array}$

随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理.

1 随机变量序列 $\{ X _ { k } \}$ 服从中心极限定理, 指其前 n 项和 $\scriptstyle \sum _ { k = 1 } ^ { n } X _ { k }$ 的标准化随机变量依分布收敛于标准正态分布随机变量 $X ,$

2 解释了现实中哪些随机变量可看服从正态分布。

3 给出了概率的近似计算公式。

中心极限定理 (Central Limit Theorem)

## 中心极限定理 (Central Limit Theorem)

林德伯格—列维定理或独立同分布中心极限定理

$\{ X _ { k } \} , k = 1 , 2 , \cdots$ 为相互独立, 具有相同分布的随机变量序列, 且 $E ( X _ { k } ) = \mu , D ( X _ { k } ) = \sigma ^ { 2 }$ , 则 $\{ X _ { k } \}$ 满足中心极限定理，即有

$$
\lim _ {n \to + \infty} P \left\{\frac {\sum_ {k = 1} ^ {n} X _ {k} - n \mu}{\sqrt {n} \sigma} \leq x \right\} = \Phi (x).
$$

## 中心极限定理 (Central Limit Theorem)

## 林德伯格—列维定理或独立同分布中心极限定理

$\{ X _ { k } \} , k = 1 , 2 , \cdots$ 为相互独立, 具有相同分布的随机变量序列, 且 $E ( X _ { k } ) = \mu , D ( X _ { k } ) = \sigma ^ { 2 }$ , 则 $\{ X _ { k } \}$ 满足中心极限定理，即有

$$
\lim _ {n \to + \infty} P \left\{\frac {\sum_ {k = 1} ^ {n} X _ {k} - n \mu}{\sqrt {n} \sigma} \leq x \right\} = \Phi (x).
$$

直观理解：无论原始分布是什么，大量独立随机变量的和/均值都会趋近正态分布.

## 中心极限定理 (Central Limit Theorem)

## 林德伯格—列维定理或独立同分布中心极限定理

$\{ X _ { k } \} , k = 1 , 2 , \cdots$ 为相互独立, 具有相同分布的随机变量序列, 且 $E ( X _ { k } ) = \mu , D ( X _ { k } ) = \sigma ^ { 2 }$ , 则 $\{ X _ { k } \}$ 满足中心极限定理，即有

$$
\lim _ {n \to + \infty} P \left\{\frac {\sum_ {k = 1} ^ {n} X _ {k} - n \mu}{\sqrt {n} \sigma} \leq x \right\} = \Phi (x).
$$

直观理解：无论原始分布是什么，大量独立随机变量的和/均值都会趋近正态分布.

统计意义：这是参数估计和假设检验的理论基石，解释了为什么正态分布如此重要.

## 中心极限定理 (Central Limit Theorem)

林德伯格—列维定理或独立同分布中心极限定理

$\{ X _ { k } \} , k = 1 , 2 , \cdots$ 为相互独立, 具有相同分布的随机变量序列, 且 $E ( X _ { k } ) = \mu , D ( X _ { k } ) = \sigma ^ { 2 }$ , 则 $\{ X _ { k } \}$ 满足中心极限定理，即有

$$
\lim _ {n \to + \infty} P \left\{\frac {\sum_ {k = 1} ^ {n} X _ {k} - n \mu}{\sqrt {n} \sigma} \leq x \right\} = \Phi (x).
$$

直观理解：无论原始分布是什么，大量独立随机变量的和/均值都会趋近正态分布.

统计意义：这是参数估计和假设检验的理论基石，解释了为什么正态分布如此重要.

棣莫佛-拉普拉斯中心极限定理

设随机变量序列 $\{ Y _ { n } \} , Y _ { n } \sim B ( n , p ) , n = 1 , 2 , \cdot \cdot \cdot$ ，对于任意的实数 x ，有

$$
\lim _ {n \to + \infty} P \left\{\frac {Y _ {n} - n p}{\sqrt {n p (1 - p)}} \leq x \right\} = \Phi (x).
$$

## 第 1 章 统计量与抽样分布

Statistics and Sampling Distributions

总体、个体与样本

## 总体、个体与样本

简单随机样本的两大特性

## 总体、个体与样本

简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布

## 总体、个体与样本

## 简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位

## 总体、个体与样本

简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布

个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

## 总体、个体与样本

## 简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布

个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

简单随机样本：独立同分布于总体分布

## 总体、个体与样本

## 简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

简单随机样本：独立同分布于总体分布

• 代表性：每个 $X _ { i }$ 与总体X 同分布

## 总体、个体与样本

简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

简单随机样本：独立同分布于总体分布

• 代表性：每个 $X _ { i }$ 与总体X 同分布

• 独立性： $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 相互独立

## 总体、个体与样本

简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

简单随机样本：独立同分布于总体分布

• 代表性：每个 $X _ { i }$ 与总体X 同分布

• 独立性： $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 相互独立

• 样本是随机变量（抽样前），抽样后得到具体数值（样本观测值）

## 总体、个体与样本

## 简单随机样本的两大特性

总体 Population: 研究对象的全体.通常用一个随机变量 X 表示，其分布即为总体分布个体 Individual: 总体中的每个元素,每一个具体的研究对象或观测单位.

样本 Sample: 从总体中选出来的 n 个个体 $X _ { 1 } , . . . , X _ { n }$

简单随机样本：独立同分布于总体分布

• 代表性：每个 $X _ { i }$ 与总体X 同分布

• 独立性： $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 相互独立

• 样本是随机变量（抽样前），抽样后得到具体数值（样本观测值）

• 样本容量n：样本中包含的个体数量

## 统计量的定义

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若 $g$ 中不含任何未知参数，则称其为一个统计量

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若 $g$ 中不含任何未知参数，则称其为一个统计量

关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若 $g$ 中不含任何未知参数，则称其为一个统计量

关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若 $g$ 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若 $g$ 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若g 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 常见统计量分类

• 描述中心位置：样本均值、样本中位数、众数

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若g 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 常见统计量分类

• 描述中心位置：样本均值、样本中位数、众数

• 描述离散程度：样本方差、样本标准差、极差、四分位距

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若g 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 常见统计量分类

• 描述中心位置：样本均值、样本中位数、众数

• 描述离散程度：样本方差、样本标准差、极差、四分位距

• 描述分布形态：偏度、峰度

## 统计量的定义

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是来自总体 X 的样本， $g ( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ 是样本的函数，若g 中不含任何未知参数，则称其为一个统计量

## 关键理解

• 统计量是样本的函数，本身也是随机变量（抽样前）

• 一旦抽样完成得到观测值，统计量就成为具体的数值

• 核心：统计量中不能包含未知参数！

## 常见统计量分类

• 描述中心位置：样本均值、样本中位数、众数

• 描述离散程度：样本方差、样本标准差、极差、四分位距

• 描述分布形态：偏度、峰度

• 顺序统计量：最小顺序统计量、最大顺序统计量

常用统计量：样本均值与样本方差

## 常用统计量：样本均值与样本方差

样本均值 (Sample Mean): $\bar { X } = \textstyle { \frac { 1 } { n } } \cdot \sum _ { i = 1 } ^ { n } X _ { i }$

## 常用统计量：样本均值与样本方差

样本均值 (Sample Mean): $\bar { X } = \textstyle { \frac { 1 } { n } } \cdot \sum _ { i = 1 } ^ { n } X _ { i }$

样本方差 (Sample Variance) $\textstyle : S ^ { 2 } = { \frac { 1 } { n - 1 } } \cdot \sum _ { i = 1 } ^ { n } ( X _ { i } - { \bar { X } } ) ^ { 2 } $

## 常用统计量：样本均值与样本方差

样本均值 (Sample Mean): $\bar { X } = \textstyle { \frac { 1 } { n } } \cdot \sum _ { i = 1 } ^ { n } X _ { i }$

样本方差 (Sample Variance) $\textstyle : S ^ { 2 } = { \frac { 1 } { n - 1 } } \cdot \sum _ { i = 1 } ^ { n } ( X _ { i } - { \bar { X } } ) ^ { 2 } $

样本标准差： $S = \sqrt { S ^ { 2 } }$

## 常用统计量：样本均值与样本方差

样本均值 (Sample Mean): $\bar { X } = \textstyle { \frac { 1 } { n } } \cdot \sum _ { i = 1 } ^ { n } X _ { i }$

样本方差 (Sample Variance): $\begin{array} { r } { S ^ { 2 } = \frac { 1 } { n - 1 } \cdot \displaystyle \sum _ { i = 1 } ^ { n } ( X _ { i } - \bar { X } ) ^ { 2 } } \end{array}$

样本标准差： $S = \sqrt { S ^ { 2 } }$

• $E ( { \bar { X } } ) = \mu$ （等于总体均值）。

$V a r ( \bar { X } ) = \sigma ^ { 2 } / n$ （等于总体方差除以样本量）。

• n 越大， $\bar { X }$ 越集中在 $\mu$ 附近（大数定律保证）。

为什么除以 $n - 1$ 而不是 $n ?$

• 直观理解：样本均值 $\bar { X }$ 消耗了一个自由度。

• 本质原因：使 $S ^ { 2 }$ 成为总体方差 $\sigma ^ { 2 }$ 的无偏估计，即 $E ( S ^ { 2 } ) = \sigma ^ { 2 }$ 。

• 自由度：n −1 表示 有n −1 个独立的偏差信息可用。

## 经验分布函数

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

重要性质

$F _ { n } ( x )$ 是一个阶梯函数，在每个样本点处跳跃 $1 / n$

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

重要性质

$F _ { n } ( x )$ 是一个阶梯函数，在每个样本点处跳跃 $1 / n$

• 对固定的 $x , n \cdot F _ { n } ( x ) \sim B ( n , F ( x ) )$ （二项分布）.

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

重要性质

$F _ { n } ( x )$ 是一个阶梯函数，在每个样本点处跳跃 $1 / n$

• 对固定的 $x , n \cdot F _ { n } ( x ) \sim B ( n , F ( x ) )$ （二项分布）.

• $E [ F ( x ) ] = F ( x )$ ：经验分布函数是总体分布函数的无偏估计.

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

重要性质

$F _ { n } ( x )$ 是一个阶梯函数，在每个样本点处跳跃 $1 / n$

• 对固定的 $x , n \cdot F _ { n } ( x ) \sim B ( n , F ( x ) )$ （二项分布）.

• $E [ F ( x ) ] = F ( x )$ ：经验分布函数是总体分布函数的无偏估计.

• 格列汶科定理：当 $n \to \infty$ 时， $F _ { n } ( x )$ 以概率 1 一致收敛于 $F ( x )$

## 经验分布函数

定义设 $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ 是总体的样本，对任意实数x，定义

$$
F _ {n} (x) = \frac {\text {样本中} \leq x \text {的个数}}{n}
$$

称 $F _ { n } ( x )$ 为经验分布函数 (Empirical Distribution Function)。

重要性质

$F _ { n } ( x )$ 是一个阶梯函数，在每个样本点处跳跃 $1 / n$

• 对固定的 $x , n \cdot F _ { n } ( x ) \sim B ( n , F ( x ) )$ （二项分布）.

• $E [ F ( x ) ] = F ( x )$ ：经验分布函数是总体分布函数的无偏估计.

• 格列汶科定理：当 $n \to \infty$ 时， $F _ { n } ( x )$ 以概率 1 一致收敛于 $F ( x )$

• 统计意义：样本量足够大时，可以用经验分布函数近似总体分布.

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

定理: 设 $X _ { 1 } , . . . , X _ { n }$ 是来自 $N ( \mu , \sigma ^ { 2 } )$ 的样本, 则

1 $\bar { X } \sim N ( \mu , \sigma ^ { 2 } / n )$ （样本均值服从正态分布）.

2 $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$ （标准化的样本方差服从卡方分布）.

3 $\bar { X }$ 与 $S ^ { 2 }$ 相互独立（正态总体下均值与方差独立）.

4 $( X - \mu ) / ( S / \sqrt { n } ) \sim t ( n - 1 )$ （t 统计量）

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

定理: 设 $X _ { 1 } , . . . , X _ { n }$ 是来自 $N ( \mu , \sigma ^ { 2 } )$ 的样本, 则

1 $\bar { X } \sim N ( \mu , \sigma ^ { 2 } / n )$ （样本均值服从正态分布）.

2 $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$ （标准化的样本方差服从卡方分布）.

3 $\bar { X }$ 与 $S ^ { 2 }$ 相互独立（正态总体下均值与方差独立）.

4 $( X - \mu ) / ( S / \sqrt { n } ) \sim t ( n - 1 )$ （t 统计量）

推导思路

1 通过正态分布的线性组合性质直接得到.

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

定理: 设 $X _ { 1 } , . . . , X _ { n }$ 是来自 $N ( \mu , \sigma ^ { 2 } )$ 的样本, 则

1 $\bar { X } \sim N ( \mu , \sigma ^ { 2 } / n )$ （样本均值服从正态分布）.

2 $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$ （标准化的样本方差服从卡方分布）.

3 $\bar { X }$ 与 $S ^ { 2 }$ 相互独立（正态总体下均值与方差独立）.

4 $( X - \mu ) / ( S / \sqrt { n } ) \sim t ( n - 1 )$ （t 统计量）

推导思路

1 通过正态分布的线性组合性质直接得到.

2 利用正交变换将 $S ^ { 2 }$ 转化为n −1 个独立标准正态的平方和.

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

定理: 设 $X _ { 1 } , . . . , X _ { n }$ 是来自 $N ( \mu , \sigma ^ { 2 } )$ 的样本, 则

1 $\bar { X } \sim N ( \mu , \sigma ^ { 2 } / n )$ （样本均值服从正态分布）.

2 $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$ （标准化的样本方差服从卡方分布）.

3 $\bar { X }$ 与 $S ^ { 2 }$ 相互独立（正态总体下均值与方差独立）.

4 $( X - \mu ) / ( S / \sqrt { n } ) \sim t ( n - 1 )$ （t 统计量）

推导思路

1 通过正态分布的线性组合性质直接得到.

2 利用正交变换将 $S ^ { 2 }$ 转化为n −1 个独立标准正态的平方和.

3 利用正态分布的独立性条件证明，这是正态总体特有的性质.

## 单正态总体抽样分布定理

核心定理，后续推断的理论基础

定理: 设 $X _ { 1 } , . . . , X _ { n }$ 是来自 $N ( \mu , \sigma ^ { 2 } )$ 的样本, 则

1 $\bar { X } \sim N ( \mu , \sigma ^ { 2 } / n )$ （样本均值服从正态分布）.

2 $( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$ （标准化的样本方差服从卡方分布）.

3 $\bar { X }$ 与 $S ^ { 2 }$ 相互独立（正态总体下均值与方差独立）.

4 $( X - \mu ) / ( S / \sqrt { n } ) \sim t ( n - 1 )$ （t 统计量）

推导思路

1 通过正态分布的线性组合性质直接得到.

2 利用正交变换将 $S ^ { 2 }$ 转化为n −1 个独立标准正态的平方和.

3 利用正态分布的独立性条件证明，这是正态总体特有的性质.

4 由⃝1 ⃝2 ⃝3 结合 t 分布定义直接推出.

## 双正态总体抽样分布定理

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

则有：

$$
① \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}} \sim N (0, 1).
$$

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

则有：

$$
① \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}} \sim N (0, 1).
$$

2 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 } = \sigma ^ { 2 }$ （方差齐性）时， $\begin{array} { r } { \frac { ( \overline { { X } } - \overline { { Y } } ) - ( \mu _ { 1 } - \mu _ { 2 } ) } { S _ { w } \sqrt { \frac { 1 } { n _ { 1 } } + \frac { 1 } { n _ { 2 } } } } \sim t ( n _ { 1 } + n _ { 2 } - 2 ) . } \end{array}$

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

则有：

$$
① \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}} \sim N (0, 1).
$$

2 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 } = \sigma ^ { 2 }$ （方差齐性）时， $\begin{array} { r } { \frac { ( \overline { { X } } - \overline { { Y } } ) - ( \mu _ { 1 } - \mu _ { 2 } ) } { S _ { w } \sqrt { \frac { 1 } { n _ { 1 } } + \frac { 1 } { n _ { 2 } } } } \sim t ( n _ { 1 } + n _ { 2 } - 2 ) . } \end{array}$

3 $\begin{array} { r } { \frac { S _ { 1 } ^ { 2 } / \sigma _ { 1 } ^ { 2 } } { S _ { 2 } ^ { 2 } / \sigma _ { 2 } ^ { 2 } } \sim F ( n _ { 1 } - 1 , n _ { 2 } - 1 ) } \end{array}$

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

则有：

$$
① \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}} \sim N (0, 1).
$$

2 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 } = \sigma ^ { 2 }$ （方差齐性）时， $\begin{array} { r } { \frac { ( \overline { { X } } - \overline { { Y } } ) - ( \mu _ { 1 } - \mu _ { 2 } ) } { S _ { w } \sqrt { \frac { 1 } { n _ { 1 } } + \frac { 1 } { n _ { 2 } } } } \sim t ( n _ { 1 } + n _ { 2 } - 2 ) . } \end{array}$

3 $\begin{array} { r } { \frac { S _ { 1 } ^ { 2 } / \sigma _ { 1 } ^ { 2 } } { S _ { 2 } ^ { 2 } / \sigma _ { 2 } ^ { 2 } } \sim F ( n _ { 1 } - 1 , n _ { 2 } - 1 ) } \end{array}$

4 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 }$ 时， $\begin{array} { r } { \frac { S _ { 1 } ^ { 2 } } { S _ { 2 } ^ { 2 } } \sim F ( n _ { 1 } - 1 , n _ { 2 } - 1 ) } \end{array}$

## 双正态总体抽样分布定理

定理:设总体 $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } ) , X _ { 1 } , X _ { 2 } , . . . , X _ { n _ { 1 } }$ 是来自X 的简单随机样本， $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n _ { 2 } }$ 是来自Y 的简单随机样本，且两组样本相互独立。记

$$
\begin{array}{r l} & {\overline {{X}} = \frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} X _ {i}, \quad \overline {{Y}} = \frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} Y _ {j}, \quad S _ {1} ^ {2} \frac {1}{n _ {1} - 1} \sum_ {i = 1} ^ {n _ {1}} (X _ {i} - \overline {{X}}) ^ {2}, \quad S _ {2} ^ {2} = \frac {1}{n _ {2} - 1} \sum_ {j = 1} ^ {n _ {2}} (Y _ {j} - \overline {{Y}}) ^ {2},} \\ & {S _ {w} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}, \quad S _ {w} = \sqrt {S _ {w} ^ {2}},} \end{array}
$$

则有：

1 $\frac { ( \overline { { X } } - \overline { { Y } } ) - ( \mu _ { 1 } - \mu _ { 2 } ) } { \sqrt { \frac { \sigma _ { 1 } ^ { 2 } } { n _ { 1 } } + \frac { \sigma _ { 2 } ^ { 2 } } { n _ { 2 } } } } \sim N ( 0 , 1 ) .$

2 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 } = \sigma ^ { 2 }$ （方差齐性）时， $\begin{array} { r } { \frac { ( \overline { { X } } - \overline { { Y } } ) - ( \mu _ { 1 } - \mu _ { 2 } ) } { S _ { w } \sqrt { \frac { 1 } { n _ { 1 } } + \frac { 1 } { n _ { 2 } } } } \sim t ( n _ { 1 } + n _ { 2 } - 2 ) . } \end{array}$

3 $\begin{array} { r } { \frac { S _ { 1 } ^ { 2 } / \sigma _ { 1 } ^ { 2 } } { S _ { 2 } ^ { 2 } / \sigma _ { 2 } ^ { 2 } } \sim F ( n _ { 1 } - 1 , n _ { 2 } - 1 ) } \end{array}$

4 当 $\sigma _ { 1 } ^ { 2 } = \sigma _ { 2 } ^ { 2 }$ 时， $\begin{array} { r } { \frac { S _ { 1 } ^ { 2 } } { S _ { 2 } ^ { 2 } } \sim F ( n _ { 1 } - 1 , n _ { 2 } - 1 ) } \end{array}$

$$
⑤ \frac {\frac {1}{n _ {1}} \sum_ {i = 1} ^ {n _ {1}} (\frac {X _ {i} - \mu_ {1}}{\sigma_ {1}}) ^ {2}}{\frac {1}{n _ {2}} \sum_ {j = 1} ^ {n _ {2}} (\frac {y _ {j} - \mu_ {2}}{\sigma_ {2}}) ^ {2}} \sim F (n _ {1}, n _ {2}).
$$

## 三大抽样分布总结对比

## 三大抽样分布总结对比

<table><tr><td>分布</td><td> $\chi^2$ 分布</td><td>t分布</td><td>F分布</td></tr><tr><td>构造方式</td><td>n个独立N(0,1)的平方和</td><td> $\frac{N(0,1)}{\sqrt{\chi^2(n)/n}}$ </td><td> $\frac{\chi^2(n_1)/n_1}{\chi^2(n_2)/n_2}$ </td></tr><tr><td>自由度</td><td>n</td><td>n</td><td> $n_1,n_2$ </td></tr><tr><td>取值范围</td><td>(0,+∞)</td><td>(-∞,+∞)</td><td>(0,+∞)</td></tr><tr><td>期望</td><td>n</td><td>0</td><td> $n_2/(n_2-2)(n_2>2)$ </td></tr><tr><td>方差</td><td>2n</td><td> $n/(n-2)(n>2)$ </td><td>复杂公式</td></tr><tr><td>主要用途</td><td>方差检验、拟合优度检验</td><td>均值检验(σ未知)</td><td>方差比检验、方差分析</td></tr></table>

## 三大抽样分布总结对比

<table><tr><td>分布</td><td> $\chi^2$ 分布</td><td>t分布</td><td>F分布</td></tr><tr><td>构造方式</td><td>n个独立N(0,1)的平方和</td><td> $\frac{N(0,1)}{\sqrt{\chi^2(n)/n}}$ </td><td> $\frac{\chi^2(n_1)/n_1}{\chi^2(n_2)/n_2}$ </td></tr><tr><td>自由度</td><td>n</td><td>n</td><td> $n_1,n_2$ </td></tr><tr><td>取值范围</td><td>(0,+∞)</td><td>(-∞,+∞)</td><td>(0,+∞)</td></tr><tr><td>期望</td><td>n</td><td>0</td><td> $n_2/(n_2-2)(n_2>2)$ </td></tr><tr><td>方差</td><td>2n</td><td> $n/(n-2)(n>2)$ </td><td>复杂公式</td></tr><tr><td>主要用途</td><td>方差检验、拟合优度检验</td><td>均值检验(σ未知)</td><td>方差比检验、方差分析</td></tr></table>

## 三大分布之间的关系

• t(n) 的平方 $= F ( 1 , n )$

## 三大抽样分布总结对比

<table><tr><td>分布</td><td> $\chi^2$ 分布</td><td>t分布</td><td>F分布</td></tr><tr><td>构造方式</td><td>n个独立N(0,1)的平方和</td><td> $\frac{N(0,1)}{\sqrt{\chi^2(n)/n}}$ </td><td> $\frac{\chi^2(n_1)/n_1}{\chi^2(n_2)/n_2}$ </td></tr><tr><td>自由度</td><td>n</td><td>n</td><td> $n_1,n_2$ </td></tr><tr><td>取值范围</td><td>(0,+∞)</td><td>(-∞,+∞)</td><td>(0,+∞)</td></tr><tr><td>期望</td><td>n</td><td>0</td><td> $n_2/(n_2-2)(n_2>2)$ </td></tr><tr><td>方差</td><td>2n</td><td> $n/(n-2)(n>2)$ </td><td>复杂公式</td></tr><tr><td>主要用途</td><td>方差检验、拟合优度检验</td><td>均值检验(σ未知)</td><td>方差比检验、方差分析</td></tr></table>

## 三大分布之间的关系

• t(n) 的平方 $= F ( 1 , n )$

• $n \to \infty$ 时， $t ( n )  N ( 0 , 1 ) , \chi ^ { 2 } ( n )  N ( n , 2 n )$

## 三大抽样分布总结对比

<table><tr><td>分布</td><td> $\chi^2$ 分布</td><td>t分布</td><td>F分布</td></tr><tr><td>构造方式</td><td>n个独立N(0,1)的平方和</td><td> $\frac{N(0,1)}{\sqrt{\chi^2(n)/n}}$ </td><td> $\frac{\chi^2(n_1)/n_1}{\chi^2(n_2)/n_2}$ </td></tr><tr><td>自由度</td><td>n</td><td>n</td><td> $n_1,n_2$ </td></tr><tr><td>取值范围</td><td>(0,+∞)</td><td>(-∞,+∞)</td><td>(0,+∞)</td></tr><tr><td>期望</td><td>n</td><td>0</td><td> $n_2/(n_2-2)(n_2>2)$ </td></tr><tr><td>方差</td><td>2n</td><td> $n/(n-2)(n>2)$ </td><td>复杂公式</td></tr><tr><td>主要用途</td><td>方差检验、拟合优度检验</td><td>均值检验(σ未知)</td><td>方差比检验、方差分析</td></tr></table>

## 三大分布之间的关系

• t(n) 的平方 $= F ( 1 , n )$

• $n \to \infty$ 时， $t ( n )  N ( 0 , 1 ) , \chi ^ { 2 } ( n )  N ( n , 2 n )$

• 三大分布都可以由正态分布构造而来，体现了正态分布的核心地位

## 本章小结

## 本章小结

## 核心概念

• 总体 → 样本 → 统计量：推断的基本路径

• 简单随机样本：独立同分布

• 统计量：不含未知参数的样本函数

## 本章小结

## 核心概念

• 总体 → 样本 → 统计量：推断的基本路径

• 简单随机样本：独立同分布

• 统计量：不含未知参数的样本函数

## 核心结论

• 样本均值 $\bar { X }$ 是总体均值的”好”估计： $E ( X ) = \mu , V a r ( X ) = \sigma ^ { 2 } / n$

• 样本方差 $S ^ { 2 }$ 除以 $n - 1$ 保证无偏性

• 正态总体下， $\bar { X }$ 与 $S ^ { 2 }$ 独立，且有精确的 $\chi ^ { 2 }$ 、t、F 分布

## 本章小结

## 核心概念

• 总体 → 样本 → 统计量：推断的基本路径

• 简单随机样本：独立同分布

• 统计量：不含未知参数的样本函数

## 核心结论

• 样本均值 $\bar { X }$ 是总体均值的”好”估计： $E ( X ) = \mu , V a r ( X ) = \sigma ^ { 2 } / n$

• 样本方差 $S ^ { 2 }$ 除以 $n - 1$ 保证无偏性

• 正态总体下， $\bar { X }$ 与 $S ^ { 2 }$ 独立，且有精确的 $\chi ^ { 2 } , \ t , \ F$ 分布

## 下章预告

• 第2 章：参数估计——利用样本统计量来估计总体中的未知参数

• 分为点估计和区间估计两大类，将大量运用本章的抽样分布结论

## 第 2 章 参数估计

Parameter Estimation

## 点估计概述

## 点估计概述

什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数θ，这就是点估计.

## 点估计概述

什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ ，这就是点估计.

点估计量 Estimator： ${ \hat { \theta } } ( X _ { 1 } , . . . , X _ { n } )$

## 点估计概述

什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ ，这就是点估计.

点估计量 Estimator： ${ \hat { \theta } } ( X _ { 1 } , . . . , X _ { n } )$

估计值 Estimate： ${ \hat { \theta } } ( x _ { 1 } , . . . , x _ { n } )$

## 点估计概述

什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ 这就是点估计.

点估计量 E $\mathrm { s t i m a t o r } \colon \hat { \theta } ( X _ { 1 } , . . . , X _ { n } )$

估计值 Estimate： ${ \hat { \theta } } ( x _ { 1 } , . . . , x _ { n } )$

估计量是样本的函数，是随机变量；用于估计的规则或公式。

## 点估计概述

## 什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ 这就是点估计.

点估计量 E $\mathrm { s t i m a t o r } \colon \hat { \theta } ( X _ { 1 } , . . . , X _ { n } )$

估计值 Estimate： ${ \hat { \theta } } ( x _ { 1 } , . . . , x _ { n } )$

估计量是样本的函数，是随机变量；用于估计的规则或公式。

代入具体样本观测值后得到的具体数值。

## 点估计概述

## 什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ ，这就是点估计.

点估计量 E $\mathrm { s t i m a t o r } \colon \hat { \theta } ( X _ { 1 } , . . . , X _ { n } )$

估计值 Estimate： ${ \hat { \theta } } ( x _ { 1 } , . . . , x _ { n } )$

估计量是样本的函数，是随机变量；用于估计的规则或公式。

代入具体样本观测值后得到的具体数值。

两种主要的点估计方法

• 矩估计法 (Method of Moments)：用样本矩代替总体矩。

## 点估计概述

## 什么是点估计？

设总体 X 的分布函数为 $F ( x ; \theta )$ ，其中 θ 是未知参数。从总体中抽取样本 $X _ { 1 } , . . . , X _ { n }$ ，构造一个统计量

$$
\hat {\theta} = \hat {\theta} (X _ {1},..., X _ {n}).
$$

用它来估计未知参数 $\theta ,$ 这就是点估计.

点估计量 E $\mathrm { s t i m a t o r } \colon \hat { \theta } ( X _ { 1 } , . . . , X _ { n } )$

估计值 Estimate： ${ \hat { \theta } } ( x _ { 1 } , . . . , x _ { n } )$

估计量是样本的函数，是随机变量；用于估计的规则或公式。

代入具体样本观测值后得到的具体数值。

两种主要的点估计方法

• 矩估计法 (Method of Moments)：用样本矩代替总体矩。

• 极大似然估计 (Maximum Likelihood Estimation)：选择使观测结果概率最大的参数。

矩估计法：原理与步骤

## 矩估计法：原理与步骤

基本思想

## 矩估计法：原理与步骤

## 基本思想

用样本矩代替相应的总体矩，用样本矩的函数代替总体矩的同一函数。

## 矩估计法：原理与步骤

## 基本思想

用样本矩代替相应的总体矩，用样本矩的函数代替总体矩的同一函数。

理论依据

大数定律：样本矩依概率收敛于总体矩（样本量足够大时，样本矩接近总体矩）。

## 矩估计法：原理与步骤

## 基本思想

用样本矩代替相应的总体矩，用样本矩的函数代替总体矩的同一函数。

## 理论依据

大数定律：样本矩依概率收敛于总体矩（样本量足够大时，样本矩接近总体矩）。

## 一般步骤

• 第1 步：写出总体的 k 阶原点矩 $\mu _ { k } = E ( X ^ { k } )$ ，通常是未知参数的函数.

• 第2 步：计算样本的k 阶原点矩 $A _ { k } = ( 1 / n ) \cdot \textstyle \sum X _ { i } ^ { k }$ .

• 第3 步：令 $\mu _ { k } = A _ { k } ~ ( k = 1 , 2 , \ldots$ , 直到方程个数等于未知参数个数）.

• 第4 步：解方程组，得到未知参数的解，即为矩估计量.

## 矩估计法：原理与步骤

## 基本思想

用样本矩代替相应的总体矩，用样本矩的函数代替总体矩的同一函数。

## 理论依据

大数定律：样本矩依概率收敛于总体矩（样本量足够大时，样本矩接近总体矩）。

## 一般步骤

• 第1 步：写出总体的 k 阶原点矩 $\mu _ { k } = E ( X ^ { k } )$ ，通常是未知参数的函数.

• 第2 步：计算样本的k 阶原点矩 $A _ { k } = ( 1 / n ) \cdot \textstyle \sum X _ { i } ^ { k }$

• 第3 步：令 $\mu _ { k } = A _ { k } ~ ( k = 1 , 2 , \ldots$ , 直到方程个数等于未知参数个数）.

• 第4 步：解方程组，得到未知参数的解，即为矩估计量.

## 记忆口诀

• ”有几个未知参数，就列几阶矩方程”.

矩估计法：实例

矩估计法：实例

例 1：指数分布 Exp(λ)

矩估计法：实例

例1：指数分布 $E x p ( \lambda )$

例2：正态分布 $N ( \mu , \sigma ^ { 2 } )$

## 矩估计法：实例

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例1：指数分布 $Exp(\lambda)$   
例2：正态分布 $N(\mu ,\sigma^2)$   
总体 $X\sim Exp(\lambda)$ ，概率密度 $f(x) = \lambda e^{-\lambda x},x &gt; 0$   
一阶矩： $E(X) = 1 / \lambda$   
令 $1 / \lambda = \bar{X}\Rightarrow \hat{\lambda} = 1 / \bar{X}$   
结论： $\lambda$ 的矩估计量为 $1 / \bar{X}$
</div>

## 矩估计法：实例

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例1：指数分布 $Exp(\lambda)$   
例2：正态分布 $N(\mu ,\sigma^2)$   
总体 $X\sim Exp(\lambda)$ ，概率密度 $f(x) = \lambda e^{-\lambda x},x &gt; 0$   
一阶矩： $E(X) = 1 / \lambda$   
令 $1 / \lambda = \bar{X}\Rightarrow \hat{\lambda} = 1 / \bar{X}$   
结论： $\lambda$ 的矩估计量为 $1 / \bar{X}$   
总体 $X\sim N(\mu ,\sigma^2)$ ，有两个未知参数 $\mu$ 和 $\sigma^2$   
一阶矩： $E(X) = \mu = \bar{X}\Rightarrow \hat{\mu} = \bar{X}$   
二阶矩： $E(X^{2}) = \sigma^{2} + \mu^{2} = (1 / n)\cdot \sum X_{i}^{2}$   
代入 $\hat{\mu} = \bar{X}$ ，解得： $\hat{\sigma}^2 = (1 / n)\cdot \sum (X_i - X)^2 = S_n^2$ （样本二阶中心矩，除以 $n$ ）
</div>

## 矩估计法：实例

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
例1：指数分布 $Exp(\lambda)$   
例2：正态分布 $N(\mu ,\sigma^2)$   
总体 $X\sim Exp(\lambda)$ ，概率密度 $f(x) = \lambda e^{-\lambda x},x &gt; 0$   
一阶矩： $E(X) = 1 / \lambda$   
令 $1 / \lambda = \bar{X}\Rightarrow \hat{\lambda} = 1 / \bar{X}$   
结论： $\lambda$ 的矩估计量为 $1 / \bar{X}$   
总体 $X\sim N(\mu ,\sigma^2)$ ，有两个未知参数 $\mu$ 和 $\sigma^2$   
一阶矩： $E(X) = \mu = \bar{X}\Rightarrow \hat{\mu} = \bar{X}$   
二阶矩： $E(X^{2}) = \sigma^{2} + \mu^{2} = (1 / n)\cdot \sum X_{i}^{2}$   
代入 $\hat{\mu} = \bar{X}$ ，解得： $\hat{\sigma}^2 = (1 / n)\cdot \sum (X_i - X)^2 = S_n^2$ （样本二阶中心矩，除以 $n$ ）注意：矩估计得到的方差是除以 $n$ 的，不是除以 $n - 1!$
</div>

极大似然估计：似然函数

# 极大似然估计：似然函数

基本思想

## 极大似然估计：似然函数

基本思想

”已经发生的事情，就是概率最大的事情”

## 极大似然估计：似然函数

## 基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

## 极大似然估计：似然函数

## 基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

## 似然函数定义

设总体X 具有概率质量/密度函数 $f ( x ; \theta ) , X _ { 1 } , . . . , X _ { n }$ 是样本，则似然函数为：

## 极大似然估计：似然函数

## 基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

## 似然函数定义

设总体X 具有概率质量/密度函数 $f ( x ; \theta ) , X _ { 1 } , . . . , X _ { n }$ 是样本，则似然函数为：

$$
L (\theta) = L (\theta ; x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta)
$$

## 极大似然估计：似然函数

## 基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

## 似然函数定义

设总体X 具有概率质量/密度函数 $f ( x ; \theta ) , X _ { 1 } , . . . , X _ { n }$ 是样本，则似然函数为：

$$
L (\theta) = L (\theta ; x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta)
$$

似然函数是 θ 的函数（样本观测值看作固定常数）。

## 极大似然估计：似然函数

## 基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

似然函数定义

设总体X 具有概率质量/密度函数 $f ( x ; \theta ) , X _ { 1 } , . . . , X _ { n }$ 是样本，则似然函数为：

$$
L (\theta) = L (\theta ; x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta)
$$

似然函数是 θ 的函数（样本观测值看作固定常数）。

对数似然函数：

$$
l (\theta) = l n L (\theta) = \sum_ {i = 1} ^ {n} l n f (x _ {i}; \theta)
$$

（取对数将乘积变求和，便于求导计算）

## 极大似然估计：似然函数

基本思想

”已经发生的事情，就是概率最大的事情”

在所有可能的参数取值中，选择使观测到这组样本的”可能性”最大的那个参数值。

似然函数定义

设总体X 具有概率质量/密度函数 $f ( x ; \theta ) , X _ { 1 } , . . . , X _ { n }$ 是样本，则似然函数为：

$$
L (\theta) = L (\theta ; x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta)
$$

似然函数是 θ 的函数（样本观测值看作固定常数）。

对数似然函数：

$$
l (\theta) = l n L (\theta) = \sum_ {i = 1} ^ {n} l n f (x _ {i}; \theta)
$$

（取对数将乘积变求和，便于求导计算）

关键区别

• 密度函数 $f ( x ; \theta ) \colon \theta$ 固定，x 变化 —— 描述不同 x 的概率

• 似然函数 $L ( \theta ) \colon x$ 固定，θ 变化 —— 描述不同 θ 下出现当前样本的可能性

极大似然估计：求解与实例

## 极大似然估计：求解与实例

求解步骤

## 极大似然估计：求解与实例

## 求解步骤

• 写出似然函数 $L ( \theta ) = \prod f ( x _ { i } ; \theta )$

• 取对数 $\begin{array} { r } { l ( \theta ) = l n L ( \theta ) = \sum l n f ( x _ { i } ; \theta ) } \end{array}$

• 对 θ 求导，令 $d l / d \theta = 0$

• 解方程，得到极大似然估计 $\hat { \theta }$

## 极大似然估计：求解与实例

## 求解步骤

• 写出似然函数 $L ( \theta ) = \prod f ( x _ { i } ; \theta )$

• 取对数 $\begin{array} { r } { l ( \theta ) = l n L ( \theta ) = \sum l n f ( x _ { i } ; \theta ) } \end{array}$

• 对 θ 求导，令 $d l / d \theta = 0$

• 解方程，得到极大似然估计 $\hat { \theta }$

例：正态分布 $N ( \mu , \sigma ^ { 2 } )$ 的 $\mathrm { M L E }$

$$
L (\mu , \sigma^ {2}) = \prod (\frac {1}{\sqrt {2 \pi \sigma^ {2}}} \cdot e x p (- \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}}
$$

$$
l (\mu , \sigma^ {2}) = - \frac {n}{2} l n (2 \pi) - \frac {n}{2} l n (\sigma^ {2}) - \frac {1}{2 \sigma^ {2}} \cdot \sum (x _ {i} - \mu) ^ {2}
$$

对 $\mu$ 求偏导得： ${ \hat { \mu } } = { \bar { X } }$ 对 $\sigma ^ { 2 }$ 求偏导得： $\begin{array} { r } { \hat { \sigma } ^ { 2 } = \frac { 1 } { n } \cdot \sum ( X _ { i } - \bar { X } ) ^ { 2 } } \end{array}$

## 极大似然估计：求解与实例

## 求解步骤

• 写出似然函数 $L ( \theta ) = \prod f ( x _ { i } ; \theta )$

• 取对数 $\begin{array} { r } { l ( \theta ) = l n L ( \theta ) = \sum l n f ( x _ { i } ; \theta ) } \end{array}$

• 对 θ 求导，令 $d l / d \theta = 0$

• 解方程，得到极大似然估计 $\hat { \theta }$

例：正态分布 $N ( \mu , \sigma ^ { 2 } )$ 的 MLE

$$
L (\mu , \sigma^ {2}) = \prod (\frac {1}{\sqrt {2 \pi \sigma^ {2}}} \cdot e x p (- \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}}
$$

$$
l (\mu , \sigma^ {2}) = - \frac {n}{2} l n (2 \pi) - \frac {n}{2} l n (\sigma^ {2}) - \frac {1}{2 \sigma^ {2}} \cdot \sum (x _ {i} - \mu) ^ {2}
$$

对 $\mu$ 求偏导得： ${ \hat { \mu } } = { \bar { X } }$ 对 $\sigma ^ { 2 }$ 求偏导得： $\begin{array} { r } { \hat { \sigma } ^ { 2 } = \frac { 1 } { n } \cdot \sum ( X _ { i } - \bar { X } ) ^ { 2 } } \end{array}$

结论：正态分布的 MLE 与矩估计结果相同（这是特例）

## 矩估计 vs 极大似然估计

## 矩估计 vs 极大似然估计

<table><tr><td>对比维度</td><td>矩估计法 (MOM)</td><td>极大似然估计 (MLE)</td></tr><tr><td>基本思想</td><td>样本矩 ≈ 总体矩</td><td>选择使观测可能性最大的参数</td></tr><tr><td>理论依据</td><td>大数定律</td><td>似然原理</td></tr><tr><td>计算难度</td><td>相对简单(解方程)</td><td>可能复杂(求极值)</td></tr><tr><td>大样本性质</td><td>一致性</td><td>渐近有效性、渐近正态(更优)</td></tr><tr><td>对分布假设</td><td>弱(只需要矩存在)</td><td>强(需要知道分布形式)</td></tr><tr><td>适用场景</td><td>分布形式未知时</td><td>分布形式已知时(更有效)</td></tr></table>

## 矩估计 vs 极大似然估计

<table><tr><td>对比维度</td><td>矩估计法 (MOM)</td><td>极大似然估计 (MLE)</td></tr><tr><td>基本思想</td><td>样本矩 ≈ 总体矩</td><td>选择使观测可能性最大的参数</td></tr><tr><td>理论依据</td><td>大数定律</td><td>似然原理</td></tr><tr><td>计算难度</td><td>相对简单(解方程)</td><td>可能复杂(求极值)</td></tr><tr><td>大样本性质</td><td>一致性</td><td>渐近有效性、渐近正态(更优)</td></tr><tr><td>对分布假设</td><td>弱(只需要矩存在)</td><td>强(需要知道分布形式)</td></tr><tr><td>适用场景</td><td>分布形式未知时</td><td>分布形式已知时(更有效)</td></tr></table>

总结

## 矩估计 vs 极大似然估计

<table><tr><td>对比维度</td><td>矩估计法 (MOM)</td><td>极大似然估计 (MLE)</td></tr><tr><td>基本思想</td><td>样本矩 ≈ 总体矩</td><td>选择使观测可能性最大的参数</td></tr><tr><td>理论依据</td><td>大数定律</td><td>似然原理</td></tr><tr><td>计算难度</td><td>相对简单(解方程)</td><td>可能复杂(求极值)</td></tr><tr><td>大样本性质</td><td>一致性</td><td>渐近有效性、渐近正态(更优)</td></tr><tr><td>对分布假设</td><td>弱(只需要矩存在)</td><td>强(需要知道分布形式)</td></tr><tr><td>适用场景</td><td>分布形式未知时</td><td>分布形式已知时(更有效)</td></tr></table>

## 总结

• 知道总体分布形式 → 优先用 MLE（大样本下更优）；

• 不知道分布形式→可用矩估计

估计量的评价标准：无偏性

## 估计量的评价标准：无偏性

定义

设 $\hat { \theta }$ 是 $\theta$ 的估计量，若 $E ( { \hat { \theta } } ) = \theta$ 对所有 $\theta$ 成立，

则称 $\hat { \theta }$ 是 $\theta$ 的无偏估计量 (Unbiased Estimator)。

## 估计量的评价标准：无偏性

定义

设 $\hat { \theta }$ 是 θ 的估计量，若 $E ( { \hat { \theta } } ) = \theta$ 对所有 θ 成立，

则称 $\hat { \theta }$ 是 θ 的无偏估计量 (Unbiased Estimator)。

直观理解

• 无偏性意味着：反复抽样多次，每次得到一个估计值，这些估计值的平均值等于真实值。

• 没有系统偏差，不会系统性地高估或低估。

## 估计量的评价标准：无偏性

定义

设 $\hat { \theta }$ 是 θ 的估计量，若 $E ( { \hat { \theta } } ) = \theta$ 对所有 $\theta$ 成立，

则称 $\hat { \theta }$ 是 θ 的无偏估计量 (Unbiased Estimator)。

直观理解

• 无偏性意味着：反复抽样多次，每次得到一个估计值，这些估计值的平均值等于真实值。

• 没有系统偏差，不会系统性地高估或低估。

## 重要结论

• 样本均值 $\bar { X }$ 是总体均值 $\mu$ 的无偏估计： $E ( { \bar { X } } ) = \mu$

• 样本方差 $S ^ { 2 }$ （除以 n −1）是总体方差 $\sigma ^ { 2 }$ 的无偏估计： $E ( S ^ { 2 } ) = \sigma ^ { 2 }$

• 样本二阶中心矩 $S _ { n } ^ { 2 }$ （除以n）是有偏的： $E ( S _ { n } ^ { 2 } ) = ( n - 1 ) / n \cdot \sigma ^ { 2 }$

• 无偏估计不唯一：一个参数可以有多个无偏估计量

• 有偏估计可以修正： $S ^ { 2 } = n / ( n - 1 ) \cdot S _ { n } ^ { 2 }$ 修正后成为无偏

为什么样本方差除以n −1？

## 为什么样本方差除以 $n - 1 :$

证明思路

要证： $E [ S ^ { 2 } ] = \sigma ^ { 2 }$ ，其中 $S ^ { 2 } = ( 1 / ( n - 1 ) ) \cdot \Sigma ( X _ { i } - X ) ^ { 2 }$

## 为什么样本方差除以 $n - 1 :$

## 证明思路

要证： $E [ S ^ { 2 } ] = \sigma ^ { 2 }$ ，其中 $S ^ { 2 } = ( 1 / ( n - 1 ) ) \cdot \Sigma ( X _ { i } - X ) ^ { 2 }$

证明关键步骤：

• 展开平方和： $\scriptstyle \sum ( X _ { i } - { \bar { X } } ) ^ { 2 } = \sum [ ( X _ { i } - \mu ) - ( { \bar { X } } - \mu ) ] ^ { 2 }$ = ∑︁(X<sub>i</sub> − µ)<sup>2</sup> − 2(X<sup>¯</sup> − µ) ∑︁(X<sub>i</sub> − µ) + n(X<sup>¯</sup> − µ)<sup>2</sup> = ∑︁(X<sub>i</sub> − µ)<sup>2</sup> − n(X<sup>¯</sup> − µ)<sup>2</sup>

• 两边取期望：

$$
\begin{array}{c} E [ \sum (X _ {i} - \bar {X}) ^ {2} ] = E [ \sum (X _ {i} - \mu) ^ {2} ] - n \cdot E [ (\bar {X} - \mu) ^ {2} ] \\ = n \sigma^ {2} - n \cdot (\sigma^ {2} / n) = n \sigma^ {2} - \sigma^ {2} = (n - 1) \sigma^ {2} \end{array}
$$

• 因此： $E [ S ^ { 2 } ] = E [ \sum ( X _ { i } - { \bar { X } } ) ^ { 2 } / ( n - 1 ) ] = ( n - 1 ) \sigma ^ { 2 } / ( n - 1 ) = \sigma ^ { 2 }$ 自由度概念

• $\Sigma ( X _ { i } - X ) ^ { 2 }$ 中有 n 个平方项，但它们满足约束： $\sum ( X _ { i } - { \bar { X } } ) = 0$

• 因此只有n −1 个独立的信息，即自由度为n −1.

• 除以自由度（而非样本量）才能得到无偏估计.

估计量的评价标准：有效性与一致性

## 估计量的评价标准：有效性与一致性

有效性 (Eficiency): 设 $\widehat { \theta } _ { 1 }$ 和 $\hat { \theta } _ { 2 }$ 都是 $\theta$ 的无偏估计量，若

$$
V a r (\hat {\theta} _ {1}) <   V a r (\hat {\theta} _ {2}),
$$

则称 $\widehat { \theta } _ { 1 }$ 比 $\hat { \theta } _ { 2 }$ 更有效。

## 估计量的评价标准：有效性与一致性

有效性 (Eficiency): 设 $\widehat { \theta } _ { 1 }$ 和 $\hat { \theta } _ { 2 }$ 都是 $\theta$ 的无偏估计量，若

$$
V a r (\hat {\theta} _ {1}) <   V a r (\hat {\theta} _ {2}),
$$

则称 $\widehat { \theta } _ { 1 }$ 比 $\hat { \theta } _ { 2 }$ 更有效。

在所有无偏估计中，方差最小的称为最小方差无偏估计 (MVUE)。

一致性 (Consistency): 设 $\hat { \theta } _ { n }$ 是 $\theta$ 的估计量（下标n 表示样本量），若对任意 $\varepsilon > 0$ ，有

$$
\lim _ {n \to \infty} P (| \hat {\theta} _ {n} - \theta | <   \varepsilon) = 1
$$

即 $\hat { \theta } _ { n }$ 依概率收敛于 $\theta$ ，则称 $\hat { \theta } _ { n }$ 是 $\theta$ 的一致估计量 (也称相合估计量)。

## 估计量的评价标准：有效性与一致性

有效性 (Eficiency): 设 $\widehat { \theta } _ { 1 }$ 和 $\hat { \theta } _ { 2 }$ 都是 $\theta$ 的无偏估计量，若

$$
V a r (\hat {\theta} _ {1}) <   V a r (\hat {\theta} _ {2}),
$$

则称 $\widehat { \theta } _ { 1 }$ 比 $\hat { \theta } _ { 2 }$ 更有效。

在所有无偏估计中，方差最小的称为最小方差无偏估计 (MVUE)。

一致性 (Consistency): 设 $\hat { \theta } _ { n }$ 是 $\theta$ 的估计量（下标 n 表示样本量），若对任意 $\varepsilon > 0$ ，有

$$
\lim _ {n \to \infty} P (| \hat {\theta} _ {n} - \theta | <   \varepsilon) = 1
$$

即 $\hat { \theta } _ { n }$ 依概率收敛于 θ，则称 $\hat { \theta } _ { n }$ 是 $\theta$ 的一致估计量 (也称相合估计量)。

## 三个标准的关系

• 无偏性：单次抽样的平均意义上准确（小样本性质）。

• 有效性：在无偏的前提下，估计值越集中越好（小样本性质）。

• 一致性：样本量越大，估计越准确（大样本性质）。

• 实践中：大样本下一致性更重要，小样本下无偏+有效更重要。

## 区间估计基本概念

## 区间估计基本概念

为什么需要区间估计？

点估计只给出一个数值，无法反映估计的精度和可靠性。

区间估计给出一个区间，并说明这个区间包含真实参数的概率（置信水平）。

## 区间估计基本概念

为什么需要区间估计？

点估计只给出一个数值，无法反映估计的精度和可靠性。

区间估计给出一个区间，并说明这个区间包含真实参数的概率（置信水平）。

## 定义

设 $\theta$ 是总体的未知参数， $X _ { 1 } , . . . , X _ { n }$ 是样本。若存在两个统计量 $\hat { \theta } _ { l }$ 和 $\hat { \theta } _ { u } \ ( \hat { \theta } _ { l } < \hat { \theta } _ { u } )$ ，使得

$$
P (\hat {\theta} _ {l} <   \theta <   \hat {\theta} _ {u}) = 1 - \alpha
$$

则称随机区间 $( \hat { \theta } _ { l } , \hat { \theta } _ { u } )$ 为 $\theta$ 的置信水平为1−α 的置信区间。

## 区间估计基本概念

为什么需要区间估计？

点估计只给出一个数值，无法反映估计的精度和可靠性。

区间估计给出一个区间，并说明这个区间包含真实参数的概率（置信水平）。

## 定义

设 $\theta$ 是总体的未知参数， $X _ { 1 } , . . . , X _ { n }$ 是样本。若存在两个统计量 $\hat { \theta } _ { l }$ 和 $\hat { \theta } _ { u } \ ( \hat { \theta } _ { l } < \hat { \theta } _ { u } )$ ，使得

$$
P (\hat {\theta} _ {l} <   \theta <   \hat {\theta} _ {u}) = 1 - \alpha
$$

则称随机区间 $( \hat { \theta } _ { l } , \hat { \theta } _ { u } )$ 为 $\theta$ 的置信水平为 $1 - \alpha$ 的置信区间。

$1 - \alpha$ 称为置信水平或置信度 ，α 称为显著性水平。

## 区间估计基本概念

## 为什么需要区间估计？

点估计只给出一个数值，无法反映估计的精度和可靠性。

区间估计给出一个区间，并说明这个区间包含真实参数的概率（置信水平）。

定义

设 $\theta$ 是总体的未知参数， $X _ { 1 } , . . . , X _ { n }$ 是样本。若存在两个统计量 $\hat { \theta } _ { l }$ 和 $\hat { \theta } _ { u } \ ( \hat { \theta } _ { l } < \hat { \theta } _ { u } )$ ，使得

$$
P (\hat {\theta} _ {l} <   \theta <   \hat {\theta} _ {u}) = 1 - \alpha
$$

则称随机区间 $( \hat { \theta } _ { l } , \hat { \theta } _ { u } )$ 为 θ 的置信水平为 $1 - \alpha$ 的置信区间。

$1 - \alpha$ 称为置信水平或置信度 ，α 称为显著性水平。

## 常见误解

• 错误说法：”真实参数θ 落在这个区间里的概率是 $9 5 \% ^ { \prime \prime }$

• 正确理解：”如果重复抽样 100次，构造100 个置信区间，约有 95个会包含真实参数”

• 置信区间是随机的（随样本变化），真实参数是固定的

## 置信区间的直观理解

## 置信区间的直观理解

反复抽样实验类比

## 置信区间的直观理解

## 反复抽样实验类比

想象这样一个实验：

• 1. 从总体中抽取容量为 n 的样本，计算一个置信区间.

• 2. 再抽一个样本，再算一个置信区间.

• 3. 重复 100 次，得到 100 个不同的区间.

• 4. 其中大约 95 个区间会包含真实参数θ，5 个不包含.

置信水平 95% 描述的是方法的可靠性，不是某个特定区间的概率。

## 置信区间的直观理解

## 反复抽样实验类比

想象这样一个实验：

• 1. 从总体中抽取容量为 n 的样本，计算一个置信区间.

• 2. 再抽一个样本，再算一个置信区间.

• 3. 重复 100 次，得到 100 个不同的区间.

• 4. 其中大约 95 个区间会包含真实参数θ，5 个不包含.

置信水平 95% 描述的是方法的可靠性，不是某个特定区间的概率。

## 影响区间宽度的因素

• 置信水平1−α：置信水平越高，区间越宽（要更确信，就得更宽）

• 样本量 n：样本量越大，区间越窄（信息越多，估计越精确）

• 总体变异程度σ：总体越分散，区间越宽（变异大则难估计）

单正态总体均值的置信区间（σ 已知）

## 单正态总体均值的置信区间（σ 已知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 已知，求 $\mu$ 的置信区间

## 单正态总体均值的置信区间（σ 已知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 已知，求 $\mu$ 的置信区间

## 枢轴量构造

利用抽样分布定理： $\begin{array} { r } { Z = \frac { \bar { X } - \mu } { \sigma / \sqrt { n } } \sim N ( 0 , 1 ) } \end{array}$

$Z$ 就是枢轴量：包含待估参数 $\mu _ { \smash { \mathstrut } }$ ，但其分布完全已知（不依赖未知参数）。

## 单正态总体均值的置信区间（σ 已知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 已知，求 $\mu$ 的置信区间

枢轴量构造

利用抽样分布定理： $\begin{array} { r } { Z = \frac { \bar { X } - \mu } { \sigma / \sqrt { n } } \sim N ( 0 , 1 ) } \end{array}$

$Z$ 就是枢轴量：包含待估参数 $\mu _ { \smash { \mathstrut } }$ ，但其分布完全已知（不依赖未知参数）。

置信区间公式

由 $P ( | Z | < z _ { \alpha / 2 } ) = 1 - \alpha$ ，即 $\begin{array} { r } { P ( - z _ { \alpha / 2 } < \frac { \bar { X } - \mu } { \sigma / \sqrt { n } } < z _ { \alpha / 2 } ) = 1 - \alpha } \end{array}$

整理得： $P ( \bar { X } - z _ { \alpha / 2 } \cdot \sigma / \sqrt { n } < \mu < \bar { X } + z _ { \alpha / 2 } \cdot \sigma / \sqrt { n } ) = 1 - \alpha$

因此 $\mu$ 的 $1 - \alpha$ 置信区间为：

$$
(\bar {X} - z _ {\alpha / 2} \cdot \sigma / \sqrt {n}, \bar {X} + z _ {\alpha / 2} \cdot \sigma / \sqrt {n})
$$

或简写为： $\bar { X } \pm z _ { \alpha / 2 } \cdot \sigma / \sqrt { n }$

## 单正态总体均值的置信区间（σ 已知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 已知，求 $\mu$ 的置信区间

枢轴量构造

利用抽样分布定理： $\begin{array} { r } { Z = \frac { \bar { X } - \mu } { \sigma / \sqrt { n } } \sim N ( 0 , 1 ) } \end{array}$

$Z$ 就是枢轴量：包含待估参数 µ，但其分布完全已知（不依赖未知参数）。

置信区间公式

由 $P ( | Z | < z _ { \alpha / 2 } ) = 1 - \alpha$ ，即 $\begin{array} { r } { P ( - z _ { \alpha / 2 } < \frac { \bar { X } - \mu } { \sigma / \sqrt { n } } < z _ { \alpha / 2 } ) = 1 - \alpha } \end{array}$

整理得： $P ( \bar { X } - z _ { \alpha / 2 } \cdot \sigma / \sqrt { n } < \mu < \bar { X } + z _ { \alpha / 2 } \cdot \sigma / \sqrt { n } ) = 1 - \alpha$

因此 $\mu$ 的 $1 - \alpha$ 置信区间为：

$$
(\bar {X} - z _ {\alpha / 2} \cdot \sigma / \sqrt {n}, \bar {X} + z _ {\alpha / 2} \cdot \sigma / \sqrt {n})
$$

或简写为： $\bar { X } \pm z _ { \alpha / 2 } \cdot \sigma / \sqrt { n }$

边际误差

• 边际误差 $E = z _ { \alpha / 2 } \cdot \sigma / \sqrt { n }$ ，置信区间 = 点估计 ± 边际误差

单正态总体均值的置信区间（σ 未知）

## 单正态总体均值的置信区间（σ 未知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 未知，求 $\mu$ 的置信区间

## 单正态总体均值的置信区间（σ 未知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 未知，求 $\mu$ 的置信区间

## 枢轴量构造

$\sigma$ 未知时，用样本标准差S 代替 $\sigma$ ，得到：

$$
T = \frac {\bar {X} - \mu}{S / \sqrt {n}} \sim t (n - 1)
$$

这就是t 分布的应用场景！自由度为 $n - 1$ 。

## 单正态总体均值的置信区间（σ 未知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 未知，求 $\mu$ 的置信区间

## 枢轴量构造

$\sigma$ 未知时，用样本标准差S 代替 $\sigma .$ ，得到：

$$
T = \frac {\bar {X} - \mu}{S / \sqrt {n}} \sim t (n - 1)
$$

这就是t 分布的应用场景！自由度为 $n - 1$ 。

置信区间公式

由 $P ( | T | < t _ { \alpha / 2 } ( n - 1 ) ) = 1 - \alpha$ 得 $\mu$ 的 1−α 置信区间为：

$$
(\bar {X} - t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n}, \bar {X} + t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n})
$$

## 单正态总体均值的置信区间（σ 未知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 未知，求 $\mu$ 的置信区间

## 枢轴量构造

$\sigma$ 未知时，用样本标准差S 代替 σ，得到：

$$
T = \frac {\bar {X} - \mu}{S / \sqrt {n}} \sim t (n - 1)
$$

这就是t 分布的应用场景！自由度为 $n - 1$ 。

置信区间公式

由 $P ( | T | < t _ { \alpha / 2 } ( n - 1 ) ) = 1 - \alpha$ 得 $\mu$ 的 1−α 置信区间为：

$$
(\bar {X} - t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n}, \bar {X} + t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n})
$$

或简写为： $\bar { X } \pm t _ { \alpha / 2 } ( n - 1 ) \cdot S / \sqrt { n }$

## 单正态总体均值的置信区间（σ 未知）

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } ) , \ \sigma ^ { 2 }$ 未知，求 $\mu$ 的置信区间

枢轴量构造

$\sigma$ 未知时，用样本标准差S 代替 σ，得到：

$$
T = \frac {\bar {X} - \mu}{S / \sqrt {n}} \sim t (n - 1)
$$

这就是t 分布的应用场景！自由度为 $n - 1$ 。

置信区间公式

由 $P ( | T | < t _ { \alpha / 2 } ( n - 1 ) ) = 1 - \alpha$ 得 $\mu$ 的 1−α 置信区间为：

$$
(\bar {X} - t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n}, \bar {X} + t _ {\alpha / 2} (n - 1) \cdot S / \sqrt {n})
$$

或简写为： $\bar { X } \pm t _ { \alpha / 2 } ( n - 1 ) \cdot S / \sqrt { n }$

与 $\sigma$ 已知情况对比

• 用t 分位数代替 Z 分位数，用 S 代替 σ；t 分布尾部更厚，因此区间更宽（更保守）

## 单正态总体方差的置信区间

## 单正态总体方差的置信区间

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } )$ ，µ 未知，求 $\sigma ^ { 2 }$ 的置信区间

## 单正态总体方差的置信区间

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } )$ ，µ 未知，求 $\sigma ^ { 2 }$ 的置信区间

枢轴量构造

利用 $\chi ^ { 2 }$ 分布 ： $: \chi ^ { 2 } = ( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$

## 单正态总体方差的置信区间

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } )$ ，µ 未知，求 $\sigma ^ { 2 }$ 的置信区间

枢轴量构造

利用 $\chi ^ { 2 }$ 分布 ： $\ : \chi ^ { 2 } = ( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$

置信区间公式

$\chi ^ { 2 }$ 分布不对称，需要找两个分位数： $P ( \chi _ { 1 - \alpha / 2 } ^ { 2 } ( n - 1 ) < \chi ^ { 2 } < \chi _ { \alpha / 2 } ^ { 2 } ( n - 1 ) ) = 1 - \alpha$ 代入$\chi ^ { 2 } = ( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ ，整理不等式：

$$
P [ (n - 1) S ^ {2} / \chi_ {\alpha / 2} ^ {2} (n - 1) <   \sigma^ {2} <   (n - 1) S ^ {2} / \chi_ {1 - \alpha / 2} ^ {2} (n - 1) ] = 1 - \alpha
$$

因此 $\sigma ^ { 2 }$ 的 1−α 置信区间为：

$$
((n - 1) S ^ {2} / \chi_ {\alpha / 2} ^ {2} (n - 1), (n - 1) S ^ {2} / \chi_ {1 - \alpha / 2} ^ {2} (n - 1))
$$

## 单正态总体方差的置信区间

条件

总体 $X \sim N ( \mu , \sigma ^ { 2 } )$ ，µ 未知，求 $\sigma ^ { 2 }$ 的置信区间

枢轴量构造

利用 $\chi ^ { 2 }$ 分布 ： $\ : \chi ^ { 2 } = ( n - 1 ) S ^ { 2 } / \sigma ^ { 2 } \sim \chi ^ { 2 } ( n - 1 )$

置信区间公式

$\chi ^ { 2 }$ 分布不对称，需要找两个分位数： $P ( \chi _ { 1 - \alpha / 2 } ^ { 2 } ( n - 1 ) < \chi ^ { 2 } < \chi _ { \alpha / 2 } ^ { 2 } ( n - 1 ) ) = 1 - \alpha$ 代入$\chi ^ { 2 } = ( n - 1 ) S ^ { 2 } / \sigma ^ { 2 }$ ，整理不等式：

$$
P [ (n - 1) S ^ {2} / \chi_ {\alpha / 2} ^ {2} (n - 1) <   \sigma^ {2} <   (n - 1) S ^ {2} / \chi_ {1 - \alpha / 2} ^ {2} (n - 1) ] = 1 - \alpha
$$

因此 $\sigma ^ { 2 }$ 的 1−α 置信区间为：

$$
((n - 1) S ^ {2} / \chi_ {\alpha / 2} ^ {2} (n - 1), (n - 1) S ^ {2} / \chi_ {1 - \alpha / 2} ^ {2} (n - 1))
$$

注意

• $\chi ^ { 2 }$ 分布不对称，因此置信区间不是 $S ^ { 2 } \pm E$ 的形式；σ 的置信区间 = 方差置信区间两端开平方

## 双正态总体均值差的置信区间

## 双正态总体均值差的置信区间

## 问题设定

两个独立正态总体： $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$

分别抽取样本 $X _ { 1 } , . . . , X _ { n _ { 1 } }$ 和 $Y _ { 1 } , . . . , Y _ { n _ { 2 } }$

## 双正态总体均值差的置信区间

## 问题设定

两个独立正态总体： $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$

分别抽取样本 $X _ { 1 } , . . . , X _ { n _ { 1 } }$ 和 $Y _ { 1 } , . . . , Y _ { n _ { 2 } }$

求 $\mu _ { 1 } - \mu _ { 2 }$ 的置信区间

## 双正态总体均值差的置信区间

## 问题设定

两个独立正态总体： $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$

分别抽取样本 $X _ { 1 } , . . . , X _ { n _ { 1 } }$ 和 $Y _ { 1 } , . . . , Y _ { n _ { 2 } }$

求 $\mu _ { 1 } - \mu _ { 2 }$ 的置信区间

<table><tr><td>情况</td><td>枢轴量分布</td><td>置信区间形式</td></tr><tr><td> $\sigma_{1}^{2}\sigma_{2}^{2}$ 均已知</td><td> $N(0,1)$ </td><td> $(\bar{X}-\bar{Y})\pm z_{\alpha/2}\cdot\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}$ </td></tr><tr><td> $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma^{2}$ (未知)</td><td> $t(n_{1}+n_{2}-2)$ </td><td> $(\bar{X}-\bar{Y})\pm t_{\alpha/2}\cdot S_{w}\cdot\sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}}$ </td></tr><tr><td> $\sigma_{1}^{2},\sigma_{2}^{2}$ 均未知, $n$ 大</td><td>近似 $N(0,1)$ </td><td> $(\bar{X}-\bar{Y})\pm z_{\alpha/2}\cdot\sqrt{\frac{S_{1}^{2}}{n_{1}}+\frac{S_{2}^{2}}{n_{2}}}$ </td></tr></table>

## 双正态总体均值差的置信区间

## 问题设定

两个独立正态总体： $X \sim N ( \mu _ { 1 } , \sigma _ { 1 } ^ { 2 } ) , Y \sim N ( \mu _ { 2 } , \sigma _ { 2 } ^ { 2 } )$

分别抽取样本 $X _ { 1 } , . . . , X _ { n _ { 1 } }$ 和 $Y _ { 1 } , . . . , Y _ { n _ { 2 } }$

求 $\mu _ { 1 } - \mu _ { 2 }$ 的置信区间

<table><tr><td>情况</td><td>枢轴量分布</td><td>置信区间形式</td></tr><tr><td> $\sigma_{1}^{2}\sigma_{2}^{2}$ 均已知</td><td> $N(0,1)$ </td><td> $(\bar{X}-\bar{Y})\pm z_{\alpha/2}\cdot\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}$ </td></tr><tr><td> $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma^{2}$ (未知)</td><td> $t(n_{1}+n_{2}-2)$ </td><td> $(\bar{X}-\bar{Y})\pm t_{\alpha/2}\cdot S_{w}\cdot\sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}}$ </td></tr><tr><td> $\sigma_{1}^{2},\sigma_{2}^{2}$ 均未知, $n$ 大</td><td>近似 $N(0,1)$ </td><td> $(\bar{X}-\bar{Y})\pm z_{\alpha/2}\cdot\sqrt{\frac{S_{1}^{2}}{n_{1}}+\frac{S_{2}^{2}}{n_{2}}}$ </td></tr></table>

注

$S _ { w } ^ { 2 } = [ ( n _ { 1 } - 1 ) S _ { 1 } ^ { 2 } + ( n _ { 2 } - 1 ) S _ { 2 } ^ { 2 } ] / ( n _ { 1 } + n _ { 2 } - 2 )$ （合并方差）

## 单侧置信限

## 单侧置信限

什么是单侧置信？

## 单侧置信限

什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

## 单侧置信限

什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

定义

若 $P ( \theta > \hat { \theta } _ { l } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { l }$ 称为 θ 的置信水平为 1−α 的单侧置信下限。

## 单侧置信限

## 什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

## 定义

若 $P ( \theta > \hat { \theta } _ { l } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { l }$ 称为 θ 的置信水平为 1−α 的单侧置信下限。

若 $P ( \theta < \hat { \theta } _ { u } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { u }$ 称为 θ 的置信水平为 1−α 的单侧置信上限。

## 单侧置信限

什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

## 定义

若 $P ( \theta > \hat { \theta } _ { l } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { l }$ 称为 θ 的置信水平为 1−α 的单侧置信下限。

若 $P ( \theta < \hat { \theta } _ { u } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { u }$ 称为 θ 的置信水平为 1−α 的单侧置信上限。

与双侧的区别

• 双侧：α 平均分配到两侧，每侧 $\alpha / 2$ ，用 $z _ { \alpha / 2 }$ 或 $t _ { \alpha / 2 }$

• 单侧：全部 α 放在一侧，用 $z _ { \alpha }$ 或 $t _ { \alpha }$ （自由度不变）

## 单侧置信限

什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

定义

若 $P ( \theta > \hat { \theta } _ { l } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { l }$ 称为 θ 的置信水平为 $1 - \alpha$ 的单侧置信下限。

若 $P ( \theta < \hat { \theta } _ { u } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { u }$ 称为 θ 的置信水平为 1−α 的单侧置信上限。

与双侧的区别

• 双侧：α 平均分配到两侧，每侧 $\alpha / 2$ ，用 $z _ { \alpha / 2 }$ 或 $t _ { \alpha / 2 }$

• 单侧：全部 α 放在一侧，用 $z _ { \alpha }$ 或 $t _ { \alpha }$ （自由度不变）

例： $\sigma$ 已知时， $\mu$ 的单侧置信下限 ${ \hat { \mu } } _ { l } = { \bar { X } } - z _ { \alpha } \cdot \sigma / { \sqrt { n } } .$

$\mu$ 的单侧置信上限 $\hat { \mu } _ { u } = \bar { X } + z _ { \alpha } \cdot \sigma / \sqrt { n }$

## 单侧置信限

什么是单侧置信？

有时我们只关心参数的下界或上界，而非双侧区间：

• 只关心”至少有多大”→ 单侧置信下限.

• 只关心”最多有多大”→ 单侧置信上限.

定义

若 $P ( \theta > \hat { \theta } _ { l } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { l }$ 称为 θ 的置信水平为 $1 - \alpha$ 的单侧置信下限。

若 $P ( \theta < \hat { \theta } _ { u } ) = 1 - \alpha$ ，则 $\hat { \theta } _ { u }$ 称为 θ 的置信水平为 1−α 的单侧置信上限。

与双侧的区别

• 双侧：α 平均分配到两侧，每侧 $\alpha / 2$ ，用 $z _ { \alpha / 2 }$ 或 $t _ { \alpha / 2 }$

• 单侧：全部 α 放在一侧，用 $z _ { \alpha }$ 或 $t _ { \alpha }$ （自由度不变）

例： $\sigma$ 已知时， $\mu$ 的单侧置信下限 ${ \hat { \mu } } _ { l } = { \bar { X } } - z _ { \alpha } \cdot \sigma / { \sqrt { n } } .$

$\mu$ 的单侧置信上限 $\hat { \mu } _ { u } = \bar { X } + z _ { \alpha } \cdot \sigma / \sqrt { n }$

（注意：单侧用 $z _ { \alpha }$ ，比双侧的 $z _ { \alpha / 2 }$ 小，因此单侧限更”紧”）.

完整实例：某班学生成绩参数估计

## 完整实例：某班学生成绩参数估计

## 问题

某班随机抽取 16 名学生的数学成绩，得样本均值 $\bar { X } = 7 5$ 分，样本标准差S = 10分。假设成绩服从正态分布 $N ( \mu , \sigma ^ { 2 } )$ 。试求：

(1) $\mu$ 的 95% 置信区间；(2) $\sigma ^ { 2 }$ 的 95% 置信区间。

## 完整实例：某班学生成绩参数估计

## 问题

某班随机抽取 16 名学生的数学成绩，得样本均值 $\bar { X } = 7 5$ 分，样本标准差S = 10分。假设成绩服从正态分布 $N ( \mu , \sigma ^ { 2 } )$ 。试求：

解答

(1) $\mu$ 的 95% 置信区间；(2) $\sigma ^ { 2 }$ 的 95% 置信区间。

## 完整实例：某班学生成绩参数估计

## 问题

某班随机抽取 16 名学生的数学成绩，得样本均值 $\bar { X } = 7 5$ 分，样本标准差S = 10分。假设成绩服从正态分布 $N ( \mu , \sigma ^ { 2 } )$ 。试求：

(1) $\mu$ 的 95% 置信区间；(2) $\sigma ^ { 2 }$ 的 95% 置信区间。

## 解答

(1)：µ 的置信区间（σ 未知，用t 分布）已知： $n = 1 6 , \bar { X } = 7 5 , S = 1 0 , 1 - \alpha = 0 . 9 5 , \alpha = 0 . 0 5$ 自由度 $d f = n - 1 = 1 5$ 查t 分布表： $t _ { 0 . 0 2 5 } ( 1 5 ) = 2 . 1 3 1 5$

## 完整实例：某班学生成绩参数估计

## 问题

某班随机抽取 16 名学生的数学成绩，得样本均值 $\bar { X } = 7 5$ 分，样本标准差S = 10分。假设成绩服从正态分布 $N ( \mu , \sigma ^ { 2 } )$ 。试求：

(1) $\mu$ 的 95% 置信区间；(2) $\sigma ^ { 2 }$ 的 95% 置信区间。

## 解答

(1)： $\mu$ 的置信区间（σ 未知，用 t 分布）已知： $n = 1 6 , \bar { X } = 7 5 , S = 1 0 , 1 - \alpha = 0 . 9 5 , \alpha = 0 . 0 5$ 自由度 $d f = n - 1 = 1 5$

查t 分布表： $t _ { 0 . 0 2 5 } ( 1 5 ) = 2 . 1 3 1 5$

边际误差

$$
E = t _ {\alpha / 2} \cdot S / \sqrt {n} = 2. 1 3 1 5 \times 1 0 / \sqrt {1 6} = 2. 1 3 1 5 \times 2. 5 = 5. 3 3
$$