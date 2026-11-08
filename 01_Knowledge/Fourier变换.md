---
schema_version: 2
type: concept
time: '2026-08-31T11:44:20+08:00'
source:
- '[[03_Sources/Reviews/归档/实变函数/复习/IV-Lp空间]]'
- '[[03_Sources/Readings/核对资料/NIST-DLMF-积分变换]]'
- '[[03_Sources/Courses/数学物理方程/课堂笔记/2026-11-06-第13节-积分变换与傅里叶变换课程]]'
topics:
- '[[02_Maps/MOC-收敛性与积分理论]]'
- '[[02_Maps/MOC-数学物理方程]]'
aliases: []
tags:
- 傅里叶变换
exam: 考试重点
---

# Fourier变换

## 一句话

Fourier 变换将函数从"时域"（或空域）转换到"频域"——$\hat{f}(t) = \frac{1}{(2\pi)^{n/2}} \int f(x) e^{-i t \cdot x} dx$，它在 $L^1$ 上产生有界连续函数、在 $L^2$ 上是等距同构，且将卷积变为乘积，是调和分析的核心工具。

## 严格定义

**$L^1(\mathbb{R}^n)$ 上的 Fourier 变换**：设 $f \in L^1(\mathbb{R}^n)$，定义

$$\hat{f}(t) = \frac{1}{(2\pi)^{n/2}} \int_{\mathbb{R}^n} f(x) e^{-i t \cdot x} \, dx, \quad t \in \mathbb{R}^n,$$

其中 $t \cdot x = \sum_{i=1}^n t_i x_i$。$\hat{f}(t)$ 是复值函数。

**基本性质（$L^1$）**：
- **有界性**：$|\hat{f}(t)| \leq (2\pi)^{-n/2} \|f\|_1$。
- **连续性**：由控制收敛定理，$\hat{f}(t)$ 在 $\mathbb{R}^n$ 上一致连续。
- **Riemann-Lebesgue 引理**：$\lim_{|t| \to \infty} \hat{f}(t) = 0$（Fourier 变换在无穷远处衰减到零）。

**$L^2(\mathbb{R}^n)$ 上的 Fourier 变换**：由于 $L^1 \cap L^2$ 在 $L^2$ 中稠密，可以将 Fourier 变换从 $L^1 \cap L^2$ 延拓到整个 $L^2$ 上，得到 $L^2$ 上的酉算子：

$$\|\hat{f}\|_2 = \|f\|_2 \quad (\text{Plancherel 定理}).$$

> [!important] 核心要点
> - **卷积与 Fourier 变换的对偶**：$\widehat{f*g} = (2\pi)^{n/2} \hat{f} \cdot \hat{g}$——卷积在频域变为乘积，乘积在频域变为卷积。
> - **导数与乘法**：Fourier 变换将求导变为乘以 $it$：$\widehat{\partial_j f}(t) = i t_j \hat{f}(t)$（例如 $f\in\mathcal S$，或 $f$ 及其弱导数均在 $L^1$ 时）。
> - **Gauss 函数的不动性**：$f(x) = e^{-|x|^2/2}$ 的 Fourier 变换为 $\hat{f}(t) = e^{-|t|^2/2}$。
> - **$L^1$ 反演公式**：若 $\hat{f} \in L^1$，则 $f(x) = \frac{1}{(2\pi)^{n/2}} \int \hat{f}(t) e^{i x \cdot t} dt$ a.e.。

## 由来与作用

- **历史起源**：Joseph Fourier（1807-1822）在研究热传导方程时引入了以他命名的级数和变换。他声称"任意"周期函数都可展开为三角级数——这一大胆论断引发了 Cauchy、Dirichlet、Riemann 等一个世纪的严格化工作，最终在 Lebesgue 积分框架下得到圆满解决。
- **解决的问题**：Fourier 变换将微分方程变为代数方程（求导 $\leftrightarrow$ 乘以 $it$），将卷积变为乘积——大大简化了信号处理、PDE 和概率论中的计算。
- **在实变函数中的角色**：
  - 是 Lebesgue 积分理论在调和分析中的核心应用——Fourier 变换的严格定义依赖于 Lebesgue 可积性。
  - $L^2$ 上的 Plancherel 定理是 Hilbert 空间理论的标准例子。
  - 卷积与 Fourier 变换的对偶关系是分析学中最优美的结构之一。
- **关键性质**：$\mathcal{F}: L^2 \to L^2$ 是酉算子；Riemann-Lebesgue 引理；$\mathcal{F}$ 将速降函数空间 $\mathcal{S}$ 映到自身。

## 相关概念

- [[01_Knowledge/Lebesgue积分]] — Fourier 变换的严格定义需要 Lebesgue 积分。
- [[01_Knowledge/L^p空间]] — Fourier 变换在 $L^1$ 和 $L^2$ 上有定义，在其他 $L^p$ 上需用插值理论。
- [[01_Knowledge/卷积]] — $\widehat{f*g} = (2\pi)^{n/2} \hat{f} \hat{g}$，卷积与 Fourier 变换互为对偶。
- [[01_Knowledge/Minkowski不等式]] — 用于证明 Fourier 变换相关的积分不等式。

## 与概率特征函数的联系

[[01_Knowledge/多维随机变量的特征函数]] 把 $E[e^{i t^TX}]$ 用作分布的特征函数，可看作概率测度的 Fourier 型变换。使用分析中的 Fourier 公式前，应核对指数正负号和归一化约定。


## 历史原始资料线索

- [[03_Sources/Courses/归档/实变函数/课件/MD/2023-RA-28]]

上述为历史原始资料链接；本轮有效核对来源见 source 属性。


## 数学物理方程中的非对称归一化约定（2026-11-08）

本笔记上文采用对称归一化；数学物理方程课堂的一维约定是
$$\widehat f(\omega)=\int_{\mathbb R}f(s)e^{-i\omega s}\,ds,\qquad f_*(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\omega)e^{i\omega x}\,d\omega.$$
两套定义不能混用常数。一维课堂像函数是上文像函数的 $\sqrt{2\pi}$ 倍；正逆前系数 $A,B$ 必须满足 $AB=1/(2\pi)$。$e^{\pm i\omega x}$ 为模长1的振荡因子，不是实指数衰减。

逐点反演条件和截断解释见 [[01_Knowledge/傅里叶级数与傅里叶积分的中点收敛]]。改变单点值不改变积分变换，在 $L^1$ 中应按几乎处处相等识别，不能声称任意逐点不同的函数必有不同频谱。