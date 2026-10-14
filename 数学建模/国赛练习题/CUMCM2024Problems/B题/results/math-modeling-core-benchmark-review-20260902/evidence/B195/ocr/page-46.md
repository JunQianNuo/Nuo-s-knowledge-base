265

$p\_part8\_ex=p\_part8\_make\_$ new

206

＃todo：得到当前半成品数，得到当前半成品次品率

267

phalfproduct1mak $ke\_new=(n\_half\_productl\_bad+n\_half$ productlnew* phalfproduct1new)/(

268

nhalfproduct1 $+n\_half\_$ product1new)

200

nhalfproduct1new $=n\_half\_product1+n\_half\_product1\_ne$ 

270

$p\_half\_$ product2makenew $=(n\_half\_product2\_bad+n\_half$ product2new* phalfproduct2new)/(

271

$n\_half\_product2+n\_half\_$ roduct2new)

272

nhalfproduct2new $=$ halfproduct2+nhalfproduct2new

273

$p\_half\_product3\_make\_new=(n\_half\_product3\_bad+n\_half\_product3\_new$ *phalfproduct3new)/(

274

nhalfproduct3 $+n\_half\_product3$ new)

275

nhalfproduct3new $=\mathrm {n}$ halfproduct3 $+n$ halfproduct3new

276

277

# print $(f"\{n\}$ halfproductlnew},{nhalfproduct2new},{nhalfproduct3new}") if count $=1:$ 

278

＃todo：保留半成品次品

279

$n\_half\_product1\_ex2=p\_half\_product1\_make\_new*n\_half\_product1\_new*$ phalfproduct1test

280

$n\_half\_product2\_ex2=p\_half\_product2\_make\_new*$ nhalfproduct2new* phalfproduct2test

281

$n\_half\_product3\_ex2=p\_half\_$ product3makenew * nhalfproduct3new* phalfproduct3test

282

＃todo：检测半成品

28.3

nhalfproduct1new,phalfproduct1makenew, nhalfproductltest= getnewpart(nhalfproduct1new,

284

phalfproduct1makenew,

285

phalfproductltest)

286

nhalfproduct2new,phalfproduct2makenew,nhalfproduct2test=

getnewpart(nhalfproduct2new,

207

phalfproduct2makenew,

288

$$p\_half\_product2\_test)$$

280 nhalfproduct3new,phalfproduct3makenew,nhalfproduct3test= getnewpart(nhalfproduct3new,

200

$$p\_half\_product3\_make\_new,$$

291

$$p\_half\_product3\_test)$$

292

else:

293

＃todo：保留半成品次品

294

$n\_half\_product1\_ex2=p\_half\_$ $\_product1\_$ makenew*nhalfproductlnew

$$p\_half\_product1\_test0$$

295

$n\_half\_product2\_ex2=p\_half\_product2\_$ makenew * nhalfproduct2new

$$p\_half\_product2\_test0$$

296

$n\_half\_product3\_ex2=p\_half\_product3\_make$ new $*$  $n\_half$ product3 $oe$ 

v.cn

$$p\_half\_product3\_test0$$

207

＃todo：检测半成品

<!-- 46 -->

