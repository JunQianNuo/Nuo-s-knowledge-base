---
title: 第7章 答疑 — 信赖域方法与Cauchy点
subject: 最优化方法
chapter: 7
type: 答疑
topics:
  - 信赖域方法
  - Cauchy点
  - 柯西点
  - 信赖域半径
  - τ参数化
  - 预测下降量
  - Lagrange函数
source_context:
  - file: "III-线搜索.md"
    line: 300
    text: "信赖域方法的思路：在 x_k 周围定义一个'信任区域'，只在这个区域内信任二次模型"
  - file: "III-线搜索.md"
    line: 323
    text: "Lagrange 函数：L(s,λ) = ½sᵀBs + gᵀs + (λ/2)(‖s‖² - r²)"
  - file: "III-线搜索.md"
    line: 352
    text: "τ_k = { 1, gᵀBg ≤ 0; min(1, ‖g‖³/(r·gᵀBg)), gᵀBg > 0 }"
  - file: "考题-信赖域Cauchy点.md"
    line: 20
    text: "s.t. ‖s‖ ≤ Δ"
  - file: "考题-信赖域Cauchy点.md"
    line: 91
    text: "无约束极小点在信赖域内部，因此 Cauchy 点取无约束极小点"
related_notes:
  - "[[../复习/III-线搜索]]"
  - "[[07-一维搜索方法-知识梳理]]"
  - "[[考题-信赖域Cauchy点]]"
  - "[[25-信赖域方法-知识梳理]]"
tags:
- 信赖域方法
- 柯西点
- 信赖域半径
- 预测下降量
---

# 第7章 答疑 — 信赖域方法与 Cauchy 点

> 问题：**我没搞懂信赖域方法——它和线搜索有什么区别？Lagrange 函数怎么来的？Cauchy 点怎么算？$\tau$ 公式里的 $r$ 是什么？**

> 来源：`III-线搜索.md` §6（第 300–393 行）；`考题-信赖域Cauchy点.md`

---

## 一、信赖域方法 vs 线搜索

### 一句话兜底

> 线搜索：先定方向，再沿方向调步长。信赖域：先定圈的范围，再在圈内全面搜最优。顺序反了。

### 为什么需要信赖域

牛顿法在两种场景下会崩：(1) Hessian 非正定时二次模型无极小；(2) 离解太远时二次近似不准。线搜索通过沿固定方向试探来解决，信赖域通过画圈限制步幅来解决。

### 完整流程

```
第 k 步：
  ① 在 xₖ 处画半径为 rₖ（或 Δ）的圈
  ② 在圈内解子问题：min q(s) = ½sᵀBs + gᵀs,  s.t. ‖s‖ ≤ rₖ
  ③ 得候选步 sₖ → x_{k+1} = xₖ + sₖ
  ④ 验货 ρₖ = 实际下降/预估下降
     ├ ρₖ ≈ 1（好）→ 接受，扩大 rₖ
     ├ ρₖ > 0（还行）→ 接受，rₖ 不变
     └ ρₖ ≤ 0（差）→ 拒绝，缩小 rₖ 重来
```

---

## 二、Lagrange 函数怎么来的

> 追问：**$\mathcal{L}(s, \lambda) = \frac{1}{2} s^T B s + g^T s + \frac{\lambda}{2}(\|s\|^2 - r^2)$ 这个式子是怎么写的？**

> 来源：`III-线搜索.md` 第 323 行

子问题 $\min \frac{1}{2}s^\top B s + g^\top s$ s.t. $\|s\| \leq r$。约束改写为标准 $\leq 0$ 形式 $\|s\|^2 - r^2 \leq 0$，标准 Lagrange 乘子法：

$$\mathcal{L}(s, \lambda) = \frac{1}{2}s^\top B s + g^\top s + \lambda(\|s\|^2 - r^2)$$

笔记写成 $\frac{\lambda}{2}$ 是故意的——对 $s$ 求导后 $\lambda$ 前面不会出现系数 2：

$$\nabla_s \mathcal{L} = Bs + g + \lambda s = 0 \quad \Rightarrow \quad (B + \lambda I)s = -g$$

---

## 三、Cauchy 点公式推导

> 追问：**Cauchy 点公式 $\tau_k = \min(1, \frac{\|g\|^3}{r \cdot g^\top B g})$ 怎么来的？$r$ 是什么？若不在信赖域内怎么办？为什么套公式得到 0.86 而不是 5/13？**

> 来源：`III-线搜索.md` 第 352–359 行；`考题-信赖域Cauchy点.md` 第 41–93 行

### 3.1 推导五步

**Step 1**：沿负梯度方向参数化 $s = -\tau g$（$\tau \ge 0$）。

**Step 2**：代入 $q(s) = \frac{1}{2}s^\top B s + g^\top s$，得到一元二次函数：

$$q(-\tau g) = \frac{g^\top B g}{2} \tau^2 - \|g\|^2 \tau$$

**Step 3**：求无约束极小点。当 $g^\top B g > 0$ 时（开口向上），令导数为零：

$$\frac{d}{d\tau} q = g^\top B g \cdot \tau - \|g\|^2 = 0 \quad \Rightarrow \quad \tau^* = \frac{\|g\|^2}{g^\top B g}$$

若 $g^\top B g \leq 0$（开口向下/平），函数单调递减，无约束极小点不存在——理解为 $\tau^* \to \infty$。

**Step 4**：信赖域约束。$\|s\| = \|\tau g\| = \tau\|g\| \leq r \Rightarrow \tau \leq r/\|g\|$。其中 **$r$ 就是信赖域半径**（考题中记为 $\Delta$）。

**Step 5**：取两者较小值——无约束最优和边界谁先到：

$$\tau^c = \min\!\left(\tau^*,\; \frac{r}{\|g\|}\right), \quad s^c = -\tau^c g$$

| 情形 | $\tau^c$ | Cauchy 点位置 |
|------|------|------|
| $\tau^* \leq r/\|g\|$ | $\tau^*$（无约束极小点） | 圈内 |
| $\tau^* > r/\|g\|$ | $r/\|g\|$（边界交点） | 圈边 |
| $g^\top B g \leq 0$ | $r/\|g\|$（单调递减，必取边界） | 圈边 |

### 3.2 两套 $\tau$ 参数化

这是最容易混淆的地方。复习笔记和考题对 $\tau$ 的**尺子不同**：

| 出处 | 参数化 | $\tau$ 含义 | 边界条件 |
|------|--------|------|------|
| 复习笔记 | $s = -\tau_k \cdot \frac{r}{\|g\|} \cdot g$ | $\tau_k \in [0,1]$，走到边界的**比例** | $\tau_k = 1$ 即边界 |
| 考题 | $s = -\tau \cdot g$ | $\tau$ 是沿 $g$ 的**原始步长** | $\tau = r/\|g\|$ 即边界 |

复习笔记的公式 $\tau_k = \min(1, \frac{\|g\|^3}{r \cdot g^\top B g})$ 是在**归一化**参数化下的。它与考题 $\tau$ 的换算：

$$\tau_{\text{考题}} = \tau_k \cdot \frac{r}{\|g\|}$$

以考题数据（$g = [2,1]^\top$，$\|g\| = \sqrt{5}$，$g^\top B g = 13$，$r = 1$）验证：

| 步骤 | 复习 $\tau_k$ | 考题 $\tau$ |
|------|:---:|:---:|
| 代入公式 | $\frac{5\sqrt{5}}{1 \cdot 13} \approx 0.86$ | — |
| 换算 | $\times 1/\sqrt{5}$ | — |
| 结果 | $0.86$（边界 86% 处） | $5/13 \approx 0.385$ |

**同一个物理位置，只是尺子刻度不同。** $\tau_k = 0.86$ 意为「走到边界的 86% 处」。

> [!warning] 套公式前先确认参数化
> 见到 $\tau$ 先看是用 $s = -\tau g$（原始步长）还是 $s = -\tau \cdot \frac{r}{\|g\|} g$（归一化比例）。考题用前者，复习笔记用后者。

---

## 相关链接

- [[../复习/III-线搜索#六、信赖域法（第25章）|复习：信赖域法完整流程]]
- [[../复习/III-线搜索#6.5 柯西点|复习：Cauchy 点公式]]
- [[考题-信赖域Cauchy点|考题-09：Cauchy 点计算]]
- [[25-信赖域方法-知识梳理|第25章：信赖域方法知识梳理]]
- [[../复习/III-线搜索#五、Zoutendijk 收敛定理|Zoutendijk 收敛定理]]
