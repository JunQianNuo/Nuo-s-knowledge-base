---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-02-第18节-深度学习理论与RNN原理授课]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-09-第20节-循环神经网络编程与考试安排宣讲]]'
---
# RNN时间展开与参数共享

## 严格定义与核心内容

基本RNN为q_t=Wh_{t−1}+Ux_t+b，h_t=σ(q_t)，y_t=Vh_t+c。

输入d、隐藏m、输出p、固定h₀下参数数m²+md+m+pm+p，不随步数T增长。

展开增加计算深度而每步复用同组数组，不等同各层独立参数的前馈网络。

序列样本可不同长，具体任务决定每步或末步输出；文本编号通常还需向量表示。

## 递推模块与任务输出的程序边界

基本递推可写为$h_t=\sigma(Wh_{t-1}+Ux_t+b)$，其中$x_t\in\mathbb R^d$、$h_t\in\mathbb R^M$，$W\in\mathbb R^{M\times M}$、$U\in\mathbb R^{M\times d}$。时间上反复使用同组参数；120步序列不表示120个循环层。

`nn.RNN`只给出隐藏态递推，$y_t=Vh_t+c$的任务映射仍须另接。例如预测下一二维点，输出维数为2而非隐藏维数。见[[01_Knowledge/PyTorch单层RNN的张量接口核对]]。截取较短序列片段可缩短一次展开的计算链，但不改变循环层的定义。
