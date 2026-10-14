205

ans $w\_new=get\_w(ans\_list\_new)$ 

206

$$\text {delta}=\text {ans_{w}_{new}[0]-ans_{w}[0]}$$

207

if $\text {delta}>0$ 

208

$$ans\_list=ans\_list\_new$$

200

else:

210

$$p=get\_p(delta,t)$$

211

# $print(p)$ 

212

if $(p<random.random())$ :

213

$$ans\_list=ans\_list\_new$$

214

$$\mathrm {t}-=0.2$$

216

print(f＂得到的净利润：{answ[0]}，环境成本：{answ[1]}，信用成本：{answ[2]｝”）

216

print(f”最优解为： {anslist[0]},{anslist[1]},{anslist[2]},{anslist[3]},{anslist $[4]\},{ans\_list[5]}")$ 

217

＃print(f”最优解为： $\{ans\_list[0]\}$  anslist[1]},{anslist[2]},{anslist[3]}")

218

$$ans\_all.append(ans\_w[0])$$

219print(f"最终得到的净利润： $\{ans\_w[0]\}$ ，环境成本： $\{ans\_w[1]\}$ ，信用成本： $\{ans\_w[2]\}")$ 

220

221

222#iteratio $n=list(range(1$ $,len(ans\_all)+1))$ 

223#plt.figure()

224#plt.plot(iteration, $ans\_all$  marke $ker="$  col $lor='b$ $',linestyle='-')$ 

225＃plt.xlabel(＇迭代次数＇）

226＃plt.ylabel(＇净利润＇）

227 ＃plt.title(＇模拟退火优化可视图）

228#plt.grid(True)

220#plt,show()

230

231＃我们抽样得到的次品率10.0％

232＃可能的真实次品率均值：0.09998004390341249

213＃可能的真实次品率置信区间：[0.09418352 0.10592778］

234＃我们抽样得到的次品率5.0％

235＃可能的真实次品率均值：0.05008980243464378

236＃可能的真实次品率置信区间：[0.04590519 0.05444447］

237＃我们抽样得到的次品率20.0％

238可能的真实次品率均值：0.19976052684094991

230＃可能的真实次品率置信区间：[0.19199026 0.20764429］

240

241＃情况一：

242＃偏小扰动：[1,0,0,1,0,1］

243＃偏大扰动：[1,0,0,1,0,1］

244

245import matplotlib.pyplot as plt

246import numpy as np

247fromitertools import product

248

240 plt.rcParams['font.sans-serif' $]=$ 'KaiTi']

250plt.rcParams['axes.unicodeminus $']=Fals$ 

261

中国大学生在线

262

26.3def $get\_ans(x\_list)$ 

dxs.moe.gov.cn

254

＃ todo：过程函数

<!-- 57 -->

