---
raw_title: Homework04
subject: Homework04
source: Homework04.pdf
status: mineru解析
parser: mineru
---

# 《深度学习》课程作业04

Exercise 1 (10pts)

计算下图中卷积网络的函数值:

![](images/b221d23769d8e9367cd9711dea4cfb1a67947aea39806d57ec2a951e081d7631.jpg)

其中

$$
X = \left[ \begin{array}{c c c c} 2 & 1 & - 4 & 3 \\ 1 & 1 & 0 & 2 \\ 2 & - 1 & 1 & 5 \\ 2 & - 4 & - 2 & 2 \end{array} \right], \quad K = \left[ \begin{array}{c c} 1 & 1 \\ 2 & - 1 \end{array} \right], \quad W = \left[ \begin{array}{c c c c} 2 & 1 & 0 & - 1 \\ 3 & 2 & - 1 & - 2 \end{array} \right]
$$

$$
b _ {1} = 4, \quad b _ {2} = - 5, \quad \sigma = \mathrm{ReLU}.
$$

Exercise 2 (15pts)

设 $\phi ( X ; \theta ) : \mathbb { R } ^ { m \times m }  \mathbb { R } ^ { m ^ { \prime } \times m ^ { \prime } }$ 是一个卷积神经网络. 它由 L 个卷积层构成, 且每一层满足: 卷积核规模为 $s \times s ;$ 步幅为 $p ;$ 激活函数记作 $\sigma ,$ 且 $\sigma ( t )$ 对任意标量 t 的计算复杂度都是 O(1).

(1) 写出 $m ^ { \prime }$ 关于 $m , L , s , p$ 的表达式 (假设 m 足够大以至于 $m ^ { \prime } > 0 \ )$ );

(2) 求对一个 $m \times m$ 矩阵作一次前向传播所需要的计算复杂度(用 $m , L , s , p$ 表示).

Exercise 3 (15pts)

设 $[ y _ { 1 } , y _ { 2 } , y _ { 3 } ] = \phi ( x _ { 1 } , x _ { 2 } , x _ { 3 } ; h _ { 0 } ; \theta )$ 是一个执行了3步的循环神经网络. 其中输入 $\boldsymbol { x } _ { t } \in \mathbb { R } ^ { 2 \times 1 }$ , 输出$y _ { t } \in$ R. 参数集 $\theta = \{ W , U , b , V , c \}$ , 其中 $W \in \mathbb { R } ^ { 3 \times 3 } , U \in \mathbb { R } ^ { 3 \times 2 } , b \in \mathbb { R } ^ { 3 \times 1 } , V \in \mathbb { R } ^ { 1 \times 3 } , c \in$ R. 初始隐藏态 $h _ { 0 } \in \mathbb { R } ^ { 3 \times 1 }$

设

$$
\begin{array}{c} x _ {1} = \left[ \begin{array}{c} 1 \\ 2 \end{array} \right], x _ {2} = \left[ \begin{array}{c} - 3 \\ 1 \end{array} \right], x _ {3} = \left[ \begin{array}{c} 2 \\ - 1 \end{array} \right], h _ {0} = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right], W = \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & - 1 \end{array} \right], U = \left[ \begin{array}{c c} 2 & 2 \\ 1 & 0 \\ 0 & 1 \end{array} \right], b = \left[ \begin{array}{c} 1 \\ - 2 \\ 0 \end{array} \right], \\ V = \left[ \begin{array}{c c c} 1 & 2 & 3 \end{array} \right], c = 1, \sigma = \text {ReLU}. \end{array}
$$

计算 y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub> 以及它们对 W, U, b, V, c 的梯度.

Exercise 4 (20pts)

用 Python + numpy/torch 等命令库编程, 实现用卷积神经网络对 2D 的 MNIST 手写数字数据集进行分类.

(1) 用PyTorch自带的torchvision库下载MNIST(2D)数据集. 参考代码如下:

```python
from torchvision.datasets import MNIST
```

```python
transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((mean,), (std,))])
```

```python
train_dataset = torchvision.datasets.MNIST(
root='./data',
train=True, # 是否为训练集
download=True, # 最好都是True，没有下载的话自动下载
transform=transform)
```

```python
test_dataset = torchvision.datasets.MNIST(
root='./data',
train=False,
download=True,
transform=transform)
```

(2) 定义如下架构的卷积神经网络:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
图片 $(28\times 28)$
</div>

→ 卷积层(输入通道1, 输出通道32, 核尺寸3 × 3, 步幅1, 上下左右各填充1行1列, ReLU激活)→ 2×2 最大池化

→ 卷积层(输入通道32, 输出通道64, 核尺寸3 × 3, 步幅1, 上下左右各填充1行1列, ReLU激活)

→ 2×2 最大池化 → 拉平成列向量 → 全连接层(输出维数128, ReLU激活)

```txt
→ 全连接层(输出维数10, softmax激活)
```

优化器选用 Adam 优化器(学习率等参数自行调整). 输出训练损失和测试准确率.

(3) 尝试调整(2)中的网络架构、激活函数、优化算法等, 观察能否获得更高的测试准确率.

## Exercise 5 (20pts)

用 Python + numpy/torch 等命令库编程, 实现循环神经网络对参数的梯度计算. 具体地, 考虑一个循环神经网络 $[ y _ { 1 } , y _ { 2 } , . . . ] = f ( x _ { 1 } , x _ { 2 } , . . . ; h _ { 0 } ; \theta )$ , 其中输入维数和输出维数分别为 $d , d _ { \mathrm { o u t } }$ , 宽度(即隐藏态 $h _ { t }$ 的长度)为 M, 而总步数并不确定, 可以为任意正整数. 现给定 $x _ { 1 } , x _ { 2 } , \dotsc , h _ { 0 } , \theta$ 的值, 需要计算 $y _ { 1 } , y _ { 2 } , . . .$ . 的值及它们对各参数的梯度.

(1) 以矩阵-向量乘法的形式, 写出该算法的伪代码(可参考讲义 2.2.3 的 Algorithm 2, 全连接神经网络的正/反向传播算法);

(2) 编写函数, 以实现上述算法. 可参考如下模版:

```txt
def RNN_grad(x_list, h0, W, U, b, V, c, activation_type):
```

<sub>#</sub> 设定<sub>,</sub> 初始化等

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
# 对 $t = 1,2,\ldots$ 逐步进行计算  
for t in range(len(x_list)):  
...  
return y_list, DyDW_list, DyDU_list, DyDb_list, DyDV_list, DyDc_list
</div>

• 输入参数中, x\_list 表示输入的向量 $x _ { 1 } , x _ { 2 } , \ldots ; \mathtt { h 0 }$ 表示初始隐藏态; <sub>W,</sub> <sub>U,</sub> <sub>b,</sub> <sub>V,</sub> <sub>c</sub> 表示网络的各参数; <sub>activation\_type</sub> 是一个字符串, 表示激活函数 σ 的类型, 例如 ‘‘<sub>ReLU"</sub>,‘‘tanh" 等.

• 输入维数 d 可以通过读取 $x _ { t }$ 的长度得到, 如 $\mathtt { d } { = } \mathtt { l e n } ( \mathtt { x \_ l i s t } [ 0 ] )$ ; 输出维数可以通过读取 V的行数得到, 如 <sub>d\_out=V.shape</sub>[<sub>0</sub>];

• 输出参数中, y\_list 表示输出的向量 $y _ { 1 } , y _ { 2 } , \ldots ;$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
DyDW_list, DyDU_list, DyDb_list, DyDV_list, DyDc_list 均是列表, 其第 t 个元素表示  $y_{t}$  对相应参数的梯度.
</div>

(3) 用 Exercise 3 中的数据对(2)中的函数进行测试, 并与 Exercise 3 中手算的结果进行比较.

```txt
Exercise 6 (20pts)
```

用 Python + numpy/torch 等命令库编程, 实现用循环神经网络对一个未知的离散动态系统$y _ { t } = F ( y _ { t - 1 } , x _ { t } ) , y _ { 0 } = 0 , t = 1 , 2 , . .$ . 进行回归, 其中 $x _ { t } \in \mathbb { R } ^ { 2 } , y _ { t } \in \mathbb { R } .$

(1) 用 pickle 库读取数据集文件 hw04.data. 其中,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
x_train 是一个 $10000 \times 20 \times 2$ 的3D-array.
</div>

x train[N,:,:] 表示第 N 个数据点的输入,

x train[:,t,:] 表示全体数据点在第 t 步时的输入,

x train[:,:,k] 表示全体数据点输入的第 k 维.

因此 x train 一共包含了 10000 个数据点, 每个数据点包含了 $x _ { 1 } , \ldots , x _ { 2 0 }$ 共20步的输入.

相应地, y train 是一个10000 × 20 的2D-array.

y train[N,:] 表示第 N 个数据点的输出,

y train[:,t] 表示全体数据点在第 t 步时的输出.

类似地, x test 和 y test 形成测试数据集.

(2) 用一个循环神经网络通过训练数据集学习潜在的动态系统, 并将训练后的神经网络在测试集上进行测试. 最终, 输出训练损失、训练误差、测试误差和泛化差距(计算误差时选用 ℓ<sup>2</sup> 误差). 激活函数选择 tanh 函数. 初始隐藏态可选用全零向量. 网络的宽度、优化算法、学习率等参数可自行选择. 可以根据实际的设备算力, 选择少量的数据点或更短的片段进行训练, 不要求使用全部10000个训练数据点和完整长度的片段进行训练.