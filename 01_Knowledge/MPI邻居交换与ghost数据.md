---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI邻居交换与ghost数据

线性非周期rank r的邻居为r−1和r+1，越界用MPI_PROC_NULL。预置物理边界所需ghost值，空源接收不会为其填数据。用配对Sendrecv向右发本地边界收左ghost，再反向交换；ghost是邻居数据的本地副本，不覆盖拥有数据。输出可Gather到root按rank核验，成功失败状态再统一传播。分别检查消息方向、标签和缓冲区，以及所有进程正常清理与收尾。
