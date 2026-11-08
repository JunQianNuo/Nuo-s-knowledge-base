---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-21-第15节-MPI并行计算与死锁课程]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-26-第16节-MPI集合通信与CMake编译教学]]'
---
# CMake构建CTest与故障注入验证

从main确认输入、算法选择、数据初始化、交换、验证和清理，再追踪函数定义。CMakeLists描述目标及依赖，cmake配置生成，make或cmake --build编译链接，ctest启动已构建测试，GoogleTest断言比较结果。源码外build分离生成物，改源码后保存再构建再测试；构建并行度不等MPI进程数。find_package查依赖并不自动下载安装。测试用已知正确整数或合理浮点阈值，EXPECT失败通常继续、ASSERT失败返回当前函数。正常→注入错误→重建→检出失败→恢复→重建→复验，可检验测试真正有效；不能放宽容差掩盖故障。
