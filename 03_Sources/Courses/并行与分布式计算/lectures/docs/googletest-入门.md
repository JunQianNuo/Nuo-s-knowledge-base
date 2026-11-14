# GoogleTest 入门与环境检查

GoogleTest 是 C++ 测试框架，常简称 gtest。我们把预期结果写成断言，由测试程序报告通过或失败。第四讲的数值计算仍用 C 编写，测试文件使用 C++；两者通过头文件里的 `extern "C"` 接口连接。

## 先确认测试能编译和运行

在仓库根目录运行：

```bash
bash scripts/check_gtest.sh
```

脚本创建一个临时测试文件，使用 C++17 编译器编译，链接 GoogleTest，随后执行一个断言测试。只有编译、链接和测试运行全部成功，才报告“GoogleTest 可用”。临时源码和可执行文件会自动清理。`bash scripts/check_env.sh` 也会调用这项检查。

编译器默认是 `c++`。脚本优先从 `pkg-config gtest` 获取头文件路径和链接参数；没有元数据时，尝试编译器的默认搜索路径以及 `-lgtest -pthread`。如果 GoogleTest 位于自定义安装目录，应把其中的 `lib/pkgconfig` 或 `lib64/pkgconfig` 加入 `PKG_CONFIG_PATH`，再运行检查。

可以显式选择编译器或 `pkg-config`，这两个变量各接受一个可执行文件名或完整路径：

```bash
CXX=g++ bash scripts/check_gtest.sh
PKG_CONFIG=pkg-config bash scripts/check_gtest.sh
```

不要仅凭 `/usr/src/googletest` 目录存在就判断环境可用：头文件、库文件以及当前编译器之间的配合，仍需实际编译和运行确认。

## 读懂一个测试

```cpp
#include <gtest/gtest.h>

TEST(ArithmeticTest, AddsTwoIntegers) {
    EXPECT_EQ(4, 2 + 2);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```

`TEST` 定义测试：`ArithmeticTest` 是测试套件名，`AddsTwoIntegers` 是该套件中的测试名。`EXPECT_EQ` 检查两个整数是否相等。失败信息给出源码位置及参与比较的值，便于回到对应代码检查。

`InitGoogleTest` 处理测试选项；`RUN_ALL_TESTS()` 执行选中的测试并返回结果。`main` 必须把结果返回给调用它的命令，才能让 Makefile 发现测试失败。

| 断言 | 用途 | 失败后当前函数的行为 |
|---|---|---|
| `EXPECT_EQ(expected, actual)` | 检查精确相等，如区间起止下标 | 继续执行 |
| `EXPECT_NEAR(actual, expected, tolerance)` | 检查绝对误差不超过给定容差 | 继续执行 |
| `ASSERT_EQ(expected, actual)` | 检查后续操作的必要前提 | 立即返回 |

例如，中点公式只使用一个小区间时，积分近似值为 3.2。测试应检查这一计算规则；若直接要求它等于真实的 π，失败原因就是错误的测试预期。浮点结果通常用 `EXPECT_NEAR`，容差应区分数值方法的离散误差与浮点舍入差异。

## 在第四讲示例中使用 Makefile

```bash
cd examples/mpi/05_pi_send_recv
make
make run NP=4 N=100000
make test
make test-mpi NP=4
make check
```

`make test` 检查计算函数和任务划分；`make test-mpi` 启动指定数量的 MPI 进程，检查实际通信与汇总结果；`make check` 按示例 Makefile 的约定运行全部检查。修改源码后重新执行测试目标，`make` 会先重建受影响的目标。

普通单元测试由一个进程执行。MPI 集成测试要求各 rank 以相同顺序进入同一批通信测试，并由配套运行器汇总失败结果。不要在尚有收发待完成时，只让某个 rank 因 `ASSERT_*` 提前返回，否则其他 rank 可能持续等待。测试超时表示需要检查通信与执行顺序，不代表计算结果通过。

GoogleTest 支持 `--gtest_filter=套件名.测试名`，其中 `*` 可匹配多个名字。第四讲用 Makefile 的 `GTEST_FLAGS` 传入筛选条件：

```bash
make test GTEST_FLAGS='--gtest_filter=PartitionTest.*'
make test-mpi NP=4 GTEST_FLAGS='--gtest_filter=MpiPiTest.*'
```

本例测试运行器只支持 `--gtest_filter=...` 与环境变量 `GTEST_FILTER`。为了让所有 rank 以相同顺序执行通信测试，它会核对各 rank 的筛选条件，拒绝不支持的测试选项；选择了零个测试也会返回失败。测试名称和框架代码见示例的程序详解。

## 常见错误

| 现象 | 检查内容 |
|---|---|
| 找不到 C++ 编译器 | 检查 `c++ --version`，或通过 `CXX` 选择已安装的编译器 |
| `gtest/gtest.h` 找不到 | 检查 GoogleTest 开发文件是否安装，以及 `pkg-config --cflags gtest` 的输出 |
| `cannot find -lgtest` 或 `library not found for -lgtest` | 检查库文件与 `pkg-config --libs gtest` 的搜索路径 |
| `undefined reference` 或 `undefined symbols` | 检查是否链接 GoogleTest、C 源文件是否按 C 编译、C++ 侧是否使用了 `extern "C"` 声明 |
| 编译通过但运行失败 | 阅读测试程序实际输出；动态库路径、程序崩溃和断言失败都要分别处理 |
| 显示运行了 0 个测试 | 检查筛选条件；没有执行目标测试不能作为验证通过的证据 |

若在 Ubuntu 24.04 自建环境中确实缺少开发包，可安装：

```bash
sudo apt update
sudo apt install -y build-essential libgtest-dev pkg-config
bash scripts/check_gtest.sh
```

上述命令用于 Ubuntu 环境。课程容器中的命令在容器终端执行；macOS 或 Windows 宿主机的库不会自动成为容器内可用的库。

## 参考资料

以下资料核对于 2026-10-17。

1. [GoogleTest Primer](https://google.github.io/googletest/primer.html)：`TEST`、`EXPECT_*` / `ASSERT_*`、测试入口和返回值。
2. [Assertions Reference](https://google.github.io/googletest/reference/assertions.html)：整数断言和 `EXPECT_NEAR` 的绝对误差语义。
3. [Using GoogleTest from various build systems](https://google.github.io/googletest/pkgconfig.html)：`pkg-config` 提供的编译、链接参数，以及自定义安装路径。
4. [Advanced GoogleTest Topics](https://google.github.io/googletest/advanced.html#running-a-subset-of-the-tests)：`--gtest_filter` 和测试选择。
5. [Ubuntu 24.04 的 libgtest-dev 软件包](https://packages.ubuntu.com/noble/libgtest-dev)：Ubuntu 的 GoogleTest 开发包。
6. [本仓库 GoogleTest 自检脚本](../scripts/check_gtest.sh)、[第四讲示例 Makefile](../examples/mpi/05_pi_send_recv/Makefile)：课程实际检查流程与运行入口。
