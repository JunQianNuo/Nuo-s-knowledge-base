---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-12-第12节-MPI并行计算与Git版本控制课程宣讲]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-14-第13节-Git与MPI编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI通信器rank与程序生命周期

> 一句话：MPI 进程在指定通信器中用 rank 标识自己；初始化后查询身份和通信，结束前完成通信，再统一结束 MPI 环境。

## 对象与编号

MPI 是消息传递接口标准，Open MPI 是其实现之一。通信器 `MPI_Comm` 包含参与进程组及消息匹配上下文；同一组进程也可用不同上下文隔离通信。

对于大小为 $p$ 的组内通信器，rank 为 $0,\ldots,p-1$，仅相对该通信器有效。它不是 CPU 核号、操作系统 PID、机器号或永久全局身份。

- 在课程使用的 World 初始化模型中，`MPI_COMM_WORLD` 是初始进程的全体通信器。
- `MPI_COMM_SELF` 对每个调用进程只含自身，所以每个进程查询得到 `rank=0`、`size=1`。
- 划分到不同通信器后，进程可在不同组内独立编号和通信；调用时必须传对应通信器。

## 最小程序与运行

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    printf("rank %d of %d\n", rank, size);
    MPI_Finalize();
    return 0;
}
```

```bash
mpicc -std=c11 hello.c -o hello_mpi
mpirun -np 4 ./hello_mpi
```

`mpicc` 封装 MPI 编译和链接配置，`mpirun` 启动进程；`-np 4` 指进程数，不保证四台机器或四个独占核心。`MPI_Comm_rank`、`MPI_Comm_size` 通过指针返回结果，所以要传 `&rank`、`&size`；`MPI_Init` 的 `&argc`、`&argv` 也要符合接口类型。

World 模型下，常规 MPI 调用放在成功初始化后、结束之前。`MPI_Finalize` 不是替程序补齐任意通信的手段：未完成请求和缓冲区生命周期仍需先正确处理，不能把它当成通用屏障使用。课程最小例不涵盖错误恢复或 MPI Sessions 初始化方式。

## 独立内存小例

若每个进程都执行 `int value=10;`，随后仅 `rank==0` 的进程执行 `value=99;`，则只有 0 号进程的本地变量变成 99，其他进程仍是 10。若改用 `MPI_COMM_SELF` 查询再作相同判断，每个进程在自己的 SELF 中都是 0 号，结果会不同。要把一个进程的数据交给其他进程，必须显式通信。

各进程独立调度，终端打印先后不是 rank 顺序，也不能证明执行先后；验证时应检查每条输出的 rank 和数值。任务划分还需兼顾通信量、负载和同步开销，见 [[01_Knowledge/并行算法的数据依赖判定]]。

范围核实：[MPI 4.1 预定义组内通信器](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node181.htm)、[Open MPI 的 MPI_Finalize 说明](https://docs.open-mpi.org/en/main/man-openmpi/man3/MPI_Finalize.3.html)。
