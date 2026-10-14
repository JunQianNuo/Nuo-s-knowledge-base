375# print(randomindices)

376 $sample=[data\_get[i]$  for i in randomindices]

377 print（”随机抽样的样本为：”，sample）

378

379

380＃todo：整群抽样

381＃依据排序进行分组，10个位一组

382 $\text {data_{get}=df[}$ 样本（0为次品，1为合格）］

383 $all\_num=len(data\_get)$ 

384 $\text {data_{get}}=[[\text {data_{get}}[\underline {}+\underline {}*10]$  for $\_in$  range(10)] forinrange(int(allnum/10))

]

385＃创建划分好的产品群体

386 $all\_num=len(data\_get)$ 

387 $\text {sample_{num}=all_{num}*}0.1$ 

383 $sample\_indices=random.sample(range(all\_num)$ ,int(samplenum))

380

300＃抽取整个群的产品作为样本

391 $\text {sample}=[]$ 

392 for indices in sampleindices:

393

$sample$ $+=data\_get[indices]$ 

394

395 ＃打印抽样结果

290 print（”整群抽样的样本为：“，sample）

897

398＃todo：二重抽样

300 ＃第一阶段抽样

400 $\text {data_{get}=df[}$ 样本（0为次品，1为合格）'1

401 $all\_num=len(data\_get)$ 

samplenum $=\text {all_{num}}*0.5$ 

randomindices = random.sample(range(allnum),int(samplenum))

404 $\text {data_{get}=[data_{get}[i]}$  for i in randomindices]

405 print（”一重抽样的样本为：” $,data\_get)$ 

406 ＃第二阶段抽样

407 data $get=np.array(data\_get)$ 

408 $all\_num=len(data\_get)$ 

409sample $\_nu$ $=\text {all_{num}}*0.2$ 

410randomindices= random.sample(range(allnum),int(samplenum))

411 $\text {sample}=[\text {data_{get}}[i]$  for i in randomindices]

412 print（”二重抽样的最终样本为：”，sample）

413

414

415

416

417

418

410

420##

421# data $\text {get}=\mathrm {np}$ $.array(sample)$ 

中国大学生在线

422＃＃进行z检验

423#wanna $p0=0.1$ 

dxs.moe.gov.cn

424# $\text {no_{num}=int}((\text {data_{get}}=0).sum())$ 

<!-- 30 -->

