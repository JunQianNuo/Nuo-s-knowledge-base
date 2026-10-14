**附录**

<table border="1" ><tr>
<td>附录1</td>
</tr><tr>
<td>介绍：蒙特卡洛模拟函数的相关python 代码</td>
</tr><tr>
<td>＃蒙特卡罗模拟函数<br>def montecarlosimulation(result):<br>$\cos t=0$ $money=0$ $L=[[]for_$in range(8)]<br>$H=[[]for_i$in range(3)]<br>$H_L=[[]$forin range(3)]<br>for j in range(8):<br>$L[j]=[0$if random.random()&lt;M1[j,0] else 1 forin range(number)]<br>L[i],$\text {cost}=\text {test}(\mathrm {j},\mathrm {\;L},$cost,result)<br>＃半成品组装<br>$\text {cost,}\mathrm {H}[0]=\text {assemble}$product([L[0],L[1],L[2]],H[0],HL[0],0,cost,result)<br>cost $H[1]=\text {assemble_{product}}([L[3],L[4],$,L[5]],H[1],HL[1],1,cost,result)<br>$cost,H[2]=assemble_$product([L[6],L[7]],H[2],HL[2],2,cost,result)<br>＃成品组装<br>while $\text {len}(\mathrm {H}[0])>0$ $\text {andln}(\mathrm {H}[1])>$ $andlen(H[2])>0:$ $index0=random.randint(0,len(H[0])-1)$ $\text {index}1=\text {random.randint}(0,\text {len}(\mathrm {H}[1])-1)$ $\text {index2=random.randint}(0,\text {len}(\mathrm {H}[2])-1)$ $\text {index}=[\text {index}0,\text {index}1,\text {index}2]$sum $\text {result}=\mathrm {H}[0][\text {index}0]+\mathrm {H}[1][\text {index}1]+\mathrm {H}[2][\text {index}2]$cost $+=\mathrm {M}3[1]$ $\text {success}=0$if random.random()&lt;M3[0] else 1<br>if result[11]:＃成品检测<br>$\cos t+=M2[2]$ $ifsum_result<3ornotsuccess:$ $cost=destroy2(cost,$,result,index,H,HL,L)<br>continue<br>if sum $result<3$or not success:<br>$\cos t+=\log s$ $\text {cost}=\text {destroy2(cost,}$, result,index,H,HL,L)<br>else:</td>
</tr></table>

<!-- 25 -->

