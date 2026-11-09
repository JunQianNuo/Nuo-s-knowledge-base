---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-23-第8节-OpenMP并行计算编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-14-第13节-Git与MPI编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-12-第12节-MPI并行计算与Git版本控制课程宣讲]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
---
# Makefile依赖目标与自动变量

> 一句话：Makefile 用“目标依赖哪些文件、怎样生成目标”描述构建关系；make 根据依赖和时间戳决定哪些配方需要执行。

## 规则、变量和伪目标

基本规则为 `目标: 依赖`，下一行写配方，通常必须用真实 Tab 开头。目标不存在，或普通依赖比目标新时，make 会重建目标；它不会自动知道所有源码依赖，也不会仅因编译选项变化而必然重编译。

| 写法 | 含义 |
|---|---|
| `CC = mpicc` | 递归展开变量赋值；普通 Makefile 赋值仍可被命令行覆盖 |
| `TARGET := hello` | 赋值时立即展开 |
| `NP ?= 4` | 仅在变量未定义时设置值，已定义为空也不设置 |
| `$@` | 当前目标名 |
| `$<` | 当前规则的第一个依赖 |
| `.PHONY: run clean` | 声明伪目标，不由同名文件的时间戳决定是否执行 |

## 一个完整的小例

假设 `hello.c` 是 MPI 源码，下面的配方行以 Tab 缩进：

```makefile
CC = mpicc
CFLAGS = -O2 -std=c11
NP ?= 4
TARGET := hello_mpi
SRC := hello.c

.PHONY: all run clean
all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $< -o $@

run: $(TARGET)
	mpirun -n $(NP) ./$(TARGET)

clean:
	rm -f $(TARGET)
```

`make` 选择第一个普通目标 `all`；`make run NP=2` 先确保程序已构建，再启动两个进程；`make clean` 只清除此处列出的生成物。`mpicc` 封装 MPI 头文件与链接选项，负责构建；`mpirun` 启动进程，二者职责不同。

对于 OpenMP 程序，可用 `CC = gcc`，并在 `CFLAGS` 加 `-fopenmp`。若代码还依赖头文件，应把它们列为依赖或使用自动生成的依赖文件。

## 常见误解与来源勘误

- 来源示例出现 `CC ?= mpicc`。GNU make 内建变量通常已经定义 `CC=cc`，所以这一行可能不会选择 `mpicc`；本例改成 `CC = mpicc`，也可运行 `make CC=mpicc`。`?=` 的条件是“未定义”，不只是“用户没有设置”。
- `all` 只是常见目标名，并非保留字；`clean` 也不会自动清任何东西，删除范围由配方决定。
- 报错 `missing separator` 时先检查配方的 Tab；编译失败还应查看实际展开的命令与错误信息。

语义核实：[GNU make 手册：条件赋值](https://www.gnu.org/software/make/manual/html_node/Conditional-Assignment.html)、[内建隐式变量](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html)。
