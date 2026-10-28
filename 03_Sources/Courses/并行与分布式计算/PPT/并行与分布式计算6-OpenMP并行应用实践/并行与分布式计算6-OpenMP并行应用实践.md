---
raw_title: 并行与分布式计算6-OpenMP并行应用实践
subject: 并行与分布式计算6-OpenMP并行应用实践
source: 并行与分布式计算6-OpenMP并行应用实践.pptx
status: mineru解析
parser: mineru
---

## OpenMP并行应用实践

## **实践1. 蒙特卡洛算法**

- 蒙特卡洛（Monte Carlo method）算法
- 20世纪40年代，在科学家冯·诺伊曼、斯塔尼斯拉夫·乌拉姆和尼古拉斯·梅特罗波利斯于洛斯阿拉莫斯国家实验室为核武器计划工作时，发明了蒙特卡罗方法。
- 因为乌拉姆的叔叔经常在摩纳哥的蒙特卡洛赌场输钱而得名。
- 蒙特卡罗方法在金融工程学、宏观经济学、生物医学、计算物理学（如粒子输运计算、量子热力学计算、空气动力学计算）、机器学习等领域应用广泛。
- 算法基础
- 大数定律：当随机样本数量 N足够大时，样本均值会依概率收敛到真实期望。
- 中心极限定理：估计误差大致服从正态分布，误差量级约为 $O\left(\frac{1}{\sqrt{N}}\right)$

![](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%976-OpenMP%E5%B9%B6%E8%A1%8C%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5/images/9a686834df74790da48020b7673b2313c7987f91f96fac5a6d0c318678d9c2ce.jpg)

课堂实践：使用蒙特卡洛算法结合OpenMP并行计算 $\pi$ ，测试并行效率和误差收敛率。

## 实践2.高斯消元法求解线性方程组

- 具体操作

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\a_{21}&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\a_{n1}&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

$a_{ij}\leftarrow a_{ij}-\left(\frac{a_{i1}}{a_{11}}\right)a_{1j}      b_{i}\leftarrow b_{i}-\left(\frac{a_{i1}}{a_{11}}\right)b_{1}, a_{11}\ne 0$

$\left[\begin{matrix}a_{11}&a_{12}&\ldots &a_{1n}\\0&a_{22}&\ldots &a_{2n}\\\vdots &\vdots &\vdots &\vdots \\0&a_{n2}&\ldots &a_{nn}\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\\\vdots \\x_{n}\end{array}\right]=\left[\begin{array}{c}b_{1}\\b_{2}\\\vdots \\b_{n}\end{array}\right]$

- 经过 $n-1$ 轮操作后

$\left\{\begin{array}{c}a_{11}x_{1}+a_{12}x_{2}+a_{13}x_{3}+                      \ldots +a_{1n}x_{n}=b_{1}\\        a_{22}x_{2}+a_{23}x_{3}+                     \ldots +a_{2n}x_{n}=b_{2}\\\vdots \\                                  a_{n-1,n-1}x_{n-1}+a_{n-1,n}x_{n}=b_{n-1}\\                                                  a_{nn}x_{n}=b_{n}\end{array}\right.$

- 回代求解

$x_{n}=b_{n}/a_{nn}$

$x_{n-1}=\left(b_{n-1}-a_{n-1,n}x_{n}\right)/a_{n-1,n-1}$

$x_{i}=\left(b_{i}-\sum_{j=i+1}^{n}a_{ij}x_{j}\right)/a_{ii}, i=n-1,n-2,\ldots ,1$

- 伪代码(pseudocode)

消元回代

![](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%976-OpenMP%E5%B9%B6%E8%A1%8C%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5/images/d64fc9548573bd4479662f596f35f4cace0794d7a03f4a363ed4242563dc0dcf.jpg)

$\tilde{a}_{ij}=a_{ij}-\left(\frac{a_{ik}}{a_{kk}}\right)a_{kj}$

$\tilde{b}_{i}=b_{i}-\left(\frac{a_{ik}}{a_{kk}}\right)b_{k}$

$x_{n}=b_{n}/a_{nn}$

$x_{i}=\left(b_{i}-\sum_{j=i+1}^{n}a_{ij}x_{j}\right)/a_{ii}$

![](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%976-OpenMP%E5%B9%B6%E8%A1%8C%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5/images/35daa88b3e5c9a54afdef131296fcac4bcb3db3dcc6a45fea750a52fda93fc92.png)

课堂实践：运用OpenMP并行实现高斯消元，使用以上系数矩阵测试并行效率。

## 实践3.雅可比迭代求解线性方程组

- $Qx_{k+1}=\left(Q-A\right)x_{k}+b, Q=D, G=-D^{-1}\left(L+U\right)$

$D=\left[\begin{matrix}a_{11}&0&\ldots &0\\0&a_{22}&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &a_{nn}\end{matrix}\right]$

$L=\left[\begin{matrix}0&0&\ldots &0\\a_{21}&0&\ddots &0\\\vdots &\ddots &\ddots &\vdots \\a_{n1}&a_{n2}&\ldots &0\end{matrix}\right], U=\left[\begin{matrix}0&a_{12}&\ldots &a_{1n}\\0&0&\ddots &a_{2n}\\\vdots &\ddots &\ddots &\vdots \\0&0&\ldots &0\end{matrix}\right]$

- 伪代码

![](../../../../../04_Assets/Images/Courses/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%976-OpenMP%E5%B9%B6%E8%A1%8C%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5/images/eaae5a06af4ce9be4626dae12daa689b68e4d0c895f439feaf1003cccb45657c.png)

迭代法则 $Qx_{k+1}=\left(Q-A\right)x_{k}+b$

收敛判别课堂实践：运用OpenMP并行实现Jacobi迭代，使用与Gauss消元相同的系数矩阵测试并行效率并与Gauss消元进行对比。