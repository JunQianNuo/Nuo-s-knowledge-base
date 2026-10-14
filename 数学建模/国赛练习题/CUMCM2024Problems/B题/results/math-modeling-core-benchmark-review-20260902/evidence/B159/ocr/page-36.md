114 ＃定义目标函数 hfunc(p1,p2,p3）

115-hfunc $<$ function(p){

116 p1 $<-$ $p[$ 

117 $\mathrm {p}2<-\mathrm {p}[2$ 

118 $p3<-p[3]$ 

119

120 result $\leftarrow j-(b+c)/(1-p1)-(e+f)/(1-p2)-h/(1-p3)$ 

121 $(k+1)=p3$ $/(1-p3)$ 

122 return(result)

123-)

124

125 定义联合密度函数

126-jointdensity $<-$ function(p,alphal,betal,alpha2,beta2,alpha3,beta3){

127 p1 $<-p[1]$ 128 p2 $<-p[$  $2$ 

129 $p3<-$ $p[$ 3]

130

131 return(betadensity(pl,alphal,betal)*

132

betadensity(p2,alpha2,beta2)*

133

betadensity(p3,alpha3,beta3))

134-)

135

136 ■定义被积函数，考虑联合密度

137-integrand $<-$ function(p,alphal,betal, alpha2,beta2,alpha3,beta3){

138 return(hfunc(p)*jointdensity(p,alphal,betal, alpha2, beta2,alpha3,beta3))

139-)

140

141 设置积分范围：每个变量的范围是［0,1］

142 lowerlimit $<-$ c(0,0,0)

143 upperlimit $<-c(1,1,1)$ 

144

145 ＃初始化结采向量和 betao 向量146 results $2$  numeric(10)

147 beta0values $<-$ 1:10

149 ＃计算每个 betao对应的期望值

150-for(beta0 in beta0values)(

151

$alphal$ $\leftarrow alphao$ $+n$ $\star$  ,

152 betal $<-beta0$ $+n-n$ 

153

154 $alpha2$ $<-alpha0$ $+n=d$ 

155 $beta2$ $<-beta0+n-n$ 

156

158

157 $alpha3$ $<-alpha0$ $+n^{+}$  $0$ $beta3$  $-0$ $<-beta0+n-n$ 

159

160

$result<-$ adaptIntegrate(function(p) integrand(p,alphal,betal,alpha2,beta2,

161

hlpha3,beta3),

162

lowerLimit= lowerlimit,upperLimit= upperlimit)

163

164

165-}

results[beta0] $<-$ resultSintegral

166

167 ＃输出结果

168 cat(＂期望值向量：",results，” $"(n")$ 

169

170 ＃将结果绘制成散点图

171 plot(beta0values,results,

172

type $="p"$ 

173

$$xlab="beta"$$

174

175

$$ylab="期望值"$$

176

$ylim=c(0,$ 20))

177 ＃进行线性拟合

178 fit $<-$ 1m(results~beta0values)

179

180 ＃添加线性拟合线

181 abline(fit, $,col=$  red

182

183 ＃输出线性拟合结果

184 cat（“线性拟合结果：\n”）

185 print(summary(fit))

中国大学生在线dxs.moe.gov.cn

<!-- 36 -->

