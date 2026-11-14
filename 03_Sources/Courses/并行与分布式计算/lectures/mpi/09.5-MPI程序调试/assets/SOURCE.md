# 图示来源

两幅 SVG 为课程自绘，首次核对日期为 2026-10-30。2026-11-02 修订的课件另用 TikZ 绘制断点和 CALL STACK 操作示意。B、C 的源码行与变量取自配套程序及课程容器内的实际调试观测。

- debug-topology.svg：一个 Open MPI 作业、两条 GDB/gdbserver 控制通道。实线为启动关系，虚线为调试控制；底部为应用 MPI 消息。
- message-evidence.svg：正常请求/回复与 tag 不匹配的对照。箭头表示消息意图，叉号表示无法匹配；不表示实测时间。

概念依据：

- [VS Code：Debug code](https://code.visualstudio.com/docs/debugtest/debugging)
- [VS Code：Configure debugging](https://code.visualstudio.com/docs/debugtest/debugging-configuration)
- [GNU GDB：Using gdbserver](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Server.html)
- [Open MPI 5.0.x：Serial Debuggers](https://docs.open-mpi.org/en/v5.0.x/app-debug/serial-debug.html)
- [Open MPI 5.0.x：Environment variables](https://docs.open-mpi.org/en/v5.0.x/tuning-apps/environment-var.html)
- [Open MPI 5.0.x：MPI_Ssend](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man3/MPI_Ssend.3.html)
- [Open MPI 5.0.x：MPI_Recv](https://docs.open-mpi.org/en/v5.0.x/man-openmpi/man3/MPI_Recv.3.html)

配色 navy/teal/amber 沿用课程；字体使用系统中文无衬线字体。图不是 VS Code 截图或性能测量结果。
