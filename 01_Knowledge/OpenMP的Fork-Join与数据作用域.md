---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-21-第7节-Linux命令与OpenMP并行编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-23-第8节-OpenMP并行计算编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-28-第9节-缺少逐字稿]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-30-第10节-OpenMP并行编程培训]]'
---
# OpenMP的Fork-Join与数据作用域

OpenMP面向共享内存，由制导、运行时和环境变量协作。parallel区域让线程团队执行结构化代码，区域结束同步并返回串行阶段。shared访问同位置；private创建独立副本且通常无外部初值；firstprivate复制初值。工作共享循环索引有预定私有属性，临时变量可在循环体定义。共享读写至少一写需分析同步。omp_get_thread_num和omp_get_num_threads查当前团队；请求线程数与实际数可不同，串行区团队数通常1。GCC以-fopenmp启用并用_OPENMP核对。
