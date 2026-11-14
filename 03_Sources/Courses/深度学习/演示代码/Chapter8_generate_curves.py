import torch, numpy
import matplotlib.pyplot as plt
import os, time
from IPython.display import display, clear_output

torch.manual_seed(2)
numpy.random.seed(2)
torch.set_default_device('cuda')

# 生成 N 组形成光滑曲线的二维点列，每个 Nt 个点
d = 2
Nt = 120
N = 10000

theta = numpy.linspace(0,2*numpy.pi,Nt+1)
theta = theta[0:Nt]  # 去掉上述 theta 的最后一个元素，因为0和2pi其实是同一个角度
r = numpy.random.uniform(low = 0.1, high = 0.9, size=(N,))
a = numpy.random.uniform(low = 0.1, high = 0.4, size=(N,))
k = numpy.random.randint(low = 2, high = 6, size=(N,))
angle = numpy.random.uniform(low = 0, high = 2*numpy.pi, size=(N,))

points = numpy.zeros((Nt,N,d))
points[:,:,0] = (r+(a*r)*numpy.sin(numpy.outer(theta,k)+angle))*numpy.cos(theta).reshape(-1,1) #.reshape(-1,1) 表示对 numpy.cos(theta) 作转置
points[:,:,1] = (r+(a*r)*numpy.sin(numpy.outer(theta,k)+angle))*numpy.sin(theta).reshape(-1,1) #.reshape(-1,1) 表示对 numpy.cos(theta) 作转置

#for n in range(10):
#    plt.plot(points[:,n,0],points[:,n,1],'.')
#    plt.pause(0.1)
    
# 生成数据集，每一个数据点长这样: feature vector (x1,x2,...,xs), label (x2,x3,...,x_{s+1})
N_train = 10000
s = 20
M = 100

xt_train = torch.zeros(s,N_train,d)
yt_train = torch.zeros(s,N_train,d)
for n in range(N_train):  # 在点列 points[:,n,:] 中截取长度为 s 的片段
    j = numpy.random.randint(0,Nt-s)
    xt_train[:,n,:] = torch.Tensor(points[j:j+s,n,:])
    yt_train[:,n,:] = torch.Tensor(points[j+1:j+s+1,n,:])

# 定义 RNN 类并且建立一个它的对象
# 面向过程编程：一句话一句话从上往下运行
# 面向对象编程：代码里面有 class(类)，而 class 的代码块可以放在任何位置。调用时可以建立多个 class 的对象，提高编程效率
class ElmanRNN(torch.nn.Module):
    def __init__(self,):
        super().__init__()
        self.rnn = torch.nn.RNN(d,M)
        self.output_layer = torch.nn.Linear(M,d)
        self.h0_type = 'zeros';
    def forward(self,xt):
        if self.h0_type == 'zeros':
            h0 = torch.zeros(1, xt.shape[1], M)
        elif self.h0_type == 'ones':
            h0 = torch.ones(1, xt.shape[1], M)
        ht, _ = self.rnn(xt,h0)
        yt = torch.zeros(xt.shape)
        for t in range(xt.shape[0]):
            yt[t,:,:] = self.output_layer(ht[t,:,:])
        return yt
net = ElmanRNN()

# 训练
if os.path.exists('net_para.data'):
    net.load_state_dict(torch.load('net_para.data'))
else:
    N_iteration = 5000
    lrseq = numpy.linspace(1e-3,1e-5,N_iteration)
    optimizer = torch.optim.Adam(net.parameters())
    yt_net = net(xt_train)
    loss = torch.sum((yt_net-yt_train)**2)/N_train
    for n in range(N_iteration):
        for param_group in optimizer.param_groups:
            param_group['lr'] = lrseq[n]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        yt_net = net(xt_train)
        loss = torch.sum((yt_net-yt_train)**2)/N_train
        if n % 500 == 0:
            print('n=%g, loss = %.3e' %(n, loss.item()))
    print('n=%g, loss = %.3e' %(n, loss.item()))
    torch.save(net.state_dict(),'net_para.data') # 第二个参数是保存下来的文件名

# 生成二维曲线 [p0,p1,...,p200]
length = 200
p = torch.zeros(length+1, 1, d)
p[0,:,:] = torch.rand((1,2)) # 相当于曲线的第一个点 p0
for t in range(length):
    all_y = net(p[0:t+1,:,:]) # 将 p0,p1,...,pt 输入RNN, 输出 [y1,...,yt]
    p[t+1,:,:] = all_y[-1,:,:] # 将 yt 赋值给 p[t+1,:,:], 即曲线的第 t 个点

fig, ax = plt.subplots()
ax.set_xlim(-1,2); ax.set_ylim(-1,2);
plt.close(fig)
(line,) = ax.plot([],[],'r.',markersize=1)
xs,ys = [],[]
for t in range(length+1):
    xs.append(p[t,0,0].cpu().detach().numpy());
    ys.append(p[t,0,1].cpu().detach().numpy());
    line.set_data(xs,ys)
    display(fig)
    clear_output(wait=True)
    time.sleep(0.05)
display(fig)

net.h0_type = 'ones'
for t in range(length):
    all_y = net(p[0:t+1,:,:]) # 将 p0,p1,...,pt 输入RNN, 输出 [y1,...,yt]
    p[t+1,:,:] = all_y[-1,:,:] # 将 yt 赋值给 p[t+1,:,:], 即曲线的第 t 个点
(line,) = ax.plot([],[],'b.',markersize=1)
xs,ys = [],[]
for t in range(length+1):
    xs.append(p[t,0,0].cpu().detach().numpy());
    ys.append(p[t,0,1].cpu().detach().numpy());
    line.set_data(xs,ys)
    display(fig)
    clear_output(wait=True)
    time.sleep(0.05)
display(fig)


        