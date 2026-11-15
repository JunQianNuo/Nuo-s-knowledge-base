---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-11-09-第20节-MPI并行计算技术授课]]'
---
# MPI邻居交换与ghost数据

任务是保留本rank拥有的数据，同时取得邻居数据的本地副本，供后续计算或验证。ghost表示这份副本；它不覆盖本地拥有的数据，也不意味着多进程共享同一内存。

## 确定邻居和物理边界

在线性非周期排列中，rank $r$ 的候选邻居为 $r-1,r+1$。不存在的邻居使用 `MPI_PROC_NULL`，不要随意把-1等负数当合法rank：

```c
int left  = rank>0   ? rank-1 : MPI_PROC_NULL;
int right = rank<P-1 ? rank+1 : MPI_PROC_NULL;
```

空源接收不会给缓冲区写入有效邻居数据，因此先将边界ghost置为问题所需的值。为了展示输出可设置明确哨兵值；解物理问题时要按实际边界条件设置，不能把演示哨兵当温度。单rank时两侧都无邻居。

## 两个方向分别对应

下例假定MPI已经初始化、rank和P已取得，`local` 是本rank的一整数，两个ghost已初始化：

```c
MPI_Sendrecv(&local,1,MPI_INT,right,0,
             &left_ghost,1,MPI_INT,left,0,
             comm,MPI_STATUS_IGNORE);
MPI_Sendrecv(&local,1,MPI_INT,left,1,
             &right_ghost,1,MPI_INT,right,1,
             comm,MPI_STATUS_IGNORE);
```

第一次向右发，却是从左收；第二次反向。按数据流同时核对来源、目的地、tag、类型、容量及独立缓冲区。若所有rank都先阻塞Send再Recv，可能构成等待；小消息不能保证内部始终有缓冲。交换组织和完成纪律见 [[01_Knowledge/MPI双向交换与非阻塞缓冲区纪律]]。

## 一个可核验的结果

四rank的local依次为10、11、12、13。若仅用于演示而预置两端ghost为-1，交换后应为：

| rank | left_ghost | local | right_ghost |
|---|---|---|---|
| 0 | -1 | 10 | 11 |
| 1 | 10 | 11 | 12 |
| 2 | 11 | 12 | 13 |
| 3 | 12 | 13 | -1 |

注意local保持原值，内点ghost来自邻居，端点空源不改写预置值。

## 输出、验证与收尾

各rank分别printf没有确定输出次序。把 `(left_ghost,local,right_ghost)` 三整数Gather到root，root分配 $3P$ 个整数后按rank打印，能把展示顺序与通信正确性分开验证。root产生总体成功或失败状态后再广播，使各rank一致收尾；释放动态内存并配对完成MPI初始化与Finalize。

矩形、不规则网格的真实分区可以复杂得多；本方法只处理线性邻居关系，不能由这一示例声称已经完成任意网格分区算法或取得实测加速。

## 多内部节点的halo交换（11月9日补充）

若每rank拥有$m\ge1$个连续内部节点，数组长度为$m+2$，内部下标为$1,\ldots,m$；$0,m+1$只保存邻居旧层值或物理边界，不是本rank拥有的未知量。设偏移$o$，则全局编号$i=o+j$；用$i$初始化坐标，不能把$j$直接当全局编号。

例如区间段数$N=11$、内部节点为1至10、3个rank的内部长度为$(4,3,3)$，偏移为$(0,4,7)$。rank 1的本地下标0至4对应全局4至8；内部值为$100+i$、物理端点20时，该rank交换后应为$(104,105,106,107,108)$。rank 1把首值105发给rank 0后，应写入rank 0的右ghost，即下标5。

```c
/* left/right为相邻rank，不存在时为MPI_PROC_NULL；old长度m+2 */
if (left == MPI_PROC_NULL) old[0] = 20.0;
if (right == MPI_PROC_NULL) old[m+1] = 20.0;
MPI_Sendrecv(&old[1],1,MPI_DOUBLE,left,71,
             &old[m+1],1,MPI_DOUBLE,right,71,comm,MPI_STATUS_IGNORE);
MPI_Sendrecv(&old[m],1,MPI_DOUBLE,right,72,
             &old[0],1,MPI_DOUBLE,left,72,comm,MPI_STATUS_IGNORE);
```

第一轮向左发送首内部值、从右接收至右ghost；第二轮向右发送末内部值、从左接收至左ghost。所有rank采用相同协议。返回是本rank的完成，不是全局同时完成；仍需类型、tag与缓冲区匹配，见[[01_Knowledge/MPI双向交换与非阻塞缓冲区纪律]]。

总内部规模1000万分给100个rank时，每rank约10万内部值，两个ghost的额外存储比例约$2/100000$；这不保证通信耗时可忽略。一维每轮全系统传输标量数量为$O(P)$，不能直接解释成实测时间随$P$线性。二维/三维需交换面或边上的数据；本示意不覆盖空分块$m=0$，也未执行教师工程。
