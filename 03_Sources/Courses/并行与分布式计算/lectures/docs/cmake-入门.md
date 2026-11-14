# CMake 入门：进入 build，配置、编译、运行与测试

从第五讲起，新示例使用 CMake。前四讲的 Makefile 仍可继续使用。本篇以 `examples/mpi/06_exchange` 为例，使用课程 Linux 环境或 macOS 终端中的默认 Makefile 构建方式；Windows 同学在课程 Linux 容器终端操作。

## 1. 先认识三个工具

| 工具 | 在本例中做什么 |
|---|---|
| CMake | 读取 `CMakeLists.txt`，查找编译器和依赖，生成 Makefile |
| make | 按生成的依赖规则调用编译器，生成库和可执行程序 |
| CTest | 运行项目登记的测试命令，汇总通过、失败与超时 |

GoogleTest 则在测试程序内部执行 `TEST` 和断言。因此，CTest 负责启动测试，GoogleTest 负责检查预期结果。

这一讲仍然会使用 `make`。变化在于：我们维护 `CMakeLists.txt`，让 CMake 生成 Makefile，无需手写每条编译和链接命令。

## 2. 第一次完整运行

从课程仓库根目录开始：

```bash
cd examples/mpi/06_exchange
mkdir build
cd build
cmake ..
make
mpirun -n 2 ./exchange_demo nonblocking 8
ctest
```

把这些步骤按目的拆开理解：

1. `mkdir build` 创建专门存放构建结果的目录。如果已经存在，直接进入即可。
2. `cd build` 进入这个目录。后面的构建、运行和测试都在这里进行。
3. `cmake ..` 中的 `..` 指上一级源码目录。CMake 读取那里的 `CMakeLists.txt`，将生成的 Makefile 和配置缓存写到当前目录。
4. `make` 按 Makefile 的规则编译、链接本例的默认目标，包括演示程序与测试程序。
5. `mpirun` 启动两个 MPI 进程，执行已编译的程序；这里 `8` 是每个数组的元素数。
6. `ctest` 运行两个已注册的测试条目。

`cmake ..` 可能做少量探测编译以检查环境，但**配置成功不表示应用程序已经编译完成**。同样，`make` 生成程序后，还需要实际运行程序或测试。

需要 CMake 3.20 或以上、C/C++ 编译器、MPI 和 GoogleTest。课程镜像构建文件列有相应依赖；是否可用仍以实际配置、编译和测试结果为准。

## 3. 为什么新建 build

```text
06_exchange/                 源码目录
  CMakeLists.txt
  exchange.c
  exchange.h
  exchange_main.c
  tests/
  build/                     构建目录
    Makefile                 CMake 生成
    CMakeCache.txt           当前机器的配置缓存
    exchange_demo            编译生成的程序
    exchange_unit_tests
    exchange_mpi_tests
```

源码在上一级，生成文件在 `build` 中。这样提交 Git 时，只保留源码、头文件、测试和 `CMakeLists.txt`；不提交缓存、本机程序和生成的 Makefile。

`CMakeCache.txt` 保存当前构建的编译器、依赖位置等信息，不能用别人的缓存替代本机配置。切换计算机或工具环境时，用新的构建目录重新执行 `cmake ..`。

## 4. 什么是 target

target（目标）是 CMake 中要构建的一个对象，可以是库或可执行程序。本例有：

| 目标名 | 用途 |
|---|---|
| `exchange_core` | 复用的 C 通信与数据函数库 |
| `exchange_demo` | 三种数组交换方法的演示程序 |
| `exchange_unit_tests` | 普通 GoogleTest 测试程序 |
| `exchange_mpi_tests` | 需要两个 rank 共同执行的测试程序 |

在 `build` 内只构建演示程序：

```bash
make exchange_demo
mpirun -n 2 ./exchange_demo sendrecv 8
```

第一条会先构建这个目标需要的库，再链接程序；第二条才运行程序。`make exchange_demo` 不会自动启动 MPI，也不保证测试程序已经构建。准备运行全部测试时，使用 `make` 构建默认目标。

## 5. 看懂 CMakeLists.txt 的基本写法

文件开头声明项目和所需语言，查找 MPI：

```cmake
cmake_minimum_required(VERSION 3.20)
project(mpi_exchange LANGUAGES C CXX)
find_package(MPI REQUIRED COMPONENTS C CXX)
```

完整文件在创建目标前还设置了 C11 和 C++17。C 函数用 C 编译器编译，GoogleTest 测试用 C++ 编译器编译；启用 C++ 不会把 `.c` 文件变成 C++。

`find_package` 查找已安装的依赖；`REQUIRED` 表示找不到时就停止配置。成功找到 MPI 后，`MPI::MPI_C` 和 `MPI::MPI_CXX` 这两个导入目标携带所需的头文件位置、库与编译链接设置。这里的 CXX 表示在 C++ 中使用 MPI C 接口，不是旧式的 MPI C++ 绑定。

先建立一个可复用的库，再建立演示程序：

```cmake
add_library(exchange_core STATIC exchange.c exchange_data.c)
target_include_directories(exchange_core
    PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
target_link_libraries(exchange_core PUBLIC MPI::MPI_C)

add_executable(exchange_demo exchange_main.c)
target_link_libraries(exchange_demo PRIVATE exchange_core)
```

- `add_library` 创建库目标；`STATIC` 表示静态库，供程序链接，本身不能像程序一样运行。
- `target_include_directories` 声明头文件目录。`${CMAKE_CURRENT_SOURCE_DIR}` 是当前 `CMakeLists.txt` 所在的源码目录。
- `add_executable` 创建程序目标。
- `target_link_libraries` 声明使用哪些库，使 CMake 知道依赖与构建顺序。
- `PUBLIC` 表示当前目标和使用它的下游目标都需要这些使用要求；本例公开头文件含 `mpi.h` 和 `MPI_Comm`，所以调用者也需要 MPI。
- `PRIVATE` 为当前目标自身添加使用要求；例如演示程序需要使用 `exchange_core`。它与 MPI 进程间的数据是否共享无关。

## 6. 让 CTest 启动 GoogleTest

普通测试目标与注册方式如下：

```cmake
include(CTest)
if(BUILD_TESTING)
    find_package(GTest REQUIRED)
    add_executable(exchange_unit_tests
        tests/unit_main.cc tests/test_core.cc)
    target_link_libraries(exchange_unit_tests
        PRIVATE exchange_core GTest::gtest)
    add_test(NAME exchange_unit COMMAND exchange_unit_tests)
endif()
```

`include(CTest)` 提供默认开启的测试支持；`BUILD_TESTING` 是项目中的测试开关，课堂直接使用默认设置。`GTest::gtest` 提供 GoogleTest 库，本例自己的运行器已经提供 `main`。

`add_test` 登记“CTest 应执行哪条命令”。`exchange_unit` 是测试名，`exchange_unit_tests` 是可执行目标名，可以不同。CMake 将这个目标名转换成构建后的程序位置。

MPI 测试也在同一个条件块中注册，但它必须经过 MPI 启动器：

```cmake
add_test(NAME exchange_mpi_2
    COMMAND ${MPIEXEC_EXECUTABLE} ${MPIEXEC_NUMPROC_FLAG} 2
            ${MPIEXEC_PREFLAGS}
            $<TARGET_FILE:exchange_mpi_tests>
            ${MPIEXEC_POSTFLAGS})
```

启动器和进程数选项来自 `FindMPI`，`2` 表示两个 rank；`TARGET_FILE` 给出测试程序的实际路径。这些设置已经写在项目里，学生执行 `ctest` 即可。

完整文件还设置测试超时，并让运行器汇总所有 rank 的失败。默认两个 CTest 条目分别运行 4 个普通用例和 9 个 MPI 用例；只看到 rank 0 的局部检查成功，不等于整个 MPI 测试通过。

## 7. 修改后，重新编译并测试

保存源码，然后在 `build` 中执行：

```bash
make
ctest
```

`make` 按源码、头文件和依赖关系重建受影响的目标。CTest 执行已有程序，**不会先替你重新编译**。

如果修改了 `CMakeLists.txt`，可以先在 `build` 中再执行一次 `cmake ..`，然后 `make`、`ctest`。生成的 Makefile 由 CMake 管理，不直接修改它。

测试失败时，在 `build` 中查看 `Testing/Temporary/LastTest.log`，或用 `ctest --output-on-failure` 显示失败输出。需要清理编译产物时，在 `build` 中执行 `make clean`；它通常保留配置和生成规则。

## 8. 常见问题

| 现象 | 先检查什么 |
|---|---|
| `cmake ..` 找不到项目 | 是否已经进入本例的 `build`，上一级是否有 `CMakeLists.txt` |
| 找不到 MPI 或 GoogleTest | 是否进入课程环境，所需开发库是否已安装 |
| 没有 `Makefile` 或程序 | `cmake ..` 与 `make` 是否成功；是否在正确的 `build` |
| 修改后结果没变化 | 是否保存源码，并重新执行 `make` |
| CTest 找不到测试程序 | 是否执行了构建全部默认目标的 `make` |
| CTest 显示没有测试 | 是否在本例构建目录，配置阶段是否启用了测试 |
| MPI 测试超时 | 检查双方消息匹配、调用顺序和非阻塞请求是否正确完成 |

本例的 `build` 与 `build-*` 已加入 Git 忽略规则。提交前仍用 `git status --short` 和 `git diff` 检查实际内容。

## 参考资料

资料核对日期：2026-10-21。

1. [CMake 3.20：cmake 命令行](https://cmake.org/cmake/help/v3.20/manual/cmake.1.html)：在构建目录指定源码目录，以及配置、生成与缓存。
2. [CMake 3.20：Unix Makefiles](https://cmake.org/cmake/help/v3.20/generator/Unix%20Makefiles.html)：生成 Makefile 与 make 构建方式。
3. [CMake 3.20：构建系统](https://cmake.org/cmake/help/v3.20/manual/cmake-buildsystem.7.html)、[target_link_libraries](https://cmake.org/cmake/help/v3.20/command/target_link_libraries.html)、[target_include_directories](https://cmake.org/cmake/help/v3.20/command/target_include_directories.html)：目标、依赖与使用要求。
4. [CMake 3.20：FindMPI](https://cmake.org/cmake/help/v3.20/module/FindMPI.html)、[FindGTest](https://cmake.org/cmake/help/v3.20/module/FindGTest.html)：依赖查找与导入目标。
5. [CMake 3.20：CTest 模块](https://cmake.org/cmake/help/v3.20/module/CTest.html)、[add_test](https://cmake.org/cmake/help/v3.20/command/add_test.html)、[ctest 命令行](https://cmake.org/cmake/help/v3.20/manual/ctest.1.html)：测试注册和执行。
6. [本课 CMakeLists.txt](../examples/mpi/06_exchange/CMakeLists.txt)、[本例程序详解](../examples/mpi/06_exchange/程序详解.md)：实际目标与命令。
