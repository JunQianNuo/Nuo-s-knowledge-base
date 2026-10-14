172##

＃n最小

173##

if $c\_>0:$ 

174##

if $\text {delta}<0:$ 

175##

$$p1,alpha=p1\_,alpha\_$$

176##

$$else:$$

177##

$$p=get\_p(delta,t)$$

178##

$$if(p>random.random()):$$

179

$p1,alpha=p1\_,$ $alpha\_$ 

180##

181##

print(f"当前最优解为： $p1=\{p1\},alpha=\{alpha\}")$ 

182##

print(f”此时n为：{n},c为： $\{c\}")$ 

183## # $t=t*$ $alpha$  ＃温度下降

184##

$$\mathrm {t}\rightarrow 0.01$$

185##

186## $n,$  $c=get\_ans(p1,alpha)$ 

187##print(f"最优解为： $p1=\{p1\}$ $,alpha=\{alpha\}")$ 

188##print(f”此时n为： ｛n},c为： $\{c\}")$ 

189＃问题一

190import scipy.statsasstats

191

192 $p=0.1$ 

103 $n\_values=range$ $(10$ ,101)

194 valid $\text {n_{values}=[]}$ 

195 for n in $n\_values:$ 

196

binom $\_dist=stats.binom(n,p)$ 

197

$$c0=binom\_dist.ppf(0.95)$$

198 $P\_X\_leq\_c0=binom\_dist.cdf(c0)$ 

190

diff $=(P\_X\_leq\_c0-0.95)/$ $0.95$ 

200

if $\text {diff}<0.01:$ 

201

$$valid\_n\_values.append([n,c0])$$

202 print(f”符合条件的所有n为：{valid $\_n\_values)")$ 

203

204 ＃问题二

205valid $\text {n_{values}}=[]$ 

206 for n in $n\_values:$ 

207

$$binom\_dist=stats.binom(n,p)$$

208

$$c0=binom\_dist.ppf(0.1)-1$$

209

$$P\_X\_leq\_c0=binom\_dist.cdf(c0)$$

210 #print $(P\_X\_leq\_co)$ 

211

$$\text {diff}=(0.1-\text {P_{X}_{leq}_{c}0)/0.1}$$

212

if $\text {diff}<0.01:$ 

213

validnvalues.append([n,c0])

214print(f”符合条件的所有n为： $\{valid\_n\_values\}")$ 

215import numpy as np

216import pandas as pd

217import random

218from statsmodels.stats.proportion import proportionsztest

210

中国大学生在线

220

221def

dxs.moe.gov.cn

222

$$ztest\_func(data\_get):$$

<!-- 26 -->

