---
schema_version: 2
type: method
time: '2026-11-15T09:08:24+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-09-第20节-循环神经网络编程与考试安排宣讲]]'
---

# PyTorch单层RNN的张量接口核对

任务：把[[01_Knowledge/RNN时间展开与参数共享]]的递推接到批次序列与任务输出。限定单层、单向、有批次输入。令$T$为步数、$N$为样本数、$d$为每步输入维数、$M$为隐藏维数。`nn.RNN(d,M,num_layers=1)`默认`tanh`，也可选`relu`，`bias`控制偏置；$M>d$不是必要条件，循环层数也不等于时间步数。

| 对象 | 默认`batch_first=False` | `batch_first=True` |
|---|---|---|
| 输入 | `(T,N,d)` | `(N,T,d)` |
| 初态`h0` | `(1,N,M)` | `(1,N,M)` |
| 全部状态`output` | `(T,N,M)` | `(N,T,M)` |
| 末态`h_n` | `(1,N,M)` | `(1,N,M)` |

先逐轴标注，再检查输入与初态的$N$一致、样本顺序一致、dtype和device与模型相容。初态没有时间轴但保留层轴，不能把`(N,M)`当作本设置的`h0`；可取零初态，随机不是唯一选择。

```python
rnn = torch.nn.RNN(10, 20, num_layers=1)
x = torch.randn(5, 3, 10)
h0 = torch.randn(1, 3, 20)
output, h_n = rnn(x, h0)
```

默认布局下，数学第$t$步、Python样本索引$n$的状态为`output[t-1,n,:]`。末步可取`output[-1,:,:]`或`h_n[0,:,:]`，均为`(N,M)`；整个`h_n`多一个层轴，不能声称其形状与`output[-1]`相同。多层或双向情形须重新核对本表，不能外推末态取法。

`output`是隐藏态，并不是任务预测；二维下一位置需接`nn.Linear(M,2)`，它作用于最后一维。例如4条10步序列、`RNN(2,8)`，输入`(10,4,2)`、初态`(1,4,8)`、全部状态`(10,4,8)`、末态`(1,4,8)`；接输出层后预测为`(10,4,2)`，才能与同形状二维标签比较。

参数名分别为`weight_ih_l0`、`weight_hh_l0`、`bias_ih_l0`、`bias_hh_l0`，形状依次为`(M,d)`、`(M,M)`、`(M,)`、`(M,)`。行批处理表达为

$$H_t=\sigma(X_tW_{ih}^{\mathsf T}+b_{ih}+H_{t-1}W_{hh}^{\mathsf T}+b_{hh}).$$

两偏置在函数表达上可合并，但程序独立保存；行列约定解释了转置，不意味着框架禁止列向量运算。[RNN接口核对](https://docs.pytorch.org/docs/stable/generated/torch.nn.RNN.html)。示意代码依据课堂形状重整，未声称取得或运行原脚本。
