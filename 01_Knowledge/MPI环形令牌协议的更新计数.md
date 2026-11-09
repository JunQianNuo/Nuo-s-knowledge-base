---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
---
# MPI环形令牌协议的更新计数

环形传递的最终值由实际执行的更新次数决定。适用协议为 $P\ge2$ 个进程，rank为 $0,\ldots,P-1$；rank 0发出初值 $a$，每个非零rank收到后加 $d$ 再发送，rank 0最终只接收。

## 路径与结果

rank $r$ 的下一站为 $(r+1)\bmod P$。非零rank从 $r-1$ 接收，rank 0最终从 $P-1$ 接收。只有rank 1至 $P-1$ 更新一次，所以

$$t_{\mathrm{final}}=a+(P-1)d.$$

证明可逐站跟踪：rank 1发出 $a+d$；若rank $r-1$ 发出 $a+(r-1)d$，则rank $r$ 发出 $a+rd$；最后一站给出所需结果。通信有 $P$ 条边，不等于有 $P$ 次更新。

## 实现示意

以下是已初始化MPI并检查 `size>=2` 后的教学片段；整数值须在类型可表示范围内。

```c
int token = a;
if (rank == 0) {
    MPI_Send(&token, 1, MPI_INT, 1, 10, MPI_COMM_WORLD);
    MPI_Recv(&token, 1, MPI_INT, size-1, 10,
             MPI_COMM_WORLD, MPI_STATUS_IGNORE);
} else {
    MPI_Recv(&token, 1, MPI_INT, rank-1, 10,
             MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    token += d;
    MPI_Send(&token, 1, MPI_INT, (rank+1)%size, 10, MPI_COMM_WORLD);
}
```

各进程的token是独立变量；收到消息后才更新。先校验进程数再进入协议，单进程不能直接照搬此“发后收”结构，以免自发送等待匹配接收。

## 例子和边界

课堂初值0、增量1，$P=4,8,16$ 的预期分别是3、7、15。若 $P=6,a=5,d=-2$，结果为 $5+5(-2)=-5$；根进程若收到后也减2，结果为 $-7$，此时协议已改变，更新次数是 $P$。

先预测，再逐进程核对“收、更新、发”的顺序。令牌沿依赖链串行推进，增加进程增加通信跳数，不能把这段示例当成“进程越多必然更快”的证据。
