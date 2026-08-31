# 最优化建模与求解 (核心基础部分)

张勇

电子科技大学 数学科学学院

2026年7月

## 目录

1. 最优化问题建模的基本过程....1
1.1. 举例说明：工厂生产优化问题....1
1.1.1. 问题描述....1
1.1.2. 建模过程....2
1.1.3. 数学模型....3
1.1.4. 总结....4
2. 优化建模与求解....5
2.1. 线性规划....5
2.1.1. 建模案例....5
2.1.2. MATLAB 优化工具箱求解....6
2.1.3. 求解实例....7
2.2. 整数线性规划....8
2.2.1. 建模案例....8
2.2.2. MATLAB 优化工具箱求解....8
2.2.3. 求解实例....9
2.3. 混合整数线性规划....10

2.3.1. 问题描述：工厂生产计划优化问题....10
2.3.2. 数学建模....11
2.3.3. MATLAB 求解程序....12
2.3.4. 说明....14
2.4. 非线性规划....15
2.4.1. 建模案例....15
2.4.2. MATLAB 优化工具箱求解....16
2.4.3. 求解实例....16
2.5. 动态规划....17
2.5.1. 建模案例....17
2.5.2. MATLAB 编程求解....18
多目标规划....20
3.1. MATLAB 最优化工具箱求解函数....21
3.1.1. fgoalattain....21
3.1.2. fminimax....23
3.1.3. gamultiobj....25
3.1.4. paretosearch....27
3.1.5. 总结....29

3.2. 多目标规划案例....30
3.2.1. 建模案例....30
3.2.2. MATLAB 优化工具箱求解....31
3.2.3. 求解实例....32
4. 遗传算法的基本思想及 MATLAB 求解实例....34
4.1. 遗传算法的基本思想....34
4.2. MATLAB 调用 ga 求解最优化模型....35
4.3. 求解实例....36
4.3.1. 问题描述....36
4.3.2. MATLAB 代码....37
4.3.3. 运行结果....38
4.3.4. 说明....38

## 1. 最优化问题建模的基本过程

最优化问题建模的关键在于明确目标、决策变量和约束条件三个要素。以下通过一个生产优化问题的案例，说明最优化问题建模的基本过程。

## 1.1. 举例说明：工厂生产优化问题

## 1.1.1. 问题描述

假设某工厂生产两种产品 $P_{1}$ 和 $P_{2}$ ，每单位 $P_{1}$ 的利润为 3 元，每单位 $P_{2}$ 的利润为 5 元。生产受限于原材料和工时：

\- 每单位 $P_{1}$ 需 1 单位原材料，每单位 $P_{2}$ 需 2 单位原材料，总量不超过 100 单位。

\- 每单位 $P_{1}$ 需 2 小时工时，每单位 $P_{2}$ 需 1 小时工时，总工时不超过 80 小时。

\- 生产数量不能为负。

目标是确定 $P_{1}$ 和 $P_{2}$ 的生产数量，以最大化总利润。

## 1.1.2. 建模过程

## 1. 确定目标

目标是最大化工厂的总利润。根据问题描述，每单位 $P_{1}$ 贡献 3 元利润，每单位 $P_{2}$ 贡献 5 元利润。假设 $x_{1}$ 和 $x_{2}$ 分别表示 $P_{1}$ 和 $P_{2}$ 的生产数量，则目标函数为：

$$
Z = 3 x _ {1} + 5 x _ {2}\tag{1}
$$

目标是最大化 Z。

## 2. 确定决策变量

决策变量是需要优化的量，即工厂决定生产多少 $P_{1}$ 和 $P_{2}$ 。定义：

\- $x_{1}$ : 生产 $P_{1}$ 的数量（单位：件）。

\- $x_{2}$ : 生产 $P_{2}$ 的数量（单位：件）。

本问题的决策变量是连续的，可以是任意非负实数。

## 3. 确定约束条件

约束条件反映了生产中的资源限制和实际要求。根据问题描述，约束条件包括：

\- 原材料约束：每单位 $P_{1}$ 需 1 单位原材料，每单位 $P_{2}$ 需 2 单位原材料，总量不超过 100 单位：

$$
x _ {1} + 2 x _ {2} \leq 1 0 0\tag{2}
$$

\- 工时约束：每单位 $P_{1}$ 需 2 小时工时，每单位 $P_{2}$ 需 1 小时工时，总工时不超过 80 小时：

$$
2 x _ {1} + x _ {2} \leq 8 0\tag{3}
$$

\- 非负约束：生产数量不能为负：

$$
x _ {1}, x _ {2} \geq 0\tag{4}
$$

## 1.1.3. 数学模型

综合以上要素，本问题抽象为如下的线性规划模型：

$$
\begin{array}{c} \max \quad Z = 3 x _ {1} + 5 x _ {2} \\ \text {s.t.} \quad x _ {1} + 2 x _ {2} \leq 1 0 0 \\ 2 x _ {1} + x _ {2} \leq 8 0 \\ x _ {1}, x _ {2} \geq 0 \end{array}\tag{5}
$$

## 1.1.4. 总结

建模过程的关键是清晰定义目标函数、决策变量和约束条件：

1. 目标：明确优化方向（最大化利润、最小化成本等）。

2. 决策变量：确定需要调整的量（如生产数量）。

3. 约束条件：列出所有限制（如资源、时间等）。

通过上述步骤，将实际问题转化为数学模型。

## 2. 优化建模与求解

## 2.1. 线性规划

## 2.1.1. 建模案例

线性规划（Linear Programming，LP）是一种优化方法，用于在线性约束条件下优化线性目标函数。以下是一个简单的生产优化问题案例：

假设某工厂生产两种产品 $P_{1}$ 和 $P_{2}$ ，每单位 $P_{1}$ 利润为 3 元，每单位 $P_{2}$ 利润为 5 元。生产受限于原材料和工时，约束条件如下：

\- 原材料：每单位 $P_{1}$ 需 1 单位原材料，每单位 $P_{2}$ 需 2 单位原材料，总量不超过 100 单位。

\- 工时：每单位 $P_{1}$ 需 2 小时，每单位 $P_{2}$ 需 1 小时，总工时不超过 80 小时。

\- 非负约束： $x_{1}, x_{2} \geq 0$ ，其中 $x_{1}, x_{2}$ 分别为 $P_{1}, P_{2}$ 的生产数量。

目标：最大化总利润 $Z = 3x_{1} + 5x_{2}$ 。

数学模型:

$$
\begin{array}{r l} & {\max Z = 3 x _ {1} + 5 x _ {2}} \\ & {\mathrm{s.t.} x _ {1} + 2 x _ {2} \leq 1 0 0} \\ & {\quad 2 x _ {1} + x _ {2} \leq 8 0} \\ & {\quad x _ {1}, x _ {2} \geq 0} \end{array}\tag{6}
$$

## 2.1.2. MATLAB 优化工具箱求解

MATLAB 优化工具箱提供 linprog 函数求解线性规划问题。基本语法如下:

```txt
x = linprog(f, A, b, Aeq, beq, lb, ub)
```

其中：

\- f: 目标函数系数向量。

\- A, b: 不等式约束 $Ax \leq b$ 的系数矩阵和右端向量。

\- Aeq, beq: 等式约束 $Aeq \cdot x = beq$ 的系数矩阵和右端向量（无等式约束时置空）。

\- lb, ub: 变量下界和上界。

## 2.1.3. 求解实例

该模型通过 MATLAB 的 linprog 函数求解，求解结果为 $x_{1}=20, x_{2}=40$ ，最大利润 $Z=3\times20+5\times40=260$ 元。验证约束：

\- 原材料： $20 + 2 \times 40 = 100 \leq 100$ ，满足。

\- 工时： $2 \times 20 + 40 = 80 \leq 80$ ，满足。

\- 非负： $x_{1} = 20, x_{2} = 40 \geq 0$ ，满足。

求解本线性规划问题的 MATLAB 代码:

```matlab
求解程序：
% 定义目标函数
f = [-3; -5]; % 最大化问题取负值
A = [1, 2; 2, 1]; % 定义不等式约束
b = [100; 80];
lb = [0; 0]; ub = []; % 定义变量界限
% 调用 linprog 求解
[x, fval] = linprog(f, A, b, [], [], lb, ub);
% 输出结果
fprintf('x1 = %.2f, x2 = %.2f\n', x(1), x(2));
fprintf('最大利润 = %.2f\n', -fval);
```

## 2.2. 整数线性规划

## 2.2.1. 建模案例

整数线性规划（Integer Linear Programming, ILP）要求部分或全部变量为整数。以下是一个背包问题案例：假设有 3 件物品，重量分别为 w = [4,5,6]，价值为 v = [10,20,30]，背包容量为 10。目标是选择物品使得总价值最大。

数学模型:

$$
\begin{array}{r l} \max & Z = 1 0 x _ {1} + 2 0 x _ {2} + 3 0 x _ {3} \\ \text {s.t.} & 4 x _ {1} + 5 x _ {2} + 6 x _ {3} \leq 1 0 \\ & x _ {1}, x _ {2}, x _ {3} \in \{0, 1 \} \end{array}\tag{7}
$$

## 2.2.2. MATLAB 优化工具箱求解

MATLAB 使用 intlinprog 函数求解整数线性规划问题。基本语法:

$$
x = \text { intlinprog } (f, \text { intcon }, A, b, A e q, b e q, l b, u b)
$$

其中 intcon 指定整数变量的索引。

## 2.2.3. 求解实例

运行结果： $x_{1}=1,x_{2}=0,x_{3}=1$ ，最大价值 $Z=10+30=40$ 。

```matlab
f = [-10; -20; -30]; % 定义目标函数
A = [4, 5, 6]; % 定义不等式约束
b = 10;
intcon = 1:3; % 定义整数变量
lb = [0; 0; 0]; % 定义变量界限
ub = [1; 1; 1];
% 调用 intlinprog 求解
x = intlinprog(f, intcon, A, b, [], [], lb, ub);
% 输出结果
fprintf('x1=%d, x2=%d, x3=%d\n', x(1), x(2), x(3));
fprintf('最大价值 = %.2f\n', -f'*x);
```

## 2.3. 混合整数线性规划

## 2.3.1. 问题描述：工厂生产计划优化问题

某工厂计划生产两种产品：产品 A 和产品 B。每种产品的单位利润分别为 40 元 和 30 元。每生产一单位产品 A 需要消耗 2 小时机器时间和 1 小时人工时间；每生产一单位产品 B 需要消耗 1 小时机器时间和 1 小时人工时间。

该工厂每周最多可提供:

\- 100 小时的机器时间

\- 80 小时的人工时间

同时，由于设备限制，每周最多只能开机生产产品 A 或产品 B 中的一种（不能同时开机生产两种产品）。即：

\- 如果生产产品 A，则不能生产产品 B，反之亦然。

目标：最大化总利润，决定每周应生产哪种产品以及生产数量。

## 2.3.2. 数学建模

## 决策变量

$x_{1}$ ：产品 A 的生产数量（连续变量）

$x_{2}$ ：产品 B 的生产数量（连续变量）

$y_{1}\in\{0,1\}$ ：是否生产产品 A（0-1 整数变量）

$y_{2}\in\{0,1\}$ ：是否生产产品 B（0-1 整数变量）

## 建立最优化模型

目标函数（最大利润）：

$$
\max Z = 4 0 x _ {1} + 3 0 x _ {2}\tag{1}
$$

## 约束条件:

1. 机器时间限制：

$$
2 x _ {1} + x _ {2} \leq 1 0 0\tag{2}
$$

2. 人工时间限制：

$$
x _ {1} + x _ {2} \leq 8 0\tag{3}
$$

3. 开机选择限制（最多只开一类）：

$$
y _ {1} + y _ {2} \leq 1\tag{4}
$$

4. 如果未开机，则不生产：

$$
x _ {1} \leq \mathrm{My} _ {1}, x _ {2} \leq \mathrm{My} _ {2},\tag{5}
$$

其中 $M$ 是一个足够大的常数，表示最大可能生产数量（如 $M = 100$ ）

5. 非负约束与变量类型:

$$
x _ {1} \geq 0, x _ {2} \geq 0, y _ {1}, y _ {2} \in \{0, 1 \},\tag{6}
$$

## 2.3.3. MATLAB 求解程序

```matlab
% ---- 定义目标函数系数 ----
f = [-40; -30; 0; 0]; % 最大化 → 转化为最小化目标函数（取负）
% ---- 定义约束 ----
% 不等式约束 A * x <= b
A = [
    2, 1, 0, 0;    % 机器时间约束
    1, 1, 0, 0;    % 人工时间约束
    0, 0, 1, 1;    % 开机限制：y1 + y2 <= 1
    1, 0, -100, 0;    % x1 <= M * y1
    0, 1, 0, -100    % x2 <= M * y2
];
b = [100; 80; 1; 0; 0];
% ---- 定义变量类型 ----
intcon = [3, 4]; % 第3个变量是 y1，第4个变量是 y2 → 整数变量
% ---- 定义变量上下限 ----
```

```matlab
1b = [0; 0; 0; 0];    % 所有变量下限为 0
ub = [Inf; Inf; 1; 1]; % x1, x2 无上限，y1, y2 最大为 1
% ---- 求解 ----
[x_opt, fval, exitflag, output] = intlinprog(f, intcon, A, b, [], [], lb, ub);
% ---- 结果显示 ----
disp('最优解：');
fprintf('产品 A 的生产量 x1 = %.2f\n', x_opt(1));
fprintf('产品 B 的生产量 x2 = %.2f\n', x_opt(2));
fprintf('是否生产 A (y1) = %d\n', x_opt(3));
fprintf('是否生产 B (y2) = %d\n', x_opt(4));
fprintf('最大利润 = %.2f\n', -fval); % 注意目标函数取过负号

运行结果如下：
最优解：
产品 A 的生产量 x1 = 0.00
产品 B 的生产量 x2 = 80.00
是否生产 A (y1) = 0
是否生产 B (y2) = 1
最大利润 = 2400.00
```

## 2.3.4. 说明

\- 使用 intlinprog 求解混合整数线性规划；

\- 目标函数转换为最小化形式;

\- 引入 y1, y2 控制是否生产某类产品;

\- intcon 指定整数变量索引;

\- 结果中 x\_opt(3) 和 x\_opt(4) 为 0 或 1，控制决策逻辑；

\- 该问题体现了混合整数线性规划在生产计划、逻辑控制和资源分配中的应用。

## 2.4. 非线性规划

## 2.4.1. 建模案例

非线性规划（Nonlinear Programming, NLP）涉及非线性目标函数或约束。以下是一个简单的非线性优化问题：目标：最小化 $f(x) = x_1^2 + x_2^2$ ，约束为：

• $x_{1} + x_{2} \geq 1$

• $x_{1}, x_{2} \geq 0$

数学模型:

$$
\begin{array}{r l} \min & f (x) = x _ {1} ^ {2} + x _ {2} ^ {2} \\ \text {s.t.} & x _ {1} + x _ {2} \geq 1 \\ & x _ {1}, x _ {2} \geq 0 \end{array}\tag{9}
$$

## 2.4.2. MATLAB 优化工具箱求解

使用 fmincon 函数求解非线性规划问题。基本语法:

```txt
x = fmincon(fun, x0, A, b, Aeq, beq, lb, ub, nonlcon)
```

其中 fun 为目标函数，nonlcon 定义非线性约束。

## 2.4.3. 求解实例

运行结果可得:

$x_{1} = 0.50, x_{2} = 0.50$ ，最小值 $f(x) = 0.50$ 。

问题：如果决策变量有整数约束，还能使用 fmincon 求解非线性规划模型吗？

```matlab
本模型的求解程序如下：
fun = @(x) x(1)^2 + x(2)^2; % 定义目标函数
x0 = [0; 0]; % 定义初始点
A = [-1, -1]; b = -1; % 定义线性约束
lb = [0; 0]; % 定义下界
% 调用 fmincon 求解
x = fmincon(fun, x0, A, b, [], [], lb, []);
% 输出结果
fprintf('x1 = %.2f, x2 = %.2f\n', x(1), x(2));
fprintf('最小值 = %.2f\n', fun(x));
```

## 2.5. 动态规划

## 2.5.1. 建模案例

设国家拨给 60 万元投资，供四个工厂扩建使用，每个工厂扩建后的利润与投资额的大小有关，投资后的利润函数如下表所示。

<table><tr><td>投资利润</td><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td></tr><tr><td> $g_1(x)$ </td><td>0</td><td>20</td><td>50</td><td>65</td><td>80</td><td>85</td><td>85</td></tr><tr><td> $g_2(x)$ </td><td>0</td><td>20</td><td>40</td><td>50</td><td>55</td><td>60</td><td>65</td></tr><tr><td> $g_3(x)$ </td><td>0</td><td>25</td><td>60</td><td>85</td><td>100</td><td>110</td><td>115</td></tr><tr><td> $g_4(x)$ </td><td>0</td><td>25</td><td>40</td><td>50</td><td>60</td><td>65</td><td>70</td></tr></table>

## 模型建立：

定义函数 $f_{k}(u)$ 表示第 1 个至第 k 个工厂投资 u 万元产生的最大利润. 依据题意，是要求 $f_{4}(60)$ 。

(1) 第一阶段: 求 $f_{1}(x)$ 。显然有 $f_{1}(x) = g_{1}(x)$ , 得到下表

<table><tr><td>投资利润</td><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td></tr><tr><td> $f_1(x)=g_1(x)$ </td><td>0</td><td>20</td><td>50</td><td>65</td><td>80</td><td>85</td><td>85</td></tr><tr><td>最优策略</td><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td></tr></table>

(2) $f_{k}(u)=\max_{\substack{y\in\{0,10,\cdots,60\} \\ \text{且}y\leq u}}\left\{g_{k}(y)+f_{k-1}(u-y)\right\}, k=2,3,4..$

最优策略为 $(20, 0, 30, 10)$ ，最大利润为160万元。

## 2.5.2. MATLAB 编程求解

动态规划通常需要自定义实现，MATLAB 可通过矩阵操作实现。

function testmain

global M v

v = [0 10 20 30 40 50 60]; % 决策集合

```matlab
M=[0 20 50 65 80 85 85 %M(i,:)第i个工厂的利润值
0 20 40 50 55 60 65
0 25 60 85 100 110 115
0 25 40 50 60 65 70];
fun(4,60)
function r= fun(k,s_k)
global M v
idx = find(v<=s_k);
t = v(idx);% 决策 u_k 从 v(idx)数组中取值
if k==1,
    idx = find(v==s_k);
    u_k = v(idx);
    r = M(1,idx);
    disp(sprintf('f%d(%d)=g(%d)=%d',k,s_k,u_k,r));
    return
end
optvalue = -inf;

程序续:
for i=1:length(idx)
    u_k = t(i);% t(i)=v(idx(i))
    idx2 = idx(i);
    value = M(k, idx2)+fun(k-1,s_k-u_k);
    if value >optvalue,
    optuk = u_k; % 存储当前搜索到“最优方案”的决策
    optvalue = value; % 存储当前搜索到的“最优方案”的最优指标。
    end
end
r = optvalue;%%
disp(sprintf('f%d(%d)=g(%d)+f%d(%d)=%d',k,s_k,optuk,k-1,s_k-optuk,r));
```

## 3. 多目标规划

多目标规划：

$$
\begin{array}{l} \min f _ {1} (X), \min f _ {2} (X), \dots , f _ {k} (X), X = \left(x _ {1}, x _ {2}, \dots , x _ {n}\right) ^ {T} \\ s. t. \left\{ \begin{array}{l} A X \leq b \\ A _ {e q} X = b _ {e q} \\ C (X) \leq 0 \\ C _ {e q} (X) = 0 \\ L _ {\text { bound }} \leq X \leq U _ {\text { bound }} \end{array} \right. \end{array}
$$

符号含义:

$$
\begin{array}{l} F (x) = \left(f _ {1} (X), f _ {2} (X), \dots , f _ {k} (X)\right) ^ {T} \\ C (X) = \left(g _ {1} (X), g _ {2} (X), \dots , g _ {p} (X)\right) ^ {T} \\ C _ {e q} (X) = \left(h _ {1} (X), h _ {2} (X), \dots , h _ {q} (X)\right) ^ {T} \\ L _ {b o u n d} = \left(l _ {1}, l _ {2}, \dots , l _ {n}\right) ^ {T} \\ U _ {b o u n d} = \left(u _ {1}, u _ {2}, \dots , u _ {n}\right) ^ {T} \end{array}
$$

## 3.1. MATLAB 最优化工具箱求解函数

## 3.1.1. fgoalattain

功能描述: fgoalattain 用于求解多目标优化问题，通过设定目标值和权重，寻找使各目标函数尽可能接近指定目标的解。适用于目标函数存在冲突但需要平衡的情况。

$$
\begin{array}{c} \min _ {X, \gamma} \gamma \\ s. t. \left\{ \begin{array}{l} F (X) - W \gamma \leq F _ {\text { goal }} \\ A X \leq b \\ A _ {e q} X = b _ {e q} \\ C (X) \leq 0 \\ C _ {e q} (X) = 0 \\ L _ {\text { bound }} \leq X \leq U _ {\text { bound }} \end{array} \right. \end{array}
$$

其中 $\gamma\in R,\quad W=\left(w_{1},w_{2},\cdots,w_{K}\right)^{T},\quad F_{goal}=\left(f_{goal,1},f_{goal,2},\cdots,f_{goal,k}\right)^{T}.$

## 3.1.1.1. 语法

```txt
[x, fval, exitflag] = fgoalattain(fun, x0, goal, weight, A, b, Aeq, beq, lb, ub, nonlcon)
```

## 3.1.1.2. 参数说明

\- fun: 目标函数（返回向量）

\- x0: 初始解

\- goal: 期望达到的目标值向量

\- weight: 权重向量（控制目标优先级）

• A, b: 线性不等式约束 $Ax \leq b$

\- Aeq, beq: 线性等式约束 $A_{eq}x = b_{eq}$

\- lb, ub: 变量上下界

\- nonlcon: 非线性约束函数

## 3.1.1.3. 编程实例

问题描述：最小化两个冲突目标 $f_{1}(x) = x_{1}^{2} + x_{2}^{2}$ 和 $f_{2}(x) = (x_{1} - 1)^{2} + x_{2}^{2}$ ，目标值设为[0.5,0.5]。

```matlab
fun = @(x) [x(1) ^2 + x(2) ^2; (x(1)-1) ^2 + x(2) ^2];
x0 = [0.5, 0.5];
goal = [0.5, 0.5];
weight = [1, 1]; % 等权重
[x, fval] = fgoalattain(fun, x0, goal, weight);
disp(['最优解: x = ['，num2str(x)，']]);
disp(['目标值: f1 = ', num2str(fval(1)), ', f2 = ', num2str(fval(2))]);
```

## 3.1.2. fminimax

功能描述:fminimax 求解极小极大问题，即最小化一组目标函数中的最大值。适用于需要优化最坏场景的性能。

$$
\begin{array}{l} \min _ {X} (\max _ {1 \leq i \leq k} f _ {i} (X)) \\ s. t. \left\{ \begin{array}{l} A X \leq b \\ A _ {e q} X = b _ {e q} \\ C (X) \leq 0 \\ C _ {e q} (X) = 0 \\ L _ {\text { bound }} \leq X \leq U _ {\text { bound }} \end{array} \right. \end{array}
$$

## 3.1.2.1. 语法

```javascript
[x, fval] = fminimax(fun, x0, A, b, Aeq, beq, lb, ub, nonlcon)
```

## 3.1.2.2. 编程实例

问题描述：最小化三个目标的最大值：

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$f_{1}(x)=x_{1}^{2}+x_{2}^{2},\quad f_{2}(x)=(x_{1}-1)^{2}+x_{2}^{2},\quad f_{3}(x)=(x_{1}-0.5)^{2}+(x_{2}-1)^{2}$ 

fun = @(x) [x(1) $^{2}$  + x(2) $^{2}$ ; (x(1)-1) $^{2}$  + x(2) $^{2}$ ; (x(1)-0.5) $^{2}$  + (x(2)-1) $^{2}$ ];

x0 = [0.5, 0.5];

[x, fval] = fminimax(fun, x0);

disp(['最优解：x = ['，num2str(x)，']');
disp(['各目标值：', num2str(fval')]);
disp(['最大值：', num2str(max(fval))]);
</div>

## 3.1.3. gamultiobj

## 3.1.3.1. 功能描述

gamultiobj基于遗传算法求解多目标优化问题，生成Pareto前沿。适用于非线性、非凸或离散问题。

## 3.1.3.2. 语法

```julia
x = gamultiobj(fun, nvars)
x = gamultiobj(fun, nvars, A, b)
x = gamultiobj(fun, nvars, A, b, Aeq, beq)
x = gamultiobj(fun, nvars, A, b, Aeq, beq, lb, ub, nonlcon, options)
[x, fval] = gamultiobj(...)
```

## 3.1.3.3. 编程实例

问题描述：求解两目标优化问题：

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$f_{1}(x) = x_{1}^{2} + x_{2}^{2}, \quad f_{2}(x) = (x_{1} - 1)^{2} + (x_{2} - 1)^{2}$

fun = @(x) [x(1) ^2 + x(2) ^2; (x(1) - 1) ^2 + (x(2) - 1) ^2];
nvars = 2;

options = optimoptions('gamultiobj', 'PopulationSize', 50);
[x, fval] = gamultiobj(fun, nvars, [], [], [], [], [], options);
</div>

```matlab
% 绘制 Pareto 前沿
scatter(fval(:,1), fval(:,2), 'filled');
xlabel('f1'); ylabel('f2'); title('Pareto 前沿');
```

## 3.1.4. paretosearch

## 3.1.4.1. 功能描述

paretosearch 使用模式搜索算法寻找 Pareto 最优解集，适合局部精细搜索。

## 3.1.4.2. 语法

```txt
x = paretosearch(fun, nvars)
```

```txt
x = paretosearch(fun, nvars, A, b)
```

```txt
x = paretosearch(fun, nvars, A, b, Aeq, beq)
```

```txt
x = paretosearch(fun, nvars, A, b, Aeq, beq, lb, ub)
[x, fval] = paretosearch(...)
```

## 3.1.4.3. 编程实例

问题描述：求解三目标优化问题：

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$f_{1}(x)=x_{1}^{2}+x_{2}^{2},\quad f_{2}(x)=(x_{1}-1)^{2}+x_{2}^{2},\quad f_{3}(x)=x_{1}^{2}+(x_{2}-1)^{2}$ 

fun = @(x) [x(1) ^2 + x(2) ^2; (x(1)-1) ^2 + x(2) ^2; x(1) ^2 + (x(2)-1) ^2];
nvars = 2;
options = optimoptions('paretosearch', 'ParetoSetSize', 50);
[x, fval] = paretosearch(fun, nvars, [], [], [], [], [], [], options)
% 可视化
scatter3(fval(:,1), fval(:,2), fval(:,3), 'filled');
xlabel('f1'); ylabel('f2'); zlabel('f3'); title('Pareto解集');
</div>

## 3.1.5. 总结

\- fgoalattain: 通过目标值和权重平衡冲突目标。

\- fminimax：优化最坏情况下的性能。

\- gamultiobj: 生成全局 Pareto 前沿（遗传算法）。

\- paretosearch: 局部精细搜索 Pareto 解（模式搜索）。

## 3.2. 多目标规划案例

## 3.2.1. 建模案例

多目标规划（Multi-Objective Programming）涉及优化多个目标函数。以下是一个生产优化问题：目标：

\- 最大化利润： $f_{1}=3x_{1}+5x_{2}$

\- 最小化成本： $f_{2}=2x_{1}+4x_{2}$

约束：

• $x_{1} + 2x_{2} \leq 100$

\- $2x_{1} + x_{2}\leq 80$

• $x_{1}, x_{2} \geq 0$

## 3.2.2. MATLAB 优化工具箱求解

MATLAB 使用 paretosearch 函数求解多目标规划问题，求解 Pareto 最优解集。基本语法：

```txt
[x, fval] = paretosearch(fun, nvars, A, b, Aeq, beq, lb, ub)
```

## 3.2.3. 求解实例

```matlab
% 定义目标函数
fun = @(x) [-3*x(1) - 5*x(2); 2*x(1) + 4*x(2)];
% 定义约束
A = [1, 2; 2, 1];
b = [100; 80];
lb = [0; 0];
% 调用 paretosearch 求解
[x, fval] = paretosearch(fun, 2, A, b, [], [], lb, []);
% 输出部分 Pareto 解
for i = 1:min(5, size(x, 1))
    fprintf('解 %d: x1 = %.2f, x2 = %.2f, 利润 = %.2f, 成本 = %.2f\n', i, x(i,1), x(i,2), -fval(i,1), fval(i,2));
end
```

```txt
解 1: x1 = 25.38, x2 = 25.38, 利润 = 203.00, 成本 = 152.25
解 2: x1 = 24.08, x2 = 31.84, 利润 = 231.46, 成本 = 175.53
解 3: x1 = 22.56, x2 = 0.31, 利润 = 69.25, 成本 = 46.38
解 4: x1 = 24.38, x2 = 23.38, 利润 = 190.00, 成本 = 142.25
解 5: x1 = 18.13, x2 = 36.63, 利润 = 237.50, 成本 = 182.75
```

运行结果：输出多个 Pareto 最优解。

## 4. 遗传算法的基本思想及 MATLAB 求解实例

## 4.1. 遗传算法的基本思想

遗传算法（Genetic Algorithm, GA）是一种基于生物进化理论的优化算法，模拟自然选择和遗传机制来搜索最优解。其基本思想包括以下几个核心步骤：

1. 初始化种群：随机生成一组初始解（个体），每个个体表示优化问题的一个可能解，通常编码为二进制或实数向量。

2. 适应度评价：根据目标函数计算每个个体的适应度（fitness），适应度反映个体解的质量。

3. 选择：根据适应度选择优质个体，适应度高的个体有更大概率被选中（如轮盘赌选择法）。

4. 交叉：模拟生物繁殖，通过交换两个个体的部分基因（如单点交叉）生成新个体，增加种群多样性。

5. 变异：以小概率随机改变个体的某些基因（如翻转或扰动），避免陷入局部最优。

6. 迭代：重复选择、交叉、变异操作，生成新一代种群，直到满足终止条件（如达到最大迭代次数或目标函数收敛）。

遗传算法适用于复杂、非线性、离散或连续的优化问题，尤其在传统方法难以求解时表现出色。

## 4.2. MATLAB 调用 ga 求解最优化模型

MATLAB 优化工具箱提供 ga 函数采用遗传算法求解最优化模型。基本语法如下：

```txt
[x, fval] = ga(fitnessfcn, nvars, A, b, Aeq, beq, lb, ub, nonlcon, options)
```

其中：

\- fitnessfcn: 目标函数句柄。

\- nvars: 决策变量数量。

\- A, b: 线性不等式约束 $Ax \leq b$ 。

\- Aeq, beq: 线性等式约束 $Aeq \cdot x = beq$ 。

\- lb, ub: 变量下界和上界。

\- nonlcon: 非线性约束函数句柄。

\- options: 算法参数设置（如种群大小、最大代数等）。

## 4.3. 求解实例

## 4.3.1. 问题描述

考虑一个非线性优化问题:

目标：最小化 $f(x)=x_{1}^{2}+x_{2}^{2}$ 。

约束：

$$
\begin{array}{r l} \bullet & x _ {1} + x _ {2} \geq 1 \\ \bullet & x _ {1}, x _ {2} \geq 0 \end{array}
$$

数学模型:

$$
\begin{array}{r l} & {\min f (x) = x _ {1} ^ {2} + x _ {2} ^ {2}} \\ & {\mathrm{s.t.} x _ {1} + x _ {2} \geq 1} \\ & {\quad x _ {1}, x _ {2} \geq 0} \end{array}\tag{11}
$$

## 4.3.2. MATLAB 代码

以下是使用 ga 函数求解该问题的 MATLAB 代码:

```matlab
fitnessfcn = @(x) x(1)^2 + x(2)^2; % 定义目标函数
% 定义线性约束
A = [-1, -1]; b = -1; % 对应 x_1 + x_2 >= 1
lb = [0; 0]; % 下界 x_1, x_2 >= 0
% 设置遗传算法参数
options = optimoptions('ga', ...
    'PopulationSize', 50, ... % 种群大小
    'MaxGenerations', 100, ... % 最大代数
    'Display', 'iter'); % 显示迭代过程
% 调用 ga 求解
[x, fval] = ga(fitnessfcn, 2, A, b, [], [], lb, [], [], options);
% 输出结果
fprintf('x1 = %.4f, x2 = %.4f\n', x(1), x(2));
fprintf('最小值 = %.4f\n', fval);
```

## 4.3.3. 运行结果

运行上述代码，典型输出如下：

$$
\mathrm{x} 1 = 0. 5 0 0 0, \mathrm{x} 2 = 0. 5 0 0 0
$$

最小值 = 0.5000

结果表明，最优解为 $x_{1} \approx 0.5, x_{2} \approx 0.5$ ，目标函数值 $f(x) \approx 0.5$ ，满足约束条件 $x_{1} + x_{2} \geq 1$ 。

## 4.3.4. 说明

\- 适应度函数：fitnessfcn 定义了目标函数 $x_{1}^{2} + x_{2}^{2}$ ，遗传算法通过最小化该函数搜索最优解。

\- 约束处理：线性约束通过 A 和 b 实现，非负约束通过 1b 设置。

\- 参数设置：options 中设置种群大小为 50，最大迭代代数为 100，Display 设置为 'iter' 显示迭代信息，便于观察算法收敛过程。

\- 结果验证：解 $x_{1} = x_{2} = 0.5$ 满足 $x_{1} + x_{2} = 1 \geq 1$ ，且目标函数值 $f(x) = 0.5$ 是理论最优值（可通过拉格朗日乘子法验证）。

通过遗传算法，MATLAB能够高效求解此类非线性优化问题，尤其适合全局优化场景。