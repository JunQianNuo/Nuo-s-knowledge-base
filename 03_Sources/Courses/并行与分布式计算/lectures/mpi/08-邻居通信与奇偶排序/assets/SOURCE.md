# 第八讲图示来源

本目录四幅 SVG 均为课程原创示意图，采用课程的 navy/teal/amber 配色。图示数据由配套小例子确定，不是性能测量结果，也不表示 MPI 库内部的网络路由或各进程同时返回。概念依据核对日期为 2026-10-27。

| 文件 | 表达的内容 | 概念依据 |
| --- | --- | --- |
| `neighbor-halo-copies.svg` | 非周期 rank 链；发送自身数值、接收邻居副本；边界处无真实邻居，缓冲区保持初值 | MPI 4.1 §4.2.7、§4.10；CSC MPI 课程的 halo 说明 |
| `odd-even-partners.svg` | P=5 的偶、奇阶段互不重叠配对；端点无伙伴时本阶段保留值 | H. W. Lang 的 Odd-even transposition sort；MPI 4.1 §4.10 |
| `odd-even-trace.svg` | [9,3,7,1] 在四个阶段中的完整轨迹；单个阶段无交换不足以判定有序 | H. W. Lang 的排序网络及 n 阶段证明；数值轨迹为课程手算 |
| `sort-vs-halo.svg` | 排序重分配数值与网格计算保存邻居副本的区别 | H. W. Lang 的比较交换；CSC MPI 课程的 halo 说明 |

## 参考资料

1. MPI Forum. *MPI 4.1*, §4.2.7 “Blocking Send-Receive”。发送与接收组合、避免链式交换的循环依赖、独立缓冲区。<https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node62.htm>
2. MPI Forum. *MPI 4.1*, §4.10 “Null MPI Processes”。`MPI_PROC_NULL` 用于边界；空来源接收不修改缓冲区。<https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node84.htm>
3. H. W. Lang. *Odd-even transposition sort*。交替邻接比较及 n 阶段正确性证明。<https://www.hwlang.de/algorithmen/sortieren/networks/oetsen.htm>
4. CSC – IT Center for Science. *MPI introduction: Heat equation solver in parallel with MPI*。边界数据保存在 ghost layers，非周期外端点只有一个邻居。<https://github.com/csc-training/mpi-introduction/blob/main/heat-equation/README.md>

图形布局、文字与数值示例为课程自绘，适用课程仓库 MIT License；未复制外部图版。
