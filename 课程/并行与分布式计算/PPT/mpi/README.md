# MPI 课程讲义

从硬件与消息传递背景开始，逐步学习 MPI 程序结构、通信和并行数值计算。第一讲之前先阅读课程导览，了解学习计划、目标，以及个人大作业与 PPT 答辩。已发布导览与以下两讲。

| 讲次 | 主要内容 | Markdown 讲义 | 课堂课件 |
| --- | --- | --- | --- |
| 导览 | 后半程课程内容、12 次课计划、学习目标、个人自选大作业与 PPT 答辩 | [阅读导览](first-day-hangout/first-day-hangout.md) | [下载 PDF](first-day-hangout/first-day-hangout.pdf) |
| 01 | 硬件层次、并行计算简史、ASPECT 网格分区实例、Git 与 Pull Request | [阅读讲义](01-背景与硬件架构/讲义.md) | [下载 PDF](01-背景与硬件架构/课件.pdf) |
| 02 | SPMD、初始化与结束、rank、通信域、本地变量与编译运行 | [阅读讲义](02-程序结构与通信域/讲义.md) | [下载 PDF](02-程序结构与通信域/课件.pdf) |

## 配套实验

- 第一讲：[Git 提交与 Pull Request 实验](../../git-practice/README.md)，[Git 与 SSH 配置入门](../../docs/git-入门.md)。
- 第二讲：[MPI 示例目录](../../examples/mpi/README.md)，包含 Hello World 和进程本地变量示例；[第一个 MPI 程序与 Makefile 详解](../../examples/mpi/01_hello_world/程序详解.md) 补充实操所需基础。
- 运行前：[课程环境搭建](../../docs/setup-docker.md)，[环境自检脚本](../../scripts/check_env.sh)。

示例程序使用各示例目录内的 Makefile 管理；进入对应目录后运行 `make`、`make run NP=4`、`make clean`。具体任务与观察问题见讲义和示例 README。

## 文件与图片

第一、第二讲目录包含 `讲义.md`、`课件.pdf`、`封面预览.png` 及 `assets/`。课程导览位于 `first-day-hangout/`，使用同名 MD、PDF 与封面预览。复制或移动时，请保留整讲目录，以便 Markdown 中的相对路径插图正常显示。

Markdown 讲义可在线阅读，PDF 课件可直接阅读或投影。

讲义与课件将参考文献集中列于末尾。第三方图片保留其原有许可或教学复用条件，详情见[图片来源与许可说明](ASSET-SOURCES.md)；课程原创代码、讲义文字和自绘图适用仓库的 [MIT License](../../LICENSE)。
