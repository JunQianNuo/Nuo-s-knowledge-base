$x_{i}=\{\begin{matrix}0,\\ \end{matrix}$ 对零件（跳过检测 $\begin{array}{c}\text {迟}1.\end{array}$ 进行检测

检测后更新状态 $\left(d_{i},q_{i}\right)$ 

·半成品检测决策变量 $x_{\text {semi}_{j}}:$ 

$x_{semi_{j}}=\{0,$  对半成品j跳过检测，决定检测

·成品检测变量 $x_{final}:$ 

$x_{final}=\{\begin{matrix}0,\\ \end{matrix}$  对成品跳过检测 $.$ ，决定检测

# ②拆解决策变量

对于不合格的半成品和成品，企业可以选择拆解。值得注意的是，当成品拆解时，如果其中的半成品合格，合格的半成品将不再被拆解，因为合格的半成品比其组成零件的回收收益更高（相较于对应零件增加半成品检测成本和装配成本）。

·半成品拆解决策变量 $y_{\text {semi}_{j}}$ 1表示拆解次品半成品，0表示不拆解。

$y_{semi_{j}}=\{\begin{matrix}0,\\ \end{matrix}$  不拆解次品半成品j ，拆解

·成品拆解决策变量 $y_{\text {final}}:$  1表示拆解次品成品，0表示不拆解。

<!-- $y_{final}=\left\{\begin{matrix}0,不拆解次品成品\\ 1,拆解\end{matrix}\right.$ -->
![](https://web-api.textin.com/ocr_image/external/e48d6471f1c0f0ce.jpg)

# 7.2 成本函数

成本函数 $C(a_{t})$ 包括零件采购成本、检测成本、装配成本和拆解成本。分别定义如下：

## 7.2.1采购成本 $C_{\text {purchase}}$ 

假设零件i的采购成本为 $A$ ，则总采购成本为：

$$C_{\text {purchase}}=\sum _{i=1}^{g}n_{i}\times p_{i}$$

其中 $n_{i}$ ，表示采购零件t的数量。

## 7.2.2检测成本 $C_{\text {inspect}}$ 

零件、半成品和成品的检测成本分别为：

$C_{\text {inspect}}=\sum _{i=1}^{8}n_{i}\times c_{\text {inspect\_part\_i}}\times x_{i}+\sum _{j=1}^{3}n_{\text {semi}_{j}}\times c_{\text {inspect\_semi\_i}}\times x_{\text {semi\_j}}$ $+n_{\text {final}}\times c_{\text {inspect\_final}}\times x_{\text {final}}$  大学生在线 $dxsmoegov.cn$ dxs.moe.gov.cn

<!-- 15 -->

