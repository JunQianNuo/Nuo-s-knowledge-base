---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-16-第6节-并行计算与Linux基础讲座]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-21-第7节-Linux命令与OpenMP并行编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
---
# Linux终端文件文本与脚本工作流

> 一句话：先确认文件位置，再用小命令查看和处理数据；把已经逐步验证的命令写成脚本，才能可靠重复执行。

## 理解环境

Linux 内核管理 CPU、内存、设备和进程；Shell 解释用户命令、启动程序并组合输入输出。图形桌面不是内核，服务器没有桌面也能在终端完成开发。

## 在练习目录操作文件

先用 `pwd` 确认当前目录，用 `ls` 或 `ls -l` 检查内容，再执行后续命令。

| 任务 | 示例 | 要核对的语义 |
|---|---|---|
| 切换目录 | `cd demo`、`cd ..` | 相对路径从当前目录解释 |
| 新建 | `mkdir demo`、`touch a.txt` | `touch` 对已存在文件会更新时间戳 |
| 复制 | `cp a.txt b.txt`、`cp -r src dst` | 检查目标是否已存在，避免覆盖 |
| 移动或改名 | `mv old new` | 同时可能改变位置和名称 |
| 软链接 | `ln -s target link` | 保存目标路径；相对目标相对于链接所在目录解释 |
| 定位 | `locate name`、`whereis gcc` | 前者依赖索引，后者定位程序等相关文件 |
| 删除 | `rm file`、`rm -r dir` | 通常不进回收站；先核对准确目标 |

遇到删除、批量移动或通配符时，先打印路径并用 `ls` 复核。不要在位置不确定时执行递归删除。

## 查看、过滤和编辑文本

`cat file` 适合短文件，长文件用 `more` 或 `less` 分页；`head`、`tail` 看开头和结尾；`grep` 按模式筛行，`sort` 排序，`awk` 按字段处理，`sed` 可做流式替换。默认排序受区域设置影响，数字排序通常需指定相应选项。

```bash
grep "error" app.log | sort | head
awk '{print $1}' data.txt
sed 's/old/new/g' input.txt
```

管道把前一命令的标准输出接到后一命令的标准输入，第一例得到筛选、排序后的前几行；它不会自动把错误输出也传过去。`sed` 此例打印结果，不原地修改文件。

Vim 默认普通模式：`i` 进入插入模式，`Esc` 返回普通模式；`:w` 保存，`:q` 退出，`:wq` 保存退出，`:q!` 放弃未保存修改。保存后重新查看文件，确认修改确实落盘。

## 把命令写成脚本

```bash
#!/usr/bin/env bash
mkdir -p demo
cd demo || exit 1
printf '%s\n' 'hello' > result.txt
cat result.txt
```

保存为 `demo.sh` 后，执行 `chmod +x demo.sh` 再 `./demo.sh`；或直接 `bash demo.sh`，后者不要求文件有执行位。shebang 指定直接执行时的解释器；显式 `bash` 则由调用者选择解释器。重定向 `>` 会覆盖目标文件，脚本中要提前确认这一点。

脚本可进一步组织编译、运行、结果整理和绘图，但每一步应检查退出状态，前一步失败时不要继续使用旧结果。`top` 动态观察进程 CPU/内存占用；`lscpu` 检查核心、逻辑处理器、缓存及 NUMA 拓扑，不能只凭线程数判断加速。Linux 的部分系统信息以虚拟文件暴露，可用 `cat` 读取，例如 `/proc/cpuinfo`；可用路径与字段须在当前系统核对。资源含义见 [[01_Knowledge/进程线程与硬件执行单元]]、[[01_Knowledge/缓存局部性与NUMA访问]]。
