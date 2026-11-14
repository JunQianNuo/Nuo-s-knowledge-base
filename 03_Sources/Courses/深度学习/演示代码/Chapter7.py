import torch, numpy
from torch import nn
import torch.nn.functional as F

torch.manual_seed(2)
torch.set_default_device('cuda')

N_train = 10000
N_test = 1000
d = 8
J = 2
task_ID = 2

# 生成训练集/测试集
if task_ID == 1:
    x_train = 2*torch.rand((N_train,1,d,d))-1  # 每个矩阵的元素在[-1,1]上均匀分布
    y_train = torch.zeros((N_train,))
    for n in range(int(N_train/2)):
        x_train[n,0,:,:] = x_train[n,0,:,:] + x_train[n,0,:,:].t()
        y_train[n] = 1
    y_train[int(N_train/2):N_train] = 2
    
    x_test = 2*torch.rand((N_test,1,d,d))-1  # 每个矩阵的元素在[-1,1]上均匀分布
    y_test = torch.zeros((N_test,))
    for n in range(int(N_test/2)):
        x_test[n,0,:,:] = x_test[n,0,:,:] + x_test[n,0,:,:].t()
        y_test[n] = 1
    y_test[int(N_test/2):N_test] = 2
elif task_ID == 2:
    x_train = 2*torch.rand((N_train,1,d,d))-1 
    y_train = torch.zeros((N_train,))
    for n in range(N_train):
        x_train[n,0,:,:] = x_train[n,0,:,:] + x_train[n,0,:,:].t()
        if numpy.min(numpy.linalg.eig(x_train[n,0,:,:].cpu().detach().numpy())[0])>-3.6:
            y_train[n] = 1
        else:
            y_train[n] = 2
    x_test = 2*torch.rand((N_test,1,d,d))-1 
    y_test = torch.zeros((N_test,))
    for n in range(N_test):
        x_test[n,0,:,:] = x_test[n,0,:,:] + x_test[n,0,:,:].t()
        if numpy.min(numpy.linalg.eig(x_test[n,0,:,:].cpu().detach().numpy())[0])>-3.6:
            y_test[n] = 1
        else:
            y_test[n] = 2

# 定义神经网络

N_channel = 10
conv1_kernel_size = 3
conv2_kernel_size = 3
pool_kernel_size = 2
width = 20

class my_net_class(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(1,N_channel,conv1_kernel_size,stride=1,padding='same')  # input:1@8X8, output:10@8X8
        self.pool1 = nn.AvgPool2d(pool_kernel_size,stride=pool_kernel_size,padding=0)   # input:10@8X8, output:10@4X4
        self.conv2 = nn.Conv2d(N_channel,N_channel,conv2_kernel_size,stride=1,padding='same')  # input:10@4X4, output:10@4X4
        self.linear1 = nn.Linear(N_channel*int(d/pool_kernel_size)*int(d/pool_kernel_size),width)  # input:160, output:20
        self.linear2 = nn.Linear(width,J)  # input:160, output:20
    def forward(self, x): # x 为数据集的特征部分(即多个数据点的特征)，即 x 是 4 维张量 (N,1,d,d)
        x = F.relu(self.conv1(x)) # self.conv1(x) 作用的就是 X*K+b, 即互相关运算
        x = self.pool1(x)
        x = F.relu(self.conv2(x))  # x 的尺寸是 [N,N_channel,d/pool_kernel_size,d/pool_kernel_size]  
        x = torch.flatten(x,1,3) # 通过 flatten(x,1,3) 把 x 的尺寸从 [N,10,4,4] 变成了 [N,160]
        x = F.relu(self.linear1(x)) # x 的尺寸是 [N,20]
        x = F.softmax(self.linear2(x),dim=1) # softmax(self.linear2(x),dim=1) 把 x 的尺寸从 [N,20] 变成了 [N,2].
        return x
net = my_net_class()

# 定义标签概率向量
v_train = torch.zeros((N_train,J))
for j in range(1,J+1):
    v_train[y_train == j,j-1] = 1  
    # v_train 中 [1,0] 的行对应 y_train 取值为 1 的那些元素
    # v_train 中 [0,1] 的行对应 y_train 取值为 2 的那些元素

# 训练及测试
N_iteration = 5000
lrseq = numpy.linspace(1e-4,1e-6,N_iteration)
optimizer = torch.optim.Adam(net.parameters())
print('N_channel = %g, width = %g' %(N_channel,width))
loss = -torch.mean(torch.sum(v_train*torch.log(net(x_train)),dim=1))
for n in range(N_iteration):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lrseq[n]
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    loss = -torch.mean(torch.sum(v_train*torch.log(net(x_train)),dim=1))
    net_classification = torch.max(net(x_test), dim=1).indices+1
    accuracy = torch.sum(net_classification==y_test)/N_test
    if n % int(N_iteration/100) == 0:
        print('n=%g, loss = %.3e, test_accuracy = %.3g ' %(n,loss.item(),accuracy))
print('n=%g, loss = %.3e, test_accuracy = %.3g ' %(n,loss.item(),accuracy))
  