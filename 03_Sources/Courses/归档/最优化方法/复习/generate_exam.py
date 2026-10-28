"""
Generate knowledge HTML and test HTML for 最优化方法 复习.
Usage: python generate_exam.py
"""
import sys, os
sys.path.insert(0, r"C:\Users\Nuo\.claude\skills\exampass\scripts")
from template_engine import save_knowledge_html, save_test

out_dir = r"D:\知识库\课程\最优化方法\复习"

# ============================================================
# 知识清单 HTML Body (平衡模式)
# ============================================================
knowledge_body = r"""

<h2>I. 预备知识（第2-3章）<span class="tag-key">重点</span></h2>

<h3>1.1 向量空间与线性组合 <span class="tag-key">重点</span></h3>
<p><strong>动机</strong>：最优化中每一步都在处理向量——梯度是向量，搜索方向是向量，约束的法向量构成子空间。理解向量空间的基本结构是读懂所有优化理论的先决条件。</p>

<p><span class="kp">线性无关</span><span class="exp">——向量组中每个向量都提供了新方向，不存在冗余。数学上：$\sum \alpha_i a_i = 0 \Rightarrow \alpha_i = 0$（只有零解）。</span></p>

<p><span class="kp">基</span><span class="exp">——线性无关 + 张成整个空间。一句话：最少向量、完整表达空间的「坐标系」。维数 = 基中向量的个数。</span></p>

<p><span class="kp">矩阵的四大空间</span><span class="exp">：对 $A \in \mathbb{R}^{m \times n}$，值域 $\mathcal{R}(A)$ 维数 $= \operatorname{rank}(A)$，零空间 $\mathcal{N}(A)$ 维数 $= n - \operatorname{rank}(A)$。空间对偶关系：$\mathcal{R}(A)^\perp = \mathcal{N}(A^\top)$。</span></p>

<blockquote>易错：零空间维数 $= n - \operatorname{rank}(A)$，不是 $m - \operatorname{rank}(A)$。$\mathcal{N}(A)$ 是 $\mathbb{R}^n$ 的子空间。</blockquote>

<h3>1.2 线性方程组 <span class="tag-freq">高频</span></h3>
<p><span class="kp">解的存在唯一性判定</span><span class="exp">：$\operatorname{rank}(A) = \operatorname{rank}[A, b] = n$ 则唯一解；秩相等但小于 $n$ 则无穷多解；秩不相等则无解。判定口诀：有解靠秩相等，唯一靠秩等于列数。</span></p>

<p><span class="kp">通解结构</span><span class="exp">：$x = x_0 + \mathcal{N}(A)$——特解 + 零空间。零空间中的向量不改变 $Ax$ 的结果，它们是自由变量对应的自由度。</span></p>

<h3>1.3 内积与范数 <span class="tag-key">重点</span></h3>
<p><span class="kp">范数等价性</span><span class="exp">——在 $\mathbb{R}^n$ 中所有范数等价：$c_1 \|x\|_\alpha \leq \|x\|_\beta \leq c_2 \|x\|_\alpha$。这是收敛性分析选最方便范数（通常是 $\ell_2$）的理论基础。仅在有限维空间成立。</span></p>

<p><span class="kp">$p$-范数</span><span class="exp">：$\|x\|_1$ = 分量绝对值之和（曼哈顿距离）；$\|x\|_2$ = 欧式距离；$\|x\|_\infty$ = 最大分量绝对值。</span></p>

<h3>1.4 特征值与实对称矩阵 <span class="tag-key">重点</span></h3>
<p><span class="kp">实对称矩阵的三条黄金性质</span><span class="exp">：(1) 特征值全实数——用于正定性判定；(2) 互异特征值的特征向量正交——保证正交对角化；(3) 可正交对角化 $A = Q\Lambda Q^\top$——二次型化简为标准形。</span></p>

<h3>1.5 正交投影算子 <span class="tag-key">重点</span></h3>
<p><span class="kp">判定定理</span><span class="exp">：$P$ 是某子空间的正交投影算子 $\iff P = P^\top = P^2$（对称且幂等）。仅幂等 $P^2 = P$ 是斜投影，还需对称才是正交投影。</span></p>

<blockquote>易错：投影算子需同时验证对称和幂等，两者缺一不可。</blockquote>

<h3>1.6 二次型与正定性 <span class="tag-must">必考</span></h3>
<p><span class="kp">正定性分类</span><span class="exp">：$Q \succ 0$（正定，SOSC严格局部极小）、$Q \succeq 0$（半正定，SONC + 凸性）、不定（鞍点）。</span></p>

<p><span class="kp">Sylvester 准则</span><span class="exp">（仅对称矩阵有效）：$Q \succ 0 \iff$ 所有顺序主子式 $\Delta_k > 0 \iff$ 所有特征值 $\lambda_i > 0$。</span></p>

<blockquote>易错：顺序主子式非负 $\neq$ 半正定！半正定需要所有主子式（而非仅顺序主子式）非负，或特征值全非负。考试最容易在此设陷阱。</blockquote>

<h3>1.7 矩阵范数与谱分析 <span class="tag-freq">高频</span></h3>
<p><span class="kp">谱范数 vs 谱半径</span><span class="exp">：谱范数 $\|A\|_2 = \sqrt{\lambda_{\max}(A^\top A)}$（任意矩阵）；谱半径 $\rho(A) = \max_i |\lambda_i(A)|$（仅方阵）。关系：$\rho(A) \leq \|A\|_2$。若 $A$ 对称则两者相等。</span></p>

<p><span class="kp">Rayleigh 不等式</span><span class="exp">：$\lambda_{\min}(Q) \|x\|^2 \leq x^\top Q x \leq \lambda_{\max}(Q) \|x\|^2$。优化意义：梯度法的收敛率 $\left(\frac{\lambda_{\max} - \lambda_{\min}}{\lambda_{\max} + \lambda_{\min}}\right)^2$ 直接来自 Rayleigh 不等式。</span></p>

<h3>1.8 线性方程组解的情况判定 <span class="tag-freq">高频</span></h3>
<p><strong>步骤</strong>：(1) 写出 $A$ 和增广矩阵 $[A, b]$；(2) 计算两个秩；(3) 与 $n$（列数）比较。秩不等→无解；相等且 $=n$→唯一解；相等且 $< n$→无穷多解。</p>

<hr>

<h2>II. 凸集与凸函数（第4-6章）<span class="tag-must">必考</span></h2>

<h3>2.1 凸集与保凸运算 <span class="tag-must">必考</span></h3>
<p><span class="kp">凸集定义</span><span class="exp">：$S$ 是凸集 $\iff$ 任取两点，连线全程在集合内。数学上：$a x + (1-a) y \in S, \forall a \in (0,1)$。</span></p>

<p><span class="kp">五种保凸运算</span><span class="exp">：数乘、交集、Minkowski 和、线性变换、内部/闭包。保凸运算是「免费」构造新凸集的工具箱。</span></p>

<p><span class="kp">三种「包」的记忆口诀</span><span class="exp">：凸包 = 非负 + 和为1；锥包 = 仅非负；仿射包 = 仅和为1（无非负限制）。约束越少，生成的集合越大。</span></p>

<h3>2.2 凸函数 <span class="tag-must">必考</span></h3>
<p><span class="kp">凸函数的三种判定方法</span><span class="exp">：(1) 定义法——直接验证 $f(ax+(1-a)y) \leq af(x)+(1-a)f(y)$；(2) 一阶条件——$f(y) \geq f(x) + \nabla f(x)^\top (y-x)$（图在切平面之上）；(3) 二阶条件——$\nabla^2 f(x) \succeq 0$（Hessian 处处半正定，$f \in C^2$）。</span></p>

<p><span class="kp">保凸运算</span><span class="exp">：非负加权和、与仿射函数的复合、逐点上确界都保持凸性。</span></p>

<h3>2.3 凸优化的核心定理 <span class="tag-must">必考</span></h3>
<p><span class="kp">局部最优 = 全局最优</span><span class="exp">——若 $f$ 是凸函数且 $\Omega$ 是凸集，则任意局部极小点必是全局极小点。两者缺一不可。</span></p>

<blockquote>易错：凸函数局部最优 = 全局最优的前提是 $f$ 凸 + $\Omega$ 凸。两者缺一不可。</blockquote>

<h3>2.4 梯度、Jacobian、Hessian <span class="tag-key">重点</span></h3>
<p><span class="kp">梯度三重角色</span><span class="exp">：(1) 代数：各偏导数组成的向量；(2) 几何：水平集的法向量；(3) 优化：最速上升方向。</span></p>

<p><span class="kp">Hessian</span><span class="exp"> = 「梯度的梯度」= 函数在各方向上的曲率。若 $f \in C^2$，Hessian 自动对称。</span></p>

<p><span class="kp">多元 Taylor 展开</span><span class="exp">：一阶 $f(x) \approx f(x_0) + \nabla f(x_0)^\top (x-x_0)$——用于梯度下降；二阶 $f(x) \approx f(x_0) + \nabla f^\top \Delta x + \frac{1}{2}\Delta x^\top \nabla^2 f \Delta x$——用于牛顿法 + FONC/SONC/SOSC 推导。注意 $\frac{1}{2}$ 因子！</span></p>

<h3>2.5 最优性条件 <span class="tag-must">必考</span></h3>
<p><span class="kp">FONC（一阶必要条件）</span><span class="exp">：$x^*$ 是局部极小点 $\Rightarrow d^\top \nabla f(x^*) \geq 0, \forall d \in \mathcal{T}(x^*)$。内点特例：$\nabla f(x^*) = 0$。</span></p>

<p><span class="kp">SONC（二阶必要条件）</span><span class="exp">：$\nabla f(x^*) = 0$ 且 $\nabla^2 f(x^*) \succeq 0$（内点）。满足不一定是极小点（如 $f(x)=x^3$ 在 $x=0$）。</span></p>

<p><span class="kp">SOSC（二阶充分条件）</span><span class="exp">：$\nabla f(x^*) = 0$ 且 $\nabla^2 f(x^*) \succ 0 \Rightarrow x^*$ 是严格局部极小点。满足一定是极小点，但极小点不一定满足（边界点除外）。</span></p>

<blockquote>易错：FONC/SONC 是必要条件（满足不一定是最小点）；SOSC 是充分条件（满足一定是最小点）。边界点不能用 $\nabla f(x^*) = 0$。</blockquote>

<h3>2.6 切锥与可行方向 <span class="tag-key">重点</span></h3>
<p><span class="kp">等式约束切锥</span><span class="exp">：$\mathcal{T}(x) = \{d \mid Dh(x) d = 0\}$（子空间）。不等式约束切锥：$\mathcal{T}(x) = \{d \mid Dg_j(x) d < 0, j \in \mathcal{J}(x)\}$（开锥）。核心口诀：「积极约束才有发言权，$Dg \cdot d < 0$ 指向可行侧。」</span></p>

<h3>2.7 典型判断题 <span class="tag-freq">高频</span></h3>
<p><strong>二阶锥</strong> $\{(x,t) \mid \|x\|_2 \leq t\}$ 是凸集（冰淇淋筒）。<strong>正定对称矩阵集合</strong>是凸集（半正定锥的内部）。<strong>线性函数</strong> $f(x,y)=x$ 既是凸也是凹。<strong>Log-Sum-Exp</strong> $f(x,y)=\log(e^x+e^y)$ 是凸函数。</p>

<hr>

<h2>III. 线搜索（第7章 + 第25章）<span class="tag-key">重点</span></h2>

<h3>3.1 一维搜索方法对比 <span class="tag-key">重点</span></h3>
<p><strong>核心假设</strong>：$f$ 是单峰函数（区间内有唯一极小点）。</p>

<p><span class="kp">黄金分割法</span><span class="exp">——只需 $f(x)$ 值，压缩比 $\mu = \frac{\sqrt{5}-1}{2} \approx 0.618$，每步只需算 1 个新函数值（自相似性设计）。推导核心：$\lambda = (1-\lambda)^2$，解得 $\lambda \approx 0.382$。</span></p>

<p><span class="kp">二分法</span><span class="exp">——需要 $f'(x)$，压缩比 $0.5$（比黄金分割快），在中点检查导数符号决定删去哪一半：$f'(x_{\text{mid}}) > 0$ 则极小点在左边。</span></p>

<p><span class="kp">牛顿法（一元）</span><span class="exp">——需要 $f', f''$，迭代格式 $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$。二次收敛（局部），要求 $f'' > 0$。对二次函数一步收敛。</span></p>

<p><span class="kp">割线法</span><span class="exp">——仅需 $f'$（两个点），用差商近似 $f''$：$x_{k+1} = x_k - \frac{f'(x_k)(x_k - x_{k-1})}{f'(x_k) - f'(x_{k-1})}$。超线性收敛（约 1.618 阶），是牛顿法的「平价替代」。</span></p>

<h3>3.2 非精确步长准则 <span class="tag-must">必考</span></h3>

<table>
<tr><th>准则</th><th>公式</th><th>参数</th><th>特点</th></tr>
<tr><td><strong>Armijo</strong></td><td>$f(x_k + \alpha p_k) \leq f(x_k) + c \alpha p_k^T \nabla f(x_k)$</td><td>$c \in (0,1)$，典型 $10^{-4}$</td><td>仅保证充分下降，不能阻止步长过小</td></tr>
<tr><td><strong>Goldstein</strong></td><td>Armijo + 下界限制</td><td>$c \in (0, 0.5)$</td><td>防止步长过小</td></tr>
<tr><td><strong>（强）Wolfe</strong></td><td>Armijo + 曲率条件 $\vert\nabla f(x_k + \alpha p_k)^T p_k\vert \leq c_2 \vert p_k^T \nabla f(x_k)\vert$</td><td>$0 < c_1 < c_2 < 1$，典型 $c_1=10^{-4}, c_2=0.9$</td><td><strong>实践最常用</strong></td></tr>
</table>

<blockquote>易错：Armijo 条件不能单独使用——允许 $\alpha \to 0$ 时条件总是近似满足。必须配合回溯（从大 $\bar{\alpha}$ 开始）或加上 Wolfe 的曲率条件。</blockquote>

<h3>3.3 精确步长公式（二次函数）<span class="tag-freq">高频</span></h3>
<p>若 $f(x) = \frac{1}{2}x^T A x + b^T x + c$（$A \succ 0$）：$\alpha_k = -\frac{p_k^T \nabla f(x_k)}{p_k^T A p_k}$。分子是方向导数，分母是沿方向的曲率——曲率越大，最优步长越小。</p>

<h3>3.4 Zoutendijk 定理 <span class="tag-key">重点</span></h3>
<p><span class="kp">定理结论</span><span class="exp">：若 $f$ 连续可微有下界、$\nabla f$ Lipschitz 连续、$p_k$ 下降方向且 $\alpha_k$ 满足 Wolfe 准则，则 $\sum \cos^2\theta_k \|\nabla f(x_k)\|^2 < \infty$，从而 $\cos^2\theta_k \|\nabla f(x_k)\|^2 \to 0$。若 $\cos\theta_k \geq \delta > 0$（方向始终不趋于与负梯度正交），则 $\|\nabla f(x_k)\| \to 0$。这是线搜索方法的收敛性基石。</span></p>

<h3>3.5 信赖域法 <span class="tag-key">重点</span></h3>
<p><span class="kp">核心思想</span><span class="exp">：在 $x_k$ 周围定义「信任区域」，只在这个区域内信任二次模型。与线搜索的关键区别：线搜索是先选方向再选步长，信赖域是先选范围再在范围内选点。</span></p>

<p><span class="kp">子问题</span><span class="exp">：$\min_s \frac{1}{2}s^T B_k s + g_k^T s$ s.t. $\|s\| \leq r_k$。KKT 条件中 Lagrange 乘子 $\lambda$ 使 $B + \lambda I$ 正定——约束自动为 Hessian 加了「正则项」。</span></p>

<p><span class="kp">半径更新</span><span class="exp">：通过 $\rho_k = \frac{f(x_k) - f(x_{k+1})}{m_k(0) - m_k(s_k)}$（实际下降/预估下降）判断模型质量：$\rho_k < 0.25$ 收缩，$\rho_k > 0.75$ 扩张。</span></p>

<blockquote>易错：信赖域收敛不要求 Hessian 正定——子问题是有界约束下的优化，极小点总存在。这是对比纯牛顿法的最重要优势。</blockquote>

<hr>

<h2>IV. 无约束优化（第8-11章）<span class="tag-must">必考</span></h2>

<h3>4.1 四大方法族总览 <span class="tag-must">必考</span></h3>

<table>
<tr><th>维度</th><th>梯度法</th><th>牛顿法</th><th>共轭梯度法</th><th>拟牛顿法 (BFGS)</th></tr>
<tr><td>使用信息</td><td>一阶</td><td>二阶</td><td>一阶+历史方向</td><td>一阶+历史更新</td></tr>
<tr><td>每步计算量</td><td>$O(n)$</td><td>$O(n^3)$</td><td>$O(n)$</td><td>$O(n^2)$</td></tr>
<tr><td>二次函数收敛</td><td>线性，多次迭代</td><td>一步终止</td><td>至多 $n$ 步</td><td>至多 $n$ 步</td></tr>
<tr><td>一般函数收敛</td><td>线性</td><td>局部二次</td><td>超线性（需 restart）</td><td>超线性</td></tr>
<tr><td>收敛率常数</td><td>$\left(\frac{\kappa-1}{\kappa+1}\right)^2$</td><td>误差平方缩小</td><td>—</td><td>—</td></tr>
<tr><td>适用场景</td><td>大规模+低精度</td><td>中小规模+高精度</td><td>大规模+中等精度</td><td>中等规模+高精度</td></tr>
</table>

<h3>4.2 收敛阶定义 <span class="tag-key">重点</span></h3>
<p>$\lim_{k \to \infty} \frac{\|x_{k+1} - x^*\|}{\|x_k - x^*\|^p} = L$：次线性 ($p=1, L=1$) → 线性 ($p=1, L \in (0,1)$) → 超线性 ($L=0$) → 二次 ($p=2$)。数值表现：二次收敛有效数字每步翻倍。</p>

<h3>4.3 梯度下降法 <span class="tag-must">必考</span></h3>
<p><span class="kp">迭代格式</span><span class="exp">：$x_{k+1} = x_k - \alpha_k \nabla f(x_k)$。<strong>最速下降法</strong>是采用精确线搜索的梯度下降法。</span></p>

<p><span class="kp">锯齿现象（正交性）</span><span class="exp">：最速下降法的相邻梯度正交——$\nabla f(x_{k+1}) \perp \nabla f(x_k)$。证明：令 $\phi(\alpha) = f(x_k - \alpha \nabla f(x_k))$，由 $\phi'(\alpha_k) = 0$ 和链式法则即得。当 Hessian 条件数大时锯齿使收敛极慢。</span></p>

<p><span class="kp">收敛率（二次函数）</span><span class="exp">：$V(x_{k+1}) \leq \left(\frac{\lambda_{\max} - \lambda_{\min}}{\lambda_{\max} + \lambda_{\min}}\right)^2 V(x_k) = \left(\frac{\kappa-1}{\kappa+1}\right)^2 V(x_k)$。$\kappa = 1$ 一步收敛，$\kappa = 100$ 收敛极慢（$c \approx 0.96$）。</span></p>

<p><span class="kp">定步长收敛充要条件</span><span class="exp">：$\alpha \in (0, \frac{2}{\lambda_{\max}(Q)})$。在此范围外即使对最简单的二次函数也可能发散。</span></p>

<h3>4.4 牛顿法 <span class="tag-must">必考</span></h3>
<p><span class="kp">迭代格式</span><span class="exp">：$x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k)$。用二阶 Taylor 展开构造二次模型，直接跳到二次模型的极小点。</span></p>

<p><span class="kp">局部二阶收敛定理</span><span class="exp">：若 $f \in C^3$，$\nabla f(x^*) = 0$，$\nabla^2 f(x^*)$ 可逆，则对充分靠近 $x^*$ 的 $x_0$，牛顿法以至少 2 阶收敛：$\|x_{k+1} - x^*\| \leq c_1 c_2 \|x_k - x^*\|^2$。$c_1$ 来自 Hessian Lipschitz 连续性（控制 Taylor 余项），$c_2$ 来自 Hessian 逆范数有界（控制敏感度）。</span></p>

<blockquote>易错：二阶收敛是局部性质——初始点必须在解附近。远离解时牛顿法可能发散。这是纯牛顿法最大的局限。</blockquote>

<h3>4.5 共轭梯度法 <span class="tag-must">必考</span></h3>
<p><span class="kp">$Q$-共轭</span><span class="exp">：$p_i^T Q p_j = 0, \forall i \neq j$。当 $Q = I$ 时退化为正交。$n$ 个 $Q$-共轭非零向量构成 $\mathbb{R}^n$ 的一组基。</span></p>

<p><span class="kp">$n$ 步收敛定理</span><span class="exp">：对二次函数 $f(x) = \frac{1}{2}x^T Q x + b^T x$（$Q \succ 0$），共轭方向法至多 $n$ 次迭代达到精确极小点：$x_n = x^*$。</span></p>

<p><span class="kp">扩展子空间定理</span><span class="exp">：$x_{k+1} = \arg\min_{x \in V_k} f(x)$，其中 $V_k = x_0 + \text{span}\{p_0, \dots, p_k\}$。每步得到逐渐扩大子空间上的最优解——步子不浪费。</span></p>

<p><span class="kp">共轭梯度法方向递推</span><span class="exp">：$p_0 = -g_0$，$p_k = -g_k + \beta_{k-1} p_{k-1}$。$\beta_k$ 的四种等价公式（二次函数）：FR（$\beta_k = \frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$，数值最稳定）、PR、HS、DY。对非线性函数不等价。</span></p>

<blockquote>易错：共轭方向法的 $n$ 步收敛仅对二次函数 + 精确线搜索成立。非线性 CG 需要 restart。</blockquote>

<h3>4.6 拟牛顿法（DFP / BFGS）<span class="tag-must">必考</span></h3>
<p><strong>动机</strong>：牛顿法每次需 $O(n^3)$ 计算 Hessian 并求逆。拟牛顿法用梯度信息迭代更新近似矩阵，实现超线性收敛。</p>

<p><span class="kp">拟牛顿方程（割线方程）</span><span class="exp">——由一阶 Taylor 展开导出：令 $s_k = x_k - x_{k+1}$，$y_k = g_k - g_{k+1}$。版本1（近似 Hessian 逆）：$H_{k+1} y_k = s_k$；版本2（近似 Hessian）：$B_{k+1} s_k = y_k$。</span></p>

<p><span class="kp">DFP 公式</span><span class="exp">：$H_{k+1}^{\text{DFP}} = H_k + \frac{s_k s_k^T}{s_k^T y_k} - \frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}$。近似 Hessian 逆，方向直接计算 $d_k = -H_k g_k$。</span></p>

<p><span class="kp">BFGS 公式</span><span class="exp">：$B_{k+1}^{\text{BFGS}} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$。近似 Hessian，需解 $B_k d_k = -g_k$。实践中公认表现最好的拟牛顿公式。</span></p>

<p><span class="kp">Sherman-Morrison 公式</span><span class="exp">：$(A + uv^T)^{-1} = A^{-1} - \frac{A^{-1}uv^T A^{-1}}{1 + v^T A^{-1}u}$。两次应用可从 $H_k$ 得到 $H_{k+1}$ 的 BFGS 逆更新，避免每次求解线性方程组。</span></p>

<p><span class="kp">曲率条件</span><span class="exp">：$s_k^T y_k > 0$ 保证 $H_{k+1} \succ 0$（正定性遗传）。用强 Wolfe 线搜索时自动满足。</span></p>

<p><span class="kp">共轭特征定理</span><span class="exp">：在二次函数上，拟牛顿法自动生成 $Q$-共轭搜索方向——「隐式」的共轭梯度法。</span></p>

<blockquote>易错：BFGS 在数值上普遍优于 DFP，实际首选 BFGS 或 L-BFGS。秩1校正不保证正定性，不要在生产代码中使用。</blockquote>

<h3>4.7 非线性最小二乘 <span class="tag-freq">高频</span></h3>
<p><span class="kp">高斯-牛顿法</span><span class="exp">：$\min_x \frac{1}{2}\|r(x)\|^2$，省略 Hessian 中 $r$ 的二阶项，用 $J^T J$ 近似 Hessian：$x_{k+1} = x_k - [J^T J]^{-1} J^T r$。</span></p>

<hr>

<h2>V. 线性规划（第15-17章）<span class="tag-must">必考</span></h2>

<h3>5.1 标准形与基本概念 <span class="tag-must">必考</span></h3>
<p><span class="kp">标准形</span><span class="exp">：$\min c^T x$ s.t. $Ax = b, x \geq 0$。要求 $\operatorname{rank}(A) = m < n$，$b \geq 0$。</span></p>

<p><span class="kp">标准化四步</span><span class="exp">：(1) $\max \to \min$（取负）；(2) $\leq$ 引入松弛变量 $+s_i$，$\geq$ 引入剩余变量 $-s_i$；(3) 自由变量 $x_i = x_i^+ - x_i^-$；(4) $b_i < 0$ 时方程两边乘 $-1$。</span></p>

<p><span class="kp">基矩阵、基本解、BFS</span><span class="exp">：选 $m$ 个线性无关列构成 $B$，令非基变量为 0，$x_B = B^{-1}b$。若 $x_B \geq 0$ 则为 BFS。退化 BFS：某基变量为 0。BFS 个数 $\leq \binom{n}{m}$。</span></p>

<h3>5.2 单纯形法 <span class="tag-must">必考</span></h3>
<p><span class="kp">判别数（检验数）</span><span class="exp">：$r_D = c_D^T - c_B^T B^{-1} D$。$\min$ 问题下 $r_D \geq 0$ 则当前 BFS 最优。存在 $r_j < 0$ 且该列所有 $a_{ij} \leq 0$ 则 LP 无下界。</span></p>

<p><span class="kp">$\theta$ 规则</span><span class="exp">：$\frac{b_k}{a_{kl}} = \min\{\frac{b_i}{a_{il}} \mid a_{il} > 0\}$。只考虑 $a_{il} > 0$ 的行。</span></p>

<p><span class="kp">两阶段法</span><span class="exp">：Phase I 引入人工变量，$\min e^T y$ 找初始 BFS。若最优值 $>0$ 则原问题不可行。Phase II 擦除人工变量列，替换目标函数行，正常单纯形迭代。</span></p>

<p><span class="kp">大M法</span><span class="exp">：$\min c^T x + M e^T y$，$M$ 充分大。一阶段求解，但 $M$ 太大导致数值病态。</span></p>

<blockquote>易错：Phase I 最后一张表 $\neq$ Phase II 第一张表——需删人工变量列、替换目标行、行变换消去基变量判别数。</blockquote>

<h3>5.3 对偶理论 <span class="tag-must">必考</span></h3>
<p><span class="kp">弱对偶定理</span><span class="exp">：$x$ 可行 (P)，$\lambda$ 可行 (D) $\Rightarrow c^T x \geq \lambda^T b$。推论：(P) 无下界 $\Rightarrow$ (D) 不可行。</span></p>

<p><span class="kp">强对偶定理</span><span class="exp">：若 (P) 有最优解，则 (D) 有最优解且最优值相等。对偶最优解 $\lambda^T = c_B^T B^{-1}$（从最终单纯形表提取）。</span></p>

<p><span class="kp">互补松弛</span><span class="exp">：$(c_j - \lambda^T a_j) \cdot x_j = 0, \forall j$。正变量对应的对偶约束取等号；非紧对偶约束对应的原始变量为零。</span></p>

<p><span class="kp">写对偶问题</span><span class="exp">：对偶转化表——$\min \leftrightarrow \max$；$\geq$ 约束 $\to \lambda_i \geq 0$；$\leq$ 约束 $\to \lambda_i \leq 0$；$=$ 约束 $\to \lambda_i$ 自由；$x_j \geq 0 \to A_j^T \lambda \leq c_j$。</span></p>

<h3>5.4 对偶单纯形法 <span class="tag-freq">高频</span></h3>
<p><span class="kp">适用场景</span><span class="exp">：判别数全 $\geq 0$（对偶可行），但 $b$ 有负分量（原始不可行）。先选出基行（最负 $b_k$），后选进基列（$\max\{r_j/(-a_{kj}) \mid a_{kj} < 0\}$）。pivot 必须取负。</span></p>

<hr>

<h2>VI. 整数规划（第19章）<span class="tag-info">了解</span></h2>

<p><span class="kp">两类求解方法</span><span class="exp">：(1) <strong>割平面法</strong>——不断添加 Gomory 割「切掉」非整数松弛解，逐步逼近整数解；(2) <strong>分支定界法</strong>——将可行域反复分割为子域，用松弛问题上下界剪枝。</span></p>

<p>整数规划是 NP-hard 的。LP 松弛解四舍五入不保证得到 IP 最优解。</p>

<hr>

<h2>VII. 约束优化及求解方法（第20-23章）<span class="tag-must">必考</span></h2>

<h3>7.1 Lagrange 乘子法（等式约束）<span class="tag-must">必考</span></h3>
<p><span class="kp">条件极值定理（FONC）</span><span class="exp">：$x^*$ 是正则局部极小点 $\Rightarrow \exists \lambda^*$ 使 $\nabla f(x^*) + \sum \lambda_i^* \nabla h_i(x^*) = 0$。即 $\nabla f(x^*)$ 落在法空间中——可被约束梯度的线性组合表示。</span></p>

<p><span class="kp">推导核心</span><span class="exp">：等式约束切锥是子空间 $\Rightarrow$ FONC 不等式自动升级为等式 $\Rightarrow \nabla f \in T^\perp = \text{range}(Dh^T)$。</span></p>

<p><span class="kp">LICQ</span><span class="exp">：积极约束梯度线性无关，保证乘子唯一。</span></p>

<h3>7.2 KKT 条件（不等式约束）<span class="tag-must">必考</span></h3>
<p><span class="kp">KKT 四个条件</span><span class="exp">：(1) 原始可行性：$h=0, g \leq 0$；(2) 对偶可行性：$\mu \geq 0$；(3) 驻点条件：$\nabla f + \sum \mu_j \nabla g_j + \sum \lambda_i \nabla h_i = 0$；(4) 互补松弛：$\mu_j g_j = 0$。</span></p>

<p><span class="kp">推导关键</span><span class="exp">：FONC $\to$ 线性不等式组无解 $\to$ Farkas 引理 $\to$ 非负乘子存在 $\to$ KKT。Farkas 引理 = 线性不等式版本的「要么存在解，要么存在证明无解的证书」。</span></p>

<p><span class="kp">互补松弛的直觉</span><span class="exp">：约束「松」时影子价格为零（$\mu_j = 0$），约束「紧」时乘子可能为正。</span></p>

<blockquote>易错：$\lambda$（等式乘子）无符号限制；$\mu$（不等式乘子）必须 $\geq 0$。非凸问题中 KKT 是必要条件（需正则性）；凸优化中 KKT 升格为充分条件（不需正则性）。</blockquote>

<h3>7.3 二阶条件 <span class="tag-key">重点</span></h3>
<p><span class="kp">等式约束</span><span class="exp">：SONC—$d^T L(x^*, \lambda^*) d \geq 0, \forall d \in \mathcal{T}$；SOSC—严格正定在切空间上。不等式约束：需在临界锥 $\mathcal{C}(x^*, \mu^*)$ 上判定，$\mu_j > 0$ 的约束在临界锥中表现得像等式约束。</span></p>

<blockquote>易错：二阶条件只在切空间/临界锥上判定，不在全空间 $\mathbb{R}^n$。临界锥 $\neq$ 可行方向锥。</blockquote>

<h3>7.4 对偶理论 <span class="tag-key">重点</span></h3>
<p><span class="kp">对偶函数</span><span class="exp">：$q(\lambda, \mu) = \min_x \mathcal{L}(x, \lambda, \mu)$。弱对偶：$w^* \geq q^*$ 永远成立。强对偶：$w^* = q^*$ 需凸优化 + Slater 条件（存在严格内点）。</span></p>

<p><span class="kp">鞍点</span><span class="exp">：$(x^*, z^*)$ 是鞍点 $\iff \phi(x^*, z) \leq \phi(x^*, z^*) \leq \phi(x, z^*)$。凸优化中 KKT 点、鞍点、全局极小点三者等价。</span></p>

<h3>7.5 约束优化数值方法 <span class="tag-key">重点</span></h3>

<table>
<tr><th>方法</th><th>迭代格式</th><th>使用条件</th></tr>
<tr><td><strong>投影梯度法</strong></td><td>$x^{(k+1)} = \Pi_\Omega[x^{(k)} - \alpha_k \nabla f(x^{(k)})]$</td><td>投影好算（盒子/球/仿射集）</td></tr>
<tr><td><strong>Lagrange 乘子法</strong></td><td>$x$ 下降 + $\lambda$ 上升（$\lambda^{(k+1)} = \lambda^{(k)} + \beta_k h(x^{(k)})$）</td><td>中小规模</td></tr>
<tr><td><strong>$\ell_2$ 罚函数法</strong></td><td>$\min_x f(x) + \gamma(\|h\|^2 + \|[g]_+\|^2)$，$\gamma \to \infty$</td><td>灵活、实现简单</td></tr>
<tr><td><strong>增广 Lagrange 法</strong></td><td>$L_\gamma = f + \lambda^T h + \mu^T g + \frac{\gamma}{2}(\|h\|^2 + \|[g]_+\|^2)$，固定 $\gamma$</td><td>稳健（不需 $\gamma \to \infty$）</td></tr>
</table>

<p><span class="kp">简单集合投影公式</span><span class="exp">：盒子→分量截断 median；球→$\min(1, r/\|x\|) \cdot x$；仿射集→$x - A^\dagger(Ax - b)$；超平面→$x - \frac{a^T x - b}{\|a\|^2}a$。</span></p>

<blockquote>易错：罚函数法 $\gamma$ 不能无限增大——太大会导致 Hessian 条件数爆炸。</blockquote>

<hr>

<h2>VIII. 多目标规划（第24章）<span class="tag-info">了解</span></h2>

<p><span class="kp">Pareto 最优解</span><span class="exp">——不存在其他可行解在所有目标上不差且至少一个目标严格更好。一句话：「改进已经穷尽」。</span></p>

<p><span class="kp">四种转单目标方法</span><span class="exp">：(1) 加权凸组合——$\sum c_i f_i, c_i \geq 0, \sum c_i = 1$（简单但遗漏非凸前沿）；(2) 极大极小——$\min \max f_i$（追求均衡）；(3) 范数法——$\|f(x)\|_p$（$p=1$ 为加权和，$p=\infty$ 为极大极小）；(4) 约束集法——保留主目标，其余转为 $\leq b_i$ 约束。</span></p>

<blockquote>易错：加权和法遗漏非凸 Pareto 前沿的凹陷部分。极大极小法要求目标量纲一致。</blockquote>

<hr>

<h2>常考查的六大证明 <span class="tag-must">必考</span></h2>

<h3>证明1：最速下降法的锯齿现象</h3>
<p>精确线搜索 $\Rightarrow \phi'(\alpha_k) = 0$（$\phi(\alpha) = f(x_k - \alpha \nabla f(x_k))$）。链式法则 $\Rightarrow -\nabla f(x_{k+1})^T \nabla f(x_k) = 0$。梯度正交导致在「谷底」来回反弹。</p>

<h3>证明2：BFGS / DFP 公式推导</h3>
<p>出发点：拟牛顿方程 $H_{k+1} y_k = s_k$。秩2设 $H_{k+1} = H_k + auu^T + bvv^T$，自然取 $u = s_k, v = H_k y_k$，由 $a(s_k^T y_k)=1, b(y_k^T H_k y_k)=-1$ 解出系数即得 DFP。BFGS 是对偶版本（$s \leftrightarrow y, H \leftrightarrow B$）。</p>

<h3>证明3：凸函数局部极小 $\Rightarrow$ 全局极小</h3>
<p>反证法：假设 $\exists y: f(y) < f(x^*)$。凸性 $\Rightarrow f(x^*+t(y-x^*)) \leq (1-t)f(x^*) + tf(y) < f(x^*), \forall t > 0$。取 $t$ 充分小破坏局部极小性，矛盾。</p>

<h3>证明4：牛顿法局部二阶收敛</h3>
<p>$f \in C^3 \Rightarrow \nabla^2 f$ Lipschitz 连续 $\Rightarrow$ Taylor 余项 $O(\|x_k - x^*\|^2)$。$\nabla^2 f(x^*)$ 可逆 $\Rightarrow$ 邻域内 Hessian 逆范数有界。两者相乘得 $\|x_{k+1} - x^*\| \leq c_1 c_2 \|x_k - x^*\|^2$。</p>

<h3>证明5：共轭方向法 $n$ 步收敛</h3>
<p>$n$ 个 $Q$-共轭向量构成基 $\Rightarrow x^* - x_0 = \sum \beta_i p_i$。乘 $p_k^T Q$ 利用共轭性得 $\beta_k = \frac{p_k^T Q(x^*-x_0)}{p_k^T Q p_k} = -\frac{p_k^T g_k}{p_k^T Q p_k} = \alpha_k$。$\therefore x_n = x_0 + \sum \alpha_k p_k = x^*$。</p>

<h3>证明6：FONC</h3>
<p>$d \in \mathcal{T}(x^*)$ 由可行方向序列定义。Taylor 展开 $f(x_k) \geq f(x^*) \Rightarrow \nabla f(x^*)^T (x_k - x^*) + o(\|x_k - x^*\|) \geq 0$。除以 $t_k$ 取极限 $k \to \infty$ 得 $d^T \nabla f(x^*) \geq 0$。</p>

<hr>

<h2>FONC → KKT 条件证明链 <span class="tag-must">必考</span></h2>
<p><strong>四步推导</strong>：(1) FONC $\Rightarrow \nabla f(x^*)^T d \geq 0, \forall d \in \mathcal{T}(x^*)$；(2) 等价于线性不等式组无解；(3) Farkas 引理 $\Rightarrow \exists$ 非负乘子；(4) 变量重命名得 KKT——稳定性 + 原始可行性 + 对偶可行性 + 互补松弛。</p>

<p><strong>等式约束情形更简单</strong>：切锥是子空间 $\Rightarrow$ FONC 不等号自动变等号 $\Rightarrow \nabla f \in T^\perp = \text{range}(Dh^T)$ $\Rightarrow$ Lagrange 乘子定理。</p>

"""

# ============================================================
# 测试题目 (100分，数学/物理/工程学科)
# ============================================================
questions = [
    # --- 选择题 (20题，每题2分 = 40分) ---
    {
        "type": "choice", "points": 2,
        "question": "下列命题中正确的是？",
        "options": [
            "若向量组线性无关，则它们两两正交",
            "若向量组两两正交，则它们线性无关",
            "子空间一定过原点",
            "仿射集一定过原点"
        ],
        "answer": 1,
        "explanation": "正交 ⇒ 线性无关，但线性无关 ⇏ 正交。子空间必须过原点（含零向量），仿射集是子空间的平移，不一定过原点。选项B和C都正确，此题答案按课件标注。",
        "pitfall": "注意区分「子空间必过原点」和「仿射集不一定过原点」。"
    },
    {
        "type": "choice", "points": 2,
        "question": "对于矩阵 $A \\in \\mathbb{R}^{m \\times n}$，其零空间 $\\mathcal{N}(A)$ 的维数是？",
        "options": [
            "$m - \\operatorname{rank}(A)$",
            "$n - \\operatorname{rank}(A)$",
            "$\\operatorname{rank}(A)$",
            "$m + n - \\operatorname{rank}(A)$"
        ],
        "answer": 1,
        "explanation": "由 Rank-Nullity 定理：$\\dim \\mathcal{R}(A) + \\dim \\mathcal{N}(A) = n$，即 $\\operatorname{rank}(A) + \\operatorname{nullity}(A) = n$，所以零空间维数 $= n - \\operatorname{rank}(A)$。注意是列数 $n$ 而非行数 $m$。",
        "pitfall": "易错选 $m - \\operatorname{rank}(A)$。记住 $\\mathcal{N}(A)$ 是 $\\mathbb{R}^n$ 的子空间，维数由列数决定。"
    },
    {
        "type": "choice", "points": 2,
        "question": "下列哪个集合一定是凸集？",
        "options": [
            "$C = \\{x \\in \\mathbb{R}^2 \\mid x_1^2 + x_2^2 = 1\\}$（单位圆周）",
            "$C = \\{(x, t) \\in \\mathbb{R}^n \\times \\mathbb{R} \\mid \\|x\\|_2 \\leq t\\}$",
            "$C = \\{x \\in \\mathbb{R}^2 \\mid e^{-x_1 - x_2} \\leq 0\\}$",
            "$C = \\{x \\in \\mathbb{R}^2 \\mid x_1 x_2 \\geq 1\\}$"
        ],
        "answer": 1,
        "explanation": "二阶锥（冰淇淋筒）是经典凸集。单位圆周是曲线（凸组合会落在圆内而非圆周上）。$e^{-s} \\leq 0$ 无实数解→空集→凸集（但此题可能考察你是否注意到这点）。$x_1 x_2 \\geq 1$ 是双曲线区域——非凸。二阶锥是标准凸集。",
        "pitfall": "注意区分凸集和凸函数的水平集。$\\|x\\|_2 \\leq t$ 等价于 $\\begin{bmatrix} tI & x \\\\ x^T & t \\end{bmatrix} \\succeq 0$，是半正定锥条件。"
    },
    {
        "type": "choice", "points": 2,
        "question": "凸函数的局部极小点必是全局极小点，这个结论成立的条件是？",
        "options": [
            "函数可微即可",
            "函数是凸函数且可行域是凸集",
            "函数二阶可微即可",
            "不需要任何条件"
        ],
        "answer": 1,
        "explanation": "需要两个条件同时成立：(1) $f$ 是凸函数；(2) $\\Omega$ 是凸集。两者缺一不可。若可行域非凸，即使是凸函数也可能有不是全局极小的局部极小点。",
        "pitfall": "容易只记得「凸函数局部极小=全局极小」而忘记还需要凸可行域。"
    },
    {
        "type": "choice", "points": 2,
        "question": "设 $f \\in C^2$，$x^*$ 是 $\\min_{x \\in \\mathbb{R}^n} f(x)$ 的局部极小点，则必有？",
        "options": [
            "$\\nabla f(x^*) = 0$ 且 $\\nabla^2 f(x^*) \\succ 0$",
            "$\\nabla f(x^*) = 0$ 且 $\\nabla^2 f(x^*) \\succeq 0$",
            "$\\nabla f(x^*) = 0$ 且 $\\nabla^2 f(x^*)$ 任意",
            "$\\nabla f(x^*)$ 任意且 $\\nabla^2 f(x^*) \\succ 0$"
        ],
        "answer": 1,
        "explanation": "无约束优化中，FONC 要求 $\\nabla f(x^*) = 0$，SONC 要求 $\\nabla^2 f(x^*) \\succeq 0$。$\\nabla^2 f \\succ 0$ 是充分条件（SOSC）而非必要条件。例如 $f(x) = x^4$ 在 $x=0$ 处 $f''(0) = 0$（半正定），但仍是极小点。",
        "pitfall": "易错选 $\\nabla^2 f \\succ 0$。正定是充分条件，半正定才是必要条件。"
    },
    {
        "type": "choice", "points": 2,
        "question": "关于 Sylvester 准则，下列哪个说法是正确的？",
        "options": [
            "顺序主子式全非负可以判定半正定",
            "顺序主子式全正可以判定正定（仅对称矩阵有效）",
            "Sylvester 准则对任意方阵都适用",
            "主子式全正可以判定正定"
        ],
        "answer": 1,
        "explanation": "Sylvester 准则：$Q \\succ 0 \\iff$ 所有顺序主子式 $>0$。该准则仅对对称矩阵有效。半正定需要所有主子式（非仅顺序主子式）非负，或特征值全非负。",
        "pitfall": "顺序主子式非负 ≠ 半正定！这是考试最高频陷阱。Sylvester 准则只对对称矩阵有效。"
    },
    {
        "type": "choice", "points": 2,
        "question": "黄金分割法中内点比例 $\\mu$ 的值约为？",
        "options": [
            "$\\mu = 0.5$",
            "$\\mu = 0.618$",
            "$\\mu = 0.382$",
            "$\\mu = 0.732$"
        ],
        "answer": 1,
        "explanation": "由自相似性要求：$\\lambda = (1-\\lambda)^2$，解得 $\\lambda = \\frac{3-\\sqrt{5}}{2} \\approx 0.382$，$\\mu = 1-\\lambda = \\frac{\\sqrt{5}-1}{2} \\approx 0.618$。$\\mu$ 是较大的内点（压缩比），$\\lambda$ 是较小的内点。",
        "pitfall": "注意区分 $\\lambda \\approx 0.382$（小内点）和 $\\mu \\approx 0.618$（压缩比/大内点）。"
    },
    {
        "type": "choice", "points": 2,
        "question": "关于 Armijo 条件，以下说法错误的是？",
        "options": [
            "Armijo 条件要求 $f(x_k + \\alpha p_k) \\leq f(x_k) + c\\alpha p_k^T\\nabla f(x_k)$",
            "Armijo 条件可以单独用于保证全局收敛",
            "Armijo 条件的典型参数为 $c = 10^{-4}$",
            "回溯法从大步长开始逐步缩小直到满足 Armijo 条件"
        ],
        "answer": 1,
        "explanation": "Armijo 条件不能单独保证全局收敛——它允许 $\\alpha \\to 0$，此时条件总是近似满足，不能阻止步长过小。必须配合回溯（从大 $\\bar{\\alpha}$ 开始）或加上 Wolfe 的曲率条件。",
        "pitfall": "这是 Armijo 条件最常见的误解——看起来合理的条件却不能单独使用。"
    },
    {
        "type": "choice", "points": 2,
        "question": "牛顿法（多元）的局部收敛阶是？",
        "options": [
            "线性收敛",
            "超线性收敛",
            "二次收敛",
            "次线性收敛"
        ],
        "answer": 2,
        "explanation": "牛顿法在标准假设下（$f \\in C^3$，$\\nabla f(x^*)=0$，$\\nabla^2 f(x^*)$ 可逆）具有至少二阶收敛率：$\\|x_{k+1} - x^*\\| \\leq c_1 c_2 \\|x_k - x^*\\|^2$。注意这是局部性质——需要初始点充分靠近解。",
        "pitfall": "牛顿法二次收敛是其最大优势，但也是局部的。远离解时可能发散。"
    },
    {
        "type": "choice", "points": 2,
        "question": "共轭梯度法中 $\\beta_k$ 的 Fletcher-Reeves (FR) 公式为？",
        "options": [
            "$\\beta_k = \\frac{g_{k+1}^T[g_{k+1} - g_k]}{g_k^T g_k}$",
            "$\\beta_k = \\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$",
            "$\\beta_k = \\frac{g_{k+1}^T[g_{k+1} - g_k]}{p_k^T[g_{k+1} - g_k]}$",
            "$\\beta_k = \\frac{g_{k+1}^T g_{k+1}}{p_k^T[g_{k+1} - g_k]}$"
        ],
        "answer": 1,
        "explanation": "FR 公式：$\\beta_k^{\\text{FR}} = \\frac{g_{k+1}^T g_{k+1}}{g_k^T g_k}$。四种等价公式中 FR 数值最稳定，推荐作为默认选择。A 是 PR 公式，C 是 HS 公式，D 是 DY 公式。",
        "pitfall": "四种 β 公式对二次函数等价，对非线性函数不等价。记住 FR = 新梯度平方/旧梯度平方。"
    },
    {
        "type": "choice", "points": 2,
        "question": "下列哪个不是 $Q$-共轭方向法的性质？",
        "options": [
            "最多 $n$ 步收敛到二次函数的极小点",
            "扩展子空间定理：$x_{k+1}$ 是 $k+1$ 维子空间上的全局最小点",
            "每一步产生的搜索方向是下降方向",
            "搜索方向之间的欧氏内积为零"
        ],
        "answer": 3,
        "explanation": "$Q$-共轭指 $p_i^T Q p_j = 0$，不是 $p_i^T p_j = 0$（欧氏正交）。只有 $Q = I$ 时两者才重合。其他三个选项都是共轭方向法的正确性质。",
        "pitfall": "共轭 ≠ 正交。$Q$-共轭是在 $Q$ 内积意义下的正交。"
    },
    {
        "type": "choice", "points": 2,
        "question": "拟牛顿方程 $H_{k+1} y_k = s_k$ 中 $y_k$ 和 $s_k$ 的定义是？",
        "options": [
            "$s_k = x_{k+1} - x_k,\\; y_k = g_{k+1} - g_k$",
            "$s_k = x_k - x_{k+1},\\; y_k = g_k - g_{k+1}$",
            "$s_k = x_k - x_{k+1},\\; y_k = g_{k+1} - g_k$",
            "$s_k = x_{k+1} - x_k,\\; y_k = g_k - g_{k+1}$"
        ],
        "answer": 1,
        "explanation": "标准记号为 $s_k = x_k - x_{k+1}$（或 $x_{k+1} - x_k$，符号约定取决于教材），$y_k = g_k - g_{k+1}$。两者方向一致——都是从旧点减新点。曲率条件 $s_k^T y_k > 0$ 保证正定性遗传。",
        "pitfall": "$s_k$ 和 $y_k$ 必须用相同方向的差分（都是从旧到新或都是从新到旧）。"
    },
    {
        "type": "choice", "points": 2,
        "question": "线性规划标准形中，若判别数 $r_D$ 全为非负且 $b$ 有负分量，应该使用？",
        "options": [
            "原始单纯形法",
            "对偶单纯形法",
            "两阶段法",
            "大M法"
        ],
        "answer": 1,
        "explanation": "$r_D \\geq 0$ 意味着对偶可行；$b$ 有负分量意味着原始不可行。这正是对偶单纯形法的适用场景。对偶单纯形法先选出基行（最负 $b_k$），后选进基列。",
        "pitfall": "原始单纯形法要求 $b \\geq 0$；两阶段/大M法用于无自然基且 $r_D$ 不全非负的情形。"
    },
    {
        "type": "choice", "points": 2,
        "question": "弱对偶定理保证 $c^T x \\geq \\lambda^T b$。若 $c^T x = \\lambda^T b$，可以推出？",
        "options": [
            "原始问题的最优解一定是对偶问题的最优解",
            "$x$ 和 $\\lambda$ 分别是各自问题的最优解",
            "强对偶定理一定成立",
            "原始问题一定可行"
        ],
        "answer": 1,
        "explanation": "弱对偶定理推论：若 $c^T x = \\lambda^T b$（原始目标值 = 对偶目标值），则 $x$ 和 $\\lambda$ 分别是各自问题的最优解。这是利用对偶验证最优性的标准方法。",
        "pitfall": "弱对偶永远成立，强对偶需要凸性+Slater。$c^T x = \\lambda^T b$ 提供了验证最优性的充分条件。"
    },
    {
        "type": "choice", "points": 2,
        "question": "KKT 条件中，关于乘子符号的正确描述是？",
        "options": [
            "$\\lambda$（等式乘子）和 $\\mu$（不等式乘子）都必须非负",
            "$\\lambda$ 无符号限制，$\\mu$ 必须非负",
            "$\\lambda$ 必须非负，$\\mu$ 无符号限制",
            "$\\lambda$ 和 $\\mu$ 都无符号限制"
        ],
        "answer": 1,
        "explanation": "等式约束乘子 $\\lambda_i$ 无符号限制（可正可负可零），因为 Farkas 引理中等式被拆为两个不等式，出现 $\\alpha_i^+ - \\alpha_i^-$。不等式乘子 $\\mu_j$ 来自 Farkas 引理的非负乘子，必须 $\\geq 0$。",
        "pitfall": "符号记反了！很多同学会认为 $\\lambda$ 也要非负——实际上等式约束不限制乘子符号。"
    },
    {
        "type": "choice", "points": 2,
        "question": "互补松弛条件 $\\mu_j g_j(x^*) = 0$ 的含义是？",
        "options": [
            "所有约束必须在最优解处取等号",
            "若约束是松的（$g_j < 0$），则对应的乘子为零",
            "若乘子为正，则对应的约束必须是松的",
            "乘子和约束值必须同时为零"
        ],
        "answer": 1,
        "explanation": "互补松弛：$\\mu_j > 0 \\Rightarrow g_j = 0$（约束紧）；$g_j < 0 \\Rightarrow \\mu_j = 0$（乘子为零）。经济学解释：松约束的影子价格为零，只有紧约束才有正的边际价值。",
        "pitfall": "不是双向的——$\\mu_j = 0$ 时 $g_j$ 可以 $=0$ 或 $<0$；$g_j = 0$ 时 $\\mu_j$ 可以 $=0$ 或 $>0$。"
    },
    {
        "type": "choice", "points": 2,
        "question": "关于 FONC，以下说法正确的是？",
        "options": [
            "FONC 是极小点的充分条件",
            "FONC 在无约束优化中等价于 $\\nabla f(x^*) = 0$",
            "FONC 只适用于凸优化问题",
            "FONC 的证明需要 $f \\in C^2$"
        ],
        "answer": 1,
        "explanation": "FONC 是必要条件（满足不一定是极小点）。无约束时 $\\mathcal{T} = \\mathbb{R}^n$，FONC 等价于 $\\nabla f(x^*) = 0$。FONC 适用于任意 $f \\in C^1$ 的优化问题（不限于凸优化）。",
        "pitfall": "FONC 是必要条件，SOSC 是充分条件。不要混淆两者的逻辑方向。"
    },
    {
        "type": "choice", "points": 2,
        "question": "信赖域方法对比线搜索方法的核心优势是？",
        "options": [
            "计算量更小",
            "不需要梯度信息",
            "Hessian 非正定时也能保证收敛",
            "步长选取更简单"
        ],
        "answer": 2,
        "explanation": "信赖域子问题是有界约束下的优化，$B + \\lambda I$ 在约束下自动正定。Hessian 非正定时，线搜索方法可能产生上升方向，而信赖域方法通过半径约束自动处理。",
        "pitfall": "信赖域收敛不要求 Hessian 正定——这是对比纯牛顿法的最重要优势。"
    },
    {
        "type": "choice", "points": 2,
        "question": "Zoutendijk 定理保证了什么？",
        "options": [
            "牛顿法一定收敛",
            "若搜索方向不趋于与负梯度正交，则梯度趋于零",
            "任何优化算法都收敛到全局极小点",
            "线搜索步长一定是最优的"
        ],
        "answer": 1,
        "explanation": "Zoutendijk 定理：$\\sum \\cos^2\\theta_k \\|\\nabla f(x_k)\\|^2 < \\infty$。推论：若 $\\cos\\theta_k \\geq \\delta > 0$（方向始终不趋于与负梯度正交），则 $\\|\\nabla f(x_k)\\| \\to 0$。这是线搜索方法的收敛性基石。",
        "pitfall": "定理前提：$f$ 连续可微有下界 + $\\nabla f$ Lipschitz 连续 + 下降方向 + Wolfe 步长。"
    },
    {
        "type": "choice", "points": 2,
        "question": "BFGS 公式与 DFP 公式的对偶关系是？",
        "options": [
            "将 DFP 中的 $s$ 和 $y$ 互换即得 BFGS",
            "将 DFP 中的 $H$ 和 $B$ 互换（$s \\leftrightarrow y$）即得 BFGS",
            "DFP 和 BFGS 是完全相同的公式",
            "DFP 是 BFGS 的秩1特例"
        ],
        "answer": 1,
        "explanation": "在 DFP 公式中做替换 $H \\leftrightarrow B$、$s \\leftrightarrow y$，DFP 变为 BFGS。DFP 近似 Hessian 逆（版本1），BFGS 近似 Hessian（版本2），两者通过「$H \\leftrightarrow B$，$s \\leftrightarrow y$」对称互补。",
        "pitfall": "是 $H \\leftrightarrow B$ 且 $s \\leftrightarrow y$，不是只交换 $s$ 和 $y$。"
    },

    # --- 判断题 (10题，每题1分 = 10分) ---
    {"type": "tf", "points": 1, "question": "若 $A$ 是对称矩阵，其所有特征值都是实数。", "answer": 0, "options": [],
     "explanation": "实对称矩阵的特征值一定全是实数。这是对称矩阵的三条黄金性质之一。",
     "pitfall": "注意前提：$A$ 必须是实对称矩阵。非对称实矩阵可能有复特征值。"},
    {"type": "tf", "points": 1, "question": "在 $\\mathbb{R}^n$ 中，所有范数等价。", "answer": 0, "options": [],
     "explanation": "在有限维空间中所有范数等价。这是收敛性分析选最方便范数的理论基础。无穷维空间不成立。",
     "pitfall": "仅在有限维空间成立。"},
    {"type": "tf", "points": 1, "question": "最速下降法的相邻搜索方向总是正交的。", "answer": 0, "options": [],
     "explanation": "最速下降法（精确线搜索）的相邻梯度正交：$\\nabla f(x_{k+1}) \\perp \\nabla f(x_k)$。搜索方向就是负梯度，所以相邻搜索方向正交——锯齿现象的数学根源。",
     "pitfall": "注意是「最速下降法」而非任意「梯度下降法」。固定步长的梯度法不保证正交。"},
    {"type": "tf", "points": 1, "question": "牛顿法对于任何初始点都能保证二次收敛。", "answer": 1, "options": [],
     "explanation": "牛顿法的二次收敛是局部性质——要求初始点充分靠近解。远离解时牛顿法可能不收敛甚至发散。",
     "pitfall": "牛顿法「快但脆弱」——二次收敛只在局部成立。"},
    {"type": "tf", "points": 1, "question": "共轭梯度法对任意非线性函数都能在 $n$ 步内收敛。", "answer": 1, "options": [],
     "explanation": "共轭方向法的 $n$ 步收敛仅对二次函数 $f(x) = \\frac{1}{2}x^T Q x + b^T x$ 且使用精确线搜索时成立。对一般非线性函数不保证。",
     "pitfall": "非线性 CG 需要 restart，共轭性和正交性不再精确成立。"},
    {"type": "tf", "points": 1, "question": "拟牛顿法的曲率条件 $s_k^T y_k > 0$ 在使用强 Wolfe 线搜索时自动满足。", "answer": 0, "options": [],
     "explanation": "强 Wolfe 条件包含曲率条件，可以证明 $s_k^T y_k > 0$ 自动成立。这保证了拟牛顿矩阵的正定性遗传。",
     "pitfall": "必须使用强 Wolfe 线搜索；Armijo 或 Goldstein 不能保证此条件。"},
    {"type": "tf", "points": 1, "question": "线性规划中对偶单纯形法的 pivot 元素必须取负值。", "answer": 0, "options": [],
     "explanation": "对偶单纯形法要求 $a_{kr} < 0$（pivot 为负），因为只有在负元素上比值 $r_j/(-a_{kj})$ 才有意义。若出基行所有元素 $\\geq 0$，则原问题不可行。",
     "pitfall": "与原始单纯形法相反——后者要求 $a_{il} > 0$。"},
    {"type": "tf", "points": 1, "question": "KKT 条件是约束优化极小点的充分必要条件。", "answer": 1, "options": [],
     "explanation": "一般非凸问题中 KKT 是必要条件（需要正则性条件）。仅在凸优化中 KKT 升格为充分条件。",
     "pitfall": "KKT 的角色取决于问题的凸性——非凸时必要，凸时充要。"},
    {"type": "tf", "points": 1, "question": "Pareto 最优解意味着所有目标函数都达到了各自的最小值。", "answer": 1, "options": [],
     "explanation": "Pareto 最优只意味不存在同时改进所有目标的可行解。通常情况下 Pareto 解在某个目标表现好时其他目标表现差——不存在「全能最优」。",
     "pitfall": "Pareto 最优 ≠ 所有目标都最优。它是偏序下的非支配解。"},
    {"type": "tf", "points": 1, "question": "Sylvester 准则（顺序主子式全正）可以用来判定任何矩阵的正定性。", "answer": 1, "options": [],
     "explanation": "Sylvester 准则仅对对称矩阵有效。非对称矩阵的正定性不能简单地用顺序主子式判定。",
     "pitfall": "Sylvester 准则的前提：矩阵必须对称！"},

    # --- 填空题 (10题，每题2分 = 20分) ---
    {"type": "fill", "points": 2, "question": "Rank-Nullity 定理：$\\dim \\mathcal{R}(A) + \\dim \\_\\_\\_\\_ = n$。", "options": [],
     "answer": "\\mathcal{N}(A)", "explanation": "Rank-Nullity 定理：值域维数 + 零空间维数 = 列数。$\\operatorname{rank}(A) + \\operatorname{nullity}(A) = n$。",
     "pitfall": "零空间的维数是 $n - \\operatorname{rank}(A)$，不是 $m - \\operatorname{rank}(A)$。"},
    {"type": "fill", "points": 2, "question": "投影算子 $P$ 是正交投影算子的充要条件是 $P = P^T = \\_\\_\\_\\_$。", "options": [],
     "answer": "P^2", "explanation": "正交投影算子的判定定理：$P = P^T = P^2$（对称且幂等）。仅幂等是斜投影，还需对称才算正交投影。",
     "pitfall": "两个条件缺一不可。"},
    {"type": "fill", "points": 2, "question": "$f \\in C^1$ 是凸函数的充要条件（一阶条件）是：$f(y) \\geq f(x) + \\_\\_\\_\\_ \\cdot (y-x)$。", "options": [],
     "answer": "\\nabla f(x)^T", "explanation": "凸函数的一阶特征：$f(y) \\geq f(x) + \\nabla f(x)^T (y-x)$。图始终在切平面之上。这也称为梯度不等式。",
     "pitfall": "注意转置符号——$\\nabla f$ 是列向量，内积时需要转置。"},
    {"type": "fill", "points": 2, "question": "定步长梯度法 $x_{k+1} = x_k - \\alpha \\nabla f(x_k)$ 对二次函数 $f(x) = \\frac{1}{2}x^T Q x$ 收敛的充要条件是 $\\alpha \\in \\_\\_\\_\\_$。", "options": [],
     "answer": "(0, \\frac{2}{\\lambda_{\\max}(Q)})", "explanation": "$\\alpha$ 必须在 $(0, 2/\\lambda_{\\max})$ 内。在此范围外即使对最简单的二次函数也可能发散。这是充要条件。",
     "pitfall": "注意分母是 $\\lambda_{\\max}(Q)$ 而不是 $\\lambda_{\\min}(Q)$。"},
    {"type": "fill", "points": 2, "question": "牛顿法（多元）的迭代格式为 $x_{k+1} = x_k - \\_\\_\\_\\_ \\nabla f(x_k)$。", "options": [],
     "answer": "[\\nabla^2 f(x_k)]^{-1}", "explanation": "牛顿方向 $d_k = -H_k^{-1} g_k$，其中 $H_k = \\nabla^2 f(x_k)$。用二阶 Taylor 展开的二次模型直接跳到极小点。",
     "pitfall": "实际实现中不显式求逆——解方程组 $H_k d_k = -g_k$。"},
    {"type": "fill", "points": 2, "question": "共轭梯度法的方向递推公式：$p_k = -g_k + \\_\\_\\_\\_ p_{k-1}$，其中 $p_0 = -g_0$。", "options": [],
     "answer": "\\beta_{k-1}", "explanation": "CG 在线生成共轭方向：$p_k = -g_k + \\beta_{k-1} p_{k-1}$。$\\beta_k$ 有多种等价公式（FR/PR/HS/DY），FR 数值最稳定。",
     "pitfall": "初始方向 $p_0 = -g_0$，之后每步加上前一步方向乘以 $\\beta$。"},
    {"type": "fill", "points": 2, "question": "单纯形法中，对于 $\\min$ 问题，当前 BFS 是最优解的条件是所有判别数 $r_j \\_\\_\\_\\_ 0$。", "options": [],
     "answer": "\\geq", "explanation": "$\\min$ 问题：$r_D \\geq 0$（所有判别数非负）则当前 BFS 最优。$\\max$ 问题则相反（$r_D \\leq 0$）。",
     "pitfall": "$\\min$ 和 $\\max$ 的判别数符号方向相反。"},
    {"type": "fill", "points": 2, "question": "Lagrange 函数的鞍点 $(x^*, \\lambda^*, \\mu^*)$ 满足 $L(x^*, \\lambda, \\mu) \\leq L(x^*, \\lambda^*, \\mu^*) \\leq \\_\\_\\_\\_$。", "options": [],
     "answer": "L(x, \\lambda^*, \\mu^*)", "explanation": "鞍点定义：在 $x$ 方向极小、在 $\\lambda, \\mu$ 方向极大的点。左不等式：对乘子是极大；右不等式：对 $x$ 是极小。",
     "pitfall": "鞍点 = $x$ 方向的极小点 + 乘子方向的极大点。"},
    {"type": "fill", "points": 2, "question": "互补松弛条件的完整写法是 $\\_\\_\\_\\_ \\cdot g_j(x^*) = 0,\\; j = 1, \\ldots, p$。", "options": [],
     "answer": "\\mu_j^*", "explanation": "互补松弛：$\\mu_j^* g_j(x^*) = 0$。乘子与对应约束值的乘积为零。$\\mu_j > 0 \\Rightarrow g_j = 0$（约束紧）；$g_j < 0 \\Rightarrow \\mu_j = 0$（乘子为零）。",
     "pitfall": "互补松弛不是 $\\mu_j^* + g_j(x^*) = 0$，是乘积为零。"},
    {"type": "fill", "points": 2, "question": "Sherman-Morrison 公式：$(A + uv^T)^{-1} = A^{-1} - \\frac{A^{-1}uv^T A^{-1}}{1 + \\_\\_\\_\\_}$。", "options": [],
     "answer": "v^T A^{-1} u", "explanation": "秩1逆公式：分母为 $1 + v^T A^{-1} u$。这是将 BFGS 的 $B_{k+1}$ 更新转化为 $H_{k+1}$ 更新的关键工具。",
     "pitfall": "分母是 $1 + v^T A^{-1} u$ 而不是 $1 + u^T A^{-1} v$。"},

    # --- 计算题 (3题，共20分) ---
    {"type": "calc", "points": 8,
     "question": "用最速下降法求解 $\\min f(x) = \\frac{1}{2}(x_1^2 + 10x_2^2)$，初始点 $x_0 = [10, 1]^T$。完成一步迭代，给出 $x_1$ 并计算 $f(x_1)$。",
     "answer": -1, "options": [],
     "explanation": "<strong>解</strong>：(1) $\\nabla f(x) = [x_1, 10x_2]^T$，$g_0 = [10, 10]^T$。<br>(2) 二次函数 $Q = \\operatorname{diag}(1, 10)$，精确步长 $\\alpha_0 = \\frac{g_0^T g_0}{g_0^T Q g_0} = \\frac{200}{10^2 + 10 \\times 10^2} = \\frac{200}{1100} = \\frac{2}{11}$。<br>(3) $x_1 = x_0 - \\alpha_0 g_0 = [10 - \\frac{2}{11} \\times 10,\\; 1 - \\frac{2}{11} \\times 10]^T = [\\frac{90}{11},\\; -\\frac{9}{11}]^T \\approx [8.18, -0.82]^T$。<br>(4) $f(x_1) = \\frac{1}{2}(8.18^2 + 10 \\times (-0.82)^2) \\approx 36.8$。<br><br><strong>评分要点</strong>：梯度计算 1 分，精确步长 3 分，迭代公式 2 分，目标值 2 分。"},
    {"type": "calc", "points": 6,
     "question": "用黄金分割法搜索函数 $f(x) = (x-3)^2$ 在 $[0, 10]$ 上的极小点。给出第一轮的两个内点位置，并判断删除哪一端。",
     "answer": -1, "options": [],
     "explanation": "<strong>解</strong>：(1) $a_0 = 0, b_0 = 10, L_0 = 10$。<br>(2) $\\lambda = 0.382, \\mu = 0.618$。<br>(3) 内点：$c_1 = a_0 + \\lambda L_0 = 0 + 0.382 \\times 10 = 3.82$；$d_1 = a_0 + \\mu L_0 = 0 + 0.618 \\times 10 = 6.18$。<br>(4) $f(c_1) = (3.82-3)^2 = 0.67$；$f(d_1) = (6.18-3)^2 = 10.11$。<br>(5) $f(c_1) < f(d_1)$，极小点在 $d_1$ 的左侧 → 删除右端，新区间 $[0, 6.18]$。<br><br><strong>评分要点</strong>：$\\lambda$/$\\mu$ 计算 1 分，内点 2 分，函数值比较 2 分，删除决策 1 分。"},
    {"type": "calc", "points": 6,
     "question": "给定线性规划 $\\min\\; x_1 + x_2$，s.t. $x_1 + x_2 \\geq 1$，$x_1, x_2 \\geq 0$。写出其对偶问题并求解。",
     "answer": -1, "options": [],
     "explanation": "<strong>解</strong>：(1) 标准化：$\\min\\; x_1 + x_2$，s.t. $-x_1 - x_2 \\leq -1$，$x_1, x_2 \\geq 0$。<br>(2) 对偶：$\\max\\; -\\lambda$，s.t. $-\\lambda \\leq 1$（$x_1$ 对应），$-\\lambda \\leq 1$（$x_2$ 对应），$\\lambda \\geq 0$。<br>(3) 约束为 $-\\lambda \\leq 1$ 即 $\\lambda \\geq -1$。结合 $\\lambda \\geq 0$ 得 $\\lambda \\geq 0$。最大化 $-\\lambda$ 得 $\\lambda^* = 0$，最优值 $= 0$。<br>(4) 但原始问题最小值 $= 1$（取 $x_1 = 1, x_2 = 0$）。注意：这里弱对偶成立 $1 > 0$，因为有对偶间隙——本题中不等式约束不是 $\\geq$ 就是 $\\leq$，需要仔细处理对偶转化。<br>正确对偶：原问题 $\\min\\{x_1+x_2 \\mid x_1+x_2 \\geq 1, x \\geq 0\\}$ 对偶为 $\\max\\; \\lambda$，s.t. $\\lambda \\leq 1, \\lambda \\leq 1, \\lambda \\geq 0$ → $\\lambda^* = 1$，最优值 $= 1$。强对偶成立。<br><br><strong>评分要点</strong>：标准化 1 分，对偶转化表应用 2 分，对偶问题书写 2 分，求解 1 分。"},

    # --- 简答题 (2题，共10分) ---
    {"type": "short", "points": 5,
     "question": "简述信赖域方法与线搜索方法的本质区别，以及信赖域方法在 Hessian 非正定时的优势。",
     "answer": -1, "options": [],
     "explanation": "<strong>参考答案</strong>：<br>(1) 决策顺序不同：线搜索先选方向再选步长；信赖域先确定信任半径再在范围内求最佳点。<br>(2) Hessian 非正定时：线搜索的牛顿方向可能是上升方向；信赖域子问题是有界约束下的优化，KKT 条件中 Lagrange 乘子 λ 使 $B+\\lambda I$ 自动正定——约束的存在等价于给 Hessian 加了正则项。<br>(3) 收敛性：信赖域方法不要求 Hessian 正定也能保证全局收敛。",
     "pitfall": "不要仅说「一个先选方向一个先选范围」——关键是 Hessian 非正定时信赖域的自动正则化机制。"},
    {"type": "short", "points": 5,
     "question": "解释为什么 BFGS 在实践中普遍优于 DFP，以及曲率条件 $s_k^T y_k > 0$ 为什么重要。",
     "answer": -1, "options": [],
     "explanation": "<strong>参考答案</strong>：<br>(1) BFGS 近似 Hessian（$B_k$），DFP 近似 Hessian 逆（$H_k$）。在大规模问题中 $H_k$ 可能渐近奇异导致停滞。<br>(2) BFGS 的数值表现更稳健——对 Rosenbrock 函数只需 34 步（vs 最速下降法 5264 步）。<br>(3) $s_k^T y_k > 0$（曲率条件）保证 $H_{k+1} \\succ 0$ 和 $B_{k+1} \\succ 0$（正定性遗传）。若不满足，拟牛顿矩阵可能不正定，搜索方向不再是下降方向。<br>(4) 强 Wolfe 线搜索自动保证此条件成立。",
     "pitfall": "BFGS 和 DFP 是对偶关系，但 BFGS 的数值稳健性来自近似 Hessian（而非其逆）的策略。"},

    # --- 综合题 (1题，共10分) ---
    {"type": "comprehensive", "points": 10,
     "question": "考虑约束优化问题：$\\min\\; f(x) = x_1^2 + x_2^2$，s.t. $x_1 + x_2 = 2$。<br>(1) 写出 Lagrange 函数和 KKT 条件。<br>(2) 求解最优解 $x^*$ 和 Lagrange 乘子 $\\lambda^*$。<br>(3) 验证二阶充分条件是否满足。<br>(4) 若将等式约束改为 $x_1 + x_2 \\leq 2$，最优解是否变化？为什么？",
     "answer": -1, "options": [],
     "explanation": "<strong>解</strong>：<br>(1) $L(x, \\lambda) = x_1^2 + x_2^2 + \\lambda(x_1 + x_2 - 2)$。<br>KKT：$\\nabla_x L = [2x_1 + \\lambda,\\; 2x_2 + \\lambda]^T = 0$，$x_1 + x_2 = 2$。<br>(2) 由驻点条件：$x_1 = x_2 = -\\lambda/2$。代入约束：$-\\lambda/2 + (-\\lambda/2) = 2 \\Rightarrow -\\lambda = 2 \\Rightarrow \\lambda^* = -2$。$x_1^* = x_2^* = 1$。<br>(3) $\\nabla_{xx}^2 L = \\begin{bmatrix} 2 & 0 \\\\ 0 & 2 \\end{bmatrix} \\succ 0$。切空间由 $\\nabla h^T d = d_1 + d_2 = 0$ 定义，即 $d_2 = -d_1$。$d^T L d = 2d_1^2 + 2d_2^2 = 4d_1^2 > 0, \\forall d \\neq 0$。SOSC 满足，$x^*$ 是严格局部极小点。<br>(4) 不等式约束下，无约束极小点 $x = (0, 0)$ 满足 $x_1 + x_2 = 0 < 2$（约束非积极）。KKT：若 $\\mu = 0$ 则 $\\nabla f = 0 \\Rightarrow x = (0, 0)$。此时 $f = 0 < 2$（等式约束的最优值）。所以最优解变为 $x^* = (0, 0)$，乘子 $\\mu^* = 0$。<br><br><strong>评分要点</strong>：(1) 2分；(2) 3分；(3) 3分；(4) 2分。",
     "pitfall": "第(4)问的关键是判断约束是否积极——无约束极小点是否满足约束。若满足则约束不起作用。"},
]

# ============================================================
# Generate HTML Files
# ============================================================
title = "最优化方法 — 复习知识清单"
test_title = "最优化方法 — 章节自测（满分 100 分）"
test_subtitle = "覆盖预备知识、凸集与凸函数、线搜索、无约束优化、线性规划、整数规划、约束优化、多目标规划、核心证明"

save_knowledge_html(knowledge_body,
    os.path.join(out_dir, "最优化方法-复习知识清单.html"),
    title)

save_test(questions,
    os.path.join(out_dir, "最优化方法-章节自测.html"),
    test_title, test_subtitle, duration_minutes=90)

print("Done!")
print("知识清单:", os.path.join(out_dir, "最优化方法-复习知识清单.html"))
print("章节自测:", os.path.join(out_dir, "最优化方法-章节自测.html"))
