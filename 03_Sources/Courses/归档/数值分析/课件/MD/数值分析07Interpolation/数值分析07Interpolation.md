---
raw_title: 数值分析07Interpolation
subject: 数值分析07Interpolation
source: 数值分析07Interpolation.pptx
status: mineru解析
parser: mineru
---

## 插值

- 插值基本概念
- 基本的多项式插值：Lagrange插值、Newton插值
- 龙格现象/切比雪夫插值
- 分段插值/样条插值

## 插值基本概念

- 计算机如何表达函数？

1. 已知函数形态

2.未知函数形态

$y$

$y$

$f(x)$

\*

$g(x)$

★

$y=ax+b$

$(x_{1},y_{1})$

$\left(x_{0},y_{0}\right)$

$x$

存储系数： $a,b$

存储点坐标： $\left(x_{0},y_{0}\right), (x_{1},y_{1})$

$x$

$x_{3}$

$x_{4}$

$x_{2}$

$x_{0}$

$x_{1}$

$x^{*}$

存储其中 $m+1$ 个点坐标(有损压缩)： $\left\{\left(x_{0},y_{0}\right), \left(x_{1},y_{1}\right),\ldots \left(x_{m},y_{m}\right)\right\}$

如何计算 $f\left(x^{*}\right)?$

*用已知函数形态* $g(x)$ *去近似* $f\left(x\right): g\left(x_{i}\right)=f\left(x_{i}\right),i=0,\ldots ,m$

$f\left(x^{*}\right)\approx g(x^{*})$

## 插值基本概念

- 插值的应用：

![](images/07e5f38a66d53fcde9845d8e136c3c30aecb1cf7e8d46077d4319a7fd16e7229.png)

数值分析数值分析数值分析数值分析数值分析

Numerical analysis

Numerical analysis

Numerical analysis

Numerical analysis

Numerical analysis

工业设计排版打印

## 插值基本概念

- 插值的应用：PDF文件中的字体

![](images/6b0b1577acd0337035e12810fe2776438bf4ad28d89575e4e30fb02d8f36140f.jpg)

![](images/c559138e5192d4ad051eb017daed829932f9048761d31dd92fcef3ac43cc6e46.jpg)

16段Bézier曲线

Times-Roman T

## 插值基本概念

- 插值问题的数学定义： $f(x)$ 为定义在区间 $[a,b]$ 上的函数， $\left\{x_{i}\right\}_{i=0}^{n}$ 为 $[a,b]$ 上 $m+1$ 个互不相同的点， $\Phi =span\left\{\phi _{0}\left(x\right),\phi _{1}\left(x\right),\ldots ,\phi _{n}(x)\right\}$ ，求 $g\left(x\right)\in \Phi$ 满足: $g\left(x_{i}\right)=f\left(x_{i}\right), i=0,\ldots ,m$
- $\left\{\phi _{0}\left(x\right),\phi _{1}\left(x\right),\ldots ,\phi _{n}(x)\right\}$ 称为基函数。
- 我们关心的问题：存在性、唯一性、如何构造、误差估计等。

## 插值基本概念

- 插值的构造：

设 $g(x)=a_{0}\phi _{0}(x)+\cdots +a_{n}\phi _{n}(x)$

$g\left(x_{i}\right)=f\left(x_{i}\right),i=0,1,\ldots ,m \Longrightarrow \left\{\begin{array}{c}a_{0}\phi _{0}\left(x_{0}\right)+a_{1}\phi _{1}\left(x_{0}\right)+\cdots +a_{n}\phi _{n}\left(x_{0}\right)=f(x_{0})\\a_{0}\phi _{0}\left(x_{1}\right)+a_{1}\phi _{1}\left(x_{1}\right)+\cdots +a_{n}\phi _{n}\left(x_{1}\right)=f(x_{1})\\\vdots \\a_{0}\phi _{0}\left(x_{m}\right)+a_{1}\phi _{1}\left(x_{m}\right)+\cdots +a_{n}\phi _{n}\left(x_{m}\right)=f(x_{n})\end{array}\right.$

$M_{\left(m+1\right)\times \left(n+1\right)}:=\left[\begin{matrix}\phi _{0}\left(x_{0}\right)&\phi _{1}\left(x_{0}\right)&\ldots &\phi _{n}\left(x_{0}\right)\\\phi _{0}\left(x_{1}\right)&\phi _{1}\left(x_{1}\right)&\ldots &\phi _{n}\left(x_{1}\right)\\\vdots &\vdots &\ddots &\vdots \\\phi _{0}\left(x_{m}\right)&\phi _{1}\left(x_{m}\right)&\ldots &\phi _{n}\left(x_{m}\right)\end{matrix}\right], \begin{matrix}a:=\left[a_{0},a_{1},\ldots ,a_{n}\right]^{T}\\f:=\left[f\left(x_{0}\right),f\left(x_{1}\right),\ldots f\left(x_{m}\right)\right]^{T}\end{matrix}\Longrightarrow Ma=f$

- $Ma=f$ 存在唯一解的充分条件？

1. $m=n$
2. 系数矩阵 $M$ 可逆

## 基本的多项式插值

- 多项式插值： $\Phi =P_{n}\left(x\right)=span\left\{1,x,x^{2},\cdots x^{n}\right\}$

$M=\left[\begin{matrix}\phi _{0}\left(x_{0}\right)&\phi _{1}\left(x_{0}\right)&\ldots &\phi _{n}\left(x_{0}\right)\\\phi _{0}\left(x_{1}\right)&\phi _{1}\left(x_{1}\right)&\ldots &\phi _{n}\left(x_{1}\right)\\\vdots &\vdots &\ddots &\vdots \\\phi _{0}\left(x_{n}\right)&\phi _{1}\left(x_{n}\right)&\ldots &\phi _{n}\left(x_{n}\right)\end{matrix}\right]=\left[\begin{matrix}1&x_{0}&\ldots &x_{0}^{n}\\1&x_{1}&\ldots &x_{1}^{n}\\\vdots &\vdots &\ddots &\vdots \\1&x_{n}&\ldots &x_{n}^{n}\end{matrix}\right]$

$\left|M\right|=\prod_{0\leq j<i\leq n}^{}(x_{i}-x_{j})\ne 0$

Vandermonde矩阵

## 基本的多项式插值

- 例:求经过 $\left\{(x_{i},y_{i})\right\}_{i=0}^{2}=\left\{\left(1,6\right),\left(2,1\right),\left(3,12\right)\right\}$ 的二次多项式。

解：设 $P_{3}\left(x\right)=a_{0}+a_{1}x+a_{2}x^{2}$

$\left[\begin{matrix}1^{0}&1&1^{2}\\2^{0}&2&2^{2}\\3^{0}&3&3^{2}\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\a_{2}\end{matrix}\right]=\left[\begin{matrix}6\\1\\12\end{matrix}\right]$

$\left[a_{0},a_{1},a_{2}\right]^{T}=[27,-29,8]$

![](images/6881c20a48cd69aa19dd7f4e2e28f0813917a7078bd211e5dc43e19ad0f52366.jpg)

函数图像

## 基本的多项式插值

- 用Gauss消元法求解 $Va=b$

$V=\left[\begin{matrix}1&x_{0}&\ldots &x_{0}^{n}\\1&x_{1}&\ldots &x_{1}^{n}\\\vdots &\vdots &\ddots &\vdots \\1&x_{n}&\ldots &x_{n}^{n}\end{matrix}\right], x_{n}=n+1, b=V\left[1,1,\ldots ,1 \right]^{T}$

## 基本的多项式插值

![](images/6a0203f30930421956735ca044890947bce763fb4c2bc884c37150d7befa60e5.jpg)

![](images/c16f96e4ea704e7db48521a84198e9e0e45dfc53f2b9021ff4f85b48957e5db7.jpg)

![](images/cc7c7cb66f63db7a7f5c6b219d900af7d84b0e33d82a38d9cfa611e6659e6d5b.jpg)

$a=$

$a=$

$n=10$

$n=20$

- 基本多项式插值
- 优点： $P_{n}\left(x\right)=a_{0}+a_{1}x+\ldots +a_{n}x^{n}$ 构造好之后计算简单
- 缺点：系数矩阵是满阵，并且条件数大（病态）

## Lagrange插值

- 如何改进？

优化基函数：设 $g\left(x\right)=a_{0}l_{0}\left(x\right)+a_{1}l_{1}\left(x\right)+\ldots +a_{n}l_{n}\left(x\right)$

$M=\left[\begin{matrix}l_{0}\left(x_{0}\right)&l_{1}\left(x_{0}\right)&\ldots &l_{n}\left(x_{0}\right)\\l_{0}\left(x_{1}\right)&l_{1}\left(x_{1}\right)&\ldots &l_{n}\left(x_{1}\right)\\\vdots &\vdots &\ddots &\vdots \\l_{0}\left(x_{n}\right)&l_{1}\left(x_{n}\right)&\ldots &l_{n}\left(x_{n}\right)\end{matrix}\right]$

如果 $l_{i}\left(x_{j}\right)=\delta _{ij}=\left\{\begin{array}{c}1,i=j\\0, i\ne j\end{array}\right.$

则 $M=\left[\delta _{ij}\right]=I, Ma=f\Longrightarrow a_{i}=f(x_{i})$

## Lagrange插值

- 如何求 $\{l_{i}(x)\}_{i=0}^{n}$ ？

1.条件1： $l_{i}\left(x_{j}\right)=0 (j=0,..,n;j\ne i)$

$\Longrightarrow l_{i}\left(x\right)=C_{i}\left(x-x_{0}\right)\ldots \left(x-x_{i-1}\right)\left(x-x_{i+1}\right)\ldots \left(x-x_{n}\right)$

2.条件2： $l_{i}\left(x_{i}\right)=1$

$\Longrightarrow C_{i}=\frac{1}{\left(x_{i}-x_{0}\right)\ldots \left(x_{i}-x_{i-1}\right)\left(x_{i}-x_{i+1}\right)\ldots \left(x_{i}-x_{n}\right)}$

3.

$l_{i}\left(x\right)=\frac{\left(x-x_{0}\right)\ldots \left(x-x_{i-1}\right)\left(x-x_{i+1}\right)\ldots \left(x-x_{n}\right)}{\left(x_{i}-x_{0}\right)\ldots \left(x_{i}-x_{i-1}\right)\left(x_{i}-x_{i+1}\right)\ldots \left(x_{i}-x_{n}\right)}$

- 最终的插值函数：

$g\left(x\right)=\sum_{i=0}^{n}f\left(x_{i}\right)l_{i}(x)$

## Lagrange插值

- 具体算法：

$Given n+1 points \left(x_{0},y_{0}\right), \left(x_{1},y_{1}\right),\ldots ,\left(x_{n},y_{n}\right)$

$g(x)=0$

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n$  **do**

$t=1$

$\mathbf{f}\mathbf{o}\mathbf{r} j=0 \mathbf{t}\mathbf{o} i-1$  **do**

$t\leftarrow t*(x-x_{j})/(x_{i}-x_{j})$

**end for**

$\mathbf{f}\mathbf{o}\mathbf{r} j=i+1 \mathbf{t}\mathbf{o} n$  **do**

$t\leftarrow t*(x-x_{j})/(x_{i}-x_{j})$

**end for**

$g\left(x\right)\leftarrow g\left(x\right)+t*y_{i}$

**end for**

$t=l_{i}\left(x\right)=\frac{\left(x-x_{0}\right)\left(x-x_{1}\right)\ldots \left(x-x_{i-1}\right)\left(x-x_{i+1}\right)\ldots \left(x-x_{n}\right)}{\left(x_{i}-x_{0}\right)\left(x_{i}-x_{1}\right)\ldots \left(x_{i}-x_{i-1}\right)\left(x_{i}-x_{i+1}\right)\ldots \left(x_{i}-x_{n}\right)}$

$g\left(x\right)=\sum_{i=0}^{n}f\left(x_{i}\right)l_{i}(x)$

## Lagrange插值

- 例：求经过 $\left\{(x_{i},y_{i})\right\}_{i=0}^{2}=\{\left(1,6\right),\left(2,1\right),\left(3,12\right)\}$ 的二次多项式。

$P_{3}\left(x\right)=$

$=3\left(x^{2}-5x+6\right)-\left(x^{2}-4x+3\right)+6(x^{2}-3x+2)$

$=8x^{2}-29x+27$

$6\frac{(x-2)(x-3)}{(1-2)(1-3)}$

$+1\frac{(x-1)(x-3)}{(2-1)(2-3)}$

$+12\frac{(x-1)(x-2)}{(3-1)(3-2)}$

## Lagrange插值

- 例：已知 $\sin(\frac{\pi }{6})=\frac{1}{2} \hspace{0.33em} , \hspace{0.33em} \hspace{0.33em} \sin(\frac{\pi }{4})=\frac{1}{\sqrt{2}} \hspace{0.33em} , \hspace{0.33em} \hspace{0.33em} \sin(\frac{\pi }{3})=\frac{\sqrt{3}}{2}$

利用多项式插值计算 $\sin(50^{\circ })=\sin(\frac{5\pi }{18})$

解：1. 利用 $x_{0}=\frac{\pi }{6} \hspace{0.33em} , \hspace{0.33em} x_{1}=\frac{\pi }{4}$ 做1次Lagrange插值得：

$P_{1}\left(x\right)=\frac{1}{2}\times \frac{x-\frac{\pi }{4}}{\frac{\pi }{6}-\frac{\pi }{4}}+\frac{1}{\sqrt{2}}\times \frac{x-\frac{\pi }{6}}{\frac{\pi }{4}-\frac{\pi }{6}}$

$\sin(\frac{5\pi }{18})\approx P_{1}\left(\frac{5\pi }{18}\right)\approx 0.77614, error\approx -0.01001$

2. 利用 $x_{1}=\frac{\pi }{4} \hspace{0.33em} , \hspace{0.33em} x_{2}=\frac{\pi }{3}$ 做1次Lagrange插值得：

$\tilde{P}_{1}\left(x\right)=\frac{1}{\sqrt{2}}\times \frac{x-\frac{\pi }{3}}{\frac{\pi }{4}-\frac{\pi }{3}}+\frac{\sqrt{3}}{2}\times \frac{x-\frac{\pi }{4}}{\frac{\pi }{3}-\frac{\pi }{4}}$

$\sin(\frac{5\pi }{18})\approx \tilde{P}_{1}\left(\frac{5\pi }{18}\right)\approx 0.76008, error\approx 0.00596$

**sin 50 = 0.7660444…**

## Lagrange插值

3. 利用 $x_{0}=\frac{\pi }{6} \hspace{0.33em} , x_{1}=\frac{\pi }{4} \hspace{0.33em} , \hspace{0.33em} x_{2}=\frac{\pi }{3}$ 做2次Lagrange插值得：

$P_{2}\left(x\right)=\frac{1}{2}\times \frac{\left(x-\frac{\pi }{4}\right)\left(x-\frac{\pi }{3}\right)}{\left(\frac{\pi }{6}-\frac{\pi }{4}\right)\left(\frac{\pi }{6}-\frac{\pi }{3}\right)}+\frac{1}{\sqrt{2}}\times \frac{\left(x-\frac{\pi }{6}\right)\left(x-\frac{\pi }{3}\right)}{\left(\frac{\pi }{4}-\frac{\pi }{6}\right)\left(\frac{\pi }{4}-\frac{\pi }{3}\right)}+\frac{\sqrt{3}}{2}\times \frac{\left(x-\frac{\pi }{6}\right)\left(x-\frac{\pi }{4}\right)}{\left(\frac{\pi }{3}-\frac{\pi }{6}\right)\left(\frac{\pi }{3}-\frac{\pi }{4}\right)}$

$\sin(\frac{5\pi }{18})\approx P_{2}\left(\frac{5\pi }{18}\right)\approx 0.76543, error\approx 0.00061$

## Lagrange插值

![](images/89219b57bae411472e31f48de1755a6dbcc2f8a44a693ec16344bff6531c1ab4.jpg)

$y=\sin(\left(x\right))$

$\frac{3\pi }{2}$

$\pi$

$2\pi$

$\frac{\pi }{2}$

- $\sin(x)$ 的对称性与反对称性：

$\sin(x)=\sin(\left(\pi -x\right)),\sin(x)=-\sin(\left(2\pi -x\right))$

- 用 $\sin(x)$ 在基础域 $x\in \left[0,\frac{\pi }{2}\right]$ 的近似多项式 $P\left(x\right)$ ，可以计算 $\sin(x)$ 在 $x\in \mathbb{R}$ 的近似值

## Lagrange插值

![](images/4481110a544d8f7b435d1dbb9d6f355dc8dd248164a5b9dd09daf0b0ee2d8871.jpg)

用3次多项式 $P_{3}\left(x\right)$ 插值近似 $sinx$

插值节点 $\left\{x_{i}\right\}_{i=0}^{3}=\left\{0,\frac{\pi }{6},\frac{\pi }{3},\frac{\pi }{2}\right\}$

![](images/97435edce8515f72f352d122efaa643d09f14c9e08d32b18111cea8e6acf44ed.jpg)

$P_{3}(x)$ 在不同点的近似误差

## Lagrange插值

- 例：所有自然数的倒数的平方和(Basel问题,由皮耶特罗·门戈利在1644年提出，有欧拉在1735年解决,Basel是欧拉的故乡)

$S=1+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\ldots =?$

![](images/577a28daa5db7dfb35237fdeeb0f412a3b8a5d95d7c93240c4274d12e79c959e.jpg)

欧拉(1707-1783)

## Lagrange插值

$=\frac{x}{1!}-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\ldots (Maclaurin series)$

$y=\sin(\left(x\right))$

$-5\pi$

$-4\pi$

$-3\pi$

$-2\pi$

$-\pi$

$0$

$\pi$

$2\pi$

$3\pi$

$4\pi$

$5\pi$

插值： $\sin(\left(x\right)=Cx\left(x+\pi \right)\left(x-\pi \right)\left(x+2\pi \right)\left(x-2\pi \right)\ldots )=Cx\left(x^{2}-\pi ^{2}\right)\left(x^{2}-\left(2\pi \right)^{2}\right)\ldots$

求导： $sin^{'}\left(0\right)=C\left(0-\pi ^{2}\right)\left(0-\left(2\pi \right)^{2}\right)\ldots =1$

$\sin(\left(x\right))=\frac{x\left(x^{2}-\pi ^{2}\right)\left(x^{2}-\left(2\pi \right)^{2}\right)\ldots }{\left(0-\pi ^{2}\right)\left(0-\left(2\pi \right)^{2}\right)\ldots }=x\left(1-\frac{x^{2}}{\pi ^{2}}\right)\left(1-\frac{x^{2}}{\left(2\pi \right)^{2}}\right)\ldots$

$x^{3}的系数=-\left(\frac{1}{\pi ^{2}}+\frac{1}{\left(2\pi \right)^{2}}+\frac{1}{\left(3\pi \right)^{2}}+\ldots \right)$

$=-\frac{1}{3!}\Longrightarrow S=1+\frac{1}{2^{2}}+\frac{1}{3^{2}}+\ldots =\frac{\pi ^{2}}{6}$

## Newton插值

- 已知经过 $\left\{x_{i}\right\}_{i=0}^{n}$ 的插值多项式为 $P_{n}(x)$ ,求经过 $\left\{x_{i}\right\}_{i=0}^{n}\bigcup_{}^{}x_{n+1}$ 的插值多项式 $P_{n+1}(x)$ ？
- 令 $P_{n+1}\left(x\right)=P_{n}\left(x\right)+Q_{n+1}(x)$

$P_{n}(x)$ 和 $P_{n+1}(x)$ 都经过 $\left\{x_{i}\right\}_{i=0}^{n} \Longrightarrow Q_{n+1}\left(x_{i}\right)=0\left(i=0,..,n\right)$

$\Longrightarrow Q_{n+1}\left(x\right)=a_{n+1}\left(x-x_{0}\right)\ldots \left(x-x_{n}\right)$

- 递推得到Newton插值： $P_{n}\left(x\right)=a_{0}+a_{1}\left(x-x_{0}\right)+\ldots +a_{n}\left(x-x_{0}\right)\ldots \left(x-x_{n-1}\right)$
- 基函数： $N_{0}\left(x\right)=1,N_{1}\left(x\right)=x-x_{0},\ldots ,N_{n}\left(x\right)=\left(x-x_{0}\right)(x-x_{1})\ldots \left(x-x_{n-1}\right)$

## Newton插值

- 基本多项式插值基函数： $\left\{1,x,x^{2},\ldots \right\}$
- Lagrange插值基函数： $l_{i}\left(x\right)=\frac{\left(x-x_{0}\right)\ldots \left(x-x_{i-1}\right)\left(x-x_{i+1}\right)\ldots \left(x-x_{n}\right)}{\left(x_{i}-x_{0}\right)\ldots \left(x_{i}-x_{i-1}\right)\left(x_{i}-x_{i+1}\right)\ldots \left(x_{i}-x_{n}\right)}$
- Newton插值基函数： $N_{i}\left(x\right)=\left(x-x_{0}\right)(x-x_{1})\ldots \left(x-x_{i-1}\right)$
- 不同插值方式是否等价？经过相同点的多项式插值是否唯一？
- 多项式插值定理：若 $x_{0},\ldots ,x_{n}$ 是不同的实数，则对任意数值 $y_{0},\ldots ,y_{n}$ 存在唯一的次数至多是 $n$ 的多项式 $P_{n}(x)$ 使得

$P_{n}\left(x_{i}\right)=y_{i} \left(0\leq i\leq n\right)$

- 经过 $\left(x_{0},y_{0}\right),\left(x_{1},y_{1}\right),\ldots ,(x_{n},y_{n})$ 的次数是 $n+1$ 的多项式 $P_{n+1}(x)$ 有多少个？

## Newton插值

- 基函数： $N_{0}\left(x\right)=1,N_{1}\left(x\right)=x-x_{0},N_{2}\left(x\right)=\left(x-x_{0}\right)\left(x-x_{1}\right),\ldots ,N_{n}\left(x\right)=\left(x-x_{0}\right)(x-x_{1})\ldots \left(x-x_{n-1}\right)$
- $N_{j}\left(x_{i}\right)=\left(x_{i}-x_{0}\right)(x_{i}-x_{1})\ldots \left(x_{i}-x_{j-1}\right)$ ,当 $i<j$ 时， $N_{j}\left(x_{i}\right)=0$
- $Ma=f$ 的系数矩阵：

$M=\left[\begin{matrix}N_{0}\left(x_{0}\right)&N_{1}\left(x_{0}\right)&N_{2}\left(x_{0}\right)&\ldots &N_{n}\left(x_{0}\right)\\N_{0}\left(x_{1}\right)&N_{1}\left(x_{1}\right)&N_{2}\left(x_{1}\right)&\ldots &N_{n}\left(x_{1}\right)\\N_{0}\left(x_{2}\right)&N_{1}\left(x_{2}\right)&N_{2}\left(x_{2}\right)&\ldots &N_{n}\left(x_{2}\right)\\\vdots &\vdots &\vdots &\ddots &\vdots \\N_{0}\left(x_{n}\right)&N_{1}\left(x_{n}\right)&N_{2}\left(x_{n}\right)&\ldots &N_{n}\left(x_{n}\right)\end{matrix}\right]$

$=\left[\begin{matrix}1&0&0&\ldots &0\\1&x_{1}-x_{0}&0&\ldots &0\\1&x_{2}-x_{0}&\left(x_{2}-x_{0}\right)\left(x_{2}-x_{1}\right)&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&x_{n}-x_{0}&\left(x_{n}-x_{0}\right)\left(x_{n}-x_{1}\right)&\ldots &\prod_{j=0}^{n-1}\left(x_{n}-x_{j}\right)\end{matrix}\right]$

下三角阵

## Newton插值

- *求解* $Ma=f$ *：*

$\left[\begin{matrix}1&0&0&\ldots &0\\1&x_{1}-x_{0}&0&\ldots &0\\1&x_{2}-x_{0}&\left(x_{2}-x_{0}\right)\left(x_{2}-x_{1}\right)&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\1&x_{n}-x_{0}&\left(x_{n}-x_{0}\right)\left(x_{n}-x_{1}\right)&\ldots &\prod_{j=0}^{n-1}\left(x_{n}-x_{j}\right)\end{matrix}\right]\left[\begin{array}{c}a_{0}\\a_{1}\\a_{2}\\\vdots \\a_{n}\end{array}\right]=\left[\begin{array}{c}f_{0}\\f_{1}\\f_{2}\\\vdots \\f_{n}\end{array}\right]$

- 定义：Newton插值的系数 $a_{n}:=f[x_{0},x_{1},x_{2},\ldots ,x_{n} ]$ 称为 $n$ 阶Newton差商。

## Newton插值

- 例： $n=2$ 时， $Ma=f$

$\left[\begin{matrix}1&0&0\\1&x_{1}-x_{0}&0\\1&x_{2}-x_{0}&\left(x_{2}-x_{0}\right)\left(x_{2}-x_{1}\right)\end{matrix}\right]\left[\begin{array}{c}a_{0}\\a_{1}\\a_{2}\end{array}\right]=\left[\begin{array}{c}f\left(x_{0}\right)\\f\left(x_{1}\right)\\f\left(x_{2}\right)\end{array}\right]$

$a_{0}:=f\left[x_{0}\right]=f\left(x_{0}\right)$

$a_{0}+a_{1}\left(x_{1}-x_{0}\right)=f\left(x_{1}\right)\Longrightarrow a_{1}:=f\left[x_{0},x_{1}\right]=\frac{f\left(x_{1}\right)-a_{0}}{x_{1}-x_{0}}=\frac{f\left[x_{1}\right]-f\left[x_{0}\right]}{x_{1}-x_{0}}$

$a_{0}+a_{1}\left(x_{2}-x_{0}\right)+a_{2}\left(x_{2}-x_{0}\right)\left(x_{2}-x_{1}\right)=f\left(x_{2}\right)$

$\Longrightarrow a_{2}:=f\left[x_{0},x_{1},x_{2}\right]=\frac{1}{x_{2}-x_{1}}\left(\frac{f\left(x_{2}\right)-a_{0}}{x_{2}-x_{0}}-a_{1}\right)=\frac{f\left[x_{0},x_{2}\right]-f\left[x_{0},x_{1}\right]}{x_{2}-x_{1}}$

## Newton插值

- Newton差商性质：

1.对称性： $f\left[x_{i_{0}}, x_{i_{1}},\ldots ,x_{i_{n}}\right]=f\left[x_{0}, x_{1},\ldots ,x_{n}\right], \{i_{0},i_{1},\ldots i_{n}\}$ 关于 $\{0,1,\ldots ,n\}$ 的任意排列。

例： $f\left[x_{0},x_{1}\right]=\frac{f\left[x_{1}\right]-f\left[x_{0}\right]}{x_{1}-x_{0}},f\left[x_{1},x_{0}\right]=\frac{f\left[x_{0}\right]-f\left[x_{1}\right]}{x_{0}-x_{1}}=f\left[x_{0},x_{1}\right]$

2.递推性： $\underset{n阶差商}{a_{n}:=\underbrace{f\left[x_{0}, x_{1},\ldots ,x_{n-1},x_{n}\right]}}=\frac{\overbrace{f\left[x_{1},\ldots ,x_{n-1},x_{n}\right]}^{n-1阶差商}-\overbrace{f\left[x_{0},x_{1},\ldots ,x_{n-1}\right]}^{n-1阶差商}}{x_{n}-x_{0}}$

例： $f\left[x_{0},x_{1}\right]=\frac{f\left[x_{1}\right]-f\left[x_{0}\right]}{x_{1}-x_{0}}, f\left[x_{0},x_{1},x_{2}\right]=f\left[x_{1},x_{0},x_{2}\right]=\frac{f\left[x_{0},x_{2}\right]-f\left[x_{0},x_{1}\right]}{x_{2}-x_{1}}$

## Newton插值

- 差商计算流程

$x_{0},f\left[x_{0}\right]$

$f[x_{0},x_{1}]$

$f[x_{0},x_{1},x_{2}]$

$f[x_{0},x_{1},x_{2},x_{3}]$

$x_{1},f\left[x_{1}\right]$

$f[x_{1},x_{2}]$

$f[x_{1},x_{2},x_{3}]$

$x_{2},f\left[x_{2}\right]$

$f[x_{2},x_{3}]$

$x_{3},f\left[x_{3}\right]$

## Newton插值

- 例：求经过 $\{\left(1,6\right),\left(2,1\right),\left(3,12\right)\}$ 的二次多项式。

解：计算差商

①

⑤

$(1,6)$

$-5$

$8$

②

⑥

$(2,1)$

$11$

③

④

$(3,12)$

①+⑤ $\rightarrow P_{2}\left(x\right)=6-5\left(x-1\right)+8(x-1)(x-2)$

②+⑤ $\rightarrow =1-5\left(x-2\right)+8(x-2)(x-1)$

③+⑥ $\rightarrow =1+11\left(x-2\right)+8(x-2)(x-3)$

*④+⑥* $\rightarrow =12+11\left(x-3\right)+8\left(x-3\right)\left(x-2\right)$

$=8x^{2}-29x+27$

## Newton插值

- 差商算法：记 $c_{ij}=f\left[x_{i},x_{i+1},\ldots ,x_{i+j}\right]$ ，则差商计算表可以表示为

$c_{ij}=f\left[x_{i},x_{i+1},\ldots ,x_{i+j}\right]=\frac{f\left[x_{i+1},\ldots ,x_{i+j}\right]-f\left[x_{i},x_{i+1},\ldots ,x_{i+j-1}\right]}{x_{i+j}-x_{i}}=\frac{c_{i+1,j-1}-c_{i,j-1}}{x_{i+j}-x_{i}}$

<table>
  <tr>
    <th>$x_0$</th>
    <th>$c_{00}$</th>
    <th>$c_{01}$</th>
    <th>$c_{02}$</th>
    <th>$c_{03}$</th>
    <th>$\cdots $</th>
    <th>$c_{0,n-1}$</th>
    <th>$c_{0n}$</th>
  </tr>
  <tr>
    <td>$x_1$</td>
    <td>$c_{10}$</td>
    <td>$c_{11}$</td>
    <td>$c_{12}$</td>
    <td>$c_{13}$</td>
    <td>$\cdots $</td>
    <td>$c_{1,n-1}$</td>
    <td></td>
  </tr>
  <tr>
    <td>$x_2$</td>
    <td>$c_{20}$</td>
    <td>$c_{21}$</td>
    <td>$c_{22}$</td>
    <td>$\cdots $</td>
    <td>$c_{2,n-2}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$x_3$</td>
    <td>$c_{30}$</td>
    <td>$c_{31}$</td>
    <td>$\cdots $</td>
    <td>$c_{3,n-3}$</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$⋰$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$x_{n-1}$</td>
    <td>$c_{n-1,0}$</td>
    <td>$c_{n-1,1}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$x_n$</td>
    <td>$c_{n0}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

%Initialization

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n$  **do**

$c_{i0}\leftarrow f(x_{i})$

**end for**

%Computing Newton difference quotient

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$  **do**

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n-j$  **do**

$c_{ij}\leftarrow (c_{i+1,j-1}-c_{i,j-1})/(x_{i+j}-x_{i})$

**end for**

**end for**

## Newton插值

$\Longrightarrow a_{i}\longleftarrow \frac{a_{i+1}-a_{i}}{x_{i+j}-x_{i}}$

$c_{ij}=\frac{c_{i+1,j-1}-c_{i,j-1}}{x_{i+j}-x_{i}}$

- 优化的程序设计方式：

<table>
  <tr>
    <th>$a_0$</th>
    <th>$x_0$</th>
    <th>$c_{00}$</th>
    <th>$c_{01}$</th>
    <th>$c_{02}$</th>
    <th>$c_{03}$</th>
    <th>$\cdots $</th>
    <th>$c_{0,n-1}$</th>
    <th>$c_{0n}$</th>
  </tr>
  <tr>
    <td>$a_1$</td>
    <td>$x_1$</td>
    <td>$c_{10}$</td>
    <td>$c_{11}$</td>
    <td>$c_{12}$</td>
    <td>$c_{13}$</td>
    <td>$\cdots $</td>
    <td>$c_{1,n-1}$</td>
    <td></td>
  </tr>
  <tr>
    <td>$a_2$</td>
    <td>$x_2$</td>
    <td>$c_{20}$</td>
    <td>$c_{21}$</td>
    <td>$c_{22}$</td>
    <td>$\cdots $</td>
    <td>$c_{2,n-2}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_3$</td>
    <td>$x_3$</td>
    <td>$c_{30}$</td>
    <td>$c_{31}$</td>
    <td>$\cdots $</td>
    <td>$c_{3,n-3}$</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$⋰$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_{n-1}$</td>
    <td>$x_{n-1}$</td>
    <td>$c_{n-1,0}$</td>
    <td>$c_{n-1,1}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_n$</td>
    <td>$x_n$</td>
    <td>$c_{n0}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

%Initialization

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n$  **do**

$a_{i}\longleftarrow f(x_{i})$

**end for**

%Computing Newton difference quotient

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$  **do**

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n-j$  **do**

$a_{i}\leftarrow (a_{i+1}-a_{i})/(x_{i+j}-x_{i})$

**end for**

**end for**

内存分配插值多项式

$P_{n}\left(x\right)=a_{n}+a_{n-1}\left(x-x_{n}\right)+a_{n-2}\left(x-x_{n}\right)\left(x-x_{n-1}\right)+\ldots +a_{0}\left(x-x_{n}\right)\left(x-x_{n-1}\right)\ldots (x-x_{1})$

## Newton插值

- Newton插值伪代码：

%Initialization

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n$  **do**

$a_{i}\longleftarrow f(x_{i})$

**end for**

%Computing Newton difference quotient

$\mathbf{f}\mathbf{o}\mathbf{r} j=1 \mathbf{t}\mathbf{o} n$  **do**

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n-j$ **do**

$a_{i}\leftarrow (a_{i+1}-a_{i})/(x_{i+j}-x_{i})$

**end for**

**end for**

%Computing $f(x)$

$f(x)\longleftarrow a_{0}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} n$ **do**

$f\left(x\right)\leftarrow a_{i}+\left(x-x_{i}\right)*f(x)$    %秦九韶算法

**end for**

$i=1, f\left(x\right)=a_{1}+a_{0}\left(x-x_{1}\right)$

$i=2, f\left(x\right)=a_{2}+a_{1}\left(x-x_{2}\right)+a_{0}\left(x-x_{2}\right)\left(x-x_{1}\right)$

$i=3, f\left(x\right)=a_{3}+a_{2}(x-x_{3})+a_{1}(x-x_{3})\left(x-x_{2}\right)+a_{0}(x-x_{3})\left(x-x_{2}\right)\left(x-x_{1}\right)$

$i=n,f\left(x\right)=a_{n}+a_{n-1}\left(x-x_{n}\right)+a_{n-2}\left(x-x_{n}\right)\left(x-x_{n-1}\right)+\ldots +a_{0}\left(x-x_{n}\right)\left(x-x_{n-1}\right)\ldots (x-x_{1})$

## Newton插值

- 已知经过 $\left\{x_{i}\right\}_{i=0}^{n}$ 的插值多项式为 $P_{n}(x)$ ,求经过 $\left\{x_{i}\right\}_{i=0}^{n}\bigcup_{}^{}x_{n+1}$ 的插值多项式 $P_{n+1}(x)$ ？

<table>
  <tr>
    <th>$a_0$</th>
    <th>$x_0$</th>
    <th>$c_{00}$</th>
    <th>$c_{01}$</th>
    <th>$c_{02}$</th>
    <th>$c_{03}$</th>
    <th>$\cdots $</th>
    <th>$c_{0,n-1}$</th>
    <th>$c_{0n}$</th>
    <th>$c_{0,n+1}$</th>
  </tr>
  <tr>
    <td>$a_1$</td>
    <td>$x_1$</td>
    <td>$c_{10}$</td>
    <td>$c_{11}$</td>
    <td>$c_{12}$</td>
    <td>$c_{13}$</td>
    <td>$\cdots $</td>
    <td>$c_{1,n-1}$</td>
    <td>$c_{1,n}$</td>
    <td></td>
  </tr>
  <tr>
    <td>$a_2$</td>
    <td>$x_2$</td>
    <td>$c_{20}$</td>
    <td>$c_{21}$</td>
    <td>$c_{22}$</td>
    <td>$\cdots $</td>
    <td>$c_{2,n-2}$</td>
    <td>$c_{2,n-1}$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_3$</td>
    <td>$x_3$</td>
    <td>$c_{30}$</td>
    <td>$c_{31}$</td>
    <td>$\cdots $</td>
    <td>$c_{3,n-3}$</td>
    <td>$c_{3,n-2}$</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$\vdots $</td>
    <td>$⋰$</td>
    <td>$⋰$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_{n-1}$</td>
    <td>$x_{n-1}$</td>
    <td>$c_{n-1,0}$</td>
    <td>$c_{n-1,1}$</td>
    <td>$c_{n-1,2}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_n$</td>
    <td>$x_n$</td>
    <td>$c_{n0}$</td>
    <td>$c_{n1}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$a_{n+1}$</td>
    <td>$x_{n+1}$</td>
    <td>$c_{n+1,0}$</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

## 不同插值方法的对比

- 基本多项式插值
    - 优点：基函数简单、直观
    - 缺点：系数矩阵满阵、条件数大
- Lagrange插值
    - 优点：插值函数构造简单、直接
    - 缺点：基函数相对复杂
- Newton插值
    - 优点：新增插值点可避免重复计算
    - 缺点：计算牛顿差商需要递推

## 多项式插值的误差

- 多项式插值误差定理：设函数 $f\in C^{n+1}[a,b]$ ， $P_{n}(x)$ 是 $f$ 在区间 $[a,b]$ 的 $n+1$ 个不同点 $x_{0},\ldots ,x_{n}$ 上的次数不超过 $n$ 的插值多项式，则对任意 $x\in [a,b]$ ,都有

$f\left(x\right)-P_{n}\left(x\right)=f[x_{0},\ldots ,x_{n},x]\prod_{i=0}^{n}\left(x-x_{i}\right)$

$=\frac{1}{\left(n+1\right)!}f^{\left(n+1\right)}\left(c\right)\prod_{i=0}^{n}\left(x-x_{i}\right),$

其中， $c\in (a,b)$

## 多项式插值的误差

- 例：用Newton插值拟合 $\sin(x)$ ,插值节点为 $0,\frac{\pi }{6},\frac{\pi }{3},\frac{\pi }{2}$ ,估计插值的误差界。

解： $\sin(x)-P_{3}\left(x\right)=\frac{1}{4!}f^{''''}\left(c\right)x(x-\frac{\pi }{6})(x-\frac{\pi }{3})(x-\frac{\pi }{2})$

$\left|\sin(x)-P_{3}\left(x\right)\right|\leq \frac{1}{24}\left|x(x-\frac{\pi }{6})(x-\frac{\pi }{3})(x-\frac{\pi }{2})\right|$

$\left|\sin(1)-P_{3}\left(1\right)\right|\leq \frac{1}{24}\left| \left(1-\frac{\pi }{6}\right)\left(1-\frac{\pi }{3}\right)\left(1-\frac{\pi }{2}\right)\right|\approx 0.0005348$

$\left|\sin(0.2)-P_{3}\left(0.2\right)\right|\leq \frac{1}{24}\left| 0.2\left(0.2-\frac{\pi }{6}\right)\left(0.2-\frac{\pi }{3}\right)\left(0.2-\frac{\pi }{2}\right)\right|\approx 0.00313$

在 $x=1,0.2$ 处的实际误差分别为 $0.0004$ 和 $0.00189$

## Runge现象

- 插值节点越多越好？

多项式插值 $\sin(\pi x)$ (等距节点)

## Runge现象

- 例：等距插值Runge函数（1901年）：

$f\left(x\right)=\frac{1}{1+25x^{2}}, x\in [-1,1]$

## Runge现象

- *插值*误差

$f\left(x\right)-P_{n}\left(x\right)=\frac{1}{\left(n+1\right)!}f^{\left(n+1\right)}\left(c\right)\prod_{i=0}^{n}\left(x-x_{i}\right), c\in \left(-1,1\right)$

![](images/7c1c671667bbd295a89869eec26405b13a7c6baa5d400938d1128533838b709c.jpg)

$f^{''}(x)$

![](images/f7d67a65278dc6aab35df44e60c188596291a7bd16fa9066290f25b7b7089c9b.jpg)

$f^{(10)}(x)$

![](images/03f8f37924d67d6a0f7f9f90b0f6ed2e8b220f172e15e28d406e564fb0ce5099.jpg)

$f^{(20)}(x)$

## Runge现象

- 例：等距多项式插值三角形突起函数

![](images/5df17473041a929198a3e624caa0d47e1be35b6898c44b632fa478e029719e2c.jpg)

插值函数在端点附近产生剧烈振荡

## Runge现象

- 如何解决？

1. 振荡发生在端点附近，可在区域外选取额外的插值节点
2. 通过调整插值节点的位置，尽量减小插值误差限

$f\left(x\right)-P_{n}\left(x\right)=\frac{1}{\left(n+1\right)!}f^{\left(n+1\right)}\left(c\right)\prod_{i=0}^{n}\left(x-x_{i}\right)$

## Chebyshev多项式

![](images/89de8747584040ca5c5cb4a6897b35d52b66bd0056af49e5255b595e74a2a707.jpg)

- Chebyshev是俄国现代数学的开创者之一他是优秀的纯粹数学家， 也是名副其实的应用数学家。他创建的彼得堡学派具有鲜明的理论联系实际的特色。著名的Chebyshev多项式就是从连杆设计中升华出来的理论精华 。（科学源流：切比雪夫和切比雪夫多项式的故事）
- “理论和实践日益相互靠近的观点带来了最有益的结果，绝非只是实践一方所取得；在此影响下，科学正在进步，因为这种靠近会衍生出新的研究对象或者使早已熟知的学科产生新的内容。尽管在过去3个世纪以来，由于伟大数学家们的工作，数学取得了长足的进展，但实践清楚地揭示了其在许多方面并不完备；这就为科学提出了具有本质意义的新课题，让人们去挑战，寻找新的方法。而且，如果在新的应用出现或者旧的方法得到发展之时能够取得很多理论成果，那么当有新的方法诞生时这些理论成果就会更加丰硕；这里，科学在实践中找到了一个可靠指南”。（ Chebyshev，1856）

Chebyshev

1821-1894

## Chebyshev多项式

- 第一类 $n$ 阶Chebyshev多项式的定义: $T_{n}\left(x\right)=\cos((ncos^{-1}x))$
- Chebyshev多项式的性质：
    1. 递推关系： $T_{n+1}=2xT_{n}-T_{n-1}$
    2. $T_{n}(x)$ 是 $n$ 次多项式， $n$ 次项系数是 $2^{n-1}\left(n\geq 1\right)$
    3. $T_{n}\left(1\right)=1,T_{n}\left(-1\right)=\left(-1\right)^{n}$
    4. $T_{n}(x)$ 的最大绝对值是1， $x\in [-1,1]$
    5. $T_{n}(x)$ 的零点为 $x=cos\frac{\left(2k+1\right)\pi }{2n}$ , $k=0,1,..,n-1$
    6. $T_{n}\left(\cos(\frac{k\pi }{n})\right)=\left(-1\right)^{k}$ , $k=0,1,..,n.$ 即 $T_{n}(x)$ 达到极值点-1和1共 $n+1$ 次

## Chebyshev多项式

![](images/055331866a7fe04e5761463fc2e161d1dbde23eba43be99bd0b8bf37e206c26b.png)

$T_{n}\left(x\right)=\cos((ncos^{-1}x))$ 的图像

![](images/d54a8dfc7190084455f09c66017f9947da3aba6cc2222afddb2da0721efc1ca8.jpg)

$T_{n}\left(x\right)=\cos((ncos^{-1}x))$ 的零点分布 $(n=15)$

$x_{k}=cos\frac{\left(2k+1\right)\pi }{2n}, k=0,1,\ldots ,n-1$

## Chebyshev多项式

- 定义：首一多项式是指最高次项系数是1的多项式。
- $q\left(x\right)=2^{1-n}T_{n}(x)$ 是首一多项式, $T_{n}(x)$ 是第一类 $n$ 阶Chebyshev多项式。
- 首一多项式定理：若 $p(x)$ 是一个 $n$ 次首一多项式,则

$\max_{-1\leq x\leq 1}\left|p(x)\right|\geq 2^{1-n}=\max_{-1\leq x\leq 1}2^{1-n}\left|T_{n}(x)\right|$

## Chebyshev插值

- 标准区间 $\left[-1,1\right]$ 的Chebyshev插值误差定理：若选取插值节点为 $T_{n+1}(x)$ 的根，即 $x_{i}=cos\frac{\left(2i+1\right)\pi }{2(n+1)} ,i=0,1,..,n$ ,则对 $\left|x\right|\leq 1$ , 多项式插值的误差满足：

$\left|f\left(x\right)-P_{n}\left(x\right)\right|=\frac{1}{\left(n+1\right)!}\left|f^{\left(n+1\right)}\left(c\right)\underbrace{\prod_{i=0}^{n}\left(x-x_{i}\right)}_{T_{n+1}\left(x\right)/2^{n}}\right|\leq \frac{1}{2^{n}\left(n+1\right)!}\left|f^{\left(n+1\right)}\left(c\right)\right|, c\in \left(-1,1\right)$

![](images/d54a8dfc7190084455f09c66017f9947da3aba6cc2222afddb2da0721efc1ca8.jpg)

$T_{n}\left(x\right)=\cos((ncos^{-1}x))$ 的零点分布 $(n=15)$

$x_{k}=cos\frac{\left(2k+1\right)\pi }{2n}, k=0,1,\ldots ,n-1$

## Chebyshev插值

- 区间变换：定义映射 $\hat{x}=L\left(x\right)=\frac{2(x-\frac{b+a}{2})}{b-a}$ , $L\left(x\right)$ 是 $\left[a,b\right]\rightarrow \left[-1,1\right]$ 的满射(一一映射)。
- 标准的Chebyshev插值节点为 $\hat{x}_{i}=cos\frac{\left(2i+1\right)\pi }{2\left(n+1\right)}, i=0,1,..,n.$ 并且有不等式

$\left|\left(\hat{x}-\hat{x}_{0}\right)\ldots (\hat{x}-\hat{x}_{n})\right|\leq \frac{1}{2^{n}}$

- 逆变换： $x=L^{-1}\left(\hat{x}\right)=\frac{b-a}{2}\hat{x}+\frac{b+a}{2}$ ,在任意区间 $[a,b]$ 上的Chebyshev插值节点为

$x_{i}=\frac{b-a}{2}cos\frac{\left(2i+1\right)\pi }{2\left(n+1\right)}+\frac{b+a}{2}, i=0,1,..,n$

且满足不等式

$\left|\left(x-x_{0}\right)\ldots (x-x_{n})\right|=\left(\frac{b-a}{2}\right)^{n+1}\left|\left(\hat{x}-\hat{x}_{0}\right)\ldots (\hat{x}-\hat{x}_{n})\right|\leq \frac{\left(\frac{b-a}{2}\right)^{n+1}}{2^{n}}$

## Chebyshev插值

- 任意区间 $\left[a,b\right]$ 的Chebyshev插值误差定理：

若选取插值节点为 $x_{i}=\frac{b-a}{2}cos\frac{\left(2i+1\right)\pi }{2\left(n+1\right)}+\frac{b+a}{2} ,i=0,1,..,n$ ,则对 $\forall x\in [a,b]$ , 多项式插值的误差满足：

$\left|f\left(x\right)-P_{n}\left(x\right)\right|=\frac{1}{\left(n+1\right)!}\left|f^{\left(n+1\right)}\left(c\right)\prod_{i=0}^{n}\left(x-x_{i}\right)\right|\leq \frac{\left(\frac{b-a}{2}\right)^{n+1}}{2^{n}\left(n+1\right)!}\left|f^{\left(n+1\right)}\left(c\right)\right|, c\in (a,b)$

## Chebyshev插值

- 9次首一多项式 $\left(x-x_{0}\right)\ldots (x-x_{8})$ 在区间 $[-1,1]$ 的图像

![](images/3d320d39228c4a5ec33c12e3643dacce9b63e49f69539adcb45c78edb47789d1.jpg)

$x_{i}$ 均匀分布

$x_{i}$ 取Chebyshev多项式 $T_{9}(x)$ 的根

## Chebyshev插值

- 例：对 $\sin(x)$ 在区间 $[0,\frac{\pi }{2}]$ 进行Chebyshev插值的误差估计。

Chebyshev插值节点：

$x_{i}=\frac{\frac{\pi }{2}-0}{2}cos\frac{\left(2i+1\right)\pi }{2\left(n+1\right)}+\frac{\frac{\pi }{2}+0}{2}, i=0,1,..,n$

误差限：

$\left|\sin(x)-P_{n}(x)\right|=\frac{\left|\left(x-x_{0}\right)\ldots (x-x_{n})\right|}{\left(n+1\right)!}\left|f^{\left(n+1\right)}(c)\right|\leq \left|\frac{\left(\frac{\frac{\pi }{2}-0}{2}\right)^{n+1}}{\left(n+1\right)!2^{n}}\right|$

## Chebyshev插值

![](images/b74080994e88aef0b75829124d818af4e6d5f209d0aa5d073988d00cc2f29869.jpg)

$\sin(x)$ 的3次、9次多项式插值误差：实线为均匀插值；虚线为Chebyshev插值

## Chebyshev插值

- 例：Runge函数的Chebyshev插值：

$f\left(x\right)=\frac{1}{1+25x^{2}}, x\in [-1,1]$

![](images/11155e324bbfd3c54c0329e6550da22a2ebb7941ab578a9ce7e96f7731551a2a.jpg)

## 样条插值

- 样条函数是由一些具有某些连续条件的子区间上的分段多项式构成。
- 结点 $x_{0},x_{1},\ldots ,x_{n}$ 上的 $k(k\geq 0)$ 次样条函数 $S(x)$ 满足：

1、在每个子区间 $\left[x_{i-1},x_{i}\right]$ 上， $S(x)$ 是一个次数 $\leq k$ 的多项式

2、在 $[x_{0},x_{n}]$ 上 $S\left(x\right)k-1$ 阶连续

## 样条插值

![](images/8e2e47a061dbd9f8380159236eafad8b937639298f9b1da9f0a75cf737b8e4b0.jpg)

- 0次样条（分段常值函数）

$S\left(x\right)=\left\{\begin{array}{c}S_{0}\left(x\right)=f\left(x_{0}\right),x\in \left[x_{0},x_{1}\right]\\S_{1}\left(x\right)=f\left(x_{1}\right),x\in \left[x_{1},x_{2}\right]\\\vdots \\S_{n-1}\left(x\right)=f\left(x_{n-1}\right),x\in [x_{n-1},x_{n}]\end{array}\right.$

- 误差

$\left|S\left(x\right)-f\left(x\right)\right|=\left|f^{'}\left(c_{i}\right)\left(x-x_{i}\right)\right|\leq \left|f^{'}\left(c_{i}\right)\left(x_{i+1}-x_{i}\right)\right|, x\in \left[x_{i},x_{i+1}\right], c_{i}\in (x_{i},x)$

11个插值节点

## 样条插值

![](images/126a5658805c5416eb6a255ad6ee3d90ae1c00b4341b421485622a047063938f.jpg)

11个插值节点

- 1次样条（分段线性函数）

$S\left(x\right)=\left\{\begin{array}{c}S_{0}\left(x\right)=a_{0}x+b_{0},x\in \left[x_{0},x_{1}\right]\\S_{1}\left(x\right)=a_{1}x+b_{1},x\in \left[x_{1},x_{2}\right]\\\vdots \\S_{n-1}\left(x\right)=a_{n-1}x+b_{n-1},x\in [x_{n-1},x_{n}]\end{array}\right.$

- 误差

$\left|S\left(x\right)-f\left(x\right)\right|=\left|\frac{f^{''}\left(c_{i}\right)}{2}\right|\left|\left(x-x_{i}\right)\left(x-x_{i+1}\right)\right|\leq \left|\frac{f^{''}\left(c_{i}\right)}{2}\right|\left(\frac{x_{i+1}-x_{i}}{2}\right)^{2}$

$x\in \left[x_{i},x_{i+1}\right], c_{i}\in (x_{i},x_{i+1})$

## 样条插值

- 三次样条

$S\left(x\right)=\left\{\begin{array}{c}S_{0}\left(x\right),x\in \left[x_{0},x_{1}\right]\\S_{1}\left(x\right),x\in \left[x_{1},x_{2}\right]\\\vdots \\S_{n-1}\left(x\right),x\in [x_{n-1},x_{n}]\end{array}\right.$

- 性质1： $S_{i}\left(x_{i}\right)=f\left(x_{i}\right), S_{i}\left(x_{i+1}\right)=f\left(x_{i+1}\right) (i=0,\ldots ,n-1)$
- 性质2： $S_{i}^{'}\left(x_{i+1}\right)=S_{i+1}^{'}\left(x_{i+1}\right)(i=0,\ldots ,n-2)$
- 性质3： $S_{i}^{''}\left(x_{i+1}\right)=S_{i+1}^{''}\left(x_{i+1}\right)(i=0,\ldots ,n-2)$

$S_{i}\left(x\right)=f\left(x_{i}\right)+b_{i}\left(x-x_{i}\right)+c_{i}\left(x-x_{i}\right)^{2}+d_{i}\left(x-x_{i}\right)^{3} (i=0,\ldots ,n-1)$

- $S_{i}\left(x\right)=f\left(x_{i}\right)+b_{i}\left(x-x_{i}\right)+c_{i}\left(x-x_{i}\right)^{2}+d_{i}\left(x-x_{i}\right)^{3} (i=0,\ldots ,n-1)$ , $3n$ 个未知数
- 性质1， $n$ 个方程 $(\delta _{i}:=x_{i+1}-x_{i},\Delta _{i}:=f\left(x_{i+1}\right)-f\left(x_{i}\right))$ ：

$S_{i}\left(x_{i+1}\right)=f\left(x_{i}\right)+b_{i}\delta _{i}+c_{i}\delta _{i}^{2}+d_{i}\delta _{i}^{3}=f\left(x_{i+1}\right) (i=0,\ldots ,n-1)$

- 性质2， $n-1$ 个方程：

$S_{i}^{'}\left(x_{i+1}\right)=b_{i}+2c_{i}\delta _{i}+3d_{i}\delta _{i}^{2}=b_{i+1}=S_{i+1}^{'}\left(x_{i+1}\right), (i=0,\ldots ,n-2)$

- 性质3， $n-1$ 个方程：

$S_{i}^{''}\left(x_{i+1}\right)=2c_{i}+6d_{i}\delta _{i}=2c_{i+1}=S_{i+1}^{''}\left(x_{i+1}\right), (i=0,\ldots ,n-2)$

- 右边界条件，1个方程：

$S^{''}\left(x_{n}\right)=S_{n-1}^{''}\left(x_{n}\right)=2c_{n-1}+6d_{n-1}\delta _{n-1}=2c_{n}=0 (自然边界)$

- 左边界条件，1个方程：

$S^{''}\left(x_{0}\right)=S_{0}^{''}\left(x_{0}\right)=2c_{0}=0 (自然边界)$

性质1 $\rightarrow b_{i}=\frac{\Delta _{i}}{\delta _{i}}-c_{i}\delta _{i}-d_{i}\delta _{i}^{2}=\frac{\Delta _{i}}{\delta _{i}}-\frac{\delta _{i}}{3}\left(2c_{i}+c_{i+1}\right) \left(i=0,\ldots ,n-1\right)    (2)$

(1)、(2)、性质2 $\rightarrow \delta _{i}c_{i}+2\left(\delta _{i}+\delta _{i+1}\right)c_{i+1}+\delta _{i+1}c_{i+2}=3\left(\frac{\Delta _{i+1}}{\delta _{i+1}}-\frac{\Delta _{i}}{\delta _{i}}\right) \left(i=0,\ldots ,n-2\right)$

性质3、右边界 $\rightarrow d_{i}=\frac{c_{i+1}-c_{i}}{3\delta _{i}} (i=0,\ldots ,n-1)      (1)$

需要求解的方程组：

$左边界：c_{0}=0$

$\delta _{i}c_{i}+2\left(\delta _{i}+\delta _{i+1}\right)c_{i+1}+\delta _{i+1}c_{i+2}=3\left(\frac{\Delta _{i+1}}{\delta _{i+1}}-\frac{\Delta _{i}}{\delta _{i}}\right) \left(i=0,\ldots ,n-2\right)$

$右边界：c_{n}=0$

矩阵形式： $Mc=\beta$

$\left[\begin{matrix}1&0&0&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&0&0&1\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\\vdots \\c_{n-1}\\c_{n}\end{matrix}\right]=\left[\begin{matrix}0\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\0\end{matrix}\right]$

对角占优

## 样条插值

$\beta =\left[\begin{matrix}0\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\0\end{matrix}\right]$

- 自然三次样条插值算法：

$Initialize:x_{0},\ldots ,x_{n};f(x_{0}),\ldots ,f(x_{n})$

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n-1 \mathbf{d}\mathbf{o}$

$a_{i}=f\left(x_{i}\right)$

$\delta _{i}=x_{i+1}-x_{i}$

$\Delta _{i}=f\left(x_{i+1}\right)-f\left(x_{i}\right)$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$u_{n}=0;v_{0}=v_{n}=1;w_{0}=0;\beta _{0}=\beta _{n}=0$

$\mathbf{f}\mathbf{o}\mathbf{r} i=1 \mathbf{t}\mathbf{o} n-1 \mathbf{d}\mathbf{o}$

$u_{i}=\delta _{i-1};v_{i}=2\left(\delta _{i-1}+\delta _{i}\right);w_{i}=\delta _{i}$

$\beta _{i}=3\left(\frac{\Delta _{i}}{\delta _{i}}-\frac{\Delta _{i-1}}{\delta _{i-1}}\right)$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{s}\mathbf{o}\mathbf{l}\mathbf{v}\mathbf{e} Mc=\beta$

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} n-1 \mathbf{d}\mathbf{o}$

$d_{i}=\frac{c_{i+1}-c_{i}}{3\delta _{i}}$

$b_{i}=\frac{\Delta _{i}}{\delta _{i}}-\frac{\delta _{i}}{3}\left(2c_{i}+c_{i+1}\right)$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$v$

$w$

$M=\left[\begin{matrix}1&0&&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\delta _{1}&2\delta _{1}+2\delta _{2}&\delta _{2}&&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&&0&1\end{matrix}\right]$

$u$

## 样条插值

- 例：用自然三次样条插值龙格函数

![](images/ccbe5c9fc7c40722bdac8e76cec9ac85de862955ba6a4a7952e9d5c190ad83c5.jpg)

![](images/1e914e1738014eb875156234a8dcb1b197aee3c851303ca044f853134abe6c34.jpg)

7个插值节点

11个插值节点

## 样条插值

- 曲率调整三次样条：

$S^{''}\left(x_{0}\right)=2c_{0}=2c_{L}$

$S^{''}\left(x_{n}\right)=2c_{n}=2c_{R}$

$\left[\begin{matrix}1&0&0&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&0&0&1\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\\vdots \\c_{n-1}\\c_{n}\end{matrix}\right]=\left[\begin{matrix}c_{L}\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\c_{R}\end{matrix}\right]$

对角占优

- 钳制三次样条：指定左边界和右边界的斜率

$S^{'}\left(x_{0}\right)=S_{0}^{'}\left(x_{0}\right)=b_{0}=\frac{\Delta _{0}}{\delta _{0}}-\frac{\delta _{0}}{3}\left(2c_{0}+c_{1}\right)=s_{L}$

$S^{'}\left(x_{n}\right)=S_{n-1}^{'}\left(x_{n}\right)=b_{n-1}+2c_{n-1}\delta _{n-1}+3d_{n-1}\delta _{n-1}^{2}=s_{R}$

即：

$2\delta _{0}c_{0}+\delta _{0}c_{1}=3\left(\frac{\Delta _{0}}{\delta _{0}}-s_{L}\right)$

$\delta _{n-1}c_{n-1}+2\delta _{n-1}c_{n}=3\left(s_{R}-\frac{\Delta _{n-1}}{\delta _{n-1}}\right)$

$\left[\begin{matrix}2\delta _{0}&\delta _{0}&0&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&0&\delta _{n-1}&2\delta _{n-1}\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\\vdots \\c_{n-1}\\c_{n}\end{matrix}\right]=\left[\begin{matrix}3\left(\frac{\Delta _{0}}{\delta _{0}}-s_{L}\right)\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\3\left(s_{R}-\frac{\Delta _{n-1}}{\delta _{n-1}}\right)\end{matrix}\right]$

对角占优

## 样条插值

- 抛物线端点的三次样条： $S_{0}\left(x\right),S_{n-1}(x)$ 至多2阶

$d_{0}=\frac{c_{1}-c_{0}}{3\delta _{0}}=0$

$d_{n-1}=\frac{c_{n}-c_{n-1}}{3\delta _{n-1}}=0$

$\left[\begin{matrix}1&-1&0&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&0&1&-1\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\\vdots \\c_{n-1}\\c_{n}\end{matrix}\right]=\left[\begin{matrix}0\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\0\end{matrix}\right]$

非严格对角占优

$M=\left[\begin{matrix}1&-1&0&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&0&1&-1\end{matrix}\right]$

用（倒数）第2行消除（倒数）第1行的非对角元

$M^{'}=\left[\begin{matrix}1+\frac{\delta _{0}}{2\delta _{0}+2\delta _{1}}&0&\frac{\delta _{1}}{2\delta _{0}+2\delta _{1}}&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&-\frac{\delta _{n-2}}{2\delta _{n-2}+2\delta _{n-1}}&0&-1-\frac{\delta _{n-1}}{2\delta _{n-2}+2\delta _{n-1}}\end{matrix}\right]$

$n\geq 2$ 可以转换为对角占优

## 样条插值

- 非纽结三次样条： $d_{0}=d_{1}, d_{n-2}=d_{n-1}$

$d_{0}=\frac{c_{1}-c_{0}}{3\delta _{0}}=\frac{c_{2}-c_{1}}{3\delta _{1}}=d_{1}\rightarrow \delta _{1}c_{0}-\left(\delta _{0}+\delta _{1}\right)c_{1}+\delta _{0}c_{2}=0$

$d_{n-2}=\frac{c_{n-1}-c_{n-2}}{3\delta _{n-2}}=\frac{c_{n}-c_{n-1}}{3\delta _{n-1}}=d_{n-1}\rightarrow \delta _{n-1}c_{n-2}-\left(\delta _{n-2}+\delta _{n-1}\right)c_{n-1}+\delta _{n-2}c_{n}=0$

$\left[\begin{matrix}\delta _{1}&-\delta _{0}-\delta _{1}&\delta _{0}&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\ddots &\ddots &\ddots &&\\&&\ddots &\ddots &\ddots &\\&&&\delta _{n-2}&2\delta _{n-2}+2\delta _{n-1}&\delta _{n-1}\\&&&\delta _{n-1}&-\delta _{n-2}-\delta _{n-1}&\delta _{n-2}\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\\vdots \\c_{n-1}\\c_{n}\end{matrix}\right]=\left[\begin{matrix}0\\3\left(\frac{\Delta _{1}}{\delta _{1}}-\frac{\Delta _{0}}{\delta _{0}}\right)\\\vdots \\\vdots \\3\left(\frac{\Delta _{n-1}}{\delta _{n-1}}-\frac{\Delta _{n-2}}{\delta _{n-2}}\right)\\0\end{matrix}\right]$

非严格对角占优

$\left[\begin{matrix}\delta _{1}&-\delta _{0}-\delta _{1}&\delta _{0}&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\delta _{1}&2\delta _{1}+2\delta _{2}&\delta _{2}&&\\&&\ddots &\ddots &\ddots &\end{matrix}\right]$

用第2行对第1行消元

$\left[\begin{matrix}\delta _{1}+\frac{\delta _{0}}{2}&0&\delta _{0}+\frac{\delta _{1}}{2}&&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\delta _{1}&2\delta _{1}+2\delta _{2}&\delta _{2}&&\\&&\ddots &\ddots &\ddots &\end{matrix}\right]$

用第3行对第1行消元

$\left[\begin{matrix}\delta _{1}+\frac{\delta _{0}}{2}&-\frac{\delta _{1}\left(\delta _{0}+\frac{\delta _{1}}{2}\right)}{2\left(\delta _{1}+\delta _{2}\right)}&0&-\frac{\delta _{2}\left(\delta _{0}+\frac{\delta _{1}}{2}\right)}{2\left(\delta _{1}+\delta _{2}\right)}&&\\\delta _{0}&2\delta _{0}+2\delta _{1}&\delta _{1}&&&\\&\delta _{1}&2\delta _{1}+2\delta _{2}&\delta _{2}&&\\&&\ddots &\ddots &\ddots &\end{matrix}\right]$

严格对角占优

## 样条插值

- 例：通过 $\left(0,3\right),\left(1,1\right),\left(2,4\right),\left(3,1\right),\left(4,2\right),(5,0)$ 的三次样条

![](images/46f6a27269335b408324e3b6ba1158296da4678306d44234d4cee285a16b8df7.jpg)

![](images/91a6344c8463d20a9e11c63e52f15f4cb723a54003958acef745993152a6e043.jpg)

非纽结样条自然样条

![](images/edbba4627f1d3a59b653b5b086428a5a8550eea4359f2ad2e0b1c7929e1d26ca.jpg)

![](images/f7420e14fcd4208db2e2a149fbb5b86699baf8bcc74c4ced5f05d2d37b9917a7.jpg)

钳制样条（端点斜率为0）

抛物线端点样条

## 思考与练习

- 分别使用Lagrange插值和Newton插值找出通过点 $\left\{\left(-1,0\right),\left(2,1\right),\left(3,1\right),\left(5,2\right)\right\}$ 的多项式，并验证两种方法的一致性。
- 确定通过如下三点的自然三次样条插值： $\left(-1,1\right),\left(1,1\right),\left(2,4\right)$
- 编程: 在区间 $[-2,2]$ 取11，21，31个点对 $f\left(x\right)=\frac{1}{1+12x^{2}}$ 进行多项式插值，比较采用均匀插值节点与Chebyshev插值节点的误差。

- 编程: 在区间 $[-2,2]$ 均匀取11，21，31个点对 $f\left(x\right)=\frac{1}{1+12x^{2}}$ 进行自然三次样条插值,并与采用相同插值节点的Newton插值进行比较。