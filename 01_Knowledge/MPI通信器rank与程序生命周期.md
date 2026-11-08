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
---
# MPI通信器rank与程序生命周期

MPI标准的一种实现是Open MPI。Init后查询Comm_rank/size，在所选通信器内分配任务、通信，最后Finalize。通信器包含成员与匹配上下文；WORLD覆盖作业成员，SELF仅自身且rank0、size1。rank是相对编号，不是CPU核、PID或固定身份。各进程同名变量仍独立，普通赋值不跨进程传播；mpirun -np设进程数，输出先后不保证rank顺序。
