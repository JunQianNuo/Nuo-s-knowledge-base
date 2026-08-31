---
title: Riesz定理
type: 知识点
subject: 实变函数
source:
  - 课程/实变函数/知识点解析梳理/03-可测函数-知识梳理.md
topics:
  - 依测度收敛
  - 几乎处处收敛
  - 子列
  - Riesz定理
exam: 考试重点
---

# Riesz定理

## 一句话

依测度收敛不保证几乎处处收敛，但总能抽出一个几乎处处收敛的子列——Riesz 定理是两种收敛性之间唯一的桥梁。

## 严格定义

设 $f_n, f$ 是可测集 $E$ 上的 a.e. 有限的可测函数。若 $f_n \xrightarrow{m} f$（即 $f_n$ 在 $E$ 上**依测度收敛**于 $f$），则存在子列 $\{f_{n_k}\}$ 使得

$$
\boxed{f_{n_k} \xrightarrow{\text{a.e.}} f \quad (k \to \infty)}
$$

即子列在 $E$ 上**几乎处处收敛**于 $f$。

> [!important] 关键条件与结论
> - **前提**：$f_n \xrightarrow{m} f$（依测度收敛），$E$ 为一般可测集（不要求 $m(E) < \infty$）
> - **结论**：存在子列 a.e. 收敛，**不是**原序列 a.e. 收敛
> - **反例**：打字机序列 $\{\chi_{[0,1)},\;\chi_{[0,\frac{1}{2})},\;\chi_{[\frac{1}{2},1)},\;\chi_{[0,\frac{1}{3})},\;\cdots\}$ 依测度收敛于 $0$，但不 a.e. 收敛；然而可以抽出子列 $\chi_{[0,1)},\chi_{[0,\frac{1}{2})},\chi_{[0,\frac{1}{3})},\cdots$ 使 a.e. 收敛于 $0$

## 推导：核心步骤

> [!proof]- 推导
> **思路**：利用依测度收敛的定义，对合适的 $\varepsilon_k \to 0$ 逐层选取子列指标 $n_k$，再通过 Borel-Cantelli 引理证明子列在除去一个零测集外逐点收敛。
>
> **第一步：构造子列指标**。由 $f_n \xrightarrow{m} f$，取 $\varepsilon_k = 1/2^k$。对每个 $k$，存在 $n_k$（可取 $n_1 < n_2 < \cdots$）使得
> $$
> m\bigl(E_k\bigr) < \frac{1}{2^k}, \quad E_k := \bigl\{x \in E : |f_{n_k}(x) - f(x)| > \tfrac{1}{2^k}\bigr\}
> $$
>
> **第二步：构造零测集 $A$（发散点集）**。令
> $$
> A := \bigcap_{N=1}^{\infty} \bigcup_{k=N}^{\infty} E_k = \limsup_{k \to \infty} E_k
> $$
> 由 Borel-Cantelli 引理，$\sum_{k=1}^{\infty} m(E_k) < \sum_{k=1}^{\infty} 1/2^k = 1 < \infty$，故 $m(A) = 0$。
>
> **第三步：在 $A$ 之外逐点收敛**。若 $x \notin A$，则 $x$ 只属于有限个 $E_k$，即存在 $K$ 使得 $\forall k \geq K$，$|f_{n_k}(x) - f(x)| \leq 1/2^k \to 0$。因此 $f_{n_k}(x) \to f(x)$ 对所有 $x \in E \setminus A$ 成立。$\square$
>
> **核心技巧**：$\varepsilon_k$ 的选取需保证 $\sum m(E_k) < \infty$ 以触发 Borel-Cantelli 引理；子列指标依赖 $\varepsilon_k$ 的选取，并非任意子列都有效。

## 关键性质

| 性质 | 说明 |
|:-----|:-----|
| 前提强度 | 仅需 $f_n \xrightarrow{m} f$，不要求 $m(E) < \infty$（区别于 Egorov 定理） |
| 结论强度 | 子列 a.e. 收敛（比原序列 a.e. 收敛弱） |
| 子列选取 | 非任意子列，须按 $\varepsilon_k = 1/2^k$ 逐层构造 |
| 核心工具 | Borel-Cantelli 引理（$\sum m(E_k) < \infty \Rightarrow m(\limsup E_k) = 0$） |
| 与 Egorov 对比 | Egorov 要求 $m(E) < \infty$ 且结论为近一致收敛；Riesz 不要求有限测度，结论为子列 a.e. 收敛 |
| 与几乎一致收敛关系 | 几乎一致收敛 $\Rightarrow$ 依测度收敛 $\Rightarrow$ 存在子列 a.e. 收敛 |

## 典型例题

> **题目**：设打字机序列 $f_n = \chi_{I_n}$，其中 $I_1 = [0,1)$，$I_2 = [0,\frac{1}{2})$，$I_3 = [\frac{1}{2},1)$，$I_4 = [0,\frac{1}{3})$，$I_5 = [\frac{1}{3},\frac{2}{3})$，$I_6 = [\frac{2}{3},1)$，$I_7 = [0,\frac{1}{4})$，$\cdots$。验证：（1）$f_n \xrightarrow{m} 0$ 在 $[0,1)$ 上成立；（2）原序列不 a.e. 收敛；（3）按 Riesz 定理构造一个 a.e. 收敛于 $0$ 的子列。

> [!example]- 解答
> **（1）依测度收敛**：对任意 $\varepsilon \in (0,1)$，$E(|f_n - 0| > \varepsilon) = I_n$。第 $k$ 轮共有 $k$ 个子区间，每个长度 $1/k$，故 $m(I_n) \to 0$。因此 $m(E(|f_n - 0| > \varepsilon)) \to 0$，即 $f_n \xrightarrow{m} 0$。
>
> **（2）不 a.e. 收敛**：对任意 $x \in [0,1)$，$x$ 出现在无穷多个 $I_n$ 中（每轮各区间覆盖 $[0,1)$），故有无穷多项 $f_n(x) = 1$；同时 $x$ 也错过无穷多个 $I_n$，有无穷多项 $f_n(x) = 0$。因此 $\lim f_n(x)$ 对任意 $x$ 都不存在，原序列处处不收敛。不存在，原序列处处不收敛。
>
> **（3）构造 a.e. 收敛子列**：取每轮的第一个函数即可：
> $$
> f_{n_1} = \chi_{[0,1)},\; f_{n_2} = \chi_{[0,\frac{1}{2})},\; f_{n_3} = \chi_{[0,\frac{1}{3})},\; f_{n_4} = \chi_{[0,\frac{1}{4})},\; \cdots
> $$
> 对任意 $x \in (0,1)$，当 $k > 1/x$ 时 $x \notin [0, 1/k]$，故 $f_{n_k}(x) = 0$。因此 $f_{n_k} \to 0$ a.e.（仅 $x=0$ 处例外，但单点集为零测集）。
>
> **点评**：打字机序列是展示 Riesz 定理必要性的标准反例——依测度收敛不保证 a.e. 收敛，但"第一个区间"子列即可 a.e. 收敛，完美呼应 Riesz 定理的结论。

## 易错点

> [!warning] 易错点 1：子列 vs 原序列
> Riesz 定理只保证**存在某个子列** a.e. 收敛，并非原序列本身 a.e. 收敛。打字机序列原序列处处不收敛，但子列可以 a.e. 收敛。

> [!warning] 易错点 2：Borel-Cantelli 的 $\sum m(E_k) < \infty$ 条件
> 子列选取时 $\varepsilon_k$ 必须满足 $\sum m(E_k) < \infty$。若取 $\varepsilon_k = 1/k$ 且 $m(E_k) = 1/k$，则 $\sum m(E_k)$ 发散，Borel-Cantelli 无法得出 $m(A) = 0$。

> [!warning] 易错点 3：子列非任意
> 不能从任意子列断言 a.e. 收敛。Riesz 定理构造的子列是特定的（依赖 $\varepsilon_k$ 的选取），打字机序列中若取子列仅含每轮的第二个区间，仍不 a.e. 收敛。

## 相关概念

- [[概念/实变函数/依测度收敛]]
- [[概念/实变函数/几乎处处收敛]]
- [[概念/实变函数/几乎一致收敛]]
- [[概念/实变函数/可测函数]]
- [[概念/实变函数/零测集]]

## 习题

- [[课程/实变函数/习题库/03-可测函数/README|第3章习题库]] — 习题 3.22（Riesz定理：依测度收敛蕴含几乎处处收敛子列）
- [[课程/实变函数/习题库/03-可测函数/习题3.18-依测度收敛但不逐点收敛（打字机序列）-习题|习题 3.18]] — 打字机序列（反例）
- [[课程/实变函数/习题库/03-可测函数/习题3.21-Egorov定理-习题|习题 3.21]] — Egorov 定理（对比）
