20 def $get\_c(p0$ ,pl,alpha,belta,n):

21

#print(p0,pl,alpha,belta,n)

22

1value $=n*p1+$ $quantile\_value(belta)*math.sqrt(n*p1*(1-p1))$ 

23

$$r\_value=n*p0+quantile\_value(1-alpha)*math.sqrt(n*p0*(1-p0))$$

24

return 1value, $r\_value$ 

25

26def $get\_ans(p1,belta):$ 

$\mathrm {n}=\mathrm {get}\_\mathrm {n}(\mathrm {p}0,$ pl,alpha,belta)

25

$c\_1,$ $c\_r=$ $get\_c(p0,$  p1,alpha,belta,n)

20

# print $(n,c\_l,c\_r)$ 

returnn, $c\_1$ 

31

def $get\_ans\_n(p1$ ,belta):

33

$\mathrm {n}=\mathrm {get}\_\mathrm {n}(\mathrm {p}0,$ ,p1,alpha,belta)

$c\_1,$ $c\_r=$ $get\_c(p0$ ,pl,alpha,belta,n)

35

#print $(n,$ $c\_l,c\_r)$ 

36

return n

38＃todo：问题一，法一

print（”问题二，法一”）

$f1=$ open（”问题二， $法一.txt"$ , $\text {mode}=\text {"w"}$ , $encoding="utf-8")$ 

$$\mathrm {p}0=0.1$$

$$belta=0$$

$$p1=0$$

44 $\text {alpha}=0.1$ 

for pl in [0.001*forin range(1,1000)if $0.001*\_!=p0]$ :

for belta in [0.01*for $-$ in range(1,,100)]:

$$n,\quad c=get\_ans(p1,belta)$$

48

if $c<0:$ 

40

continue

60

$\text {f1.write}\left(\mathrm {f}^{\prime \prime }\mathrm {pl}=\{\mathrm {pl}\}\right.$ ， $belta=\{belta\},,,$ 此时n为： $\{n\},c为:\{c\}n")$ 

61

＃print(f”解为： $\mathrm {p}1=\{\mathrm {p}1\}$ $,alpha=\{alpha\}")$ 

52

＃print(f”此时n为：{n},c为： $\{c\}")$ 

53 $x=np$ ,array $([0.001*\_$ for $\checkmark$  range(1,1000)if $0.001*\underline {}!=p0])$ 

54 $y=np$ $.array($ $([0.01*\_$ forinrange(1,,100)])

55 $x,$ $y=np.meshgrid(x,y)$ 

50customfunctionvectorized $=np$ $.vectorize(get\_ans\_n)$ 

57z=customfunctionvectorized(x,y)

58＃创建三维图形对象

50 $fig=plt.figure()$ 

60 $ax=fig.add\_subplot(111$ ,projectic $on='3d'$ $\therefore$ 

61

62＃绘制三维图形

6.3 $ax.plot\_surface(x$ $,y$ ,2 $,cmap='viridis$  -

64

65＃设置坐标轴标签

66 $ax.set\_xlabel('p1')$ 

67 $ax.set\_ylabel('belta')$ 

中国大学生在线

68 $ax.set\_zlabel('n')$ 

60 $ax.set\_title($ 问题二 方法一＇）

dxs.moe.gov.cn

70 plt.show()

<!-- 23 -->

