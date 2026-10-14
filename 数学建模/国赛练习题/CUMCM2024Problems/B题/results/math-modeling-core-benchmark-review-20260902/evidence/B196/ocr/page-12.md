<!-- Stuation 1 Situation 2 0 0 Situation 3 Situation 4 20 Stuation 5 Situation 6 [0000][0001][0010][0011][0100][0101][0110][0111][1000][1001][1010][1011][1100][1101][1110][1111] -->
![](https://web-api.textin.com/ocr_image/external/16bb680e832570e1.jpg)

图6问题二中六中情况的决策热点图

在图表n中，我们可以观察到，在任意给定的情况下，利润最高的前十个策略最多仅涉及两种不同的决策类型。并且，这些策略中以一种决策类型为主导。据此，我们可以推断，该主导决策类型即为该情况下的最优决策。基于这一分析，我们构建了如下的决策表：

表1 问题二中六种情况的决策

<table border="1" ><tr>
<td>情况决策</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr><tr>
<td>零件1 是否检测</td>
<td>是</td>
<td>是</td>
<td>否</td>
<td>是</td>
<td>否</td>
<td>否</td>
</tr><tr>
<td>零件2 是否检测</td>
<td>否</td>
<td>是</td>
<td>否</td>
<td>是</td>
<td>是</td>
<td>否</td>
</tr><tr>
<td>成品是否检测</td>
<td>否</td>
<td>否</td>
<td>是</td>
<td>是</td>
<td>否</td>
<td>否</td>
</tr><tr>
<td>成品是否拆解</td>
<td>是</td>
<td>是</td>
<td>是</td>
<td>是</td>
<td>是</td>
<td>否</td>
</tr></table>

基于这些决策进行模拟计算，假设采购的零件1和零件2数量相同，我们得到各情况在1000次采购2000个零件A和B进行制作售卖情况下的平均利润如下表：

表2问题二中六种情况的最优决策平均利润值

<table border="1" ><tr>
<td></td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr><tr>
<td>最优决策平均利润</td>
<td>35934 元</td>
<td>20668 元</td>
<td>31878 元</td>
<td>25040 元</td>
<td>26527 元</td>
<td>40138 元</td>
</tr></table>

<!-- 12 -->

