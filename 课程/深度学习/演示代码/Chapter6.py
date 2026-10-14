import torch, numpy
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import time

torch.manual_seed(2) 
torch.set_default_device('cuda')

N_train = 10000
N_test = 1000
d = 2
J = 4

# 生成训练集/测试集
x_train = torch.normal(mean=torch.zeros((N_train,d)),std=torch.ones((N_train,d)))
y_train = torch.zeros((N_train,))
logic = (x_train[:,0]>=0) & (x_train[:,1]>=0)
y_train[logic] = 1
logic = (x_train[:,0]<0) & (x_train[:,1]>=0)
y_train[logic] = 2
logic = (x_train[:,0]<0) & (x_train[:,1]<0)
y_train[logic] = 3
logic = (x_train[:,0]>=0) & (x_train[:,1]<0)
y_train[logic] = 4

x_test = torch.normal(mean=torch.zeros((N_test,d)),std=torch.ones((N_test,d)))
y_test = torch.zeros((N_test,))
logic = (x_test[:,0]>=0) & (x_test[:,1]>=0)
y_test[logic] = 1
logic = (x_test[:,0]<0) & (x_test[:,1]>=0)
y_test[logic] = 2
logic = (x_test[:,0]<0) & (x_test[:,1]<0)
y_test[logic] = 3
logic = (x_test[:,0]>=0) & (x_test[:,1]<0)
y_test[logic] = 4


# 定义全连接网络
M = 10
L = 3 # 3 or 5
class my_net_class(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear1 = nn.Linear(d, M)
        self.linear2 = nn.Linear(M, M)
        if L == 3:
            self.linear3 = nn.Linear(M, J)
        elif L == 5:
            self.linear3 = nn.Linear(M, M)
            self.linear4 = nn.Linear(M, M)
            self.linear5 = nn.Linear(M, J)
    def forward(self, x):
        if L == 3:
            x = F.relu(self.linear1(x))
            x = F.relu(self.linear2(x))
            x = F.softmax(self.linear3(x), dim=1)
        elif L == 5:
            x = F.relu(self.linear1(x))
            x = F.relu(self.linear2(x))
            x = F.relu(self.linear3(x))
            x = F.relu(self.linear4(x))
            x = F.softmax(self.linear5(x), dim=1)
        return x
net = my_net_class()
      
# 定义标签概率向量和损失函数
v_train = torch.zeros((N_train,J))
for j in range(1,J+1):
    v_train[y_train==j,j-1] = 1
loss = -torch.sum(torch.sum(v_train*torch.log(net(x_train)), dim=1))/N_train

# 训练及测试
N_iteration = 5000
lrseq = numpy.linspace(1e-4,1e-6,N_iteration)
optimizer = torch.optim.Adam(net.parameters())
print('Depth = %g, Width = %g' %(L,M))
for n in range(N_iteration):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lrseq[n]
    optimizer.zero_grad()
    loss.backward() 
    optimizer.step()  
    loss = -torch.sum(torch.sum(v_train*torch.log(net(x_train)), dim=1))/N_train
    net_classification = torch.max(net(x_test),dim=1).indices+1
    accuracy = torch.sum(net_classification == y_test)/N_test
    if n%100 == 0:
        print('n = %g, loss = %.3e，test_accuracy = %.3g ' %(n, loss.item(), accuracy))
        logic = (net_classification==1)
        plt.plot(x_test[logic,0].cpu().detach().numpy(),x_test[logic,1].cpu().detach().numpy(),'.', color = 'red', markersize=1)    
        logic = (net_classification==2)
        plt.plot(x_test[logic,0].cpu().detach().numpy(),x_test[logic,1].cpu().detach().numpy(),'.', color = 'green', markersize=1)     
        logic = (net_classification==3)
        plt.plot(x_test[logic,0].cpu().detach().numpy(),x_test[logic,1].cpu().detach().numpy(),'.', color = 'blue', markersize=1)      
        logic = (net_classification==4)
        plt.plot(x_test[logic,0].cpu().detach().numpy(),x_test[logic,1].cpu().detach().numpy(),'.', color = 'orange', markersize=1)       
        plt.show()
        time.sleep(0.5)
        plt.clf()
        
           
print('Final loss = %.3e，test_accuracy = %.3g  ' %(loss.item(), accuracy))

