---
title: IV. L^p空间 — 复习
subject: 实变函数
type: 复习
source: 考试范围.txt, 知识图谱.png
topics:
  - Hölder不等式
  - Minkowski不等式
  - 完备性
  - 可分性
  - 对偶性
  - 强收敛与弱收敛
  - 正交基与Fourier展开
---

# IV. $L^p$ 空间

> 一句说清：$L^p$ = $p$ 次幂可积函数构成的空间，由 Hölder/Minkowski 不等式赋予范数结构，完备（Riesz-Fisher）、可分（$p<\infty$）、有对偶（$L^p\leftrightarrow L^q$）。

> [!important] 考试重点
> 考点多且零散：Hölder/Minkowski 不等式应用、完备性/可分性/对偶性、强弱收敛、正交基与 Fourier 展开、$L^p$ 可积函数判断。

---

## 一、核心定义速查

### 1.1 $L^p$ 范数与空间

| 概念 | 定义 | 备注 |
|:--|:--|:--|
| $L^p$ 范数 | $\|f\|_p = (\int_E\|f\|^p)^{1/p}$ | $1\leq p<\infty$ |
| $L^\infty$ 范数 | $\|f\|_\infty = \inf\{M: \|f\|\leq M\text{ a.e.}\}$ | 本性上界 |
| $L^p(E)$ | $\{f\in\mathfrak{M}(E): \|f\|_p<\infty\}$ | $p$ 次幂可积函数 |
| 共轭指数 | $1/p+1/q=1$ | $p=2$ 时 $q=2$（自共轭） |

### 1.2 强弱收敛

| 收敛类型 | 定义 | 记号 |
|:--|:--|:--:|
| **强收敛**（$L^p$ 收敛） | $\|f_n-f\|_p\to 0$ | $f_n\xrightarrow{L^p}f$ |
| **弱收敛** | $\forall g\in L^q$，$\int f_ng\to\int fg$ | $f_n\rightharpoonup f$ |

> 强收敛 $\Rightarrow$ 弱收敛（由 Hölder 不等式），反之一般不成立。

---

## 二、核心不等式

### 2.1 Hölder 不等式 ★★

$$\|fg\|_1 \leq \|f\|_p\|g\|_q\quad\left(\frac{1}{p}+\frac{1}{q}=1\right)$$

即 $\int_E |fg| \leq (\int_E|f|^p)^{1/p}(\int_E|g|^q)^{1/q}$。

**特例**：$p=q=2$ → **Schwarz 不等式**：$|\int fg|\leq\|f\|_2\|g\|_2$。

**证明核心**：利用 Young 不等式 $a^{1/p}b^{1/q}\leq a/p+b/q$，取 $a=|f|^p/\|f\|_p^p$，$b=|g|^q/\|g\|_q^q$。

### 2.2 Minkowski 不等式 ★

$$\|f+g\|_p \leq \|f\|_p+\|g\|_p$$

> 这就是 $L^p$ 范数的三角不等式。

**证明核心**：$\|f+g\|_p^p\leq\int|f+g|^{p-1}|f|+\int|f+g|^{p-1}|g|$，对两项各用 Hölder。

### 2.3 Young 不等式（卷积版）

$f\in L^p(\mathbb{R}^n)$，$g\in L^1(\mathbb{R}^n)$ → $f*g\in L^p$，且 $\|f*g\|_p\leq\|f\|_p\|g\|_1$。

---

## 三、核心定理

### 3.1 完备性（Riesz-Fisher 定理）★★★

**定理**：$\forall 1\leq p\leq\infty$，$L^p(E)$ 完备——每个基本列必收敛。

**证明思路**（$1\leq p<\infty$）：基本列 → 测度基本列 → 依测度收敛 → Riesz 子列 a.e. 收敛 → Fatou 引理 → $L^p$ 收敛。

> 关键对比：黎曼可积函数空间在 $L^1$ 范数下**不完备**——这正是引入 $L^p$ 空间的动因。

### 3.2 可分性 ★

**定理**：$1\leq p<\infty$ 时，$L^p(E)$ 可分（存在可数稠密子集）。

**不可分**：$L^\infty[0,1]$ 不可分（$\chi_{[0,t]}$ 两两距离为 $1$，不可数个）。

**逼近链**：简单函数 → $C_c$（紧支连续） → 阶梯函数（有理系数）→ 可数稠密子集。

### 3.3 对偶性 ★★

**定理 4.1.5**：$\|f\|_p = \sup_{\|g\|_q=1}\int_E fg$（$1\leq p<\infty$）。

> $L^p$ 的对偶空间是 $L^q$（等距同构）。$L^\infty$ 情形等号不一定能取到。

### 3.4 有限测度集上的包含关系 ★

$m(E)<\infty$，$p_1<p_2$ → $L^{p_2}(E)\subset L^{p_1}(E)$，且

$$\|f\|_{p_1} \leq m(E)^{\frac{1}{p_1}-\frac{1}{p_2}}\|f\|_{p_2}.$$

> 有限测度上高指数空间"更小"。$\lim_{p\to\infty}\|f\|_p=\|f\|_\infty$。

### 3.5 $L^p$ 控制收敛定理 ★

$\lvert f_n\rvert\leq g\in L^p$，$f_n\to f$ a.e.（或依测度） → $f_n\xrightarrow{L^p}f$。

---

## 四、正交基与 Fourier 展开（$L^2$ 空间）★

### 4.1 标准正交系

$\{\varphi_k\}\subset L^2(E)$ 满足 $(\varphi_i,\varphi_j)=\delta_{ij}$（$(\cdot,\cdot)$ 为 $L^2$ 内积）。

### 4.2 完全正交系与标准正交基

| 概念 | 条件 |
|:--|:--|
| 完全系 | $f\in L^2$ 且 $(f,\varphi_k)=0$（$\forall k$）→ $f=0$ a.e. |
| 标准正交基 | 每个 $f\in L^2$ 可展开为 $f=\sum c_k\varphi_k$（$L^2$ 收敛） |

**等价条件**（定理 4.2.14）：
- (1) 标准正交基
- (2) 有限线性组合在 $L^2$ 中稠密
- (3) 完全性
- (4) Parseval 等式：$\|f\|^2=\sum|(f,\varphi_k)|^2$

### 4.3 重要例子

**三角函数系**（$L^2[-\pi,\pi]$）：
$$\frac{1}{\sqrt{2\pi}},\frac{1}{\sqrt{\pi}}\cos x,\frac{1}{\sqrt{\pi}}\sin x,\cdots,\frac{1}{\sqrt{\pi}}\cos kx,\frac{1}{\sqrt{\pi}}\sin kx,\cdots$$

→ Fourier 级数：$f(x)=\frac{a_0}{2}+\sum(a_n\cos nx+b_n\sin nx)$（$L^2$ 收敛）。

**Legendre 多项式**（$L^2[-1,1]$）：
$$L_k(x)=\frac{1}{2^k k!}\sqrt{\frac{2k+1}{2}}\frac{d^k}{dx^k}[(x^2-1)^k]$$

**Hermite 函数**（$L^2(\mathbb{R})$）：由 $e^{-x^2}$ 的导数构造，构成 $L^2(\mathbb{R})$ 的标准正交基。

---

## 五、卷积与磨光算子（第 28-29 讲）★★

### 5.1 卷积定义

$f*g(x)=\int_{\mathbb{R}^n}f(x-y)g(y)dy$。交换性：$f*g=g*f$（变量代换）。

### 5.2 Young 不等式（定理 4.3.1）

$f\in L^p(\mathbb{R}^n)$，$g\in L^1(\mathbb{R}^n)$ → $f*g\in L^p$，且 $\|f*g\|_p\leq\|f\|_p\|g\|_1$。

**证明核心**（$1\leq p<\infty$）：$|f*g(x)|\leq\int|f(x-y)||g(y)|^{1/p}|g(y)|^{1/q}dy$，用 Hölder 拆分。

### 5.3 磨光算子（定理 4.3.6）★★★

取 $\varphi\in L^1(\mathbb{R}^n)$，$\varphi\geq 0$，$\|\varphi\|_1=1$。定义 $\varphi_\varepsilon(x)=\varepsilon^{-n}\varphi(x/\varepsilon)$。

**核心结论**：若 $f\in L^p(\mathbb{R}^n)$（$1\leq p<\infty$），则
$$\|\varphi_\varepsilon * f - f\|_p \to 0 \quad (\varepsilon\to 0)$$

**证明**：$\varphi_\varepsilon*f(x)-f(x)=\int(f(x-\varepsilon y)-f(x))\varphi(y)dy$，用 Hölder + 控制收敛定理。

> 直观：$\varphi_\varepsilon$ 像一个"尖峰逼近"，$\varphi_\varepsilon*f$ 是 $f$ 的局部加权平均，$\varepsilon\to 0$ 时恢复 $f$。

**重要推论**：
- $C_c^\infty(\mathbb{R}^n)$ 在 $L^p(\mathbb{R}^n)$ 中稠密
- $[a,b]$ 上全体多项式在 $L^p[a,b]$ 中稠密（Weierstrass 逼近定理的 $L^p$ 版本）
- $S(\mathbb{R}^n)$（速降函数）在 $L^p(\mathbb{R}^n)$ 中稠密

**经典 mollifier 例子**：
- $\varphi(x)=c\cdot e^{1/(|x|^2-1)}$（$|x|<1$），否则 $0$
- Gauss 核：$W(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$

---

## 六、Fourier 变换（第 28 讲）★★

### 6.1 定义与基本性质

**定义 4.3.7**：$f\in L^1(\mathbb{R}^n)$，Fourier 变换：
$$\hat{f}(t) = (2\pi)^{-n/2}\int_{\mathbb{R}^n} f(x) e^{-it\cdot x} dx$$

**基本性质**（引理 4.3.8）：$f,g\in L^1(\mathbb{R}^n)$

| 操作 | 函数 | Fourier 变换 |
|:--|:--|:--|
| 平移 | $T_x f(y)=f(y-x)$ | $e_{-x}\hat{f}$（乘相位） |
| 调制 | $e_x f(y)=e^{ix\cdot y}f(y)$ | $T_x\hat{f}$（平移） |
| **卷积** | $f*g$ | $\hat{f}\cdot\hat{g}$（乘积） |
| 伸缩 | $f(x/\lambda)$，$\lambda>0$ | $\lambda^n\hat{f}(\lambda t)$ |

> 核心口诀：**卷积的 Fourier 变换 = Fourier 变换的乘积**。

### 6.2 $L^1$ 上的 Riemann-Lebesgue 引理

**定理 4.3.12**：$f\in L^1(\mathbb{R}^n)$ → $\hat{f}\in C_0(\mathbb{R}^n)$（连续且在无穷远处趋于 0），且 $\|\hat{f}\|_\infty\leq\|f\|_1/(2\pi)^{n/2}$。

### 6.3 速降函数空间 $S(\mathbb{R}^n)$

**定义 4.3.9**：$f\in C^\infty$，满足 $\forall N,\forall\alpha$，$(1+|x|^2)^N|D^\alpha f(x)|$ 有界。

> $S$ 的好处：Fourier 变换将 $S$ 映到 $S$（命题 4.3.11），且可定义逆变换。

**$S$ 上的运算与 Fourier 变换**（命题 4.3.11）：
- $(P(D)f)^\wedge = P\cdot\hat{f}$（求导 ↔ 乘多项式）
- $(P\cdot f)^\wedge = P(-D)\hat{f}$（乘多项式 ↔ 求导）

### 6.4 逆变换与 Plancherel

**逆定理**（定理 4.3.13）：$F: S\to S$ 是双射，$F^4=I$。逆变换：
$$f(x) = (2\pi)^{-n/2}\int_{\mathbb{R}^n} \hat{f}(t) e^{ix\cdot t} dt$$

**Plancherel 定理**（定理 4.3.15）：Fourier 变换可唯一延拓为 $L^2(\mathbb{R}^n)$ 上的酉算子：
$$\|\hat{f}\|_2 = \|f\|_2 \quad (\forall f\in L^2)$$

**经典例子**：Gauss 函数 $G(x)=e^{-|x|^2/2}$ → $\hat{G}=G$，$G(0)=1$。

---

## 五、典型考题

### 5.1 判断函数是否属于 $L^p$

**核心**：检查 $\int_E|f|^p$ 是否有限。关注奇点（如 $0$）和无穷远处的衰减。

**例**：$E=(0,1)$，$f(x)=x^{-3/2}$ 是否在 $L^p$ 中？
需 $p\cdot 3/2 < 1$ → $p<2/3$。

### 5.2 Hölder 不等式应用

**典型题**：证明 $\int_0^1 f(x)dx \leq (\int_0^1|f|^p)^{1/p}$（用 Hölder，取 $g\equiv 1$，$\|g\|_q=1$）。

### 5.3 正交展开

验证某函数系是否正交，计算 Fourier 系数。

---

## 六、易错点

> [!warning] $L^p$ 收敛 $\not\Rightarrow$ 几乎处处收敛
> 只能保证存在子列 a.e. 收敛（推论 4.1.13）。

> [!warning] 有限测度集上 $L^p$ 的包含方向
> $p_1<p_2$ 时 $L^{p_2}\subset L^{p_1}$——高指数空间"更小"。无限测度集上不成立。

> [!warning] $L^\infty$ 不可分
> $1\leq p<\infty$ 时 $L^p$ 可分，但 $L^\infty$ 不可分。

> [!warning] 弱收敛 $\not\Rightarrow$ 强收敛
> $L^2[0,1]$ 中 $f_n(x)=\sin(n\pi x)$：弱收敛于 $0$（Riemann-Lebesgue），但 $\|f_n\|_2=1/\sqrt{2}\not\to 0$。

---

## 七、相关知识点梳理

| 链接 | 内容 |
|:--|:--|
| [[../知识点解析梳理/05-重积分与Lp空间-知识梳理#六、L^p 空间的定义与基本概念]] | $L^p$ 定义与基本性质 |
| [[../知识点解析梳理/05-重积分与Lp空间-知识梳理#七、Holder 不等式与 Minkowski 不等式]] | 核心不等式 |
| [[../知识点解析梳理/05-重积分与Lp空间-知识梳理#十、L^p 空间的完备性]] | Riesz-Fisher 定理 |
| [[../知识点解析梳理/05-重积分与Lp空间-知识梳理#十一、L^p 空间的逼近链与可分性]] | 可分性证明 |
| [[../课件/MD/2023-RA-26]] | $L^2$ 空间、标准正交基 |
| [[../课件/MD/2023-RA-27]] | 正交基性质、三角函数系 |
| [[../课件/MD/2023-RA-28]] | 卷积、Fourier 变换、速降函数 |
| [[../课件/MD/2023-RA-29]] | 磨光算子、逼近理论 |

## 八、作业回顾

- 判断幂函数 $x^{-\alpha}$ 在不同区域上的 $L^p$ 性质
- Hölder/Minkowski 不等式证明积分估计
- 验证某函数系的完全性/正交性
- $L^p$ 空间包含关系判断
