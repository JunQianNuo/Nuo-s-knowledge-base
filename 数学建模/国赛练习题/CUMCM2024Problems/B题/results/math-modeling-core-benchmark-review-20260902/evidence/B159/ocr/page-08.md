可供企业考虑的决策共下述16种情况：

**表2 16种决策方案及对应编号表**

<table border="1" ><tr>
<td>不合格成品是否拆解</td>
<td>是否检测零配件1</td>
<td>是否检测零配件2</td>
<td>是否检测成品</td>
<td>编号</td>
</tr><tr>
<td rowspan="8">是</td>
<td rowspan="4">是</td>
<td rowspan="2">是</td>
<td>是</td>
<td>001</td>
</tr><tr>
<td>否</td>
<td>002</td>
</tr><tr>
<td rowspan="2">否</td>
<td>是</td>
<td>003</td>
</tr><tr>
<td>否</td>
<td>004</td>
</tr><tr>
<td rowspan="4">否</td>
<td rowspan="2">是</td>
<td>是</td>
<td>005</td>
</tr><tr>
<td>否</td>
<td>006</td>
</tr><tr>
<td rowspan="2">否</td>
<td>是</td>
<td>007</td>
</tr><tr>
<td>否</td>
<td>008</td>
</tr><tr>
<td rowspan="8">否</td>
<td rowspan="4">是</td>
<td rowspan="2">是</td>
<td>是</td>
<td>009</td>
</tr><tr>
<td>否</td>
<td>010</td>
</tr><tr>
<td rowspan="2">否</td>
<td>是</td>
<td>011</td>
</tr><tr>
<td>否</td>
<td>012</td>
</tr><tr>
<td rowspan="4">否</td>
<td rowspan="2">是</td>
<td>是</td>
<td>013</td>
</tr><tr>
<td>否</td>
<td>014</td>
</tr><tr>
<td rowspan="2">否</td>
<td>是</td>
<td>015</td>
</tr><tr>
<td>否</td>
<td>016</td>
</tr></table>

**由于当对不合格的成品进行拆解时，如果始终未对零配件1和零配件2进行检测，则零配件的次品会永远处于流水线中永远不会被丢弃，故做出如下假设：当企业的决策为对不合格的成品进行拆解时，若开始进行（1）时未对零配件1或零配件2进行检测，则拆解后重复（1）时必然对其进行检测。**

下文将计算16种不同决策下生产每个合格成品花销的期望与各产品次品率、购买单价、检测成本、装配成本以及调换损失、拆解费用的关系。由于上述假设的存在，是否对不合格**的成品拆解会对表达式的求解产生较大影响，丢弃不合格成品的8种决策情况可以给出统**一的表达式，拆解不合格成品的8种决策情况较为复杂，由于篇幅原因，只详细说明编号为008的表达式推导过程，其余编号直接给出表达式。

# 6.1 丢弃不合格的成品下表达式的求解

在丢弃不合格的成品的前提条件下，根据是否检测零配件1、是否检测零配件2、是否检测成品建立三个示性变量 $I_{1},I_{2},I_{3}$ ，其定义如下：

$$I_{1}=\left\{\begin{matrix}1,不检验零配件1\\ 0,检验零配件1\end{matrix}\right.$$

$$I_{2}=\left\{\begin{matrix}1,不检验零配件2\\ 0,检验零配件2\end{matrix}\right.$$

中国大学生在线

dxs.moe.gov.cn

<!-- 8 -->

