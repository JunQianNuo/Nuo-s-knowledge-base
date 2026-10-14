734

$p\_half\_product3\_swap=p\_half\_$ product3new1

735

W $1=w\_1\_new$ 

736

#print(f”最终得到的净利润： $\{w\_1\_new\}")$ 

＃print(f”总循环数：{count}"）

738 # $print(ans\_list)$ 

730 *if len( $(ans\_list)=1$ 

740

#

return anslist[0]

741

#if $ans\_list[-2]>ans\_list[-1]:$ 

742

#returnans $\_list[-2]$ 

743

# $returnans\_list[-1]$ 

744

return $ans\_list$ 

745

746＃＃寻找策略

747## print $:(get\_ans([1,1,1,1,1,1,1,1,1,1,0,0,0,0,1]))$ 

748##print $([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1])$ 

749 ##print $(get\_ans([1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1]))$ 

750#ansmay $be\_list=list$ (product([0,1], $repeat=16))$ 

761# ans $list=[]$ 

75.2#count $=0$ 

753#for maybelist in $ans\_maybe\_lis:$ 

754#

count $+=1$ 

765 # print(count)

756#

$ans\_$ list.append([rmaybelist,getans(maybelist)])

##print(sorted(anslist,key=lambda x: $x[1]))$ 

758 * ans $\_list=$ enum for enum in anslist if enum[1]&gt;0]

750* ans $\_list=$  sorted(ans $\_lis$  key=lambdax: $x[1])$ 

760#for enum in $ans\_list:$ 

761# #if $\text {enum}[1]<2000000:$ 

762# print(enum)

763

764＃展示策略

765 print(f”最速收敛：{[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1]｝”）

700 print(f”全局最优：{[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1]｝”）

767#[(1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1),448518.046585434]

768#[(1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1),435188.3987616001]

709

770 $x=[\underline {}+1$ forin range(21)]

771 $\mathrm {y}1=\text {get_{ans}}([1,$ ，1,1,1,1,1,1,1,1,1,1,0,0,0,0,1])＃最速收敛

772y2=getans([1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1])＃全局最优

773 $plt.figure(figsize=(10,6))$ 

774 plt.subplot(111)

775 plt.plot $(x,$ y1,,'red', $label='$ ＇最速收敛＇, $marker='o'$  ）

776 $plt.plot(x,$ $y2$  $color='blue'$  $label='$ 全局最优＇, $marker='D'$ '）

777 plt.legend()

778 plt.title(＇问题四决策 变大扰动 利润上升曲线＇）

779 plt.xlabel(＇循环次数＇）

780 plt.ylabel（“净利润＇）

781 $plt.xticks(x)$ 

中国大学生在线

782 plt.grid(True)

783 $plt.show()$ 

dxs.moe.gov.cn

784 print(y1)

<!-- 69 -->

