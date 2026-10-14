165 ＃定义联合密度函数

166·jointdensity&lt;-function(p, alphal,betal,alpha2,beta2,alpha3,beta3){

167

168

p1&lt;-p[1]

p2&lt;-p[2]

169

p3 $<-p$ 

170

171 return(betadensity(pl,alphal,betal)*

172

betadensity(p2,alpha2,beta2)

173

betadensity(p3,alpha3,beta3))

174-)

175

176定义被积函数，考虑联合密度

177-integrand&lt;-function(p,func, alphal,betal,alpha2,beta2,alpha3,beta3,param)(

178

return(func(p,param) *jointdensity(p, alphal,betal,alpha2,beta2,alpha3,beta3))

179-)

180

181 ＃设置积分范围：每个变量的范围是［0,1］182 lowerlimit $\therefore$  $c(0,0,0)$ 183 upperlimit $<-$ c(1,1,1)

184

185 ＃定义参数组

186 paramslist $<-$ list(

187

$$1ist(n=100,\quad a=0.1,\quad b=4,\quad c=2\quad d=0.1,\quad e=18,\quad f=3,g=0.1,h=6,$$

188

189

$$i=3,j\quad i=\quad 56,k=6,\quad 1=5)$$

$$list(n=\quad 100,\quad a=0.2,\quad b=4,c=2,\quad d=0.2,\quad e=18,\quad f=3,g=0.2,h=6,$$

190

191

$$i=3,j=\quad 56,k=6,\quad 1=5)$$

192

$$list(n=\quad 100,a=0.1,b=4,\quad =100,\quad c=2,d=0.1,e=18,\quad f=3,g=0.1,h=6,$$

$$i=3,j=56,k=30,1=5)$$

193 $list(n=$ $-3$ $100,a=0.2,b=4,c=1,d=0.2,e=18,$ $f=1,g=0.2,h=6,$ 

194

$$i=2,j=56,k=30,1=5),$$

195 $1ist(n=1$ $00$  $-0.1$  $=$ $a=0.1,b=4,c=8,$  $d=0.2,e=18,$ $f=1,g=0.1,h=6,$ 

196

197

$$i=2,j=56,k=10,1=5),$$

198

$$1ist(n=1\quad 100\quad 100,a=0.05,b=4,c=2\quad d=0.05,e=18,f=3,g=0.05,h=6,$$

199 )

$$i=\quad 3,j=56,\quad k=10,\quad 1=40)$$

201 ＃函数列表

202 functions&lt;-list(jjjc,jjbc,jjjb,jjbb,jbjb,jbbb,bjjb,bjbb, bbjb,bbbb,

203

bjjc,jbjc,bbjc,bjbc,jbbc,bbbc)

204

205 ＃初始化结果矩阵

206 resultsmatrix $<-$ $matrix(0$  $\text {nrow=16,ncol=6)}$ 

207 ＃计算每组参数下的积分

208-for(col in 1:6){

209

210

params $<-$  paramslist[[co1]]

211 ＃计算 Beta 分布参数

212 alpha1 $<-1+prmsSn$ paramsSa

213 betal $<-1+paramsn-paramsn$  paramsSa

214 alpha2 $<-1+paramsSn$ 

215 beta2 $<-1+paramsSn-paramsSn$ params&#36;d

216 $alpha3<-1+$ paramsSn*paramssg

217 beta3 $<-1+paramsn-params$  paramssd

218 ＃计算每个函数的积分

219

for (row in 1:16) $\{$ 

220

func $<-$ functions[[row]]

221

$result<-$ adaptIntegrate(function(p) integrand(p, func, alphal,betal,

222

alpha2,beta2,alpha3,beta3,param5),

223

lowerLimit=lowerlimit,upperLimit=upperlimit)

224

resultsmatrix[row,col] $<-$ resultSintegral

225 }

226)

227 ＃输出结果矩阵

228 $print(results$ matrix)

229 ＃安装并加载necessary packages

230 library(openx1sx)

231 ＃定义 Excel 文件路径

232 filepath $<-$ "resultsmatrix.xlsx"

233 ＃创建 个工作簿

234 wb $<-$ createworkbook()

235 ＃添加一个工作表

236 addworksheet(wb,"Results")

237 ＃写入矩阵到工作表

238 writeData(wb,"Results",resultsmatrix)

中国大学生在线

dxs.moe.gov.cn

<!-- 33 -->

