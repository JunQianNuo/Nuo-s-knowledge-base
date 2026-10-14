237import matplotlib.pyplot as plt

23.8import numpy as np

239

240plt.rcParams['font.sans-serif' $']=['KaiTi']$ 

241plt.rcParams['axes.unicodeminus $\vert =False$ 

242

243

244＃todo：过程函数

245 def $get\_new\_part(n\_part\_ori,$  $p\_part\_make,$ $p\_part\_test):$ 

146

＃零件检测函数，输入零件数、次品率、检测率，得到新零件数、新次品率、检测数

247

$$n\_part\_good=n\_part\_ori*(1-p\_part\_make)$$

248 $n\_part\_bad=n\_part\_ori*p\_part\_make$ 

240

$$n\_part\_bad\_test=n\_part\_bad*p\_part\_test$$

250

$$n\_part\_new=n\_part\_ori-n\_part\_bad\_test$$

251

$p\_part\_new=1-n\_part\_good$ $/$ $n\_part\_$ new

262

return $n\_part\_new$ , $p\_part\_new$  $n\_part\_ori*p\_part\_test$ 

253

264

255def getproduct(nparts, pparts,pproductmake):

256

＃输入每种零件的个数，得到产品生产数、次品数、正品数

267

$$p\_good=1-p\_product\_make$$

268

for enum in $p\_parts:$ 

259

$p\_good$ $*=1-\text {enum}$ 

200

nparts=np.array $(n\_parts)$ 

261

nproduct $=$ $np$ .min(nparts)

262

nproductgood $=$ $\_product*p\_good$ 

263

nproductbad $=n$ product-nproductgood

264

returnnproduct,nproductgood,nproductbad

265

200

# 267 $defdeal\_product\_bad2(n\_product\_bad,$ $p\_parts):$ 

268

＃输入次品数、每个零件的次品率，得到每种新的零件个数，每种新的零件的次品率（一个成品由两个零件构成）

200

$$\text {n_{part}_{1}=n_{product}_{bad}}$$

270

$$\text {n_{part}_{2}=n_{product}_{bad}}$$

271

$$p\_swap=p\_parts[0]+p\_parts[1]-p\_parts[0]*p\_parts[1]+(1-p\_parts[0])*(1-$$

$$p\_parts[1])*p\_product\_make$$

272

$$p\_part\_1=p\_parts[0]/p\_swap$$

273

$$\text {p_{part}_{2}=p_{parts}[1]/}\quad p\_swap$$

274

return $n\_part\_1$ , $n\_part\_2,$ $p\_part\_1,p\_part\_2$ 

275

276

277＃循环仿真直至不能盈利

278＃此处使用法一（全程固定）进行循环处理

279 print（”此处使用法一（全程固定）进行循环处理”）

280＃todo：决策变量

281＃总盈利值、丢弃成本，调换成本

282 $\text {w_{1}=}0$ 

在线中国大学生 $cn$ 

283 $\text {w_{2}=}0$ 

284 $\text {w_{3}=}0$ 

dxs.moe.gov.

285# todo: 决策方案变量

<!-- 37 -->

