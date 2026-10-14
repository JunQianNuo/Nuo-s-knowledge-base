import torch, numpy
from torch import nn

torch.manual_seed(2)

N_train = 10000
N_test = 1000
d = 5

# 生成训练集/测试集
x_train = torch.zeros((N_train,d))
for i in range(d):
    x_train[:,i] = torch.rand((N_train,))*2-1
y_train = 1/(torch.sum(x_train**2, dim = 1)+1)
x_test = torch.zeros((N_test,d))
for i in range(d):
    x_test[:,i] = torch.rand((N_test,))*2-1
y_test = 1/(torch.sum(x_test**2, dim = 1)+1)

# 定义全连接网络（ReLU, 3层, 宽度为10）
M = 10
Net_L3M10 = nn.Sequential(nn.Linear(d,M),nn.ReLU(),nn.Linear(M,M),nn.ReLU(),nn.Linear(M,1))
# print(Net_L3M10(x_train))  # 神经网络Net_L3M10 逐行作用于 x_train
# print(Net_L3M10[0].weight)  # 神经网络输入层的权重矩阵，即 W_1
# print(Net_L3M10[4].bias)  # 神经网络输出层的偏置向量，即 b_3

# 定义损失函数
loss = torch.sum((Net_L3M10(x_train).squeeze()-y_train)**2)/N_train

# 优化
N_iteration = 5000
lrseq = numpy.linspace(1e-2,1e-4,N_iteration)
optimizer = torch.optim.Adam(Net_L3M10.parameters())
print('L=3, M=10:')
for n in range(N_iteration):
    if n%1000 == 0:
        print('n = %g, loss = %.3e' %(n, loss.item()) )
    ## 设置学习率
    for param_group in optimizer.param_groups:
        param_group['lr'] = lrseq[n]
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss = torch.sum((Net_L3M10(x_train).squeeze()-y_train)**2)/N_train
    
loss_train = torch.sum((Net_L3M10(x_train).squeeze()-y_train)**2)/N_train
print('Final training loss = %.3e \n' %(loss_train.item()))
loss_test = torch.sum((Net_L3M10(x_test).squeeze()-y_test)**2)/N_test
print('Final testing loss = %.3e \n' %(loss_test.item()))

# 定义 L=3, M=20 的全连接网络
M = 20
Net_L3M20 = nn.Sequential(nn.Linear(d,M),nn.ReLU(),nn.Linear(M,M),nn.ReLU(),nn.Linear(M,1))
loss = torch.sum((Net_L3M20(x_train).squeeze()-y_train)**2)/N_train
optimizer = torch.optim.Adam(Net_L3M20.parameters())
print('L=3, M=20:')
for n in range(N_iteration):
    if n%1000 == 0:
        print('n = %g, loss = %.3e' %(n, loss.item()))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lrseq[n]
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss = torch.sum((Net_L3M20(x_train).squeeze()-y_train)**2)/N_train

loss_train = torch.sum((Net_L3M20(x_train).squeeze()-y_train)**2)/N_train
print('Final training loss = %.3e \n' %(loss_train.item()))
loss_test = torch.sum((Net_L3M20(x_test).squeeze()-y_test)**2)/N_test
print('Final testing loss = %.3e \n' %(loss_test.item()))

# 定义 L=5, M=10 的全连接网络
M = 10
Net_L5M10 = nn.Sequential(nn.Linear(d,M),nn.ReLU(),nn.Linear(M,M),nn.ReLU(),nn.Linear(M,M),nn.ReLU(),nn.Linear(M,M),nn.ReLU(),nn.Linear(M,1))
loss = torch.sum((Net_L5M10(x_train).squeeze()-y_train)**2)/N_train
optimizer = torch.optim.Adam(Net_L5M10.parameters())
print('L=5, M=10:')
for n in range(N_iteration+1):
    if n%1000 == 0:
        print('n = %g, loss = %.3e' %(n, loss.item()) )
    for param_group in optimizer.param_groups:
        param_group['lr'] = lrseq[n]
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss = torch.sum((Net_L5M10(x_train).squeeze()-y_train)**2)/N_train

loss_train = torch.sum((Net_L5M10(x_train).squeeze()-y_train)**2)/N_train
print('Final training loss = %.3e \n' %(loss_train.item()))
loss_test = torch.sum((Net_L5M10(x_test).squeeze()-y_test)**2)/N_test
print('Final testing loss = %.3e \n' %(loss_test.item()))

    
