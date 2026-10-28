---
raw_title: 数值分析08Fitting
subject: 数值分析08Fitting
source: 数值分析08Fitting.pptx
status: mineru解析
parser: mineru
---

## 数据拟合与最小二乘

- 数据拟合的基本概念与用途
- 最小二乘法
- QR分解与最小二乘

## 数据拟合的基本概念

- 真实世界的数据特征：零散、数据量巨大

- 定义：给定一组数据点 $\left(t_{0},y_{0}\right), \ldots ,(t_{m},y_{m})$ ，确定函数 $y=\phi \left(t\right)，$ 使对应的曲线使其对应的曲线能反映给定数据点的数据变换规律(与给定数据点的距离最小)，则函数 $y=\phi (t)$ 称为拟合函数。

- 拟合函数 $\phi \left(t\right)=a_{0}\phi _{0}\left(t\right)+\cdots +a_{n}\phi _{n}\left(t\right) ，\left\{\phi _{0}\left(t\right),\phi _{1}\left(t\right),\ldots ,\phi _{n}\left(t\right)\right\}$ 为基函数。

## 数据拟合的用途

- 开普勒范式：从大量的观测数据中总结规律（数据驱动）

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/94b363b6ab5c1cf273cdfd46797df1ad26e37b64bfce1bd53d5f40fbbbab88d6.jpg)

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/eb13ffb786f884acfee5d58dd063924d1fe37c751ef685b89b7925d93507f48c.jpg)

开普勒(1571-1630)

*开普勒*第三定律： $\left(\frac{P_{1}}{P_{2}}\right)^{2}=\left(\frac{r_{1}}{r_{2}}\right)^{3}$

$P:$ 行星公转周期， $r:$ 椭圆轨道的半长轴。

## 数据拟合的用途

- 牛顿范式：先“猜测”某种规律（第一性原理），再通过实验数据去拟合待定参数

$P=f\left(r,m,F\right)=?$

$P:$ 行星公转周期， $r:$ 椭圆轨道的半长轴， $m:$ 行星质量， $F:$ 引力。

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/c9394e1cc664f9d6f5863ee9fcc572aba7d6ca573bc0da451d2b425d1563f830.jpg)

量纲分析： $X=T^{a}L^{b}M^{c}(T:时间，L:长度，M:质量)$

<table>
  <tr>
    <th></th>
    <th>$a$</th>
    <th>$b$</th>
    <th>$c$</th>
  </tr>
  <tr>
    <td>$P$</td>
    <td>$1$</td>
    <td>$0$</td>
    <td>$0$</td>
  </tr>
  <tr>
    <td>$q$</td>
    <td>$0$</td>
    <td>$1$</td>
    <td>$0$</td>
  </tr>
  <tr>
    <td>$m$</td>
    <td>$0$</td>
    <td>$0$</td>
    <td>$1$</td>
  </tr>
  <tr>
    <td>$F$</td>
    <td>$-2$</td>
    <td>$1$</td>
    <td>$1$</td>
  </tr>
</table>

牛顿(1643-1727)

令 $P=Cr^{x}m^{y}F^{z}$ , $C$ 是无量纲的常数等式两边量纲相等 $\rightarrow P=C\left(\frac{mr}{F}\right)^{\frac{1}{2}}$

## 数据拟合的用途

$F=GMmr^{\alpha }, \alpha =?,G=?$

$\left.\begin{array}{c}\left(\frac{P_{1}}{P_{2}}\right)^{2}=\left(\frac{r_{1}}{r_{2}}\right)^{3}\\P=C\left(\frac{mr}{F}\right)^{\frac{1}{2}}\end{array}\right\}\Longrightarrow \left(\frac{P_{1}}{P_{2}}\right)^{2}=\frac{\left(\frac{m_{1}r_{1}}{F_{1}}\right)}{\left(\frac{m_{2}r_{2}}{F_{2}}\right)}=\frac{\left(\frac{m_{1}r_{1}}{GMm_{1}r_{1}^{\alpha }}\right)}{\left(\frac{m_{2}r_{2}}{GMm_{2}r_{2}^{\alpha }}\right)}=\left(\frac{r_{1}}{r_{2}}\right)^{1-\alpha }\Longrightarrow \alpha =-2$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/63dd8f03a7b7a2660ff171278c740f4e6655357c1b5deb1a2f0e5796e3bb3bad.jpg)

卡文迪许(1731-1810)

1797-1798年通过实验测定了 $G$

## 数据拟合的用途

- 1945年7月16日上午5:30，美国的第一颗原子弹在新墨西哥州的沙漠中试爆成功

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/63ec1dff5dbaac20639d4b877733dbcab4b2edf4e55015d4bcb6103151f42f39.png)

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/0faa7d5e35106d5112c7e9bb49e5aeec8be975e8746853cbe68fae972060f281.jpg)

G.I. Taylor(1886-1975)

- $E=Cf\left(\rho ,R,t\right)=C\frac{R^{5}\rho }{t^{2}}(E:能量,\rho :空气密度,R:爆炸半径,t:时间)$
- 估算当量为2万吨TNT，与官方公布的2.1万吨TNT仅相差5%！！

## 最小二乘

- 核心思想：在数据点上通过平方误差度量拟合的余项，并找出模型的参数 $\{a_{0},\ldots ,a_{n}\}$ 使得该误差最小(与给定数据点的2范数距离最小) 。
- 例：最小二乘法拟合数据点： $\left(t_{0},y_{0}\right), \ldots ,(t_{m},y_{m})$

1、选定拟合函数 $\phi \left(t\right)=a_{0}\phi _{0}\left(t\right)+\cdots +a_{n}\phi _{n}\left(t\right)$

2、残差向量(余项)： $r=\left[\phi \left(t_{0}\right)-y_{0},\ldots ,\phi \left(t_{m}\right)-y_{m}\right]^{T}$

3、平方误差：

$SE\left(a_{0},\ldots ,a_{n}\right):=\left\|r\right\|_{2}^{2}=\sum_{i=0}^{m}\left[\phi \left(t_{i}\right)-y_{i}\right]^{2}=\sum_{i=0}^{m}\left[\sum_{j=0}^{n}a_{j}\phi _{j}\left(t_{i}\right)-y_{i}\right]^{2}$

4、最小化平方误差：

$\frac{\partial SE}{\partial a_{k}}=2\sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)\left[\sum_{j=0}^{n}a_{j}\phi _{j}\left(t_{i}\right)-y_{i}\right] =0 \left(k=0,\ldots ,n\right)$

$r_{3}$

$r_{1}$

$r_{2}$

$\phi \left(t\right)$

$\sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)\left[\sum_{j=0}^{n}a_{j}\phi _{j}\left(t_{i}\right)-y_{i}\right] =0\left(k=0,\ldots ,n\right)$

移项、交换求和顺序：

$\sum_{j=0}^{n}\left[\sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)\phi _{j}\left(t_{i}\right)\right]a_{j} =\sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)y_{i} \left(k=0,\ldots ,n\right)$

定义 $：\varphi _{s}:=\left[\phi _{s}\left(t_{0}\right),\ldots ,\phi _{s}\left(t_{m}\right)\right]^{T}, f:=\left[y_{0},\ldots ,y_{m}\right]^{T}$

$\sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)\phi _{j}\left(t_{i}\right)=\left⟨\varphi _{k},\varphi _{j}\right⟩    \sum_{i=0}^{m}\phi _{k}\left(t_{i}\right)y_{i} =\left⟨\varphi _{k},f\right⟩$

矩阵形式：             $\left[\begin{matrix}\left⟨\varphi _{0},\varphi _{0}\right⟩&\left⟨\varphi _{0},\varphi _{1}\right⟩&\cdots &\left⟨\varphi _{0},\varphi _{n}\right⟩\\\left⟨\varphi _{1},\varphi _{0}\right⟩&\left⟨\varphi _{1},\varphi _{1}\right⟩&\vdots &\left⟨\varphi _{1},\varphi _{n}\right⟩\\\vdots &\vdots &\ddots &\vdots \\\left⟨\varphi _{n},\varphi _{0}\right⟩&\left⟨\varphi _{n},\varphi _{1}\right⟩&\cdots &\left⟨\varphi _{n},\varphi _{n}\right⟩\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\\vdots \\a_{n}\end{matrix}\right]=\left[\begin{matrix}\left⟨\varphi _{0},f\right⟩\\\left⟨\varphi _{1},f\right⟩\\\vdots \\\left⟨\varphi _{n},f\right⟩\end{matrix}\right]$

## 最小二乘

- 多项式拟合： $\phi \left(t\right)=span\left\{\phi _{0}\left(t\right),\phi _{1}\left(t\right), \cdots ,\phi _{n}\left(t\right)\right\}=span\left\{1,t, \cdots ,t^{n}\right\}$

$\varphi _{s}:=\left[\phi _{s}\left(t_{0}\right),\phi _{s}\left(t_{1}\right),\ldots ,\phi _{s}\left(t_{m}\right)\right]^{T}=\left[t_{0}^{s},t_{1}^{s},\ldots ,t_{m}^{s}\right]^{T}$

$\left[\begin{matrix}m+1&\sum_{i=0}^{m}t_{i}&\cdots &\sum_{i=0}^{m}t_{i}^{n}\\\sum_{i=0}^{m}t_{i}&\sum_{i=0}^{m}t_{i}^{2}&\vdots &\sum_{i=0}^{m}t_{i}^{n+1}\\\vdots &\vdots &\ddots &\vdots \\\sum_{i=0}^{m}t_{i}^{n}&\sum_{i=0}^{m}t_{i}^{n+1}&\cdots &\sum_{i=0}^{m}t_{i}^{2n}\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\\vdots \\a_{n}\end{matrix}\right]=\left[\begin{matrix}\sum_{i=0}^{m}y_{i}\\\sum_{i=0}^{m}t_{i}y_{i}\\\vdots \\\sum_{i=0}^{m}t_{i}^{n}y_{i}\end{matrix}\right]$

- 超定线性方程组的最小二乘法
- 例：最小二乘法拟合数据点 $\left(t_{0},y_{0}\right), \ldots ,(t_{m},y_{m})$

1. 选定拟合函数 $\phi \left(t\right)=a_{0}\phi _{0}\left(t\right)+\cdots +a_{n}\phi _{n}\left(t\right)$ ，代入各数据点条件得到：

$\left[\begin{matrix}\phi _{0}\left(t_{0}\right)&\phi _{1}\left(t_{0}\right)&\cdots &\phi _{n}\left(t_{0}\right)\\\phi _{0}\left(t_{1}\right)&\phi _{1}\left(t_{1}\right)&\vdots &\phi _{n}\left(t_{1}\right)\\\vdots &\vdots &\ddots &\vdots \\\phi _{0}\left(t_{m}\right)&\phi _{1}\left(t_{m}\right)&\cdots &\phi _{n}\left(t_{m}\right)\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\\vdots \\a_{n}\end{matrix}\right]=\left[\begin{matrix}y_{0}\\y_{1}\\\vdots \\y_{m}\end{matrix}\right], m>n时超定$

2. 误差： $\left\|r\right\|_{2}=\left\|b-Ax\right\|_{2}$

2. 最小化误差： $A^{T}Ax=A^{T}b$

2. 定义： $\varphi _{s}:=A_{s}=\left[\phi _{s}\left(t_{0}\right),\ldots ,\phi _{s}\left(t_{m}\right)\right]^{T}, f:=b=\left[y_{0},\ldots ,y_{m}\right]^{T}$ 得：

$\left[\begin{matrix}\left⟨\varphi _{0},\varphi _{0}\right⟩&\left⟨\varphi _{0},\varphi _{1}\right⟩&\cdots &\left⟨\varphi _{0},\varphi _{n}\right⟩\\\left⟨\varphi _{1},\varphi _{0}\right⟩&\left⟨\varphi _{1},\varphi _{1}\right⟩&\vdots &\left⟨\varphi _{1},\varphi _{n}\right⟩\\\vdots &\vdots &\ddots &\vdots \\\left⟨\varphi _{n},\varphi _{0}\right⟩&\left⟨\varphi _{n},\varphi _{1}\right⟩&\cdots &\left⟨\varphi _{n},\varphi _{n}\right⟩\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\\vdots \\a_{n}\end{matrix}\right]=\left[\begin{matrix}\left⟨\varphi _{0},f\right⟩\\\left⟨\varphi _{1},f\right⟩\\\vdots \\\left⟨\varphi _{n},f\right⟩\end{matrix}\right]$

$A$

$x$

$b$

## 最小二乘

- 最小二乘的几何解释
- 例： $Ax=b$ 的具体形式为

$\left[\begin{matrix}1&1\\1&-1\\1&1\end{matrix}\right]\left[\begin{matrix}x_{1}\\x_{2}\end{matrix}\right]=\left[\begin{matrix}2\\1\\3\end{matrix}\right]$

方程等价于 $x_{1}\left[\begin{matrix}1\\1\\1\end{matrix}\right]+x_{2}\left[\begin{matrix}1\\-1\\1\end{matrix}\right]=\left[\begin{matrix}2\\1\\3\end{matrix}\right]$

一般地，任何 $m\times n$ 方程组 $Ax=b$ 都能写成

$x_{1}A_{1}+\ldots +x_{n}A_{n}=b, A_{i}\in \mathbb{R}^{m}$ 是矩阵 $A$ 的列

$b$

$b-Ax$

- 最优解 $\overbar{x}$ 满足：

$\left(b-A\overbar{x}\right)\perp \left\{x\in R^{n}\right\}$

即： $\left(Ax\right)^{T}\left(b-A\overbar{x}\right)=0$

$\Longrightarrow A^{T}A\overbar{x}=A^{T}b$ (法线方程)

$v_{1}$

$Ax$

$v_{2}$

- 例:找出拟合 $\left(1,2\right), \left(-1,1\right), (1,3)$ 的最优直线（线性回归）
- 解： 令： $y=a_{0}+a_{1}t$

代入数据点得：

$\left[\begin{matrix}1&1\\1&-1\\1&1\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}2\\1\\3\end{matrix}\right]$

法线方程：

$\left[\begin{matrix}1&1&1\\1&-1&1\end{matrix}\right]\left[\begin{matrix}1&1\\1&-1\\1&1\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}1&1&1\\1&-1&1\end{matrix}\right]\left[\begin{matrix}2\\1\\3\end{matrix}\right]\Longrightarrow \left[\begin{matrix}3&1\\1&3\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}6\\4\end{matrix}\right]$

最终模型：

$y=\frac{7}{4}+\frac{3}{4}t$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/dfbca4f6575448941086ab55b51e23eb5860dc021d2dd1db20853c94b9e94c47.jpg)

$t$

拟合图像

<table>
  <tr>
    <th>$t$</th>
    <th>$y$</th>
    <th>line</th>
    <th>error</th>
  </tr>
  <tr>
    <td>$1$</td>
    <td>$2$</td>
    <td>$2.5$</td>
    <td>$-0.5$</td>
  </tr>
  <tr>
    <td>$-1$</td>
    <td>$1$</td>
    <td>$1.0$</td>
    <td>$0.0$</td>
  </tr>
  <tr>
    <td>$1$</td>
    <td>$3$</td>
    <td>$2.5$</td>
    <td>$0.5$</td>
  </tr>
</table>

拟合误差

## 最小二乘

- 例:找出拟合 $\left(-1,1\right), \left(0,0\right), \left(1,0\right),(2,-2)$ 的最优直线和最优抛物线
- 解：直线拟合令： $y=a_{0}+a_{1}t$

*拟合*条件 $：$

$\left[\begin{matrix}1&-1\\1&0\\1&1\\1&2\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}1\\0\\0\\-2\end{matrix}\right]$

*法线*方程 $：$

$\left[\begin{matrix}1&1&1&1\\-1&0&1&2\end{matrix}\right]\left[\begin{matrix}1&-1\\1&0\\1&1\\1&2\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}1&1&1&1\\-1&0&1&2\end{matrix}\right]\left[\begin{matrix}1\\0\\0\\-2\end{matrix}\right]\Longrightarrow \left[\begin{matrix}4&2\\2&6\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\end{matrix}\right]=\left[\begin{matrix}-1\\-5\end{matrix}\right]$

最终模型： $y=0.2-0.9t$

## 最小二乘抛物线拟合令： $y=a_{0}+a_{1}t+a_{2}t^{2}$

*拟合点* $：\left(-1,1\right), \left(0,0\right), \left(1,0\right),(2,-2)$

$\left[\begin{matrix}1&-1&1\\1&0&0\\1&1&1\\1&2&4\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\a_{2}\end{matrix}\right]=\left[\begin{matrix}1\\0\\0\\-2\end{matrix}\right]$

*法线*方程 $：$

$\left[\begin{matrix}1&1&1&1\\-1&0&1&2\\1&0&1&4\end{matrix}\right]\left[\begin{matrix}1&-1&1\\1&0&0\\1&1&1\\1&2&4\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\a_{2}\end{matrix}\right]=\left[\begin{matrix}1&1&1&1\\-1&0&1&2\\1&0&1&4\end{matrix}\right]\left[\begin{matrix}1\\0\\0\\-2\end{matrix}\right]\Longrightarrow \left[\begin{matrix}4&2&6\\2&6&8\\6&8&18\end{matrix}\right]\left[\begin{matrix}a_{0}\\a_{1}\\a_{2}\end{matrix}\right]=\left[\begin{matrix}-1\\-5\\-7\end{matrix}\right]$

最终模型： $y=0.45-0.65t-0.25t^{2}$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/eef32be9d4de70ee3abf64b4829b4877580588d8a5bc367738fbc7092da94101.jpg)

$t$

直线拟合

<table>
  <tr>
    <th>$t$</th>
    <th>$y$</th>
    <th>line</th>
    <th>error</th>
  </tr>
  <tr>
    <td>$-1$</td>
    <td>$1$</td>
    <td>$1.1$</td>
    <td>$-0.1$</td>
  </tr>
  <tr>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0.2$</td>
    <td>$-0.2$</td>
  </tr>
  <tr>
    <td>$1$</td>
    <td>$0$</td>
    <td>$-0.7$</td>
    <td>$0.7$</td>
  </tr>
  <tr>
    <td>$2$</td>
    <td>$-2$</td>
    <td>$-1.6$</td>
    <td>$-0.4$</td>
  </tr>
</table>

直线拟合平方误差 $\left\|r\right\|_{2}^{2}=0.7$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/2cd27764dcedec5cfc9e48c6483466d74f2466c98e47062b675f82a6b6220577.jpg)

$t$

抛物线拟合

<table>
  <tr>
    <th>$t$</th>
    <th>$y$</th>
    <th>parabola</th>
    <th>error</th>
  </tr>
  <tr>
    <td>$-1$</td>
    <td>$1$</td>
    <td>$0.85$</td>
    <td>$0.15$</td>
  </tr>
  <tr>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0.45$</td>
    <td>$-0.45$</td>
  </tr>
  <tr>
    <td>$1$</td>
    <td>$0$</td>
    <td>$-0.45$</td>
    <td>$0.45$</td>
  </tr>
  <tr>
    <td>$2$</td>
    <td>$-2$</td>
    <td>$-1.85$</td>
    <td>$-0.15$</td>
  </tr>
</table>

抛物线拟合平方误差 $\left\|r\right\|_{2}^{2}=0.45$

- 非线性模型的最小二乘拟合：
- 例：给定数据点： $\left(t_{0},y_{0}\right),\left(t_{1},y_{1}\right),\ldots ,\left(t_{m},y_{m}\right),$ 拟合模型为： $y=c_{1}e^{c_{2}t}$

1. 拟合的平方误差：

$SE(c_{1},c_{2})=\left(c_{1}e^{c_{2}t_{0}}-y_{0}\right)^{2}+\ldots +\left(c_{1}e^{c_{2}t_{m}}-y_{m}\right)^{2}$

2. 极小化平方误差：

$\frac{\partial SE}{\partial c_{1}}=2e^{c_{2}t_{0}}\left(c_{1}e^{c_{2}t_{0}}-y_{0}\right)+\ldots +2e^{c_{2}t_{m}}\left(c_{1}e^{c_{2}t_{m}}-y_{m}\right)=0$

$\frac{\partial SE}{\partial c_{2}}=2c_{1}t_{0}e^{c_{2}t_{0}}\left(c_{1}e^{c_{2}t_{0}}-y_{0}\right)+\ldots +2c_{1}t_{m}e^{c_{2}t_{m}}\left(c_{1}e^{c_{2}t_{m}}-y_{m}\right)=0$

- 将上述模型两边取对数将问题线性化

$\hat{y}:=lny=lnc_{1}+c_{2}t=k+c_{2}t$

线性化问题的平方误差:

$\hat{SE}=\left(k+c_{2}t_{0}-lny_{0}\right)^{2}+\ldots +\left(k+c_{2}t_{m}-lny_{m}\right)^{2}$

## 最小二乘

- 使用模型 $y=c_{1}e^{c_{2}t}$ 拟合Intel CPU单元中的晶体管数量随年份的变化：

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/7de8fedc8a2be16824748d7c0e2c597a043fa741f0a6a361601bec9e138b0137.jpg)

## 最小二乘

- 解：1、线性化模型： $\hat{y}:=lny=lnc_{1}+c_{2}t=k+c_{2}t$  ( $t=0$ 对应于1970年)
- 代入数据得到 $Ax=b, x=\left[k,c_{2}\right]^{T}$

$A=\left[\begin{matrix}1&1\\1&2\\1&4\\1&8\\\vdots &\vdots \\1&33\end{matrix}\right], b=\left[\begin{array}{c}ln2250\\ln2500\\ln5000\\ln29000\\\vdots \\ln410000000\end{array}\right]$

- 法线方程 $A^{T}Ax=A^{T}b$ 为：

$\left[\begin{matrix}13&235\\235&5927\end{matrix}\right]\left[\begin{matrix}k\\c_{2}\end{matrix}\right]=\left[\begin{matrix}176.90\\3793.23\end{matrix}\right]$

- 解得 $\left[k,c_{2}\right]^{T}=\left[7.197,0.3546\right]^{T}\longrightarrow \left[c_{1},c_{2}\right]^{T}=\left[1335.3,0.3546\right]^{T}.$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/f67f22fddbfc98b757e352ff76c587eeb8a16816dfb996e288e7eca724778f7d.png)

## 最小二乘

- 最终模型 $y=1335.3e^{0.3546t}$
- 单个CPU单元晶体管个数翻倍时间

$\frac{y_{2}}{y_{1}}=e^{0.3546(t_{2}-t_{1})}=2\rightarrow t_{2}-t_{1}=\frac{ln2}{0.3546}\approx 1.95年（Moore定律）$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/2ab89521970573241ed538c18ec41e4ad7032e0952633129706c838b88c3b3e4.jpg)

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/d0ebb41461bc4bdc70c9bef04e2d87e8dc6274011a62b928a99b0ba0a5cc3af2.jpg)

题中的数据直到近年的数据

## 最小二乘

- 例：令 $\left\{x_{0},\ldots ,x_{10}\right\}$ 为区间 $[2,4]$ 上间隔均匀的点，并设 $y_{i}=\sum_{n=0}^{7}x_{i}^{n} (0\leq i\leq 10)$ .使用法线方程找出拟合 $\left\{\left(x_{i},y_{i}\right)\right\}_{i=0}^{10}$ 的最小二乘多项式 $P\left(x\right)=\sum_{n=0}^{7}c_{n}x^{n}$
- 解：将数据条件代入模型多项式得到：

$\left[\begin{matrix}1&x_{0}&\cdots &x_{0}^{7}\\1&x_{1}&\vdots &x_{1}^{7}\\\vdots &\vdots &\ddots &\vdots \\1&x_{10}&\cdots &x_{10}^{7}\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\c_{7}\end{matrix}\right]=\left[\begin{matrix}y_{0}\\y_{1}\\\vdots \\y_{10}\end{matrix}\right]$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/a399b0749b8faa47a9e6b4775dba9855643d225dc299d4d7ec4ac53090db7627.png)

- 使用MATLAB求解：

与精确解相差很大

$A^{T}A条件$ 数太大属于病态问题！

## QR分解与最小二乘

- 实现QR分解的方法

1. Gram-Schmidt正交
2. Householder变换

- $QR$ 分解的应用

1. 求解 $n\times n$ 线性方程组： $Ax=b\rightarrow QRx=b\rightarrow Rx=Q^{T}b$ .
2. 求 $A$ 的特征值的QR算法
3. 求解 $m\times n(m>n超定)$ 线性方程组的最小二乘解

## QR分解与最小二乘

- $QR$ 分解求解超定线性方程组 $Ax=b$ 的最小二乘解：最小化 $\left\|b-Ax\right\|_{2}$

正交矩阵保持向量的欧几里得长度不变： $\left\|b-Ax\right\|_{2}=\left\|b-QRx\right\|_{2}=\left\|Q^{T}b-Rx\right\|_{2}$

最小二乘解相当于最小化 $\left\|Q^{T}b-Rx\right\|_{2}$ ，令 $d:=Q^{T}b$ ，则

$Rx-d=\left[\begin{matrix}r_{11}&r_{12}&\cdots &r_{1n}\\&r_{22}&\cdots &r_{2n}\\&&\ddots &\vdots \\&&&r_{nn}\\0&\cdots &\cdots &0\\\vdots &&&\vdots \\0&\cdots &\cdots &0\end{matrix}\right]\left[\begin{array}{c}x_{1}\\\vdots \\x_{n}\end{array}\right]-\left[\begin{array}{c}d_{1}\\\vdots \\d_{n}\\d_{n+1}\\\vdots \\d_{m}\end{array}\right]=\left[\begin{array}{c}e_{1}\\\vdots \\e_{n}\\e_{n+1}\\\vdots \\e_{m}\end{array}\right]$

当 $\hat{e}=\hat{R}x-\hat{d}=0$ 时， $\left\|Q^{T}b-Rx\right\|_{2}=\left\|d-Rx\right\|_{2}$ 取得最小值即最小二乘解为 $\hat{R}x=\hat{d}$  (避免了求解法向方程 $A^{T}Ax=A^{T}b$ )

$\hat{d}$

$\hat{e}$

$\hat{R}$

$=\left[\begin{array}{c}-d_{n+1}\\\vdots \\-d_{m}\end{array}\right]$

- 例：求解方程组的最小二乘解

$\left[\begin{matrix}1&-4\\2&3\\2&2\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{array}{c}-3\\15\\9\end{array}\right]$

解：法线方程为 $A^{T}Ax=A^{T}b$ :

$\left[\begin{matrix}1&2&2\\-4&3&2\end{matrix}\right]\left[\begin{matrix}1&-4\\2&3\\2&2\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{matrix}1&2&2\\-4&3&2\end{matrix}\right]\left[\begin{array}{c}-3\\15\\9\end{array}\right]$

即：

$\left[\begin{matrix}9&6\\6&29\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{array}{c}45\\75\end{array}\right]\Rightarrow \left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{array}{c}3.8\\1.8\end{array}\right]$

误差： $r=b-Ax=\left[\begin{array}{c}-3\\15\\9\end{array}\right]-\left[\begin{matrix}1&-4\\2&3\\2&2\end{matrix}\right]\left[\begin{array}{c}3.8\\1.8\end{array}\right]=\left[\begin{array}{c}0.4\\2\\-2.2\end{array}\right], \left\|r\right\|_{2}=\sqrt{\left(0.4\right)^{2}+2^{2}+\left(-2.2\right)^{2}}=3$

- QR分解法求解

1. 对系数矩阵做QR分解

$A=\left[\begin{matrix}\frac{1}{3}&-\frac{14}{15}&\frac{2}{15}\\\frac{2}{3}&\frac{1}{3}&\frac{2}{3}\\\frac{2}{3}&\frac{2}{15}&-\frac{11}{15}\end{matrix}\right]\left[\begin{matrix}3&2\\0&5\\0&0\end{matrix}\right]=QR$

2. 求解 $Rx=Q^{T}b$

$\left[\begin{matrix}3&2\\0&5\\0&0\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{matrix}\frac{1}{3}&\frac{2}{3}&\frac{2}{3}\\-\frac{14}{15}&\frac{1}{3}&\frac{2}{15}\\\frac{2}{15}&\frac{2}{3}&-\frac{11}{15}\end{matrix}\right]\left[\begin{array}{c}-3\\15\\9\end{array}\right]=\left[\begin{array}{c}15\\9\\3\end{array}\right]$

最小二乘解： $\left[x_{1},x_{2}\right]^{T}=\left[3.8,1.8\right]^{T}$

误差： $r=\left\|Q^{T}b-Rx\right\|_{2}=3$

- 例：令 $\left\{x_{0},\ldots ,x_{10}\right\}$ 为区间 $[2,4]$ 上间隔均匀的点，并设 $y_{i}=\sum_{n=0}^{7}x_{i}^{n} (0\leq i\leq 10)$ .使用法线方程找出拟合 $\left\{\left(x_{i},y_{i}\right)\right\}_{i=0}^{10}$ 的最小二乘多项式 $P\left(x\right)=\sum_{n=0}^{7}c_{n}x^{n}$

解：将数据条件代入模型多项式得到：

$\left[\begin{matrix}1&x_{0}&\cdots &x_{0}^{7}\\1&x_{1}&\vdots &x_{1}^{7}\\\vdots &\vdots &\ddots &\vdots \\1&x_{10}&\cdots &x_{10}^{7}\end{matrix}\right]\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\c_{7}\end{matrix}\right]=\left[\begin{matrix}y_{0}\\y_{1}\\\vdots \\y_{10}\end{matrix}\right]$

![](../../../../../../../04_Assets/Images/Courses/%E5%BD%92%E6%A1%A3/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90/%E8%AF%BE%E4%BB%B6/MD/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%9008Fitting/images/72aea8708d88d4e3c681ee94ec30d2f8d7f3d0d533e11b0530365da7fa881686.jpg)

$\left[\begin{matrix}c_{0}\\c_{1}\\\vdots \\c_{7}\end{matrix}\right]=$

QR分解得到的解

## 思考与练习

- 用周期模型 $F_{3}\left(t\right)=c_{1}+c_{2}\cos(2\pi t+c_{3}\sin(2\pi t))$ 拟合以下数据：

$\left(0,0\right),\left(\frac{1}{6},2\right),\left(\frac{1}{3},0\right),\left(\frac{1}{2},-1\right),\left(\frac{2}{3},1\right),\left(\frac{5}{6},1\right)$

- 分别使用法线方程和QR分解求解方程的最小二乘解，并求出二范数误差

$\left[\begin{matrix}-4&-4\\-2&7\\4&-5\end{matrix}\right]\left[\begin{array}{c}x_{1}\\x_{2}\end{array}\right]=\left[\begin{array}{c}3\\9\\0\end{array}\right]$

- 编程：令 $\left\{x_{0},\ldots ,x_{20}\right\}$ 为区间 $[2,4]$ 上间隔均匀的点，并设 $y_{i}=\sum_{n=0}^{10}x_{i}^{n} (0\leq i\leq 20)$ .使用法线方程和QR分解找出拟合 $\left\{\left(x_{i},y_{i}\right)\right\}_{i=0}^{20}$ 的最小二乘多项式 $P\left(x\right)=\sum_{n=0}^{10}c_{n}x^{n}$