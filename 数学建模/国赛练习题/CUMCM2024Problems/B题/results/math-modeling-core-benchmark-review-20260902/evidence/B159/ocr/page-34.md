# 附录5 问题四求解问题三代码

1Iimport numpy as np

from scipy.stats inport beta

4＃模拟基于Beta分布的次品率商率的函数

5def defectprobability(n,p):

6

＃Beta分布参数：np1（成动次数）,n-np1（失收次数）

7

$$a=1+n\star p$$

8

$$b=1+n-n\star p$$

9

return beta(a,b)

10

11 ＃计算零件、半成品和成品的次品分布的函数

12 **def simulatedefect(n,p** $\text {trials=10000}$  :

13

14

betadistribution=defectprobability(n,p)

15

defectratesamples=betadistribution.rvs(size=trials)

16

17

partdefects= np.randon.binomial(1,defectratesamples,size=trials)

18

semiproductdefects=np.randon.binomial(1,defectratesamples,size=trials)

19

finalproductdefects=np.random.binomial(1,defectratesamples,size=trials)

20

21

return partdefects,seniproductdefects,finalproductdefects

22

23 $n=100$ 

24 $p=0.1$ 

25 trials=10000

26

27 ＃运行模拟

28 partdefects,seniproductdefects,finalproductdefects=sinulatedefect(n,p,trials)

29

30 ＃计算改品率

31 $part\_defect\_prob=np.mean(part\_defects)$ 

32 semiproductdefectprob=np.mean(semiproductdefects)

33 $final\_product\_defect\_prob=np.mean(final\_product\_defects)$ 

## 附录6 灵敏度检验代码

1ibrary(cubature)

＃定义常数参数

n&lt;-100

a&lt;-0.1

d&lt;-0.1

9 $<-$ 0.1

&lt;-56

--

&lt;-

10

--

12 --

13

14

15 beta0 $<-1$ 

16

17 定义Beta 分布的密度函数

19

18-betadensity return(dbeta $<$ function(x, (x,shapel=s $alpha,beta)$  $、$ 2beta))

20-)

21

22 定义目标函数 $h\_func(pl,$ p2,p3)

23-hfunc $<-$ function(p)(

24 $p1$ $p$ 1]

25

26 $p3<-p[3]$ 

27

28

30 return(result)

31-1

result 29 $<-j-(b+c)/(1-p1)-(e+f)/(1-p2)-h/(1-p3)-$ $i_{\text {D}}$ $(k+1)=p3$ $/(1-p3)$  中国大学生在线

dxs.moe.gov.cn

<!-- 34 -->

