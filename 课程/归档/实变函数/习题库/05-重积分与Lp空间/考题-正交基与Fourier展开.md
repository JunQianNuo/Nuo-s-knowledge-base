---
title: 考题 - 正交基与Fourier展开
subject: 实变函数
chapter: 5
section: 重积分与L^p空间
source: 2023-RA-27.md
status: 已校对
type: 考题
topics:
  - 正交基
  - Fourier展开
  - Parseval等式
  - L^2空间
knowledge_tags:
  - 正交基与Fourier展开
method_tags:
  - 
tags:
- Fourier展开
- Parseval等式
- 正交基与Fourier展开
- L2空间
---

# 考题：正交基与 Fourier 展开

## 题目

(1) 写出 $L^2[-\pi,\pi]$ 中标准正交三角函数系的完整形式。

(2) 对 $f(x) = x$（$x \in [-\pi,\pi]$），计算其关于该标准正交系的 Fourier 系数，并写出 Parseval 等式。

(3) 利用 (2) 的结果证明：$\displaystyle \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$。

---

> [!hint]- 点击展开提示
> 三角函数系经归一化后才是标准正交的。$x$ 是奇函数，只有正弦项系数非零。Parseval 等式将 $\|f\|_2^2$ 与 Fourier 系数的平方和联系起来。

> [!solution]- 点击展开详细解析
> **解**：
>
> **(1)** $L^2[-\pi,\pi]$ 中的标准正交三角函数系为：
> $$\varphi_0(x) = \frac{1}{\sqrt{2\pi}}, \quad \varphi_n(x) = \frac{\cos(nx)}{\sqrt{\pi}}, \quad \psi_n(x) = \frac{\sin(nx)}{\sqrt{\pi}} \quad (n=1,2,\ldots)$$
>
> **(2)** $f(x)=x$ 是奇函数，故 $\langle f, \varphi_n \rangle = 0$（余弦项全为零）。
>
> $$\langle f, \varphi_0 \rangle = \frac{1}{\sqrt{2\pi}}\int_{-\pi}^{\pi} x \, dx = 0$$
>
> $$\langle f, \psi_n \rangle = \frac{1}{\sqrt{\pi}}\int_{-\pi}^{\pi} x \sin(nx) \, dx = \frac{1}{\sqrt{\pi}} \left[ -\frac{x\cos(nx)}{n}\Big|_{-\pi}^{\pi} + \frac{1}{n}\int_{-\pi}^{\pi}\cos(nx)dx \right]$$
> $$= \frac{1}{\sqrt{\pi}} \cdot \frac{-2\pi\cos(n\pi)}{n} = \frac{2\sqrt{\pi}(-1)^{n+1}}{n}$$
>
> Parseval 等式：
> $$\|f\|_2^2 = \sum_{n=1}^\infty |\langle f, \psi_n \rangle|^2$$
>
> 计算 $\|f\|_2^2 = \int_{-\pi}^{\pi} x^2 dx = \frac{2\pi^3}{3}$。
>
> 代入：$\frac{2\pi^3}{3} = \sum_{n=1}^\infty \frac{4\pi}{n^2}$。整理得：
> $$\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$$
>
> **(3)** 已在 (2) 中证明。
>
> **答案**：(1) 见上；(2) $\langle f, \psi_n \rangle = \frac{2\sqrt{\pi}(-1)^{n+1}}{n}$；(3) $\frac{\pi^2}{6}$。
>
> **点评**：这是 Parseval 等式最经典的应用——通过计算一个简单函数的 Fourier 系数，反推出著名级数和。考试中常以此为考题形式。
