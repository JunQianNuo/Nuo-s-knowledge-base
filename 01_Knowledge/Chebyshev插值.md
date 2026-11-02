---
schema_version: 2
type: method
source:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/07-插值法-知识梳理]]'
- '[[03_Sources/Reviews/归档/数值分析/复习/VI-插值法]]'
- '[[03_Sources/Reviews/归档/数值分析/归档合并记录/Chebyshev节点选取流程]]'
legacy_topics:
- Chebyshev插值
- 插值节点
- 最优逼近
- Runge现象
tags:
- Chebyshev插值
- Runge现象
topics:
- '[[02_Maps/MOC-数值计算]]'
time: '2026-08-31T11:44:20+08:00'
aliases:
- Chebyshev节点选取流程
legacy_status: 已整理
---

# Chebyshev插值

## 适用场景
需要高精度多项式插值且可自由选取节点时，用 Chebyshev 节点代替等距节点，减轻等距高次插值的边界振荡；对任意连续函数并无无条件一致收敛保证。

## 核心公式/步骤

1. 将目标区间 $[a,b]$ 映射到 $[-1,1]$：$\boxed{t=\frac{2x-(a+b)}{b-a}}$
2. 在 $[-1,1]$ 上计算 Chebyshev 节点（$n+1$ 个）：
   $\boxed{t_k=\cos\left(\frac{(2k+1)\pi}{2n+2}\right)}$，$k=0,1,\ldots,n$
3. 逆向映射回 $[a,b]$：$\boxed{x_k=\frac{a+b}{2}+\frac{b-a}{2}t_k}$
4. 在 Chebyshev 节点 $\{x_k\}$ 上构造 Lagrange 或 Newton 插值多项式
5. 若 $f\in C^{n+1}[a,b]$，插值误差上界为 $\boxed{\|f-P_n\|_\infty\le\frac{(b-a)^{n+1}}{2^{2n+1}(n+1)!}\|f^{(n+1)}\|_\infty}$

```mermaid
flowchart TD
    A["确定区间 [a,b] 和节点数 n+1"] --> B["映射到 [-1,1]\nt = (2x-(a+b))/(b-a)"]
    B --> C["计算 Chebyshev 节点\nx_k = cos((2k+1)π/(2n+2))"]
    C --> D["逆向映射回 [a,b]\nx_k = (a+b)/2 + (b-a)t_k/2"]
    D --> E["在 Chebyshev 节点上\n构造 Lagrange/Newton 插值"]
    E --> F["评估误差上界\n≤ (b-a)^{n+1}/(2^{2n+1}(n+1)!)·||f^{(n+1)}||"]
    F --> G["输出插值多项式"]
```

## 典型例题

> **题目**：在 $[-1,1]$ 上用 5 个 Chebyshev 节点插值 $f(x)=1/(1+25x^2)$，与等距节点对比。

> [!example]- 解答
> Chebyshev 节点（$n=4$）：$t_k=\cos(\frac{(2k+1)\pi}{10})$ → $\approx\pm0.951,\pm0.588,0$
> 对本例的五节点插值，密网格复算最大误差约为：等距 0.43836、Chebyshev 0.40202。此处改善有限；经典 Runge 现象主要讨论节点数不断增加时的表现。
> 点评：Chebyshev 零点使首一节点多项式 $\prod_{k=0}^n(x-x_k)$ 的一致范数最小，从而优化上述导数误差上界；这不等于对给定 $f$ 的实际插值误差最小，也不等于最佳一致逼近多项式。

## 链接的知识点
- [[01_Knowledge/Chebyshev插值]]
- [[01_Knowledge/Lagrange插值]]

## 链接的习题
- [[03_Sources/Courses/归档/数值分析/习题库/07-插值法/README|第7章习题库]]


## 延伸材料

完整历史例题与补充说明见 [[03_Sources/Reviews/归档/数值分析/归档合并记录/Chebyshev节点选取流程]]。
