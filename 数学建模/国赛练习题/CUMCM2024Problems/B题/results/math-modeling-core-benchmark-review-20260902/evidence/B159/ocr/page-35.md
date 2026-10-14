33定义联合密度函数

34-jointdensity&lt;-function(p, alphal,betal,alpha2,beta2,alpha3,beta3){

35

p1&lt;-p[1]

36

p2&lt;-p[2]

37

p3 $<$ p[3]

38

39

return(betadensity(pl,alphal,betal)*

40

betadensity(p2,alpha2,beta2)

41

betadensity(p3,alpha3,beta3))

42-)

43

44 ■定义被积函数，考虑联合密度

45-integrand $<-$ function(p,alphal,betal,alpha2,beta2,alpha3,beta3)(

46 return(hfunc(p) jointdensity(p,alphal,betal,alpha2,beta2,alpha3,beta3))

47-)

48

49 ＃设置积分范围：每个变量的范围是［0,1］

50 lowerlimit $<-$ c(0,0,0)

51 $upper\_limi$ $<-$ c(1,1,1)

52

53

初始化结果向量和alphao向量

54 results $<-$ numeric(10)

55 alpha0values $<-$ 1:10

56

57 计算每个alpha0 对应的期望值

58-for(alpha0 in alpha0values){

59

alpha1&lt;-alphao $+^{\circ }$ 

60

**betal** $<-beta0+n-n^{\circ }$ 

61

62 $alpha2$ $<-alpha0+n^{\circ }d$ 

63

$$beta2\quad <-beta0+n-n^{\circ }d$$

64

65

$alpha3$ $<-alpha0+n^{\circ }$ 66 $beta3$  $\;\cdot \;$ $<-beta0+n-n^{\circ }$ 

67

68

69

**result** $<-$ adaptIntegrate(function(p) integrand(p,alphal,betal,alpha2,beta2,

alpha3,beta3),

70

lowerLimit-lowerTimit,upperLimit=upperTimit)

71

72 $results[alpha0]$ &lt;-resultSintegral

73-)

75 输出结果

76 cat(＂期望值向量：”，results,"\n"）

77

78 ■将结果绘制成散点图

79 plot(alpha0values,results,

80

$type$ $="p"$ 

81

82

83

84

$$ylab="期望值",\\ ylim=c(0,20))$$

85 ■进行线性拟合

86 $fit<-Im(results-alphao\_values)$ 

87

88 ＃添加线性拟合线

89 abline(fit,col-blue

90

91 ■输出线性拟合结果

92 cat（“线性报合结果：\n”）

93 print(summary(fit))

94

95 &lt;-100

96 &lt;-0.1

97 d&lt;-0.1

98 9-- 0.1

99 -56

100 b

101 &lt;-

102 e&lt;-18

103 &lt;-

104

105 --

106 1&lt;

107 alpha0&lt;-1 #alpha0 不变

108

109 ■定义 Beta分布的密度函数

111

110-betadensity $<-$ function(x,alpha,beta)、return(dbeta(x,shapel=alpha,shape2-beta))

112-)

中国大学生在线

dxs.moe.gov.cn

<!-- 35 -->

