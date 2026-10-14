其中， $c_{\text {inspect_{part}}}$ s $c_{\text {inspect_{part}_{j}}}$ j $c_{\text {inspect_{final}}}$ t分别指代零件t、半成品j和成品的单独检测成本： $n_{i}、$ $n_{\text {semi}_{j}}$ $n_{\text {final}}$ 分别表示零件i、半成品j和成品的数量； $x_{i}、$ $x_{semi_{j}}、$ $x_{final}分$ 别表示零件i、半成品j和成品是否检测的决策变量。

# 7.2.3 装配成本 $C_{assemble}$ 

零件装配为半成品、半成品装配为成品的成本分别为：

$$C_{\text {assemble\_semi}}=\sum _{j=1}^{3}n_{\text {semi}_{j}}\times c_{a,j}$$

$$C_{\text {assemble\_final}}=n_{\text {final}}\times c_{\text {a\_final}}$$

其中， $c_{a,j}$ $c_{a,final}$ 别表示零件装配为半成品j、半成品装配为成品的单个装配成本。

# 7.2.4拆解成本 $C_{\text {disassemble}}$ 

拆解半成品和成品的成本为：

$$C_{\text {disassemble\_semi}}=n_{\text {semi}_{j}}\times c_{d,j}\times r_{\text {semi}_{j}}$$

$$C_{\text {disassemble\_final}}=n_{\text {final}}\times c_{\text {d\_final}}\times r_{\text {final}}$$

其中， $c_{d,j}、c_{d,final}$ 分别表示半成品j和成品的单个拆解成本。

# 7.2.5 成本函数总结

总成本 $C(a_{t})$ 的表达式为：

$C\left(a_{t}\right)=C_{\text {purchase}}+C_{\text {inspect}}+C_{\text {assemble_{sem}l}}+C_{\text {assemble_{f}inal}}+C_{\text {}}$ disassemblesemt+Cdisassemblefinal

# 7.3 收益函数

收益函数 $R\left(S_{t},a_{t}\right)$ 包括成品销售收益和回收收益。

## 7.3.1 成品销售收入 $R_{\text {final}}$ 

$$R_{\text {final}}=n_{\text {final}}\times P\times q_{\text {final}}$$

其中，P表示成品售价， $q_{\text {final}}=1$  表示仅合格成品能带来销售收益。

## 7.3.2回收收益 $R_{\text {recycle}}$ 

拆解回收零件和半成品的收益为：

$$R_{\text {recycle\_part}}=\sum _{i=1}^{8}n_{i}\times \left(p_{i}+c_{\text {inspect\_part\_i}}\right)\times x_{i}\times \left(1-q_{i}\right)$$

$$R_{\text {recycl.semi}}=\sum _{j=1}^{3}n_{\text {semi}_{j}}\times \left(\sum _{i\in \text {semi},j}p_{i}+c_{\text {inspect.semi},j}+c_{a,j}\right)\times x_{\text {semi}_{j}}\times \left(1-q_{\text {semi}_{j}}\right)$$

## 7.3.3 收益函数总结

$$R\left(S_{t},a_{t}\right)=R_{\text {final}}+R_{\text {recycle_{part}}}+R_{\text {recycl_{seml}}}$$

# 7.4 模型总结

综上所述，系统的目标是找到使得总收益最大化的决策路径 $a_{t}$  即，我们希望最大化如 $cn$ 

<!-- 16 -->

