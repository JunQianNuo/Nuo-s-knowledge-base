---
title: Zoutendijk定理
type: 知识点
source:
- 课程/最优化方法/知识点解析梳理/07-一维搜索方法-知识梳理.md
topics:
- Zoutendijk定理
- 线搜索
- 收敛分析
- Wolfe准则
status: 已整理
---

# Zoutendijk 定理

## 一句话

Zoutendijk 定理说明：只要搜索方向不与负梯度方向渐近正交，且步长满足 Wolfe 准则，则梯度一定趋于零——即线搜索迭代保证收敛到稳定点。

## 严格定义

> [!important] **定理 (Zoutendijk)**：设 $f:\mathbb{R}^n\to\mathbb{R}$ 连续可微且有下界，$\nabla f$ **Lipschitz 连续**（即存在 $L$ 使得 $\|\nabla f(x)-\nabla f(y)\|\leq L\|x-y\|$）。对于线搜索迭代 $x_{k+1}=x_k+\alpha_k p_k$，若 $p_k$ 是下降方向且 $\alpha_k$ 满足 **Wolfe 准则**，则：

$$
\boxed{\sum_{k=0}^{\infty}\cos^2\theta_k\;\|\nabla f(x_k)\|^2<+\infty}
$$

其中 $\theta_k$ 是 $p_k$ 与 $-\nabla f(x_k)$ 的夹角：

$$
\cos\theta_k=\frac{-p_k^T\nabla f(x_k)}{\|p_k\|\;\|\nabla f(x_k)\|}
$$

## 证明思路

> [!proof]- 证明思路
> 1. 由 Wolfe 准则的曲率条件：$\nabla f(x_k+\alpha_k p_k)^T p_k\geq c_2\nabla f(x_k)^T p_k$
> 2. 由 Lipschitz 连续性：$(\nabla f(x_k+\alpha_k p_k)-\nabla f(x_k))^T p_k\leq\alpha_k L\|p_k\|^2$
> 3. 结合 1 和 2，导出步长下界：$\alpha_k\geq\frac{1-c_2}{L}\cdot\frac{-\nabla f(x_k)^T p_k}{\|p_k\|^2}$
> 4. 利用 Wolfe 第一条件（Armijo）和步长下界，每一步下降量：
> 
>    $$
>    f(x_k)-f(x_{k+1})\geq\frac{c_1(1-c_2)}{L}\cos^2\theta_k\;\|\nabla f(x_k)\|^2
>    $$
> 
> 5. 对 $k=0,\dots,N-1$ 求和，左侧有界（$f$ 有下界），故级数收敛。

## 重要推论

由于 $\sum\cos^2\theta_k\;\|\nabla f(x_k)\|^2$ 收敛，必有 $\cos^2\theta_k\;\|\nabla f(x_k)\|^2\to0$。因此：

- 若 $\cos\theta_k\geq\delta>0$（方向不趋于与负梯度正交），则 $\|\nabla f(x_k)\|\to0$
- 最速下降法中 $\cos\theta_k=1$，直接得到梯度趋于零
- 牛顿、拟牛顿、共轭梯度方向均满足此条件

## 易错点

> [!warning] 仅 Armijo 不能保证 Zoutendijk
> Armijo 允许步长任意小，无法导出步长下界。必须配合 Wolfe 的曲率条件或回溯策略。

> [!warning] Lipschitz 连续是必要条件
> $\nabla f$ 需要 Lipschitz 连续（比 $C^1$ 更强），保证 Taylor 展开余项可控。

> [!warning] $\cos\theta_k\to0$ 时定理不能保证收敛
> 如果搜索方向渐近正交于负梯度，即使梯度不趋于零，级数也可能收敛。

## 相关概念
- [[概念/最优化方法/Wolfe准则]]
- [[概念/最优化方法/线搜索]]

- [[知识点/最优化方法/回溯线搜索]]

## 习题

- [[课程/最优化方法/习题库/07-一维搜索方法/README|第7章习题库]]
