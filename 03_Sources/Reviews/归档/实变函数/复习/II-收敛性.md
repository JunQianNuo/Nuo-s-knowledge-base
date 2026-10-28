---
subject:
- 实变函数
type: review
source:
- 考试范围.txt, 知识图谱.png
tags:
- 几乎处处收敛
- 几乎一致收敛
- 依测度收敛
- Egorov定理
- Riesz定理
- Lusin定理
aliases:
- II. 收敛性 — 复习
schema_version: 2
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- 几乎处处收敛
- 几乎一致收敛
- 依测度收敛
- Egorov定理
- Riesz定理
- Lusin定理
status: not done
---

# II. 收敛性

> 一句说清：可测函数列有四种收敛——从强到弱：一致 → 几乎一致 → 几乎处处/依测度。有限测度下 Egorov 定理把 a.e. 拉回到 a.u.，Riesz 定理把依测度"拉"出 a.e. 子列。

> [!important] 考试重点
> **只考各种收敛的定义及它们之间的关系**。测度定义、可列可加性等不考。

---

## 一、核心定义速查

### 1.1 四种收敛定义

| 收敛类型 | 定义 | 记号 |
|:--|:--|:--:|
| **一致收敛** | $\forall\varepsilon>0,\exists K,\forall k\geq K,\forall x\in E: \lvert f_k-f\rvert<\varepsilon$ | $f_k\rightrightarrows f$ |
| **几乎一致收敛** | $\forall\delta>0,\exists E_\delta\subset E,m(E\setminus E_\delta)<\delta$，在 $E_\delta$ 上 $f_k\rightrightarrows f$ | $f_k\xrightarrow{a.u.}f$ |
| **几乎处处收敛** | $\exists Z,m(Z)=0,\forall x\in E\setminus Z:\lim f_k(x)=f(x)$ | $f_k\xrightarrow{a.e.}f$ |
| **依测度收敛** | $\forall\varepsilon>0,\lim_k m(E(\lvert f_k-f\rvert>\varepsilon))=0$ | $f_k\xrightarrow{m}f$ |

### 1.2 核心对比

| 收敛 | 关注什么 | 控制对象 |
|:--|:--|:--|
| 一致 | 最坏点的误差 | 统一的 $K$，对所有 $x$ |
| 几乎一致 | 切除小测度集后一致 | 坏集的测度 $<\delta$ |
| 几乎处处 | 除零测集外逐点收敛 | 发散集测度为 $0$ |
| 依测度 | 偏离超 $\varepsilon$ 的测度 $\to 0$ | $m(\{\text{偏差}\})\to 0$ |

---

## 二、核心定理

### 2.1 Egorov 定理（定理 2.3.3）★★★

**定理**：$m(E)<\infty$，$f_k\xrightarrow{a.e.}f$ $\Rightarrow$ $f_k\xrightarrow{a.u.}f$。

> 一句话：有限测度上，a.e. 收敛"几乎"就是一致收敛——丢掉一个测度任意小的集即可。

**反例（$m(E)=\infty$）**：$E=(0,\infty)$，$f_k=\chi_{(0,k)}$，处处收敛到 $f\equiv 1$，但不 a.u. 收敛。

### 2.2 Riesz 定理（定理 2.3.7）★★★

**定理**：$f_k\xrightarrow{m}f$ $\Rightarrow$ 存在子列 $\{f_{k_i}\}$ 使 $f_{k_i}\xrightarrow{a.e.}f$。

> 一句话：依测度收敛虽然弱，但总能抽出 a.e. 收敛的子列。

**证明核心**：取 $k_1<k_2<\cdots$ 使 $m(E(\lvert f_{k_i}-f\rvert\geq 2^{-i}))<2^{-i}$，则子列在 $\varlimsup E_i$ 之外处处收敛。

### 2.3 依测度极限唯一性（定理 2.3.5）

**定理**：$f_k\xrightarrow{m}f$ 且 $f_k\xrightarrow{m}g$ $\Rightarrow$ $f=g$ a.e.。

### 2.4 依测度基本列完备性（定理 2.3.9）

**定理**：$f_k\xrightarrow{m}f$ $\iff$ $\{f_k\}$ 是依测度基本列（$\lim_{k,j}m(E(\lvert f_j-f_k\rvert>\varepsilon))=0$）。

### 2.5 Lusin 定理（定理 2.3.10）★

**定理**：$f\in\mathfrak{M}(E)$ 几乎处处有限 $\Rightarrow$ $\forall\delta>0$，存在闭集 $F\subset E$，$m(E\setminus F)<\delta$，使 $f$ 在 $F$ 上连续。

> 一句话：任何可测函数丢掉小测度集后就是连续的。

---

## 三、收敛关系图（核心）

```
一致收敛 ⟹ 几乎一致收敛 ⟹ 几乎处处收敛
              ⟹ 依测度收敛 (有限测度下，a.e. 也蕴含依测度)
依测度收敛 ⟹ 存在子列几乎处处收敛 (Riesz)
```

**关键蕴含关系**（$m(E)<\infty$ 且函数 a.e. 有限时）：

| 蕴含 | 是否成立 | 条件/定理 |
|:--|:--:|:--|
| $f_k\rightrightarrows f \Rightarrow f_k\xrightarrow{a.u.}f$ | ✅ | $\delta$ 任意时取 $E_\delta=E$ |
| $f_k\xrightarrow{a.u.}f \Rightarrow f_k\xrightarrow{a.e.}f$ | ✅ | 取 $Z=E\setminus\bigcup_n E_{1/n}$ |
| $f_k\xrightarrow{a.u.}f \Rightarrow f_k\xrightarrow{m}f$ | ✅ | 显然 |
| $f_k\xrightarrow{a.e.}f \Rightarrow f_k\xrightarrow{a.u.}f$ | ✅ | Egorov（需 $m(E)<\infty$） |
| $f_k\xrightarrow{a.e.}f \Rightarrow f_k\xrightarrow{m}f$ | ✅ | 由 Egorov（需 $m(E)<\infty$） |
| $f_k\xrightarrow{m}f \Rightarrow f_k\xrightarrow{a.e.}f$ | ❌ | 反例：$[0,1)$ 上的"移动脉冲"列 |
| $f_k\xrightarrow{m}f \Rightarrow$ 子列 $\xrightarrow{a.e.}f$ | ✅ | Riesz 定理 |

---

## 四、典型考题

### 4.1 经典反例（"移动脉冲"）

$E=[0,1)$，$f_k(x)=\chi_{[j/2^i,(j+1)/2^i)}(x)$，$k=2^i+j$（$0\leq j<2^i$）。

- 依测度收敛于 $0$（支撑区间长度 $\to 0$）
- 但**在任何点处都不收敛**（每点都有无穷多次取 $1$）
- Riesz 定理只能抽出子列 a.e. 收敛，不能说原列 a.e. 收敛

### 4.2 判断收敛类型

给定具体函数列，判断属于哪种收敛并给出证明：
- 先判断是否一致收敛（最严格）
- 若否，看是否 a.u. 收敛
- 若否，看是否 a.e. 收敛
- 若否，看是否依测度收敛

---

## 五、易错点

> [!warning] Egorov 需要 $m(E)<\infty$
> $m(E)=\infty$ 时不成立。反例：$\chi_{(0,k)}$ 在 $(0,\infty)$ 上。

> [!warning] 依测度收敛 $\not\Rightarrow$ 几乎处处收敛
> "移动脉冲"反例说明原列可以不收敛。Riesz 只能保证**子列** a.e. 收敛。

> [!warning] Littlewood 三原理
> ① 可测集 ≈ 有限个区间的并 ② 可测函数 ≈ 连续函数（Lusin） ③ a.e. 收敛 ≈ 一致收敛（Egorov）。核心思想：一切"坏"的东西都可控制在任意小的测度内。

---

## 六、相关知识点梳理

| 链接 | 内容 |
|:--|:--|
| [[03_Sources/Reviews/归档/实变函数/知识点解析梳理/03-可测函数-知识梳理#六、可测函数列的收敛性（本章核心 / 难点）]] | 四种收敛完整定义与关系 |
| [[03_Sources/Reviews/归档/实变函数/知识点解析梳理/03-可测函数-知识梳理#七、收敛性之间的关系——三大定理（核心 / 难点）]] | Egorov/Riesz/Lusin 详细证明 |

## 七、作业回顾

- 判断具体函数列属于哪种收敛（一致/a.u./a.e./依测度）
- 构造反例说明四种收敛间不可逆的蕴含关系
- 验证 Egorov 定理条件：为什么需要 $m(E)<\infty$
- Riesz 定理应用中子列的选择
