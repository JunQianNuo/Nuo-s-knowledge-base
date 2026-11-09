---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI双向交换与非阻塞缓冲区纪律

本方法让两个MPI进程互换各自的数组，并判断何时可以使用结果。前提是通信器恰有两个进程，rank为0、1，对端 `peer=1-rank`；类型相容、接收容量足够，来源、目标、tag和上下文正确对应。

## 先写预期，再选交换组织方式

可令rank $r$ 的发送数组为

$$s_r[i]=10\,000\,000r+i,\qquad 0\le i<n.$$

交换成功后，应逐项检查接收区等于 $s_{1-r}[i]$。例如 $n=4$，rank 0收到10000000至10000003，rank 1收到0至3；$n$ 是数组长度，不是进程数，不能只核对首元素或只检查rank 0。

有三种组织方式：互补阻塞顺序中rank 0先发后收、rank 1先收后发；或者用Sendrecv；或者先投递全部所需非阻塞操作，再确认完成。它们都解除“两边先等待发送”的依赖，但不免除消息匹配责任。推广到环或更复杂拓扑须重新分析依赖。

## Sendrecv：把配对收发放在一次调用中

```c
MPI_Sendrecv(sendbuf, n, MPI_INT, peer, 20,
             recvbuf, n, MPI_INT, peer, 20,
             comm, MPI_STATUS_IGNORE);
```

前五项描述发送，后五项描述接收，最后给通信器和接收状态。它仍是阻塞接口，收发缓冲区应不重叠；原地交换须采用相应接口。它能处理组合收发的调度依赖，不能修复错误tag、缺少对端或容量不足。

## 非阻塞：发起和完成分开

```c
MPI_Request requests[2];
MPI_Irecv(recvbuf, n, MPI_INT, peer, 20, comm, &requests[0]);
MPI_Isend(sendbuf, n, MPI_INT, peer, 20, comm, &requests[1]);
/* 只做不依赖接收结果、也不冲突的独立工作。 */
MPI_Waitall(2, requests, MPI_STATUSES_IGNORE);
/* 成功完成后才能使用recvbuf，改写或释放sendbuf。 */
```

请求句柄跟踪操作，不是消息数据。`Irecv/Isend` 返回仅表示发起；Waitall的2是本rank列出的请求数，不是数组长度或进程数，也不是全局屏障。这里的普通非持久请求成功完成后释放，相应句柄变成 `MPI_REQUEST_NULL`。

| 尚未完成的操作 | 必须保持的内存纪律 |
|---|---|
| 发送 | 缓冲区始终有效，不能改写或释放；可读取 |
| 接收 | 缓冲区始终有效，不能提前读取、改写或释放 |

不重叠且无数据依赖的其他数组可以计算；实际是否隐藏通信代价取决于实现、硬件和工作安排，不保证自动加速。

## 两个常见失败

只 `Wait` 发送请求，不保证接收完成，不能随后读取接收数组。若两项操作都已投递，分别Wait各自请求也可行；单个Wait并非天然错误，错误是把它当作所有操作的完成保证。

双方写成“Isend、立即Wait发送、再Irecv”，则匹配接收尚未投递，仍可能重建循环等待。正确顺序要保证解除依赖所需的操作已发起。

错误版本可能偶尔输出正确，也可能错数或失败；一次运行现象不代替接口保证。以不同数组长度、全部元素、两边状态及受控超时验证；完整教师工程未取得时只保留预期，不编造PASS。

官方核对：[MPI_Sendrecv](https://docs.open-mpi.org/en/main/man-openmpi/man3/MPI_Sendrecv.3.html)、[MPI_Waitall](https://docs.open-mpi.org/en/main/man-openmpi/man3/MPI_Waitall.3.html)。
