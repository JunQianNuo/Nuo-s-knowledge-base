121def $get\_p(delta,t):$ 

122

＃返回一个无限小的正数，范围为0到1

123

＃随着退火次数增加而越来越小

124

return $math.exp(-delta/t)$ 

125

126＃#todo：问题一，法一

127#print（”问题一，法一”）

128# $f1=open$ （”问题一，法 $一.txt"$ , $mode="w"$ ,encodi $ng="utf-8")$ 

129# $p0=0.1$ 

130# $\text {belta}=0.05$ 

131 # $\mathrm {p}1=0.15$ 

132# $\text {alpha}=0.1$ 

133# for $p1$  in [0.001*for in $range(1$ $,1000)if0.001*\_!=p0]:$ 

134#

foralpha in [0.01* $for\_in$ range(1,100)]:

135#

n, $c=get\_ans(p1,alpha)$ 

136 #

if $c<0:$ 

137#

continue

138#

f1.write( $(f"p1=\{p1\}$  $alpha=\{alpha\},,此时n为:$ ｛n},c为： $\{c\}n")$ 

130#

＃print(f”解为： $p1=\{p1\}$ 、 $alph$ $a=\{alpha\}")$ 

140#

＃print(f”此时n为：{n},c为： $\{c\}")$ 

141# $x=np.array([0.001*\_$ $for$  range(1,1000)if 0 $0.001*\_!=p0]$ 

142# $y=np.array([0.01*\_for\_in$  range(1 $,100)])$ 

145# $x,$ $y=np.meshgrid(x,y)$ 

144#customfunctionvectorized $=np.vectorize(get\_ans\_n)$ 

145# $z=custom\_function\_vectorized(x,y)$ 

146＃＃创建三维图形对象

147# $fig=plt.figure()$ 

148# $ax=fig$ ,addsubplot(111 $,projection='3d')$ 

140#

150＃＃绘制三维图形

151# $ax.plot\_surface(x,y,z$  $cmap='viridis$ ')

152#

16.3＃＃设置坐标轴标签

154# $ax.set\_xlabel('p1')$ 

155#ax.set $\_ylabel$ $('alpha')$ 

15.0# $ax.set\_zlabel('n')$ 

167＃ax.settitle(＇问题一 方法一＇）

158##ax.setzlim(0,10)

159#plt.show()

160#

161## $\mathrm {t}=1000$ 

＃初始化温度值

162## $t\_min=980$  ＃设置温度下限

163## $k=1000$ 

＃设置迭代次数（有用吗）

164##

165## while $(\mathrm {t}>\mathrm {t}\_\mathrm {min}):$ 

166##

for i in range(500):

167##

$$n,\quad c=\quad get\_ans\quad (p1,\quad alpha)$$

168##

$$p1\_,alpha\_=get\_new\_ans(p1,alpha,t)$$

在线中国大学生 $cn$ 

160##

if $is\_ans(pl\_,$ $alpha\_):$ 

$$n\_,c\_=get\_ans(pl\_,alpha\_)$$

dxs.moe.gov.

170##

171##

$$delta=n\_-n$$

<!-- 25 -->

