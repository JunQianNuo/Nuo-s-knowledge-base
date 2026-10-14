在给定n、c的情况下，将 $L(p,n,c)$ 简记为 $L(p)$ 。由此可以将问题一转化为以下数学问题：

从整批产品中随机抽取n件产品进行检验（即检验次数为n)，其中次品的件数记为v。若 $v\leq c$ 时，接受 $H_{0}$ 事件；若 $v\geq c$ 时，拒绝 $H_{0}$ 事件，即接受 $H_{1}$ 事件。若这批产品的次品率 $p\geq p_{1}$ ，则理想情况下应当出现 $H_{1}$ 事件，而 $L(p)$ 的值为判断成 $H_{0}$ 事件的概率，亦即判断错误的概率。由题知，该概率应当小于等于 $\beta$ ，即

$$L\left(p_{1}\right)\leq L(p)\leq \beta$$

同理，若这批产品的次品率 $p\leq p_{0}$ ，则理想情况下应当出现 $H_{0}$  事件，而 $L(p)$ 的值为判断成 $H_{0}$ 事件的概率，则错判为 $H_{1}$ 事件的概率为 $1-L(p)$ 。由题知，该概率应当小于等于α，即

$$1-L(p_{0})\leq 1-L(p)\leq \alpha$$

即对给定的 $p_{0}、p_{1}、\alpha 、\beta$ ，给出检验次数n、检验判据c，使之满足以上两个约束条件。因为L的表达式较复杂，精确求解以上两式较为困难，当n较大时，可以利用

$$T=\frac {v-np}{\sqrt {np(1-p)}}$$

渐近于N(0,1）标准正态分布作近似处理。因为在实际应用中，当样本容量较大时（通常大于30),t分布的t值会逼近于标准正态分布的z值，因此可以使用正态分布表中的值来近似t 分布的计算。由于n较大的情况下，二项分布 $B(n,p)$ 也近似于正态分布，则所给约束条件可进行如下转化

$$L\left(p_{1}\right)\leq \beta \Leftrightarrow T\left(n,c,p_{1}\right)\leq Z(1-\beta )\quad L\left(p_{0}\right)\geq 1-α\Leftrightarrow T\left(n,c,p_{0}\right)\geq Z(α)$$

解得

$$np_{1}+Z(1-\beta )\sqrt {np_{1}\left(1-p_{1}\right)}\geq c\geq np_{0}+Z(α)\sqrt {np_{0}\left(1-p_{0}\right)}$$

$$\sqrt {n}\geq \frac {Z(α)\sqrt {p_{0}\left(1-p_{0}\right)}-Z(1-\beta )\sqrt {p_{1}\left(1-p_{1}\right)}}{p_{1}-p_{0}}$$

# 5.1.6 问题1(1）的求解

未知数为 $p_{1}$ 和α。

方法一：

通过遍历 $p_{1}$ 1和α得到n的最小值。

因为

$$\sqrt {n}\geq \frac {Z(α)\sqrt {p_{0}\left(1-p_{0}\right)}-Z(1-\beta )\sqrt {p_{1}\left(1-p_{1}\right)}}{p_{1}-p_{0}}$$

故

$$n_{\min }=\frac {\left[Z(α)\sqrt {p_{0}\left(1-p_{0}\right)}-Z(1-\beta )\sqrt {p_{1}\left(1-p_{1}\right)}\right]^{2}}{\left(p_{1}-p_{0}\right)^{2}}$$

为便于分析，以 $p_{1}$ 1和α为横、纵坐标，n为纵坐标，作出二维函数图。

<!-- 7 -->

