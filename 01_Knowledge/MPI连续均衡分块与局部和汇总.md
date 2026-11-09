---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI连续均衡分块与局部和汇总

任务是把 $N$ 个指标 $0,\ldots,N-1$ 分给 $P$ 个进程，保证每项恰算一次、负载最多差一项，再把局部结果合并。要求 $N>0,P\ge1$，rank $r\in\{0,\ldots,P-1\}$，各进程使用相同输入和通信器；整数类型能容纳索引。

## 连续分块的推导

作带余除法 $N=qP+s$，其中 $q=\lfloor N/P\rfloor$、$0\le s<P$。先给每个rank分 $q$ 项，再给前 $s$ 个rank各一项：

$$
c_r=q+\mathbf1_{\{r<s\}},\qquad
b_r=rq+\min(r,s),\qquad e_r=b_r+c_r.
$$

$c_r$ 是项数，$b_r,e_r$ 是指标端点，循环使用半开区间 $[b_r,e_r)$。起点中的 $\min(r,s)$ 正是前面 $r$ 个进程多领的总项数；故相邻块首尾相接，右端点不算，既不重复也不遗漏。

```c
int q=N/P, s=N%P;
int begin=rank*q + (rank<s ? rank:s);
int end=begin + q + (rank<s);
double local=0.0;
for (int i=begin; i<end; ++i) {
    double x=(i+0.5)/(double)N;
    local += 4.0/(1.0+x*x);
}
```

这里begin/end是小区间的编号，不是积分实变量端点；局部和尚未乘步长。

## 例子与结构检查

| $N,P$ | 按rank的区间 | 长度 |
|---|---|---|
| $10,3$ | $[0,4),[4,7),[7,10)$ | $4,3,3$ |
| $11,4$ | $[0,3),[3,6),[6,9),[9,11)$ | $3,3,3,2$ |
| $3,4$ | $[0,1),[1,2),[2,3),[3,3)$ | $1,1,1,0$ |
| $N,1$ | $[0,N)$ | $N$ |

检查首块起于0、末块止于 $N$，每块满足 $0\le b_r\le e_r\le N$，相邻满足 $e_r=b_{r+1}$，长度总和为 $N$，最大与最小长度之差不超过1。空块局部和是加法单位元0，仍按协议通信，不能提前消失。

## 从局部和得到全局和

对 $S_r=\sum_{i=b_r}^{e_r-1}f(x_i)$，积分近似为 $Q_N=N^{-1}\sum_rS_r$。点对点版root从自身局部和开始，依次接收其他rank贡献：

```c
if (rank==0) {
    double total=local;
    for (int src=1; src<P; ++src) {
        double part;
        MPI_Recv(&part,1,MPI_DOUBLE,src,10,comm,MPI_STATUS_IGNORE);
        total+=part;
    }
    /* Q_N = total/(double)N */
} else {
    MPI_Send(&local,1,MPI_DOUBLE,0,10,comm);
}
```

root贡献只加入一次，不额外向自身发送；真正自发送仍有匹配和等待语义。依次收取是清楚的教学实现，但root可能成为瓶颈；正确、并行、加速须分别论证。

集合版让所有rank调用 `MPI_Reduce(&local,&total,1,MPI_DOUBLE,MPI_SUM,root,comm)`，仅root最后除 $N$ 一次。不要除以进程数，也不要局部已除 $N$ 后再重复归一化。

## 统一输入和退出路径

root解析输入后，先由所有rank广播有效标志valid；无效则共同结束，有效再广播 $N$、计算并归约。valid只是解析结果，不是通信可靠性保证。删掉本例有效标志广播可能导致root退出而其他rank继续等待；不能泛化成“删除任意广播必死锁”。$N<P$ 时空任务rank仍参与广播和归约。例如 $N=2,P=4$，分块为 $[0,1),[1,2),[2,2),[2,2)$。

课堂某工程口述允许 $1\le N\le10^7$，是工程参数范围，须以其实际输入检查为准，不当作MPI或分块公式的统一上限。数值精度另见 [[01_Knowledge/复合中点积分的分层数值验证]]。
