---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-28-第17节-MPI并行计算与热扩散方程课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-11-09-第20节-MPI并行计算技术授课]]'
---
# CMake构建CTest与故障注入验证

本方法把“读懂工程、产生可执行文件、检查结果、验证测试确实能检错”连成可重复的流程。输入是完整源码、工程配置和测试依赖；输出应包含可追溯的构建、测试结果。缺少教师工程时可以讲清操作路线，不能把课堂报告或示意代码写成本地复现PASS。

## 从main确认数据流

先看主入口：MPI初始化和rank/size，解析输入和算法名，分配并初始化数据，调用交换，逐项验证，汇总状态，释放资源并Finalize；再跳到函数定义看具体实现。ordered、sendrecv、nonblocking可以是同一交换接口的不同函数，由函数指针选择实现；它们不是线性方程或C++模板。未知名字如ABC应报告用法错误，不能悄悄选默认值。

接口用头文件声明。C源文件和C++测试通常分别编译、最后链接；C++侧可写

```cpp
extern "C" {
#include "pi_core.h"
}
```

它指定C语言链接约定，不是让C++编译器自动改用C编译器。具体目标和文件名须对实际工程确认。

## 配置、构建、运行、测试分别做什么

| 层次 | 工具 | 职责 |
|---|---|---|
| 项目描述 | CMakeLists.txt | 描述语言、目标、依赖和测试 |
| 配置生成 | CMake | 查找编译器及依赖，生成选定构建系统的文件 |
| 编译链接 | Make或其他生成器工具 | 按规则产生库、程序和测试程序 |
| 启动MPI | mpirun | 启动规定数量的MPI进程 |
| 执行测试 | CTest | 运行已注册、已构建的测试命令并汇总退出状态 |
| 核对结果 | GoogleTest等测试程序内部断言 | 检查数据和逻辑约束 |

课堂源码外构建路线为进入工程后 `mkdir build`、`cd build`、`cmake ..`、`make -j4`、`ctest --output-on-failure`。已有build直接进入即可，不必反复建目录，更不盲目递归删除。通用补充写法为：

```bash
cmake -S . -B build
cmake --build build --parallel 4
ctest --test-dir build --output-on-failure
```

CMake不只支持Makefile，还可生成Visual Studio、Xcode等工程。配置成功不等于编译成功，编译成功不等于数值正确；CTest不会替你重建修改后的程序。每次改动须保存、构建、再测试。构建并行度4表示最多四个构建任务，不等于 `mpirun -n 4` 的四个rank，也不保证始终同时跑四个任务。

创建文件并不意味着已将它加入构建；课程Makefile切换TARGET后才能编译对应演示文件，这个变量名是工程约定，不是Make通用内置规则。`make test`、`make check` 等目标也只有实际项目定义后才存在。

## 以target为单位读配置

下列是第16节讲义支持的配置片段，最小CMake版本为3.20，不是转写中的3.2；C标准11，C++标准17：

```cmake
cmake_minimum_required(VERSION 3.20)
project(mpi_exchange LANGUAGES C CXX)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
find_package(MPI REQUIRED COMPONENTS C CXX)
add_library(exchange_core STATIC exchange.c exchange_data.c)
target_include_directories(exchange_core PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
target_link_libraries(exchange_core PUBLIC MPI::MPI_C)
add_executable(exchange_demo exchange_main.c)
target_link_libraries(exchange_demo PRIVATE exchange_core)
```

`REQUIRED` 表示找不到依赖就配置失败，`find_package` 不自动下载，也不保证任意安装位置都能被找到。exchange_core是静态库，exchange_demo是可执行目标；DLL通常指动态链接库，不能与静态库混称。头文件搜索路径不会把目录内全部源文件自动加入编译。

`MPI::MPI_C` 是导入目标，携带MPI编译和链接条件；PUBLIC表示本目标和使用者都获得相应使用要求，PRIVATE仅用于当前目标。FindMPI的CXX组件表示MPI C API可用于C++，并非已移除的旧MPI C++绑定。此片段不是完整可构建工程，更未包含所有测试注册。

## 测试组织与有效性

GoogleTest的 `TEST(套件名,测试名)` 组织用例；`EXPECT_EQ`用于整数等精确比较，`EXPECT_TRUE`用于逻辑条件，`EXPECT_NEAR(a,b,eps)`检查绝对差不超过eps。EXPECT失败通常记录非致命失败并继续；ASSERT失败从当前函数返回，不等于终止整个测试程序或整个MPI作业。它们不是普通C++异常机制；MPI测试还须协调各rank后续路径，避免某rank离开而其他rank仍等待。

可对实际测试可执行文件使用筛选参数：

```bash
./test_core --gtest_filter='PiSerial.*'
```

课程Makefile可能转发该参数，但没有源码不能猜变量拼写。CMake通过 `include(CTest)`、查找GoogleTest、`add_test` 等注册测试；MPI测试的命令须实际包含启动器和进程数。CTest的PROCESSORS属性是调度信息，不能替代启动参数；TIMEOUT是执行时间上限，不能解除MPI协议死锁。

验证测试有效性要完成闭环：先正常测试，再在交换后、断言前故意改接收值；保存重建，确认GoogleTest/CTest检出失败；恢复正确代码，再保存重建并复验。整数数组逐项精确比较，所有rank都应核验；积分测试用有依据的误差预算。若注入已知可观察错误仍通过，应查是否测试了旧程序、断言范围遗漏或错误未传播，不能扩大容差掩盖问题。

死锁演示用外部约3秒超时包装器终止两端先Ssend后Recv的程序。实际 `run_with_timeout.py` 未取得时，不猜工具路径或宣称已运行；超时只能结束演示，不说明协议已修复，也不能单独证明所有超时都是死锁。

官方语义参考：[FindMPI](https://cmake.org/cmake/help/v3.20/module/FindMPI.html)、[target_link_libraries](https://cmake.org/cmake/help/v3.20/command/target_link_libraries.html)、[GoogleTest断言](https://google.github.io/googletest/reference/assertions.html)。上述通用命令和语义解释为整理补充；教师工程与本地实际运行记录须另行核验。

## 构建配置与性能实验的边界

在已有单配置Makefile/Ninja构建目录中，可依次运行`cmake .. -DCMAKE_BUILD_TYPE=Debug`、`cmake --build .`、`ctest --output-on-failure`；切换Release需重新配置和构建。`CMAKE_BUILD_TYPE`针对单配置生成器，多配置生成器另选配置。[CMake官方说明](https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html)。

Debug通常便于调试，Release通常启用更多优化，适合性能测量；具体选项仍以工具链为准。`assert`是否生效取决于`NDEBUG`等设置，Release不等于删除全部检查或禁用C++异常，优化也不保证编译更快。性能对比须使用一致构建配置。CTest可能因迭代量较大而较慢，不能只由等待较久认定失败。

11月9日教师演示了构建、CTest和CSV绘图，但完整热方程第11示例及脚本未取得，本地未执行，不能登记为本次已通过的测试。可确认的运行输入语义为网格数量与最终时间，不能把后者写成时间步长；实际可执行文件与完整选项应查对应工程说明，不拼造启动命令。
