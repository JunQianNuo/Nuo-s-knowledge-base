---
schema_version: 2
type: method
time: '2026-11-15T09:08:24+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-11-09-第20节-MPI并行计算技术授课]]'
---

# MPI不等长数组的Gatherv拼接

任务：把各rank拥有的不等长连续数据按全局顺序放入root数组。输入为每rank内部数组、长度$m_p$，以及root约定的布局；输出是拼接结果。所有成员参加同一通信器、同一root的对应集合操作，类型签名相容，root接收空间足够且各接收区不重叠。

1. root建立`recvcounts[p]=m_p`。
2. 紧凑拼接时设`displs[0]=0`，后续位移为前面长度之和。
3. 各rank只发送拥有的内部值，不发送ghost。
4. 检查长度总和、首尾位置、非整除分块与已知值序列。

```c
MPI_Gatherv(&old[1],m,MPI_DOUBLE,
            gathered,recvcounts,displs,MPI_DOUBLE,0,comm);
```

这里`old`含两侧ghost，内部为下标1至$m$。root的数组参数需已正确建立；示意不等于完整教师源码。普通`MPI_Gather`不能直接用同一count表示每rank不同长度。

例如10个内部值分为$(4,3,3)$，紧凑长度10数组的位移为$(0,4,7)$。若接收区包含全局物理端点，内部从下标1开始，位移改为$(1,5,8)$，端点另填。混用两种布局会错位；把$m+2$全部发送会重复邻居未知量并混入边界。

`displs`按接收类型的extent计量，普通`MPI_DOUBLE`可理解为元素偏移，不是字节偏移。root内存可能成为大规模汇总限制；本卡不宣称该方案必然加速。[Open MPI接口语义](https://docs.open-mpi.org/en/v5.0.7/man-openmpi/man3/MPI_Gatherv.3.html)。
