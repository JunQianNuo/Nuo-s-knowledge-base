178 $P\_part4\_swap=0$ 

179

$$\text {p_{part}5_{swap}=0}$$

180

$$\text {P_{part}6_{swap}=0}$$

181

$$\text {p_{part}7_{swap}=}0$$

182

$$\text {p_{part}8_{swap}=}0$$

183

$$p\_half\_product1\_swap=0$$

184

$$p\_half\_product2\_swap=0$$

185

$$p\_half\_product3\_swap=0$$

186

＃todo：开始循环

187

$$\text {ans_{list}}=[]$$

188

$$\text {count}=0$$

189

while True:

190

＃todo：继承循环

191

$$\text {w_{1}_{new}=w_{1}}$$

192

count $+=1$ 

193

＃print(f”当前是第｛count｝次循环”）

194

＃todo：零件检测

195

if count $=$ $1.$ 

196

＃todo：计算零件成本

197

$w\_1$ new $-=n\_part1\_ori*m\_part1\_buy+n\_part2\_ori*m\_part2\_buy$ 

198

$$w\_1\_new\quad -=n\_part3\_ori*m\_part3\_buy+n\_part4\_ori*m\_part4\_buy$$

199

$$w\_1\_new-=n\_part5\_ori*m\_part5\_buy+n\_part6\_ori*m\_part6\_buy$$

200

$w\_1\_new$ $-=n\_part7\_ori*m\_part7\_buy+n\_part8\_ori*m\_part8\_buy$ 

201

#print $(w\_1\_new)$ 

202

＃todo：零件进行检测，更新数据

203

npartlnew, $p\_part1\_make\_$ $\_new$  $n\_partl\_test=get\_new\_part(n\_part1\_ori$ 

ppartlmake, $p\_part1\_test)$ 

204

npart2new,ppart2makenew, $n\_part2\_test=get\_new\_part(n\_part2\_ori$ $p\_part2\_make$ , $p\_part2\_test)$ 

205

$n\_part3\_new,p\_part3\_make\_new,$ $n\_part3\_test=get\_new\_part(n\_part3\_ori,$ $p\_part3\_make$ ,ppart3test)

206 npart4new,ppart4makenew, . $n\_part4\_test=get\_new\_part(n\_part4\_ori$ $p\_part4$ make, $p\_part4\_test)$ 

207

npart5new, $p\_part5\_make\_$ new, $n\_part5\_test=get\_new\_part(n\_part5\_ori$ ppart5make,ppart5test)

208

npart6new,ppart6makenew, $n\_part6\_test=get\_new\_part(n\_part6\_ori$ ppart6make,ppart6test)

200 npart7new, $p\_part7\_make\_new$  $\text {n_part7_test}=\text {get_new_part}(\text {n_part}7\text {_ori}$ $p\_part7\_make$ ,ppart7test)

210

npart8new,ppart8makenew, $n\_part8\_test=get\_new\_part(n\_part8\_ori$ $p\_part8$ make,F $p\_part8\_test)$ 

211

nhalfproduct1new,phalfproduct1new $=0$ ,0

212

nhalfproduct2new,phalfproduct2new=0,0

213

$n\_half\_product3\_new$ ,phalfproduct3new=0,0

214

＃todo：计算检测费

215

w1new $-$ npartltest* $m\_part1\_test+n\_part2\_test*m\_part2\_tes$ 

216

w1new $-=n\_part3\_test*m\_part3\_test+n\_part4\_test*m\_part4\_test$ 

217

w1new $一$ $n\_part5\_test*m\_part5\_test+n\_part6\_test*$ $m\_part6\_test$ 

$$cn$$

218

210

#print(w1new)

else:

w1new $-=n\_part7\_test*m\_part7\_test+n\_part8\_test$  $m\_part8$ $oester$ 

220

<!-- 44 -->

