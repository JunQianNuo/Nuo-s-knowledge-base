187

if $\text {enum}<0$  or $\text {enum}>1:$ 

188

returnFalse

189

return True

190＃todo：设定初始值

191 $\mathrm {t}=1000$ 

＃初始化温度值

192 $\text {t_{min}}=100$  设置温度下限

193# $\text {alpha}=0.99$  ＃设置温度下降率

194 $k=10000$ 

＃设置迭代次数

195＃todo：给定一个初始解，

100 ans $\text {list}=[0.5$  $0.2$ $0.1,0.1,0.1,0.1]$ 

107 ans $w=0$ 

195 $\text {ans_{all}=}[]$ 

190＃todo：开始退火过程

200#while $(\mathrm {t}>\mathrm {t}\_\mathrm {min}):$ 

201 for i in range(50):

202

for i in range(k):

203

$$ans\_w=get\_w(ans\_list)$$

204

ans $list\_new=get\_new\_ans\_list(ans\_list$ $,t)$ 

205

if $is\_ans\_$ list(anslist $\_new)$ 

206

#print $("ok")$ 

207

ans $w\_new$ $=get\_w(ans\_list\_new)$ 

208

$$\text {delta}=\text {ans_{w}_{new}}[0]-\text {ans_{w}}[0]$$

200

if $\text {delta}>0:$ 

210

$$ans\_list=ans\_list\_new$$

211

#else:

212

#

$$p=get\_p(delta,t)$$

213

#

# $print(p)$ 

214

#

if $(p<rar$ ndom.random()):

215

#

$\text {ans_{list}}=\text {ans_{list}_{}}$ new

216 # $t=t=alpha$ 

217

t $-=0.2$ 

218

print(f”得到的净利润：{answ[0]｝，环境成本：{answ[1]}，信用成本：{answ[2]｝”）

210

print(f”最优解为： $\{ans\_list[0]\},$ {anslist[1]},{anslist[2]},{anslist[3]},{anslist

$$[4]\},{ans\_list[5]}")$$

220

＃print(f”最优解为： {anslist[0]},{anslist[1]},{anslist[2]},{anslist[3]}")

221

$$ans\_all.append(ans\_w[0])$$

print(f"最终得到的净利润： $\{ans\_w[0]\}$ ，环境成本：{answ[1]｝，信用成本： $\{ans\_w[2]\}")$ 

223

224

225 iteration $=list(range(1,len(ans\_all)+1))$ 

200 plt.figure()

227 plt.plot(iteration, $ans\_al$ , $marker=''$ , $color='b'$ $,linestyle='-')$ 

228 plt.xlabel(＇迭代次数＇）

plt.ylabel（“净利润＇）

230 plt.title(＇模拟退火优化可视图＇）

231 plt.grid(True)

232 plt.show()

23.3

中国大学生在线

234import numpy as np

235import pandas as pd

dxs.moe.gov.cn

230import random

<!-- 36 -->

