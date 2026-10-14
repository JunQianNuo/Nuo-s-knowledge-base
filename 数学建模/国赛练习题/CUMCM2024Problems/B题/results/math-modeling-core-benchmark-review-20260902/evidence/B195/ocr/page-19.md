# 5.4.1 先验分布

首先假设真实的次品率服从Beta分布，即先验分布。（Beta分布具有较好的性质，适于表示在［0,1］区间上各种形状的概率分布。因为它具有良好的形状灵活性，能够很好地描述对参数的先验认识，在贝叶斯统计中，Beta分布常常被用作先验分布。）Beta函数的定义为

$$B(\alpha ,\beta )=\int _{0}^{1}u^{\alpha -1}(1-u)^{\beta -1}du$$

Beta 分布的均值和方差分别为

$$\mu =\frac {\alpha }{\alpha +\beta }$$

$$\sigma ^{2}=\frac {\alpha \beta }{(\alpha +\beta )^{2}(\alpha +\beta +1)}$$

归一化后得到的次品概率密度分布函数

$$p(\theta )=f(\theta ;\alpha ,\beta )=\frac {\theta ^{\alpha -1}(1-\theta )^{\beta -1}}{B(\alpha ,\beta )}$$

# 5.4.2 似然函数

抽样数据服从二项分布，若次品率为 $\theta$ ，抽样n次，则出现c次次品的概率可以表示为

$$L(\theta ,c)=\binom {n}{c}\theta ^{c}(1-\theta )^{n-c}$$

# 5.4.3 后验概率

最后利用贝叶斯公式计算后验分布，并通过后验均值（即后验分布的最可能值）来估计真实的次品率，从而得到可能的真实次品率以及对应的置信度。积分形式下贝叶斯公式为

$$P(\theta |c)=\frac {L(\theta |c)p(\theta )}{\int L(\theta |c)p(\theta )\mathrm {d}\theta }$$

对于连续的参数变量 $\theta$ θ，其后验概率密度即为 $P(\theta \vert c)。$ 

为计算以上公式，需要设定 $α$ 、 $\beta$ 的初始值。其取值大小取决于对参数的信心程度。取值较小时，即对参数的先验知识不强，从而准许更多可能性；取值较大时，即对参数的先验性较强，对概率分布情况更有信心。参数的选择可以显著影响最终的后验分布，从而影响对真实参数的估计结果。

在贝叶斯推断中，通常会根据先验信息和信念程度来选择合适的先验分布参数alpha和beta。根据似然原则，令先验函数与似然函数成比例，则

$$α-1=c$$

$$\beta -1=n-c$$

带入贝叶斯公式，得到二项分布数据的后验概率密度函数

$$P(\theta \vert c)=\frac {\theta ^{\bar {\alpha }-1}(1-\theta )^{\bar {\beta }-1}}{B(\bar {\alpha },\bar {\beta })}$$

dxs.moe.gov.cn

<!-- 19 -->

