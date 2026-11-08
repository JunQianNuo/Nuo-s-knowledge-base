---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
---
# MPI点对点消息匹配与接收容量

Send/Recv的buf、count、datatype描述本地数据地址、元素数和类型；发送dest、接收source、tag、comm约定消息选择。信封匹配看目的、来源、标签、上下文；类型兼容与容量足够是正确存放的额外条件，datatype不参与信封匹配。接收count是最大容量，发3收5仅写前三位，发3收2产生截断错误。Status记录实际来源和标签，Get_count查实际元素数；ANY_SOURCE/ANY_TAG扩大选择，不保证最小rank优先，也无任意通信器通配。
