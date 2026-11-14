# 图示、数值与复现

核对日期：2026-11-01。全部图为课程原创，概念依据集中列于讲义末尾。

| 图 | 数据或依据 | 用途 |
|---|---|---|
| domain-partition.svg | N=11、P=3，10 个内部节点分成 4/3/3 | 拥有关系；物理端点不参加内部更新 |
| halo-values.svg | halo_demo 实际输出；内部值人为取 100+i | 显示 ghost 数值来源，不是热方程初值 |
| time-step.svg | 配套 heat_mpi.c 的循环与 Sendrecv 语义 | 单个 rank 的程序顺序；不表示全局锁步 |
| gatherv-layout.svg | counts=[4,3,3]、displs=[0,4,7]，基址 global+1 | 只收集拥有值；偏移单位为 MPI_DOUBLE 的 extent |
| parallel-profile | N=20、t=10 s、r 请求0.4；实际 MPI P=1/3 CSV | 彩色散点为各 rank 拥有的节点；深色线为同一 MPI 程序单进程基线 |
| refinement | P=3，N=20/40/80，同一终止时刻 | 真实最大误差；虚线是首个误差缩放后的 N^-2 趋势 |

数值采集环境：macOS ARM64、Open MPI 5.0.9、Debug 构建。results.json 保存实际摘要，含单次循环耗时；本次数据用于正确性验证，不作为可扩展性基准。课程容器另独立通过全部测试。

从示例 build 目录运行，例如：

```bash
mpirun -n 3 ./halo_demo > halo-demo.txt
mpirun -n 1 ./heat_mpi 20 10 > solution-N20-P1.csv
mpirun -n 2 ./heat_mpi 20 10 > solution-N20-P2.csv
mpirun -n 3 ./heat_mpi 20 10 > solution-N20-P3.csv
mpirun -n 4 ./heat_mpi 20 10 > solution-N20-P4.csv
mpirun -n 3 ./heat_mpi 40 10 > solution-N40-P3.csv
mpirun -n 3 ./heat_mpi 80 10 > solution-N80-P3.csv
```

将 CSV 保存到本目录后运行 `python3 generate_figures.py`，需要 Matplotlib。脚本读取实际 CSV 并生成结构 SVG 与科学曲线的 SVG/PDF/PNG；Beamer 结构图用等义 TikZ 绘制。

概念来源：

- [MPI_Sendrecv](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man3/MPI_Sendrecv.3.html)
- [MPI_PROC_NULL](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node84.htm)
- [MPI_Gatherv](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man3/MPI_Gatherv.3.html)
- [Demmel：热方程的并行局部性](https://people.eecs.berkeley.edu/~demmel/cs267/lecture17/lecture17.html)

## 强扩展与弱扩展补充

`scaling-work` 为固定步数的工作量示意，格子数仅用于说明概念；`scaling-ideal` 是理想趋势，均非实测。定义依据讲义文末LLNL与EPCC资料。

`scaling-measured` 来自本目录 `scaling-data/raw.csv` 与 `summary.csv`，采用课程容器 `course-mpi-debug:9.5`、GNU 13.3、Open MPI 4.1.6、Release（-O3 -DNDEBUG）。容器可见16个逻辑CPU，当前cgroup的cpu.max为max 100000，未保证宿主机独占或指定绑核；完整资源与编译信息见 `scaling-data/environment.json`。这组数据与上面的macOS Debug正确性数据分别采集，不混用计时基线。

固定r=0.4、M=50000，强扩展K=1600，弱扩展每rank k=400，P=1/2/4。每配置一次排除的预热作业，再测5次。所有36次作业CHECK=PASS，计时只包围每步交换、更新与指针交换。点为5次的中位数，误差线为最小至最大，不是置信区间；虚线按各自P=1中位数画理想趋势。原始命令及程序摘要见 `scaling-data/runs.log`。

复现：在示例的新Release构建目录通过ctest后，运行 `python3 ../run_scaling.py ./heat_mpi`。保存完整scaling-results目录，将其内容复制到scaling-data，再运行 `python3 generate_scaling_figures.py`（绘图需Matplotlib）。这组小问题测量约数毫秒至数十毫秒，有明显并行开销与样本波动，用于教学分析，不作为跨节点集群扩展结论。

物理终止时刻由M dt给出，弱扩展改变N时终止时刻不同。本例固定L，固定物理时间的网格加密会增加步数，不满足固定每rank累计工作量。该推导依据讲义末LeVeque显式稳定性资料。

## 学生绘图流程补充（2026-11-09）

`student-temperature-error.png/pdf` 由课程共用的 `examples/mpi/plot_heat.py` 生成，使用本目录 `solution-N20-P3.csv` 与 `solution-N20-P1.csv`。这两份归档 CSV 与 2026-11-09 课程容器重新运行的 N=20、t=10 s、P=3/P=1 输出逐字节一致。本次绘图文件名为 `solution-p3.csv` 与 `baseline.csv`，因此图内显示这两个标签。

在示例 build 目录中运行：

```bash
mpirun -n 1 ./heat_mpi 20 10 > baseline.csv
mpirun -n 3 ./heat_mpi 20 10 > solution-p3.csv
python3 ../../plot_heat.py solution-p3.csv --ranks 3 --baseline baseline.csv -o ranks.png
python3 ../../plot_heat.py solution-p3.csv --ranks 3 --baseline baseline.csv -o ranks.pdf
```

温度、精确解、分区拥有值和逐点绝对误差均来自真实 CSV，分区颜色使用与 heat_block 相同的商余分块。图中误差峰约 0.0850 K；P=1/P=3 重合是并行一致性证据。

学生自己的性能图由 `11_heat_mpi/plot_scaling.py` 读取自己的 `summary.csv` 生成，三面板依次为强扩展耗时、强扩展加速比和弱扩展耗时。本讲仍保留 2026-11-01 的历史性能图作为已归档读图材料；2026-11-09 的流程验证不替换或伪装成这组历史数值。

## 接口与计时说明修订（2026-11-09）

Gatherv 的 4/3/3 接收表沿用 N=11、P=3 的分块规则，位移 [0,4,7] 相对 `global+1`。屏障的进入先后情形为教学示意，不代表实际同步耗时。计时示例中的 0.0040、0.0050、0.0045 秒为手算假设，用于说明对各 rank 的本地耗时取最大值。

日志示例的 `loop_max_s=0.00482` 来自本目录 `results.json` 中 P=3、N=20、t=10 s 的已归档记录。该记录属于此前 macOS ARM64、Open MPI 5.0.9 的 Debug 功能验证，仅用于解释日志字段，不用于本讲 Release 强弱扩展实验的基线。`slowest` 经 `HeatMPIStats` 的第二个成员 `loop_seconds` 保存，再由 `main.c` 输出为 `loop_max_s`，与配套源程序核对一致。

## Runge–Kutta对照实验（2026-11-09）

`rk-comparison.png/pdf`由配套`rk_extension/plot_compare.py`读取`rk-data/summary.csv`绘制。数据采集于课程容器`course-mpi-debug:9.5`，GNU 13.3、Open MPI 4.1.6、Release（-O3 -DNDEBUG）、16个可见CPU、MPI默认绑定，未请求超额订阅，未保证宿主机CPU独占。环境、可执行文件哈希与参数保存于`rk-data/environment.json`。

两种规模为small：N=1601、M=50000；large：N=160001、M=500。r均为0.4；三种方法euler/rk2/rk4，P=1/2/4。每配置预热1次、采样5次，共108次作业、90个正式样本。全部CHECK=PASS、串行最大差值为0；18条统计由raw.csv独立复算一致。图点表示五次采样中位数，误差线为最小—最大范围；每种方法和规模使用自己的P=1基线。

计时包含各阶段的邻居交换、右端计算、阶段组合与数组交换；不包含初始化、计时前屏障、最终归约/收集、串行核对与输出。两规模的物理终止时刻不同，工作粒度、交换轮数和缓存行为均变化，不解释为同一物理问题的耗时比较。新Euler采用统一阶段框架，不能与原heat_mpi历史耗时拼接基线；旧scaling-data保持原样。

在扩展的build目录运行`python3 ../run_compare.py ./heat_rk`；随后用`python3 ../plot_compare.py rk-results/summary.csv -o rk-results/comparison.png`（或.pdf）重绘。归档目录保留raw.csv、summary.csv、runs.log和environment.json。

`rk-accuracy`保存N=10、P=3、t=10 s的九次精度运行，M=25/50/100，r=0.4/0.2/0.1，三个方法分别运行。每份CSV与.log同名，accuracy-summary.csv保留两种误差和相邻时间误差比。半离散精确解是本例离散正弦特征模的解析演化，用于分离时间误差；模型推导与外部依据见讲义末尾RK参考文献。

## 大规模网格八进程补充（2026-11-09）

第88页的`rk-large-p8.png/pdf`来自新一轮独立测量，图中P=1/2/4/8均重新运行，没有拼接此前`rk-data`的单进程基线。N=160001、内部节点K=160000、M=500、r=0.4，三种方法Euler/RK2/RK4。每配置预热1次、采样5次，共72次作业、60个正式样本、12行统计，全部CHECK=PASS且串行差值为0。计时、取各rank最大值及样本中位数的口径与原实验相同。

镜像`course-mpi-debug:9.5`，GNU 13.3、Open MPI 4.1.6、Release；实测前核对容器16个可用CPU，affinity=0–15，cpu.max为max 100000，未超额订阅。MPI使用默认绑定，宿主机CPU非独占。P=8表示8个MPI进程，不能把它描述为已保证独占8个物理核心。数据与完整环境保存于`rk-large-p8-data`，原`rk-data`和第86/87页的首次测量保留。

在扩展build目录运行`python3 ../run_compare.py ./heat_rk --grids large --processes 1 2 4 8 --output rk-large-p8`；再运行`python3 ../plot_compare.py rk-large-p8/summary.csv -o rk-large-p8/comparison.png`（或.pdf）。脚本按数据中的网格数量绘图，单组为一行两面板。图点是五次中位数，左图误差线为最小—最大范围，右图虚线是理想S=P。
