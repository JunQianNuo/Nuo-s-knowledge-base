---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-23-第8节-OpenMP并行计算编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-14-第13节-Git与MPI编程教学]]'
---
# Makefile依赖目标与自动变量

Make规则左侧目标、右侧依赖，配方通常以真实Tab起行。变量固化编译器和选项，?=仅在未定义时给默认值；$@是当前目标，$<是首个依赖。all可构建默认目标，run先依赖可执行文件再启动，clean只清生成物；.PHONY避免伪目标受同名文件影响。MPI编译使用带头文件链接配置的mpicc驱动，运行由mpirun启动，各自职责不同。
