import torch

d = 5
x = torch.ones((d,), requires_grad=True)

optimizer_SGD_001 = torch.optim.SGD( [x] , lr=0.01 )

def f(y): # y 必须是Tensor变量
    s = torch.Tensor([0])
    for i in range(1,d-2):
        s = s + (y[i-1]*y[i]+y[i]*y[i+1]+y[i+1]*y[i+2]-i/(d-3))**2
    s = s/(d-3)
    return s

import numpy
N_iteration = 1000
fseq = numpy.zeros((N_iteration+1,))

# SGD
for n in range(N_iteration):
    optimizer_SGD_001.zero_grad() # 将梯度重置为0
    loss = f(x)
    fseq[n] = loss.detach() # 此时fseq[n]存下的是一个“干净”的值，不包括计算图
    loss.backward() # 反向传播（计算 loss 关于 x 的梯度）
    optimizer_SGD_001.step() # 更新 x
loss = f(x)
print('SGD: Final loss ='+str(loss.item()))
fseq[N_iteration] = loss.detach()
from matplotlib.pyplot import semilogy
semilogy(range(0,N_iteration+1),fseq,'r-')

# Adam
x = torch.ones((d,), requires_grad=True)
optimizer_Adam_001 = torch.optim.Adam( [x] , lr=0.01 )
for n in range(N_iteration):
    optimizer_Adam_001.zero_grad() # 将梯度重置为0
    loss = f(x)
    fseq[n] = loss.detach() # 此时fseq[n]存下的是一个“干净”的值，不包括计算图
    loss.backward() # 反向传播（计算 loss 关于 x 的梯度）
    optimizer_Adam_001.step() # 更新 x
loss = f(x)
print('Adam: Final loss ='+str(loss.item()))
fseq[N_iteration] = loss.detach()
semilogy(range(0,N_iteration+1),fseq,'b-')

# RMSProp
x = torch.ones((d,), requires_grad=True)
optimizer_RMSProp_001 = torch.optim.RMSprop( [x] , lr=0.01 )
for n in range(N_iteration):
    optimizer_RMSProp_001.zero_grad() # 将梯度重置为0
    loss = f(x)
    fseq[n] = loss.detach() # 此时fseq[n]存下的是一个“干净”的值，不包括计算图
    loss.backward() # 反向传播（计算 loss 关于 x 的梯度）
    optimizer_RMSProp_001.step() # 更新 x
loss = f(x)
print('RMSProp: Final loss ='+str(loss.item()))
fseq[N_iteration] = loss.detach()
semilogy(range(0,N_iteration+1),fseq,'k-')