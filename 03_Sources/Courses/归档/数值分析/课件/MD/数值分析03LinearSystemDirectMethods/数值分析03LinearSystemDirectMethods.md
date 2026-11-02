---
raw_title: 数值分析03LinearSystemDirectMethods
subject: 数值分析03LinearSystemDirectMethods
source: 数值分析03LinearSystemDirectMethods.pptx
status: mineru解析
parser: mineru
---

## 线性方程组的直接解法

- Gauss消元法
- LU三角分解
- 范数/误差
- 部分主元Gauss消元法
- LU分解与Gauss消元法的联系

## 理论基础

- 求解 $n\times n$ 线性方程组

$\left\{\begin{array}{c}a_{11}x_{1}+a_{12}x_{2}+\ldots +a_{1n}x_{n}=b_{1}\\a_{21}x_{1}+a_{22}x_{2}+\ldots +a_{2n}x_{n}=b_{2}\\\vdots \\a_{n1}x_{1}+a_{n2}x_{2}+\ldots +a_{nn}x_{n}=b_{n}\end{array}\right.$

定义： $x=\left[x_{1},x_{2},\ldots ,x_{n}\right]^{T}, b=\left[b_{1},b_{2},\ldots ,b_{n}\right]^{T}$

$A=\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\a_{21}&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&\ldots &a_{nn}\end{matrix}\right]$

方程组可表示为 $Ax=b$

## 理论基础

- 如何求解 $Ax=b$ ？

1.如果 $\left|A\right|\ne 0, x=A^{-1}b$

2.如果 $\left|A\right|\ne 0$ ,由Cramer法则知：

$x_{k}=\frac{\left|A_{k}\right|}{\left|A\right|}$

- 有没有更简单实用的求解方法？

## 理论基础

- 容易求解的情况

$A=D=\left[\begin{matrix}d_{1}&0&\ldots &0\\0&d_{2}&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &d_{n}\end{matrix}\right]$

$A=I=\left[\begin{matrix}1&0&\ldots &0\\0&1&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &1\end{matrix}\right]$

$A=L=\left[\begin{matrix}l_{11}&0&\ldots &0\\l_{21}&l_{22}&\ddots &0\\\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&\ldots &l_{nn}\end{matrix}\right]$

$A=L^{*}=\left[\begin{matrix}l_{11}^{*}&l_{12}^{*}&\ldots &l_{1n}^{*}\\l_{21}^{*}&l_{22}^{*}&\adots &0\\\vdots &\adots &\vdots &\vdots \\l_{n1}^{*}&0&\ldots &0\end{matrix}\right]$

$A=U=\left[\begin{matrix}u_{11}&u_{12}&\ldots &u_{1n}\\0&u_{22}&\ddots &u_{2n}\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &u_{nn}\end{matrix}\right]$

$A=U^{*}=\left[\begin{matrix}0&0&\ldots &u_{1n}^{*}\\0&0&\adots &u_{2n}^{*}\\\vdots &\adots &\vdots &\vdots \\u_{n1}^{*}&u_{n2}^{*}&\ldots &u_{nn}^{*}\end{matrix}\right]$

## 高斯消元

- 核心思想：将方程组化简为三角形方程组

- 理论支撑：对一个方程组做有限次行初等运算得到的方程与原方程同解
    - 交换方程组中的两个方程
    - 用一个非零数乘一个方程
    - 一个方程加上某个其它方程的倍数

![](images/71b7a0c72e230b6b8aeac96bb1d4be235fcf56b86b2fe4f489e940d761088384.jpg)

![](images/090d36a608d67e3c819543c65975f232950a11680dd695271929fb8c5a3dd43c.png)

高斯1777-1855

九章算术成书于约公元前150年

## 高斯消元

- 具体操作

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\a_{21}&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

$a_{ij}\leftarrow a_{ij}-\left(\frac{a_{i1}}{a_{11}}\right)a_{1j}      b_{i}\leftarrow b_{i}-\left(\frac{a_{i1}}{a_{11}}\right)b_{1}, a_{11}\ne 0$

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\0&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\0&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

## 高斯消元

- 经过 $n-1$ 轮操作后

$\left\{\begin{array}{c}a_{11}x_{1}+a_{12}x_{2}+a_{13}x_{3}+                      \ldots +a_{1n}x_{n}=b_{1}\\        a_{22}x_{2}+a_{23}x_{3}+                     \ldots +a_{2n}x_{n}=b_{2}\\\vdots \\                                  a_{n-1,n-1}x_{n-1}+a_{n-1,n}x_{n}=b_{n-1}\\                                                  a_{nn}x_{n}=b_{n}\end{array}\right.$

- 回代求解

$x_{n}=b_{n}/a_{nn}$

$x_{n-1}=\left(b_{n-1}-a_{n-1,n}x_{n}\right)/a_{n-1,n-1}$

$x_{i}=\left(b_{i}-\sum_{j=i+1}^{n}a_{ij}x_{j}\right)/a_{ii}, i=n-1,n-2,\ldots ,1$

## 高斯消元

- 例：求解线性方程组

$\left\{\begin{array}{c}x+2y-z=3\\2x+y-2z=3\\-3x+y+z=-6\end{array}\right.$

## 高斯消元

![](images/d64fc9548573bd4479662f596f35f4cace0794d7a03f4a363ed4242563dc0dcf.jpg)

- 伪代码(pseudocode)

$\tilde{a}_{ij}=a_{ij}-\left(\frac{a_{ik}}{a_{kk}}\right)a_{kj}$

$\tilde{b}_{i}=b_{i}-\left(\frac{a_{ik}}{a_{kk}}\right)b_{k}$

消元

$x_{n}=b_{n}/a_{nn}$

$x_{i}=\left(b_{i}-\sum_{j=i+1}^{n}a_{ij}x_{j}\right)/a_{ii}$

回代

## 高斯消元

- 第一轮消元计算量

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\a_{21}&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

$a_{ij}\leftarrow a_{ij}-\left(\frac{a_{i1}}{a_{11}}\right)a_{1j}      b_{i}\leftarrow b_{i}-\left(\frac{a_{i1}}{a_{11}}\right)b_{1}, a_{11}\ne 0$

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\0&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\0&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

消去一个元的计算量：1次除法， $n$ 次乘法， $n$ 次减法（加法）

## 高斯消元

- 消元总体计算量 $\left(N_{e}\right)$

$\left[\begin{matrix}0&&&&\\2n+1&0&&&\\2n+1&2\left(n-1\right)+1&\ddots &&\\\vdots &\vdots &\ddots &0&\\2n+1&2\left(n-1\right)+1&\ldots &2\left(2\right)+1&0\end{matrix}\right]$

$N_{e}=\sum_{j=1}^{n}\left(2j+1\right)\left(j-1\right)=\frac{2}{3}n^{3}+\frac{1}{2}n^{2}-\frac{7}{6}n=O\left(n^{3}\right)$

## 高斯消元

- 回代计算量 $\left(N_{b}\right)$

$x_{n}=b_{n}/a_{nn}$

$x_{i}=\left(b_{i}-\sum_{j=i+1}^{n}a_{ij}x_{j}\right)/a_{ii}, i=n-1,n-2,\ldots ,1$

$N_{b}=\sum_{i=1}^{n}\left[2\left(n-i\right)+1\right]=n^{2}=O\left(n^{2}\right)$

## 高斯消元

- 例：估算在求解一个规模为 $500\times 500$ 个未知量的系统时，计算机系统消元过程和回代过程所花的时间之比。

$\frac{t_{b}}{t_{e}}\approx \frac{N_{b}}{N_{e}}\approx \frac{500^{2}}{\frac{2}{3}\times 500^{3}}=0.003$

## LU分解

- 什么是矩阵 $A$ 的 $LU$ 分解？
- $LU分解$ 有什么用？
- 怎么分解？

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&u_{12}&u_{13}&\ldots &u_{1n}\\0&u_{22}&u_{23}&\ldots &u_{2n}\\0&0&u_{33}&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{ij}=\sum_{s=1}^{s=n}l_{is}u_{sj}=\sum_{s=1}^{s=min (i,j)}l_{is}u_{sj}$

$n^{2}$ 个方程， $n^{2}+n$ 个未知数

## LU分解

- Doolittle分解

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}1&0&0&\ldots &0\\l_{21}&1&0&\ldots &0\\l_{31}&l_{32}&1&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &1\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&u_{12}&u_{13}&\ldots &u_{1n}\\0&u_{22}&u_{23}&\ldots &u_{2n}\\0&0&u_{33}&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

- Crout分解

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}1&u_{12}&u_{13}&\ldots &u_{1n}\\0&1&u_{23}&\ldots &u_{2n}\\0&0&1&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &1\end{matrix}\right]$

## LU分解

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&u_{12}&u_{13}&\ldots &u_{1n}\\0&u_{22}&u_{23}&\ldots &u_{2n}\\0&0&u_{33}&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{11}=\sum_{s=1}^{s=min (1,1)}l_{1s}u_{s1}=l_{11}u_{11}\rightarrow l_{11} \textbackslash u_{11}$

$a_{1j}=\sum_{s=1}^{s=min (1,j)}l_{1s}u_{sj}=l_{11}u_{1j}\rightarrow u_{1j} \left(2\leq j\leq n\right)$

$a_{i1}=\sum_{s=1}^{s=min (i,1)}l_{is}u_{s1}=l_{i1}u_{11}\rightarrow l_{i1} \left(2\leq i\leq n\right)$

## LU分解

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&u_{12}&u_{13}&\ldots &u_{1n}\\0&u_{22}&u_{23}&\ldots &u_{2n}\\0&0&u_{33}&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{22}=\sum_{s=1}^{s=min (2,2)}l_{2s}u_{s2}=l_{21}u_{12}+l_{22}u_{22}\rightarrow l_{22} \textbackslash u_{22}$

$a_{2j}=\sum_{s=1}^{s=min (2,j)}l_{2s}u_{sj}=l_{21}u_{1j}+l_{22}u_{2j}\rightarrow u_{2j} \left(3\leq j\leq n\right)$

$a_{i2}=\sum_{s=1}^{s=min (i,2)}l_{is}u_{s2}=l_{i1}u_{12}+l_{i2}u_{22}\rightarrow l_{i2} \left(3\leq i\leq n\right)$

## LU分解

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\\vdots &\ddots &0&\ldots &0\\l_{k-1,1}&\ldots &l_{k-1,k-1}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&\ldots &l_{n,k-1}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&\ldots &u_{1,k-1}&\ldots &u_{1n}\\0&\ddots &\vdots &\ldots &\vdots \\0&0&u_{k-1,k-1}&\ldots &u_{k-1,n}\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

$a_{k,k}=\sum_{s=1}^{s=min (k,k)}l_{ks}u_{sk}=\sum_{s=1}^{k-1}l_{ks}u_{sk}+l_{kk}u_{kk}\rightarrow l_{kk} \textbackslash u_{kk}$

$a_{kj}=\sum_{s=1}^{s=min (k,j)}l_{ks}u_{sj}=\sum_{s=1}^{k-1}l_{ks}u_{sj}+l_{kk}u_{k,j}\rightarrow u_{kj} (k<j\leq n)$

$a_{ik}=\sum_{s=1}^{s=min (i,k)}l_{is}u_{sk}=\sum_{s=1}^{k-1}l_{is}u_{sk}+l_{ik}u_{kk}\rightarrow l_{ik} (k<i\leq n)$

## LU分解

- $A=LU$ 分解过程

$\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1n}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2n}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&a_{n3}&\ldots &a_{nn}\end{matrix}\right]=\left[\begin{matrix}l_{11}&0&0&\ldots &0\\l_{21}&l_{22}&0&\ldots &0\\l_{31}&l_{32}&l_{33}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\l_{n1}&l_{n2}&l_{n3}&\ldots &l_{nn}\end{matrix}\right]\bullet \left[\begin{matrix}u_{11}&u_{12}&u_{13}&\ldots &u_{1n}\\0&u_{22}&u_{23}&\ldots &u_{2n}\\0&0&u_{33}&\ldots &u_{3n}\\\vdots &\vdots &\vdots &\vdots &\vdots \\0&0&0&\ldots &u_{nn}\end{matrix}\right]$

求解顺序: $u_{11}\rightarrow l_{i1},u_{1j}\rightarrow u_{22}\rightarrow l_{i2},u_{2j}\rightarrow \ldots \rightarrow u_{nn}$

显式求解：

$u_{kj}=\left(a_{kj}-\sum_{s=1}^{k-1}l_{ks}u_{sj}\right)/l_{kk}$

$l_{ik}=\left(a_{ik}-\sum_{s=1}^{k-1}l_{is}u_{sk}\right)/u_{kk}$

## LU分解

- 例： $3\times 3$ 矩阵的Doolittle分解

$A=\left[\begin{matrix}1&2&-1\\2&1&-2\\-3&1&1\end{matrix}\right]=LU=\left[\begin{matrix}1&0&0\\l_{21}&1&0\\l_{31}&l_{32}&1\end{matrix}\right]\left[\begin{matrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\end{matrix}\right]$

$=\left[\begin{matrix}u_{11}&u_{12}&u_{13}\\l_{21}u_{11}&l_{21}u_{12}+u_{22}&l_{21}u_{13}+l_{22}u_{23}\\l_{31}u_{11}&l_{31}u_{12}+l_{32}u_{22}&l_{31}u_{13}+l_{32}u_{23}+u_{33}\end{matrix}\right]$

- 求解

$\left[\begin{matrix}1&2&-1\\2&1&-2\\-3&1&1\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\end{array}\right]=\left[\begin{array}{c}3\\3\\-6\end{array}\right]$

## LU分解

- Doolittle分解的伪代码

![](images/d31237b2fd9b31cf42729b85416aed440907675bee3dc936b1eb55ee385f513b.jpg)

把 $1$ 赋值给 $L$ 的对角元更新 $U$ 的第 $k$ 行更新 $L$ 的第 $k列$

## LU分解

- Doolittle分解计算量？

![](images/d31237b2fd9b31cf42729b85416aed440907675bee3dc936b1eb55ee385f513b.jpg)

$k-1次$ 乘法， $k-1次$ 减法

$k-1次$ 乘法， $k-1次$ 减法，1次除法

$\sum_{k=1}^{n}\left[2\left(k-1\right)\left(n-k+1\right)+\left(2k-1\right)\left(n-k\right)\right]=\frac{2}{3}n^{3}-\frac{1}{2}n^{2}-\frac{1}{6}n$

总计算量=

$LU$ 分解相比Gauss消元有什么优势？

## LU分解

- $LU$ 分解的存在性？
- $LU$ 分解定理：若 $n\times n$ 矩阵 $A$ 的 $n$ 个前主子式非奇异，则 $A$ 有 $LU$ 分解。

$A的$ 第 $k个$ 前主子式定义为：

$A_{k}=\left[\begin{matrix}a_{11}&a_{12}&a_{13}&\ldots &a_{1k}\\a_{21}&a_{22}&a_{23}&\ldots &a_{2k}\\a_{31}&a_{32}&a_{33}&\ldots &a_{3k}\\\vdots &\vdots &\vdots &\vdots &\vdots \\a_{k1}&a_{k2}&a_{k3}&\ldots &a_{kk}\end{matrix}\right]$

## 误差

- 直接法有误差吗？
- 如何衡量误差？
- 向量 $x\in \mathbb{R}^{n}$ 的范数 $\left\|x\right\|\in \mathbb{R}$ 满足

1. 正定性 $：\left\|x\right\|\geq 0$ ，仅当 $x=0$ 时等号成立
2. 齐次性： $\left\|\alpha x\right\|=\left|\alpha \right|\bullet \left\|x\right\|$
3. 三角不等式： $\left\|x+y\right\|\leq \left\|x\right\|+\left\|y\right\|$

- 例：

$\left\|x\right\|_{1}=\left|x_{1}\right|+\ldots +\left|x_{n}\right|$

$\left\|x\right\|_{2}=\sqrt{x_{1}^{2}+\ldots +x_{n}^{2}}$

$\left\|x\right\|_{\infty }=\max_{1\leq i\leq n}\left|x_{i}\right|$

## 误差

- 矩阵 $A$ 的范数 $\left\|A\right\|\in \mathbb{R}$ 满足

1. 正定性 $：\left\|A\right\|\geq 0$ ，仅当 $A=0$ 时等号成立
2. 齐次性： $\left\|\alpha A\right\|=\left|\alpha \right|\bullet \left\|A\right\|$
3. 三角不等式： $\left\|A+B\right\|\leq \left\|A\right\|+\left\|B\right\|$

- 算子（从属矩阵）范数： $\left\|A\right\|=max\frac{\left\|Ax\right\|}{\left\|x\right\|} \left(\forall x\in \mathbb{R}^{n}, x\ne 0\right)$

性质 $1.\left\|I\right\|=1$

性质 $2.\left\|A\right\|\bullet \left\|x\right\|\geq \left\|Ax\right\|, \forall x\in \mathbb{R}^{n}$

性质 $3. \left\|A\right\|\bullet \left\|B\right\|\geq \left\|AB\right\|$

## 误差

- 算子范数的例子

1. $\left\|A\right\|_{1}=\max_{1\leq j\leq n}\left(\left|a_{1j}\right|+\ldots +\left|a_{nj}\right|\right)$ , 最大绝对列和
2. $\left\|A\right\|_{2}=\sqrt{\rho (A^{T}A)}$ ， $A^{T}A$ 的谱半径(特征值的最大模)的平方根
3. $\left\|A\right\|_{\infty }=\max_{1\leq i\leq n}\left(\left|a_{i1}\right|+\ldots +\left|a_{in}\right|\right)$ , 最大绝对行和

## 误差

- 求解 $Ax=b$ 的误差定义：

1. 近似解 $x_{a}$ 的前向误差 $\left\|x_{a}-x\right\|_{\infty }$
2. 后向误差 $\left\|b-Ax_{a}\right\|_{\infty }=\left\|r\right\|_{\infty }$
3. 误差放大因子 $=\frac{\left\|x_{a}-x\right\|_{\infty }/\left\|x\right\|_{\infty }}{\left\|r\right\|_{\infty }/\left\|b\right\|_{\infty }}$
4. 也可以采用其它范数来定义误差

## 误差

- 定义： $n$ 阶可逆方阵 $A$ 的条件数 $cond(A)$ 为求解 $Ax=b$ 时，对于所有 $b\ne 0$ 可能出现的最大误差放大因子，即：

$cond\left(A\right)=\max_{b\in \mathbb{R}^{n},b\ne 0}\frac{\left\|x_{a}-x\right\|_{\infty }/\left\|x\right\|_{\infty }}{\left\|r\right\|_{\infty }/\left\|b\right\|_{\infty }}$

- 定理：可逆方阵 $A$ 的条件数 $cond(A)=$  $\left\|A\right\|_{\infty }$  $\left\|A^{-1}\right\|_{\infty }$ ，即：

$\frac{\left\|x_{a}-x\right\|_{\infty }}{\left\|x\right\|_{\infty }}\leq \left\|A\right\|_{\infty } \left\|A^{-1}\right\|_{\infty }\frac{\left\|r\right\|_{\infty }}{\left\|b\right\|_{\infty }}$

## 误差

- 定理：求解方程 $Ax=b$ 时，前向误差和后向误差满足:

$\frac{1}{cond(A)}\frac{\left\|r\right\|_{\infty }}{\left\|b\right\|_{\infty }}\leq \frac{\left\|x_{a}-x\right\|_{\infty }}{\left\|x\right\|_{\infty }}\leq cond(A)$  $\frac{\left\|r\right\|_{\infty }}{\left\|b\right\|_{\infty }}$

- 大条件数的矩阵是病态的。

## 误差

- 例： $\left\{\begin{array}{c}x_{1}+x_{2}=2\\1.0001x_{1}+x_{2}=2.0001\end{array}\right.$

近似解 $x_{a}=\left[-1,3.0001\right]^{T}$ 的前向误差与后向误差？

系数矩阵条件数？

$A=\left[\begin{matrix}1&1\\1.0001&1\end{matrix}\right], A^{-1}=\left[\begin{matrix}-10000&10000\\10001&-10000\end{matrix}\right]$

$cond\left(A\right)=\left\|A\right\|_{\infty }\left\|A^{-1}\right\|_{\infty }\approx 40000$

![](images/f508433a7435dfa706435cd3f9e8cabcbea431f9dd3a61cb2faac8df40326de8.jpg)

问题的几何解释

![](images/e5da226fa1aac0b35d233ab4d65ea6fc16696f7afb750d0e633801869001dd0d.png)

11位

Matlab求解

## 误差

- Hilbert矩阵 $H\left(h_{ij}=\frac{1}{i+j-1}\right)$ 是有名的病态矩阵

$H_{5}=\left[\begin{matrix}1&\frac{1}{2}&\frac{1}{3}&\frac{1}{4}&\frac{1}{5}\\\frac{1}{2}&\frac{1}{3}&\frac{1}{4}&\frac{1}{5}&\frac{1}{6}\\\frac{1}{3}&\frac{1}{4}&\frac{1}{5}&\frac{1}{6}&\frac{1}{7}\\\frac{1}{4}&\frac{1}{5}&\frac{1}{6}&\frac{1}{7}&\frac{1}{8}\\\frac{1}{5}&\frac{1}{6}&\frac{1}{7}&\frac{1}{8}&\frac{1}{9}\end{matrix}\right]$

Matlab实验条件数

## 误差

- 例： $\left\{\begin{array}{c}10^{-20}x_{1}+x_{2}=1\\x_{1}+2x_{2}=4\end{array}\right.$ ，精确解为 $x_{1}=\frac{2}{1-2\times 10^{-20}},x_{2}=\frac{1-4\times 10^{-20}}{1-2\times 10^{-20}}$

顺序高斯消元： $\hat{x}_{1}=0,\hat{x}_{2}=1$

系数矩阵条件数？

$A=\left[\begin{matrix}10^{-20}&1\\1&2\end{matrix}\right],A^{-1}=\frac{1}{2\times 10^{-20}-1}\left[\begin{matrix}2&-1\\-1&10^{-20}\end{matrix}\right]$

调换方程顺序消元： $\hat{x}_{1}=2,\hat{x}_{2}=1$

‘淹没’引起的误差放大可以通过列主消元避免

## 误差

- 列主消元：在消除第 $i$ 列元素前找到绝对值最大的元素 $a_{ji}(i\leq j\leq n)$

$\left[\begin{matrix}a_{11}&\ldots &a_{1i}&\ldots &a_{1j}&\ldots &a_{1n}\\\vdots &\ddots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &a_{ii}&\ldots &a_{ij}&\ldots &a_{in}\\\vdots &\vdots &\vdots &\ddots &\vdots &\vdots &\vdots \\0&\ldots &a_{ji}&\ldots &a_{jj}&\ldots &a_{jn}\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &a_{ni}&\ldots &a_{nj}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\\vdots \\x_{i}\\\vdots \\x_{j}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\\vdots \\b_{i}\\\vdots \\b_{j}\\\vdots \\b_{n}\end{array}\right]$

交换第 $i$ 行和第 $j$ 行

## LU分解与高斯消元的联系

- 高斯消元基本的行变换操作与左乘初等矩阵对应

1. 交换第 $i$ 行和第 $j$ 行 $\Longleftrightarrow$ 左乘初等矩阵

$P=\left[\begin{matrix}1&\ldots &0&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\ldots &\vdots \\0&\ldots &0&\ldots &1&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &1&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &0&\ldots &0&\ldots &1\end{matrix}\right]$

第 $i$ 行第 $j$ 行第 $i$ 列第 $j$ 列

## LU分解与高斯消元的联系

2. 非零数 $\lambda$ 乘第 $i$ 行 $加到$ 第 $j$ 行 $\Longleftrightarrow$ 左乘初等矩阵

$E=\left[\begin{matrix}1&\ldots &0&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\ldots &\vdots \\0&\ldots &1&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &\lambda &\ldots &1&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &0&\ldots &0&\ldots &1\end{matrix}\right]$

第 $i$ 行第 $j$ 行第 $i$ 列第 $j$ 列

## LU分解与高斯消元的联系

- 顺序高斯消元 $\Longleftrightarrow E_{m}\ldots E_{1}A=U\Longleftrightarrow A=E_{1}^{-1}\ldots E_{m}^{-1}U, m\leq \frac{n(n-1)}{2}$
- $E_{1}^{-1}\ldots E_{m}^{-1}=L$ ？

$\left[\begin{matrix}1&\ldots &0&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\ldots &\vdots \\0&\ldots &1&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &\lambda &\ldots &1&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &0&\ldots &0&\ldots &1\end{matrix}\right]^{-1}=\left[\begin{matrix}1&\ldots &0&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\ldots &\vdots \\0&\ldots &1&\ldots &0&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &-\lambda &\ldots &1&\ldots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\ldots &0&\ldots &0&\ldots &1\end{matrix}\right]$

## LU分解与高斯消元的联系

$=E_{1}^{-1}\ldots E_{m-2}^{-1}\bullet \left[\begin{matrix}1&\ldots &0&0&0\\0&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\0&\ddots &0&1&0\\0&\ldots &c_{n,n-2}&c_{n,n-1}&1\end{matrix}\right]$

$E_{1}^{-1}\ldots E_{m}^{-1}=E_{1}^{-1}\ldots E_{m-1}^{-1}\bullet \left[\begin{matrix}1&\ldots &0&0&0\\0&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\0&\ddots &0&1&0\\0&\ldots &0&c_{n,n-1}&1\end{matrix}\right]$

$=E_{1}^{-1}\ldots E_{n-2}^{-1}\bullet \left[\begin{matrix}1&\ldots &0&0&0\\0&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\0&\ddots &c_{n-1,n-2}&1&0\\c_{n,1}&\ldots &c_{n,n-2}&c_{n,n-1}&1\end{matrix}\right]$

$=E_{1}^{-1}\ldots E_{m-3}^{-1}\bullet \left[\begin{matrix}1&\ldots &0&0&0\\0&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\0&\ddots &c_{n-1,n-2}&1&0\\0&\ldots &c_{n,n-2}&c_{n,n-1}&1\end{matrix}\right]$

$=\left[\begin{matrix}1&\ldots &0&0&0\\c_{21}&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\c_{n-1,1}&\ddots &c_{n-1,n-2}&1&0\\c_{n,1}&\ldots &c_{n,n-2}&c_{n,n-1}&1\end{matrix}\right]$

$=E_{1}^{-1}\ldots E_{n-3}^{-1}\bullet \left[\begin{matrix}1&\ldots &0&0&0\\0&\ddots &\vdots &0&0\\\vdots &\ddots &1&\vdots &\vdots \\c_{n-1,1}&\ddots &c_{n-1,n-2}&1&0\\c_{n,1}&\ldots &c_{n,n-2}&c_{n,n-1}&1\end{matrix}\right]$

## LU分解与高斯消元的联系

- 例：推导 $A$ 的 $LU$ 分解

$A=\left[\begin{matrix}1&2&-1\\2&1&-2\\-3&1&1\end{matrix}\right]$

## LU分解与高斯消元的联系

- 伪代码

$\mathbf{p}\mathbf{r}\mathbf{o}\mathbf{c}\mathbf{e}\mathbf{d}\mathbf{u}\mathbf{r}\mathbf{e}   \mathbf{L}\mathbf{U}\_\mathbf{F}\mathbf{a}\mathbf{c}\mathbf{t}\mathbf{o}\mathbf{r}\mathbf{i}\mathbf{z}\mathbf{a}\mathbf{t}\mathbf{i}\mathbf{o}\mathbf{n}\left(\left(a_{ij}\right)\right)$

$\mathbf{i}\mathbf{n}\mathbf{t}\mathbf{e}\mathbf{g}\mathbf{e}\mathbf{r} i,j,k,n;\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} xmult$

$\mathbf{r}\mathbf{e}\mathbf{a}\mathbf{l} \mathbf{a}\mathbf{r}\mathbf{r}\mathbf{a}\mathbf{y} \left(a_{ij}\right)_{1:n\times 1:n}$

$\mathbf{f}\mathbf{o}\mathbf{r} k=1 \mathbf{t}\mathbf{o} n-1 \mathbf{d}\mathbf{o}$

$\mathbf{f}\mathbf{o}\mathbf{r} i=k+1 \mathbf{t}\mathbf{o} n \mathbf{d}\mathbf{o}$

$xmult\leftarrow a_{ik}/a_{kk}$

$a_{ik}\leftarrow xmult$

$\mathbf{f}\mathbf{o}\mathbf{r} j=k+1 \mathbf{t}\mathbf{o} n \mathbf{d}\mathbf{o}$

$a_{ij}\leftarrow a_{ij}-\left(xmult\right)a_{kj}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

$l_{ik}=\frac{a_{ik}}{a_{kk}}$

## LU分解与高斯消元的联系

- 列主高斯消元 $\Longleftrightarrow E_{m}P_{n-1}E_{m-1}E_{m-2}P_{n-2}\ldots E_{2n-3}\ldots E_{n}P_{2}E_{n-1}\ldots E_{1}P_{1}A=U, m=n(n-1)/2$

$\Longrightarrow E_{m}\underbrace{E_{m-1}E_{m-2}P_{n-1}}P_{n-2}\ldots E_{2n-3}\ldots E_{n}P_{2}E_{n-1}\ldots E_{1}P_{1}A=U$

$\Longrightarrow E_{m}E_{m-1}E_{m-2}\ldots E_{2n-3}\ldots E_{n}E_{n-1}\ldots E_{1}P_{n-1}P_{n-2}\ldots P_{2}P_{1}A=U$

$\Longrightarrow \underbrace{P_{n-1}P_{n-2}\ldots P_{2}P_{1}}_{P}A=\underbrace{E_{1}^{-1}\ldots E_{n-1}^{-1}E_{n}^{-1}\ldots E_{2n-3}^{-1}\ldots E_{m-2}^{-1}E_{m-1}^{-1}E_{m}^{-1}}_{L}U$

## LU分解与高斯消元的联系

- $PA=LU$ 回代求解 $Ax=b$

$PAx=Pb \rightarrow LUx=Pb \rightarrow \left\{\begin{array}{c}Ly=Pb\\Ux=y\end{array}\right.$

- 例：用 $PA=LU$ 分解求解

$\left[\begin{matrix}2&1&5\\4&4&-4\\1&3&1\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\end{array}\right]=\left[\begin{array}{c}5\\0\\6\end{array}\right]$

## LU分解与高斯消元的联系

- 定义：严格行对角占优矩阵是指

$|a_{ii}|>\sum_{j=1,j\ne i}^{n}\left|a_{ij}\right|, (1\leq i\leq n)$

- 定理：不选主元Gauss消元法保持矩阵的严格行对角占优性质。
- 推论：行对角占优矩阵可逆且有 $LU$ 分解。

## LU分解与高斯消元的联系

- 例：

$A=\left[\begin{matrix}4&1&1&1\\2&4&0&1\\1&2&5&1\\3&1&1&6\end{matrix}\right]$

## 带状方程组的求解

- 三对角方程组

$\left[\begin{matrix}d_{1}&c_{1}&&&&&&\\a_{1}&d_{2}&c_{2}&&&&&\\&a_{2}&d_{3}&c_{3}&&&&\\&&\ddots &\ddots &\ddots &&&\\&&&a_{i-1}&d_{i}&c_{i}&&\\&&&&\ddots &\ddots &\ddots &\\&&&&&a_{n-2}&d_{n-1}&c_{n-1}\\&&&&&&a_{n-1}&d_{n}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\\\vdots \\x_{i}\\\vdots \\x_{n-1}\\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\b_{3}\\\vdots \\b_{i}\\\vdots \\b_{n-1}\\b_{n}\end{array}\right]$

## 带状方程组的求解

- 高斯消元法（追赶法）

$\left[\begin{matrix}d_{1}&c_{1}&&&&&&\\0&d_{2}&c_{2}&&&&&\\&0&d_{3}&c_{3}&&&&\\&&\ddots &\ddots &\ddots &&&\\&&&0&d_{i}&c_{i}&&\\&&&&\ddots &\ddots &\ddots &\\&&&&&0&d_{n-1}&c_{n-1}\\&&&&&&0&d_{n}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\\\vdots \\x_{i}\\\vdots \\x_{n-1}\\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\b_{3}\\\vdots \\b_{i}\\\vdots \\b_{n-1}\\b_{n}\end{array}\right]$

## 带状方程组的求解

- 追赶法的伪代码

![](images/e066a993cfdc2517053092b9acbd546d8b5656b71e0b8f8dfc08684429b73671.jpg)

消元回代计算量 $O(n)$

## 思考与练习

- 证明矩阵的无穷算子范数 $\left\|A\right\|_{\infty }=\max_{1\leq i\leq n}\left(\left|a_{i1}\right|+\ldots +\left|a_{in}\right|\right)$
- 给定方程组 $\left[\begin{matrix}1&1\\1+\delta &1\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{array}{c}2\\2+\delta \end{array}\right],\delta >0$ .1、计算系数矩阵的条件数。2、计算近似解 $x_{a}=[-1, 3+\delta ]的$ 误差放大因子。
- 用Gauss消元法、列主消元法、 $LU$ 分解法、 $PA=LU$ 分解法求解下列方程组

$\left[\begin{matrix}3&1&2\\6&3&4\\3&2&5\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\x_{3}\end{array}\right]=\left[\begin{array}{c}11\\24\\22\end{array}\right]$

- 编写通用的Gauss消元法和 $LU$ 分解法程序:1、求解以上方程组对程序进行验证；2、用程序求解 $Hx=b$ ， $H$ 设置为12阶和20阶Hilbert矩阵， $b=H\bullet \left[1,\ldots ,1\right]^{T}$ 。