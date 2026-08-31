# 遗传算法：从自然进化到智能优化

数学科学学院 张勇

日期：2026.07.16

## 目录

遗传算法（Genetic Algorithm）教学讲稿
- 遗传算法的核心思想
- 遗传算法流程图
- 二进制编码
- 二进制编码精度
- 四种编码方式对比
- 适应度函数
- 约束处理方法
- 选择算子——轮盘赌
- 选择算子——锦标赛选择
- 选择算子——排序选择
- 精英保留策略
- 交叉算子概述
- 变异算子概述
- 关键参数一览
- 收敛判断与终止条件
- MATLAB GA 工具箱简介
- 算例1：函数优化（Rastrigin函数）
- 课程总结

## 课程导引

本课程将带领大家从自然界的进化现象出发，理解遗传算法的核心思想。

## 学习目标:

\- 掌握遗传算法的基本原理与流程

\- 理解四种主要编码方式及其适用场景

\- 能够使用 MATLAB 实现遗传算法解决优化问题

\- 具备分析算法性能和调参的基本能力

课程安排：理论讲解 → 核心算子 → 完整案例 → 实践练习

## 为什么需要遗传算法？

传统优化方法（如梯度下降）要求：

\- 目标函数连续可微

\- 搜索空间规则

但现实问题往往:

\- 目标函数不可导、不连续

\- 搜索空间复杂、高维

\- 存在大量局部最优解

## 提问：

面对一个包含离散变量和复杂约束的优化问题，传统方法遇到了困难，我们该如何解决？

## 从达尔文到算法

1859年，达尔文发表《物种起源》，提出自然选择理论：

\- 变异：生物个体之间存在差异

\- 遗传：亲代特征可以传递给子代

\- 选择：适应环境的个体更容易生存和繁衍

\- 进化：经过多代积累，种群逐渐适应环境

遗传算法正是模拟这一过程，将“进化”搬到计算机中！

生物与算法的类比

<table><tr><td>生物进化</td><td>遗传算法</td></tr><tr><td>染色体</td><td>解的编码（个体）</td></tr><tr><td>基因</td><td>决策变量</td></tr><tr><td>等位基因</td><td>变量的取值</td></tr><tr><td>个体</td><td>一个候选解</td></tr><tr><td>种群</td><td>候选解集合</td></tr><tr><td>适应度</td><td>目标函数值</td></tr><tr><td>选择</td><td>保留优质解</td></tr><tr><td>交叉</td><td>产生新解</td></tr><tr><td>变异</td><td>引入新特性</td></tr></table>

提问：在这个类比中，什么是“环境”？在算法中如何体现？

## 遗传算法发展简史

• 1975年：John Holland 出版《Adaptation in Natural and Artificial Systems》，奠定理论基础

• 1980年代：Goldberg 将 GA 推广到工程优化领域

• 1990年代：GA成为智能计算的核心方法之一

• 至今：GA 已被广泛应用于函数优化、组合优化、机器学习、工程设计等领域

## 遗传算法的核心思想

遗传算法的本质是群体搜索策略：

1. 维护一组候选解（种群）

2. 通过“优胜劣汰”机制逐步改讲解的质量

3. 搜索过程具有隐式并行性——同时探索解空间的多个区域

4. 不依赖于梯度信息，具有全局搜索能力

提问：为什么群体搜索比单点搜索更有优势？

## 基本概念正式定义

个体（Individual）：问题的一个候选解，编码后的数据结构。

染色体（Chromosome）：个体的编码表示。

基因（Gene）：编码的基本单元，对应一个决策变量。

种群（Population）：所有个体的集合，大小为 N。

代（Generation）：种群的一次迭代更新。

适应度（Fitness）：衡量个体优劣的指标，由适应度函数计算。

# 基因型与表现型

在遗传算法中，存在两重空间：

![](images/872ced43a498b8f2e152c55cf16aa96092132d2b6f3db21700fc71730a3cd40e.jpg)

编码：将问题的解表示为染色体（如二进制串）

解码：将染色体还原为实际问题的解

提问：为什么需要区分基因型和表现型？直接操作表现型不行吗？

## 遗传算法流程图

![](images/3207bb22f6a886ebce5d23f14fc5e95e55b9efa98d7016fa0545795d2a8d2c34.jpg)

## 算法伪代码

## 算法：遗传算法（Genetic Algorithm）

输入：问题定义，算法参数（种群大小N，交叉率pc，变异率pm，最大代数Gmax）

输出：最优解和最优适应度

1. 初始化种群 P(0) ← 随机生成 N 个个体

2. 评估种群适应度 $F(0) \leftarrow$ 计算每个个体的适应度

3. FOR t ← 1 TO Gmax:

4. 选择操作：从 $P(t - 1)$ 中选择父代个体

5. 交叉操作：以概率 pc 对父代进行交叉，产生子代

6. 变异操作：以概率 pm 对子代进行变异

7. 评估子代适应度

8. 替换操作：由子代形成新种群 P(t)

9. 精英保留：保留最优个体，防止退化

10. END FOR

11. 返回最优解

## 一个直观的比喻

想象有一群动物在寻找食物最丰富的区域：

1. 初始化：动物随机分布在各个位置

2. 评估：每个动物评估当前位置的食物量

3. 选择：食物量多的动物有更多繁殖机会

4. 交叉：两个动物的“觅食策略”结合，产生后代

5. 变异：后代的策略发生微小随机变化

6. 迭代：重复上述过程，种群逐渐向食物丰富区域集中这就是遗传算法在解空间中的搜索过程！

## 编码的重要性

编码是遗传算法设计的第一步，也是最关键的一步。

好的编码应具备：

1. 完整性：解空间中的所有点都能被表示

2. 遗传性：编码结构适合交叉和变异操作

3. 合法性：任意编码都能对应一个合法解

提问：如果编码设计不当，会产生什么问题？

## 二进制编码

## 原理：将决策变量映射为二进制串

变量 x ∈ [L, U] → 二进制串 b = [b1, b2, ..., bm]

解码： $x = L + (U - L) \times (\text{二进制值}) / (2^{m} - 1)$

优点：

\- 简单直观

\- 便于理论分析（模式定理）

\- 算子设计简单

## 缺点：

\- 连续变量需要离散化，存在精度损失

\- 二进制 Hamming 距离与实数距离不一致

## 二进制编码精度

设编码长度为 $m$ ，则精度为：

$$
\Delta = \frac {U - L}{2 ^ {m} - 1}
$$

示例： $x\in [-10,10]$ ， $m = 10$

$$
\Delta = \frac {2 0}{2 ^ {1 0} - 1} \approx 0. 0 1 9 5
$$

增加 $m$ 可提高精度，但增加计算代价。

MATLAB 实现:

% 解码

$$
x = L + (U - L) ^ {*} \text {bin2dec(num2str(b))} / (2 ^ {\wedge} m - 1);
$$

% 编码

$$
b = \text { de2bi(round((x - L) / (U - L)   *   (2^m - 1)) , m) ; }
$$

## 实数编码

原理：直接使用实数向量表示个体

$$
\mathrm{个体} = [ x _ {1}, x _ {2}, \ldots , x _ {n} ], \quad x _ {i} \in [ L _ {i}, U _ {i} ]
$$

## 优点：

\- 无需编码/解码，直接对应问题变量

\- 精度高，无量化误差

\- 适合连续优化问题

缺点：

\- 需要设计专门的交叉和变异算子

\- 理论分析较复杂

提问：实数编码的个体如何保证变量始终在边界内？

## MATLAB 实数编码示例

```matlab
% 问题定义
nvars = 5; % 变量个数
lb = [0, 0, 0, 0, 0]; % 下界
ub = [10, 10, 10, 10, 10]; % 上界
% 随机初始化一个个体
chrom = lb + (ub - lb) .* rand(1, nvars);
% 种群初始化（N个个体）
N = 50;
population = zeros(N, nvars);
for i = 1:N
    population(i,:) = lb + (ub - lb) .* rand(1, nvars);
end
```

## 整数编码

原理：决策变量为整数，个体为整数向量

$$
\mathrm{个体} = [ x _ {1}, x _ {2}, \ldots , x _ {n} ], \quad x _ {i} \in \mathbb {Z} \cap [ L _ {i}, U _ {i} ]
$$

## 适用场景：

\- 整数规划问题

\- 离散优化问题（如设施选址）

\- 包含整数变量的工程问题

## MATLAB 实现:

% 整数编码初始化

```javascript
chrom = randi([lb_i, ub_i], 1, nvars);
```

% 实数编码+取整（简化方案）

```javascript
chrom = round(lb + (ub - lb) .* rand(1, nvars));
```

## 排列编码

原理：个体是一个排列，每个元素出现且仅出现一次

$$
\mathrm{个体} = [ \pi_ {1}, \pi_ {2}, \ldots , \pi_ {n} ], \quad \{\pi_ {1}, \ldots , \pi_ {n} \} = \{1, 2, \ldots , n \}
$$

适用场景：

\- 旅行商问题（TSP）

\- 作业调度问题

\- 车辆路径问题（VRP）

\- 任何需要“访问所有元素一次”的问题

提问：排列编码为什么不能使用普通的算术交叉？

## 排列编码的特点

排列编码的特殊性：

1. 唯一性约束：每个元素只能出现一次

2. 交叉操作的挑战：简单交叉会破坏排列性质

3. 变异操作的特殊性：交换、插入、倒置

% 排列编码初始化

```matlab
n = 8;
chrom = randperm(n);
```

示例：城市访问顺序

\- 个体：[3, 1, 4, 2, 5] 表示先访问城市3，再访问城市1，依此类推
- 每个城市恰好访问一次

四种编码方式对比

<table><tr><td>编码方式</td><td>适用问题</td><td>典型交叉</td><td>典型变异</td><td>MATLAB函数</td></tr><tr><td>二进制</td><td>离散/简单连续</td><td>单点/多点/均匀</td><td>位翻转</td><td>自定义</td></tr><tr><td>实数</td><td>连续优化</td><td>算术/SBX</td><td>高斯/均匀</td><td>ga</td></tr><tr><td>整数</td><td>整数规划</td><td>算术取整</td><td>随机取整</td><td>ga + IntCon</td></tr><tr><td>排列</td><td>组合优化</td><td>PMX/OX/CX</td><td>交换/插入/倒置</td><td>自定义算子</td></tr></table>

## 编码选择指南

![](images/900564bef9dd1033226e2b152b0e367d2acdccc3fbea211f67ba52fbf0dae206.jpg)

## 适应度函数

适应度函数是评价个体优劣的唯一标准：

$$
\mathrm{适应度} = f (\mathrm{个体})
$$

设计原则：

适应度值越大，个体越优

计算效率要高

应能有效区分不同个体

最大化与最小化：

<table><tr><td>原问题</td><td>适应度转换</td></tr><tr><td>最大化</td><td>F=f</td></tr><tr><td>最小化</td><td>F=1/(1+f) 或 F=-f</td></tr></table>

## 适应度缩放

当适应度差异过大时，可能导致早熟收敛。缩放可以调节选择压力：线性缩放：

$$
F ^ {\prime} = a \cdot F + b
$$

幂律缩放：

$$
F ^ {\prime} = F ^ {k}
$$

指数缩放：

$$
F ^ {\prime} = e ^ {\beta F}
$$

提问：什么情况下适应度差异过大会成为问题？

## 约束处理方法

遗传算法天然适合处理有约束的问题：

<table><tr><td>方法</td><td>原理</td><td>适用场景</td></tr><tr><td>惩罚函数</td><td>对不可行解施加惩罚</td><td>约束松弛</td></tr><tr><td>修复法</td><td>将不可行解修复为可行</td><td>约束可修复</td></tr><tr><td>拒绝法</td><td>丢弃不可行解</td><td>约束严格</td></tr><tr><td>多目标法</td><td>约束作为额外目标</td><td>复杂约束</td></tr></table>

惩罚函数公式：

$$
F (x) = f (x) - \lambda \cdot \sum_ {i} \max {(0, g _ {i} (x))}
$$

## 选择算子——轮盘赌

轮盘赌选择：适应度越高的个体被选中的概率越大

$$
p _ {i} = \frac {F _ {i}}{\sum_ {j = 1} ^ {N} F _ {j}}
$$

![](images/7e4bfafbb8ed83d5df2d42c26842e48cbc323f1fd752f0b649683dcc783ea1a1.jpg)

## 轮盘赌 MATLAB 代码

```matlab
function idx = roulette_selection(fitness)
    % 轮盘赌选择
    % 输入：fitness - 适应度向量（越大越好）
    % 输出：idx - 选中个体的索引

    N = length(fitness);
    p = fitness / sum(fitness);    % 选择概率
    c = cumsum(p);    % 累积概率

    r = rand();    % 随机数 [0,1]
    idx = find(r <= c, 1, 'first');    % 选择
end
```

## 选择算子——锦标赛选择

锦标赛选择：随机抽取 k 个个体，选择最优者

![](images/37b62f5a4061b64c08a7e48ca11ea6eb98d8cca9197aefd61612544930e899fa.jpg)

参数 $k$ 的作用：

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- $k = 2$：选择压力小，多样性好
- $k$ 增大：选择压力增大，收敛加快
function idx = tournament_selection(fitness, k)
    N = length(fitness);
    candidates = randi(N, 1, k);
    [~, best] = max(fitness(candidates));
    idx = candidates(best);
end
</div>

## 选择算子——排序选择

## 排序选择：按适应度排序后分配选择概率

1. 将个体按适应度从高到低排序

2. 根据排名分配概率:

3. $p_{i}=\frac{2(N-i+1)}{N(N+1)}$

优点：不受适应度绝对大小影响，避免适应度差异过大导致的问题  
适用场景：适应度值集中在相近区间时

## 精英保留策略

## 精英保留：

将当前种群的最优个体直接保留到下一代

1. 找出当前种群的最优个体

2. 将其直接复制到下一代

3. 其余个体通过选择、交叉、变异产生

## 重要性:

\- 保证算法单调收敛（最优适应度不下降）

\- 防止优良基因丢失

\- 实践中几乎必须使用

提问：如果没有精英保留，算法会出现什么问题？

## 交叉算子概述

交叉是遗传算法的核心探索算子：

\- 模拟生物繁殖过程中的基因重组

\- 在父代之间交换信息，产生新个体

\- 作用是探索解空间的新区域

交叉率 $p_{c}$ :

\- 通常设为 $0.6 \sim 0.95$

\- 控制交叉操作的使用频率

重要原则：交叉算子必须与编码方式匹配！

## 二进制编码交叉——单点交叉

单点交叉：选择一个交叉点，交换交叉点后的基因

```matlab
父代1: [1 0 1 1 | 0 1 0]
父代2: [0 1 1 0 | 1 0 1]
↑ 交叉点
子代1: [1 0 1 1 | 1 0 1]
子代2: [0 1 1 0 | 0 1 0]
function [c1, c2] = single_point_crossover(p1, p2)
n = length(p1);
point = randi(n-1);
c1 = [p1(1:point), p2(point+1:end)];
c2 = [p2(1:point), p1(point+1:end)];
end
```

## 二进制编码交叉——多点与均匀

## 多点交叉：选择多个交叉点，交替交换基因片段

父代1：[1 0 | 1 1 0 | 1 0]

父代2：[0 1 | 1 0 1 | 0 1]

子代1：[1 0 | 1 0 1 | 1 0]

均匀交叉：每个基因位独立决定是否交换

父代1：[1，0，1，1，0，1，0]

父代2：[0，1，1，0，1，0，1]

掩码：[1，0，1，0，1，0，0]

子代1：[1，1，1，0，0，1，1]

子代2：[0，0，1，1，1，0，0]

## 实数编码交叉——算术交叉

算术交叉：子代是父代的线性组合

$$
\begin{array}{r} \pmb {c} _ {1} = \alpha \pmb {p} _ {1} + (1 - \alpha) \pmb {p} _ {2} \\ \pmb {c} _ {2} = (1 - \alpha) \pmb {p} _ {1} + \alpha \pmb {p} _ {2} \end{array}
$$

其中 $\alpha \in [0,1]$ 是随机数。

```matlab
function [c1, c2] = arithmetic_crossover(p1, p2)
alpha = rand;
c1 = alpha * p1 + (1 - alpha) * p2;
c2 = (1 - alpha) * p1 + alpha * p2;
end
```

## 实数编码交叉——模拟二进制交叉（SBX）

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
SBX: 模拟二进制编码的单点交叉效果，适用于实数编码
特点：
- 子代与父代的“距离”可控
- 保持变量边界约束
- 分布指数 $\eta_c$ 控制子代分布
function child = sbx_crossover(p1, p2, eta_c, lb, ub)
    u = rand;
    if u &lt;= 0.5
    beta = (2*u)^(1/(eta_c+1));
    else
    beta = (1/(2*(1-u)))^(1/(eta_c+1));
    end
    child = 0.5*((1+beta)*p1 + (1-beta)*p2);
    child = max(min(child, ub), lb); % 边界约束
end
</div>

## 排列编码交叉——部分映射交叉（PMX）

## PMX: Partially Mapped Crossover

## 步骤:

1. 随机选择两个交叉点

2. 交换两个交叉点之间的基因片段

3. 建立映射关系

4. 修复冲突

父代1：[1 2 | 3 4 5 | 6 7]

父代2：[3 5 | 1 2 6 | 4 7]

子代1：[ ? | 1 2 6 | ? ] → 修复 → [3, 2, 1, 2, 6, 5, 7] → [3, 4, 1, 2, 6, 5, 7]

## PMX MATLAB 代码

```matlab
function [c1, c2] = pmx_crossover(p1, p2)
    n = length(p1);
    % 选择两个交叉点
    pos1 = randi(n-1);
    pos2 = randi([pos1+1, n]);
    c1 = zeros(1, n);
    c2 = zeros(1, n);
    % 复制中间片段
    c1(pos1:pos2) = p1(pos1:pos2);
    c2(pos1:pos2) = p2(pos1:pos2);
    % 建立映射并修复
    for i = pos1:pos2
    % 修复c1
    if ~ismember(p2(i), c1)
    % 找到p2(i)在p1中的位置
    idx = find(p1 == p2(i));
    % 追踪映射链
    while c1(idx) ~= 0
    idx = find(p1 == p2(idx));
    end
    c1(idx) = p2(i);
    end
    % 类似修复c2
end
% 填入剩余位置
% ...（完整实现略）
end
```

## 排列编码交叉——OX 与 CX

顺序交叉（OX）：

\- 保留一个父代的相对顺序

\- 适合需要保持顺序的问题

循环交叉（CX）：

\- 基于循环结构交换基因

\- 保持绝对位置不变

<table><tr><td>交叉方式</td><td>特点</td><td>适用场景</td></tr><tr><td>PMX</td><td>保持绝对位置</td><td>路径问题</td></tr><tr><td>OX</td><td>保持相对顺序</td><td>顺序依赖问题</td></tr><tr><td>CX</td><td>保持循环结构</td><td>循环调度</td></tr></table>

## 变异算子概述

变异是遗传算法的开发算子：

\- 模拟生物繁殖过程中的基因突变

\- 在个体上产生微小随机变化

\- 作用是维持种群多样性，避免陷入局部最优

变异率 $p_{m}$ :

\- 通常设为 $0.01 \sim 0.1$

\- 控制变异操作的使用频率

提问：变异率过大或过小会分别导致什么问题？

各种变异算子

<table><tr><td>编码方式</td><td>变异算子</td><td>操作</td></tr><tr><td>二进制</td><td>位翻转</td><td>以概率 翻转每一位</td></tr><tr><td>实数</td><td>高斯变异</td><td> $x' = x + N(0, \sigma)$ </td></tr><tr><td>实数</td><td>均匀变异</td><td> $x' \sim U(L, U)$ </td></tr><tr><td>排列</td><td>交换变异</td><td>随机交换两个位置</td></tr><tr><td>排列</td><td>插入变异</td><td>将某元素插入到新位置</td></tr><tr><td>排列</td><td>倒置变异</td><td>反转子序列</td></tr></table>

## 变异算子 MATLAB 代码

```matlab
% 位翻转
function child = bit_flip(parent, pm)
    child = parent;
    for i = 1:length(parent)
    if rand < pm
    child(i) = 1 - child(i);
    end
    end
end
% 高斯变异
function child = gaussian_mutation(parent, sigma, lb, ub)
    child = parent + sigma * randn(size(parent));
    child = min(max(child, lb), ub);
end
% 交换变异（排列）
function child = swap_mutation(parent)
    n = length(parent);
    idx = randperm(n, 2);
    child = parent;
    child(idx(1)) = parent(idx(2));
    child(idx(2)) = parent(idx(1));
end
```

关键参数一览

<table><tr><td>参数</td><td>含义</td><td>典型值</td><td>影响</td></tr><tr><td>N</td><td>种群大小</td><td>20-200</td><td>大:搜索充分但慢;小:快但易早熟</td></tr><tr><td> $p_c$ </td><td>交叉率</td><td>0.6-0.95</td><td>大:探索能力强;小:收敛快</td></tr><tr><td> $p_m$ </td><td>变异率</td><td>0.01-0.1</td><td>大:多样性好但易破坏优良解</td></tr><tr><td> $G_{max}$ </td><td>最大代数</td><td>100-1000</td><td>影响搜索深度</td></tr><tr><td>k</td><td>锦标赛大小</td><td>2-4</td><td>大:选择压力大;小:多样性好</td></tr><tr><td>e</td><td>精英数</td><td>1-2</td><td>保证收敛,一般为1-2</td></tr></table>

## 种群大小的影响

## 选择建议：

\- 简单问题: $N = 20 - 50$

\- 复杂问题： $N = 100 - 200$

\- 经验公式： $N \propto n$ （变量数）

![](images/95894784323a6563ec47233c1d44977ce1e1731ff2153748a85723276a18e684.jpg)

## 收敛判断与终止条件

收敛：种群逐渐趋同，最优解不再改善

常用终止条件:

1. 最大代数: $t > G_{max}$

2. 最优适应度阈值： $F_{best} \geq F_{target}$

3. 停滞判断： $|F_{best}^{t} - F_{best}^{t - \Delta}| < \epsilon$

4. 计算时间限制

收敛曲线：记录每代的最优适应度，观察算法进展

提问：如何判断算法是否已经收敛？

## 早熟收敛问题

早熟收敛：算法过早收敛到局部最优

种群多样性丧失

无法探索新区域

陷入局部最优

无法找到全局最优

## 预防策略：

1. 增大种群规模

2. 使用合适的变异率

3. 采用多样性保持机制（小生境、拥挤距离）

4. 使用自适应参数

## 自适应遗传算法

思想：根据种群状态动态调整参数

![](images/c6a0e80b6fb479c15929f4e144b59c717892d51803e1d1ba2641a6985e8d7905.jpg)

自适应交叉率:

自适应变异率:

$$
p _ {c} = p _ {c 0} \cdot \frac {F _ {m a x} - F _ {a v g}}{F _ {m a x} - F _ {m i n}}
$$

$$
p _ {m} = p _ {m 0} \cdot \frac {F _ {m a x} - F}{F _ {m a x} - F _ {a v g}}
$$

# MATLAB GA 工具箱简介

MATLAB 自带 ga 函数:

% 实数编码

[x, fval] = ga(@fitness, nvars, A, b, Aeq, beq, lb, ub, nonlcon, IntCon, options);

% 参数说明:

% @fitness - 适应度函数句柄

% nvars - 变量个数

% lb, ub - 变量下界和上界

% IntCon - 整数变量索引 (1-based)

% options - 算法参数设置

## 整数约束:

IntCon = [1, 3, 5]; % 第1、3、5个变量为整数

## 自定义算子与参数设置

## % 设置算法参数

```txt
options = optimoptions('ga', ...
'PopulationSize', 100, ...
'MaxGenerations', 500, ...
'CrossoverFraction', 0.8, ...
'MutationFcn', @mutationadaptfeasible, ...
'Display', 'iter', ...
'PlotFcn', {@gaplotbestf, @gaplotscorediversity});
```

```txt
% 运行GA
[x, fval, exitflag, output, population, scores]
= ...
ga(@fitness, nvars, A, b, [], [], lb, ub, [], IntCon, options);
```

算例1：函数优化（Rastrigin函数）

问题描述：最小化 Rastrigin 函数

$$
f (\pmb {x}) = 1 0 n + \sum_ {i = 1} ^ {n} \left[ x _ {i} ^ {2} - 1 0 \cos (2 \pi x _ {i}) \right]
$$

其中 $x_{i}\in [-5.12,5.12]$ ， $n$ 为变量个数。

特点：

\- 多峰函数，有大量局部最优解

\- 全局最优在 $x = 0, f = 0$

编码方式：实数编码

## 算例1: MATLAB 代码

```matlab
% Rastrigin 函数
function f = rastrigin(x)
    n = length(x);
    f = 10*n + sum(x.^2 - 10*cos(2*pi*x));
end
% 主程序
nvars = 2;
lb = -5.12 * ones(1, nvars);
ub = 5.12 * ones(1, nvars);
options = optimoptions('ga', ...
    'PopulationSize', 50, ...
    'MaxGenerations', 200, ...
    'Display', 'iter', ...
    'PlotFcn', @gaplotbestf);
[x_opt, fval] = ga(@rastrigin, nvars, [], [], [], [], lb, ub, [], options);
fprintf('最优解: x = [%.4f, %.4f]\n', x_opt(1), x_opt(2));
fprintf('最优值: f = %.4f\n', fval);
```

## 算例1：结果分析

收敛曲线：展示最优适应度随代数变化

提问：为什么 Rastrigin 函数难优化？遗传算法是如何克服的？

参数敏感性分析:

\- 种群大小的影响

\- 变异率的影响

<table><tr><td>参数组合</td><td>最优值</td><td>收敛代数</td></tr><tr><td>N=20, pm=0.01</td><td>0.123</td><td>150</td></tr><tr><td>N=50, pm=0.05</td><td>0.002</td><td>80</td></tr><tr><td>N=100, pm=0.02</td><td>0.000</td><td>45</td></tr></table>

## 算例2：0-1背包问题

问题描述:

• 有 n 个物品，每个物品有重量 $w_{i}$ 和价值 $v_{i}$

\- 背包容量为 $W$

\- 选择物品使总价值最大，且总重量不超过容量

$$
\begin{array}{r} {{\mathrm{最大化} \sum_ {i = 1} ^ {n} v _ {i} x _ {i}}} \\ {{\mathrm{约束} \sum_ {i = 1} ^ {n} w _ {i} x _ {i} \leq W, \quad x _ {i} \in \{0, 1 \}}} \end{array}
$$

编码方式：二进制编码

## 算例2: MATLAB 代码

```matlab
% 数据
n = 20;
w = randi([1, 10], 1, n);
v = randi([1, 20], 1, n);
W = 50;

% 适应度函数（带惩罚）
function fit = knapsack_fitness(x)
    total_w = sum(w .* x);
    total_v = sum(v .* x);
    if total_w > W
    fit = total_v - 100 * (total_w - W); % 惩罚
    else
    fit = total_v;
    end
end
% 遗传算法设置
options = optimoptions('ga', 'PopulationSize', 50, 'MaxGenerations', 100);
IntCon = 1:n; % 所有变量为整数
lb = zeros(1, n);
ub = ones(1, n);

[x_opt, fval] = ga(@knapsack_fitness, n, [], [], [], [], lb, ub, [],
IntCon, options);
```

## 算例3: TSP 问题

问题描述：旅行商从起点出发，访问所有城市后返回，求最短路径难点：

\- 组合爆炸： $n$ 个城市有 $(n - 1)! / 2$ 条路径

• 20个城市有约 $10^{16}$ 条路径

编码方式：排列编码

关键设计：

\- 个体：城市访问顺序

\- 适应度： $F = 1 / D$ （D为总距离）

\- 交叉: PMX或OX

\- 变异：交换或倒置

## 算例3: MATLAB 框架

```matlab
% 城市坐标
cities = 10 * rand(20, 2);

% 计算距离矩阵
D = pdist2(cities, cities);

% 适应度函数
function dist = tsp_fitness(route)
    dist = 0;
    for i = 1:length(route) - 1
    dist = dist + D(route(i), route(i+1));
    end
    dist = dist + D(route(end), route(1)); % 返回起点
end

% 注意: MATLAB ga 默认不支持排列编码
% 需要使用自定义交叉和变异算子
% 或使用第三方工具箱
```

## GA的优点

1. 不依赖于梯度信息
- 适用于不可导、不连续的问题
- 适用于黑盒优化
2. 全局搜索能力强
- 同时探索解空间多个区域
- 不易陷入局部最优
3. 并行性
- 隐式并行，适合并行计算
- 天然适合GPU加速
4. 灵活性强
- 可处理各种类型的决策变量
- 可结合其他启发式算法
5. 鲁棒性好
- 对问题数学性质要求低
- 适合工程实际应用

## GA 的缺点

1. 收敛速度慢
- 需要大量函数评估
- 接近最优解时收敛慢
2. 参数敏感
- 性能依赖参数设置
- 需要经验调参
3. 不保证最优性
- 不能保证找到全局最优
- 结果是概率性的
4. 理论支撑不足
- 理论分析困难
- 缺乏严格的收敛保证
5. 计算代价高
- 大规模问题计算量大
- 复杂适应度函数计算慢

## 适用场景总结

## 使用 GA 的场景:

\- 目标函数复杂（非线性、非凸、不可导）

\- 搜索空间大且不规则

\- 需要全局最优（而非局部最优）

\- 没有现成的梯度信息

\- 可接受较长的计算时间

## 不使用 GA 的场景:

\- 问题有解析解

\- 对求解时间要求严格

\- 需要严格的最优性保证

\- 目标函数是线性的（用线性规划更快）

提问：你的研究或工作中，哪些问题适合用遗传算法解决？

## 练习题1：概念理解

题目：请解释遗传算法中“选择”、“交叉”、“变异”三个算子的作用，并说明它们各自模拟了生物进化中的哪些机制。

## 要求：

1. 分别说明三个算子的功能

2. 分析三个算子之间的平衡关系

3. 举例说明如果缺少某个算子会怎样

## 提示:

\- 选择 $\rightarrow$ 优胜劣汰

\- 交叉 $\rightarrow$ 基因重组

\- 变异 $\rightarrow$ 基因突变

## 练习题2：编码设计

题目：考虑一个生产调度问题：有5个工件需要在3台机器上加工，每个工件需要按指定顺序经过多台机器。请设计一种遗传算法的编码方式。

要求:

1. 说明采用什么编码方式

2. 给出一个具体的编码示例

3. 讨论该编码的优点和可能的局限性

提示：可以尝试排列编码 + 整数编码的组合

## 练习题3：算子应用

题目：给定两个排列编码的父代个体：

• P1 = [2, 4, 1, 5, 3, 6]

• P2 = [3, 5, 2, 1, 6, 4]

请分别使用：

1. 单点交叉（交叉点位置为3）

2. 交换变异（交换位置2和5）

计算产生的子代个体，并说明操作过程。

## 练习题4：参数分析

题目：假设您要用遗传算法求解一个包含100个变量的连续优化问题，请设计一组参数设置并说明理由。

## 需要指定的参数：

1. 种群大小

2. 交叉率

3. 变异率

4. 精英数

5. 最大代数

6. 选择方式

要求：解释每个参数选择的依据，说明它们之间的相互影响。

## 练习题5：综合应用

题目：考虑一个简单的设施选址问题：有10个候选位置和50个需求点，需要选择3个位置建设施，使总覆盖距离最小。

要求:

1. 建立问题的数学模型

2. 设计遗传算法的编码方式

3. 设计适应度函数（包含约束处理）

4. 选择合适的交叉和变异算子

5. 用伪代码描述算法

加分项：考虑算法参数如何随问题规模调整。

## 课程总结

本课程核心知识点回顾：

1. 基本原理：模拟生物进化的群体搜索策略

2. 算法流程：初始化 → 评估 → 选择 → 交叉 → 变异 → 替换

3. 核心算子：选择、交叉、变异（必须与编码匹配）

4. 四种编码：二进制、实数、整数、排列

5. 参数设置：N、 $p_{c}$ 、 $p_{m}$ 、 $G_{max}$

## 讨论

## 讨论问题:

1. 遗传算法在你所在领域有哪些潜在应用？

2. 你认为遗传算法的最大优势是什么？

3. 如果要改进遗传算法，你会从哪个方向入手？