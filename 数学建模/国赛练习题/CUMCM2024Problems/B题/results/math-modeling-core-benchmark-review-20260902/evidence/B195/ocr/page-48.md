336

#

break

337

if $\text {count}>20:$ 

33.5

break

330

＃todo：成品次品拆成半成品

340

nhalfproduct1new1,nhalfproduct2newl,nhalfproduct3new1,

phalfproductlnewl,phalfproduct2newl,phalfproduct3new $1=$ 

341

dealproductbad3(nproductbad * pproductdismantle,

242

[phalfproductlmakenew,phalfproduct2makenew,

$p\_half\_$ product3makenew]

343

pproductmake)

344

＃todo：计算拆解费

345

4 $\_1\_new$ =nhalfproduct1newl * mproductdismantle

346

＃#todo：处理半成品次品（前方造留半成品有检测不合格和多余，此处检测不合格应当不进行检测，数目多余与拆除之后的进行检测进行检测）

347

＃todo：得到当前未检验半成品数目，（多余与拆除之后）

343

if $n\_half\_product1\_new1+n\_half\_product1\_ex=0:$ 

340

$$p\_half\_product1\_new1=0$$

360

$$n\_half\_product1\_new1=0$$

351

else:

352

phalfproduct1new $1=(n\_half\_$ product1new1. $p\_half\_$ roduct1new1x

$n\_half\_product1\_ex*p\_half\_product1\_ex)$ $/$ $(n\_half\_$ productlnew $1+$ halfproduct1ex 一

363

354

nhalfproductlnew $1=n\_half$ product1newl $+n\_$ halfproduct1ex if nhalfproduct2new1 $+n\_half\_product2\_ex=0:$ 

35.5

$$p\_half\_product2\_new1=0$$

356

nhalfproduct2new $1=0$ 

367

else:

35.5

phalIfproduct2newl=(nhalfproduct2newl *phalfproduct2new1+

$n\_haf\_product2\_ex*p\_haf\_product2\_ex)/$ $(n\_half\_$ $product2\_new1+n\_$ $half$ product2ex )

350

360

$n\_half\_product2\_new1=n\_half\_$ product2new1 $+n\_half\_product2\_ex$ if $n\_half\_product3\_new1+n\_half\_product3\_ex=0:$ 

361

$$p\_half\_product3\_new1=0$$

301

$$n\_half\_product3\_new1=0$$

363

else:

364

phalfproduct3new $1=(n\_half\_product3\_newl*p\_half$ product3newl+

$n\_half\_product3\_ex*p\_half\_product3\_ex)$ $/$ $(n\_half\_$ $product3\_new1+n\_$ $\_half\_$ product3ex

365

nhalfproduct3new $=n\_half\_$ $product3\_new1+n\_half\_$ roduct3ex

366

＃todo：半成品拆成零件（仅拆前方留下半成品次品）

367

npartlnewl, $n\_part2\_$ new1,npart3new1, ppartlnewl,ppart2new1, $p\_part3\_$ new $1=$ 

368

dealproductbad3(nhalfproduct1ex2*phalfproduct1dismantle,

300

[ppart1make,ppart1make,ppartlmake],

$p\_half\_$ roduct1make)

370

npart4newl,npart5newl,npart6newl,ppart4newl,ppart5newl, ppart6new $1=1$ 

371

dealproductbad3(nhalfproduct2ex2 * phalfproduct2dismantle

372

phalfproduct2make)

373

$n\_part7\_new1,$ npart8new1,、ppart7new1,ppart8new1-

$cn$ [ppart4make,ppart5make,ppart6make], dxs.moe.gov

<!-- 48 -->

