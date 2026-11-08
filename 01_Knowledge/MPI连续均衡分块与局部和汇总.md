---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
---
# MPI连续均衡分块与局部和汇总

N=qP+s，0≤s<P，rank r取count=q+1_{r<s}、begin=rq+min(r,s)、end=begin+count，使用半开区间[begin,end)。检查首尾0与N、相邻连续、合法端点、数量和N、最大负载差≤1。空块局部和0但仍参与通信。各rank算局部S_r，root把自身贡献加一次并接收或Reduce合并，最终归一化只除N一次；不向自身多发消息。输入合法性与N先统一，使全部进程选择一致通信路径。
