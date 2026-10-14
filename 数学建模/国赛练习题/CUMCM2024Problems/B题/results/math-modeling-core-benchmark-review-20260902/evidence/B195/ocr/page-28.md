<table border="1" ><tr>
<td>274<br>275<br>276<br>27<br>278<br>279<br>280<br>201<br>282<br>283<br>284<br>285<br>286<br>280<br>200<br>201<br>292<br>293<br>204<br>295<br>298<br>301<br>302</td>
<td>#np.random.shuffle(dataget)<br>＃#print(f”生成数据： $\{data_get\}")$＃样本生成（正态分布，较大的90 ％为正品，其余为次品）<br>$\text {data_{get}}=\mathrm {np}$.random.normal( $1oc=0$, $scale=1$ $size=data_num)$＃均值为0 ，标准差为1<br>threshold $du=$.percentile(dataget $cipin_lv*100)$ $data_get|data_get$ $>=\text {threshold}]=1$data $_get[data_ge$ $!=1]=0$＃print(f”生成数据：{dataget｝”）<br>＃样本保存<br>$df=pd.DataFrame(data_get$ ,<br>$\text {columns=[}$＇样本（0 为次品，1 为合格）'1 ）<br>$f1='第一间/问题一数据.xlsx$＇<br>d $f.to_excel(f1$1<br>$index=False$e)<br>print ( f ”样本已成功生成并保存到｛f1 ｝文件中。”）<br>$no_num=int((data_get=0).sum())$all $num=len(data_get)$print(f＂次品个数：{nonum}，整体数目：$\{all_num\}")$＃todo ：尝试不同的抽样方法<br>＃简单随机抽样，整群抽样，二重抽样<br>＃载入数据并建检验数据<br>$df=pd.read_excel($ 第一问／问题一数据，xlsx ',  $sheet_name='Sheet1')$）<br>data $\text {get}=\text {df}[$＇样本（0 为次品，1 为合格）］<br>print(f”首先进行数据检验，此批产品中合格率为：{np.sum(dataget)/len(dataget)}"）<br>print ( f ”此批产品中次品率为： $\{(1-np.\}$sum(dataget)/len(dataget))·100}%”)</td>
</tr><tr>
<td rowspan="2">303<br>304<br>305<br>306<br>307<br>308<br>309<br>310<br>311<br>312<br>313<br>314<br>315<br>316<br>317<br>318<br>319<br>320<br>321<br>322<br>323</td>
<td>＃todo ：简单随机抽样<br>＃确定抽样比例<br>$\text {data_{get}=df[}$样本（0 为次品，1 为合格）］<br>nonum $=\text {int}((\text {data_{get}}=0).\text {sum}())$ $all_num=len(data_get)$sample $\text {num}=\text {all_{num}}*0.1$＃进行抽样<br>randomindices = random.sample(range(allnum),int(samplenum))<br># print(randomindices)<br>$\text {sample}=[\text {data_{get}}[i]$ for i in randomindices]<br>print（”随机抽样的样本为：”，sample）<br>ztestfunc(sample)</td>
</tr><tr>
<td>＃todo：整群抽样<br>＃依据排序进行分组，10 个位一组<br>$\text {data_{get}}=\text {df}[$样本（0 为次品，1 为合格）'］<br>$all_num=len(data_get)$ $\text {data_{get}}=[[\text {data_{get}}[\underline {}+\underline {}*10]$ for $-$inrange(10)]forinrange(int(allnum<br>-<br>＃创建划分好的产品群体<br>$all_num=len(data_get)$dxs.moe.gov.crto)) $\text {sample_{num}=all_{num}*}0.1$</td>
</tr></table>

<!-- 28 -->

