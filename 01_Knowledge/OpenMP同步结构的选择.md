---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-30-第10节-OpenMP并行编程培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-10-第11节-OpenMP并行编程与作业布置课程]]'
---
# OpenMP同步结构的选择

更新单一受支持内存位置可用atomic；多步共享不变量用critical或锁；可结合求和用reduction；阶段依赖用barrier。single由某线程执行一次且默认末尾屏障，master由0号线程执行且无隐式屏障；sections每段由团队某线程执行一次，critical则每个遇到的线程依次执行。ordered控制指定片段的迭代顺序；nowait仅在后续不依赖全部结果时移除工作共享隐式屏障。锁需初始化、所有路径释放并销毁，范围过大造成串行化。
