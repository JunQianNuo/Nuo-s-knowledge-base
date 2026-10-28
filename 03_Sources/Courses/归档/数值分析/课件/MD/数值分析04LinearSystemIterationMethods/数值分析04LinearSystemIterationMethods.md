---
raw_title: 数值分析04LinearSystemIterationMethods
subject: 数值分析04LinearSystemIterationMethods
source: 数值分析04LinearSystemIterationMethods.pptx
status: mineru解析
parser: mineru
---

## 线性方程组的迭代法

- 迭代法的一般形式
    - Richardson迭代
    - Jacobi迭代
    - Gauss-Seidel迭代
    - 连续过松弛(SOR)迭代
- 迭代法的收敛性

## 线性方程组的迭代法

- 引例：求解方程组 $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$

迭代1: $\left\{\begin{array}{c}u_{k+1}=\frac{5-v_{k}}{3}\\v_{k+1}=\frac{5-u_{k}}{2}\end{array}\right.$

迭代2: $\left\{\begin{array}{c}u_{k+1}=5-2v_{k}\\v_{k+1}=5-3u_{k}\end{array}\right.$

- 需要回答的问题：

1. 为什么需要迭代法？
2. 如何设计通用的迭代法？
3. 迭代的收敛性？

## 迭代法的一般形式

- $Qx_{k+1}=\left(Q-A\right)x_{k}+b$ ， $Q$ 是分裂矩阵
- 不动点形式 $x_{k+1}=\left(I-Q^{-1}A\right)x_{k}+Q^{-1}b$

迭代矩阵 $G=\left(I-Q^{-1}A\right)$

- 设计原则：易算、收敛
- (定义）赋范线性空间 $(V,\left\|\bullet \right\|)$ 向量序列 $\left(v_{0},v_{1},\ldots ,v_{k},\ldots \right)$ 收敛： $\lim_{k\to \infty }\left\|v_{k}-v\right\|$ =0

## Richardson迭代

- $Qx_{k+1}=\left(Q-A\right)x_{k}+b$ , $Q=I,G=I-A$

- 例： $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$

系数矩阵 $A=\left[\begin{matrix}3&1\\1&2\end{matrix}\right]$

Richardson迭代： $\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{matrix}-2&-1\\-1&-1\end{matrix}\right]\left[\begin{array}{c}u_{k}\\v_{k}\end{array}\right]+\left[\begin{array}{c}5\\5\end{array}\right]$

## Richardson迭代

$u$

$v$

$k$

迭代过程： $x_{0}=\left[0,0\right]^{T}$

$\left[\begin{array}{c}u_{1}\\v_{1}\end{array}\right]=\left[\begin{matrix}-2&-1\\-1&-1\end{matrix}\right]\left[\begin{array}{c}0\\0\end{array}\right]+\left[\begin{array}{c}5\\5\end{array}\right]=\left[\begin{array}{c}5\\5\end{array}\right]$

$\left[\begin{array}{c}u_{2}\\v_{2}\end{array}\right]=\left[\begin{matrix}-2&-1\\-1&-1\end{matrix}\right]\left[\begin{array}{c}5\\5\end{array}\right]+\left[\begin{array}{c}5\\5\end{array}\right]=\left[\begin{array}{c}-10\\-5\end{array}\right]$

$\left[\begin{array}{c}u_{3}\\v_{3}\end{array}\right]=\left[\begin{matrix}-2&-1\\-1&-1\end{matrix}\right]\left[\begin{array}{c}-10\\-5\end{array}\right]+\left[\begin{array}{c}5\\5\end{array}\right]=\left[\begin{array}{c}30\\20\end{array}\right]$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/9706d4f64ee0e5a514dcda3ed8e953f17d4bd81b1fa352ac23fbd637b958e326.png)

## Jacobi迭代

- $Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=D, G=-D^{-1}\left(L+U\right)$

$D=\left[\begin{matrix}a_{11}&0&\ldots &0\\0&a_{22}&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &a_{nn}\end{matrix}\right]$

$L=\left[\begin{matrix}0&0&\ldots &0\\a_{21}&0&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\a_{n1}&a_{n2}&\ldots &0\end{matrix}\right], U=\left[\begin{matrix}0&a_{12}&\ldots &a_{1n}\\0&0&\ddots &a_{2n}\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &0\end{matrix}\right]$

## Jacobi迭代

- 例： $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$

系数矩阵 $A=\left[\begin{matrix}3&1\\1&2\end{matrix}\right]$

Jacobi迭代： $Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=D$

$\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{matrix}3&0\\0&2\end{matrix}\right]^{-1}\left[\begin{matrix}0&-1\\-1&0\end{matrix}\right]\left[\begin{array}{c}u_{k}\\v_{k}\end{array}\right]+\left[\begin{matrix}3&0\\0&2\end{matrix}\right]^{-1}\left[\begin{array}{c}5\\5\end{array}\right]$

$=\left[\begin{matrix}0&-1/3\\-1/2&0\end{matrix}\right]\left[\begin{array}{c}u_{k}\\v_{k}\end{array}\right]+\left[\begin{array}{c}5/3\\5/2\end{array}\right]$

$D^{-1}$

$D-A$

$D^{-1}$

$=\left[\begin{array}{c}(5-v_{k})/3\\(5-u_{k})/2\end{array}\right]$

## Jacobi迭代

$u$

$v$

$k$

迭代过程： $x_{0}=\left[0,0\right]^{T}$

$\left[\begin{array}{c}u_{1}\\v_{1}\end{array}\right]=\left[\begin{array}{c}(5-v_{0})/3\\(5-u_{0})/2\end{array}\right]=\left[\begin{array}{c}5/3\\5/2\end{array}\right]$

$\left[\begin{array}{c}u_{2}\\v_{2}\end{array}\right]=\left[\begin{array}{c}(5-v_{1})/3\\(5-u_{1})/2\end{array}\right]=\left[\begin{array}{c}5/6\\5/3\end{array}\right]$

$\left[\begin{array}{c}u_{3}\\v_{3}\end{array}\right]=\left[\begin{array}{c}(5-v_{2})/3\\(5-u_{2})/2\end{array}\right]=\left[\begin{array}{c}10/9\\25/12\end{array}\right]$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/9215a9f34efe6902bd3b5070dad3da6cb83ec0a471b4336c139ee0aed6969f29.jpg)

## Gauss-Seidel迭代

- $Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=D+L, G=-\left(L+D\right)^{-1}U$

$D=\left[\begin{matrix}a_{11}&0&\ldots &0\\0&a_{22}&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &a_{nn}\end{matrix}\right]$

$L=\left[\begin{matrix}0&0&\ldots &0\\a_{21}&0&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\a_{n1}&a_{n2}&\ldots &0\end{matrix}\right], U=\left[\begin{matrix}0&a_{12}&\ldots &a_{1n}\\0&0&\ddots &a_{2n}\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &0\end{matrix}\right]$

## Gauss-Seidel迭代

- 例： $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$

系数矩阵 $A=\left[\begin{matrix}3&1\\1&2\end{matrix}\right]$

Gauss-Seidel迭代： $Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=L+D$

$\Longrightarrow \left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{k}}{3}\\\frac{5-u_{k+1}}{2}\end{array}\right]$

$\left[\begin{matrix}3&0\\1&2\end{matrix}\right]\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{matrix}0&-1\\0&0\end{matrix}\right]\left[\begin{array}{c}u_{k}\\v_{k}\end{array}\right]+\left[\begin{array}{c}5\\5\end{array}\right]$

$-U$

$L+D$

## Gauss-Seidel迭代

- Gauss-Seidel迭代与Jacobi迭代的区别与联系

Jacobi迭代： $Dx_{k+1}=\left(D-A\right)x_{k}+b,$     $\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{k}}{3}\\\frac{5-u_{k}}{2}\end{array}\right]$

Gauss-Seidel迭代： $(D+L)x_{k+1}=\left(D+L-A\right)x_{k}+b,$  $\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{k}}{3}\\\frac{5-u_{k+1}}{2}\end{array}\right]$

## Gauss-Seidel迭代

$u$

$v$

$k$

- 迭代过程： $x_{0}=\left[0,0\right]^{T}$

$\left[\begin{array}{c}u_{1}\\v_{1}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{0}}{3}\\\frac{5-u_{1}}{2}\end{array}\right]=\left[\begin{array}{c}\frac{5}{3}\\\frac{5}{3}\end{array}\right]$

$\left[\begin{array}{c}u_{2}\\v_{2}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{1}}{3}\\\frac{5-u_{2}}{2}\end{array}\right]=\left[\begin{array}{c}\frac{10}{9}\\\frac{35}{18}\end{array}\right]$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/73552f46c50a1371f5cdff2cf555eba3e866a4482a1e586cf8b3662225dc3fcc.jpg)

Gauss-Seidel迭代通常收敛比Jacobi迭代快

Jacobi迭代更适合并行计算

## 连续超松弛（SOR）迭代

- 对于一般的线性迭代

$x_{k+1}=Gx_{k}+c$

采用外推(松弛)法得到新的迭代

$x_{k+1}=\gamma \left(Gx_{k}+c\right)+\left(1-\gamma \right)x_{k}, \gamma \ne 0$

即：

$x_{k+1}=G_{\gamma }x_{k}+\gamma c$ , $G_{\gamma }=\gamma G+\left(1-\gamma \right)I$

## 连续超松弛（SOR）迭代

Gauss-Seidel

- SOR迭代： $x_{k+1}=\left(1-\omega \right)x_{k}+\omega D^{-1}(b-Ux_{k}-Lx_{k+1})$
    1. $\omega =1$ ,Gauss-Seidel
    2. $\omega >1$ ,超松弛
    3. $\omega <1$ ,欠松弛
- *不动点形式：* $Qx_{k+1}=\left(Q-A\right)x_{k}+b$

分裂矩阵： $Q=\frac{1}{\omega }(D+\omega L)$

迭代矩阵： $G=\left(D+\omega L\right)^{-1}[\left(1-\omega \right)D-\omega U]$

## 连续超松弛（SOR）迭代

- 例： $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$

Gauss-Seidel迭代： $\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left[\begin{array}{c}\frac{5-v_{k}}{3}\\\frac{5-u_{k+1}}{2}\end{array}\right]$

SOR迭代： $\left[\begin{array}{c}u_{k+1}\\v_{k+1}\end{array}\right]=\left(1-\omega \right)\left[\begin{array}{c}u_{k}\\v_{k}\end{array}\right]+\omega \left[\begin{array}{c}\frac{5-v_{k}}{3}\\\frac{5-u_{k+1}}{2}\end{array}\right]$

## 连续超松弛（SOR）迭代迭代过程

$\omega =0.8,$ 欠松弛

$\omega =1,$ Gauss-Seidel

$\omega =1.2,$ 超松弛

$u$

$v$

$k$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/28254b543e97c1acabd6ee48fe1b523b713989c6bb2e2a5d40536b58cbebf317.jpg)

$u$

$v$

$k$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/73552f46c50a1371f5cdff2cf555eba3e866a4482a1e586cf8b3662225dc3fcc.jpg)

$u$

$v$

$k$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/8a9ca6311ea397c2900f74f84d0ab262a9e34f217848af9cf1a5225390d52cfb.jpg)

## 连续超松弛（SOR）迭代

$\omega$ 取值对收敛步数 $N_{iter}$ 的影响 $\left(TOL=10^{-5}\right)$

<table>
  <tr>
    <th>$$</th>
    <th>0.5</th>
    <th>0.6</th>
    <th>0.7</th>
    <th>0.8</th>
    <th>0.9</th>
    <th>1.0</th>
    <th>1.1</th>
    <th>1.2</th>
    <th>1.3</th>
    <th>1.4</th>
    <th>1.5</th>
  </tr>
  <tr>
    <td>$N_{iseq}$</td>
    <td>15</td>
    <td>12</td>
    <td>10</td>
    <td>9</td>
    <td>7</td>
    <td>6</td>
    <td>5</td>
    <td>7</td>
    <td>9</td>
    <td>11</td>
    <td>14</td>
  </tr>
</table>

## 对比不同迭代法

- 例：

$\left[\begin{matrix}3&-1&0&0&0&\frac{1}{2}\\-1&3&-1&0&\frac{1}{2}&0\\0&-1&3&-1&0&0\\0&0&-1&3&-1&0\\0&\frac{1}{2}&0&-1&3&-1\\\frac{1}{2}&0&0&0&-1&3\end{matrix}\right]\left[\begin{array}{c}u_{1}\\u_{2}\\u_{3}\\u_{4}\\u_{5}\\u_{6}\end{array}\right]=\left[\begin{array}{c}\frac{5}{2}\\\frac{3}{2}\\1\\1\\\frac{3}{2}\\\frac{5}{2}\end{array}\right]$

真解： $x=\left[1,1,1,1,1,1\right]^{T}$

## 对比不同迭代法

$x_{0}=\left[0,0,0,0,0,0\right]^{T}$

$\left\|x_{k}-x_{k-1}\right\|_{\infty }$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/6cbd1464e2aa1c39cc07c48215069603de416784adb30b3a825174763b7563af.jpg)

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/7e953d0357ba76aa7727a3c2570fbecfba1fe69c76d245da4c70f16f298da6c1.jpg)

$\left[\begin{array}{c}u_{1}\\u_{2}\\u_{3}\\u_{4}\\u_{5}\\u_{6}\end{array}\right]$

$\omega$

6步迭代 $(SOR取\omega =1.1)$

6步SOR迭代误差的 $\infty$ 范数

## 迭代法的代码

- 伪代码

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/eaae5a06af4ce9be4626dae12daa689b68e4d0c895f439feaf1003cccb45657c.png)

迭代法则 $Qx_{k+1}=\left(Q-A\right)x_{k}+b$

收敛判别

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/e04f737098fe133e42534f50df1cf27ca4494f28a49a02209b829f8bcee81d02.jpg)

## 迭代法的代码求解 $\left(D+L\right)x=c$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/f350b515f52ab3ff02519b4662a378e7add29cfe0ab32ba5fc780f1483e40382.jpg)

Gauss-Seidel C Code示例向量加法问题定义向量减法向量复制计算 $\left(D+L-A\right)x$

向量无穷范数

## 迭代法的代码主循环

$tem=x$

$y=(D+L-A)x$

$c=y+b=\left(D+L-A\right)x+b$

Solve $\left(D+L\right)x=c$

$y=x-tem$

$Error=\left\|y\right\|_{\infty }$

## 迭代法的收敛性

- 引理（诺伊曼级数定理）：若对某个算子范数 $\left\|G\right\|<1$ ,则 $I-G$ 可逆，且

$\left(I-G\right)^{-1}=\sum_{k=0}^{\infty }G^{k}$

- 迭代收敛定理：若迭代矩阵的某个算子范数 $\left\|I-Q^{-1}A\right\|=\delta <1$ ,则 $x_{k+1}=\left(I-Q^{-1}A\right)x_{k}+Q^{-1}b$ 收敛于 $Ax=b$ 的解。并且

$\left\|x-x_{k}\right\|\leq \frac{\delta }{1-\delta }\left\|x_{k}-x_{k-1}\right\|\leq \ldots \frac{\delta ^{k}}{1-\delta }\left\|x_{1}-x_{0}\right\|$

## 迭代法的收敛性

- 推论1：如果 $A$ 是单位严格行/列对角占优矩阵，即

$a_{ii}=1>\sum_{j=1,j\ne i}^{n}\left|a_{ij}\right|, (1\leq i\leq n)$

或

$a_{jj}=1>\sum_{i=1,i\ne j}^{n}\left|a_{ij}\right|, (1\leq j\leq n)$

则Richardson迭代 $x_{k+1}=\left(I-A\right)x_{k}+b$ 收敛。

## 迭代法的收敛性

- 例： 求解 $Ax=b$ ，Richardson迭代能否保证收敛？

$A=\left[\begin{matrix}3&1\\1&2\end{matrix}\right]$

$A=\left[\begin{matrix}1&1/2&1/3\\1/2&1&1/3\\1/3&1/2&1\end{matrix}\right]$

$A=\left[\begin{matrix}1&1/2&1/2\\1/2&1&1/3\\1/3&1/3&1\end{matrix}\right]$

×

√

√

## 迭代法的收敛性

- 推论2：如果 $A$ 是严格行对角占优矩阵，即

$|a_{ii}|>\sum_{j=1,j\ne i}^{n}\left|a_{ij}\right|, (1\leq i\leq n)$

则Jacobi迭代 $x_{k+1}=-D^{-1}\left(L+U\right)x_{k}+D^{-1}b$ 收敛。

## 迭代法的收敛性

- 例：求解 $Ax=b$ ，Jacobi迭代能否保证收敛？

$\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.\Longrightarrow A=\left[\begin{matrix}3&1\\1&2\end{matrix}\right]$

$\left\{\begin{array}{c}u-v+3w=b_{1}\\-5u+2v+2w=b_{2}\\6u+8v+w=b_{3}\end{array}\right.\Longrightarrow A=\left[\begin{matrix}1&-1&3\\-5&2&2\\6&8&1\end{matrix}\right]$

$\left\{\begin{array}{c}-5u+2v+2w=b_{2}\\6u+8v+w=b_{3}\\u-v+3w=b_{1}\end{array}\right.\Longrightarrow A=\left[\begin{matrix}-5&2&2\\6&8&1\\1&-1&3\end{matrix}\right]$

√

×

√

## 迭代法的收敛性

- Gauss-Seidel迭代收敛性？

$Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=D+L, G=-\left(L+D\right)^{-1}U$

- Schur酉三角化定理：每个方阵 $A$ 酉相似于一个上三角阵 $T$ ，即：

$A=UTU^{*}, \left(UU^{*}=I, U^{*}是U的共轭转置\right)$

- Schur酉三角化定理的推论：每个方阵 $A$ 相似于非对角元是任意小（可能为复数）的上三角阵。

## 迭代法的收敛性

- 谱半径定理：
    - 矩阵 $A$ 的谱半径满足 $\rho \left(A\right)\leq \left\|A\right\|, \left\|\bullet \right\|$ 为“任意算子范数"

- 存在算子范数 $\left\|\bullet \right\|^{*}$ 任意接近 $\rho \left(A\right)$ ，即：

$\left\|A\right\|^{*}\leq \rho \left(A\right)+\varepsilon , \varepsilon$ 为任意正数

## 迭代法的收敛性

- 迭代收敛定理2：迭代 $x_{k+1}=Gx_{k}+c$ （ $c$ 为任意向量）对任意初始向量 $x_{0}$ 收敛于 $\left(I-G\right)^{-1}c$ 的充要条件是 $\rho \left(G\right)<1$ .
- 定理：若 $A$ 严格行对角占优，对任何初始向量Gauss-Seidel迭代 $x_{k+1}=-\left(L+D\right)^{-1}Ux_{k}+\left(L+D\right)^{-1}b$ 收敛到 $Ax=b$ 的解。
- 定理：若 $A$ 的主对角元 $a_{ii}\ne 0\left(i=1,..,n\right)$ ，则SOR迭代 $\left(G=\left(D+\omega L\right)^{-1}[\left(1-\omega \right)D-\omega U]\right)$ 收敛的必要条件是 $0<\omega <2$ 。

## 迭代法的收敛性

- 例： $\left\{\begin{array}{c}3u+v=5\\u+2v=5\end{array}\right.$
- Richardson迭代: $G=I-A=\left[\begin{matrix}-2&-1\\-1&-1\end{matrix}\right],\rho \left(G\right)=\frac{3+\sqrt{5}}{2}$
- Jacobi迭代： $G=I-D^{-1}A=\left[\begin{matrix}0&-\frac{1}{3}\\-\frac{1}{2}&0\end{matrix}\right],\rho (G)=\frac{1}{\sqrt{6}}$
- Gauss-Seidel迭代： $G=-\left(L+D\right)^{-1}U=\left[\begin{matrix}0&-\frac{1}{3}\\0&\frac{1}{6}\end{matrix}\right],\rho \left(G\right)=\frac{1}{6}$

×

√

√

## 为什么需要迭代方法？

- Gauss消元/LU分解复杂度 $O(n^{3})$ , 矩阵乘向量 $O(n^{2})，$ 迭代法复杂度 $O(kn^{2}) ，k$ 为迭代步数。
- 对于稀疏矩阵,非零元个数为 $O(n) ，$ 迭代法优势明显：更少的内存更快的速度！

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/e91068cfa4f623fedc85bb0661b349a3f90d49d1116eec8548b3bac4cd5ff5a8.jpg)

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9004LinearSystemIterationMethods/images/faf05224e42714e9595f2cce15b8dd6427dacc78c3b0ed352dd7feafd06de9b9.jpg)

消元

## 为什么需要迭代方法？

- 例：稀疏矩阵大规模计算： $n=10^{5}$

1. Gauss消元：双精度内存 $8\times n^{2}=8\times 10^{10}$ =80G字节；操作数的量级 $n^{3}=10^{15}$ ,CPU频率几个GHz（每秒 $10^{8}$ 次浮点数操作），计算时间量级 $10^{7}$ 秒（1年 $3\times 10^{7}$ 秒）
2. 迭代法：内存 $O(n)$ ，每步迭代操作数 $O(n)$ ，100次迭代的计算时间在秒量级

## 为什么需要迭代方法？

- 稀疏矩阵求解，精确解为 $\left[0,1,2,\ldots ,n-1\right]$ ：Gauss消元与Gauss-Seidel对比

Gauss-Seidel迭代次数 $N_{iter}$ 随矩阵维度 $n$ 的变化 $\left(TOL=10^{-7}\right)$

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
    <td>$N_{iseq}$</td>
    <td>28</td>
    <td>56</td>
    <td>64</td>
    <td>71</td>
    <td>78</td>
    <td>84</td>
    <td>91</td>
  </tr>
</table>

计算时间随矩阵维度 $n$ 的变化 $\left(Gauss-Seidel取TOL=10^{-7}\right)$

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
</table>

## 思考与练习

- 对方程重新组织，得到一个严格行对角占优系数矩阵，并推导相应的Jacobi迭代和Gauss-Seidel迭代公式

$\left\{\begin{array}{c}u-8v-2w=1 \\u+v+5w=4\\3u-v+w=-2\end{array}\right.$

- 编程实现Jacobi迭代、Gauss-Seidel迭代和SOR迭代，并迭代求解以上方程组。所有迭代初始向量取0，误差限取 $10^{-6}$ ，结果保留8位小数。
- 编程实现Jacobi迭代求解课件中的稀疏系数矩阵的线性方程组(矩阵维度尽可能高)，并与之前实现的Gauss消元进行比较。