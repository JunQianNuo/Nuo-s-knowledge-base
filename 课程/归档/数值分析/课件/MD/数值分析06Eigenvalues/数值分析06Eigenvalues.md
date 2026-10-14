---
raw_title: 数值分析06Eigenvalues
subject: 数值分析06Eigenvalues
source: 数值分析06Eigenvalues.pptx
status: mineru解析
parser: mineru
---

## 矩阵特征值的数值解法

- 特征值的估计
- 幂法
- QR算法

## 特征值计算的用处

- $Ax=b$ 的迭代法收敛性可以用迭代矩阵的谱半径来判定
- 搜索引擎技术依赖于特征值问题
- 求解结构的固有频率

1940年刚通车4个月的美国塔科马海峡吊桥被微风吹垮

## 特征值的定义

- $A$ 是方阵， $Ax=\lambda x$ , $x$ 为非零向量，标量 $\lambda$ 称为 $A$ 的特征值。
- $Ax=\lambda x\rightarrow \left(A-\lambda I\right)x=0\rightarrow \left|A-\lambda I\right|=0$
- 例： $A=\left[\begin{matrix}1&3\\2&2\end{matrix}\right]$

$\left|\begin{matrix}1-\lambda &3\\2&2-\lambda \end{matrix}\right|=\lambda ^{2}-3\lambda -4=0$

$\lambda _{1}=4, \lambda _{2}=-1$

- 如何计算大型矩阵的特征值？
- 高次多项式求根属于病态问题，例：Wilkinson多项式 $W\left(x\right)=\left(x-1\right)\left(x-2\right)\ldots \left(x-20\right)$

Matlab求 $W\left(x\right)=0$ 在16附近的根

## 特征值的估计

- 盖尔(Gershgorin)圆盘定理： $n$ 阶方阵 $A$ 的谱（特征值集）包含在下列复平面中 $n$ 个圆盘 $C_{i}$ 的并

$C_{i}=\left\{z\in \mathbb{C}:\left|z-a_{ii}\right|\leq \sum_{j=1,j\ne i}^{n}|a_{ij}|\right\} (1\leq i\leq n)$

- 由于 $A^{T}$ 与 $A$ 具有相同的特征值，因此， $A$ 的谱同时包含在下列复平面中 $n$ 个圆盘 $D_{i}$ 的并

$D_{i}=\left\{z\in \mathbb{C}:\left|z-a_{ii}\right|\leq \sum_{k=1,k\ne i}^{n}|a_{ki}|\right\} (1\leq i\leq n)$

- 最终可以将 $A$ 的谱定位在下列圆盘集合

$\left(\bigcup_{i=1}^{n}C_{i}\right)\bigcap_{}^{}\left(\bigcup_{i=1}^{n}D_{i}\right)$

## 特征值的估计

- 例： $A=\left[\begin{matrix}4-i&2&i\\-1&2i&2\\1&-1&-5\end{matrix}\right]$

![](images/b773e74af223f9e406ec70276eaa586ecc5e2ab164364cad46d1869ec66ee6cf.jpg)

Gershgorin圆盘

\*代表特征值真实位置

## 特征值的估计

- 圆盘定理的用处？
- $Ax=b$ 问题：
    1. 帮助判定某些迭代法收敛性： $x_{k+1}=Gx_{k}+c$

Richardson迭代： $G=I-A$

Jacobi迭代： $G=-D^{-1}\left(L+U\right)$

1. 帮助判定某些矩阵的可逆性与正定性

![](images/dfa5338d87302a364b228f969296e26b2a5ec0d75b3c9eb10895f83fb6dfb016.png)

例：

## 特征值的估计

- 扰动矩阵特征值圆盘定理：若 $n$ 阶方阵 $A$ 用相似变换 $P^{-1}AP$ 对角化，而 $B$ 是任意 $n$ 阶方阵，则 $A+B$ 的特征值 $\mu$ 位于下列圆盘之并中：

$\left\{\mu \in \mathbb{C}:\left|\mu -\lambda _{i}\right|\leq cond_{\infty }\left(P\right)\left\|B\right\|_{\infty }\right\}$

其中 $\lambda _{i}$ 是 $A$ 的特征值， $cond_{\infty }\left(P\right)=\left\|P\right\|_{\infty }\left\|P^{-1}\right\|_{\infty }$ 是 $P$ 基于无穷范数的条件数。

## 幂法求特征值

- *引例：* $A=\left[\begin{matrix}1&3\\2&2\end{matrix}\right],\lambda _{1}=4, v_{1}=\left[1,1\right]^{T}, \lambda _{2}=-1, v_{2}=\left[-3,2\right]^{T}$

迭代：取向量 $x_{0}=\left[-5,5\right]^{T}$ 用 $A$ 反复作用于该向量

$x_{1}=Ax_{0}=\left[\begin{matrix}1&3\\2&2\end{matrix}\right]\left[\begin{array}{c}-5\\5\end{array}\right]=\left[\begin{array}{c}10\\0\end{array}\right]$

$x_{2}=A^{2}x_{0}=\left[\begin{matrix}1&3\\2&2\end{matrix}\right]\left[\begin{array}{c}10\\0\end{array}\right]=\left[\begin{array}{c}10\\20\end{array}\right]$

$x_{3}=A^{3}x_{0}=\left[\begin{matrix}1&3\\2&2\end{matrix}\right]\left[\begin{array}{c}10\\20\end{array}\right]=\left[\begin{array}{c}70\\60\end{array}\right]$

$x_{4}=A^{4}x_{0}=\left[\begin{matrix}1&3\\2&2\end{matrix}\right]\left[\begin{array}{c}70\\60\end{array}\right]=\left[\begin{array}{c}250\\260\end{array}\right]$

$=10\left[\begin{array}{c}1\\0\end{array}\right]$

$=20\left[\begin{array}{c}1/2\\1\end{array}\right]$

$=70\left[\begin{array}{c}1\\7/6\end{array}\right]$

$=260\left[\begin{array}{c}25/26\\1\end{array}\right]$

## 幂法求特征值

- 是否巧合？

$x_{0}=\left[\begin{array}{c}-5\\5\end{array}\right]=\left[\begin{array}{c}1\\1\end{array}\right]+2\left[\begin{array}{c}-3\\2\end{array}\right]$

$\lambda _{1}=4, v_{1}=\left[1,1\right]^{T}, \lambda _{2}=-1, v_{2}=\left[-3,2\right]^{T}$

$x_{1}=Ax_{0}=4\left[\begin{array}{c}1\\1\end{array}\right]-2\left[\begin{array}{c}-3\\2\end{array}\right]$

$x_{2}=A^{2}x_{0}=4^{2}\left[\begin{array}{c}1\\1\end{array}\right]+2\left[\begin{array}{c}-3\\2\end{array}\right]$

$x_{3}=A^{3}x_{0}=4^{3}\left[\begin{array}{c}1\\1\end{array}\right]-2\left[\begin{array}{c}-3\\2\end{array}\right]$

$x_{4}=A^{4}x_{0}=4^{4}\left[\begin{array}{c}1\\1\end{array}\right]+2\left[\begin{array}{c}-3\\2\end{array}\right]$

$x_{k}=A^{k}x_{0}=4^{k}\left[\begin{array}{c}1\\1\end{array}\right]+2\left(-1\right)^{k}\left[\begin{array}{c}-3\\2\end{array}\right]$

## 幂法求特征值

- $n$ 阶 $A$ 方阵存在 $n$ 个线性无关的特征向量 $\left\{v_{1},v_{2},\ldots ,v_{n}\right\}，\lambda _{i}$ 是对应特征值幂迭代： $x_{k}=A^{k}x_{0}=A^{k}\left(c_{1}v_{1}+c_{2}v_{2}\ldots +c_{n}v_{n}\right)$

$=\lambda _{1}^{k}\left[c_{1}v_{1}+\left(\frac{\lambda _{2}}{\lambda _{1}}\right)^{k}c_{2}v_{2}+\ldots +\left(\frac{\lambda _{n}}{\lambda _{1}}\right)^{k}c_{n}v_{n}\right]$

*1、* $\left|\lambda _{1}\right|>\left|\lambda _{2}\right|\geq \ldots \geq \left|\lambda _{n}\right|$

$\lim_{k\to \infty }x_{k}=\lambda _{1}^{k}\left[c_{1}v_{1}+\left(\frac{\lambda _{2}}{\lambda _{1}}\right)^{k}c_{2}v_{2}\right], c_{1}\ne 0$

特征向量： $\hat{v}_{1}\approx x_{k}$

特征值： $\lambda _{1}\approx r_{k}=\frac{x_{k}^{\left(i\right)}}{x_{k-1}^{\left(i\right)}},x_{k-1}^{\left(i\right)}\ne 0, 1\leq i\leq n$

线性收敛率： $S\leq \left|\lambda _{2}/\lambda _{1}\right|$

## 幂法求特征值

*2、* $\left|\lambda _{1}\right|=\left|\lambda _{2}\right|>\ldots \geq \left|\lambda _{n}\right|, \lambda _{1}=-\lambda _{2}$

$\lim_{k\to \infty }x_{k}=\lambda _{1}^{k}\left[\underbrace{c_{1}v_{1}+\left(-1\right)^{k}c_{2}v_{2}}_{w}+\left(\frac{\lambda _{3}}{\lambda _{1}}\right)^{k}c_{3}v_{3}\right], w\ne 0$

特征值：

$x_{k}\approx \lambda _{1}^{2}x_{k-2}\rightarrow \lambda _{1}^{2}\approx \frac{x_{k}^{\left(i\right)}}{x_{k-2}^{\left(i\right)}}$

特征向量：

$\left.\begin{array}{c}x_{k}\approx \lambda _{1}^{k}\left(c_{1}v_{1}+\left(-1\right)^{k}c_{2}v_{2}\right)\\x_{k-1}\approx \lambda _{1}^{k-1}\left(c_{1}v_{1}+\left(-1\right)^{k-1}c_{2}v_{2}\right) \end{array}\right\}\rightarrow \left\{\begin{array}{c}\hat{v}_{1}\approx x_{k}+\lambda _{1}x_{k-1}\\\hat{v}_{2}\approx x_{k}-\lambda _{1}x_{k-1}\end{array}\right.$

线性收敛率： $S\leq \left|\lambda _{3}/\lambda _{1}\right|$

- 幂法伪代码

$\mathbf{i}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{g}\mathbf{e}\mathbf{r} k,k_{max},i,j; \mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \lambda _{1}, e_{1},e_{2}$

$\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \mathbf{a}\mathbf{r}\mathbf{r}\mathbf{a}\mathbf{y} \left(a_{ij}\right)_{1:n\times 1:n},\left(x_{0}\right)_{1:n},x_{1:n},y_{1:n},z_{1:n}$

$x\leftarrow x_{0}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} k_{max} \mathbf{d}\mathbf{o}$

$\mathbf{F}\mathbf{i}\mathbf{n}\mathbf{d} i \mathbf{s}\mathbf{u}\mathbf{c}\mathbf{h} \mathbf{t}\mathbf{h}\mathbf{a}\mathbf{t} \left|x^{\left(i\right)}\right|=\max_{1\leq j\leq n}\left|x^{\left(j\right)}\right|$

$x\leftarrow x/x^{\left(i\right)}$

$y\leftarrow Ax$

$t=y^{\left(i\right)}/x^{(i)},e_{1}=\left\|y/t-x\right\|$

$\mathbf{i}\mathbf{f} e_{1}<TOL \mathbf{d}\mathbf{o}$

$\lambda _{1}\leftarrow t$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t}\left(\lambda _{1},y\right),\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

归一化，防止溢出情况1

$z\leftarrow Ay$

$t=z^{\left(i\right)}/x^{(i)}, e_{2}=\left\|z/t-x\right\|$

$\mathbf{i}\mathbf{f} e_{2}<TOL \mathbf{a}\mathbf{n}\mathbf{d} e_{1}>100*TOL \mathbf{d}\mathbf{o}$

$\lambda _{1}\leftarrow \sqrt{t},x\leftarrow z+\lambda _{1}y,y\leftarrow z-\lambda _{1}y$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t}\left(\lambda _{1},x,-\lambda _{1},y\right),\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$x\leftarrow z$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

情况2

## 幂法求特征值

- 如何求其它特征值和特征向量？

1. 逆幂法： $x_{k+1}=A^{-1}x_{k}\rightarrow Ax_{k+1}=x_{k}$ (求模最小特征值及对应特征向量)
2. 位移幂法： $x_{k+1}=\left(A-\mu I\right)x_{k}$  (求离 $\mu$ 最远的特征值及对应特征向量)
3. 位移逆幂法： $\left(A-\mu I\right)x_{k+1}=x_{k}$  (求离 $\mu$ 最近的特征值及对应特征向量)

- 逆幂法伪代码

$\mathbf{i}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{g}\mathbf{e}\mathbf{r} k,k_{max},i,j; \mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \lambda _{1}, e_{1},e_{2}$

$\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \mathbf{a}\mathbf{r}\mathbf{r}\mathbf{a}\mathbf{y} \left(a_{ij}\right)_{1:n\times 1:n},\left(x_{0}\right)_{1:n},x_{1:n},y_{1:n},z_{1:n}$

$x\leftarrow x_{0}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} k_{max} \mathbf{d}\mathbf{o}$

$\mathbf{F}\mathbf{i}\mathbf{n}\mathbf{d} i \mathbf{s}\mathbf{u}\mathbf{c}\mathbf{h} \mathbf{t}\mathbf{h}\mathbf{a}\mathbf{t} \left|x^{\left(i\right)}\right|=\max_{1\leq j\leq n}\left|x^{\left(j\right)}\right|$

$x\leftarrow \frac{x}{x^{i}}$

$\mathbf{s}\mathbf{o}\mathbf{l}\mathbf{v}\mathbf{e} Ay=x$

$t=y^{\left(i\right)}/x^{(i)},e_{1}=\left\|y/t-x\right\|$

$\mathbf{i}\mathbf{f} e_{1}<TOL \mathbf{d}\mathbf{o}$

$\lambda _{1}\leftarrow 1/t$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t}\left(\lambda _{1},y\right),\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

提前 $做好A=LU$ 分解归一化，防止溢出情况1

$\mathbf{s}\mathbf{o}\mathbf{l}\mathbf{v}\mathbf{e} Az=y$

$t=z^{\left(i\right)}/x^{(i)}, e_{2}=\left\|z/t-x\right\|$

$\mathbf{i}\mathbf{f} e_{2}<TOL \mathbf{a}\mathbf{n}\mathbf{d} e_{1}>100*TOL \mathbf{d}\mathbf{o}$

$\lambda _{1}\leftarrow 1/\sqrt{t},x\leftarrow z+\sqrt{t}y,y\leftarrow z-\sqrt{t}y$

$\mathbf{o}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t}\left(\lambda _{1},x,-\lambda _{1},y\right),\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$x\leftarrow z$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

情况2

## 幂法求特征值

- 例：用幂法和逆幂法求 $A$ 的最大模和最小模特征值

$A=\left[\begin{matrix}-4&14&0\\-5&13&0\\-1&0&2\end{matrix}\right],x_{0}=\left[\begin{array}{c}1\\1\\1\end{array}\right],\lambda =6,3,2$

$幂迭代$

$k$

$逆$ 幂迭代

![](images/d0a467b544b482cf449f788c65191d4940b21b79bdf24bbe12e21a9579c8f4c3.jpg)

![](images/e82b53ee4a3a83cc9e65768cbb2474c65522c24ba8b59354f45ff0e1380abda4.jpg)

## Rayleigh商迭代

- 已知 $x$ 是 $A$ 的近似特征向量，求对应特征值的近似

$Ax\approx \lambda x$ （超定方程）

最小化残差： $\lambda =\frac{x^{T}Ax}{x^{T}x}$ (Rayleigh商)

- Rayleigh商迭代算法：

$x\leftarrow x_{0}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=0 \mathbf{t}\mathbf{o} k_{max} \mathbf{d}\mathbf{o}$

$u\leftarrow x/\left\|x\right\|_{2}$

$x\leftarrow Au$

$\lambda \leftarrow u^{T}x$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$u\leftarrow x/\left\|x\right\|_{2}$

$\lambda _{k}=\frac{x_{k}^{T}Ax_{k}}{x_{k}^{T}x_{k}}$

## Rayleigh商迭代

- 如果 $A$ 为实对称矩阵，且有 $\left|\lambda _{1}\right|>\left|\lambda _{2}\right|\geq \ldots \geq |\lambda _{n}|$ ，则幂法中使用Rayleigh商迭代得到的特征值序列收敛速率 $S\leq \left(\frac{\lambda _{2}}{\lambda _{1}}\right)^{2}$ 。

## Rayleigh商迭代

- 例：用幂法求 $A$ 的最大模的特征值

$A=\left[\begin{matrix}-4&14&0\\-5&13&0\\-1&0&2\end{matrix}\right],x_{0}=\left[\begin{array}{c}1\\1\\1\end{array}\right],\lambda =6,3,2$

$k$

$幂迭代$

$Rayleigh$

![](images/7f60e345ba39934ce2e5ae733e2f8530563cfa26d1ab7ac5998199bdc89fedb1.jpg)

![](images/1d28d4c2fdc38542bcbbcc988553ad19005ba7d705df7e76db48b5562aafe7d4.jpg)

## Rayleigh商迭代

- 例：

$A=\left[\begin{matrix}1&2&1\\2&3&1\\1&1&3\end{matrix}\right],x_{0}=\left[\begin{array}{c}1\\1\\1\end{array}\right]$

$幂迭代$

$Rayleigh$

$k$

![](images/320c70274937586f24d5c90282fb4ec097bccfefdf6118b9038fb82e5ff5b3f3.jpg)

![](images/16a0950bf7a29a65593a40ec1b1783c7e1eb3be6b36ae2d10f383c00c4fe043c.jpg)

## QR分解

- Schur酉三角化定理：每个方阵 $A$ 酉相似于一个上三角阵 $R$ ，即：

$A=URU^{*}, \left(UU^{*}=I, U^{*}是U的共轭转置\right)$

- QR分解：把 $m\times n$ 矩阵 $A$ 分解为: $A=QR$

$Q$ 为 $m\times m$ 正交阵， $R$ 为 $m\times n$ 上三角阵。

## QR分解：Gram-Schmit正交化

- Gram-Schmit正交化实现 $QR$ 分解

1、如果 $m\times n$ 矩阵 $A$ 的列向量 $A_{1},\ldots ,A_{n}\in \mathbb{R}^{m}$ 线性无关 $\left(m\geq n\right)$ ，则可进行Gram-Schmit正交化

$y_{1}=A_{1}, q_{1}=\frac{y_{1}}{\left\|y_{1}\right\|_{2}}$

$y_{2}=A_{2}-\left(q_{1}^{T}A_{2}\right)q_{1}, q_{2}=\frac{y_{2}}{\left\|y_{2}\right\|_{2}}$

$\vdots$

$y_{j}=A_{j}-\left(q_{1}^{T}A_{j}\right)q_{1}-\ldots -\left(q_{j-1}^{T}A_{j}\right)q_{j-1}, q_{j}=\frac{y_{j}}{\left\|y_{j}\right\|_{2}}, 2\leq j\leq n$

2、定义 $r_{jj}=\left\|y_{j}\right\|_{2}, r_{ij}=q_{i}^{T}A_{j},$ 则有：

$A_{1}=r_{11}q_{1}$

$A_{2}=r_{12}q_{1}+r_{22}q_{2}$

$\vdots$

$A_{j}=r_{1j}q_{1}+\ldots +r_{j-1,j}q_{j-1}+r_{jj}q_{j}, 2\leq j\leq n$

$⇒\left[A_{1},A_{2},\ldots ,A_{n}\right]=\left[\underbrace{q_{1},q_{2},\ldots ,q_{n}}_{m\times n}\right]\left[\begin{matrix}r_{11}&r_{12}&\cdots &r_{1n}\\&r_{22}&\cdots &r_{2n}\\&&\ddots &\vdots \\&&&r_{nn}\end{matrix}\right]$

- 例：利用Gram-Schmidt正交化对 $A$ 进行消减QR分解

$A=\left[\begin{matrix}1&-4\\2&3\\2&2\end{matrix}\right]$

$1. y_{1}=A_{1}=\left[1,2,2\right]^{T},r_{11}=\left\|y_{1}\right\|_{2}=3, q_{1}=\frac{y_{1}}{\left\|y_{1}\right\|_{2}}=\left[\frac{1}{3},\frac{2}{3},\frac{2}{3}\right]^{T}$

$2. r_{12}=q_{1}^{T}A_{2}=2,y_{2}=A_{2}-r_{12}q_{1}=\left[\begin{matrix}-4\\3\\2\end{matrix}\right]-2\left[\begin{matrix}\frac{1}{3}\\\frac{2}{3}\\\frac{2}{3}\end{matrix}\right]=\left[\begin{matrix}-\frac{14}{3}\\\frac{5}{3}\\\frac{2}{3}\end{matrix}\right]$

$r_{22}=\left\|y_{2}\right\|_{2}=5, q_{2}=\frac{y_{2}}{\left\|y_{2}\right\|_{2}}=\left[-\frac{14}{15},\frac{1}{3},\frac{2}{15}\right]^{T}$

$A=\left[\begin{matrix}\frac{1}{3}&-\frac{14}{15}\\\frac{2}{3}&\frac{1}{3}\\\frac{2}{3}&\frac{2}{15}\end{matrix}\right]\left[\begin{matrix}3&2\\0&5\end{matrix}\right]=QR$

## QR分解：Gram-Schmit正交化

- Gram-Schmit正交化实现完全 $QR$ 分解

1、如果 $m\times n$ 矩阵 $A$ 的列向量 $A_{1},\ldots ,A_{n}$ 线性无关 $\left(m>n\right)$ ，则可进行Gram-Schmit正交化

$y_{1}=A_{1}, q_{1}=\frac{y_{1}}{\left\|y_{1}\right\|_{2}}$

$y_{2}=A_{2}-\left(q_{1}^{T}A_{2}\right)q_{1}, q_{2}=\frac{y_{2}}{\left\|y_{2}\right\|_{2}}$

$\vdots$

$y_{n}=A_{n}-\left(q_{1}^{T}A_{n}\right)q_{1}-\ldots -\left(q_{j-1}^{T}A_{n}\right)q_{j-1}, q_{n}=\frac{y_{n}}{\left\|y_{n}\right\|_{2}}$

任意增加 $m-n$ 个 $\mathbb{R}^{m}$ 向量构成线性无关向量组 $\left\{A_{1},\ldots ,A_{n}, A_{n+1},\ldots ,A_{m}\right\}$ 进行正交化

$y_{k}=A_{k}-\left(q_{1}^{T}A_{k}\right)q_{1}-\ldots -\left(q_{k-1}^{T}A_{k}\right)q_{k-1}, q_{k}=\frac{y_{k}}{\left\|y_{k}\right\|_{2}}, 1+n\leq k\leq m$

## QR分解：Gram-Schmit正交化

2、定义 $r_{jj}=\left\|y_{j}\right\|_{2}, r_{ij}=q_{i}^{T}A_{j},$ 则有：

$A_{1}=r_{11}q_{1}$

$A_{2}=r_{12}q_{1}+r_{22}q_{2}$

$\vdots$

$A_{n}=r_{1n}q_{1}+\ldots +r_{n-1,n}q_{n-1}+r_{nn}q_{n}$

$A_{k}=r_{1k}q_{1}+\ldots +r_{k-1,k}q_{k-1}+r_{kk}q_{k},1+n\leq k\leq m$

$⇒\left[A_{1},A_{2},\ldots ,A_{n}\right]=\left[q_{1},q_{2},\ldots ,q_{n},q_{n+1},\ldots ,q_{m}\right]\left[\begin{matrix}r_{11}&r_{12}&\cdots &r_{1n}\\&r_{22}&\cdots &r_{2n}\\&&\ddots &\vdots \\&&&r_{nn}\\0&0&\cdots &0\\\vdots &\vdots &\vdots &\vdots \\0&0&\cdots &0\end{matrix}\right]$

## QR分解：Gram-Schmit正交化

- Gram-Schmidt正交化算法计算量

$A_{1},\ldots ,A_{n}\in \mathbb{R}^{m}$  $are linearly independent vectors$

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$

$y=A_{j}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} j-1$

$r_{ij}=q_{i}^{T}A_{j}$

$y\leftarrow y-r_{ij}q_{i}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$r_{jj}=\left\|y\right\|_{2}$

$q_{j}=y/r_{jj}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$m$ 次乘法

$m$ 次乘法

$m$ 次乘法，1次开方

$m$ 次除法

$=\sum_{j=1}^{n}\left[2m\left(j-1\right)+2m+1\right]=mn^{2}+mn+n$

乘法、除法、开方计算量

## QR分解：Gram-Schmit正交化

- 例：利用Gram-Schmidt正交化对 $A$ 进行完全QR分解

$A=\left[\begin{matrix}1&-4\\2&3\\2&2\end{matrix}\right]$

解：1、前面已经得到： $r_{11}=\left\|y_{1}\right\|_{2}=3, q_{1}=\frac{y_{1}}{\left\|y_{1}\right\|_{2}}=\left[\frac{1}{3},\frac{2}{3},\frac{2}{3}\right]^{T}$

$r_{12}=2,r_{22}=\left\|y_{2}\right\|_{2}=5, q_{2}=\frac{y_{2}}{\left\|y_{2}\right\|_{2}}=\left[-\frac{14}{15},\frac{1}{3},\frac{2}{15}\right]^{T}$

2、令 $A_{3}=\left[1,0,0\right]^{T}$

$y_{3}=A_{3}-\left(q_{1}^{T}A_{3}\right)q_{1}-\left(q_{2}^{T}A_{3}\right)q_{2}=\frac{1}{225}\left[4,20,-22\right]^{T}$

$q_{3}=\frac{y_{3}}{\left\|y_{3}\right\|_{2}}=\left[\frac{2}{15},\frac{2}{3}, -\frac{11}{15}\right]^{T}$

$A=\left[\begin{matrix}\frac{1}{3}&-\frac{14}{15}&\frac{2}{15}\\\frac{2}{3}&\frac{1}{3}&\frac{2}{3}\\\frac{2}{3}&\frac{2}{15}&-\frac{11}{15}\end{matrix}\right]\left[\begin{matrix}3&2\\0&5\\0&0\end{matrix}\right]=QR$

$A=\left[\begin{matrix}1&1&1\\\delta &0&0\\0&\delta &0\\0&0&\delta \end{matrix}\right], \delta =10^{-10}$

- 例：利用Gram-Schmidt正交化对 $A$ 的列向量进行正交化

$y_{1}=A_{1}=\left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right], q_{1}=\frac{1}{\sqrt{1+\delta ^{2}}}\left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right]\approx \left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right]$

$y_{2}=\left[\begin{array}{c}1\\0\\\delta \\0\end{array}\right]-\underbrace{q_{1}^{T}A_{2}}_{1}\left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right]=\left[\begin{array}{c}0\\-\delta \\\delta \\0\end{array}\right], q_{2}=\frac{1}{\sqrt{2\delta ^{2}}}\left[\begin{array}{c}0\\-\delta \\\delta \\0\end{array}\right]=\left[\begin{array}{c}0\\-\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{array}\right]$

$y_{3}=\left[\begin{array}{c}1\\0\\0\\\delta \end{array}\right]-\underbrace{q_{1}^{T}A_{3}}_{1}\left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right]-\underbrace{q_{2}^{T}A_{3}}_{0}\left[\begin{array}{c}0\\-\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{array}\right]=\left[\begin{array}{c}0\\-\delta \\0\\\delta \end{array}\right], q_{3}=\frac{1}{\sqrt{2\delta ^{2}}}\left[\begin{array}{c}0\\-\delta \\0\\\delta \end{array}\right]=\left[\begin{array}{c}0\\-\frac{1}{\sqrt{2}}\\0\\\frac{1}{\sqrt{2}}\end{array}\right]$

不严格正交不正交

## QR分解：Gram-Schmit正交化

- 经典Gram-Schmidt正交化算法

$Linearly independent vectors:A_{1},\ldots ,A_{n}$

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$

$y=A_{j}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} j-1$

$r_{ij}=q_{i}^{T}A_{j}$

$y\leftarrow y-r_{ij}q_{i}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$r_{jj}=\left\|y\right\|_{2}$

$q_{j}=y/r_{jj}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- 改进Gram-Schmidt正交化算法

$Linearly independent vectors:A_{1},\ldots ,A_{n}$

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$

$y=A_{j}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} j-1$

$r_{ij}=q_{i}^{T}y$

$y\leftarrow y-r_{ij}q_{i}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$r_{jj}=\left\|y\right\|_{2}$

$q_{j}=y/r_{jj}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$y=A_{j}-r_{1j}q_{1}-\ldots -r_{i-1,j}q_{i-1}$

$q_{i}^{T}y=q_{i}^{T}A_{j}$

$A=\left[\begin{matrix}1&1&1\\\delta &0&0\\0&\delta &0\\0&0&\delta \end{matrix}\right], \delta =10^{-10}$

- 例：利用改进Gram-Schmidt正交化对 $A$ 的列向量进行正交化

$y_{1}=A_{1}, q_{1}\approx \left[\begin{matrix}1&\delta &0&0\end{matrix}\right]^{T}$

$y_{2}=A_{2}-\underbrace{q_{1}^{T}A_{2}}_{1}q_{1}=\left[\begin{matrix}0&-\delta &\delta &0\end{matrix}\right]^{T}, q_{2}=\left[\begin{matrix}0&-\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\end{matrix}\right]^{T}$

$y_{3}^{1}=\left[\begin{array}{c}1\\0\\0\\\delta \end{array}\right]-\underbrace{q_{1}^{T}A_{3}}_{1}\left[\begin{array}{c}1\\\delta \\0\\0\end{array}\right]=\left[\begin{array}{c}0\\-\delta \\0\\\delta \end{array}\right];y_{3}=y_{3}^{1}-\underbrace{q_{2}^{T}y_{3}^{1}}_{\frac{\delta }{\sqrt{2}}}\left[\begin{array}{c}0\\-\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{array}\right]=\left[\begin{array}{c}0\\-\frac{\delta }{2}\\-\frac{\delta }{2}\\\delta \end{array}\right], q_{3}=\left[\begin{array}{c}0\\-\frac{1}{\sqrt{6}}\\-\frac{1}{\sqrt{6}}\\\frac{2}{\sqrt{6}}\end{array}\right]$

正交

## QR变换：Householder变换

- 引理： $x,w\in \mathbb{R}^{n}$ ,如果 $\left\|x\right\|_{2}=\left\|w\right\|_{2},$ 则 $\left⟨w-x,w+x\right⟩=0$
- (定义)投影矩阵 $P$ 满足： $P^{T}=P(对称),P^{2}=P$ (幂等)。
- $v\in \mathbb{R}^{n}$ , $P=\frac{vv^{T}}{v^{T}v}$ 是投影矩阵，且 $Pu$ 是 $u$ 在 $v$ 上的投影。
- 已知 $x,w\in \mathbb{R}^{n}$ , $\left\|x\right\|_{2}=\left\|w\right\|_{2}$ ， $x→w$

$w=x+\underbrace{\left(w-x\right)}_{v}=x-2Px=\underbrace{\left(I-2\frac{vv^{T}}{v^{T}v}\right)}_{H}x, v=w-x$

$-Px$

$x$

$H:$ Householder反射子

$v=w-x$

$Hx$ 是 $x$ 关于超平面 $v^{\perp }$ 的镜像

$w$

$H$ 是对称、正交矩阵： $H^{2}=I$

## QR变换：Householder变换

- 定理 $：x,w\in \mathbb{R}^{n}$ ,且 $\left\|x\right\|_{2}=\left\|w\right\|_{2},$ 定义 $v:=w-x, H:=I-2\frac{vv^{T}}{v^{T}v}$ ，则 $H$ 为 $对称正交矩阵，且Hx=w$
- 例：已知 $x=\left[3,4\right]^{T},w=\left[5,0\right]^{T}$ ,找出 $H$ 使得 $Hx=w$

解： $v=w-x=\left[\begin{array}{c}5\\0\end{array}\right]-\left[\begin{array}{c}3\\4\end{array}\right]=\left[\begin{array}{c}2\\-4\end{array}\right]$

计算投影矩阵： $P=\frac{vv^{T}}{v^{T}v}=\frac{1}{20}\left[\begin{matrix}4&-8\\-8&16\end{matrix}\right]$

$H=I-2P=\left[\begin{matrix}1&0\\0&1\end{matrix}\right]-\left[\begin{matrix}0.4&-0.8\\-0.8&1.6\end{matrix}\right]=\left[\begin{matrix}0.6&0.8\\0.8&-0.6\end{matrix}\right]$

## QR变换：Householder变换

- 如何利用Householder变换做QR分解？
- 引例：对矩阵 $A=\left[\begin{matrix}3&1\\4&3\end{matrix}\right]$ 进行QR分解

$A=\left[A_{1},A_{2}\right], A_{1}=\left[\begin{array}{c}3\\4\end{array}\right],A_{2}=\left[\begin{array}{c}1\\3\end{array}\right]$

$A=QR\rightarrow Q^{T}A=R\rightarrow \left[Q^{T}A_{1},Q^{T}A_{2}\right]=\left[\begin{matrix}\times &\times \\0&\times \end{matrix}\right]$

令 $Q^{T}=H=\left[\begin{matrix}0.6&0.8\\0.8&-0.6\end{matrix}\right]$

$Q^{T}A=\left[HA_{1},HA_{2}\right]=\left[\begin{matrix}5&3\\0&-1\end{matrix}\right]$

$A=QR=HR=\left[\begin{matrix}0.6&0.8\\0.8&-0.6\end{matrix}\right]\left[\begin{matrix}5&3\\0&-1\end{matrix}\right]$

## QR变换：Householder变换

- $A=\left[A_{1},A_{2},\ldots ,A_{n}\right],A_{j}\in \mathbb{R}^{m}$ , Householder变换实现QR分解的具体算法：
- 第一步：约化第一列

1. 如果 $\left\|A_{1}\right\|_{2}=0, H_{1}=I,$ 跳到第二步
2. $\left|r_{11}\right|=\left\|A_{1}\right\|_{2}, w=r_{11}e_{1}$
3. $v=w-A_{1}\left(避免相近的数相减，取r_{11}=\left\{\begin{array}{c}-\left\|A_{1}\right\|_{2}, a_{11}>0\\\left\|A_{1}\right\|_{2}, a_{11}<0\end{array}\right.\right)$
4. $H_{1}=I-2\frac{vv^{T}}{v^{T}v}$
5. $H_{1}A=\left[\begin{matrix}r_{11}&b_{1\times (n-1)}\\0_{(m-1)\times 1}&\tilde{A}_{(m-1)\times (n-1)}\end{matrix}\right]$

## QR变换：Householder变换

- 执行 $k$ 步之后

$H_{k}\ldots H_{1}A=\left[\begin{matrix}\tilde{R}_{k\times k}&W_{k\times (n-k)}\\0_{(m-k)\times k}&\tilde{A}_{(m-k)\times (n-k)}\end{matrix}\right]$

- 第 $k+1$ 步：约化第 $k+1$ 列

1. 如果 $\left\|\tilde{A}_{1}\right\|_{2}=0，H_{k+1}=I$ 跳到下一步
2. $w=r_{kk}\tilde{e}_{1},r_{kk}=\left\{\begin{array}{c}-\left\|\tilde{A}_{1}\right\|_{2}, \tilde{a}_{11}>0\\\left\|\tilde{A}_{1}\right\|_{2},\tilde{a}_{11}<0\end{array}\right.$
3. $v=w-\tilde{A}_{1}$
4. $\tilde{H}_{k+1}=I_{(m-k)\times (m-k)}-2\frac{vv^{T}}{v^{T}v}$
5. $H_{k+1}H_{k}\ldots H_{1}A=\left[\begin{matrix}I_{k\times k}&0_{k\times (m-k)}\\0_{(m-k)\times k}&\tilde{H}_{k+1}\end{matrix}\right]\left[\begin{matrix}\tilde{R}_{k\times k}&W_{k\times (n-k)}\\0_{(m-k)\times k}&\tilde{A}_{(m-k)\times (n-k)}\end{matrix}\right]=\left[\begin{matrix}R&W\\0&\tilde{H}\tilde{A}\end{matrix}\right]$

- *第* $n$ *步之后：* $H_{n}\ldots H_{1}A=R\rightarrow A=\underbrace{H_{1}\ldots H_{n}}_{Q}R$

- Householder变换实现QR分解的伪代码：

$A=\left[A_{1},A_{2},\ldots ,A_{n}\right],A_{j}\in \mathbb{R}^{m},Q=I_{m\times m}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} n$

$t\leftarrow \left\|A_{k:m,k}\right\|_{2}$

$\mathbf{i}\mathbf{f} t=0 \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n} \mathbf{e}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{r} \mathbf{t}\mathbf{h}\mathbf{e} \mathbf{n}\mathbf{e}\mathbf{x}\mathbf{t} \mathbf{l}\mathbf{o}\mathbf{o}\mathbf{p}$

$\mathbf{i}\mathbf{f} a_{kk}>0 \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n} t\leftarrow -t$

$v\leftarrow te_{1}-A_{k:m,k}$

$A_{k:m,k}\leftarrow te_{1}$

$t_{0}\leftarrow \frac{2}{v^{T}v}$

$\mathbf{f}\mathbf{o}\mathbf{r} j=k+1 \mathbf{t}\mathbf{o} n$

$t\leftarrow t_{0}\left(v^{T}A_{k:m,j}\right)$

$A_{k:m,j}\leftarrow A_{k:m,j}-tv$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} m$

$t=t_{0}\left(Q_{i,k:m}v\right)$

$Q_{i,k:m}\leftarrow Q_{i,k:m}-tv^{T}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$更新Q=H_{1}\ldots H_{n}$

$Q_{k}=Q_{k-1}H_{k}$

$x^{T}H=x^{T}\left(\underbrace{I-2\frac{vv^{T}}{v^{T}v}}_{H}\right)$

$=x^{T}-2\left(\frac{x^{T}v}{v^{T}v}\right)v^{T}$

$约化A的第k列$

$\left[\begin{matrix}R_{\left(k-1\right)\times \left(k-1\right)}&W\\0&\tilde{H}_{k}\tilde{A}\end{matrix}\right]$

$Hx=\left(\underbrace{I-2\frac{vv^{T}}{v^{T}v}}_{H}\right)x$

$=x-2\left(\frac{v^{T}x}{v^{T}v}\right)v$

$Q_{k}=\left[\begin{matrix}Q_{1:k-1,1:k-1}&Q_{1:k-1,k:m}\\Q_{k:m,1:k-1}&Q_{k:m,k:m}\end{matrix}\right]\left[\begin{matrix}I_{\left(k-1\right)\times \left(k-1\right)}&0_{\left(k-1\right)\times (m-k+1)}\\0_{(m-k+1)\times \left(k-1\right)}&\tilde{H}_{k}\end{matrix}\right]$

$=\left[\begin{matrix}Q_{1:k-1,1:k-1}&Q_{1:k-1,k:m}\tilde{H}_{k}\\Q_{k:m,1:k-1}&Q_{k:m,k:m}\tilde{H}_{k}\end{matrix}\right]$

- Householder变换实现QR分解的计算量：

$A=\left[A_{1},A_{2},\ldots ,A_{n}\right],A_{j}\in \mathbb{R}^{m},Q=I_{m\times m}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} n$

$t\leftarrow \left\|A_{k:m,k}\right\|_{2}$

$\mathbf{i}\mathbf{f} t=0 \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n} \mathbf{e}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{r} \mathbf{t}\mathbf{h}\mathbf{e} \mathbf{n}\mathbf{e}\mathbf{x}\mathbf{t} \mathbf{l}\mathbf{o}\mathbf{o}\mathbf{p}$

$\mathbf{i}\mathbf{f} a_{kk}>0 \mathbf{t}\mathbf{h}\mathbf{e}\mathbf{n} t\leftarrow -t$

$v\leftarrow te_{1}-A_{k:m,k}$

$A_{k:m,k}\leftarrow te_{1}$

$t_{0}\leftarrow \frac{2}{v^{T}v}$

$\mathbf{f}\mathbf{o}\mathbf{r} j=k+1 \mathbf{t}\mathbf{o} n$

$t\leftarrow t_{0}\left(v^{T}A_{k:m,j}\right)$

$A_{k:m,j}\leftarrow A_{k:m,j}-tv$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} m$

$t=t_{0}\left(Q_{i,k:m}v\right)$

$Q_{i,k:m}\leftarrow Q_{i,k:m}-tv^{T}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$m-k+2$ 次乘法

$m-k+1$ 次乘法

$m-k+1$ 次乘法,1次开方

$第一部分=\sum_{k=1}^{n}\left[2(m-k+2)+(2m-2k+3)\left(n-k\right)\right]$

$=\left(m-\frac{n}{3}+\frac{1}{2}\right)n^{2}+mn+\frac{11}{6}n$

$m-k+1$ 次乘法,1次除法

$第二部分=\sum_{k=1}^{n}\left[\left(2m-2k+3\right)m\right]$

$=mn\left(2m-n+2\right)$

$m-k+2$ 次乘法

$m-k+1$ 次乘法

- 例：利用Householder反射子找到矩阵 $A$ 的QR分解

$A=\left[\begin{matrix}1&-4\\\begin{array}{c}2\\2\end{array}&\begin{array}{c}3\\2\end{array}\end{matrix}\right]$

解：1.约化第一列： $\left\|A_{1}\right\|_{2}=3, v=-\left\|A_{1}\right\|_{2}e_{1}-A_{1}=\left[-4,-2,-2\right]^{T}$

$H_{1}=I-2\frac{vv^{T}}{v^{T}v}=\left[\begin{matrix}1&0&0\\0&1&0\\0&0&1\end{matrix}\right]-\frac{2}{24}\left[\begin{matrix}16&8&8\\8&4&4\\8&4&4\end{matrix}\right]=\left[\begin{matrix}-\frac{1}{3}&-\frac{2}{3}&-\frac{2}{3}\\-\frac{2}{3}&\frac{2}{3}&-\frac{1}{3}\\-\frac{2}{3}&-\frac{1}{3}&\frac{2}{3}\end{matrix}\right]$

$H_{1}A=\left[\begin{matrix}-\frac{1}{3}&-\frac{2}{3}&-\frac{2}{3}\\-\frac{2}{3}&\frac{2}{3}&-\frac{1}{3}\\-\frac{2}{3}&-\frac{1}{3}&\frac{2}{3}\end{matrix}\right]\left[\begin{matrix}1&-4\\\begin{array}{c}2\\2\end{array}&\begin{array}{c}3\\2\end{array}\end{matrix}\right]=\left[\begin{matrix}-3&-2\\\begin{array}{c}0\\0\end{array}&\begin{array}{c}4\\3\end{array}\end{matrix}\right]$

2.约化第二列： $\left\|\tilde{A}_{1}\right\|_{2}=5,  v=-\left\|\tilde{A}_{1}\right\|_{2}e_{1}-\tilde{A}_{1}=\left[-9,-3\right]^{T}$

$H_{2}=\left[\begin{matrix}1&0\\0&I-2\frac{vv^{T}}{v^{T}v}\end{matrix}\right]=\left[\begin{matrix}1&0&0\\0&1&0\\0&0&1\end{matrix}\right]-\frac{2}{90}\left[\begin{matrix}0&0&0\\0&81&27\\0&27&9\end{matrix}\right]=\left[\begin{matrix}1&0&0\\0&-\frac{4}{5}&-\frac{3}{5}\\0&-\frac{3}{5}&\frac{4}{5}\end{matrix}\right]$

$H_{2}(H_{1}A)=\left[\begin{matrix}1&0&0\\0&-\frac{4}{5}&-\frac{3}{5}\\0&-\frac{3}{5}&\frac{4}{5}\end{matrix}\right]\left[\begin{matrix}-3&-2\\\begin{array}{c}0\\0\end{array}&\begin{array}{c}4\\3\end{array}\end{matrix}\right]=\underbrace{\left[\begin{matrix}-3&-2\\\begin{array}{c}0\\0\end{array}&\begin{array}{c}-5\\0\end{array}\end{matrix}\right]}_{R}$

*3.*

$Q=H_{1}H_{2}=\left[\begin{matrix}-\frac{1}{3}&-\frac{2}{3}&-\frac{2}{3}\\-\frac{2}{3}&\frac{2}{3}&-\frac{1}{3}\\-\frac{2}{3}&-\frac{1}{3}&\frac{2}{3}\end{matrix}\right]\left[\begin{matrix}1&0&0\\0&-\frac{4}{5}&-\frac{3}{5}\\0&-\frac{3}{5}&\frac{4}{5}\end{matrix}\right]=\left[\begin{matrix}-\frac{1}{3}&\frac{14}{15}&-\frac{2}{15}\\-\frac{2}{3}&-\frac{1}{3}&-\frac{2}{3}\\-\frac{2}{3}&-\frac{2}{15}&\frac{11}{15}\end{matrix}\right]$

- 例：利用Householder变换对 $A$ 进行 $QR$ 分解

$A=\left[\begin{matrix}1&1&1\\\delta &0&0\\0&\delta &0\\0&0&\delta \end{matrix}\right], \delta =10^{-10}$

解：1.约化第一列： $\left\|A_{1}\right\|_{2}=\sqrt{1+\delta ^{2}}\approx 1, v=-\left\|A_{1}\right\|_{2}e_{1}-A_{1}=\left[-2,-\delta ,0,0\right]^{T}$

$H_{1}=I-2\frac{vv^{T}}{v^{T}v}=\left[\begin{matrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}\right]-\frac{2}{4}\left[\begin{matrix}4&2\delta &0&0\\2\delta &\delta ^{2}&0&0\\0&0&0&0\\0&0&0&0\end{matrix}\right]=\left[\begin{matrix}-1&-\delta &0&0\\-\delta &1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}\right]$

$H_{1}A=\left[\begin{matrix}-1&-\delta &0&0\\-\delta &1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}\right]\left[\begin{matrix}1&1&1\\\delta &0&0\\0&\delta &0\\0&0&\delta \end{matrix}\right]=\left[\begin{matrix}-1&-1&-1\\0&-\delta &-\delta \\0&\delta &0\\0&0&\delta \end{matrix}\right]$

2.约化第二列： $\left\|\tilde{A}_{1}\right\|_{2}=\sqrt{\delta ^{2}+\delta ^{2}}=\sqrt{2}\delta , v=\left\|\tilde{A}_{1}\right\|_{2}e_{1}-\tilde{A}_{1}=\left[\left(1+\sqrt{2}\right)\delta ,-\delta ,0\right]^{T}$

$H_{2}=\left[\begin{matrix}1&0\\0&I-2\frac{vv^{T}}{v^{T}v}\end{matrix}\right]=\left[\begin{matrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}\right]-\frac{2}{\left(4+2\sqrt{2}\right)\delta ^{2}}\left[\begin{matrix}0&0&0&0\\0&\left(3+2\sqrt{2}\right)\delta ^{2}&-\left(1+\sqrt{2}\right)\delta ^{2}&0\\0&-\left(1+\sqrt{2}\right)\delta ^{2}&\delta ^{2}&0\\0&0&0&0\end{matrix}\right]$

$=\left[\begin{matrix}1&0&0&0\\0&-\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\0&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\0&0&0&1\end{matrix}\right]$

## QR变换：Householder变换

$H_{2}(H_{1}A)=\left[\begin{matrix}1&0&0&0\\0&-\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\0&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\0&0&0&1\end{matrix}\right]\left[\begin{matrix}-1&-1&-1\\0&-\delta &-\delta \\0&\delta &0\\0&0&\delta \end{matrix}\right]=\left[\begin{matrix}-1&-1&-1\\0&\sqrt{2}\delta &\frac{1}{\sqrt{2}}\delta \\0&0&-\frac{1}{\sqrt{2}}\delta \\0&0&\delta \end{matrix}\right]$

3.约化第三列： $\left\|\tilde{A}_{1}\right\|_{2}=\sqrt{\frac{3}{2}}\delta , v=\left\|\tilde{A}_{1}\right\|_{2}e_{1}-\tilde{A}_{1}=\left[\frac{\left(1+\sqrt{3}\right)}{\sqrt{2}}\delta ,-\delta \right]^{T}$

$H_{3}=\left[\begin{matrix}1&0\\0&I-2\frac{vv^{T}}{v^{T}v}\end{matrix}\right]=\left[\begin{matrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{matrix}\right]-\frac{2}{\left(3+\sqrt{3}\right)\delta ^{2}}\left[\begin{matrix}0&0&0&0\\0&0&0&0\\0&0&\left(2+\sqrt{3}\right)\delta ^{2}&-\frac{\left(1+\sqrt{3}\right)}{\sqrt{2}}\delta ^{2}\\0&0&-\frac{\left(1+\sqrt{3}\right)}{\sqrt{2}}\delta ^{2}&\delta ^{2}\end{matrix}\right]$

$=\left[\begin{matrix}1&0&0&0\\0&1&0&0\\0&0&-\frac{1}{\sqrt{3}}&\sqrt{\frac{2}{3}}\\0&0&\sqrt{\frac{2}{3}}&\frac{1}{\sqrt{3}}\end{matrix}\right]$

$H_{3}H_{2}H_{1}A=\left[\begin{matrix}1&0&0&0\\0&1&0&0\\0&0&-\frac{1}{\sqrt{3}}&\sqrt{\frac{2}{3}}\\0&0&\sqrt{\frac{2}{3}}&\frac{1}{\sqrt{3}}\end{matrix}\right]\left[\begin{matrix}-1&-1&-1\\0&\sqrt{2}\delta &\frac{1}{\sqrt{2}}\delta \\0&0&-\frac{1}{\sqrt{2}}\delta \\0&0&\delta \end{matrix}\right]=\left[\begin{matrix}-1&-1&-1\\0&\sqrt{2}\delta &\frac{1}{\sqrt{2}}\delta \\0&0&\sqrt{\frac{3}{2}}\delta \\0&0&0\end{matrix}\right]$

改进Gram-Schmidt方法： $R=\left[\begin{matrix}1&1&1\\0&\sqrt{2}\delta &\frac{1}{\sqrt{2}}\delta \\0&0&\sqrt{\frac{3}{2}}\delta \\0&0&0\end{matrix}\right]$

## QR分解的应用

1、求解 $n\times n$ 线性方程组 $Ax=b\rightarrow QRx=b\rightarrow Rx=Q^{T}b$ .

- 缺点：QR分解实现比较复杂，计算量比 $LU$ 分解大得多

2、求解 $m\times n\left(m>n\right)$ 线性方程组的最小二乘解

3、数值求解特征值

## QR算法

- QR算法的思路： $n$ 阶实对称阵 $A$ 的特征向量构成正交基 $\left\{v_{1},v_{2},\ldots ,v_{n}\right\}，\lambda _{i}$ 是对应特征值幂迭代： $x_{k}=A^{k}x_{0}=A^{k}\left(c_{1}v_{1}+c_{2}v_{2}\ldots +c_{n}v_{n}\right)$

$=\lambda _{1}^{k}\left[c_{1}v_{1}+\left(\frac{\lambda _{2}}{\lambda _{1}}\right)^{k}c_{2}v_{2}+\ldots +\left(\frac{\lambda _{n}}{\lambda _{1}}\right)^{k}c_{n}v_{n}\right]$

- $\left|\lambda _{1}\right|>\left|\lambda _{2}\right|>\ldots >\left|\lambda _{n}\right|$

当 $c_{1}\ne 0,\lim_{k\to \infty }x_{k}=\lambda _{1}^{k}c_{1}v_{1}$

当 $c_{1}=0,c_{2}\ne 0,\lim_{k\to \infty }x_{k}=\lambda _{2}^{k}c_{2}v_{2}$

$\vdots$

选取一组正交向量同时进行迭代，每次迭代都对向量进行正交化，最终可得到所有的特征向量及对应的特征值

- 求特征值的归一化同时迭代算法：

1. 初始选取一组正交向量，例如： $\left[e_{1},e_{2},\ldots ,e_{n}\right]$
2. 第一步迭代 $\left[Ae_{1},Ae_{2},\ldots ,Ae_{n}\right]=AI$
3. 将 $\{Ae_{1},Ae_{2},\ldots ,Ae_{n}\}$ 正交化、归一化：

$\left[Ae_{1},Ae_{2},\ldots ,Ae_{n}\right]=\left[q_{1}^{1},q_{2}^{1},\ldots ,q_{n}^{1}\right]\left[\begin{matrix}r_{11}^{1}&r_{12}^{1}&\cdots &r_{1n}^{1}\\&r_{22}^{1}&\cdots &r_{2n}^{1}\\&&\ddots &\vdots \\&&&r_{nn}^{1}\end{matrix}\right]$

4. 第二步迭代 $\left[Aq_{1}^{1},Aq_{2}^{1},\ldots ,Aq_{n}^{1}\right]=\left[q_{1}^{2},q_{2}^{2},\ldots ,q_{n}^{2}\right]\left[\begin{matrix}r_{11}^{2}&r_{12}^{2}&\cdots &r_{1n}^{2}\\&r_{22}^{2}&\cdots &r_{2n}^{2}\\&&\ddots &\vdots \\&&&r_{nn}^{2}\end{matrix}\right]$

4. 最终 $R$ 的对角则收敛到相应的特征值。

## QR算法

- 归一化同时迭代算法伪代码

$\overbar{Q}\leftarrow I$

$C\leftarrow I$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$B\leftarrow A\overbar{Q}$

$\mathbf{i}\mathbf{f} \left\|B-C\right\|<TOL$  $\mathbf{d}\mathbf{o}$

$\mathbf{O}\mathbf{u}\mathbf{t}\mathbf{p}\mathbf{u}\mathbf{t} 'convergence'$

$\mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$C\leftarrow B$

$B\rightarrow \overbar{Q}R$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- 归一化同时迭代算法

$\overbar{Q}_{0}=I$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$A\overbar{Q}_{j}=\overbar{Q}_{j+1}R_{j+1}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$B=A\overbar{Q}_{j}$

收敛判别

$B=\overbar{Q}_{j+1}R_{j+1}$

## QR算法

- 归一化同时迭代算法

$\overbar{Q}_{0}=I$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$A\overbar{Q}_{j}=\overbar{Q}_{j+1}R_{j+1}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- QR算法

$A_{0}\leftarrow A$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$A_{j}=Q_{j}R_{j}$

$A_{j+1}=R_{j}Q_{j}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$A_{j+1}=R_{j}Q_{j}=Q_{j}^{T}A_{j}Q_{j}$

$A_{1}=Q_{0}^{T}A_{0}Q_{0}=Q_{0}^{T}AQ_{0}$

- 归一化同时迭代算法伪代码

$\overbar{Q}\leftarrow I$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$B\leftarrow A\overbar{Q}$

$B\rightarrow \overbar{Q}R$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- QR算法伪代码

$\mathbf{I}\mathbf{n}\mathbf{i}\mathbf{t}\mathbf{i}\mathbf{a}\mathbf{l}\mathbf{i}\mathbf{z}\mathbf{e} A$

$\overbar{Q}\leftarrow I$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} N_{iter}$

$A\rightarrow QR$

$A\leftarrow RQ$

$\overbar{Q}\leftarrow \overbar{Q}Q$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$A_{2}=Q_{1}^{T}A_{1}Q_{1}=Q_{1}^{T}Q_{0}^{T}AQ_{0}Q_{1}$

$A_{j+1}=Q_{j}^{T}\ldots Q_{1}^{T}Q_{0}^{T}AQ_{0}Q_{1}\ldots Q_{j}$

$Q_{0}Q_{1}\ldots Q_{j}A_{j+1}=AQ_{0}Q_{1}\ldots Q_{j}$

$\underbrace{Q_{0}Q_{1}\ldots Q_{j}Q_{j+1}}_{\overbar{Q}_{j+1}}R_{j+1}=A\underbrace{Q_{0}Q_{1}\ldots Q_{j}}_{\overbar{Q}_{j}}$

## QR方法

- 定理：设 $A\in \mathbb{R}^{n\times n}$ ,则存在正交阵 $Q$ ，使得 $Q^{T}AQ=\left[\begin{matrix}R_{11}&\cdots &R_{1m}\\0&\ddots &\vdots \\0&0&R_{mm}\end{matrix}\right]$ ,其中 $R_{ii}$ 至多为二阶块矩阵（实Schur型）。若 $R_{ii}$ 是一阶，其元素是 $A$ 的特征值。若 $R_{ii}$ 是二阶，其特征值是 $A$ 的一对共轭特征值。

- 定理：假设 $n$ 阶实对称矩阵 $A$ 有 $n$ 个不同的特征值，则QR算法 $A_{j}$ 将会收敛于对角阵， $\overbar{Q}_{j}=Q_{1}\ldots Q_{j}$ 收敛到正交矩阵，对应的列是特征向量。

- 定理：如果非奇异矩阵 $A\in \mathbb{R}^{n\times n}$ 有 $n$ 个不同的特征值，则QR算法 $A_{j}$ 将会收敛于实Schur型）。

## QR算法

- 例：用QR算法求 $A$ 的所有特征值

$A=\left[\begin{matrix}-4&14&0\\-5&13&0\\-1&0&2\end{matrix}\right], \lambda =6,3,2$

## QR算法

QR迭代 $(TOL=10^{-6})$ 的收敛过程

![](images/e7f5a6ec99dcc524fd667b5fbd663210ca77c4d314d548a2ec2b70e8ac966d31.jpg)

![](images/0c9f026435cba38c8dcfe34f7ce5f410420ec6d1ea0f54199bd37379e99246ec.jpg)

## QR算法

- 例：用QR算法求 $A$ 的所有特征值

$A=\left[\begin{matrix}1&2&1\\2&3&1\\1&1&3\end{matrix}\right]$

## QR算法

QR迭代 $(TOL=10^{-6})$ 的收敛过程

![](images/c8665406261fcfeb2e5e1f850c5b322c386c9cce4c8bab020888d3566481fe1f.jpg)

![](images/a4d041e6492d57d7c3b804062cb7aee261756e1aece1d070251d8972f18e1d74.jpg)

## 思考与练习

- 如果 $A$ 是一个 $6\times 6$ 方阵，对应的特征值为 $-6,-3,1,2,5,7$ 。如下算法可以找出 $A$ 的哪个特征值？并说明理由。 $(a)$ 幂迭代， $(b)$ 逆向幂迭代，平移 $\mu =4.$  $(c)$ 找出两种算法的线性收敛率，哪种收敛会更快？
- 对 $A$ 进行完全QR分解 $A=\left[\begin{matrix}-4&-4\\-2&7\\4&-5\end{matrix}\right]$
- 编程用幂迭代和逆幂迭代各迭代12次求 $A$ 的模最大和模最小的特征值，初始向量取 $x_{0}=\left[1,1,1\right]^{T}$ 。

$A=\left[\begin{matrix}8&-8&-4\\12&-15&-7\\-18&26&12\end{matrix}\right]$