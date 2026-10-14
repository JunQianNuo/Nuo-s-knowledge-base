# 附录1 问题一求解代码

1定义 calculateexpression 函数

2calculateexpression &lt;-function(n,p){

u0.95&lt;-qnorm(0.95)

terml $<-0.3=u\_0.95/sqrt(n$ 

6

term2 $<-$ $0.1-p$ 

7

term3 $<-$ $\text {sqrt}(p*(1-p)/n)$ 

8

zvalue $<-(terml+term2)/$ term3

9

$$result<-1-pnorm(z\_value)$$

10

11

return(result)

12-}

13

14#初始化结果向量

15 $x<-numeric(1000)$ 

16

17 ＃循环计算积分

18-for(n in 1:1000)(

19

定义被积函数，将n固定到当前循环的值

20 integrand $<-$ function(p)(

21

return(calculateexpression(n,p))

22- }

23

24 ＃计算从0.1到1对p的积分

25 result &lt;-integrate(integrand, $\text {lower}=0.1$ , $\text {upper=1)}$ 

26

27 ＃计算最终结果并存储

28

x[n] $<--resultsvalue=0.999+0.001=n$ 

29-)

30 minvalue $<-$ min(x)

31 minposition&lt;-which.min(x)

32

33 cat（“最小值：”，minvalue， $"(n")$ 

34 cat（”最小值出现的位置：",minposition,"\n"）

# 附录2 问题二求解代码

第一组数据

a-0.1

b-4

c-2

d=0.1

e-18

f-3

g-0.1

h-6

10 i=3

1-56

k-6

13 1-5

14 jjjc=j-(b+c)/(1-a)-(e+f)/(1-d)-(h+i)/(1-9)-1*g/(1-g)

15 jjbc-j $(b+c)/(1-a)-(e+f)/(1-d)-h/(1-g)-(k+1)^{2}g/(1-g)$ 

16 jjjb=j-((b+c)/(1a)(e+f)/(1d)+h+i)/1-g)

17 jjbb=j-((b+c)/(1-a)+(e+f)/(1-d)+h)/(1-g)-k*g/(1-g)

18 jbjb-j-((b+c)/(1-a)+e+h+1)/(1-(d+(1-d)*g))

19 jbbb=j-( $(b+c)/(1-a)+e+h)/(1-(d+(1-d)^{\circ }g))-k^{\circ }(d+(1-d)^{\circ }g)/(1-(d+(1-d)^{\circ }g))$ 

20 bjjb-j-(+(e+f/(1-d)+h+1)/(1-(a+(1-a)*g))

21 bjbb-j-(b+(e+f)/(1-d)+h)/(1-(a+(1-a)*g))-k*(a+(1-a)"g)/C1-Ca+(1-a)*g))

22 bbjb-j-(b+e+h+i)/(1-a)/(1-d)/(1-g)

23 bbbb=j-(b+e+h)/(1-a)/(1-d)/(1-g)-k*(1/(1-a)/(1-d)/(1-g)-1)

24 b $jjc=j-(b+(e+f)/(1-d)+h+i+(a+g-a^{\circ }g)^{\circ }(c+(h+i+1)/(1-g))+a^{\circ }(b+c)/(1-a))$ 

25 jbjc-j-(e+(b+c)/(1-a)+h+i+(d-g-d'g)*(f+(h+1+1)/(1-g))+d*(e+f)/(1-d))

26 bbjc-j-((b+e+h+i)+((c+f)+(h+i+1)/(1-g))*(1-(1-a)*(1-d)*(1-g))+(e+f)*d/(1-d)+(b+c)*a/(1-a))

27 bjbc=j-(b+(e+f)/(1-d)+h+(c+(h+k+1)/(1-g))*(a+g-a*g)+(b+c)*a/(1-a))

28 jbbc=j-(e+(b+c)/(1-a)+h+(f+(h+k+1)/(1-g))*(d+g-d°g)+(e+f)*d/(1-d))

29

30 jjjc

31 jjbc

jjjb

33 13b6

34 jbjb

35 jbbb

36 bjjb

37 bjbb

38 bbjb

39 bbbb

40 bjjc

41 jbjc

中国大学生在线

42 bbic

dxs.moe.gov.cn

<!-- 25 -->

