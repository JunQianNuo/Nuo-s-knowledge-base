---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-12-第11节-深度学习编程与分类模型宣讲]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-14-第12节-神经网络分类模型代码编写]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-19-第13节-神经网络与卷积网络课程宣讲]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-02-第18节-深度学习理论与RNN原理授课]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-08-31-第1节-转写_电子科大王君豪的快速会议]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-09-02-第2节-机器学习基础概念与模型构建教学]]'
---
# Softmax概率与交叉熵

## 严格定义与核心内容

每样本logits z的p_j=e^{z_j}/∑e^{z_k}，one-hot真实类y的交叉熵−∑Y_j log p_j=−log p_y。

批量(N,J)沿类别轴归一化再沿样本平均，不能跨样本归一化。

稳定实现令m=max z，ℓ=−z_y+m+log∑exp(z_j−m)。

PyTorch CrossEntropyLoss常直接收logits，整数标签是0起long或使用同形概率标签；不可把已Softmax概率再次当logits。

分类并非数学上绝不允许平方损失，不同损失绝对数值不可直接排名。


## 稳定数值和批次聚合的手算检查

两个logits为1000、999、真实类为第一类时，减最大值得损失$\log(1+e^{-1})\approx.3133$，不直接计算$e^{1000}$；共同平移logits不改变概率。

两样本真实类为1、3，概率$(.7,.1,.1,.1)$和$(.1,.2,.6,.1)$，one-hot矩阵和概率矩阵均为$2\times4$，逐元素乘积同形，沿类别轴求和为$(2,)$，再平均为零维标量；$L=-(\log .7+\log .6)/2\approx.4338$。它衡量真实类置信度，而非只看argmax。

手写`-(Y*log(P)).sum(dim=1).mean()`在one-hot和概率匹配时对应公式，但极端P可下溢到0，甚至出现零乘负无穷；稳定实现应基于logits/log-softmax。库CrossEntropyLoss整数目标为0起long；概率目标需与logits同形并满足有效分布，不因接口接收浮点就自动验证标签。网络先Softmax后再把概率误作logits会改变优化目标。[官方接口](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)。


## 历史来源可用性（2026-11-22）

本卡曾引用的汇编作业目前未在知识库中找到。无法解析的元数据来源移至此处保留，现存课堂来源与原有知识正文保持。此记录不表示缺失文件已经恢复或其中题目已经重建。

历史路径：`03_Sources/Courses/深度学习/作业/第1-6章-课件与课堂提问汇编作业.md`。
