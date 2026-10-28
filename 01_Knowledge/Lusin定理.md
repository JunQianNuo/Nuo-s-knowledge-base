---
schema_version: 2
type: proposition
source:
- '[[03_Sources/Reviews/归档/实变函数/知识点解析梳理/03-可测函数-知识梳理]]'
legacy_topics:
- Lusin定理
- Littlewood第二原理
- 可测函数
- 连续函数逼近
- Egorov定理
exam: 考试重点
tags:
- Lusin定理
- 可测函数
- Egorov定理
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
about:
- '[[01_Knowledge/可测函数]]'
legacy_topic_links:
- '[[01_Knowledge/可测函数]]'
- '[[01_Knowledge/Egorov定理]]'
time: "2026-08-31T11:44:20+08:00"
aliases: []
legacy_status: 已整理
---

# Lusin定理

## 一句话

任意可测函数去掉一个**任意小测度**的集合后，就变成了**连续函数**——可测函数"几乎"是连续的。

## 严格定义

**定理（Lusin / Littlewood 第二原理）**：设 $f$ 是 $E \subset \mathbb{R}^n$ 上**几乎处处有限**的可测函数。则对任意 $\delta > 0$，存在闭集 $F_\delta \subset E$，满足

$$
\boxed{m(E \setminus F_\delta) < \delta \quad \text{且} \quad f|_{F_\delta} \text{ 在 } F_\delta \text{ 上连续}}
$$

> [!important] 关键条件
> - $f$ 必须**几乎处处有限**（a.e. 取有限值），否则结论不成立。
> - 若 $E$ 有界，$F_\delta$ 可取为**紧集**。
> - 结论是 $f$ **限制在子集上**连续，不是 $f$ 在原定义域上连续。

## 推导：Lusin定理

> [!proof]- 推导
> **核心思路**：由特殊到一般——先证简单函数成立，再用简单函数列逼近一般可测函数，结合 Egorov 定理完成。
>
> **Step 1 — 简单函数情形**：
> 设 $\varphi = \sum_{k=1}^{n} c_k \chi_{E_k}$，其中 $E_k$ 两两不交且每个 $E_k$ 可测。
> 对每个 $E_k$，由可测集的内逼近性质，$\forall \varepsilon > 0$，存在闭集 $F_k \subset E_k$ 使得 $m(E_k \setminus F_k) < \varepsilon/n$。
> 令 $F = \bigcup_{k=1}^{n} F_k$，则 $F$ 是闭集（有限个闭集的并），且 $m(E \setminus F) < \varepsilon$。
> $\varphi|_F$ 在每个不相交的闭集 $F_k$ 上取常值 $c_k$，故在 $F$ 上连续。
>
> **Step 2 — 一般可测函数**：
> 存在简单函数列 $\varphi_n \to f$ a.e. 于 $E$。
> 对每个 $\varphi_n$，由 Step 1 存在闭集 $F_n \subset E$ 满足 $m(E \setminus F_n) < \delta/2^{n+1}$，且 $\varphi_n|_{F_n}$ 连续。
> 令 $F' = \bigcap_{n=1}^{\infty} F_n$，则 $F'$ 是闭集，且 $m(E \setminus F') \le \sum_{n=1}^{\infty} \delta/2^{n+1} = \delta/2$。
>
> **Step 3 — 利用 Egorov 定理**：
> 在 $F'$ 上 $\varphi_n \to f$ a.e.，由 Egorov 定理，存在闭集 $F_\delta \subset F'$ 满足 $m(F' \setminus F_\delta) < \delta/2$，使得 $\varphi_n \rightrightarrows f$ 在 $F_\delta$ 上**一致收敛**。
> 则 $m(E \setminus F_\delta) = m(E \setminus F') + m(F' \setminus F_\delta) < \delta/2 + \delta/2 = \delta$。
> 每个 $\varphi_n|_{F_\delta}$ 连续（因为 $F_\delta \subset F' \subset F_n$），且它们在 $F_\delta$ 上一致收敛于 $f|_{F_\delta}$，故 $f|_{F_\delta}$ 作为连续函数列的一致极限**也是连续的**。

## 关键性质

| 性质 | 内容 |
|:--|:--|
| 逆命题 | 若对任意 $\delta > 0$ 存在闭集 $F_\delta$ 使 $f|_{F_\delta}$ 连续且 $m(E \setminus F_\delta) < \delta$，则 $f$ 可测（Lusin 定理的逆也成立） |
| 范围 | 在 $\mathbb{R}^n$ 的 Lebesgue 测度空间上成立；更一般地，在正则测度空间上成立 |
| 与 Egorov 的关系 | Littlewood 三原理之二是 Lusin（可测≈连续），之三是 Egorov（a.e. 收敛≈一致收敛）；Lusin 定理的证明依赖 Egorov |
| 紧集版本 | 若 $E$ 有界，$F_\delta$ 可取为紧集（闭集 + 有界集 → 紧集） |
| 应用 | 用于将可测函数的性质转化为连续函数的性质（例如证明可测函数的逼近定理） |

## 典型例题

> **题目**：设 $f = \chi_{\mathbb{Q} \cap [0,1]}$ 为 Dirichlet 函数在 $[0,1]$ 上的限制。$f$ 在 $[0,1]$ 上处处不连续，验证 Lusin 定理对此函数成立——即对任意 $\delta > 0$，找到闭集 $F_\delta$ 满足定理条件。

> [!example]- 解答
> **分析**：$f$ 在有理点取 1，无理点取 0，实际上 $f = 0$ a.e.。需要去掉一个测度小于 $\delta$ 的集，使 $f$ 在剩余部分连续。
>
> **构造**：$\mathbb{Q} \cap [0,1]$ 是可数集，故 $m(\mathbb{Q} \cap [0,1]) = 0$。
> 对任意 $\delta > 0$，取 $F_\delta = [0,1] \setminus \mathbb{Q}$（即 $[0,1]$ 中全体无理数）。
> 则 $m([0,1] \setminus F_\delta) = m(\mathbb{Q} \cap [0,1]) = 0 < \delta$。
> $f|_{F_\delta} \equiv 0$，是常值函数，在 $F_\delta$ 上显然连续。
>
> **注**：$F_\delta = [0,1] \setminus \mathbb{Q}$ 不是闭集（无理数集在 $[0,1]$ 中不闭，其闭包是 $[0,1]$），但这不影响结论——Lusin 定理保证**存在**闭集，不一定是我们选的那个。实际上可如下修正：取开集 $U \supset \mathbb{Q} \cap [0,1]$ 满足 $m(U) < \delta$，令 $F_\delta = [0,1] \setminus U$，则 $F_\delta$ 是闭集，$f|_{F_\delta} \equiv 0$ 连续。
>
> **点评**：此例说明 Lusin 定理的强大之处——即使 Dirichlet 函数极其"不连续"（处处不连续），去掉一个零测集后立刻变成连续函数。这正是 Littlewood 第二原理的精髓：**可测函数"几乎"是连续的**。

## 易错点

> [!warning] 易错点 1：混淆"原函数连续"与"限制在子集上连续"
> Lusin 定理的结论是 $f$ **限制在** $F_\delta$ 上连续，不是说 $f$ 在原定义域 $E$ 上连续。Dirichlet 函数在 $[0,1]$ 上仍然处处不连续，但限制在无理数集上恒为 0 是连续的。

> [!warning] 易错点 2：忽视"几乎处处有限"条件
> 若 $f$ 在一个正测度集上取无穷值，Lusin 定理不成立。例如 $f(x) = +\infty$ 对所有 $x \in [0,1]$，去掉任意小测度集后仍有无穷值点，不可能连续。

> [!warning] 易错点 3：$\delta$ 越小 $F_\delta$ 可能越复杂
> $\delta \to 0$ 时 $F_\delta$ 逼近 $E$ 但 $F_\delta$ 本身的结构可能非常复杂（例如 $F_\delta$ 可能是完全集但不含任何区间）。

> [!warning] 易错点 4：在一般拓扑测度空间未必成立
> Lusin 定理依赖 $\mathbb{R}^n$ 中 Lebesgue 测度的正则性（可测集可由闭集从内逼近）。在一般的测度空间上需要额外条件。

## 相关概念

- [[01_Knowledge/可测函数]]
- [[01_Knowledge/简单函数]]
- [[01_Knowledge/几乎处处收敛]]
- [[01_Knowledge/几乎一致收敛]]
- [[01_Knowledge/零测集]]
- [[01_Knowledge/Egorov定理]]

## 习题

- [[03_Sources/Courses/归档/实变函数/作业/03-可测函数/习题3.24-Lusin定理（可测函数接近于连续函数）-习题|习题3.24 — Lusin定理]]
- [[03_Sources/Courses/归档/实变函数/作业/03-可测函数/习题3.25-可测函数可由连续函数列几乎处处逼近-习题|习题3.25 — 可测函数可由连续函数列 a.e. 逼近]]
- [[03_Sources/Courses/归档/实变函数/作业/03-可测函数/习题3.26-收敛性关系总图-习题|习题3.26 — 收敛性关系总图（含 Lusin）]]
