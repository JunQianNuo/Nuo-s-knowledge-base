传入一维列表，表示样本

224 :param dataget:

225

:return:

226

350.10

227

＃ todo：对抽样数据进行检验 检验

228 $data\_get=np.array(data\_get$ $,dtype="int32")$ 

229

＃进行z检验

230

wanna $p0=0.1$ 

231

$$no\_num=int((data\_get=0).sum())$$

233

all $\_num=len(data\_get)$ 

233

print(f”次品个数：{nonum}，整体数目： $\{all\_num\}")$ 

234

235

＃检验一

236

print(＂检验一”）

237

＃'smaller＇代表低于alpha时成立，

238

$$z\_stat,$$

$p\_val=proportion$ sztest(nonum,allnum, $wanna\_p0$ , $alternative='smaller'$ ')

230

print(f"Zstatistic: $\{z\_stat\},P-value:\{p\_val\}")$ 

240

241

＃判断原假设

242

$$\text {alpha}=0.10$$

243

if $p\_val<alpha:$ 

244

print（”拒绝零假设：即认为有90％的把握认为次品率低于10％”）

245

else:

246

print（”接受零假设：即认为没有90％的把握认为次品率低于10％”）

247

248

＃检验二

249

print（”检验二”）

250 ＃'larger＇代表高于alpha时成立，

251

$$z\_stat,$$

,allnum, $wanna\_p0$ , $alternative='larger')$ 

$$p\_val=proportions\_ztest(no\_num$$

263

print(f"Z statistic: $\{z\_stat\},$ $P-value:\{p\_val\}")$ 

253

254

＃判断原假设

265

$$\text {alpha}=0.05$$

256

if $p\_val<alpha:$ 

257

print(＂拒绝零假设：即认为有95％的把握认为次品率大于10％”）

268

else:

250

print（”接受零假设：即认为没有95％的把握认为次品率大于10％”）

260

261

262 np.random.seed(12845425)

263random.seed(10524)＃设置随机数种子，以确保结果可重复

264

265＃todo：生成合理的样本

200＃样本总数确定

267 $\text {data_{num}}=100000$ 

263 $\text {cipin_{lv}=}0.11$ 

生在线

260

270＃＃样本生成（应当是二项分布）

271#data $0$ $\_num=int(data\_num*cipin\_lv)$ 

moe.gov.cn

272# $data\_1\_$ $\_num=int(data\_$ $\_num-data\_0\_$ num)

273# $data\_get=np.concatenate((np.$ ,zeros(data0num), $np.ones(data\_1\_num)))$ 0

<!-- 27 -->

