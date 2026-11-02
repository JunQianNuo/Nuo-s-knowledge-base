---
raw_title: deep_learning_handout (1)
subject: deep_learning_handout (1)
source: deep_learning_handout (1).pdf
status: mineru解析
parser: mineru
---

# Mathematical Foundation of Deep Learning

Handout

Yiqi Gu

University of Electronic Science and Technology of China

## Contents

Introduction 1   
1 Neural Networks 8   
1.1 Activation Functions 8   
1.1.1 Examples of activation functions 8   
1.1.2 Sigmoidal functions 15   
1.1.3 Squashing functions 17   
1.2 Feedforward Neural Networks 18   
1.2.1 Abstract neurons 18   
1.2.2 Forward pass through the network 20   
1.2.3 Differentiation of fully-connected neural networks 23   
1.2.4 Differentiation of general deep neural networks 29   
1.2.5 Weight initialization 31   
1.2.6 Continuum number of neurons and inputs 34   
1.3 Convolutional Neural Networks 35   
1.3.1 Cross-correlation 35   
1.3.2 Pooling 38   
1.3.3 Architecture of convolutional neural networks 39   
1.3.4 Forward and back propagation 39   
1.3.5 Continuum analogy 42   
1.3.6 Invariance of max/min-pooling 42   
1.4 Exercises 43   
2 Approximation Theory of Neural Networks 46   
2.1 Universal Approximation in One Dimension 46   
2.1.1 Stone-Weierstrass' theorem 46   
2.1.2 Wiener's Tauberian theorems 48   
2.1.3 Approximation with Heaviside activation 50   
2.1.4 Approximation with sigmoidal activation 51   
2.1.5 Approximation with ReLU activation 54   
2.1.6 Approximation with softplus activation 55   
2.2 Universal Approximation in Multi-dimension 57   
2.2.1 Approximating continuous functions 57   
2.2.2 Approximating $L^2$ -functions 60   
2.2.3 Approximating $L^1$ -functions 63   
2.2.4 Approximating measurable functions 64   
2.3 Error Bounds Estimation 69

2.3.1 Spectral Barron norm and approximation 69
2.3.2 Barron-type spaces 77
2.3.3 Higher-order derivatives 79
2.3.4 Approximation by deep and wide networks 80
2.4 Exact Learning 81
2.4.1 Fitting a finite dataset 81
2.4.2 Exact learning with ReLU 83
2.4.3 Kolmogorov-Arnold-Sprecher theorem 87
2.4.4 Exact learning with fixed activation and finite parameters 89
2.5 Exercises 91
3 Optimization in Machine Learning 94
3.1 Loss Functions 94
3.1.1 $L^{\infty}$ and $L^{2}$ -loss functions 94
3.1.2 Mean square error 95
3.1.3 Cross-entropy 95
3.1.4 Empirical computation in classification 97
3.1.5 Other loss functions 98
3.2 Algorithms of Optimization 99
3.2.1 Gradient descent algorithms 99
3.2.2 Stochastic gradient descent 103
3.3 Optimization theory in deep learning 105
3.3.1 Optimization of shallow networks 105
3.3.2 Optimization of deep networks 114
3.4 Exercise 114
4 Appendix 115
4.1 Concepts in Real Analysis 115
4.1.1 Dini's theorem 115
4.1.2 Riesz representation theorem 115
4.1.3 Distribution and Dirac delta function 116
4.2 Measure Theory 117
4.2.1 Measurable spaces and measurable functions 117
4.2.2 Abstract measures 117
4.2.3 Signed measures 118
4.2.4 Total variation of signed measures 118
4.2.5 Fourier transform of measures 119
4.3 Concepts in Probability 119
4.3.1 Inequalities 119

## Bibliography

## Introduction

Deep learning is the subset of machine learning methods based on artificial neural networks. The adjective “deep” means the use of multiple layers in the network. Simply, we can say,

Deep learning = Machine learning with deep neural networks.

## Derivation from Fourier series

Neural networks, the core of deep learning, are nothing but a family of functions. Let us first focus on the shallow neural networks (“shallow” means these types of neural networks only have one hidden layer) that can be viewed as an analogy of the finite Fourier series. Recall the real-valued finite Fourier series is defined as the following family of functions,

$$
\mathcal {F} _ {M} = \left\{f (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (m x) + b _ {m} \sin (m x): a _ {0}, a _ {m}, b _ {m} \in \mathbb {R} \text {   for   } 1 \leq m \leq M \right\},\tag{1}
$$

where M is a fixed integer<sup>1</sup>. Note that the functions in $\mathcal { F } _ { M }$ are 2π-periodic in $( - \infty , \infty )$ . The functions cos(mx) and sin(mx) for all m, as well as the constant function 1 multiplied by $a _ { 0 }$ , are playing the role of basis functions, and they are also named as Fourier modes. The coeficients $a _ { 0 } , a _ { 1 } , b _ { 1 } , \dotsc$ . are arbitrary real numbers and can also be named as free parameters as they vary freely over the whole real line. If $a _ { 0 } , a _ { 1 } , b _ { 1 } , \dotsc , a _ { M } , b _ { M }$ are fixed, then $f ( x )$ is also fixed; so, we say $f ( x )$ is completely determined by the free parameters. Denote $\theta = \{ a _ { 0 } , a _ { 1 } , b _ { 1 } , \dotsc , a _ { M } , b _ { M } \}$ as an ordered set of all free parameters, then $f ( x )$ can be rewritten as $f ( x ; \theta )$ , indicating its dependence on θ. Moreover, this dependence is unique. Namely, for two sets $\theta _ { 1 }$ and $\theta _ { 2 }$ , if $f ( x ; \theta _ { 1 } ) = f ( x ; \theta _ { 2 } )$ for all $x \in \mathbb { R }$ , then it is necessarily that $\theta _ { 1 } = \theta _ { 2 }$

In the structure of the Fourier series, the basis functions $\{ 1 , \cos ( m x ) , \sin ( m x ) \}$ are always fixed. Only the coeficients of basis functions are variables. Namely, all Fourier series are linear combinations of Fourier modes. In this sense, we can view f in ${ \mathcal { F } } _ { M }$ as a linear structure with respect to its free parameters θ. Linear structures appear very widely in numerical approximation. Other types of linear structures include polynomials, finite element functions, wavelet series, etc.

In comparison, neural networks are functions that are nonlinear with respect to their free parameters. A typical example of neural networks can be derived from ${ \mathcal { F } } _ { M }$ by unfixing the basis functions. For cos(mx) and sin(mx), we replace the wavenumber m by two free parameters, say $w _ { m }$ and $v _ { m }$ . Then we have the following family of functions,

$$
\mathcal {S} _ {M} = \left\{\phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (w _ {m} x) + b _ {m} \sin (v _ {m} x): a _ {0}, a _ {m}, b _ {m}, w _ {m}, v _ {m} \in \mathbb {R} \text {for} 1 \leq m \leq M \right\}.\tag{2}
$$

In (2), $w _ { m }$ and $v _ { m }$ are also ranging over R. So $\{ a _ { 0 } , a _ { m } , b _ { m } \} _ { m = 1 } ^ { M }$ and $\{ w _ { m } , v _ { m } \} _ { m = 1 } ^ { M }$ are both sets of free parameters. It is clear that $\mathcal { F } _ { M } \subset \mathcal { S } _ { M }$ . Similarly, we denote $\tilde { \theta } = \{ a _ { 0 } , a _ { m } , \stackrel {  } { b _ { m } } , w _ { m } , v _ { m } \} _ { m = 1 } ^ { M }$ , and $\phi ( x )$ can be rewritten as $\phi ( x ; \tilde { \theta } )$ . So far, we have successfully built a neural network, $\mathrm { i . e . , ~ } \phi ( x ; { \tilde { \theta } } )$ In later sections, we will recognize $\phi$ as a one-hidden layer neural network with sine and cosine activation.

Indeed, $\phi ( x ; \tilde { \theta } )$ is determined by ${ \tilde { \theta } } .$ . However, unlike the Fourier series, the determination is not unique. For example, when $M = 1 , \ \tilde { \theta } _ { 1 } = \{ a _ { 0 } = 1 , a _ { 1 } = 1 , b _ { 1 } = 1 , w _ { 1 } = 0 , v _ { 1 } = 1 \}$ and $\tilde { \theta } _ { 2 } = \{ a _ { 0 } = 2 , a _ { 1 } = 0 , b _ { 1 } = 1 , w _ { 1 } = 1 , v _ { 1 } = 1 \}$ both lead to $\phi ( x ; \tilde { \theta } ) = 2 + \sin ( x )$

Note that any function $\phi ( x ; \tilde { \theta } ) \in S _ { M }$ is nonlinear with the free parameters $\{ w _ { m } , v _ { m } \}$ . Therefore, $\boldsymbol { \mathcal { S } } _ { M }$ is not a linear space. In fact, for any $\phi _ { 1 } , \phi _ { 2 } \in \mathcal { S } _ { M } , \phi _ { 1 } + \phi _ { 2 }$ is not necessarily in $\boldsymbol { \mathcal { S } } _ { M }$ . In comparison, ${ \mathcal { F } } _ { M }$ is a linear space with dimension $2 M + 1$

## Learning real-valued functions

One of the typical machine learning tasks is learning real-valued functions, which is also known as regression<sup>2</sup>. Suppose there is a function $g : [ 0 , 2 \pi ] \to { \mathbb R }$ . But g is unknown to us except for its value on a finite subset of [0, 2π], say $\{ x _ { 1 } , \ldots , x _ { N } \}$ . Denote $y _ { n } = g ( x _ { n } )$ for $1 \leq n \leq N$ , then the set of pairs $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ are given to us, which is usually named as a dataset. The goal of $l e a r n i n g ^ { 3 }$ is to find a rule or formula that can evaluate $g ( x )$ for any $x \in [ 0 , 2 \pi ]$ based on the dataset.

We further assume that $g$ is $C ^ { \infty }$ smooth and 2π-periodic with respect to its derivatives of all orders. Then a good idea for learning is to use a finite Fourier series $f ( x ; \theta ) \in \mathcal { F } _ { M }$ to approximate $g ( x )$ . If such $f$ learns $g$ well, $f ( x ; \theta )$ is likely to be an good approximation to $g ( x )$ for any $x \in [ 0 , 2 \pi ]$ The reason for using Fourier series rather than other approximation functions is that Fourier series are always 2π-periodic, so they are consistent with the function to be learned. Here, the parametric family of Fourier series $\mathcal { F } _ { M }$ acting as an approximation set is also called a hypothesis space.

We choose an integer $M > 0$ and let

$$
f (x; \theta) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (m x) + b _ {m} \sin (m x)\tag{3}
$$

to be the learner. The principle of learning is to minimize the error between $f$ and g on the given dataset by tuning the free parameters of f. A common method is to minimize the following mean square error,

$$
\min _ {\theta} \frac {1}{N} \sum_ {n = 1} ^ {N} | f (x _ {n}; \theta) - y _ {n} | ^ {2}.\tag{4}
$$

Taking (3) into (4) leads to

$$
\min _ {\theta} \frac {1}{N} \sum_ {n = 1} ^ {N} \left| a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (m x _ {n}) + b _ {n} \sin (m x _ {n}) - y _ {n} \right| ^ {2}.\tag{5}
$$

Note that (5) is equivalent to a least squares linear system. Up to a constant $1 / N$ , we can rewrite

(5) in matrix form as follows,

$$
\left[ \begin{array}{c c c c c c} 1 & \cos (x _ {1}) & \sin (x _ {1}) & \ldots & \cos (M x _ {1}) & \sin (M x _ {1}) \\ 1 & \cos (x _ {2}) & \sin (x _ {2}) & \ldots & \cos (M x _ {2}) & \sin (M x _ {2}) \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 1 & \cos (x _ {N}) & \sin (x _ {N}) & \ldots & \cos (M x _ {N}) & \sin (M x _ {N}) \end{array} \right] \left[ \begin{array}{c} a _ {0} \\ a _ {1} \\ b _ {1} \\ \vdots \\ a _ {M} \\ b _ {M} \end{array} \right] \approx \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {N} \end{array} \right],\tag{6}
$$

where $a _ { 0 } , a _ { 1 } , b _ { 1 } , \dots , a _ { M } , b _ { M }$ are the unknowns. And (5) is basically minimizing the $\ell ^ { 2 }$ residual of the linear system (6). In usual cases, the number of data samples N is much larger than the number of Fourier modes 2M + 1, so (6) is an overdetermined system. This system can be solved by standard linear least squares solvers, e.g., by solving the normal equations (see Exercise 3).

If we find a least squares solution $\theta ^ { * } = \{ a _ { 0 } ^ { * } , a _ { 1 } ^ { * } , b _ { 1 } ^ { * } , \ldots , a _ { M } ^ { * } , b _ { M } ^ { * } \}$ of (6), then the Fourier series $f ( x ; \theta ^ { * } )$ given by (3) can be regarded as an approximation of $g .$ . Namely, for any $x \in [ 0 , 2 \pi ]$ , we can estimate g(x) by $g ( x ) \approx f ( x ; \theta ^ { * } )$ . This process of estimation is called prediction.

On the other hand, we can also take a neural network $\phi ( x ; \tilde { \theta } ) \in S _ { M }$ to approximate $g ( x )$ . A similar argument leads to the following minimization,

$$
\min _ {\tilde {\theta}} \frac {1}{N} \sum_ {n = 1} ^ {N} \left| \phi (x _ {n}; \tilde {\theta}) - y _ {n} \right| ^ {2},\tag{7}
$$

or

$$
\min _ {\tilde {\theta}} \frac {1}{N} \sum_ {n = 1} ^ {N} \left| a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (w _ {m} x _ {n}) + b _ {n} \sin (v _ {m} x _ {n}) - y _ {n} \right| ^ {2}.\tag{8}
$$

Suppose we find a feasible solution $\tilde { \theta } ^ { * }$ of $( 8 )$ , then $\phi ( x ; \tilde { \theta } ^ { * } )$ can also be used for the prediction of $g .$

As discussed above, ${ \mathcal { F } } _ { M }$ is merely a subfamily of ${ \mathcal { S } } _ { M } .$ , so the latter has a better capability of approximation. This is reflected by that the objective function<sup>4</sup> in (7) has a smaller minimum than (4). However, compared with (4), (7) has a major dificulty: it is a non-convex optimization! The objective function in (7) is non-convex with the variables $\{ w _ { m } , v _ { m } \}$ . The non-convexity is the main diference between deep learning and other machine learning types that use linear approximation structures.

It is known that solving linear equations is much easier than solving non-convex optimization. For a system of linear equations containing many unknowns, current linear solvers can find numerical solutions up to machine precision as long as the system is well-conditioned. However, this is usually impossible for non-convex optimization with many variables. Unfortunately, practical deep learning tasks not only contain a huge number of variables (i.e., the free parameters of neural networks) but also have a highly non-convex structure with these variables. In most cases, people can only adopt first-order optimizers such as the gradient descent method and its variants for optimization in deep learning, and the accuracy of the solution is always limited.

## Three types of errors

Fixing a function $g : \mathbb { R } ^ { d }  \mathbb { R }$ with $d \geq 1$ being the dimension, we can define the expected risk of a function $f$ with respect to $^ { g , }$ i.e.

$$
\mathcal {R} _ {\mathcal {D}} [ f ] = \mathbb {E} _ {x \sim \mathcal {D}} | f (x) - g (x) | ^ {2},\tag{9}
$$

where $\mathcal { D }$ is some probability distribution on $\mathbb { R } ^ { d } .$ . Note that the expected risk characterizes the expectation of the squared error between $f$ and $g .$ . In particular, if D has a continuous probability density function $\rho ( x )$ , then (9) can be formulated as

$$
\mathcal {R} _ {\mathcal {D}} [ f ] = \int_ {\mathbb {R} ^ {d}} | f (x) - g (x) | ^ {2} \rho (x) \mathrm{d} x.\tag{10}
$$

In machine learning problems, g is usually a function that is just partially known, and we are supposed to find a function $f \in { \mathcal { F } }$ that approximates $^ { g , }$ where $\mathcal { F }$ is some hypothesis space. However, choosing $\mathcal { F }$ is often based on specific circumstances. If it is lucky enough that $g$ is in ${ \mathcal { F } } ,$ we can find $f = g$ such that the expected risk is exactly zero. But in usual cases, ${ \mathit { g } } \notin { \mathcal { F } } ,$ which means there is a gap between $g$ and $\mathcal { F }$ . Such a gap can be characterized by the following approximation error,

$$
\inf _ {f \in \mathcal {F}} \mathcal {R} _ {\mathcal {D}} [ f ],\tag{11}
$$

which is the expected risk between the best approximator $f \in { \mathcal { F } }$ and $g .$

In practice, the information of $g$ is only revealed through a finite dataset ${ \cal S } = \{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ where $\{ x _ { n } \} _ { n = 1 } ^ { N }$ is a set of feature vectors with distribution D and $y _ { n } = g ( x _ { n } ) ^ { 5 }$ is the label of $x _ { n }$ for each $n .$ . Then we define the empirical risk of a function $f$ with respect to $S$ ,

$$
\mathcal {R} _ {S} [ f ] = \frac {1}{N} \sum_ {n = 1} ^ {N} | f (x _ {n}) - g (x _ {n}) | ^ {2}.\tag{12}
$$

Clearly, $\mathcal { R } _ { S } [ f ]$ is a discrete version of $\mathcal { R } _ { \mathcal { D } } [ f ]$ . And we can imagine that as the dataset becomes larger, $\mathcal { R } _ { S } [ f ]$ will be closer to $\mathcal { R } _ { \mathcal { D } } [ f ]$ ; namely,

$$
\mathcal {R} _ {S} [ f ] \to \mathcal {R} _ {\mathcal {D}} [ f ], \quad \mathrm{as} N \to \infty .\tag{13}
$$

If S is fixed, the gap between $\mathcal { R } _ { \mathcal { D } } [ f ]$ and $\mathcal { R } _ { S } [ f ]$ is named as the generalization gap of $f ,$ i.e.

$$
\left| \mathcal {R} _ {\mathcal {D}} [ f ] - \mathcal {R} _ {S} [ f ] \right|.\tag{14}
$$

As discussed above, we can not compute or minimize the expected risk $\mathcal { R } _ { \mathcal { D } } [ f ]$ directly, since g is at most partially known in $\mathbb { R } ^ { d }$ . So what we do is minimize the empirical risk instead, i,e.

$$
\inf _ {f \in \mathcal {F}} \mathcal {R} _ {S} [ f ].\tag{15}
$$

Note that $( 4 )$ and $( 7 )$ are two instances of (15). Then we denote any global minimizer (if there is one) of $\mathcal { R } _ { S } [ f ]$ ] as $f _ { S } ^ { * } ;$ namely,

$$
\mathcal {R} _ {S} [ f _ {S} ^ {*} ] = \inf _ {f \in \mathcal {F}} \mathcal {R} _ {S} [ f ].\tag{16}
$$

This optimization (15) is usually solved via specific numerical algorithms, $\mathrm { e . g . }$ , gradient descent and BFGS algorithm. However, the obtained numerical solution denoted as $\hat { f } _ { S }$ is usually not exactly the global minimizer $f _ { S } ^ { * }$ because of kinds of errors. Therefore, we define the optimization error as

$$
\left| \mathcal {R} _ {S} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ f _ {S} ^ {*} ] \right|,
$$

which is the diference between the numerical minima and global minima.

Now we use $f ^ { * }$ to denote the best approximator in (11), i.e.

$$
\mathcal {R} _ {\mathcal {D}} [ f ^ {*} ] = \inf _ {f \in \mathcal {F}} \mathcal {R} _ {\mathcal {D}} [ f ].
$$

Then the squared error between the numerical solution $\hat { f } _ { S }$ obtained by us and the target function $g$ is the expected risk of $\hat { f } _ { S }$ , which is given by

$$
\begin{array}{r l} & {\mathcal {R} _ {\mathcal {D}} [ \hat {f} _ {S} ] = \mathcal {R} _ {\mathcal {D}} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ \hat {f} _ {S} ] + \mathcal {R} _ {S} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ f _ {S} ^ {*} ] + \mathcal {R} _ {S} [ f _ {S} ^ {*} ] - \mathcal {R} _ {\mathcal {D}} [ f ^ {*} ] + \mathcal {R} _ {\mathcal {D}} [ f ^ {*} ]} \\ & {\quad \leq \mathcal {R} _ {\mathcal {D}} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ \hat {f} _ {S} ] + \mathcal {R} _ {S} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ f _ {S} ^ {*} ] + \mathcal {R} _ {S} {[ f ^ {*} ] - \mathcal {R} _ {\mathcal {D}} [ f ^ {*} ] + \inf _ {f \in \mathcal {F}} \mathcal {R} _ {\mathcal {D}} [ f ]}} \\ & {\quad \leq \underbrace {\inf _ {f \in \mathcal {F}} \mathcal {R} _ {\mathcal {D}} [ f ]} _ {\text {approximation error}} + \underbrace {\left| \mathcal {R} _ {S} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ f _ {S} ^ {*} ] \right|} _ {\text {optimization error}} + \underbrace {\left| \mathcal {R} _ {\mathcal {D}} [ \hat {f} _ {S} ] - \mathcal {R} _ {S} [ \hat {f} _ {S} ] \right| + | \mathcal {R} _ {\mathcal {D}} [ f ^ {*} ] - \mathcal {R} _ {S} [ f ^ {*} ] |} _ {\text {generalization gaps}}.} \end{array}
$$

Clearly, to estimate the final error $\mathcal { R } _ { \mathcal { D } } [ \hat { f } _ { S } ]$ , we need the estimates of the approximation error, optimization error and generalization gaps. These errors correspond to three types of work in machine learning theory: approximation theory, optimization analysis, and generalization analysis.

## Why do we use neural networks?

In low-dimensional situations, learning with linear structures is always optimal. For example, to learn a 2π-periodic function $g ( x )$ , using finite Fourier series will lead to a linear system (6), which can be eficiently solved by standard linear solvers. Comparatively, using neural networks will lead to non-convex optimization, e.g., the minimization (8), which is much more dificult to address.

However, when the dimension is moderately large, common linear structures often have trouble in approximation. Suppose $d > 0$ is the dimension, and $\Omega \subset \mathbb { R } ^ { d }$ is a domain. Let $g$ be a function in the Sobolev space $H ^ { \alpha } ( \Omega )$ ; namely,

$$
\| g \| _ {H ^ {\alpha} (\Omega)} ^ {2} := \sum_ {k = 0} ^ {\alpha} \int_ {\Omega} | D ^ {k} g (x) | ^ {2} \mathrm{d} x <   \infty ,
$$

where $D ^ { k } g$ is taken over all derivatives of order k. Let $\mathcal { F }$ be a hypothesis space and let

$$
f ^ {*} := \arg \min _ {f \in \mathcal {F}} \| f - g \| _ {L ^ {2} (\Omega)}
$$

be the best approximator in $L ^ { 2 }$ norm. It is studied that if $\mathcal { F }$ is one of the followings:

1. the set of polynomials with degree no more than $p ;$

2. the set of piecewise polynomials;

3. the set of finite Fourier series,

with number of free parameters N, then the error typically satisfies

$$
\| f ^ {*} - g \| _ {L ^ {2} (\Omega)} \leq C N ^ {- \alpha / d} \| g \| _ {H ^ {\alpha} (\Omega)},
$$

where $C > 0$ is some constant. The appearance of $1 / d$ in the exponent of N is a signature of an important phenomenon, the curse of dimensionality: The degree of freedom required to achieve certain accuracy grows exponentially with the dimension. For example, if we want $N ^ { - \alpha / d } \leq 0 . 1$ then we need $N \geq 1 0 ^ { d / \alpha }$ . And if g has low regularity, say $\alpha = 1$ , then $N \geq 1 0 ^ { d }$ , which is a huge number for large d. In practical computation, the limited capacity of machine memory does not allow the use of such a huge degree of freedom.

Neural networks can lessen or overcome the curse of dimensionality in the approximation of some special functions. For example, given $M > 0$ , let $\mathcal { F }$ be the following set of neural networks,

$$
\mathcal {F} = \left\{f: \mathbb {R} ^ {d} \to \mathbb {R}, f (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma \left(w _ {m} ^ {\top} x + b _ {m}\right): a _ {0}, a _ {m}, b _ {m} \in \mathbb {R}, w _ {m} \in \mathbb {R} ^ {d} \right\},
$$

where $\sigma$ is a sigmoidal function (see Section 1.1.2). If $g$ is Barron-type function [1] with norm $\| g \| _ { B } < \infty$ , then it holds that

$$
\| f ^ {*} - g \| _ {L ^ {2} (\Omega)} \leq C M ^ {- 1 / 2} \| g \| _ {\mathcal {B}}.
$$

Note that the exponent of M is fixed as $- 1 / 2$ , which is independent of the dimension. Therefore, if want $M ^ { - 1 / 2 } = 0 . 1$ , we only need $M = 1 0 0$ , and the number of parameters is $( d + 2 ) M + 1 =$ $1 0 0 d + 2 0 1$ , which only increases linearly with d.

Consequently, the advantages of neural networks are mainly reflected in solving high-dimensional problems. Actually, many deep learning applications are of very high dimensions. For example, in the field of computer vision, the inputs are usually digital images or videos. For an image with $8 0 0 \times 6 0 0$ pixels, the dimension is 480000.

## Exercises

## Exercise 1

(1) Given a continuous function $g ( x ) : [ 0 , 1 ]  \mathbb { R }$ . Let ${ \mathcal { F } } = \{ f ( x ) = a x + b : \ f ( 0 ) = g ( 0 ) , \ a , b \in \mathbb { R } \}$ Find the best approximator $f ^ { * } \in { \mathcal { F } }$ such that

$$
\mathcal {L} [ f ^ {*} ] = \min _ {f \in \mathcal {F}} \mathcal {L} [ f ],
$$

where $\begin{array} { r } { \mathcal { L } [ f ] : = \int _ { 0 } ^ { 1 } | f ( x ) - g ( x ) | ^ { 2 } \mathrm { d } x } \end{array}$ is the $L ^ { 2 } .$ -loss function;

(2) Given a continuous function $g ( x , y ) : [ 0 , 1 ] \times [ 0 , 1 ]  \mathbb { R }$ . Let $\mathcal { F } = \{ f ( x , y ) = a _ { 1 } x + a _ { 2 } y +$ $b : \ f ( 0 , 0 ) = g ( 0 , 0 ) , \ a _ { 1 } , a _ { 2 } , b \in \mathbb { R } \}$ . Find the best approximator $f ^ { * } \in { \mathcal { F } }$ such that

$$
\mathcal {L} [ f ^ {*} ] = \min _ {f \in \mathcal {F}} \mathcal {L} [ f ],
$$

where $\begin{array} { r } { \mathcal { L } [ f ] : = \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } | f ( x , y ) - g ( x , y ) | ^ { 2 } } \end{array}$ dxdy is the $L ^ { 2 } .$ -loss function.

## Exercise 2

Suppose $g ( x ) = \sin ( x )$ with domain $[ 0 , \frac { \pi } { 2 } ]$ is the target function. Let ${ \mathcal { F } } = \{ f ( x ) = a x + b : ~ a , b \in \mathbb { R } \}$ be the set of all polynomials with degree no more than one. Let $\begin{array} { r } { { \mathcal { L } } [ f ] = \frac { 2 } { \pi } \int _ { 0 } ^ { \frac { \pi } { 2 } } | f ( x ) - g ( x ) | ^ { 2 } \mathrm { d } x } \end{array}$ be the $L ^ { 2 } .$ -loss function.

(1) Compute the approximation error between $\mathcal { F }$ and g, i.e., min $_ { f \in \mathcal { F } } \mathcal { L } [ f ]$ . Write out the best approximator f<sup>∗</sup> = arg min $_ { f \in { \mathcal { F } } } { \mathcal { L } } [ f ]$ ;

(2) Assume the expression of $\dot { \boldsymbol g } ( \boldsymbol x )$ is unknown to us, and we only have a dataset $S : = \{ x _ { m } , g ( x _ { m } ) \} _ { m = 1 } ^ { 3 } =$ $\{ ( 0 , 0 ) , ( { \textstyle { \frac { \pi } { 4 } } } , { \textstyle { \frac { \sqrt { 2 } } { 2 } } } ) , ( { \textstyle { \frac { \pi } { 2 } } } , 1 ) \}$ in hand. Let $\textstyle { \mathcal { L } } _ { S } [ f ] = { \frac { 1 } { 3 } } \sum _ { m = 1 } ^ { 3 } | f ( x _ { m } ) - g ( x _ { m } ) | ^ { 2 }$ be the empirical $L ^ { 2 } .$ -loss function with respect to S. Find the global minimizer $f _ { S } ^ { * }$ of $\begin{array} { r } { \mathcal { L } _ { S } \mathrm { ~ , ~ i . e . , ~ } f _ { S } ^ { * } = \arg \operatorname* { m i n } _ { f \in \mathcal { F } } \mathcal { L } _ { S } [ f ] ; } \end{array}$ ;

(3) Assume one finally obtains a numerical solution $\hat { f } _ { S } = 0 . 6 x + 0 . 1$ . Compute the optimization

error between $\hat { f } _ { S }$ and $f _ { S } ^ { * }$ , i.e., $\left. \mathcal { L } _ { S } [ \hat { f } _ { S } ] - \mathcal { L } _ { S } [ f _ { S } ^ { * } ] \right.$ ;

(4) Compute the generalization gap of the final solution $\hat { f } _ { S } , \mathrm { i . e . , } \left| \mathcal { L } [ \hat { f } _ { S } ] - \mathcal { L } _ { S } [ \hat { f } _ { S } ] \right|$ . Similarly, compute the generalization gap of the best approximator $f ^ { * }$ ;

(5) Use the above results to verify that the $L ^ { 2 } \mathrm { - e r r o r }$ between $\hat { f } _ { S }$ and $^ { g , }$ i.e. $\mathcal { L } [ \hat { f } _ { S } ]$ , is bounded by the sum of approximation error, optimization error and the two generalization gaps.

## Exercise 3 (Normal equations)

Suppose $A \in \mathbb { R } ^ { m \times n }$ is matrix with full column rank and $b \in \mathbb { R } ^ { m }$ . Prove that the least squares problem mi $\mathrm { n } _ { x \in \mathbb { R } ^ { n } } \| A x - b \| _ { 2 }$ has a unique solution $x ^ { * }$ , and $x ^ { * }$ is a solution of the normal equations $A ^ { \top } A x = A ^ { \top } b$ . Here $\| \cdot \| _ { 2 }$ means the Euclidean norm of a vector.

## Exercise 4 (Approximation property of finite Fourier series)

Let $f \in C ^ { k } ( \mathbb { R } )$ be 2π-periodic, with $f ^ { ( j ) }$ also 2π-periodic for $j = 1 , \dots , k$ , where $k \geq 1$ is an integer. $\mathrm { A }$ ssume that $f ^ { ( k ) } \in L ^ { 2 } ( [ - \pi , \pi ] ) \cup$ . Let $f _ { N }$ be the N-degree finite Fourier series of $f , { \mathrm { i . e . } }$

$$
f _ {N} = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {N} \left(a _ {n} \cos (n x) + b _ {n} \sin (n x)\right),
$$

where $a _ { n } , b _ { n }$ are the Fourier coeficients of $f .$ . Prove that

$$
\| f - f _ {N} \| _ {L ^ {2} ([ - \pi , \pi ])} \leq N ^ {- k} \| f ^ {(k)} \| _ {L ^ {2} ([ - \pi , \pi ])}.
$$

## Chapter 1

# Neural Networks

From a mathematical perspective, neural networks, also named as artificial neural networks, are nothing but a class of parametrized functions. While in computer science and engineering, neural networks are often described vividly as an object or a model comprised of connected layers and nodes, propagating information from one end to another. Originally, the neural network is inspired by the principles of neuronal organization discovered by connectionism in biology and mimics the way the human brain operates. However, the latest neural network models are far beyond the original concept and serve various machine learning tasks.

## 1.1 Activation Functions

The activation functions play as a key ingredient of a neural network. Usually, an activation function is a universal function with a closed form that receives a vector (or matrix) as the input, applies the function element-wise, and produces the resulting vector (or matrix) of the same size as the output. For example, the special neural network $\phi ( x )$ in (2) in Introduction can be rewritten as

$$
\phi (x) = a _ {0} + a ^ {\top} \sigma_ {1} (w x) + b ^ {\top} \sigma_ {2} (v x),
$$

where $\begin{array} { r } { \boldsymbol { a } = [ a _ { 1 } \ a _ { 2 } \ \dots \ a _ { M } ] ^ { \top } , \boldsymbol { b } = [ b _ { 1 } \ b _ { 2 } \ \dots \ b _ { M } ] ^ { \top } , \boldsymbol { w } = [ w _ { 1 } \ w _ { 2 } \ \dots \ w _ { M } ] ^ { \top } , \boldsymbol { v } = [ v _ { 1 } \ v _ { 2 } \ \dots \ v _ { M } ] ^ { \top } } \end{array}$ are column vectors in $\mathbb { R } ^ { M } ;$ ; wx (same for vx) is regarded as the product of a $M \times 1$ matrix w and a $1 \times 1$ column vector x; $\sigma _ { 1 }$ and $\sigma _ { 2 }$ are the sine and cosine activation functions that apply sin(·) and cos(·) element-wise to its input vector, respectively.

## 1.1.1 Examples of activation functions

We list some common examples of activation functions. Note that all the following expressions of activation functions are applied to a vector or a matrix element-wise.

## Linear functions

This is the simplest activation function, which is given by

$$
\ell (x) = c x,\tag{1.1}
$$

where $c > 0$ is a constant. In the special case $c = 1$ , (1.1) is the identity function.

![](images/37797fa42d6a3e0efea49bcec0a56cc61b75bfa260d2e98e4b000c9ec71e34c1.jpg)  
(a) Heaviside function

![](images/0b7420ad61abb9a7e777aef10a9695d20e4e963b0c334314e3158774b3d28220.jpg)  
(b) bipolar step function  
Figure 1.1: Step functions.

## Step functions

The most simple step function is the Heaviside function (or unit step function)

$$
H (x) = \left\{ \begin{array}{l l} 0, & \text { if } x <   0, \\ 1, & \text { if } x \geq 0. \end{array} \right.\tag{1.2}
$$

Clearly, $H ( x )$ has a jump discontinuity and hence not diferentiable at $x = 0$ . However, in sense of distribution, its derivative is given by the Dirac’s function, i.e., $H ^ { \prime } ( x ) = \delta ( x )$ , where $\delta ( x )$ is the probability distribution measure for a unit mass centered at the origin. Roughly, we can write

$$
\delta (x) = \left\{ \begin{array}{l l} 0, & \text {if} x \neq 0, \\ + \infty , & \text {if} x = 0, \end{array} \right.
$$

which is also constrained to satisfy the identity

$$
\int_ {- \infty} ^ {\infty} \delta (x) \mathrm{d} x = 1.
$$

More details can be referred to in Section 4.1.3.

Moreover, a similar step function called bipolar step function is defined by

$$
S (x) = \left\{ \begin{array}{l l} - 1, & \text { if } x <   0, \\ 1, & \text { if } x \geq 0. \end{array} \right.
$$

And it holds that $S ( x ) = 2 H ( x ) - 1$

These types of step functions are shown in Figure 1.1.

## Hockey-stick functions

This class of functions has graphs that resemble a hockey stick or an increasing L-shaped curve. The most common one is the rectified linear unit (ReLU), which is given by

$$
\operatorname{ReLU} (x) = x H (x) = \max \{x, 0 \} = \left\{ \begin{array}{l l} 0, & \text { if } x <   0, \\ x, & \text { if } x \geq 0. \end{array} \right.
$$

ReL $\boldsymbol J ( \boldsymbol x )$ is only $C ^ { 0 }$ smooth at $x = 0$ , but it has a weak derivative everywhere. In fact, ReL $\begin{array} { r l } { \boldsymbol { { \mathrm { { U } } } ^ { \prime } } ( \boldsymbol { x } ) = } \end{array}$ $H ( x )$ in the weak sense.

The parametric rectified linear unit (PReLU) is a slight modification of ReLU, which is linearly increasing for $x < 0 \AA$

$$
\operatorname{PReLU} (x; \alpha) = \left\{ \begin{array}{l l} \alpha x, & \text {if} x <   0, \\ x, & \text {if} x \geq 0, \end{array} \right.
$$

where $\alpha > 0$ is a constant.

The exponential linear unit (ELU) is also a slight modification of ReLU, which is exponentially increasing for $x < 0 \colon$

$$
\operatorname{ELU} (x; \alpha) = \left\{ \begin{array}{l l} \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ x, & \text { if } x \geq 0. \end{array} \right.
$$

Note that the function is diferentiable at $x = 0$ only if $\alpha = 1$ ; in this case $\mathrm { E L U } ^ { \prime } ( 0 ; 1 ) = 1$

The scaled exponential linear unit (SELU) is a multiple of ELU; namely,

$$
\operatorname{SELU} (x; \alpha , \lambda) = \left\{ \begin{array}{l l} \lambda \alpha (e ^ {x} - 1), & \text { if } x <   0, \\ \lambda x, & \text { if } x \geq 0, \end{array} \right.
$$

where $\lambda > 0$ is a constant.

The sigmoid linear unit (SLU) is defined by

$$
\phi (x) = \frac {x}{1 + e ^ {- x}}.
$$

Unlike the other activation functions of hockey-stick type, this activation function is not monotonic, having a minimum. The critical point is located at $x \approx - 1 . 2 7 .$

The softplus function is an increasing positive function that has range $( 0 , \infty )$ , which is given by

$$
\operatorname{sp} (x) = \ln (1 + e ^ {x}).
$$

It holds that $\operatorname { s p } ( x ) - \operatorname { s p } ( - x ) = x$

These types of hockey-stick functions are shown in Figure 1.2.

## Sigmoid functions

The most common sigmoid function is the logistic function, which is defined by

$$
\lg s (x) = \frac {1}{1 + e ^ {- x}}.
$$

It holds that

$$
\lg \mathrm{s} ^ {- 1} (x) = \ln (\frac {x}{1 - x}),
$$

![](images/8115abd5ee22147ab82dad59cda45554e5ddbaa113b82211c0759800cc435e60.jpg)  
(a) ReLU

![](images/356e4e3f6ad627f760c65f2cee09d9748d0e37042d0b6bf83413e8e7c8a20785.jpg)  
(b) PReLU with α = 0.5

![](images/956ad9f02db2b0e8213325bf80ac5469ab7b8f7acdf5a5018a655f9b60be8bfa.jpg)  
(c) ELU with α = 0.5

![](images/dccec7bdc06350279f6a6d8e68c0828b64400865e69737c563322b732f3213ef.jpg)  
(d) SELU with α = 0.5 and λ = 1.5

![](images/993e2a271b9bd9c62353f4a528ef5b8da0e8383d408a4e199a060c16fbeaf21e.jpg)  
(e) SLU

![](images/2c3a9028988ebd6010327410cba5efb5b4f6b6c6bc0ea116c4303a846e9a198f.jpg)  
(f) softplus  
Figure 1.2: Hockey-stick functions.

and

$$
\operatorname{sp} ^ {\prime} (x) = \operatorname{lgs} (x).
$$

More generally, we can define the logistic function with parameter $c > 0$ by

$$
\lg s _ {c} (x) = \frac {1}{1 + e ^ {- c x}}.
$$

Note that large values of c correspond to a fast change of $\mathrm { l g s } _ { c } ( x )$ from 0 to 1 near $x = 0$ . And $\mathrm { l g s } _ { c } ( x )$ approximates the Heaviside function as $c \to + \infty$ for all nonzero x. Specifically,

$$
\lim _ {c \to \infty} \lg s _ {c} (x) = \left\{ \begin{array}{l l} 0, & \text {if} x <   0, \\ 1 / 2, & \text {if} x = 0, \\ 1, & \text {if} x > 0. \end{array} \right.
$$

Note that $\mathrm { l g s } _ { c } ( x )$ satisfies the following diferential equation,

$$
\mathrm{lg} \mathrm{s} _ {c} ^ {\prime} (x) = c \mathrm{lg} \mathrm{s} _ {c} (x) \left(1 - \mathrm{lg} \mathrm{s} _ {c} (x)\right).
$$

The hyperbolic tangent function is another common type of sigmoid functions. It is defined by

$$
\tanh (x) = \frac {e ^ {x} - e ^ {- x}}{e ^ {x} + e ^ {- x}},
$$

which has range $( - 1 , 1 )$ . And it holds that

$$
\tanh (x) = 2 \mathrm{lgs} _ {2} (x) - 1.
$$

The arctangent function scaled by $\textstyle { \frac { 2 } { \pi } }$ is also a sigmoid function, which has range $( - 1 , 1 )$

$$
h (x) = \frac {2}{\pi} \arctan (x).
$$

The softsign function has range (−1, 1) and is defined by

$$
\operatorname{so} (x) = \frac {x}{1 + | x |}.
$$

Softsign is diferentiable everywhere, including $x = 0$ . In spite of its similarities with the hyperbolic tangent function, softsign has tails that are $O ( x ^ { - 1 } )$ rather than exponential, and hence it approaches asymptotes at a slower rate.

One can also construct piecewise linear sigmoid functions such as

$$
f _ {\alpha} (x) = \left\{ \begin{array}{l l} - 1, & \text { if } x \leq - \alpha , \\ x / \alpha , & \text { if } - \alpha <   x <   \alpha , \\ 1, & \text { if } x \geq \alpha . \end{array} \right.
$$

And as $\alpha  0 , f _ { \alpha } ( x )$ converges to $S ( x )$ pointwise for all nonzero x.

These types of sigmoid functions are shown in Figure 1.3.

![](images/3db375c1187f0f3bdc3358510e0236fbbc3507010ff49f8ec1320ca0c90e31c3.jpg)  
(a) logistic function

![](images/c89de4d443a547f506b0e244fd3b87118e7d1911e1b6566938f5ff82ac818aae.jpg)  
(b) logistic function with $c = 2$

![](images/bf039921c133fa9c8917af466362453e37a5259eaf3ac2c014c2676990976e03.jpg)  
(c) hyperbolic tangent function

![](images/6c23eb4b745e10c88b5a2f471311a384604eed0f8aaea81217fcfaafcfb5789a.jpg)  
(d) arctangent function

![](images/79213accc9a692740060cf948b13d6ba9863b7dda068f0ea16892dfbe46af3bb.jpg)  
(e) softsign function  
Figure 1.3: Sigmoid functions.

![](images/640cb92324ad740b9f5f57a8403566019c7158efd758ccbe9244fcd892edf608.jpg)  
(f) piecewise linear sigmoid function with $\alpha = 1$

![](images/8bf6dda950a97faaab9c363700442ec582061dd166a55cc464a868ea114bf1f2.jpg)  
(a) Gaussian function

![](images/a9841cc0ec273666aff867df8af2c11e51c01a2c43c6c7757c1b3552dea82192.jpg)  
(b) double exponential function  
Figure 1.4: Bumped-type functions.

## Bumped-type functions

These types of activation functions have a maximum for a certain value in $( - \infty , \infty )$ ; it can occur in a smooth bumped way or with a bump of a thorn type.

The Gaussian function is given by

$$
G (x) = e ^ {- x ^ {2}},
$$

which achieves its maximum 1 at $x = 0$

The double exponential function is given by

$$
D (x) = e ^ {- \lambda | x |},
$$

with constant $\lambda > 0$

These types of bumped-type functions are shown in Figure 1.4.

## Classification functions

Recall that

$$
e _ {i} = (0, \dots , 0, 1, 0, \dots , 0) \in \mathbb {R} ^ {n}
$$

with 1 in the ith entry is the ith standard unit vector in $\mathbb { R } ^ { n }$ . And $\{ e _ { i } \} _ { i = 1 } ^ { n }$ are also called one-hot vectors in natural language processing. These vectors are useful in classification problems. The softmax activation function can transform any vectors towards standard unit vectors. Specifically, the softmax function depending on a parameter $c > 0$ is defined by

$$
\mathrm{softmax} _ {c} (x) = \frac {e ^ {c x}}{\| e ^ {c x} \|},
$$

where $e ^ { c x } = ( e ^ { c x _ { 1 } } , e ^ { c x _ { 2 } } , \ldots , e ^ { c x _ { n } } )$ and $\| \cdot \|$ is a certain type of vector norm. Note that softmax functions magnify the largest component of x but suppress the rest. Usually, ∥ · ∥ is taken as the $\ell ^ { 1 }$ norm, i.e., the sum of all components of the vector. In this case, the output of softmax is a probability vector $y = ( y _ { 1 } , y _ { 2 } , \dotsc , y _ { n } )$ satisfying $y _ { i } \in ( 0 , 1 )$ and $\textstyle \sum _ { i = 1 } ^ { n } y _ { i } = 1$

The usual softmax function is defined with $c = 1$ . However, if $c \to \infty$ 2

$$
\lim _ {c \to \infty} \mathrm{softmax} _ {c} (x) = e _ {k},\tag{1.3}
$$

given that $x _ { k } > x _ { j }$ for all $j \neq k$ . This can be easily verified for the $\ell ^ { p \ }$ norm. For any $1 \leq j \leq n ,$ the jth component of softmax<sub>c</sub>(x) is

$$
\frac {e ^ {c x _ {j}}}{\left(e ^ {c p x _ {1}} + e ^ {c p x _ {2}} + \cdots + e ^ {c p x _ {n}}\right) ^ {\frac {1}{p}}} = \frac {1}{\left(e ^ {c p (x _ {1} - x _ {j})} + e ^ {c p (x _ {2} - x _ {j})} + \cdots + e ^ {c p (x _ {n} - x _ {j})}\right) ^ {\frac {1}{p}}}.
$$

Then (1.3) is proved using the fact

$$
\lim _ {c \to \infty} e ^ {c p (x _ {1} - x _ {j})} + e ^ {c p (x _ {2} - x _ {j})} + \dots + e ^ {c p (x _ {n} - x _ {j})} = \left\{ \begin{array}{l l} 1, & j = k, \\ \infty , & j \neq k. \end{array} \right.
$$

## 1.1.2 Sigmoidal functions

In general, a measurable function $\sigma : \mathbb { R }  [ 0 , 1 ]$ is called sigmoidal if

$$
\lim _ {x \to - \infty} \sigma (x) = 0, \quad \lim _ {x \to + \infty} \sigma (x) = 1.
$$

Namely, a sigmoidal function is a function bounded by 0 and 1 having two horizontal asymptotes $y = 0$ and $y = 1$

Given a compact set $K \subset \mathbb { R } ^ { d }$ , we use $B ( K )$ to denote the space of finite signed Borel measures supported on $K$ . Namely,

$B ( K ) = \Big \{ \mu$ is a signed Borel measure : for any Borel set S, $| \mu ( S ) | < \infty$

$$
\text { and } \mu (S) = 0 \forall S \subset \mathbb {R} ^ {d} \backslash K \Big \}.\tag{1.4}
$$

We have the following result.

Lemma 1.1 Let $K \subset \mathbb { R } ^ { d }$ be a compact set and $\mu \in { \mathfrak { B } } ( K )$ be a measure. If

$$
\mu (P _ {w, \theta}) = 0, \quad \mu (H _ {w, \theta}) = 0, \quad \forall w \in \mathbb {R} ^ {d}, \theta \in \mathbb {R},
$$

then $\mu = 0 ,$ where $P _ { w , \theta } = \{ x \in \mathbb { R } ^ { d } : w ^ { \top } x + \theta = 0 \}$ denotes a hyperplane, $H _ { w , \theta } \mathrm { ~ = ~ } \{ x \in \mathbb { R } ^ { d }$ $w ^ { \top } x + \theta > 0 \}$ denotes an open half-space.

Proof: Given $w \in \mathbb { R } ^ { d }$ , define the compact set (see Exercise 8) $K _ { w } : = \{ y = w ^ { \top } x : \ x \in K \} \subset \mathbb { R }$ and the linear functional $\ell _ { w } : L ^ { \infty } ( K _ { w } ) \to \mathbb { R }$ by

$$
\ell_ {w} (f) = \int_ {K} f (w ^ {\top} x) \mathrm{d} \mu (x).
$$

Then $\ell _ { w }$ is a bounded (therefore continuous) functional since

$$
| \ell_ {w} (f) | = \left| \int_ {K} f (w ^ {\top} x) \mathrm{d} \mu (x) \right| \leq \| f \| _ {\infty} \int_ {K} \mathrm{d} | \mu | (x) = | \mu | (K) \cdot \| f \| _ {\infty},
$$

noting that $| \mu | ( K ) < \infty$

For $f = 1 _ { [ \theta , \infty ) \cap K _ { w } } , \operatorname { i . e . , } f$ is the characteristic function of the interval $[ \theta , \infty ) \cap K _ { w }$ . Then

$$
\ell_ {w} (f) = \int_ {K} f (w ^ {\top} x) \mathrm{d} \mu (x) = \int_ {w ^ {\top} x \geq \theta} \mathrm{d} \mu (x) = \mu (P _ {w, - \theta}) + \mu (H _ {w, - \theta}) = 0.
$$

Similarly, for $f = 1 _ { ( \theta , \infty ) \cap K _ { w } }$ 2

$$
\ell_ {w} (f) = \int_ {K} f (w ^ {\top} x) \mathrm{d} \mu (x) = \int_ {w ^ {\top} x > \theta} \mathrm{d} \mu (x) = \mu (H _ {w, - \theta}) = 0.
$$

By the facts $1 _ { [ a , b ] \cap K _ { w } } = 1 _ { [ a , \infty ) \cap K _ { w } } - 1 _ { ( b , \infty ) \cap K _ { w } }$ and $1 _ { ( a , b ) \cap K _ { w } } = 1 _ { ( a , \infty ) \cap K _ { w } } - 1 _ { [ b , \infty ) \cap K _ { w } }$ , it holds that $\ell _ { w } ( 1 _ { [ a , b ] \cap K _ { w } } ) \dot { = } \ell _ { w } ( 1 _ { ( a , b ) \cap K _ { w } } ) = 0$ for any intervals $[ a , b ]$ and $( a , b )$ . Therefore, for any step function $\begin{array} { r } { f = \sum _ { n = 1 } ^ { N } \alpha _ { n } 1 _ { I _ { n } } . } \end{array}$

$$
\ell_ {w} (f) = \sum_ {n = 1} ^ {N} \alpha_ {n} \ell_ {w} (1 _ {I _ {n}}) = 0,
$$

where $\alpha _ { n } \in \mathbb { R }$ and $I _ { n }$ is an interval in $K _ { w }$ for each n.

Note that step functions on $K _ { w }$ are $L ^ { \infty }$ -dense in $C ( K _ { w } )$ , the space of all continuous functions on $K _ { w } ,$ which is a subspace of $L ^ { \infty } ( K _ { w } )$ . Then for any $f \in C ( K _ { w } )$ , there is a sequence of step functions $( s _ { n } ) _ { n }$ such that $s _ { n } \to f$ in $L ^ { \infty } ( K _ { w } )$ norm. So $\begin{array} { r } { \ell _ { w } ( f ) = \ell _ { w } ( \operatorname* { l i m } _ { n \to \infty } s _ { n } ) = \operatorname* { l i m } _ { n \to \infty } \ell _ { w } ( s _ { n } ) = 0 } \end{array}$ by the continuity of $\ell _ { w }$ .

Now $\mu = 0$ follows that the Fourier transform of the measure $\mu$ is zero. More precisely,

$$
\begin{array}{l} \widehat {\mu} (w) = \int_ {\mathbb {R} ^ {d}} e ^ {- \mathrm{i} w ^ {\top} x} \mathrm{d} \mu (x) = \int_ {K} e ^ {- \mathrm{i} w ^ {\top} x} \mathrm{d} \mu (x) = \int_ {K} \cos (w ^ {\top} x) \mathrm{d} \mu (x) - \mathrm{i} \int_ {K} \sin (w ^ {\top} x) \mathrm{d} \mu (x) \\ = \ell_ {w} (\cos (\cdot)) - \mathrm{i} \ell_ {w} (\sin (\cdot)) = 0, \quad \forall w \in \mathbb {R}. \end{array}
$$

Lemma 1.1 implies that if a finite signed Borel measure with compact support vanishes on all hyperplanes and open half-spaces in $\mathbb { R } ^ { d }$ , then it is the zero measure.

We say a function σ is discriminatory for measures in $B ( K )$ if

$$
\int_ {K} \sigma (w ^ {\top} x + \theta) \mathrm{d} \mu (x) = 0, \forall w \in \mathbb {R} ^ {d}, \forall \theta \in \mathbb {R} \quad \text { for   some } \mu \in \mathcal {B} (K) \quad \Longrightarrow \quad \mu = 0.
$$

It can be proved that continuous sigmoidal fucntions are always discriminatory.

Theorem 1.1 Let σ be a continuous sigmoidal function. Then σ is discriminatory for measures in $B ( K )$

Proof: Let $\mu \in { \mathfrak { B } } ( K )$ be a measure. Suppose

$$
\int_ {K} \sigma (w ^ {\top} x + \theta) \mathrm{d} \mu (x) = 0, \quad \forall w \in \mathbb {R} ^ {d}, \forall \theta \in \mathbb {R}.\tag{1.5}
$$

We need to prove $\mu = 0$

Since σ is sigmoidal, there are two real numbers $\phi _ { 1 }$ and $\phi _ { 2 }$ such that $\sigma ( \phi _ { 1 } ) \neq \sigma ( \phi _ { 2 } )$ . First, for any $w \in \mathbb { R } ^ { d }$ and $\theta \in \mathbb { R }$ , we define

$$
\sigma_ {n} (x) = \sigma (n (w ^ {\top} x + \theta) + \phi_ {1}), \quad \text { for } n = 1, 2, \ldots .
$$

Then

$$
\lim _ {n \to \infty} \sigma_ {n} (x) = \gamma (x) := \left\{ \begin{array}{l l} 1, & \text {if w^{\top} x + \theta > 0}, \\ 0, & \text {if w^{\top} x + \theta <   0}, \\ \sigma (\phi_ {1}), & \text {if w^{\top} x + \theta = 0}, \end{array} \right.
$$

pointwise on R. Since $\sigma _ { n } ( x )$ is bounded and $\mu$ is a finite measure, by the bounded convergence theorem we have

$$
\begin{array}{l} \lim _ {n \to \infty} \int_ {K} \sigma_ {n} (x) \mathrm{d} \mu (x) = \int_ {K} \lim _ {n \to \infty} \sigma_ {n} (x) \mathrm{d} \mu (x) = \int_ {K} \gamma (x) \mathrm{d} \mu (x) \\ \qquad = \int_ {w ^ {\top} x + \theta > 0} \gamma (x) \mathrm{d} \mu (x) + \int_ {w ^ {\top} x + \theta <   0} \gamma (x) \mathrm{d} \mu (x) + \int_ {w ^ {\top} x + \theta = 0} \gamma (x) \mathrm{d} \mu (x) \\ \qquad = \mu (H _ {w, \theta}) + \sigma (\phi_ {1}) \mu (P _ {w, \theta}). \end{array}\tag{1.6}
$$

On the other hand, (1.5) implies that $\begin{array} { r } { \int _ { K } \sigma _ { n } ( x ) \mathrm { d } \mu ( x ) = 0 } \end{array}$ for all $n ,$ so the limit term on the left in (1.6) is zero. Therefore,

$$
\mu (H _ {w, \theta}) + \sigma (\phi_ {1}) \mu (P _ {w, \theta}) = 0, \quad \forall w \in \mathbb {R} ^ {d}, \forall \theta \in \mathbb {R}.\tag{1.7}
$$

Similarly, the equation (1.7) with $\phi _ { 1 }$ replaced by $\phi _ { 2 }$ also holds. Then these two equations lead to $\mu ( H _ { w , \theta } ) = 0$ and $\mu ( P _ { w , \theta } ) = 0$ for all w and θ. By Lemma 1.1, $\mu = 0$ □

Remark 1.1 The conclusion of Theorem 1.1 still holds true if we replace “continuous” by “bounded measurable” in the hypothesis.

## 1.1.3 Squashing functions

We can further define squashing functions. A function $\varphi : \mathbb { R }  [ 0 , 1 ]$ is called squashing if it is sigmoidal and

$$
\varphi (x _ {1}) \leq \varphi (x _ {2}), \quad \text { if } x _ {1} <   x _ {2}.
$$

Namely, an increasing sigmoidal function is a squashing function. The Heaviside function and logistic function with parameter c introduced in Section 1.1.1 are squashing functions. And the hyperbolic tangent function, arctangent function and softsign function can also be rescaled to squashing functions.

The next Helly’s selection theorem states that we can always select a sequence of pointwise convergent functions from a family of uniformly bounded increasing functions.

Lemma 1.2 Let $\boldsymbol { \mathcal { S } }$ be an infinite family of increasing functions mapping R into R, and suppose that there is some $a > 0$ such that $\textstyle \operatorname* { s u p } _ { x \in \mathbb { R } } | f ( x ) | < a$ for all $f \in S$ . Then there is a sequence $( f _ { n } ) _ { n } \subset S$ such that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ exists for any $x \in \mathbb { R }$

Actually, it is trivial that the limit function is also increasing.

By Lemma 1.2, we directly have the following result for squashing functions.

Corollary 1.1 Any infinite sequence of squashing functions $( \varphi _ { n } ) _ { n }$ contains a subsequence $\left( \varphi _ { n _ { k } } \right)$ that converges pointwise to an increasing function $f .$

However, the limit function $f$ is not necessarily a squashing function. More precisely, despite that $\scriptstyle \operatorname* { l i m } _ { x \to \pm \infty } f ( x )$ exists, it may not be 0 or 1.

![](images/4242ccc7e646a31d4181f18679461d1508032fa9b2a522a133593bd67589d7a4.jpg)  
Figure 1.5: Abstract neuron $y = \sigma ( w ^ { \top } x + b )$

## 1.2 Feedforward Neural Networks

## 1.2.1 Abstract neurons

The abstract neuron is the building block of any neural network. It is consists of an input vector, a weight vector (sometimes with a scalar bias) and an activation function. Specifically, an abstract neuron is defined as the function

$$
y = \sigma (w ^ {\top} x + b) = \sigma (w _ {1} x _ {1} + \dots + w _ {n} x _ {n} + b),
$$

where $x = ( x _ { 1 } x _ { 2 } \ldots x _ { n } ) ^ { \top }$ is the input, $w = ( w _ { 1 } \ w _ { 2 } \ \dots \ w _ { n } ) ^ { \top }$ is the weight, b is a scalar and σ is the activation function.

In computer science and engineering, people like to represent an abstract neuron by a graph (see Figure 1.5). In the graph, every edge with arrow towards the circle means multiplying a certain component of input x by a certain component of the weight w. And the circle means two steps: firstly, summarize all products of $w _ { i } x _ { i }$ for $i = 1 , \ldots , n$ and $b ;$ secondly, apply the activation σ to the preceding sum. The edge with arrow leaving the circle means the output scalar y.

The input vector x can be of several numerical types, such as:

• binary if $x _ { i } \in \{ 0 , 1 \}$ for $i = 1 , \ldots , n ;$

• signed if $x _ { i } \in \{ - 1 , 1 \}$ for $i = 1 , \ldots , n ;$

• integers if $x _ { i } \in S \subset \mathbb { I }$ for $i = 1 , \ldots , n ,$ , where I is set of all integers;

• real numbers if $x _ { i } \in \Omega \subset \mathbb { R }$ for $i = 1 , \ldots , n ;$

For instance, in the areas of image processing, the neurons take a picture with $m _ { 1 } \times m _ { 2 }$ pixels as the input. The color of every pixel is represented by an integer (e.g., for 8-bit grayscale pictures, the pixels are coded with $\{ 1 , \ldots , 2 ^ { 8 } \} )$ . Moreover, in spite of the “matrix” shape of the picture, it can be reshaped to a vector of length m<sub>1</sub>m<sub>2</sub> and then be received by neurons. However, a more popular way is using convolutional neurons which directly take a matrix (or a tensor) as the input, see later sections.

## Perceptrons

A perceptron is a neuron with binary inputs and the Heaviside activation function. More precisely, it is given by

$$
y = H (w ^ {\top} x + b) = \left\{ \begin{array}{l l} 0, & \text { if } w ^ {\top} x + b <   0, \\ 1, & \text { if } w ^ {\top} x + b \geq 0. \end{array} \right.
$$

Traditionally, perceptrons are used for logical (Boolean) operations. It can represent the AND operation, which is:

<table><tr><td> $x_1$ </td><td> $x_2$ </td><td> $y = x_1 \land x_2$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

It sufices to let

$$
y = H (x _ {1} + x _ {2} - 1. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   1. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 1. 5. \end{array} \right.
$$

Perceptrons can also represent the OR operation, which is:

<table><tr><td> $x_1$ </td><td> $x_2$ </td><td> $y = x_1 \lor x_2$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td></tr></table>

It sufices to let

$$
y = H (x _ {1} + x _ {2} - 0. 5) = \left\{ \begin{array}{l l} 0, & \text { if } x _ {1} + x _ {2} <   0. 5, \\ 1, & \text { if } x _ {1} + x _ {2} \geq 0. 5. \end{array} \right.
$$

However, a perceptron cannot implement all logical functions. For instance, it cannot implement XOR function, which is an operation defined by

<table><tr><td> $x_1$ </td><td> $x_2$ </td><td> $y = x_1 \oplus x_2$ </td></tr><tr><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>0</td></tr></table>

## Sigmoid neurons

Sigmoid neurons are the neurons with a sigmoidal activation function. For example, the neuron with logistic activation function $\textstyle \sigma ( t ) = { \frac { 1 } { 1 + e ^ { - c t } } }$ is given by

$$
y = \frac {1}{1 + e ^ {- c (w ^ {\top} x + b)}}.
$$

Clearly, as the parameter c becomes large, the above logistic sigmoid neuron tends to be a perceptron. Moreover, the neuron can take all values in $( 0 , 1 )$ , and if c is not too large, small changes in the weights and bias correspond to small changes in the output. Note that the neuron is $C ^ { \infty }$ smooth, allowing the diferentiation with the input x as well as the weight w and bias b.

## Linear neurons

The linear neuron is a neuron with identity activation function, $\sigma ( x ) = x$ . In this case, the neuron

$$
y = w ^ {\top} x + b
$$

![](images/e163a20f07686003e0ad769cb1e96c8075b7f522c88df78e835695f936f5a0a2.jpg)  
Figure 1.6: Madaline with two Adaline units.

is a linear function lifted by b. So the regression using linear neurons as the approximator is basically the linear regression. It is well known that linear regression enjoys many advantages. For example, linear regression with $L ^ { 2 }$ loss function is a convex optimization whose global optima can be found by solving a symmetric positive definite linear system.

## Adaline and Madaline

The Adaline (Adaptive Linear Neuron) is a neuron with binary inputs {±1} and sign activation function $\sigma ( x ) = \mathrm { s i g n } ( x )$ . More precisly, it is given by

$$
y = \mathrm{sign} (w ^ {\top} x + b).
$$

The Madaline (Multilayer adaptive linear element) consists of a layer of Adaline neurons connected to a fixed logic gate (AND, OR, etc.), which produces an output, see Figure 1.6. Only the weights associated with the Adaline units are free parameters, while the weights of the output logic gate are fixed.

For instance, a Madaline mapping $\mathbb { R } ^ { 2 }$ to {±1} with two Adaline units and AND output gate is given by

$$
y = M (x _ {1}, x _ {2}) = \mathrm{sign} (x _ {1} + x _ {2} + 1) \land \mathrm{sign} (- x _ {1} - x _ {2} + 0. 5).
$$

And it can be verified that $M ( 1 , 1 ) = M ( - 1 , - 1 ) = - 1$ and $M ( 1 , - 1 ) = M ( - 1 , 1 ) = 1$ . Namely, $M ( x _ { 1 } , x _ { 2 } )$ implement the XOR function (with 1 being true and −1 being false).

## 1.2.2 Forward pass through the network

As shown in Figure 1.5, an abstract neuron receives several scalars $x _ { 1 } , x _ { 2 } , \ldots , x _ { n }$ as the inputs, and produces a scalar y as the output. So it is natural to connect neurons one after another to construct a network of neurons. Specifically, we can take the output of a front neuron as an input of the next neuron. If the next neuron receives totally n scalars, we can set n front neurons whose outputs form the n-dimensional input vector. By such connections, it is possible to construct any complex network as we want.

For example, the graph in Figure 1.7 represents a network consisting of 5 neurons. The first and second neurons have common inputs $x _ { 2 }$ and $x _ { 3 }$ , but the second neuron has an extra input $x _ { 1 }$ . The outputs of the first and second neurons form the inputs of the third neuron. Moreover. the output of the first neuron is also received by the fourth neuron, which also takes $x _ { 1 }$ as another input. Finally, the outputs of the third and fourth neurons go to the fifth neuron, which produces the final output. We can formulate the above process as

![](images/95bd8c1400d38a7c1afddc7ca18d222c0fb174a0899f151a5a686aa05af5ee4b.jpg)  
Figure 1.7: A general neural network with 3 scalar inputs, 5 neurons and 1 scalar output.

$$
\begin{array}{r l} & y = y _ {5} \\ & y _ {5} = \sigma_ {5} (w _ {5} ^ {1} y _ {4} + w _ {5} ^ {2} y _ {3} + b _ {5}), \\ & y _ {4} = \sigma_ {4} (w _ {4} ^ {1} x _ {1} + w _ {4} ^ {2} y _ {1} + b _ {4}), \\ & y _ {3} = \sigma_ {3} (w _ {3} ^ {1} y _ {1} + w _ {3} ^ {2} y _ {2} + b _ {3}), \\ & y _ {1} = \sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1}), \\ & y _ {2} = \sigma_ {2} (w _ {2} ^ {1} x _ {1} + w _ {2} ^ {2} x _ {2} + w _ {2} ^ {3} x _ {3} + b _ {2}), \end{array}
$$

or write it as the composite form

$$
\begin{array}{l} y = \sigma_ {5} \Bigg [ \Bigg (w _ {5} ^ {1} \Big (\sigma_ {4} (w _ {4} ^ {1} x _ {1} + w _ {4} ^ {2} (\sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1})) + b _ {4}) \Big) \\ \qquad + w _ {5} ^ {2} \Big (\sigma_ {3} \big (w _ {3} ^ {1} (\sigma_ {1} (w _ {1} ^ {1} x _ {2} + w _ {1} ^ {2} x _ {3} + b _ {1})) + w _ {3} ^ {2} (\sigma_ {2} (w _ {2} ^ {1} x _ {1} + w _ {2} ^ {2} x _ {2} + w _ {2} ^ {3} x _ {3} + b _ {2})) \big) + b _ {3} \Big) \Bigg) + b _ {5} \Bigg ]. \end{array}
$$

Generally, a directed graph formed by connecting abstract neurons is called a neural network. The starting points are the inputs and the end points are the outputs (there could be multiple scalar outputs for a neural network). While essentially, such a directed graph is formed by function compositions. So we can also say a neural network is a composite function of abstract neurons. In Figure 1.7, all scalar inputs are passed from the front (left) to the end (right), so we say such a neural network is a feedforward neural network.

For practical purposes, we do not expect rambling or disordered neural networks. So we usually consider the neural networks with regular architectures, in which the neurons are connected layer by layer, see Figure 1.8. In this graph, the most front layer consisting of inputs is called the input layer; the end layer consisting of two output neurons is called the output layer; all the other layers between the input and output layers are called the hidden layers. We note in Figure 1.8 that every neuron in one hidden layer is connected to all the neurons (or inputs) in the last layer and all the neurons in the next layer; namely, all neurons are $f u l l y$ connected. A fully-connected feedforward neural network (also called a multilayer perceptron) with d inputs, L hidden layers and $d ^ { \prime }$ outputs can be formulated as follows:

![](images/29e7f1d0a0f1759f25fef137eaac5d3384f34dc64488682d801d14a20d512519.jpg)  
Figure 1.8: A fully-connected feedforward neural network with 5 scalar inputs, $\it 4$ hidden layers and 2 scalar outputs.

$$
y _ {j} = y _ {j} ^ {L + 1}, \quad \text { for } j = 1, \ldots , d ^ {\prime},\tag{1.8}
$$

$$
y _ {j} ^ {\ell} = \sigma_ {j} ^ {\ell} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}), \quad \text { for } j = 1, \ldots , M _ {\ell}, \ell = 1, \ldots , L + 1,\tag{1.9}
$$

$$
y _ {j} ^ {0} = x _ {j}, \quad \mathrm{for} j = 1, \ldots , d,\tag{1.10}
$$

where the input layer is indexed with $\ell = 0$ , hidden layers are indexed with $\ell = 1 , \ldots , L$ and the output layer is indexed with $\ell = L + 1$ ; for $1 \le \ell \le L$ , M<sub>ℓ</sub> is the number of neurons in the ℓth layer, which is also called the width of the ℓth layer; $M _ { 0 } = d$ is the number of inputs $x _ { 1 } , \ldots , x _ { d } .$ and $M _ { L + 1 } = d ^ { \prime }$ is the number of outputs $y _ { 1 } , \ldots , y _ { d ^ { \prime } } ; \sigma _ { j } ^ { \ell }$ denotes the activation function of the jth neuron in the ℓth layer; $\{ w _ { j i } ^ { \ell } \}$ and $\{ b _ { j } ^ { \ell } \}$ are the weights and biases in the ℓth layer, respectively. The number $L + 1$ is called the $d e p t h ,$ and we describe a neural network deep if L is large.

It is convenient to represent a fully-connected feedforward neural network in matrix-vector form. For simplicity we assume the activation functions in every layer are the same, i.e., $\sigma ^ { \ell } : = \sigma _ { 1 } ^ { \ell } = \cdot \cdot \cdot =$ $\sigma _ { M _ { \ell } } ^ { \ell }$ . And we denote

$$
y ^ {\ell} = \left( \begin{array}{c} y _ {1} ^ {\ell} \\ y _ {2} ^ {\ell} \\ \dots \\ y _ {M _ {\ell}} ^ {\ell} \end{array} \right), \quad W ^ {\ell} = \left( \begin{array}{c c c c} w _ {1 1} ^ {\ell} & w _ {1 2} ^ {\ell} & \ldots & w _ {1, M _ {\ell - 1}} ^ {\ell} \\ w _ {2 1} ^ {\ell} & w _ {2 2} ^ {\ell} & \ldots & w _ {2, M _ {\ell - 1}} ^ {\ell} \\ \ldots & \ldots & \ldots & \ldots \\ w _ {M _ {\ell}, 1} ^ {\ell} & w _ {M _ {\ell}, 2} ^ {\ell} & \ldots & w _ {M _ {\ell}, M _ {\ell - 1}} ^ {\ell} \end{array} \right), \quad b ^ {\ell} = \left( \begin{array}{c} b _ {1} ^ {\ell} \\ b _ {2} ^ {\ell} \\ \ldots \\ b _ {M _ {\ell}} ^ {\ell} \end{array} \right),
$$

then (1.8)-(1.10) can be rewritten as

$$
\begin{array}{l} y = y ^ {L + 1}, \\ y ^ {\ell} = \sigma^ {\ell} (W ^ {\ell} y ^ {\ell - 1} + b ^ {\ell}), \quad \ell = 1, \ldots , L + 1, \\ y ^ {0} = x, \end{array}
$$

or simply

$$
y = \sigma^ {L + 1} \left(W ^ {L + 1} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b ^ {L + 1}\right).\tag{1.11}
$$

In regression problems, the activation function of the output layer is often set as the identity function $\sigma ^ { L + 1 } ( t ) = t ,$ , in which case we can omit $\sigma ^ { L + 1 }$ in the architecture of neural networks; namely,

$$
y = W ^ {L + 1} \sigma^ {L} \Big (W ^ {L} \sigma^ {L - 1} \big (\ldots \sigma^ {1} (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b ^ {L + 1}.
$$

While in classification problems, the output activation is often set as the softmax function.

If $d ^ { \prime } = 1$ , the output y is a scalar. Then the weight matrix $W ^ { L + 1 }$ of the output layer is a row vector, and the bias vector $b ^ { L + 1 }$ is a scalar. In this case, we can denote $\boldsymbol { a } = \left( W ^ { L + 1 } \right) ^ { \top }$ as a column vector and $b = b ^ { L + 1 }$ as a scalar, and rewrite (1.11) as

$$
y = \sigma^ {L + 1} \left(a ^ {\top} \sigma^ {L} \left(W ^ {L} \sigma^ {L - 1} \left(\dots \sigma^ {1} \left(W ^ {1} x + b ^ {1}\right) \dots\right) + b ^ {L}\right) + b\right).\tag{1.12}
$$

Usually, we use the notation of function $f ( x ; \theta )$ to represent a neural network, where x is the input vector and θ is the set of all free parameters. In (1.11), the free parameters are $\{ b ^ { \ell } , W ^ { \ell } \} _ { \ell = 1 } ^ { L + 1 }$ Note that the free parameters completely determine the neural network function. However, the same neural network may be determined by diferent sets of parameters. This is diferent from the functions in finite-dimensional linear spaces, where any function is a linear combination of basis functions and is uniquely determined by the coeficients.

So far, the fully-connected feedforward neural network has been the most fundamental and widely used network in science and engineering. So in the rest of Section 1.2, the term “neural network” means exclusively the fully-connected feedforward neural network unless otherwise stated.

Evaluating $f ( x ; \theta )$ for a given vector $\boldsymbol { x } \in \mathbb { R } ^ { d }$ is equivalent to pass x forward through the network flow graph (see Figure 1.8). The process is also called forward propagation. It is easy to count the complexity of the forward propagation. For simplicity, we consider the network (1.12) assuming that all hidden layers have the same width M and the activations $\{ \sigma ^ { \ell } \}$ are suficiently simple so that $\boldsymbol { \sigma } ^ { \ell } ( t )$ costs $O ( 1 )$ for every scalar t and all ℓ. Then $\sigma ^ { \ell } ( W ^ { \ell } y ^ { \ell - 1 } { + } b ^ { \ell } )$ costs $( 2 M - 1 ) M + M + O ( M ) = O ( M ^ { 2 } )$ for $\ell = 2 , \ldots , L$ and $( 2 d - 1 ) M + M + O ( M ) = O ( d M )$ for $\ell = 1$ . Besides, the output layer $\sigma ^ { L + 1 } ( a ^ { \top } y ^ { L } + b )$ costs $O ( M )$ . Consequently, the total complexity of the forward propagation for the network (1.12) is $O ( ( L - 1 ) M ^ { 2 } + d M )$ if d and M are large quantities. Note that this complexity is exactly the number of edges in the flow graph.

## 1.2.3 Diferentiation of fully-connected neural networks

The diferentiation of deep fully-connected neural networks can be also understood as propagation in the flow graph. Generally, we let $y = f ( x ; \theta )$ be a neural network mapping $\mathbb { R } ^ { d }$ to R formulated

by

$$
y = \sigma^ {L + 1} (\sum_ {i = 1} ^ {M _ {L}} a _ {i} y _ {i} ^ {L} + b),\tag{1.13}
$$

$$
y _ {j} ^ {\ell} = \sigma_ {j} ^ {\ell} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}), \quad \text { for } j = 1, \ldots , M _ {\ell}, \ell = 2, \ldots , L,\tag{1.14}
$$

$$
y _ {j} ^ {1} = \sigma_ {j} ^ {1} (\sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}), \quad \text { for } j = 1, \ldots , M _ {1},\tag{1.15}
$$

where $a _ { i } , b , w _ { j i } ^ { \ell } , b _ { j } ^ { \ell }$ are scalar free parameters and $\sigma ^ { L + 1 } , \sigma _ { j } ^ { \ell }$ are diferentiable activation functions.

## Derivatives w.r.t. one input

First, we consider the computation of the derivatives with respect to one input $x _ { k }$ for any $1 \leq k \leq d .$ Denote $\begin{array} { r } { z _ { i } ^ { \ell } = \frac { \partial y _ { i } ^ { \ell } } { \partial x _ { k } } } \end{array}$ . Then by the chain rule, we have

$$
\frac {\partial y}{\partial x _ {k}} = \left(\sigma^ {L + 1}\right) ^ {\prime} (\sum_ {i = 1} ^ {M _ {L}} a _ {i} y _ {i} ^ {L} + b) \cdot \sum_ {i = 1} ^ {M _ {L}} a _ {i} z _ {i} ^ {L},\tag{1.16}
$$

$$
z _ {j} ^ {\ell} = \left(\sigma_ {j} ^ {\ell}\right) ^ {\prime} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}) \cdot \sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} z _ {i} ^ {\ell - 1}, \quad \text {for} j = 1, \ldots , M _ {\ell}, \ell = 2, \ldots , L,\tag{1.17}
$$

$$
z _ {j} ^ {1} = \left(\sigma_ {j} ^ {1}\right) ^ {\prime} (\sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}) \cdot w _ {j k} ^ {1}, \quad \mathrm{for} j = 1, \ldots , M _ {1}.\tag{1.18}
$$

Therefore, computing $\frac { \partial y } { \partial x _ { k } }$ can be implemented by forward propagation. In every iteration, we compute not only $\{ y _ { j } ^ { \ell } \}$ using (1.13)-(1.15), but also $\{ z _ { j } ^ { \ell } \}$ and $\textstyle { \frac { \partial y } { \partial x _ { k } } }$ using (1.16)-(1.18). All the computation can be performed in matrix-vector multiplications. We denote the matrix and column vectors as

$$
a = (a _ {i}) _ {i = 1, \dots , M _ {L}}, W ^ {\ell} = \left(w _ {j i} ^ {\ell}\right) _ {j = 1, \dots , M _ {\ell}} ^ {i = 1, \dots , M _ {\ell - 1}}, b ^ {\ell} = \left(b _ {i} ^ {\ell}\right) _ {i = 1, \dots , M _ {\ell}},
$$

for $\ell = 1 , \ldots , L \left( M _ { 0 } = d \right)$ . Also, let $\sigma ^ { \ell } ( q ) : = \left( \sigma _ { 1 } ^ { \ell } ( q _ { 1 } ) \ldots \sigma _ { M _ { \ell } } ^ { \ell } ( q _ { M _ { \ell } } ) \right) ^ { \top }$ be the vector-valued function that is applied to any $q \in \mathbb { R } ^ { M _ { \ell } }$ componentwise. And similar notation is for $( \sigma ^ { \ell } ) ^ { \prime } ( p )$ . Then the above algorithm is shown as Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Forward propagation. $(f(x;\theta)$ is given by (1.13)-(1.15))

Input: A set of parameters $\theta = \{a, W^1, \ldots, W^L, b, b^1, \ldots, b^L\}$; an vector $x \in \mathbb{R}^d$.

Output: $z = \frac{\partial f(x;\theta)}{\partial x_k}$ evaluated at the input $(x;\theta)$.

1: $q^1 = W^1 x + b^1$, $y^1 = \sigma^1(q^1)$, $z^1 = (\sigma^1)'(q^1) \odot W^1(:, k)$;

2: for $\ell = 2, \ldots, L$ do

3: $q^\ell = W^\ell y^{\ell-1} + b^\ell$, $y^\ell = \sigma^\ell(q^\ell)$, $z^\ell = (\sigma^\ell)'(q^\ell) \odot (W^\ell z^{\ell-1})$;

4: end for

5: $q^{L+1} = a^\top y^L + b$, $y = \sigma^{L+1}(q^{L+1})$, $z = (\sigma^{L+1})'(q^{L+1}) \odot (a^\top z^L)$;
</div>

In Algorithm 1, ⊙ means the entrywise multiplication of two vectors of the same size and $W ^ { 1 } ( : , k )$ means the kth column of $W ^ { 1 }$ . Although the goal is to compute $\frac { \partial f ( x ; \theta ) } { \partial x _ { k } }$ , we actually obtain the byproduct $y = f ( x ; \theta )$

In the special case that $M = M _ { \ell }$ for $\ell = 1 , \ldots , L$ , assuming that $\sigma _ { j } ^ { \ell }$ and $\sigma ^ { L + 1 }$ as well as their diferentiation cost $O ( 1 )$ operations, then it is trivial to see that the complexity of Algorithm 1 is $O ( ( L - 1 ) M ^ { 2 } + d M )$ for large d and $M$

## Derivatives w.r.t. weights, biases and inputs

The above algorithm of computing $\frac { \partial f ( x ; \theta ) } { \partial x _ { k } }$ for a sole $x _ { k }$ is straightforward and easy to implement. But if we use it to compute $\nabla _ { x } f ( x ; \theta )$ , it requires to repeat Algorithm 1 for d times, each of which is for one derivative. So the total complexity will be enlarged to $O ( ( L - 1 ) d M ^ { 2 } )$ . Fortunately, the next algorithm can compute not only $\nabla _ { x } f ( x ; \theta )$ but $\nabla _ { { \boldsymbol { \theta } } } f ( { \boldsymbol { x } } ; { \boldsymbol { \theta } } )$ with only $O ( ( L - 1 ) M ^ { 2 } + d M )$ complexity. Note that the computation of the latter is very common in deep learning applications. For example, when using gradient descent to solve the optimization, one needs to compute the gradient with respect to the free parameters of the neural network in every iteration; namely, one needs to compute $\begin{array} { r } { \nabla _ { \theta } f ( x ; \theta ) = \left\{ \frac { \partial f ( x ; \theta ) } { \partial a _ { j } } , \frac { \partial f ( x ; \theta ) } { \partial w _ { j i } ^ { \ell } } , \frac { \partial f ( x ; \theta ) } { \partial b } , \frac { \partial f ( x ; \theta ) } { \partial b _ { j } ^ { \ell } } \right\} } \end{array}$

We rewrite the neural network (1.13)-(1.15) as

$$
y = \sigma^ {L + 1} (q ^ {L + 1}), \quad q ^ {L + 1} = \sum_ {i = 1} ^ {M _ {L}} a _ {i} y _ {i} ^ {L} + b,\tag{1.19}
$$

$$
y _ {j} ^ {\ell} = \sigma_ {j} ^ {\ell} (q _ {j} ^ {\ell}), \quad q _ {j} ^ {\ell} = \sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} + b _ {j} ^ {\ell}, \quad \text {for} j = 1, \ldots , M _ {\ell}, \ell = 2, \ldots , L,\tag{1.20}
$$

$$
y _ {j} ^ {1} = \sigma_ {j} ^ {1} (q _ {j} ^ {1}), \quad q _ {j} ^ {1} = \sum_ {i = 1} ^ {d} w _ {j i} ^ {1} x _ {i} + b _ {j} ^ {1}, \quad \text { for } j = 1, \ldots , M _ {1}.\tag{1.21}
$$

Also, we introduce intermediate variables $\begin{array} { r } { p ^ { L + 1 } : = \frac { \mathrm { d } f ( x ; \theta ) } { \mathrm { d } q ^ { L + 1 } } = \frac { \mathrm { d } y } { \mathrm { d } q ^ { L + 1 } } } \end{array}$ and $\begin{array} { r } { p _ { i } ^ { \ell } : = \frac { \partial f ( x ; \theta ) } { \partial q _ { i } ^ { \ell } } = \frac { \partial y } { \partial q _ { i } ^ { \ell } } } \end{array}$

Now suppose we have already performed forward propagation, obtain $y _ { j } ^ { \ell }$ and $q _ { j } ^ { \ell }$ for all ℓ and j, and save them in the memory. Then the so-called “back propagation” algorithm is to compute all derivatives recursively from the ℓth layer to the $( \ell - 1 ) \mathrm { t h }$ layer. Diferent from the forward propagation that starts from the inputs, back propagation starts from the output neuron $N _ { 1 } ^ { L + 1 }$ and goes from right to left.

At the first step, we first compute

$$
p ^ {L + 1} = \frac {\mathrm{d} f (x ; \theta)}{\mathrm{d} q ^ {L + 1}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} = (\sigma^ {L + 1}) ^ {\prime} (q ^ {L + 1}).\tag{1.22}
$$

Then by the chain rule, we have the derivatives with respect to $a _ { i } ~ ( 1 \leq i \leq M _ { L } )$ ,

$$
\frac {\partial f (x ; \theta)}{\partial a _ {i}} = \frac {\mathrm{d} f (x ; \theta)}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial a _ {i}} = p ^ {L + 1} \cdot y _ {i} ^ {L}
$$

At the second step, we first compute $p _ { i } ^ { L }$ by

$$
\begin{array}{c} p _ {i} ^ {L} = \frac {\partial f (x ; \theta)}{\partial q _ {i} ^ {L}} = \frac {\mathrm{d} y}{\mathrm{d} q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial y _ {i} ^ {L}} \cdot \frac {\mathrm{d} y _ {i} ^ {L}}{\mathrm{d} q _ {i} ^ {L}} \\ = p ^ {L + 1} \cdot a _ {i} \cdot (\sigma_ {i} ^ {L}) ^ {\prime} (q _ {i} ^ {L}) \end{array}\tag{1.23}
$$

and then use the result to compute the derivatives with respect to $w _ { j i } ^ { L } \left( 1 \leq j \leq M _ { L } , 1 \leq i \leq M _ { L - 1 } \right)$ 2

$$
\begin{array}{r} \frac {\partial f (x ; \theta)}{\partial w _ {j i} ^ {L}} = \frac {\partial f (x ; \theta)}{\partial q _ {j} ^ {L}} \cdot \frac {\partial q _ {j} ^ {L}}{\partial w _ {j i} ^ {L}} \\ = p _ {j} ^ {L} \cdot y _ {i} ^ {L - 1} \end{array}\tag{1.24}
$$

Next, for $\ell = L - 1 , L - 2 , \dots , 1$ , we similarly have

$$
\begin{array}{c} p _ {i} ^ {\ell} = \frac {\partial f (x ; \theta)}{\partial q _ {i} ^ {\ell}} = \sum_ {j = 1} ^ {M _ {\ell + 1}} \frac {\partial f (x ; \theta)}{\partial q _ {j} ^ {\ell + 1}} \cdot \frac {\partial q _ {j} ^ {\ell + 1}}{\partial y _ {i} ^ {\ell}} \cdot \frac {\mathrm{d} y _ {i} ^ {\ell}}{\mathrm{d} q _ {i} ^ {\ell}} \\ = \sum_ {j = 1} ^ {M _ {\ell + 1}} p _ {j} ^ {\ell + 1} \cdot w _ {j i} ^ {\ell + 1} \cdot (\sigma_ {i} ^ {\ell}) ^ {\prime} (q _ {i} ^ {\ell}) \end{array}\tag{1.25}
$$

and

$$
\begin{array}{r} \frac {\partial f (x ; \theta)}{\partial w _ {j i} ^ {\ell}} = \frac {\partial f (x ; \theta)}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial w _ {j i} ^ {\ell}} \\ = \left\{ \begin{array}{l l} p _ {j} ^ {\ell} \cdot y _ {i} ^ {\ell - 1}, & \text {if} \ell \geq 2, \\ p _ {j} ^ {\ell} \cdot x _ {i}, & \text {if} \ell = 1. \end{array} \right. \end{array}\tag{1.26}
$$

So far, we have completed computing all the derivatives with respect to $\{ a _ { i } , w _ { j i } ^ { \ell } \}$ . And we can step further to obtain the derivatives with respect to $\{ x _ { i } \}$ , i.e.

$$
\frac {\partial f (x ; \theta)}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} \frac {\partial f (x ; \theta)}{\partial q _ {j} ^ {1}} \cdot \frac {\partial q _ {j} ^ {1}}{\partial x _ {i}} = \sum_ {j = 1} ^ {M _ {1}} p _ {j} ^ {1} w _ {j i} ^ {1},
$$

for $i = 1 , \ldots , d .$

Similarly, we can deduce the formula for the derivatives with respect to $\{ b , b _ { j } ^ { \ell } \}$ as follows:

$$
\begin{array}{l} \frac {\partial f (x ; \theta)}{\partial b} = \frac {\partial f (x ; \theta)}{\partial q ^ {L + 1}} \cdot \frac {\partial q ^ {L + 1}}{\partial b} = p ^ {L + 1} \cdot 1 = p ^ {L + 1}, \\ \frac {\partial f (x ; \theta)}{\partial b _ {j} ^ {\ell}} = \frac {\partial f (x ; \theta)}{\partial q _ {j} ^ {\ell}} \cdot \frac {\partial q _ {j} ^ {\ell}}{\partial b _ {j} ^ {\ell}} = p _ {j} ^ {\ell} \cdot 1 = p _ {j} ^ {\ell}, \end{array}
$$

for $j = 1 , \ldots , M _ { \ell }$ and $\ell = 2 , \ldots , L$ . Figure 1.9 visualizes the procedure of back propagation on a 4-layer neural network with width 3 in every layer.

![](images/f35976df35210751bc11e14b1a4ef21e7f58c9cff1deef7753d57b02f7bff482.jpg)  
(a) computation in the output layer

![](images/b7880d4ec59584c2a99c12136fc9d6cfdd1f4132878f3ab21fba6785b3b05c5c.jpg)  
(b) from the output layer to the 3rd layer

![](images/aa8f9f5e8884486837bf656ffe2e792b7e7da91d80728183c7abfcdfeb7b7bd0.jpg)  
(c) from the 3rd layer to the 2nd layer

![](images/6f5f4314949eebbfb346c17130751ee4bf23e34d9c3c9f4e77fb7c59d0a0a3ab.jpg)  
(d) from the 2nd layer to the 1st layer

![](images/2e20b1563f2dae08ea78fe13ae7e53b91c66c84635f30ae71e7f8f9dad89a515.jpg)  
(e) from the 1st layer to input layer  
Figure 1.9: Back propagation to compute derivatives with respect to weights. Here $N _ { i } ^ { \ell }$ means the ith neuron in the ℓth layer; $\tilde { y } ^ { 4 } : = ( \sigma ^ { 4 } ) ^ { \prime } ( q ^ { 4 } )$ and $\tilde { y } _ { i } ^ { \ell } : = ( \sigma _ { i } ^ { \ell } ) ^ { \prime } ( q _ { i } ^ { \ell } )$ for $\ell = 1 , 2 , 3$ . (The red variables are currently computed using the blue variables that are computed previously.)

The algorithm in matrix-vector form is summarized in Algorithm 2. The outputs are saved by

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$u^{L + 1} = \left(\frac{\partial f(x;\theta)}{\partial a_1}\right.\dots \frac{\partial f(x;\theta)}{\partial a_{M_L}}\right)\in \mathbb{R}^{1\times M_L},$ $U^{\ell} = \left( \begin{array}{lll}\frac{\partial f(x;\theta)}{\partial w_{11}^{\ell}} &amp; \frac{\partial f(x;\theta)}{\partial w_{12}^{\ell}} &amp; \dots \\ \frac{\partial f(x;\theta)}{\partial w_{21}^{\ell}} &amp; \frac{\partial f(x;\theta)}{\partial w_{22}^{\ell}} &amp; \dots \\ \dots &amp; \dots &amp; \dots \\ \frac{\partial f(x;\theta)}{\partial w_{M_\ell,1}^\ell} &amp; \frac{\partial f(x;\theta)}{\partial w_{M_\ell,2}^\ell} &amp; \dots \\ \end{array} \right)\in \mathbb{R}^{M_\ell\times M_\ell - 1},\quad \ell = 1,\ldots ,L,$ $p^{L + 1} = \frac{\partial f(x;\theta)}{\partial b},\quad p^{\ell} = \left(\frac{\partial f(x;\theta)}{\partial b_1^{\ell}}\right.\dots \frac{\partial f(x;\theta)}{\partial b_{M_\ell}^\ell}\right)^{\top}\in \mathbb{R}^{M_\ell\times 1},\quad \ell = 1,\ldots ,L,$ $z = \left(\frac{\partial f(x;\theta)}{\partial x_1}\right.\dots \left.\frac{\partial f(x;\theta)}{\partial x_d}\right)^{\top}\in \mathbb{R}^{d\times 1}.$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Forward &amp; back propagation. (f(x;θ) is given by (1.13)-(1.15))

Input: A set of parameters θ = {a, W¹, ..., W^L, b, b¹, ..., b^L}; an vector x ∈ ℝ^d.

Output: $\frac{\partial f(x;\theta)}{\partial a_i}$, $\frac{\partial f(x;\theta)}{\partial w_{ji}^\ell}$, $\frac{\partial f(x;\theta)}{\partial b}$, $\frac{\partial f(x;\theta)}{\partial b_j^\ell}$, $\frac{\partial f(x;\theta)}{\partial x_i}$ evaluated at the input (x;θ) for all i, j, ℓ.

1: y⁰ = x;

2: for ℓ = 1, ..., L do

3: $q^\ell = W^\ell y^{\ell-1} + b^\ell$, $y^\ell = \sigma^\ell(q^\ell)$, $\tilde{y}^\ell = (\sigma^\ell)'(q^\ell)$;

4: end for

5: $q^{L+1} = a^\top y^L + b$, $y = \sigma^{L+1}(q^{L+1})$, $\tilde{y} = (\sigma^{L+1})'(q^{L+1})$;

6: $p^{L+1} = \tilde{y}$, $u^{L+1} = p^{L+1}(y^L)^\top$;

7: $p^L = (ap^{L+1}) \odot \tilde{y}^L$, $U^L = p^L(y^{L-1})^\top$;

8: for ℓ = L - 1, ..., 1 do

9: $p^\ell = \left((W^{\ell+1})^\top p^{\ell+1}\right) \odot \tilde{y}^\ell$, $U^\ell = p^\ell(y^{\ell-1})^\top$;

10: end for

11: $z = (W^1)^\top p^1$;
</div>

In Algorithm 2, Line 1-5 is the forward propagation with $O ( ( L - 1 ) M ^ { 2 } + d M )$ complexity, and Line 6-11 is the back propagation with $O ( ( L - 1 ) M ^ { 2 } )$ complexity. So the total complexity is $O ( ( L - 1 ) M ^ { 2 } + d M )$ for large d and M. In the case that $f ( x ; \theta )$ has $d ^ { \prime } > 1$ scalar outputs, we have to run Line 5-11 for $d ^ { \prime }$ times, each of which has a particular weight a for the certain scalar output. So the total complexity is $O \left( d ^ { \prime } ( ( L - 1 ) M ^ { 2 } + d M ) \right)$

Note that the complexity increases linearly with $d ^ { \prime } .$ One may worry that when the output dimension $d ^ { \prime }$ is large, the complexity of back propagation becomes significantly large and dominates the complexity of forward propagation. In practice, for $d ^ { \prime } > 1$ , we do not compute the gradient of the neural network with respect to the parameters; instead, we directly compute the gradient of the loss function with respect to the parameters using back propagation. Specifically, let $f : \mathbb { R } ^ { d }  \mathbb { R } ^ { d ^ { \prime } }$ $( x _ { 1 } , \ldots , x _ { d } )  ( y _ { 1 } , \ldots , y _ { d ^ { \prime } } )$ be a vector-valued neural network, and let $\mathcal { L } ( \cdot ) : \mathbb { R }  \mathbb { R }$ be some scalarvalued loss function. The learning task is to solve min<sub>θ</sub> $\mathcal { L } ( f ( x _ { 1 } , \dots , x _ { d } ; \theta ) )$ over some dataset. In this case, we only need to regard $g ( x ; \theta ) : = \mathcal { L } ( f ( x _ { 1 } , \dots , x _ { d } ; \theta ) )$ as an “augmented” neural network from $\mathbb { R } ^ { d }$ to $\mathbb { R } ,$ and compute the gradient $\nabla _ { \boldsymbol { \theta } } g$ by the preceding back propagation scenario. The complexity is usually much less than $O \left( d ^ { \prime } ( ( L - 1 ) M ^ { 2 } + d M ) \right)$ . (See Exercises)

![](images/2df3f431b7f09ddf2f3ab590c95198739812281586a0b70415f3b7163369734f.jpg)  
Figure 1.10: A general deep neural network.

## 1.2.4 Diferentiation of general deep neural networks

The forward & back propagation algorithm discussed above can be generalized to the diferentiation of arbitrary deep neural networks. For a general network, it may not be split layer by layer, but it can be still represented by a flow graph. And hence the back propagation is performed by starting from the output neuron, passing information backward, and ending at the inputs.

More precisely, given a graph of neural network $f ( x ; \theta )$ mapping from $\mathbb { R } ^ { d }$ to $\mathbb { R } ,$ , we label the inputs by $x _ { 1 } , \ldots , x _ { d }$ and neurons by $N _ { d + 1 } , \dots , N _ { d + K }$ , supposing there are totally K neurons. For convenience, the neurons are labeled such that the directed edges are always from small indices to large indices.

We denote the weight of the edge from neuron $N _ { i }$ (or input $x _ { i } )$ to neuron $N _ { j }$ by $w _ { i , j }$ . Let $P _ { j }$ be the set consisting of the indices of the direct predecessors of the neuron $N j \ ( d + 1 \leq j \leq d + K )$ Similarly, let $S _ { j }$ be the set consisting of the indices of the direct successors of the vertex $x _ { j } \ ( 1 \leq j \leq$ $d )$ or $N j \ \left( d + 1 \leq j < d + K \right)$ . For example, in Figure 1.10, $P _ { 7 } = \{ 2 , 3 , 5 , 6 \}$ and $S _ { 7 } = \{ 9 , 1 0 , 1 1 \}$ .

Now, suppose the following computation occurs at $N _ { j }$ :

$$
y _ {j} = \sigma_ {j} (q _ {j}), \quad q _ {j} = \sum_ {k \in P _ {j}} w _ {k, j} y _ {k} + b _ {j}, \quad \text { for } d + 1 \leq j \leq d + K,\tag{1.27}
$$

where $\sigma _ { j }$ and $b _ { j }$ are the activation function and bias of $N _ { j }$ . And we denote

$$
y _ {j} = x _ {j}, \quad \text { for } 1 \leq j \leq d.\tag{1.28}
$$

for convenience in notation. Note that $y _ { j }$ means the output value of the vertex $N _ { j }$ or $x _ { j }$ . Also, we denote $\begin{array} { r } { p _ { j } : = \frac { \partial f ( x ; \theta ) } { \partial q _ { j } } } \end{array}$ for $d + 1 \leq j \leq d + K$ . Using the chain rule, if $i \in P _ { j }$ , we have

$$
\frac {\partial f (x ; \theta)}{\partial w _ {i , j}} = \frac {\partial f (x ; \theta)}{\partial q _ {j}} \cdot \frac {\partial q _ {j}}{\partial w _ {i , j}} = p _ {j} \cdot y _ {i},\tag{1.29}
$$

$$
\frac {\partial f (x ; \theta)}{\partial b _ {j}} = \frac {\partial f (x ; \theta)}{\partial q _ {j}} \cdot \frac {\partial q _ {j}}{\partial b _ {j}} = p _ {j}.\tag{1.30}
$$

Also, $p _ { j }$ can be computed by

$$
p _ {d + K} = \frac {\partial f (x ; \theta)}{\partial q _ {d + K}} = \frac {\mathrm{d} y _ {d + K}}{\mathrm{d} q _ {d + K}} = \sigma_ {d + K} ^ {\prime} (q _ {d + K})\tag{1.31}
$$

and

$$
\begin{array}{l} p _ {j} = \frac {\partial f (x ; \theta)}{\partial q _ {j}} = \sum_ {k \in S _ {j}} \frac {\partial f (x ; \theta)}{\partial q _ {k}} \cdot \frac {\partial q _ {k}}{\partial y _ {j}} \cdot \frac {\mathrm{d} y _ {j}}{\mathrm{d} q _ {j}} \\ \qquad = \sigma_ {j} ^ {\prime} (q _ {j}) \cdot \sum_ {k \in S _ {j}} p _ {k} \cdot w _ {j, k} \quad \text { for } d + 1 \leq j <   d + K. \end{array}\tag{1.32}
$$

Moreover, we have

$$
\begin{array}{c} \frac {\partial f (x ; \theta)}{\partial x _ {j}} = \sum_ {k \in S _ {j}} \frac {\partial f (x ; \theta)}{\partial q _ {k}} \cdot \frac {\partial q _ {k}}{\partial y _ {j}} \cdot \frac {\partial y _ {j}}{\partial x _ {j}} \\ = \sum_ {k \in S _ {j}} p _ {k} \cdot w _ {j, k} \quad \text { for } 1 \leq j \leq d. \end{array}\tag{1.33}
$$

Consequently, we can first implement the forward propagation (1.27)-(1.28), which passes the information from inputs $x _ { 1 } , \ldots , x _ { d }$ to the output neuron $N _ { d + K }$ . At this stage, we compute and save $\{ y _ { j } \}$ and $\{ q _ { j } \}$ for $j = 1 , \ldots , d + K$ from small to large. Next, we implement the back propagation (1.29)-(1.32), which passes from $N _ { d + K }$ to the inputs. Specifically, we compute $\{ p _ { j } \} , \left\{ \begin{array} { l }  \frac { \partial f ( \boldsymbol { x } ; \boldsymbol { \theta } ) } { \partial w _ { i , j } } \right\} _ { i \in P _ { j } } \end{array}$ and $\left\{ \frac { \partial f ( x ; \theta ) } { \partial b _ { j } } \right\}$ for $j = d + K , d + K - 1 , \dots , d + 1$ from large to small. And finally, $\left\{ \frac { \partial f ( x ; \theta ) } { \partial x _ { j } } \right\}$ for $j = 1 , \ldots , d$ are computed by (1.33).

## Derivatives formulated by paths

More generally, we can formulate the closed forms for the derivatives. In the sense of graph theory, denote $\mathcal { P } ( j , n _ { 1 } , n _ { 2 } , . . . , n _ { k } , d + K )$ as a path from the vertex $N _ { j }$ or $x _ { j }$ to the output neuron $N _ { d + K }$ through neurons $N _ { n _ { 1 } } , N _ { n _ { 2 } } , \ldots , N _ { n _ { k } }$ successively. Then by the chain rule, for any $d + 1 \leq j \leq d + K$ and $i \in P _ { j }$

$$
\begin{array}{c} \frac {\partial f (x ; \theta)}{\partial w _ {i , j}} = y _ {i} \cdot \sum_ {\mathcal {P} (j, n _ {1}, n _ {2}, \ldots , n _ {k}, d + K)} \sigma_ {j} ^ {\prime} (q _ {j}) \cdot w _ {j, n _ {1}} \cdot \sigma_ {n _ {1}} ^ {\prime} (q _ {n _ {1}}) \cdot w _ {n _ {1}, n _ {2}} \cdot \sigma_ {n _ {2}} ^ {\prime} (q _ {n _ {2}}) \\ \dots w _ {n _ {k}, d + K} \cdot \sigma_ {d + K} ^ {\prime} (q _ {d + K}), \end{array}\tag{1.34}
$$

where the summation is taken over all paths from $N _ { j }$ to $N _ { d + K }$ . Similarly, for $1 \leq j \leq d _ { \cdot }$

$$
\frac {\partial f (x ; \theta)}{\partial x _ {j}} = \sum_ {\substack {\mathcal {P} (j, n _ {1}, n _ {2}, \ldots , n _ {k}, d + K)}} w _ {j, n _ {1}} \cdot \sigma_ {n _ {1}} ^ {\prime} (q _ {n _ {1}}) \cdot w _ {n _ {1}, n _ {2}} \cdot \sigma_ {n _ {2}} ^ {\prime} (q _ {n _ {2}})   \dots w _ {n _ {k}, d + K} \cdot \sigma_ {d + K} ^ {\prime} (q _ {d + K}),
$$

where the summation is taken over all paths from $x _ { j }$ to $N _ { d + K }$

Suppose all activation functions of $f ( x ; \theta )$ are sigmoid functions. Note that if an intermediate variable $q _ { i }$ has a moderately large modulus $| q _ { i } |$ , the term $\sigma _ { i } ^ { \prime } ( q _ { i } )$ will be close to zero. Then for long paths, the product on the right hand side containing with many small multipliers $\sigma _ { i } ^ { \prime } ( q _ { i } )$ will be very close to zero. Consequently, if the edge with weight $w _ { i , j }$ is far from the output neuron, the derivative $\frac { \partial f ( \boldsymbol { x } ; \boldsymbol { \theta } ) } { \partial w _ { i , j } }$ might be very close to zero and even underflowed by the machine precision in practical computation.

Moreover, suppose we have a loss function $\mathcal { L } ( f ( x ; \theta ) )$ , where $\mathcal { L } ( \cdot )$ is diferentiable. When using gradient descent to optimize ${ \mathcal { L } } ,$ we compute $\nabla _ { \boldsymbol { \theta } } \mathcal { L }$ that has components

$$
\nabla_ {w _ {i, j}} \mathcal {L} = \mathcal {L} ^ {\prime} (f (x; \theta)) \cdot \frac {\partial f (x ; \theta)}{\partial w _ {i , j}}.
$$

So vanishing $\frac { \partial f ( \boldsymbol { x } ; \boldsymbol { \theta } ) } { \partial w _ { i , j } }$ will probably cause the vanishing of $\nabla _ { w _ { i , j } } \mathcal { L }$ . In this case, the parameter $w _ { i , j }$ can be hardly changed by gradient descent, and hence the convergence will be vastly slowed down. This vanishing gradient problem often appears in the optimization involving very deep neuron networks with sigmoid functions. One possible efective way to resolve the vanishing gradient problem is using residual neural networks (ResNets) [7].

## 1.2.5 Weight initialization

In the case of networks with a small number of layers initializing all weights and biasses to zero, or sample them from a uniform or a Gaussian distribution of zero mean, usually provides satisfactory enough convergence results. However, in the case of deep neural networks, a correct initialization of weights makes a significant diference in the way the convergence of the optimality algorithm works.

Too small or large magnitude of weights may cause vanishing or exploding gradient problems. This can be recognized partially from the gradient expression (1.34). If $\sigma _ { j } ^ { \prime }$ are finite and the weights $w _ { j i }$ have too small magnitude, the products of long paths will be close to zero, hence leading to vanishing gradients. On the other hand, for sigmoid activation fruitions, if $| w _ { j i } |$ are moderately large, $\begin{array} { r } { q _ { j } = \sum _ { k \in P _ { i } } w _ { k , j } y _ { k } + b _ { j } } \end{array}$ will also be large such that $\sigma _ { j } ^ { \prime } ( q _ { j } )$ are close to zero. Then the products of long paths will vanish as well as the gradient. But for hockey-stick activation functions, the products with many large $| w _ { j i } |$ will be very large, and thus the gradients blows up.

## Forward propagation point of view

Now let us investigate proper initialization strategies for the weights $w _ { j i }$ . We suppose the information is passed by forward propagation from $( \ell - 1 )$ )th layer to ℓth layer, i.e.

$$
y _ {j} ^ {\ell} = \sigma_ {j} ^ {\ell} (\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1}),\tag{1.35}
$$

where $j$ is the index of the neuron in the ℓth layer. Here we omit the bias. In practice, the biases are often initialized to zero or random variables with zero mean. For simplicity, we assume that $\{ w _ { i j } ^ { \ell } \} _ { i , j }$ and $\{ y _ { i } ^ { \ell - 1 } \}$ are two sets of independent and identically distributed random variables with zero mean. Also, in the forward propagation, $y _ { i } ^ { \ell - 1 }$ are computed by previous weights and is hence independent of $w _ { i j } ^ { \ell }$ . Then we are supposed to find distributions of $w _ { i j } ^ { \ell }$ such that the output in ℓth layer is as dispersive as its input; namely, $\operatorname { V a r } ( y _ { j } ^ { \ell } ) = \operatorname { V a r } ( y _ { i } ^ { \ell - 1 } )$

We first introduce the following results.

Lemma 1.3 If X and $Y$ are two independent random variables and $\mathbb { E } [ ( X ) ] = \mathbb { E } [ ( Y ) ] = 0$ , then $\operatorname { V a r } ( X Y ) = \operatorname { V a r } ( X ) \operatorname { V a r } ( Y )$

Proof:

$$
\begin{array}{r l} & {\mathrm{Var} (X Y) = \mathbb {E} [ (X Y) ^ {2} ] - \mathbb {E} [ X Y ] ^ {2} = \mathbb {E} [ X ^ {2} Y ^ {2} ] - (\mathbb {E} [ X ] \mathbb {E} [ Y ]) ^ {2}} \\ & {\qquad = \mathbb {E} [ X ^ {2} ] \mathbb {E} [ Y ^ {2} ] = (\mathbb {E} [ X ^ {2} ] - \mathbb {E} [ X ] ^ {2}) (\mathbb {E} [ Y ^ {2} ] - \mathbb {E} [ Y ] ^ {2})} \\ & {\qquad = \mathrm{Var} (X) \mathrm{Var} (Y).} \end{array}
$$

Besides, let f be a diferentiable function. Then the linear approximation of $f ( x )$ at $x = \mathbb { E } [ X ]$ gives

$$
f (x) \approx f (\mathbb {E} [ X ]) + f ^ {\prime} (\mathbb {E} [ X ]) (x - \mathbb {E} [ X ]).
$$

Replacing the variable x by the random variable X leads to

$$
f (X) \approx f (\mathbb {E} [ X ]) + f ^ {\prime} (\mathbb {E} [ X ]) (X - \mathbb {E} [ X ]),
$$

so

$$
\operatorname{Var} (f (X)) \approx \operatorname{Var} \left(f ^ {\prime} (\mathbb {E} [ X ]) (X - \mathbb {E} [ X ])\right) = f ^ {\prime} (\mathbb {E} [ X ]) ^ {2} \operatorname{Var} (X).\tag{1.36}
$$

Then it follows (1.35) that

$$
\begin{array}{r l} & {\mathrm{Var} (y _ {j} ^ {\ell}) \approx (\sigma_ {j} ^ {\ell}) ^ {\prime} \left(\sum_ {i = 1} ^ {M _ {\ell - 1}} \mathbb {E} [ w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1} ]\right) ^ {2} \cdot \mathrm{Var} \left(\sum_ {i = 1} ^ {M _ {\ell - 1}} w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1}\right)} \\ & {\quad = (\sigma_ {j} ^ {\ell}) ^ {\prime} \left(\sum_ {i = 1} ^ {M _ {\ell - 1}} \mathbb {E} [ w _ {j i} ^ {\ell} ] \mathbb {E} [ y _ {i} ^ {\ell - 1} ]\right) ^ {2} \cdot \sum_ {i = 1} ^ {M _ {\ell - 1}} \mathrm{Var} \left(w _ {j i} ^ {\ell} y _ {i} ^ {\ell - 1}\right)} \\ & {\quad = \left((\sigma_ {j} ^ {\ell}) ^ {\prime} (0)\right) ^ {2} \cdot \sum_ {i = 1} ^ {M _ {\ell - 1}} \mathrm{Var} \left(w _ {j i} ^ {\ell}\right) \mathrm{Var} \left(y _ {i} ^ {\ell - 1}\right)} \\ & {\quad = M _ {\ell - 1} \left((\sigma_ {j} ^ {\ell}) ^ {\prime} (0)\right) ^ {2} \mathrm{Var} \left(w _ {j i} ^ {\ell}\right) \mathrm{Var} \left(y _ {i} ^ {\ell - 1}\right),} \end{array}
$$

where Lemma 1.3 and (1.36) is used. Enforcing $\operatorname { V a r } ( y _ { j } ^ { \ell } ) = \operatorname { V a r } ( y _ { i } ^ { \ell - 1 } )$ leads to

$$
\operatorname{Var} \left(w _ {j i} ^ {\ell}\right) = \frac {1}{M _ {\ell - 1} \left((\sigma_ {j} ^ {\ell}) ^ {\prime} (0)\right) ^ {2}}.\tag{1.37}
$$

Consequently, we encounter two useful cases:

1. If $w _ { j i } ^ { \ell }$ are drawn from a normal distribution, then $\begin{array} { r } { w _ { j i } ^ { \ell } \sim \mathcal N \left( 0 , \frac { 1 } { M _ { \ell - 1 } \left( ( \sigma _ { j } ^ { \ell } ) ^ { \prime } ( 0 ) \right) ^ { 2 } } \right) } \end{array}$

2. If $w _ { j i } ^ { \ell }$ are drawn from a uniform distribution. Since $U [ - a , a ]$ has variance $a ^ { 2 } / 3$ , we have w<sup>ℓ</sup><sub>ji</sub> ∼ U √<sub>3</sub> √<sub>3</sub> √<sub>Mℓ−1(σ</sub>ℓ<sub>j )</sub>′<sub>(0)</sub> √<sub>Mℓ−1(σ</sub>ℓ<sub>j )</sub>′<sub>(0)</sub>

## Back propagation point of view

Another strategy is derived in the view of back propagation, which is also called the Xavier initialization [6]. It is expected that

$$
\operatorname{Var} \left(\frac {\partial f (x ; \theta)}{\partial w _ {i j} ^ {\ell - 1}}\right) = \operatorname{Var} \left(\frac {\partial f (x ; \theta)}{\partial w _ {i j} ^ {\ell}}\right).\tag{1.38}
$$

We assume that all weights in $\{ a _ { i } , w _ { j i } ^ { \ell } \} _ { i , j , \ell }$ are independent and identically distributed random variables with zero mean. Also, we assume all activation functions are identity, then the relations

(1.22)-(1.25) read

$$
p ^ {L + 1} = 1, \quad p _ {i} ^ {L} = p ^ {L + 1} a _ {i},\tag{1.39}
$$

$$
p _ {i} ^ {\ell - 1} = \sum_ {j = 1} ^ {M _ {\ell}} p _ {j} ^ {\ell} w _ {j i} ^ {\ell}, \quad \text { for } \ell = L, L - 1, \dots , 2.\tag{1.40}
$$

By back recursion, $p _ { j } ^ { \ell }$ is determined by $\{ w _ { j i } ^ { \ell + 1 } \} _ { i , j } \cup \cdot \cdot \cdot \cup \{ w _ { j i } ^ { L } \} _ { i , j } \cup \{ a _ { i } \}$ <sub>i</sub> but independent of $\{ w _ { j i } ^ { \ell } \} _ { i , j }$ and $\{ y _ { i } ^ { \ell - 1 } \} _ { i }$ <sub>i</sub>. Then we have

$$
\mathbb {E} \left[ \sum_ {j = 1} ^ {M _ {\ell}} p _ {j} ^ {\ell} w _ {j i} ^ {\ell} \right] = \sum_ {j = 1} ^ {M _ {\ell}} \mathbb {E} [ p _ {j} ^ {\ell} ] \mathbb {E} [ w _ {j i} ^ {\ell} ] = 0,
$$

where we used $\mathbb { E } [ w _ { j i } ^ { \ell } ] = 0$ . By (1.40), $\mathbb { E } [ p _ { i } ^ { \ell - 1 } ] = 0$ , and similarly, $\mathbb { E } [ p _ { i } ^ { \ell } ] = 0$

Moreover, since $\begin{array} { r } { y _ { j } ^ { \ell } = \sum _ { i = 1 } ^ { M _ { \ell - 1 } } w _ { j i } ^ { \ell } y _ { i } ^ { \ell - 1 } } \end{array}$ and $w _ { j i } ^ { \ell }$ is independent of $y _ { i } ^ { \ell - 1 }$ 2

$$
\mathbb {E} [ y _ {j} ^ {\ell} ] = \sum_ {i = 1} ^ {M _ {\ell - 1}} \mathbb {E} [ w _ {j i} ^ {\ell} ] \mathbb {E} [ y _ {i} ^ {\ell - 1} ] = 0.
$$

Similarly, $\mathbb { E } [ y _ { i } ^ { \ell - 1 } ] = \mathbb { E } [ y _ { i } ^ { \ell - 2 } ] = 0 .$

Now for $\ell \geq 2 .$ , by (1.24)-(1.26), the goal (1.38) requires

$$
\mathrm{Var} (p _ {j} ^ {\ell - 1} y _ {i} ^ {\ell - 2}) = \mathrm{Var} (p _ {j} ^ {\ell} y _ {i} ^ {\ell - 1}).
$$

Using Lemma 1.3 leads to

$$
\operatorname{Var} (p _ {j} ^ {\ell - 1}) \operatorname{Var} (y _ {i} ^ {\ell - 2}) = \operatorname{Var} (p _ {j} ^ {\ell}) \operatorname{Var} (y _ {i} ^ {\ell - 1}).
$$

As discussed above, we also expect $\mathrm { V a r } ( y _ { i } ^ { \ell - 2 } ) = \mathrm { V a r } ( y _ { i } ^ { \ell - 1 } )$ , therefore it must hold that

$$
\operatorname{Var} (p _ {j} ^ {\ell - 1}) = \operatorname{Var} (p _ {j} ^ {\ell}).\tag{1.41}
$$

Applying the variance to (1.40), using the independence and Lemma 1.3, we obtain

$$
\operatorname{Var} (p _ {i} ^ {\ell - 1}) = \sum_ {j = 1} ^ {M _ {\ell}} \operatorname{Var} (p _ {j} ^ {\ell}) \operatorname{Var} (w _ {j i} ^ {\ell}) = M _ {\ell} \operatorname{Var} (p _ {j} ^ {\ell}) \operatorname{Var} (w _ {j i} ^ {\ell}),\tag{1.42}
$$

where we used the fact that $\{ p _ { j } ^ { \ell } \} _ { j }$ are identically distributed. Combining (1.41) and (1.42), we have

$$
\mathrm{Var} (w _ {j i} ^ {\ell}) = \frac {1}{M _ {\ell}}.\tag{1.43}
$$

The relation (1.43) means the variance of $w _ { j i } ^ { \ell }$ is inversely proportional to the width of ℓth layer. Comparatively, under the assumption of the identity activation function, the relation (1.37) becomes

$$
\mathrm{Var} (w _ {j i} ^ {\ell}) = \frac {1}{M _ {\ell - 1}},\tag{1.44}
$$

which means the variance of $w _ { j i } ^ { \ell }$ is inversely proportional to the width of $\ell - 1$ 1th layer.

Now, (1.43) and (1.44) are satisfied simultaneously only in the case $M _ { \ell } = M _ { \ell - 1 }$ , i.e., when the width is the same in any two consecutive layers. Since this condition is too restrictive, a lucrative compromise is to take the harmonic mean of the two, the case in which

$$
\mathrm{Var} (w _ {j i} ^ {\ell}) = \frac {2}{M _ {\ell} + M _ {\ell - 1}}.
$$

Again, we emphasize two cases of practical importance

1. If $w _ { j i } ^ { \ell }$ are drawn from a normal distribution, then $\begin{array} { r } { w _ { j i } ^ { \ell } \sim \mathcal N \left( 0 , \frac { 2 } { M _ { \ell } + M _ { \ell - 1 } } \right) } \end{array}$

2. If $w _ { j i } ^ { \ell }$ are drawn from a uniform distribution, have $\begin{array} { r } { w _ { j i } ^ { \ell } \sim U \left[ - \frac { \sqrt { 6 } } { \sqrt { M _ { \ell } + M _ { \ell - 1 } } } , \frac { \sqrt { 6 } } { \sqrt { M _ { \ell } + M _ { \ell - 1 } } } \right] . } \end{array}$

## 1.2.6 Continuum number of neurons and inputs

For very wide neural networks, the number of neurons in each hidden layer is seen as almost infinity. So the infinite analogy of a very wide neural network has continuum number of neurons, and it can be represented as integrals rather than finite sums of neurons. Similarly, neural networks with a huge number of inputs also have infinite analogies that have continuum number of inputs.

We first consider the two-layer neural network mapping from $\mathbb { R } ^ { d }$ to R given by

$$
f (x; \theta) = \sum_ {j = 1} ^ {M} a _ {j} \sigma \left(w _ {j 1} x _ {1} + \dots + w _ {j d} x _ {d} + b _ {j}\right),\tag{1.45}
$$

where $\sigma$ is some activation function, $w _ { j i }$ is the weight between the ith input and the jth neuron, $a _ { j }$ is the weight between the jth neuron and the output, and $b _ { j }$ denotes the bias for the jth neuron in the hidden layer. Here we let the activation function of the output layer be the identity and omit the bias in the output layer.

Now, suppose the width M is infinitely large. Then we replace the finite number of neurons in the hidden layer, by a continuous infinite number of hidden neurons, which are parametrized by $s \in [ 0 , 1 ]$ . Hence, the index $j$ is replaced by the real number s. Consequently, $w _ { j i } , \ b _ { j }$ become functions $w _ { i } ( s ) , b ( s )$ , respectively, while the weights $a _ { j }$ are replaced by some measure $a ( s ) \mathrm { d } s$ . The summation for $j$ is transformed into an integral, by which the network is formulated as

$$
f (x; \theta^ {\prime}) = \int_ {0} ^ {1} \sigma \left(w _ {1} (s) x _ {1} + \dots + w _ {d} (s) x _ {d} + b (s)\right) a (s) \mathrm{d} s.\tag{1.46}
$$

Here $\theta ^ { \prime }$ denotes the set of free parameter functions $w _ { i } ( s ) , a ( s )$ and $b ( s )$

Next, we consider the network (1.46) by further supposing d is infinitely large. Therefore, the finite number of inputs are replaced by a continuous infinite number of inputs, which are parametrized by $t \in [ 0 , 1 ]$ . Namely, the indices $1 , \ldots , d$ are replaced by the real number t, and the input vector $\boldsymbol { x } = ( x _ { 1 } , \dots , x _ { d } )$ becomes a function $x ( t )$ . Correspondingly, the functions $w _ { i } ( s )$ are further transformed into a bivariate functions $w ( s , t ) \mathrm { d } t$ . The summation $w _ { 1 } ( s ) x _ { 1 } + \cdot \cdot \cdot + w _ { d } ( s ) x _ { d }$ is also transformed into an integral. To sum up, the network is formulated as

$$
f (x; \theta^ {\prime \prime}) = \int_ {0} ^ {1} \sigma \left(\int_ {0} ^ {1} w (s, t) x (t) \mathrm{d} t + b (s)\right) a (s) \mathrm{d} s.\tag{1.47}
$$

Here $\theta ^ { \prime \prime } = \{ w ( s , t ) , a ( s ) , b ( s ) \}$

Similar argument can be applied to deep neural networks. For example, we consider the following network with depth $L + 1$ and width M in every layer mapping $\mathbb { R } ^ { d }$ to $\mathbb { R } ^ { d ^ { \prime } }$

$$
f (x) = W ^ {L + 1} \sigma_ {L} (W ^ {L} \sigma_ {L - 1} (\dots \sigma_ {1} (W ^ {1} x + b ^ {1}) \dots) + b ^ {L}) + b ^ {L + 1},\tag{1.48}
$$

where $W ^ { L + 1 } \ \in \ \mathbb R ^ { d ^ { \prime } \times M } , \ W ^ { \ell } \ \in \ \mathbb R ^ { M \times M } \ ( 2 \ \leq \ \ell \leq \ L ) , \ W ^ { 1 } \ \in \ \mathbb R ^ { M \times d } , \ b ^ { L + 1 } \ \in \ \mathbb R ^ { d ^ { \prime } \times 1 } , \ b ^ { \ell } \ \in \ \mathbb R ^ { M \times 1 }$ $( 1 \leq \ell \leq L )$ are weights and biases. Suppose $M , d , d ^ { \prime }$ are infinitely large, then (1.48) is transformed into the continuum formulation

$$
\begin{array}{r l} & f [ x ] (s) = \int_ {0} ^ {1} w ^ {L + 1} (s, t) y ^ {L} (t) \mathrm{d} t + b ^ {L + 1} (s), \\ & y ^ {\ell} (s) = \sigma_ {\ell} \left(\int_ {0} ^ {1} w ^ {\ell} (s, t) y ^ {\ell - 1} (t) \mathrm{d} t + b ^ {\ell} (s)\right), \quad \ell = 2, \ldots , L, \\ & y ^ {1} (s) = \sigma_ {1} \left(\int_ {0} ^ {1} w ^ {1} (s, t) x (t) \mathrm{d} t + b ^ {1} (s)\right), \end{array}\tag{1.49}
$$

where $w ^ { \ell } ( s , t )$ is the continuum analogy to the weight matrix $W ^ { \ell }$ . Due to infinite continuum of $d ^ { \prime }$ the mapping f in (1.49) is an operator mapping functions to functions, instead of mapping functions to scalars or vectors. We also note that f is actually a multiple integral with $L + 1$ single integrals over [0, 1].

Conversely, if we discretize the preceding integrals by quadrature rules, then these continuum forms will return to the standard neural networks. For example, we use the rectangle rule to rewrite the integrals in (1.47). Specifically, we set quadrature nodes

$$
t _ {i} = (i - \frac {1}{2}) / d, i = 1, \ldots , d
$$

for variable t and

$$
s _ {j} = (j - \frac {1}{2}) / M, \quad j = 1, \ldots , M
$$

for variable s. Then (1.47) is approximately

$$
\frac {1}{M} \sum_ {j = 1} ^ {M} a (s _ {j}) \sigma \left(\frac {1}{d} \sum_ {i = 1} ^ {d} w (s _ {j}, t _ {i}) x (t _ {i}) + b (s _ {j})\right).
$$

Then $a ( s _ { j } ) / M$ is equivalent to $a _ { j } , w ( s _ { j } , t _ { i } ) / d$ is equivalent to $w _ { j i } , b ( s _ { j } )$ is equivalent to $b _ { j }$ and $x ( t _ { i } )$ is equivalent to $x _ { i }$ in (1.45).

## 1.3 Convolutional Neural Networks

Convolutional neural networks (CNNs) have special architectures diferent from fully-connected ones. They have excellent performance in image processing due to their adaptability to a 2-D grid like topology. CNN is a biologically inspired piece of AI, whose design is based on neuroscientific principles, and successfully applied to pattern recognition.

## 1.3.1 Cross-correlation

Cross-correlation is the fundamental ingredient of the convolutional layer involved in CNNs. The cross-correlation operator can be applied to finite vectors/matrices/high-dimensional tensors or infinite sequences. For example, let

$$
x = (\ldots , x _ {- 2}, x _ {- 1}, x _ {0}, x _ {1}, x _ {2}, \ldots)\tag{1.50}
$$

be a sequence. Given a vector $k = \left( k _ { 0 } , k _ { 1 } , \ldots , k _ { n - 1 } \right)$ of length $n ,$ then the cross-correlation operation (denoted by ∗) on x with respect to k is defined by

$$
y = x * k = (\ldots , y _ {- 2}, y _ {- 1}, y _ {0}, y _ {1}, y _ {2}, \ldots),\tag{1.51}
$$

with

$$
y _ {j} = \sum_ {i = 0} ^ {n - 1} k _ {i} x _ {j + i}.\tag{1.52}
$$

Here k is called a kernel. Clearly, the cross-correlation operator mapping x to y is a linear operator. Note that the element $y _ { j }$ of y only depends on the elements $x _ { j } , x _ { j + 1 } , \dotsc , x _ { j + n - 1 }$ of x, and the latter is said to be the receptive field of $y _ { j }$

Similarly, cross-correlation operator can be applied to vectors in $\mathbb { R } ^ { d }$ . Given the kernel $k =$ $( k _ { 1 } , k _ { 2 } , \ldots , k _ { n } )$ , then for any column vectors $x = ( x _ { 1 } \ x _ { 2 } \ \hdots \ x _ { d } ) ^ { \top } \in \mathbb { R } ^ { d }$ with $d \geq n .$ , the result is

$$
y = x * k = (y _ {1} y _ {2} \dots y _ {d - n + 1}) ^ {\top},\tag{1.53}
$$

with

$$
y _ {j} = \sum_ {i = 1} ^ {n} k _ {i} x _ {j - 1 + i}.\tag{1.54}
$$

The cross-correlation can be represented by the graph in Figure 1.11, where an input vector of length 6 is mapped to a vector of length 4 using a kernel of length 3. It can be seen that cross-correlation from one layer to another layer has shared weights and sparse interactions, which is diferent from the fully-connected architecture. Also, the operation in Figure 1.11 can be formulated as matrixvector multiplication; namely, $x * k = K x$ , where

$$
K = \left( \begin{array}{c c c c c c} k _ {1} & k _ {2} & k _ {3} & 0 & 0 & 0 \\ 0 & k _ {1} & k _ {2} & k _ {3} & 0 & 0 \\ 0 & 0 & k _ {1} & k _ {2} & k _ {3} & 0 \\ 0 & 0 & 0 & k _ {1} & k _ {2} & k _ {3} \end{array} \right).
$$

Clearly, K is a sparse structured matrix with shared non-zero entries $\boldsymbol { k } _ { 1 } , \boldsymbol { k } _ { 2 } , \boldsymbol { k } _ { 3 }$

In one step of cross-correlation, we observe that the width of the input layer x will be reduced by $n - 1$ in the output layer $y .$ To prevent the width from diminishing, one can pad x before doing cross-correlation. For example,

• pad top: $x = ( x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } ) ^ { \top }  x _ { \mathrm { p a d } } = ( x _ { \mathrm { T } } \ x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } ) ^ { \top }$

• pad bottom: $x = ( x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } ) ^ { \top }  x _ { \mathrm { p a d } } = ( x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } \ x _ { \mathrm { B } } ) ^ { \top }$

• pad two ends: $x = ( x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } ) ^ { \top }  x _ { \mathrm { p a d } } = ( x _ { \mathrm { T } } \ x _ { 1 } \ x _ { 2 } \ \dots \ x _ { d } \ x _ { \mathrm { B } } ) ^ { \top }$

where $x _ { \mathrm { T } }$ and x<sub>B</sub> can be chosen as

• pad by zeros: $x _ { \mathrm { T } } = x _ { \mathrm { B } } = 0 ;$

• pad by averages: $\begin{array} { r } { x _ { \mathrm { T } } = x _ { \mathrm { B } } = \frac { 1 } { d } \sum _ { i = 1 } ^ { d } x _ { i } ; } \end{array}$

• pad periodically: $x _ { \mathrm { T } } = x _ { d } , x _ { \mathrm { B } } = x _ { 1 }$ ;

![](images/ff2956517710abc71b9f129ecb3debfdca5a1b990b89e156f1f4ed631cf6cf5b.jpg)  
Figure 1.11: Cross correlation operation applied to vectors.

After padding, x is lengthened by a few elements, then the cross-correlation applied to the padded $x _ { \mathrm { p a d } }$ may preserve the length of x. The padding operation can also be formulated as matrix-vector product. For example, the two-end periodic padding can be written as

$$
x _ {\mathrm{pad}} = P x,
$$

where

$$
P = \left( \begin{array}{c c c c c} 0 & 0 & \ldots & 0 & 1 \\ 1 & 0 & \ldots & 0 & 0 \\ 0 & 1 & \ldots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \ldots & 1 & 0 \\ 0 & 0 & \ldots & 0 & 1 \\ 1 & 0 & \ldots & 0 & 0 \end{array} \right).
$$

The cross-correlation can be understood as the kernel k sliding from top to bottom on the vector $x ,$ and each time the inner product of k and part of x is used as an element of the output vector. In the definition (1.53)-(1.54), the kernel slides one position at a time, so we say the stride of this cross-correlation is 1. Similarly, we can define the cross-correlation with general stride $s \in \mathbb { Z } ^ { + }$ by

$$
y = x * k := \left(y _ {1} y _ {2} \dots y _ {(d - n) / s + 1}\right) ^ {\top},\tag{1.55}
$$

with

$$
y _ {j} = \sum_ {i = 1} ^ {n} k _ {i} x _ {(j - 1) s + i}.\tag{1.56}
$$

Correspondingly, the kernel matrix K has non-zero blocks shifted in s elements row by row. For

example, when $n = 3 , s = 2$ , the kernel matrix is given by

$$
K = \left( \begin{array}{c c c c c c c c c} k _ {1} & k _ {2} & k _ {3} & 0 & 0 & \ldots & 0 & 0 & 0 \\ 0 & 0 & k _ {1} & k _ {2} & k _ {3} & \ldots & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & k _ {1} & \ldots & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & 0 & 0 & \ldots & k _ {3} & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & \ldots & k _ {1} & k _ {2} & k _ {3} \end{array} \right).
$$

The preceding concepts can be extended for multi-dimensional inputs, such as matrices and high-dimensional tensors. For example, given a 2-D kernel $\boldsymbol { k } = ( k _ { i j } ) \in \mathbb { R } ^ { s _ { 1 } \times s _ { 2 } }$ , then for any 2-D input $x = ( x _ { i j } ) \in \mathbb { R } ^ { m _ { 1 } \times m _ { 2 } }$ , the cross-correlation with stride 1 is defined by

$$
y = x * k = (y _ {p q}) \in \mathbb {R} ^ {(m _ {1} - s _ {1} + 1) \times (m _ {2} - s _ {2} + 1)},\tag{1.57}
$$

with

$$
y _ {p q} = \sum_ {i = 1} ^ {s _ {1}} \sum_ {j = 1} ^ {s _ {2}} k _ {i j} x _ {p + i - 1, q + j - 1}, \quad 1 \leq p \leq m _ {1} - s _ {1} + 1, 1 \leq q \leq m _ {2} - s _ {2} + 1.\tag{1.58}
$$

If we write $k = [ k _ { 1 } ~ \dots ~ k _ { s _ { 2 } } ]$ and $x = [ x _ { 1 } ~ \ldots ~ x _ { m _ { 2 } } ]$ columnwise, then it is clear that

$$
y = [ y _ {1} \dots y _ {m _ {2} - s _ {2} + 1} ]\tag{1.59}
$$

with

$$
y _ {q} = \sum_ {j = 1} ^ {s _ {2}} x _ {q + j - 1} * k _ {j}, \quad 1 \leq q \leq m _ {2} - s _ {2} + 1.\tag{1.60}
$$

${ \mathrm { S o } } ,$ the 2-D cross-correlation can be seen as applying 1-D cross-correlation to the matrix with each column being an element.

In multi-dimensional cases, we can also use padding before cross-correlation to preserve the output size. That is, we insert extra elements before or after the input in every dimension. Also, we can use a larger stride in each dimension, that is, the number of steps the kernel slides each time.

## 1.3.2 Pooling

Similar to the cross-correlation, pooling operation is also commonly used in building CNNs. The process of pooling is very like the cross-correlation, which uses a “pooling kernel” to slide on the input and determine one element of the output at every step. More frequently, the “pooling kernel” is called $\mathrm { ~ a ~ } f l t t r$ . For example, let

$$
x = (\ldots , x _ {- 2}, x _ {- 1}, x _ {0}, x _ {1}, x _ {2}, \ldots)
$$

be a sequence. Then with filter size $n \geq 2$ and stride $s = 1$ , the result of pooling is a sequence

$$
y = \mathcal {P} (x) = (\ldots , y _ {- 2}, y _ {- 1}, y _ {0}, y _ {1}, y _ {2}, \ldots),
$$

with

• max-pooling

$$
y _ {j} = \max \{x _ {j}, x _ {j + 1}, \ldots , x _ {j + n - 1} \};\tag{1.61}
$$

• min-pooling

$$
y _ {j} = \min \{x _ {j}, x _ {j + 1}, \ldots , x _ {j + n - 1} \};\tag{1.62}
$$

• average-pooling

$$
y _ {j} = \frac {1}{n} \sum_ {i = 0} ^ {n - 1} x _ {j + i}.\tag{1.63}
$$

Clearly, average-pooling is equivalent to the cross-correlation with all kernel elements being $1 / n$ However, max-pooling and min-pooling are not linear operators.

Similarly, pooling can be applied to vectors in $\mathbb { R } ^ { d }$ . For any column vectors $x = ( x _ { 1 } x _ { 2 } \dots x _ { d } ) ^ { \top } \in$ $\mathbb { R } ^ { d }$ with $d \geq n$ , the result of pooling is given by

$$
y = \mathcal {P} (x) = \left(y _ {1} y _ {2} \dots y _ {d - n + 1}\right) ^ {\top},\tag{1.64}
$$

with formulae (1.61)-(1.63). Pooling also shares the concepts (receptive field, padding and stride) and multi-dimensional extension introduced in Section 1.3.1 in a similar way.

## 1.3.3 Architecture of convolutional neural networks

CNNs are neural networks that contain convolutional layers. They usually also contain several pooling layers and fully connected layers. Here We introduce the layers with one-dimensional inputs as an example. First, the convolutional layer is formed as follows:

$$
y = \sigma (x * k + b),\tag{1.65}
$$

where $\sigma$ is some activation function; k is the kernel; b is the bias that has the same size of $x * k$ In many practical situations, all components of b are the same; namely, b can be viewed as a scalar broadcasted to $x * k$ . We can also pad x before doing cross-correlation, so the convolutional layer $x \mapsto y$ is operated by

$$
y = \sigma (x _ {\mathrm{pad}} * k + b).\tag{1.66}
$$

The components of k and b are the free parameters to be trained.

Similarly, the pooling layer can be formulated as follows:

$$
y = \sigma (\mathcal {P} (x) + b).\tag{1.67}
$$

However, in most situations of pooling, σ is taken as the identity function, and b is fixed as 0. So, the pooling layer just consists of a pooling operation. Here no free parameters are involved.

## 1.3.4 Forward and back propagation

Since the architecture of CNNs is very flexible in practical use, here we only discuss the propagation through one or two specific layers instead of an entire CNN.

## Forward propagation

Considering the convolutional layer (1.65) in d dimensions, we suppose that the size of the kernel k is $n _ { 1 } \times \cdots \times n _ { d }$ , the stride for every dimension is $s _ { i } ~ ( i = 1 , \ldots , d )$ , and the size of the input x is $( s _ { 1 } t _ { 1 } + n _ { 1 } ) \times \cdots \times ( s _ { d } t _ { d } + n _ { d } )$ (so that the kernel can slide on x for $t _ { i } + 1$ steps in the i-th dimension). Then the kernel will slide on x for totally $\Pi _ { i = 1 } ^ { d } ( t _ { i } + 1 )$ steps, each of which costs $\Pi _ { i = 1 } ^ { d } n _ { i }$ times of multiplication and $\Pi _ { i = 1 } ^ { d } n _ { i } - 1$ times of addition. Moreover, we assume that $\sigma ( t )$ costs $O ( 1 )$ operations for any scalar t. Then the complexity of (1.65) is about

![](images/9789b0c5ee085d4a0fad0d74979efa39e8b819e8e9c2781432198aa0cf124126.jpg)  
Figure 1.12: A neural network forward passing through one convolution layer and one fullyconnected layer.

$$
2 \prod_ {i = 1} ^ {d} (t _ {i} + 1) \prod_ {i = 1} ^ {d} n _ {i} \sim 2 \prod_ {i = 1} ^ {d} t _ {i} \prod_ {i = 1} ^ {d} n _ {i}\tag{1.68}
$$

when $t _ { i }$ are suficiently large and minor terms are omitted.

Now consider the pooling layer (1.67). The size of the pooling kernel, the stride and the size of the input are given as above. First, for the average-pooling, we do not have to do multiplication in every step of the tensor inner product, and only need to sum all elements of the receptive field up. By similar argument, the complexity of (1.67) with average-pooling is about

$$
\prod_ {i = 1} ^ {d} (t _ {i} + 1) \prod_ {i = 1} ^ {d} n _ {i} \sim \prod_ {i = 1} ^ {d} t _ {i} \prod_ {i = 1} ^ {d} n _ {i}.\tag{1.69}
$$

The similar argument applies to the max/min-pooling. The only diference is that one needs to sort elements in every step of the tensor inner product instead of doing addition, and the complexity depends on the algorithm used.

## Back propagation

The back propagation through the convolutional layer is slightly diferent from that of the fullyconnected layer given in Section 1.2.3 due to parameter sharing. Consider the following three-layer architecture with one 1-D convolution layer and one fully-connected layer (Figure 1.12). Here the stride is 1. We Denote the final output by z and the output of every hidden layer by $y _ { i }$ $( i = 1 , \dots , M )$ . Also, we denote the kernel size by n (In the figure we specify $n = 3 ,$ but we consider the general case), so $M = d - n + 1$ . Then the neural network can be written layer-wise as

$$
z = \sigma_ {2} (q), \quad q = \sum_ {i = 1} ^ {M} w _ {i} y _ {i} + c\tag{1.70}
$$

$$
y _ {i} = \sigma_ {1} (q _ {i}), \quad q _ {i} = \sum_ {j = 1} ^ {n} k _ {j} x _ {i + j - 1} + b _ {i}, \quad \text { for } i = 1, \dots , M,\tag{1.71}
$$

Here, $\{ w _ { i } , b _ { i } \} _ { i = 1 , \dots , M } , \ \{ k _ { j } \} _ { j = 1 , \dots , n }$ and c are given network parameters.

First, we need to do one round of forward propagation (1.70)-(1.71), obtaining $\{ q _ { i } , y _ { i } \} _ { i = 1 , \dots , M }$ and $q , z$ . Then, by the chain rule, we can compute

$$
\frac {\partial z}{\partial w _ {i}} = \frac {\mathrm{d} z}{\mathrm{d} q} \frac {\partial q}{\partial w _ {i}} = \sigma_ {2} ^ {\prime} (q) y _ {i},\tag{1.72}
$$

$$
\frac {\partial z}{\partial y _ {i}} = \frac {\mathrm{d} z}{\mathrm{d} q} \frac {\partial q}{\partial y _ {i}} = \sigma_ {2} ^ {\prime} (q) w _ {i},\tag{1.73}
$$

for all $i = 1 , \ldots , M$ . Next, we have

$$
\frac {\partial z}{\partial k _ {j}} = \sum_ {i = 1} ^ {M} \frac {\partial z}{\partial y _ {i}} \frac {\partial y _ {i}}{\partial k _ {j}} = \sum_ {i = 1} ^ {M} \frac {\partial z}{\partial y _ {i}} \frac {\mathrm{d} y _ {i}}{\mathrm{d} q _ {i}} \frac {\partial q _ {i}}{\partial k _ {j}} = \sum_ {i = 1} ^ {M} \frac {\partial z}{\partial y _ {i}} \sigma_ {1} ^ {\prime} (q _ {i}) x _ {i + j - 1}\tag{1.74}
$$

for all $j = 1 , \dotsc , n$ , where $\frac { \partial z } { \partial y _ { i } }$ is obtained by (1.73). This is the formula to compute the derivative of z with respect the kernel weights $\{ k _ { j } \} _ { j = 1 } ^ { n }$

In more general cases, given a convolutional layer $y = \sigma ( x * k + b )$ with input $\boldsymbol { x } = [ x _ { 1 } , \dots , x _ { d } ]$ 1-D kerne $k = [ k _ { 1 } , \ldots , k _ { n } ]$ with stride 1 and bias $\left[ b _ { 1 } , \ldots , b _ { d - n + 1 } \right]$ . Let ψ be a general neural network from $\mathbb { R } ^ { d - n + 1 }$ to R. We can formulate the derivatives of the network $\phi ( x ) : = \psi ( y ) = \psi ( \sigma ( x * k + b ) )$ with respect to the kernel, which is given by

$$
\begin{array}{c} \frac {\partial \phi}{\partial k _ {j}} = \sum_ {i = 1} ^ {d - n + 1} \frac {\partial \psi}{\partial y _ {i}} \frac {\partial y _ {i}}{\partial k _ {j}} = \sum_ {i = 1} ^ {M} \frac {\partial \psi}{\partial y _ {i}} \frac {\mathrm{d} y _ {i}}{\mathrm{d} q _ {i}} \frac {\partial q _ {i}}{\partial k _ {j}} = \sum_ {i = 1} ^ {d - n + 1} \frac {\partial \psi}{\partial y _ {i}} \sigma^ {\prime} (q _ {i}) x _ {i + j - 1} \\ = (\nabla_ {y} \psi) ^ {\top} \left(\sigma^ {\prime} (x * k + b) \odot x _ {j: j + d - n}\right). \end{array}\tag{1.75}
$$

The back propagation through the pooling layer is easier to handle since no free parameters exist in the layer. We only need to focus on the derivative with respect to the input. Specifically, let us consider the pooling layer (1.67) with b fixed as 0. We assume that $\mathcal { P }$ has kernel size n and stride 1, $x \in \mathbb { R } ^ { d }$ , and therefore $y \in \mathbb { R } ^ { d - n + 1 }$ . Denoting $q = [ q _ { 1 } , \dotsc , q _ { d - n + 1 } ] = \mathcal { P } ( x )$ , then for any component $y _ { j }$ of y and any component $x _ { k }$ of x, we have

$$
\frac {\partial y _ {j}}{\partial x _ {k}} = \sigma^ {\prime} (q _ {j}) \frac {\partial q _ {j}}{\partial x _ {k}}.\tag{1.76}
$$

For the average-pooling, it satisfies that

$$
\frac {\partial q _ {j}}{\partial x _ {k}} = \left\{ \begin{array}{l l} 1 / n, & k \in \{j, \ldots , j + n - 1 \}, \\ 0, & \text { others }. \end{array} \right.\tag{1.77}
$$

And for the max-pooling, it satisfies almost everywhere that

$$
\frac {\partial q _ {j}}{\partial x _ {k}} = \left\{ \begin{array}{l l} 1, & k \in \{j, \ldots , j + n - 1 \} \text {and} x _ {k} \geq x _ {j}, \ldots , x _ {k} \geq x _ {j + n - 1}, \\ 0, & \text {others.} \end{array} \right.\tag{1.78}
$$

A Similar formula is for the min-pooling.

## 1.3.5 Continuum analogy

We consider the cross-correlation on the infinite sequence x defined by (1.50), obtaining y given in (1.51)-(1.52). Note that x can be analogous to a continuum function $x ( t )$ with $t \in \mathbb { R }$ . And the kernel vector k can be rewritten as an infinite sequence $k = ( \dots , 0 , 0 , k _ { 0 } , k _ { 1 } , \dots , k _ { n - 1 } , 0 , 0 , \dots )$ so it can be analogous to a continuum function $k ( t )$ with compact support. The output y is also analogous to $y ( s )$ with $s \in \mathbb { R }$ . Then the cross-correlation has the continuum analogy

$$
y (s) = \int_ {- \infty} ^ {\infty} x (s + t) k (t) \mathrm{d} t.\tag{1.79}
$$

If we let ${ \hat { x } } ( t ) : = x ( - t )$ and ${ \hat { y } } ( s ) : = y ( - s )$ , then it follows that

$$
\hat {y} (s) = y (- s) = \int_ {- \infty} ^ {\infty} x (- s + t) k (t) \mathrm{d} t = \int_ {- \infty} ^ {\infty} \hat {x} (s - t) k (t) \mathrm{d} t,\tag{1.80}
$$

which is exactly the convolution of the functions $\hat { x }$ and k. This is why we call the network layer of cross-correlation the convolutional layer.

Applying the rectangle rule to discretize (1.79) will lead to the cross-correlation formula (1.51). Specifically, we suppose that the support of $k ( t )$ is [0, 1], then (1.79) becomes

$$
y (s) = \int_ {0} ^ {1} x (s + t) k (t) \mathrm{d} t.\tag{1.81}
$$

We divide $[ 0 , 1 ]$ into n equidistant subintervals and let $h : = 1 / n$ , then the rectangle rule has quadrature nodes $( i + \textstyle { \frac { 1 } { 2 } } ) h , i = 0 , \dots , n - 1$ and uniform weights h. So, for any $j \in \mathbb Z$ 2

$$
y (j h) \approx \sum_ {i = 0} ^ {n - 1} x \left((j + i + \frac {1}{2}) h\right) k \left((i + \frac {1}{2}) h\right) h.\tag{1.82}
$$

Denoting $y _ { j } = y ( j h ) / h , x _ { j + i } = x ( ( j + i + \textstyle \frac 1 2 ) h )$ and $k _ { i } = k ( ( i + \textstyle \frac { 1 } { 2 } ) h )$ , (1.82) formally changes to (1.51).

## 1.3.6 Invariance of max/min-pooling

Max/min-pooling provides a degree of invariance under slight translation. For example, let

$$
x = [ 3, 2, 1, 4, 3, 0, 1, 2, 1, 0, 2, 1 ],\tag{1.83}
$$

then applying max-pooling P with filter size 3 and stride 3, we obtain

$$
y = \mathcal {P} (x) = [ 3, 4, 2, 2 ].\tag{1.84}
$$

On the other hand, we do translation on x by shifting each element one position to the right (and padding the first element by 0), obtaining

$$
x ^ {\prime} = [ 0, 3, 2, 1, 4, 3, 0, 1, 2, 1, 0, 2 ].\tag{1.85}
$$

Then it holds that

$$
y ^ {\prime} := \mathcal {P} (x ^ {\prime}) = [ 3, 4, 2, 2 ].\tag{1.86}
$$

Note that $y = y ^ { \prime } ;$ namely,

$$
\mathcal {P} (x) = \mathcal {P} (\mathcal {T} (x)),\tag{1.87}
$$

where $\tau$ is the shift operator defined above. (1.87) implies that ${ \mathcal { P } } ( x )$ keeps unchanged if shifting x slightly.

Moreover, let $\mathcal { T } _ { s }$ be an operator that shifts all elements of a vector right by s positions (and pads the first s elements by 0). Then for any kernel k with stride s and any vector $x ,$ it is trivial to see that

$$
\mathcal {T} _ {s} (x) * k = \mathcal {T} _ {s} (x * k),\tag{1.88}
$$

except for the first s elements. By this property, it frequently holds that

$$
\mathcal {P} (x * k) = \mathcal {P} (\mathcal {T} (x) * k)\tag{1.89}
$$

for slight translation T . We follow the above example: given $k = [ 3 , 2 , 1 , 0 ]$ , then

$$
x * k = [ 1 4, 1 2, 1 4, 1 8, 1 0, 4, 8, 8, 5 ],\tag{1.90}
$$

and

$$
\mathcal {P} (x * k) = [ 1 4, 1 8, 8 ].\tag{1.91}
$$

On the other hand,

$$
\mathcal {T} (x) * k = \mathcal {T} (x * k) = [ 0, 1 4, 1 2, 1 4, 1 8, 1 0, 4, 8, 8 ],\tag{1.92}
$$

and

$$
\mathcal {P} (\mathcal {T} (x) * k) = [ 1 4, 1 8, 8 ].\tag{1.93}
$$

## 1.4 Exercises

## Exercise 1

(1) Let $\sigma ( t )$ be a nondecreasing and non-constant function defined on $( - \infty , \infty )$ . Suppose that $| \sigma ( t ) | < C , \forall t \in ( - \infty , \infty )$ for some constant $C > 0$ . Show that there exist some $a , b \in \mathbb { R }$ such that $a \sigma ( t ) + b$ is a squashing function.

(2) Give an example of a sigmoidal function $\sigma ( t )$ which satisfies:

(i) σ is a analytic function (i.e. σ has an analytic expression);

(ii) σ is not a squashing function.

(3) Give an example of a squashing function $\sigma ( t )$ which satisfies:

(i) σ is $C ^ { \infty }$ smooth (i.e. σ has continuous derivatives of all orders);

(ii) $\sigma ( t ) = 0$ for all $t \leq 0 .$

## Exercise 2

(1) Can a single perceptron learn the following mapping:

$$
\begin{array}{l l l l} (0, 0, 0) \to 1, & (1, 0, 0) \to 0, & (0, 1, 0) \to 0, & (0, 0, 1) \to 0, \\ (0, 1, 1) \to 1, & (1, 1, 0) \to 0, & (1, 0, 1) \to 0, & (1, 1, 1) \to 1? \end{array}
$$

(2) Draw a multi-perceptron neural network that performs as the previous mapping. State the weights and biases of all perceptrons in the network.

## Exercise 3

(1) Show that the function $f ( x ) = { \mathrm { R e L U } } ( x _ { 1 } x _ { 2 } ) + { \mathrm { R e L U } } ( x _ { 1 } x _ { 3 } ) + { \mathrm { R e L U } } ( x _ { 2 } x _ { 3 } )$ can be written as a three-layer neural network, whose activation function in the output layer is the identity function; namely,

$$
f (x) = a ^ {\top} \sigma_ {2} (W _ {2} \sigma_ {1} (W _ {1} x + b _ {1}) + b _ {2}) + b \quad \text { with } \quad x := (x _ {1} x _ {2} x _ {3}) ^ {\top},
$$

where b is a scalar; $a , b _ { 1 } , b _ { 2 }$ are column vectors; $W _ { 1 } , \ W _ { 2 }$ are matrices; $\sigma _ { 1 } ( \cdot ) , \sigma _ { 2 } ( \cdot )$ are activation functions chosen by yourself.

(2) Repeat (1) with $f ( x ) = \mathrm { R e L U } ( x _ { 1 } + x _ { 2 } ) \mathrm { R e L U } ( x _ { 1 } - x _ { 3 } )$

## Exercise 4

Let $f ( x ; \theta ) = a ^ { \top } \sigma ( W ^ { 2 } \sigma ( W ^ { 1 } x + b ^ { 1 } ) + b ^ { 2 } ) + b .$ where $x , a , b ^ { 1 } , b ^ { 2 } \in \mathbb { R } ^ { 2 } ; W ^ { 1 } , W ^ { 2 } \in \mathbb { R } ^ { 2 \times 2 } ; b \in \mathbb { R }$ ; $\sigma ( t ) = | t |$ . Suppose

$$
x = \binom{2}{0}, a = \binom{1}{- 2}, W ^ {1} = \left( \begin{array}{c c} 2 & - 1 \\ - 1 & 2 \end{array} \right), W ^ {2} = \left( \begin{array}{c c} 3 & 1 \\ 1 & 3 \end{array} \right), b ^ {1} = \binom{1}{1}, b ^ {2} = \binom{- 1}{0}, b = 2.
$$

Compute $\begin{array} { r } { \frac { \partial f } { \partial { x _ { k } } } \ ( k = 1 , 2 ) } \end{array}$ and $\frac { \partial f } { \partial w _ { 1 1 } ^ { 1 } }$ with these values $( x _ { k }$ is the kth component of x and $w _ { 1 1 } ^ { 1 }$ is left top entry of $W ^ { 1 } )$

## Exercise 5

Denote the neural network in Figure by $f ( x ; \theta )$ . Suppose $w _ { i } ^ { j } = 1 , b _ { i } = 1$ for all $i ,$ j; $\sigma _ { i } ( t ) = t ^ { 2 }$ for $1 \leq i \leq 4$ and $\sigma _ { 5 } ( t ) = t .$ Let $x ^ { * } = ( 1 0 - 1 ) ^ { \top }$ be an input vector.

(1) Use forward propagation to compute $f ( x ^ { * } ; \theta )$ ;

(2) Use back propagation to compute $\nabla _ { { \boldsymbol { \theta } } } f ( x ^ { * } ; { \boldsymbol { \theta } } )$ and $\nabla _ { x } f ( x ^ { * } ; \theta )$

## Exercise 6

Consider the learning task

$$
\min _ {\theta} \mathcal {L} (\theta) := \| f (x ^ {*}; \theta) - y ^ {*} \| _ {2} ^ {2},
$$

where $( x ^ { * } , y ^ { * } ) \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d ^ { \prime } }$ is a given data point; $f ( x ; \theta )$ is a fully-connected neural network given by $( 1 . 8 ) ‐ ( 1 . 1 0 )$ with $M _ { \ell } = M$ for $\ell = 1 , \ldots , L + 1 ; \| \cdot \| _ { 2 }$ means the Euclidean norm of vectors. Design an algorithm to compute $\nabla _ { \boldsymbol { \theta } } \mathcal { L }$ that costs complexity $O ( ( L - 1 ) M ^ { 2 } + d M + d ^ { \prime } M )$

## Exercise 7

Suppose $\sigma ( \cdot ) \in C ^ { 1 } ( \mathbb { R } )$

(1) Let f be a two-layer neural network mapping from $\mathbb { R } ^ { d }$ to R given by

$$
f (x; \theta) = \sum_ {j = 1} ^ {M} a _ {j} \sigma (w _ {j 1} x _ {1} + \dots + w _ {j d} x _ {d}).
$$

Write out $\begin{array} { r } { \nabla _ { w _ { 1 } } f ( x ; \theta ) : = \left( \frac { \partial f } { \partial w _ { 1 1 } } ~ \frac { \partial f } { \partial w _ { 2 1 } } ~ \cdot \cdot ~ \frac { \partial f } { \partial w _ { M 1 } } \right) ^ { \top } } \end{array}$

(2) Let f be a two-layer infinitely wide neural network mapping from $\mathbb { R } ^ { d }$ to R given by

$$
\tilde {f} (x; w _ {1}, w _ {2}, \dots , w _ {d}, a) = \int_ {0} ^ {1} \sigma \left(w _ {1} (s) x _ {1} + \dots + w _ {d} (s) x _ {d}\right) a (s) \mathrm{d} s,
$$

where $w _ { 1 } ( s ) , w _ { 2 } ( s ) , \ldots , w _ { d } ( s ) , a ( s ) \in C ( [ 0 , 1 ] )$ . Write out the Fr´echet derivative of $\tilde { f }$ with respect to $w _ { 1 }$ , that is, find a bounded linear functional $\mathcal { L } : C ( [ 0 , 1 ] ) \to \mathbb { R }$ such that

$$
\lim _ {\| h \| _ {\infty} \to 0} \frac {\left| \tilde {f} (x ; w _ {1} + h , w _ {2} , \ldots , w _ {d} , a) - \tilde {f} (x ; w _ {1} , w _ {2} , \ldots , w _ {d} , a) - \mathcal {L} (h) \right|}{\| h \| _ {\infty}} = 0,
$$

where $\| h \| _ { \infty } : = \operatorname* { m a x } _ { s \in [ 0 , 1 ] } | h ( s ) |$ |. And describe how to relate the results of (1) and (2).

## Exercise 8

Let $K \subset \mathbb { R } ^ { d }$ be a compact set. Given $w \in \mathbb { R } ^ { d }$ . Prove that the set $K _ { w } : = \{ y = w ^ { \top } x : x \in K \}$ is a compact subset of R.

## Exercise 9

Let $f ( x ; \theta ) = a ^ { \top } \sigma ( x * k + b ) + c$ be a CNN, where the input $x \in \mathbb { R } ^ { 3 }$ , kernel $k = ( 1 , 2 )$ , and other parameters $a = ( 1 ~ - 1 ) ^ { \top } , b = - 6 , c = 1$ . Here $\theta = \{ k , a , b , c \}$ is the set of free parameters, and ∗ has stride 1 and no padding. $\sigma ( t ) = | t |$ . Let $x _ { 0 } = ( 1 2 3 ) ^ { \top }$ . Compute $f ( x _ { 0 } ; \theta )$ and $\nabla _ { \boldsymbol { \theta } } f ( \boldsymbol { x } _ { 0 } ; \boldsymbol { \theta } )$

## Exercise 10

(1) Show that the logistic function $\begin{array} { r } { \sigma _ { c } ( t ) = \frac { 1 } { 1 + e ^ { - c t } } } \end{array}$ is a squashing function for every $c > 0$

(2) Prove that lim $\mathsf { i } _ { c  \infty } \sigma _ { c } ( t ) = H ( t )$ for every $t \neq 0$

(3) Is the convergence uniform on R? Justify your answer.

## Exercise 11

Consider average-pooling with filter size 2 and stride 1: $\begin{array} { r } { P ( x ) _ { j } = \frac { x _ { j } + x _ { j + 1 } } { 2 } } \end{array}$

(1) Write the matrix form of $P : \mathbb { R } ^ { 4 }  \mathbb { R } ^ { 3 }$

(2) Compute the adjoint operator (denoted by P<sup>∗</sup>) of P.

(3) Use this to derive the gradient of $\mathcal { L } ( \boldsymbol { x } ) = \| \boldsymbol { P } ( \boldsymbol { x } ) - \boldsymbol { c } \| _ { 2 } ^ { 2 }$ with respect to x, where $c \in \mathbb { R } ^ { 3 }$ is fixed.

## Exercise 12

Let $f ( x _ { 1 } , x _ { 2 } ) = \mathrm { R e L U } ( x _ { 1 } ) + \mathrm { R e L U } ( x _ { 2 } ) - \mathrm { R e L U } ( x _ { 1 } + x _ { 2 } )$

(1) $\mathrm { P a r t i t i o n \mathbb { R } ^ { 2 } }$ into regions where f is afine.

(2) Write the explicit expression of f on each region.

(3) Determine whether f is convex, concave, or neither.

# Approximation Theory of Neural Networks

The approximation theory of neural networks can help to estimate the approximation errors in deep learning.

## 2.1 Universal Approximation in One Dimension

Neural networks behave as universal approximators. That is, their output is an accurate approximation to any desired degree of accuracy of functions in certain spaces of functions. The universal approximation can be characterized by the density of neural network sets. Let M be a metric space of functions (e.g. all continuous functions on a compact set) with metric $d ( \cdot , \cdot )$ , and let $\mathcal { N }$ be a set of neural networks. We say N is dense in M if for any $f \in \mathcal { M }$ and any $\epsilon > 0$ , there is some $\phi \in \mathcal N$ such that $d ( \phi , f ) < \epsilon$ . In this section, we first study the universal approximation in one dimension.

## 2.1.1 Stone-Weierstrass’ theorem

In this section, we denote by K a compact set in $\mathbb { R } ^ { n } ;$ namely, K is a bounded and closed subset of $\mathbb { R } ^ { n }$ . The set of continuous real-valued functions on K is denoted by $C ( K )$ . Then the space $C ( K )$ is a metric space with the metric

$$
d (f, g) = \max _ {x \in K} | f (x) - g (x) |, \quad f, g \in C (K).
$$

In fact, $C ( K )$ with the norm $\| f \| _ { \infty } : = \operatorname* { m a x } _ { x \in K } | f ( x ) |$ is a Banach space and also a Banach algebra. A subset A of $C ( K )$ is called an subalgebra if A is closed with respect to linear combinations and multiplication with reals:

1. if $f , g \in { \mathcal { A } }$ , then $f + g \in A ;$

2. if $f \in { \mathcal { A } }$ and $k \in \mathbb { R }$ , then $k f \in { \mathcal { A } }$ ;

3. if $f , g \in { \mathcal { A } }$ , then $f g \in A .$

The first two conditions state that A is a linear subspace of $C ( K )$

Example 2.1 Let F be the set of finite Fourier series of all degrees on $[ 0 , 2 \pi ]$ , i.e.

$$
\mathcal {F} = \left\{\phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \cos (m x) + b _ {m} \sin (m x): a _ {0}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {N} \right\}.
$$

Clearly, F is a linear space. And using trigonometric formulas such as $\cos ( m x ) \cos ( n x ) = { \textstyle { \frac { 1 } { 2 } } } [ \cos ( m +$ $n ) x + \cos ( m - n ) x ]$ , it follows that $\phi _ { 1 } \phi _ { 2 } \in \mathcal { F } \mathrm { ~ i f ~ } \phi _ { 1 } , \phi _ { 2 } \in \mathcal { F }$ . Hence, $\mathcal { F }$ is an subalgebra of $C [ 0 , 2 \pi ]$

Example 2.2 Let $\mathcal { P } ( [ a , b ] )$ be the set of polynomials of all degrees on $[ a , b ]$ , i.e.

$$
\mathcal {P} ([ a, b ]) = \left\{p (x) = \sum_ {m = 0} ^ {M} c _ {m} x ^ {m}: c _ {m} \in \mathbb {R}, M \in \mathbb {N} \right\}.
$$

Clearly, $\mathcal { P } ( [ a , b ] )$ is a linear space. And $\textstyle { \mathcal { P } } ( [ a , b ] )$ is an subalgebra of $C [ \boldsymbol { a } , \boldsymbol { b } ]$ since the sum and product of two polynomials are still polynomials.

An subalgebra A is said to separate points in K, if for any distinct $x _ { 1 } , x _ { 2 } \in K$ , there is some $f \in { \mathcal { A } }$ such that $f ( x _ { 1 } ) \neq f ( x _ { 2 } )$

The set of finite Fourier series $\mathcal { F }$ does not separate points in $[ 0 , 2 \pi ]$ , because for any function $\phi \in \mathcal { F } , \phi ( 0 ) = \phi ( 2 \pi )$ . However, it separates points in any compact subset of $( 0 , 2 \pi )$ . Indeed, for any $x _ { 1 } , x _ { 2 } \in ( 0 , 2 \pi )$ and $x _ { 1 } \neq x _ { 2 }$ , we choose $\phi = a _ { 1 } \cos ( x ) + b _ { 1 } \sin ( x )$ Then $\phi ( x _ { 1 } ) \neq \phi ( x _ { 2 } )$ is equivalent to $a _ { 1 } ( \cos ( x _ { 1 } ) - \cos ( x _ { 2 } ) ) \neq b _ { 1 } ( \sin ( x _ { 2 } ) - \sin ( x _ { 1 } ) )$ . If $\cos ( x _ { 1 } ) - \cos ( x _ { 2 } ) \neq 0$ , it sufices to let $\begin{array} { r } { a _ { 1 } = 1 + b _ { 1 } \cdot \frac { \sin ( x _ { 2 } ) - \sin ( x _ { 1 } ) } { \cos ( x _ { 1 } ) - \cos ( x _ { 2 } ) } } \end{array}$ ; if $\cos ( x _ { 1 } ) - \cos ( x _ { 2 } ) = 0$ , then $x _ { 1 } + x _ { 2 } = 2 \pi$ , so sin $. ( x _ { 2 } ) \neq \sin ( x _ { 1 } )$ , and it sufices to let $\begin{array} { r } { b _ { 1 } = 1 + a _ { 1 } \cdot \frac { \cos ( x _ { 1 } ) - \cos ( x _ { 2 } ) } { \sin ( x _ { 2 } ) - \sin ( x _ { 1 } ) } } \end{array}$

It is clear that the set of polynomials $\textstyle { \mathcal { P } } ( [ a , b ] )$ separate points in $[ a , b ]$ . For any $x _ { 1 } , x _ { 2 } \in [ a , b ]$ and $x _ { 1 } \neq x _ { 2 }$ , we choose $p ( x ) = x$ , then $f ( x _ { 1 } ) \neq f ( x _ { 2 } )$ always holds.

Theorem 2.1 (Stone-Weierstrass) Let K be a compact set in $\mathbb { R } ^ { d }$ and A be a subalgebra $o f C ( K )$ that contains a non-zero constant function. Then A is dense in $C ( K )$ if and only if it separates points in K.

Recall that A is dense in $C ( K )$ means for any $f \in C ( K )$ and any $\epsilon > 0$ , there is some $\phi \in { \mathcal { A } }$ such that

$$
d (\phi , f) = \max _ {x \in K} | \phi (x) - f (x) | <   \epsilon .
$$

The property that A contains a non-zero constant function is equivalent to that A contains the constant function $\phi ( x ) \equiv 1$ , which is also equivalent to that A contains all constant functions.

The set of polynomials $\mathcal { P } ( [ a , b ] )$ separates points in $[ a , b ]$ and contains constant functions. By Stone-Weierstrass theorem, for any continuous function $f : [ a , b ] \to \mathbb { R }$ and any $\epsilon > 0$ , there is a polynomial function $p$ such that $| f ( x ) - p ( x ) | < \epsilon , \forall x \in [ a , b ]$ . If we consider a positive sequence $\epsilon _ { n }  0$ and denote the associated polynomials by $p _ { n }$ , then the sequence $( p _ { n } ) _ { n }$ converges uniformly to f on $[ a , b ]$

Using Stone-Weierstrass’ theorem, we can further prove that the set of 2-D polynomials on $[ a _ { 1 } , b _ { 1 } ] \times [ a _ { 2 } , b _ { 2 } ]$ , i.e.

$$
\begin{array}{l} \mathcal {P} ([ a _ {1}, b _ {1} ] \times [ a _ {2}, b _ {2} ]) = \left\{p (x, y) = \sum_ {m + n = 0} ^ {M} c _ {m, n} x ^ {m} y ^ {n}: c _ {m, n} \in \mathbb {R}, M \in \mathbb {N} \right\} \\ = \left\{p (x, y) = \sum_ {j = 1} ^ {J} g _ {j} (x) h _ {j} (y): g _ {j} \in \mathcal {P} ([ a _ {1}, b _ {1} ]), h _ {j} \in \mathcal {P} ([ a _ {2}, b _ {2} ]), J \in \mathbb {N} \right\}, \end{array}
$$

is dense in $C ( [ a _ { 1 } , b _ { 1 } ] \times [ a _ { 2 } , b _ { 2 } ] )$

The set of finite Fourier series $\mathcal { F }$ is not dense in $C ( [ 0 , 2 \pi ] )$ , but it is dense in

$$
C _ {p} ^ {1} ([ 0, 2 \pi ]) := \left\{f \in C ^ {1} ([ 0, 2 \pi ]): f (0) = f (2 \pi) \right\},
$$

i.e. the set of 2π-periodic functions on $[ 0 , 2 \pi ]$ that have continuous derivatives.

## Application to neural networks

We consider the following set of two-layer neural networks on a closed interval $K \subset \mathbb { R }$

$$
\mathcal {N} = \left\{\phi : K \to \mathbb {R}, \phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} x + b _ {m}): a _ {0}, a _ {m}, w _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {N} \right\},
$$

where σ is a continuous activation function. It is clear that $\mathcal { N }$ is closed under linear combinations. For some special σ such that $\sigma ( t ) = \sin ( t )$ , cos(t) or $e ^ { t } , \mathcal { N }$ is closed under the multiplication and thus a subalgebra of $C ( K )$ . Moreover, $\mathcal { N }$ contains all constant functions. So $\mathcal { N }$ is dense in $C ( K )$ if and only if $\mathcal { N }$ can separate points in K.

1. If $\sigma ( t ) = e ^ { t }$ , for any distinct $x _ { 1 } , x _ { 2 } \ \in \ K$ , we only need to let $\phi ( x ) = e ^ { x } \in \mathcal { N }$ and then $\phi ( x _ { 1 } ) = e ^ { x _ { 1 } } \neq e ^ { x _ { 2 } } = \phi ( x _ { 2 } )$ ;

2. If $\sigma ( t ) = \sin ( t )$ , we choose $c _ { 1 } , c _ { 2 } \in K$ such that $c _ { 1 } \neq c _ { 2 }$ and $\sin ( c _ { 1 } ) \neq \sin ( c _ { 2 } )$ (it is always possible). For any distinct $x _ { 1 } , x _ { 2 } \in K$ , we only need to let

$$
\phi (x) = \sin \left(\frac {c _ {1} - c _ {2}}{x _ {1} - x _ {2}} x + \frac {c _ {2} x _ {1} - c _ {1} x _ {2}}{x _ {1} - x _ {2}}\right) \in \mathcal {N}.
$$

Then $\phi ( x _ { 1 } ) = \sin ( c _ { 1 } ) \neq \sin ( c _ { 2 } ) = \phi ( x _ { 2 } )$ . Similar argument applies to $\sigma ( t ) = \cos ( t )$

Therefore, suppose that $\sigma ( t ) = \sin ( t )$ , cos(t) or $e ^ { t }$ . For any $f \in C ( K ) , \mathcal { N }$ can achieve zero approximation error; namely,

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {\infty} = 0.
$$

## 2.1.2 Wiener’s Tauberian theorems

We introduce Wiener’s theorems to illustrate the density of special neural networks in $L ^ { 1 } ( \mathbb { R } )$ and $L ^ { 2 } ( \mathbb { R } )$ . The next theorem is for $L ^ { 1 } ( \mathbb { R } )$

Theorem 2.2 Let $f \in L ^ { 1 } ( \mathbb { R } )$ and define the translation functions $f _ { \boldsymbol { \theta } } ( \boldsymbol { x } ) = f ( \boldsymbol { x } + \boldsymbol { \theta } )$ . Then the linear span of the family $\{ f _ { \theta } : \theta \in \mathbb { R } \}$ is dense in $L ^ { 1 } ( \mathbb { R } )$ if and only if $\hat { f } ( \omega ) \neq 0$ for all $\omega \in \mathbb { R }$ , where $\scriptstyle { \hat { f } } ( \omega )$ is the Fourier transform of f.

By Theorem 2.2, we directly have the density of the following set of two-layer neural networks,

$$
\mathcal {N} = \left\{\phi : \mathbb {R} \to \mathbb {R}, \phi (x) = \sum_ {m = 1} ^ {M} a _ {m} \sigma (x + b _ {m}): a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {Z} ^ {+} \right\}.\tag{2.1}
$$

Theorem 2.3 Suppose $\sigma \in L ^ { 1 } ( \mathbb { R } )$ and $\hat { \sigma } ( \omega ) \neq 0$ for all $\omega \in \mathbb { R }$ . Then $\mathcal { N }$ given by (2.1) is dense in $L ^ { 1 } ( \mathbb { R } )$ ; namely, for any $f \in L ^ { 1 } ( \mathbb { R } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \int_ {\mathbb {R}} | \phi (x) - f (x) | \mathrm{d} x = 0.
$$

The next some activation functions satisfy the above properties.

1. Double exponential Let $\sigma ( x ) = e ^ { - \lambda | x | }$ with $\lambda > 0$ . Then

$$
\int_ {\mathbb {R}} | \sigma (x) | \mathrm{d} x = 2 \int_ {0} ^ {\infty} e ^ {- \lambda x} \mathrm{d} x = \frac {2}{\lambda} <   \infty ,
$$

and hence $\sigma \in L ^ { 1 } ( \mathbb { R } )$ . The Fourier transform is

$$
\hat {\sigma} (\omega) = \frac {2 \lambda}{\lambda^ {2} + \omega^ {2}} \neq 0;
$$

2. Laplace potential Let $\textstyle \sigma ( x ) = { \frac { 1 } { a ^ { 2 } + x ^ { 2 } } }$ with $a > 0$ . Then

$$
\int_ {\mathbb {R}} | \sigma (x) | \mathrm{d} x = \frac {1}{a} \arctan \left(\frac {x}{a}\right) \Big | _ {- \infty} ^ {\infty} = \frac {\pi}{a} <   \infty ,
$$

and hence $\sigma \in L ^ { 1 } ( \mathbb { R } )$ . The Fourier transform is

$$
\hat {\sigma} (\omega) = \frac {\pi}{a} e ^ {- a | \omega |} \neq 0;
$$

3. Gaussian Let $\sigma ( x ) = e ^ { - a x ^ { 2 } }$ with $a > 0$ . Then

$$
\int_ {\mathbb {R}} | \sigma (x) | \mathrm{d} x = \int_ {\mathbb {R}} e ^ {- a x ^ {2}} \mathrm{d} x = \sqrt {\frac {\pi}{a}} <   \infty ,
$$

and hence $\sigma \in L ^ { 1 } ( \mathbb { R } )$ . The Fourier transform is

$$
\hat {\sigma} (\omega) = \sqrt {\frac {\pi}{a}} e ^ {- \frac {\omega^ {2}}{4 a}} \neq 0.
$$

The next theorem is for the $L ^ { 2 }$ case.

Theorem 2.4 Let $f \in L ^ { 2 } ( \mathbb { R } )$ and define the translation functions $f _ { \boldsymbol { \theta } } ( \boldsymbol { x } ) = f ( \boldsymbol { x } + \boldsymbol { \theta } )$ . Then the linear span of the family $\{ f _ { \theta } : \theta \in \mathbb { R } \}$ is dense in $L ^ { 2 } ( \mathbb { R } )$ if and only if the set $\{ \omega \in \mathbb { R } : \hat { f } ( \omega ) = 0 \}$ has zero Lebesgue measure.

In practice, it sufices to have a finite or countable number of zeros for $\scriptstyle { \hat { f } } ( \omega )$ to guarantee that the Lebesgue measure of $\{ \omega \in \mathbb { R } : \hat { f } ( \omega ) = 0 \}$ is zero. So we have

Theorem 2.5 Suppose $\sigma \in L ^ { 2 } ( \mathbb { R } )$ and $\hat { \sigma } ( \omega )$ has at most countably many zeros on $\mathbb { R }$ . Then $\mathcal { N }$ given by (2.1) is dense in $L ^ { 2 } ( \mathbb { R } )$ ; namely, for any $f \in L ^ { 2 } ( \mathbb { R } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \int_ {\mathbb {R}} | \phi (x) - f (x) | ^ {2} \mathrm{d} x = 0.
$$

It is worth noting that the previously presented activation functions (1), (2), and (3) are also in $L ^ { 2 } ( \mathbb { R } )$ and do not have any zeros on R.

Unfortunately, for activation functions of sigmoid type or hockey-stick shape, such as the logistic function or ReLU are not in $L ^ { p } ( \mathbb { R } )$ with $p \geq 1$ . Therefore, Wiener’s theorem is not applicable in this case.

## 2.1.3 Approximation with Heaviside activation

We consider the set of two-layer neural networks with Heaviside activation function, i.e.

$$
\mathcal {N} = \left\{\phi : [ a, b ] \to \mathbb {R}, \phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} H (x - b _ {m}): a _ {0}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {N} \right\},\tag{2.2}
$$

where $H ( \cdot )$ is the Heaviside function defined by (1.2). Note that the weights in the hidden layer are all fixed as 1.

It is trivial to see that neural networks in $\mathcal { N }$ are piecewise constant functions (or step functions). The weights $a _ { n }$ determine the values that will be taken, and the biases $b _ { n }$ determine the position of pieces. Moreover, any step function that is continuous from the right on $[ a , b ]$ can be formulated as a neural network in ${ \mathcal { N } } .$ Specifically, let $a = x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { m } < x _ { m + 1 } = b$ and

$$
\phi (x) = \left\{ \begin{array}{l l} c _ {1}, & x \in [ x _ {1}, x _ {2}), \\ c _ {2}, & x \in [ x _ {2}, x _ {3}), \\ \dots \\ c _ {m}, & x \in [ x _ {m}, x _ {m + 1} ]. \end{array} \right.
$$

Then

$$
\phi (x) = c _ {1} H (x - x _ {1}) + (c _ {2} - c _ {1}) H (x - x _ {2}) + \dots + (c _ {m} - c _ {m - 1}) H (x - x _ {m}).
$$

So $\phi \in \mathcal N$ . This means $\mathcal { N }$ contains all step functions on $[ a , b ]$

It is well known that continuous functions on compact sets can be approximated uniformly by step functions to any desired accuracy; That is, the functions in $\mathcal { N }$ can approximate continuous functions on compact sets. More precisely, we have

Theorem 2.6 The set N given by (2.2) is dense in $C ( [ a , b ] )$ : for any $f \in C ( [ a , b ] )$ and any $\epsilon > 0$ there is some $\begin{array} { r } { \phi ( x ) = a _ { 0 } + \sum _ { m = 1 } ^ { M } a _ { m } H ( x - b _ { m } ) \in \mathcal { N } } \end{array}$ with $| a _ { m } | < \epsilon f o r m = 1 , \ldots , M$ such that

$$
| \phi (x) - f (x) | <   \epsilon , \quad \forall x \in [ a, b ].
$$

Proof: Since f is uniformly continuous on $[ a , b ]$ . Given $\epsilon > 0$ , there is some $M \in \mathbb { Z } ^ { + }$ such that

$$
| f (x) - f (y) | <   \epsilon , \quad \text { whenever } | x - y | \leq \frac {b - a}{M + 1}.
$$

Let $a = x _ { 0 } < x _ { 1 } < \cdot \cdot \cdot < x _ { M + 1 } = b$ be an equidistant partition. Then for $x \in [ x _ { k } , x _ { k + 1 } ]$ 2

$$
\left| f (x) - f \left(x _ {k + 1}\right) \right| <   \epsilon ,
$$

We construct $\phi$ by letting $a _ { 0 } = f ( x _ { 1 } ) , a _ { m } = f ( x _ { m + 1 } ) - f ( x _ { m } )$ and $b _ { m } = x _ { m }$ for $1 \leq m \leq M$ . Then it can be verified that $\phi ( x ) = f ( x _ { m + 1 } )$ for all $x \in [ x _ { m } , x _ { m + 1 } )$ . Therefore for any $x \in [ a , b )$ , assume that $x \in [ x _ { m } , x _ { m + 1 } )$ 2

$$
| \phi (x) - f (x) | <   | \phi (x) - f (x _ {m + 1}) | + | f (x _ {m + 1}) - f (x) | = | f (x _ {m + 1}) - f (x) | <   \epsilon .
$$

Also, $\phi ( b ) = f ( b ) , \mathrm { s o } | \phi ( b ) - f ( b ) | = 0 < \epsilon$ . Moreover, for $1 \leq m \leq M , | a _ { m } | = | f ( x _ { m + 1 } ) - f ( x _ { m } ) | <$ ϵ. □

## 2.1.4 Approximation with sigmoidal activation

We consider the two-layer neural networks with sigmoidal activation function. In Section 1.1.1, we mention that the logistic sigmoidal function can approximate the Heaviside function. Therefore sigmoidal neural networks can also approximate Heaviside neural networks. Specifically, we suppose $\sigma : \mathbb { R }  \mathbb { R }$ is a sigmoidal function satisfying the following properties:

1. $\sigma$ is increasing;

2. $\sigma ( \infty ) - \sigma ( - \infty ) = 1 ;$

3. σ is diferentiable with $| \sigma ^ { \prime } |$ bounded,

and define the set of two-layer neural networks with σ activation, i.e.,

$$
\mathcal {N} = \left\{\phi : [ a, b ] \to \mathbb {R}, \phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w x + b _ {m}): a _ {0}, a _ {m}, b _ {m}, w \in \mathbb {R}, M \in \mathbb {N} \right\}.\tag{2.3}
$$

Then we have the following result.

Theorem 2.7 The set N given by (2.3) is dense in $C ( [ a , b ] )$ : for any $f \in C ( [ a , b ] )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {\infty} = 0.
$$

Proof: Let $f \in C ( [ a , b ] )$ . Given $\epsilon > 0$ , by Theorem 2.6, there is some $\begin{array} { r } { \psi ( x ) = a _ { 0 } + \sum _ { m = 1 } ^ { M } a _ { m } H ( x - } \end{array}$ $x _ { m } )$ with $\vert a _ { m } \vert < \frac { \epsilon } { 4 }$ for $m \geq 1$ such that

$$
| \psi (x) - f (x) | <   \frac {\epsilon}{2}, \quad \forall x \in [ a, b ].\tag{2.4}
$$

Next, we construct a smoother of $\psi ( x )$ using convolution. Let $\begin{array} { r } { \sigma _ { \alpha } ( x ) = \sigma ( \frac { x } { \alpha } ) } \end{array}$ with $\alpha > 0$ (see Figure 2.1 for graphs). Define

$$
\phi_ {\alpha} (x) := (\psi * \sigma_ {\alpha} ^ {\prime}) (x) = \int_ {- \infty} ^ {\infty} \psi (y) \sigma_ {\alpha} ^ {\prime} (x - y) \mathrm{d} y.
$$

We can prove that $\phi _ { \alpha }$ is a sigmoidal neural network in ${ \mathcal { N } } .$ In fact, using integration by parts, we have in the sense of derivatives of generalized functions:

$$
\begin{array}{r l} & {\phi_ {\alpha} (x) = \int_ {- \infty} ^ {\infty} \psi (y) \sigma_ {\alpha} ^ {\prime} (x - y) \mathrm{d} y = - \int_ {- \infty} ^ {\infty} \psi (y) \partial_ {y} (\sigma_ {\alpha} (x - y)) \mathrm{d} y} \\ & {\qquad = \int_ {- \infty} ^ {\infty} \psi^ {\prime} (y) \sigma_ {\alpha} (x - y) \mathrm{d} y - \psi (y) \sigma_ {\alpha} (x - y) \Big | _ {- \infty} ^ {\infty}} \\ & {\qquad = \int_ {- \infty} ^ {\infty} \psi^ {\prime} (y) \sigma_ {\alpha} (x - y) \mathrm{d} y - (\psi (\infty) \sigma_ {\alpha} (- \infty) - \psi (- \infty) \sigma_ {\alpha} (\infty))} \\ & {\qquad = \int_ {- \infty} ^ {\infty} \left(\sum_ {m = 1} ^ {M} a _ {m} H ^ {\prime} (y - x _ {m})\right) \sigma_ {\alpha} (x - y) \mathrm{d} y - \left(\lambda \sum_ {m = 0} ^ {M} a _ {m} - a _ {0} (\lambda + 1)\right)} \\ & {\qquad = \sum_ {m = 1} ^ {M} a _ {m} \int_ {- \infty} ^ {\infty} \delta (y - x _ {m}) \sigma_ {\alpha} (x - y) \mathrm{d} y - \left(\lambda \sum_ {m = 1} ^ {M} a _ {m} - a _ {0}\right)} \\ & {\qquad = \sum_ {m = 1} ^ {M} a _ {m} \sigma_ {\alpha} (x - x _ {m}) + a _ {0} - \lambda \sum_ {m = 1} ^ {M} a _ {m},} \end{array}
$$

![](images/5967bf928f453187263e1ff0bad3b359f6374c862452639584e8eb50850e6d21.jpg)  
(a) $\sigma _ { \alpha } ( x )$

![](images/deafbb43f77ac079e25d03f8d0e0536a0e12d7f4ef37e5111895605315668688.jpg)  
(b) $\sigma _ { \alpha } ^ { \prime } ( x )$

Figure 2.1: Logistic sigmoidal function $\begin{array} { r } { \sigma _ { \alpha } ( x ) = \frac { 1 } { 1 + e ^ { - x / \alpha } } } \end{array}$ and its derivative.  
![](images/13f47d84447338aaf9ac7817d4cad330370c34ae7a8dda6d673de1011e82edf8.jpg)  
(a) $\alpha = 0 . 1$

![](images/a747ce0ebfe3eb5f4d00bb3630b02186406a1795834177295f99fabb1f1f96e7.jpg)  
(b) $\alpha = 0 . 0 2$  
Figure 2.2: A step function $\psi ( x )$ and its smoother $\phi _ { \alpha } ( x )$

where $\lambda : = \sigma _ { \alpha } ( - \infty )$ and $\delta ( \cdot )$ means the Dirac delta function. We let $\begin{array} { r } { \tilde { a } _ { 0 } = a _ { 0 } - \lambda \sum _ { m = 1 } ^ { M } a _ { m } , w = 1 / \alpha } \end{array}$ and $b _ { m } = - x _ { m } / \alpha$ , then

$$
\phi_ {\alpha} (x) = \tilde {a} _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w x + b _ {m}).
$$

So $\phi _ { \alpha } \in \mathcal { N }$ for all $\alpha > 0 .$

Now we prove that $| \psi ( x ) - \phi _ { \alpha } ( x ) | < { \frac { \epsilon } { 2 } }$ for all x if α is suficiently small (see Figure 2.2 for the graph representation of the smoother). Using the fact $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \sigma _ { \alpha } ^ { \prime } ( y ) \mathrm { d } y = 1 } \end{array}$ , we have

$$
\begin{array}{c} \psi (x) - \phi_ {\alpha} (x) = \psi (x) \int_ {- \infty} ^ {\infty} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y - \int_ {- \infty} ^ {\infty} \sigma_ {\alpha} ^ {\prime} (y) \psi (x - y) \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} \sigma_ {\alpha} ^ {\prime} (y) (\psi (x) - \psi (x - y)) \mathrm{d} y \end{array}\tag{2.5}
$$

Note that for fixed $y , \psi ( x - y )$ is a function obtained from the graph of $\psi ( x )$ by a horizontal shift y. Let $\epsilon ^ { \prime } > 0$ be small enough such that there is only one bump of the diference $\psi ( x ) -$ $\psi ( x - y ) { \mathrm { ~ i f ~ } } | y | < \epsilon ^ { \prime }$ . For example, we can choose $\begin{array} { r } { \epsilon ^ { \prime } = \frac { 1 } { 2 } \operatorname* { m i n } _ { 1 \leq m \leq M - 1 } | x _ { m } - x _ { m + 1 } | } \end{array}$ . In this case, $\begin{array} { r } { | \psi ( x ) - \psi ( x - y ) | \leq \operatorname* { m a x } _ { 1 \leq m \leq M } | a _ { m } | < \frac { \epsilon } { 4 } } \end{array}$ , because the height of every bump is equal to one of the coeficients $a _ { m } ,$ see Figure 2.3.

![](images/ce8bcbf9cd824742f811c9595f6a28d74170470ca6e72ef7a9a743c6e8f5907d.jpg)  
Figure 2.3: (a) The step functions $\psi ( x )$ and $\psi ( x - y )$ for $| y | < \epsilon ^ { \prime } ;$ (b) The diference $\psi ( x ) - \psi ( x - y )$

On the other hand, note that

$$
\begin{array}{r l} & {\int_ {(- \infty , - \epsilon^ {\prime} ] \cup [ \epsilon^ {\prime}, \infty)} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y = \sigma_ {\alpha} (y) \Big | _ {- \infty} ^ {- \epsilon^ {\prime}} + \sigma_ {\alpha} (y) \Big | _ {\epsilon^ {\prime}} ^ {\infty}} \\ & {\qquad = (\sigma_ {\alpha} (- \epsilon^ {\prime}) - \sigma_ {\alpha} (- \infty)) + (\sigma_ {\alpha} (\infty) - \sigma_ {\alpha} (\epsilon^ {\prime}))} \\ & {\qquad = (\sigma (- \frac {\epsilon^ {\prime}}{\alpha}) - \sigma (- \infty)) + (\sigma (\infty) - \sigma (\frac {\epsilon^ {\prime}}{\alpha})).} \end{array}
$$

Since $\sigma ( - \frac { \epsilon ^ { \prime } } { \alpha } ) \to \sigma ( - \infty )$ and $\sigma ( \frac { \epsilon ^ { \prime } } { \alpha } )  \sigma ( \infty )$ as $\alpha \searrow 0 ,$ , for α small enough, it holds that

$$
\sigma (- \frac {\epsilon^ {\prime}}{\alpha}) - \sigma (- \infty) <   \frac {\epsilon}{8 (2 | | f | | _ {\infty} + \epsilon)}, \quad \sigma (\infty) - \sigma (\frac {\epsilon^ {\prime}}{\alpha}) <   \frac {\epsilon}{8 (2 | | f | | _ {\infty} + \epsilon)}.
$$

So

$$
\int_ {(- \infty , - \epsilon^ {\prime} ] \cup [ \epsilon^ {\prime}, \infty)} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y <   \frac {\epsilon}{4 (2 | | f | | _ {\infty} + \epsilon)}.
$$

Therefore, for α small enough, it follows (2.5) that

$$
\begin{array}{l} | \psi (x) - \phi_ {\alpha} (x) | \leq \left| \int_ {(- \infty , - \epsilon^ {\prime} ] \cup [ \epsilon^ {\prime}, \infty)} \sigma_ {\alpha} ^ {\prime} (y) (\psi (x) - \psi (x - y)) \mathrm{d} y \right| + \left| \int_ {- \epsilon^ {\prime}} ^ {\epsilon^ {\prime}} \sigma_ {\alpha} ^ {\prime} (y) (\psi (x) - \psi (x - y)) \mathrm{d} y \right| \\ \leq \int_ {(- \infty , - \epsilon^ {\prime} ] \cup [ \epsilon^ {\prime}, \infty)} \sigma_ {\alpha} ^ {\prime} (y) (| \psi (x) | + | \psi (x - y) |) \mathrm{d} y + \int_ {- \epsilon^ {\prime}} ^ {\epsilon^ {\prime}} \sigma_ {\alpha} ^ {\prime} (y) | \psi (x) - \psi (x - y) | \mathrm{d} y \\ \leq (2 | | f | | _ {\infty} + \epsilon) \int_ {(- \infty , - \epsilon^ {\prime} ] \cup [ \epsilon^ {\prime}, \infty)} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y + \frac {\epsilon}{4} \int_ {- \epsilon^ {\prime}} ^ {\epsilon^ {\prime}} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y \\ \leq \frac {\epsilon}{4} + \frac {\epsilon}{4} \int_ {- \infty} ^ {\infty} \sigma_ {\alpha} ^ {\prime} (y) \mathrm{d} y = \frac {\epsilon}{2}. \end{array}\tag{2.6}
$$

Combining (2.4) and (2.6) leads to

$$
| f (x) - \phi_ {\alpha} (x) | <   \epsilon , \quad \forall x \in [ a, b ],\tag{2.7}
$$

which is the desired result.

Theorem 2.6 and 2.7 proved in the last two sections state that any continuous function on [0, 1] can be learned in two ways: Theorem 2.6 assures that the learning can be done by step functions, while Theorem 2.7 by smooth functions. However, the latter result is more useful, since the approximator is smooth and thus diferentiable, fact that makes possible the backpropagation.

## 2.1.5 Approximation with ReLU activation

We consider the two-layer neural networks with ReLU activation function. Define

$$
\mathcal {N} = \left\{\phi : [ a, b ] \to \mathbb {R}, \phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \mathrm{ReLU} (x + b _ {m}): a _ {0}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {N} \right\},\tag{2.8}
$$

where ${ \mathrm { R e L U } } ( x ) = \operatorname* { m a x } \{ 0 , x \}$ is the ReLU activation. It is clear that for any $\phi \in \mathcal { N } , \mathrm { i f } \ \xi \neq - b _ { m }$ $( m = 1 , \ldots , M )$ , then $\phi$ is a linear function in some neighborhood of $x = \xi . \mathrm { ~ I f ~ } \xi = - b _ { m }$ for some $m$ , then $\phi$ is still $C ^ { 0 }$ continuous at $x = \xi$ . Consequently, any function in $\mathcal { N }$ is a piecewise linear function. Conversely, any piecewise linear function on $[ a , b ]$ can be formulated as functions in ${ \mathcal { N } } .$

Moreover, we have the following result.

Theorem 2.8 The set $\mathcal { N }$ given by (2.8) is dense in $C ( [ a , b ] )$ : for any $f \in C ( [ a , b ] )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {\infty} = 0.
$$

Proof: Let $f \in C ( [ a , b ] )$ , then $f$ is uniformly continuous on $[ a , b ]$ . Given $\epsilon > 0$ , there is some $\delta > 0$ such that

$$
| f (x) - f (y) | <   \frac {\epsilon}{2}, \quad \text { whenever } | x - y | <   \delta .
$$

Let $a = x _ { 1 } < x _ { 2 } < \cdot \cdot \cdot < x _ { M + 1 } = b$ be an equidistant partition, where M is large enough such that $\begin{array} { r } { h : = | x _ { m + 1 } - x _ { m } | = \frac { ( b - a ) } { M } < \delta } \end{array}$ . Then we can construct $\phi \in \mathcal N$ such that $\phi$ interpolates $( x _ { m } , f ( x _ { m } ) )$ for all m. In fact, we can just let $b _ { m } = - x _ { m }$ for $m = 1 , \ldots , M$ . And the relation $\phi ( x _ { m } ) = f ( x _ { m } )$ $m = 1 , \ldots , M + 1$ leads to the linear system

$$
\begin{array}{r l r} {a _ {0}} & & {= f (x _ {1}),} \\ {a _ {0} + h a _ {1}} & & {= f (x _ {2}),} \\ {\dots} & & \\ {a _ {0} + (M - 1) h a _ {1} + \ldots + h a _ {M - 1}} & & {= f (x _ {M}),} \\ {a _ {0} + M h a _ {1}} & & {+ \ldots + 2 h a _ {M - 1} + h a _ {N} = f (x _ {M + 1}),} \end{array}
$$

which has a unique solution

$$
a _ {0} = f (x _ {1}), \quad a _ {1} = \frac {f (x _ {2}) - f (x _ {1})}{h}, \quad a _ {m} = \frac {f (x _ {m + 1}) - 2 f (x _ {m}) + f (x _ {m - 1})}{h} \text {for} m = 2, \ldots , M.
$$

Now the constructed $\begin{array} { r } { \phi ( { \boldsymbol x } ) = a _ { 0 } + \sum _ { m = 1 } ^ { M } a _ { m } \mathrm { R e L U } ( { \boldsymbol x } - { \boldsymbol x } _ { m } ) } \end{array}$ is a piecewise linear function with M pieces, each of which is located on $[ x _ { 1 } , x _ { 2 } ] , [ x _ { 2 } , x _ { 3 } ] , \dotsc , [ x _ { M } , x _ { M + 1 } ]$ , respectively (see Figure 2.4). Therefore, for any $x \in [ a , b ]$ , suppose that $x \in [ x _ { k } , x _ { k + 1 } ]$ , we have

$$
\begin{array}{r l} & {| \phi (x) - f (x) | \leq | \phi (x) - f (x _ {k}) | + | f (x _ {k}) - f (x) |} \\ & {\quad = | \phi (x) - \phi (x _ {k}) | + | f (x _ {k}) - f (x) |} \\ & {\quad \leq | \phi (x _ {k + 1}) - \phi (x _ {k}) | + | f (x _ {k}) - f (x) |} \\ & {\quad = | f (x _ {k + 1}) - f (x _ {k}) | + | f (x _ {k}) - f (x) | <   \frac {\epsilon}{2} + \frac {\epsilon}{2} = \epsilon .} \end{array}
$$

![](images/9f2af32a611b4f0d6f12d861bc54cb4b43ab60a5ef83a054b67acd016502d0bd.jpg)  
Figure 2.4: The continuous function f(x) and the interpolating piecewise linear function $\phi ( x )$

## 2.1.6 Approximation with softplus activation

Let us consider the two-layer neural network with softplus activation function $\operatorname { s p } ( x ) = \ln ( 1 + e ^ { x } )$ It is observed in Figure 1.2 that the softplus function is like a smoother of the ReLU function. Recall in Section 2.1.4 we construct a smoother $f _ { \alpha }$ of piecewise linear function $\phi$ by taking $f _ { \alpha }$ as the convolution of $\phi$ and $\sigma _ { \alpha } ^ { \prime } ( x )$ , where $\begin{array} { r } { \sigma _ { \alpha } ( x ) = \sigma ( \frac { x } { \alpha } ) } \end{array}$ and $\sigma$ is a sigmoidal function. So it is natural to ask if sp(x) is the convolution of ReL $\boldsymbol { \mathrm { { I } } } \boldsymbol { \mathrm { { } } } \boldsymbol { \mathrm { { } } } , \boldsymbol { \mathrm { { U } } } ( \boldsymbol { x } )$ and $\sigma _ { \alpha } ^ { \prime } ( x )$ for some specific sigmoidal function σ. The question can be answered by the following discussion.

We let $\textstyle \sigma ( x ) = { \frac { 1 } { 1 + e ^ { - x } } }$ be the logistic sigmoidal function. Then $\operatorname { s p } ^ { \prime } ( x ) = \sigma ( x )$ and $\sigma ^ { \prime } ( x ) =$ $\frac { 1 } { ( 1 + e ^ { x } ) ( 1 + e ^ { - x } ) }$ . We have

## Proposition 2.1 It holds that

$$
\alpha \mathrm{sp} (\frac {x}{\alpha}) = (\mathrm{ReLU} * \sigma_ {\alpha} ^ {\prime}) (x).
$$

In particular, $\operatorname { s p } ( x ) = ( \operatorname { R e L U } * \sigma ^ { \prime } ) ( x )$

Proof:

$$
\begin{array}{r l} & {(\mathrm{ReLU} * \sigma_ {\alpha} ^ {\prime}) (x) = \int_ {- \infty} ^ {\infty} \mathrm{ReLU} (y) \sigma_ {\alpha} ^ {\prime} (x - y) \mathrm{d} y = \int_ {0} ^ {\infty} y \sigma_ {\alpha} ^ {\prime} (x - y) \mathrm{d} y} \\ & {\qquad = - \int_ {x} ^ {- \infty} (x - t) \sigma_ {\alpha} ^ {\prime} (t) \mathrm{d} t = \int_ {- \infty} ^ {x} (x - t) \sigma_ {\alpha} ^ {\prime} (t) \mathrm{d} t} \\ & {\qquad = x \int_ {- \infty} ^ {x} \sigma_ {\alpha} ^ {\prime} (t) \mathrm{d} t - \int_ {- \infty} ^ {x} t \sigma_ {\alpha} ^ {\prime} (t) \mathrm{d} t} \\ & {\qquad = x (\sigma_ {\alpha} (x) - \sigma_ {\alpha} (- \infty)) - \left(t \sigma_ {\alpha} (t) \Big | _ {- \infty} ^ {x} - \int_ {- \infty} ^ {x} \sigma_ {\alpha} (t) \mathrm{d} t\right)} \\ & {\qquad = \lim _ {t \to - \infty} t \sigma_ {\alpha} (t) + \int_ {- \infty} ^ {x} \sigma_ {\alpha} (t) \mathrm{d} t} \\ & {\qquad = 0 + \alpha \ln (1 + e ^ {t / \alpha}) \Big | _ {- \infty} ^ {x} = \alpha \ln (1 + e ^ {x / \alpha}).} \end{array}
$$

Proposition 2.1 means the convolution of a ReLU function and $\sigma _ { \alpha } ^ { \prime }$ is a softplus function. $\mathrm { B y }$ linear combination, it is trivial to conclude that the convolution of a two-layer ReLU network and $\sigma _ { \alpha } ^ { \prime }$ is a two-layer softplus network. More precisely, we define

$$
\mathcal {N} = \left\{\phi : [ a, b ] \to \mathbb {R}, \phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \mathrm{sp} (w x + b _ {m}): a _ {0}, a _ {m}, b _ {m}, w \in \mathbb {R}, M \in \mathbb {N} \right\},\tag{2.9}
$$

which is a set of two-layer neural networks with softplus activation. We have the following result. Proposition 2.2 Suppose $\begin{array} { r } { \psi = c _ { 0 } + \sum _ { m = 1 } ^ { M } c _ { m } \mathrm { R e L U } ( x - x _ { m } ) } \end{array}$ is a two-layer ReLU network. Let $\phi _ { \alpha } = \psi * \sigma _ { \alpha } ^ { \prime }$ . Then $\phi _ { \alpha } \in \mathcal { N }$ , and $\phi _ { \alpha }  \psi$ uniformly on $[ a , b ]$ as $\alpha \searrow 0$ , i.e., $\forall \epsilon > 0$ there is $\eta > 0$ such that

$$
\left| \phi_ {\alpha} (x) - \psi (x) \right| <   \epsilon , \quad \forall x \in [ a, b ],
$$

whenever $0 < \alpha < \eta$

Proof: Using the argument in the proof of Proposition 2.1, we have

$$
\mathrm{ReLU} (x - x _ {m}) * \sigma_ {\alpha} ^ {\prime} (x) = \alpha \ln (1 + e ^ {(x - x _ {m}) / \alpha}) = \alpha \mathrm{sp} (\frac {x - x _ {m}}{\alpha}).
$$

Then

$$
\begin{array}{l} \phi_ {\alpha} (x) = (\psi * \sigma_ {\alpha} ^ {\prime}) (x) = c _ {0} * \sigma_ {\alpha} ^ {\prime} (x) + \sum_ {m = 1} ^ {M} c _ {m} \mathrm{ReLU} (x - x _ {m}) * \sigma_ {\alpha} ^ {\prime} (x) \\ \qquad = c _ {0} + \sum_ {m = 1} ^ {M} c _ {m} \alpha \mathrm{sp} (\frac {x - x _ {m}}{\alpha}). \end{array}\tag{2.10}
$$

Let $a _ { 0 } = c _ { 0 } , a _ { m } = c _ { m } \alpha , w = 1 / \alpha , b _ { m } = - x _ { m } / \alpha$ , then

$$
\phi_ {\alpha} (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \mathrm{sp} (w x + b _ {m}),
$$

so $\phi _ { \alpha } \in \mathcal { N }$

Moreover, by simple calculation we have $\mathrm { x s p } ( \frac { x - x _ { m } } { \alpha } )  \mathrm { R e L U } ( x - x _ { m } )$ as $\alpha \searrow 0$ for any $x \in [ a , b ]$ pointwise. And we can show that $\alpha \mathrm { s p } \big ( \frac { x - x _ { m } } { \alpha } \big )$ is an increasing function with respect to $\alpha$ . In fact,

$$
\frac {\mathrm{d}}{\mathrm{d} \alpha} \left(\alpha \mathrm{sp} (\frac {x - x _ {m}}{\alpha})\right) = \ln (1 + e ^ {\frac {x - x _ {m}}{\alpha}}) + \frac {- \frac {x - x _ {m}}{\alpha}}{1 + e ^ {- \frac {x - x _ {m}}{\alpha}}}.
$$

if $\textstyle { \frac { x - x _ { m } } { \alpha } } \leq 0$ , the last two terms are both positive, and so is $\begin{array} { r } { \frac { \mathrm { d } } { \mathrm { d } \alpha } \left( \alpha \mathrm { s p } \left( \frac { x - x _ { m } } { \alpha } \right) \right) ; \mathrm { i f } \frac { x - x _ { m } } { \alpha } > 0 } \end{array}$ 2

$$
\frac {\mathrm{d}}{\mathrm{d} \alpha} \left(\alpha \mathrm{sp} (\frac {x - x _ {m}}{\alpha})\right) > \ln (e ^ {\frac {x - x _ {m}}{\alpha}}) + \frac {- \frac {x - x _ {m}}{\alpha}}{1 + e ^ {- \frac {x - x _ {m}}{\alpha}}} = \frac {x - x _ {m}}{\alpha} \cdot \frac {e ^ {- \frac {x - x _ {m}}{\alpha}}}{1 + e ^ {- \frac {x - x _ {m}}{\alpha}}} > 0.
$$

Now let $( \alpha _ { k } ) _ { k }$ be any decreasing sequence converging to 0 as $k  \infty$ . Then $\left( \alpha _ { k } \mathrm { s p } ( \textstyle { \frac { x - x _ { m } } { \alpha _ { k } } } ) \right) _ { k }$ is a decreasing sequence of functions, i.e.

$$
\alpha_ {k + 1} \mathrm{sp} (\frac {x - x _ {m}}{\alpha_ {k + 1}}) \leq \alpha_ {k} \mathrm{sp} (\frac {x - x _ {m}}{\alpha_ {k}}).
$$

By Dini’s theorem (Theorem 4.1), $\alpha _ { k } \mathrm { s p } ( \textstyle { \frac { x - x _ { m } } { \alpha _ { \ell } } } ) \to \mathrm { R e L U } ( x - x _ { m } )$ uniformly on $[ a , b ]$ as $k  \infty$ α<sub>k</sub> Replacing $\alpha _ { k }$ with $\alpha ,$ we have that $\alpha \mathrm { s p } \big ( \frac { x - x _ { m } } { \alpha } \big )  \mathrm { R e L U } ( x - x _ { m } )$ uniformly on $[ a , b ]$ as $\alpha \searrow 0$ α

Consequently, it follows (2.10) that $\phi _ { \alpha } ( x )  \psi ( x )$ uniformly on $[ a , b ]$ as $\alpha \searrow 0$ , because the linear combination of uniformly convergent sequences is also uniformly convergent. □

Finally, we have the following result.

Theorem 2.9 The set N given by (2.9) is dense in $C ( [ a , b ] )$ : for any $f \in C ( [ a , b ] )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {\infty} = 0.
$$

Proof: Given $\epsilon > 0$ , by Theorem 2.8, there is a ReLU network $\begin{array} { r } { \psi = c _ { 0 } + \sum _ { m = 1 } ^ { M } c _ { m } \mathrm { R e L U } ( x - x _ { m } ) } \end{array}$ such that

$$
| f (x) - \psi (x) | <   \frac {\epsilon}{2}, \quad \forall x \in [ a, b ].\tag{2.11}
$$

By Proposition 2.2, there is a softplus network $\phi _ { \alpha } \in \mathcal { N }$ with α suficiently small such that

$$
| \psi (x) - \phi_ {\alpha} (x) | <   \frac {\epsilon}{2}, \quad \forall x \in [ a, b ].\tag{2.12}
$$

Combining (2.11) and (2.12) leads to

$$
| f (x) - \phi_ {\alpha} (x) | <   \epsilon , \quad \forall x \in [ a, b ],\tag{2.13}
$$

which completes the proof.

## 2.2 Universal Approximation in Multi-dimension

In this section, we investigate the neural network approximation in multi-dimension. Denote the unit hypercube in $\mathbb { R } ^ { d }$ by $I _ { d } .$ , i.e. $I _ { d } = [ 0 , 1 ] ^ { d }$ . Let us see how and why neural networks can approximate functions defined on $I _ { d }$ . Define the set of two-layer neural network without bias in the output layer as follows.

$$
\mathcal {N} = \left\{\phi : I _ {d} \to \mathbb {R}, \phi (x) = \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}): w _ {m} \in \mathbb {R} ^ {d}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {Z} ^ {+} \right\},\tag{2.14}
$$

where $\sigma$ is some activation function in the hidden layer.

## 2.2.1 Approximating continuous functions

Before the development of the main results, some preliminary results of functional analysis are needed. The first lemma states that for a non-dense subspace, there exists a functional that vanishes on the subspace and has a nonzero value outside of the subspace.

Lemma 2.1 Let U be a linear subspace of a normed linear space X . Let $x _ { 0 } \in \mathcal { X }$ such that

$$
\mathrm{dist} (x _ {0}, \mathcal {U}) := \inf _ {u \in \mathcal {U}} \| u - x _ {0} \| _ {\mathcal {X}} \geq \delta
$$

for some $\delta > 0$ . Then there exists a bounded linear functional ℓ on $\mathcal { X }$ such that

(i) $\| \ell \| _ { \mathcal { X } ^ { * } } \leq 1$ ;

(ii) $\ell ( u ) = 0 , \forall u \in \mathcal { U } ;$

(iii) $\ell ( x _ { 0 } ) = \delta .$

Proof: Consider the linear space $\tau$ spanned by U and $x _ { 0 }$ , i.e.

$$
\mathcal {T} = \{y \in \mathcal {X}: y = u + \lambda x _ {0}, u \in \mathcal {U}, \lambda \in \mathbb {R} \},
$$

and define the operator $\ell : \mathcal T \to \mathbb { R }$ by

$$
\ell (u + \lambda x _ {0}) = \lambda \delta , \quad \forall u + \lambda x _ {0} \in \mathcal {T}.
$$

It is trivial to show that ℓ is a linear functional. We first prove that $\ell ( y ) \leq \| y \| _ { \mathcal { X } }$ for all $y \in \mathcal T$ . Let $y = u + \lambda x _ { 0 } \in \mathcal { T }$ . If $\lambda = 0$ , then $\ell ( y ) = 0$ and the result is trivial. Otherwise, $- \lambda ^ { - 1 } u \in \mathcal { U }$ since $u \in \mathcal { U } .$ . By the hypothesis,

$$
\| x _ {0} + \lambda^ {- 1} u \| _ {\mathcal {X}} = \| x _ {0} - (- \lambda^ {- 1} u) \| _ {\mathcal {X}} \geq \delta .
$$

Then

$$
\ell (y) = \lambda \delta \leq | \lambda | \delta \leq | \lambda | \| x _ {0} + \lambda^ {- 1} u \| _ {\mathcal {X}} = \| \lambda x _ {0} + u \| _ {\mathcal {X}} = \| y \| _ {\mathcal {X}}.
$$

Applying the Hahn-Banach Theorem, we obtain that ℓ can be extended to a linear functional (still denoted by $\ell )$ on X such that

$$
\ell (x) \leq \| x \| _ {\mathcal {X}}, \forall x \in \mathcal {X}.
$$

Therefore $\begin{array} { r } { \| \ell \| _ { \mathcal { X } ^ { * } } = \operatorname* { s u p } _ { x \in \mathcal { X } } \frac { \ell ( x ) } { \| x \| _ { \mathcal { X } } } \leq 1 } \end{array}$ . From the definition of $\ell ,$ we also have

$$
\ell (u) = \ell (u + 0 \cdot x _ {0}) = 0 \cdot \delta = 0, \quad \forall u \in \mathcal {U},
$$

and

$$
\ell (x _ {0}) = \ell (0 + 1 \cdot x _ {0}) = 1 \cdot \delta = \delta ,
$$

which proves the lemma.

Now suppose U is a non-dense linear subspace of X. It implies that there is some $x _ { 0 } \in \mathcal { X }$ such that dis $( x _ { 0 } , \mathcal { U } ) > 0$ . By Lemma 2.1, we directly have

Lemma 2.2 Let U be a non-dense linear subspace of a normed linear space X . Then there exists a bounded linear functional ℓ on X such that

(i) $\ell \neq 0 \ o n \ \mathcal { X } ;$

(ii) $\ell ( u ) = 0 , \forall u \in \mathcal { U } .$

Recall that $C ( I _ { d } )$ denotes the linear space of continuous functions on the hypercube $I _ { d } .$ , and it is a normed space with the norm

$$
\| f \| _ {\infty} = \sup _ {x \in I _ {d}} | f (x) |, \quad \forall f \in C (I _ {d}).
$$

Besides, following the definition $( 1 . 4 ) , \ B ( I _ { d } )$ denotes the space of finite signed Borel measures supported on $I _ { d } .$ . Then the next result states that there is always a signed measure in $B ( I _ { d } )$ that vanishes on a non-dense subspace of $C ( I _ { d } )$

Lemma 2.3 Let U be a non-dense linear subspace of $C ( I _ { d } )$ . Then there is a measure $\mu \in \mathcal { B } ( I _ { d } )$ such that $\mu \neq 0$ and

$$
\int_ {I _ {d}} u \mathrm{d} \mu = 0, \quad \forall u \in \mathcal {U}.
$$

Proof: Considering $\textstyle { \mathcal { X } } = C ( I _ { d } )$ in Lemma 2.2, there is a bounded linear functional $\ell : C ( I _ { d } ) \to$ R such that $\ell \neq 0$ on $C ( I _ { d } )$ and $\ell | _ { \mathcal { U } } = 0$ . By Riesz-Markov-Kakutani representation theorem 4.3, there exists a unique measure $\mu \in \mathcal { B } ( I _ { d } )$ such that $\begin{array} { r } { \ell ( f ) = \int _ { I _ { d } } f ( x ) \mathrm { d } \mu ( x ) } \end{array}$ for all $f \in C ( I _ { d } )$ . Since $\ell \neq 0 , \mu \neq 0$ . And for all $u \in \mathcal { U }$ 2

$$
\int_ {I _ {d}} u \mathrm{d} \mu = \ell (u) = 0,
$$

which is the desired result.

Now we move to the density of two-layer neural networks with discriminatory activation functions (see the definition in Section 1.1.2). The following result holds.

Theorem 2.10 Let $\sigma$ be a continuous discriminatory function for all measures in $B ( I _ { d } )$ . Then the set $\mathcal { N }$ given by (2.14) is dense in $C ( I _ { d } )$ : for any $f \in C ( I _ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {\infty} = 0.
$$

Proof: Since $\sigma$ is continuous, it follows that $\mathcal { N }$ is a subspace of $C ( I _ { d } )$ . We can finish the proof by contradiction.

Assume that $\mathcal { N }$ is not dense in $C ( I _ { d } )$ . By Lemma 2.3, there is a nonzero measure $\mu \in \mathcal { B } ( I _ { d } )$ such that

$$
\int_ {I _ {d}} \phi \mathrm{d} \mu = 0, \quad \forall \phi \in \mathcal {N}.
$$

Namely,

$$
\sum_ {m = 1} ^ {M} a _ {m} \int_ {I _ {d}} \sigma (w _ {m} ^ {\top} x + b _ {m}) \mathrm{d} \mu = 0, \quad \forall w _ {m} \in \mathbb {R} ^ {d}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {Z} ^ {+}.
$$

Specifically, letting $M = 1$ and $a _ { m } { = } 1$ , we have

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) \mathrm{d} \mu = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R}.
$$

Using that $\sigma$ is discriminatory, we obtain $\mu = 0$ , which is a contradiction.

Combining Theorem 2.10 and Theorem 1.1, it directly follows that

Proposition 2.3 (Cybenko, 1989) The set N given by (2.14) with continuous sigmoidal function σ is dense in $C ( I _ { d } )$

The next result of density weakens the requirement of the activation function, but adopts a more complicated network architecture. Diferent from the neural networks in (2.14) that are finite sums of activation neurons, the next result takes finite sums of finite products of several activation neurons.

Theorem 2.11 (Hornik, Stinchcombe, White, 1989) Let $\sigma$ be any continuous nonconstant activation function. Then the following set

$$
\widetilde {\mathcal {N}} = \left\{\phi : I _ {d} \to \mathbb {R}, \phi (x) = \sum_ {m = 1} ^ {M} a _ {m} \prod_ {n = 1} ^ {N _ {m}} \sigma (w _ {m n} ^ {\top} x + b _ {m n}): w _ {m n} \in \mathbb {R} ^ {d}, a _ {m}, b _ {m n} \in \mathbb {R}, M, N _ {m} \in \mathbb {Z} ^ {+} \right\}
$$

is dense in $C ( I _ { d } )$

Proof: The proof can be done by Stone-Weierstrass theorem (Theorem 2.1). First, we can verify $\widetilde { \mathcal { N } }$ is a subalgebra of $C ( I _ { d } )$ . In fact, for any $\phi \in \widetilde { \mathcal { N } }$ and $\lambda \in \mathbb { R }$

$$
\lambda f \in \widetilde {\mathcal {N}}.
$$

And for any $\phi _ { 1 } , \phi _ { 2 } \in \widetilde { \mathcal { N } }$

$$
\phi_ {1} + \phi_ {2} \in \widetilde {\mathcal {N}}, \quad \phi_ {1} \phi_ {2} \in \widetilde {\mathcal {N}}.
$$

Also, since $\sigma$ is not constant zero, there exists some $\xi \in \mathbb { R }$ such that $\sigma ( \boldsymbol { \xi } ) \neq 0$ Let $N = 1 , a _ { n } = 1$ $M _ { 1 } = 1$ , w = [0, . . . , 0] ∈ R<sup>d</sup> and $b _ { 1 1 } = \xi$ , then $\phi ( x ) = \sigma ( \xi )$ which is a non-zero constant. So $\widetilde { \mathcal { N } }$ contains a non-zero constant function.

Moreover, since σ is nonconstant, there exist $c _ { 1 } , c _ { 2 } \in \mathbb { R }$ such that $\sigma ( c _ { 1 } ) \neq \sigma ( c _ { 2 } )$ . Let $x _ { 1 } , x _ { 2 } \in I _ { d } .$ $x _ { 1 } \neq x _ { 2 }$ . Then the linear system with unknowns w and $b ,$

$$
\left\{ \begin{array}{l} x _ {1} ^ {\top} w + b = c _ {1}, \\ x _ {2} ^ {\top} w + b = c _ {2}, \end{array} \right.
$$

always admits solutions. Denote one solution as $w = \hat { w } , b = \hat { b }$ , and let $\phi = \sigma ( \hat { w } ^ { \top } x + \hat { b } ) \in \widetilde { \mathcal { N } }$ , then $\phi ( x _ { 1 } ) = \sigma ( c _ { 1 } ) \neq \sigma ( c _ { 2 } ) = \phi ( x _ { 2 } )$ . So $\widetilde { \mathcal { N } }$ separates points of $I _ { d }$ .

Applying now Stone-Weierstrass Theorem, it follows that $\widetilde { \mathcal { N } }$ is dense in $C ( I _ { d } )$ , which ends the proof of the theorem. □

## 2.2.2 Approximating $L ^ { 2 } \mathbf { \cdot }$ -functions

We consider the density of two-layer neural networks in $L ^ { 2 } ( I _ { d } )$ , the space of square-integrable functions on $I _ { d } .$ . In this case, we characterize the magnitude of functions by $L ^ { 2 }$ norm, i.e.

$$
\| f \| _ {2} = \left(\int_ {I _ {d}} | f (x) | ^ {2} \mathrm{d} x\right) ^ {1 / 2}, \quad \forall f \in L ^ {2} \left(I _ {d}\right).
$$

First, we say a measurable function σ is discriminatory in $L ^ { 2 } .$ -sense on $I _ { d }$ if

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R} \quad \text { for   some } p \in L ^ {2} (I _ {d}) \quad \Longrightarrow \quad p = 0, \text { a.e. }
$$

Then we have the following density result.

Theorem 2.12 Suppose σ is discriminatory in $L ^ { 2 }$ -sense on $I _ { d } ,$ and $\sigma ( t )$ is bounded on $\mathbb { R }$ . Then the set $\mathcal { N }$ given by (2.14) with activation function σ is dense in $L ^ { 2 } ( I _ { d } )$ : for any $g \in L ^ { 2 } ( I _ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {2} = 0.
$$

Proof: We prove it by contradiction. Since σ is bounded, any $\begin{array} { r } { \phi ( x ) = \sum _ { m = 1 } ^ { M } a _ { m } \sigma ( w _ { m } ^ { \top } x + b _ { m } ) } \end{array}$ in $\mathcal { N }$ is square-integrable on $I _ { d } .$ . So $\mathcal { N }$ is a subspace of $L ^ { 2 } ( I _ { d } )$ . Assume that $\mathcal { N }$ is not dense in $L ^ { 2 } ( I _ { d } )$ By Lemma 2.2, there is a bounded linear functional ℓ on $L ^ { 2 } ( I _ { d } )$ such that $\ell \neq 0$ on $L ^ { 2 } ( I _ { d } )$ and $\ell | _ { \mathcal { N } } = 0$ . By Riesz representation theorem, there is a non-zero function $p \in L ^ { 2 } ( I _ { d } )$ such that

$$
\ell (f) = \int_ {I _ {d}} f (x) p (x) \mathrm{d} x, \quad \forall f \in L ^ {2} (I _ {d}).
$$

The condition $\ell | _ { \mathcal { N } } = 0$ implies that

$$
\int_ {I _ {d}} \phi (x) p (x) \mathrm{d} x = 0, \quad \forall \phi \in \mathcal {N}.
$$

In particular,

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R}.
$$

By the hypothesis that $\sigma$ is discriminatory in $L ^ { 2 } \mathrm { - s e n s e }$ , we have $p = 0 ~ { \mathrm { a . e } } .$ ., which is contradictory to that $p$ is non-zero. □

To illustrate which type of activation functions is discriminatory in $L ^ { 2 } .$ -sense, we first introduce the following result.

Lemma 2.4 Let $p \in L ^ { 2 } ( I _ { d } )$ such that $\begin{array} { r } { \int _ { H _ { w , \theta } \cap I _ { d } } p ( x ) \mathrm { d } x = 0 } \end{array}$ for any half-space $H _ { w , \theta } = \{ x \in \mathbb { R } ^ { d }$ $w ^ { \top } x + \theta > 0 \}$ . Then $p = 0$ almost everywhere.

Proof: We define the extension of $p$ on $\mathbb { R } ^ { d }$ by

$$
p _ {\mathrm{e}} (x) = \left\{ \begin{array}{l l} p (x), & x \in I _ {d}, \\ 0, & x \in \mathbb {R} ^ {d} \backslash I _ {d}. \end{array} \right.
$$

It sufices to prove the Fourier transform of $p _ { \mathrm { e } }$ is zero, i.e.

$$
\widehat {p} _ {\mathrm{e}} (w) := \int_ {\mathbb {R} ^ {d}} e ^ {- \mathrm{i} w ^ {\top} x} p _ {\mathrm{e}} (x) \mathrm{d} x = \int_ {I _ {d}} e ^ {- \mathrm{i} w ^ {\top} x} p (x) \mathrm{d} x = \int_ {I _ {d}} \cos (w ^ {\top} x) p (x) \mathrm{d} x - \mathrm{i} \int_ {I _ {d}} \sin (w ^ {\top} x) p (x) \mathrm{d} x \equiv 0.
$$

Now let us prove $\begin{array} { r } { \int _ { I _ { d } } \cos ( w ^ { \top } x ) p ( x ) \mathrm { d } x = 0 } \end{array}$ for all $w \in \mathbb { R } ^ { d }$

We fix $w \in \mathbb { R } ^ { d }$ . For any characteristic function $1 _ { ( \theta , \infty ) } ( t )$ 2

$$
\int_ {I _ {d}} 1 _ {(\theta , \infty)} (w ^ {\top} x) p (x) \mathrm{d} x = \int_ {\{w ^ {\top} x > \theta \} \cap I _ {d}} p (x) \mathrm{d} x = \int_ {H _ {w, - \theta} \cap I _ {d}} p (x) \mathrm{d} x = 0.
$$

Similarly,

$$
\int_ {I _ {d}} 1 _ {[ \theta , \infty)} (w ^ {\top} x) p (x) \mathrm{d} x = 0.
$$

since the hyperplane $\{ x : w ^ { \top } x = \theta \}$ has zero measure. By linearity, for any interval $A \subset \mathbb { R }$

$$
\int_ {I _ {d}} 1 _ {A} (w ^ {\top} x) p (x) \mathrm{d} x = 0.
$$

Therefore, for any step function $\begin{array} { r } { \phi ( t ) = \sum _ { j = 1 } ^ { J } \alpha _ { j } \boldsymbol { 1 } _ { A _ { j } } ( t ) } \end{array}$ where $\alpha _ { j } \in \mathbb { R }$ and $A _ { j }$ are intervals, it follows that

$$
\int_ {I _ {d}} \phi (w ^ {\top} x) p (x) \mathrm{d} x = \sum_ {j = 1} ^ {J} \alpha_ {j} \int_ {I _ {d}} 1 _ {A _ {j}} (w ^ {\top} x) p (x) \mathrm{d} x = 0.
$$

On the other hand, note that $| w ^ { \top } x | \leq \| w \| \| x \| \leq \sqrt { d } \| w \|$ for any $x \in \ I _ { d }$ . Since $\cos ( t )$ is uniformly continuous on $[ - \sqrt { d } \| w \| , \sqrt { d } \| w \| ]$ , using similar argument as in the proof of Theorem

2.6, we can show that there is a sequence of step functions $\phi _ { n } ( t )$ on $[ - { \sqrt { d } } \| w \| , { \sqrt { d } } \| w \| ]$ such that $\phi _ { n } ( t )  \cos ( t )$ uniformly as $n  \infty ,$ i.e.

$$
\| \cos (t) - \phi_ {n} (t) \| _ {\infty} := \max _ {t \in [ - \sqrt {d} \| w \|, \sqrt {d} \| w \| ]} | \cos (t) - \phi_ {n} (t) | \to 0.
$$

Consequently,

$$
\begin{array}{r l} & {\left| \int_ {I _ {d}} \cos (w ^ {\top} x) p (x) \mathrm{d} x \right| = \left| \int_ {I _ {d}} \cos (w ^ {\top} x) p (x) \mathrm{d} x - \int_ {I _ {d}} \phi_ {n} (w ^ {\top} x) p (x) \mathrm{d} x \right|} \\ & {\qquad \leq \int_ {I _ {d}} \left| \cos (w ^ {\top} x) - \phi_ {n} (w ^ {\top} x) \right| | p (x) | \mathrm{d} x} \\ & {\qquad \leq \| \cos (t) - \phi_ {n} (t) \| _ {\infty} \int_ {I _ {d}} | p (x) | \mathrm{d} x \leq \| \cos (t) - \phi_ {n} (t) \| _ {\infty} \| p \| _ {2} \to 0,} \end{array}
$$

where Cauchy-Schwarz inequality is used in the last inequality. So $\begin{array} { r } { \int _ { I _ { d } } \cos ( w ^ { \top } x ) p ( x ) \mathrm { d } x = 0 } \end{array}$

By similar argument, we can show $\begin{array} { r } { \int _ { I _ { d } } \sin ( w ^ { \top } x ) p ( x ) \mathrm { d } x = 0 } \end{array}$ , which ends the proof.

Example 2.3 The Heaviside function $H ( t ) = { \left\{ \begin{array} { l l } { 1 , } & { { \mathrm { i f ~ } } t \geq 0 , } \\ { 0 , } & { { \mathrm { i f ~ } } t < 0 , } \end{array} \right. }$ is discriminatory in $L ^ { 2 } .$ -sense on $I _ { d }$ Let $p \in L ^ { 2 } ( I _ { d } )$ and assume

$$
\int_ {I _ {d}} H (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R}.
$$

Equivalently,

$$
\int_ {H _ {w, b} \cap I _ {d}} p (x) \mathrm{d} x = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R},
$$

which implies $p = 0 { \mathrm { ~ a . e . } }$ , by Lemma 2.4. Hence $H ( x )$ is discriminatory in $L ^ { 2 } \mathrm { - s e n s e }$

Example 2.4 The logistic function $\begin{array} { r } { \sigma ( t ) = \frac { 1 } { 1 + e ^ { - t } } } \end{array}$ is discriminatory in $L ^ { 2 } \mathrm { - s e n s e }$ on $I _ { d }$

We fix $w \in \mathbb { R } ^ { d } , b \in \mathbb { R }$ and let $\sigma _ { n } ( x ) = \sigma ( n ( w ^ { \top } x + b ) )$ for $n = 1 , 2 , \ldots$ . Define

$$
\gamma (x) = \left\{ \begin{array}{l l} 1, & w ^ {\top} x + b > 0, \\ 1 / 2, & w ^ {\top} x + b = 0, \\ 0, & w ^ {\top} x + b <   0. \end{array} \right.
$$

Then

$$
\begin{array}{r l} & {\| \sigma_ {n} - \gamma \| _ {2} ^ {2} = \int_ {I _ {d}} | \sigma_ {n} (x) - \gamma (x) | ^ {2} \mathrm{d} x} \\ & {\qquad = \int_ {H _ {w, b} \cap I _ {d}} | \sigma_ {n} (x) - 1 | ^ {2} \mathrm{d} x + \int_ {H _ {- w, - b} \cap I _ {d}} | \sigma_ {n} (x) | ^ {2} \mathrm{d} x} \\ & {\qquad = \int_ {H _ {w, b} \cap I _ {d}} \frac {1}{(1 + e ^ {n (w ^ {\top} x + b)}) ^ {2}} \mathrm{d} x + \int_ {H _ {- w, - b} \cap I _ {d}} \frac {1}{(1 + e ^ {- n (w ^ {\top} x + b)}) ^ {2}} \mathrm{d} x.} \end{array}
$$

Note that

$$
\frac {1}{(1 + e ^ {n (w ^ {\top} x + b)}) ^ {2}} \rightarrow 0, \quad \forall x \in H _ {w, b} \cap I _ {d}
$$

and

$$
\frac {1}{(1 + e ^ {- n (w ^ {\top} x + b)}) ^ {2}} \to 0, \quad \forall x \in H _ {- w, - b} \cap I _ {d},
$$

as $n  \infty$ . Since $\begin{array} { r } { \left| \frac { 1 } { ( 1 + e ^ { n ( w ^ { \top } x + b ) } ) ^ { 2 } } \right| < 1 } \end{array}$ and $\left| \frac { 1 } { ( 1 + e ^ { - n ( w ^ { \top } x + b ) } ) ^ { 2 } } \right| < 1$ , by the bounded convergence theorem,

$$
\int_ {H _ {w, b} \cap I _ {d}} \frac {1}{(1 + e ^ {n (w ^ {\top} x + b)}) ^ {2}} \mathrm{d} x \to 0,
$$

and

$$
\int_ {H _ {- w, - b} \cap I _ {d}} \frac {1}{(1 + e ^ {- n (w ^ {\top} x + b)}) ^ {2}} \mathrm{d} x \to 0.
$$

So $\| { \sigma } _ { n } - { \gamma } \| _ { 2 } \to 0$

Now let $p \in L ^ { 2 } ( I _ { d } )$ and assume

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R}.
$$

In particular, for any $w \in \mathbb { R } ^ { d }$ and $b \in \mathbb { R }$

$$
\int_ {I _ {d}} \sigma_ {n} (x) p (x) \mathrm{d} x = \int_ {I _ {d}} \sigma (n (w ^ {\top} x + b)) p (x) \mathrm{d} x = \int_ {I _ {d}} \sigma ((n w) ^ {\top} x + n b) p (x) \mathrm{d} x = 0.
$$

Then by Cauchy-Schwarz inequality,

$$
\begin{array}{l} \left| \int_ {H _ {w, b} \cap I _ {d}} p (x) \mathrm{d} x \right| = \left| \int_ {I _ {d}} \gamma (x) p (x) \mathrm{d} x \right| = \left| \int_ {I _ {d}} \gamma (x) p (x) \mathrm{d} x - \int_ {I _ {d}} \sigma_ {n} (x) p (x) \mathrm{d} x \right| \\ \qquad \leq \int_ {I _ {d}} | \gamma (x) - \sigma_ {n} (x) | | p (x) | \mathrm{d} x \leq \| \gamma - \sigma_ {n} \| _ {2} \| p \| _ {2} \to 0, \end{array}
$$

so $\begin{array} { r } { \int _ { H _ { w , b } \cap I _ { d } } p ( x ) \mathrm d x = 0 ; } \end{array}$ ; note that it holds for all half-space $H _ { w , b }$ . By Lemma 2.4, $p = 0 ~ \mathrm { a . e }$ . Hence the logistic function is discriminatory in $L ^ { 2 } .$ -sense.

## 2.2.3 Approximating L<sup>1</sup>-functions

We continue to consider the density in $L ^ { 1 } ( I _ { d } )$ , the space of integrable functions on $I _ { d } ,$ which is associated with the norm

$$
\| f \| _ {1} = \int_ {I _ {d}} | f (x) | \mathrm{d} x, \quad \forall f \in L ^ {1} (I _ {d}).
$$

Similar to the discussion in the last section, we can define discriminatory functions in $L ^ { 1 }$ -sense. We say a measurable function $\sigma$ is discriminatory in L<sup>1</sup>-sense on $I _ { d }$ if

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R} \quad \text { for   some } p \in L ^ {\infty} (I _ {d}) \quad \Longrightarrow \quad p = 0, \text { a.e. }
$$

And we have the following result.

Theorem 2.13 Suppose $\sigma$ is discriminatory in $L ^ { 1 } { - } s e n s e$ on ${ \cal I } _ { d _ { \it \perp } }$ , and $\sigma ( t )$ is bounded on $\mathbb { R }$ . Then the set $\mathcal { N }$ given by (2.14) with activation function σ is dense in $L ^ { 1 } ( I _ { d } )$ : for any $f \in L ^ { 1 } ( I _ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N}} \| \phi - f \| _ {1} = 0.
$$

Proof: The proof is similar to the one given for Theorem 2.12. Since σ is bounded, any $\phi ( x ) = $ $\begin{array} { r } { \sum _ { m = 1 } ^ { M } a _ { m } \sigma ( w _ { m } ^ { \top } x + b _ { m } ) } \end{array}$ in $\mathcal { N }$ is integrable on $I _ { d } .$ . So $\mathcal { N }$ is a subspace of $L ^ { 1 } ( I _ { d } )$ . Assume that $\mathcal { N }$ is not dense in $L ^ { 1 } ( I _ { d } )$ . By Lemma 2.2, there is a bounded linear functional ℓ on $L ^ { 1 } ( I _ { d } )$ such that $\ell \neq 0$ on $L ^ { 1 } ( I _ { d } )$ and $\ell | _ { \mathcal { N } } = 0$ . By Riesz representation theorem, there is a non-zero function $p$ in $L ^ { \infty } ( I _ { d } )$ , the dual space of $L ^ { 1 } ( I _ { d } )$ , such that

$$
\ell (f) = \int_ {I _ {d}} f (x) p (x) \mathrm{d} x, \quad \forall f \in L ^ {1} (I _ {d}).
$$

The condition $\ell | _ { \mathcal { N } } = 0$ implies that

$$
\int_ {I _ {d}} \phi (x) p (x) \mathrm{d} x = 0, \quad \forall \phi \in \mathcal {N}.
$$

In particular,

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + b) p (x) \mathrm{d} x = 0, \quad \forall w \in \mathbb {R} ^ {d}, b \in \mathbb {R}.
$$

By the hypothesis that $\sigma$ is discriminatory in $L ^ { 1 } \mathrm { - s e n s e } ,$ we have $p = 0 ~ { \mathrm { a . e . } }$ ., which is contradictory to that $p$ is non-zero. □

Example 2.5 The logistic function $\begin{array} { r } { \sigma ( t ) = \frac { 1 } { 1 + e ^ { - t } } } \end{array}$ is discriminatory in $L ^ { 1 } .$ -sense on $I _ { d }$ This fact can be proved using similar argument as in Example 2.4.

## 2.2.4 Approximating measurable functions

In the end, we consider the neural network approximation towards measurable functions that are finite almost everywhere. For simplicity, we consider Borel measurable functions<sup>1</sup>. We use $\mathcal { M } ( \mathbb { R } ^ { d } )$ to denote the space of all Borel-measurable functions from $\mathbb { R } ^ { d }$ to R. Also, we use $B ( \mathbb { R } ^ { d } )$ to denote the space of all Borel probability measures; namely, for any $\mu \in { \mathcal { B } } ( \mathbb { R } ^ { d } ) , \mu : { \mathcal { B } } \to [ 0 , 1 ]$ , where B is the Borel σ-algebra of $\mathbb { R } ^ { d }$ , such that

$$
\mu (\varnothing) = 0, \quad \mu (\mathbb {R} ^ {d}) = 1,
$$

and $\mu$ satisfies the countable additivity. In this section, we make the remark that all functions in $\mathcal { M } ( \mathbb { R } ^ { d } )$ are considered to be finite almost everywhere with respect to any $\mu \in \mathcal { B } ( \mathbb { R } ^ { d } )$ , i.e., $\mu \{ x \in \mathbb { R } ^ { d } : | f ( x ) | = \infty \} = 0$

Given $\mu \in B ( \mathbb { R } ^ { d } )$ , then $\mathcal { M } ( \mathbb { R } ^ { d } )$ is a metric space with the following metric

$$
d _ {\mu} (f, g) = \inf \{\epsilon > 0: \mu (| f - g | > \epsilon) <   \epsilon \}, \quad \forall f, g \in \mathcal {M} (\mathbb {R} ^ {d}).
$$

Note that the triangle inequality holds:

$$
d _ {\mu} (f, g) \leq d _ {\mu} (f, h) + d _ {\mu} (h, g), \quad \forall f, g, h \in \mathcal {M} (\mathbb {R} ^ {d}).\tag{2.15}
$$

There are a few equivalent convergence properties of the metric $d _ { \mu }$ .

Lemma 2.5 Let $( f _ { n } ) _ { n } \subset \mathcal { M } ( \mathbb { R } ^ { d } ) , f \in \mathcal { M } ( \mathbb { R } ^ { d } )$ . The following statements are equivalent:

(a) $d _ { \mu } ( f _ { n } , f ) \to 0 , n \to \infty ;$

(b) For any $\epsilon > 0 , \mu ( \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon \} \to 0 , n \to \infty ;$

(c) $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \operatorname* { m i n } ( | f _ { n } ( x ) - f ( x ) | , 1 ) \mathrm { d } \mu ( x ) \to 0 , n \to \infty . } \end{array}$

Proof: $( \mathrm { a } ) \Longrightarrow ( \mathrm { b } )$ We prove it by contradiction. Assume (b) does not hold, then there are $\epsilon _ { 0 } , \epsilon _ { 1 } > 0$ such that $\mu \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon _ { 0 } \} > \epsilon _ { 1 }$ for infinitely many n.

• If $\epsilon _ { 1 } > \epsilon _ { 0 }$ , then $\mu \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon _ { 0 } \} > \epsilon _ { 0 } ;$

• If $\epsilon _ { 1 } \leq \epsilon _ { 0 }$ , then $\mu \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon _ { 1 } \} > \mu \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon _ { 0 } \} > \epsilon _ { 1 } .$

So in a word, there is some $\epsilon ^ { \prime } > 0$ such that

$$
\mu \{x: | f _ {n} (x) - f (x) | > \epsilon^ {\prime} \} > \epsilon^ {\prime}
$$

for infinitely many $n .$

On the other hand, (a) implies that for any $\epsilon ^ { \prime } > 0$ , there are only finite n such that $d _ { \mu } ( f _ { n } , f ) > \epsilon ^ { \prime }$ 2 i.e.

$$
\inf \{\epsilon > 0: \mu (| f _ {n} - f | > \epsilon) <   \epsilon \} > \epsilon^ {\prime},
$$

which implies $\epsilon ^ { \prime } \notin \{ \epsilon > 0 : \mu ( | f _ { n } - f | > \epsilon ) < \epsilon \}$ . So it satisfies that

$$
\mu \{x: | f _ {n} (x) - f (x) | > \epsilon^ {\prime} \} \geq \epsilon^ {\prime}.\tag{2.16}
$$

In a word, for any $\epsilon ^ { \prime } > 0$ , (2.16) holds for only finite $n _ { \mathrm { : } }$ , which is contradictory to the above discussion.

$( \mathrm { b } ) \Longrightarrow ( \mathrm { a } )$ For any $\epsilon ^ { \prime } > 0 , \mu \{ x : | f _ { n } ( x ) - f ( x ) | > \epsilon ^ { \prime } \}  0 .$ , so

$$
\mu \{x: | f _ {n} (x) - f (x) | > \epsilon^ {\prime} \} <   \epsilon^ {\prime}
$$

for suficiently large n. This implies $\epsilon ^ { \prime } \in \lbrace \epsilon > 0 : \mu ( | f _ { n } - f | > \epsilon ) < \epsilon \rbrace$ , so

$$
\inf \{\epsilon > 0: \mu (| f _ {n} - f | > \epsilon) <   \epsilon \} \leq \epsilon^ {\prime}.\tag{2.17}
$$

In a word, for any $\epsilon ^ { \prime } > 0 , ( 2 . 1 7 )$ holds for suficiently large $n ,$ which is exactly (a).

$( \mathrm { c } ) \Longrightarrow ( \mathrm { b } )$ For any $0 < \epsilon < 1$ , the following inequality holds,

$$
\epsilon 1 _ {(\epsilon , + \infty)} (t) \leq \min (t, 1) \leq \epsilon + 1 _ {(\epsilon , + \infty)} (t), \quad \forall t \geq 0.\tag{2.18}
$$

Replacing in (2.18) the variable t by $| f _ { n } ( x ) - f ( x ) |$ , integrating with respect to $\mu$ and using that

$$
\int_ {\mathbb {R} ^ {d}} 1 _ {| f _ {n} (x) - f (x) | > \epsilon} \mathrm{d} \mu (x) = \mu \{x: | f _ {n} (x) - f (x) | > \epsilon \},
$$

we obtain

$$
\epsilon \mu \{x: | f _ {n} (x) - f (x) | > \epsilon \} \leq \int_ {\mathbb {R} ^ {d}} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x)\tag{2.19}
$$

$$
\epsilon + \mu \{x: | f _ {n} (x) - f (x) | > \epsilon \} \geq \int_ {\mathbb {R} ^ {d}} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x).\tag{2.20}
$$

Now, if (c) holds, inequality (2.19) implies (b).

(b) =⇒ (c) If (b) holds, then inequality (2.20) provides

$$
\epsilon \geq \lim _ {n \rightarrow \infty} \int_ {\mathbb {R} ^ {d}} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x)
$$

for all $\epsilon \in ( 0 , 1 )$ . So the limit on the right has to be zero; hence (c) holds.

The uniform convergence and the d<sub>µ</sub>-convergence are related by the following result:

Proposition 2.4 Let $( f _ { n } ) _ { n }$ be a sequence of functions in $\mathcal { M } ( \mathbb { R } ^ { d } )$ that converges uniformly on all compact sets to $f ,$ i.e. $\forall K \subset \mathbb { R } ^ { d }$ compact,

$$
\sup _ {x \in K} | f _ {n} (x) - f (x) | \to 0, \quad n \to \infty .
$$

Then $d _ { \mu } ( f _ { n } , f ) \to 0$ , as $n \to \infty$

Proof: Given any $\epsilon > 0$ . Let $K \subset \mathbb { R } ^ { d }$ be a compact set such that $\mu ( \mathbb { R } ^ { d } \backslash K ) < \epsilon / 2$ . Such a compact set always exists. For example, let $B _ { r } = \{ x \in \mathbb { R } ^ { d } : \| x \| \leq r \}$ be the closed ball centered at origin with radius r. Since

$$
\mathbb {R} ^ {d} = \bigcup_ {r = 1} ^ {\infty} B _ {r} = \limsup _ {r \to \infty} B _ {r},
$$

it follows that $1 = \mu ( \mathbb { R } ^ { d } ) = \operatorname* { l i m } _ { r \to \infty } \mu ( B _ { r } )$ . So $\mu ( \mathbb { R } ^ { d } \backslash B _ { r } ) < \epsilon / 2$ when r is suficiently large.

Since $\begin{array} { r } { \operatorname* { s u p } _ { x \in K } | f _ { n } ( x ) - f ( x ) |  0 } \end{array}$ , for the preceding ϵ, there is some $N > 0$ such that

$$
\sup _ {x \in K} | f _ {n} (x) - f (x) | <   \epsilon / 2, \quad \text { if } n > N.
$$

Therefore,

$$
\begin{array}{l} \int_ {\mathbb {R} ^ {d}} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x) \\ = \int_ {K} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x) + \int_ {\mathbb {R} ^ {d} \setminus K} \min (| f _ {n} (x) - f (x) |, 1) \mathrm{d} \mu (x) \\ \leq \int_ {K} | f _ {n} (x) - f (x) | \mathrm{d} \mu (x) + \int_ {\mathbb {R} ^ {d} \setminus K} 1 \mathrm{d} \mu (x) \\ <   \frac {\epsilon}{2} \mu (K) + \mu (\mathbb {R} ^ {d} \setminus K) <   \frac {\epsilon}{2} + \frac {\epsilon}{2} = \epsilon , \end{array}
$$

if $n > N$ . So $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \operatorname* { m i n } ( \vert f _ { n } ( x ) - f ( x ) \vert , 1 ) \mathrm { d } \mu ( x ) \to 0 \mathrm { ~ a s ~ } n \to \infty } \end{array}$ . By Lemma 2.5, we obtain the desired result. □

Moreover, we can extend the result of Proposition 2.3. Given an activation function σ and a subset $D \subset \mathbb { R } ^ { d }$ , define

$$
\mathcal {N} (D) = \left\{f: D \to \mathbb {R}, f (x) = \sum_ {m = 1} ^ {M} a _ {m} \sigma \left(w _ {m} ^ {\top} x + b _ {m}\right): w _ {m} \in \mathbb {R} ^ {d}, a _ {m}, b _ {m} \in \mathbb {R}, M \in \mathbb {Z} ^ {+} \right\}.\tag{2.21}
$$

Then we have the following result.

Lemma 2.6 Suppose σ is a continuous sigmoidal function. Then $\mathcal { N } ( \mathbb { R } ^ { d } )$ with activation function σ is dense in $C ( \mathbb { R } ^ { d } )$ on all compact sets: for any $f \in C (  { \mathbb { R } } ^ { d } )$ there is a sequence $( \phi _ { n } ) _ { n } \subset \mathcal { N }$ such that $\phi _ { n }$ converges uniformly to f on any compact set $K \subset \mathbb { R } ^ { d } \mathrm { ~ } a s \mathrm { ~ } n  \infty$

Proof: First, we claim that given $f \in C (  { \mathbb { R } } ^ { d } )$ and any compact set $K \subset \mathbb { R } ^ { d }$ , there is a sequence $( \phi _ { n } ) _ { n } \subset { \mathcal { N } } ( K )$ such that $\phi _ { n }$ converges uniformly to $f$ on K. This fact is a slightly general case of Proposition 2.3 when $I _ { d }$ is replaced by $K .$ , and the proof is similar. Also, note that the neural networks in ${ \mathcal { N } } ( K )$ have explicit expressions for all $x \in \mathbb { R } ^ { d }$ , so the preceding statement still holds when ${ \mathcal { N } } ( K )$ is replaced by $\mathcal { N } ( \mathbb { R } ^ { d } )$

Next, as in the proof of Proposition 2.4, let $B _ { r } = \{ x \in \mathbb { R } ^ { d } : \| x \| \leq r \}$ . Then $( B _ { r } ) _ { r }$ is an ascending sequence of compact sets such that $B _ { r } ~ \subset ~ B _ { r + 1 }$ and $B _ { r } \nearrow \ \mathbb { R } ^ { d }$ as $r  \infty$ . By the preceding fact, given $g \in C (  { \mathbb { R } } ^ { d } )$ , for every $r \in \mathbb { Z } ^ { + }$ , there is a sequence $( \phi _ { n } ^ { ( r ) } ) _ { n } \subset \mathcal { N } ( \mathbb { R } ^ { d } )$ such that $\phi _ { n } ^ { ( r ) } \to g$ uniformly on $B _ { r }$ as $n \to \infty$ . So for every $r \in \mathbb { Z } ^ { + }$ , there exists $k _ { r } \in \mathbb { Z } ^ { + }$ such that

$$
\sup _ {x \in B _ {r}} | \phi_ {k _ {r}} ^ {(r)} (x) - f (x) | <   \frac {1}{r}.
$$

Now the sequence $\phi _ { k _ { 1 } } ^ { ( 1 ) } , \phi _ { k _ { 2 } } ^ { ( 2 ) } , \cdots$ is the desired sequence such that $\phi _ { k _ { n } } ^ { ( n ) } \to f$ uniformly on any compact set $K \subset \mathbb { R } ^ { d }$ as $n \to \infty$ . In fact, for any compact set $K$ , there is some $n _ { 0 } \in \mathbb { Z } ^ { + }$ such that $K \subset B _ { n _ { 0 } } \subset B _ { n _ { 0 } + 1 } \subset \cdot \cdot \cdot$ . And for any $\epsilon > 0$ , we let $N = \textstyle \operatorname* { m a x } \{ n _ { 0 } , \lceil \frac { 1 } { \epsilon } \rceil \}$ , then for all $n > N$ , it satisfies

$$
\sup _ {x \in K} | \phi_ {k _ {n}} ^ {(n)} (x) - f (x) | \leq \sup _ {x \in B _ {n _ {0}}} | \phi_ {k _ {n}} ^ {(n)} (x) - f (x) | \leq \sup _ {x \in B _ {n}} | \phi_ {k _ {n}} ^ {(n)} (x) - f (x) | <   \frac {1}{n} <   \epsilon .
$$

We remark that the choice of $( \phi _ { n } ) _ { n }$ is independent of the compact set $K$ . That $\mathrm { i s } , ( \phi _ { n } ) _ { n }$ is only determined by $f .$ We first have $( \phi _ { n } ) _ { n } ,$ then it holds that for any compact set $K , ( \phi _ { n } ) _ { n }  f$ uniformly on K. No matter how K varies, the uniform convergence of $( \phi _ { n } ) _ { n }$ on K is always satisfied. This is diferent from Proposition 2.3, in which the convergent sequence $( \phi _ { n } ) _ { n }$ exists after $f$ and the domain $I _ { d }$ are both given.

The following result states that any measurable function can be approximated by a continuous function in the probability sense.

Proposition 2.5 The set of continuous functions $C ( \mathbb { R } ^ { d } )$ is $d _ { \mu }$ -dense in $\mathcal { M } ( \mathbb { R } ^ { d } )$

Proof: Let $f \in \mathcal { M } ( \mathbb { R } ^ { d } )$ be a measurable function. We need to show that there is a sequence of functions in $C ( \mathbb { R } ^ { d } )$ that converges to $f$ in the metric $d _ { \mu }$

Given $\epsilon > 0$ . First, we claim that there is some $N \in \mathbb { Z } ^ { + }$ large enough such that $\mu \{ x : | f ( x ) | >$ $N \} < \epsilon / 2$ . In fact, $A _ { n } : = \{ x : | f ( x ) | > n \}$ for $n \geq 1$ form a descending sequence of measurable sets with limit $A _ { n } \searrow \{ x : | f ( x ) | = \infty \}$ , which has zero measure. So $\mu ( A _ { n } )  0$

Define

$$
\hat {f} (x) = \left\{ \begin{array}{l l} f (x), & \text { if } | f (x) | \leq N, \\ 0, & \text { if } | f (x) | > N. \end{array} \right.
$$

Then

$$
\begin{array}{l} \int_ {\mathbb {R} ^ {d}} \min (| f (x) - \hat {f} (x) |, 1) \mathrm{d} \mu (x) \\ = \int_ {| f | \leq N} \min (| f (x) - \hat {f} (x) |, 1) \mathrm{d} \mu (x) + \int_ {| f | > N} \min (| f (x) - \hat {f} (x) |, 1) \mathrm{d} \mu (x) \\ = \int_ {| f | \leq N} \min (0, 1) \mathrm{d} \mu (x) + \int_ {| f | > N} \min (| f (x) |, 1) \mathrm{d} \mu (x) = \int_ {| f | > N} 1 \mathrm{d} \mu (x) \\ = \mu \{| f | > N \} <   \frac {\epsilon}{2}. \end{array}\tag{2.22}
$$

Note that $\hat { f }$ is a measurable function, so there is a sequence of step functions $( \phi _ { n } ) _ { r }$ that converges to $\hat { f }$ for almost every point on $\mathbb { R } ^ { d }$ . Since $| { \hat { f } } | \leq N$ , we may assume $| \phi _ { n } | \leq N + 1$ when n is suficiently large. Also, $\mu ( \mathbb { R } ^ { d } ) = 1$ is finite. By the bounded convergence theorem,

$$
\int_ {\mathbb {R} ^ {d}} \min (| \hat {f} (x) - \phi_ {n} (x) |, 1) \mathrm{d} \mu (x) \leq \int_ {\mathbb {R} ^ {d}} | \hat {f} (x) - \phi_ {n} (x) | \mathrm{d} \mu (x) \to 0, \quad n \to \infty ,
$$

So there exists $n _ { 0 } \in \mathbb { Z } ^ { + }$ such that

$$
\int_ {\mathbb {R} ^ {d}} \min (| \hat {f} (x) - \phi_ {n} (x) |, 1) \mathrm{d} \mu (x) <   \frac {\epsilon}{4} \quad \text {and} \quad | \phi_ {n} | \leq N + 1\tag{2.23}
$$

for all $n > n _ { 0 }$

Finally, for every $n > n _ { 0 } .$ , we construct a continuous function $f _ { n }$ that is close enough to $\phi _ { n }$ Specifically, we write $\begin{array} { r } { \phi _ { n } = \sum _ { j = 1 } ^ { J } \alpha _ { j } \boldsymbol { 1 } _ { A _ { j } } ( \boldsymbol { x } ) } \end{array}$ with constants $\alpha _ { j }$ and rectangles $A _ { j }$ . Then for each $A _ { j }$ there is a compact set $K _ { j } \subset A _ { j }$ such that $\begin{array} { r } { \mu ( A _ { j } \backslash K _ { j } ) < \frac { \epsilon } { 4 J ( N + 1 ) } } \end{array}$ . It is easy to find some $h _ { j } \in C (  { \mathbb { R } } ^ { d } )$ such that $h _ { j } = 1$ on $K _ { j } , h _ { j } = 0$ on $\mathbb { R } ^ { d } \backslash A _ { j }$ and $h _ { j } \in [ 0 , 1 ]$ on $\mathbb { R } ^ { d }$ . Let $\begin{array} { r } { f _ { n } ( x ) = \sum _ { j = 1 } ^ { J } \alpha _ { j } h _ { j } ( x ) } \end{array}$ , then $f _ { n } \in C (  { \mathbb { R } } ^ { d } )$ , and

$$
\begin{array}{l} \int_ {\mathbb {R} ^ {d}} \min (| \phi_ {n} (x) - f _ {n} (x) |, 1) \mathrm{d} \mu (x) = \int_ {\mathbb {R} ^ {d}} \min (\left| \sum_ {j = 1} ^ {J} \alpha_ {j} (1 _ {A _ {j}} (x) - h _ {j} (x)) \right|, 1) \mathrm{d} \mu (x) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \sum_ {j = 1} ^ {J} \int_ {\mathbb {R} ^ {d}} \min (| \alpha_ {j} | | 1 _ {A _ {j}} (x) - h _ {j} (x) |, 1) \mathrm{d} \mu (x), \end{array}\tag{2.24}
$$

where the relation min $\begin{array} { r } { ( \left| \sum _ { i = 1 } ^ { J } a _ { i } \right| , 1 ) \leq \sum _ { i = 1 } ^ { J } } \end{array}$ min $( | a _ { i } | , 1 )$ for $a _ { i } \in \mathbb { R }$ is used. Note tha $\vert 1 _ { A _ { j } } ( x ) -$ $h _ { j } ( x ) | = 0$ on $K _ { j }$ and $\mathbb { R } ^ { d } \backslash A _ { j }$ , it follows (2.24) that

$$
\begin{array}{r l} & {\int_ {\mathbb {R} ^ {d}} \min (| \phi_ {n} (x) - f _ {n} (x) |, 1) \mathrm{d} \mu (x) \leq \sum_ {j = 1} ^ {J} \int_ {A _ {j} \setminus K _ {j}} \min (| \alpha_ {j} | | 1 _ {A _ {j}} (x) - h _ {j} (x) |, 1) \mathrm{d} \mu (x)} \\ & {\qquad \leq \sum_ {j = 1} ^ {J} \int_ {A _ {j} \setminus K _ {j}} \min (| \alpha_ {j} |, 1) \mathrm{d} \mu (x) \leq \sum_ {j = 1} ^ {J} \int_ {A _ {j} \setminus K _ {j}} | \alpha_ {j} | \mathrm{d} \mu (x)} \\ & {\qquad = \sum_ {j = 1} ^ {J} | \alpha_ {j} | \mu (A _ {j} \setminus K _ {j}) \leq \frac {\epsilon}{4 J (N + 1)} \sum_ {j = 1} ^ {J} | \alpha_ {j} | \leq \frac {\epsilon}{4},} \end{array}\tag{2.25}
$$

where ma $\begin{array} { r } { \mathfrak { c } _ { 1 \le j \le J } | \alpha _ { j } | = \operatorname* { m a x } _ { x \in \mathbb { R } ^ { d } } | \phi _ { n } ( x ) | \le N + 1 } \end{array}$ is used in the last inequality. Next, it follows (2.22), (2.23), (2.25) that

$$
\int_ {\mathbb {R} ^ {d}} \min (| f (x) - f _ {n} (x) |, 1) \mathrm{d} \mu (x) <   \frac {\epsilon}{2} + \frac {\epsilon}{4} + \frac {\epsilon}{4} = \epsilon ,\tag{2.26}
$$

for all $n > n _ { 0 }$

We summarize the previous discussion: for any $\epsilon > 0$ , there is some $f _ { \epsilon } \in C ( \mathbb { R } ^ { d } )$ such that $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \operatorname* { m i n } ( | f ( x ) - f _ { \epsilon } ( x ) | , 1 ) \mathrm { d } \mu ( x ) < \epsilon } \end{array}$ . Now let $( \epsilon _ { n } ) _ { n } > 0$ be a sequence converging to $0 ,$ then there is a sequence $( f _ { \epsilon _ { n } } ) _ { n } \subset C ( \mathbb { R } ^ { d } )$ such that $\int _ {  { \mathbb { R } } ^ { d } }$ min $( | f ( x ) - f _ { \epsilon _ { n } } ( x ) | , 1 ) \mathrm { d } \mu ( x ) \to 0$ as $n \to \infty$ . Since $f _ { \epsilon _ { n } }$ is also in $\mathcal { M } ( \mathbb { R } ^ { d } )$ , by Lemma 2.5, $d _ { \mu } ( f , \tilde { f } _ { \epsilon _ { n } } )  0$ , which finishes the proof. □

The following theorem is the main result of this section. It states that any measurable function in $\mathcal { M } ( \mathbb { R } ^ { d } )$ can be approximated within any desired accuracy by two-layer sigmoidal neural networks, in terms of any Borel probability measure in $B ( \mathbb { R } ^ { d } )$

Theorem 2.14 Suppose σ is a continuous sigmoidal function. Then the set $\mathcal { N } ( \mathbb { R } ^ { d } )$ with activation function σ is $d _ { \mu }$ -dense in $\mathcal { M } ( \mathbb { R } ^ { d } )$ : for any $f \in \mathcal { M } ( \mathbb { R } ^ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} (\mathbb {R} ^ {d})} d _ {\mu} (\phi , f) = 0.
$$

Proof: Let $f \in \mathcal { M } ( \mathbb { R } ^ { d } )$ and fix $\epsilon > 0$ . By Proposition 2.5, there is some $\hat { f } \in C (  { \mathbb { R } } ^ { d } )$ such that $d _ { \mu } ( \hat { f } , f ) < \epsilon / 2$ . By Lemma 2.6, there is a sequence $( \phi _ { n } ) _ { n } \subset \mathcal N ( \mathbb R ^ { d } )$ such that $\phi _ { n }$ converges uniformly to $\hat { f }$ on any compact set $K \subset \mathbb { R } ^ { d }$ as $n \to \infty$ . Since $\phi _ { n }$ are also in $\mathcal { M } ( \mathbb { R } ^ { d } )$ , by Proposition $2 . 4 , d _ { \mu } ( \phi _ { n } , \hat { f } ) \to 0 \mathrm { a s } n \to \infty$ , which means there is $n ^ { \prime } \in \mathbb { Z } ^ { + }$ large enough such that $d _ { \mu } ( \phi _ { n ^ { \prime } } , \hat { f } ) < \epsilon / 2$ By the triangle inequality (2.15),

$$
d _ {\mu} (\phi_ {n ^ {\prime}}, f) \leq d _ {\mu} (\phi_ {n ^ {\prime}}, \hat {f}) + d _ {\mu} (\hat {f}, f) \leq \epsilon ,
$$

which shows that $\mathcal { N } ( \mathbb { R } ^ { d } )$ is $d _ { \mu } \mathrm { - d e n s e }$ in $\mathcal { M } ( \mathbb { R } ^ { d } )$

## 2.3 Error Bounds Estimation

The universal approximation introduced in previous sections is an important result, but it is of limited use due to the lack of quantitative information about the approximation error. In this section, we will discuss the error estimation by giving explicit error bounds.

As mentioned in the introduction, some classical approximation structures such polynomials, Fourier series and wavelets are ineficient at approximating high-dimensional functions because of the curse of dimensionality. That ${ \mathrm { i s } } ,$ for a fixed target function, the convergence rate has the form $O ( - \frac { 1 } { d } )$ . This implies that the required number of parameters to achieve given accuracy will increase exponentially with the dimension. However, neural networks can lessen or overcome this issue in the approximation of some special functions. This fact can be validated by observing the approximation error bound, whose convergence rate is independent of $d .$ So if the target function is fixed, the required number of parameters will not blow up in high-dimensional cases.

Recall that the concept closure is closely related to density. Let S be a subset of a Banach space X. The closure of S is defined as a subset of X, which is the union of S and the set of accumulation points of S. So, we say a vector $f$ is in the closure of S if there is a sequence $( s _ { n } ) _ { n } \subset S$ such that $\| f - s _ { n } \| \to 0 ;$ ; namely, for any $\epsilon > 0$ , there is some $s \in S$ such that $\| f - s \| < \epsilon$

## 2.3.1 Spectral Barron norm and approximation

We consider the set of two-layer neural networks of width M, which is given by

$$
\mathcal {N} _ {M} = \left\{\phi (x) = b + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}): w _ {m} \in \mathbb {R} ^ {d}, a _ {m}, b _ {m}, b \in \mathbb {R} \right\}.\tag{2.27}
$$

In this subsection, we let $\Omega \subset \mathbb { R } ^ { d }$ be a compact set that contains the zero vector.

## Approximation by sigmoidal networks

In the early work [1], Barron proposed a special norm of functions. For any function $f : \Omega $ R, we use $\mathcal { E } _ { f }$ to denote the set of all extensions of $f$ over $\mathbb { R } ^ { d }$ that have Fourier transforms, i.e.

$$
\mathcal {E} _ {f, \Omega} = \left\{f _ {\mathrm{e}}: \mathbb {R} ^ {d} \to \mathbb {R} \text {s.t.} f _ {\mathrm{e}} | _ {\Omega} = f \text {and} \hat {f} _ {\mathrm{e}} (w) := \int_ {\mathbb {R} ^ {d}} e ^ {- \mathrm{i} w ^ {\top} x} f _ {\mathrm{e}} (x) \mathrm{d} x \text {exists} \right\}.
$$

Then the so-called spectral Barron norm defined on Ω is given by

$$
\| f \| _ {\mathcal {B}} = \inf _ {f _ {\mathrm{e}} \in \mathcal {E} _ {f, \Omega}} \int_ {\mathbb {R} ^ {d}} \| w \| _ {\Omega} | \hat {f} _ {\mathrm{e}} (w) | \mathrm{d} w,\tag{2.28}
$$

given that $\mathcal { E } _ { f , \Omega }$ is non-empty, where $\| \cdot \| _ { \Omega }$ is defined by

$$
\| w \| _ {\Omega} = \sup _ {x \in \Omega} | w ^ {\top} x |, \quad \forall w \in \mathbb {R} ^ {d}.\tag{2.29}
$$

Specifically, if Ω is the d-ball $\{ x \in \mathbb { R } ^ { d } : \| x \| _ { 2 } < R \}$ , then $\| \boldsymbol { w } \| _ { \Omega } = R \| \boldsymbol { w } \| _ { 2 } ;$ if Ω is the d-box $[ - R , R ] ^ { d }$ then $\| \boldsymbol { w } \| _ { \Omega } = R \| \boldsymbol { w } \| _ { 1 }$ . Now we have the following result.

Theorem 2.15 (Barron, 1993) Let $M \in \mathbb { Z } ^ { + }$ . Suppose the activation function σ in $\mathcal { N } _ { M }$ is a sigmoidal function. Then for any function $f : \Omega $ R satisfying $\| f \| _ { B } < \infty$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} _ {M}} \| \phi - f \| _ {L _ {\mu} ^ {2} (\Omega)} := \inf _ {\phi \in \mathcal {N} _ {M}} \left(\int_ {\Omega} | \phi (x) - f (x) | ^ {2} \mu (\mathrm{d} x)\right) ^ {\frac {1}{2}} \leq \frac {2 \| f \| _ {\mathcal {B}}}{\sqrt {M}},\tag{2.30}
$$

for every probability measure $\mu .$

To prove the above theorem, we first introduce the following lemma.

Lemma 2.7 Let G be a subset of a Hilbert space H equipped with norm $\| \cdot \|$ and inner product $\langle \cdot , \cdot \rangle$ . Suppose $\| g \| \le B$ for all $g \in G$ for some $B > 0$ . Let $f ^ { o }$ be a non-zero vector in the closure of the set $\begin{array} { r } { G _ { \mathrm { c . h . } } : = \Big \{ h \in H , h = \sum _ { n = 1 } ^ { N } c _ { n } g _ { n } } \end{array}$ for some $\begin{array} { r } { c _ { n } \geq 0 , \sum _ { n = 1 } ^ { N } c _ { n } = 1 } \end{array}$ and , $N \in \mathbb { Z } ^ { + } , \ g _ { n } \in G \Big \}$ namely, the convex hull of G. Then for any $M \in \mathbb { Z } ^ { + }$ , there is some $\begin{array} { r } { f _ { M } = \sum _ { m = 1 } ^ { M } c _ { m } g _ { m } \in G _ { \mathrm { c } . \mathrm { h } } , } \end{array}$ such that $\begin{array} { r } { \| f _ { M } - f ^ { o } \| ^ { 2 } \le \frac { B ^ { 2 } } { M } } \end{array}$

Proof: Given $M \in \mathbb { Z } ^ { + }$ and $\delta > 0$ , since $f ^ { o }$ is in the closure of $G _ { \mathrm { c . h . } }$ , there is some $\begin{array} { r } { f ^ { * } = \sum _ { n = 1 } ^ { N } c _ { n } g _ { n } ^ { * } \in \quad } \end{array}$ $G _ { \mathrm { c . h } }$ <sub>.</sub> such that

$$
\left\| f ^ {*} - f ^ {o} \right\| \leq \frac {\delta}{\sqrt {M}},\tag{2.31}
$$

where $g _ { n } ^ { * } \in G$ and $\begin{array} { r } { c _ { n } \ge 0 , \sum _ { n = 1 } ^ { N } c _ { n } = 1 } \end{array}$ . Let ξ be the random variable drawn from the set $\{ g _ { 1 } ^ { * } , \ldots , g _ { N } ^ { * } \}$ with $\mathbb { P } [ \xi = g _ { n } ^ { * } ] = c _ { n } ( n = 1 , \ldots , N )$ . And let $\xi _ { 1 } , \dots , \xi _ { M }$ be i.i.d. random variables with the same distribution as $\xi$ . Let $\begin{array} { r } { \bar { \xi } = \frac { 1 } { M } \sum _ { m = 1 } ^ { M } \xi _ { m } } \end{array}$ , then

$$
\mathbb {E} \bar {\xi} = \frac {1}{M} \sum_ {m = 1} ^ {M} \mathbb {E} \xi_ {m} = \mathbb {E} \xi = \sum_ {n = 1} ^ {N} c _ {n} g _ {n} ^ {*} = f ^ {*}.
$$

Therefore,

$$
\begin{array}{l} \mathbb {E} \| \bar {\xi} - f ^ {*} \| ^ {2} = \mathbb {E} \left\langle \frac {\xi_ {1} + \cdots + \xi_ {M}}{M} - f ^ {*}, \frac {\xi_ {1} + \cdots + \xi_ {M}}{M} - f ^ {*} \right\rangle \\ \qquad = \frac {1}{M ^ {2}} \mathbb {E} \langle \xi_ {1} - f ^ {*} + \dots + \xi_ {M} - f ^ {*}, \xi_ {1} - f ^ {*} + \dots + \xi_ {M} - f ^ {*} \rangle \\ \qquad = \frac {1}{M ^ {2}} \left[ \sum_ {m = 1} ^ {M} \mathbb {E} \langle \xi_ {m} - f ^ {*}, \xi_ {m} - f ^ {*} \rangle - \sum_ {i \neq j} \mathbb {E} \langle \xi_ {i} - f ^ {*}, \xi_ {j} - f ^ {*} \rangle \right]. \end{array}\tag{2.32}
$$

Note that if $i \neq j$

$$
\mathbb {E} \left\langle \xi_ {i} - f ^ {*}, \xi_ {j} - f ^ {*} \right\rangle = \left\langle \mathbb {E} \left(\xi_ {i}\right) - f ^ {*}, \mathbb {E} \left(\xi_ {j}\right) - f ^ {*} \right\rangle = \left\langle f ^ {*} - f ^ {*}, f ^ {*} - f ^ {*} \right\rangle = 0.\tag{2.33}
$$

So it follows (2.32) that

$$
\begin{array}{r l} & {\mathbb {E} \| \bar {\xi} - f ^ {*} \| ^ {2} = \frac {1}{M ^ {2}} \sum_ {m = 1} ^ {M} \mathbb {E} \langle \xi_ {m} - f ^ {*}, \xi_ {m} - f ^ {*} \rangle = \frac {1}{M} \mathbb {E} \langle \xi - f ^ {*}, \xi - f ^ {*} \rangle} \\ & {= \frac {1}{M} (\mathbb {E} \langle \xi , \xi \rangle - 2 \mathbb {E} \langle \xi , f ^ {*} \rangle + \langle f ^ {*}, f ^ {*} \rangle) = \frac {1}{M} (\mathbb {E} \langle \xi , \xi \rangle - 2 \langle \mathbb {E} \xi , f ^ {*} \rangle + \langle f ^ {*}, f ^ {*} \rangle) = \frac {1}{M} (\mathbb {E} \| \xi \| ^ {2} - \| f ^ {*} \| ^ {2})} \end{array}
$$

$$
\leq \frac {1}{M} (B ^ {2} - \| f ^ {*} \| ^ {2}).\tag{2.34}
$$

Since the expected value is bounded in this way, there must exist a sample of $\bar { \xi }$ (denoted by $f _ { M } )$ such that

$$
\| f _ {M} - f ^ {*} \| ^ {2} \leq \frac {1}{M} (B ^ {2} - \| f ^ {*} \| ^ {2}),\tag{2.35}
$$

where $\begin{array} { r } { f _ { M } = \frac { 1 } { M } \sum _ { m = 1 } ^ { M } g _ { m } } \end{array}$ with $g _ { m }$ being a sample of the random variable $\xi _ { m }$ . Combining (2.31) and (2.35) by triangle inequality and using the fact $\textstyle \left\| f ^ { * } \right\| \geq \left\| f ^ { o } \right\| - { \frac { \delta } { \sqrt { M } } }$ lead to

$$
\| f _ {M} - f ^ {o} \| \leq \frac {1}{\sqrt {M}} (\sqrt {B ^ {2} - \| f ^ {*} \| ^ {2}} + \delta) \leq \frac {1}{\sqrt {M}} \left(\sqrt {B ^ {2} - \| f ^ {o} \| ^ {2} - \delta (\frac {\delta}{M} + 2 \frac {\| f ^ {o} \|}{\sqrt {M}})} + \delta\right)\tag{2.36}
$$

The proof is completed by making δ suficiently small so that the upper bound of (2.36) is less than $B ^ { 2 }$ □

Now given a constant $C > 0$ , we define $\Gamma _ { C , \Omega }$ as the function set consisting of all functions $f :$ $\Omega \to \mathbb { R }$ such that $\mathcal { E } _ { f , \Omega }$ is non-empty (namely, f has an extension on $\mathbb { R } ^ { d }$ that is Fourier transformable) and satisfy

$$
\| f \| _ {\mathcal {B}} \leq C.\tag{2.37}
$$

Moreover, we define the function set $G _ { C , \mathrm { { c o s } } }$ by

$$
G _ {C, \mathrm{cos}} = \left\{\frac {\gamma}{\| w \| _ {\Omega}} \left(\cos (w ^ {\top} x + b) - \cos b\right): w \neq 0 \in \mathbb {R} ^ {d}, | \gamma | \leq C, b \in \mathbb {R} \right\}.\tag{2.38}
$$

Recall that the $L _ { \mu } ^ { 2 } ( \Omega )$ for any probability measure $\mu$ is a Hilbert space, whose norm is defined by

$$
\| f \| _ {L _ {\mu} ^ {2} (\Omega)} = \left(\int_ {\Omega} | f (x) | ^ {2} \mu (\mathrm{d} x)\right) ^ {\frac {1}{2}}\tag{2.39}
$$

Now we have the following lemma.

Lemma 2.8 For any $f \in \Gamma _ { C , \Omega }$ and any probability measure $\mu ,$ the function $f ( x ) - f ( 0 )$ is in the closure of the convex hull of $G _ { C , \mathrm { { c o s } } }$ under the norm $L _ { \mu } ^ { 2 } ( \Omega )$

Proof: Let $\hat { f } ( w )$ be the Fourier transform of some extension of $f$ such that $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \| w \| _ { \Omega } | \hat { f } ( w ) | \mathrm { d } w \leq C } \end{array}$ Then $\begin{array} { r } { f ( x ) = \int _ { \mathbb { R } ^ { d } } e ^ { \mathrm { i } w ^ { \top } x } \hat { f } ( w ) } \end{array}$ dw for $x \in \Omega$ and $\begin{array} { r } { f ( 0 ) = \int _ { \mathbb { R } ^ { d } } \hat { f } ( w ) } \end{array}$ dw. Since $f ( x ) - f ( 0 )$ is real,

$$
\begin{array}{c} h (x) := f (x) - f (0) = \operatorname{Re} \int_ {\mathbb {R} ^ {d}} \left(e ^ {\mathrm{i} w ^ {\top} x} - 1\right) \hat {f} (w) \mathrm{d} w = \operatorname{Re} \int_ {\mathbb {R} ^ {d}} \left(e ^ {\mathrm{i} w ^ {\top} x} - 1\right) e ^ {\mathrm{i} \theta} | \hat {f} (w) | \mathrm{d} w \\ = \int_ {\mathbb {R} ^ {d}} \left(\cos (w ^ {\top} x + \theta) - \cos \theta\right) | \hat {f} (w) | \mathrm{d} w, \end{array}\tag{2.40}
$$

where $\theta$ is the argument of $\hat { f } ( w )$ . Let

$$
g (x; w) := \frac {\int_ {\mathbb {R} ^ {d}} \| w \| _ {\Omega} | \hat {f} (w) | \mathrm{d} w}{\| w \| _ {\Omega}} \left(\cos (w ^ {\top} x + \theta) - \cos \theta\right), \forall w \neq 0.
$$

Then $g ( x ; w ) \in G _ { C , \mathrm { c o s } }$ since $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \| w \| _ { \Omega } | \hat { f } ( w ) | \mathrm { d } w \leq C } \end{array}$ , and

$$
| g (x; w) | \leq \frac {C}{\| w \| _ {\Omega}} \left| - 2 \sin \left(\frac {1}{2} w ^ {\top} x + \theta\right) \sin \left(\frac {1}{2} w ^ {\top} x\right) \right| \leq \frac {C | w ^ {\top} x |}{\| w \| _ {\Omega}} \leq C.\tag{2.41}
$$

From (2.40), we have

$$
h (x) = \int_ {\mathbb {R} ^ {d} \backslash \{0 \}} g (x; w) p (w) \mathrm{d} w,\tag{2.42}
$$

where $\begin{array} { r } { p ( w ) : = \frac { \Vert w \Vert _ { \Omega } \Vert \hat { f } ( w ) \Vert } { \int _ { \mathbb { R } ^ { d } } \Vert w \Vert _ { \Omega } \Vert \hat { f } ( w ) \vert \mathrm { d } w } } \end{array}$ can be viewed as a probability density function. Let n be any positive integer and $\xi , \xi _ { 1 } , \ldots , \xi _ { n }$ be i.i.d. random variables in $\mathbb { R } ^ { d } \backslash \{ 0 \}$ under the distribution of $p .$ Note that (2.42) implies that $\mathbb { E } _ { \xi } g ( x ; \xi ) = h ( x )$ , then

$$
\begin{array}{l} \mathbb {E} _ {\xi_ {1}, \ldots , \xi_ {n}} \left(h (x) - \frac {1}{n} \sum_ {i = 1} ^ {n} g (x; \xi_ {i})\right) ^ {2} = \mathbb {E} _ {\xi_ {1}, \ldots , \xi_ {n}} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} [ h (x) - g (x; \xi_ {i}) ]\right) ^ {2} \\ = \frac {1}{n ^ {2}} \left(\sum_ {i = 1} ^ {n} \mathbb {E} _ {\xi_ {i}} [ h (x) - g (x; \xi_ {i}) ] ^ {2} + \sum_ {i \neq j} \mathbb {E} _ {\xi_ {i}, \xi_ {j}} [ h (x) - g (x; \xi_ {i}) ] [ h (x) - g (x; \xi_ {j}) ]\right) \\ = \frac {1}{n} \left(\mathbb {E} _ {\xi} [ h (x) - g (x; \xi) ] ^ {2}\right) \leq \frac {1}{n} \left(h ^ {2} (x) - 2 h (x) \mathbb {E} _ {\xi} g (x; \xi) + (\mathbb {E} _ {\xi} g (x; \xi)) ^ {2}\right) \\ = \frac {1}{n} \left((\mathbb {E} _ {\xi} g (x; \xi)) ^ {2} - h ^ {2} (x)\right) \leq \frac {1}{n} (\mathbb {E} _ {\xi} g (x; \xi)) ^ {2} \leq \frac {C ^ {2}}{n}, \end{array}\tag{2.43}
$$

where the last inequality is due to (2.41). Therefore, using Fubini’ theorem, we have

$$
\begin{array}{l} \mathbb {E} _ {\xi_ {1}, \dots , \xi_ {n}} \int_ {\Omega} \left(h (x) - \frac {1}{n} \sum_ {i = 1} ^ {n} g (x; \xi_ {i})\right) ^ {2} \mu (\mathrm{d} x) = \int_ {\Omega} \mathbb {E} _ {\xi_ {1}, \dots , \xi_ {n}} \left(h (x) - \frac {1}{n} \sum_ {i = 1} ^ {n} g (x; \xi_ {i})\right) ^ {2} \mu (\mathrm{d} x) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq \int_ {\Omega} \frac {C ^ {2}}{n} \mu (\mathrm{d} x) = \frac {C ^ {2}}{n} \end{array}\tag{2.44}
$$

since $\mu$ is a probability measure. So there exist samples of $\xi _ { 1 } , \ldots , \xi _ { n }$ , denoted as $w _ { 1 } , \ldots , w _ { n }$ , such that 2

$$
\int_ {\Omega} \left(h (x) - \frac {1}{n} \sum_ {i = 1} ^ {n} g (x; w _ {i})\right) ^ {2} \mu (\mathrm{d} x) \leq \frac {C ^ {2}}{n}.\tag{2.45}
$$

The proof is completed by noting that $\begin{array} { r } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( x ; w _ { i } ) \ d t } \end{array}$ is in the convex hull of $G _ { C , \mathrm { { c o s } } }$ and letting $n \to \infty$ in (2.45). □

Next, we define the function set consisting of certain Heaviside neurons, i.e.,

$$
G _ {C, \mathrm{H}} := \{\gamma H (v ^ {\top} x - b): | \gamma | \leq 2 C, \| v \| _ {\Omega} = 1, | b | \leq 1 \},\tag{2.46}
$$

where $H ( \cdot )$ is defined by (1.2). We will prove

Lemma 2.9 For any $g \in G _ { C , \cos } , g$ is in the closure of the convex hull of $G _ { C , { \mathrm { H } } }$

Proof: Let $\begin{array} { r } { g ( x ; w ) = \frac { \gamma } { \| w \| _ { \mathrm { o } } } \left( \cos ( w ^ { \top } x + b ) - \cos b \right) \in G _ { C , \mathrm { c o s } } } \end{array}$ with $x \in \Omega , w \in \mathbb { R } \backslash \{ 0 \}$ . We denote $\begin{array} { r } { z = \frac { w ^ { \top } x } { \| w \| _ { \Omega } } } \end{array}$ , then $- 1 \leq z \leq 1$ . Then we consider the approximation of the one-dimensional function $\begin{array} { r } { \tilde { g } ( z ) \mathrel { \mathop : } = \tilde { g } ( x ; w ) = \frac { \gamma } { \| w \| _ { \mathrm { O } } } \left( \cos ( \| w \| _ { \Omega } z + b ) - \cos b \right) } \end{array}$ by linear combinations of Heaviside neurons using similar argument in the proof of Theorem 2.6. We first consider $\tilde { g } ( z )$ on $[ 0 , 1 ]$ , where $| \tilde { g } ( z ) | \leq | \gamma | \leq C$ and $\begin{array} { r } { | \tilde { g } ^ { \prime } ( z ) | \leq \frac { | \gamma | } { \| w \| _ { \Omega } } | \sin ( \| w \| _ { \Omega } z + b ) | \| w \| _ { \Omega } \leq | \gamma | \leq C } \end{array}$ . Given $\epsilon > 0$ , by the uniform continuity, there exists $M \in \mathbb { Z } ^ { + }$ such that

$$
| \tilde {g} (x) - \tilde {g} (y) | <   \epsilon , \quad \text { whenever } | x - y | \leq \frac {1}{M}.\tag{2.47}
$$

Let $0 = z _ { 0 } < z _ { 1 } < \dots < z _ { M } = 1$ be an equidistant partition. We construct the Heaviside network

$$
\phi^ {+} (z) = \sum_ {m = 1} ^ {M} \gamma_ {m} ^ {+} H (z - z _ {m}),\tag{2.48}
$$

where $\gamma _ { m } ^ { + } : = \tilde { g } ( z _ { m } ) - \tilde { g } ( z _ { m - 1 } )$ , and it satisfies

$$
| \tilde {g} (z) - \phi^ {+} (z) | <   \epsilon , \quad \forall z \in [ 0, 1 ].\tag{2.49}
$$

Also, it holds for any m that $\begin{array} { r } { | \gamma _ { m } ^ { + } | = | \tilde { g } ( z _ { m } ) - \tilde { g } ( z _ { m - 1 } ) | = | \tilde { g } ^ { \prime } ( \xi _ { m } ) | \cdot \frac { 1 } { M } \le \frac { C } { M } } \end{array}$ , where $\xi _ { m } \in ( z _ { m - 1 } , z _ { m } )$ Similarly, writing $\tilde { h } ( z ) = \tilde { g } ( - z )$ with $z \in [ 0 , 1 ]$ and using the same argument as above, we conclude that there exists $\begin{array} { r } { \phi ^ { - } ( z ) = \sum _ { m = 1 } ^ { M } \gamma _ { m } ^ { - } H ( - z - z _ { m } ) } \end{array}$ such that

$$
| \tilde {g} (z) - \phi^ {-} (z) | <   \epsilon , \quad \forall z \in [ 0, 1 ],\tag{2.50}
$$

and $\begin{array} { r } { | \gamma _ { m } ^ { - } | \le { \frac { C } { M } } } \end{array}$ . Since $\phi ^ { + } ( z ) = 0 \ \mathrm { f o r } \ z \leq 0$ and $\phi ^ { - } ( z ) = 0 \mathrm { ~ f o r ~ } z \ge 0$ , the Heaviside network $\phi ( z ) : = \phi ^ { + } ( z ) + \phi ^ { - } ( z )$ satisfies

$$
| \tilde {g} (z) - \phi (z) | <   \epsilon , \quad \forall z \in [ - 1, 1 ].\tag{2.51}
$$

Therefore,

$$
\left| g (x; w) - \Phi (x; w) \right| <   \epsilon , \quad \forall x \in \Omega ,\tag{2.52}
$$

where $\begin{array} { r } { \Phi ( { \boldsymbol x } ; { \boldsymbol w } ) = \sum _ { m = 1 } ^ { M } \gamma _ { m } ^ { + } H \left( \frac { 1 } { \| { \boldsymbol w } \| _ { \Omega } } { \boldsymbol w } ^ { \top } { \boldsymbol x } - z _ { m } \right) + \sum _ { m = 1 } ^ { M } \gamma _ { m } ^ { - } H \left( - \frac { 1 } { \| { \boldsymbol w } \| _ { \Omega } } { \boldsymbol w } ^ { \top } { \boldsymbol x } - z _ { m } \right) } \end{array}$ . Note that $\Phi ( x ; w )$ is a convex linear combination of $\begin{array} { r } { \left\{ 2 M \gamma _ { m } ^ { + } H \left( \frac { 1 } { \| w \| _ { \Omega } } w ^ { \top } x - z _ { m } \right) \right\} \cup \left\{ 2 M \gamma _ { m } ^ { - } H \left( - \frac { 1 } { \| w \| _ { \Omega } } w ^ { \top } x - z _ { m } \right) \right\} } \end{array}$ with coeficients $\textstyle { \frac { 1 } { 2 M } }$ . And it can be verified that

$$
2 M \gamma_ {m} ^ {+} H \left(\frac {1}{\| w \| _ {\Omega}} w ^ {\top} x - z _ {m}\right) \in G _ {C, \mathrm{H}}, \quad 2 M \gamma_ {m} ^ {-} H \left(- \frac {1}{\| w \| _ {\Omega}} w ^ {\top} x - z _ {m}\right) \in G _ {C, \mathrm{H}}.\tag{2.53}
$$

In the last step, we define the function set consisting of sigmoidal neurons, i.e.,

$$
G _ {C, \sigma} := \{\gamma \sigma (v ^ {\top} x + b): | \gamma | \leq 2 C, v \in \mathbb {R} ^ {d}, b \in \mathbb {R} \},\tag{2.54}
$$

where $\sigma ( t )$ is a sigmoidal function. We have the following result similar to Lemma 2.9.

Lemma 2.10 For any $g \in G _ { C , \cos } , g$ is in the closure of the convex hull of $G _ { C , \sigma }$

The proof directly follows Lemma 2.9 and the fact that a Heaviside neuron in $G _ { C , { \mathrm { H } } }$ is in the closure of $G _ { C , \sigma } ;$ the latter can be proved using the similar argument in the proof of Theorem 2.7.

Combining Lemma 2.8 and Lemma 2.10, we directly have

Lemma 2.11 For any $f \in \Gamma _ { C , \Omega }$ and any probability measure $\mu ,$ the function $f ( x ) - f ( 0 )$ is in the closure of the convex hull of $G _ { C , \sigma }$ under the norm $L _ { \mu } ^ { 2 } ( \Omega )$ .

Proof: Given $\epsilon > 0$ and denote $h ( x ) = f ( x ) - f ( 0 )$ . By Lemma 2.8. there exist $g _ { 1 } , \ldots , g _ { M }$ in $G _ { C , \mathrm { { c o s } } }$ such that

$$
\left\| h - \sum_ {m = 1} ^ {M} c _ {m} g _ {m} \right\| _ {L _ {\mu} ^ {2} (\Omega)} <   \frac {\epsilon}{2}\tag{2.55}
$$

with $\textstyle \sum _ { m = 1 } ^ { M } c _ { m } = 1$ and $c _ { m } \geq 0$ . And by lemma 2.10, for every $g _ { m }$ , there exist $h _ { 1 } ^ { ( m ) } , \ldots , h _ { N _ { m } } ^ { ( m ) }$ in $G _ { C , \sigma }$ such that

$$
\left\| g _ {m} - \sum_ {n = 1} ^ {N _ {m}} c _ {n} ^ {(m)} h _ {n} ^ {(m)} \right\| _ {L _ {\mu} ^ {2} (\Omega)} <   \frac {\epsilon}{2}\tag{2.56}
$$

with $\begin{array} { r } { \sum _ { n = 1 } ^ { N _ { m } } c _ { n } ^ { ( m ) } = 1 } \end{array}$ and $c _ { n } ^ { ( m ) } \geq 0$ . Then by triangle inequality,

$$
\begin{array}{r l} \left\| h - \sum_ {m = 1} ^ {M} \sum_ {n = 1} ^ {N _ {m}} c _ {m} c _ {n} ^ {(m)} h _ {n} ^ {(m)} \right\| _ {L _ {\mu} ^ {2} (\Omega)} & \leq \left\| f - \sum_ {m = 1} ^ {M} c _ {m} g _ {m} \right\| _ {L _ {\mu} ^ {2} (\Omega)} + \sum_ {m = 1} ^ {M} c _ {m} \left\| \sum_ {n = 1} ^ {N _ {m}} c _ {n} ^ {(m)} h _ {n} ^ {(m)} - g _ {m} \right\| _ {L _ {\mu} ^ {2} (\Omega)} \\ & \leq \frac {\epsilon}{2} + \sum_ {m = 1} ^ {M} c _ {m} \cdot \frac {\epsilon}{2} = \epsilon . \end{array}\tag{2.57}
$$

The proof is completed by the fact that $\begin{array} { r } { \sum _ { m = 1 } ^ { M } \sum _ { n = 1 } ^ { N _ { m } } c _ { m } c _ { n } ^ { ( m ) } h _ { n } ^ { ( m ) } } \end{array}$ is a convex linear combination of $\{ h _ { n } ^ { ( m ) } \}$ □

Now let us figure out the proof of Theorem 2.15.

Proof of Theorem 2.15: Given $f : \Omega \to { \mathbb { R } }$ satisfying $\| f \| _ { B } < \infty$ and given any probability measure $\mu .$ If $f = 0 ,$ , then $f \in \mathcal { N } _ { M }$ and the proof is trivial. Otherwise, it is clear that $f \in \Gamma _ { \| f \| _ { B } , \Omega }$ . By Lemma 2.11, $f ( x ) - f ( 0 )$ is in the closure of the convex hull of $G _ { \parallel f \parallel _ { B } , \sigma }$ under the norm $L _ { \mu } ^ { 2 } ( \Omega )$ Also, since $\sigma ( t ) \in [ 0 , 1 ]$ , for any $h = \gamma \sigma ( v ^ { \top } x + b ) \in G _ { \parallel f \parallel _ { B } , \sigma }$ 2

$$
\| h \| _ {L _ {\mu} ^ {2} (\Omega)} = \left(\int_ {\Omega} | \gamma \sigma (v ^ {\top} x + b) | ^ {2} \mu (\mathrm{d} x)\right) ^ {\frac {1}{2}} \leq \left(\int_ {\Omega} | \gamma | ^ {2} \mu (\mathrm{d} x)\right) ^ {\frac {1}{2}}
$$

$$
\leq 2 \| f \| _ {\mathcal {B}} \left(\int_ {\Omega} \mu (\mathrm{d} x)\right) ^ {\frac {1}{2}} = 2 \| f \| _ {\mathcal {B}}.\tag{2.58}
$$

By Lemma 2.7, there exists a convex linear combination $\begin{array} { r } { \sum _ { m = 1 } ^ { M } c _ { m } \left( \gamma _ { m } \sigma ( v _ { m } ^ { \top } x + b _ { m } ) \right) } \end{array}$ such that

$$
\left\| f (x) - f (0) - \sum_ {m = 1} ^ {M} c _ {m} \left(\gamma_ {m} \sigma (v _ {m} ^ {\top} x + b _ {m})\right) \right\| _ {L _ {\mu} ^ {2} (\Omega)} \leq \frac {2 \| f \| _ {\mathcal {B}}}{\sqrt {M}}.\tag{2.59}
$$

Note that here $c _ { m } \in \mathbb { R } ^ { + } , \ \gamma _ { m } , b _ { m } \in \mathbb { R } , \ v _ { m } \in \mathbb { R } ^ { d } , \ \sum _ { m = 1 } ^ { M } c _ { m } = 1 , \ | \gamma _ { m } | \leq 2 \| f \| _ { B }$ . The proof is completed by letting

$$
\phi_ {M} = f (0) + \sum_ {m = 1} ^ {M} c _ {m} \gamma_ {m} \sigma (v _ {m} ^ {\top} x + b _ {m}),\tag{2.60}
$$

then $\begin{array} { r } { \phi _ { M } \in \mathcal { N } _ { M } \mathrm { ~ a n d ~ } \operatorname* { i n f } _ { \phi \in \mathcal { N } _ { M } } \| \phi - f \| _ { L _ { \mu } ^ { 2 } ( \Omega ) } \leq \| \phi _ { M } - f \| _ { L _ { \mu } ^ { 2 } ( \Omega ) } < \frac { 2 \| f \| _ { \mathcal { B } } } { \sqrt { M } } . } \end{array}$

Theorem 2.15 implies that for any target function with finite spectral Barron norm, there always exists a two-layer sigmoid neural network of width M such that the L<sup>2</sup>-approximation error is no more than $O ( M ^ { - 1 / 2 } )$ . As the width M approaches infinity, the error bound will decrease to zero with the rate $- 1 / 2$ . Note that the convergence rate in (2.30) is independent of dimension d. However, the constant $\| f \| _ { B }$ could be dimension-dependent since it makes use of the Fourier transform.

In [1], several examples of functions having a finite spectral Barron norm are presented. A notable example is that if $f : \Omega $ R has an extension $f _ { \mathrm { e } } \in C ^ { s } ( \mathbb { R } ^ { d } ) \cap H ^ { s } ( \mathbb { R } ^ { d } )$ with $s = \lfloor d / 2 \rfloor + 2$ In this case, let $R _ { \Omega } = \operatorname* { s u p } _ { x \in \Omega } \| x \| _ { 2 }$ 2

$$
\begin{array}{l} \| f \| _ {\mathcal {B}} \leq R _ {\Omega} \int_ {\mathbb {R} ^ {d}} \| w \| _ {2} | \tilde {f} _ {\mathrm{e}} (w) | \mathrm{d} w \\ \qquad = R _ {\Omega} \int_ {\mathbb {R} ^ {d}} | \tilde {f} _ {\mathrm{e}} (w) | \| w \| _ {2} \left(1 + \| w \| _ {2} ^ {2 (s - 1)}\right) ^ {1 / 2} \cdot \frac {1}{\left(1 + \| w \| _ {2} ^ {2 (s - 1)}\right) ^ {1 / 2}} \mathrm{d} w \\ \qquad \leq R _ {\Omega} \left(\int_ {\mathbb {R} ^ {d}} | \tilde {f} _ {\mathrm{e}} (w) | ^ {2} \left(\| w \| _ {2} ^ {2} + \| w \| _ {2} ^ {2 s}\right) \mathrm{d} w\right) ^ {1 / 2} \left(\int_ {\mathbb {R} ^ {d}} \frac {1}{1 + \| w \| _ {2} ^ {2 (s - 1)}} \mathrm{d} w\right) ^ {1 / 2}. \end{array}\tag{2.61}
$$

Note that

$$
\begin{array}{r l r} & & {\int_ {\mathbb {R} ^ {d}} \frac {1}{1 + \| w \| _ {2} ^ {2 (s - 1)}} \mathrm{d} w = \lim _ {R \to \infty} \int_ {0} ^ {R} \frac {1}{1 + r ^ {2 (s - 1)}} \cdot A _ {d} r ^ {d - 1} \mathrm{d} r} \\ & & {\qquad = A _ {d} \lim _ {R \to \infty} \left(\int_ {1} ^ {R} \frac {1}{r ^ {2}} \mathrm{d} r + \int_ {0} ^ {1} \frac {r ^ {d - 1}}{1 + r ^ {2 (s - 1)}} \mathrm{d} r\right) <   \infty ,} \end{array}\tag{2.62}
$$

where $A _ { d }$ is the area of the unit ball in $\mathbb { R } ^ { d }$ . On the other hand, taking derivatives k times on $\begin{array} { r } { f _ { \mathrm { e } } ( \boldsymbol { x } ) = \int _ { \mathbb { R } ^ { d } } e ^ { \mathrm { i } \boldsymbol { w } ^ { \top } \boldsymbol { x } } \tilde { f } _ { \mathrm { e } } ( \boldsymbol { w } ) } \end{array}$ dw leads to

$$
\partial_ {x _ {i _ {1}}} \ldots \partial_ {x _ {i _ {k}}} f _ {\mathrm{e}} (x) = \int_ {\mathbb {R} ^ {d}} e ^ {\mathrm{i} w ^ {\top} x} \tilde {f} _ {\mathrm{e}} (w) w _ {i _ {1}} \ldots w _ {i _ {k}} \mathrm{d} w,\tag{2.63}
$$

which implies the Fourier transform of $\partial _ { x _ { i _ { 1 } } } \cdot \cdot \cdot \partial _ { x _ { i _ { k } } } f _ { \mathrm { e } } ( x )$ is $\tilde { f } _ { \mathrm { e } } ( w ) w _ { i _ { 1 } } \dots w _ { i _ { k } }$ . By Parseval’s identity,

$$
\int_ {\mathbb {R} ^ {d}} \left| \partial_ {x _ {i _ {1}}} \dots \partial_ {x _ {i _ {k}}} f _ {\mathrm{e}} (x) \right| ^ {2} \mathrm{d} x = \int_ {\mathbb {R} ^ {d}} \left| \tilde {f} _ {\mathrm{e}} (w) \right| ^ {2} w _ {i _ {1}} ^ {2} \dots w _ {i _ {k}} ^ {2} \mathrm{d} w.\tag{2.64}
$$

By taking $k = 1$ and $k = s$ in (2.64) and summing up for all indices, we can obtain

$$
\int_ {\mathbb {R} ^ {d}} | \tilde {f} _ {\mathrm{e}} (w) | ^ {2} \left(\| w \| _ {2} ^ {2} + \| w \| _ {2} ^ {2 s}\right) \mathrm{d} w = \int_ {\mathbb {R} ^ {d}} \sum_ {i = 1} ^ {d} | \partial_ {x _ {i}} f _ {\mathrm{e}} | ^ {2} + \sum | D ^ {s} f _ {\mathrm{e}} | ^ {2} \mathrm{d} x \leq \| f _ {\mathrm{e}} \| _ {H ^ {s} (\mathbb {R} ^ {d})} ^ {2} <   \infty ,\tag{2.65}
$$

where the second sum is taken over all s-order partial derivatives. Combining (2.61), (2.62) and (2.65), we conclude $\| f \| _ { B }$ is finite.

In particular, for any $f \in C ^ { s } ( \overline { { \Omega } } )$ , it can always be extended smoothly on $\mathbb { R } ^ { d }$ such that the extension is in $C ^ { s } ( \mathbb { R } ^ { d } ) \cap H ^ { s } ( \mathbb { R } ^ { d } )$ . Therefore, $\| f \| _ { B } < \infty$

## Approximation by ReLU networks

Now let us turn to the approximation by two-layer ReLU networks. We slightly modify the Barron norm (2.28) to the following norm

$$
\| f \| _ {\mathcal {B}, 2} = \inf _ {f _ {\mathrm{e}} \in \mathcal {E} _ {f, \Omega}} \int_ {\mathbb {R} ^ {d}} \| w \| _ {\Omega} ^ {2} | \hat {f} _ {\mathrm{e}} (w) | \mathrm{d} w.\tag{2.66}
$$

Then any Barron function $f$ with $\| f \| _ { B , 2 } < \infty$ can be approximated by two-layer ReLU networks.

Theorem 2.16 (Klusowski & Barron, 2016) Let $M \in \mathbb { Z } ^ { + }$ . Suppose the activation function σ in $\mathcal { N } _ { M }$ is $R e L U$ . Then for any function $f : \Omega \to { \mathbb { R } }$ satisfying $\| f \| _ { B , 2 } < \infty$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} _ {M + 2}} \| \phi - f \| _ {L _ {\mu} ^ {2} (\Omega)} \leq \frac {4 \| f \| _ {\mathcal {B} , 2}}{\sqrt {M}},\tag{2.67}
$$

for every probability measure $\mu .$

Proof: By (2.66), for any $\epsilon > 0$ , there is an extension of f (still denoted by $f )$ such that

$$
\int_ {\mathbb {R} ^ {d}} \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \mathrm{d} w \leq \| f \| _ {\mathcal {B}, 2} + \frac {\epsilon}{4}.\tag{2.68}
$$

Note that

$$
f (x) - x ^ {\top} \nabla f (0) - f (0) = \int_ {\mathbb {R} ^ {d}} \left(e ^ {\mathrm{i} w ^ {\top} x} - \mathrm{i} w ^ {\top} x - 1\right) \hat {f} (w) \mathrm{d} w,\tag{2.69}
$$

which is real. We use the identity

$$
- \int_ {0} ^ {c} [ (y - u) _ {+} e ^ {\mathrm{i} u} + (- y - u) _ {+} e ^ {- \mathrm{i} u} ] \mathrm{d} u = e ^ {\mathrm{i} y} - \mathrm{i} y - 1, \quad \forall y \in [ - c, c ].\tag{2.70}
$$

Taking $\begin{array} { r } { c = \| w \| _ { \Omega } , y = w ^ { \top } x , \alpha = \frac { w } { \| w \| _ { \Omega } } } \end{array}$ in (2.70) and using change of variables $u = \| w \| _ { \Omega } t$ with $t \in [ 0 , 1 ]$ , we have

$$
- \| w \| _ {\Omega} ^ {2} \int_ {0} ^ {1} [ (\alpha^ {\top} x - t) _ {+} e ^ {\mathrm{i} \| w \| _ {\Omega} t} + (- \alpha^ {\top} x - t) _ {+} e ^ {- \mathrm{i} \| w \| _ {\Omega} t} ] \mathrm{d} t = e ^ {\mathrm{i} w ^ {\top} x} - \mathrm{i} w ^ {\top} x - 1.\tag{2.71}
$$

Multiplying the above by $\hat { f } ( w ) = e ^ { \mathrm { i } \theta ( w ) } | \hat { f } ( w ) |$ and integrating over $\mathbb { R } ^ { d }$ , where $\theta ( w )$ is the argument of $\hat { f } ( w )$ . Since the result is real, we obtain

$$
\begin{array}{r l} & {\int_ {\mathbb {R} ^ {d}} \left(e ^ {\mathrm{i} w ^ {\top} x} - \mathrm{i} w ^ {\top} x - 1\right) \hat {f} (w) \mathrm{d} w} \\ & {\qquad = - \int_ {\mathbb {R} ^ {d}} \int_ {0} ^ {1} \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \left[ (\alpha^ {\top} x - t) _ {+} e ^ {\mathrm{i} (\theta (w) + \| w \| _ {\Omega} t)} + (- \alpha^ {\top} x - t) _ {+} e ^ {- \mathrm{i} (\theta (w) - \| w \| _ {\Omega} t)} \right] \mathrm{d} t \mathrm{d} w} \\ & {\qquad = \int_ {\mathbb {R} ^ {d}} \int_ {0} ^ {1} - \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \left[ (\alpha^ {\top} x - t) _ {+} \cos (\theta (w) + \| w \| _ {\Omega} t) + (- \alpha^ {\top} x - t) _ {+} \cos (\theta (w) - \| w \| _ {\Omega} t) \right] \mathrm{d} t \mathrm{d} w} \end{array}\tag{2.72}
$$

Construct the probability density function

$$
p (z, t, w) = \frac {1}{P _ {0}} | \cos (z \| w \| _ {\Omega} t + \theta (w)) | \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \mathrm{for} (z, t, w) \in \{- 1, 1 \} \times [ 0, 1 ] \times \mathbb {R} ^ {d},\tag{2.73}
$$

where the constant $\begin{array} { r } { P _ { 0 } = \int _ { \mathbb { R } ^ { d } } \int _ { 0 } ^ { 1 } \left( | \cos ( \| w \| _ { \Omega ^ { t } } + \theta ( w ) ) | + | \cos ( - \| w \| _ { \Omega ^ { t } } + \theta ( w ) ) | \right) \| w \| _ { \Omega } ^ { 2 } | \hat { f } ( w ) | \mathrm { d } t \mathrm { d } w } \end{array}$ is for normalization. Note that

$$
P _ {0} \leq \int_ {\mathbb {R} ^ {d}} \int_ {0} ^ {1} 2 \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \mathrm{d} t \mathrm{d} w = 2 \int_ {\mathbb {R} ^ {d}} \| w \| _ {\Omega} ^ {2} | \hat {f} (w) | \mathrm{d} w \leq 2 \| f \| _ {\mathcal {B}, 2} + \frac {\epsilon}{2}.\tag{2.74}
$$

Now let $h ( x ; z , t , w ) : = - ( z \alpha ^ { \top } x - t ) _ { + } \cdot \mathrm { s i g n } ( \cos ( z \| w \| _ { \Omega } t + \theta ( w ) ) )$ , then it follows (2.69) and (2.72) that

$$
f (x) - x ^ {\top} \nabla f (0) - f (0) = \sum_ {z = \pm 1} \int_ {\mathbb {R} ^ {d}} \int_ {0} ^ {1} P _ {0} h (x; z, t, w) p (z, t, w) \mathrm{d} t \mathrm{d} w,\tag{2.75}
$$

For the given M, we define $( \xi , \eta , \zeta ) , ( \xi _ { 1 } , \eta _ { 1 } , \zeta _ { 1 } ) , \ldots , ( \xi _ { M } , \eta _ { M } , \zeta _ { M } )$ as i.i.d. random variables under the density $p ( z , t , w )$ , then

$$
f (x) - x ^ {\top} \nabla f (0) - f (0) = \mathbb {E} _ {\xi , \eta , \zeta \sim p} P _ {0} h (x; \xi , \eta , \zeta).\tag{2.76}
$$

Moreover, we define the random variable $\begin{array} { r } { \psi ( x ) = \frac { 1 } { M } \sum _ { m = 1 } ^ { M } P _ { 0 } h ( x ; \xi _ { m } , \eta _ { m } , \zeta _ { m } ) } \end{array}$ . Note that

$$
\begin{array}{c} \| P _ {0} h \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} = P _ {0} ^ {2} \int_ {\Omega} | z \alpha^ {\top} x - t | ^ {2} \mu (\mathrm{d} x) \leq P _ {0} ^ {2} \int_ {\Omega} (| z | | \alpha^ {\top} x | + | t |) ^ {2} \mu (\mathrm{d} x) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{2.77}
$$

By the argument similar to (2.34)-(2.35), there exist samples of $\{ \xi _ { m } , \eta _ { m } , \zeta _ { m } \}$ (still denoted by $\{ \xi _ { m } , \eta _ { m } , \zeta _ { m } \} )$ such that the corresponding sampled $\psi$ satisfies

$$
\| \psi (x) - (f (x) - x ^ {\top} \nabla f (0) - f (0)) \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} \leq \frac {1}{M} \| P _ {0} h \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} \leq \frac {(4 \| f \| _ {\mathcal {B} , 2} + \epsilon) ^ {2}}{M}.\tag{2.78}
$$

Denote $\phi ( x ) = \psi ( x ) + { x } ^ { \top } \nabla f ( 0 ) + f ( 0 )$ , then

$$
\begin{array}{l} \phi (x) = \psi (x) + x ^ {\top} \nabla f (0) + f (0) \\ \qquad = \sum_ {m = 1} ^ {M} - \frac {P _ {0}}{M} \text {sign} (\cos (\xi_ {m} \| \zeta_ {m} \| _ {\Omega} \eta_ {m} + \theta (\zeta_ {m}))) \sigma (\xi_ {m} \frac {\zeta_ {m} ^ {\top}}{\| \zeta_ {m} \| _ {\Omega}} x - \eta_ {m}) \\ \qquad \qquad \qquad \qquad + \sigma (\nabla f (0) ^ {\top} x) - \sigma (- \nabla f (0) ^ {\top} x) + f (0), \end{array}\tag{2.79}
$$

which is in $\mathcal { N } _ { M + 2 }$ . Therefore, (2.78) means that for any small ϵ, we can always find $\phi \in \mathcal { N } _ { M + 2 }$ such that the error $\| \phi - f \| _ { L _ { \mu } ^ { 2 } ( \Omega ) }$ is bounded by $\frac { 4 \| f \| _ { \displaystyle B , 2 } + \epsilon } { \sqrt { M } }$ , which is exactly the desired result (2.67). □

## 2.3.2 Barron-type spaces

From Lemma 2.11, for any $f \in \Gamma _ { C , \Omega }$ , the function $f ( x ) - f ( 0 )$ can be approximated by linear combinations of sigmoid neurons $\{ a \sigma ( \boldsymbol { w } ^ { \top } \boldsymbol { x } + b ) \}$ up to any desired accuracy with positive coeficients summed up to 1. Formally, we have

$$
f (x) - f (0) = \sum_ {m = 1} ^ {\infty} \rho_ {m} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m})\tag{2.80}
$$

where $\rho _ { m } > 0$ and $\textstyle \sum _ { m = 1 } ^ { \infty } \rho _ { m } = 1$ . By Riemann-Stieltjes integration theory, (2.80) can be written as an integral with variables a, w and b under some probability measure $\rho$ on $\mathbb { R } \times \mathbb { R } ^ { d } \times \mathbb { R }$ ; namely,

$$
f (x) - f (0) = \int_ {\mathbb {R} \times \mathbb {R} ^ {d} \times \mathbb {R}} a \sigma (w ^ {\top} x + b) \rho (\mathrm{d} a, \mathrm{d} w, \mathrm{d} b).\tag{2.81}
$$

The representation (2.81) can be generalized by taking $\sigma$ as any type of activation functions and removing the constant f(0); namely,

$$
f (x) = \int_ {\mathbb {R} \times \mathbb {R} ^ {d} \times \mathbb {R}} a \sigma (w ^ {\top} x + b) \rho (\mathrm{d} a, \mathrm{d} w, \mathrm{d} b), \quad \forall x \in \Omega ,\tag{2.82}
$$

where $\Omega$ is a bounded domain in $\mathbb { R } ^ { d }$ . Accordingly, given $1 \leq p \leq \infty$ , the Barron-type space is characterized by

$\begin{array} { r } { B _ { p } ^ { \prime } = \Big \{ f \in C ( \Omega ) : } \end{array}$ f has the representation (2.82)

$$
\text { for   some   probability   measure } \rho , \| f \| _ {\mathcal {B} _ {p} ^ {\prime}} <   \infty \Big \}\tag{2.83}
$$

with

$$
\| f \| _ {\mathcal {B} _ {p} ^ {\prime}} := \inf _ {\rho} \left(\mathbb {E} _ {(a, w, b) \sim \rho} [ | a | ^ {p} (\| w \| _ {\Omega} + | b |) ^ {p} ]\right) ^ {1 / p},\tag{2.84}
$$

where the infimum is taken over all $\rho$ for which (2.82) holds.

In [3], the representation (2.82) with ReLU activation and $\Omega = I _ { d }$ is considered. Using H¨older’s inequality, one can trivially prove $B _ { \infty } ^ { \prime } \subset \ldots B _ { 2 } ^ { \prime } \subset B _ { 1 } ^ { \prime }$ . And for ReLU activation, we can also prove $B _ { 1 } ^ { \prime } \subset B _ { \infty } ^ { \prime }$ and $\| f \| _ { B _ { 1 } ^ { \prime } } = \| f \| _ { B _ { \infty } ^ { \prime } }$ for all $f \in B _ { 1 } ^ { \prime }$ . Consequently, $B _ { p } ^ { \prime }$ with $\| \cdot \| _ { B _ { p } ^ { \prime } }$ are the same for all $p .$ So we can merely use $B ^ { \prime }$ and $\| \cdot \| _ { B ^ { \prime } }$ to denote this Barron-type space and norm. Barron-type spaces for other activation functions are discussed in [5, 9].

The approximation theorem is given as follows.

Theorem 2.17 Let $M \in \mathbb { Z } ^ { + }$ . Suppose the activation function $\sigma$ in $\mathcal { N } _ { M }$ is $R e L U$ Then for any function $f \in B ^ { \prime }$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} _ {M}} \| \phi - f \| _ {L _ {\mu} ^ {2} (\Omega)} \leq \frac {\| f \| _ {\mathcal {B} ^ {\prime}}}{\sqrt {M}},\tag{2.85}
$$

for every probability measure $\mu .$

Proof: By the definition of (2.83), for any $\epsilon > 0$ , there exists some probability measure $\rho$ such that

$$
f (x) = \int_ {\mathbb {R} \times \mathbb {R} ^ {d} \times \mathbb {R}} a \sigma (w ^ {\top} x + b) \rho (\mathrm{d} a, \mathrm{d} w, \mathrm{d} b) = \mathbb {E} _ {(a, w, b) \sim \rho} [ a \sigma (w ^ {\top} x + b) ], \quad \forall x \in \Omega ,\tag{2.86}
$$

and

$$
\left(\mathbb {E} _ {(a, w, b) \sim \rho} [ | a | ^ {2} (\| w \| _ {\Omega} + | b |) ^ {2} ]\right) ^ {1 / 2} \leq \| f \| _ {\mathcal {B} ^ {\prime}} + \epsilon .\tag{2.87}
$$

For all $( a , w , b ) \in \mathbb { R } \times \mathbb { R } ^ { d } \times$ R, using the facts $| \sigma ( t ) | \leq | t |$ , we have

$$
\begin{array}{r l} & {\| a \sigma (w ^ {\top} x + b) \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} = \int_ {\Omega} | a \sigma (w ^ {\top} x + b) | ^ {2} \mu (\mathrm{d} x)} \\ & {\qquad \leq \int_ {\Omega} | a | ^ {2} (\| w \| _ {\Omega} + | b |) ^ {2} \mu (\mathrm{d} x) = | a | ^ {2} (\| w \| _ {\Omega} + | b |) ^ {2}.} \end{array}\tag{2.88}
$$

So

$$
\mathbb {E} _ {(a, w, b) \sim \rho} \left[ \| a \sigma (w ^ {\top} x + b) \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} \right] \leq \mathbb {E} _ {(a, w, b) \sim \rho} \left[ | a | ^ {2} (\| w \| _ {\Omega} + | b |) ^ {2} \right] \leq (\| f \| _ {\mathcal {B} ^ {\prime}} + \epsilon) ^ {2}.\tag{2.89}
$$

Let $( a _ { 1 } , w _ { 1 } , b _ { 1 } ) , \dots , ( a _ { M } , w _ { M } , b _ { M } )$ be i.i.d. random variables in $\mathbb { R } \times \mathbb { R } ^ { d } \times \mathbb { R }$ under the distribution $\rho .$ Using the argument similar to (2.34) and, we can derive

$$
\begin{array}{r l} & {\mathbb {E} _ {\{(a _ {m}, w _ {m}, b _ {m}) \} \sim \rho^ {M}} \left\| \sum_ {m = 1} ^ {M} \frac {1}{M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}) - \mathbb {E} _ {(a, w, b) \sim \rho} [ a \sigma (w ^ {\top} x + b) ] \right\| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2}} \\ & {\qquad \leq \frac {1}{M} \mathbb {E} _ {(a, w, b) \sim \rho} \left[ \| a \sigma (w ^ {\top} x + b) \| _ {L _ {\mu} ^ {2} (\Omega)} ^ {2} \right] \leq \frac {(\| f \| _ {\mathcal {B} ^ {\prime}} + \epsilon) ^ {2}}{M},} \end{array}\tag{2.90}
$$

which implies that there exists a set of samples of $\{ ( a _ { m } , w _ { m } , b _ { m } ) \}$ (still denoted by $\{ ( a _ { m } , w _ { m } , b _ { m } ) \} )$ such that

$$
\left\| \sum_ {m = 1} ^ {M} \frac {1}{M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}) - f (x) \right\| _ {L _ {\mu} ^ {2} (\Omega)} \leq \frac {\| f \| _ {\mathcal {B} ^ {\prime}} + \epsilon}{\sqrt {M}}.\tag{2.91}
$$

The proof is then completed by noting that $\begin{array} { r } { \phi ( x ) : = \sum _ { m = 1 } ^ { M } \frac { 1 } { M } a _ { m } \sigma ( w _ { m } ^ { \top } x + b _ { m } ) } \end{array}$ is in $\mathcal { N } _ { M }$ and using the arbitrariness of $\epsilon .$ □

A $L ^ { \infty } .$ -version of Theorem 2.17 can be found in [4], but the bound is $\frac { 4 \sqrt { d + 1 } \| f \| _ { B ^ { \prime } } } { \sqrt { M } }$

## 2.3.3 Higher-order derivatives

Preceding theorems describe the $L ^ { 2 }$ and $L ^ { \infty }$ -errors between the best approximating neural network and the target Barron function. However, in many applications, we are interested in the error characterized by Sobolev norms $\| \cdot \| _ { H ^ { s } }$ . In this case, the approximating neural network should have regularity $s ,$ and so is the activation function. To estimate the error bound, in the work [15, 16] the following generalized spectral Barron norm is defined:

$$
\| f \| _ {\mathcal {B} ^ {s}} := \inf _ {f _ {\mathrm{e}} \in \mathcal {E} _ {f, \Omega}} \int_ {\mathbb {R} ^ {d}} (1 + \| \omega \| _ {2}) ^ {s} | \hat {f} _ {\mathrm{e}} (\omega) | \mathrm{d} \omega
$$

for any $f : \Omega \to { \mathbb { R } }$ that $\mathcal { E } _ { f , \Omega }$ is non-empty. Then the following estimate holds:

Theorem 2.18 Suppose the activation function in $\mathcal { N } _ { M }$ is given by $\sigma ( t ) = ( 1 + e ^ { - t } ) ^ { - 1 }$ or arctan(t) or tanh(t) or ln(1+e<sup>t</sup>). Let $s \geq 0$ be an integer. Then for any function $g : \Omega  \mathbb { R }$ with $\| g \| _ { B ^ { s + 1 } } < \infty$ 2 it holds that Q

$$
\inf _ {f \in \mathcal {N} _ {M}} \| f - g \| _ {H ^ {s} (\Omega)} \leq \frac {C \| g \| _ {\mathcal {B} ^ {s + 1}}}{\sqrt {M}},
$$

where $C > 0$ is a constant only depending on $\Omega , \sigma _ { \cdot }$ , and s.

An improvement on the convergence rate was made in [16] for the $\mathrm { R e L U } ^ { k }$ activation function, i.e., $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \} ^ { k }$ for some integer $k \geq 1$ . It shows that given $g : \Omega  \mathbb { R }$ with $\| g \| _ { B ^ { \alpha } } < \infty$ for some $\alpha \geq 0 , \operatorname { i f } \alpha > ( d + 1 ) ( k - s + { \frac { 1 } { 2 } } ) + s + { \frac { 1 } { 2 } }$ , then there is a two-layer neural network $f$ with width $M$ and activation σ satisfying

$$
\| f - g \| _ {H ^ {s} (\Omega)} \leq C \| g \| _ {\mathcal {B} ^ {\alpha}} M ^ {s - k - 1} \ln M.
$$

In this case, the convergence rate with respect to M is increased from $\scriptstyle { { \frac { 1 } { 2 } } - \operatorname { t h } }$ order to $\left( k - s + 1 \right)$ -th order.

## 2.3.4 Approximation by deep and wide networks

Previous results are all for the approximation of two-layer neural networks. In this part, we show some latest results for neural networks with arbitrary depth and width. In [13], the following approximation theorem for continuous functions is given.

Theorem 2.19 Given $g \in C ( I _ { d } )$ , for any J, $K \in \mathbb { Z } ^ { + }$ , and $1 \leq p \leq \infty$ , there exists a neural network f with ReLU activation, which satisfies:

(i) f has $1 2 J + C _ { 2 }$ hidden layers;

(ii) the width of every hidden layer of f is no more than $C _ { 1 }$ max $\{ d \lfloor K ^ { 1 / d } \rfloor , K + 1 \}$

$$
\| f - g \| _ {L ^ {p} (I _ {d})} \leq 1 9 \sqrt {d} \omega_ {g} (K ^ {- 2 / d} J ^ {- 2 / d}),
$$

where

$$
C _ {1} = \left\{ \begin{array}{l l} 1 2, & 1 \leq p <   \infty , \\ 3 ^ {d + 3}, & p = \infty \end{array} \right., \quad C _ {2} = \left\{ \begin{array}{l l} 1 4, & 1 \leq p <   \infty , \\ 1 4 + 2 d, & p = \infty \end{array} \right.,
$$

$$
\omega_ {g} (r) := \sup \left\{\left| g (x) - g (y) \right|: x, y \in I _ {d}, \| x - y \| _ {2} \leq r \right\}, \quad \forall r \geq 0.
$$

Note that $\omega _ { g }$ characterizes the continuity of g. Specifically, if $g$ is Lipschitz continuous with constant $c , \mathrm { i . e . , } | g ( x ) - g ( y ) | \leq c \| x - y \| _ { 2 }$ for all $x , y \in I _ { d }$ , then $\omega _ { g } ( r ) \leq c r$

The error bound given in Theorem 2.19 still sufers from the curse of dimensionality, since the convergence rate has the form $O ( 1 / d )$ . Another similar result for smooth functions is presented in [10], which is given as follows.

Theorem 2.20 Given $g \in C ^ { s } ( I _ { d } )$ with $s \in \mathbb { Z } ^ { + }$ , for any integers $M \geq 1 7 s ^ { d + 1 } 3 ^ { d + 2 } d$ and $L \ \geq$ $1 0 8 s ^ { 2 } + 2 d$ , there exists a neural network f with ReLU activation, which satisfies:

(i) f has L hidden layers;

(ii) the width of every hidden layer of f is no more than $M$

such that

$$
\begin{array}{c} \| f - g \| _ {L ^ {\infty} (I _ {d})} \leq \\ 8 5 (s + 1) ^ {d} 8 ^ {s} \| g \| _ {C ^ {s} (I _ {d})} \left(\frac {M}{6 8 s ^ {d + 1} 3 ^ {d} d \log_ {2} (8 M + 8)}\right) ^ {- 2 s / d} \left(\frac {L - 2 d}{7 2 s ^ {2} \log_ {2} (4 L + 4)}\right) ^ {- 2 s / d}. \end{array}
$$

An improved result that can lessen the curse of dimensionality is presented in [14], which is given as follows.

Theorem 2.21 Given $g \in C ( I _ { d } )$ , for any integers $M \geq \operatorname* { m a x } \{ d , 1 8 \}$ and $L \geq 6 4 d + 3$ , there exists a neural network f, which satisfies:

(i) f has L hidden layers;

(ii) the width of every hidden layer of f is no more than M;

(iii) the activation function of every neuron is either Floor function $\sigma ( t ) = \lfloor t \rfloor$ or ReLU function $\sigma ( t ) = \operatorname* { m a x } \{ 0 , t \}$ ,

such that

$$
\| f - g \| _ {L ^ {\infty} (I _ {d})} \leq \omega_ {g} \left(\sqrt {d} \lfloor \frac {M - 1 3}{5} \rfloor^ {- \sqrt {\lfloor \frac {L - 3}{6 4 d} \rfloor}}\right) + 2 \omega_ {g} (\sqrt {d}) \lfloor \frac {M - 1 3}{5} \rfloor^ {- \sqrt {\lfloor \frac {L - 3}{6 4 d} \rfloor}}.
$$

In Theorem 2.21, one can set $L = O ( d )$ so that the power of $\lfloor \frac { M - 1 3 } { 5 } \rfloor$ is independent of $d ,$ obtaining a convergence rate independent of the dimension.

## 2.4 Exact Learning

By exact learning we mean that the neural network can exactly express the desired target function. That is, the error between the network and target function is identically zero. Even if this is unlikely to occur in general, there are a few particular cases when this happens. These cases will be discussed in this section.

## 2.4.1 Fitting a finite dataset

We shall start with the simplest case of finite support functions, i.e. the functions defined on a set of finite points. More precisely, let $\Gamma = \{ x _ { 1 } , x _ { 2 } , \ldots , x _ { N } \} \subset \mathbb { R } ^ { d }$ be a set consisting of N distinct points in $\mathbb { R } ^ { d }$ . Then any function $f : \Gamma \to \mathbb { R }$ can be viewed as a finite support function. Learning f requires to find a neural network $\phi : \mathbb { R } ^ { d } $ R such that $\phi ( x _ { n } ) \approx f ( x _ { n } )$ for $n = 1 , \ldots , N$ . In another perspective, it is finding a neural network $\phi$ such that $\phi ( x _ { n } ) \approx y _ { n }$ given a dataset $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ where $y _ { n } : = f ( x _ { n } )$ . So learning a finite support function is equivalent to fitting a finite dataset.

For simplicity, we consider the two-layer neural network $\phi : \mathbb { R } ^ { d }  \mathbb { R }$ given by

$$
\phi (x) = \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}),
$$

where $w _ { m } \in \mathbb { R } ^ { d } , a _ { m } , b _ { m } \in \mathbb { R } , M \in \mathbb { Z } ^ { + }$ . We expect that $\phi$ fits the data $\{ ( x _ { n } , y _ { n } ) \} _ { n = 1 } ^ { N }$ exactly, i.e. $\phi ( x _ { n } ) = y _ { n }$ , which leads to

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {1} + b _ {m}) = y _ {1}
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {2} + b _ {m}) = y _ {2}\tag{2.92}
$$

$$
\sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x _ {N} + b _ {m}) = y _ {N}
$$

Since the data $\left\{ \left( x _ { n } , y _ { n } \right) \right\}$ is fixed, finding a neural network $\phi$ that fits the data exactly is equivalent to finding free parameters $\{ a _ { m } , w _ { m } , b _ { m } \}$ such that the equations (2.92) are satisfied. Note the equations are usually nonlinear with respect to the free parameters since the activation function $\sigma$ is usually nonlinear.

The number of equations is fixed as M. So as N becomes larger, the equations (2.92) will have more unknowns and are hence more likely to have a solution. Actually, it sufices to let $M = N$ to guarantee the existence of solutions for many types of activation function σ. Note that (2.92) with $M = N$ can be rewritten as

$$
\boldsymbol {A} _ {w, b} \boldsymbol {a} = \boldsymbol {y},\tag{2.93}
$$

where

$$
\boldsymbol {A} _ {w, b} = \left[ \begin{array}{c c c c} \sigma (w _ {1} ^ {\top} x _ {1} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {1} + b _ {2}) & \dots & \sigma (w _ {N} ^ {\top} x _ {1} + b _ {N}) \\ \sigma (w _ {1} ^ {\top} x _ {2} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {2} + b _ {2}) & \dots & \sigma (w _ {N} ^ {\top} x _ {2} + b _ {N}) \\ \vdots & \vdots & \ddots & \vdots \\ \sigma (w _ {1} ^ {\top} x _ {N} + b _ {1}) & \sigma (w _ {2} ^ {\top} x _ {N} + b _ {2}) & \dots & \sigma (w _ {N} ^ {\top} x _ {N} + b _ {N}) \end{array} \right], \boldsymbol {a} = \left[ \begin{array}{c} a _ {1} \\ a _ {2} \\ \vdots \\ a _ {N} \end{array} \right], \boldsymbol {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {N} \end{array} \right].
$$

One simple way to find solutions of (2.92) is constructing $\{ w _ { m } , b _ { m } \}$ such that the matrix $A _ { w , b }$ is invertible, and then $\{ a _ { m } \}$ can be directly found by $\pmb { a } = \pmb { A } _ { w , b } ^ { - 1 } \pmb { y } .$

We take the ReLU activation function as an example. Suppose that $\sigma ( x ) = \mathrm { R e L U } ( x ) =$ $\operatorname* { m a x } \{ 0 , x \}$ . Consider the finite number of hyperplanes, ${ \mathcal { H } } _ { i j } = \{ z \in \mathbb { R } ^ { d } : z ^ { \top } ( x _ { i } - x _ { j } ) = 0 \}$ for $1 \leq i < j \leq N$ . Then we choose a vector $w \in \mathbb { R } ^ { d }$ such that w does not belong to any of the hyperplanes, i.e.

$$
w \in \mathbb {R} ^ {d} \backslash \bigcup_ {i <   j} \mathcal {H} _ {i j}.
$$

Then for any $i \neq j , w ^ { \top } x _ { i } \neq w ^ { \top } x _ { j }$ . Without loss of generality, we assume that

$$
w ^ {\top} x _ {1} <   w ^ {\top} x _ {2} <   \dots <   w ^ {\top} x _ {N}.
$$

Then there exist $b _ { 1 } , b _ { 2 } , \dotsc , b _ { N } \in \mathbb { R }$ such that

$$
- b _ {1} <   w ^ {\top} x _ {1} <   - b _ {2} <   w ^ {\top} x _ {2} <   \dots <   - b _ {N - 1} <   w ^ {\top} x _ {N - 1} <   - b _ {N} <   w ^ {\top} x _ {N}.
$$

Finally, let $w _ { 1 } = w _ { 2 } = \cdot \cdot \cdot = w _ { N } = w$ . We have

$$
\left\{ \begin{array}{l l} w _ {i} ^ {\top} x _ {j} + b _ {i} <   0, & \text { if } j <   i, \\ w _ {i} ^ {\top} x _ {j} + b _ {i} > 0, & \text { if } j \geq i. \end{array} \right.
$$

So

$$
\boldsymbol {A} _ {w, b} = \left[ \begin{array}{c c c c} w _ {1} ^ {\top} x _ {1} + b _ {1} & 0 & \dots & 0 \\ w _ {1} ^ {\top} x _ {2} + b _ {1} & w _ {2} ^ {\top} x _ {2} + b _ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ w _ {1} ^ {\top} x _ {N} + b _ {1} & w _ {2} ^ {\top} x _ {N} + b _ {2} & \dots & w _ {N} ^ {\top} x _ {N} + b _ {N} \end{array} \right]
$$

is a lower-triangular matrix with positive diagonals, which is invertible. Therefore, we obtain the following result.

Proposition 2.6 Given N data samples, $( x _ { n } , y _ { n } ) \in \mathbb { R } ^ { d } \times \mathbb { R } , 1 \leq n \leq N$ , there is a two-layer ReLU neural network $\begin{array} { r } { \phi ( x ) = \sum _ { m = 1 } ^ { N } a _ { m } \mathrm { R e L U } ( w _ { m } ^ { \top } x + b _ { m } ) } \end{array}$ with $w _ { m } \in \mathbb { R } ^ { d } , a _ { m } , b _ { m } \in \mathbb { R }$ such that

$$
\phi (x _ {n}) = y _ {n}, \quad \forall 1 \leq n \leq N.
$$

We remark that Proposition 2.6 also holds for many other types of activation functions, e.g. Heaviside activation function. And these results can be proved by similar argument.

## 2.4.2 Exact learning with ReLU

We consider the fully-connected neural networks with ReLU activation in all hidden-layers and linear activation in the output layer, i.e. $\phi : \mathbb { R } ^ { d } $ R given by

$$
\phi (x) = a ^ {\top} \sigma \Big (W ^ {L} \sigma \big (\ldots \sigma (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b,\tag{2.94}
$$

where $\sigma ( t ) = \operatorname { R e L U } ( t ) = \operatorname* { m a x } \{ 0 , t \}$ , and $a \in \mathbb { R } ^ { M _ { L } \times 1 } , b \in \mathbb { R } , W ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times M _ { \ell - 1 } } , b ^ { \ell } \in \mathbb { R } ^ { M _ { \ell } \times 1 } ( M _ { \ell } \in \mathbb { Z } ^ { + }$ for $\ell = 1 , \dots , L ; M _ { 0 } : = d )$ are the free parameters.

In Section 2.1.5, we mentioned that the neural networks with ReLU activation are piecewise linear functions. Simply speaking, ReLU networks have more pieces if they are deep or wider. Conversely, given a piecewise linear function, we can always find a ReLU network that is equal to it. Or equivalently, we can always represent a piecewise linear function by a ReLU network. For example, the absolute value function $f ( t ) = | t | , t \in \mathbb { R }$ can be written as

$$
| t | = \operatorname{ReLU} (t) + \operatorname{ReLU} (- t),\tag{2.95}
$$

which can be viewed as a two-layer neural network with two neurons in the hidden layer.

## Representation of maximum function

Since the maximum function $f ( x _ { 1 } , \dots , x _ { d } ) = \operatorname* { m a x } \{ x _ { 1 } , \dots , x _ { d } \}$ is a piecewise linear function, we consider the representation of the maximum function using ReLU networks. First, we consider the simple case when $d = 2$ . Using the relation (2.95) and

$$
t = \mathrm{ReLU} (t) - \mathrm{ReLU} (- t), \quad \forall t \in \mathbb {R},
$$

we have

$$
\begin{array}{l} \max \{x _ {1}, x _ {2} \} = \frac {1}{2} (x _ {1} + x _ {2} + | x _ {1} - x _ {2} |) \\ \qquad = \frac {1}{2} (\operatorname{ReLU} (x _ {1} + x _ {2}) - \operatorname{ReLU} (- x _ {1} - x _ {2}) + \operatorname{ReLU} (x _ {1} - x _ {2}) + \operatorname{ReLU} (- x _ {1} + x _ {2})) \\ \qquad = \frac {1}{2} \operatorname{ReLU} (x _ {1} + x _ {2}) - \frac {1}{2} \operatorname{ReLU} (- x _ {1} - x _ {2}) + \frac {1}{2} \operatorname{ReLU} (x _ {1} - x _ {2}) + \frac {1}{2} \operatorname{ReLU} (- x _ {1} + x _ {2}). \end{array}
$$

Or in matrix form,

$$
\max \{x _ {1}, x _ {2} \} = \left[ \begin{array}{c c c c} \frac {1}{2} & - \frac {1}{2} & \frac {1}{2} & \frac {1}{2} \end{array} \right] \operatorname{ReLU} (\left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 1 \\ 1 & - 1 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]),\tag{2.96}
$$

which can be viewed as a two-layer neural network with four neurons in the hidden layer.

In more general case, we have the following result.

Proposition 2.7 The function $f ( x _ { 1 } , \dots , x _ { d } ) = \operatorname* { m a x } \{ x _ { 1 } , \dots , x _ { d } \}$ can be represented exactly by a $R e L U$ neural network given by (2.94) with

$$
L = \left\{ \begin{array}{l l} k, & \text {if d = 2^{k} for some k\in\mathbb {Z} ^{+}}, \\ \lfloor \log_ {2} d \rfloor + 1, & \text {if d\neq 2^{k} for all k\in\mathbb {Z} ^{+}}. \end{array} \right.
$$

Proof: For $d = 2 ^ { k }$ , we can prove the statement by induction over $k .$

The case $k = 1$ follows from the previous discussion, which shows that max $\{ x _ { 1 } , x _ { 2 } \}$ can be represented exactly by (2.96). In this case the network has one hidden layer $( L = 1 )$ , and its biases are all zero.

We assume that when $d = 2 ^ { k - 1 } , f ( x _ { 1 } , \dots , x _ { 2 ^ { k - 1 } } ) = \operatorname* { m a x } \{ x _ { 1 } , \dots , x _ { 2 ^ { k - 1 } } \}$ can be represented exactly by a network $\phi ( x _ { 1 } , \ldots , x _ { 2 ^ { k - 1 } } )$ with $L = k - 1$ hidden layers and zero biases, which is given by

$$
\phi (y) = a ^ {\top} \sigma \left(W ^ {k - 1} \sigma \left(\dots \sigma \left(W ^ {1} y\right) \dots\right)\right),
$$

where $\sigma = { \mathrm { R e L U } } ( x ) , y = \left[ x _ { 1 } \ \dots \ x _ { 2 ^ { k - 1 } } \right] ^ { \top }$ , a is a column vector and $W ^ { \ell }$ are matrices. Then using (2.96), we obtain

$$
\begin{array}{l} f (x _ {1}, \ldots , x _ {2 ^ {k}}) = \max \{x _ {1}, \ldots , x _ {2 ^ {k}} \} \\ \qquad = \max \{\max \{x _ {1}, \ldots , x _ {2 ^ {k - 1}} \}, \max \{x _ {2 ^ {k - 1} + 1}, \ldots , x _ {2 ^ {k - 1} + 2 ^ {k - 1}} \} \} \\ \qquad = \max \{\phi (x _ {1}, \ldots , x _ {2 ^ {k - 1}}), \phi (x _ {2 ^ {k - 1} + 1}, \ldots , x _ {2 ^ {k - 1} + 2 ^ {k - 1}}) \} \\ \qquad = \left[ \begin{array}{c c c c} \frac {1}{2} & - \frac {1}{2} & \frac {1}{2} & \frac {1}{2} \end{array} \right] \sigma \Big (\left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 1 \\ 1 & - 1 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{c} \phi (x _ {1}, \ldots , x _ {2 ^ {k - 1}}) \\ \phi (x _ {2 ^ {k - 1} + 1}, \ldots , x _ {2 ^ {k - 1} + 2 ^ {k - 1}}) \end{array} \right] \Big). \end{array}\tag{2.97}
$$

Note that

$$
\left[ \begin{array}{c} \phi (x _ {1}, \ldots , x _ {2 ^ {k - 1}}) \\ \phi (x _ {2 ^ {k - 1} + 1}, \ldots , x _ {2 ^ {k - 1} + 2 ^ {k - 1}}) \end{array} \right] = \left[ \begin{array}{c c} a ^ {\top} & \\ & a ^ {\top} \end{array} \right] \sigma \Big (\left[ \begin{array}{c c} W ^ {k - 1} & \\ & W ^ {k - 1} \end{array} \right] \sigma \big (\ldots \sigma (\left[ \begin{array}{c c} W ^ {1} & \\ & W ^ {1} \end{array} \right] \tilde {y}) \ldots \big) \Big),\tag{2.98}
$$

where $\tilde { y } = [ x _ { 1 } \dots x _ { 2 ^ { k } } ] ^ { \top }$ , is a ReLU network with $L = k - 1$ from $\mathbb { R } ^ { 2 ^ { k } }$ to $\mathbb { R } ^ { 2 }$ . Therefore, (2.97) and (2.98) imply that

$$
f (x _ {1}, \dots , x _ {2 ^ {k}}) = \tilde {a} ^ {\top} \sigma \Big (\tilde {W} ^ {k} \sigma \big (\tilde {W} ^ {k - 1} \sigma \big (\dots \sigma (\tilde {W} ^ {1} \tilde {y}) \dots \big) \big) \Big),
$$

where

$$
\tilde {a} ^ {\top} = \left[ \begin{array}{c c c c} \frac {1}{2} & - \frac {1}{2} & \frac {1}{2} & \frac {1}{2} \end{array} \right], \quad \tilde {W} ^ {k} = \left[ \begin{array}{c c} 1 & 1 \\ - 1 & - 1 \\ 1 & - 1 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{c c} a ^ {\top} & \\ & a ^ {\top} \end{array} \right]
$$

$$
\tilde {W} ^ {\ell} = \left[ \begin{array}{c c} W ^ {\ell} & \\ & W ^ {\ell} \end{array} \right] \text { for } \ell = 1, \ldots , k - 1.
$$

This finishes the proof for $d = 2 ^ { k }$

For $2 ^ { k - 1 } < d < 2 ^ { k }$ for some $k \in \mathbb { Z } ^ { + }$ , we note the fact that

$$
\left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {d} \\ \vdots \\ x _ {d} \end{array} \right] _ {2 ^ {k} \times 1} = \left[ \begin{array}{c c c c} 1 & & & \\ & 1 & & \\ & & \ddots & \\ & & & 1 \\ & & & 1 \\ & & & \vdots \\ & & & 1 \end{array} \right] _ {2 ^ {k} \times d} \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {d} \end{array} \right] _ {d \times 1} := E \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {d} \end{array} \right] _ {d \times 1}.
$$

By the preceding result, for $d = 2 ^ { k }$ , we have

$$
\max \{x _ {1}, \ldots , x _ {2 ^ {k}} \} = a ^ {\top} \sigma \Big (W ^ {k} \sigma \big (\ldots \sigma (W ^ {1} \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {2 ^ {k}} \end{array} \right]) \ldots \big) \Big),
$$

for some column vector a and matrices $W ^ { \ell } \left( \ell = 1 , \ldots , k \right)$ . Therefore,

$$
f (x _ {1}, \ldots , x _ {d}) = \max \{x _ {1}, \ldots , x _ {d} \} = \max \{x _ {1}, \ldots , x _ {d}, \underbrace {x _ {d} , x _ {d} , \ldots , x _ {d}} _ {2 ^ {k} - d \text {times}} \}
$$

$$
= a ^ {\top} \sigma \Big (W ^ {k} \sigma \big (\dots \sigma (W ^ {1} \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ \vdots \\ x _ {d} \end{array} \right]) \dots \big) \Big) = a ^ {\top} \sigma \Big (W ^ {k} \sigma \big (\dots \sigma (W ^ {1, *} \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \end{array} \right] _ {d \times 1}) \dots \big) \Big),\tag{2.99}
$$

where $W ^ { 1 , * } = W ^ { 1 } E$ . Since $\lfloor \log _ { 2 } d \rfloor = k - 1$ , (2.99) finishes the proof for $d < 2 ^ { k }$

It is worth noting that a similar result holds for representing the minimum of d numbers. The proof is similar, using the formula

$$
\min \left\{x _ {1}, x _ {2} \right\} = \frac {1}{2} \left(x _ {1} + x _ {2} - | x _ {1} - x _ {2} |\right).
$$

## Width versus depth

A shallow ReLU neural network with large width can be transformed to a deep ReLU neural network with limited width. This fact is shown in the following result.

Proposition 2.8 Suppose $\sigma ( x ) = \mathrm { R e L U } ( x )$ . Let $\phi : \mathbb { R } ^ { d }  \mathbb { R }$ be a neural network with one hidden layer given $b y$

$$
\phi (x) = a _ {0} + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}),
$$

where $a _ { 0 } , a _ { m } , b _ { m } \in \mathbb { R }$ and $w _ { m } \in \mathbb { R } ^ { d }$ . Then $\phi$ can be represented exactly by a deep $R e L U$ neural network $\hat { \phi } : \mathbb { R } ^ { d }  \mathbb { R } \ o n \ [ 0 , 1 ] ^ { d }$ , which has $M + 1$ hidden layers, each of width $d + 2 ,$ namely,

$$
\phi (x) = \hat {\phi} (x) = \hat {a} ^ {\top} \sigma \Big (\hat {W} ^ {M + 1} \sigma \big (\dots \sigma (\hat {W} ^ {1} x + \hat {b} ^ {1}) \dots \big) + \hat {b} ^ {M + 1} \Big) + \hat {b}, \quad \forall x \in [ 0, 1 ] ^ {d},
$$

where $\begin{array} { r } { \hat { a } , \hat { b } ^ { \ell } \in \mathbb { R } ^ { d + 2 } \ f o r \ \ell = 1 , \dots , M + 1 ; \hat { W } ^ { 1 } \in \mathbb { R } ^ { ( d + 2 ) \times d } ; \hat { W } ^ { \ell } \in \mathbb { R } ^ { ( d + 2 ) \times ( d + 2 ) } \ f o r \ \ell = 2 , \dots , M + 1 , } \end{array}$ $\hat { b } \in \mathbb { R }$

Proof: We shall construct the network $\hat { \phi }$ by choosing appropriate $\{ \hat { a } , \hat { b } , \hat { b } ^ { \ell } , \hat { W } ^ { \ell } \}$ . Since every neuron $a _ { m } \sigma ( w _ { m } ^ { \top } x + b _ { m } )$ is continuous on the compact set $[ 0 , 1 ] ^ { d }$ , there is a constant $\lambda > 0$ such that

$$
\lambda + \max _ {k = 1, \dots , M} \max _ {x \in [ 0, 1 ] ^ {d}} \sum_ {m = 1} ^ {k} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}) > 0.
$$

Denote

$$
x = [ x _ {1} \ldots x _ {d} ] ^ {\top} \in \mathbb {R} ^ {d}, y = [ y _ {1} \ldots y _ {d + 2} ] ^ {\top} \in \mathbb {R} ^ {d + 2}.
$$

Then we construct $\{ \hat { W } ^ { \ell } , \hat { b } ^ { \ell } \}$ by

$$
\hat {W} ^ {1} x + \hat {b} ^ {1} = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ w _ {1} ^ {\top} x + b _ {1} \\ \lambda \end{array} \right], \quad \hat {W} ^ {\ell} y + \hat {b} ^ {\ell} = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {d} \\ w _ {\ell} ^ {\top} \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {d} \end{array} \right] + b _ {\ell} \\ y _ {d + 2} + a _ {\ell - 1} y _ {d + 1} \end{array} \right] \text {for} \ell = 2, \ldots , M + 1,
$$

where $w _ { M + 1 }$ and $b _ { M + 1 }$ are defined as zeros. We also construct $\{ \hat { a } , \hat { b } \}$ by

$$
\hat {a} ^ {\top} y + \hat {b} = y _ {d + 2} - \lambda + a _ {0}.
$$

Now let us track the first few layers,

$$
y ^ {(1)} := \sigma (\hat {W} ^ {1} x + \hat {b} ^ {1}) = \sigma (\left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ w _ {1} ^ {\top} x + b _ {1} \\ \lambda \end{array} \right]) = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ \sigma (w _ {1} ^ {\top} x + b _ {1}) \\ \lambda \end{array} \right],
$$

$$
y ^ {(2)} := \sigma (\hat {W} ^ {2} y ^ {(1)} + \hat {b} ^ {2}) = \sigma (\left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ w _ {2} ^ {\top} x + b _ {2} \\ \lambda + a _ {1} \sigma (w _ {1} ^ {\top} x + b _ {1}) \end{array} \right]) = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ \sigma (w _ {2} ^ {\top} x + b _ {2}) \\ \lambda + a _ {1} \sigma (w _ {1} ^ {\top} x + b _ {1}) \end{array} \right],
$$

Inductively, we obtain

$$
y ^ {(k)} := \sigma (\hat {W} ^ {k} y ^ {(k - 1)} + \hat {b} ^ {k}) = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {d} \\ \sigma (w _ {k} ^ {\top} x + b _ {k}) \\ \lambda + \sum_ {m = 1} ^ {k - 1} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}) \end{array} \right]
$$

for $k = 2 , \ldots , M + 1$ . And finally,

$$
\hat {a} ^ {\top} y ^ {(M + 1)} + \hat {b} = \lambda + \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x + b _ {m}) - \lambda + a _ {0} = f (x),
$$

which finishes the proof.

We have mentioned that all ReLU neural networks are piecewise linear functions. And the converse statement is also true. In the following we first present a slightly weaker result where the network is allowed to have both ReLU and linear neurons.

Proposition 2.9 Let $f : \mathbb { R } ^ { d }  \mathbb { R }$ be a continuous piecewise linear function. Then f can be represented exactly by a deep neural network having at most $L = \lfloor \log _ { 2 } ( d + 1 ) \rfloor + 1$ hidden layers, which have ReLU activation functions.

Proof: The proof is based on a result of $[ 1 7 ]$ , which states that for any continuous piecewise linear function $f ,$ there exist $K \in \mathbb { Z } ^ { + }$ and $w _ { k } \in \mathbb { R } ^ { d } , \ b _ { k } \in \mathbb { R }$ for $k = 1 , \ldots , K$ , such that $f$ can be represented as

$$
f (x) = \sum_ {j = 1} ^ {J} s _ {j} \max _ {k \in S _ {j}} \{w _ {k} ^ {\top} x + b _ {k} \},\tag{2.100}
$$

where $J \in \mathbb { Z } ^ { + } ; S _ { j }$ is a subset of $\{ 1 , 2 , \ldots , K \}$ with at most $d + 1$ elements and $s _ { j } = 1 \mathrm { o r } \mathrm { \Pi } ^ { - 1 }$ for $j = 1 , \dots , J ,$

The function ma $\mathfrak { c } _ { k \in S _ { j } } \{ w _ { k } ^ { \top } x + b _ { k } \}$ takes the maximum among at most $d { + 1 }$ previous neurons. By Proposition 2.7, such a max function can be represented by a network having at most $\lfloor \log _ { 2 } ( d { + } 1 ) \rfloor { + } 1$ hidden layers with ReLU activation and an output layer with identity activation. Then by (2.100), $f$ can be represented as

$$
f (x) = \tilde {s} ^ {\top} \left[ \right. A \sigma \left(W ^ {L} \sigma (\dots \sigma \left(W ^ {2} \sigma \left(W ^ {1} (\tilde {W} x + \tilde {b}) + b ^ {1}\right) + b ^ {2}\right) \dots\right) + b ^ {L}\left. \right) + b \left. \right],
$$

where $W ^ { 1 } , \dots , W ^ { L }$ are certain matrices and $b ^ { 1 } , \ldots , b ^ { L }$ are certain vectors with $L \leq \lfloor \log _ { 2 } ( d + 1 ) \rfloor + 1$ ; $\tilde { s } = [ s _ { 1 } \dots s _ { J } ] ^ { \top } \in \mathbb { R } ^ { J \times 1 } ; \tilde { W } = [ w _ { 1 } \dots w _ { K } ] ^ { \top } \in \mathbb { R } ^ { K \times d } ; \tilde { b } = [ b _ { 1 } \dots b _ { K } ] ^ { \top } \in \mathbb { R } ^ { K \times 1 } ; \tilde { \sigma ( t ) }$ is the ReLU activation. Note that $f$ can be rewritten as

$$
f (x) = \hat {s} ^ {\top} \sigma \Bigl (W ^ {L} \sigma (\dots \sigma \bigl (W ^ {2} \sigma \bigl (\hat {W} ^ {1} x + \hat {b} ^ {1} \bigr) + b ^ {2} \bigr) \dots) + b ^ {L} \Bigr) + \hat {b}
$$

with $\hat { s } = \tilde { s } ^ { \top } A , \hat { b } = \tilde { s } ^ { \top } b , \hat { W } ^ { 1 } = W ^ { 1 } \tilde { W } , \hat { b } ^ { 1 } = W ^ { 1 } \tilde { b } + b ^ { 1 }$ , which is exactly a ReLU neural network with L hidden layers. □

## 2.4.3 Kolmogorov-Arnold-Sprecher theorem

Continuous functions of multiple variables can be written as a finite superposition of continuous functions of only one variable. Specifically, Arnold and Kolmogorov proved the following representation theorem in 1957.

Theorem 2.22 (Kolmogorov) Let $d \geq 2$ be an integer. There exist monotone functions of one variable $\psi _ { i j } ( \cdot )$ for $i = 1 , \ldots , d$ and $j = 1 , \ldots , 2 d + 1$ such that for any $f ( x _ { 1 } , \dots , x _ { d } ) \in C ( I _ { d } )$ , it can be written in the form

$$
f (x _ {1}, \dots , x _ {d}) = \sum_ {j = 1} ^ {2 d + 1} \chi_ {j} \left(\sum_ {i = 1} ^ {d} \psi_ {i j} (x _ {i})\right),\tag{2.101}
$$

where $\chi _ { j } ( \cdot )$ are continuous functions of one variable for $j = 1 , \ldots , 2 d + 1$

Note that the expression in (2.101) can be viewed as a neural network having two hidden layers: the first layer has activation $\psi _ { i j }$ and the second layer has activation $\chi _ { j }$ . For example, in the case $d = 2$ , we have

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}) = \chi_ {1} \left(\psi_ {1 1} (x _ {1}) + \psi_ {2 1} (x _ {2})\right) + \chi_ {2} \left(\psi_ {1 2} (x _ {1}) + \psi_ {2 2} (x _ {2})\right) \\ & \qquad + \chi_ {3} \left(\psi_ {1 3} (x _ {1}) + \psi_ {2 3} (x _ {2})\right) + \chi_ {4} \left(\psi_ {1 4} (x _ {1}) + \psi_ {2 4} (x _ {2})\right) + \chi_ {5} \left(\psi_ {1 5} (x _ {1}) + \psi_ {2 5} (x _ {2})\right), \end{array}\tag{2.102}
$$

which can be represented by the graph in Figure 2.5.

Sprecher refined Kolmogorov’s result to the following version, where the outer functions $\chi _ { j }$ are replaced by a single function $\chi$ and the inner functions $\psi _ { i j }$ are of a special type and shifted by a translation:

![](images/8c5b65917e95fb1225c1e3e9e0f4b5dcb447bca11a55535ea216546a888b5cdd.jpg)  
Figure 2.5: Two-hidden layer exact representation of a continuous function f in the case $d = 2$ (the weights of all edges are equal to $1 )$

Theorem 2.23 (Sprecher, 1964) Let $d \geq 2$ be an integer. There exists a monotone increasing function of one variable $\psi ( \cdot )$ , with $\psi ( [ 0 , 1 ] ) = [ 0 , 1 ]$ , dependent on d and having the following property: for any $\delta > 0$ , there is a rational number $\epsilon ,$ with $0 < \epsilon < \delta$ , and a constant $\rho$ such that for any $f ( x _ { 1 } , \dots , x _ { d } ) \in C ( I _ { d } )$ , it can be written in the form

$$
f (x _ {1}, \dots , x _ {d}) = \sum_ {j = 1} ^ {2 d + 1} \chi \left(\sum_ {i = 1} ^ {d} \rho^ {i} \psi (x _ {i} + (j - 1) \epsilon) + j - 1\right),\tag{2.103}
$$

where $\chi ( \cdot )$ is a continuous function of one variable.

The expression in (2.103) is also a neural network having two hidden layers: the first layer has activation $\psi$ and the second layer has activation $\chi .$ The case for $d = 2$ is written as

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}) = \chi (\rho \psi (x _ {1}) + \rho^ {2} \psi (x _ {2})) \\ & \qquad + \chi (\rho \psi (x _ {1} + \epsilon) + \rho^ {2} \psi (x _ {2} + \epsilon) + 1) + \chi (\rho \psi (x _ {1} + 2 \epsilon) + \rho^ {2} \psi (x _ {2} + 2 \epsilon) + 2) \\ & \qquad + \chi (\rho \psi (x _ {1} + 3 \epsilon) + \rho^ {2} \psi (x _ {2} + 3 \epsilon) + 3) + \chi (\rho \psi (x _ {1} + 4 \epsilon) + \rho^ {2} \psi (x _ {2} + 4 \epsilon) + 4), \end{array}
$$

or equivalently,

$$
f (x _ {1}, x _ {2}) = a ^ {\top} \chi \left(W _ {2} \psi (W _ {1} x + b _ {1}) + b _ {2}\right),
$$

where

$$
a = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{array} \right], \quad W _ {1} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \\ 1 & 0 \\ 0 & 1 \\ 1 & 0 \\ 0 & 1 \\ 1 & 0 \\ 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{array} \right], \quad b _ {1} = \left[ \begin{array}{c} 0 \\ 0 \\ \epsilon \\ \epsilon \\ 2 \epsilon \\ 2 \epsilon \\ 3 \epsilon \\ 3 \epsilon \\ 4 \epsilon \\ 4 \epsilon \end{array} \right],
$$

$$
W _ {2} = \left[ \begin{array}{c c c c c c c c c c} \rho & \rho^ {2} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & \rho & \rho^ {2} & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & \rho & \rho^ {2} & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & \rho & \rho^ {2} & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \rho & \rho^ {2} \end{array} \right], \quad b _ {2} = \left[ \begin{array}{c} 0 \\ 1 \\ 2 \\ 3 \\ 4 \end{array} \right], \quad x = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right].
$$

Kolmogorov-Arnold-Sprecher’s theorem does not have much practical applicability due to the fact that the activation functions ψ and χ are not set a priori, and their construction is laborious. But it is worthy to note the following trade-of property: in Kolmogorov’s theorem the width of the hidden layers is given, but there is no control on the expressions of $\psi$ and $\chi .$ However, in previous results the activation function was fixed a priori, while the width or depth was increased as needed until some desired level of approximation accuracy was reached.

## 2.4.4 Exact learning with fixed activation and finite parameters

In Section 2.3.4, to approximate a continuous function more accurately, it requires wider or deeper neural networks. If we expect zero approximation error, the required width or depth will be infinitely large. And in Section 2.4.3, the exact learning with zero approximation error requires appropriate activation functions instead of infinitely many free parameters. So we have a question: whether there exists a neural network architecture with fixed activation functions, width and depth such that neural networks of this architecture can exactly learn any continuous function.

If we consider the similar question for finite-dimensional linear spaces, the answer is clearly no. Suppose $S _ { d }$ is a d-dimensional linear space of functions with a basis $\{ \phi _ { 1 } , \ldots , \phi _ { d } \}$ , then $S _ { d }$ can never be dense in $C ( I _ { d } ) \ ^ { 2 }$ . Namely, there is some $f \in C ( I _ { d } )$ and some $\epsilon _ { 0 } > 0$ such that $\| \phi - f \| _ { \infty } > \epsilon _ { 0 }$ for all functions $\phi : = c _ { 1 } \phi _ { 1 } + \cdot \cdot \cdot + c _ { d } \phi _ { d }$ with coeficients $c _ { 1 } , \ldots , c _ { d }$

However, some special neural networks can learn continuous functions exactly by fixed activation and finite parameters. The latest work [18] gives a type of architecture of such neural networks. Let

$$
\sigma_ {1} (t) = \left| t - 2 \left\lfloor \frac {t + 1}{2} \right\rfloor \right|, \quad \forall t \in \mathbb {R},
$$

where ⌊·⌋ is the floor function. Note that $\sigma _ { 1 }$ is periodic with period $2 ,$ and it can be also written as

$$
\sigma_ {1} (t) = \left\{ \begin{array}{l l} | t |, & t \in [ - 1, 1 ], \\ \sigma_ {1} (t \pm 2), & t \in (- \infty , \infty). \end{array} \right.
$$

![](images/62b0d32f8ca6d7813a7f4f445c380ce8835c313e310b8405cc4da382ff7896b3.jpg)  
Figure 2.6: The graph of σ on [−10, 10].

And let $\sigma _ { 2 }$ be the softsign activation function, i.e.

$$
\sigma_ {2} (t) = \frac {t}{| t | + 1}, \quad t \in \mathbb {R}.
$$

Then the needed activation function σ is defined as

$$
\sigma (t) = \left\{ \begin{array}{l l} \sigma_ {1} (t), & t \geq 0, \\ \sigma_ {2} (t), & t <   0, \end{array} \right.\tag{2.104}
$$

whose graph is shown in Figure 2.6.

Let $\mathcal { N } _ { M , L }$ be the set of all neural networks having width M, depth $L + 1$ and activation function $\sigma$ for hidden layers; namely,

$$
\begin{array}{r l} & {\mathcal {N} _ {M, L} = \Big \{\phi : \mathbb {R} ^ {d} \to \mathbb {R}, f (x) = a ^ {\top} \sigma \Big (W ^ {L} \sigma \big (\ldots \sigma (W ^ {1} x + b ^ {1}) \ldots \big) + b ^ {L} \Big) + b;} \\ & {\qquad a \in \mathbb {R} ^ {M \times 1}, b \in \mathbb {R}, W ^ {1} \in \mathbb {R} ^ {M \times d}, b ^ {1} \in \mathbb {R} ^ {M \times 1},} \\ & {\qquad W ^ {\ell} \in \mathbb {R} ^ {M \times M}, b ^ {\ell} \in \mathbb {R} ^ {M \times 1} \mathrm{for} \ell = 2, \ldots , L \Big \}.} \end{array}\tag{2.105}
$$

Then the following result holds.

Theorem 2.24 (Zhang, Shen & Yang, 2022) Let $M = 3 6 d ( 2 d + 1 )$ and $L = 1 1$ be fixed integers. Then the set $\mathcal { N } _ { M , L }$ given by (2.105) with activation function σ given by (2.104) is dense in $C ( I _ { d } )$ and $L ^ { p } ( I _ { d } )$ with $1 \leq p < \infty { : }$

(i) for any $f \in C ( I _ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} _ {M, L}} \| \phi - f \| _ {\infty} = \inf _ {f \in \mathcal {N} _ {M, L}} \max _ {x \in I _ {d}} | \phi (x) - f (x) | = 0;
$$

(ii) for any $g \in L ^ { p } ( I _ { d } )$ , it holds that

$$
\inf _ {\phi \in \mathcal {N} _ {M, L}} \| \phi - f \| _ {p} = \inf _ {f \in \mathcal {N} _ {M, L}} \left(\int_ {I _ {d}} | \phi (x) - f (x) | ^ {p} \mathrm{d} x\right) ^ {1 / p} = 0.
$$

Theorem 2.24 means that for any target function f and any $\epsilon > 0 .$ , there always exists a neural network $\phi$ with width $3 6 d ( 2 d + 1 )$ , depth 11 and activation function σ defined in (2.104) such that $\| \phi - f \| < \epsilon$ . The number of free parameters is

$$
(d \times M + M) + (M \times M + M) \times (L - 1) + M \times 1 + 1 \sim d ^ {4},
$$

with the conditions $M = 3 6 d ( 2 d + 1 )$ and $L = 1 1$ . However, in the proof given in [18], it is enough to adjust $5 4 3 7 ( d + 1 ) ( 2 d + 1 ) = O ( d ^ { 2 } ) \ll d ^ { 4 }$ parameters and set all the others to 0.

One may ask whether the given error $\epsilon > 0$ mentioned above can be reduced to 0. This is not true in general, but it is true for a class of functions widely used in image classification. Given any pairwise disjoint compact subsets $K _ { 1 } , K _ { 2 } , \ldots , K _ { J } \subset \mathbb { R } ^ { d }$ , define the space of rational-valued simple functions by

$$
\mathbb {S} (K _ {1}, \dots , K _ {J}) := \left\{\phi : \mathbb {R} ^ {d} \to \mathbb {R}, \phi (x) = \sum_ {j = 1} ^ {J} r _ {j} \cdot 1 _ {K _ {j}}, r _ {j} \in \mathbb {Q} \text {for} j = 1, \dots , J \right\},\tag{2.106}
$$

where $1 _ { K _ { j } }$ is the characteristic function of $K _ { j }$ for every $j .$ . The following result shows that any function in $\mathbb { S } ( K _ { 1 } , \ldots , K _ { J } )$ can be represented exactly by neural networks in $\mathcal { N } _ { M , L }$ for fixed M and $L .$

Corollary 2.1 Let $K _ { 1 } , K _ { 2 } , \ldots , K _ { J } \subset \mathbb { R } ^ { d }$ be pairwise disjoint compact subsets. Let $M = 3 6 d ( 2 d +$ 1) and $L = 1 2$ be fixed integers. Then any function in $\mathbb { S } ( K _ { 1 } , \ldots , K _ { J } )$ given by (2.106) can be represented exactly by some network in $\mathcal { N } _ { M , L }$ given by (2.105) with activation function σ given $b y$ (2.104) on the domain $\textstyle \bigcup _ { j = 1 } ^ { J } K _ { j }$ . That is, for any $f \in \mathbb { S } ( K _ { 1 } , \ldots , K _ { J } )$ , there exists some $\phi \in \mathcal { N } _ { M , L }$ such that

$$
f (x) = \phi (x), \quad \forall x \in \bigcup_ {j = 1} ^ {J} K _ {j}.
$$

Same as the preceding remark, the exact representation only needs to adjust $5 5 0 9 ( d { + } 1 ) ( 2 d { + } 1 ) =$ $O ( d ^ { 2 } ) \ll d ^ { 4 }$ parameters and set all the others to 0.

Although the neural networks with activation σ given by (2.104) can approximate continuous functions to any desired accuracy without enlarging its width and depth, the weights $W ^ { \ell }$ might be extremely large in high-accuracy approximation. So such an architecture is usually impractical in real applications.

## 2.5 Exercises

Exercise 1

Let $[ a , b ] \subset \mathbb { R }$ . Prove that for any $f \in C ( [ a , b ] )$ and any $\epsilon > 0$ , there exists some $n \in \mathbb { Z } ^ { + }$ and $\alpha _ { 1 } , \ldots , \alpha _ { n } \in \mathbb { R }$ and nonnegative integers $m _ { 1 } , \ldots , m _ { n }$ such that

$$
\left| f (x) - \sum_ {i = 1} ^ {n} \alpha_ {i} e ^ {m _ {i} x} \right| <   \epsilon , \quad \forall x \in [ a, b ].
$$

Exercise 2

Let

$$
\sigma (x) = \left\{ \begin{array}{l} 1 - x ^ {2}, \quad x \in [ - 1, 1 ], \\ 0, \quad \text { otherwise }. \end{array} \right.
$$

Define

$$
\mathcal {N} = \left\{\phi : \mathbb {R} \to \mathbb {R}, \phi (x) = \sum_ {n = 1} ^ {N} a _ {n} \sigma (x + b _ {n}): a _ {n}, b _ {n} \in \mathbb {R}, N \in \mathbb {Z} ^ {+} \right\}.
$$

Is $\mathcal { N }$ dense in $L ^ { 1 } ( \mathbb { R } ) ?$ Is $\mathcal { N }$ dense in $L ^ { 2 } ( \mathbb { R } ) ?$

## Exercise 3

Let $[ a , b ] \subset \mathbb { R }$ . Prove: the following set

$$
\mathcal {N} = \left\{\phi : [ a, b ] \to \mathbb {R}, \phi (x) = a _ {0} + \alpha \sum_ {n = 1} ^ {N} \gamma_ {n} H (x + b _ {n}): a _ {0}, \alpha , b _ {n} \in \mathbb {R}, \gamma_ {n} \in \{1, - 1 \}, N \in \mathbb {Z} ^ {+} \right\},
$$

is dense in $C ( [ a , b ] )$ .

## Exercise 4

Let $f : [ 0 , 1 ] \to \mathbb { R }$ be a Lipschitz continuous function; namely, f is continuous and

$$
| f (x) - f (y) | \leq c _ {L} | x - y |, \quad \forall x, y \in [ 0, 1 ],
$$

where $c _ { L } > 0$ is a constant. Prove: for any integer $N > 0$ , there exists a two-layer neural network

$$
\phi (x) = \sum_ {n = 1} ^ {N} a _ {n} \sigma (w _ {n} x + b _ {n}) + b,
$$

with $\sigma ( x ) = \operatorname* { m a x } ( 0 , x )$ and $a _ { n } , w _ { n } , b _ { n } , b \in \mathbb { R }$ such that

$$
\sup _ {x \in [ 0, 1 ]} | \phi (x) - f (x) | \leq \frac {c _ {L}}{N}.
$$

Exercise 5

Let N = nϕ : [0, 1] → R, ϕ(x) = a0x + P<sup>N</sup><sub>n=1</sub> an sin(wnx + bn), a0, an, wn, bn ∈ R, N ∈ Z<sup>+</sup>o.

(1) Prove $\mathcal { N }$ is dense in $C ( [ 0 , 1 ] )$ with the norm $\| f \| _ { \infty } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) | .$

(2) Prove $\mathcal { N }$ is dense in $C ^ { 1 } ( [ 0 , 1 ] )$ with the norm $\begin{array} { r } { \| f \| _ { \infty , 1 } : = \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ( x ) | + \operatorname* { s u p } _ { x \in [ 0 , 1 ] } | f ^ { \prime } ( x ) | } \end{array}$ . Here $C ^ { 1 } ( [ 0 , 1 ] )$ is the space of all functions on [0, 1] that have continuous derivatives.

## Exercise 6

Prove: the following set

$$
\mathcal {N} = \left\{\phi : I _ {2} \to \mathbb {R}, \phi (x, y) = \sum_ {n = 1} ^ {N} a _ {n} \mathrm{ReLU} (x + b _ {n}) \mathrm{ReLU} (y + c _ {n}): a _ {n}, b _ {n}, c _ {n} \in \mathbb {R}, N \in \mathbb {Z} ^ {+} \right\},
$$

is dense in $C ( I _ { 2 } )$

## Exercise 7

Let $x _ { 0 }$ and $x _ { 1 }$ be two distinct nonzero vectors in a normed linear space $\mathcal { X } .$ Suppose $x _ { 0 }$ and $x _ { 1 }$ are not parallel, i.e., there is no $k \in \mathbb { R }$ such that $x _ { 0 } = k x _ { 1 }$

(1) Show that there is a bounded linear functional ℓ on X such that $\ell ( x _ { 0 } ) = 0 { \mathrm { ~ a n d ~ } } \ell ( x _ { 1 } ) = 1$

(2) Define $\begin{array} { r } { \delta _ { 1 } = \operatorname* { i n f } _ { k \in \mathbb { R } } \| x _ { 0 } - k x _ { 1 } \| , \delta _ { 2 } = \operatorname* { i n f } _ { k \in \mathbb { R } } \| x _ { 1 } - k x _ { 0 } \| } \end{array}$ . Show that there is a bounded linear functional ℓ on X such that $\begin{array} { r } { \ell ( x _ { 0 } ) = \ell ( x _ { 1 } ) = \frac 1 2 } \end{array}$ and $\begin{array} { r } { \| \ell \| _ { \mathcal { X } ^ { * } } \leq \frac { \delta _ { 0 } + \delta _ { 1 } } { 2 \delta _ { 0 } \delta _ { 1 } } } \end{array}$

Exercise 8

(1) An activation function σ is called weak discriminatory for measures in $B ( I _ { d } )$ if

$$
\int_ {I _ {d}} \sigma (f (x)) \mathrm{d} \mu (x) = 0, \forall f \in C (I _ {d}) \text {   for   some   } \mu \in \mathcal {B} (I _ {d}) \Longrightarrow \mu = 0.
$$

Show that if σ is discriminatory, i.e.,

$$
\int_ {I _ {d}} \sigma (w ^ {\top} x + \theta) \mathrm{d} \mu (x) = 0, \forall w \in \mathbb {R} ^ {d}, \forall \theta \in \mathbb {R} \text {   for   some   } \mu \in \mathcal {B} (I _ {d}) \quad \Longrightarrow \mu = 0,
$$

then it is weak discriminatory.

(2) For $d = 1$ , find an activation function $\sigma ( \cdot )$ that is not discriminatory, i.e., there exists some $\mu \in B ( [ 0 , 1 ] )$ such that

$$
\int_ {0} ^ {1} \sigma (w x + \theta) \mathrm{d} \mu (x) = 0, \forall w, \theta \in \mathbb {R},
$$

but $\mu \neq 0$

## Exercise 9

Let $\Omega \subset \mathbb { R } ^ { d }$ be a bounded set and $\| \cdot \| _ { B ( \Omega ) }$ be the spectral Barron norm defined on Ω. Let $f , f _ { i } : \Omega $ R be functions. Prove the following properties: (a) Translation: If $\| f ( x ) \| _ { B ( \Omega ) } \leq C$ , then $\| f ( x + b ) \| _ { B ( \Omega _ { b } ) } \leq C$ for all $b \in \mathbb { R } ^ { d }$ , where $\Omega _ { b } : = \{ x \in \mathbb { R } ^ { d }$ $x + b \in \Omega \}$ }; (b) Scaling: $\mathrm { I f ~ } \| f ( x ) \| _ { B ( \Omega ) } \leq C$ , then $\| f ( \lambda x ) \| _ { B ( \Omega _ { \lambda } ) } \leq | \lambda | C$ for all nonzero $\lambda \in \mathbb { R }$ , where $\Omega _ { \lambda } : = \{ x \in$ $\mathbb { R } ^ { d } : \lambda x \in \Omega \}$ ; (c) Linear Combination: $\mathrm { I f } \parallel f _ { i } ( x ) \parallel _ { B ( \Omega ) } \leq C _ { i }$ , then $\begin{array} { r } { \lVert \sum _ { i = 1 } ^ { N } \alpha _ { i } f _ { i } ( x ) \rVert _ { \boldsymbol { B } ( \Omega ) } < \sum _ { i = 1 } ^ { N } | \alpha _ { i } | C _ { i } } \end{array}$ for any $\alpha _ { 1 } , \ldots , \alpha _ { N } \in \mathbb { R } ;$ $( \mathrm { d } ) \mathrm { ~ I f ~ } f ( x ) = e ^ { - \| x \| _ { 2 } ^ { 2 } / 2 }$ , then $\| f ( x ) \| _ { B ( \Omega ) } \leq \sqrt { d } ( 2 \pi ) ^ { d }$ . (Hint: use the fact that $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \| \omega \| _ { 2 } ^ { 2 } e ^ { - \| \omega \| _ { 2 } ^ { 2 } / 2 } \mathrm { d } \omega = } \end{array}$ $d ( 2 \pi ) ^ { d / 2 } . )$

## Exercise 10

Find a two-layer ReLU network from $\mathbb { R } ^ { 2 }$ to R with width no more than 3, such that it exactly fits the dataset $\{ ( ( 0 , 1 ) , 0 ) , ( ( 0 , - 1 ) , 1 ) , ( ( 0 , 0 ) , 2 ) , ( ( 1 , 0 ) , 4 ) , ( ( - 1 , 0 ) , 5 ) \}$

Exercise 11

(a) Find a fully-connected feedforward neural network $\phi _ { 1 } ( x )$ such that

$$
\bullet \phi_ {1} (x) = x ^ {4} + 4 x ^ {3} + 1 0 x ^ {2} + 1 2 x + 1 2, \forall x \in \mathbb {R};
$$

$\phi _ { 1 }$ has exactly two hidden layers, each of which has activation $\sigma ( t ) = t ^ { 2 }$

(b) Find a fully-connected feedforward neural network $\phi _ { 2 } ( x )$ such that

$$
\bullet \phi_ {2} (x) = 8 \cos^ {4} (x) + 2 \sin^ {2} (x), \forall x \in \mathbb {R};
$$

$\phi _ { 2 }$ has exactly one hidden layer, which has activation $\sigma ( t ) = \cos ( t )$

Declare how wide your neural networks are.

## Chapter 3

# Optimization in Machine Learning

Almost all types of machine learning involve the process of optimization (usually it is minimization). That is, we are supposed to find a minimizer of a certain objective function. This is also known under the equivalent names of loss function or cost function. In deep learning, the variables of optimization are the free parameters of neural networks. Wide networks will lead to a large number of variables, and deep networks will cause the objective function very non-convex. Both cases mak solving the optimization a challenging task.

## 3.1 Loss Functions

## 3.1.1 $L ^ { \infty }$ and $L ^ { 2 } .$ -loss functions

Let $f ( x ) : [ 0 , 1 ] \to \mathbb { R }$ be an unknown function to be learned. And let $\phi ( x ; \theta ) : [ 0 , 1 ] \to \mathbb { R }$ be the approximator with θ being the set of free parameters. Then the loss function in machine learning characterizes the distance between $g$ and $\phi$ in some sense. For example, the $L ^ { \infty }$ -loss function (or supremum loss function) is defined as

$$
\mathcal {L} (\theta) = \sup _ {x \in [ 0, 1 ]} | \phi (x; \theta) - f (x) |.\tag{3.1}
$$

If a dataset $\{ ( x _ { m } , y _ { m } ) \} _ { m = 1 } ^ { M }$ is available, where $x _ { m } \in [ 0 , 1 ]$ and $y _ { m } = f ( x _ { m } )$ for each m. We have the following empirical $L ^ { \infty } .$ -loss function

$$
\mathcal {L} (\theta) = \max _ {1 \leq m \leq M} | \phi (x _ {m}; \theta) - y _ {m} |,\tag{3.2}
$$

which is computable since everything in the loss function is known.

Despite that the $L ^ { \infty }$ -loss is natural and intuitive to measure the distance between functions, it has a notorious drawback that the max function is not diferentiable everywhere. This limits the use of gradient-based algorithms. A more common choice is the $L ^ { 2 } \mathrm { _ - }$ loss function, i.e.

$$
\mathcal {L} (\theta) = \int_ {0} ^ {1} | \phi (x; \theta) - f (x) | ^ {2} \mathrm{d} x,\tag{3.3}
$$

assuming that $f$ is square integrable. Similarly, the empirical $L ^ { 2 } .$ -loss function associated with the dataset is given by

$$
\mathcal {L} (\theta) = \frac {1}{M} \sum_ {m = 1} ^ {M} (\phi (x _ {m}; \theta) - y _ {m}) ^ {2}.\tag{3.4}
$$

Since the square function is diferentiable everywhere, the empirical $L ^ { 2 } .$ -loss is a smooth function of $\theta$ if $\phi$ is smooth with θ. Then gradient-based algorithms are allowed. Specifically, the gradient $\nabla _ { \boldsymbol { \theta } } \mathcal { L }$ of (3.4) is

$$
\nabla_ {\theta} \mathcal {L} = \frac {2}{M} \sum_ {m = 1} ^ {M} (\phi (x _ {m}; \theta) - y _ {m}) \nabla_ {\theta} \phi (x _ {m}; \theta).\tag{3.5}
$$

## 3.1.2 Mean square error

Suppose $x \in \mathbb { R }$ is a random variable with some probability distribution $\mathcal { D } .$ . Then $y _ { \boldsymbol { \theta } } = \phi ( x ; \boldsymbol { \theta } )$ and $y = f ( x )$ are also random variables. We define the expectation of their squared diference

$$
\mathcal {L} (\theta) = \mathbb {E} _ {x \sim \mathcal {D}} \left[ (y _ {\theta} - y) ^ {2} \right] = \mathbb {E} _ {x \sim \mathcal {D}} \left[ (\phi (x; \theta) - f (x)) ^ {2} \right]\tag{3.6}
$$

as the mean square error, which is also a type of loss functions. In particular, if $x$ is an absolutely continuous random variable and $\mathcal { D }$ is described by a probability density function $\rho ,$ the mean square error (3.6) can be formulated as

$$
\mathcal {L} (\theta) = \int_ {\mathbb {R}} | \phi (x; \theta) - f (x) | ^ {2} \rho (x) \mathrm{d} x,\tag{3.7}
$$

which is a $L ^ { 2 } \mathrm { _ - }$ loss function weighted by $\rho .$

Note that in this case, a dataset $\{ ( x _ { m } , y _ { m } ) \} _ { m = 1 } ^ { M }$ is actually a set of M measurements of random variables $( x , y )$ , and the empirical mean square error can be evaluated as (2.5).

## 3.1.3 Cross-entropy

Cross-entropy is another type of loss functions, and it measures the distance between two probability distributions rather than two general functions. $\mathrm { S o }$ it is often used in classification problems. Here we first consider two absolutely continuous distributions $\mathcal { P }$ and $\mathcal { Q }$ on $\mathbb { R } .$ , whose probability density functions are $p ( y )$ and $q ( y )$ , respectively. Then the cross-entropy of $q$ relative to $p$ is defined as

$$
S (p, q) = \mathbb {E} _ {y \sim \mathcal {P}} [ - \ln q (y) ] = - \int_ {\mathbb {R}} p (y) \ln q (y) \mathrm{d} y.\tag{3.8}
$$

For a sole distribution $\mathcal { P } _ { \cdot }$ , we can define its Shannon entropy by the cross-entropy of $p$ relative to $p$ itself, i.e.

$$
H (p) = \mathbb {E} _ {y \sim \mathcal {P}} [ - \ln p (y) ] = - \int_ {\mathbb {R}} p (y) \ln p (y) \mathrm{d} y.\tag{3.9}
$$

The following result show that $S ( p , q )$ is always bounded below by $H ( p )$

Proposition 3.1 For any two probability density functions p and $q ,$ it holds that $S ( p , q ) \geq H ( p )$ And $S ( p , q ) = H ( p )$ if and only if $p = q$

Proof: Note that ln $u \leq u - 1$ for $u > 0$ and equality holds if and only if $u = 1$ , then

$$
\begin{array}{r l} & S (p, q) - H (p) = - \int_ {\mathbb {R}} p (y) \ln q (y) \mathrm{d} y + \int_ {\mathbb {R}} p (y) \ln p (y) \mathrm{d} y \\ & \qquad = - \int_ {\mathbb {R}} p (y) \ln \frac {q (y)}{p (y)} \mathrm{d} y \geq \int_ {\mathbb {R}} p (y) \left(1 - \frac {q (y)}{p (y)}\right) \mathrm{d} y \\ & \qquad = \int_ {\mathbb {R}} p (y) \mathrm{d} y - \int_ {\mathbb {R}} q (y) \mathrm{d} x = 1 - 1 = 0. \end{array}
$$

If the distributions $\mathcal { P }$ and $\mathcal { Q }$ are discrete, we can similarly define the cross-entropy and Shannon entropy. In this case, the above $p$ and q are probability mass functions instead of probability density functions, and the integral over R is replaced with a discrete sum. Specifically, let Y be the support of $p$ and $q ,$ then the cross-entropy of $q$ relative to $p$ is given by

$$
S (p, q) = \mathbb {E} _ {y \sim \mathcal {P}} [ - \ln q (y) ] = - \sum_ {y \in \mathcal {Y}} p (y) \ln q (y).\tag{3.10}
$$

And the Shannon entropy of $p$ is given by

$$
H (p) = \mathbb {E} _ {y \sim \mathcal {P}} [ - \ln p (y) ] = - \sum_ {y \in \mathcal {Y}} p (y) \ln p (y).\tag{3.11}
$$

Note that the discrete set Y can be either finite or countably infinite.

In the discrete case, the cross-entropy and Shannon entropy are always finite and positive. While in the continuous case, they can be either finite (positive or negative) or infinite.

The next results implies that the Shannon entropy of a distribution is bounded above by the variance.

Corollary 3.1 Let $p$ be a probability density function of an absolutely continuous random variable y on R. Then

$$
H (p) \leq \frac {1}{2} \ln (2 \pi e \mathrm{Var} (y)).\tag{3.12}
$$

Proof: Let $\mu = \mathbb { E } [ y ]$ and $\sigma ^ { 2 } = \operatorname { V a r } ( y )$ , and consider the probability density function of normal distribution $\begin{array} { r } { q ( y ) = \frac { 1 } { \sqrt { 2 \pi } \sigma } e ^ { - \frac { ( y - \mu ) ^ { 2 } } { 2 \sigma ^ { 2 } } } } \end{array}$ with mean $\mu$ and variance $\sigma .$ . Note that $\begin{array} { r } { \sigma ^ { 2 } = \int _ { \mathbb { R } } p ( y ) ( y - \mu ) ^ { 2 } \mathrm { d } y } \end{array}$ ， then

$$
\begin{array}{r l} & S (p, q) = - \int_ {\mathbb {R}} p (y) \ln q (y) \mathrm{d} y = \frac {1}{2} \ln (2 \pi \sigma^ {2}) + \frac {1}{2 \sigma^ {2}} \int_ {\mathbb {R}} p (y) (y - \mu) ^ {2} \mathrm{d} y \\ & \qquad = \frac {1}{2} \ln (2 \pi \sigma^ {2}) + \frac {1}{2} = \frac {1}{2} \ln (2 \pi e \sigma^ {2}). \end{array}
$$

The proof is completed by using Proposition 3.1. The equality holds if $p$ corresponds to a normal distribution. □

For an random event, we say it is more uncertain if its Shannon entropy is larger. The above corollary shows that for a large Shannon entropy, the variance must be large. This means very uncertain events must have large variances.

The diference between the cross-entropy and the Shannon entropy is the Kullback-Leibler divergence, i.e.

$$
D _ {\mathrm{KL}} (p \| q) = S (p, q) - H (p).\tag{3.13}
$$

In machine learning, we take the above $p$ as the unknown target function. And we take $q$ as the learner function; hence we denote $q$ as $q ( y ; \theta )$ with the set of parameters θ. Then the learning process is minimizing the cross-entropy, i.e.

$$
\min _ {\theta} S (p (y), q (y; \theta)),\tag{3.14}
$$

or equivalently, minimizing the K-L divergence

$$
\min _ {\theta} D _ {\mathrm{KL}} (p (y) \| q (y; \theta)).\tag{3.15}
$$

In practice, taking the K-L divergence as the loss function is more helpful because it has a known minimum value of zero, so that one can estimate the extent of the optimization progress.

![](images/72fb10eb393855d6e0dd4524ea7ee6dc9891f86be0ddf88554f36cd0cd2392db.jpg)  
Figure 3.1: All points in $\mathbb { R } ^ { 2 }$ are classified into $\mathcal { B }$ categories: Solid circles are in Category ${ \mathcal { B } } ;$ Blank circles are in Category 2; Solid squares are in Category 1.

## 3.1.4 Empirical computation in classification

The empirical computation of the cross-entropy minimization (3.14) and K-L divergence minimization (3.15) has a diferent story from that of the $L ^ { \infty } , L ^ { 2 }$ and mean square error minimization discussed above. For example, if the distribution is absolutely continuous, a simple dataset $\left\{ \left( y _ { m } , z _ { m } \right) \right\}$ with $z _ { m } = p ( y _ { m } )$ is usually unavailable, because as a probability density function, the value of $p$ at any isolated point does not make any sense. Another question is that even if the distribution is discrete, what $p ( y )$ really means in the learning problem.

This question can be partially answered by considering the classification problem. Suppose we aim to classify all points in $\mathbb { R } ^ { d }$ into several categories based on some rule. Then for each $\boldsymbol { x } \in \mathbb { R } ^ { d }$ there is a discrete distribution relative to x characterizing the probability that x is classified into each category. For example, given classification mapping $\zeta$ on $\mathbb { R } ^ { 2 }$ that

$$
\zeta (x) = \frac {1}{2} \left(\mathrm{sign} (x _ {1}) + \mathrm{sign} (x _ {2})\right) + 2,
$$

where the sign function maps negative numbers to −1 and others to 1, then all points in $\mathbb { R } ^ { 2 }$ can be classified into one of categories 1,2 and 3 (Figure 3.1). For any $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } )$ with $x _ { 1 } , x _ { 2 } \ge 0 _ { : }$ , its probability mass function

$$
p (y) = \left\{ \begin{array}{l l} 0, & \text {if y = 1 or 2 ,} \\ 1, & \text {if y = 3 .} \end{array} \right.
$$

That ${ \mathrm { i s } } ,$ such $x$ is classified into Category 3 with one hundred percent. We have seen that every point in $\mathbb { R } ^ { d }$ has its own probability mass function, so we rewrite the probability mass function as $p ( y | x )$ to emphasize that it is associated with $x ,$ which means the probability that x is classified into Category y. The concept $p ( y | x )$ is also named as the conditional probability given x in probability theory.

While in the classification problem, $p ( y | x )$ can be regarded as a classifier; namely, x is classified into Category $\{ y : p ( y | x ) = 1 \}$ . In practice, $p ( y | x )$ with variables x and $y$ is an unknown target function to be learned. So we choose an approximator $f ( x , y ; \theta ) : \mathbb { R } ^ { d } \times \{ 1 , 2 , \dots , s \}  [ 0 , 1 ]$ and expect $f ( x , y ; \theta ) \approx p ( y | x )$ , where s is the number of categories. $f ( x , y ; \theta )$ should also satisfy the condition that $\begin{array} { r } { \sum _ { y = 1 } ^ { s } f ( x , y ; \theta ) = 1 } \end{array}$ for all $\boldsymbol { x } \in \mathbb { R } ^ { d }$

Now suppose a dataset $\{ ( x _ { m } , y _ { m } ) \} _ { m = 1 } ^ { M }$ is in hand, where $x _ { m } \in \mathbb { R } ^ { d }$ is a feature vector and $y _ { m }$ is the category number of $x _ { m }$ for each m.

Empirically, the cross-entropy of every $x _ { m }$ should be part of the entire loss function. Consequently, the empirical cross-entropy loss functions is given by

$$
\begin{array}{l} \mathcal {L} (\theta) = \sum_ {m = 1} ^ {M} S (p (y | x _ {m}), f (x _ {m}, y; \theta)) = \sum_ {m = 1} ^ {M} \left[ - \sum_ {y = 1} ^ {s} p (y | x _ {m}) \ln f (x _ {m}, y; \theta) \right] \\ = - \sum_ {m = 1} ^ {M} \ln f (x _ {m}, y _ {m}; \theta), \end{array}
$$

where the fact that $p ( y | x _ { m } ) = 1 { \mathrm { ~ i f ~ } } y = y _ { m }$ and $p ( y | x _ { m } ) = 0 { \mathrm { ~ i f ~ } } y \neq y _ { m }$ is used. Similarly, the empirical K-L divergence loss functions given by

$$
\begin{array}{l} \mathcal {L} (\theta) = \sum_ {m = 1} ^ {M} D _ {\mathrm{KL}} (p (y | x _ {m}) \| f (x _ {m}, y; \theta)) = \sum_ {m = 1} ^ {M} [ S (p (y | x _ {m}), f (x _ {m}, y; \theta)) - H (p (y | x _ {m})) ] \\ \qquad = - \sum_ {m = 1} ^ {M} \ln f (x _ {m}, y _ {m}; \theta), \end{array}
$$

where the fact that $H ( p ( y | x _ { m } ) ) = 0$ for all $m \in \{ 1 , 2 , \ldots , M \}$ is used. Note that in this classification problem, the empirical loss functions of cross-entropy and K-L divergence are exactly the same.

## 3.1.5 Other loss functions

Let $g ( x )$ be the target function and $f ( x , \theta )$ be the approximator. Some other types of loss functions are listed as follows.

L<sup>p</sup>-loss function The L<sup>p</sup>-loss function is defined as

$$
\mathcal {L} (\theta) = \int_ {D} | f (x; \theta) - g (x) | ^ {p} \mathrm{d} x,
$$

where $D$ is the domain of the functions. Except $p = 2 .$ , a common choice is $p = 1$

Hellinger distance If $g$ and f are both probability density functions, the Hellinger distance $H ( f , g )$ is defined as

$$
H ^ {2} (f, g) = \frac {1}{2} \int_ {\mathbb {R}} \left[ \sqrt {f (x ; \theta)} - \sqrt {g (x)} \right] ^ {2} \mathrm{d} x.
$$

Jefrey distance If $g$ and $f$ are both probability density functions, the Jefrey distance $J ( f , g )$ is defined as

$$
J (f, g) = \frac {1}{2} \int_ {\mathbb {R}} \left(f (x; \theta) - g (x)\right) \left(\ln f (x; \theta) - \ln g (x)\right) \mathrm{d} x.
$$

R´enyi entropy For any $\alpha > 1$ and $\alpha \neq 1$ , define the R´enyi entropy for any probability density function $p$ by

$$
H _ {\alpha} (p) = \frac {1}{1 - \alpha} \ln \int_ {\mathbb {R}} p (x) ^ {\alpha} \mathrm{d} x,
$$

which is a generalization of the Shannon entropy. It can be proved that $\begin{array} { r } { H ( p ) = \operatorname* { l i m } _ { \alpha \to 1 } H _ { \alpha } ( p ) } \end{array}$

## 3.2 Algorithms of Optimization

Let $f : D  \mathbb { R }$ be a function with domain $D \subset \mathbb { R } ^ { d }$ . We say $x ^ { * } \in D$ is a global minimum point (or global minimizer) of f if $f ( x ^ { * } ) \leq f ( x )$ for all $x \in D$ , and the value $f ( x ^ { * } )$ is called the global minimum<sup>1</sup> of $f .$ Clearly, the global minimum of a function is unique, while the global minimum points may be multiple.

Also, we can define the minimum concepts locally. A point $\hat { x } \in D$ is called a local minimum point (or local minimizer) of $f$ if there is a neighborhood $D _ { \hat { x } }$ of ˆx in $\mathbb { R } ^ { d }$ such that $f ( { \hat { x } } ) \leq f ( x )$ for all $x \in D _ { \hat { x } } \cap D$ . And the corresponding $f ( \hat { x } )$ is called the local minimum of f. A function may have multiple local minima and local minimum points.

Finding global minimizers of given functions has been a fundamental research work for a long period, just as the study of finding solutions of linear algebraic equations. An easy case is when the function $f$ is convex; namely, for all $0 \leq t \leq 1$ and all $x _ { 1 } , x _ { 2 } \in D$ , it holds that

$$
f (t x _ {1} + (1 - t) x _ {2}) \leq t f (x _ {1}) + (1 - t) f (x _ {2}).\tag{3.16}
$$

Many classical optimization algorithms is ensured to converge to the global minimum point of convex functions, and the convergence is quite fast. However, for the optimization in deep learning, the loss functions are usually non-convex. The convergence to global minimum points is hardly to achieved, and what we obtain are often local minimum points. However, not all local minimum points are unacceptable results. We say a local minimum point ˆx of $f$ is “good” if $| f ( \hat { x } ) - f ( x ^ { * } ) | < \epsilon$ where ϵ is some acceptable threshold. In practical deep learning, the goal of optimization is never finding the global minimum of the loss function. Instead, it is always finding “good” local minimum of the loss function.

## 3.2.1 Gradient descent algorithms

## The steepest descent

General functions do not have any closed-forms of its minimum points. So finding the minimum points has to be implemented by iterations. Now let us minimize a function $f$ by iterations. We denote the intermediate solution at the k-th iteration step as $x ^ { ( k ) }$ , then a straightforward idea at the (k + 1)-th iteration is updating x toward a specific direction $\delta _ { k } \in \mathbb { R } ^ { d }$ , that is

$$
x ^ {(k + 1)} = x ^ {(k)} + \eta \delta_ {k},\tag{3.17}
$$

where $\eta > 0$ is the step size toward the direction $\delta _ { k }$ . In machine learning, η has a more popular name: the learning rate.

We suppose η in the k-th iteration has been chosen and fixed, then a good choice of the direction $\delta _ { k }$ is the vector toward which the function f decreases fast; namely, the steepest descent direction. We further assume that $f ( x )$ is diferentiable at $x = x ^ { ( k ) }$ . Note that any direction in $\mathbb { R } ^ { d }$ can be characterized by a unit vector $\mathbf { n } = ( n _ { 1 } , \ldots , n _ { d } ) \in \mathbb { R } ^ { d }$ Then the directional derivative of $f$ at $x = x ^ { ( k ) }$ toward n is given by n · $\nabla f ( x ^ { ( k ) } )$ . By the Cauchy-Schwarz inequality, the directional derivative takes its minimum when $\mathbf { n } = - \nabla f ( x ^ { ( k ) } ) / \| \nabla f ( x ^ { ( k ) } ) \| _ { 2 }$ , where $\| \cdot \| _ { 2 }$ means the Euclidean norm. This implies the steepest descent direction of $f$ is its negative gradient. Taking $\delta _ { k }$ in (3.17) as the negative gradient leads to the following gradient descent method (or the method of steepest descent),

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \nabla f (x ^ {(k)}).\tag{3.18}
$$

![](images/2fb0192ac8ae70c08802dbd3cf623b12c35d1fe8c535a628f9da009b36cc6f4d.jpg)  
(a) Case 0 < η < 1/8.

![](images/876500de5277539ee7c18f85e4169d5cac255f4c7b54be1ffd532ffe8b385386.jpg)  
(b) Case 1/8 < η < 1/4.  
Figure 3.2: Gradient descent iterations.

In the case that $\eta$ is fixed for all k, it is derived from (3.18) that $\begin{array} { r } { x ^ { ( k ) } = x ^ { ( 0 ) } - \eta \sum _ { i = 0 } ^ { k - 1 } \nabla f ( x ^ { ( i ) } ) } \end{array}$ So the above sequence $( x ^ { ( k ) } ) _ { k }$ computed by gradient descent is convergent if and only if the series $\textstyle \sum _ { i = 0 } ^ { \infty } \nabla f ( x ^ { ( i ) } )$ is convergent. And if it is true, the sequence $\left( \nabla f ( x ^ { ( k ) } ) \right) _ { k }$ is convergent to the zero vector as $k \to \infty$ . However, lim $_ { 1 _ { k } \to \infty } \nabla f ( x ^ { ( k ) } ) = 0$ does not imply $( x ^ { ( k ) } ) _ { k }$ is convergent.

Diferent choices of the learning rate η will lead to diferent behaviours of the gradient descent algorithm. For example, consider the function $f : [ 0 , 1 ] \times [ - 2 , 2 ] $ R, given by $f ( x ) = x _ { 1 } ^ { 2 } + 4 x _ { 2 } ^ { 2 }$ 2 whose minimum is taken at $x = ( 0 , 0 )$ . The gradient of f is $\nabla f ( x ) = ( 2 x _ { 1 } , 8 x _ { 2 } )$ , and the gradient descent method is implemented by

$$
\begin{array}{r} x _ {1} ^ {(k + 1)} = (1 - 2 \eta) x _ {1} ^ {(k)}, \\ x _ {2} ^ {(k + 1)} = (1 - 8 \eta) x _ {2} ^ {(k)}. \end{array}\tag{3.19}
$$

Given an initial point $x ^ { ( 0 ) }$ , the iteration (3.19) can be solved explicitly by

$$
\begin{array}{r} x _ {1} ^ {(k)} = (1 - 2 \eta) ^ {k} x _ {1} ^ {(0)}, \\ x _ {2} ^ {(k)} = (1 - 8 \eta) ^ {k} x _ {2} ^ {(0)}. \end{array}
$$

Then the following two cases lead to two distinct behaviors of the iteration:

1. If $0 < \eta < 1 / 8 , 1 - 2 \eta \in ( 0 , 1 )$ and $1 - 8 \eta \in ( 0 , 1 )$ . The sequence $( x _ { 1 } ^ { ( k ) } ) _ { k }$ converges to 0 keeping a constant sign (the sign of $x _ { 1 } ^ { ( 0 ) } )$ . And so is the sequence $( x _ { 2 } ^ { ( k ) } ) _ { k }$ . See Figure 3.2 (a).

2. If $1 / 8 < \eta < 1 / 4 , 1 - 2 \eta \in ( 0 , 1 )$ and $1 - 8 \eta \in ( - 1 , 0 )$ . The sequence $( x _ { 1 } ^ { ( k ) } ) _ { k }$ converges to 0 keeping a constant sign (the sign of $x _ { 1 } ^ { ( 0 ) } )$ . But the sequence $( x _ { 2 } ^ { ( k ) } ) _ { k }$ converges to 0 with an alternative sign. See Figure 3.2 (b).

In practice, usually the learning rate η is not fixed during the iteration. So we can replace η with $\eta _ { k }$ to emphasize that it is the learning rate used at the k-th iteration. Many experiences show it is always good to set $\eta _ { k }$ decreasing with k for the convergence of the algorithm. And some advanced research studies the adaptive learning rates for specific problems.

## Line search

We go back to the general iteration scheme (3.17), which can be rewritten as

$$
x ^ {(k + 1)} = x ^ {(k)} + \eta_ {k} \delta_ {k},\tag{3.20}
$$

Here $\delta _ { k }$ is the direction of descent and $\eta _ { k }$ is step size by which the current point $x ^ { ( k ) }$ moves. Sometimes, $\eta _ { k }$ is prescribed for all iterations. While another way is computing $\eta _ { k }$ in every iteration so that the updated $x ^ { ( k + 1 ) }$ is the optimal point on the current direction; namely, the learning rate $\eta _ { k }$ is computed by

$$
\eta_ {k} = \arg \min _ {\eta} f (x ^ {(k)} + \eta \delta_ {k}).\tag{3.21}
$$

Then by the update (3.20), it holds that $f ( x ^ { ( k + 1 ) } ) \leq f ( x ^ { ( k ) } + \eta \delta _ { k } )$ for all $\eta .$ . This procedure is searching the line for the “best” point in every iteration.

Consider the function $g ( \eta ) : = f ( x ^ { ( k ) } + \eta \delta _ { k } )$ , if f is diferentiable,

$$
g ^ {\prime} (\eta) = - \left(\nabla f (x ^ {(k)} + \eta \delta_ {k}), \delta_ {k}\right).
$$

Since $\eta _ { k }$ is chosen to minimize $g ( \eta )$ , we have $g ^ { \prime } ( \eta _ { k } ) = 0$

Unfortunately, the zeros of $g ^ { \prime } ( \eta )$ usually do not have closed forms. So computing $\eta _ { k }$ by (3.21) has to be implemented by iterative methods, and the cost is often expensive. While indeed, the line search strategy gives us an optimal learning rate of every iteration, and hence it can speed up the convergence of the algorithm to some extent.

## Momentum method

Updating x along the negative gradient for all iterations is not always a good idea. A variant of the gradient descent is the momentum method, which introduces a “velocity” vector to perturb the gradient as the new direction of descent. A classical formulation of the momentum method [12] is performed by the following updates

$$
v ^ {(k + 1)} = \mu v ^ {(k)} - \eta \nabla f (x ^ {(k)}),\tag{3.22}
$$

$$
x ^ {(k + 1)} = x ^ {(k)} + v ^ {(k + 1)},\tag{3.23}
$$

given an initial pair $( x ^ { ( 0 ) } , v ^ { ( 0 ) } )$ . Here $\eta > 0$ is the learning rate and $\mu \in ( 0 , 1 ]$ is the momentum coeficient.

In the case that η is fixed for all k, it is derived from (3.22)-(3.23) that

$$
v ^ {(k)} = \mu^ {k} v ^ {(0)} - \eta \sum_ {i = 0} ^ {k - 1} \mu^ {k - i - 1} \nabla f (x ^ {(i)}),\tag{3.24}
$$

$$
x ^ {(k)} = x ^ {(0)} + \frac {\mu (1 - \mu^ {k})}{1 - \mu} v ^ {(0)} - \eta \left(\sum_ {i = 0} ^ {k - 1} \frac {1 - \mu^ {k - i}}{1 - \mu} \nabla f (x ^ {(i)})\right).\tag{3.25}
$$

We need the following result to show the convergence of $( x ^ { ( k ) } ) _ { k }$ and $( v ^ { ( k ) } ) _ { k }$ .

Proposition 3.2 Let $( a _ { n } ) _ { n }$ be a sequence of real numbers convergent to 0 and $\textstyle \sum _ { n \geq 0 } b _ { n }$ be an absolute convergent series of real numbers. Then

$$
\lim _ {n \to \infty} \sum_ {i = 0} ^ {n} a _ {n - i} b _ {i} = 0.
$$

Applying Proposition 3.2 to (3.24)-(3.25) leads to

Proposition 3.3 Assume the series $\begin{array} { r } { \sum _ { k \geq 0 } \| \nabla f ( x ^ { ( k ) } ) \| _ { 2 } } \end{array}$ is convergent. Then $( v ^ { ( k ) } ) _ { k }$ is convergent to the zero vector, and $( x ^ { ( k ) } ) _ { k }$ is convergent.

An improvement of the classical momentum method has been proposed in [11], and it is formulated as

$$
\begin{array}{r l} & v ^ {(k + 1)} = \mu v ^ {(k)} - \eta \nabla f (x ^ {(k)} + \mu v ^ {(k)}), \\ & x ^ {(k + 1)} = x ^ {(k)} + v ^ {(k + 1)}, \end{array}
$$

which is called the Nesterov Accelerated Gradient (NAG). Same as the gradient descent, NAG is a first-order optimization method but has better convergence rate than the gradient descent. Compared with the momentum method, NAG changes velocity v in a more responsive way, fact that makes the method more stable, especially for larger value of $\mu .$

## AdaGrad

Adaptive Gradient (AdaGrad) proposed in [2] is another variant of the gradient descent method. Starting from $k = 0$ , the iteration of AdaGrad is given by

$$
\begin{array}{c} G ^ {(k)} = \sum_ {i = 0} ^ {k} \nabla f (x ^ {(i)}) \nabla f (x ^ {(i)}) ^ {\top}, \\ x ^ {(k + 1)} = x ^ {(k)} - \eta \left(G ^ {(k)}\right) ^ {- 1 / 2} \nabla f (x ^ {(k)}), \end{array}
$$

Recall that $\boldsymbol { x } ^ { ( k ) } \in \mathbb { R } ^ { d }$ . If $k < d ,$ , then $G ^ { ( k ) }$ is merely positive semi-definite and not invertible. In this case, $\left( G ^ { ( k ) } \right) ^ { - 1 / 2 }$ can be chosen as the pseudoinverse of $\left( G ^ { ( k ) } \right) ^ { 1 / 2 }$ . Another way to tackle this problem is using AdaGrad only for $k \geq d .$

If d is very large, $\left( G ^ { ( k ) } \right) ^ { - 1 / 2 }$ is computationally expensive. Then the update for $x ^ { ( k + 1 ) }$ can be done using only the diagonal elements of the matrix; namely,

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \operatorname{diag} (G ^ {(k)}) ^ {- 1 / 2} \nabla f (x ^ {(k)}).
$$

The diagonal elements of $G ^ { ( k ) }$ can be calculated by

$$
\left(G ^ {(k)}\right) _ {j j} = \sum_ {i = 0} ^ {k} \left(\nabla_ {j} f (x ^ {(i)})\right) ^ {2}.
$$

## RMSProp

The Root Mean Square Propagation (RMSProp) is a variant of the gradient descent method with adaptive learning rate. Specifically, the learning rate is divided by a running average of the magnitude of the gradient. The iteration of RMSProp is given by

$$
v ^ {(k + 1)} = \gamma v ^ {(k)} + (1 - \gamma) (\nabla f (x ^ {(k)})) ^ {2},
$$

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \frac {\nabla f (x ^ {(k)})}{\sqrt {| v ^ {(k + 1)} |}},
$$

where $\gamma \in ( 0 , 1 )$ , which controls the exponential decay rate; $\left( \nabla f ( x ^ { ( k + 1 ) } ) \right) ^ { 2 }$ means the elementwise square of the gradient $\begin{array} { r } { \nabla f ( x ^ { ( k + 1 ) } ) ; \frac { \nabla f ( x ^ { ( k ) } ) } { \sqrt { | v ^ { ( k + 1 ) } | } } } \end{array}$ mean the elementwise division of the vector $\nabla f ( x ^ { ( k ) } )$ by the vector $\sqrt { | v ^ { ( k + 1 ) } | }$ . It can be shown that

$$
v ^ {(k)} = \gamma^ {k} v ^ {(0)} + (1 - \gamma) \sum_ {i = 1} ^ {k} \gamma^ {k - i} \left(\nabla f (x ^ {(i - 1)})\right) ^ {2}.
$$

So $v ^ { ( k ) }$ can be regarded as a weighted sum of a fixed vector $\boldsymbol { v } ^ { ( 0 ) }$ (which is usually taken equal to zero) and all the previous squared gradients, giving larger weights to more recent gradients.

## Adam and AdaMax

Adaptive moment estimation (Adam) [8] is a popular variant of the gradient descent method with adaptive learning rates, and it is like a combination of the previous AdaGrad and RMSProp methods. Two vectors $m ^ { ( k ) }$ and $v ^ { ( k ) }$ , called the first and second moment of the gradient, are introduced in the iteration. Fixing an initial vector $x ^ { ( 0 ) } = x _ { 0 }$ and initializing the moments by $m ^ { ( 0 ) } = v ^ { ( 0 ) } = 0$ the updates are given by

$$
\begin{array}{l} m ^ {(k + 1)} = \beta_ {1} m ^ {(k)} + (1 - \beta_ {1}) \nabla f (x ^ {(k)}), \\ v ^ {(k + 1)} = \beta_ {2} v ^ {(k)} + (1 - \beta_ {2}) \left(\nabla f (x ^ {(k)})\right) ^ {2}, \\ x ^ {(k + 1)} = x ^ {(k)} - \eta \frac {m ^ {(k + 1)}}{(1 - \beta_ {1} ^ {k + 1}) \left(\sqrt {| v ^ {(k + 1)} | / (1 - \beta_ {2} ^ {k + 1})} + \epsilon\right)}, \end{array}
$$

where $\epsilon > 0$ a small scalar used to prevent division by zero and $\beta _ { 1 } , \beta _ { 2 } \in [ 0 , 1 )$ are two exponential decay rates for the moment estimates.

In the deep learning $\mathrm { P y }$ thon library PyTorch, the command torch.optim.Adam is the implementation of Adam method. The default hyperparameters are $\eta = 0 . 0 0 1 , \beta _ { 1 } = 0 . 9 , \beta _ { 2 } = 0 . 9 9 9$ and $\epsilon = 1 0 ^ { - 8 }$ (PyTorch version 2.1).

Another method, Adaptive Maximum (AdaMax) [8], is a variant of Adam based on the infinity norm. Introducing a scalar variable $u ^ { ( k ) }$ , the iteration of AdaMax is as follows:

$$
\begin{array}{r l} & m ^ {(k + 1)} = \beta_ {1} m ^ {(k)} + (1 - \beta_ {1}) \nabla f (x ^ {(k)}), \\ & u ^ {(k + 1)} = \max \{\beta_ {2} u ^ {(k)}, | \nabla f (x ^ {(k)}) | \}, \\ & x ^ {(k + 1)} = x ^ {(k)} - \frac {\eta}{(1 - \beta_ {1} ^ {k + 1}) u ^ {(k + 1)}} m ^ {(k + 1)}, \end{array}
$$

with moment initialization $m ^ { ( 0 ) } = 0$ and $u ^ { ( 0 ) } = 0$ , where max $\{ \beta _ { 2 } u ^ { ( k ) } , | \nabla f ( x ^ { ( k ) } ) | \}$ means the elementwise maximum of the two vectors $\beta _ { 2 } u ^ { ( k ) }$ and $| \nabla f ( x ^ { ( k ) } ) |$

## 3.2.2 Stochastic gradient descent

In usual learning problems, the loss function is the average of many terms having the same type. For example, the $L ^ { 2 }$ loss given by (3.4) is the average of M squared terms, each of which involves the data $( x _ { m } , y _ { m } )$ . Generally, suppose the loss function is given by

$$
f (x) = \frac {1}{M} \sum_ {m = 1} ^ {M} f _ {m} (x),\tag{3.26}
$$

![](images/d451800f1d46a1217dbe16bf3d96be8ba28b0402286bf8151113cbd86699e070.jpg)  
Figure 3.3: Choosing disjoint subsets sequentially from the entire dataset with batch size $M ^ { \prime } .$

where each summand function $f _ { m } ( x )$ is associated with the m-th data sample in the dataset.

The gradient descent method and its variants require evaluating $\begin{array} { r } { \nabla f = \frac { 1 } { M } \sum _ { m = 1 } ^ { M } \nabla f _ { m } } \end{array}$ . When the dataset is enormous and no simple formulas exist, evaluating the sums of gradients becomes very expensive, because it requires evaluating all the summand functions’ gradients. To economize on the computational cost at every iteration, stochastic gradient descent (SGD) samples a subset of summand functions at every step. This makes large-scale machine learning problems feasible.

At the k-th iteration of SGD, we only select a small number of summand functions in (3.26) and take their average as the loss function at the current step. Specifically, we obtain $x ^ { ( k + 1 ) }$ as follows:

$$
x ^ {(k + 1)} = x ^ {(k)} - \eta \nabla \tilde {f} _ {k} (x ^ {(k)}),
$$

where

$$
\tilde {f} _ {k} (x) = \frac {1}{| I _ {k} |} \sum_ {m \in I _ {k}} f _ {m} (x),
$$

and the index set $I _ { k }$ is a subset of $\{ 1 , \dots , M \}$ . Note that $I _ { k }$ is chosen to be various for diferent iterations. And by repeated iterations, the selected indices can cover the whole dataset.

In practice, $\left| I _ { k } \right|$ is set to be small so that the above computation can be handled by the used machine. If $| I _ { k } | = 1$ , only a single sample is taken to compute the gradient at the current step. If $1 < | I _ { k } | < M , I _ { k }$ indexes a small batch of data samples, and this method is also called the mini-batch SGD. While if $| I _ { k } | = M$ , the SGD becomes the (standard) gradient descent method, so the gradient descent method is sometimes called batch gradient descent method.

The choice of $I _ { k }$ can be either stochastic or deterministic. In the stochastic case, a straightforward way is selecting $\left| I _ { k } \right|$ numbers from $\{ 1 , \dots , M \}$ with uniform distribution at every iteration. In the deterministic case, it is common to take sequential disjoint subsets of the same size covering $\{ 1 , \dots , M \}$ as $I _ { k }$ . In pseudocode, a canonical type of the mini-batch SGD is presented as

• for $k = 1 , 2 , \dots$

• for $\begin{array} { r } { j = 1 , 2 , \dots , \frac { M } { M ^ { \prime } } } \end{array}$

$$
I = \{(j - 1) M ^ {\prime} + 1, (j - 1) M ^ {\prime} + 2, \dots , j M ^ {\prime} \};
$$

$\begin{array} { r } { x  x - \frac { \eta } { M ^ { \prime } } \sum _ { m \in I } \nabla f _ { m } ( x ) . } \end{array}$

Here, $M ^ { \prime }$ is the size of the index set I which divides M. In machine learning implementation, $M ^ { \prime }$ is called the batch size, and every outer loop associated with k is called an epoch (see Figure 3.3).

Besides the standard gradient descent method, its variants (Momentum method, AdaGrad, RMSProp, etc.) have similar stochastic formulation. Although SGD and its variants with small batch sizes are computationally economic, their convergence behaviors are not as stable as the methods with large batch sizes. It is sometimes observed in numerical experiments that the loss function is hardly decreased by small-batch SGD, but it can be decreased by the batch gradient descent.

## 3.3 Optimization theory in deep learning

In this section, we consider the typical problem: regression with $L ^ { 2 }$ loss function. The goal of regression is the approximate a potential target function $f$ on $\mathbb { R } ^ { d }$ . Let $\{ ( x _ { n } , y _ { n } \} _ { n = 1 } ^ { N }$ be a dataset, where the feature vectors $X : = \{ x _ { n } \} _ { n = 1 } ^ { N }$ are independent samples under some distribution $\mathcal { D }$ over $\mathbb { R } ^ { d }$ and the labels $y _ { n } : = f ( x _ { n } )$ . Then the empirical loss function is given by

$$
\min _ {\phi} \frac {1}{N} \sum_ {n = 1} ^ {N} | \phi (x _ {n}) - y _ {n} | ^ {2},\tag{3.27}
$$

where $\phi$ is the learner/approximator/estimator and the minimum is taken over all possible forms of $\psi .$ . We further assume that the label set $\left\{ y _ { n } \right\}$ has an upper bound $Y > 0 , { \mathrm { i . e . ~ } } \left| y _ { n } \right| \leq Y$ for all $n .$

Generally, for $a , b \geq 0 ,$ , people use the notation $a = O ( b )$ , or equivalently $b = \Omega ( a )$ , if there exists a constant $C > 0$ independent of a and b such that $a \leq C b$ . Similarly, $a = \Theta ( b )$ means that there exist two constants $C _ { 1 } , C _ { 2 } > 0$ such that $C _ { 1 } b \leq a \leq C _ { 2 } b$ . For any positive integer $n ,$ we denote $[ n ] = \{ 1 , 2 , \dots , n \}$ . Besides, we let $\mathcal { U } ( S )$ be the uniform distribution on the bounded (finite or infinite) set $S ,$ and let I<sub>E</sub> be the indicator on whether the event E happens.

## 3.3.1 Optimization of shallow networks

Settings

We first consider the case $\psi$ is a two-layer (shallow) ReLU neural network without bias. Specifically, let

$$
\phi (x; W, a) = \frac {1}{\sqrt {M}} \sum_ {m = 1} ^ {M} a _ {m} \sigma (w _ {m} ^ {\top} x),\tag{3.28}
$$

where $\sigma$ is the ReLU activation; $W = [ w _ { 1 } \ \dots \ w _ { M } ] \in \mathbb { R } ^ { d \times M }$ is the matrix with columns being the trainable weight vectors; $a = [ a _ { 1 } \dots a _ { m } ] \in \mathbb { R } ^ { M }$ is the vector composed of the weights in the output layer.

Let us consider the gradient descent solving the optimization (3.27). First, we initialize the parameters $W$ and a by assigning

$$
\begin{array}{r} a _ {m} \leftarrow a _ {m} ^ {(0)} \sim \mathcal {U} (\{\pm 1 \}), \\ w _ {m} \leftarrow w _ {m} ^ {(0)} \sim \mathcal {N} (0, I). \end{array}\tag{3.29}
$$

For simplicity, we fix $a _ { m }$ once they have been initialized, and only tune the weight vectors $w _ { m }$ during the iteration. Then the learner neural network can be rewritten as

$$
\phi (x; W) = \frac {1}{\sqrt {M}} \sum_ {m = 1} ^ {M} a _ {m} ^ {(0)} (w _ {m} ^ {\top} x) \cdot \mathbb {I} _ {w _ {m} ^ {\top} x \geq 0},\tag{3.30}
$$

Denote

$$
\mathcal {L} (W) = \frac {1}{N} \sum_ {n = 1} ^ {N} | \phi (x _ {n}; W) - y _ {n} | ^ {2},\tag{3.31}
$$

then the minimization (3.27) becomes

$$
\min _ {W} \mathcal {L} (W).\tag{3.32}
$$

We use $W ^ { ( t ) } = [ w _ { 1 } ^ { ( t ) } ~ . . . ~ w _ { M } ^ { ( t ) } ]$ to denote the weight W after t iterations of gradient descent $( W ^ { ( 0 ) }$ means the initialized weight). Then, the gradient descent algorithm is given by

$$
\begin{array}{c} \text { for } t = 1, 2, \ldots \\ W ^ {(t)} = W ^ {(t - 1)} - \eta \nabla_ {W} \mathcal {L} (W ^ {(t - 1)}) \end{array}
$$

where $\eta > 0$ is the learning rate. It is trivial to compute the gradient, i.e.,

$$
\nabla_ {w _ {m}} \mathcal {L} (W) = \frac {2}{N \sqrt {M}} \sum_ {n = 1} ^ {N} (\phi (x _ {n}; W) - y _ {n}) a _ {m} \mathbb {I} _ {w _ {m} ^ {\top} x _ {n} \geq 0} x _ {n}, \forall m \in [ M ].
$$

For simplicity, we assume all feature vectors $\{ x _ { n } \}$ are sampled on the unit sphere, i.e. $\| x _ { n } \| _ { 2 } = 1$ for all $n .$ . The results can be easily generalized for $\{ x _ { n } \}$ located in a bounded region in $\mathbb { R } ^ { d }$ . By this assumption, we have the estimate of the gradient

$$
\begin{array}{l} \| \nabla_ {w _ {m}} \mathcal {L} (W) \| _ {2} \leq \frac {2}{N \sqrt {M}} \sum_ {n = 1} ^ {N} | \phi (x _ {n}; W) - y _ {n} | \cdot | a _ {m} | \cdot \mathbb {I} _ {w _ {m} ^ {\top} x _ {n} \geq 0} \cdot \| x _ {n} \| _ {2} \\ \leq \frac {2}{N \sqrt {M}} \sum_ {n = 1} ^ {N} | \phi (x _ {n}; W) - y _ {n} | \leq \frac {2}{\sqrt {M N}} \left(\sum_ {n = 1} ^ {N} | \phi (x _ {n}; W) - y _ {n} | ^ {2}\right) ^ {1 / 2} = \frac {2}{\sqrt {M}} \mathcal {L} (W) ^ {1 / 2}, \end{array}\tag{3.33}
$$

which holds for all $m \in [ M ]$

## Gram matrices and estimation

Define the symmetric matrix $H ^ { \infty } \in \mathbb { R } ^ { N \times N }$ with

$$
H _ {i j} ^ {\infty} = x _ {i} ^ {\top} x _ {j} \mathbb {E} _ {w \sim \mathcal {N} (0, I)} [ \mathbb {I} _ {w ^ {\top} x _ {i} \geq 0, w ^ {\top} x _ {j} \geq 0} ],
$$

and let $\lambda _ { 0 } = \lambda _ { \operatorname* { m i n } } ( H ^ { \infty } )$ be the smallest eigenvalue of $H ^ { \infty }$ . Here $H ^ { \infty }$ is the Gram matrix induced by the ReLU activation function and the random initialization. Note that $H ^ { \infty }$ and $\lambda _ { 0 }$ are both determined by the dataset of feature vectors $\{ x _ { n } \}$ . One can prove that if no two vectors in $\{ x _ { n } \}$ are parallel, then $\lambda _ { 0 }$ must be positive. However, $\lambda _ { 0 }$ usually approaches zero as $N \to \infty$ (See Figure 3.4).

Similarly, define the symmetric matrices $H ^ { ( t ) } \in \mathbb { R } ^ { n \times n }$ for $t = 0 , 1 , \ldots , T$ with $( i , j )$ -th entry

$$
H _ {i j} ^ {(t)} = \frac {1}{M} \sum_ {m = 1} ^ {M} x _ {i} ^ {\top} x _ {j} \mathbb {I} _ {w _ {m} ^ {(t) ^ {\top}} x _ {i} \geq 0, w _ {m} ^ {(t) ^ {\top}} x _ {j} \geq 0}.\tag{3.34}
$$

Note that $H ^ { ( 0 ) }$ can be seen as random variables since it is a function of the normal random vectors $w _ { m } ^ { ( 0 ) } ; H ^ { ( t ) } ( t \geq 1 )$ are also random variables since they are functions of $w _ { m } ^ { ( t ) }$ , which are determined by $w _ { m } ^ { ( 0 ) }$ via the gradient descent updates. First, we prove that with high probability $H ^ { ( 0 ) }$ is close to $H ^ { \infty }$ as long as M is large enough.

Lemma 3.1 Suppose that $M \geq { \frac { 3 2 N ^ { 2 } \ln \left( { \frac { 2 N ^ { 2 } } { \delta } } \right) } { \lambda _ { 0 } ^ { 2 } } }$ . For any $\delta \in ( 0 , 1 )$ , with probability at least $1 - \delta$ over the random variables $\{ w _ { m } ^ { ( 0 ) } \}$ , it holds that $\begin{array} { r } { \| H ^ { ( 0 ) } - H ^ { \infty } \| _ { 2 } \leq \frac { \lambda _ { 0 } } { 4 } } \end{array}$ and $\begin{array} { r } { \lambda _ { \operatorname* { m i n } } ( H ^ { ( 0 ) } ) \ge \frac { 3 } { 4 } \lambda _ { 0 } } \end{array}$

![](images/6b94b1a3c0fd989c4f389d9bdc4ce084f7873b2213275b7e0c21edcede88244f.jpg)  
Figure 3.4: We set $\{ x _ { n } \} _ { n = 1 } ^ { N }$ as 2D equispaced points on the $1 / \%$ unit ball (with angles from 0 to $\textstyle { \frac { \pi } { 2 } } \int$ The $\lambda _ { 0 }$ are numerically computed for $N = 2 , 4 , 8 , \dots , 1 0 2 4$ . We show the loglog plot of λ<sub>0</sub> versus N in this figure, which behaves almost as a straight line. Specifically, $\begin{array} { r } { \lambda _ { 0 } \approx \frac { 1 } { N ^ { 1 . 0 7 } } } \end{array}$

Proof: The diference of the (i, j)-th entry is

$$
H _ {i j} ^ {(0)} - H _ {i j} ^ {\infty} = \frac {1}{M} \sum_ {m = 1} ^ {M} x _ {i} ^ {\top} x _ {j} \left(\mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x _ {i} \geq 0, w _ {m} ^ {(0) ^ {\top}} x _ {j} \geq 0} - \mathbb {E} _ {w \sim \mathcal {N} (0, I)} \bigl [ \mathbb {I} _ {w ^ {\top} x _ {i} \geq 0, w ^ {\top} x _ {j} \geq 0} \bigr ]\right).
$$

Since $x _ { i } ^ { \top } x _ { j } \mathbb { I } _ { w _ { m } ^ { ( 0 ) } } { } ^ { \top } { } _ { x _ { i } \geq 0 , w _ { m } ^ { ( 0 ) } } { } ^ { \top } x _ { j } \geq 0 \} \in [ - 1 , 1 ]$ , by Hoefdings’ inequality,

$$
\mathbb {P} (\left| H _ {i j} ^ {(0)} - H _ {i j} ^ {\infty} \right| \leq C) \geq 1 - 2 \exp (- \frac {M C ^ {2}}{2}), \quad \forall C \geq 0.
$$

Letting $\begin{array} { r } { C = \sqrt { \frac { 2 \ln \left( \frac { 2 N ^ { 2 } } { \delta } \right) } { M } } } \end{array}$ above, we have with probability at least $\textstyle 1 - { \frac { \delta } { N ^ { 2 } } }$

$$
\left| H _ {i j} ^ {(0)} - H _ {i j} ^ {\infty} \right| \leq \sqrt {\frac {2 \ln \left(\frac {2 N ^ {2}}{\delta}\right)}{M}}.\tag{3.35}
$$

Note that the least probability $\textstyle 1 - { \frac { \delta } { N ^ { 2 } } }$ that (3.35) holds is for one pair $( i , j )$ . If the events (3.35) hold for all $( i , j )$ with $1 \leq i , j \leq N$ , the probability is at least $\begin{array} { r } { ( 1 - \frac { \delta } { N ^ { 2 } } ) ^ { N ^ { 2 } } \geq 1 - \delta } \end{array}$ . And with this probability,

$$
\| H ^ {(0)} - H ^ {\infty} \| _ {2} ^ {2} \leq \| H ^ {(0)} - H ^ {\infty} \| _ {F} ^ {2} \leq \sum_ {i, j} \left| H _ {i j} ^ {(0)} - H _ {i j} ^ {\infty} \right| ^ {2} \leq \frac {2 N ^ {2} \ln \left(\frac {2 N ^ {2}}{\delta}\right)}{M}.\tag{3.36}
$$

If $M \geq \frac { 3 2 N ^ { 2 } \ln \left( \frac { 2 N ^ { 2 } } { \delta } \right) } { \lambda _ { 0 } ^ { 2 } }$ , (3.36) leads to $\begin{array} { r } { \| H ^ { ( 0 ) } - H ^ { \infty } \| _ { 2 } \leq \frac { \lambda _ { 0 } } { 4 } } \end{array}$ . Moreover, using $\lambda _ { \operatorname* { m i n } } ( H ^ { \infty } ) - \lambda _ { \operatorname* { m i n } } ( H ^ { ( 0 ) } ) \leq$ $\| H ^ { ( 0 ) } - H ^ { \infty } \| _ { 2 }$ (see Exercise 3) leads to $\begin{array} { r } { \lambda _ { \operatorname* { m i n } } ( H ^ { ( 0 ) } ) \ge \frac { 3 } { 4 } \lambda _ { 0 } } \end{array}$ □

Next, we prove that $H ^ { ( t ) }$ is close to $H ^ { ( 0 ) }$ if $w _ { m } ^ { ( t ) }$ is close to $w _ { m } ^ { ( 0 ) }$ . We use $B ( x , r )$ to denote the closed ball centered at x with radius $r > 0$ in the d-dimensional Euclidean space, i.e., $B ( x , r ) =$ $\{ y \in \mathbb { R } ^ { d } : \| y - x \| _ { 2 } \leq r \}$

Lemma 3.2 For any $\delta \in ( 0 , 1 )$ , with probability at least $1 - \delta$ over the random variables $\{ w _ { m } ^ { ( 0 ) } \}$ }, the following statement holds: for any vectors $w _ { 1 } , \hdots , w _ { M } \in \mathbb { R } ^ { d }$ satisfying $\begin{array} { r } { w _ { m } \in B \left( w _ { m } ^ { ( 0 ) } , \frac { \sqrt { 2 \pi } \delta \lambda _ { 0 } } { 1 6 N ^ { 2 } } \right) } \end{array}$ $\lambda _ { \operatorname* { m i n } } ( H ) > \lambda _ { 0 } / 2$ , where $H \in \mathbb { R } ^ { N \times N }$ is the matrix with $( i , j ) \ – t h$ entry

$$
H _ {i j} = \frac {1}{M} \sum_ {m = 1} ^ {M} x _ {i} ^ {\top} x _ {j} \mathbb {I} _ {w _ {m} ^ {\top} x _ {i} \geq 0, w _ {m} ^ {\top} x _ {j} \geq 0}.\tag{3.37}
$$

Proof: For simplicity, we denote $\begin{array} { r } { c = \frac { \sqrt { 2 \pi } \delta } { 1 6 } } \end{array}$ . We define $A _ { n m }$ as the event that there exists some $\begin{array} { r } { w \in B ( w _ { m } ^ { ( 0 ) } , \frac { c \lambda _ { 0 } } { N ^ { 2 } } ) } \end{array}$ such that $\mathbb { I } _ { w _ { m } ^ { ( 0 ) } } \mathbb { T } _ { x _ { n } \geq 0 } \neq \mathbb { I } _ { w ^ { \top } x _ { n } \geq 0 }$ . This event happens if and only if $\begin{array} { r } { \left| w _ { m } ^ { ( 0 ) } { } ^ { \top } x _ { n } \right| < \frac { c \lambda _ { 0 } } { N ^ { 2 } } } \end{array}$ (see Exercise 2). Since $w _ { m } ^ { ( 0 ) } \sim \mathcal { N } ( 0 , I )$ , we have $w _ { m } ^ { ( 0 ) ^ { \top } } x _ { n } \sim \mathcal { N } ( 0 , 1 )$ , so

$$
\mathbb {P} (A _ {n m}) = \mathbb {P} _ {\xi \sim \mathcal {N} (0, 1)} \left(| \xi | <   \frac {c \lambda_ {0}}{N ^ {2}}\right) = \int_ {- c \frac {\lambda_ {0}}{N ^ {2}}} ^ {\frac {c \lambda_ {0}}{N ^ {2}}} \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t \leq \int_ {- \frac {c \lambda_ {0}}{N ^ {2}}} ^ {\frac {c \lambda_ {0}}{N ^ {2}}} \frac {1}{\sqrt {2 \pi}} \mathrm{d} t = \frac {2 c \lambda_ {0}}{\sqrt {2 \pi} N ^ {2}}, \quad \forall m, n.\tag{3.38}
$$

Now for vectors $w _ { 1 } , \dots , w _ { M }$ given by the hypothesis of the lemma, it holds that for any $1 \leq i , j \leq N$ 2

$$
\begin{array}{r l} & {\mathbb {E} [ | H _ {i j} ^ {(0)} - H _ {i j} | ] = \mathbb {E} \left[ \frac {1}{M} \left| x _ {i} ^ {\top} x _ {j} \sum_ {m = 1} ^ {M} \left(\mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x _ {i} \geq 0, w _ {m} ^ {(0) ^ {\top}} x _ {j} \geq 0} - \mathbb {I} _ {w _ {m} ^ {\top} x _ {i} \geq 0, w _ {m} ^ {\top} x _ {j} \geq 0}\right) \right| \right]} \\ & {\qquad \leq \mathbb {E} \left[ \frac {1}{M} \sum_ {m = 1} ^ {M} \left| \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x _ {i} \geq 0, w _ {m} ^ {(0) ^ {\top}} x _ {j} \geq 0} - \mathbb {I} _ {w _ {m} ^ {\top} x _ {i} \geq 0, w _ {m} ^ {\top} x _ {j} \leq 0} \right| \right].} \end{array}\tag{3.39}
$$

When $\begin{array} { r } { \left| \mathbb { I } _ { { w _ { m } ^ { ( 0 ) } } ^ { \top } x _ { i } \geq 0 , w _ { m } ^ { ( 0 ) } ^ { \top } x _ { j } \geq 0 } - \mathbb { I } _ { w _ { m } ^ { \top } x _ { i } \geq 0 , w _ { m } ^ { \top } x _ { j } \geq 0 } \right| = 1 } \end{array}$ , one of the indicators is 1 and the other is 0. This implies one of the following two cases holds:

$$
\bullet w _ {m} ^ {(0) ^ {\top}} x _ {i} \geq 0; w _ {m} ^ {(0) ^ {\top}} x _ {j} \geq 0; w _ {m} ^ {\top} x _ {i} <   0 \mathrm{or} w _ {m} ^ {\top} x _ {j} <   0;
$$

$$
\bullet w _ {m} ^ {(0) ^ {\top}} x _ {i} <   0 \mathrm{or} w _ {m} ^ {(0) ^ {\top}} x _ {j} <   0; w _ {m} ^ {\top} x _ {i} \geq 0; w _ {m} ^ {\top} x _ {j} \geq 0.
$$

This implies $w _ { m } ^ { ( 0 ) ^ { \top } } x _ { i }$ and $w _ { m } ^ { \top } x _ { i }$ have diferent signs, or $w _ { m } ^ { ( 0 ) ^ { \top } } x _ { j }$ and $w _ { m } ^ { \top } x _ { j }$ have diferent signs. And it is equivalent to $A _ { m i }$ or $A _ { m j }$ happens, i.e., $\mathbb { I } _ { A _ { m i } { \mathrm { ~ o r ~ } } A _ { m j } } = 1$ . Therefore, we conclude that

$$
\left| \mathbb {I} _ {w _ {m} ^ {(0)} ^ {\top} x _ {i} \geq 0, w _ {m} ^ {(0)} ^ {\top} x _ {j} \geq 0} - \mathbb {I} _ {w _ {m} ^ {\top} x _ {i} \geq 0, w _ {m} ^ {\top} x _ {j} \geq 0} \right| \leq \mathbb {I} _ {A _ {m i} \text {or} A _ {m j}}\tag{3.40}
$$

Combining (3.39) and (3.40) leads to

$$
\begin{array}{r l} & {\mathbb {E} [ | H _ {i j} ^ {(0)} - H _ {i j} | ] \leq \frac {1}{M} \sum_ {m = 1} ^ {M} \mathbb {E} [ \mathbb {I} _ {A _ {m i} \text {or} A _ {m j}} ] = \frac {1}{M} \sum_ {m = 1} ^ {M} \mathbb {P} (A _ {m i} \text {or} A _ {m j})} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \pmod {2},} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \pmod {2}.} \end{array}\tag{3.41}
$$

Summing over $( i , j )$ leads to $\begin{array} { r } { \mathbb { E } \left[ \sum _ { i , j = 1 } ^ { N } | H _ { i j } ^ { ( 0 ) } - H _ { i j } | \right] \leq \frac { 4 c \lambda _ { 0 } } { \sqrt { 2 \pi } } } \end{array}$ . Then by Markov’s inequality, with probability $1 - \delta ,$ , it holds that $\begin{array} { r } { \sum _ { i , j = 1 } ^ { N } | H _ { i j } ^ { ( 0 ) } - H _ { i j } | \leq \frac { 4 c \lambda _ { 0 } } { \sqrt { 2 \pi } \delta } } \end{array}$ . Therefore, with this probability,

$$
\lambda_ {\mathrm{min}} (H ^ {(0)}) - \lambda_ {\mathrm{min}} (H) \leq \| H ^ {(0)} - H \| _ {2} \leq \| H ^ {(0)} - H \| _ {F} \leq \sum_ {i, j = 1} ^ {N} | H _ {i j} ^ {(0)} - H _ {i j} | \leq \frac {4 c \lambda_ {0}}{\sqrt {2 \pi} \delta},\tag{3.42}
$$

which leads to

$$
\lambda_ {\mathrm{min}} (H) \geq \lambda_ {\mathrm{min}} (H ^ {(0)}) - \frac {4 c \lambda_ {0}}{\sqrt {2 \pi} \delta} \geq \frac {\lambda_ {0}}{2},\tag{3.43}
$$

where Lemma 3.1 is used.

## Estimation of sign preserving indices

Given $\delta \in ( 0 , 1 )$ , we define the set of indices

$$
S _ {n} = \left\{m \in [ M ]: \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x _ {n} \geq 0} = \mathbb {I} _ {w ^ {\top} x _ {n} \geq 0}, \forall w \in B \left(w _ {m} ^ {(0)}, \frac {\sqrt {2 \pi} \delta \lambda_ {0}}{1 6 N ^ {2}}\right) \right\}.
$$

Namely, $S _ { n }$ consists of all indices m that all vectors near $w _ { m } ^ { ( 0 ) }$ has the same sign as $w _ { m } ^ { ( 0 ) }$ in the sense of the inner product with $x _ { n }$ . We also define the its complement by

$$
S _ {n} ^ {\perp} = [ M ] \backslash S _ {n} = \left\{m \in [ M ]: \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x _ {n} \geq 0} \neq \mathbb {I} _ {w ^ {\top} x _ {n} \geq 0}, \exists w \in B \left(w _ {m} ^ {(0)}, \frac {\sqrt {2 \pi} \delta \lambda_ {0}}{1 6 N ^ {2}}\right) \right\}.
$$

The cardinality of $S _ { n } ^ { \perp }$ can be estimated by the following lemma.

Lemma 3.3 For any $\delta \in ( 0 , 1 )$ , with probability at least $1 - \delta$ over the initialization (3.29), we have $\begin{array} { r } { \sum _ { n = 1 } ^ { N } | S _ { n } ^ { \perp } | \le \frac { \bar { M ^ { \lambda } } _ { 0 } } { 8 N } } \end{array}$

Proof: As in the proof of Lemma 3.2, we denote $\begin{array} { r } { c = \frac { \sqrt { 2 \pi } \delta } { 1 6 } } \end{array}$ , and define $A _ { n m }$ by the event that there exists some $\begin{array} { r } { v \in B ( w _ { m } ^ { ( 0 ) } , \frac { c \lambda _ { 0 } } { N ^ { 2 } } ) } \end{array}$ such that $\mathbb { I } _ { w _ { m } ^ { ( 0 ) } } { } ^ { \top } { } _ { x _ { n } \geq 0 } \neq \mathbb { I } _ { w ^ { \top } x _ { n } \geq 0 }$ , and we have proven $\begin{array} { r } { \mathbb { P } ( A _ { n m } ) \leq \frac { 2 c \lambda _ { 0 } } { \sqrt { 2 \pi } N ^ { 2 } } . } \end{array}$ which holds for all $m \in [ M ]$ . Also, note that $A _ { n m }$ are independent events in terms of $m .$ , so

$$
\mathbb {E} \left[ | S _ {n} ^ {\perp} | \right] = M \cdot \mathbb {P} (A _ {n m}) \leq \frac {2 M c \lambda_ {0}}{\sqrt {2 \pi} N ^ {2}},
$$

and

$$
\mathbb {E} \left[ \sum_ {n = 1} ^ {N} | S _ {n} ^ {\perp} | \right] \leq \frac {2 M c \lambda_ {0}}{\sqrt {2 \pi} N}.
$$

By Markov’s inequality,

$$
\mathbb {P} \left(\sum_ {n = 1} ^ {N} | S _ {n} ^ {\perp} | \leq C\right) \geq 1 - \frac {\mathbb {E} \left[ \sum_ {n = 1} ^ {N} | S _ {n} ^ {\perp} | \right]}{C} \geq 1 - \frac {\frac {2 M c \lambda_ {0}}{\sqrt {2 \pi N}}}{C}
$$

for any $C > 0$ . Taking $\begin{array} { r } { C = \frac { 2 M c \lambda _ { 0 } } { \sqrt { 2 \pi } N \delta } } \end{array}$ completes the proof.

Next, we estimate the loss function immediately after the random initialization of $a _ { m }$ and $w _ { m }$

Lemma 3.4 For any $\delta \in ( 0 , 1 )$ , with probability at least $1 - \delta$

$$
\mathcal {L} (W ^ {(0)}) \leq \frac {\frac {1}{2} + Y ^ {2}}{\delta},\tag{3.44}
$$

under the random initialization (3.29) of variables $\{ a _ { m } ^ { ( 0 ) } , w _ { m } ^ { ( 0 ) } \} _ { m = 1 } ^ { M }$

Proof: Note that

$$
\begin{array}{r l r} & & {\mathbb {E} [ \phi (x _ {n}; W ^ {(0)}) ] = \mathbb {E} \left[ \frac {1}{\sqrt {M}} \sum_ {m = 1} ^ {M} a _ {m} ^ {(0)} (w _ {m} ^ {(0) ^ {\top}} x) \cdot \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} \right]} \\ & & {= \frac {1}{\sqrt {M}} \sum_ {m = 1} ^ {M} \mathbb {E} [ a _ {m} ^ {(0)} ] \mathbb {E} [ (w _ {m} ^ {(0) ^ {\top}} x) \cdot \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} ] = 0} \end{array}\tag{3.45}
$$

and

$$
\begin{array}{r l} & {\mathbb {E} [ \phi^ {2} (x _ {n}; W ^ {(0)}) ] = \mathbb {E} \left[ \frac {1}{M} \left(\sum_ {m = 1} ^ {M} a _ {m} ^ {(0)} (w _ {m} ^ {(0) ^ {\top}} x) \cdot \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0}\right) ^ {2} \right]} \\ & {\quad = \frac {1}{M} \mathbb {E} \left[ \sum_ {m, m ^ {\prime} = 1} ^ {M} a _ {m} ^ {(0)} a _ {m ^ {\prime}} ^ {(0)} (w _ {m} ^ {(0) ^ {\top}} x) (w _ {m ^ {\prime}} ^ {(0) ^ {\top}} x) \cdot \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} \mathbb {I} _ {w _ {m ^ {\prime}} ^ {(0) ^ {\top}} x \geq 0} \right]} \\ & {\quad \frac {1}{M} \Big (\sum_ {m \neq m ^ {\prime}} \mathbb {E} [ a _ {m} ^ {(0)} ] \mathbb {E} [ a _ {m ^ {\prime}} ^ {(0)} ] \mathbb {E} [ (w _ {m} ^ {(0) ^ {\top}} x) (w _ {m ^ {\prime}} ^ {(0) ^ {\top}} x) \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} \mathbb {I} _ {w _ {m ^ {\prime}} ^ {(0) ^ {\top}} x \geq 0} ]} \\ & {\qquad + \sum_ {m = 1} ^ {M} \mathbb {E} [ | a _ {m} ^ {(0)} | ^ {2} ] \mathbb {E} [ (w _ {m} ^ {(0) ^ {\top}} x) ^ {2} \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} ^ {2} ] \Big) = \frac {1}{2},} \end{array}\tag{3.46}
$$

where $\mathbb { E } [ a _ { m } ^ { ( 0 ) } ] = 0 , \mathbb { E } [ | a _ { m } ^ { ( 0 ) } | ^ { 2 } ] = 1$ and

$$
\begin{array}{r l} & {\mathbb {E} [ (w _ {m} ^ {(0) ^ {\top}} x) ^ {2} \mathbb {I} _ {w _ {m} ^ {(0) ^ {\top}} x \geq 0} ^ {2} ] = \mathbb {E} _ {\xi \sim \mathcal {N} (0, 1)} [ \xi^ {2} \mathbb {I} _ {\xi \geq 0} ] = \int_ {- \infty} ^ {\infty} t ^ {2} \mathbb {I} _ {t \geq 0} \cdot \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t} \\ & {\qquad = \int_ {0} ^ {\infty} t ^ {2} \cdot \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t = \frac {1}{2} \int_ {- \infty} ^ {\infty} t ^ {2} \cdot \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t = \frac {1}{2} \mathbb {E} _ {\xi \sim \mathcal {N} (0, 1)} [ \xi^ {2} ] = \frac {1}{2}.} \end{array}\tag{3.47}
$$

are used. Therefore,

$$
\begin{array}{r l} & {\mathbb {E} [ L (W ^ {(0)}) ] = \mathbb {E} \left[ \frac {1}{N} \sum_ {n = 1} ^ {N} \left| \phi (x _ {n}; W ^ {(0)}) - y _ {n} \right| ^ {2} \right]} \\ & {\qquad = \frac {1}{N} \mathbb {E} \left[ \sum_ {n = 1} ^ {N} \left(\phi^ {2} (x _ {n}; W ^ {(0)}) - 2 \phi (x _ {n}; W ^ {(0)}) \cdot y _ {n} + y _ {n} ^ {2}\right) \right]} \\ & {\qquad = \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\mathbb {E} [ \phi^ {2} (x _ {n}; W ^ {(0)}) ] - 2 \mathbb {E} [ \phi (x _ {n}; W ^ {(0)}) ] \cdot y _ {n} + y _ {n} ^ {2}\right) = \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\frac {1}{2} + y _ {n} ^ {2}\right) \leq \frac {1}{2} + Y ^ {2}.} \end{array}\tag{3.48}
$$

By Markov’s inequality, we have with probability at least $\begin{array} { r } { 1 - \delta , L ( W ^ { ( 0 ) } ) \le \frac { \frac { 1 } { 2 } + Y ^ { 2 } } { \delta } } \end{array}$

## Proof of the main theorem

Finally, the main theorem for the convergence of gradient descent is given as follows.

Theorem 3.1 Assume that $\lambda _ { 0 } > 0$ . For any $\delta \in ( 0 , 1 )$ , let the width $M \ge \frac { 2 ^ { 1 3 } N ^ { 6 } ( \frac { 1 } { 2 } + Y ^ { 2 } ) } { \pi \lambda _ { 0 } ^ { 4 } \delta ^ { 3 } }$ and the learning rate $\begin{array} { r } { \eta \le \frac { \lambda _ { 0 } } { 8 N } } \end{array}$ . Then with probability at least $1 - 4 \delta$ over the random initialization (3.29), it holds that for $t = 0 , 1 , 2 , . . .$

$$
\mathcal {L} (W ^ {(t)}) \leq \left(1 - \frac {\eta \lambda_ {0}}{2 N}\right) ^ {t} \mathcal {L} (W ^ {(0)}).\tag{3.49}
$$

Proof: We prove (3.49) by induction. Suppose (3.49) holds for $t = 1 , \ldots , k$ . Then using (3.33), for every $m \in [ M ]$ 2

$$
\| w _ {m} ^ {(k + 1)} - w _ {m} ^ {(0)} \| _ {2} \leq \sum_ {t = 0} ^ {k} \| w _ {m} ^ {(t + 1)} - w _ {m} ^ {(t)} \| _ {2} \leq \eta \sum_ {t = 0} ^ {k} \| \nabla_ {w _ {m}} \mathcal {L} (W ^ {(t)}) \| _ {2} \leq \frac {2 \eta}{\sqrt {M}} \sum_ {t = 0} ^ {k} \mathcal {L} (W ^ {(t)}) ^ {1 / 2}
$$

$$
\leq \frac {2 \eta}{\sqrt {M}} \sum_ {t = 0} ^ {k} \left(1 - \frac {\eta \lambda_ {0}}{2 N}\right) ^ {t} \mathcal {L} (W ^ {(0)}) ^ {1 / 2} \leq \frac {2 \eta}{\sqrt {M}} \cdot \frac {1}{1 - (1 - \frac {\eta \lambda_ {0}}{2 N}) ^ {1 / 2}} \cdot \mathcal {L} (W ^ {(0)}) ^ {1 / 2}.\tag{3.50}
$$

Using $\begin{array} { r } { 1 - ( 1 - \frac { \eta \lambda _ { 0 } } { 2 N } ) ^ { 1 / 2 } = 1 - \left( 1 - \frac { 1 } { 2 } \cdot \frac { \eta \lambda _ { 0 } } { 2 N } - \frac { 1 } { 8 } \cdot \frac { \eta ^ { 2 } \lambda _ { 0 } ^ { 2 } } { 4 N ^ { 2 } } + \dots \right) \geq 1 - ( 1 - \frac { \eta \lambda _ { 0 } } { 4 N } ) = \frac { \eta \lambda _ { 0 } } { 4 N } } \end{array}$ , it follows that

$$
\| w _ {m} ^ {(k + 1)} - w _ {m} ^ {(0)} \| _ {2} \leq \frac {8 N}{\lambda_ {0} \sqrt {M}} \mathcal {L} (W ^ {(0)}) ^ {1 / 2} \triangleq R.\tag{3.51}
$$

In particular, (3.49) holds for $t = 1 , \ldots , k - 1$ , so a similar argument also deduces that

$$
\| w _ {m} ^ {(k)} - w _ {m} ^ {(0)} \| _ {2} \leq R.\tag{3.52}
$$

Next, for every $n \in [ N ]$ 2

$$
\phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) = \frac {1}{\sqrt {M}} \sum_ {m = 1} ^ {M} a _ {m} \left[ \sigma \left(w _ {m} ^ {(k + 1) ^ {\top}} x _ {n}\right) - \sigma \left(w _ {m} ^ {(k) ^ {\top}} x _ {n}\right) \right] \triangleq I _ {n} + J _ {n},\tag{3.53}
$$

where

$$
I _ {n} = \frac {1}{\sqrt {M}} \sum_ {m \in S _ {n}} a _ {m} \left[ \sigma \left(w _ {m} ^ {(k + 1) ^ {\top}} x _ {n}\right) - \sigma \left(w _ {m} ^ {(k) ^ {\top}} x _ {n}\right) \right],\tag{3.54}
$$

$$
J _ {n} = \frac {1}{\sqrt {M}} \sum_ {m \in S _ {n} ^ {\perp}} a _ {m} \left[ \sigma \left(\left(w _ {m} ^ {(k)} - \eta \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)})\right) ^ {\top} x _ {n}\right) - \sigma \left(w _ {m} ^ {(k) ^ {\top}} x _ {n}\right) \right].\tag{3.55}
$$

Using the fact $| \sigma ( t _ { 1 } ) - \sigma ( t _ { 2 } ) | \leq | t _ { 1 } - t _ { 2 } |$ and (3.33), we estimate $\left| J _ { n } \right|$ by

$$
\begin{array}{l} | J _ {n} | \leq \frac {1}{\sqrt {M}} \sum_ {m \in S _ {n} ^ {\perp}} | a _ {m} | \left| \eta \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)}) ^ {\top} x _ {n} \right| \leq \frac {\eta}{\sqrt {M}} \sum_ {m \in S _ {n} ^ {\perp}} \left\| \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)}) \right\| _ {2} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}\tag{3.56}
$$

By Lemma 3.4, with probability 1−δ, $R \leq \frac { 4 N ^ { 2 } \sqrt { \frac { 1 } { 2 } + Y ^ { 2 } } } { \lambda _ { 0 } \sqrt { M \delta } }$ . So if $\begin{array} { r } { M \ge \frac { 2 ^ { 1 3 } N ^ { 6 } ( \frac { 1 } { 2 } + Y ^ { 2 } ) } { \pi \lambda _ { 0 } ^ { 4 } \delta ^ { 3 } } } \end{array}$ , with this probability we have $\begin{array} { r } { R \le \frac { \sqrt { 2 \pi } \delta \lambda _ { 0 } } { 1 6 N ^ { 2 } } } \end{array}$ , and therefore by (3.51) and (3.52),

$$
w _ {m} ^ {(k)}, w _ {m} ^ {(k + 1)} \in B \left(w _ {m} ^ {(0)}, \frac {\sqrt {2 \pi} \delta \lambda_ {0}}{1 6 N ^ {2}}\right).\tag{3.57}
$$

Now recall that $H ^ { ( k ) }$ is the matrix with $( n , j )$ -th entry being $H _ { n j } ^ { ( k ) }$ defined in (3.34). We can use Lemma 3.2 to estimate $\lambda _ { \operatorname* { m i n } } \left( H ^ { ( k ) } \right)$ . In fact, with probability at least $1 - \delta$ , (3.57) holds, in which case, with probability at least $1 - \delta$ 2

$$
\lambda_ {\mathrm{min}} \left(H ^ {(k)}\right) > \frac {\lambda_ {0}}{2}.\tag{3.58}
$$

Consequently, we claim that with probability at least $( 1 - \delta ) ^ { 2 }$ , (3.58) holds.

Moreover, (3.57) implies that $w _ { m } ^ { ( k + 1 ) ^ { \top } } x _ { n }$ and $w _ { m } ^ { ( k ) } \mathbf { \Phi } _ { x _ { n } } ^ { \mid }$ have the same signs as $w _ { m } ^ { ( 0 ) ^ { \top } } x _ { n }$ , and hence

$$
\begin{array}{l} I _ {n} = \frac {1}{\sqrt {M}} \sum_ {m \in S _ {n}} a _ {m} \mathbb {I} _ {w _ {m} ^ {(k)} ^ {\top} x _ {n} \geq 0} \left(w _ {m} ^ {(k + 1) ^ {\top}} x _ {n} - w _ {m} ^ {(k) ^ {\top}} x _ {n}\right) \\ = \frac {1}{\sqrt {M}} \sum_ {m \in S _ {n}} a _ {m} \mathbb {I} _ {w _ {m} ^ {(k)} ^ {\top} x _ {n} \geq 0} \left(- \eta \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)}) ^ {\top} x _ {n}\right) \\ = - \frac {2 \eta}{M N} \sum_ {m \in S _ {n}} a _ {m} ^ {2} \sum_ {j = 1} ^ {N} \mathbb {I} _ {w _ {m} ^ {(k)} ^ {\top} x _ {n} \geq 0, w _ {m} ^ {(k)} ^ {\top} x _ {j} \geq 0} (\phi (x _ {j}; W ^ {(k)}) - y _ {j}) x _ {j} ^ {\top} x _ {n} \\ = - \frac {2 \eta}{N} \sum_ {j = 1} ^ {N} (\phi (x _ {j}; W ^ {(k)}) - y _ {j}) (H _ {n j} ^ {(k)} - H _ {n j} ^ {\perp , (k)}), \end{array}\tag{3.59}
$$

where

$$
H _ {n j} ^ {\perp , (k)} := \frac {1}{M} \sum_ {m \in S _ {n} ^ {\perp}} x _ {n} ^ {\top} x _ {j} \mathbb {I} _ {w _ {m} ^ {(k)} ^ {\top} x _ {n} \geq 0, w _ {m} ^ {(k)} ^ {\top} x _ {j} \geq 0}.
$$

Similar to $H ^ { ( k ) }$ , we use $H ^ { \perp , ( k ) }$ to denote the matrix with $( n , j )$ -th entry being $H _ { n j } ^ { \perp , ( k ) }$ . Then it is estimated using Lemma 3.3 that with probability at least $1 - \delta$

$$
\| H ^ {\perp , (k)} \| _ {2} \leq \| H ^ {\perp , (k)} \| _ {F} \leq \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} | H _ {n j} ^ {\perp , (k)} | \leq \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} \frac {| S _ {n} ^ {\perp} |}{M} \leq \sum_ {j = 1} ^ {N} \frac {1}{M} \cdot \frac {M \lambda_ {0}}{8 N} = \frac {\lambda_ {0}}{8}.\tag{3.60}
$$

Next, we denote $e _ { n } ^ { ( k ) } = \phi ( x _ { n } ; W ^ { ( k ) } ) - y _ { n }$ for simplicity, and use (3.53) and (3.59) to obtain

$$
\begin{array}{l} L (W ^ {(k + 1)}) = \frac {1}{N} \sum_ {n = 1} ^ {N} | e _ {n} ^ {(k + 1)} | ^ {2} = \frac {1}{N} \sum_ {n = 1} ^ {N} | \phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) + e _ {n} ^ {(k)} | ^ {2} \\ = \frac {1}{N} \sum_ {n = 1} ^ {N} \left(\left| \phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) \right| ^ {2} + 2 \left(\phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)})\right) e _ {n} ^ {(k)} + | e _ {n} ^ {(k)} | ^ {2}\right) \\ = \frac {1}{N} \sum_ {n = 1} ^ {N} \left| \phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) \right| ^ {2} + \frac {1}{N} \sum_ {n = 1} ^ {N} | e _ {n} ^ {(k)} | ^ {2} + \frac {2}{N} \sum_ {n = 1} ^ {N} (I _ {n} + J _ {n}) e _ {n} ^ {(k)} \\ = \frac {1}{N} \sum_ {n = 1} ^ {N} \left| \phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) \right| ^ {2} + \mathcal {L} (W ^ {(k)}) - \frac {4 \eta}{N ^ {2}} \sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} e _ {n} ^ {(k)} e _ {j} ^ {(k)} (H _ {n j} ^ {(k)} - H _ {n j} ^ {\perp , (k)}) \\ + \frac {2}{N} \sum_ {n = 1} ^ {N} J _ {n} e _ {n} ^ {(k)}. \end{array} \tag {3.61}
$$

Using a similar argument as in (3.56), the first term above can be roughly estimated by

$$
\begin{array}{l} \left| \phi (x _ {n}; W ^ {(k + 1)}) - \phi (x _ {n}; W ^ {(k)}) \right| \\ = \frac {1}{\sqrt {M}} \sum_ {m \in [ M ]} a _ {m} \left[ \sigma \left(\left(w _ {m} ^ {(k)} - \eta \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)})\right) ^ {\top} x _ {n}\right) - \sigma \left(w _ {m} ^ {(k) ^ {\top}} x _ {n}\right) \right] \\ \leq \frac {1}{\sqrt {M}} \sum_ {m \in [ M ]} | a _ {m} | \left| \eta \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)}) ^ {\top} x _ {n} \right| \leq \frac {\eta}{\sqrt {M}} \sum_ {m \in [ M ]} \left\| \nabla_ {w _ {m}} \mathcal {L} (W ^ {(k)}) \right\| _ {2} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \leq 2 \eta \mathcal {L} (W ^ {(k)}) ^ {1 / 2} \end{array}\tag{3.62}
$$

Besides, denoting $e ^ { ( k ) } = [ e _ { 1 } ^ { ( k ) } ~ . . . ~ e _ { N } ^ { ( k ) } ] ^ { \top }$ , we can use (3.58), (3.60) and Lemma 3.3 to estimate other terms:

• with probability at least $( 1 - \delta ) ^ { 2 }$

$$
\sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} e _ {n} ^ {(k)} e _ {j} ^ {(k)} H _ {n j} ^ {(k)} = \boldsymbol {e} ^ {(k) ^ {\top}} H ^ {(k)} \boldsymbol {e} ^ {(k)} \geq \frac {\lambda_ {0}}{2} \| \boldsymbol {e} ^ {(k)} \| _ {2} ^ {2} = \frac {\lambda_ {0} N}{2} \mathcal {L} (W ^ {(k)});\tag{3.63}
$$

• with probability at least $1 - \delta$ 2

$$
\sum_ {n = 1} ^ {N} \sum_ {j = 1} ^ {N} e _ {n} ^ {(k)} e _ {j} ^ {(k)} H _ {n j} ^ {\perp , (k)} = \boldsymbol {e} ^ {(k) ^ {\top}} H ^ {\perp , (k)} \boldsymbol {e} ^ {(k)} \leq \frac {\lambda_ {0}}{8} \| \boldsymbol {e} ^ {(k)} \| _ {2} ^ {2} = \frac {\lambda_ {0} N}{8} \mathcal {L} (W ^ {(k)});\tag{3.64}
$$

• with probability at least $1 - \delta$

$$
\begin{array}{l} \sum_ {n = 1} ^ {N} J _ {n} e _ {n} ^ {(k)} \leq \left(\sum_ {n = 1} ^ {N} J _ {n} ^ {2}\right) ^ {1 / 2} \left(\sum_ {n = 1} ^ {N} e _ {n} ^ {(k) ^ {2}}\right) ^ {1 / 2} \leq \left(\sum_ {n = 1} ^ {N} | J _ {n} |\right) \cdot N ^ {1 / 2} \mathcal {L} (W ^ {(k)}) ^ {1 / 2} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \q\tag{3.65}
$$

Finally, substituting (3.62)-(3.65) to (3.61), we have that with probability at least $( 1 - \delta ) ^ { 4 } >$ $1 - 4 \delta$ that

$$
L (W ^ {(k + 1)}) \leq \left(4 \eta^ {2} + 1 - \frac {2 \eta \lambda_ {0}}{N} + \frac {\eta \lambda_ {0}}{2 N} + \frac {\eta \lambda_ {0}}{2 N ^ {3 / 2}}\right) \mathcal {L} (W ^ {(k)}) \leq \left(1 - \frac {\eta \lambda_ {0}}{N} + 4 \eta^ {2}\right) \mathcal {L} (W ^ {(k)}).\tag{3.66}
$$

So, if $\begin{array} { r } { \eta \le \frac { \lambda _ { 0 } } { 8 N } } \end{array}$ , with the above probability,

$$
L (W ^ {(k + 1)}) \leq \left(1 - \frac {\eta \lambda_ {0}}{N} + 4 \eta \cdot \frac {\lambda_ {0}}{8 N}\right) \mathcal {L} (W ^ {(k)}) = \left(1 - \frac {\eta \lambda_ {0}}{2 N}\right) \mathcal {L} (W ^ {(k)}) \leq \left(1 - \frac {\eta \lambda_ {0}}{2 N}\right) ^ {k + 1} \mathcal {L} (W ^ {(0)}),
$$

which completes the proof.

## 3.3.2 Optimization of deep networks

## 3.4 Exercise

## Problem 1

Let $A \in \mathbb { R } ^ { n \times n }$ be a nonsingular matrix and $b \in \mathbb { R } ^ { n \times 1 }$ be a vector. Define $\begin{array} { r } { \mathcal { L } ( x ) = ( \frac { 1 } { 2 } x ^ { \top } A x - b ^ { \top } x ) ^ { 2 } } \end{array}$ for $x \in \mathbb { R } ^ { n \times 1 }$

(1) Find the gradient $\nabla _ { x } \mathcal { L } ;$

(2) Write the iteration scheme of the gradient descent method;

(3) Suppose A is symmetric positive definite. Show that the Hessian matrix of $\mathcal { L } , \mathrm { i . e . , } \left[ \partial _ { x _ { i } x _ { j } } \mathcal { L } ( x ) \right] _ { i = 1 , \ldots , n } ^ { j = 1 , \ldots , n }$ is symmetric positive definite if ${ \begin{array} { l } { { \frac { 1 } { 2 } } x ^ { \top } A x - b ^ { \top } x > 0 } \end{array} }$ (so that $\mathcal { L }$ is convex).

## Exercise 2

Let $x _ { 0 } , y _ { 0 } \in \mathbb { R } ^ { d }$ be two vectors with $\| x _ { 0 } \| _ { 2 } = 1$ . Let $c > 0$ be a constant. Prove that the statement

$$
\mathbb {I} _ {x _ {0} ^ {\top} y \geq 0} = \mathbb {I} _ {x _ {0} ^ {\top} y _ {0} \geq 0}, \quad \forall y \in B (x _ {0}, c)
$$

holds true if and only $\mathrm { i f ~ } | x _ { 0 } ^ { \top } y _ { 0 } | \geq c .$

## Exercise 3

Let A, $B \in \mathbb { R } ^ { n \times n }$ be two symmetric matrices.

(1) Suppose $B - A$ is semi-positive definite. Prove that $\lambda _ { \operatorname* { m i n } } ( B ) \geq \lambda _ { \operatorname* { m i n } } ( A )$

(2) Prove that $| \lambda _ { \operatorname* { m i n } } ( A ) - \lambda _ { \operatorname* { m i n } } ( B ) | \leq \| A - B \| _ { 2 } .$

(Hint: use the theorem of Rayleigh quotient - for any real symmetric matrix $A , x ^ { \top } A x$ with $\| { \boldsymbol { x } } \| _ { 2 } = 1$ ranges over $[ \lambda _ { \operatorname* { m i n } } ( A ) , \lambda _ { \operatorname* { m a x } } ( A ) ] . )$

## Chapter 4

## Appendix

## 4.1 Concepts in Real Analysis

## 4.1.1 Dini’s theorem

Theorem 4.1 (Dini’s theorem) Let $( f _ { n } ) _ { n } \subset C ( [ a , b ] )$ satisfy $f _ { n + 1 } ( x ) \leq f _ { n } ( x )$ (or $f _ { n + 1 } ( x ) \geq$ $f _ { n } ( x ) )$ for all $x \in [ a , b ]$ . Suppose $f _ { n } ( x )$ converges to $g ( x )$ pointwise on $[ a , b ]$ and $g \in C ( [ a , b ] )$ , then the convergence is uniform.

## 4.1.2 Riesz representation theorem

Let H be a Hilbert space equipped with inner product $\langle \cdot , \cdot \rangle$ . We say ℓ is a linear functional if it is a linear transformation from H to a field of scalars such as R or C. A linear functional ℓ is said to be continuous if

$$
| \ell (f) | \leq C \| f \|, \quad \forall f \in H,
$$

where $C > 0$ is a constant only depending on $\ell ,$ and $\lVert x \rVert = \langle x , x \rangle$ is the norm of x induced by $\langle \cdot , \cdot \rangle$ Then it holds that

Theorem 4.2 (Riesz representation theorem) Let ℓ be a continuous linear functional on a Hilbert space H. Then, there exists a unique $g \in H$ such that

$$
\ell (f) = \langle f, g \rangle , \quad \forall f \in H.
$$

Moreover, $\| \ell \| _ { * } = \| g \|$ , where $\| \ell \| _ { * } : = \operatorname* { i n f } \{ c > 0 : \| \ell ( f ) \| \leq c \| f \| , \forall f \in H \| \}$ is the operator norm of ℓ.

For any $\Omega \subset \mathbb { R } ^ { d }$ , the representation theorem for $L ^ { 2 } ( \Omega )$ is given as follows.

Proposition 4.1 Let ℓ be a continuous linear functional on $L ^ { 2 } ( \Omega )$ . Then, there exists a function $g \in L ^ { 2 } ( \Omega )$ such that

$$
\ell (f) = \int_ {\Omega} f (x) g (x) \mathrm{d} x, \quad \forall f \in L ^ {2} (\Omega).
$$

Moreover, it holds that

Theorem 4.3 (Riesz-Markov-Kakutani representation theorem) Let ℓ be a bounded linear functional on $C ( K )$ with K compact. Then there exists a unique finite signed Borel measure $\mu$ supported on K, such that $\begin{array} { r } { \ell ( f ) = \int _ { K } f ( x ) \mathrm { d } \mu ( x ) } \end{array}$ for all $f \in C ( K )$ . Moreover, $\| \ell \| _ { * } = | \mu | ( K )$ .

## 4.1.3 Distribution and Dirac delta function

Let $\Omega \subset \mathbb { R } ^ { d }$ be a region and $C _ { c } ^ { \infty } ( \Omega )$ be the class of infinitely diferentiable functions whose support is a compact subset of Ω. Then distributions (or Schwartz distributions) on Ω are continuous linear functionals on $C _ { c } ^ { \infty } ( \Omega )$ when this vector space is endowed with a particular topology called the canonical LF-topology. Briefly, a distribution T maps a function $f \in C _ { c } ^ { \infty } ( \Omega )$ to a scalar $T [ f ]$ . One equivalent condition of distribution is as follows.

Theorem 4.4 Let T be a linear functional on $C _ { c } ^ { \infty } ( \Omega )$ . Then $T$ is a distribution if and only if for every compact set $K \subset \Omega$ , there exist $C > 0$ and $N \in  { \mathbb { N } }$ such that

$$
| T [ f ] | \leq C \sup \{| \partial^ {\alpha} f (x) |: x \in \Omega , | \alpha | \leq N | \}\tag{4.1}
$$

for all $f \in C _ { c } ^ { \infty } ( \Omega )$ with support contained in K.

The Dirac delta function δ is a distribution on $\mathbb { R }$ rather than a function in the classical sense. Specifically, δ is defined by

$$
\delta [ f ] = f (0), \quad \forall f \in C _ {c} ^ {\infty} (\mathbb {R}).
$$

Namely, δ is an evaluation operator that returns the value at zero of any function. Note that δ satisfies the condition (4.1) with $C = 1$ and $N = 0$

The delta function can be approximated in the following sense. For every $n \in \mathbb { Z } ^ { + }$ , we define the function

$$
\phi_ {n} (x) = \left\{ \begin{array}{l l} n, & x \in [ - \frac {1}{2 n}, \frac {1}{2 n} ], \\ 0, & x \in \mathbb {R} \backslash [ - \frac {1}{2 n}, \frac {1}{2 n} ] \end{array} \right.\tag{4.2}
$$

satisfying the normalization condition $\begin{array} { r } { \int _ { \mathbb { R } } \phi _ { n } ( x ) \mathrm { d } x = 1 } \end{array}$ . And we define the following distribution

$$
T _ {n} [ f ] = \int_ {\mathbb {R}} f (x) \phi_ {n} (x) \mathrm{d} x, \quad \forall f \in C _ {c} ^ {\infty} (\mathbb {R}),\tag{4.3}
$$

in which $\phi _ { n }$ can be viewed as the representation of $T _ { n }$ in the Hilbert space $L ^ { 2 } ( \mathbb { R } )$ . Then $T _ { n } \to \delta$ in the sense of linear operators. (more details) Strictly, we can not find a classical function $\phi ( x )$ such that

$$
\delta [ f ] = \int_ {\mathbb {R}} f (x) \phi (x) \mathrm{d} x, \quad \forall f \in C _ {c} ^ {\infty} (\mathbb {R}).\tag{4.4}
$$

But $\phi$ can be represented heuristically as

$$
\phi (x) = \left\{ \begin{array}{l l} \infty , & x = 0, \\ 0, & x \neq 0, \end{array} \right.\tag{4.5}
$$

which is enforced to satisfy

$$
\int_ {\mathbb {R}} \phi (x) \mathrm{d} x = 1.\tag{4.6}
$$

Note that (4.5) and (4.6) can not hold together in Lebesgue integration theory, because the function (4.5) is zero almost everywhere and has integral equal to zero.

It is also noted that $\phi _ { n }  \phi$ pointwise. But the representation functions $\phi _ { n }$ approximating to $\phi$ are not unique. There exist other types of functions approximating to $\phi ( x )$ , and they can even be not compactly supported. Moreover, let $H ( x ) = { \left\{ \begin{array} { l l } { 1 , } & { x \geq 0 , } \\ { 0 , } & { x < 0 } \end{array} \right. }$ be the Heaviside function. Then for any $f \in C _ { c } ^ { \infty } (  { \mathbb { R } } )$

$$
\int_ {\mathbb {R}} f ^ {\prime} (x) H (x) \mathrm{d} x = \int_ {0} ^ {\infty} f ^ {\prime} (x) \mathrm{d} x = f (\infty) - f (0) = - f (0) = - \delta [ f ].\tag{4.7}
$$

Heuristically, using integration by parts, we have

$$
\int_ {\mathbb {R}} f (x) H ^ {\prime} (x) \mathrm{d} x = - \int_ {\mathbb {R}} f ^ {\prime} (x) H (x) \mathrm{d} x = \int_ {\mathbb {R}} f (x) \phi (x) \mathrm{d} x,\tag{4.8}
$$

which implies $H ^ { \prime } ( x ) = \phi ( x )$ in the distribution sense.

## 4.2 Measure Theory

## 4.2.1 Measurable spaces and measurable functions

A measurable space is a pair (X, Σ), where X is a set and $\Sigma \subseteq 2 ^ { X }$ is a σ-algebra:

1. $X \in \Sigma$

2. $A \in \Sigma \Rightarrow A ^ { c } \in \Sigma .$

3. $A _ { 1 } , A _ { 2 } , \cdot \cdot \cdot \in \Sigma \Rightarrow \bigcup _ { n = 1 } ^ { \infty } A _ { n } \in \Sigma .$

Elements of Σ are called measurable sets. A function $f : X \to \mathbb { R }$ is measurable if $f ^ { - 1 } ( ( - \infty , t ] ) \in \Sigma$ for all $t \in \mathbb { R }$ . In practice, $X = \mathbb { R } ^ { d }$ and Σ is the Borel σ-algebra $B ( \mathbb { R } ^ { d } )$ generated by open sets.

## 4.2.2 Abstract measures

An abstract measure on (X, Σ) is a map $\mu : \Sigma  [ 0 , \infty ]$ such that

$\mu ( \emptyset ) = 0$ , and

• (countable additivity) if $\left\{ A _ { n } \right\}$ are pairwise disjoint measurable sets, then

$$
\mu \left(\bigcup_ {n = 1} ^ {\infty} A _ {n}\right) = \sum_ {n = 1} ^ {\infty} \mu (A _ {n}).
$$

A triple $( X , \Sigma , \mu )$ is a measure space. A measure is finite if $\mu ( X ) < \infty ,$ and σ-finite if X can be covered by countably many measurable sets of finite measure.

Important examples include:

• Lebesgue measure dx on $\mathbb { R } ^ { d }$ , capturing “volume”.

• Counting measure on a countable set, where $\mu ( A ) = | A |$

• Dirac measure $\delta _ { x }$ at $x \in X$ , defined by $\delta _ { x } ( A ) = \mathbf { 1 } _ { A } ( x )$ . This is useful for empirical measures in learning:

$$
\hat {\mu} _ {n} = \frac {1}{n} \sum_ {i = 1} ^ {n} \delta_ {x _ {i}}.
$$

• Probability measures: measures with $\mu ( X ) = 1$

## 4.2.3 Signed measures

In optimization and Fourier analysis, it is often natural to consider measures that can take negative values (e.g., diferences of probability measures). A signed measure on $( X , \Sigma )$ is a function $\nu : \Sigma $ $\mathbb { R } \cup \{ \pm \infty \}$ that is countably additive and satisfies $\nu ( \emptyset ) = 0$ , with the convention that ν does not take both +∞ and −∞.

Key examples include:

• the diference of two finite measures $\nu = \mu _ { 1 } - \mu _ { 2 }$ 2

• the centered empirical measure ${ \hat { \mu } } _ { n } - \mu .$ , which appears in generalization bounds.

A central structural result is the Hahn decomposition: there exist disjoint measurable sets $P , N$ with $P \cup N = X$ such that $\nu ( A ) \geq 0$ for all $A \subseteq P$ and $\nu ( A ) \leq 0$ for all $A \subseteq N$ . From this one obtains the Jordan decomposition:

$$
\nu = \nu^ {+} - \nu^ {-},
$$

where $\nu ^ { + } , \nu ^ { - }$ are mutually singular finite measures (on appropriate σ-finite spaces) representing the positive and negative parts of ν.

## 4.2.4 Total variation of signed measures

The total variation measure $| \nu |$ of a signed measure ν quantifies its “mass ignoring sign.” There are two equivalent definitions:

Partition definition.

$$
| \nu | (A) = \sup \left\{\sum_ {i = 1} ^ {\infty} | \nu (A _ {i}) |: A = \bigsqcup_ {i = 1} ^ {\infty} A _ {i}, A _ {i} \in \Sigma \right\}.
$$

Jordan decomposition definition. If $\nu = \nu ^ { + } - \nu ^ { - }$ <sup>−</sup>, then

$$
| \nu | = \nu^ {+} + \nu^ {-}.
$$

The total variation norm of ν is

$$
\| \nu \| _ {\mathrm{TV}} := | \nu | (X).
$$

Basic facts (for finite signed measures) include:

$\| \nu \| _ { \mathrm { T V } } = 0$ if and only if $\nu = 0$

$| \nu ( A ) | \leq | \nu | ( A )$ for all A.

• If $\nu = \mu _ { 1 } - \mu _ { 2 }$ for probability measures $\mu _ { 1 } , \mu _ { 2 }$ , then $\| \nu \| _ { \mathrm { T V } } \leq 2$

Many texts use the total variation distance

$$
d _ {\mathrm{TV}} \left(\mu_ {1}, \mu_ {2}\right) := \sup _ {A \in \Sigma} \left| \mu_ {1} (A) - \mu_ {2} (A) \right| = \frac {1}{2} \| \mu_ {1} - \mu_ {2} \| _ {\mathrm{TV}}.
$$

This distance controls the worst-case discrepancy over events and shows up in distribution shift and hypothesis testing.

A useful dual characterization links variation to bounded test functions:

$$
\| \nu \| _ {\mathrm{TV}} = \sup \left\{\int \varphi d \nu : \varphi \text {measurable,} | \varphi | \leq 1 \right\}.
$$

This viewpoint is the measure-theoretic ancestor of integral probability metrics (IPMs), Wassersteintype distances, and adversarial objectives.

## 4.2.5 Fourier transform of measures

Fourier methods appear in kernels, random features, spectral bias analyses, and distribution embeddings. Measure theory lets us define Fourier transforms even for objects that are not functions (e.g., discrete or singular distributions).

Let $\mu$ be a finite (complex or signed) measure on $\mathbb { R } ^ { d } .$ . Its Fourier transform (also called its characteristic function in probability) is the bounded continuous function

$$
\widehat {\mu} (\xi) := \int_ {\mathbb {R} ^ {d}} e ^ {- i \xi \cdot x} d \mu (x), \qquad \xi \in \mathbb {R} ^ {d}.
$$

Examples:

• If $\mu = \delta _ { x _ { 0 } }$ , then ${ \widehat { \mu } } ( \xi ) = e ^ { - i \xi \cdot x _ { 0 } }$

$\operatorname { I f } \mu$ has density $f \in L ^ { 1 } ( \mathbb { R } ^ { d } )$ with respect to Lebesgue measure $( \mathrm { i . e . , ~ } d \mu ( x ) = f ( x ) d x )$ , then $\widehat { \mu }$ reduces to the usual Fourier transform $\begin{array} { r } { \widehat { f } ( \xi ) = \int e ^ { - i \xi \cdot x } f ( x ) d x } \end{array}$

• For an empirical measure $\begin{array} { r } { \hat { \mu } _ { n } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \delta _ { x _ { j } } } \end{array}$

$$
\widehat {\hat {\mu} _ {n}} (\xi) = \frac {1}{n} \sum_ {j = 1} ^ {n} e ^ {- i \xi \cdot x _ {j}},
$$

which connects directly to random Fourier features and spectral estimators.

A useful bound ties Fourier transforms to total variation:

$$
| \widehat {\mu} (\xi) | \leq \int d | \mu | (x) = | \mu | (\mathbb {R} ^ {d}) = \| \mu \| _ {\mathrm{TV}}.
$$

Thus finite variation ensures the Fourier transform is well-defined and uniformly bounded.

In probability, if $\mu$ is a probability measure, then $\widehat \mu ( 0 ) = 1$ and $\widehat { \mu }$ is positive definite. Conversely, under standard conditions, $\widehat { \mu }$ uniquely determines $\mu$ (an identification that underlies kernel mean embeddings, moment problems, and certain generative modeling perspectives).

## 4.3 Concepts in Probability

## 4.3.1 Inequalities

Theorem 4.5 (Markov’s inequality) Let $\xi$ be a nonnegative random variable. Then

$$
\mathbb {P} (\xi > C) \leq \frac {\mathbb {E} [ \xi ]}{C}
$$

for any $C > 0$

Theorem 4.6 (Hoefding’s inequality) Let $\xi _ { 1 } , \ldots , \xi _ { n }$ be independent bounded random variables with $\xi _ { i } \in [ a , b ]$ for all i. Then

$$
\mathbb {P} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} (\xi_ {i} - \mathbb {E} [ \xi_ {i} ]) \geq C\right) \leq \exp \left(- \frac {2 n C ^ {2}}{(b - a) ^ {2}}\right)
$$

and

$$
\mathbb {P} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} (\xi_ {i} - \mathbb {E} [ \xi_ {i} ]) \leq - C\right) \leq \exp \left(- \frac {2 n C ^ {2}}{(b - a) ^ {2}}\right)
$$

for any $C > 0$

## Bibliography

[1] A. R. Barron. Universal approximation bounds for superpositions of a sigmoidal function. IEEE Trans. Inform. Theory, 39:930–945, 1993.

[2] J. Duchi, E. Hazan, and Y. Singer. Adaptive subgradient methods for online learning and stochastic optimization. J. Mach. Learn. Res, 12:2121––2159, 2011.

[3] W. E, C. Ma, and L. Wu. The barron space and the flow-induced function spaces for neural network models. Constr. Approx., 55:369–406, 2022.

[4] W. E, C. Ma, L. Wu, and S. Wojtowytsch. Towards a mathematical understanding of neural network-based machine learning: what we know and what we don’t. CSIAM Trans. Appl. Math., 1(4):561–614, 2020.

[5] W. E and S. Wojtowytsch. Kolmogorov width decay and poor approximators in machine learning: Shallow neural networks, random feature models and neural tangent kernels. Res. Math. Sci., 8(1):1–28, 2021.

[6] X. Glorot and Y. Bengio. Understanding the dificulty of training deep feedforward neural networks. In Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, volume 9, pages 249–256, 2010.

[7] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 770–778, 2016.

[8] D. P. Kingma and J. Ba. Adam: a method for stochastic optimization. https://arxiv.org/abs/1412.6980, 2014.

[9] Z. Li, C. Ma, and L. Wu. Complexity measures for neural networks with general activation functions using path-based norms. https://arxiv.org/abs/2009.06132, 2020.

[10] J. Lu, Z. Shen, H. Yang, and S. Zhang. Deep network approximation for smooth functions. SIAM J. Math. Anal., 53(5):5465–5506, 2021.

[11] Y. A. Nesterov. A method of solving a convex programming problem with convergence rate o(1/ k). Sov. Math. Dokl, 27:372–376, 1983.

[12] B. T. Polyak. Some methods of speeding up the convergence of iteration methods. USSR Comput. Math. Math. Phys., 4(5):1–17, 1964.

[13] Z. Shen, H. Yang, and S. Zhang. Deep network approximation characterized by number of neurons. https://arxiv.org/abs/1906.05497, 2020.

[14] Z. Shen, H. Yang, and S. Zhang. Deep network with approximation error being reciprocal of width to power of square root of depth. Neural Comput., 33(4):1005–1036, 2021.

[15] J. W. Siegel and J. Xu. Approximation rates for neural networks with general activation functions. Neural Netw., 128:313–321, 2020.

[16] J. W. Siegel and J. Xu. High-order approximation rates for shallow neural networks with cosine and relu<sup>k</sup> activation functions. Appl. Comput. Harmon. Anal., 58:1–26, 2022.

[17] S. Wang and X. Sun. Generalization of hinging hyperplanes. IEEE Trans. Inform. Theory, 51:4425–4431, 2005.

[18] S. Zhang, Z. Shen, and H. Yang. Deep network approximation: Achieving arbitrary accuracy with fixed number of neurons. J. Mach. Learn. Res., 23(276):1–60, 2022.