# MPI 课程讲义

从硬件与消息传递背景开始，逐步学习 MPI 程序结构、通信和并行数值计算。第一讲之前先阅读课程导览，了解学习计划、目标，以及个人大作业与 PPT 答辩。已发布材料见下表。

| 讲次 | 主要内容 | Markdown 讲义 | 课堂课件 |
| --- | --- | --- | --- |
| 导览 | 后半程课程内容、12 次课计划、学习目标、个人自选大作业与 PPT 答辩 | [阅读导览](first-day-hangout/first-day-hangout.md) | [下载 PDF](first-day-hangout/first-day-hangout.pdf) |
| 01 | 硬件层次、并行计算简史、ASPECT 网格分区实例、Git 与 Pull Request | [阅读讲义](01-背景与硬件架构/讲义.md) | [下载 PDF](01-背景与硬件架构/课件.pdf) |
| 02 | SPMD、初始化与结束、rank、通信域、本地变量与编译运行 | [阅读讲义](02-程序结构与通信域/讲义.md) | [下载 PDF](02-程序结构与通信域/课件.pdf) |
| 03 | Send/Recv、消息匹配、状态与计数、Ping-Pong、环形通信 | [阅读讲义](03-点对点通信与消息匹配/讲义.md) | [下载 PDF](03-点对点通信与消息匹配/课件.pdf) |
| 04 | 中点求积、连续分块、局部汇总、GoogleTest 单元与 MPI 测试 | [阅读讲义](04-数据划分与并行数值积分/讲义.md) | [下载 PDF](04-数据划分与并行数值积分/课件.pdf) |
| 05 | 循环等待、Sendrecv、非阻塞请求与缓冲区、CMake/CTest | [阅读讲义](05-死锁与非阻塞通信/讲义.md) | [下载 PDF](05-死锁与非阻塞通信/课件.pdf) |
| 06 | 广播、归约、root、集合调用顺序与 π 积分 | [阅读讲义](06-广播与归约/讲义.md) | [下载 PDF](06-广播与归约/课件.pdf) |
| 08 | 非周期邻居、Sendrecv、PROC_NULL、奇偶排序与结果验证 | [阅读讲义](08-邻居通信与奇偶排序/讲义.md) | [下载 PDF](08-邻居通信与奇偶排序/课件.pdf) |
| 09 | 热流与守恒、热方程、初边值条件、解析基准与数值求解思路 | [阅读讲义](09-热传导方程与数值求解思路/讲义.md) | [下载 PDF](09-热传导方程与数值求解思路/课件.pdf) |
| 09.5 | 断点、变量与调用栈、双 rank 调试、消息错误与循环等待 | [阅读讲义](09.5-MPI程序调试/讲义.md) | [下载 PDF](09.5-MPI程序调试/课件.pdf) |
| 10 | 中心差分、显式时间推进、稳定性、串行求解与误差验证 | [阅读讲义](10-有限差分与串行热传导求解/讲义.md) | [下载 PDF](10-有限差分与串行热传导求解/课件.pdf) |
| 11 | 域分解、幽灵节点、邻居交换、并行验证、加速比与强弱扩展 | [阅读讲义](11-热传导的MPI并行实现/讲义.md) | [下载 PDF](11-热传导的MPI并行实现/课件.pdf) |

## 配套实验

- 第一讲：[Git 提交与 Pull Request 实验](../../git-practice/README.md)，[Git 与 SSH 配置入门](../../docs/git-入门.md)。
- 第二讲：[MPI 示例目录](../../examples/mpi/README.md)，包含 Hello World 和进程本地变量示例；[第一个 MPI 程序与 Makefile 详解](../../examples/mpi/01_hello_world/程序详解.md) 补充实操所需基础。
- 第三讲：[Ping-Pong](../../examples/mpi/03_ping_pong/README.md) 和 [环形令牌](../../examples/mpi/04_ring_token/README.md)，含 Makefile、程序详解、练习与参考答案。
- 第四讲：[并行数值积分与测试](../../examples/mpi/05_pi_send_recv/README.md)，[程序详解](../../examples/mpi/05_pi_send_recv/程序详解.md) 与 [GoogleTest 入门](../../docs/googletest-入门.md)。
- 第五讲：[两个进程交换数组](../../examples/mpi/06_exchange/README.md)，[程序详解](../../examples/mpi/06_exchange/程序详解.md) 与 [CMake 入门](../../docs/cmake-入门.md)。
- 第六讲：[广播与归约程序](../../examples/mpi/07_pi_collective/README.md) 与 [程序详解](../../examples/mpi/07_pi_collective/程序详解.md)，包括完整短程序、集合通信积分和多进程测试。
- 第八讲：[邻居通信与奇偶排序](../../examples/mpi/08_odd_even/README.md) 与 [程序详解](../../examples/mpi/08_odd_even/程序详解.md)，包括左右副本、逐阶段轨迹和 GoogleTest/CTest。
- 第九讲：[热传导解析基准](../../examples/mpi/09_heat_reference/README.md) 与 [程序详解](../../examples/mpi/09_heat_reference/程序详解.md)，先观察一维/二维温度场并验证初边值和衰减规律。
- 第 9.5 讲：[VS Code 多进程调试实验](../../examples/mpi/09a_mpi_debug/README.md)与[程序详解](../../examples/mpi/09a_mpi_debug/程序详解.md)，从课程根目录启动双会话，先看接收数组，再核对回复 46。
- 第十讲：[串行热传导求解](../../examples/mpi/10_heat_serial/README.md) 与 [程序详解](../../examples/mpi/10_heat_serial/程序详解.md)，含稳定性演示、加密实验与故障注入练习。
- 第十一讲：[MPI 热传导与 halo 实验](../../examples/mpi/11_heat_mpi/README.md) 与 [程序详解](../../examples/mpi/11_heat_mpi/程序详解.md)，含不均匀分块、编号值交换、多进程回归、加速比、强扩展与固定步数弱扩展。
- 运行前：[课程环境搭建](../../docs/setup-docker.md)，[环境自检脚本](../../scripts/check_env.sh)。

前四讲的示例（01–05）保留各自的 Makefile；进入对应目录后运行 `make`、`make run`、`make clean`；Ping-Pong 使用 `NP=2`，环形示例默认 `NP=4`。第四讲新增 `make test`、`make test-mpi` 和 `make check`。第五讲及后续新示例使用 CMake/CTest：先在示例目录创建并进入 `build`，再执行 `cmake ..` 配置、`make` 编译和 `ctest` 测试；`make exchange_demo` 可单独构建第五讲演示目标。具体任务、MPI 启动命令与观察问题见讲义和示例 README。

## 文件与图片

各讲目录包含 `讲义.md`、`课件.pdf`、`封面预览.png` 及 `assets/`。课程导览位于 `first-day-hangout/`，使用同名 MD、PDF 与封面预览。复制或移动时，请保留整讲目录，以便 Markdown 中的相对路径插图正常显示。

Markdown 讲义可在线阅读，PDF 课件可直接阅读或投影。

讲义与课件将参考文献集中列于末尾。第三方图片保留其原有许可或教学复用条件，详情见[图片来源与许可说明](ASSET-SOURCES.md)；课程原创代码、讲义文字和自绘图适用仓库的 [MIT License](../../LICENSE)。
