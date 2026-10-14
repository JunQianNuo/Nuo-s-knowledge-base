---
raw_title: 数值分析02NonlinearEq
subject: 数值分析02NonlinearEq
source: 数值分析02NonlinearEq.pptx
status: mineru解析
parser: mineru
---

## 非线性求解方程

- 二分法
- 不动点迭代
- 精度极限\根搜索敏感性
- 牛顿迭代法
- 割线法
- 抛物法\混合方法
- 方程组的牛顿迭代法

## 数值求解方程的必要性

- 方程求解是工程计算中最重要的问题之一
- 很多方程无法得到解析解，依赖于数值技术
- 光的衍射理论： $x-\tan(x)=0$
- 行星轨道计算的开普勒方程： $x-asinx=b$

## 二分法

- **定理**： 如果 $f\left(x\right)\in C[a,b]$ ，并满足 $f(a)f(b)<0$ ，则 $\exists r\in (a,b)$ 使得 $f(r)=0$ .

![](images/e779a435e45d115010feafdb7558d087b82b120e855c17303fb9b2c9175a8222.jpg)

$f\left(x\right)=x^{3}+x-1$ 的函数图像

## 二分法

- **二分法伪代码(pseudo-code)**

![](images/fea563b1ca3a452b60f2e1e4b69436a3c3736437d9e14bc17d91aae3148ad5d2.jpg)

- 误差？计算量？

## 二分法

- 例：用二分法求 $f\left(x\right)=cos (x)-x$ 在 $[0,1]$ 之间的根，并使得根的第6位小数是有效数字。

估算二分次数：

$\epsilon _{n}=\frac{1}{2^{n+1}}<0.5\times 10^{-6}$

$\rightarrow n>\frac{6}{log_{10}2}\approx 19.9$

![](images/bb3dcce2af6efd1ba677ae78d6f2ccac0b7d55c46cf35b2c89e0216658185c84.jpg)

## 不动点迭代

- 引例：对任意初值重复应用余弦函数

$x_{0}=0$

$x_{0}=1234$

![](images/fcaed9cc44f9f6175bbad80a8bdd5226d433d00edb2564c607af700d303acc2c.jpg)

![](images/3ad73608a47446435ff393b9ba6011372d85eeb6ae578b080e135e093df396c8.jpg)

![](images/4574168bde48077541c4135197e2c86c5316a33df540f714e77901178debe652.jpg)

![](images/67257c90a82bdb047a33a3b3c25fdd115a68266d7d23d5b1d45ebe106f06faa5.jpg)

## 不动点迭代

- 定义：如果 $g\left(r\right)=r$ ，则 $r$ 为 $g(x)$ 的不动点。

- 例： $g\left(x\right)=\cos(\left(x\right))$ 的不动点为 $0.739085\ldots$

- 例：地图

![](images/9d3ec4e0f6a4d12110fc112904bb4556b85f9e3db916b113371dc9913fd2c8af.jpg)

## 不动点迭代

- 例： $g\left(x\right)=x^{3}$ 的不动点？

- 不动点与方程根的关系： $g\left(r\right)=r\Longleftrightarrow f\left(r\right)=g\left(r\right)-r=0$
- 例： $r=0.739085\ldots$ 为 $f\left(x\right)=\cos(x)-x$ 的根。

## 不动点迭代

- 不动点迭代

![](images/c1b440fe763785a5965c05567e08c7764c16722062dd16189157b60e18a5810a.jpg)

![](images/c1b440fe763785a5965c05567e08c7764c16722062dd16189157b60e18a5810a.jpg)

- 如果 $g(x)$ 连续且 $\lim_{i\to \infty }x_{i}=r$ （收敛）：

$g\left(r\right)=g\left(\lim_{i\to \infty }x_{i}\right)=\lim_{i\to \infty }g\left(x_{i}\right)=\lim_{i\to \infty }x_{i+1}=r$

## 不动点迭代

- 需要回答的问题：

1. 方程的不动点函数是否唯一？
2. 是否总是收敛？
3. 什么条件下收敛？
4. 收敛速度？

## 不动点迭代

- 例：用不动点迭代求解 $x^{3}+x-1=0$

$g\left(x\right)=\frac{1+2x^{3}}{1+3x^{2}}$

$g\left(x\right)=\sqrt[3]{1-x}$

$g\left(x\right)=1-x^{3}$

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0bf8f31b83ddc4e6265a30bc3ad055e80e8c052384a6888e16b2da24e269f9ec.jpg)

![](images/0543001925002c7838c7b4494b19dc0886b745c0e9c3214e192d8def5ae76c18.jpg)

## 不动点迭代

- 收敛的几何解释

$y=g(x)$

$y=x$

$L_{1}$

$g\left(x_{0}\right)$

$x_{0}$

$g\left(x_{1}\right)$

$L_{0}$

$x_{2}$

$x_{0}$

$L_{2}$

$x_{1}=g\left(x_{0}\right)$

不收敛情况1

$L_{2}=\left|g\left(x_{1}\right)-g\left(x_{0}\right)\right|>L_{0}=L_{1}=\left|x_{1}-x_{0}\right|$

## 不动点迭代

$g\left(x_{0}\right)$

$y=g(x)$

$L_{1}$

$x_{0}$

$g\left(x_{1}\right)$

$L_{0}$

$y=x$

$L_{2}$

$x_{0}$

$x_{2}$

$x_{1}=g\left(x_{0}\right)$

情况2

不收敛

$L_{2}=\left|g\left(x_{1}\right)-g\left(x_{0}\right)\right|=L_{0}=L_{1}=\left|x_{1}-x_{0}\right|$

## 不动点迭代

$g\left(x_{0}\right)$

$y=g(x)$

$L_{1}$

$g\left(x_{1}\right)$

$x_{0}$

$L_{0}$

$y=x$

$L_{2}$

$x_{2}$

$x_{0}$

$x_{1}=g\left(x_{0}\right)$

收敛情况3

$L_{2}=\left|g\left(x_{1}\right)-g\left(x_{0}\right)\right|<L_{0}=L_{1}=\left|x_{1}-x_{0}\right|$

## 不动点迭代

- 不同不动点迭代的蛛网图(cobweb)

![](images/d342a515cdace1c3b25bc7376c2aa24b05da6af891c442fb5bee6f60d2a00650.jpg)

$g\left(x\right)=1-x^{3}$

![](images/4da8502aac579160d4c5a2d2b547f563b943a2ef9ba8c95890222829e90325b9.jpg)

$g\left(x\right)=\sqrt[3]{1-x}$

![](images/7c7d2e6beb23d406ea978433c00c4583d248eaf9695a4ccc6a9d74a43ce37eb7.jpg)

$g\left(x\right)=\frac{1+2x^{3}}{1+3x^{2}}$

## 不动点迭代

- 定义：假设 $g\left(x\right)$ 在区间 $I$ 存在不动点 $x^{*}$ ，若对 $\forall x_{0}\in I$ ，不动点迭代产生的序列 $\left\{x_{k}\right\}$ 收敛到 $x^{*}，$ 则称不动点迭代在区间 $I$ 全局收敛。
- 定义：假设 $g\left(x\right)$ 在区间 $I$ 存在不动点 $x^{*}$ ，若存在 $x^{*}$ 的邻域 $N\subset I$ ，对 $\forall x_{0}\in N$ ，不动点迭代产生的序列 $\left\{x_{k}\right\}$ 收敛到 $x^{*}，$ 则称不动点迭代在区间 $I$ 局部收敛。

- 定义：如果存在常数 $L>0,$ 使得 $\forall x_{1},x_{2}\in I$ 满足 $\left|f\left(x_{1}\right)-f\left(x_{2}\right)\right|\leq L\left|x_{1}-x_{2}\right|$ ，则称函数 $f\left(x\right)$ 在区间 $I$ 满足Lipschitz条件，其中 $L$ 称为Lipschitz常数。

## 不动点迭代

- 定理： $g\left(x\right)\in C[a,b]$ 连续

1、如果 $\forall x\in \left[a,b\right]$ 有 $a\leq g\left(x\right)\leq b,$ 则 $g\left(x\right)$ 在 $\left[a,b\right]$ 上存在不动点。

2、在满足条件1的基础上，如果存在常数 $L\in \left(0,1\right)$ ，使得

$\left|g\left(x_{1}\right)-g\left(x_{2}\right)\right|\leq L\left|x_{1}-x_{2}\right|, \forall x_{1},x_{2}\in \left[a,b\right],$

则:

1. $g\left(x\right)$ 在 $\left[a,b\right]$ 上存在唯一不动点 $x^{*}$
2. $\forall x_{0}\in \left[a,b\right]$ ,不动点迭代收敛到 $x^{*}$ (全局收敛)，误差满足：

$\left|x_{k}-x^{*}\right|\leq \frac{L}{1-L}\left|x_{k}-x_{k-1}\right|\leq \ldots \leq \frac{L^{k}}{1-L}\left|x_{1}-x_{0}\right|$

## 不动点迭代

- 推论： $g\left(x\right)$ 在 $[a,b]$ 连续，在 $\left(a,b\right)$ 可微，对 $\forall x\in \left[a,b\right]$ 有 $a\leq g\left(x\right)\leq b$ ，且存在常数 $L\in \left(0,1\right)$ ，使得

$\left|g^{'}\left(x\right)\right|\leq L, \forall x\in \left(a,b\right)$

则 $g\left(x\right)$ 在 $\left[a,b\right]$ 上存在唯一不动点，并且不动点迭代在 $[a,b]$ 上全局收敛。

- 局部收敛定理：设 $x^{*}$ 为 $g\left(x\right)$ 的不动点，如果 $g^{'}\left(x\right)$ 在区间 $I$ 连续且 $\left|g^{'}\left(x^{*}\right)\right|<1$ ，则不动点迭代 $x_{i+1}=g\left(x_{i}\right)$ 局部收敛。

## 不动点迭代

- 例： $g\left(x\right)=\cos(x)$ 是否局部\全局收敛？
- 例：求解 $x^{3}+x-1=0$ 的不动点迭代对于 $r\approx 0.6823$ 是否收敛？

1. $g\left(x\right)=1-x^{3};  \left|g^{'}\left(r\right)\right|=3r^{2}\approx 1.395$
2. $g\left(x\right)=\sqrt[3]{1-x}; \left|g^{'}\left(r\right)\right|=\frac{1}{3}\left(1-r\right)^{-\frac{2}{3}}\approx 0.716$
3. $g\left(x\right)=\frac{1+2x^{3}}{1+3x^{2}}; g^{'}\left(x\right)=\frac{6x^{2}\left(1+3x^{2}\right)-6x\left(1+2x^{3}\right)}{\left(1+3x^{2}\right)^{2}}=\frac{6x\left(x^{3}+x-1\right)}{\left(1+3x^{2}\right)^{2}}$

## 不动点迭代

- 例：迭代寻找 $g(x)=2.8x-x^{2}$ 的不动点

![](images/b9fbf91e8fa4033dcbba543bb5882c3cd514c04b6418a8dd323775545022bc8e.jpg)

![](images/cb872e3f83d361302f4c6ef4fc7059d7015a6527645c251b4c9d4fd90847441a.jpg)

迭代过程的蛛网图

## 不动点迭代

- 例：古巴比伦人计算 $\sqrt{2}=1.41421356\ldots$

$x_{1}=\frac{x_{0}+\frac{2}{x_{0}}}{2}=\frac{1+\frac{2}{1}}{2}=\frac{3}{2}$

$x_{2}=\frac{x_{1}+\frac{2}{x_{1}}}{2}=\frac{\frac{3}{2}+\frac{4}{3}}{2}=\frac{17}{12}\approx 1.41666\ldots$

$x_{0}=1$

$x_{3}=\frac{x_{2}+\frac{2}{x_{2}}}{2}=\frac{\frac{17}{12}+\frac{24}{17}}{2}=\frac{577}{408}\approx 1.41421568\ldots$

$x_{4}=\frac{x_{3}+\frac{2}{x_{3}}}{2}\approx 1.41421356\ldots$

- 该过程相当于不动点迭代: $x_{i+1}=\frac{x_{i}+\frac{2}{x_{i}}}{2}$

## 不动点迭代

- 迭代终止条件
    1. 绝对误差终止条件

$\left|x_{i+1}-x_{i}\right|<TOL$

2. 相对误差终止条件 $(x_{i}$ 不在零附近 $)$

$\frac{\left|x_{i+1}-x_{i}\right|}{\left|x_{i}\right|}<TOL$

3. 混合终止条件 $(x_{i}$ 在零附近 $)$

$\frac{\left|x_{i+1}-x_{i}\right|}{\max((\theta ,\left|x_{i}\right|))}<TOL, \theta >0$

4. 为了防止迭代失败出现锁死的情况，需要加上迭代步数的限制

## 精度的极限

- 例：二分法求根 $f\left(x\right)=x^{3}-2x^{2}+\frac{4}{3}x-\frac{8}{27}=\left(x-\frac{2}{3}\right)^{3}$

![](images/74b880228f017795eca3f87c2b3bb0845354e41ff573278cedc05bda9f650d16.jpg)

## 精度的极限

![](images/c0faf84c66feff968bff99b58e2cb18819730fdf3543a3f9f5c1dbcbb537d5d7.jpg)

![](images/c0faf84c66feff968bff99b58e2cb18819730fdf3543a3f9f5c1dbcbb537d5d7.jpg)

$f\left(x\right)=\left(x-\frac{2}{3}\right)^{3}$ 的函数图像放大的双精度函数图像

- 前向误差： $|x_{n}-r|$
- 后向误差： $|f(x_{n})|$
- 误差放大因子=相对前向误差/相对后向误差
- 条件数：问题本身所决定的误差放大

## 精度的极限

- 定义：如果 $f\left(r\right)=f^{'}\left(r\right)=\ldots =f^{\left(m-1\right)}\left(r\right)=0, f^{\left(m\right)}\left(r\right)\ne 0$ ，则称 $r$ 为 $f\left(x\right)=0$ 的 $m$ 重根。
- 例： $f\left(x\right)=\sin(x)-x$ 的 $近似根x_{c}=0.001$

前向误差： $\left|x_{c}-r\right|=0.001$

后向误差： $\left|\sin(\left(0.001\right))-0.001\right|\approx 1.6667\times 10^{-10}$

## 根搜索的敏感度

- 例：Wilkinson多项式 $W\left(x\right)=\left(x-1\right)\left(x-2\right)\ldots \left(x-20\right)$

![](images/ae3aa391ee3b59a7b5498e0b305bf6d4a5bbda12f334bb1427c8cba0576591cc.jpg)

- 用Matlab求根，初始估计为 $r=16$

![](images/c4f512a804f697db60c9b694c232fa887ce096f2da3a396acc6429672996c818.jpg)

## 根搜索的敏感度

- 敏感性问题：输入的小误差 $\Longrightarrow$ 输出的大误差。
- 例：求 $f(x)$ 的根原问题 $：f\left(x\right)=0\Longrightarrow x=r$

输入有误差的问题： $f\left(x\right)+\varepsilon g\left(x\right)=0\Longrightarrow x=r+\Delta r$

$\Delta r\approx \frac{-\varepsilon g\left(r\right)}{f^{'}\left(r\right)+\varepsilon g^{'}\left(r\right)}\approx -\varepsilon \frac{g\left(r\right)}{f^{'}\left(r\right)}$

$误差$ 放大因子 $=\left|\frac{\Delta r/r}{\varepsilon g\left(r\right)/g(r)}\right|=\left|\frac{g\left(r\right)}{rf^{'}\left(r\right)}\right|$

## 根搜索的敏感度

- 例：估计 $P\left(x\right)=\left(x-1\right)\left(x-2\right)\left(x-3\right)\left(x-4\right)\left(x-5\right)\left(x-6\right)-10^{-6}x^{7}$ 的最大根

$\Delta r\approx -\varepsilon \frac{g\left(r\right)}{f^{'}\left(r\right)}=-\varepsilon \frac{6^{7}}{5!}=-2332.8\varepsilon , \varepsilon =-10^{-6}$

$r+\Delta r\approx 6.0023328$

精确的根是6.0023268

$误差放大因子=\left|\frac{g(r)}{rf'(r)}\right|=\frac{6^{7}}{6\times 5!}\approx 388.8$

## 根搜索的敏感度

- 例：Wilkinson多项式中 $，x^{15}$ 项中的误差对于 $r=16$ 的影响。

定义: $W_{\varepsilon }\left(x\right)=W\left(x\right)+\varepsilon g(x)$ , $g\left(x\right)=-1672280820x^{15}$

$\Delta r=-\frac{\varepsilon g\left(r\right)}{W^{'}\left(r\right)}=\frac{16^{15}\times 1672280820\varepsilon }{15!4!}\approx 6.1432\times 10^{13}\varepsilon$

$\epsilon _{mach}\approx \pm 2^{-52}\approx \pm 2.22\times 10^{-16}, \Delta r\approx \pm 0.0136$

Matlab解 $\approx 16.01468$

$误差放大因子=\left|\frac{g(r)}{rW^{'}\left(r\right)}\right|\approx 3.8\times 10^{12}$

## 牛顿迭代法

- 不动点迭代遗留的问题：收敛速度？

![](images/d342a515cdace1c3b25bc7376c2aa24b05da6af891c442fb5bee6f60d2a00650.jpg)

![](images/4da8502aac579160d4c5a2d2b547f563b943a2ef9ba8c95890222829e90325b9.jpg)

![](images/7c7d2e6beb23d406ea978433c00c4583d248eaf9695a4ccc6a9d74a43ce37eb7.jpg)

$g\left(x\right)=\frac{1+2x^{3}}{1+3x^{2}}$

$g\left(x\right)=1-x^{3}$

$g\left(x\right)=\sqrt[3]{1-x}$

$\left|g^{'}\left(r\right)\right|\approx 1.395$

$\left|g^{'}\left(r\right)\right|\approx 0.716$

$\left|g^{'}\left(r\right)\right|=0$

- 定义：设序列 $\left\{x_{k}\right\}$ 收敛到 $x^{*}$ ，定义 $误差e_{i}:=\left|x_{i}-x^{*}\right|$ ，如果存在实数 $p\geq 1,$ 使得

$\lim_{i\to \infty }\frac{e_{i+1}}{e_{i}^{p}}=C$

则称序列 $p$ 阶收敛( $p=1$ 称为线性收敛，需满足 $C<1$ ； $p=2$ 称为平方收敛)。

- 定理：假设函数 $g\in C^{p}\left(a,b\right),g\left(x^{*}\right)=x^{*}\in \left(a,b\right),$ 并且满足

$g^{'}\left(x^{*}\right)=g^{''}\left(x^{*}\right)\ldots =g^{\left(p-1\right)}\left(x^{*}\right)=0, g^{\left(p\right)}\left(x^{*}\right)\ne 0, \left(p\geq 1\right)$

则不动点迭代 $x_{i+1}=g\left(x_{i}\right), p$ 阶局部收敛到不动点 $x^{*}$ ，且有

$\lim_{i\to \infty }\frac{e_{i+1}}{e_{i}^{p}}=\frac{\left|g^{\left(p\right)}\left(x^{*}\right)\right|}{p!},$

$p=1$ 时需满足 $\left|g^{'}\left(x^{*}\right)\right|<1$ 。

## 牛顿迭代法

- 例：求 $\sqrt{a}的$ 不动点迭代 $x_{i+1}=\frac{x_{i}+\frac{a}{x_{i}}}{2}$ 几阶收敛？
- 思考：能否专门设计不动点迭代使得 $g^{'}\left(x^{*}\right)=0?$

## 牛顿迭代法

- Newton–Raphson 迭代法经过 $\left(x_{i},f\left(x_{i}\right)\right)$ 的切线 $L_{i}$ ：

$y=f\left(x_{i}\right)+f^{'}\left(x_{i}\right)\left(x-x_{i}\right)$

迭代公式( $L_{i}$ 与 $x$ 轴的交点)：

$x_{i+1}=x_{i}-\frac{f\left(x_{i}\right)}{f^{'}(x_{i})}$

$x_{2}$

$x_{1}$

$x_{0}$

$f(x)$

代数解释：

$0=f\left(x\right)=f\left(x_{i}\right)+f^{'}\left(x_{i}\right)\left(x-x_{i}\right)+\frac{1}{2}f^{''}\left(\xi \right)\left(x-x_{i}\right)^{2}$

几何解释

## 牛顿迭代

- 例：求解 $x^{3}+x-1=0$

$x_{i+1}=\frac{1+2x_{i}^{3}}{1+3x_{i}^{2}}$

不动点迭代： $x_{i+1}=\sqrt[3]{1-x_{i}}$

牛顿迭代？

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0543001925002c7838c7b4494b19dc0886b745c0e9c3214e192d8def5ae76c18.jpg)

## 牛顿迭代法

- 定理：如果 $f\in C^{2}\left[a,b\right],\exists r\in \left(a,b\right)$ 满足 $f(r)=0$ ,且 $f'(r)\ne 0,f^{''}\left(r\right)$  $\ne 0$ ,则牛顿迭代法局部二次收敛到 $r$ .且迭代误差 $e_{i}=\left|x_{i}-r\right|$ 满足

$\lim_{i\to \infty }\frac{e_{i+1}}{e_{i}^{2}}=\left|\frac{f '' (r)}{2f'(r)}\right|$

- 定理：如果 $f\in C^{2}\left(\mathbb{R}\right)$ 是单调递增的凸函数， $f(r)=0$ ,则 $r$ 是唯一零点，并且对 $\forall x_{0}\in \mathbb{R}$ 牛顿迭代都将收敛到 $r$ .

## 牛顿迭代法

- 例：计算 $\sqrt{a}$

问题转换为求 $f\left(x\right)=x^{2}-a$ 的根，用牛顿迭代法。

- 例：牛顿法求 $f\left(x\right)=ax+b$ 的根， $a\ne 0$
- 例：牛顿法求 $f\left(x\right)=x^{m}$ 的根。

## 牛顿迭代法

- 定理：假设 $f\in C^{m+1}\left[a,b\right]$ 在 $[a,b]$ 上有 $m$ 重根 $r\left(m>1\right)$ ，则牛顿迭代法局部线性收敛到 $r$ ，误差满足

$\lim_{i\to \infty }\frac{e_{i+1}}{e_{i}}=\frac{m-1}{m}$

- 定理：假设 $f\in C^{m+1}\left[a,b\right]$ 在 $[a,b]$ 上有 $m$ 重根 $r$ 且 $f^{\left(m+1\right)}\left(r\right)\ne 0$ ，则改进的牛顿迭代法

$x_{i+1}=x_{i}-\frac{mf(x_{i})}{f'(x_{i})}$

局部二次收敛到 $r$ ，误差满足

$\lim_{i\to \infty }\frac{e_{i+1}}{e_{i}^{2}}=\frac{1}{m\left(m+1\right)}\left|\frac{f^{\left(m+1\right)}\left(r\right)}{f^{\left(m\right)}\left(r\right)}\right|$

- 例：从 $x_{0}=1$ 开始,用牛顿法寻找 $f\left(x\right)=\sin(x)+x^{2}\cos(x)-x^{2}-x$ 的重根 $r=0$ ，并评估需要多少步才能精确到小数点后第6位。

$f^{'}\left(x\right)=\cos(x)+2x\cos(x)-x^{2}\sin(x)-2x-1$

$f^{''}\left(x\right)=-\sin(x)+2\cos(x)-4x\sin(x)-x^{2}\cos(x)-2$

$f^{'''}\left(x\right)=-\cos(x)-6\sin(x)-6x\cos(x)+x^{2}\sin(x)$

$r=0$ 是三重根，第 $n$ 步的误差

$Error=\left(\frac{2}{3}\right)^{n}<0.5\times 10^{-6}$

$n>\frac{log_{10}0.5-6}{log_{10}\left(\frac{2}{3}\right)}\approx 35.78$

## 牛顿迭代法

![](images/c6f7e745b7b6543dc9db4cd9a3dae36b7bf88c2f0613bd021cd7527590a0eaa7.jpg)

- 标准的牛顿迭代

- 改进的牛顿迭代

![](images/78972ca3f818252a1c6f1f30ffa9b43f109912815da635670f49486eb003abce.png)

## 牛顿迭代法

- 牛顿迭代失败的方式：

1. 初始估计不在局部收敛域内
2. 导数为零
3. 根式下出现负值等

- 例：求 $f\left(x\right)=4x^{4}-6x^{2}-\frac{11}{4}$ 的根， $x_{0}=\frac{1}{2}$

$x_{i+1}=\frac{12x_{i}^{4}-6x_{i}^{2}+\frac{11}{4}}{16x_{i}^{3}-12x_{i}}$

$x_{1}=-\frac{1}{2},x_{2}=\frac{1}{2},\ldots$

![](images/6fa432ec14c385c973be331817792467b1ba43eb26feb70ca1e35937099cc38d.jpg)

## 牛顿迭代法

- 牛顿下山法： $x_{i+1}=x_{i}-\lambda \frac{f(x_{i})}{f'(x_{i})}$
    - 初始取 $\lambda =1$ ，如果 $\left|f\left(x_{i+1}\right)\right|<\left|f\left(x_{i}\right)\right|，$ 则进入下一次迭代
    - 否则，让 $\lambda$ 减半重新进行迭代，直到 $\left|f\left(x_{i+1}\right)\right|<\left|f\left(x_{i}\right)\right|$ 。

$x_{1}^{*}$

$x_{0}$

$f(x)$

几何解释

$x_{1}$

## 割线法牛顿迭代公式( $切线$ 与 $x$ 轴的交点)：

$x_{i+1}=x_{i}-\frac{f\left(x_{i}\right)}{f^{'}(x_{i})}$

$x_{1}$

$x_{2}$

$f(x)$

几何解释

$x_{0}$

$x_{3}$

割线法迭代公式( $割线$ 与 $x$ 轴的交点)：

$x_{i+1}=x_{i}-\frac{f\left(x_{i}\right)\left(x_{i}-x_{i-1}\right)}{f\left(x_{i}\right)-f\left(x_{i-1}\right)}$

谁会收敛更快？

$f\left(x\right)=f\left(x_{i}\right)+f^{'}\left(x_{i}\right)\left(x-x_{i}\right)+\frac{1}{2}f^{''}\left(\xi \right)\left(x-x_{i}\right)^{2}$

## 割线法

- 例：求解 $x^{3}+x-1=0$

不动点迭代： $x_{i+1}=\sqrt[3]{1-x_{i}}$

$牛顿$ 迭代

$割线法$

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0937646a009c8b0f76127e4cc1b062d74757feb2ee5b3bece9bf6041ae6a8b1c.jpg)

![](images/0543001925002c7838c7b4494b19dc0886b745c0e9c3214e192d8def5ae76c18.jpg)

![](images/1cd6a137599711762abcc8272f5c26d7a37c352cee0a36a71fd9e6d24be3ae14.jpg)

## 割线法

- 误差分析：如果割线法收敛到函数 $f\in C^{2}\left(\mathbb{R}\right)$ 的根 $r$ ，且 $f'(r)\ne 0,f^{''}\left(r\right)\ne 0$ ，我们有近似误差关系

$e_{i+1}\approx \left|\frac{f '' (r)}{2f^{'}\left(r\right)}\right|e_{i}e_{i-1}$

$e_{i+1}\approx \left|\frac{f '' (r)}{2f^{'}\left(r\right)}\right|^{\alpha -1}e_{i}^{\alpha }$

其中 $\alpha =\frac{1+\sqrt{5}}{2}\approx 1.62$ (超线性收敛)

- 牛顿法与割线法谁的效率更好？

## 割线法试位法

- 割线法的变种：试位法

$x_{1}$

$x_{2}$

$x_{2}$

$x_{0}$

$x_{3}$

标准割线法

$f(x)$

几何解释

- 割线法伪代码

$Given interval \left[a,b\right]$

$such that f\left(a\right)f\left(b\right)<0$

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} N$

$c\leftarrow \frac{bf\left(a\right)-af\left(b\right)}{f\left(a\right)-f\left(b\right)}$

$\mathbf{i}\mathbf{f} f\left(c\right)=0, \mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{l}\mathbf{s}\mathbf{e}$

$a\leftarrow b$

$b\leftarrow c$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

- 试位法伪代码

$Given interval \left[a,b\right]$

$such that f\left(a\right)f\left(b\right)<0$

$\mathbf{f}\mathbf{o}\mathbf{r} i=0 \mathbf{t}\mathbf{o} N$

$c\leftarrow \frac{bf\left(a\right)-af\left(b\right)}{f\left(a\right)-f\left(b\right)}$

$\mathbf{i}\mathbf{f} f\left(c\right)=0, \mathbf{s}\mathbf{t}\mathbf{o}\mathbf{p}$

$\mathbf{e}\mathbf{l}\mathbf{s}\mathbf{e} \mathbf{i}\mathbf{f} f\left(a\right)f\left(c\right)<0$

$b\leftarrow c$

$\mathbf{e}\mathbf{l}\mathbf{s}\mathbf{e}$

$a\leftarrow c$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{i}\mathbf{f}$

$\mathbf{e}\mathbf{n}\mathbf{d} \mathbf{f}\mathbf{o}\mathbf{r}$

## 割线法

- 例：求解 $x^{3}+x-1=0$

割线法

![](images/d2725cae2b608368e7a89d2f1f8606d127d1856500ca7b6ddc5b2cc84d3bd62c.jpg)

试位法

![](images/f6f5671159b24de81a4c3c8a417de4b39f24c49ef0216fa2cb71c9f99c400cdd.jpg)

## 抛物线法

- 如何进一步提升迭代收敛速度？

1. 方案一：提供一个初始点

$0=f\left(x\right)=f\left(x_{i}\right)+f^{'}\left(x_{i}\right)\left(x-x_{i}\right)+\frac{1}{2}f^{''}\left(x_{i}\right)\left(x-x_{i}\right)^{2}+\frac{1}{3!}f^{'''}\left(\xi \right)\left(x-x_{i}\right)^{3}$

2.方案二：提供三个初始点 $\left(a,A\right), \left(b,B\right), \left(c,C\right)$ 确定通过三点的抛物线(Muller法)：

$y=\alpha +\beta x+\gamma x^{2}$

- 与 $x$ 轴出现两个交点，取离 $c$ 较近的点

- 与 $x$ 轴没有交点时，出现复数解

## 抛物线法

- 逆二次插值（Inverse Quadratic Interpolation）

$x=P\left(y\right)=a\frac{\left(y-B\right)\left(y-C\right)}{\left(A-B\right)\left(A-C\right)}+b\frac{\left(y-A\right)\left(y-C\right)}{\left(B-A\right)\left(B-C\right)}+c\frac{\left(y-A\right)\left(y-B\right)}{\left(C-A\right)\left(C-B\right)}$

与 $x$ 轴的交点

$P\left(0\right)=c-\frac{r\left(r-q\right)\left(c-b\right)+\left(1-r\right)s\left(c-a\right)}{\left(q-1\right)\left(r-1\right)\left(s-1\right)}$

$q=\frac{A}{B}, r=\frac{C}{B}, s=\frac{C}{A}$

迭代格式：

$x_{i+3}=x_{i+2}-\frac{r\left(r-q\right)\left(x_{i+2}-x_{i+1}\right)+\left(1-r\right)s\left(x_{i+2}-x_{i}\right)}{\left(q-1\right)\left(r-1\right)\left(s-1\right)}$

## 抛物线法

- Muller方法与IQI方法的不同

![](images/8c6458b9f91c930711aa3d3e531e90cc25a1568a88220a43a1140ca12761cbb5.jpg)

IQI

Muller

## Brent混合方法

- Brent混合方法的思路：兼顾收敛与稳定
    1. 记录当前点 $x_{i}（$ 具有最优后向误差），同时记录包含根的区间 $\left[a_{i}, b_{i}\right]$
    2. 尝试IQI法，如果：i.后向误差减小；ii.包含根的区间至少减半。则用新的点替换原来的一个
    3. 否则尝试割线法，如果割线法也失败则用二分法。

## 非线性方程组的牛顿迭代

- 包含 $n$ 未知数的 $n$ 个非线性方程组：

$\left\{\begin{array}{c}f_{1}\left(x_{1},x_{2},\ldots ,x_{n}\right)=0\\f_{2}\left(x_{1},x_{2},\ldots ,x_{n}\right)=0\\\vdots \\f_{n}\left(x_{1},x_{2},\ldots ,x_{n}\right)=0\end{array}\right.$

如何求解？

- 迭代思想：给定 $X_{i}=\left[x_{1}^{\left(i\right)},x_{2}^{\left(i\right)},\ldots ,x_{n}^{\left(i\right)}\right]^{T}$ 递推计算 $X_{i+1}$

- 线性化

$\left\{\begin{array}{c}0=f_{1}\left(X\right)\approx f_{1}\left(X_{i}\right)+\frac{\partial f_{1}\left(X_{i}\right)}{\partial x_{1}}\left(x_{1}-x_{1}^{\left(i\right)}\right)+\frac{\partial f_{1}\left(X_{i}\right)}{\partial x_{2}}\left(x_{2}-x_{2}^{\left(i\right)}\right)+\ldots +\frac{\partial f_{1}\left(X_{i}\right)}{\partial x_{n}}\left(x_{n}-x_{n}^{\left(i\right)}\right)\\0=f_{2}\left(X\right)\approx f_{2}\left(X_{i}\right)+\frac{\partial f_{2}\left(X_{i}\right)}{\partial x_{1}}\left(x_{1}-x_{1}^{\left(i\right)}\right)+\frac{\partial f_{2}\left(X_{i}\right)}{\partial x_{2}}\left(x_{2}-x_{2}^{\left(i\right)}\right)+\ldots +\frac{\partial f_{2}\left(X_{i}\right)}{\partial x_{n}}\left(x_{n}-x_{n}^{\left(i\right)}\right)\\\vdots \\0=f_{n}\left(X\right)\approx f_{n}\left(X_{i}\right)+\frac{\partial f_{n}\left(X_{i}\right)}{\partial x_{1}}\left(x_{1}-x_{1}^{\left(i\right)}\right)+\frac{\partial f_{n}\left(X_{i}\right)}{\partial x_{2}}\left(x_{2}-x_{2}^{\left(i\right)}\right)+\ldots +\frac{\partial f_{n}\left(X_{i}\right)}{\partial x_{n}}\left(x_{n}-x_{n}^{\left(i\right)}\right)\end{array}\right.$

定义： $F=\left[f_{1},f_{2},\ldots ,f_{3}\right]^{T},$ **Jacobi矩阵：** $J\left(X\right)=F^{'}(X)=\left(\begin{matrix}\frac{\partial f_{1}\left(X\right)}{\partial x_{1}}&\cdots &\frac{\partial f_{1}\left(X\right)}{\partial x_{n}}\\\vdots &\ddots &\vdots \\\frac{\partial f_{n}\left(X\right)}{\partial x_{1}}&\cdots &\frac{\partial f_{n}\left(X\right)}{\partial x_{n}}\end{matrix}\right)$

线性化方程可写成： $F\left(X_{i}\right)+J\left(X_{i}\right)\left(X-X_{i}\right)=0$

→牛顿迭代： $X_{i+1}=X_{i}-J^{-1}\left(X_{i}\right)F\left(X_{i}\right)$

## 非线性方程组的牛顿迭代

- 例：求解方程组

$\left\{\begin{array}{c}f_{1}\left(u,v\right)=v-u^{3}=0\\f_{2}\left(u,v\right)=u^{2}+v^{2}-1=0\end{array}\right.$

Jacobi矩阵

$J\left(u,v\right)=\left[\begin{matrix}-3u^{2}&1\\2u&2v\end{matrix}\right]$

牛顿迭代式 $\left(X=\left[u,v\right]^{T},F=\left[f_{1},f_{2}\right]\right)$ ：

$J\left(u_{i},v_{i}\right)\left(X_{i+1}-X_{i}\right)=-F\left(X_{i}\right)$

取 $X_{0}=\left[1,2\right]$

第一步迭代计算为

$\left[\begin{matrix}-3&1\\2&4\end{matrix}\right]\left[\begin{array}{c}u_{i+1}-u_{i}\\v_{i+1}-v_{i}\end{array}\right]=-\left[\begin{array}{c}1\\4\end{array}\right]\Longrightarrow \left[\begin{array}{c}u_{i+1}\\v_{i+1}\end{array}\right]=\left[\begin{array}{c}1\\1\end{array}\right]$

## 非线性方程组的牛顿迭代

![](images/1b8d44918556127bd47da8f8decc98177f91f315e7c73c73c157bbf78ab8881f.jpg)

计算机迭代过程

![](images/8fa6ea3cc68b919c6514442cc36be2ad4f40ad52181d0df1b0b3484d492e1a77.jpg)

迭代过程的图像

## 思考与练习

- 对以下几种计算 $\sqrt[4]{2}$ 的算法的收敛速率从最快到最慢排序，并说明理由

1. 使用二分法求解 $f\left(x\right)=x^{4}-2=0$
2. 使用割线法求解 $f\left(x\right)=x^{4}-2=0$
3. 通过迭代求 $g\left(x\right)=\frac{x}{2}+\frac{1}{x^{3}}$ 的不动点
4. 通过迭代求 $g\left(x\right)=\frac{5x}{6}+\frac{1}{3x^{3}}$ 的不动点
5. 使用牛顿法求解 $f\left(x\right)=x^{4}-2=0$

- *如果* $f\left(x\right)\in C^{m}\left(\mathbb{R}\right)，$ *并满足* $f\left(r\right)=0, f^{'}\left(r\right)\ne 0, f^{''}\left(r\right)=\ldots =f^{\left(m-1\right)}\left(r\right)=0,$

$f^{\left(m\right)}\left(r\right)\ne 0 \left(m>2\right) ,$ 试分析标准牛顿迭代法的收敛性及误差。

## 练习与思考

- 找出函数 $g\left(x\right)=x^{2}-\frac{3}{2}x+\frac{3}{2}$ 的每个不动点，并确定不动点迭代是否局部收敛\$ \$
- 令 $f\left(x\right)=x^{4}-7x^{3}+18x^{2}-20x+8$ ,牛顿法是否会二次收敛到根 $r=2$ ？确定 $\lim_{i\to \infty }e_{i+1}/e_{i}$
- 取 $\left(u_{0},v_{0}\right)=(1,1)$ ，使用牛顿迭代进行两步迭代求解

$\left\{\begin{array}{c}u^{2}+v^{2}=1\\\left(u-1\right)^{2}+v^{2}=1\end{array}\right.$

- 编程：使用二分法、不动点迭代、牛顿法、试位法求 $e^{x}+x=7$ 的根,结果精确到小数点后8位，并对各方法的收敛性进行比较。