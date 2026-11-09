---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/作业/第1-6章-课件与课堂提问汇编作业]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-12-第11节-深度学习编程与分类模型宣讲]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-14-第12节-神经网络分类模型代码编写]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-10-19-第13节-神经网络与卷积网络课程宣讲]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-02-第18节-深度学习理论与RNN原理授课]]'
---
# Softmax概率与交叉熵

## 严格定义与核心内容

每样本logits z的p_j=e^{z_j}/∑e^{z_k}，one-hot真实类y的交叉熵−∑Y_j log p_j=−log p_y。

批量(N,J)沿类别轴归一化再沿样本平均，不能跨样本归一化。

稳定实现令m=max z，ℓ=−z_y+m+log∑exp(z_j−m)。

PyTorch CrossEntropyLoss常直接收logits，整数标签是0起long或使用同形概率标签；不可把已Softmax概率再次当logits。

分类并非数学上绝不允许平方损失，不同损失绝对数值不可直接排名。
