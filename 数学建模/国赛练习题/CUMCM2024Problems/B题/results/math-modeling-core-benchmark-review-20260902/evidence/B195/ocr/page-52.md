506#ansmaybe $list=list$ (product([0, $,1]$  $repeat=16))$ 

507 # $\text {ans_{list}=[]}$ 

508# count $t=0$ 

509 #for $maybe\_$ list in $ans\_maybe\_list:$ 

510# count $+=1$ 

511# print(count)

512# $ans\_$ list.append $([maybe\_$ list,getans(maybelist)])

513## print(sorted(anslist,key=lambda x: $x[1]))$ 

514#ans $\_list=[$ enum for enum in ans1list if $enum[1]>0]$ 516#ans $list$ $=$  $orted(ans\_list$  key=lambda&gt; $4$ $x[1])$ 

516#for enumin anslist:

517#

#if enum $[1]<2000000:$ 

518#

print(enum)

619 print(f”最速收敛：{[1,1,1,1,1,1,1, 1, 1,1,1,0,0,0,0,1]}”)

620 print(f”全局最优：{[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1]｝”）

521

522 $x=[\_+1for\_inrange(21)]$ 

523y1=getans([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1])＃最速收敛

524y2= getans([1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1])＃全局最优

525 $plt.figure(figsize=(10,6))$ 

526 plt.subplot(111)

627 $plt.plot(x,$ $y1$ .'red', $label=^{3}$ 最速收敛＇, $marker='o')$ ）

520plt.plot(x, $y2$  $color='blue'$  $label='$ 全局最优＇, $marker='D'$ ）

629 plt.legend()

530 plt.title(＇问题三决策 利润上升曲线＇）

531 plt.xlabel(＇循环次数＇）

532 plt.ylabel(＇净利润＇）

533 plt.xticks(x)

534 plt.grid(True)

535 plt.show()

536

# 题三代码

import random

import math

import matplotlib.pyplot as plt

import numpy as np

$plt.rcParams['font.sans-serif']=[$ 'KaiTi']

plt.rcParams['axes.unicodeminus $']=Fals$ 

def $get\_w(data\_list):$ 

12

＃此处进行仿真，为时间角度考虑，仅循环两次

13

$$\text {ans_{list}}=[]$$

14

＃ todo：过程函数

v.cn

15

def $get\_new\_part(n\_part\_ori$  $P\_part\_$ make, $p\_part\_test):$ 

16

＃零件检测函数，输人零件数、次品率、检测率，得到新零件数， 新次 率 检测数 $n\_part\_good=n\_part\_ori*(1-p\_part\_make)$ 

<!-- 52 -->

