---
title: 答疑 — 梯度Taylor展开 vs 函数Taylor展开
subject: 最优化方法
type: 答疑
topics:
  - Taylor展开
  - 梯度
  - Hessian
  - 牛顿法收敛性
source_context:
  - file: "常考查的证明.md"
    line: 200
    text: "∇f(x*) = ∇f(x^(k)) + ∇²f(x^(k))(x* - x^(k)) + O(‖x* - x^(k)‖²)"
  - file: "常考查的证明.md"
    line: 199
    text: "对 ∇f 在 x^(k) 处做一阶 Taylor 展开"
related_notes:
  - "[[../复习/常考查的证明]]"
  - "[[../复习/IV-无约束优化]]"
  - "[[09-牛顿法-知识梳理]]"
---

# 答疑 — 梯度 Taylor 展开 vs 函数 Taylor 展开

> 问题：**牛顿法收敛证明中的 Taylor 展开 $\nabla f(x^*) = \nabla f(x^{(k)}) + \nabla^2 f(x^{(k)})(x^* - x^{(k)}) + O(\cdots)$ 为什么没有二次型 $\frac{1}{2}(x^*-x^{(k)})^\top H (x^*-x^{(k)})$？**

> 来源：`常考查的证明.md` 第 200 行

---

## 一句话兜底

> 这个展开的对象是**梯度函数 $\nabla f$**（向量值函数），不是原函数 $f$（标量函数）。对 $\nabla f$ 做一阶展开，一阶导数恰好是 Hessian，不会出现二次型。

---

## 两条不同层次的展开

| | 函数 $f$ 的展开 | 梯度 $\nabla f$ 的展开 |
|------|------|------|
| 对象 | $f: \mathbb{R}^n \to \mathbb{R}$（标量） | $\nabla f: \mathbb{R}^n \to \mathbb{R}^n$（向量） |
| 阶数 | 二阶 | 一阶 |
| 公式 | $f(y) \approx f(x) + \nabla f^\top (y-x) + \frac{1}{2}(y-x)^\top \nabla^2 f (y-x)$ | $\nabla f(y) \approx \nabla f(x) + \nabla^2 f(x) (y-x)$ |
| 二阶项 | $\frac{1}{2}d^\top H d$（**二次型**） | $O(\|d\|^2)$（余项中，不展开） |

---

## 一元类比一目了然

| 一元 | 多元 |
|------|------|
| $f(y) \approx f(x) + f'(x)(y-x) + \frac{1}{2}f''(x)(y-x)^2$ | $f(y) \approx f(x) + \nabla f^\top (y-x) + \frac{1}{2}(y-x)^\top H (y-x)$ |
| $f'(y) \approx f'(x) + f''(x)(y-x)$ | $\nabla f(y) \approx \nabla f(x) + \nabla^2 f(x)(y-x)$ |

左边是 $f'$ 的一阶展开，用到了二阶导数 $f''$——但不会出现 $(y-x)^2$ 项（那是 $f$ 本身二阶展开的产物）。

右边同理：$\nabla f$ 的一阶展开用到 Hessian，但 Hessian 在这里是作为 $\nabla f$ 的 **Jacobi 矩阵**（一阶导数），不是作为 $f$ 的二阶项系数。所以没有 $\frac{1}{2}d^\top H d$。

---

## 在牛顿法收敛证明中的作用

证明中故意对 $\nabla f$ 展开而非对 $f$ 展开，因为：

1. 极小点处 $\nabla f(x^*) = 0$，代入后直接消去常数项
2. Hessian 出现在 $\nabla f(x^{(k)})$ 和 $x^* - x^{(k)}$ 之间，恰好与牛顿步 $H_k^{-1} g_k$ 对接
3. 余项 $O(\|x^* - x^{(k)}\|^2)$ 直接推出牛顿法的二次收敛

---

## 相关链接

- [[../复习/常考查的证明#证明 1：牛顿法的局部二次收敛|常考证明：牛顿法二次收敛]]
- [[../复习/IV-无约束优化#三、牛顿法（第9章）|复习：牛顿法]]
- [[09-牛顿法-知识梳理#三、收敛性分析|第9章：牛顿法收敛性]]
