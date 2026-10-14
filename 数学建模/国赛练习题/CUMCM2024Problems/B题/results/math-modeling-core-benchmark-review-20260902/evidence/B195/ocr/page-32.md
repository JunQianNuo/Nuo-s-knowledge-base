import numpy as np

import pandas as $pd$ 

import random

import math

import matplotlib.pyplot as plt

import numpy as np

plt.rcParams['font.sans-serif' $']=$ $'KaiTi']$ 

plt.rcParams['axes.unicodeminus $']=Fals$ 

def $get\_w(data\_list):$ 

14

＃此处进行仿真，为时间角度考虑，仅循环两次

ans $\text {as_{list}}=[]$ 

16

＃todo：过程函数

def $get\_new\_part(n\_part\_ori,$ $p\_part\_make,p\_part\_test):$ 

18

＃零件检测函数，输入零件数、次品率、检测率，得到新零件数、新次品率、检测数

19

$$n\_part\_good=n\_part\_ori*(1-p\_part\_make)$$

20

$$n\_part\_bad=n\_part\_ori*p\_part\_make$$

21

$$\_part\_bad\_test=n\_part\_bad*p\_part\_test$$

22

$n\_part\_$ $\_new$ $=n\_part\_ori-n\_part\_bad\_test$ 

23

$\text {p_{part_{new}}}=1-\text {n_{part_{good}}}$ $/$ $n\_part\_new$ 

return $n\_part\_new$ , $p\_part\_new$ , $n\_part\_ori*p\_part\_test$ 

25

26

def $get\_product(n\_parts$ s, $p\_parts$ , $p\_product\_make)$ ):

＃输入每种零件的个数，得到产品生产数、次品数、正品数

28

$$\text {p_{good}}=1-\text {p_{product}_{make}}$$

29

for enum in $P\_parts:$ 

30

$p\_good$ $*=1-enum$ 

nparts $=np.$ array $(n\_parts)$ 

32

$\text {n_{product}}=\text {np}$ ,min $(n\_parts)$ 

3.3

nproductgood $=n\_product*p\_good$ 

34

nproductbad $=n\_product-n\_product\_goo$ 

35

return $n\_product$ , $n\_product\_good$ , $n\_product\_bad$ 

30

37

def $deal\_product\_bad2(n\_product\_bad$ , $p\_parts):$ 

38

＃输入次品数、每个零件的次品率，得到每种新的零件个数，每种新的零件的次品率（一个成品由两个零件构成）

30

$$n\_part\_1=n\_product\_bad$$

40

$$\text {n_{part}_{2}=n_{product}_{bad}}$$

41

$$p\_swap=p\_parts[0]+p\_parts[1]-p\_parts[0]*p\_parts[1]+(1-p\_parts[0])*($$

42

$$1-p\_parts[1])*p\_product\_make$$

43

$$p\_part\_1=p\_parts[0]/p\_swap$$

44

$$p\_part\_2=p\_parts[1]/p\_swap$$

45

return $n\_part\_1,$ $n\_part\_2,$ $p\_part\_1,$ $p\_part\_2$ 

46

47

＃循环仿真直至不能盈利

48

＃此处使用法一（全程固定）进行循环处理

49

＃print（”此处使用法一（全程固定）进行循环处理”）

$cn$ 中国大dxs.moe.gov

<!-- 32 -->

