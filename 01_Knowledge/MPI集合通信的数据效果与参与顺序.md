---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI集合通信的数据效果与参与顺序

Bcast把root数据复制为各进程本地副本；Reduce把成员贡献逐元素按运算合并到root；Scatter分发不同分块；Gather按rank拼接，区别于数值排序或归约。基本示例count是每rank元素数，Reduce返回值是错误码，root贡献已含其中。所有成员按一致调用次序、root及兼容类型参与，不能仅root调用或缺成员后用Recv补齐。阻塞集合完成提供本地保证，通常不等于所有成员同时到达返回的屏障；集合通信不会把普通变量变共享。
