---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-23-第8节-OpenMP并行计算编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-28-第9节-缺少逐字稿]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-30-第10节-OpenMP并行编程培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-10-第11节-OpenMP并行编程与作业布置课程]]'
---
# OpenMP循环分工与归约

确认各迭代无会改变语义的数据依赖，再用parallel for分工；手动循环可令tid处理tid、tid+P等同余指标，核对覆盖且无重复。累加用每线程局部和后归并或reduction(+:sum)，避免共享sum直接竞争。critical每线程末尾一次通常优于每项加锁。collapse合并规范嵌套迭代空间，适合外层过少，仍须检查依赖和所用OpenMP版本约束；嵌套创建线程组可能过量，应测量验证。
