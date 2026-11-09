---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-21-第7节-Linux命令与OpenMP并行编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-23-第8节-OpenMP并行计算编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-28-第9节-缺少逐字稿]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-30-第10节-OpenMP并行编程培训]]'
---
# OpenMP的Fork-Join与数据作用域

> 一句话：OpenMP 在共享地址空间里创建线程团队执行并行域；变量由谁共享、谁各持一份，必须和任务分工一起明确。

## Fork-Join 与作用域

OpenMP 支持 C、C++、Fortran，由编译制导、运行时函数和环境变量共同组成。典型程序由初始线程串行开始，遇到 `parallel` 时形成团队，各线程执行域内代码；末尾有隐式屏障，团队完成后继续外层执行。这里的 Fork 是形成线程团队的模型，不是 Unix `fork()` 复制进程，也不要求运行时每次都实际创建全新线程。

| 属性 | 存储与初值 | 典型用途 |
|---|---|---|
| `shared(x)` | 各线程访问同一存储位置 | 只读输入、明确分区写入的输出 |
| `private(x)` | 各线程独立副本；普通 C 标量不继承外部初值 | 每线程临时值，使用前赋值 |
| `firstprivate(x)` | 独立副本，并复制进入结构前的值 | 每线程从同一初始参数开始 |

并行域外的普通变量通常共享，域内自动局部变量通常私有；静态变量等有例外，不能仅靠“写在里面”判断。工作共享循环的迭代变量有预定私有属性；临时量宜在循环体内定义。

```c
#include <omp.h>
#include <stdio.h>

int main(void)
{
    int seed = 10;
    #pragma omp parallel firstprivate(seed)
    {
        seed += omp_get_thread_num();
        printf("tid=%d team=%d value=%d\n",
               omp_get_thread_num(), omp_get_num_threads(), seed);
    }
    printf("outside=%d\n", seed); /* 仍为 10 */
}
```

改成 `private(seed)` 就必须先初始化私有副本，不能直接 `+=`；改成共享后并发 `+=` 会产生竞争。共享不等于不安全：各线程只读同一数组，或无重叠地写不同元素，可以是安全的。未同步的冲突访问中至少一个为写时，需要分析数据竞争。

## 运行时速查

| 函数 | 要回答的问题 |
|---|---|
| `omp_get_thread_num()` | 我在当前团队中是几号（从 0 开始）？ |
| `omp_get_num_threads()` | 当前团队实际有多少线程？串行区通常为 1 |
| `omp_set_num_threads(n)` | 后续相关并行域请求多少线程？ |
| `omp_get_max_threads()` | 当前设置下，后续不带 `num_threads` 的并行域团队大小上界是多少？ |
| `omp_get_thread_limit()` | 当前竞争组允许的 OpenMP 线程数上限是多少？ |
| `omp_get_num_procs()` | 运行时可用处理器数是多少？ |
| `omp_in_parallel()` | 当前是否处于活动并行域？ |
| `omp_get_wtime()`、`omp_get_wtick()` | 墙钟时间及其计时分辨率是多少？ |

请求线程数可能受动态调整、线程上限和环境限制，实际数量要在域内查询。多个 `printf` 的先后不保证线程编号顺序，输出也可能交错；打印顺序不是逻辑顺序。

## 启用与检查

```bash
gcc -Wall -O2 -fopenmp demo.c -o demo
```

GCC 的 `-fopenmp` 启用编译与链接支持，`-Wall` 打开常见警告，`-o` 指输出名。可用 `#ifdef _OPENMP` 检查 OpenMP 是否启用；缺少支持时制导可能被忽略，不能只看程序是否编译成功。

分工与归并见 [[01_Knowledge/OpenMP循环分工与归约]]，互斥和屏障见 [[01_Knowledge/OpenMP同步结构的选择]]。9月28日仅作为课件和前后课重建来源，不代表有当日录音或实测输出。运行时接口核实：[OpenMP 5.2 规范目录](https://www.openmp.org/spec-html/5.2/openmpli1.html)。
