---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
---
# MPI集合通信的数据效果与参与顺序

集合通信在一个通信器的成员之间共同完成数据操作。本卡讨论组内通信器。选择接口时，先问需要复制相同输入、分发不同数据、拼接结果，还是合并贡献；这些效果不能混淆。

## 四种数据效果

| 操作 | 输入和结果 | 本课基本类型示例中的count |
|---|---|---|
| Bcast | root的一份数据复制到每个成员的本地内存 | 整份广播数据的元素数 |
| Scatter | root数组按rank分成各自的一份 | 每个接收者的一份元素数 |
| Gather | 各rank的数据按rank顺序拼接到root | 每个发送者贡献或被接收的一份元素数 |
| Reduce | 各rank的输入按指定运算逐分量合并，结果给root | 每rank贡献的元素数 |

例如root数组 `(9,3,7,1)` 用每rank一整数的Scatter分给4个rank；直接Gather回来仍是该rank顺序，不会自动变成数值排序。Gather接收区须容纳全部份数；每rank三个整数时root需要 $3P$ 个整数。等长Scatter/Gather的示例不代表任意不等长分发可直接使用同一个count。

## 广播得到的是副本

```c
const int root=0;
int n=(rank==root ? 10:-1);
MPI_Bcast(&n,1,MPI_INT,root,comm);
```

包括root在内的所有成员调用；各自成功返回后本地n为10。count=1表示一个整数，不是一个rank；各进程的地址数值不必相同。后来某rank独自改n不会更新其他副本，输出次序也不由广播排定。

root可改为最后一个rank或其他合法rank，但大家须对本轮root达成一致，且数据要在新root先初始化。改变root不改变rank编号或参与者。

## 归约按位置合并

```c
int local=rank+1, total=0;
MPI_Reduce(&local,&total,1,MPI_INT,MPI_SUM,root,comm);
if (rank==root) {
    /* total 为全局和 */
}
```

4个rank各贡献1、2、3、4，root得到10；8个rank贡献1至8则得到36。root自己的贡献已包含，不能再额外加一次；求和也不会自动除以进程数。函数C返回值是错误码，不能用 `total=MPI_Reduce(...)` 取得和；非root的接收变量不承载本次全局结果。

各rank贡献 $(r+1,10(r+1))$、count=2时，四rank归约得到 $(10,100)$，无论root为0还是3。两个位置分别相加，既不是8个元素拼接，也不是把全部元素求成110。长度2的数组不必是二维矩阵，归约更不是矩阵乘法。操作与类型须构成受支持的组合。

## 一致参与和顺序

同一通信器的成员须参加对应的集合操作，root、数量和类型签名等须满足接口要求；本课基本类型例子采用相同count与datatype。各rank的调用次序一致：不能某rank先Bcast后Reduce，另一rank反过来。只把赋值放在root分支可以，只在root分支调用Bcast不行；不能用普通Recv补齐缺席成员。

成员可以不同时间到达与返回。阻塞集合调用给相应的本地完成保证，通常不是“所有成员已同时返回”的屏障。集合调用无应用指定tag；普通变量不会因参与集合操作变成共享内存。不得让某成员在还需后续集合通信时提前退出；输入和错误路径见 [[01_Knowledge/MPI连续均衡分块与局部和汇总]]。

逻辑数据流不规定内部一定由root逐个直连，也不是性能实测；换成集合接口不能直接断言必然加速。

语义核对：[MPI集合通信](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node116.htm)、[MPI_Bcast](https://docs.open-mpi.org/en/v5.0.10/man-openmpi/man3/MPI_Bcast.3.html)、[MPI_Reduce](https://docs.open-mpi.org/en/v5.0.10/man-openmpi/man3/MPI_Reduce.3.html)。
