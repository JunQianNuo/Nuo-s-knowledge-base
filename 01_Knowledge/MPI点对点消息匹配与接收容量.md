---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
---
# MPI点对点消息匹配与接收容量

MPI接收需要分别回答三个问题：消息能否被选中、数据能否正确存放、调用是否已经完成。把它们分开，才能解释“标签相同却收不到”和“收到消息但数组后面没变”等现象。

## 参数描述本地数据与消息信封

```c
MPI_Send(buf, count, datatype, dest, tag, comm);
MPI_Recv(buf, count, datatype, source, tag, comm, &status);
```

`buf` 是当前进程内存中的起始地址；`count` 是 `datatype` 的元素数，不是字节数。基本类型对应为 `int/MPI_INT`、`double/MPI_DOUBLE`、`char/MPI_CHAR`。标量通常传 `&value`，数组通常传数组名；传地址让MPI访问本地数据，不意味着远端可解引用这个地址。

`dest` 是目标rank，`source` 是允许的来源rank，`tag` 是程序约定的消息类别整数，`comm` 指定通信上下文。tag不提供加密或身份认证；rank也不是固定物理CPU核心。

一条消息被某次接收选中，要求它的目的地是当前进程、上下文相同、来源符合 `source`、标签符合 `tag`。两个通信器即使成员相同，上下文不同也不会混收。datatype不属于信封匹配字段，但正确传输仍要求相容的基本类型序列；不能据此把整数任意当双精度数接收。

## 接收count是容量

对本卡相同基本类型的收发，可以直接比较元素数。发送三项，接收容量五项，仅写入前三项；其余位置保持原值。容量只有两项则发生消息截断错误，并非安全地截取前两项；错误处理器还可能直接终止程序。

例如两进程中，rank 0发送 `{10,20,30}`，rank 1执行：

```c
int values[5] = {-1,-1,-1,-1,-1};
MPI_Status status;
int actual_count;
MPI_Recv(values, 5, MPI_INT, 0, 30, MPI_COMM_WORLD, &status);
MPI_Get_count(&status, MPI_INT, &actual_count);
```

成功后数组为 `(10,20,30,-1,-1)`，`actual_count` 为3。未初始化的剩余位置没有可预测数值。若发送tag为30而接收要求20，这条消息根本不能被该接收选中，不能据此推断调用已完成。

## 状态、通配与返回值

`MPI_Status` 记录接收结果，`status.MPI_SOURCE`、`status.MPI_TAG` 是实际来源与标签；`MPI_Get_count` 查询实际元素数。本卡使用单一基本类型；复杂派生类型的计数还须按相应类型定义解释。

`MPI_ANY_SOURCE` 和 `MPI_ANY_TAG` 分别放宽来源和标签条件。没有“任意通信器”通配；发送目的地仍须合法。多个来源可匹配时，不保证最小rank先到，这不等于所有消息顺序约束都消失。不需要状态时用 `MPI_STATUS_IGNORE`，不要传未初始化指针。

MPI函数的C返回值是错误码，成功常量为 `MPI_SUCCESS`，不是收到的数据，也不要猜成功值固定为1。阻塞完成与远端业务结束的区别见 [[01_Knowledge/MPI阻塞完成与死锁的等待依赖]]。

## 从诊断到验证

先核目的地、来源、tag、上下文，再核类型和容量，然后用状态及实际长度验证。两进程往返还可采用“rank 0发送10；rank 1接收后加一，再发回；rank 0应收到11”的轨迹；若去程tag为10、回程tag为20，则根进程最终状态应为source=1、tag=20、count=1。必须先验证 `size==2`，否则普通 `else` 不一定只代表rank 1。各进程均可在进程数错误时先Finalize再返回错误，由rank 0输出说明。去程和回程不同tag只是清晰的协议约定，不是必须使用不同tag，更不是数值大小决定执行顺序。接收并不会自动打印数据；只接收不输出时，不能仅凭屏幕无结果判定通信失败。

容量与完成语义核对：[Open MPI：MPI_Recv](https://docs.open-mpi.org/en/main/man-openmpi/man3/MPI_Recv.3.html)。数组具体数值是教学示例，不冒充缺失教师源码。
