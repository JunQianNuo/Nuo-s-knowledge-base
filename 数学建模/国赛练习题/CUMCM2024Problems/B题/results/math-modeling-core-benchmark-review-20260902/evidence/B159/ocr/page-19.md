$$\hat {p}=\frac {\alpha +k-1}{\alpha +\beta +n-2}=\frac {k}{n}$$

故 $p$ 的后验分布为 $\text {Beta}(1+n\widehat {p},1+n-n\widehat {p})$ 

# 8.2求解问题二

回忆第二问中每生产一件合格单品利润期望的表达式，不难发现在给定策略之下，利润的期望仅与零配件1、零配件2、成品的次品率 $p_{1},p_{2},p_{3}$ 有关，故可将策略i的利润期望写成 $p_{1},p_{2},p_{3}$ 的函数 $h_{i}\left(p_{1},p_{2},p_{3}\right)$ 假定 $p_{1},p_{2},p_{3}$ 的密度函数分别为 $\varphi _{1}\left(p_{1}\right),\varphi _{2}\left(p_{2}\right),\varphi _{3}\left(p_{3}\right)$ ，则在上述条件之下利润期望 $E\left(h_{i}\left(p_{1},p_{2},p_{3}\right)\right)$ 满足：

$$E\left(h_{i}\left(p_{1},p_{2},p_{3}\right)\right)=\int _{0}^{1}\int _{0}^{1}\int _{0}^{1}h_{i}\left(p_{1},p_{2},p_{3}\right)\varphi _{1}\left(p_{1}\right)\varphi _{2}\left(p_{2}\right)\varphi _{3}\left(p_{3}\right)dp_{1}dp_{2}dp_{3}$$

由于不同零件检测单价的不同，不同零件的检测样本量n并不完全相同。在第一问中，得到了样本量n的决策函数 $g(n)$ ，即：

$$n_{i}=\text {argming}\left(n_{i}\right)=\underset {n}{\text {argmin}}\left(w_{1}c_{i}n_{i}-w_{2}\int _{0.1}^{1}\pi (p)K\left(n_{i},p\right)dp\right)(i=1,2,3)$$

其中 $n_{1},n_{2},n_{3}$ 3分别表示零配件1、零配件2、成品的检验样本量，决定 $p_{1},p_{2},p_{3}$ 的后验分布： $c_{1},c_{2},c_{3}$ 分别表示零配件1、零配件2、成品的检测成本； $w_{1},w_{2}$ 为实现给定的权重，衡量企业对于检测费用和检测效果的看重程度； $K\left(n_{i},p\right)$ 为问题一中假设检验的功效函数， $\pi (p)为p$ 的先验分布，已假定为均匀分布。

综 $E\left(h_{i}\left(p_{1},p_{2},p_{3}\right)\right)$ $\begin{array}{l}\text {合上述信息，得到}E\left(h_{i}\left(p_{1},p_{2},p_{3}\right)\right)\text {的计算公式如下：}\\
\left\{\begin{array}{c}E\left(h_{i}\left(p_{1},p_{2},p_{3}\right)\right)=\int_{0}^{1}\int_{0}^{1}\int_{0}^{1}h_{i}\left(p_{1},p_{2},p_{3}\right)\varphi_{1}\left(p_{1}\right)\varphi_{2}\left(p_{2}\right)\varphi_{3}\left(p_{3}\right)dp_{1}dp_{2}dp_{3}\\
\varphi_{i}\left(p_{i}\right)=\frac{\Gamma\left(2+n_{i}\right)}{\Gamma\left(1+n_{i}p_{i}\right)\Gamma\left(1+n_{i}-n_{i}p_{i}\right)}p_{i}^{n_{i}\hat{p}_{i}}\left(1-p_{i}\right)^{n_{i}-n_{i}\hat{p}_{i}}\\
n_{i}=\operatorname{argmin}\left(w_{1}c_{i}n_{i}-w_{2}\int^{1}\pi(p)K\left(n_{i},p\right)dp\right)(i=1,2,3)\end{array}\right.\end{array}$ 

运用R语言计算积分，得到在问题四假设下，各种决策策略生成一个合格成品的平均利润如下表所示：

**表7 问题二6种情况16种决策方案对应的利润期望值表**

<table border="1" ><tr>
<td>决策编号</td>
<td>情况1</td>
<td>情况2</td>
<td>情况3</td>
<td>情况4</td>
<td>情况5</td>
<td>情况6</td>
</tr><tr>
<td>001</td>
<td>14.99</td>
<td>9.24</td>
<td>14.99</td>
<td>14.29</td>
<td>8.96</td>
<td>15.20</td>
</tr><tr>
<td>002</td>
<td>17.62</td>
<td>11.45</td>
<td>14.69</td>
<td>8.94</td>
<td>9.98</td>
<td>17.76</td>
</tr><tr>
<td>003</td>
<td>15.87</td>
<td>8.25</td>
<td>15.87</td>
<td>12.24</td>
<td>6.99</td>
<td>14.98</td>
</tr><tr>
<td>004</td>
<td>18.18</td>
<td>9.84</td>
<td>12.65</td>
<td>1.13</td>
<td>6.36</td>
<td>17.12</td>
</tr><tr>
<td>005</td>
<td>15.07</td>
<td>7.62</td>
<td>15.07</td>
<td>12.24</td>
<td>13.92</td>
<td>14.09</td>
</tr><tr>
<td>006</td>
<td>17.38</td>
<td>9.21</td>
<td>11.86</td>
<td>1.13</td>
<td>14.08</td>
<td>16.24</td>
</tr><tr>
<td>007</td>
<td>15.68</td>
<td>6.57</td>
<td>15.68</td>
<td>10.49</td>
<td>10.86</td>
<td>13.77</td>
</tr><tr>
<td>008</td>
<td>17.70</td>
<td>7.67</td>
<td>9.87</td>
<td>-5.21</td>
<td>9.55</td>
<td>15.53</td>
</tr><tr>
<td>009</td>
<td>11.90</td>
<td>1.60</td>
<td>11.90</td>
<td>7.65</td>
<td>4.99</td>
<td>15.91</td>
</tr></table>

$$cn$$

$$dxs.moe.$$

<!-- 19 -->

