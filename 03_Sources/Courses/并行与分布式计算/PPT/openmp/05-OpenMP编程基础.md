# OpenMP 编程基础

## 一、Linux 学习环境

### 1. Linux 的起源与生态

1969 年，Ken Thompson 与 Dennis Ritchie 在贝尔实验室研发 UNIX，随后使用 C 语言重写，提高了系统的可移植性。UNIX 的设计对后来的类 UNIX 系统产生了深远影响。

1991 年，芬兰大学生 Linus Torvalds 开发了 Linux 内核。Linux 内核与 GNU 工具链等软件结合，形成可以实际使用的操作系统。开源社区不断完善内核、工具和应用，并形成 Ubuntu、CentOS、Red Hat 等发行版。

![Linux 创始人 Linus Torvalds](assets/05-OpenMP%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/slide-02-image-01.jpeg)

![早期 Linux 系统启动界面](assets/05-OpenMP%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/slide-02-image-02.jpeg)

### 2. Linux 的主要特性

- **开源与自由**：可以查看、修改和分发源代码，使用和再分发时应遵守相应许可证。开源软件同样受著作权和许可证约束。
- **多用户与多任务**：支持多用户登录，通过进程调度和资源管理运行多个任务。不同进程之间仍可能通过共享资源发生相互影响。
- **稳定性与安全性**：权限管理、文件访问控制和持续维护为长期运行提供基础，实际效果取决于配置、更新和运行环境。
- **命令行与自动化**：Shell 命令和脚本可用于系统管理、数据处理、批量编译与运行。

### 3. 系统的基本组成

| 组成 | 主要作用 |
| --- | --- |
| 内核（Kernel） | 管理处理器、内存、设备、进程调度和文件系统，向上层程序提供系统服务 |
| Shell | 解释命令并启动程序，是用户与系统交互的一种方式，常见实现包括 Bash 和 Zsh |
| 文件系统 | 使用以 `/` 为根的树形目录组织文件，并通过文件接口表示许多设备和系统信息 |

“一切皆文件”概括了类 UNIX 系统中许多资源的统一访问方式。终端是运行 Shell 的常见界面。

![Linux 终端界面](assets/05-OpenMP%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/slide-04-image-04.png)

### 4. Linux 与 Windows 的对比

| 维度 | Linux | Windows |
| --- | --- | --- |
| 源代码与授权 | Linux 内核采用 GPL，发行版由多种许可证的软件组成 | 微软提供的主要桌面系统是商业闭源软件 |
| 硬件与驱动 | 主流硬件支持广泛，具体设备需检查驱动支持 | 消费级硬件通常有厂商提供的驱动 |
| 界面与定制 | 可选择 GNOME、KDE 等桌面环境，也可使用命令行 | 提供较统一的图形界面和操作方式 |
| 软件生态 | 开发、科学计算、服务器和运维工具丰富 | 商业办公、设计软件及游戏生态丰富 |
| 安全与稳定 | 依靠权限管理、维护和更新保障运行 | 依靠权限管理、系统更新和安全防护保障运行 |
| 成本 | 有免费社区版本，也有付费企业支持 | 授权与服务费用取决于版本和购买方式 |

### 5. Linux 的应用领域

Linux 广泛用于 Web 服务、数据库和服务器，也用于路由器、智能家居与工业控制等嵌入式设备。在云计算中，Linux 为容器和许多集群管理工具提供运行环境。Android 使用 Linux 内核。Ubuntu、Fedora 等发行版也可作为开发者的桌面环境。

### 6. 学习环境与练习

常见发行版包括 Ubuntu、Linux Mint 和 Fedora。搭建学习环境的方式包括：

- **虚拟机**：使用 VirtualBox、VMware 等软件，便于隔离环境和保存快照。
- **WSL 2**：在 Windows 上使用 Linux 环境，方便文件与工具协作。
- **双系统**：通过分别启动不同系统学习 Linux。

从文件和目录管理开始，逐步练习编译程序、编写脚本和配置开发环境。

**课堂练习**：测试常用 Linux 命令的实际效果，可参阅同目录的 [Linux 常用命令](Linux%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.pdf)。

**课后练习**：进一步熟悉常用命令，借助 AI 深入研究 `sed`、`awk`、`grep` 的用法，在下一节课演示并口头说明。

### 7. 脚本文件

脚本首行的 shebang 指定解释器。以下是不同脚本的首行选项，应按实际脚本语言选用其中一行：

```text
#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/usr/bin/python3
```

下面的 Bash 脚本创建一个目录和一个文件：

```bash
#!/usr/bin/env bash
mkdir newdir
touch newfile
# 按任务需要继续添加命令。
```

例如把上述脚本保存为 `example.sh`，可用 `bash example.sh` 执行。

**课后练习**：自行设计脚本完成一系列任务，按需要查阅 Bash 语法，在下一节课演示并口头说明。

## 二、OpenMP 的基本模型

### 1. OpenMP 简介

OpenMP 是面向共享内存并行程序的接口规范，本课主要使用它在 SMP 和多核处理器上组织多个线程。它支持 C、C++ 和 Fortran，由三部分组成：

| 组成 | 用途 | 示例 |
| --- | --- | --- |
| 编译制导 | 描述并行区域、工作分配、同步和数据属性 | `#pragma omp parallel` |
| 运行时库函数 | 查询线程信息、控制执行和计时 | `omp_get_thread_num()` |
| 环境变量 | 在运行前配置线程等参数 | `OMP_NUM_THREADS` |

OpenMP 的发展与 ANSI X3H5 共享内存并行标准化工作有关。1997 年 10 月发布 OpenMP Fortran 1.0，1998 年 10 月发布 OpenMP C/C++ 1.0。早期支持厂商包括 DEC、Intel、IBM、HP、Sun 和 SGI，运行平台包括 Linux、UNIX 和 Windows。

规范入口：[OpenMP 官方网站](https://www.openmp.org/)。

### 2. Fork-Join 执行模型

程序开始时通常由一个初始线程执行串行部分。遇到 `parallel` 构造时，该线程形成一个线程团队，并作为团队的主线程参与并行区域的执行。

1. **Fork**：团队中的线程分别执行并行区域。
2. **并行执行**：通过工作共享指令把循环迭代或代码段分给线程，需要时进行同步。
3. **Join**：并行区域结束时进行隐式屏障同步，然后由进入该区域的线程继续执行后续代码。

线程运行库可能复用工作线程。“Join”不要求每次都销毁工作线程。执行模型详见 [OpenMP 5.2 执行模型](https://www.openmp.org/spec-html/5.2/openmpse3.html)。

![串行部分与并行区域交替执行](assets/05-OpenMP%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/slide-19-image-01.png)

图中每组竖线表示一个线程团队，组内包含主线程，并行区域末尾对应一次同步。

### 3. 共享与私有存储

![OpenMP 共享内存与线程私有数据模型](assets/05-OpenMP%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/memory-model.png)

多个线程可以访问同一份共享数据，也可以分别持有私有变量。共享数据如果受到并发修改，程序必须正确安排同步。把变量声明为 `shared` 仅说明共享属性，并不自动保证访问安全。

### 4. 编译器与编译选项

下面列出早期 OpenMP 工具链的编译器和启用选项。实际使用时，应以所安装编译器版本的文档为准。

| 厂商与历史平台 | 编译器 | OpenMP 选项 |
| --- | --- | --- |
| Intel，Linux Opteron/Xeon | `icc`、`icpc`、`ifort` | `-openmp` |
| PGI，Linux Opteron/Xeon | `pgcc`、`pgCC`、`pgf77`、`pgf90` | `-mp` |
| GNU，Linux Opteron/Xeon、IBM Blue Gene | `gcc`、`g++`、`gfortran` | `-fopenmp` |
| IBM，Blue Gene | `bgxlc_r`、`bgcc_r`、`bgxlC_r`、`bgxlc++_r`、`bgxlc89_r`、`bgxlc99_r`、`bgxlf_r`、`bgxlf90_r`、`bgxlf95_r`、`bgxlf2003_r` | `-qsmp=omp` |

上述 IBM Blue Gene 工具链使用名称以 `_r` 结尾的线程安全编译器。

本讲义中的 C 示例可在已配置 GCC 与 OpenMP 运行库的 Linux 环境中编译：

```bash
gcc -O2 -Wall -fopenmp hello.c -o hello
OMP_NUM_THREADS=4 ./hello
```

`-fopenmp` 启用 OpenMP 制导处理并安排运行库链接，见 [GCC OpenMP 文档](https://gcc.gnu.org/onlinedocs/gcc/OpenMP.html)。

Fortran 程序使用 `gfortran -fopenmp` 启用 OpenMP，见 [GNU Fortran OpenMP 文档](https://gcc.gnu.org/onlinedocs/gfortran/OpenMP.html)。

## 三、条件编译与运行时库

### 1. `_OPENMP` 条件编译

启用 OpenMP 支持时，可以用 `_OPENMP` 判断编译配置。示例如下：

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    (void)argc;
    (void)argv;
#ifdef _OPENMP
    printf("Compiled by an OpenMP-compliant implementation.\n");
#endif
    return 0;
}
```

**课堂练习**：

1. 比较启用和不启用 OpenMP 时的条件编译效果。
2. 研究 `main` 的 `argc`、`argv` 参数，编写通过命令行对两个数进行四则运算的 C 程序。
3. 编写脚本，自动完成程序的编译和运行。

**课后练习**：设计一个实现命令行功能的 C 程序，在下一节课展示。

### 2. 常用运行时库函数

使用这些函数时包含 `omp.h`。

| 函数原型 | 作用 |
| --- | --- |
| `int omp_get_num_procs(void)` | 查询当前设备可用的处理器数量 |
| `int omp_get_thread_limit(void)` | 查询线程数量上限 |
| `int omp_get_thread_num(void)` | 查询当前线程在团队内的编号，主线程编号为 0 |
| `int omp_get_num_threads(void)` | 查询当前团队的线程数，在串行环境中通常为 1 |
| `int omp_get_max_threads(void)` | 查询后续没有显式 `num_threads` 子句的并行区域可用线程数的上界 |
| `void omp_set_num_threads(int n)` | 设置当前任务后续并行区域的线程数配置 |
| `int omp_in_parallel(void)` | 判断当前是否位于活动并行区域中 |
| `double omp_get_wtime(void)` | 返回墙钟时间，单位为秒，可通过两次调用之差测量耗时 |
| `double omp_get_wtick(void)` | 返回计时器的时间分辨率，单位为秒 |
| `void omp_init_lock(omp_lock_t *lock)` | 初始化简单锁 |
| `void omp_destroy_lock(omp_lock_t *lock)` | 销毁简单锁 |
| `void omp_set_lock(omp_lock_t *lock)` | 获取锁，必要时等待 |
| `void omp_unset_lock(omp_lock_t *lock)` | 释放锁 |
| `int omp_test_lock(omp_lock_t *lock)` | 尝试获取锁，成功返回非 0，失败返回 0 |

`omp_get_max_threads()`、`omp_get_thread_limit()` 和 `omp_get_num_threads()` 回答不同问题，不能互相替代。`omp_set_num_threads()` 配置期望线程数，实际团队规模还可能受到运行时资源和限制影响。

**课堂练习**：测试以上非锁函数的作用。

## 四、编译制导与并行区域

### 1. 编译制导的组成

OpenMP 通过在源程序中加入编译制导表达并行化要求。制导通常由标识符、构造名称和可选子句组成。

```text
制导标识符  构造名称  [子句]
```

| 语言 | 标识符与示例 |
| --- | --- |
| C/C++ | `#pragma omp parallel private(x) shared(a)` |
| Fortran 自由格式 | `!$OMP PARALLEL PRIVATE(X) SHARED(A)` |
| Fortran 固定格式 | 可使用 `C$OMP`、`*$OMP`、`!$OMP` 等标识形式 |

`parallel`、`for` / `do`、`sections` 等描述执行结构；`private`、`shared`、`reduction`、`copyin` 等子句补充数据或执行属性。

### 2. `parallel` 并行区域

```c
#pragma omp parallel /* 可选子句 */
{
    /* 团队中的每个线程执行此代码块。 */
}
```

```fortran
!$OMP PARALLEL
    ! 并行区域中的语句
!$OMP END PARALLEL
```

Fortran 子句可用逗号或空格分隔。本讲的 C/C++ 示例采用空格分隔子句，规范也允许子句之间使用可选逗号，见 [OpenMP 制导格式](https://www.openmp.org/spec-html/5.1/openmpse9.html)。并行区域结束时存在隐式屏障。

C/C++ 程序结构示例如下：

```c
#include <omp.h>

int main(void)
{
    int var1, var2;
    int var3 = 0;

#pragma omp parallel private(var1, var2) shared(var3)
    {
        /* 使用前初始化 var1 和 var2 的私有副本。 */
        /* 需要修改共享 var3 时，安排必要的同步。 */
    }
    return 0;
}
```

**课堂练习**：编译并运行下面的 Hello World 并行程序：

```c
#include <stdio.h>
#include <omp.h>

int main(void)
{
#pragma omp parallel
    {
        printf("Hello from thread %d of %d\n",
               omp_get_thread_num(), omp_get_num_threads());
    }
    return 0;
}
```

线程输出的先后顺序通常不固定。

## 五、工作分配

### 1. `parallel for` 与圆周率积分

`parallel for` 组合了创建线程团队和分配循环迭代两个动作。正确并行化要求处理循环之间的数据依赖，不能让不同迭代在缺少同步时相互干扰。

```c
#pragma omp parallel for private(var1, var2) shared(var3)
for (int i = 0; i < I; ++i) {
    /* 相互独立的迭代工作。 */
}
```

圆周率可以由积分表示：

$$
\pi=\int_0^1\frac{4}{1+x^2}\,\mathrm{d}x
=\left[4\arctan x\right]_0^1.
$$

把区间等分为 $n$ 份，使用中点求积：

$$
\pi\approx\frac{1}{n}\sum_{i=1}^{n}
\frac{4}{1+\left((i-0.5)/n\right)^2}.
$$

每个采样点的函数值可以独立计算，总和需要通过规约或其他正确同步方式汇总。

**课堂练习**：编译求 $\pi$ 的串行和并行程序，比较结果与运行时间。

### 2. `collapse` 合并嵌套循环

`collapse(n)` 把前 $n$ 层符合规范的循环迭代组合成一个迭代空间，再分配给线程。双重循环可以使用 `collapse(2)`：

```c
#pragma omp parallel for collapse(2)
for (int i = 0; i < I; ++i) {
    for (int j = 0; j < J; ++j) {
        /* 处理第 (i, j) 个元素。 */
    }
}
```

在本讲的规则矩形循环示例中，使用整数循环变量和边界，迭代之间应满足并行执行条件。`n` 是指定合并层数的常量，不能超过实际可合并循环层数。本例采用紧密嵌套写法，循环之间不插入其他语句。

### 3. 嵌套并行区域

下面设置两层活动并行区域，并在内外两层循环分别形成线程团队：

```c
omp_set_max_active_levels(2);  /* 允许两层活动并行区域。 */
omp_set_dynamic(0);            /* 关闭运行时动态调整线程数。 */

#pragma omp parallel for num_threads(m)
for (int i = 0; i < I; ++i) {
#pragma omp parallel for num_threads(n)
    for (int j = 0; j < J; ++j) {
        /* 相互独立的工作。 */
    }
}
```

两层分别形成线程团队，与 `collapse(2)` 的单个团队分配组合迭代空间不同。`omp_set_dynamic(0)` 不保证资源不足时仍能形成任意指定规模的团队。选择 `m`、`n` 时要考虑处理器数量与嵌套开销。

**课堂练习**：

1. 比较数组按行遍历和按列遍历的计算速度。
2. 比较不同并行方式的加速效果。
3. 分别按 Amdahl 和 Gustafson 的假设设计实验，分析加速比，参阅 [性能评测标准](<../../../../../%E8%AF%BE%E7%A8%8B/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/openmp/%E8%AF%BE%E7%A8%8B/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/openmp/03-%E6%80%A7%E8%83%BD%E8%AF%84%E6%B5%8B%E6%A0%87%E5%87%86.md>)。

### 4. `parallel sections` 分配代码段

`parallel sections` 用于把若干独立代码段分配给团队中的线程。每个 `section` 执行一次，具体由哪个线程执行不固定。

```c
#pragma omp parallel sections num_threads(3)
{
#pragma omp section
    {
        /* Section A */
    }
#pragma omp section
    {
        /* Section B */
    }
#pragma omp section
    {
        /* Section C */
    }
}
```

### 5. `master` 与 `single`

下面的片段放在已有并行区域内。

```c
#pragma omp master
{
    /* 由当前团队的主线程执行。 */
}

#pragma omp single
{
    /* 由团队中某一个线程执行。 */
}
```

| 构造 | 执行线程 | 结束时是否存在隐式屏障 |
| --- | --- | --- |
| `master` | 当前团队的主线程 | 无 |
| `single` | 团队中的某一个线程，可能是主线程 | 有，除非指定 `nowait` |

两种构造的执行线程和屏障语义见 [single](https://www.openmp.org/spec-html/5.2/openmpse62.html) 和 [master / masked 语义](https://www.openmp.org/spec-html/5.1/openmpse16.html)。

## 六、互斥、原子操作与规约

### 1. `critical` 临界区

对于同一临界区名称，任意时刻只允许一个线程执行对应代码块。

```c
#pragma omp critical
{
    /* 临界区。 */
}

#pragma omp critical(update_result)
{
    /* 名为 update_result 的临界区。 */
}
```

未命名的 `critical` 使用同一个互斥名称，彼此互斥。同名临界区彼此互斥，不同名称的临界区可以并发执行。如果不同临界区访问同一个共享对象，名称不同并不能保证该对象安全。

### 2. 显式锁

```c
#include <omp.h>

int main(void)
{
    omp_lock_t lock;
    int counter = 0;
    omp_init_lock(&lock);

#pragma omp parallel for shared(lock, counter)
    for (int i = 0; i < 100; ++i) {
        omp_set_lock(&lock);
        ++counter;
        omp_unset_lock(&lock);
    }

    omp_destroy_lock(&lock);
    return counter == 100 ? 0 : 1;
}
```

锁应先初始化，再由线程获取和释放，最后在不再使用时销毁。

**课堂练习**：编译 `lock` 示例，测试锁的作用。

### 3. `atomic` 原子操作

以下展示原子操作的不同形式，使用时须先声明相应变量。

```c
#pragma omp atomic
sum += i;

#pragma omp atomic
counter++;

#pragma omp atomic read
local = shared_value;

#pragma omp atomic write
shared_value = value;

#pragma omp atomic capture
old = x++;
```

默认形式用于允许的原子更新操作。`read` 和 `write` 分别进行原子读、写；`capture` 可以在更新同时取得旧值。它保护特定内存位置的操作，使用时必须满足相应语法限制，不能直接把任意代码块改成 `atomic`。

### 4. `reduction` 规约

规约为各线程建立局部结果，结束时把局部结果与原变量合并。求和与求积示例如下：

```c
int sum = 0;
long long product = 1;

#pragma omp parallel for reduction(+:sum) reduction(*:product)
for (int i = 1; i <= 10; ++i) {
    sum += i;
    product *= i;
}
```

| 操作符 | 含义 | 私有副本初值 | 典型用途 |
| --- | --- | --- | --- |
| `+` | 求和 | `0` | 累加 |
| `*` | 求积 | `1` | 连乘 |
| `-` | 支持局部减法累积，合并时使用加法 | `0` | 已弃用，宜用 `+` 合并带符号的局部结果 |
| `&` | 按位与 | `~0` | 位集合交集 |
| `\|` | 按位或 | `0` | 位集合并集 |
| `^` | 按位异或 | `0` | 奇偶校验 |
| `&&` | 逻辑与 | `1` | 条件全部满足 |
| `\|\|` | 逻辑或 | `0` | 条件至少一个满足 |
| `max` | 最大值 | 对应类型可表示的最小值 | 求最大值 |
| `min` | 最小值 | 对应类型可表示的最大值 | 求最小值 |

`reduction(-:x)` 的局部副本初值为 0，但局部结果的合并操作为加法。它不表示把各线程结果按顺序相减，OpenMP 5.2 将该规约标识符标为弃用，见 [内置规约标识符](https://www.openmp.org/spec-html/5.2/openmpsu47.html)。

原变量的初值也参与最终结果。例如求积时，原变量若初始化为 0，最终结果仍为 0。浮点求和的合并顺序可能改变末位舍入结果。

### 5. 三种方法的比较

| 特性 | `atomic` | `critical` | `reduction` |
| --- | --- | --- | --- |
| 保护或处理范围 | 规范允许的原子操作形式 | 任意符合构造要求的临界代码块 | 多个局部结果的合并 |
| 常见开销 | 原子操作和同一内存位置的争用 | 互斥与进入临界区的等待 | 局部副本和最终合并 |
| 灵活性 | 操作形式受限 | 可以组织复杂共享访问 | 用于规约问题 |
| 典型场景 | `x++`、`x += expr` 等 | 复杂共享资源操作、需要互斥的输出 | 求和、求积、最值 |

在可用规约表达的累加问题中，`reduction` 通常能减少逐次同步；`atomic` 适合受支持的简单共享更新；`critical` 提供更灵活的互斥范围。实际性能取决于竞争程度、任务规模、编译器和硬件，应通过测量比较。

**课堂练习**：比较三种方法在累加、连乘、求最值中的效率。先确认结果正确，再测量运行时间。

## 七、顺序控制与屏障同步

### 1. `ordered` 顺序区域

在下列用法中，`ordered` 让循环里的指定代码块按逻辑迭代顺序执行，其他部分仍可并行。

```c
#pragma omp parallel
{
#pragma omp for ordered
    for (int i = 0; i < n; ++i) {
        /* 并行工作。 */
#pragma omp ordered
        {
            /* 这一部分按 i = 0, 1, ..., n-1 的顺序执行。 */
        }
        /* 后续并行工作。 */
    }
}
```

只有 `ordered` 区域受到该顺序约束，循环体的其他部分仍可并行执行。

### 2. `barrier` 屏障

显式屏障要求当前团队的线程都到达该同步点后，才继续执行屏障后的代码。

```c
#pragma omp parallel
{
    /* 第一阶段。 */
#pragma omp barrier
    /* 依赖第一阶段已完成的第二阶段。 */
}
```

团队中的线程必须一致地遇到屏障。若只有部分线程进入含屏障的分支，程序可能无法完成。

常见隐式屏障包括：

- `parallel` 区域结束时。
- `for`、`single`、`sections` 等工作共享构造结束时，除非该构造允许并使用了 `nowait`。

`parallel` 区域结束处的屏障不能用 `nowait` 删除。

**课堂练习**：编译 `barrier` 示例程序，测试屏障的作用。

## 八、线程私有状态与常用子句

### 1. `threadprivate` 与 `private`

`threadprivate` 为符合要求的全局或静态变量提供每线程副本，可以用来保存线程级状态。它与某个构造中的 `private` 子句作用不同。

| 特性 | `threadprivate` | `private` 子句 |
| --- | --- | --- |
| 作用对象 | 符合规范的全局、命名空间或静态变量等 | 构造中指定的变量 |
| 生命周期 | 按线程副本与静态存储规则管理，跨区域保留有条件 | 私有副本在相应构造中使用 |
| 存储位置 | 由实现安排，常用线程本地存储 | 由实现安排，不能仅凭子句断定物理位置 |
| 初值 | 按语言和声明初始化规则处理，可用 `copyin` 复制进入并行区的主线程副本值 | C/C++ 普通标量不会自动继承原值，使用前需赋值，或使用 `firstprivate` |
| 主线程 | 使用该线程已有的 `threadprivate` 副本 | 同样使用构造生成的私有副本 |

`threadprivate` 的跨并行区域状态保留需要满足规范条件，例如团队规模与亲和性策略一致、没有动态调整等，不能假定任意两个并行区域中相同编号的线程总保留同一份状态。详见 [threadprivate 规范](https://www.openmp.org/spec-html/5.2/openmpse24.html)。

声明形式示例：

```c
static int thread_counter = 0;
#pragma omp threadprivate(thread_counter)
```

**课堂练习**：编译 `threadprivate` 示例程序，观察线程副本及跨区域状态。

### 2. 常用子句速查

| 子句 | 作用与注意事项 |
| --- | --- |
| `private(list)` | 为指定变量建立私有副本，不自动复制原变量的值 |
| `shared(list)` | 多个线程访问同一个原对象，写访问需要正确同步 |
| `default(...)` | 指定隐式确定属性的变量的数据共享规则；`parallel` 未指定此子句时，这类变量默认为 `shared`，具有预定属性的变量仍按相应规则处理；本课可用 `default(none)` 练习显式声明 |
| `firstprivate(list)` | 私有副本用遇到构造前相应原变量的值初始化 |
| `lastprivate(list)` | 把逻辑上最后一次迭代或最后一个 section 的私有结果复制回原变量，不取决于哪个线程最后完成 |
| `reduction(op:list)` | 创建局部副本，并按指定运算合并结果 |
| `nowait` | 在允许的构造上省略结束处隐式等待，使用前必须检查后续数据依赖 |
| `num_threads(n)` | 指定并行区域期望的团队线程数 |
| `schedule(...)` | 控制循环迭代如何分配给团队中的线程 |
| `ordered` | 声明相应循环支持顺序区域等顺序约束 |
| `copyprivate(list)` | 在 `single` 中把执行线程的私有值广播给团队中其他线程的相应副本 |
| `copyin(list)` | 在进入并行区域时，用团队主线程的值初始化其他线程的 `threadprivate` 副本 |

子句只能用于规范允许的构造，例如 `copyprivate` 用于 `single`，并且不能同时使用 `nowait`。

数据共享属性的完整规则见 [OpenMP 5.2 数据共享属性](https://www.openmp.org/spec-html/5.2/openmpsu33.html)。

---

下一讲：[OpenMP 并行应用实践](<../../../../../%E8%AF%BE%E7%A8%8B/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/openmp/%E8%AF%BE%E7%A8%8B/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/PPT/openmp/06-OpenMP%E5%B9%B6%E8%A1%8C%E5%BA%94%E7%94%A8%E5%AE%9E%E8%B7%B5.md>)。
