---
raw_title: 并行与分布式计算5-OpenMP编程基础
subject: 并行与分布式计算5-OpenMP编程基础
source: 并行与分布式计算5-OpenMP编程基础.pptx
status: mineru解析
parser: mineru
---

## OpenMP编程基础

## **Linux系统简介**

### **01 UNIX 的诞生 (1969年)**

由Ken Thompson与Dennis Ritchie在贝尔实验室研发，后用C语言重写实现了高度可移植性。它奠定了现代操作系统的核心架构与设计思想，是Linux等类UNIX系统的重要源头。

### **02 Linux 的诞生 (1991年)**

芬兰大学生Linus Torvalds为学习操作系统原理，开发了Linux内核。最初仅为个人爱好项目，凭借开源精神迅速吸引全球开发者参与，开启了自由软件时代的新篇章。

### **03 开源生态的蓬勃发展**

Linux内核与GNU工具链结合形成完整系统，依托开源社区协作持续迭代。如今衍生出Ubuntu、CentOS、RedHat等丰富发行版，广泛应用于服务器、云计算、嵌入式设备及超级计算机领域。

![](images/cf76f6b4fd245e3fca622c4ad119c305139903618ad7779c23792ff6d15308b3.jpg)

Linux 创始人：Linus Torvalds

![](images/5b02977b1d481b12b6cdc3eff51b8309a1e25d37a4a94da144e284deacfe5d89.jpg)

早期 Linux 系统启动界面

## **Linux系统的特性**

### **01 开源与自由**

源代码完全公开，允许任何人查看、修改和分发。用户享有使用、修改及分享的自由，无商业版权限制，这是Linux生态繁荣的基石。

### **02 多用户与多任务**

支持多用户同时独立登录，进程间互不干扰。基于高效的调度机制，可并行运行多个程序，充分利用系统资源，提升工作效率。

### **03 稳定性与安全性**

系统可7x24小时不间断运行，极少出现崩溃。基于严格的权限管理和文件访问控制，配合社区快速的漏洞响应，安全性备受信赖。

### **04 强大的命令行界面**

提供灵活高效的操作方式，单条命令即可完成复杂管理。支持Shell脚本编写，轻松实现系统运维、数据处理等任务的自动化。

## **Linux系统的基本组成结构**

### **01 内核 (Kernel) - 系统核心**

操作系统的“心脏”，负责管理CPU、内存、磁盘等硬件资源，处理进程调度与文件系统交互。它是连接上层软件与底层硬件的核心桥梁，决定了系统的稳定性与性能。

### **02 Shell - 交互界面**

用户与内核之间的“翻译官”，负责解释用户输入的命令并调用内核服务执行。常见的Shell包括Bash（默认）、Zsh等，是用户操作Linux系统的主要交互入口。

### **03 文件系统 - 资源管理**

遵循“一切皆文件”的设计哲学，将硬件设备、进程数据等统一抽象为文件进行管理。采用树形目录结构，以根目录“/”为起点，层次分明，便于数据的组织、存储与访问。

![](images/67f12202cb3ee1d6395753a4651904970c55c1325b893cef75e61c3b081ac5ca.jpg)

## **Linux 系统 vs Windows 系统**

核心维度对比分析

### **Linux 系统**

![](images/ec7d99e1bdf9ab0010b1b140a60c19271e2bc05c4ea5de872ed4e09123d60fc4.jpg)

![](images/83d2ebe01d9b032d8e0c44f91f5c9ca48edef48816869adb47a69fac46769eb7.jpg)

**01 开源与自由**

基于GPL协议，源代码完全开放，支持自由分发与二次修改，社区驱动发展。

**03 高度可定制**

支持GNOME、KDE等多种桌面环境，界面与功能可根据需求深度个性化配置。

**05 安全与稳定**

严格的权限管理机制，病毒攻击极少，系统运行稳定，适合服务器长期部署。

**02 驱动与硬件**

主流硬件支持完善，开源驱动生态成熟，新硬件支持可能存在短暂延迟。

**04 软件生态**

开发工具极其丰富，商业软件与游戏支持相对较少，适合开发与运维场景。

**06 成本优势**

社区版本完全免费，企业级技术支持按需付费，整体拥有成本相对较低。

### **Windows 系统**

![](images/6b858e76c13c22fab898466148ccc0ed66eae85546e52a31fee5729d97df5030.jpg)

![](images/4ee8bc69e73f8fcb3a85413c4863c259b982ba0f00fe5a59a92c1ca7479da5c0.jpg)

**01 商业闭源**

微软专有商业软件，源代码封闭，提供标准化的统一用户体验与服务。

**02 易用直观**

图形界面统一且操作逻辑一致，上手门槛极低，对普通用户和新手非常友好。

**03 生态丰富**

拥有最全面的商业软件与游戏资源，专业设计与娱乐应用的首选平台。

**04 硬件兼容**

硬件兼容性极佳，即插即用体验完善，几乎支持所有主流消费级硬件。

**05 安全防护**

用户基数庞大，是病毒攻击的主要目标，需依赖杀毒软件保障系统安全。

**06 授权模式**

需购买正版许可证，家庭版、专业版等不同版本定价不同，成本相对较高。

## **Linux的主要应用领域**

![](images/5671b463d6c64099c5a619538b9d4897ae9978067bd8c20e6dcbdf2172a5616a.jpg)

### **01 服务器领域**

占据超90%市场份额，是Web服务、数据库及云计算的首选，具备极高稳定性。

支撑全球绝大多数互联网后台业务，拥有强大的并发处理能力和安全防护机制。

![](images/4346f2b8b52dd116d392192ab1788f21b1b7e542b10371dee8556387544ece9d.jpg)

### **02 嵌入式与IoT**

广泛应用于智能家居、路由及工控设备，以轻量、可裁剪著称。

适配各类硬件平台，功耗低、响应快，是物联网设备操作系统的核心选择。

![](images/597e1ac8241653f0c89d3b90b422e4474357ac9015498df60f0a12ceba17460d.jpg)

### **03 云计算基石**

Docker、K8s的原生载体，为微服务架构提供高效运行环境。

支持快速部署与弹性伸缩，是构建现代化云原生基础设施的底层技术。

![](images/7a326c5e2d15d306866c13310e4e908d901b4185c8559a5e693be378537ba028.jpg)

### **04 移动智能终端**

Android系统基于Linux内核，覆盖全球超70%的智能手机。

为移动互联网生态提供稳定的底层支持，是全球移动设备的核心操作系统之一。

![](images/ac221cffe608248ddfebfa9834d9501aa9b8f8c659417a7f42b3a8e86b50f97f.jpg)

### **05 开发者桌面**

提供高度可定制环境，深受程序员与技术爱好者青睐。

Ubuntu、Fedora等发行版功能强大，是编程开发、系统管理的理想桌面平台。

## **Linux初学者建议**

**01 选择合适的发行版**

• **Ubuntu：** 最受欢迎的桌面发行版，社区支持强，适合新手入门 • **Linux Mint：** 界面直观友好，预装多媒体插件，上手零门槛 • **Fedora：** 紧跟前沿技术，软件包更新快，适合开发者探索

**02 搭建灵活的学习环境**

• **虚拟机：** VirtualBox/VMware，安全隔离，支持随时快照恢复 • **WSL 2：** Windows无缝集成，无需重启，文件互通便捷高效 • **双系统：** 体验最纯粹的Linux环境，性能损耗最小，适合进阶

### **03“动手实践是掌握 Linux 的关键！”**

Linux 不是一门“看会”的技术，而是一门“练会”的技术。不要畏惧命令行的黑窗口，每一次输入指令都是对系统底层逻辑的探索。从简单的文件管理开始，逐步尝试编写脚本、搭建服务，在不断的实践中积累经验，才能真正打通 Linux 的任督二脉。

![](images/8c4ab47424756854b5abe1ec63b6dbc2a68b702413085a678d38fcaac93dddf8.png)

课堂练习：测试常用Linux命令的实际效果。

课后练习：进一步熟悉常用命令，借助AI深入研究sed、awk、grep命令的使用方法，

在下一节课进行演示加口头说明。

## 脚本文件

#!/usr/bin/env bash

#!/bin/bash

#!/bin/sh

#!/usr/bin/python3

mkdir newdir

touch newfile

…

指定解释器脚本命令流课后练习：自行设计一个脚本文件完成一系列任务，在设计过程中根据自己需求查阅相关的bash语法规则，在下一节课进行演示加口头说明。

## OpenMP简介

- OpenMP是共享存储体系结构上的一个并行编程模型。适合于SMP共享内存多处理系统和多核处理器体系结构。
    - 起源于ANSI X3H5标准
    - 1997年10月：OpenMP Fortran 1.0 发布，这是 OpenMP 的首个官方规范
    - 1998年10月：OpenMP C/C++ 1.0 发布，将支持扩展到了 C 和 C++ 语言
    - 简单、移植性好和可扩展性等特点
    - 提供了支持Fortran、C/C++的API和规范
    - 由一组编译制导、运行时库函数（Run-Time routines）和环境变量组成。
    - 工业标准
        - DEC、Intel、IBM、HP、Sun、SGI等公司支持
        - 包括Linux、UNIX和Windows等多种操作系统平台
    - [http://www.openmp.org/](http://www.openmp.org/)

## OpenMP编程模式

- OpenMP是基于线程的并行编程模型。
- OpenMP采用Fork-Join并行执行方式：
    - OpenMP程序开始于一个单独的主线程（Master Thread），然后主线程一直串行执行，直到遇见第一个并行域(Parallel Region)，然后开始并行执行并行区域。其过程如下：
        - Fork:主线程创建一个并行线程队列，然后，并行域中的代码在不同的线程上并行执行；
        - Join:当并行域执行完之后，它们或被同步或被中断，最后只有主线程在执行。

**F**

**O**

**R**

**K**

**J**

**I**

**O**

**N**

**F**

**O**

**R**

**K**

**J**

**I**

**O**

**N**

**Master**

**thread**

**串行部分**

**并行域**

**串行部分**

**并行域**

**串行部分**

## OpenMP存储模型

![](images/5e383d1d45b7de4b9fa9143e4e9ea41713e055a9d72ac00614059c40393f341c.jpg)

## OpenMP编译器

![](images/31eb2fe37ce54c70f4068bbd39e83d24cff4852bd8ad658b1858a4e95daa28ae.png)

## OpenMP条件编译

int main(int argc, char \*argv[])

{

#ifdef \_OPENMP

printf("Compiled by an OpenMP-compliant implementation.\n");

#endif

return 0;

}

课堂练习：

1. 测试OpenMP条件编译的实际效果。
2. 测试main函数参数的涵义；编写一个简单的C程序来实现用命令行进行两个数的四则运算。
3. 写一个脚本文件自动完成程序的编译和执行。

课后练习：自己设计一个C程序来实现某种命令行功能，在下一节课进行展示。

## OpenMP常用库函数

- int omp\_get\_num\_procs(void)	           		获取可用处理器数量
- int omp\_get\_thread\_limit(void)                          获取最大线程上线
- int omp\_get\_thread\_num(void)			获取当前线程在并行团队中的编号
- int omp\_get\_num\_threads(void)		获取当前并行区域的线程数
- int omp\_get\_max\_threads(void)		获取后续并行区域默认最大线程数
- void omp\_set\_num\_threads(int n)		设置后续并行区域线程数
- int omp\_in\_parallel(void)	          		判断当前是否在并行区域内
- double omp\_get\_wtime(void)	           		获取当前墙钟时间，单位秒
- double omp\_get\_wtick(void)	           		获取时钟精度，单位秒
- void omp\_init\_lock(omp\_lock\_t \*lock)	 	初始化锁
- void omp\_destroy\_lock(omp\_lock\_t \*lock)	销毁锁
- void omp\_set\_lock(omp\_lock\_t \*lock)		加锁，阻塞
- void omp\_unset\_lock(omp\_lock\_t \*lock)	解锁
- int omp\_test\_lock(omp\_lock\_t \*lock)		尝试加锁，成功返回非 0

课堂练习：测试以上库函数（除了锁函数外）的作用。

## 编译制导

- OpenMP的并行化是通过使用嵌入到C/C++或Fortran源代码中的编译制导语句来实现。
- 编译制导是对程序设计语言的扩展。
- 通过对串行程序添加制导语句实现并行化。
- 支持并行区域、工作共享、同步等。
- 支持数据的共享和私有化。
- 编译制导语句由下列几部分组成：
    - 制导标识符 （ !\$OMP 、 #pragma omp ）
    - 制导名称（parallel，DO/for，section等）
    - 子句（private, shared, reduction, copyin等）

## 制导语句格式

- 编译制导语句由下列几部分组成：
    - 制导标识符 （ !\$OMP 、 #pragma omp ）
    - 制导名称（parallel，DO/for，section等）
    - 子句（private, shared, reduction, copyin等）

## 编译制导标识

- 制导是特殊的、仅用于特定编译器的源代码。
- 制导由一个位于行首的标识加以区分。
- 格式：制导标识符制导名称  [子句，]
- OpenMP 制导标识:
    - Fortran:
        - !\$OMP  (or C\$OMP or \*\$OMP)
    - C/C++:
        - #pragma omp

## 并行域制导

- 一个并行域就是一个能被多个线程并行执行的程序段

Fortran：

！\$OMP PARALLEL [clauses]

BLOCK

！\$OMP END PARALLEL

C/C++：

#pragma omp parallel [clauses]

{

BLOCK

}

- 在并行域结尾有一个隐式同步（barrier）。
- 子句（clause）用来说明并行域的附加信息。
- 在Fortran语言中，子句间用逗号或空格分隔； C/C++子句间用空格分开。

## 并行域结构

![](images/8bf6d3e00cac2da37d6d04167b710fc8098a8389657a24554d89528451cc62a3.jpg)

Master thread

Threads

barrier

Master thread

Threads

barrier

Master thread

## OpenMP程序结构

- 基于C/C++语言的OpenMP程序结构

#include<omp.h>

void main()

{

int var1, var2, var3;

……

#pragma omp parallel private(var1, var2) shared(var3)//OpenMP制导:表示这段代码将被多个线程并行执行

{

…………

}

……………

}

课堂练习：编译Hello world并行程序

## OpenMP制导指令

- parallel for是parallel 和 for语句的结合，也是用在一个for循环之前，表示for循环的代码将被多个线程并行执行，必须保证每次循环之间无相关性。

#pragma omp parallel for private(var1, var2) shared(var3)//

for(i=0;i<I;i++)

{

…………

}

- 例：求圆周率的积分公式

$\pi =\int_{0}^{1}\frac{4}{1+x^{2}}dx=4\arctan(x)\left.​\right|_{0}^{1}\approx \frac{1}{n}\sum_{i=1}^{n}\frac{4}{1+\left(\frac{i-0.5}{n}\right)^{2}}$

课堂练习：编译求pi的串行和并行程序，并进行对比。

- 嵌套循环并行1

#pragma omp parallel for collapse(n)

for(i=0;i<I;i++)

{

for(j=0;j<J;j++)//J必须为整数

{

…………

}

}

- n 不能大于实际循环层数;循环之间不能有任何语句或 OpenMP 指令

- 嵌套循环并行2

omp\_set\_nested(1);       // 启用嵌套并行

omp\_set\_max\_active\_levels(2); // 允许两层活动并行区域

omp\_set\_dynamic(0);      // 禁用动态调整，确保线程数固定

#pragma omp parallel for num\_threads(m)

for(i=0;i<I;i++)

{

#pragma omp parallel for num\_threads(n)

for(j=0;j<J;j++)

{

…………

}

}

课堂练习：

1.测试不同数组访问方式（行遍历、列遍历）对于计算速度的影响

2.测试不同并行方式的加速效果

- parallel sections: parallel和sections两个语句的结合, 用在可能会被并行执行的代码段之前

#pragma omp parallel sections num\_threads(3)

{

#pragma omp section

{

Section A;

}

#pragma omp section

{

Section B;

}

#pragma omp section

{

Section C;

}

}

- master：用于指定一段代码块由主线程执行

#pragma omp master

{

Section;//由主线程执行

}

- single：用于指定一段代码块由当个线程执行

#pragma omp single

{

Section;//由单个线程执行

}

- critical 用在一段代码临界区之前，只允许

#pragma omp critical [(name)]

{

// 临界区代码：一次只能有一个线程执行

}

- name 是可选的，用于给临界区命名。
- 如果不写名称，所有未命名的 critical 区域共享同一把锁，彼此互斥。
- 如果写了名称，不同名称的 critical 区域使用不同的锁，可以并发执行。

- atomic：同步指令，用于确保对单个内存位置的读-改-写操作作为一个不可分割的原子操作执行。

#pragma omp atomic//原子更新

sum += i;

#pragma omp atomic//原子更新

counter++;

#pragma omp atomic read

local = shared;

#pragma omp atomic write

shared = value;

int old;

#pragma omp atomic capture

old = x++;// old 得到 x 的旧值，x 原子地加 1

- reduction：归约操作。

#pragma omp parallel for reduction(+:sum) reduction(\*:product)

for (int i = 1; i <= 10; i++)

{

sum += i;

product \*= i;

}

- 规约的操作符操作符操作类型私有副本初始值适用场景

\+		求和			0				累加、求和

\*		求积			1				连乘、阶乘

\-		求差			0				累减（注意结合性）

&		按位与	\~0 (所有位为1)			位运算、求交集

|		按位或		0				位运算、求并集

^		按位异或		0				位运算、奇偶校验

&&		逻辑与		1 (true)			逻辑判断、布尔归约

||		逻辑或		0 (false)			逻辑判断、布尔归约

max		求最大值该类型可表示的最小值寻找最大值

min		求最小值该类型可表示的最大值寻找最小值

- critical、atomic、reduction的对比

![](images/b3d8f2eedc8b4a7e2c8f33b96432335714c7da11401a1801971e106e2e08d047.jpg)

课堂练习：对比以上三种操作在累加、连乘、求最值中的效率。

- ordered  用于指定并行区域的循环按顺序执行

#pragma omp for ordered [子句...]

for (int i = 0; i < n; i++)

{

// 并行执行的代码...

#pragma omp ordered

{

// 这里的代码将按 i 从 0 到 n-1 的顺序执行

}

// 继续并行执行的代码...

}

- barrier：用于并行区内代码的线程同步，所有线程执行到barrier时要停止直到所有线程都执行到barrier时才继续往下执行。很多 OpenMP 构造在结束时默认带有隐式屏障，例如：#pragma omp parallel 结束时；#pragma omp for 结束时；#pragma omp single 结束时；#pragma omp sections 结束时。

#pragma omp barrier  // 等待所有线程完成课堂练习：编译barrier示例程序，测试barrier的作用。

- threadprivate 用于指定一个变量是线程私有，用于让全局/静态变量在每个线程中拥有独立且可跨并行区域持久的副本。它适合维护线程级的长期状态（如线程私有缓冲区、累积计数器）。与 private 的核心区别在于作用对象、生命周期和主线程语义。

![](images/e1445d96b6b86c86565ce746dfbe67957aaa141122fa5afe80751bdb6c904219.jpg)

课堂练习：编译threadprivate示例程序，测试threadprivate的作用。

## OpenMP子句

- private, 指定每个线程都有它自己的变量私有副本。
- firstprivate，指定每个线程都有它自己的变量私有副本，并且变量要被继承主线程中的初值。
- lastprivate，主要是用来指定将线程中的私有变量的值在并行处理结束后复制回主线程中的对应变量。
- reduction，用来指定一个或多个变量是私有的，并且在并行处理结束后这些变量要执行指定的运算。
- nowait，忽略指定中暗含的等待
- num\_threads，指定线程的个数
- schedule，指定如何调度for循环迭代
- shared，指定一个或多个变量为多个线程间的共享变量
- ordered，用来指定for循环的执行要按顺序执行
- copyprivate，用于single指导中的指定变量广播到并行区中其它线程
- copyin，用来指定一个threadprivate的变量的值用主线程的值初始化。
- default，用来指定并行处理区域内的变量的使用方式，缺省是shared