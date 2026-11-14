# MPI 讲义图片来源与许可说明

本目录中的课程原创文字、代码和自绘示意图适用仓库的 [MIT License](../../LICENSE)。以下第三方图片保留各自的来源、署名和许可条件，不因随课程仓库发布而改用 MIT 许可。讲义及 PDF 课件末尾同时保留图片参考文献。

## 第一讲：第三方图片

| 文件 | 作者与来源 | 许可或复用依据 | 本课程使用方式 |
| --- | --- | --- | --- |
| [nersc-racks-cc0.jpg](01-背景与硬件架构/assets/nersc-racks-cc0.jpg) | Derrick Coetzee，[Front of server racks at NERSC](https://commons.wikimedia.org/wiki/File:Front_of_server_racks_at_NERSC.jpg)，Wikimedia Commons | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | 原照片；课件封面按版式裁切显示 |
| [cray-1-museum-cc-by-sa.jpg](01-背景与硬件架构/assets/cray-1-museum-cc-by-sa.jpg) | Jud McCranie，[Cray-1 at Computer Museum of America](https://commons.wikimedia.org/wiki/File:Cray-1_at_Computer_Museum_of_America.jpg)，Wikimedia Commons | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | 照片未修改，保留作者与许可署名 |
| [aspect-2012-fig8-temperature.png](01-背景与硬件架构/assets/aspect-2012-fig8-temperature.png)；[aspect-2012-fig8-partition.png](01-背景与硬件架构/assets/aspect-2012-fig8-partition.png) | Kronbichler, M., Heister, T., & Bangerth, W. (2012). *High accuracy mantle convection simulation through modern numerical methods*. *Geophysical Journal International*, 191(1), 12–29，[正式发表版 Fig. 8](https://academic.oup.com/gji/article/191/1/12/585193) | 按[期刊教学复用说明](https://academic.oup.com/gji/pages/rights_and_new_business_development)在完整注明出处的条件下用于教学；不宣称图像为 MIT 或其他开放许可 | 两个原图面板从[作者公开稿](https://www.sci.utah.edu/~heister/preprints/mantle_conv.pdf)第 15 页 Fig. 6 无改动提取，对应正式发表版 Fig. 8；完整提取说明见 [ASPECT 原图来源](01-背景与硬件架构/assets/aspect-2012-fig8-SOURCE.md) |

ASPECT 的两幅原图展示同一次三维球壳模拟的温度等值面与处理器网格分区。二维网格分区示意图为本课程自行绘制，与原论文图像分别列明。

## 课程自绘图

- 课程导览 `first-day-hangout/`：PDF 内的学习路线、课程位置和网格分区 TikZ 图，依据任课教师确认的教学安排与 MPI 概念；网格图为原理示意。
- 第一讲：`hardware-hierarchy.svg`、`rank-placement.svg`、`programming-models.svg`、`git-workflow.svg`、`aspect-mesh-partition.svg` 及后者用于排版的 PNG 版本；新增 [image-tiles-parallel.svg](01-背景与硬件架构/assets/image-tiles-parallel.svg) 展示图像分块、本地处理与并行输出。
- 第二讲：`spmd-flow.svg`、`world-ranks.svg`，以及 PDF 课件中的 TikZ 示意图。
- 第三讲：`message-envelope.svg`、`ping-pong.svg`、`ring-token.svg`，以及 PDF 中相应 TikZ 图；依据 MPI 5.0 点对点通信语义与课程源码，分别展示消息信封、往返依赖和逻辑环。核对日期：2026-10-17。

- 第四讲：`midpoint-rule.svg`、`block-partition.svg`、`local-to-global.svg`，以及 PDF 中对应 TikZ 图；分别按实际函数值绘制 N=4 的中点矩形，展示 N=10/P=3 与 N=3/P=4 的分块，以及局部和经点对点通信汇总的逻辑。数学依据为讲义末尾 OpenStax 数值积分章节，通信依据为 MPI 5.0 与本课程源码。核对日期：2026-10-17。

- 第五讲：原有 wait-cycle.svg、request-buffer-lifetime.svg、cmake-workflow.svg，以及新增的 [blocking-recv-timeline.svg](05-死锁与非阻塞通信/assets/blocking-recv-timeline.svg)、[send-first-stall.svg](05-死锁与非阻塞通信/assets/send-first-stall.svg)、[nonblocking-exchange-timeline.svg](05-死锁与非阻塞通信/assets/nonblocking-exchange-timeline.svg)。PDF 中以原创 TikZ 图讲解对应概念：阻塞接收返回、双发送循环等待，以及非阻塞收发与本地请求完成。依据为 [MPI 5.0 标准](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report.pdf)、[Open MPI 的 eager/rendezvous 说明](https://docs.open-mpi.org/en/v5.0.10/mca.html)、[CMake 官方文档](https://cmake.org/cmake/help/v3.20/manual/cmake.1.html)和[本课交换程序](../../examples/mpi/06_exchange/README.md)。时间线表示调用顺序和依赖，不表示实测耗时或所有进程同步；大消息握手不等于将标准发送改为同步模式。构建流程为在 build 中执行 cmake ..、make、ctest。核对日期：2026-10-21。
- 第六讲：[bcast-local-copies.svg](06-广播与归约/assets/bcast-local-copies.svg)、[reduce-root-result.svg](06-广播与归约/assets/reduce-root-result.svg)、[pi-collective-flow.svg](06-广播与归约/assets/pi-collective-flow.svg) 为课程自绘，分别表示广播前后的本地副本、归约到 root 的结果，以及广播输入和局部求和的程序流程。依据 [MPI 5.0 集合通信概述](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node116.htm)、[Broadcast](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node122.htm)、[Reduce](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node132.htm) 和[本课集合通信程序](../../examples/mpi/07_pi_collective/README.md)。PDF 用等义 TikZ 图展示；箭头不规定实际网络算法，行列对齐不表示所有 rank 同步返回。核对日期：2026-10-24。

- 第八讲：[neighbor-halo-copies.svg](08-邻居通信与奇偶排序/assets/neighbor-halo-copies.svg)、[odd-even-partners.svg](08-邻居通信与奇偶排序/assets/odd-even-partners.svg)、[odd-even-trace.svg](08-邻居通信与奇偶排序/assets/odd-even-trace.svg)、[sort-vs-halo.svg](08-邻居通信与奇偶排序/assets/sort-vs-halo.svg) 为课程自绘，展示非周期邻居副本、交替配对、每 rank 一个数的逐阶段排序及网格边界副本。依据 MPI 4.1 Send-Receive/Null Processes、Lang 的奇偶排序说明与 CSC 原课程 halo 说明，详细链接见[本讲图片来源](08-邻居通信与奇偶排序/assets/SOURCE.md)。PDF 以等义 TikZ 图展示。箭头不代表物理网络或全局屏障；−1 是本例初始化的显示占位值。核对日期：2026-10-27。

- 第九讲：[rod-energy-balance.svg](09-热传导方程与数值求解思路/assets/rod-energy-balance.svg)、[slope-vs-curvature.svg](09-热传导方程与数值求解思路/assets/slope-vs-curvature.svg)、[heat-line-profiles.svg](09-热传导方程与数值求解思路/assets/heat-line-profiles.svg)、[heat-plate-fields.svg](09-热传导方程与数值求解思路/assets/heat-plate-fields.svg) 为课程自绘，分别展示控制体能量账本、梯度与曲率、一维温度曲线及二维温度场。科学图按本讲指定的正弦模态解析公式生成，保留相同温标与单位，不作为差分模拟结果。概念依据为 MIT、Stanford 的热方程原课程资料，详见[本讲图片与生成数据说明](09-热传导方程与数值求解思路/assets/SOURCE.md)。核对日期：2026-10-27。

自绘图用于解释课程概念，不表示某一具体机器的实物布线。各目录的 `封面预览.png` 是对应 PDF 封面的预览；课程导览封面为课程自绘，第一讲预览含上述 NERSC 照片。

- 第 9.5 讲：两幅结构与消息图为课程自绘，说明 MPI 作业、调试控制通道和 tag 匹配。依据及用途见[来源记录](09.5-MPI程序调试/assets/SOURCE.md)。核对日期：2026-10-30。

- 第十讲：`stencil.svg` 为三点旧层到下一层的数据依赖示意，PDF 用 TikZ 重绘；`solution-error`、`convergence`、`stability` 为实际 C 程序输出的科学曲线，保留 CSV、参数和生成脚本。模型、公式来源与复现见[本讲来源记录](10-有限差分与串行热传导求解/assets/SOURCE.md)。核对日期：2026-11-01。

- 第十一讲：`domain-partition.svg`、`halo-values.svg`、`time-step.svg`、`gatherv-layout.svg` 为课程原创，展示拥有关系、ghost、时间步顺序及收集位置；`parallel-profile` 与 `refinement` 根据实际 MPI CSV 绘制；`scaling-work`、`scaling-ideal` 为工作量与理想趋势示意，`scaling-measured` 来自固定步数强弱扩展的容器重复测量，保留原始样本与环境记录。数据、运行环境和脚本见[本讲来源记录](11-热传导的MPI并行实现/assets/SOURCE.md)。核对日期：2026-11-01。

## 来源记录

本说明依据随原讲义保留的图片参考文献与 [ASPECT 图像提取记录](01-背景与硬件架构/assets/aspect-2012-fig8-SOURCE.md)整理。原讲义的资料核对日期：第一讲 2026-09-27，第二讲 2026-10-11；新增图像分块案例依据第一讲参考文献第 22 项，核对日期为 2026-10-11。复用第三方图片时，请继续保留署名，并按各自许可或权利方复用条件处理。
