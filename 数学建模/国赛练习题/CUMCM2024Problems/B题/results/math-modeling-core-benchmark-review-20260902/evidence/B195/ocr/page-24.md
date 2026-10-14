71

72from scipy.stats import norm

73import math

74import random

76import matplotlib.pyplot as plt

70import numpy as np

77

78plt.rcParams['font.sans-serif' $]=$ 'KaiTi']

70 plt.rcParams['axes.unicodeminus $']=Fals$ 

80

def $quantile\_value(p):$ 

82

＃计算标准正态分布的第p分位数值

83

$$\text {value}=\text {norm.ppf(p)}$$

84

return value

85

86 def $get\_n(p0,p1,alpha,belta):$ 

87

$$\text {swap_{n}=quantile_{value}(1-alpha)*math.sqrt(p0*(1-p0))-quantile_{value}(belta)}$$

$$\text {math.sqrt}(\mathrm {p}1*(1-\mathrm {p}1))$$

88

swap $p\_n$ $/=p1-p0$ 

return swapn**2if $swap\_n**$ $2<100$ else 100

90

92

91 def $get\_c(p0,p1,alpha$ ,belta, 2 $l\_value$ $=\mathrm {n}*\mathrm {pl}+$ quantilevalue(belta)*math. $\text {sqrt}(\mathrm {n}*\mathrm {pl}*(1-\mathrm {pl})$ 

$$r\_value=n*p0+quantile\_value(1-alpha)*math.sqrt(n*p0*(1-p0))$$

94

return $l\_value,r\_value$ 

95

96defgetnew $\_ans(p1$ ,alpha,t)

97

p1 $+=2*$ $random.random()*math.exp(t-1000)-math.exp(t-1000)$ 

03

$\text {alpha}+=2*$ random.random()* math.exp(t-1000)-math.exp(t-1000)

00

returnp1,alpha

100

101def $get\_ans(p1$ ,alpha):

102

$n=$ $get\_n(p0$ ,p1,alpha,belta)

103

$c\_1,$ $\text {c_{r}=get_{c}(p0,}$ p1,alpha,belta,n)

104 # print $(n,$ $c\_l,c\_r)$ 

105

return。 $c\_1$ 

106

107 def $get\_ans\_n(p1,alpha):$ 

108

$\mathrm {n}=\text {get_{n}(p0,}$ -p1,alpha,belta)

109

$c\_l,c\_r=$ getc(p0,pl,alpha,belta,n)

110 # $print(n,c\_l,c\_r)$ 

111

return n

112

113def $is\_ans(p1$ . $alpha):$ 

114

if $\mathrm {p}1<0.13$ or $\mathrm {p}1>0.19\text {or}\mathrm {p}1<=\mathrm {p}0:$ 

115

return $False$ 

116

if $\text {alpha}<0\text {oralpha}>1:$ 

117

return False

中国大学生在线

118

return True

dxs.moe.gov.cn

119

120

<!-- 24 -->

