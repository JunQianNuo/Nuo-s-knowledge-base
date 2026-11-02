---
raw_title: 数值分析05SymmetricPositiveDefiniteLinearSystem
subject: 数值分析05SymmetricPositiveDefiniteLinearSystem
source: 数值分析05SymmetricPositiveDefiniteLinearSystem.pptx
status: mineru解析
parser: mineru
---

## 对称正定线性方程组的解法

- 对称正定矩阵的定义和性质
- Cholesky分解
- 梯度（最速）下降法
- 共轭方向法：共轭梯度法

## 对称正定矩阵

- 定义：如果 $A^{T}=A$ ，则 $n\times n$ 矩阵 $A$ 是对称矩阵。
- 定义： $A$ 是 $n$ 阶方阵，如果 $\forall x\in \mathbb{R}^{n},x\ne 0,$ 有 $x^{T}Ax>0,$ **则** $A$ 是正定矩阵。
- 例：

$A=\left[\begin{matrix}2&2\\2&5\end{matrix}\right]$

$A=\left[\begin{matrix}2&4\\4&5\end{matrix}\right]$

正定非正定

## 对称正定矩阵

- 性质1：对称正定矩阵非奇异(可逆)
- 性质2：任何对称正定矩阵的主子式也是对称正定矩阵。
- 性质3：如果 $A$ 是对称矩阵，则 $A$ 是正定矩阵的充要条件是其所有特征值是正数。
- 性质4：如果 $A$ 是 $n\times n$ 对称正定矩阵, $P$ 是一个满秩的 $n\times m$ 矩阵（ $n\geq m$ ），则 $P^{T}AP$ 是 $m\times m$ 对称正定矩阵。

## Cholesky分解

- 引理1：两个上（下）三角阵相乘是上（下）三角阵。

- 引理2：上（下）三角阵的逆是上（下）三角阵。

$L^{-1}=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]^{-1}=L^{*}?$

## Cholesky分解

- $LDL^{T}$ 分解定理： $A$ 是实对称非奇异矩阵，并存在 $LU$ 分解，则它可以分解为 $A=LDL^{T}$ ，其中 $L$ 是下三角阵。

- Cholesky分解定理： $A$ 是实对称正定矩阵，则它可以分解为 $A=LL^{T}$ ,其中 $L$ 是下三角阵。

André-Louis Cholesky,1875-1918

## Cholesky分解

- 怎么分解？

$\left[\begin{matrix}a_{11}&a_{21}&a_{31}&\ldots &a_{n1}\\a_{21}&a_{22}&a_{32}&\ldots &a_{n2}\\a_{31}&a_{32}&a_{33}&\ldots &a_{n3}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}l_{11}&l_{21}&l_{31}&\ldots &l_{n1}\\0&l_{22}&l_{32}&\ldots &l_{n2}\\0&0&l_{33}&\ldots &l_{n3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{ij}=\sum_{s=1}^{s=n}l_{is}u_{sj}=\sum_{s=1}^{s=min (i,j)}l_{is}l_{js}$

$(n^{2}+n)/2$ 个方程， $(n^{2}+n)/2$ 个未知数

## Cholesky分解

$\left[\begin{matrix}a_{11}&a_{21}&a_{31}&\ldots &a_{n1}\\a_{21}&a_{22}&a_{32}&\ldots &a_{n2}\\a_{31}&a_{32}&a_{33}&\ldots &a_{n3}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}l_{11}&l_{21}&l_{31}&\ldots &l_{n1}\\0&l_{22}&l_{32}&\ldots &l_{n2}\\0&0&l_{33}&\ldots &l_{n3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{11}=\sum_{s=1}^{s=min (1,1)}l_{1s}l_{s1}=l_{11}^{2}\rightarrow l_{11}$

$a_{i1}=\sum_{s=1}^{s=min (i,1)}l_{is}l_{1s}=l_{i1}l_{11}\rightarrow l_{i1} \left(2\leq i\leq n\right)$

## Cholesky分解

$\left[\begin{matrix}a_{11}&a_{21}&a_{31}&\ldots &a_{n1}\\a_{21}&a_{22}&a_{32}&\ldots &a_{n2}\\a_{31}&a_{32}&a_{33}&\ldots &a_{n3}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}l_{11}&l_{21}&l_{31}&\ldots &l_{n1}\\0&l_{22}&l_{32}&\ldots &l_{n2}\\0&0&l_{33}&\ldots &l_{n3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{22}=\sum_{s=1}^{s=min (2,2)}l_{2s}l_{2s}=l_{21}^{2}+l_{22}^{2}\rightarrow l_{22}$

$a_{i2}=\sum_{s=1}^{s=min (i,2)}l_{is}l_{2s}=l_{i1}l_{21}+l_{i2}l_{22}\rightarrow l_{i2} \left(3\leq i\leq n\right)$

## Cholesky分解

$\left[\begin{matrix}a_{11}&a_{21}&a_{31}&\ldots &a_{n1}\\a_{21}&a_{22}&a_{32}&\ldots &a_{n2}\\a_{31}&a_{32}&a_{33}&\ldots &a_{n3}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\\vdots &\ddots &0&\ldots &0\\l_{k-1,1}&\ldots &l_{k-1,k-1}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&\ldots &l_{n,k-1}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}l_{11}&\ldots &l_{k-1,1}&\ldots &l_{n1}\\0&\ddots &\vdots &\ldots &\vdots \\0&0&l_{k-1,k-1}&\ldots &l_{n,k-1}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &l_{nn}\end{matrix}\right]$

$a_{kk}=\sum_{s=1}^{s=min (k,k)}l_{ks}l_{ks}=\sum_{s=1}^{k-1}l_{ks}^{2}+l_{kk}^{2}\rightarrow l_{kk}$

$a_{ik}=\sum_{s=1}^{s=min (i,k)}l_{is}l_{ks}=\sum_{s=1}^{k-1}l_{is}l_{ks}+l_{ik}l_{kk}\rightarrow l_{ik} (k<i\leq n)$

## Cholesky分解

- $A=LL^{T}$ 分解过程( $A$ 对称正定)

$\left[\begin{matrix}a_{11}&a_{21}&a_{31}&\ldots &a_{n1}\\a_{21}&a_{22}&a_{32}&\ldots &a_{n2}\\a_{31}&a_{32}&a_{33}&\ldots &a_{n3}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}l_{11}&l_{21}&l_{31}&\ldots &l_{n1}\\0&l_{22}&l_{32}&\ldots &l_{n2}\\0&0&l_{33}&\ldots &l_{n3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

求解顺序: $l_{11}\rightarrow l_{i1}\rightarrow l_{22}\rightarrow l_{i2}\rightarrow \ldots \rightarrow l_{nn}$

显式求解：

$l_{kk}=\left(a_{kk}-\sum_{s=1}^{k-1}l_{ks}^{2}\right)^{1/2}$

$l_{ik}=\left(a_{ik}-\sum_{s=1}^{k-1}l_{is}l_{ks}\right)/l_{kk}$

## Cholesky分解

- 例：

$A=\left[\begin{matrix}4&-2&2\\-2&2&-4\\2&-4&11\end{matrix}\right]=LL^{T}=\left[\begin{matrix}l_{11}&0&0\\l_{21}&l_{22}&0\\l_{31}&l_{32}&l_{33}\end{matrix}\right]\left[\begin{matrix}l_{11}&l_{21}&l_{31}\\0&l_{22}&l_{32}\\0&0&l_{33}\end{matrix}\right]$

$=\left[\begin{matrix}l_{11}^{2}&l_{11}l_{21}&l_{11}l_{31}\\l_{21}l_{11}&l_{21}^{2}+l_{22}^{2}&l_{21}l_{31}+l_{22}l_{32}\\l_{31}l_{11}&l_{31}l_{21}+l_{32}l_{22}&l_{31}^{2}+l_{32}^{2}+l_{33}^{2}\end{matrix}\right]$

$L=\left[\begin{matrix}2&0&0\\-1&1&0\\1&-3&1\end{matrix}\right]$

## Cholesky分解直接Cholesky分解的伪代码

![](images/2fab8ca0fedd86747dcb51f1540c6c438d1ee6f20e0d695096ce83a114f96a33.jpg)

$k-1次$ 乘法， $k-1次$ 减法，1次开方

$k-1次$ 乘法， $k-1次$ 减法，1次除法求解顺序: $l_{11}\rightarrow l_{i1}\rightarrow l_{22}\rightarrow l_{i2}\rightarrow \ldots \rightarrow l_{nn}$

$\sum_{k=1}^{n}\left[\left(2k-1\right)\left(n-k+1\right)\right]=\frac{1}{3}n^{3}+\frac{1}{2}n^{2}+\frac{1}{6}n$

总计算量=

## Cholesky分解

- 例： $A=\left[\begin{matrix}4&-2&2\\-2&2&-4\\2&-4&11\end{matrix}\right]$ 的Cholesky分解？

## 梯度下降法

- 二次型引理：若 $A$ 是 $n$ 阶对称正定方阵，则求解 $Ax=b$ 等价于极小化二次型问题（优化问题）

$arg\min_{x\in \mathbb{R}^{n}}q\left(x\right)=\frac{1}{2}\left⟨x,Ax\right⟩-\left⟨x,b\right⟩$

其中 $\left⟨x,y\right⟩=x^{T}y.$

## 梯度下降法

- 二次型引理引出的一类迭代法：在第 $k$ 步确定合适的搜索方向 $v_{k}$ ,进行一次迭代

$x_{k+1}=x_{k}+t_{k}v_{k}$

$t_{k}=\frac{\left⟨r_{k},v_{k}\right⟩}{\left⟨v_{k},Av_{k}\right⟩},$ 残差向量： $r_{k}=b-Ax_{k}$

- 迭代的性质： $\left⟨r_{k+1},v_{k}\right⟩=0$

- 梯度（最速）下降法，取负梯度方向

$v_{k}=-\nabla q\left(x_{k}\right)=b-Ax_{k}$

## 梯度下降法

- 梯度下降法的几何解释

$x_{0}$

$x_{2}$

$x_{4}$

$x_{3}$

$x_{1}$

## 梯度下降法

- 梯度下降法伪代码：

$\mathbf{i}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{g}\mathbf{e}\mathbf{r} k,k_{max}; \mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} t$

$\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \mathbf{a}\mathbf{r}\mathbf{r}\mathbf{a}\mathbf{y} \left(a_{ij}\right)_{1:n\times 1:n},b_{1:n},x_{1:n},y_{1:n}, x_{1:n}^{\left(0\right)},v_{1:n},w_{1:n}$

$x\leftarrow x^{(0)}$

$v=b-Ax$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} k_{max} \mathbf{d}\mathbf{o}$

$w\leftarrow Av$

$t=\left⟨v,v\right⟩/\left⟨v,w\right⟩$

$x\leftarrow x+tv$

$v\leftarrow v-tw$

$\mathbf{i}\mathbf{f} \left\|v\right\|<TOL \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n}$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t} 'convergence'$

$\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- 梯度下降算法

$x_{k+1}=x_{k}+t_{k}v_{k}$

$t_{k}=\frac{\left⟨r_{k},v_{k}\right⟩}{\left⟨v_{k},Av_{k}\right⟩}$

$v_{k}=r_{k}=b-Ax_{k}$

迭代法则收敛判别

## 梯度下降法

- 例：

$\left[\begin{matrix}2&2\\2&5\end{matrix}\right]\left[\begin{array}{c}u\\v\end{array}\right]=\left[\begin{array}{c}6\\3\end{array}\right], u=4,v=-1$

$x_{0}=\left[0,0\right]^{T},v_{0}=b-Ax_{0}=\left[6,3\right]^{T},Av_{0}=\left[18,27\right]^{T}$

$t_{0}=\frac{\left⟨v_{0},v_{0}\right⟩}{\left⟨v_{0},Av_{0}\right⟩}=\frac{45}{189}=\frac{5}{21}$

$x_{1}=x_{0}+t_{0}v_{0}=\left[\frac{10}{7},\frac{5}{7}\right]^{T}$

$v_{1}=v_{0}-tAv_{0}=\left[\frac{12}{7},-\frac{24}{7}\right]^{T}$

## 梯度下降法

$v$

$u$

$k$

$v$

$u$

$k$

![](images/105fcb91a1e9cb5424746f85ad94c0fc4751e044a1bb0c53608635f0ac1feae3.jpg)

![](images/105fcb91a1e9cb5424746f85ad94c0fc4751e044a1bb0c53608635f0ac1feae3.jpg)

梯度下降法

$v$

$u$

$k$

![](images/798056ee896fccd091fb7d87b3620196eef9e69a71e1e29492f0dbb1f113e9a0.jpg)

Gauss-Seidel

## 梯度下降法

$v$

![](images/e4683bd6988a1fb9150e644bb2e778b58b6e26c0e97c105e1c9b2677b5279894.jpg)

![](images/691b58b63f005821adb6024eaf4b100e101e42b14020f052de0faef2f7d5907e.jpg)

$u$

迭代收敛路径

$q\left(u,v\right)$ 的等值线及梯度下降的路径

## 共轭方向法

- $A$ 共轭（ $A$ 正交）的定义：A是n阶对称正定方阵，对两个 $n$ 维向量定义内积

$\left⟨v,w\right⟩_{A}=v^{T}Aw$

当 $\left⟨v,w\right⟩_{A}=0$ 时， $v$ 和 $w$ 为 $A$ 共轭。

- $A$ 正交系的定义： $A$ 是 $n$ 阶对称正定方阵，如果向量组 $\{u_{1},u_{2},\ldots ,u_{n}\}$ 满足 $\left⟨u_{i}, u_{j}\right⟩_{A}=\left\{\begin{array}{c}0,     i\ne j\\d_{i}>0, i=j\end{array}\right. \left(1\leq i,j\leq n\right)$ ，则称 $\{u_{1},u_{2},\ldots ,u_{n}\}$ 为 $A$ -正交系 $。$
- $A$ 标准正交系的定义： $A$ 是 $n$ 阶对称正定方阵，如果向量组 $\{v_{1},v_{2},\ldots ,v_{n}\}$ 满足 $\left⟨v_{i}, v_{j}\right⟩_{A}=\delta _{ij} \left(0\leq i,j\leq n\right)$ ，则称 $\{v_{1},v_{2},\ldots ,v_{n}\}$ 为 $A$ -标准正交系 $。$
- $\{u_{1},u_{2},\ldots ,u_{n}\}$ 和 $\{v_{1},v_{2},\ldots ,v_{n}\}$ 均是 $\mathbb{R}^{n}$ 的线性无关向量组。

## 共轭方向法

- $A$ -正交系迭代定理：假设 $A$ 是 $n$ 阶对称正定方阵， $\{u_{1},u_{2},\ldots ,u_{n}\}$ 是一组 $A$ -正交系，即 $\left⟨u_{i}, u_{j}\right⟩_{A}=d_{i}\delta _{ij} \left(1\leq i,j\leq n\right)。$

定义迭代： $x_{k}=x_{k-1}+\left(\frac{\left⟨b-Ax_{k-1},u_{k}\right⟩}{\left⟨u_{k},u_{k}\right⟩_{A}}\right)u_{k}\left(1\leq k\leq n\right)$ , 对于任意初始向量 $x_{0}\in R^{n}$ ,通过迭代可以得到 $Ax_{n}=b$ .

- $A$ -标准正交系迭代定理：假设 $A$ 是 $n$ 阶对称正定方阵， $\{v_{1},v_{2},\ldots ,v_{n}\}$ 是一组 $A$ -标准正交系， $即\left⟨v_{i},v_{j}\right⟩_{A}=\delta _{ij} \left(1\leq i,j\leq n\right)。$

定义迭代： $x_{k}=x_{k-1}+\left⟨b-Ax_{k-1},v_{k}\right⟩v_{k}\left(1\leq k\leq n\right)$ , 对于任意初始向量 $x_{0}\in R^{n}$ , 通过迭代可以得到 $Ax_{n}=b$ .

## 共轭方向法

- 格拉姆-施密特正交化构造 $A$ 正交系：

1. 取标准单位向量组 $\{e_{1},\ldots ,e_{n}\}$
2. 取 $u_{1}=e_{1}$
3. 令 $u_{2}=e_{2}-\beta _{21}u_{1}, \beta _{21}=\frac{\left⟨e_{2},u_{1}\right⟩_{A}}{\left⟨u_{1}, u_{1}\right⟩_{A}}$
4. 令 $u_{k}=e_{k}-\beta _{k1}u_{1}\ldots -\beta _{k,k-1}u_{k-1} (2\leq k\leq n)$

$\beta _{km}=\frac{\left⟨e_{k},u_{m}\right⟩_{A}}{\left⟨u_{m},u_{m}\right⟩_{A}} (1\leq i\leq k-1)$

- 格拉姆-施密特正交化构造 $A$ 标准正交系：

1. 取标准单位向量组 $\{e_{1},\ldots ,e_{n}\}$
2. 取 $v_{1}=\frac{e_{1}}{\sqrt{\left⟨e_{1}, e_{1}\right⟩_{A}}}$
3. 令 $u_{2}=e_{2}-\beta _{21}v_{1}, \beta _{21}=\left⟨e_{2},v_{1}\right⟩_{A},v_{2}=\frac{u_{2}}{\sqrt{\left⟨u_{2}, u_{2}\right⟩_{A}}}$
4. 令 $u_{k}=e_{k}-\beta _{k1}v_{1}\ldots -\beta _{k,k-1}v_{k-1} (2\leq k\leq n)$

$\beta _{km}=\left⟨e_{k},v_{m}\right⟩_{A}(1\leq i\leq k-1)$

$v_{k}=\frac{u_{k}}{\sqrt{\left⟨u_{k},u_{k}\right⟩_{A}}}$

## 共轭方向法

- 例：使用共轭方向法求解 $\left[\begin{matrix}2&2\\2&5\end{matrix}\right]\left[\begin{array}{c}u\\v\end{array}\right]=\left[\begin{array}{c}6\\3\end{array}\right]$

1、构造A正交系 $u_{1}=e_{1}=\left[\begin{array}{c}1\\0\end{array}\right]$ , $u_{2}=e_{2}-\frac{\left⟨e_{2},u_{1}\right⟩_{A}}{\left⟨u_{1},u_{1}\right⟩_{A}}u_{1}=\left[\begin{array}{c}0\\1\end{array}\right]-\left[\begin{array}{c}1\\0\end{array}\right]=\left[\begin{array}{c}-1\\1\end{array}\right]$

2、迭代 $x_{0}=\left[\begin{array}{c}0\\0\end{array}\right]$

$x_{1}=x_{0}+\frac{\left⟨b-Ax_{0},u_{1}\right⟩}{\left⟨u_{1},u_{1}\right⟩_{A}}u_{1}=\left[\begin{array}{c}0\\0\end{array}\right]+3\left[\begin{array}{c}1\\0\end{array}\right]=\left[\begin{array}{c}3\\0\end{array}\right]$

$x_{2}=x_{1}+\frac{\left⟨b-Ax_{1},u_{2}\right⟩}{\left⟨u_{2},u_{2}\right⟩_{A}}u_{2}=\left[\begin{array}{c}3\\0\end{array}\right]-\left[\begin{array}{c}-1\\1\end{array}\right]=\left[\begin{array}{c}4\\-1\end{array}\right]$

## 共轭方向法

$v$

$v$

![](images/e4683bd6988a1fb9150e644bb2e778b58b6e26c0e97c105e1c9b2677b5279894.jpg)

![](images/535332b0c21c1bf2ed4b73b645c1e36471a7fd505357e70070803e061f1a0fb5.jpg)

$u$

$u$

共轭方向的路径梯度下降的路径

- 共轭方向法具体算法：

$\mathbf{i}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{g}\mathbf{e}\mathbf{r} k,m,n; \mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} t$

$\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \mathbf{a}\mathbf{r}\mathbf{r}\mathbf{a}\mathbf{y} \left(a_{ij}\right)_{1:n\times 1:n},\left(v_{ij}\right)_{1:n\times 1:n},$

$\left(w_{ij}\right)_{1:n\times 1:n},b_{1:n},x_{1:n}, x_{1:n}^{\left(0\right)},r_{1:n}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} n \mathbf{d}\mathbf{o}$

$v_{k}\leftarrow e_{k}$

$\mathbf{f}\mathbf{o}\mathbf{r} m=1 \mathbf{t}\mathbf{o} k-1 \mathbf{d}\mathbf{o}$

$t=\left⟨e_{k},w_{m}\right⟩$

$v_{k}\leftarrow v_{k}-tv_{m}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$w_{k}\leftarrow Av_{k}$

$t=\sqrt{\left⟨v_{k},w_{k}\right⟩}$

$v_{k}\leftarrow v_{k}/t$

$w_{k}\leftarrow w_{k}/t$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

施密特正交化

$x\leftarrow x^{(0)}$

$r=b-Ax$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} n \mathbf{d}\mathbf{o}$

$t=\left⟨r,v_{k}\right⟩$

$x\leftarrow x+tv_{k}$

$r\leftarrow r-tw_{k}$

$\mathbf{i}\mathbf{f} \left\|r\right\|<TOL \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n}$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t} 'convergence'$

$\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

优化迭代法则不追求精确解

- 共轭梯度算法：

$x_{0}=initial guess$

$v_{0}=r_{0}=b-Ax_{0}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=0 \mathbf{t}\mathbf{o} n-1 \mathbf{d}\mathbf{o}$

$\mathbf{i}\mathbf{f} r_{k}=0, \mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}, \mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$t_{k}=\frac{\left⟨r_{k},v_{k}\right⟩}{\left⟨v_{k}, v_{k}\right⟩_{A}}= \frac{\left⟨r_{k},r_{k}\right⟩}{\left⟨v_{k}, v_{k}\right⟩_{A}}$

$x_{k+1}=x_{k}+t_{k}v_{k}$

$r_{k+1}=r_{k}-t_{k}Av_{k}$

$s_{k}=-\frac{\left⟨v_{k},r_{k+1}\right⟩_{A}}{\left⟨v_{k}, v_{k}\right⟩_{A}}=\frac{\left⟨r_{k+1},r_{k+1}\right⟩}{\left⟨r_{k},r_{k}\right⟩}$

$v_{k+1}=r_{k+1}+s_{k}v_{k}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- **定理**：令 $A$ 为 $n\times n$ 的对称正定矩阵， $b$ 是非零向量。在求解 $Ax=b$ 的共轭梯度法中，假设 $r_{k}\ne 0$ ,其中 $k<n$ (如果 $r_{k}=0，$ 方程已求解)。则对于每个 $1\leq k\leq n$ 有：

（a） $\mathbb{R}^{n}$ 的两个子空间等价(相互线性表示)：

$\left\{r_{0},\ldots ,r_{k-1}\right\}\Longleftrightarrow \left\{v_{0},\ldots ,v_{k-1}\right\}$

（b）余项 $r_{k}$ 两两正交 $\left⟨r_{k},r_{j}\right⟩=0$ ，其中 $j<k$

（c）搜索方向 $v_{k}$ 两两 $A$ 共轭 $\left⟨v_{k},v_{j}\right⟩_{A}=0$ ，其中 $j<k$

极小化 $q$

搜索方向共轭：

$\left⟨v_{k}, v_{k+1}\right⟩_{A}=0$

## 共轭梯度法

- 例：使用共轭梯度法求解 $\left[\begin{matrix}2&2\\2&5\end{matrix}\right]\left[\begin{array}{c}u\\v\end{array}\right]=\left[\begin{array}{c}6\\3\end{array}\right]$

1、 $x_{0}=\left[\begin{array}{c}0\\0\end{array}\right]$ , $r_{0}=v_{0}=\left[\begin{array}{c}6\\3\end{array}\right]$

*2、* $t_{0}=\frac{\left⟨r_{0},r_{0}\right⟩}{\left⟨v_{0},Av_{0}\right⟩}=\frac{5}{21},  x_{1}=x_{0}+t_{0}v_{0}=$  $\left[\begin{array}{c}0\\0\end{array}\right]+\frac{5}{21}\left[\begin{array}{c}6\\3\end{array}\right]=\left[\begin{array}{c}\frac{10}{7}\\\frac{5}{7}\end{array}\right]$

$r_{1}=r_{0}-t_{0}Av_{0}=\left[\begin{array}{c}6\\3\end{array}\right]-\frac{5}{21}\left[\begin{matrix}2&2\\2&5\end{matrix}\right]\left[\begin{array}{c}6\\3\end{array}\right]=\left[\begin{array}{c}\frac{12}{7}\\-\frac{24}{7}\end{array}\right]$

## 共轭梯度法

$s_{0}=\frac{\left⟨r_{1},r_{1}\right⟩}{\left⟨r_{0},r_{0}\right⟩}=\frac{16}{49}$

$v_{1}=r_{1}+s_{0}v_{0}=\left[\begin{array}{c}\frac{12}{7}\\-\frac{24}{7}\end{array}\right]+\frac{16}{49}\left[\begin{array}{c}6\\3\end{array}\right]=\left[\begin{array}{c}\frac{180}{49}\\-\frac{120}{49}\end{array}\right]$

3、 $x_{2}=x_{1}+\frac{\left⟨r_{1},r_{1}\right⟩}{\left⟨v_{1},Av_{1}\right⟩}v_{1}=\left[\begin{array}{c}\frac{10}{7}\\\frac{5}{7}\end{array}\right]+\frac{7}{10}\left[\begin{array}{c}\frac{180}{49}\\-\frac{120}{49}\end{array}\right]=\left[\begin{array}{c}4\\-1\end{array}\right]$

## 共轭梯度法

$v$

$v$

$v$

![](images/3ddb47eecf8b63f796023b16cb59e5cd88aeca9081d91e8d00b6981062d1c935.jpg)

![](images/e4683bd6988a1fb9150e644bb2e778b58b6e26c0e97c105e1c9b2677b5279894.jpg)

![](images/535332b0c21c1bf2ed4b73b645c1e36471a7fd505357e70070803e061f1a0fb5.jpg)

$u$

$u$

$u$

梯度下降的路径共轭方向的路径共轭梯度的路径

## 共轭梯度法

- 稀疏矩阵求解，精确解为 $\left[0,1,2,\ldots ,n-1\right]$

![](images/faf05224e42714e9595f2cce15b8dd6427dacc78c3b0ed352dd7feafd06de9b9.jpg)

## 共轭梯度法

- 稀疏矩阵求解：Gauss消元与Gauss-Seidel、共轭梯度对比迭代次数 $N_{iter}$ 随矩阵维度 $n$ 的变化 $\left(TOL=10^{-7}\right)$

<table>
  <tr>
    <th>$n$</th>
    <th>10</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
  </tr>
  <tr>
    <td>$Gauss-Seidel$</td>
    <td>28</td>
    <td>56</td>
    <td>64</td>
    <td>71</td>
    <td>78</td>
    <td>84</td>
    <td>91</td>
  </tr>
  <tr>
    <td>共轭梯度</td>
    <td>11</td>
    <td>34</td>
    <td>38</td>
    <td>42</td>
    <td>45</td>
    <td>49</td>
    <td>53</td>
  </tr>
</table>

计算时间随矩阵维度 $n$ 的变化 $\left(迭代取TOL=10^{-7}\right)$

<table>
  <tr>
    <th>$n$</th>
    <th>10</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
    <th>$10^$</th>
  </tr>
  <tr>
    <td>$Gauss$消元</td>
    <td>0s</td>
    <td>0.001s</td>
    <td>1.02s</td>
    <td>1483.46s</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Gauss-Seidel迭代</td>
    <td>0s</td>
    <td>0s</td>
    <td>0.002s</td>
    <td>0.02s</td>
    <td>0.20s</td>
    <td>2.73s</td>
    <td>22.65s</td>
  </tr>
  <tr>
    <td>共轭梯度</td>
    <td>0s</td>
    <td>0s</td>
    <td>0.002s</td>
    <td>0.0019s</td>
    <td>0.18s</td>
    <td>1.91s</td>
    <td>19.94s</td>
  </tr>
</table>

## 思考与练习

1. 判断下列矩阵是否正定，如果正定请给出Cholesky分解，否则给出 $LDL^{T}$ 分解，并进行回代求解：

$\left[\begin{matrix}4&-2&0\\-2&2&-1\\0&-1&5\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\end{array}\right]=\left[\begin{array}{c}0\\3\\-7\end{array}\right]$

2. 使用共轭方向法手动求解： $\left[\begin{matrix}2&2\\2&6\end{matrix}\right]\left[\begin{array}{c}u\\v\end{array}\right]=\left[\begin{array}{c}6\\10\end{array}\right]$

2. 编程实现梯度下降法及共轭梯度法，用程序求解第1题中的方程并对两种方法进行比较。