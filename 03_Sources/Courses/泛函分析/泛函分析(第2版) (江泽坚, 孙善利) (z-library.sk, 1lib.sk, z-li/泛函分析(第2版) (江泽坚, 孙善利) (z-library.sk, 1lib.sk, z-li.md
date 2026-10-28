---
raw_title: 泛函分析(第2版) (江泽坚, 孙善利) (z-library.sk, 1lib.sk, z-li
subject: 泛函分析(第2版) (江泽坚, 孙善利) (z-library.sk, 1lib.sk, z-li
source: 泛函分析(第2版) (江泽坚, 孙善利) (z-library.sk, 1lib.sk, z-li.pdf
status: mineru解析
parser: mineru
---

## 泛函分析第2版江泽坚孙善利

## 内容提要本书是作者根据高等学校数学与力学教学指导委员会审定的“泛函分析教材编写大纲”为数学类本科各专业学生编写的泛函分析教材。第一版于1994年出版以来受到许多高校师生的欢迎。这次新版主要针对高等教育改革对各门课程提出新的要求，适应泛函分析课时压缩新情况，对第1版内容进行适当调整。将 $F-$ 空间，序列弱收敛，序列弱\*收敛，弱拓扑，广义函数等加上\*号，供有能力者选学。原来定理及其证明做了相应改写，保证删去加\*号内容后，教材体系不受影响。同时鉴于商空间及对偶理论的重要性，在第三章§6增加了关于商空间及其对偶的内容。新版教材仍然内容适中，深浅适宜，简明扼要，论述清晰，保持了第1版的特色。

本书适合作为高等学校数学系“泛函分析”课程的教材。

## 图书在版编目(CIP)数据泛函分析/江泽坚,孙善利.—2版.—北京:高等教育出版社,2005.5

ISBN 7-04-016619-4

I. 泛… II. ①江… ②孙… III. 泛函分析 - 高等学校 - 教材 IV. 0177

中国版本图书馆 CIP 数据核字(2005)第 026867 号策划编辑李蕊责任编辑崔梅萍封面设计王凌波责任绘图郝林版式设计王莹责任校对殷然责任印制朱学忠出版发行高等教育出版社社址北京市西城区德外大街 4 号购书热线 010-58581118

免费咨询 800-810-0598

邮政编码 100011

网址 http://www.hep.edu.cn

总机 010-58581000

http://www.hep.com.cn

网上订购 \*http://www.landraco.com

经销北京蓝色畅想图书发行有限公司

http://www.landraco.com.cn

印刷北京鑫海金澳胶印有限公司版次 1994 年 5 月第 1 版开本 $787 \times 960$ 1/16

印张 15.5

字数 290 000

印次 2005 年 5 月第 1 次印刷定价 19.70 元本书如有缺页、倒页、脱页等质量问题，请到所购图书销售部门联系调换。

版权所有侵权必究物料号 16619-00

## 第 2 版前言本书第1版于1994年出版以后一直在吉林大学使用，也在四川大学，辽宁大学，东北师范大学，北京航空航天大学等高等学校使用过，受到这些高校师生的欢迎。使用本书的同人向我们提出过一些宝贵意见。对此我们表示衷心的感谢，也感谢出版社给我们修订本书和表达谢意的机会。

这次新版保持原书的基本内容和特色,同时吸收好的意见,对个别地方作了修改.为适应泛函分析课时压缩的新情况,也对第1版部分内容进行适当修订.

1. 将 $F-$ 空间, 序列弱收敛, 序列弱\*收敛, 弱拓扑, 广义函数等内容加上\*号, 供有能力者选学. 原来涉及这部分内容的定理及其证明做了相应改写, 以保证删去加\*号内容后, 教材体系不受影响.

2. 鉴于商空间及对偶理论的重要性,在第三章 §6 增加了关于商空间及其对偶的内容.

3. 借再版机会补充上第1版曾遗漏的参考文献.

尽管做了努力，仍恐有许多不足，还望海内同人指正。

编者

2004年12月

# 序本书是为数学系本科学生写的教材，其内容大体如高等学校数学、力学教材编审委员会函数论泛函分析编审组于1990年11月在南京大学召开的会议上制订的《泛函分析教材编写大纲》。

我们认为所讲的主要内容应该是本科数学类各专业所共同必需的，不应该因为个别专业或少数方向的需要而使大多数学生增加负担。我们删去了自伴算子谱分解定理的证明，只介绍谱射影算子族，谱分解定理的结论，以及与之有关的自伴算子函数演算。而对于一般紧算子的 Riesz-Schauder 理论以及紧自伴算子的谱分解定理则予以详细的证明。

鉴于在学习本课程时,学生在偏微分方程、概率论以及计算方法等方面的知识都还完全不知道或者不很熟悉,所以我们常常偏向以线性代数、数学分析,也偶尔以初等Fourier分析、逼近论、积分方程(虽然学生也很少知道,但它比较好懂)等为背景来引出泛函分析的一些基本概念和定理。例如,关于共轭算子理论,算子的值域与零空间的关系,紧算子理论的讲解。正因为学生们知道 $L^{1}$ 与 $L^{2}$ 之Fourier变换的初等理论,也可能听说过它在一般 $L^{p}$ 空间上推广的困难,所以我们介绍广义函数论时就偏重于急减函数空间 $\mathcal{S}(\mathbf{R}^{n})$ 上的广义函数,希望用广义Fourier变换来说明广义函数的意义和重要性,但是回避了过于艰深的卷积理论。我们尽量以学生最熟悉的知识为背景来讲抽象的概念和结果。我们同意前人的提法,认为线性泛函与在无穷维空间上引进坐标的思想有关,而对偶理论则有如无穷维线性空间上的解析几何学。这符合历史发展,当年H.Hahn正是对扩张定理作了这方面的应用以后才提出当今所谓对偶空间的概念。此外,这样讲也或者可能使初学者更直观地理解对偶理论的意义和应用。有鉴于弱拓扑的特殊重要性,我们稍稍走出初等范围,先举例说明序列弱收敛不足以描述一般的弱拓扑,然后一般地介绍局部凸的线性拓扑空间。

以上所说种种思虑目下还多属于主观愿望,是否真有助于初学者,仍有待于实践的证明,还望海内同人不吝赐教。

最后,我们感谢参加评审的南京大学、复旦大学、华东师范大学、云南大学、湘潭大学的同志,他们对本书提出许多宝贵意见,特别是郑维行教授仔细阅读手稿,指出了一些错误与不当之处。我们谨在此表示衷心的感谢。

编者

1992年12月于长春

## 目录第一章距离线性空间 …… 1
§ 1 选择公理,良序定理,Zorn 引理 …… 1
§ 2 线性空间,Hamel 基 …… 2
§ 3 距离空间,距离线性空间 …… 6
§ 4 距离空间中的拓扑,可分空间 …… 12
§ 5 完备的距离空间 …… 14
§ 6 列紧性 …… 19
§ 7 赋范线性空间 …… 25
§ 8\* F-空间 …… 32
§ 9 压缩映象原理,Fréchet 导数 …… 38
习题 …… 43

第二章 Hilbert 空间 …… 47
§ 1 内积空间 …… 47
§ 2 正规正交基 …… 53
§ 3 射影定理,Fréchet-Riesz 表现定理 …… 58
§ 4 Hilbert 共轭算子,Lax-Milgram 定理 …… 63
习题 …… 70

第三章 Banach 空间上的有界线性算子 …… 73
§ 1 有界线性算子 …… 73
§ 2 Hahn-Banach 定理 …… 79
§ 3 Baire 纲推理 …… 93
§ 4 对偶空间,二次对偶,自反空间 …… 104
§ 5 Banach 共轭算子 …… 117
§ 6 算子的值域与零空间,商空间 …… 123
§ 7\* 序列弱收敛与序列弱\*收敛 …… 131
§ 8\* 弱拓扑 …… 139
习题 …… 142

第四章有界线性算子谱论 …… 145
§ 1 有界线性算子的谱 …… 145
§ 2 射影算子与约化 …… 154
§ 3 紧算子 …… 160
§ 4 有界自伴算子 …… 178

§ 5 有界自伴算子的谱测度与函数演算 …… 186
§ 6 酉算子 …… 198
习题 …… 203
第五章\* 广义函数论大意 …… 207
引言 …… 207
§ 1 基本函数空间 ℰ上的广义函数及其导数 …… 208
§ 2 基本函数空间 ℰ上的广义函数及其 Fourier 变换 …… 212
习题 …… 221
附录拓扑空间 …… 222
参考文献 …… 226
索引 …… 228
记号表 …… 236

## 第一章距离线性空间

## § 1 选择公理,良序定理,Zorn 引理我们熟知数学归纳法, 它是关于可数多个命题, 或者说关于与正整数 $n$ 有关的定理 $P(n)$ 的证明方法. 但如我们要讨论的是不可数个命题, 那怎么办呢? 设想我们要证明一个定理 $P(\alpha)$ 对一切 $\alpha \in \mathcal{A}$ 皆成立, 这里 $\mathcal{A}$ 未必是可数集, 我们就需要一个比数学归纳法更一般的方法.

假定集合 $\mathcal{A}$ 中任意两个元素 $a, b$ 之间总有先后次序，并且

(1) 若 $a$ 在 $b$ 之先, 则 $b$ 便不在 $a$ 之先.

(2) 若 $a$ 在 $b$ 之先, $b$ 又在 $c$ 之先, 则 $a$ 在 $c$ 之先. 这样的集合 $\mathcal{A}$ 叫做有序集. 以下把 $a$ 在 $b$ 之先记作 $a < b$ .

更重要的是我们还时常要求 $\mathcal{A}$ 是良序的，即

$\mathcal{A}$ 的任何非空子集 $\mathcal{S}$ 都必有一个属于 $\mathcal{S}$ 的最先的元素.

取 $\mathcal{S} = \mathcal{A}$ , 则良序集 $\mathcal{A}$ 便总有最先的元素, 这个元素记作 $\alpha_0$ .

定理1.1 对良序集 $\mathcal{A}$ , 如果

(1) $P(\alpha_0)$ 为真, 这里 $\alpha_0$ 是 $\mathcal{A}$ 中最先的元素.

(2) 若 $P(\alpha)$ 对一切 $\alpha, \alpha_0 < \alpha < \beta$ ，为真，则 $P(\beta)$ 亦真。那么 $P(\alpha)$ 对一切 $\alpha \in \mathcal{A}$ 皆真。

证若定理不真, 则集合 $\mathcal{S} = \{\alpha \in \mathcal{A}: P(\alpha)$ 不真 | 非空. 从 $\mathcal{A}$ 是良序的知 $\mathcal{S}$ 有最先的元素 $\alpha_{*}$ .

由(1)有 $\alpha_0 < \alpha_*$ . 显然当 $\alpha_0 < \alpha < \alpha_*$ 时, $P(\alpha)$ 为真. 由(2)便知 $P(\alpha_*)$ 亦真, 这与 $\alpha_* \in \mathcal{S}$ 矛盾. 证毕.

人们把这个定理叫做超限归纳法.

但是,是否每个集合都能赋予一个先后次序并且使之成为良序集呢?答案是肯定的,这叫做良序定理.它可以用所谓 Zermelo 的选择公理来证明.(参见 [13]第 14 章, §7, 定理 2)

选择公理设 $\mathcal{N} = \{N\}$ 是一个非空集合构成的族, 则必存在定义在 $\mathcal{N}$ 上的函数 $f$ , 使得对一切 $N \in \mathcal{N}$ 都有 $f(N) \in N$ .

B. Russell 说得很有意思, 对于无穷多双鞋子, 选择公理显然是对的. 例如, 我们可以说都选取右脚的鞋子. 但是对于无穷多双袜子呢? 那就很不显然了.

选择公理远不如欧氏几何学上的公理那样直观. 它多年来在数学界引起极大的争论, 迫使每个搞数学的人必须对它表态. 由于选择公理与世所公认的公理系统 $ZF$ 既是相容的, 又是独立的; 更由于没有选择公理, 现今泛函分析的基石, 如 Hahn-Banach 定理, Banach-Alaoglu 定理等的证明就将失去了依据 (参见 [21]), 所以我们承认选择公理和与之等价的良序定理以及下文的 Zorn 引理. 今后在需要的时候, 将按照我们的方便而随意引用其中一个.

定义 1.1 对一族元素 X, 如果在某些对元素 $(a, b)$ 上有二元关系, 记作 a < b. 它具有性质:

$$
a \prec a;
$$

若 $a < b$ 且 $b < a$ ，则 $a = b$ ；

若 $a < b$ 且 $b < c$ ，则 $a < c$

则称 $\mathcal{X}$ 按照关系 $<$ 为部分有序的.

例 1 设 X 是某个非空集合 E 之一切子集的集合. 定义 A < B, 若 A, B ∈ X 且 A ⊂ B. 那么 X 按 < 为部分有序集.

应该指出,这是最直观,但也是最典型、最常见的部分有序集.

定义1.2 设 $\mathcal{X}$ 按 $<$ 为部分有序集.

(1) 对 $\mathcal{S} \subset \mathcal{X}$ , 若有 $p \in \mathcal{X}$ , 使 $x < p$ 对一切 $x \in \mathcal{S}$ 都成立, 则称 $p$ 为 $\mathcal{S}$ 的上界.

(2) 设 $\mathcal{S} \subset \mathcal{X}$ , 如果对 $\mathcal{S}$ 中任意两个元素 $x, y$ , 必有 $x < y$ 或 $y < x$ , 则称 $\mathcal{S}$ 是完全有序的.

(3) $m \in \mathcal{X}$ 称为 $\mathcal{X}$ 的极大元, 如果对任何 $x \in \mathcal{X}$ , 当 $m < x$ , 必有 $x = m$ .

例2 对复数 $z = x + \mathrm{i}y, w = u + \mathrm{i}v$ ，定义 $z < w$ ，当 $x \leqslant u$ 且 $y \leqslant v$ 。可见复平面是部分有序的，而实轴、虚轴及某些直线则是完全有序的。

定理 1.2(Zorn 引理, 1935) 设 X 为非空的部分有序集. 如果 X 的任何完全有序的子集都有一个上界在 X 中, 则 X 必含有极大元.

可以证明 Zorn 引理和选择公理是等价的. 参见 [44], 第 6 页.

## § 2 线性空间, Hamel 基定义2.1 设 $X$ 是非空集合, $K$ 是数域(实数域或复数域). 如果在 $X$ 上定义了加法运算, 即对 $X$ 中每对元素 $x, y$ 都对应 $X$ 中一个元素 $z$ , 用 $z = x + y$ 表示; 又定义了数乘运算, 即对每个数 $\alpha \in K$ 和每个元素 $x \in X$ 都对应 $X$ 中一个元素 $u$ , 用 $u = \alpha x$ 表示; 而且满足如下公设:

(1) $x + y = y + x$ .

(2) $x + (y + z) = (x + y) + z.$

(3) $X$ 中存在唯一的元素, 用 $\theta$ 表示, 使对每个 $x \in X, x + \theta = x, \theta$ 称为 $X$

中零元.

(4) 对 $X$ 中每个元素 $x$ , 都存在唯一的元素, 用 $-x$ 表示, 使 $x + (-x) = \theta$ .

(5) $a(x + y) = ax + ay$ .

(6) $(\alpha + \beta)x = \alpha x + \beta x$ .

(7) $\alpha (\beta x) = (\alpha \beta)x$

(8) $1x = x$ .

这里 $x, y, z \in X, \alpha, \beta \in K$ . 则称 $X$ 按上述加法和数乘成为复 (当 $K$ 为复数域) 或实 (当 $K$ 为实数域) 线性空间. 通常又称为向量空间. 空间中的元素又称为向量或点.

今后如不特别指明，“线性空间”既可以是复的，亦可以是实的，其中的“数” $\alpha, \beta$ 则按所论空间是复或实的而定。任何复线性空间必然也是实线性空间。

容易证明,在线性空间 X 中对所有向量 x 和数 $\alpha$ 都有

$$
\begin{array}{l} {0 x = \theta ,} \\ {(- 1) x = - x,} \\ {\alpha \theta = \theta .} \end{array}
$$

为了方便起见,今后我们记 x-y 代替 $x+(-y)$ . 不难证明下述消去律在线性空间 X 中成立.

$$
\begin{array}{l} {x + y = x + z \Rightarrow y = z  ,} \\ {\alpha x = \alpha y \text {且} \alpha \neq 0 \Rightarrow x = y  ,} \\ {\alpha x = \beta x \text {且} x \neq \theta \Rightarrow \alpha = \beta  .} \end{array}
$$

定义2.2 线性空间 $X$ 中的一个非空子集 $M$ 称为 $X$ 中的线性流形，如果对任意的 $x, y \in M$ 与数 $\alpha$ ，都有 $x + y, ax \in M$ .

如果 $M$ 是 $X$ 的一个线性流形, 不难看出线性空间定义中的八条公设在 $M$ 中亦成立, 因此 $M$ 本身也成为线性空间. $X$ 的线性流形称为真的, 如果它不是全空间 $X$ . 只由一个零元组成的集合也是线性流形, 我们用 $\{\theta\}$ 表示它.

设 $x_{1},\cdots,x_{n}$ 是线性空间 X 中的 n 个元素， $\alpha_{1},\cdots,\alpha_{n}$ 是 n 个数，形如 $\alpha_{1}x_{1}+\cdots+\alpha_{n}x_{n}$ 的元素称为元素 $x_{1},\cdots,x_{n}$ 的线性组合.

设 $S$ 是线性空间 $X$ 的任意非空子集, 考虑 $S$ 中元素的所有线性组合形成的集合 $M$ . 易见它是 $X$ 的一个线性流形, 称为由 $S$ 张成的线性流形, 记为 $M = \operatorname{Sp}\{S\}$ . 容易验证下述论断成立.

(1) M 是 X 中包含 S 的所有的线性流形的交.

(2) $M$ 是 $X$ 中包含 $S$ 的最小线性流形, 即如果 $N$ 是 $X$ 中包含 $S$ 的线性流形, 则 $N$ 亦包含 $M$ .

线性空间中最重要的概念是线性相关与线性无关.

定义 2.3 线性空间 X 中有限的向量集合 $\{x_{1},\cdots,x_{n}\}$ 说是线性相关的，如果存在不全为零的数 $\alpha_{1},\cdots,\alpha_{n}$ ，使 $\alpha_{1}x_{1}+\cdots+\alpha_{n}x_{n}=\theta$ 。否则，就称其为线性无关的，这时关系 $\alpha_{1}x_{1}+\cdots+\alpha_{n}x_{n}=\theta$ 蕴含 $\alpha_{1}=\cdots=\alpha_{n}=0$ 。一个无穷的向量集合 S 称为线性无关的，如果 S 的每个有限子集都是线性无关的。否则，S 称为线性相关的。

容易看出,包含一个线性相关子集的集合一定线性相关,线性无关集一定不包含零向量.

定义 2.4 设 X 是线性空间, 如果存在正整数 n, 使 X 包含由 n 个向量组成的线性无关集, 而且 X 中每 $n+1$ 个向量的集合都是线性相关的, 则 X 称为有限维的, 如此的 n 称为 X 的维数, 有时记作 $\dim X = n$ .

只有零向量的线性空间也称为有限维的, 即零维的. 如果 X 不是有限维的, 就称为无穷维的, 这时记作 $\dim X = \infty$ .

正如我们将要看到的,在泛函分析中最感兴趣的空间是无穷维的,但是考虑有限维空间却经常是有益的.

定义 2.5 线性空间 X 中的有限子集 S 称为 X 的基, 如果 S 是线性无关的, 而且 S 张成的线性流形就是整个 X.

在线性代数中我们已经知道:线性空间 X 是 n 维的, 当且仅当 X 有一个由 n 个元素组成的基. n 维线性空间的每个基都含有 n 个元素.

有限维线性空间 X 的任意一个线性流形 M 亦是有限维的, 而且 $\dim M \leqslant \dim X$ .

参见[2],第六章.

定义2.6 设 $X$ 是线性空间. 给定 $X$ 的两个线性流形 $M, N$ , 我们用 $M + N$ 表示所有形如 $m + n, m \in M, n \in N$ 之元素的集合, 称之为 $M$ 与 $N$ 的和. 如果还有 $M \cap N = \{\theta\}$ , 即 $M$ 与 $N$ 有唯一公共元 $\theta$ , 则以 $M \oplus N$ 代替 $M + N$ , 称之为 $M$ 与 $N$ 的直接和.

如果 $X = M \oplus N$ ，则称 $M$ 与 $N$ 是代数互补的线性流形， $N$ 是 $M$ 在 $X$ 中的一个代数补。

定理2.1 设 $M, N$ 是线性空间 $X$ 的线性流形, 则 $X = M \oplus N$ 当且仅当对每个 $x \in X$ 有唯一表达式

(2.1)

$$
x = m + n, \quad m \in M, n \in N.
$$

证假设 $X = M \oplus N$ ，则每个 $x \in X$ 可以表为

$$
x = m + n, \quad m \in M, n \in N.
$$

如果又有 $m_{1} \in M, n_{1} \in N$ ，使

$$
x = m _ {1} + n _ {1},
$$

则

$$
m + n = m _ {1} + n _ {1},
$$

从而

$$
m - m _ {1} = n _ {1} - n \in M \cap N.
$$

由假设， $M\cap N = \{\theta \}$ ，故

$$
m - m _ {1} = n _ {1} - n = \theta ,
$$

即 $m_{1} = m, n_{1} = n$ .

反之, 如果每个 $x \in X$ 有形如(2.1)的唯一表达式, 则 $X = M + N$ . 假如 $x \in M \cap N$ , 则 $x$ 形如(2.1)的表达式为

$$
x = x + \theta , \text {及} x = \theta + x.
$$

根据假设, 表达式是唯一的, 故 $x = \theta$ . 从而 $M \cap N = \{\theta\}$ . 证毕.

定理2.2 如果 $X = M \oplus N$ ，则

$$
\dim X = \dim M + \dim N.
$$

证如果 $M$ 和 $N$ 有一个是无穷维的, 则 $X$ 亦是无穷维的, 结论自然成立. 故不妨设 $M$ 和 $N$ 都是有限维的.

设 $\{m_{1},\cdots,m_{j}\}$ 是M的基， $\{n_{1},\cdots,n_{k}\}$ 是N的基.因为 $X=M+N$ ，则 $\{m_{1},\cdots,m_{j},n_{1},\cdots,n_{k}\}$ 张成X.又因 $M\cap N=\{\theta\}$ ，可知 $\{m_{1},\cdots,m_{j},n_{1},\cdots,n_{k}\}$ 线性无关.于是 $\{m_{1},\cdots,m_{j},n_{1},\cdots,n_{k}\}$ 是X的一个基.从而

$$
\dim X = j + k = \dim M + \dim N.
$$

证毕.

给定线性空间 $X$ 的一个线性流形 $M$ , 是否一定存在 $M$ 在 $X$ 中的代数补? 为了回答这个问题, 我们需要引进 Hamel 基的概念.

定义 2.7 设 X 是具有非零元的线性空间. X 的子集 H 称为 X 的 Hamel 基, 如果

(1) H 是线性无关的；

(2) H 张成的线性流形是整个空间 X.

与有限维线性空间的基不同, Hamel 基的存在性不是明显的.

定理 2.3 设 X 是线性空间, S 是 X 中任意的线性无关子集, 则存在 X 的一个 Hamel 基 H, 使 $S \subset H$ .

证设 $\mathcal{S}$ 是 $X$ 中所有包含 $S$ 之线性无关子集的族, 则 $\mathcal{S}$ 按集合的包含关系是部分有序集, 即如果 $M, N \in \mathcal{S}$ , 且 $M \subset N$ , 则 $M < N$ . 显然 $\mathcal{S}$ 是非空的 (因 $S \in \mathcal{S}$ ). 如果 $\mathcal{S}_0$ 是 $\mathcal{S}$ 的完全有序子集, 则 $\mathcal{S}_0$ 中所有集合的并仍是 $X$ 中包含 $S$ 的线性无关子集, 即这个并仍在 $\mathcal{S}$ 中, 它是 $\mathcal{S}_0$ 的上界. 因此 $\mathcal{S}$ 满足 Zorn 引理条件, 故 $\mathcal{S}$ 中必有极大元, 记为 $H$ . 则 $H \supset S$ , 且 $H$ 是线性无关的. 如果 $H$ 张成的线性流形不是 $X$ ，则存在 $X$ 中元 $x$ ，它不在 $H$ 张成的线性流形中.这样 $H$ 与 $x$ 的并仍是 $X$ 中包含 $S$ 的线性无关子集， $H$ 又是它的真子集.这和 $H$ 是 $\mathcal{S}$ 的极大元矛盾.所以 $H$ 张成的线性流形是整个空间 $X$ .总之， $H$ 就是 $X$ 的Hamel基.证毕.

由这个定理可见:任何非零线性空间必有一个 Hamel 基.

事实上，假设 $X$ 是线性空间，包含非零元 $x_0$ 。记 $S = \{x_0\}$ ，则 $S$ 是 $X$ 中线性无关子集。由定理2.3，存在 $X$ 的一个Hamel基。

定理2.4 设 $M$ 是线性空间 $X$ 的线性流形, 则必存在 $X$ 的线性流形 $N$ , 使 $X = M \oplus N$ , 即 $N$ 是 $M$ 的一个代数补.

证不失一般性, 设 $M$ 是 $X$ 之非零的真线性流形, 因为 $M$ 本身也是线性空间, 它具有 Hamel 基 $H_{1} \cdot H_{1}$ 也是 $X$ 的线性无关子集. 由定理 2.3, 存在 $X$ 的一个 Hamel 基 $H$ , 使 $H \supset H_{1}$ . 设 $N$ 是由 $H \setminus H_{1}$ 张成的线性流形, 则 $N$ 就是 $M$ 的一个代数补. 事实上, 任给 $x \in X$ , 它是 $H$ 中元的线性组合, 从而可以表成 $H_{1}$ 中元的线性组合与 $H \setminus H_{1}$ 中元的线性组合之和, 即 $M$ 中元与 $N$ 中元之和. 所以 $X = M + N$ . 假若 $x \in M \cap N$ , 则存在 $u_{1}, \cdots, u_{j} \in H_{1}, v_{1}, \cdots, v_{k} \in H \setminus H_{1}$ 以及数 $\alpha_{1}, \cdots, \alpha_{j}, \beta_{1}, \cdots, \beta_{k}$ , 使

$$
x = \alpha_ {1} u _ {1} + \dots + \alpha_ {j} u _ {j} = \beta_ {1} v _ {1} + \dots + \beta_ {k} v _ {k}.
$$

从而

$$
\alpha_ {1} u _ {1} + \dots + \alpha_ {j} u _ {j} + (- \beta_ {1}) v _ {1} + \dots + (- \beta_ {k}) v _ {k} = \theta .
$$

因 $u_{1},\dots ,u_{j},v_{1},\dots ,v_{k}$ 是线性无关的，故

$$
\alpha_ {1} = \dots = \alpha_ {j} = \beta_ {1} = \dots = \beta_ {k} = 0.
$$

即 $x = \theta$ . 因此 $M \cap N = \{\theta\}$ . 证毕.

注意以后为简便,线性空间的零元常记为0.

## § 3 距离空间,距离线性空间定义3.1 若非空集合 $X$ 中任意两个元素 $x, y$ 都对应于一个实数 $d(x, y)$ , 使

(1) $d(x,y)\geqslant 0,d(x,y) = 0$ 当且仅当 $x = y$

(2) $d(x,y) = d(y,x)$

(3) $d(x,z)\leqslant d(x,y) + d(y,z)$

对任意的 $x, y, z \in X$ 成立，则称 $X$ 为距离空间，记作 $\langle X, d \rangle$ ，而称 $d(x, y)$ 为 $x$ 与 $y$ 之间的距离。通常称(3)为三角不等式。

定义3.2 设距离空间 $\langle X, d \rangle$ 中的点列 $\{x_{n}\}_{n=1}^{\infty}$ , 使

$$
\lim _ {n \to \infty} d (x _ {n}, x) = 0 (\text {或者} d (x _ {n}, x) \to 0),
$$

则称 $\{x_{n}\}_{n = 1}^{\infty}$ 按距离 $d(\cdot ,\cdot)$ 收敛到 $x$ ，并记作 $x_{n}\xrightarrow{d} x.$ 假如不致引起误会，通常也简记为 $x_{n}\rightarrow x$

上面我们只涉及 $X$ 上的拓扑. 一般在泛函分析中, $X$ 还是个线性空间, 有必要把其上的代数结构与拓扑结构结合起来. 这就很自然地导致下面的概念.

定义 3.3 设线性空间 X 上还赋有距离 $d(\cdot,\cdot)$ ，加法和数乘都按 $d(\cdot,\cdot)$ 所确定的极限是连续的，即

(1) $d(x_{n},x)\rightarrow 0,d(y_{n},y)\rightarrow 0\Rightarrow d(x_{n} + y_{n},x + y)\rightarrow 0.$

(2) $d(x_{n},x)\rightarrow 0,\alpha_{n}\rightarrow \alpha \Rightarrow d(\alpha_{n}x_{n},\alpha x)\rightarrow 0.$

那么线性空间 $X$ 称为距离线性空间.

下面我们看一些具体的距离线性空间的例子,它们在今后会经常遇到.

例 1 有界序列空间(m).

设 $X$ 代表所有的有界数列

$$
x = \{\xi_ {1}, \xi_ {2}, \dots , \xi_ {j}, \dots \} (\text {常简记为} x = \{\xi_ {j} \})
$$

的集合. 即对每个 $x = \{\xi_j\}$ , 存在常数 $K_x > 0$ , 使得对所有的 $j, |\xi_j| \leqslant K_x, \xi_j$ 称为元 $x = \{\xi_j\}$ 的第 $j$ 个坐标.

设 $x = \{\xi_j\}, y = \{\eta_j\}$ 属于 $X, \alpha$ 是数，定义

$$
\begin{array}{l} x + y = \{\xi_ {j} + \eta_ {j} \}, \\ \alpha x = \{\alpha \xi_ {j} \}, \\ d (x, y) = \sup _ {j \geqslant 1} | \xi_ {j} - \eta_ {j} |. \end{array}
$$

不难验证 $d(\cdot, \cdot)$ 满足距离定义， $X$ 是赋以距离 $d(\cdot, \cdot)$ 的距离线性空间。这样得到的空间称为有界序列空间，记作 $(m)$ ，有时也记作 $\ell^{\infty}$ 。

设 $x_{n}=\{\xi_{j}^{(n)}\}, n=1,2,\cdots,x=\{\xi_{j}\}$ 都是 $(m)$ 中的元，而且 $d(x_{n},x)\rightarrow0$ ，即任给 $\varepsilon>0$ ，存在 $n_{0}=n_{0}(\varepsilon)$ ，使当 $n\geqslant n_{0}$ 时，

$$
d \left(x _ {n}, x\right) = \sup _ {j \geqslant 1} \left| \xi_ {j} ^ {(n)} - \xi_ {j} \right| <   \varepsilon .
$$

则当 $n \geqslant n_0$ 时，对一切 $j$

$$
\mid \xi_ {j} ^ {(n)} - \xi_ {j} \mid <   \varepsilon .
$$

反之，如果对任给 $\varepsilon > 0$ ，存在 $n_0 = n_0(\varepsilon)$ ，使当 $n \geqslant n_0$ 时，对一切 $j$

$$
\left| \xi_ {j} ^ {(n)} - \xi_ {j} \right| <   \varepsilon .
$$

则

$$
d \left(x _ {n}, x\right) = \sup _ {j \geqslant 1} \left| \xi_ {j} ^ {(n)} - \xi_ {j} \right| \leqslant \varepsilon .
$$

即 $d(x_{n},x)\rightarrow 0$

由此可见空间 $(m)$ 中的收敛就是按坐标的一致收敛.

例2 设 $X$ 代表所有收敛数列

$$
x = \{\xi_ {1}, \xi_ {2}, \dots , \xi_ {j}, \dots \}
$$

的集合. 即对每个 $x = \{\xi_j\} \in X, \lim_{j \to \infty} \xi_j = \xi$ 存在且有限.

像空间 $(m)$ 一样定义加法、数乘和距离 $d(\cdot,\cdot)$ ，容易验证X是赋有距离 $d(\cdot,\cdot)$ 的线性空间，称为收敛序列空间，记作 $(c)$ .

易见 $(c)$ 是 $(m)$ 的线性流形，而且距离的定义也是一样的，因此 $(c)$ 中的收敛亦是按坐标的一致收敛.

例3 本质有界可测函数空间 $L^{\infty}[a,b]$ ，这里 $a, b$ 是任意两个实数，而且 $-\infty < a < b < \infty$ 。

在引进这个空间之前,先引进本质上确界的概念.

设 $f(t)$ 是区间 $[a, b]$ 上Lebesgue可测函数. 如果存在 $[a, b]$ 的一个零测度子集 $E$ , 使 $f(t)$ 在 $[a, b] \setminus E$ 上是有界函数, 则称 $f$ 是 $[a, b]$ 上本质有界可测函数. 称

$$
\operatorname * {e s s} _ {t \in [ a, b ]} | f (t) | = \inf _ {m (E) = 0} \left\{\sup _ {t \in [ a, b ] \setminus E} | f (t) | \right\}
$$

为 $f(t)$ 在 $[a, b]$ 上的本质上确界，这里 $m(E)$ 表示集合 $E$ 的Lebesgue测度.

设 $X$ 代表区间 $[a, b]$ 上所有本质有界可测函数的集合. $X$ 中两个元 $x = x(t), y = y(t)$ 看作是相等的, 如果 $x(t)$ 与 $y(t)$ 是几乎处处相等的, 即 $x(t) = y(t)$ , a.e. 于 $[a, b]$ . 对 $X$ 中的两个元 $x = x(t), y = y(t)$ , 数 $\alpha$ , 定义

$$
(x + y) (t) = x (t) + y (t), (\alpha x) (t) = \alpha x (t), t \in [ a, b ],
$$

即逐点定义函数的加法和数乘运算. 易见 $X$ 是个线性空间, 又定义

$$
d (x, y) = \underset {t \in [ a, b ]} {\operatorname{esssup}} | x (t) - y (t) |.
$$

我们来验证它满足距离公设.

(1) 显然 $d(x, y) \geqslant 0$ . 如果 $x(t) = y(t)$ , a.e. 于 $[a, b]$ , 则由定义有 $d(x, y) = 0$ . 另一方面, 如果

$$
d (x, y) = \inf _ {m (E) = 0} \left\{\sup _ {t \in [ a, b ] \setminus E} | x (t) - y (t) | \right\} = 0,
$$

则对每个正整数 $n$ ，存在 $E_{n}\subset [a,b],m(E_{n}) = 0$ ，且

$$
\sup _ {t \in [ a, b ] \setminus E _ {n}} | x (t) - y (t) | \leqslant \frac {1}{n}.
$$

令 $E = \bigcup_{n=1}^{\infty} E_n$ ，则 $m(E) = 0$ ，而且

$$
\sup _ {t \in [ a, b ] \setminus E} | x (t) - y (t) | \leqslant \sup _ {t \in [ a, b ] \setminus E _ {n}} | x (t) - y (t) | \leqslant \frac {1}{n}.
$$

令 $n\to \infty$ ，可见

$$
\sup _ {t \in [ a, b ] \setminus E} | x (t) - y (t) | = 0.
$$

于是， $x(t) = y(t)$ ，a.e.于 $[a,b]$ ，即 $x = y$

(2) 是显然的.

(3) 设 $x(t), y(t), z(t)$ 都是 $X$ 中元, 则对任意 $\varepsilon > 0$ , 存在 $[a, b]$ 的零测度集 $E_{\epsilon}^{1}, E_{\epsilon}^{2}$ , 使

$$
\sup _ {t \in [ a, b ] \setminus E _ {\varepsilon} ^ {l}} | x (t) - y (t) | \leqslant d (x, y) + \frac {\varepsilon}{2},
$$

$$
\sup _ {t \in [ a, b ] \setminus E _ {\epsilon} ^ {2}} | y (t) - z (t) | \leqslant d (y, z) + \frac {\epsilon}{2}.
$$

令 $E_{\epsilon} = E_{\epsilon}^{1}\bigcup E_{\epsilon}^{2}$ ，则 $E_{\epsilon}$ 仍是 $[a,b]$ 的零测度集，且

$$
\begin{array}{l} \sup _ {t \in [ a, b ] \setminus E _ {\epsilon}} | x (t) - z (t) | \\ \leqslant \sup _ {t \in [ a, b ] \setminus E _ {\epsilon}} | x (t) - y (t) | + \sup _ {t \in [ a, b ] \setminus E _ {\epsilon}} | y (t) - z (t) | \\ \leqslant \sup _ {t \in [ a, b ] \setminus E _ {\epsilon} ^ {1}} | x (t) - y (t) | + \sup _ {t \in [ a, b ] \setminus E _ {\epsilon} ^ {2}} | y (t) - z (t) | \\ \leqslant d (x, y) + d (y, z) + \varepsilon . \end{array}
$$

从而

$$
\begin{array}{r l} d (x, z) & = \inf _ {m (E) = 0} \{\sup _ {t \in [ a, b ] \setminus E} | x (t) - z (t) | \} \\ & \leqslant \sup _ {t \in [ a, b ] \setminus E _ {\epsilon}} | x (t) - z (t) | \\ & \leqslant d (x, y) + d (y, z) + \epsilon . \end{array}
$$

$\varepsilon > 0$ 是任意的，故

$$
d (x, z) \leqslant d (x, y) + d (y, z).
$$

总之， $d(\cdot ,\cdot)$ 是一个距离.又容易验证 $X$ 中加法和数乘按这个距离 $d(\cdot ,\cdot)$ 是连续的.一般称这样得到的距离线性空间为本质有界可测函数空间，记作 $L^{\infty}[a,b]$

可以证明 $L^{\infty}[a,b]$ 中收敛是几乎处处一致收敛，即设 $x_{n}(t), x(t) \in L^{\infty}[a,b]$ ，则 $d(x_{n},x) \to 0$ 等价于任给 $\varepsilon > 0$ ，存在正整数 $n_0$ 及零测度集 $E_{\varepsilon}$ ，使 $|x_{n}(t) - x(t)| < \varepsilon$ ，对 $n \geqslant n_0$ 和所有 $t \in [a,b] \setminus E_{\varepsilon}$ .（参见[11]，第17—18页）

例 4 所有序列空间(s).

设 $X$ 是所有数列的集合. 如果 $x = \{\xi_j\}, y = \{\eta_j\}$ 属于 $X, \alpha$ 是数, 定义

$$
x + y = \left\{\xi_ {j} + \eta_ {i} \right\}, \quad a x = \left\{a \xi_ {j} \right\},
$$

易见 $X$ 是线性空间，又定义

$$
d (x, y) = \sum_ {j = 1} ^ {\infty} \frac {1}{2 ^ {j}} \frac {| \xi_ {j} - \eta_ {j} |}{1 + | \xi_ {j} - \eta_ {j} |},
$$

显然 $d(\cdot, \cdot)$ 满足距离公设的(1)，(2). 为证明它满足(3)，我们需要一个不等式：对任意复数 $a, b$ ，

$$
\frac {| a + b |}{1 + | a + b |} \leqslant \frac {| a |}{1 + | a |} + \frac {| b |}{1 + | b |}.\tag{3.1}
$$

考虑 $(0, +\infty)$ 上函数

$$
f (t) = \frac {t}{1 + t}.
$$

我们有

$$
f ^ {\prime} (t) = \frac {1}{(1 + t) ^ {2}} > 0.
$$

于是 $f(t)$ 是 $(0, +\infty)$ 上单调增加函数. 因为

$$
\mid a + b \mid \leqslant \mid a \mid + \mid b \mid ,
$$

故

$$
\begin{array}{r l} \frac {| a + b |}{1 + | a + b |} & \leqslant \frac {| a | + | b |}{1 + | a | + | b |} \\ & = \frac {| a |}{1 + | a | + | b |} + \frac {| b |}{1 + | a | + | b |} \\ & \leqslant \frac {| a |}{1 + | a |} + \frac {| b |}{1 + | b |}. \end{array}
$$

即不等式(3.1)成立.

假设 $x=\{\xi_{j}\},y=\{\eta_{j}\},z=\{\zeta_{j}\}$ 都属于 X，因为 $\xi_{j}-\zeta_{j}=(\xi_{j}-\eta_{j})+(\eta_{j}-\zeta_{j}),j=1,2,\cdots$ ，则由不等式(3.1)，

$$
\begin{array}{r l} d (x, z) & = \sum_ {j = 1} ^ {\infty} \frac {1}{2 ^ {j}} \frac {| \xi_ {j} - \zeta_ {j} |}{1 + | \xi_ {j} - \zeta_ {j} |} \\ & \leqslant \sum_ {j = 1} ^ {\infty} \frac {1}{2 ^ {j}} \left[ \frac {| \xi_ {j} - \eta_ {j} |}{1 + | \xi_ {j} - \eta_ {j} |} + \frac {| \eta_ {j} - \zeta_ {j} |}{1 + | \eta_ {j} - \zeta_ {j} |} \right] \\ & = \sum_ {j = 1} ^ {\infty} \frac {1}{2 ^ {j}} \frac {| \xi_ {j} - \eta_ {j} |}{1 + | \xi_ {j} - \eta_ {j} |} + \sum_ {j = 1} ^ {\infty} \frac {1}{2 ^ {j}} \frac {| \eta_ {j} - \zeta_ {j} |}{1 + | \eta_ {j} - \zeta_ {j} |} \\ & = d (x, y) + d (y, z). \end{array}
$$

所以 $d(\cdot, \cdot)$ 是 $X$ 上的距离. 容易验证 $X$ 中加法和数乘按上述定义的距离 $d(\cdot, \cdot)$ 是连续的. 这样得到的距离线性空间称为所有序列空间, 记作 $(s)$ .

设 $x_{n}=\{\xi_{j}^{(n)}\}\in(s)$ , $n=1,2,\cdots,x_{0}=\{\xi_{j}^{0}\}\in(s)$ . 如果 $x_{n}\to x_{0}$ ，则 $\lim_{n\to\infty}\xi_{j}^{(n)}=\xi_{j}^{0}, j=1,2,\cdots$ . 否则，存在某个正整数 j 及 $\varepsilon_{0}>0$ ，与正整数列的子序列 $\{n_{k}\}_{k=1}^{\infty}$ ，使

$$
\mid \xi_ {j} ^ {(n _ {k})} - \xi_ {j} ^ {0} \mid \geqslant \varepsilon_ {0}, k = 1, 2, \dots .
$$

由不等式(3.1)的证明知道, $f(t)=\frac{t}{1+t}$ 是单调递增的,故

$$
\begin{array}{r l} d (x _ {n _ {k}}, x _ {0}) & \geqslant \frac {1}{2 ^ {j}} \frac {| \xi_ {j} ^ {(n _ {k})} - \xi_ {j} ^ {0} |}{1 + | \xi_ {j} ^ {(n _ {k})} - \xi_ {j} ^ {0} |} \\ & \geqslant \frac {1}{2 ^ {j}} \frac {\varepsilon_ {0}}{1 + \varepsilon_ {0}}, k = 1, 2, \dots . \end{array}
$$

这与 $d(x_{n_k}, x_0) \to 0$ 矛盾.

反之，若 $\{x_{n}\}_{n = 1}^{\infty}$ 按坐标收敛于 $x_0$ ，易证 $\{x_{n}\}_{n = 1}^{\infty}$ 在（s）中收敛于 $x_0$ .请读者把这当作习题来做.

这说明(s)中收敛等价于按坐标收敛.

例5 空间 $\ell^p (1\leqslant p <   \infty)$

设 $X$ 代表满足条件 $\sum_{j=1}^{\infty} |\xi_j|^p < \infty$ 的所有数列 $x = \{\xi_j\}$ 的集合. 如果 $x = \{\xi_j\}, y = \{\eta_j\}$ 属于 $X, \alpha$ 是数, 定义

$$
x + y = \left\{\xi_ {j} + \eta_ {j} \right\}, \alpha x = \left\{\alpha \xi_ {j} \right\}.
$$

对任意复数 $a, b$ ，显然

(3.2) $|a + b|^p \leqslant (|a| + |b|)^p \leqslant [2\max \{|a|, |b|\}]^p \leqslant 2^p (|a|^p + |b|^p).$

据此容易证明 $X$ 按上述定义的加法和数乘是一个线性空间. 又定义

$$
d (x, y) = \left(\sum_ {j = 1} ^ {\infty} \left| \xi_ {j} - \eta_ {j} \right| ^ {p}\right) ^ {1 / p}.
$$

易见它满足距离公设(1),(2).利用Minkowski不等式(参见[6],第六章,§1,定理4),

$$
\left(\sum_ {j = 1} ^ {\infty} \mid \xi_ {j} + \eta_ {j} \mid^ {p}\right) ^ {1 / p} \leqslant \left(\sum_ {j = 1} ^ {\infty} \mid \xi_ {j} \mid^ {p}\right) ^ {1 / p} + \left(\sum_ {j = 1} ^ {\infty} \mid \eta_ {j} \mid^ {p}\right) ^ {1 / p},
$$

可见它也满足距离公设(3)，所以 $d(\cdot ,\cdot)$ 是 $X$ 上的距离.进一步易证 $X$ 是赋以距离 $d(\cdot ,\cdot)$ 的距离线性空间，称为空间 $\ell^p$

可以证明, 空间 $\ell^{p}$ 的序列 $x_{n}=\{\xi_{j}^{(n)}\}, n=1,2,\cdots$ 收敛于 $x=\{\xi_{j}\}$ , 当

(1) $\xi_{j}^{(n)}\rightarrow \xi_{j}, n\rightarrow \infty$ ，对所有 $j$ .

(2) 任给 $\varepsilon > 0$ , 存在 $N_0 = N_0(\varepsilon)$ , 使 $\sum_{j=N}^{\infty} |\xi_j^{(n)}|^p < \varepsilon$ , 对所有 $N \geqslant N_0$ 和所有 $n$ .

参见[11],第22页.

例6 空间 $L^p [a,b](1\leqslant p < \infty)$ ，与例3一样，这里 $a,b$ 是任意两个实数，而且 $-\infty < a < b < \infty$

设 $X$ 代表所有满足条件 $\int_{a}^{b}|x(t)|^{p}\mathrm{d}t < \infty$ 的区间 $[a,b]$ 上可测函数 $x(t)$ 的集合.这样的 $x(t)$ 称为 $[a,b]$ 上 $\pmb{p}$ 幂可积函数. $X$ 中两个元 $x = x(t),y$ $= y(t)$ 看作是相等的，如果 $x(t)$ 与 $y(t)$ 是几乎处处相等的，即 $x(t) = y(t),\mathrm{a}.$ e.于 $[a,b]$ . 设 $x = x(t),y = y(t)$ 属于 $X,\alpha$ 是数，定义

$$
(x + y) (t) = x (t) + y (t), \quad (\alpha x) (t) = \alpha x (t), \quad t \in [ a, b ].
$$

利用不等式(3.2)可以证明 $X$ 是线性空间. 又定义

$$
d (x, y) = \left(\int_ {a} ^ {b} | x (t) - y (t) | ^ {p} d t\right) ^ {1 / p},
$$

显然它满足距离公设(1)，(2).由Minkowski不等式(见[6]第六章，§1，定理4)，如果 $p \geqslant 1, x, y \in L^{p}[a, b]$ ，则

$$
\left(\int_ {a} ^ {b} | x (t) + y (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p} \leqslant \left(\int_ {a} ^ {b} | x (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p} + \left(\int_ {a} ^ {b} | y (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p}.
$$

可见距离公设(3)成立,所以 $d(\cdot,\cdot)$ 是 X 上的距离.容易验证 X 是赋有距离 $d(\cdot,\cdot)$ 的距离线性空间,称为空间 $L^{p}[a,b]$ .

设 $x_{n}=x_{n}(t)$ , $x=x(t)\in L^{p}[a,b]$ , $n=1,2,\cdots$ , 而且

$$
\int_ {a} ^ {b} \mid x _ {n} (t) - x (t) \mid^ {p} \mathrm{d} t \to 0, \text {当} n \to \infty ,
$$

则称函数列 $\{x_{n}(t)\}_{n = 1}^{\infty}\pmb{p}$ 阶平均收敛于函数 $x(t)$ .

显然 $L^p [a,b]$ 中收敛就是 $\pmb{p}$ 阶平均收敛.

注意例3函数空间 $L^{\infty}[a,b]$ 和例6函数空间 $L^{p}[a,b]$ 中的元不是一个函数，而是一个几乎处处相等的函数的等价类.

## § 4 距离空间中的拓扑,可分空间定义 4.1 对距离空间 $\langle X, d \rangle$ ,

(1) 设 $x_0 \in X, r > 0$ . $B(x_0, r) = \{x \in X : d(x, x_0) < r\}$ 称为以 $x_0$ 为心, $r$ 为半径的球.

(2) $X$ 中的点集 $O$ 称为开的, 如果对任何 $y \in O$ , 都有 $r > 0$ , 使 $B(y, r) \subset O$ .

(3) 设 $y \in X, X$ 的子集 $U$ 称为 $y$ 的邻域, 如果有 $r > 0$ , 使 $B(y, r) \subset U$ .

(4) 对 $E \subset X$ , 点 $x_0 \in X$ 称为 $E$ 的极限点, 如果对任何 $r > 0$ , 球 $B(x_0, r)$ 包含了 $E$ 中异于 $x_0$ 的点.

(5) $X$ 中的点集 $F$ 称为闭的, 如果 $F$ 的极限点都在 $F$ 中.

(6) 设 $G \subset X$ , 点 $x_0 \in X$ 称为 $G$ 的内点, 若 $G$ 是 $x_0$ 的邻域. 点集 $G$ 的内点全体称为 $G$ 的内部.

定义4.2 设 $y = f(x)$ 是从距离空间 $\langle X, d \rangle$ 到距离空间 $\langle Y, \rho \rangle$ 的函数. $x_0 \in X, y_0 \in Y, f(x_0) = y_0$ . 如果对 $y_0$ 的任何邻域 $V_{y_0}$ 都有 $x_0$ 的邻域 $U_{x_0}$ , 使 $f(x) \in V_{y_0}$ , 当 $x \in U_{x_0}$ , 则称 $f(x)$ 在 $x_0$ 处连续. 如果 $f(x)$ 在 $X$ 中每点都连续, 就称 $f(x)$ 是连续函数.

定理 4.1 从距离空间 $\langle X, d \rangle$ 到距离空间 $\langle Y, \rho \rangle$ 的函数 $f(x)$ 是连续的必须且只须对 Y 中任何开集 $O, f^{-1}(O)$ 都是 X 中开集.

这里 $f^{-1}(O)$ 表示 $O$ 的原象 $\{x \in X : f(x) \in O\}$ .

证设 $f(x)$ 连续, $O$ 是 $Y$ 中开集. 对任意的 $x_0 \in f^{-1}(O)$ , 必有 $y_0 = f(x_0) \in O$ . 取 $y_0$ 的邻域 $V_0$ 使 $V_0 \subset O$ , 由 $f(x)$ 在 $x_0$ 处连续, 必有 $x_0$ 的邻域 $U_0$ . 使 $f(x) \in V_0$ , 当 $x \in U_0$ . 故 $U_0 \subset f^{-1}(V_0) \subset f^{-1}(O)$ , 即 $f^{-1}(O)$ 是 $X$ 中开集.

反之，任给 $x_0 \in X$ ，设 $f(x_0) = y_0$ 。取 $y_0$ 的任一邻域 $V_0$ ，不失一般性，可以假定 $V_0$ 是开的。由假设 $f^{-1}(V_0)$ 也是开的。因 $x_0 \in f^{-1}(V_0)$ ，故有 $x_0$ 的邻域 $U_0$ ，使 $U_0 \subset f^{-1}(V_0)$ 。于是 $f(x) \in V_0$ ，当 $x \in U_0$ ，即 $f(x)$ 在 $x_0$ 处连续。证毕。

全体有理数是可数的,而且在实数轴上稠密,这给我们研究实数带来许多方便.同样,实数轴的这个性质在一般距离空间中的推广:可分空间概念,也使我们能够在空间可分的假设下比较容易地证出一些深刻的结果.

定义4.3 设 $\langle X, d \rangle$ 是距离空间, 子集 $S \subset X$ 称为 $X$ 的稠密集, 如果任给 $\varepsilon > 0$ , 对任何的 $x \in X$ , 存在元 $x_0 \in S$ , 使 $d(x, x_0) < \varepsilon$ .

空间 X 称为可分的, 如果 X 内存在一个可数的稠密集.

我们在上节列举的许多空间都是可分的.

例1 空间 $l^p (1\leqslant p <   \infty)$ 可分.

设 $S_0$ 是 $\ell^p$ 中所有形如

$$
\left\{r _ {1}, r _ {2}, \dots , r _ {n}, 0, 0, \dots \right\}
$$

的元素的集合, 其中 n 是任意正整数, $r_{j}(j=1,2,\cdots,n)$ 是任意的有理数. 则 $S_{0}$ 是可数的. 易证 $S_{0}$ 在实空间 $l^{p}$ 中稠密.

事实上，任给 $\varepsilon > 0$ ，对任何 $x = \{\xi_{j}\} \in \ell^{p}, \xi_{j} (j = 1, 2, \cdots)$ 是实数，都存在正整数 n，使

$$
\sum_ {j = n + 1} ^ {\infty} | \xi_ {j} | ^ {p} <   \frac {\varepsilon^ {p}}{2}.
$$

显然可选有理数 $r_{j}, j = 1, \cdots, n$ ，使

$$
\sum_ {j = 1} ^ {n} \mid \xi_ {j} - r _ {j} \mid^ {p} <   \frac {\varepsilon^ {p}}{2}.
$$

令 $x_{0}=\{r_{1},\cdots,r_{n},0,0,\cdots\}$ ，则 $x_{0}\in S_{0}$ ，且

$$
\left[ d \left(x, x _ {0}\right) \right] ^ {p} = \sum_ {j = 1} ^ {n} \left| \xi_ {j} - r _ {j} \right| ^ {p} + \sum_ {j = n + 1} ^ {\infty} \left| \xi_ {j} \right| ^ {p} <   \varepsilon^ {p}.
$$

从而

$$
d (x, x _ {0}) <   \varepsilon .
$$

因而实空间 $l^p$ 是可分的. 进而还可以证明复空间 $l^p$ 也是可分的.

例 2 空间(s)可分.

像例 1 一样, 令 $S_{0}$ 表示所有形如

$$
\left\{r _ {1}, r _ {2}, \dots , r _ {n}, 0, 0, \dots \right\}
$$

的元素的集合, 其中 $n$ 是任意正整数, $r_j (j = 1,2,\dots,n)$ 是任意的有理数. 则 $S_0$ 可数. 为证明 $S_0$ 在实空间 $(s)$ 内稠密, 只须证明任给 $x \in (s)$ , 存在 $S_0$ 中元列 $\{x_k\}_{k=1}^{\infty}$ , 使 $x_k \to x$ . 由前节例4知道, 这等价于对所有的正整数 $j$ , $x_k$ 的第 $j$ 个坐标收敛于 $x$ 的第 $j$ 个坐标. 设 $x = \{\xi_1, \xi_2, \cdots, \xi_j, \cdots\} \in (s)$ , 对每个 $\xi_j$ , 我们可以构造一个有理数列 $\{r_j^{(k)}\}_{k=1}^{\infty}$ , 使 $r_j^{(k)} \to \xi_j$ , 当 $k \to \infty$ . 令

$$
x _ {k} = \left\{r _ {1} ^ {(k)}, r _ {2} ^ {(k)}, \dots , r _ {k} ^ {(k)}, 0, 0, \dots \right\}, k = 1, 2, \dots ,
$$

则 $x_{k} \in S_{0}$ , 而且 $x_{k} \to x$ . 因此实空间 $(s)$ 是可分的.

进一步可以证明复空间(s)也是可分的.

例3 空间 $(m)$ 不可分.

令

$$
E _ {0} = \{x = \{\xi_ {j} \} \in (m): \xi_ {j} = 0   \text {或}   1, j = 1, 2, \dots \}.
$$

注意 $E_0$ 中每个元 $x = \{\xi_j\}$ 对应着[0,1]上一个二进位小数，据此可建立 $E_0$ 和区间[0,1]之间1-1对应关系，因此 $E_0$ 的基数为 $c$ ，即 $E_0$ 是不可数的.任取 $E_0$ 内两个不同元 $x = \{\xi_j\}, y = \{\eta_j\}$ ，显然 $d(x,y) = 1.$ 由此可断定（ $m$ )是不可分的.

事实上, 如果 $(m)$ 内存在可数的稠密集 $S$ , 以 $S$ 中每个元为心, $\varepsilon = 1/3$ 为半径作球, $(m)$ 的所有元都将落在这些球内. 但这些球是可数的, 于是不可数集 $E_0$ 中至少有两个不同元 $x, y$ 落在同一球内. 设该球球心为 $x_0$ , 则

$$
1 = d (x, y) \leqslant d (x, x _ {0}) + d (x _ {0}, y) \leqslant \frac {1}{3} + \frac {1}{3} = \frac {2}{3}.
$$

矛盾.

尽管空间 $(m)$ 不可分，但可以证明，作为空间 $(m)$ 的线性流形 $(c)$ 是可分的.

利用测度论上的 Лузин 定理与 Weierstrass 逼近定理, 我们还可以证明空间 $L^{p}[a, b](1 \leqslant p < \infty)$ 是可分的. (参见[11], 第47页)

## § 5 完备的距离空间定义5.1 设 $\{x_{n}\}_{n = 1}^{\infty}$ 是距离空间 $\langle X,d\rangle$ 中的序列，如果对任给的 $\varepsilon >0$ ，都有正整数 $N$ ，使

$$
d (x _ {n}, x _ {m}) <   \varepsilon , \text {当} n, m \geqslant N,
$$

则称 $\{x_{n}\}_{n = 1}^{\infty}$ 为Cauchy序列.

显然凡收敛序列都是 Cauchy 序列,但其逆不真.例如全体有理数构成的距离空间中就有不收敛的 Cauchy 序列.

定义5.2 若距离空间 $\langle X, d \rangle$ 中任何Cauchy序列都收敛，则称距离空间 $\langle X, d \rangle$ 为完备的.

回想各种实数的定义,其精神实质无非就是把有理数集加以完备化而已.只有对于完备的空间,极限运算才能顺利进行,也才有可能用上经典分析的技巧.明白了这点,为什么人们对各种空间常要考虑其完备性,便是很自然的事了.

以下且看两个最常见的完备空间的例子.

例1 $C[0,1]$ 是完备空间.

$C[0,1]$ 表示区间 $[0,1]$ 上的所有复值连续函数的集合，逐点定义加法和数乘运算，即

$$
(x + y) (t) = x (t) + y (t), \quad (\alpha x) (t) = \alpha x (t), t \in [ 0, 1 ],
$$

当 $x(t), y(t) \in C[0,1], \alpha \in \mathbf{C}$ . 赋以如下距离

$$
d (x, y) = \max _ {0 \leqslant t \leqslant 1} | x (t) - y (t) |.
$$

不难证明 $C[0,1]$ 是赋以距离 $d(\cdot ,\cdot)$ 的距离线性空间，通常称为连续函数空间.

下面证明 $C[0,1]$ 是完备的.

设 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 是 $C[0,1]$ 中的Cauchy序列，则任给 $\varepsilon >0$ ，存在正整数 $N$ ，使

$$
d (x _ {n}, x _ {m}) <   \varepsilon , \quad \text {当} n, m \geqslant N.
$$

即

$$
| x _ {n} (t) - x _ {m} (t) | <   \epsilon , \quad \text {当} n, m \geqslant N, 0 \leqslant t \leqslant 1.
$$

显然对每个 $t \in [0,1], \{x_n(t)\}_{n=1}^{\infty}$ 收敛. 设 $\lim_{n \to \infty} x_n(t) = x(t)$ , 则在上式中令 $m \to \infty$ 可得

$$
| x _ {n} (t) - x (t) | \leqslant \varepsilon , \text {当} n \geqslant N, 0 \leqslant t \leqslant 1.
$$

这表明 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 在[0,1]上一致地收敛到 $x(t)$ . 由数学分析可知, $x(t)$ 也是[0,1]上连续函数. 又由上式

$$
d (x _ {n}, x) = \max _ {0 \leqslant t \leqslant 1} | x _ {n} (t) - x (t) | \leqslant \varepsilon , \text {当} n \geqslant N,
$$

即 $x_{n}\rightarrow x$ .故 $C[0,1]$ 是完备的.

例2 $L^p [a,b](1\leqslant p\leqslant \infty)$ 是完备空间.

我们只讨论 $1 < p < \infty$ 情形，对 $p = 1$ 或 $\infty$ 情形可类似证明.

设 $\{x_{n}\}_{n = 1}^{\infty}$ 是 $L^{p}[a,b]$ 中的Cauchy序列，则有正整数 $N_{k}$ ，使当 $n,m\geqslant N_k$ 时，

$$
d \left(x _ {n}, x _ {m}\right) <   \frac {1}{2 ^ {k}}.
$$

不妨设 $N_{1}<N_{2}<\cdots<N_{k}<\cdots$ ，则

$$
\sum_ {k = 1} ^ {\infty} d \left(x _ {N _ {k + 1}}, x _ {N _ {k}}\right) \leqslant \sum_ {k = 1} ^ {\infty} \frac {1}{2 ^ {k}} <   \infty ,
$$

设 $1 < q < \infty$ ，使 $\frac{1}{p} + \frac{1}{q} = 1$ ，由 Hölder 不等式

$$
\begin{array}{r l} \int_ {a} ^ {b} | x _ {N _ {k + 1}} (t) - x _ {N _ {k}} (t) | \mathrm{d} t & \leqslant \left(\int_ {a} ^ {b} | x _ {N _ {k + 1}} (t) - x _ {N _ {k}} (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p} (\int_ {a} ^ {b} 1 \mathrm{d} t) ^ {1 / q} \\ & = d (x _ {N _ {k + 1}}, x _ {N _ {k}}) (b - a) ^ {1 / q} \end{array}
$$

于是

$$
\sum_ {k = 1} ^ {\infty} \int_ {a} ^ {b} | x _ {N _ {k + 1}} (t) - x _ {N _ {k}} (t) | \mathrm{d} t \leqslant (b - a) ^ {1 / q} \sum_ {k = 1} ^ {\infty} d \left(x _ {N _ {k + 1}}, x _ {N _ {k}}\right) <   \infty .
$$

则

$$
\int_ {a} ^ {b} \left(\sum_ {k = 1} ^ {\infty} \left| x _ {N _ {k + 1}} (t) - x _ {N _ {k}} (t) \right|\right) d t <   \infty .
$$

这说明 $\sum_{k=1}^{\infty}\left|x_{N_{k+1}}(t)-x_{N_k}(t)\right|$ , 从而 $\sum_{k=1}^{\infty}\left[x_{N_{k+1}}(t)-x_{N_k}(t)\right]$ 在 $[a,b]$ 上几乎处处收敛.于是

$$
\lim _ {j \rightarrow \infty} x _ {N _ {j}} (t) = x _ {N _ {1}} (t) + \lim _ {j \rightarrow \infty} \sum_ {k = 1} ^ {j - 1} \left[ x _ {N _ {k + 1}} (t) - x _ {N _ {k}} (t) \right]
$$

在 $[a, b]$ 上几乎处处存在. 设

$$
\lim _ {j \to \infty} x _ {N _ {j}} (t) = x (t), \mathrm{a.e.} \text {于} [ a, b ],
$$

则 $x(t)$ 可测，根据Fatou引理(参见[6]，第五章，§5)

$$
\begin{array}{r l}\int_ {a} ^ {b} | x _ {N _ {k}} (t) - x (t) | ^ {p} \mathrm{d} t&\leqslant \underset {j \rightarrow \infty} {\lim} \int_ {a} ^ {b} | x _ {N _ {k}} (t) - x _ {N _ {j}} (t) | ^ {p} \mathrm{d} t\\&= \underset {j \rightarrow \infty} {\lim} [ d (x _ {N _ {k}}, x _ {N _ {j}}) ] ^ {p} \leqslant \frac {1}{2 ^ {k p}},\end{array}
$$

故 $x_{N_k}(t) - x(t)\in L^p [a,b]$ .已知 $x_{N_k}(t)\in L^p [a,b]$ ，由 $L^p [a,b]$ 是线性空间可知 $x(t)\in L^{p}[a,b]$

任给 $\varepsilon > 0$ ，由 $\{x_{n}\}_{n=1}^{\infty}$ 是 Cauchy 序列，应有正整数 $N$ ，使

$$
d (x _ {n}, x _ {m}) <   \varepsilon , \text {当} n, m \geqslant N.
$$

显然存在正整数 $K$ ，使 $N_{k}\geqslant N$ ，当 $k\geqslant K$ .于是

$$
d (x _ {n}, x _ {N _ {k}}) <   \varepsilon , \text {当} n \geqslant N, k \geqslant K.
$$

根据 Fatou 引理, 当 $n \geqslant N$ 时,

$$
\begin{array}{r l}{[ d (x _ {n}, x) ] ^ {p}}&= \int_ {a} ^ {b} | x _ {n} (t) - x (t) | ^ {p} \mathrm{d} t\\&\leqslant \underset {j \rightarrow \infty} {\lim} \int_ {a} ^ {b} | x _ {n} (t) - x _ {N _ {j}} (t) | ^ {p} \mathrm{d} t\\&= \underset {j \rightarrow \infty} {\lim} [ d (x _ {n}, x _ {N _ {j}}) ] ^ {p} \leqslant \varepsilon^ {p},\end{array}
$$

由此可见， $d(x_{n},x)\rightarrow 0,n\to \infty$ .证毕.

定义 5.3 对距离空间 $\langle X, d \rangle$ ，若有完备的距离空间 $\langle \tilde{X}, \rho \rangle$ ，使 X 等距于 $\tilde{X}$ 的稠密子集，即存在映射 $T: X \to \tilde{X}$ 使

$$
d (x, y) = \rho (T (x), T (y)), \quad \forall x, y \in X,
$$

且 $T(X)$ 是 $\tilde{X}$ 中稠密子集, 则称 $\tilde{X}$ 为 $X$ 的完备化.

定理 5.1 任何距离空间都存在完备化.

证将距离空间 $\langle X, d \rangle$ 中所有 Cauchy 序列的集合记作 $\tilde{X}$ . 对 $\tilde{X}$ 中元 $\xi = \{x_n\}$ 与 $\eta = \{y_n\}$ , 若

$$
\lim _ {n \rightarrow \infty} d (x _ {n}, y _ {n}) = 0,
$$

则称 $\xi$ 与 $\eta$ 相等，并记作 $\xi = \eta$ . 又对 $\tilde{X}$ 中任意两个元 $\xi = \{x_{n}\}, \eta = \{y_{n}\}$ ，定义

$$
\rho (\xi , \eta) = \lim _ {n \rightarrow \infty} d (x _ {n}, y _ {n}).
$$

因为 $\{x_{n}\},\{y_{n}\}$ 是 $X$ 中Cauchy序列，不难证明 $\{d(x_n,y_n)\}_{n = 1}^{\infty}$ 是Cauchy数列，所以上述极限是存在的.假设又有Cauchy序列 $\{x_n'\} ,\{y_n'\}$ ，使 $\xi = \{x_n'\} ,\eta =$ $\{y_n'\}$ ，则

$$
\lim _ {n \rightarrow \infty} d (x _ {n}, x _ {n} ^ {\prime}) = 0, \quad \lim _ {n \rightarrow \infty} d (y _ {n}, y _ {n} ^ {\prime}) = 0.
$$

利用距离公设(3)，

$$
d \left(x _ {n} ^ {\prime}, y _ {n} ^ {\prime}\right) \leqslant d \left(x _ {n} ^ {\prime}, x _ {n}\right) + d \left(x _ {n}, y _ {n}\right) + d \left(y _ {n}, y _ {n} ^ {\prime}\right).
$$

于是

$$
\lim _ {n \rightarrow \infty} d (x _ {n} ^ {\prime}, y _ {n} ^ {\prime}) \leqslant \lim _ {n \rightarrow \infty} d (x _ {n}, y _ {n}).
$$

类似地可有相反的不等式.总之

$$
\lim _ {n \rightarrow \infty} d \left(x _ {n} ^ {\prime}, y _ {n} ^ {\prime}\right) = \lim _ {n \rightarrow \infty} d \left(x _ {n}, y _ {n}\right).
$$

这说明 $\rho (\xi ,\eta)$ 不依赖于表示 $\pmb {\xi},\eta$ 的具体Cauchy序列.因而 $\rho (\cdot ,\cdot)$ 的定义是完善的.

显然 $\rho (\cdot ,\cdot)$ 满足距离公设中的(1)，(2)，设 $\xi = \{x_{n}\} ,\eta = \{y_{n}\} ,\zeta = \{z_{n}\} \in$

$\widetilde{X}$ ，则

$$
\begin{array}{r l} \rho (\xi , \zeta) & = \lim _ {n \to \infty} d (x _ {n}, z _ {n}) \\ & \leqslant \lim _ {n \to \infty} d (x _ {n}, y _ {n}) + \lim _ {n \to \infty} d (y _ {n}, z _ {n}) \\ & = \rho (\xi , \eta) + \rho (\eta , \zeta), \end{array}
$$

即 $\rho (\cdot ,\cdot)$ 也满足距离公设中的(3).总之， $\tilde{X}$ 按 $\rho (\cdot ,\cdot)$ 成为距离空间.

定义 $\langle X, d \rangle$ 到 $\langle \tilde{X}, \rho \rangle$ 的映射 $T$ 如下：

$$
T (x) = \tilde {x} = \{x, x, \dots , x, \dots \}, \text {当} x \in X.
$$

设 $y \in X$ ，则 $T(y) = \tilde{y} = \{y, y, \cdots, y, \cdots\}$ ，于是

$$
\rho (T (x), T (y)) = \lim _ {n \rightarrow \infty} d (x, y) = d (x, y).
$$

所以 $T: X \to \widetilde{X}$ 是一个等距映射. 往证 $T(X)$ 在 $\widetilde{X}$ 中稠密. 设 $\xi = \{x_{n}\} \in \widetilde{X}$ . 令 $\tilde{x}_{k} = \{x_{k}, x_{k}, \cdots, x_{k}, \cdots\}, k = 1, 2, \cdots$ , 则 $\tilde{x}_{k} = T(x_{k}) \in T(X)$ . 对任何 $\varepsilon > 0$ , 因为 $\{x_{n}\}_{n=1}^{\infty}$ 是 X 中 Cauchy 序列, 存在正整数 N, 使 $d(x_{n}, x_{m}) < \varepsilon$ , 当 $n, m \geqslant N$ . 于是

$$
\rho (\xi , \tilde {x} _ {k}) = \lim _ {n \to \infty} d (x _ {n}, x _ {k}) \leqslant \epsilon  , \text {当} k \geqslant N.
$$

可见 $T(X)$ 在 $\tilde{X}$ 中稠密.

最后，只须证明 $\widetilde{X}$ 是完备的. 设 $\{\xi_n\}_{n=1}^{\infty}$ 是 $\widetilde{X}$ 中 Cauchy 序列，由于 $T(X)$ 在 $\widetilde{X}$ 中稠密，对每个 $\xi_n$ ，必有 $x_n \in X$ ，使 $\tilde{x}_n = T(x_n) \in \widetilde{X}$ 且 $\rho(\tilde{x}_n, \xi_n) < 1/n$ ，于是

$$
\begin{array}{r l} d (x _ {n}, x _ {m}) & = \rho (\tilde {x} _ {n}, \tilde {x} _ {m}) \leqslant \rho (\tilde {x} _ {n}, \xi_ {n}) + \rho (\xi_ {n}, \xi_ {m}) + \rho (\xi_ {m}, \tilde {x} _ {m}) \\ & \leqslant 1 / n + \rho (\xi_ {n}, \xi_ {m}) + 1 / m. \end{array}
$$

由此可见 $\{x_{n}\}_{n = 1}^{\infty}$ 是 $X$ 中Cauchy序列，记 $\xi = \{x_{n}\}_{n = 1}^{\infty}$ ，则 $\xi \in \widetilde{X}$ . 而

$$
\rho (\xi_ {n}, \xi) \leqslant \rho (\xi_ {n}, \tilde {x} _ {n}) + \rho (\tilde {x} _ {n}, \xi) \leqslant 1 / n + \lim _ {k \rightarrow \infty} d (x _ {n}, x _ {k}) \rightarrow 0,
$$

当 $n \to \infty$ . 即 $\tilde{X}$ 是完备的. 证毕.

设想我们不把有理数集完备化,那么像 $x^{2}-2=0$ 这类方程就没有解.同样,如果不把某些函数空间完备化,那么许多数理方程也没有解.例如,对波动方程

$$
\left\{ \begin{array}{l} \Delta u - \frac {\partial^ {2} u}{\partial t ^ {2}} = F, \\ u (x, y, z, 0) = u _ {t} ^ {\prime} (x, y, z, 0) = 0, \\ \left. \frac {\partial u}{\partial n} \right| _ {s} = 0, \end{array} \right.\tag{5.1}
$$

这里 S 是空间区域 $\Omega$ 的边界. C. JI. Соболев 就考虑一串 $L^{2}(\Omega)$ 中函数 $F_{1}, F_{2}, \cdots, F_{k}, \cdots$ , 使

$$
\lim _ {k \rightarrow \infty} \iiint_ {\Omega} | F _ {k} - F | ^ {2} \mathrm{d} x \mathrm{d} y \mathrm{d} z = 0,
$$

若方程

$$
\left\{ \begin{array}{l} \Delta u - \frac {\partial^ {2} u}{\partial t ^ {2}} = F _ {k}, \\ u (x, y, z, 0) = u _ {t} ^ {\prime} (x, y, z, 0) = 0, \\ \left. \frac {\partial u}{\partial n} \right| _ {s} = 0 \end{array} \right.\tag{5.2}
$$

的寻常解 $u_{k}$ 存在，使得

$$
\lim _ {k \rightarrow \infty} \iiint_ {\Omega} | u _ {k} - u | ^ {2} \mathrm{d} x \mathrm{d} y \mathrm{d} z = 0,
$$

他就称 $u$ 是方程(5.1)的广义解. 而且他果然利用空间 $L^2(\Omega)$ 的完备性或 Riesz-Fisher 定理证出上述广义解的存在性.(参见[20], 第 XXII 讲)

## § 6 列紧性我们知道：

直线上每个有界的无穷点集都至少有一个聚点.

这是古典分析的基础. 推广到一般距离空间, 人们引进下列概念:

定义 6.1 距离空间 X 中的集合 M 称为列紧的, 如果 M 中任何序列都含有一个收敛的子序列(这个子序列的极限未必还在 M 中). 闭的列紧集称为自列紧集.

这是距离空间中非常重要的几何概念.

设 $M, N$ 都是距离空间 $\langle X, d \rangle$ 中的集合， $\varepsilon$ 为给定正数。如果对 $M$ 中任何一点 $x$ ，必存在 $N$ 中一点 $x'$ ，使 $d(x, x') < \varepsilon$ ，则称 $N$ 是 $M$ 的 $\varepsilon - \text{网}$ 。

定义 6.2 距离空间 X 中的集合 M 称为完全有界的, 如果对任给的 $\varepsilon > 0$ , 总存在由有限个元组成的 M 的 $\varepsilon - 网$ .

定理 6.1 在距离空间 X 中, 列紧性蕴含完全有界性. 若更设 X 是完备的, 则列紧性与完全有界性等价.

证设 $M$ 是 $X$ 中列紧集. 如果 $M$ 不是完全有界的, 则必存在某个 $\varepsilon_0 > 0$ , 使 $M$ 没有只包含有限个元素的 $\varepsilon_0 - \text{网}$ . 从而任取 $x_1 \in M$ , 必存在 $x_2 \in M$ , 使 $d(x_2, x_1) \geqslant \varepsilon_0$ , 否则, $\{x_1\}$ 就是 $M$ 之有限的 $\varepsilon_0 - \text{网}$ . 同理, 存在 $x_3 \in M$ , 使 $d(x_3, x_j) \geqslant \varepsilon_0, j = 1, 2$ . 这个步骤可以一直进行下去, 这样我们得到 $M$ 中一个序列 $\{x_n\}_{n=1}^{\infty}$ ; 使 $d(x_n, x_m) \geqslant \varepsilon_0$ , 当 $n \neq m$ . 显然 $\{x_n\}_{n=1}^{\infty}$ 没有收敛的子序列, 这与 $M$ 是列紧的矛盾.

若更设 $X$ 是完备的， $M$ 是 $X$ 中完全有界集， $\{x_{n}\}_{n=1}^{\infty}$ 是 $M$ 中任一序列。不失一般性，可假定 $\{x_{n}\}_{n=1}^{\infty}$ 有无穷多个元。取定一个正数列 $\{\varepsilon_{k}\}_{k=1}^{\infty}$ ，使 $\varepsilon_{k} \searrow 0$ 。由假设存在 $M$ 的 $\varepsilon_{1}$ -网只包含有限个元，于是存在 $X$ 中半径为 $\varepsilon_{1}$ 的球 $B_{1}$ ，它包含了 $\{x_{n}\}_{n = 1}^{\infty}$ 中无穷多个元. 记 $S_{1} = B_{1} \cap \{x_{n}\}_{n = 1}^{\infty}$ , 则 $S_{1}$ 是 $\{x_{n}\}_{n = 1}^{\infty}$ 的无穷子集. 又存在 $M$ 的 $\varepsilon_{2}$ -网只包含有限个元, 故存在 $X$ 中半径为 $\varepsilon_{2}$ 的球 $B_{2}$ , 包含 $S_{1}$ 中无穷多个元, 令 $S_{2} = B_{2} \cap S_{1}$ . 如此类推, 我们得到 $X$ 中一串球 $\{B_{k}\}_{k = 1}^{\infty}$ , 其半径分别为 $\varepsilon_{k}$ , 以及 $\{x_{n}\}_{n = 1}^{\infty}$ 的一串无穷子集 $\{S_{k}\}_{k = 1}^{\infty}$ , 满足

$$
S _ {k + 1} \subset S _ {k} \subset B _ {k}, k = 1, 2, \dots .
$$

于是我们可以依次选取

$$
x _ {n _ {1}} \in S _ {1}, x _ {n _ {2}} \in S _ {2} \setminus \left\{x _ {n _ {1}} \right\}, \dots , x _ {n _ {k}} \in S _ {k} \setminus \left\{x _ {n _ {1}}, x _ {n _ {2}}, \dots , x _ {n _ {k - 1}} \right\}, \dots .
$$

这样我们得到 $\{x_{n}\}_{n = 1}^{\infty}$ 的一个子序列 $\{x_{n_k}\}_{k = 1}^{\infty}$ ，根据构造， $x_{n_j} \in B_k$ 当 $j \geqslant k$ 。于是 $d(x_{n_k}, x_{n_j}) < 2\varepsilon_k$ ，当 $j > k$ 。

因 $\varepsilon_{k} \searrow 0$ ，所以 $\{x_{n_k}\}_{k=1}^{\infty}$ 是 Cauchy 序列。而 $X$ 是完备的，故 $\{x_{n_k}\}_{k=1}^{\infty}$ 收敛。证毕。

定理 6.2 在距离空间中,任何完全有界集都是可分的.

证设 M 是距离空间 $\langle X, d \rangle$ 的完全有界集. 则对任给的 $\varepsilon > 0$ , 可以取 M 的有限子集作为 M 的 $\varepsilon - 网$ . 事实上, 由假设存在 M 之有限的 $\frac{\varepsilon}{2} - 网$ , 记为 $\{y_{1}, \cdots, y_{j}\}$ . 任取 $x_{k} \in M \cap B\left(y_{k}, \frac{\varepsilon}{2}\right), k = 1, \cdots, j$ , 则 $\{x_{1}, \cdots, x_{j}\} \subset M$ . 易见它是 M 的 $\varepsilon - 网$ .

现在,对每个正整数 n, 设 $N_{n} \subset M$ 是 M 之有限的 $\frac{1}{n} -$ 网. 令

$$
N = \bigcup_ {n = 1} ^ {\infty} N _ {n},
$$

则 $N \subset M$ ，且是一个可数集。任给 $\varepsilon > 0, x \in M$ ，应有正整数 $n$ ，使 $\frac{1}{n} < \varepsilon$ ，及 $x_n \in N_n$ ，使

$$
d \left(x _ {n}, x\right) <   \frac {1}{n} <   \varepsilon ,
$$

可见 $N$ 在 $M$ 中稠密. 总之, $M$ 是可分的. 证毕.

定义 6.3 距离空间 X 中的集合 M 称为紧的, 如果 M 的任何开覆盖都存在有限的子覆盖.

定理 6.3 在距离空间中, 紧性与自列紧性等价.

证设 $M$ 是距离空间 $X$ 的紧子集, $\{x_{n}\}_{n=1}^{\infty}$ 是 $M$ 中任一序列. 如果 $\{x_{n}\}_{n=1}^{\infty}$ 不存在收敛于 $M$ 中某点的子序列, 则对每点 $\xi \in M$ , 必存在 $\delta_{\xi} > 0$ , 使 $B(\xi, \delta_{\xi})$ 不包含 $\{x_{n}\}_{n=1}^{\infty}$ 中异于 $\xi$ 的点. 否则, 存在某个 $\xi \in M$ , 在 $\xi$ 的任何邻域中都包含 $\{x_{n}\}_{n=1}^{\infty}$ 中异于 $\xi$ 的点, 这个 $\xi$ 便是 $\{x_{n}\}_{n=1}^{\infty}$ 中某个子序列的极限, 这与 $\{x_{n}\}_{n=1}^{\infty}$ 不存在收敛于 $M$ 中某点的子序列的假设矛盾. 显然 $B(\xi, \delta_{\xi})$ 的全体形成 $M$ 的一个开覆盖. 因 $M$ 是紧的, 必存在有限子覆盖. 设其为 $B(\xi_1, \delta_{\xi_1}), \cdots, B(\xi_k, \delta_{\xi_k})$ . 根据 $B(\xi_j, \delta_{\xi_j})$ 的选取, 每个最多只包含 $\{x_n\}_{n=1}^{\infty}$ 中一个点. 于是 $\{x_n\}_{n=1}^{\infty}$ 中只有有限个不同点, 必然至少有一个点重复出现无穷多次, 从而 $\{x_n\}_{n=1}^{\infty}$ 有收敛于 $M$ 中某点的子序列. 这和假设矛盾. 故 $M$ 必是自列紧的.

反之，设 $M$ 是自列紧的，由定理6.1及6.2， $M$ 是可分的，即 $M$ 中存在可数稠密子集 $M_0$ 。

设 $\{G_{a}\}_{a\in J}$ 是 $M$ 的一个开覆盖.任给 $x\in M$ ，必有某个 $G_{a}$ ，使 $x\in G_{a}$ .因 $G_{a}$ 是开集，存在 $\delta >0$ ，使 $B(x,\delta)\subset G_{a}$ .因 $M_0$ 是 $M$ 的稠密子集，故存在某个 $x^{\prime}\in M_0$ 及有理数 $r^{\prime} > 0$ ，使

$$
x \in B (x ^ {\prime}, r ^ {\prime}) \subset B (x, \delta) \subset G _ {a}.
$$

现在我们考虑以 $M_0$ 的元为心，正有理数为半径，而且包含于某个 $G_{\alpha}$ 内的球的全体，它们最多是可数个，记为 $B_{1}, B_{2}, \cdots$ 。根据构造它们形成了 $M$ 的一个开覆盖。我们断言， $\{B_{n}\}_{n=1}^{\infty}$ 中必有有限个覆盖了 $M$ 。若不然，对每个正整数 $n$ ，都存在点 $x_{n} \in M \setminus \left[\bigcup_{j=1}^{n} B_{j}\right]$ 。因 $M$ 是自列紧的， $\{x_{n}\}_{n=1}^{\infty}$ 存在一个子序列 $\{x_{n_{k}}\}_{k=1}^{\infty}$ 收敛于一点 $x_{0} \in M$ 。易证 $x_{0}$ 不属于任何 $B_{n}$ 。这与 $\{B_{n}\}_{n=1}^{\infty}$ 是 $M$ 的覆盖矛盾。故存在 $\{B_{n}\}_{n=1}^{\infty}$ 中有限个 $\{B_{1}, \cdots, B_{k}\}$ 覆盖了 $M$ 。由 $B_{n}$ 的构造应有 $G_{a_{j}}, a_{j} \in J$ ，使 $G_{a_{j}} \supset B_{j}, j = 1, \cdots, k$ 。于是 $\{G_{a_{1}}, \cdots, G_{a_{k}}\}$ 是 $\{G_{a}\}_{a \in J}$ 的有限子覆盖。证毕。

分析中常用到一种被称为对角线方法的技巧,它是证明紧性的典型方法.为便于今后使用,我们来详细地介绍这种方法.

设 $\{\alpha_{kn}\}_{n=1}^{\infty}(k=1,2,\cdots)$ 是一串有界数列. 则对每个 $k$ , 由于 $\{\alpha_{kn}\}_{n=1}^{\infty}$ 是有界数列, 必有一个收敛子序列 $\{\alpha_{kn_k(j)}\}_{j=1}^{\infty}$ . 一般说来, 对不同的 $k$ , $\{n_k(j)\}_{j=1}^{\infty}$ 是不同的正整数子序列. 对角线方法就是要对所有 $k$ , 找到一个共同的正整数列的子序列 $\{n(j)\}_{j=1}^{\infty}$ , 使得对每个 $k$ , $\{\alpha_{kn(j)}\}_{j=1}^{\infty}$ 都收敛. 具体做法如下:

把 $\left\{\alpha_{kn}\right\}_{n=1}^{\infty}, k=1,2,\cdots$ ，排成一个无穷方阵，第一个数列 $\left\{\alpha_{1n}\right\}_{n=1}^{\infty}$ 排在第一行，第二个数列 $\left\{\alpha_{2n}\right\}_{n=1}^{\infty}$ 排在第二行。依次类推，便有

$$
\begin{array}{c c c c c c} \alpha_ {1 1} & \alpha_ {1 2} & \alpha_ {1 3} & \dots & \alpha_ {1 n} & \dots \\ \alpha_ {2 1} & \alpha_ {2 2} & \alpha_ {2 3} & \dots & \alpha_ {2 n} & \dots \\ \alpha_ {3 1} & \alpha_ {3 2} & \alpha_ {3 3} & \dots & \alpha_ {3 n} & \dots \\ \vdots & \vdots & \vdots & & \vdots \\ \alpha_ {k 1} & \alpha_ {k 2} & \alpha_ {k 3} & \dots & \alpha_ {k n} & \dots \\ \vdots & \vdots & \vdots & & \vdots \end{array}
$$

先看第一行，由于 $\{\alpha_{1n}\}_{n = 1}^{\infty}$ 是有界数列，必有收敛子序列，记为 $\{\alpha_{1n_1(j)}\}_{j = 1}^{\infty}$ ，然后再看第二行的子序列 $\{\alpha_{2n_1(j)}\}_{j = 1}^{\infty}$ ，它也是有界的，必有收敛子序列，记为 $\{\alpha_{2n_2(j)}\}_{j = 1}^{\infty}$ . 再看第三行的子序列 $\{\alpha_{3n_2(j)}\}_{j = 1}^{\infty}$ ，它也是有界的，故有收敛子序列，记为 $\{\alpha_{3n_3(j)}\}_{j = 1}^{\infty}$ . 如此继续下去，便得到一串收敛数列排成的无穷方阵

$$
\begin{array}{c c c c c c} \alpha_ {1 n _ {1} (1)} & \alpha_ {1 n _ {1} (2)} & \alpha_ {1 n _ {1} (3)} & \dots & \alpha_ {1 n _ {1} (j)} & \dots \\ \alpha_ {2 n _ {2} (1)} & \alpha_ {2 n _ {2} (2)} & \alpha_ {2 n _ {2} (3)} & \dots & \alpha_ {2 n _ {2} (j)} & \dots \\ \alpha_ {3 n _ {3} (1)} & \alpha_ {3 n _ {3} (2)} & \alpha_ {3 n _ {3} (3)} & \dots & \alpha_ {3 n _ {3} (j)} & \dots \\ \vdots & \vdots & \vdots & & \vdots \\ \alpha_ {k n _ {k} (1)} & \alpha_ {k n _ {k} (2)} & \alpha_ {k n _ {k} (3)} & \dots & \alpha_ {k n _ {k} (j)} & \dots \\ \vdots & \vdots & \vdots & & \vdots \end{array}
$$

这个方阵中的每一行都是一个收敛的无穷数列.

对应地,我们得到这些数列的第二个指标排成的无穷方阵

$$
\begin{array}{c c c c c c} n _ {1} (1) & n _ {1} (2) & n _ {1} (3) & \dots & n _ {1} (j) & \dots \\ n _ {2} (1) & n _ {2} (2) & n _ {2} (3) & \dots & n _ {2} (j) & \dots \\ n _ {3} (1) & n _ {3} (2) & n _ {3} (3) & \dots & n _ {3} (j) & \dots \\ \vdots & \vdots & \vdots & & \vdots \\ n _ {k} (1) & n _ {k} (2) & n _ {k} (3) & \dots & n _ {k} (j) & \dots \\ \vdots & \vdots & \vdots & & \vdots \end{array}
$$

根据前面的选取,我们看到该方阵中下面一行的指标序列都是上面一行的指标序列的子序列,即 $\left\{n_{2}(j)\right\}_{j=1}^{\infty}$ 是 $\left\{n_{1}(j)\right\}_{j=1}^{\infty}$ 的子序列, $\left\{n_{3}(j)\right\}_{j=1}^{\infty}$ 是 $\left\{n_{2}(j)\right\}_{j=1}^{\infty}$ 的子序列等等.现在我们把上述无穷方阵中对角线上的元素取出来,得到一个指标序列 $\left\{n_{j}(j)\right\}_{j=1}^{\infty}$ ,这就是我们要找的正整数列的子序列,使对每个k, $\left\{\alpha_{kn_{j}(j)}\right\}_{j=1}^{\infty}$ 都收敛.事实上,对每个k,当 $j\geqslant k$ 以后, $\left\{n_{j}(j)\right\}_{j=1}^{\infty}$ 便是 $\left\{n_{k}(j)\right\}_{j=1}^{\infty}$ 的子序列,从而 $\left\{\alpha_{kn_{j}(j)}\right\}_{j=1}^{\infty}$ 是 $\left\{\alpha_{kn_{k}(j)}\right\}_{j=1}^{\infty}$ 的子序列.而 $\left\{\alpha_{kn_{k}(j)}\right\}_{j=1}^{\infty}$ 是收敛的,故 $\left\{\alpha_{kn_{j}(j)}\right\}_{j=1}^{\infty}$ 也是收敛的.

对于[0,1]上的一族连续函数 $\mathcal{F}$ , 把它看作是 $C[0,1]$ 空间中的一个点集, 这可以说是 $\mathcal{F}$ 的几何化. 自然对于 $\mathcal{F}$ 我们就要问

## (6.1) $\mathcal{F}$ 何时是列紧的？

如果 $\mathcal{F}$ 是列紧的, 则 $\mathcal{F}$ 是完全有界的, 当然便也一致有界, 即存在常数 $K > 0$ , 使

$$
| f (t) | \leqslant K, \text {对一切} t \in [ 0, 1 ] \text {和} f \in \mathcal {F}.
$$

任给 $\varepsilon>0, F$ 存在有限的 $\frac{\varepsilon}{3}-网: f_{1}, \cdots, f_{n}$ ，使对任给的 $f \in F$ 都有一个

$f_{k}(1 \leqslant k \leqslant n)$ 使得

$$
\rho (f, f _ {k}) <   \frac {\varepsilon}{3}.
$$

这里， $\rho(\cdot,\cdot)$ 是 C[0,1] 上的距离。注意 $f_{1}(t),\cdots,f_{n}(t)$ 都在 [0,1] 上一致连续，因此有 $\delta>0$ ，使

$|f_{k}(t'') - f_{k}(t')| < \frac{\epsilon}{3}$ ，对一切 $t', t'' \in [0,1]$ 且 $|t'' - t'| < \delta$ ，和 $1 \leqslant k \leqslant n$ .

于是对任给的 $f \in \mathcal{F}$ 有

$$
\begin{array}{r l} & {\mid f (t ^ {\prime \prime}) - f (t ^ {\prime}) \mid} \\ & {\leqslant \mid f (t ^ {\prime \prime}) - f _ {k} (t ^ {\prime \prime}) \mid + \mid f _ {k} (t ^ {\prime \prime}) - f _ {k} (t ^ {\prime}) \mid + \mid f _ {k} (t ^ {\prime}) - f (t ^ {\prime}) \mid} \\ & {\leqslant \rho (f, f _ {k}) + \mid f _ {k} (t ^ {\prime \prime}) - f _ {k} (t ^ {\prime}) \mid + \rho (f, f _ {k})} \\ & {<   \frac {\varepsilon}{3} + \frac {\varepsilon}{3} + \frac {\varepsilon}{3}} \\ & {= \varepsilon , \qquad \text {当} \mid t ^ {\prime \prime} - t ^ {\prime} \mid <   \delta .} \end{array}
$$

这导致下面的重要概念.

定义6.4 设 $\mathcal{F}$ 是一族从距离空间 $\langle X, d \rangle$ 到距离空间 $\langle Y, \rho \rangle$ 的函数. 如果任给 $\varepsilon > 0$ , 都存在 $\delta > 0$ , 使得对一切 $f \in \mathcal{F}$ 都有

$$
\rho (f (x), f (x ^ {\prime})) <   \varepsilon , \text {当} d (x, x ^ {\prime}) <   \delta ,
$$

则称 $\mathcal{F}$ 是同等连续的.

下面著名定理回答了前面所提问题(6.1).

定理 6.4 （Arzelá-Ascoli,1889） $F \subset C[0,1]$ 是列紧的必须且只须 F 是一致有界而且同等连续的.

证必要性已见于前面的分析,问题只在于充分性.

设 $\{f_n\}_{n=1}^{\infty}$ 是 $\mathcal{F}$ 中一个无穷序列. 因为 $C[0,1]$ 中元列 $\{f_n\}_{n=1}^{\infty}$ 收敛等价于 $\{f_n(t)\}_{n=1}^{\infty}$ 在 $[0,1]$ 上一致收敛. 故只须证明存在 $\{f_n(t)\}_{n=1}^{\infty}$ 的某个子序列 $\{f_{n_j}(t)\}_{j=1}^{\infty}$ 在 $[0,1]$ 上一致收敛.

将 $[0,1]$ 中全体有理数排成序列 $r_{1},r_{2},\cdots,r_{i},\cdots$ ，考察无穷方阵

$$
f _ {n} (r _ {i}), n, i = 1, 2, \dots .
$$

由假设,它们是一致有界的,根据对角线方法,有子序列 $\left\{f_{n_{j}(j)}(t)\right\}_{j=1}^{\infty}$ 在一切 $r_{i}(i=1,2,\cdots)$ 处收敛,简记这个子序列为 $\left\{f_{n(j)}(t)\right\}_{j=1}^{\infty}$ .

任给 $\varepsilon>0$ ，由 $\left\{f_{n(j)}(t)\right\}_{j=1}^{\infty}$ 的同等连续性，有 $\delta>0$ ，使对一切 $j=1,2,\cdots,$

$$
\mid f _ {n (j)} \left(t ^ {\prime \prime}\right) - f _ {n (j)} \left(t ^ {\prime}\right) \mid <   \frac {\epsilon}{3}, \text {当} \mid t ^ {\prime \prime} - t ^ {\prime} \mid <   \delta .
$$

显然我们可以找到有限个 $r_{i}, i=1,\cdots,I$ ，使

$$
[ 0, 1 ] \subset \bigcup_ {i = 1} ^ {l} (r _ {i} - \delta , r _ {i} + \delta).
$$

因为对每个 $r_{i}, \left\{f_{n(j)}(r_{i})\right\}_{j=1}^{\infty}$ 收敛. 于是存在 $N = N(\varepsilon)$ ，对每个 $i = 1, \cdots, I$ ，

$$
| f _ {n (j)} (r _ {i}) - f _ {n (k)} (r _ {i}) | <   \frac {\varepsilon}{3}, \text {当} j, k \geqslant N.
$$

对任何 $t \in [0,1]$ ，应有某个 $r_{i} (i=1,\cdots,I)$ 使 $|t - r_{i}| < \delta$ ，从而

$$
\begin{array}{r l} & {\mid f _ {n (j)} (t) - f _ {n (k)} (t) \mid} \\ & {\leqslant \mid f _ {n (j)} (t) - f _ {n (j)} (r _ {i}) \mid + \mid f _ {n (j)} (r _ {i}) - f _ {n (k)} (r _ {i}) \mid + \mid f _ {n (k)} (r _ {i}) - f _ {n (k)} (t) \mid} \\ & {<   \frac {\varepsilon}{3} + \frac {\varepsilon}{3} + \frac {\varepsilon}{3} = \varepsilon , \quad \text {当} j, k \geqslant N.} \end{array}
$$

这说明 $\{f_{n(j)}(t)\}_{j=1}^{\infty}$ 在 $[0,1]$ 上一致收敛. 证毕.

设 $M$ 是 $\mathbf{R}^n$ 中的紧子集，对在 $M$ 上连续的函数 $u, v$ 定义其距离为

$$
d (u, v) = \max _ {x \in M} | u (x) - v (x) |.
$$

则全体在 $M$ 上连续的函数按这个距离和逐点定义的线性运算形成一个距离线性空间，记为 $C(M)$ 。应该指出，上述定理对 $C(M)$ 也是成立的。

20 世纪之初(大约 1906 年), Fréchet 对抽象空间引进列紧性概念后, 很快就被 P. Montel 用于单复变函数论, 得到辉煌的成就, 即后来所谓的正常函数族理论. 以下且来介绍这理论中一个最初的但是具有代表性的结果.

引理 6.1 设 D 代表复平面上圆域 $\{z:|z|<3d\}(d>0)$ , $f_{n}(z)(n=1,2,\cdots)$ 是 D 内解析函数，且 $\{f_{n}(z)\}_{n=1}^{\infty}$ 在 D 上是一致有界的，则 $\{f_{n}(z)\}_{n=1}^{\infty}$ 在 $\{z:|z|\leqslant d\}$ 上是同等连续的.

证设 $|z_1| \leqslant d, |z_2| \leqslant d, \Gamma$ 代表圆周 $|z| = 2d$ . 根据 Cauchy 积分公式，

$$
\left| f _ {n} \left(z _ {1}\right) - f _ {n} \left(z _ {2}\right) \right| = \frac {1}{2 \pi} \left| \int_ {\Gamma} \frac {z _ {1} - z _ {2}}{\left(w - z _ {1}\right) \left(w - z _ {2}\right)} f _ {n} (w) d w \right|.
$$

由假设存在常数 K > 0，使

$$
| f _ {n} (z) | \leqslant K, \text {对所有} z \in D \text {与} n = 1, 2, \dots .
$$

注意 $\Gamma \subset D$ ，于是

$$
\mid f _ {n} (z _ {1}) - f _ {n} (z _ {2}) \mid \leqslant \frac {1}{2 \pi} \cdot \frac {K 4 \pi d}{d ^ {2}} \mid z _ {1} - z _ {2} \mid = \frac {2 K}{d} \mid z _ {1} - z _ {2} \mid .
$$

从而任给 $\varepsilon > 0$

$$
\mid f _ {n} (z _ {1}) - f _ {n} (z _ {2}) \mid <   \varepsilon , \text {当} \mid z _ {1} - z _ {2} \mid <   \frac {\varepsilon d}{2 K}.
$$

这里 $\frac{\varepsilon d}{2K}$ 与 $n$ 和 $z$ 无关，故 $\{f_n(z)\}_{n=1}^{\infty}$ 在 $\{z:|z|\leqslant d\}$ 上是同等连续的.证毕.

定理6.5(Montel定理,1907) 设 $\{f_n(z)\}_{n=1}^{\infty}$ 是区域 $\Omega$ 上一致有界的解析函数列, 则于任何完全位于 $\Omega$ 内的有界区域 $D$ (即 $D$ 的闭包 $\bar{D} \subset \Omega$ ), 恒有子序列 $\{f_{n_j}(z)\}_{j=1}^{\infty}$ 在 $D$ 上一致收敛.

证设 3d 表示从 D 到 $\Omega$ 的边界 $\partial\Omega$ 的距离，则 d>0 。根据 Heine-Borel 覆盖定理，有限多个以 d 为半径的小圆域 $K_{i}(i=1,\cdots,N)$ 完全覆盖了 $\overline{D}$ 。由引理 6.1， $\left\{f_{n}(z)\right\}_{n=1}^{\infty}$ 在 $\overline{K}_{1}$ 上是同等连续的。根据 Arzelá-Ascoli 定理， $\left\{f_{n}(z)\right\}_{n=1}^{\infty}$ 有子序列 $\left\{f_{n_{j}}(z)\right\}_{j=1}^{\infty}$ 按 $C(\overline{K}_{1})$ 中距离收敛，亦即 $\left\{f_{n_{j}}(z)\right\}_{j=1}^{\infty}$ 在 $\overline{K}_{1}$ 上一致收敛。注意再由引理 6.1， $\left\{f_{n_{j}}(z)\right\}_{j=1}^{\infty}$ 亦在 $\overline{K}_{2}$ 上是同等连续的。因此有子序列，不妨仍记作 $\left\{f_{n_{j}}(z)\right\}_{j=1}^{\infty}$ ，在 $\overline{K}_{2}$ 上，从而亦在 $\overline{K}_{1}\cup\overline{K}_{2}$ 上一致收敛。经过有限次抽子序列手续，便得到 $\left\{f_{n}(z)\right\}_{n=1}^{\infty}$ 的子序列 $\left\{f_{n_{j}}(z)\right\}_{j=1}^{\infty}$ 在 $\bigcup_{i=1}^{N}\overline{K}_{i}$ 上一致收敛，当然在 D 上一致收敛。证毕。

有人说：“在19世纪末及20世纪初，发现了分析的几何化的新运河——即函数被看成‘函数’空间中的点或向量”（见[14]，第2页）. Montel定理正是把 $\{f_n(z)\}_{n=1}^{\infty}$ 几何化以后，研究它的重要几何性质——列紧性而有的结果. 有了分析的几何化才能提出相应的几何问题，得到几何的结果，然后又自然地用到分析上去.

## § 7 赋范线性空间定义7.1 对复(或实)的线性空间 $X$ ，若有从 $X$ 到 $\mathbf{R}$ 的函数 $\| x\|$ ，使

(1) $\| x \| \geqslant 0, \| x \| = 0$ 当且仅当 $x = 0$ ;

(2) $\| \alpha x \| = |\alpha|\| x\|$ ;

(3) $\| x + y \| \leqslant \| x \| + \| y \|$

对任意的 $x, y \in X, \alpha \in \mathbf{C}$ (或 $\mathbf{R}$ ) 成立, 则称 $X$ 为复 (或实) 赋范线性空间, 记为 $\langle X, \| \cdot \| \rangle$ , 称 $\| x \|$ 为 $x$ 的范数.

例1 设 $\Omega$ 为 $\mathbf{R}^n$ 中的有界闭集, 令 $C(\Omega)$ 表示 $\Omega$ 上一切复值连续函数的集合. 定义

$$
(x + y) (t) = x (t) + y (t), \quad (\alpha x) (t) = \alpha x (t), \quad \text {当} t \in \Omega ,
$$

这里 $\alpha$ 是常数. 又以

$$
\| x \| = \max _ {t \in \Omega} | x (t) |
$$

作为范数. 容易证明 $C(\Omega)$ 是赋范线性空间.

例 2 设 $(\Omega, \mu)$ 是 $\sigma$ -有限测度空间，即 $\mu$ 是 $\Omega$ 上测度，而 $\Omega$ 可以表成 $\Omega = \bigcup_{n=1}^{\infty} E_n$ ，这里 $\mu(E_n) < \infty, n = 1, 2, \cdots$ . 对 $p \geqslant 1$ ，设

$$
L ^ {p} (\Omega , \mu) = \{x (t): \int_ {\Omega} | x (t) | ^ {p} d \mu (t) <   + \infty \}.
$$

以下有时将它简记为 $L^p$

根据 §3 中不等式(3.2)可见, $L^p$ 按逐点定义的加法和数乘形成一个线性空间. 注意这里几乎处处相等的函数视为 $L^p$ 中同一个元素.

对 $x(t)\in L^p$ ，定义

$$
\| x \| = \left[ \int_ {\Omega} | x (t) | ^ {p} d \mu (t) \right] ^ {1 / p}.
$$

容易验证如此定义的 $\| \cdot \|$ 满足范数公设(1)，(2)，利用Minkowski不等式可验证它也满足(3)，于是 $L^p$ 是一个赋范线性空间，容易看到，当 $\Omega = [a,b],\mu$ 是Lebesgue测度时， $L^p$ 就是§3中例6的 $L^p [a,b]$

例 3 在例 2 中, 特别取 $\Omega = \{1, 2, \cdots, n, \cdots\}$ , $\mu(n) = 1$ , $n = 1, 2, \cdots$ . 则

$$
L ^ {p} (\Omega , \mu) = \{x = \{\xi_ {n} \}: \sum_ {n = 1} ^ {\infty} | \xi_ {n} | ^ {p} <   + \infty \},
$$

相应的范数为

$$
\parallel x \parallel = (\sum_ {n = 1} ^ {\infty} | \xi_ {n} | ^ {p}) ^ {1 / p}, \text {当} x = \{\xi_ {n} \}.
$$

这种特殊的 $L^p (\Omega ,\mu)$ 也是赋范线性空间，一般记作 $\ell^p$ ，显然它和 §3 中例5的 $\ell^p$ 是同一个空间.

例4 假设 $1 \leqslant p < \infty$ . 对在单位圆盘 $D = \{z : |z| < 1\}$ 内解析的函数 $f$ 和 $0 \leqslant r < 1$ , 令

$$
m _ {p} [ f; r ] = \left[ \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} | f (r e ^ {i \theta}) | ^ {p} d \theta \right] ^ {1 / p}.
$$

设 $H^p$ 表示所有满足条件

$$
\sup _ {0 \leqslant r <   1} m _ {p} [ f; r ] <   \infty ,
$$

且在单位圆盘 $D$ 内解析的函数 $f$ 的集合. 逐点定义加法和数乘, 根据 Minkowski 不等式, 当 $f, g \in H^p$ , 则 $f + g \in H^p$ , 所以 $H^p$ 是线性空间. 又定义

$$
\parallel f \parallel = \sup _ {0 \leqslant r <   1} m _ {p} [ f; r ], \text {当} f \in H ^ {p}.
$$

易证它满足范数公设,从而 $H^{p}$ 是赋范线性空间.

例5 设 $H^{\infty}$ 是所有在单位圆盘 $D$ 内有界的解析函数的集合, 逐点定义加法和数乘运算, 又定义

$$
\| f \| = \sup _ {| z | <   1} | f (z) |,
$$

易见 $H^{\infty}$ 是赋范线性空间.

设 $A(\bar{D})$ 表示在 $D$ 内解析而且在 $\bar{D}$ 上连续的函数组成的集合. 按着 $H^{\infty}$ 的运算和范数, $A(\bar{D})$ 也是赋范线性空间, 它是 $H^{\infty}$ 中的线性流形. 根据解析函数的最大模原理和 $f$ 在 $\bar{D}$ 上连续，可知对每个 $f \in A(\bar{D})$ ，其范数也可表成

$$
\| f \| = \max _ {| z | = 1} | f (z) |.
$$

下面我们考察赋范线性空间的简单但是基本的性质.

首先,对赋范线性空间 $\langle X,\|\cdot\|\rangle$ ,总可用下面方式引进距离

$$
d (x, y) = \parallel x - y \parallel , \quad \text {当} x, y \in X.
$$

容易看出,如此定义的 $d(\cdot,\cdot)$ 满足距离公设, X 中加法和数乘按 $d(\cdot,\cdot)$ 确定的极限是连续的, 因此 X 也是距离线性空间. 于是赋范线性空间中序列的收敛就有意义, 它总是理解为按范数的收敛, 即 $\lim_{n\to\infty}x_n=x$ 指的是

$$
\parallel x _ {n} - x \parallel \rightarrow 0, \text {当} n \rightarrow \infty .
$$

常简记为 $x_{n}\rightarrow x$

命题7.1 在赋范线性空间 $X$ 中, 范数 $\| x\|$ 是 $x \in X$ 的连续函数.

证设 $\{x_{n}\}_{n = 1}^{\infty}$ 收敛于 $x$ .由

$$
\parallel x _ {n} \parallel \leqslant \parallel x _ {n} - x \parallel + \parallel x \parallel
$$

和

$$
\| x \| \leqslant \| x _ {n} - x \| + \| x _ {n} \|
$$

可知

$$
\mid \parallel x _ {n} \parallel - \parallel x \parallel \mid \leqslant \parallel x _ {n} - x \parallel .
$$

因为 $\| x_{n} - x\| \to 0$ ，故 $\| x_{n}\| \to \| x\|$ ，当 $n\to \infty$ .证毕.

定义7.2 设 $T$ 是从赋范线性空间 $\langle X, \| \cdot \|_1 \rangle$ 到赋范线性空间 $\langle Y, \| \cdot \|_2 \rangle$ 的函数(或映射)，如果对一切 $x, y \in X$ 和数 $\alpha, \beta$ 都有

$$
T (\alpha x + \beta y) = \alpha T x + \beta T y,
$$

则称 $T$ 为从 $X$ 到 $Y$ 的线性算子. 如果还存在常数 $C > 0$ , 使对一切 $x \in X$ 都有

$$
\| T x \| _ {2} \leqslant C \| x \| _ {1},
$$

则称 $T$ 是有界的. 如上的 $C$ 的下确界称为 $T$ 的范数, 记作 $\| T \|$ . 显然

$$
\| T \| = \sup _ {\| x \| _ {1} = 1} \| T x \| _ {2}.
$$

线性算子和一般函数不一样,它的性质要整齐得多.这表现在下面结果中.

定理7.1 设 $X, Y$ 都是赋范线性空间, $T$ 是从 $X$ 到 $Y$ 的线性算子. 则下述条件等价:

(1) T 在 X 中某点连续；

(2) $T$ 在 $X$ 中所有点连续；

(3) $T$ 是有界的.

证设 $X, Y$ 的范数分别为 $\| \cdot \|_1, \| \cdot \|_2$ .

(3) $\Rightarrow(2)$ . 因 T 有界, 存在常数 C>0, 使

$$
\parallel T x \parallel_ {2} \leqslant C \parallel x \parallel_ {1}, \quad \text {当} x \in X.
$$

任给 $x, x' \in X$ ，则 $x - x' \in X$ ，于是

$$
\| T x - T x ^ {\prime} \| _ {2} = \| T (x - x ^ {\prime}) \| _ {2} \leqslant C \| x - x ^ {\prime} \| _ {1},
$$

这表明 $T$ 在 $x^{\prime}$ 处连续.

(2) $\Rightarrow$ (1). 是显然的.

(1) $\Rightarrow (3)$ . 设 $T$ 在 $x_0 \in X$ 处连续. 于是存在 $\delta > 0$ , 使

$$
\parallel T x - T x _ {0} \parallel_ {2} \leqslant 1, \text {当} \parallel x - x _ {0} \parallel_ {1} \leqslant \delta .
$$

任给 $x \in X, x \neq 0$ ，记 $x_{1} = \frac{\delta}{\|x\|_{1}} x$ ，由

$$
\left\| \left(x _ {1} + x _ {0}\right) - x _ {0} \right\| _ {1} = \left\| x _ {1} \right\| _ {1} = \delta ,
$$

可知

$$
\parallel T x _ {1} \parallel_ {2} = \parallel T (x _ {1} + x _ {0}) - T x _ {0} \parallel_ {2} \leqslant 1.
$$

因 $x = \frac{\|x\|_1}{\delta} x_1$ ，故 $Tx = \frac{\|x\|_1}{\delta} Tx_1$ ，于是

$$
\| T x \| _ {2} = \frac {\| x \| _ {1}}{\delta} \| T x _ {1} \| _ {2} \leqslant \frac {\| x \| _ {1}}{\delta}.
$$

取 $C = \frac{1}{\delta}$ ，则

$$
\parallel T x \parallel_ {2} \leqslant C \parallel x \parallel_ {1}, \text {当} x \in X.
$$

即 $T$ 是有界的. 证毕.

设 $X, Y$ 都是赋范线性空间， $T$ 是从 $X$ 到 $Y$ 的有界线性算子。记

$$
R (T) \stackrel {\mathrm{d}} {=} \{y \in Y: \text {存在} x \in X, \text {使} y = T x \},
$$

称为 $T$ 的值域. 如果 $R(T) = Y$ , 称 $T$ 是满射的. 如果对任何的 $y \in R(T)$ , 只有唯一的 $x \in X$ , 使 $y = Tx$ , 称 $T$ 是单射的. 这时, 可以定义从 $R(T)$ 到 $X$ 中的算子:

$$
T ^ {- 1} y = x, \quad \text {当} y = T x.
$$

称 $T^{-1}$ 为 $T$ 的逆算子. 显然 $T^{-1}$ 也是线性算子, 但一般说来 $T^{-1}$ 未必是有界的.

如果 $T$ 既是单射, 又是满射的, 则 $T^{-1}$ 是从 $Y$ 到 $X$ 上的线性算子. 进一步, 如果 $T^{-1}$ 还是有界的, 称 $T$ 是有界可逆的.

例6 设 $f \in C[0,1]$ , 定义

$$
(T f) (x) = \int_ {0} ^ {x} f (t) \mathrm{d} t, \text {当} 0 \leqslant x \leqslant 1.
$$

易见 $T$ 是从 $C[0,1]$ 到 $C[0,1]$ 中的有界线性算子. 根据数学分析知识容易知道, $T$ 的值域为

$$
R (T) = \{g: g ^ {\prime} \in C [ 0, 1 ] \text {且} g (0) = 0 \},
$$

而且 $T$ 是单射的，当 $g \in R(T)$ ，

$$
(T ^ {- 1} g) (t) = g ^ {\prime} (t), \quad 0 \leqslant t \leqslant 1.
$$

这里 $g'$ 表示 g 的导函数.

定义 7.3 线性空间 X 上的复值函数 $f: X \to C$ ，称为线性泛函，如果对任意 $x, y \in X$ ，数 $\alpha, \beta$ 都有

$$
f (\alpha x + \beta y) = \alpha f (x) + \beta f (y).
$$

显然, 赋范线性空间上线性泛函是线性算子的特殊情形. 因此从定理 7.1 可知, 赋范线性空间上线性泛函是有界的当且仅当它是连续的.

引理 7.1 设 $x_{1}, \cdots, x_{n}$ 是赋范线性空间 X 中线性无关元素，则有 $\mu > 0$ ，使

$$
\left| \alpha_ {1} \right| + \dots + \left| \alpha_ {n} \right| \leqslant \mu \| \alpha_ {1} x _ {1} + \dots + \alpha_ {n} x _ {n} \|
$$

对任意的数 $\alpha_{1},\cdots,\alpha_{n}$ 成立.

证设

$$
r = \inf \left\{\| \alpha_ {1} x _ {1} + \dots + \alpha_ {n} x _ {n} \|: \sum_ {j = 1} ^ {n} | \alpha_ {j} | = 1 \right\}.
$$

往证 $r > 0$ .由下确界定义，有

$$
y _ {k} = \sum_ {j = 1} ^ {n} \alpha_ {j} ^ {(k)} x _ {j}, \sum_ {j = 1} ^ {n} | \alpha_ {j} ^ {(k)} | = 1, k = 1, 2, \dots ,
$$

使

$$
\parallel y _ {k} \parallel \rightarrow r, \text {当} k \rightarrow \infty .
$$

从 $|\alpha_j^{(k)}| \leqslant 1, k = 1, 2, \cdots, j = 1, \cdots, n$ ，可知存在 $\{k\}_{k=1}^{\infty}$ 的子序列 $\{k_m\}_{m=1}^{\infty}$ 使

$$
\alpha_ {j} ^ {(k _ {m})} \rightarrow \beta_ {j}, \quad \text {当} m \rightarrow \infty , j = 1, \dots , n,
$$

而且

$$
\mid \beta_ {1} \mid + \dots + \mid \beta_ {n} \mid = 1.
$$

当然 $x = \beta_{1}x_{1} + \cdots + \beta_{n}x_{n} \neq 0$ . 此外由

$$
\| y _ {k _ {m}} - x \| \leqslant \sum_ {j = 1} ^ {n} | \alpha_ {j} ^ {(k _ {m})} - \beta_ {j} | \| x _ {j} \|,
$$

可见 $y_{k_m} \to x$ ，从而 $\| y_{k_m} \| \to \| x \|$ ，当 $m \to \infty$ 。于是 $0 < \| x \| = r$ 。取 $\mu = \frac{1}{r}$ ，则由 $r$ 的定义，

$$
1 \leqslant \mu \parallel \alpha_ {1} x _ {1} + \dots + \alpha_ {n} x _ {n} \parallel , \text {当} | \alpha_ {1} | + \dots + | \alpha_ {n} | = 1.
$$

现在,对一般的不全为0的 $(\alpha_{1},\cdots,\alpha_{n})$ ,我们有

$$
1 \leqslant \mu \| \sum_ {k = 1} ^ {n} \frac {\alpha_ {k}}{\sum_ {j = 1} ^ {n} | \alpha_ {j} |} x _ {k} \|.
$$

由此立见引理成立.证毕.

命题 7.2 设 $\{e_{1},\cdots,e_{n}\}$ 是赋范线性空间 X 的基，则

$$
y _ {k} = \sum_ {j = 1} ^ {n} \alpha_ {j} ^ {(k)} e _ {j} \rightarrow y = \sum_ {j = 1} ^ {n} \alpha_ {j} e _ {j}
$$

必须且只须

$$
\lim _ {k \rightarrow \infty} \alpha_ {j} ^ {(k)} = \alpha_ {j}, j = 1, \dots , n.
$$

证易见

$$
y _ {k} - y = \sum_ {j = 1} ^ {n} \left(\alpha_ {j} ^ {(k)} - \alpha_ {j}\right) e _ {j}, k = 1, 2, \dots .
$$

由引理7.1, 存在正数 $\mu$ , 对所有 $k$ ,

$$
\sum_ {j = 1} ^ {n} \mid \alpha_ {j} ^ {(k)} - \alpha_ {j} \mid \leqslant \mu \parallel y _ {k} - y \parallel .
$$

由此可得必要性.

另外，

$$
\parallel y _ {k} - y \parallel \leqslant \sum_ {j = 1} ^ {n} \mid \alpha_ {j} ^ {(k)} - \alpha_ {j} \mid \parallel e _ {j} \parallel ,
$$

可见充分性也成立. 证毕.

由命题 7.2 可见,有限维赋范线性空间中点列收敛等价于按坐标收敛.

命题7.3 任何 $n$ 维实赋范线性空间必与 $\mathbf{R}^n$ 线性同构且同胚.

证设 X 是 n 维实赋范线性空间. $\{e_{1},\cdots,e_{n}\}$ 是 X 的一个基, 对每个 $x\in X$ , 有唯一表达式

$$
x = \xi_ {1} e _ {1} + \dots + \xi_ {n} e _ {n},
$$

这里 $\xi_{j}(j=1,\cdots,n)$ 都是实数. 故 $(\xi_{1},\cdots,\xi_{n})\in\mathbf{R}^{n}$ . 定义 X 到 $R^{n}$ 的映射 T:

$$
T x = (\xi_ {1}, \dots , \xi_ {n}), \text {当} x = \xi_ {1} e _ {1} + \dots + \xi_ {n} e _ {n}.
$$

易证 T 是线性的、双射(既是单射又是满射)，故 T 是同构映射.

根据引理7.1,存在 $\mu >0$ ，对一切 $(\xi_1,\dots ,\xi_n)\in \mathbf{R}^n$

$$
\sum_ {j = 1} ^ {n} | \xi_ {j} | \leqslant \mu \| \sum_ {j = 1} ^ {n} \xi_ {j} e _ {j} \|.
$$

于是对每个 $x = \sum_{j=1}^{n} \xi_j e_j \in X$ ,

$$
\begin{array}{r l} \parallel T x \parallel^ {2} & = \sum_ {j = 1} ^ {n} | \xi_ {j} | ^ {2} \leqslant (\sum_ {j = 1} ^ {n} | \xi_ {j} |) ^ {2} \\ & \leqslant \mu^ {2} \parallel \sum_ {j = 1} ^ {n} \xi_ {j} e _ {j} \parallel^ {2} = \mu^ {2} \parallel x \parallel^ {2}, \end{array}
$$

即 $\| Tx\| \leqslant \mu \| x\|$ .这说明 $T$ 是有界的，根据定理7.1， $T$ 是连续的.

另一方面，对任何 $(\xi_{1},\cdots,\xi_{n})\in\mathbf{R}^{n},x=\sum_{j=1}^{n}\xi_{j}e_{j}\in X$ ，且 $Tx=(\xi_{1},\cdots,\xi_{n})$ ，由 Hölder 不等式

$$
\| x \| \leqslant \sum_ {j = 1} ^ {n} | \xi_ {j} | \| e _ {j} \| \leqslant \left(\sum_ {j = 1} ^ {n} | \xi_ {j} | ^ {2}\right) ^ {1 / 2} \left(\sum_ {j = 1} ^ {n} \| e _ {j} \| ^ {2}\right) ^ {1 / 2} = \left(\sum_ {j = 1} ^ {n} \| e _ {j} \| ^ {2}\right) ^ {1 / 2} \| T x \|,
$$

这里 $(\sum_{j=1}^{n} \| e_j \|^2)^{1/2}$ 是与 $x$ 无关的常数. 这说明 $T$ 的逆映射 $T^{-1}$ 是有界的, 从而连续. 故 $X$ 与 $\mathbf{R}^n$ 同胚. 证毕.

命题 7.4 在有限维赋范线性空间中, Bolzano-Weierstrass 聚点原理成立.

证设 $\{e_{1},\cdots,e_{n}\}$ 是有限维赋范线性空间 X 的一个基， $y_{k}=\sum_{j=1}^{n}\alpha_{j}^{(k)}e_{j}\in X,\parallel y_{k}\parallel\leqslant M,k=1,2,\cdots$ ，这里 M 是正的常数.

根据引理7.1,存在正数 $\mu$ ，使

$$
\sum_ {j = 1} ^ {n} | \alpha_ {j} ^ {(k)} | \leqslant \mu \| \sum_ {j = 1} ^ {n} \alpha_ {j} ^ {(k)} e _ {j} \| = \mu \| y _ {k} \| \leqslant \mu M.
$$

显然可有 $\{k\}_{k=1}^{\infty}$ 的子序列 $\{k_{m}\}_{m=1}^{\infty}$ 使对每个 $j=1,\cdots,n,\lim_{m\to\infty}\alpha_{j}^{(k_{m})}=\beta_{j}$ 都存在.
由命题7.2，

$$
y _ {k _ {m}} \rightarrow \sum_ {j = 1} ^ {n} \beta_ {j} e _ {j} \in X, m \rightarrow \infty .
$$

证毕.

在无穷维的距离线性空间中,一般的线性流形未必是闭集,因此我们需要下面的概念.

定义 7.4 在距离线性空间中,闭的线性流形称为子空间.

定理7.2（Riesz引理，1918)设 $M$ 是赋范线性空间 $X$ 的子空间，且 $M \neq X$ ，则对任给的正数 $\varepsilon < 1$ ，都有 $x_{\varepsilon} \in X$ ，使 $\| x_{\varepsilon} \| = 1$ ，且

$$
\rho (x _ {\epsilon}, M) \stackrel {{\mathrm{d}}} {=} \inf _ {x \in M} \| x - x _ {\epsilon} \| \geqslant 1 - \varepsilon .
$$

证取定 $x_0 \in X \setminus M$ . 因为 $M$ 是闭的, $\rho(x_0, M) = d > 0$ . 对任给的正数 $\varepsilon < 1$ 与 $\eta$ , 由 $d$ 的定义, 存在 $y_0 \in M$ , 使

$$
d \leqslant \| x _ {0} - y _ {0} \| <   d + \eta .
$$

令

$$
x _ {\varepsilon} = \frac {x _ {0} - y _ {0}}{\| x _ {0} - y _ {0} \|},
$$

则 $x_{\varepsilon} \in X, \| x_{\varepsilon} \| = 1$ ，且对任何 $x \in M$ ，

$$
\begin{array}{r l} \parallel x - x _ {\epsilon} \parallel & = \parallel x - \frac {x _ {0} - y _ {0}}{\parallel x _ {0} - y _ {0} \parallel} \parallel \\ & = \frac {\parallel (\parallel x _ {0} - y _ {0} \parallel x + y _ {0}) - x _ {0} \parallel}{\parallel x _ {0} - y _ {0} \parallel} \end{array}
$$

$$
\geqslant \frac {d}{d + \eta}
$$

$$
\geqslant 1 - \varepsilon ,
$$

当 $\eta \leqslant d\varepsilon$ 时.证毕.

我们知道, 在有限维空间 $\mathbf{R}^n$ 中. 以原点为心的小球总是列紧的. 现在我们可以看到, 这是有限维空间所独有的特性. 因为根据 Riesz 引理, 对任何赋范线性空间 $X$ , 若小球 $B = \{x \in X: \| x \| < r\} (r > 0)$ 是列紧的, 则 $X$ 必是有限维的. (见习题 11)

在 §5 中, 我们已经着重指出空间完备性的重要意义. 因此有必要也很自然地要研究完备的赋范线性空间, 即现今通称的 Banach 空间. 这很早就出现在 S. Banach 的博士论文中 (1920 年). 虽然差不多同时, 还有另一些人也独立地提出了这个概念, 但是自从 S. Banach 的名著 Theorie des Operations Lineaires 1932 年出版以后, 人们鉴于 S. Banach 在这方面的全面而且重要的贡献, 便通称这类空间为 Banach 空间. 它在众多数学分支中经常出现, 无论从理论还是应用的角度来看, 它都是非常重要的.

## § 8\* F - 空间在20世纪40年代中期以前，泛函分析学家的兴趣几乎集中在赋范线性空间方面。但是后来发现许多重要的空间（主要来自广义函数论，例如L.Schwartz的 $\mathcal{S}$ 空间等）却不是赋范的。本节将要讲述一种比之赋范空间稍广的空间。

定义8.1 复(或实)线性空间 $X$ 上的函数 $\rho: X \to [0, +\infty)$ 若具有性质：

(1) $\forall x, y \in X, \rho(x + y) \leqslant \rho(x) + \rho(y)$ , (次可加性)

(2) $\forall \lambda \in \mathbf{C}$ (或 $\mathbf{R}$ ), $x \in X$ , $\rho(\lambda x) = |\lambda| \rho(x)$ , (正齐次性) 则称 $\rho$ 是 $X$ 上的一个半范数.

称这样的 $\rho$ 为半范数是因为从 $\rho(x) = 0$ 一般并不能导出 $x = 0$ .

定义8.2 设 $\{\rho_{\alpha}\}_{\alpha \in \mathcal{A}}$ 是线性空间 $X$ 上的一族半范数. 如果对所有的 $\alpha \in \mathcal{A}$ , $\rho_{\alpha}(x) = 0$ , 蕴含 $x = 0$ , 则称 $\{\rho_{\alpha}\}_{\alpha \in \mathcal{A}}$ 分离点. 易见这时对任何 $x_0 \neq 0$ , 必有某个 $\alpha_0 \in \mathcal{A}$ , 使 $\rho_{\alpha_0}(x_0) \neq 0$ .

设 $\{\rho_{a}\}_{a\in \mathcal{A}}$ 是线性空间 $X$ 上一族分离点的半范数.以形如

$$
N (\alpha_ {1}, \dots , \alpha_ {n}; \varepsilon) = \{x \in X: \rho_ {\alpha_ {i}} (x) <   \varepsilon_ {j}, j = 1, \dots , n \}
$$

的集合为0点的邻域基，其中 $\pmb {\varepsilon} = (\varepsilon_1,\dots ,\varepsilon_n),\varepsilon_j > 0,j = 1,\dots ,n.$ 以形如

$$
x _ {0} + N \left(a _ {1}, \dots , a _ {n}; \varepsilon\right) = \left\{x \in X: \rho_ {a _ {j}} \left(x - x _ {0}\right) <   \varepsilon_ {j}, j = 1, \dots , n \right\}
$$

的集合为 $x_0$ 点的邻域基，这样就由 $\{\rho_{a}\}_{a\in \mathcal{A}}$ 诱导出 $X$ 上一个拓扑，这个拓扑称为由半范数族 $\{\rho_{a}\}_{a\in \mathcal{A}}$ 生成的.

定理8.1 设线性空间 $X$ 上的拓扑是由分离点的可数多个半范数 $\{\rho_n\}_{n=1}^{\infty}$ 生成, 则 $X$ 是距离线性空间.

即在 $X$ 上能够赋以距离，使之成为距离线性空间，而且 $X$ 按这个距离产生的拓扑与 $X$ 上原来的拓扑即 $\{\rho_n\}_{n=1}^{\infty}$ 生成的拓扑是一致的.

证定义

$$
\rho (x, y) = \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} \frac {\rho_ {n} (x - y)}{1 + \rho_ {n} (x - y)}, x, y \in X.
$$

容易验证, $\rho (\cdot ,\cdot)$ 满足距离公设, 而且 $X$ 按 $\rho (\cdot ,\cdot)$ 是距离线性空间. 根据附录中定理3后面的注, 下面只须证明 $X$ 上按 $\rho (\cdot ,\cdot)$ 的距离拓扑与 $\{\rho_n\}_{n = 1}^{\infty}$ 生成的拓扑在 $X$ 中每点的邻域基等价.

设 $x_0 \in X, x_0 + N(n_1, \cdots, n_k; \varepsilon)$ 是 $\{\rho_n\}_{n=1}^{\infty}$ 生成的拓扑中 $x_0$ 的一个邻域，其中 $\varepsilon = (\varepsilon_1, \cdots, \varepsilon_k)$ . 令 $\varepsilon = \min \left\{\frac{2^{-n_1}\varepsilon_1}{1 + \varepsilon_1}, \cdots, \frac{2^{-n_k}\varepsilon_k}{1 + \varepsilon_k}\right\}$ , 则 $\varepsilon > 0$ . 而 $B(x_0, \varepsilon) = \{x \in X: \rho(x, x_0) < \varepsilon\}$ 就是距离拓扑中 $x_0$ 的一个邻域.

当 $x \in B(x_0, \varepsilon)$ 时， $\rho(x, x_0) < \varepsilon$

$$
\frac {1}{2 ^ {n _ {j}}} \frac {\rho_ {n _ {j}} (x - x _ {0})}{1 + \rho_ {n _ {j}} (x - x _ {0})} \leqslant \rho (x, x _ {0}) <   \varepsilon , j = 1, \dots , k,
$$

即

$$
\frac {\rho_ {n _ {j}} (x - x _ {0})}{1 + \rho_ {n _ {j}} (x - x _ {0})} <   2 ^ {n _ {j}} \varepsilon \leqslant \frac {\varepsilon_ {j}}{1 + \varepsilon_ {j}}, j = 1, \dots , k.
$$

由于函数 $f(t) = \frac{t}{1 + t}$ 在 $(0, +\infty)$ 上是单调增加的，因此

$$
\rho_ {n _ {j}} (x - x _ {0}) <   \varepsilon_ {j}, j = 1, \dots , k,
$$

所以 $x \in x_{0} + N(n_{1}, \cdots, n_{k}; \varepsilon)$ . 即

$$
B (x _ {0}, \varepsilon) \subset x _ {0} + N (n _ {1}, \dots , n _ {k}; \varepsilon).
$$

反之，设 $B(x_0, \eta)$ 是 $x_0$ 在距离拓扑中任一邻域，这里 $\eta > 0$ 。注意存在充分大正整数 $m$ ，使 $\sum_{n=m+1}^{\infty} \frac{1}{2^n} < \frac{\eta}{2}$ 。记 $\boldsymbol{\eta} = (\eta_1, \cdots, \eta_m)$ ，这里 $\eta_j = \frac{\eta}{4}, j = 1, \cdots, m$ 。则 $x_0 + N(1, \cdots, m; \boldsymbol{\eta})$ 是 $\{\rho_n\}_{n=1}^{\infty}$ 生成的拓扑中 $x_0$ 的一个邻域，当 $x \in x_0 + N(1, \cdots, m; \boldsymbol{\eta})$ 时，

$$
\rho_ {j} (x - x _ {0}) <   \eta_ {j}, j = 1, \dots , m.
$$

于是

$$
\begin{array}{r l} \rho (x, x _ {0}) & = \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} \frac {\rho_ {n} (x - x _ {0})}{1 + \rho_ {n} (x - x _ {0})} \\ & \leqslant \sum_ {n = 1} ^ {m} \frac {1}{2 ^ {n}} \rho_ {n} (x - x _ {0}) + \sum_ {n = m + 1} ^ {\infty} \frac {1}{2 ^ {n}} \\ & <   \sum_ {n = 1} ^ {m} \frac {1}{2 ^ {n}} \frac {\eta}{4} + \frac {\eta}{2} \\ & <   \eta . \end{array}
$$

可见 $x \in B(x_0, \eta)$ , 即

$$
x _ {0} + N (1, \dots , m; \eta) \subset B (x _ {0}, \eta).
$$

证毕.

定义 8.3 如果 X 是完备的距离线性空间, 则称 X 为 F-空间.

这个概念始见于文献[30]中.

例 1 设 $\Omega$ 是 $R^{n}$ 的开子集, X 是所有在 $\Omega$ 上连续的实值(或复值)函数的集合. 逐点定义加法和数乘, 易见 X 是一个线性空间. 对每个紧集 $K \subset \Omega$ , 定义

$$
\rho_ {K} (x) = \max _ {t \in K} | x (t) |, x \in X,
$$

容易验证这是 $X$ 上一个半范数. 半范数族 $\{\rho_K: K \subset \Omega$ 是紧集分离点, 生成了 $X$ 上一个拓扑, 当 $X$ 被赋予这个拓扑时得到的拓扑空间通常用 $\mathcal{C}(\Omega)$ 表示, 我们证明 $\mathcal{C}(\Omega)$ 便是 $F-$ 空间.

首先，设 $\{K_j\}_{j=1}^{\infty}$ 是 $\Omega$ 的紧子集序列，使

$$
\begin{array}{r l} & K _ {j} \subset \mathrm{int} (K _ {j + 1}), j = 1, 2, \dots , \\ & \bigcup_ {j = 1} ^ {\infty} \mathrm{int} (K _ {j}) = \Omega , \end{array}
$$

这里 $\operatorname{int}(K_j)$ 表示点集 $K_{j}$ 的内部，容易证明 $\Omega$ 的每个紧子集必含于某个 $K_{j}$ 中，于是 $\mathcal{C}(\Omega)$ 上由半范数族 $\{\rho_K: K \subset \Omega$ 是紧集 $\}$ 生成的拓扑与由半范数序列 $\{\rho_{K_j}\}_{j=1}^{\infty}$ 生成的拓扑相同. 而且半范数序列 $\{\rho_{K_j}\}_{j=1}^{\infty}$ 分离点，根据定理8.1, $\mathcal{C}(\Omega)$ 是一个距离线性空间.

其次，证明 $\mathcal{C}(\Omega)$ 是完备的. 设 $\{x_{n}\}_{n=1}^{\infty}$ 是 $\mathcal{C}(\Omega)$ 中 Cauchy 序列，根据定义， $\mathcal{C}(\Omega)$ 中序列 $\{x_{n}\}_{n=1}^{\infty}$ 收敛等价于 $\{x_{n}(t)\}_{n=1}^{\infty}$ 在 $\Omega$ 中每个紧子集上一致收敛. 于是对每个紧集 $K \subset \Omega$ 和 $\varepsilon > 0$ ，存在正整数 $N$ ，它只与 $K$ 及 $\varepsilon$ 有关，使

$$
| x _ {n} (t) - x _ {m} (t) | <   \varepsilon , \text {当} n, m \geqslant N, t \in K.
$$

由此可见，对每个 $t \in \Omega, \{x_n(t)\}_{n=1}^{\infty}$ 是Cauchy数列，因而收敛到某个数 $x(t)$ ，这样我们得到定义于 $\Omega$ 上的函数 $x(t)$ . 在上述不等式中，令 $m \to \infty$ ，可得

$$
| x _ {n} (t) - x (t) | \leqslant \varepsilon , \text {当} n \geqslant N, t \in K.
$$

这表明在 $K$ 上 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 一致收敛到 $x(t)$ ，故 $x(t)\in \mathcal{C}(\Omega)$ . 因为 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 在 $\Omega$ 的每个紧子集 $K$ 上一致收敛于 $x(t)$ ，故按 $\mathcal{C}(\Omega)$ 拓扑 $\{x_n\}_{n=1}^{\infty}$ 收敛于 $x$ 。总之， $\mathcal{C}(\Omega)$ 是完备的距离线性空间，即 $F-$ 空间。

例 2 为介绍空间 $\mathcal{C}^{m}(\Omega)$ ，需先引进某些记号。以后，我们总用 $N^{n}$ 表示 n 个非负整数的数表 $l=(l_{1},\cdots,l_{n})$ 的集合， $N^{n}$ 中每个元称为重指标。一个重指标 $l=(l_{1},\cdots,l_{n})$ 的阶 $|l|$ ，定义为 $|l|=l_{1}+\cdots+l_{n}$ 。设 f 是 n 个变量 $x_{1},\cdots,x_{n}$ 的函数，而且 f 至少有 $|l|$ 阶偏导数，我们记

$$
\partial^ {l} f = \frac {\partial^ {| l |} f}{\partial x _ {1} ^ {l _ {1}} \cdots \partial x _ {n} ^ {l _ {n}}}.
$$

另外,我们还采用记号

$$
x = \left(x _ {1}, \dots , x _ {n}\right), \quad x ^ {l} = x _ {1} ^ {l _ {1}} \dots x _ {n} ^ {l _ {n}}.
$$

现在，设 $\Omega$ 是 $\mathbf{R}^n$ 中开子集， $m$ 是正整数，考虑定义在 $\Omega$ 上，对任意 $l \in \mathbb{N}^n$ ， $|l| \leqslant m$ ，偏导数 $\partial^l f$ 在 $\Omega$ 上存在且连续的实值（或复值）函数 $f$ 的全体形成的线性空间 $X$ 。对每个紧子集 $K \subset \Omega$ 和每个重指标 $l \in \mathbb{N}^n$ ， $|l| \leqslant m$ ，定义

$$
\rho_ {K l} (f) = \sup _ {x \in K} | \partial^ {l} f (x) |, f \in X.
$$

容易验证， $\rho_{Kl}$ 是 $X$ 上一个半范数。由半范数族 $\{\rho_{Kl}: K \subset \Omega$ 是紧集， $l \in \mathbb{N}^n, |l| \leqslant m\}$ 生成 $X$ 上一个拓扑，这样得到的拓扑线性空间，用 $\mathcal{C}^m(\Omega)$ 表示。可以证明 $\mathcal{C}^m(\Omega)$ 是一个 $F-$ 空间。

像例 1 一样, 选取 $\Omega$ 中紧子集序列 $\{K_j\}_{j=1}^{\infty}$ , 则由半范数序列 $\{\rho_{K_j l}: j = 1, 2, \cdots, l \in \mathbb{N}^n, |l| \leqslant m\}$ 生成的拓扑与 $\mathcal{C}^m(\Omega)$ 上拓扑相同. 注意这个半范数序列分离点, 根据定理 8.1, $\mathcal{C}^m(\Omega)$ 是距离线性空间. 完备性的证明是繁琐的例行手续, 我们删去, 有兴趣的读者可参见 [31], 第 136 页.

例3 急减函数空间 $\mathcal{S}(\mathbf{R}^n)$ .

设 $X$ 表示 $\mathbf{R}^n$ 上所有满足如下条件的无穷次可微的复值函数 $f$ 的集合

$$
\sup _ {x \in \mathbb {R} ^ {n}} | x ^ {l} \partial^ {m} f (x) | <   \infty , \forall l, m \in \mathbf {N} ^ {n},
$$

按逐点定义的加法和数乘， $X$ 形成一个线性空间.对每个 $l,m\in \mathbf{N}^n$ ，定义

$$
\rho_ {l m} \left(f\right) = \sup _ {x \in \mathbb {R} ^ {n}} \mid x ^ {l} \partial^ {m} f (x) \mid , \text {当}   f \in X.
$$

容易验证 $\rho_{lm}$ 是 $X$ 上半范数. 半范数族 $\{\rho_{lm}: l, m \in \mathbb{N}^n\}$ 生成 $X$ 上拓扑, 所得到的拓扑线性空间称为急减函数空间, 记为 $\mathcal{S}(\mathbf{R}^n)$ . 可以证明它是一个 $F-$ 空间.

首先，半范数族 $\{\rho_{lm}: l, m \in \mathbf{N}^n\}$ 是可数的，易见它分离点，根据定理8.1，可见 $\mathcal{S}(\mathbf{R}^n)$ 是距离线性空间。下面只须证明它是完备的。

设 $\{f_k\}_{k=1}^{\infty}$ 是 $\mathcal{S}(\mathbf{R}^n)$ 中 Cauchy 序列, 于是按每个半范数 $\rho_{lm}$ , 它亦是 Cauchy 序列. 即对每个 $l, m \in \mathbf{N}^n$ , $\{x^l \partial^m f_k(x)\}_{k=1}^{\infty}$ 在 $\mathbf{R}^n$ 上一致收敛. 因为 $C(\mathbf{R}^n)$ 是完备的 (见习题 8), 故存在 $g_{lm} \in C(\mathbf{R}^n)$ , 使 $\{x^l \partial^m f_k(x)\}_{k=1}^{\infty}$ 在 $\mathbf{R}^n$ 上一致收敛于$g_{lm}(x), l, m \in \mathbf{N}^n$ . 如果我们能证明 $g = g_{00}$ 是无穷次可微的，而且 $g_{lm}(x) = x^l \partial^m g(x)$ ，那么实际上我们就证明了 $g \in \mathcal{S}(\mathbf{R}^n)$ ，而且按 $\mathcal{S}(\mathbf{R}^n)$ 拓扑， $\lim_{k \to \infty} f_k = g$ . 为了简便，我们只证明在 $n = 1$ 情形， $g$ 是一次连续可微的，而且 $g' = g_{01}$ ，对一般情形可以类似地证明.

我们知道

$$
f _ {k} (x) = f _ {k} (0) + \int_ {0} ^ {x} f _ {k} ^ {\prime} (t) \mathrm{d} t, k = 1, 2, \dots .
$$

因为在 $\mathbb{R}^1$ 上一致地有 $f_{k}\rightarrow g,f_{k}^{\prime}\rightarrow g_{01}$ ，当 $k\to \infty$ .于是在上式中令 $k\to \infty$ ，可得

$$
g (x) = g (0) + \int_ {0} ^ {x} g _ {0 1} (t) \mathrm{d} t,
$$

这表明 g 是连续可微的，且 $g' = g_{01}$ . 证毕.

例4 将 $[0,1]$ 上全体实值可测函数的集合记作 $S[0,1]$ , 两个几乎处处相等的函数相应于 $S[0,1]$ 中同一个元, 按逐点定义的加法和数乘, $S[0,1]$ 是一个线性空间. 定义

$$
d (x, y) = \int_ {0} ^ {1} {\frac {| x (t) - y (t) |}{1 + | x (t) - y (t) |}} \mathrm{d} t  , \text {当}   x, y \in S [ 0, 1 ].
$$

利用 §3 中不等式(3.1)容易证明 $d(\cdot, \cdot)$ 满足距离公设, $S[0,1]$ 按 $d(\cdot, \cdot)$ 成为距离线性空间.

现在我们来证明 $S[0,1]$ 中序列 $\{x_{n}\}_{n = 1}^{\infty}$ 收敛于 $x$ 等价于函数列 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 依测度收敛于 $x(t)$ .

设 $d(x_{n},x)\rightarrow 0$ ，当 $n\to \infty$ .对任给 $\varepsilon >0$ ，令

$$
E _ {n} (\varepsilon) = \{t \in [ 0, 1 ]: | x _ {n} (t) - x (t) | \geqslant \varepsilon \}.
$$

因为函数 $f(s) = \frac{s}{1 + s}$ 是 $(0, +\infty)$ 上单调递增函数，所以

$$
\begin{array}{r l} d (x _ {n}, x) & = \int_ {0} ^ {1} \frac {| x _ {n} (t) - x (t) |}{1 + | x _ {n} (t) - x (t) |} \mathrm{d} t \\ & \geqslant \int_ {E _ {n} (\epsilon)} \frac {| x _ {n} (t) - x (t) |}{1 + | x _ {n} (t) - x (t) |} \mathrm{d} t \\ & \geqslant \int_ {E _ {n} (\epsilon)} \frac {\varepsilon}{1 + \varepsilon} \mathrm{d} t \\ & \geqslant \frac {\varepsilon}{1 + \varepsilon} m (E _ {n} (\varepsilon)), \end{array}
$$

这里 $m(E_n(\varepsilon))$ 表示 $E_{n}(\varepsilon)$ 的Lebesgue测度.由此可见， $m(E_n(\varepsilon)) \to 0$ ，当 $n \to \infty$ .故 $\{x_{n}(t)\}_{n=1}^{\infty}$ 依测度收敛于 $x(t)$ .

反之，设 $\{x_{n}(t)\}_{n = 1}^{\infty}$ 依测度收敛于 $x(t)$ ，则 $\{x_{n}(t) - x(t)\}_{n = 1}^{\infty}$ 依测度收敛于0，而

$$
\frac {\mid x _ {n} (t) - x (t) \mid}{1 + \mid x _ {n} (t) - x (t) \mid} \leqslant 1, \quad n = 1, 2, \dots .
$$

根据Lebesgue收敛定理(参见[6],第五章,§5)

$$
d (x _ {n}, x) = \int_ {0} ^ {1} {\frac {| x _ {n} (t) - x (t) |}{1 + | x _ {n} (t) - x (t) |}} \mathrm{d} t \to 0, \text {当} n \to \infty .
$$

下面我们进一步证明 $S[0,1]$ 是完备的.

设 $\{x_{n}\}_{n = 1}^{\infty}$ 是 $S[0,1]$ 中Cauchy序列，则存在正整数 $n_k$ ，使

$$
d (x _ {n}, x _ {n _ {k}}) <   2 ^ {- k} \text {, 当} n \geqslant n _ {k}, k = 1, 2, \dots .
$$

不妨设 $n_{1}<n_{2}<\cdots<n_{k}<\cdots$ ，则

$$
\begin{array}{r l} & \sum_ {k = 1} ^ {\infty} \int_ {0} ^ {1} \frac {| x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) |}{1 + | x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) |} \mathrm{d} t \\ & = \sum_ {k = 1} ^ {\infty} d (x _ {n _ {k + 1}}, x _ {n _ {k}}) \\ & \leqslant \sum_ {k = 1} ^ {\infty} 2 ^ {- k} <   \infty . \end{array}
$$

令

$$
\alpha_ {k} (t) = \frac {\left| x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) \right|}{1 + \left| x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) \right|}, k = 1, 2, \dots .
$$

则

$$
\int_ {0} ^ {1} \left[ \sum_ {k = 1} ^ {\infty} \alpha_ {k} (t) \right] \mathrm{d} t = \sum_ {k = 1} ^ {\infty} \int_ {0} ^ {1} \alpha_ {k} (t) \mathrm{d} t <   \infty ,
$$

(参见[6], 第五章, §5, 定理 5). 故

$$
\sum_ {k = 1} ^ {\infty} \alpha_ {k} (t) <   \infty , \mathrm{a.e.} \text {于} [ 0, 1 ].
$$

对某个 $t \in [0,1]$ , 如果这个级数收敛, 则对充分大的 $k, \alpha_k(t) < \frac{1}{2}$ , 从而,

$$
\mid x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) \mid \leqslant 1.
$$

这样

$\mid x_{n_{k + 1}}(t) - x_{n_k}(t)\mid \leqslant 2\alpha_k(t)$ ，对充分大的 $k$

由此可见级数 $\sum_{k=1}^{\infty}|x_{n_{k+1}}(t) - x_{n_k}(t)|$ 在[0,1]上几乎处处收敛，从而级数

$$
x _ {n _ {1}} (t) + \sum_ {k = 1} ^ {\infty} \left[ x _ {n _ {k + 1}} (t) - x _ {n _ {k}} (t) \right]
$$

在 $[0,1]$ 上几乎处处收敛. 设其和函数为 $x_0(t)$ , 则

$$
x _ {n _ {k}} (t) = x _ {n _ {1}} (t) + \sum_ {j = 1} ^ {k - 1} [ x _ {n _ {j + 1}} (t) - x _ {n _ {j}} (t) ] \rightarrow x _ {0} (t), \mathrm{a.e.} \text {于} [ 0, 1 ].
$$

当然更有 $\{x_{n_k}(t)\}_{k=1}^{\infty}$ 依测度收敛于 $x_0(t)$ (参见[6], 第五章, §5, 定理1). 根据前段结论, $d(x_{n_k}, x_0) \to 0$ , 当 $k \to \infty$ . 进而可以证明, $d(x_n, x_0) \to 0$ , 当 $n \to \infty$ .

总之， $S[0,1]$ 是完备的距离线性空间，即 $F-$ 空间.

## § 9 压缩映象原理, Fréchet 导数关于多项式根的近似计算最显著的技巧或许就是逐次迭代法, 这个方法起源很早, 在许多方面都有应用. 首先将这个技巧应用于无穷维情形的似乎是 Liouville, 他还成功地利用这个技巧解常微分方程初值问题. 到 1922 年, Banach 把这方面结果抽象化, 用距离空间及压缩映射等概念更一般地描述这个方法, 这就是著名的 Banach 不动点定理或压缩映象原理, 以后发展成非线性泛函分析的重要内容之一. 这节我们简要介绍压缩映象原理以及它的某些应用.

定义 9.1 设 $\langle X, d \rangle$ 是距离空间, T 是从 X 到 X 中的映射, 如果存在常数 q > 0, 使对所有 $x, y \in X$ ,

$$
d (T x, T y) \leqslant q d (x, y),
$$

则称 T 满足 Lipschitz 条件, q 称为 T 的 Lipschitz 常数.

特别,如果 q<1,则 T 称为压缩映射.

设 $x \in X$ ，使 $Tx = x$ ，则 $x$ 称为映射 $T$ 的不动点.

定理9.1 设 $\langle X, d \rangle$ 是距离空间，映射 $T: X \to X$ 满足Lipschitz条件，则 $T$ 是连续的.

证设 $T$ 的Lipschitz常数为 $q$ . 任给 $x_0 \in X$ , 设 $V$ 是 $Tx_0$ 的任一邻域, 则有 $r > 0$ , 使 $B(Tx_0, r) \subset V$ . 注意 $B(x_0, r/q)$ 是 $x_0$ 的一个邻域, 当 $x \in B(x_0, r/q)$ 时,

$$
d (T x, T x _ {0}) \leqslant q d (x, x _ {0}) <   q (r / q) = r.
$$

即 $Tx \in B(Tx_0, r) \subset V$ . 所以 $T$ 在 $x_0$ 处连续，证毕.

定理 9.2(压缩映象原理,1922) 设 $\langle X,d\rangle$ 是完备距离空间, $T:X\to X$ 是压缩映射,则 T 在 X 中恰有一个不动点.设这个不动点为 $\bar{x}$ ,则对任何初始点 $x_{0}\in X$ ,逐次迭代点列 $x_{n+1}=Tx_{n},n=0,1,2,\cdots$ ,收敛于 $\bar{x}$ ,且关于收敛速度有如下的估计式:

$$
d \left(x _ {n}, \bar {x}\right) \leqslant q ^ {n} (1 - q) ^ {- 1} d \left(T x _ {0}, x _ {0}\right),
$$

这里 q 是 T 的 Lipschitz 常数.

证由 Lipschitz 条件, 对所有正整数 n,

$$
d \left(x _ {n + 1}, x _ {n}\right) = d \left(T x _ {n}, T x _ {n - 1}\right) \leqslant q d \left(x _ {n}, x _ {n - 1}\right).
$$

由此利用数学归纳法易证

$$
d \left(x _ {n + 1}, x _ {n}\right) \leqslant q ^ {n} d \left(T x _ {0}, x _ {0}\right), n = 1, 2, \dots .
$$

于是

(9.1)

$$
\begin{array}{r l} d (x _ {n + k}, x _ {n}) & \leqslant d (x _ {n + k}, x _ {n + k - 1}) + \dots + d (x _ {n + 1}, x _ {n}) \\ & \leqslant (q ^ {n + k - 1} + \dots + q ^ {n}) d (T x _ {0}, x _ {0}) \\ & \leqslant q ^ {n} (1 - q) ^ {- 1} d (T x _ {0}, x _ {0}). \end{array}
$$

因 $T$ 是压缩映射， $0 < q < 1$ ，可见 $\{x_{n}\}_{n=1}^{\infty}$ 是 Cauchy 序列。又 $X$ 是完备的，故 $\{x_{n}\}_{n=1}^{\infty}$ 必收敛到 $X$ 中某个元，设 $\lim_{n\to \infty}x_n = \bar{x}$ 。根据定理9.1， $T$ 是连续的，于是

$$
T \bar {x} = \lim _ {n \rightarrow \infty} T x _ {n} = \lim _ {n \rightarrow \infty} x _ {n + 1} = \bar {x},
$$

即 $\bar{x}$ 是 $T$ 的不动点. 假设 $\bar{y}$ 是 $T$ 的另一个不动点, 则

$$
d (\bar {x}, \bar {y}) = d (T \bar {x}, T \bar {y}) \leqslant q d (\bar {x}, \bar {y}).
$$

因 $q < 1$ ，故 $d(\bar{x},\bar{y}) = 0$ ，即 $\bar{x} = \bar{y}$

最后，在(9.1)式中，令 $k \to \infty$ ，可得

$$
d (\bar {x}, x _ {n}) \leqslant q ^ {n} (1 - q) ^ {- 1} d (T x _ {0}, x _ {0}).
$$

证毕.

压缩映象原理是非线性泛函分析的一个重要结果,它有许多应用.特别在微分方程、积分方程等解的存在唯一性定理的证明中,它是一个有力工具.

例1 常微分方程初值问题解的存在唯一性.

我们考虑常微分方程初值问题

$$
\left\{ \begin{array}{l} x ^ {\prime} (t) = f (t, x (t)), \\ x (t _ {0}) = x _ {0}. \end{array} \right.\tag{9.2}
$$

利用压缩映象原理我们可以证明解的存在唯一性定理.

定理9.3 (Picard,1893) 设 $f(t,x)$ 是带形

$$
\{(t, x): | t - t _ {0} | <   \delta , - \infty <   x <   \infty \}
$$

上二元连续函数，而且关于 $x$ 满足Lipschitz条件，即存在常数 $K > 0$ ，对任意 $t\in (t_0 - \delta ,t_0 + \delta),x,y\in (-\infty ,\infty)$ 都有

$$
\mid f (t, x) - f (t, y) \mid \leqslant K \mid x - y \mid .
$$

则初值问题(9.2)在区间 $[t_0 - \beta, t_0 + \beta]$ 上有唯一的连续解，这里 $0 < \beta < \min\{\delta, 1/K\}$ .

证设 $C[t_0 - \beta, t_0 + \beta]$ 表示区间 $[t_0 - \beta, t_0 + \beta]$ 上连续函数全体按距离

$$
d (x, y) = \max _ {t \in [ t _ {0} - \beta , t _ {0} + \beta ]} | x (t) - y (t) |
$$

所成的距离空间. 则 $C[t_0 - \beta, t_0 + \beta]$ 是完备的 (见习题8).

人们自然考察从 $C[t_{0}-\beta,t_{0}+\beta]$ 到自身的映射 T:

$$
(T x) (t) = x _ {0} + \int_ {t _ {0}} ^ {t} f (s, x (s)) \mathrm{d} s, x \in C [ t _ {0} - \beta , t _ {0} + \beta ].
$$

试在区间 $[t_0, t]$ 上积分(9.2)式，易见， $x = x(t), t \in [t_0 - \beta, t_0 + \beta]$ 是初值问题(9.2)的连续解当且仅当 $x(t) \in C[t_0 - \beta, t_0 + \beta]$ 是映射 $T$ 的不动点。由假设 $f(t, x)$ 关于 $x$ 满足Lipschitz条件，故

$$
\begin{array}{r l} | (T x) (t) - (T y) (t) | & = \left| \int_ {t _ {0}} ^ {t} [ f (s, x (s)) - f (s, y (s)) ] \mathrm{d} s \right| \\ & \leqslant \left| \int_ {t _ {0}} ^ {t} K | x (s) - y (s) | \mathrm{d} s \right| \\ & \leqslant K | t - t _ {0} | \max _ {t \in [ t _ {0} - \beta , t _ {0} + \beta ]} | x (t) - y (t) | \\ & \leqslant K \beta d (x, y), \end{array}
$$

当 $t_0 - \beta \leqslant t \leqslant t_0 + \beta$ . 令 $q = K\beta$ , 由 $\beta$ 的定义, $0 < q < 1$ , 于是

$$
d (T x, T y) = \max _ {t \in [ t _ {0} - \beta , t _ {0} + \beta ]} | T x (t) - T y (t) | \leqslant q d (x, y).
$$

这说明 $T$ 是一个压缩映射. 根据定理9.2, $T$ 有唯一的不动点, 故初值问题(9.2)在 $[t_0 - \beta, t_0 + \beta]$ 上有唯一解. 证毕.

例 2(隐函数存在定理) 设 $x^{0}=(x_{1}^{0},\cdots,x_{n}^{0})\in\mathbb{R}^{n},y^{0}=(y_{1}^{0},\cdots,y_{m}^{0})\in\mathbb{R}^{m},U\times V\subset\mathbb{R}^{n}\times\mathbb{R}^{m}$ 是 $(x^{0},y^{0})$ 的邻域， $f:U\times V\to\mathbb{R}^{m}$ 是连续函数，且 f 关于 $y=(y_{1},\cdots,y_{m})$ 的各个偏导数都在 $U\times V$ 上连续。如果

$$
\begin{array}{c} {f (x ^ {0}, y ^ {0}) = 0,} \\ {\det [ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) ] \neq 0,} \end{array}
$$

则存在 $x^0$ 的一个邻域 $U_0 \subset U$ 及唯一的连续函数 $\varphi: U_0 \to \mathbb{R}^m$ , 使

$$
\left\{ \begin{array}{l} f (x, \varphi (x)) = 0, x \in U _ {0}, \\ \varphi (x ^ {0}) = y ^ {0}. \end{array} \right.\tag{9.3}
$$

这里

$$
\frac {\partial f}{\partial y} \left(x ^ {0}, y ^ {0}\right) = \left( \begin{array}{c c c} \frac {\partial f _ {1}}{\partial y _ {1}} \left(x ^ {0}, y ^ {0}\right) & \dots & \frac {\partial f _ {1}}{\partial y _ {m}} \left(x ^ {0}, y ^ {0}\right) \\ \vdots & & \vdots \\ \frac {\partial f _ {m}}{\partial y _ {1}} \left(x ^ {0}, y ^ {0}\right) & \dots & \frac {\partial f _ {m}}{\partial y _ {m}} \left(x ^ {0}, y ^ {0}\right) \end{array} \right)
$$

是 $f(x^0, y)$ 作为 $y$ 的函数在 $y^0$ 处的 Jacobi 矩阵, $\operatorname{det}\left[\frac{\partial f}{\partial y}(x^0, y^0)\right]$ 表示它的行列式.

证为了书写简单,我们只就 $n = 2, m = 1$ 的情形给出证明. 这时 $\frac{\partial f}{\partial y}(x, y)$ 退化成一阶矩阵, 即实数. 由假设 $\frac{\partial f}{\partial y}(x, y)$ 的连续性及 $\operatorname{det}\left[\frac{\partial f}{\partial y}(x^0, y^0)\right] \neq 0$ , 可知存在 $\delta > 0$ , 使当 $x \in \overline{B(x^0, \delta)}, y \in \overline{B(y^0, \delta)}$ 时,

$$
\left| \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} \frac {\partial f}{\partial y} (x, y) - 1 \right| <   \frac {1}{2}.\tag{9.4}
$$

又因为 $f(x,y)$ 在 $U\times V$ 上连续及 $f(x^0,y^0) = 0$ ，故存在充分小的正数 $r < \delta$ 使当 $x\in \overline{B(x^0,r)}$ 时，

$$
\left| \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} f (x, y ^ {0}) \right| <   \frac {\delta}{2}.\tag{9.5}
$$

现在用 $C_{\mathbb{R}}(B(x^0,r))$ 表示 $\overline{B(x^0,r)}$ 上全体实值连续函数的Banach空间，其范数用 $\| \cdot \|$ 表示.令

$$
X = \{\varphi \in C _ {\mathbf {R}} (\overline {{{B (x ^ {0} , r)}}}): \varphi (x ^ {0}) = y ^ {0}, \| \varphi - y ^ {0} \| \leqslant \delta \},
$$

则 $X$ 是 $C_{\mathbb{R}}(\overline{B(x^0,r)})$ 的闭子集，因而是完备距离空间. $X$ 上的距离定义为

$$
d (\varphi , \psi) = \| \varphi - \psi \|, \text {当} \varphi , \psi \in X.
$$

定义 $X$ 上的映射 $T$ :

$$
(T \varphi) (x) = \varphi (x) - \left[ \frac {\partial f}{\partial y} \left(x ^ {0}, y ^ {0}\right) \right] ^ {- 1} f (x, \varphi (x)), \varphi \in X, x \in \overline {{{B \left(x ^ {0} , r\right)}}}.
$$

显然 $T\varphi \in C_{\mathbb{R}}(\overline{B(x^0,r)})$ ，又由 $\varphi (x^0) = y^0,f(x^0,y^0) = 0$ ，可见

$$
(T \varphi) (x ^ {0}) = \varphi (x ^ {0}) - \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} f (x ^ {0}, \varphi (x ^ {0})) = y ^ {0}.
$$

若 $\varphi, \psi \in X$ ，则根据微分中值定理

$$
\begin{array}{l} (T \varphi) (x) - (T \psi) (x) \\ = \varphi (x) - \psi (x) - \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} [ f (x, \varphi (x)) - f (x, \psi (x)) ] \\ = \varphi (x) - \psi (x) - \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} \frac {\partial f}{\partial y} (x, [ 1 - \theta (x) ] \varphi (x) + \\ \theta (x) \psi (x)) ] [ \varphi (x) - \psi (x) ] \\ = \left(1 - \left[ \frac {\partial f}{\partial y} (x ^ {0}, y ^ {0}) \right] ^ {- 1} \frac {\partial f}{\partial y} (x, [ 1 - \theta (x) ] \varphi (x) + \theta (x) \psi (x))\right) \\ [ \varphi (x) - \psi (x) ], \end{array}
$$

这里 $0 < \theta(x) < 1$ ，注意 $x \in \overline{B(x^0, r)} \subset \overline{B(x^0, \delta)}$ ，且

$$
\left| (1 - \theta (x)) \varphi (x) + \theta (x) \psi (x) - y ^ {0} \right| <   \delta ,
$$

于是根据(9.4)可得

$$
\| T \varphi - T \psi \| = \max _ {x \in B (x ^ {0}, r)} | (T \varphi) (x) - (T \psi) (x) |
$$

$$
\begin{array}{l} \leqslant \frac {1}{2} \underset {x \in B (x ^ {0}, r)} {\max} | \varphi (x) - \psi (x) | \\ = \frac {1}{2} \| \varphi - \psi \|. \end{array}\tag{9.6}
$$

又常值函数 $y^0 \in X$ ，而且

$$
\left(T y ^ {0}\right) (x) = y ^ {0} - \left[ \frac {\partial f}{\partial y} \left(x ^ {0}, y ^ {0}\right) \right] ^ {- 1} f (x, y ^ {0}).
$$

根据(9.5)

$$
\| T y ^ {0} - y ^ {0} \| = \max _ {x \in B (x ^ {0}, r)} \left| \left[ \frac {\partial f}{\partial y} \left(x ^ {0}, y ^ {0}\right) \right] ^ {- 1} f (x, y ^ {0}) \right| <   \delta / 2.
$$

于是，当 $\varphi \in X$ ，由(9.6)可得

$$
\begin{array}{r l} \| T \varphi - y ^ {0} \| & \leqslant \| T \varphi - T y ^ {0} \| + \| T y ^ {0} - y ^ {0} \| \\ & \leqslant \frac {1}{2} \| \varphi - y ^ {0} \| + \delta / 2 \leqslant \delta , \end{array}
$$

可见 $T\varphi \in X$ .再由(9.6)可见 $T$ 是 $X$ 上压缩映射.根据定理9.2， $T$ 在 $X$ 上有唯一的不动点，从而存在 $\overline{B(x^0,r)}$ 上唯一的连续函数 $\varphi$ 满足(9.3).证毕.

人们自然会问, 对于一般 Banach 空间上一个非线性映射, 类似例 2 的研究是否可能? 显然, 首先是要对无穷维空间引进类似于 Jacobi 矩阵的概念. 下面我们介绍著名的 Fréchet 导数, 它在非线性分析中起着重要的作用.

定义9.2 设 $X, Y$ 都是Banach空间， $\Omega$ 是 $X$ 的开子集， $A: \Omega \to Y$ 是一个映射， $x \in \Omega$ 。如果存在一个从 $X$ 到 $Y$ 的有界线性算子 $L$ ，使

$$
\lim _ {\| h \| \rightarrow 0} \frac {\| A (x + h) - A x - L h \|}{\| h \|} = 0,
$$

则称 $A$ 在点 $x$ 处 Fréchet 可微, 易见当 $A$ 在 $x$ 处 Fréchet 可微时, 使上述极限成立的算子 $L$ 是唯一的. 这个算子 $L$ 称为 $A$ 在 $x$ 处的 Fréchet 导数, 通常记为 $A'(x)$ .

有人说得好：“由于 $A'(x)$ 定义成映象的线性主部，所以正好反映了将非线性问题线性化。它是应用得最多的一种微分概念。”（参见[15]，第26页）

例3 任何有界线性算子 $T: X \to Y$ 在任意点的 Fréchet 导数都是 $T$ 本身. 这点从恒等式

$$
T (x + h) - T x - T h = 0, \forall x, h \in X,
$$

立刻得出.

例4 设 $\Omega$ 是 $\mathbf{R}^n$ 的开子集, $\varphi: \Omega \to \mathbf{R}^n$ 具有连续的各个偏导数, 将 $\mathbf{R}^n$ 中的点表成列向量, 即

$$
x = \left( \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right), \quad \varphi (x) = \left( \begin{array}{c} \varphi_ {1} (\boldsymbol {x}) \\ \vdots \\ \varphi_ {n} (\boldsymbol {x}) \end{array} \right)
$$

如果 $h = \begin{pmatrix} h_1 \\ \vdots \\ h_n \end{pmatrix}$ 的范数充分小，根据微分中值定理

$$
\varphi_ {j} (x + h) - \varphi_ {j} (x) = \frac {\partial \varphi_ {j}}{\partial x _ {1}} (x) h _ {1} + \dots + \frac {\partial \varphi_ {j}}{\partial x _ {n}} (x) h _ {n} + o (\| h \|), j = 1, \dots , n.
$$

即

(9.7)

这里

$$
\varphi (x + h) - \varphi (x) = A h + o (\| h \|),
$$

$$
A = \left( \begin{array}{c c c} \frac {\partial \varphi_ {1}}{\partial x _ {1}} (x) & \dots & \frac {\partial \varphi_ {1}}{\partial x _ {n}} (\boldsymbol {x}) \\ \vdots & & \vdots \\ \frac {\partial \varphi_ {n}}{\partial x _ {1}} (x) & \dots & \frac {\partial \varphi_ {n}}{\partial x _ {n}} (\boldsymbol {x}) \end{array} \right).
$$

从(9.7)式可见 $\varphi(x)$ 在 $x$ 处的 Fréchet 导数 $\varphi'(x)$ 正是经典的 Jacobi 矩阵 $A$ .

有了 Fréchet 导数的概念, 就可以类似于例 2 建立 Banach 空间上隐函数存在定理. 关于这个定理及其证明可参见 [19], 第 383—384 页.

## 习题

1. 试证明: 在线性空间中, 对任意向量 $x$ , 及数 $\alpha$ 都有

$$
\begin{array}{c} 0 x = \theta , \\ (- 1) x = - x, \\ \alpha \theta = \theta . \end{array}
$$

2. 试证明下述消去律在线性空间中成立：

$$
\begin{array}{r l} & {x + y = x + z \Rightarrow y = z  ,} \\ & {\alpha x = \alpha y \text {且} \alpha \neq 0 \Rightarrow x = y  ,} \\ & {\alpha x = \beta x \text {且} x \neq \theta \Rightarrow \alpha = \beta .} \end{array}
$$

3. 试证明: 在空间 (s) 中, 如果 $\{x_{n}\}_{n=1}^{\infty}$ 按坐标收敛于 $x_{0}$ , 则 $\{x_{n}\}_{n=1}^{\infty}$ 按距离收敛于 $x_{0}$ .

4. 证明: 空间 $(c)$ 是可分的.

5. 设 $\{x_{n}\}_{n=1}^{\infty}, \{y_{n}\}_{n=1}^{\infty}$ 是距离空间 $\langle X, d \rangle$ 中两个 Cauchy 序列，试证明 $\{d(x_{n}, y_{n})\}_{n=1}^{\infty}$ 是 Cauchy 数列.

6. 距离空间 $X$ 中的点集 $S$ 称为有界的, 如果存在 $X$ 中某个球 $B(x_0, r)$ , 使 $B(x_0, r) \supset S$ .

试证明:距离空间中任何 Cauchy 序列都是有界的.

7. 设 $\langle X, d \rangle$ 是距离空间, $A$ 是 $X$ 中的一个给定的子集. 定义

$$
\mathrm{dist} (x, A) \stackrel {\mathrm{d}} {=} \inf \{d (x, y): y \in A \}, \text {当} x \in X.
$$

称之为 x 与 A 的距离.

证明: $\mathrm{dist}(x,A)$ 是 x 的连续函数.

8. 设 $S$ 是 $\mathbf{R}^n$ 的子集, $C(S)$ 表示 $S$ 上有界连续函数全体按逐点定义的加法和数乘形成的线性空间. 对 $f, g \in C(S)$ , 定义距离为

$$
d (f, g) = \sup _ {x \in S} | f (x) - g (x) |.
$$

试证明： $C(S)$ 是完备的距离线性空间.

9. 证明: $l^p (1 \leqslant p \leqslant \infty)$ 是完备的距离空间.

10. 设 $X$ 是赋范线性空间, $A$ 是 $X$ 中有界的集合. 试证明: $A$ 是完全有界集当且仅当对任何 $\varepsilon > 0$ , 存在 $X$ 的有限维子空间 $M$ , 使 $A$ 中每个点与 $M$ 的距离都小于 $\varepsilon$ .

11. 设 $\langle X, \| \cdot \| \rangle$ 是赋范线性空间， $r > 0$ . 如果球 $B = \{x \in X : \| x \| < r\}$ 是列紧的，则 $X$ 必是有限维的. 试利用 Riesz 引理(定理 7.2)证明之.

提示假如 X 不是有限维的. 不妨设 r > 1. 如果我们已经找到 n 个向量 $\{x_{j}\}_{j=1}^{n} \subset B$ ，使 $\|x_{j} - x_{k}\| > \frac{1}{2}$ ，当 $j \neq k$ . 令 $M = S_{p} \{x_{1}, \cdots, x_{n}\}$ ，则 M 是 X 的有限维子空间，故 $M \neq X$ . 由 Riesz 引理，存在 $x_{n+1} \in X, \|x_{n+1}\| = 1$ ，使 $\|x_{n+1} - x_{j}\| > \frac{1}{2}, j = 1, \cdots, n$ . 根据数学归纳法，存在 $\{x_{j}\}_{j=1}^{\infty} \subset B$ ，使 $\|x_{j} - x_{k}\| > \frac{1}{2}$ ，当 $j \neq k$ ，这与 B 是列紧的矛盾.

12. 证明: $n$ 维欧氏空间 $\mathbf{R}^n$ 是 Banach 空间. 这里 $\mathbf{R}^n$ 表示 $n$ 个实数组成的有序数组 $(\xi_1, \cdots, \xi_n)$ 的全体按如下定义的加法、数乘和范数形成的赋范线性空间

$$
\begin{array}{r l} x + y & = \left(\xi_ {1} + \eta_ {1}, \dots , \xi_ {n} + \eta_ {n}\right), \\ \alpha x & = \left(\alpha \xi_ {1}, \dots , \alpha \xi_ {n}\right), \end{array}
$$

$$
\| x \| = \left(\sum_ {j = 1} ^ {n} | \xi_ {j} | ^ {2}\right) ^ {1 / 2},
$$

对 $x=(\xi_{1},\cdots,\xi_{n}),y=(\eta_{1},\cdots,\eta_{n})\in\mathbf{R}^{n},\alpha\in\mathbf{R}.$

13. 如果在 $\mathbf{R}^n$ 中定义

$$
\rho (x, y) = \max _ {1 \leqslant j \leqslant n} | \xi_ {j} - \eta_ {j} |,
$$

当 $x=(\xi_{1},\cdots,\xi_{n}),y=(\eta_{1},\cdots,\eta_{n})\in\mathbf{R}^{n}$

试证明： $R^{n}$ 按距离 $\rho(\cdot,\cdot)$ 也是完备的距离线性空间.

14. 设 $\langle X, d \rangle$ 是完备的距离空间, $E$ 是 $X$ 的闭子集, 试证明 $\langle E, d \rangle$ 也是完备的距离空间.

15. 证明: $l^p (1 \leqslant p < \infty)$ 中子集 $S$ 是列紧的充要条件是

(i) 存在常数 $M > 0$ ，使对一切 $x = \{\xi_n\}_{n=1}^{\infty} \in S$ ，都有 $\sum_{n=1}^{\infty} |\xi_n|^p \leqslant M$ .

(ii) 任给 $\varepsilon > 0$ , 存在正整数 $N$ , 使当 $k \geqslant N$ , 对一切 $x = \{\xi_n\}_{n=1}^{\infty} \in S$ 有 $\sum_{n=k}^{\infty} |\xi_n|^p \leqslant \varepsilon$ .

16. 试证明: 空间(s)中子集 S 是列紧的充要条件是对每个正整数 n, 存在常数 $M_{n}>0$ , 使当 $x=\left\{\xi_{n}\right\}_{n=1}^{\infty}\in S$ , 便有 $\left|\xi_{n}\right|\leqslant M_{n}, n=1,2,\cdots$ .

17. 设 $M[a, b]$ 是区间 $[a, b]$ 上有界函数全体按逐点定义的加法和数乘形成的线性空间. 当 $x = x(t) \in M[a, b]$ , 定义范数

$$
\| x \| = \sup _ {a \leqslant t \leqslant b} | x (t) |.
$$

证明:按这个范数 $M[a,b]$ 是 Banach 空间.

18. 设 $V[a, b]$ 表示在区间 $[a, b]$ 上右连续的有界变差函数全体，按逐点定义的加法和数乘形成的线性空间，定义范数为

$\| x \| = |x(a)| + V_a^b(x)$ , 当 $x = x(t) \in V[a, b]$ ,

这里 $\mathrm{V}_a^b (x)$ 表示函数 $x(t)$ 在 $[a,b]$ 上的全变差.

试证明： $V[a,b]$ 按此范数是Banach空间.

19. 举例说明, 在一般的距离空间中, 完全有界集不一定是列紧的.

20. 设 $\{x_{n}\}_{n=1}^{\infty}$ 是距离空间 $X$ 中的 Cauchy 序列, 如果 $\{x_{n}\}_{n=1}^{\infty}$ 有子序列 $\{x_{n_{k}}\}_{k=1}^{\infty}$ 收敛于 $x$ , 则 $\{x_{n}\}_{n=1}^{\infty}$ 也收敛于 $x$ .

21. 设 $f$ 是从距离空间 $X$ 到距离空间 $Y$ 的函数, 则 $f$ 是连续的当且仅当对 $Y$ 中任意闭集 $F, f^{-1}(F)$ 是 $X$ 中闭集.

22. 设 X 是 n 维复线性空间, $\{e_{1}, \cdots, e_{n}\}$ 是 X 的一个基. 试问, 当 X 看作实线性空间时, 其维数是多少? 请指出它的一个基.

23. 设 $X$ 是赋范线性空间, $x_{n} \in X, n = 1,2,\dots$ . 如果 $\{\sum_{n=1}^{k} x_{n}\}_{k=1}^{\infty}$ 是 $X$ 中收敛序列, 称级数 $\sum_{n=1}^{\infty} x_{n}$ 收敛. 如果数值级数 $\sum_{n=1}^{\infty} \| x_{n} \|$ 收敛, 称级数 $\sum_{n=1}^{\infty} x_{n}$ 绝对收敛.

试证明: X 中任何绝对收敛的级数都收敛当且仅当 X 是 Banach 空间.

24. 设 $X, Y$ 是赋范线性空间, $T$ 是从 $X$ 到 $Y$ 的线性算子. 试证明: 如果 $X$ 是有限维的, 则 $T$ 是有界的, 且 $T$ 的值域 $R(T)$ 也是有限维的.

25. 设 $X, Y$ 是赋范线性空间, $T$ 是从 $X$ 到 $Y$ 的线性算子. 如果 $T$ 是单射的,则 $\{x_{1},\cdots,x_{n}\}$ 是X中线性无关的当且仅当 $\{Tx_{1},\cdots,Tx_{n}\}$ 是Y中线性无关的.

26. 设 $T$ 是从赋范线性空间 $\langle X, \| \cdot \|_1 \rangle$ 到赋范线性空间 $\langle Y, \| \cdot \|_2 \rangle$ 的有界线性算子, 证明

$$
\| T \| = \sup _ {\| x \| _ {1} = 1} \| T x \| _ {2} = \sup _ {\| x \| _ {1} \leqslant 1} \| T x \| _ {2}.
$$

27. 设 $T$ 是 Banach 空间 $X$ 上有界线性算子, 如果存在 $X$ 上有界线性算子 $S$ , 使

$$
T S = S T = I,
$$

则 T 是有界可逆的, 而且 $T^{-1} = S$ .

反之, 如果 T 是有界可逆的, 则

$$
T T ^ {- 1} = T ^ {- 1} T = I.
$$

这里 $I$ 是 $X$ 上恒等算子，即

$$
I x = x, \forall x \in X.
$$

28. 设 $X$ 是距离空间, $T: X \to X$ 是映射. 如果 $T$ 是压缩的, 求证: 对任意自然数 $n, T^n$ 也是压缩的. 如果对某个自然数 $n > 1$ , $T^n$ 是压缩映射, $T$ 也一定是压缩映射吗?

29. 设 $F$ 是 $n$ 维欧氏空间 $\mathbf{R}^n$ 中非空有界闭集, 映射 $T: F \to F$ 满足

$$
d (T x, T y) <   d (x, y), \forall x, y \in F, x \neq y.
$$

试证明： $T$ 在 $F$ 中有唯一不动点.

30. 设 $K(t, s)$ 是矩形 $\{(t, s): 0 \leqslant t, s \leqslant 1\}$ 上可测函数，且

$$
\int_ {0} ^ {1} \int_ {0} ^ {1} | K (t, s) | ^ {2} d t d s <   \infty .
$$

考虑积分方程

$$
x (t) = f (t) + \lambda \int_ {0} ^ {1} K (t, s) x (s) d s,
$$

其中 $f \in L^2[0,1]$ 是一给定函数， $\lambda$ 为参数。

试利用压缩映象原理证明: 当 $\left|\lambda\right|$ 适当小时, 上述积分方程在 $L^{2}[0,1]$ 中的解存在且唯一.

## 第二章 Hilbert 空间

## § 1 内积空间有限维欧氏空间 $\mathbf{R}^n$ 具有线性的和几何的性质. 解析几何告诉我们, 对空间 $\mathbf{R}^n$ 中的两个向量 $a$ 与 $b$ 的夹角 $\theta$ , 有公式

$$
\cos \theta = \frac {(a , b)}{\| a \| \| b \|},
$$

这里 $(\cdot,\cdot)$ 是向量的内积， $\|\cdot\|$ 表示向量的长度，而且

$$
\| a \| = [ (a, a) ] ^ {1 / 2}.
$$

所以，“角度”和“长度”这两个概念都可以通过内积来定义.

现在来考虑无穷维空间上的内积概念.

定义1.1 设 $X$ 为复线性空间, 如果对任给的 $x, y \in X$ 都恰有一个复数, 记为 $(x, y)$ , 与之对应, 并且这个对应具有下列性质:

(1) $(x, x) \geqslant 0; (x, x) = 0$ 必须且只须 $x = 0$ .

(2) $(x + y, z) = (x, z) + (y, z)$ .

(3) $(\alpha x, y) = \alpha(x, y)$ .

(4) $(x, y) = (\overline{y, x})$ .

对任意的 $x, y \in X, \alpha \in \mathbf{C}$ . 则称 $(x, y)$ 为 $x$ 与 $y$ 的内积, 称 $X$ 为具有内积 $(\cdot, \cdot)$ 的内积空间.

由内积的定义,还有 $(x,\alpha y)=\bar{\alpha}(x,y)$ .

定义1.2 内积空间 $X$ 中的元素 $x, y$ 称为正交的，如果 $(x, y) = 0$ ，记作 $x \perp y$ .

$X$ 中的一族元素 $\{x_{j}\}$ 称为正规正交集，如果

$$
\left(x _ {j}, x _ {k}\right) = \delta_ {j k},
$$

这里 $\delta_{jk}$ 是 Kronecker 常数: $\delta_{jk} = 1$ , 当 $j = k$ ; $\delta_{jk} = 0$ , 当 $j \neq k$ .

在内积空间 $X$ 中, 我们定义

$$
\parallel x \parallel = [ (x, x) ] ^ {1 / 2}, \text {当} x \in X.
$$

不久我们将证明它满足前章所说的范数公设,按这个范数 X 是赋范线性空间.

若 $x$ 与 $y$ 正交，则

$$
\begin{array}{r l} \left\| x + y \right\| ^ {2} & = (x + y, x + y) \\ & = (x, x) + (x, y) + (y, x) + (y, y) \end{array}
$$

$$
= (x, x) + (y, y) = \| x \| ^ {2} + \| y \| ^ {2}.
$$

于是有

(1.1)

$$
\| x + y \| ^ {2} = \| x \| ^ {2} + \| y \| ^ {2}.
$$

这正是勾股定理在无穷维空间的推广.

定理1.1 设 $\{x_{n}\}_{n = 1}^{N}$ 是内积空间 $X$ 中的正规正交集，则对任何 $x\in X$ 都有

$$
\| x \| ^ {2} = \sum_ {n = 1} ^ {N} | (x, x _ {n}) | ^ {2} + \| x - \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \| ^ {2}.
$$

证将 $x$ 表成

$$
x = \left[ \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \right] + \left[ x - \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \right],
$$

由内积定义及假设,容易验证上式右端第一项与第二项是正交的.根据(1.1)及假设,

$$
\begin{array}{r l} \parallel x \parallel^ {2} & = \parallel \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \parallel^ {2} + \parallel x - \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \parallel^ {2} \\ & = \sum_ {n = 1} ^ {N} | (x, x _ {n}) | ^ {2} + \parallel x - \sum_ {n = 1} ^ {N} (x, x _ {n}) x _ {n} \parallel^ {2}. \end{array}
$$

证毕.

推论 1(Bessel 不等式) 设 $\{x_{n}\}_{n=1}^{N}$ 是内积空间 X 中的正规正交集，则于任何 $x \in X$ 都有

$$
\sum_ {n = 1} ^ {N} \mid (x, x _ {n}) \mid^ {2} \leqslant \| x \| ^ {2}.
$$

推论 2(Schwarz 不等式) 对内积空间 X 中任意两个向量 x, y 都有

$$
\left| (x, y) \right| \leqslant \| x \| \| y \|.
$$

证若 $y = 0$ ，则

$$
(x, y) = (x, 0 y) = 0 (x, y) = 0,
$$

可见等式成立. 若 $y \neq 0, \left\{ \frac{y}{\|y\|} \right\}$ 就是正规正交集，由 Bessel 不等式，

$$
\| x \| ^ {2} \geqslant \left| \left(x, \frac {y}{\| y \|}\right) \right| ^ {2} = \frac {| (x , y) | ^ {2}}{\| y \| ^ {2}}.
$$

由此即知所论成立.证毕.

定理1.2 每个内积空间 $X$ 按范数 $\| x \| = [(x, x)]^{1/2}$ 成为赋范线性空间.

证由内积定义, 易见 $\| \cdot \|$ 满足范数公设(1),(2), 只须证明它也满足(3). 对任意 $x, y \in X$ ,

$$
\begin{array}{r l} \parallel x + y \parallel^ {2} & = (x + y, x + y) \\ & = (x, x) + (x, y) + (y, x) + (y, y) \end{array}
$$

$$
\begin{array}{l} = \parallel x \parallel^ {2} + 2 \mathrm{Re} (x, y) + \parallel y \parallel^ {2} \\ \leqslant \parallel x \parallel^ {2} + 2 | (x, y) | + \parallel y \parallel^ {2}. \end{array}
$$

由 Schwarz 不等式, 可知

$\| x + y \|^{2} \leqslant \| x \|^{2} + 2 \| x \| \| y \| + \| y \|^{2} = (\| x \| + \| y \|)^{2}$ . 证毕.

命题 1.1 内积 $(x,y)$ 是 x,y 的二元连续函数, 即当 $n\to\infty$ 时,

$$
x _ {n} \rightarrow x, y _ {n} \rightarrow y \Rightarrow (x _ {n}, y _ {n}) \rightarrow (x, y).
$$

证显然

$$
\begin{array}{r l} & {\mid (x _ {n}, y _ {n}) - (x, y) \mid \leqslant \mid (x _ {n}, y _ {n}) - (x, y _ {n}) \mid + \mid (x, y _ {n}) - (x, y) \mid} \\ & {\qquad = \mid (x _ {n} - x, y _ {n}) \mid + \mid (x, y _ {n} - y) \mid} \\ & {\qquad \leqslant \| x _ {n} - x \| \| y _ {n} \| + \| x \| \| y _ {n} - y \|.} \end{array}
$$

如果 $x_{n}\rightarrow x,y_{n}\rightarrow y$ ，则还有 $\{\| y_n\| \}_{n = 1}^{\infty}$ 是有界数列，故当 $n\to \infty$ ，上式右端趋于0.证毕.

命题1.2 设点集 $M$ 在内积空间 $X$ 中稠密，若 $x_0 \in X$ 使

$$
(x, x _ {0}) = 0, \quad \forall x \in M,
$$

则 $x_0 = 0$

证由点集 M 在内积空间 X 中稠密知, 存在 $x_{n} \in M, n = 1, 2, \cdots$ , 使 $x_{n} \rightarrow x_{0}$ . 根据命题 1.1 及假设

$$
(x _ {0}, x _ {0}) = \lim _ {n \rightarrow \infty} (x _ {n}, x _ {0}) = 0,
$$

故 $x_0 = 0$ .证毕.

前面我们通过内积引出范数,反过来,对于内积空间,我们有下列重要结果.

定理 1.3(极化恒等式) 对内积空间 X 中任意两个向量 x, y 都有

$$
(x, y) = \frac {1}{4} \left(\| x + y \| ^ {2} - \| x - y \| ^ {2} + i \| x + i y \| ^ {2} - i \| x - i y \| ^ {2}\right).\tag{1.2}
$$

证由范数与内积关系易得

(1.3)

$$
\| x + y \| ^ {2} = (x, x) + (x, y) + (y, x) + (y, y),\tag{1.4}
$$

$$
\| x - y \| ^ {2} = (x, x) - (x, y) - (y, x) + (y, y),\tag{1.5}
$$

$$
\| x + \mathrm{i} y \| ^ {2} = (x, x) - \mathrm{i} (x, y) + \mathrm{i} (y, x) + (y, y),\tag{1.6}
$$

$$
\| x - \mathrm{i} y \| ^ {2} = (x, x) + \mathrm{i} (x, y) - \mathrm{i} (y, x) + (y, y),
$$

则由(1.3)-(1.4)+i(1.5)-i(1.6)可得

$$
\left\| x + y \right\| ^ {2} - \left\| x - y \right\| ^ {2} + i \| x + i y \| ^ {2} - i \| x - i y \| ^ {2} = 4 (x, y).
$$

证毕.

必须指出,内积空间中向量的范数有着异于其他赋范线性空间中向量范数的独特性质.

命题1.3(平行四边形法则）对内积空间 $X$ 中任意两个向量 $x, y$ 都有

$$
\| x + y \| ^ {2} + \| x - y \| ^ {2} = 2 \left(\| x \| ^ {2} + \| y \| ^ {2}\right).
$$

证在定理 1.3 证明中, (1.3) 与 (1.4) 相加即得所欲证者.

人们自然会想到, 是否每个赋范线性空间 $X$ 都能赋以内积 $(x, y)$ , 使得原来的范数 $\| x \|$ 总可以表成为 $[(x, x)]^{1/2}$ 呢? 答案是否定的. 可以证明, $X$ 能赋以内积的充要条件是 $X$ 中的范数满足平行四边形法则. 其证明方法是用(1.2)式右端来定义 $(x, y)$ , 然后利用平行四边形法则验证如此定义的 $(x, y)$ 满足内积公设. 详见[18], 第268—270页.

例1 在空间 $C[0,1]$ 中，取 $x(t) = 1, y(t) = t$ ，则

$$
\begin{array}{r l} & {\| x + y \| = \max _ {0 \leqslant t \leqslant 1} | 1 + t | = 2,} \\ & {\| x - y \| = \max _ {0 \leqslant t \leqslant 1} | 1 - t | = 1,} \\ & {\| x \| = 1, \| y \| = 1,} \end{array}
$$

显然不满足平行四边形法则. 这说明 $C[0,1]$ 不是内积空间.

定义1.3 若内积空间 $H$ 是完备的, 则称 $H$ 为 Hilbert 空间.

最早是 Hilbert 在他的积分方程工作中考察函数按某个正规正交基展开所对应的 Fourier 系数(参见[6], 第六章, §6). 这些系数序列自然属于下面所说的空间 $l^2$ . 虽然 Hilbert 并没有把这些系数序列看成空间中点的坐标, 也没有使用几何的语言(内积空间几何化这一步是由 Schmidt 和 Fréchet 开始的), 但人们还是称完备的内积空间为 Hilbert 空间, 以纪念这位伟大的先行者.

例2 空间 $\ell^2$

考察使 $\sum_{n=1}^{\infty} |\xi_n|^2 < \infty$ 的复数序列 $x = \{\xi_n\}_{n=1}^{\infty}$ 的全体形成的线性空间，记作 $t^2$ 。由 Hölder 不等式，可以定义

$$
(x, y) = \sum_ {n = 1} ^ {\infty} \xi_ {n} \bar {\eta} _ {n}, \text {当} x = \{\xi_ {n} \} _ {n = 1} ^ {\infty}, y = \{\eta_ {n} \} _ {n = 1} ^ {\infty} \in l ^ {2}.
$$

容易验证它满足内积公设, $t^{2}$ 按 $(\cdot,\cdot)$ 成为内积空间.下面证明 $l^{2}$ 是完备的.

设 $x_{k}=\{\xi_{n}^{(k)}\}_{n=1}^{\infty}, k=1,2,\cdots$ ，是 $\ell^{2}$ 中的 Cauchy 序列，于是任给 $\varepsilon>0$ ，存在正整数 N，当 $k,j\geqslant N$ ，

$$
\| x _ {k} - x _ {j} \| = \left(\sum_ {n = 1} ^ {\infty} | \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(j)} | ^ {2}\right) ^ {1 / 2} <   \varepsilon .\tag{1.7}
$$

从而对每个正整数 $n$

$$
| \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(j)} | <   \varepsilon , \text {当} k, j \geqslant N.
$$

这说明 $\{\xi_n^{(k)}\}_{k = 1}^{\infty}$ 是Cauchy数列，故

$$
\lim _ {k \rightarrow \infty} \xi_ {n} ^ {(k)} = \xi_ {n} ^ {(0)}
$$

存在且有限. 记 $x_0 = \{\xi_n^{(0)}\}_{n=1}^{\infty}$ . 由 (1.7) 式, 对每个正整数 $m$ ,

$$
\sum_ {n = 1} ^ {m} \mid \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(j)} \mid^ {2} <   \varepsilon^ {2}, \text {当} k, j \geqslant N.
$$

令 $j\to \infty$ ，可得

$$
\sum_ {n = 1} ^ {m} \mid \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(0)} \mid^ {2} {\leqslant} \varepsilon^ {2}, \text {当} k {\geqslant} N.
$$

再令 $m \to \infty$ ，可得

$$
\sum_ {n = 1} ^ {\infty} \mid \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(0)} \mid^ {2} \leqslant \epsilon^ {2}, \text {当} k \geqslant N.
$$

这表明 $x_{k} - x_{0}\in l^{2}$ ，当 $k\geqslant N$ .因 $\ell^2$ 是线性空间，故 $x_0\in \ell^2$ .由上式

$$
\parallel x _ {k} - x _ {0} \parallel = \left(\sum_ {n = 1} ^ {\infty} | \xi_ {n} ^ {(k)} - \xi_ {n} ^ {(0)} | ^ {2}\right) ^ {1 / 2} \leqslant \epsilon , \text {当} k \geqslant N.
$$

即 $x_{k}\rightarrow x_{0}$ .证毕.

常用的 Hilbert 空间是函数空间, 其中最简单的是下面所说的空间 $L^{2}[a, b]$ .

例3 空间 $L^2 [a,b]$

考察有限区间 $[a, b]$ 上复值平方可积函数 $f(x)$ 的全体按逐点定义的加法和数乘形成的一个线性空间，记作 $L^2[a, b]$ . 由 Hölder 不等式，可以定义内积

$$
(f, g) = \int_ {a} ^ {b} f (x)   \overline {{{{g (x)}}}} \mathrm{d} x, \text {当}   f, g \in L ^ {2} [ a, b ].
$$

容易验证 $L^2 [a,b]$ 按这个内积成为内积空间，而且按这个内积确定的距离恰好是第一章 §5 中例 2 当 $p = 2$ 时的距离，从那里得知 $L^2 [a,b]$ 是完备的，因此 $L^2 [a,b]$ 是 Hilbert 空间.

例4 $H_0^k (\Omega)$

设 $\Omega$ 是 $\mathbf{R}^n$ 中开集, 定义

$C_0^k (\Omega) = \{f(x):f$ 在 $\Omega$ 内有直到 $k$ 阶的连续偏导数，

且 $\operatorname{supp}(f) \subset \Omega$ 是紧的，

这里 $\operatorname{supp}(f) = \{\overline{x \in \Omega : f(x) \neq 0}\}$ . 定义内积

$$
(f, g) _ {k} = \sum_ {| j | \leqslant k} \int_ {\Omega} \partial^ {j} f (x)   \overline {{\partial^ {j} g (x)}} \mathrm{d} x  , \text {当}   f, g \in C _ {0} ^ {k} (\Omega)  ,
$$

这里 $j=(j_{1},\cdots,j_{n})$ 是重指标， $|j|=j_{1}+\cdots+j_{n}$

$$
\partial^ {j} f (x) = \frac {\partial^ {| j |} f}{\partial x _ {1} ^ {j _ {1}} \cdots \partial x _ {n} ^ {j _ {n}}} (x _ {1}, \dots , x _ {n}).
$$

$C_0^k (\Omega)$ 按这个内积形成的内积空间记作 $\hat{H}_0^k (\Omega)$ ，而 $\hat{H}_0^k (\Omega)$ 按这个内积导出的范数的完备化，记作 $H_0^k (\Omega)$ ，这是一个 Hilbert 空间。据文献[26]，第 250 页，

Schauder 已经考虑过空间 $\hat{H}_0^k (\Omega)$ , 可惜他没有考虑它的完备化. 这里的 $H_0^k (\Omega)$ 其实是著名的 Соболев 空间 $W^k (\Omega)$ 的子空间. (参见[3], 第50页)

例 5 $A^{2}(D)$ .

设 $D$ 是复平面上的一个有界区域，令

$A^2 (D) = \{f(z):f(z)$ 在 $D$ 内解析，且 $\iint_{D}|f(z)|^2\mathrm{d}x\mathrm{d}y <   \infty \}$ 这里 $z = x + \mathrm{i}y.$ 在 $A^2 (D)$ 中引进内积

$$
(f, g) = \iint_ {D} f (z)   \overline {{{{g (z)}}}} \mathrm{d} x \mathrm{d} y, \text {当}   f, g \in A ^ {2} (D).
$$

容易证明 $A^2 (D)$ 是一个内积空间，下面证明它还是完备的.

设 $\{f_n(z)\}_{n=1}^{\infty}$ 是 $A^2 (D)$ 中的一个Cauchy序列.注意 $A^2 (D)$ 是 $L^2 (D)$ 的一个线性流形，而 $L^2 (D)$ 是Hilbert空间(见习题5)，从而存在 $f_0\in L^2 (D)$ ，使(1.8） $\iint_{D}|f_n(z) - f_0(z)|^2\mathrm{d}x\mathrm{d}y\to 0$ ，当 $n\to \infty$

我们只须证明 $f_{0}(z)$ 在 $D$ 内解析.

设 $\{z:|z-z_{0}|\leqslant\rho\}$ 是包含于D内的任意闭圆盘，由于 $f_{n}(z)$ 在D内解析，有Taylor展式

$$
f _ {n} (z) - f _ {m} (z) = \sum_ {j = 0} ^ {\infty} c _ {j} (z - z _ {0}) ^ {j}.
$$

从而利用复数的指数形式 $z - z_0 = r\mathrm{e}^{\mathrm{j}\theta}$ ，可得

$$
\begin{array}{r l} \parallel f _ {n} - f _ {m} \parallel^ {2} & = \iint_ {D} | f _ {n} (z) - f _ {m} (z) | ^ {2} \mathrm{d} x \mathrm{d} y \\ & \geqslant \iint_ {| z - z _ {0} | \leqslant \rho} | f _ {n} (z) - f _ {m} (z) | ^ {2} \mathrm{d} x \mathrm{d} y \\ & = \int_ {0} ^ {\rho} \left[ \int_ {0} ^ {2 \pi} \left(\sum_ {j = 0} ^ {\infty} c _ {j} r ^ {j} \mathrm{e} ^ {\mathrm{i} j \theta}\right) \left(\sum_ {k = 0} ^ {\infty} \bar {c} _ {k} r ^ {k} \mathrm{e} ^ {- \mathrm{i} k \theta}\right) \mathrm{d} \theta \right] r \mathrm{d} r \\ & = \sum_ {j = 0} ^ {\infty} 2 \pi \int_ {0} ^ {\rho} | c _ {j} | ^ {2} r ^ {2 j + 1} \mathrm{d} r \\ & = 2 \pi \sum_ {j = 0} ^ {\infty} \rho^ {2 j + 2} | c _ {j} | ^ {2} (2 j + 2) ^ {- 1} \\ & \geqslant \pi \rho^ {2} | c _ {0} | ^ {2} \\ & = \pi \rho^ {2} | f _ {n} (z _ {0}) - f _ {m} (z _ {0}) | ^ {2}. \end{array}
$$

因 $\{f_n\}_{n=1}^{\infty}$ 按 $\|\cdot\|$ 是 Cauchy 序列, 这个式子表明 $\{f_n(z)\}_{n=1}^{\infty}$ 在包含于 $D$ 内的任意闭圆盘上一致收敛. 于是

$$
f _ {0} (z) = \lim _ {n \rightarrow \infty} f _ {n} (z)
$$

在 $D$ 内解析.

总之， $A^2 (D)$ 是一个Hilbert空间.

命题1.4 内积空间 $X$ 的完备化 $\tilde{X}$ 是Hilbert空间.

证内积空间 $X$ 按内积 $(\cdot, \cdot)$ 所确定的范数成为赋范线性空间，于是由第一章 §5 中定理 5.1，存在 $X$ 的完备化 $\widetilde{X}$ ，使对 $\tilde{x}, \tilde{y} \in \widetilde{X}$ ，有 $X$ 中的 Cauchy 序列 $\{x_n\}_{n=1}^{\infty}, \{y_n\}_{n=1}^{\infty}$ ，使 $\tilde{x} = \{x_n\}_{n=1}^{\infty}, \tilde{y} = \{y_n\}_{n=1}^{\infty}$ ，注意

$$
\begin{array}{r l} & {\mid (x _ {n}, y _ {n}) - (x _ {m}, y _ {m}) \mid} \\ & {\leqslant \mid (x _ {n}, y _ {n}) - (x _ {m}, y _ {n}) \mid + \mid (x _ {m}, y _ {n}) - (x _ {m}, y _ {m}) \mid} \\ & {\leqslant \| x _ {n} - x _ {m} \| \| y _ {n} \| + \| x _ {m} \| \| y _ {n} - y _ {m} \|,} \end{array}
$$

可见 $\{(x_{n},y_{n})\}_{n = 1}^{\infty}$ 是Cauchy数列，从而收敛.定义

$$
(\tilde {x}, \tilde {y}) _ {1} = \lim _ {n \rightarrow \infty} (x _ {n}, y _ {n}).
$$

假设 $\{x_{n}^{\prime}\}_{n = 1}^{\infty},\{y_{n}^{\prime}\}_{n = 1}^{\infty}$ 亦是 $X$ 中Cauchy序列，使 $\tilde{x} = \{x_n^\prime \}_{n = 1}^{\infty},\tilde{y} = \{y_n^\prime \}_{n = 1}^{\infty}$ . 则 $\lim_{n\to \infty}\| x_n - x_n'\| = 0,\lim_{n\to \infty}\| y_n - y_n'\| = 0.$ 注意

$$
\begin{array}{l} \left| \left(x _ {n}, y _ {n}\right) - \left(x _ {n} ^ {\prime}, y _ {n} ^ {\prime}\right) \right| \\ \leqslant \left| \left(x _ {n}, y _ {n}\right) - \left(x _ {n}, y _ {n} ^ {\prime}\right) \right| + \left| \left(x _ {n}, y _ {n} ^ {\prime}\right) - \left(x _ {n} ^ {\prime}, y _ {n} ^ {\prime}\right) \right| \\ \leqslant \| x _ {n} \| \| y _ {n} - y _ {n} ^ {\prime} \| + \| x _ {n} - x _ {n} ^ {\prime} \| \| y _ {n} ^ {\prime} \|, \end{array}
$$

可见

$$
\lim _ {n \rightarrow \infty} (x _ {n}, y _ {n}) = \lim _ {n \rightarrow \infty} (x _ {n} ^ {\prime}, y _ {n} ^ {\prime}).
$$

这说明 $(\tilde{x},\tilde{y})_1$ 的定义与表示 $\tilde{x},\tilde{y}$ 的具体的Cauchy序列选择无关，所以定义是完善的，容易验证 $(\cdot ,\cdot)_1$ 满足内积公设，因而 $\widetilde{X}$ 按 $(\cdot ,\cdot)_1$ 成为内积空间.

注意, $\widetilde{X}$ 按第一章 §5 中定理 5.1 完备化构造所确定的范数 $\|\cdot\|$ 与内积 $(\cdot,\cdot)_{1}$ 之间有如下关系

$$
\| \tilde {x} \| ^ {2} = \lim _ {n \rightarrow \infty} (x _ {n}, x _ {n}) = (\tilde {x}, \tilde {x}) _ {1},
$$

即 $\tilde{X}$ 的范数 $\| \cdot \|$ 恰是由内积 $(\cdot, \cdot)_1$ 确定的范数，所以 $\tilde{X}$ 作为内积空间是完备的，即 $\tilde{X}$ 是 Hilbert 空间. 证毕.

## § 2 正规正交基此后,如无特殊声明,我们总用 H 表示非零的 Hilbert 空间.

设 $\{u_n\} \subset H$ 是线性无关的序列. 现在如线性代数所说的, 令

$$
w _ {1} = u _ {1}, \quad v _ {1} = \frac {w _ {1}}{\| w _ {1} \|},
$$

$$
w _ {2} = u _ {2} - \left(u _ {2}, v _ {1}\right) v _ {1}, \quad v _ {2} = \frac {w _ {2}}{\| w _ {2} \|},\tag{2.1}
$$

$$
w _ {n} = u _ {n} - \sum_ {k = 1} ^ {n - 1} \left(u _ {n}, v _ {k}\right) v _ {k}, \quad v _ {n} = \frac {w _ {n}}{\| w _ {n} \|},
$$

则 $\{v_{1}, v_{2}, \cdots, v_{n}, \cdots\}$ 便是一个正规正交集，并且对任何正整数 m，都有

$$
\operatorname{Sp} \left\{u _ {1}, \dots , u _ {m} \right\} = \operatorname{Sp} \left\{v _ {1}, \dots , v _ {m} \right\}.\tag{2.2}
$$

上述的按(2.1)式从 $\{u_{n}\}$ 构造 $\{v_{n}\}$ 的方法叫做Schmidt正规正交法.

定义 2.1 设 S 是 H 中的正规正交集, 如果 H 中没有其他的正规正交集真包含 S, 则称 S 为 H 的正规正交基.

下面命题给出 Hilbert 空间正规正交基的一个等价描述.

命题2.1 设 $S$ 是 $H$ 的正规正交集. 则 $S$ 是 $H$ 的正规正交基的充要条件是 $H$ 中没有非零元与 $S$ 中每个元正交.

证必要性. 设 $x \in H$ 与 $S$ 中每个元正交. 如果 $x \neq 0$ , 令 $x_{1} = \frac{x}{\|x\|}$ , 则 $S_{1} = S \cup \{x_{1}\}$ 便是 $H$ 中真包含 $S$ 的一个正规正交集. 这与 $S$ 是正规正交基矛盾:

充分性. 否则, 存在 $H$ 的正规正交集 $S'$ 真包含 $S$ , 取非零的 $x \in S' \setminus S$ , 则 $x$ 与 $S$ 中每个元正交, 与假设矛盾. 证毕.

定理 2.1 若 H 可分, 则 H 有一个可数的正规正交基.

证由于 $H$ 可分, $H$ 中存在可数的稠密子集 $S$ . 利用数学归纳法可以证明必存在 $S$ 中一个线性无关子集 $\{x_{n}\}$ , 使得 $S$ 中每个元都可以表示成 $\{x_{n}\}$ 中某些元的线性组合.

将 Schmidt 正规正交法用于 $\{x_{n}\}$ ，得到正规正交集 $\{e_{n}\}$ .

若有 $e \in H$ ，使

$$
(e, e _ {n}) = 0, \quad n = 1, 2, \dots .
$$

注意由Schmidt正规正交法，每个 $x_{n}$ 可以表成 $x_{n} = \sum_{j = 1}^{n}c_{j}^{(n)}e_{j}$ ，从而

$$
(e, x _ {n}) = 0, \quad n = 1, 2, \dots .
$$

又任给 $x \in S$ ，可以表成 $\{x_{n}\}$ 中某些元的线性组合，故

$$
(e, x) = 0, \quad \forall x \in S.
$$

由于 $S$ 是 $H$ 中稠密子集，根据命题1.2可知， $e = 0$ 。再根据命题2.1，可见 $\{e_n\}$ 是

H 的正规正交基. 证毕.

定理2.2 每个非零的Hilbert空间都有正规正交基.

证设 $H$ 是一个非零的 Hilbert 空间, 考虑 $H$ 中一切正规正交集构成的族 $\mathcal{I}, \mathcal{I}$ 是非空的, 因为任取 $x \neq 0$ , $\left\{\frac{x}{\|x\|}\right\}$ 便是 $\mathcal{I}$ 中的一个元. 对 $S_1, S_2 \in \mathcal{I}$ , 定义 $S_1 < S_2$ , 当 $S_1 \subset S_2$ . 则 $\mathcal{I}$ 按“<”成为一个部分有序集. 若 $\{S_a\}_{a \in \mathcal{I}}$ 是 $\mathcal{I}$ 中的完全有序子集, 则 $\bigcup_{a \in \mathcal{I}} S_a \in \mathcal{I}$ , 而且是 $\{S_a\}_{a \in \mathcal{A}}$ 的上界. 根据 Zorn 引理, $\mathcal{I}$ 中存在极大元 $S_M$ , 则 $S_M$ 便是 $H$ 的一个正规正交基. 证毕.

定理2.3 设 $S = \{x_{a}\}_{a\in \mathcal{A}}$ 是 $H$ 的一个正规正交基，则对任何的 $x\in H$ 都有

$$
\begin{array}{r l} x & = \sum_ {a \in \mathcal {A}} (x, x _ {a}) x _ {a}, \\ \| x \| ^ {2} & = \sum_ {a \in \mathcal {A}} | (x, x _ {a}) | ^ {2}, \end{array}
$$

这里 $\sum_{a\in \mathcal{N}}z_a$ 表示最多只有可数多个 $z_{a}\neq 0$ ，而且级数无条件收敛.

特别, 当 $H$ 是可分的 Hilbert 空间, $\{x_{n}\}_{n=1}^{\infty}$ 是 $H$ 的正规正交基, 则对任何的 $x \in H$ 都有

$$
\| x \| ^ {2} = \sum_ {n = 1} ^ {\infty} | (x, x _ {n}) | ^ {2}.\tag{2.3}
$$

式(2.3)通常被称为 Parseval 公式.

证设 $x \in H$ , 由 Schwarz 不等式, 对每个 $\alpha \in \mathcal{A}$ ,

$$
\mid (x, x _ {a}) \mid \leqslant \| x \|. \tag {1}
$$

注意

$$
\bigcup_ {k = 1} ^ {\infty} \left[ \frac {1}{k + 1} \| x \|, \quad \frac {1}{k} \| x \| \right] = (0, \| x \| ].
$$

于是，若有不可数个 $(x, x_{a}) \neq 0$ ，则至少有一个区间

$$
\left[ \frac {1}{k + 1} \| x \|, \frac {1}{k} \| x \| \right]
$$

中包含无穷多个 $|(x, x_{\alpha})|$ . 这与 Bessel 不等式矛盾.

现在 $\{(x, x_{\alpha})\}_{\alpha \in \mathcal{A}}$ 中最多只有可数多个不为0者，将它们排列成

$$
(x, x _ {a _ {1}}), (x, x _ {a _ {2}}), \dots , (x, x _ {a _ {j}}), \dots ,
$$

由 Bessel 不等式, 对任意正整数 N,

$$
\sum_ {j = 1} ^ {N} \mid (x, x _ {\alpha_ {j}}) \mid^ {2} \leqslant \| x \| ^ {2},
$$

故 $\sum_{j=1}^{\infty}|(x, x_{a_j})|^2$ 收敛.

令 $y_{n}=\sum_{j=1}^{n}(x,x_{a_{j}})x_{a_{j}},n=1,2,\cdots$ ，则当 n>m 时，

$$
\| y _ {n} - y _ {m} \| ^ {2} = \left\| \sum_ {j = m + 1} ^ {n} \left(x, x _ {a _ {j}}\right) x _ {a _ {j}} \right\| ^ {2} = \sum_ {j = m + 1} ^ {n} | (x, x _ {a _ {j}}) | ^ {2},
$$

可见 $\{y_{n}\}_{n = 1}^{\infty}$ 是Cauchy序列. $H$ 是完备的，故可设 $y_{n}\rightarrow x^{\prime}\in H.$ 往证 $x^{\prime} = x$

显然，对一切 $x_{\alpha_k}$ 有

$$
\begin{array}{r l}(x - x ^ {\prime}, x _ {a _ {k}})&= \left(x - \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}}, x _ {a _ {k}}\right)\\&= (x, x _ {a _ {k}}) - \lim _ {n \rightarrow \infty} \left(\sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}}, x _ {a _ {k}}\right)\\&= (x, x _ {a _ {k}}) - \lim _ {n \rightarrow \infty} \left[ \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) (x _ {a _ {j}}, x _ {a _ {k}}) \right]\\&= (x, x _ {a _ {k}}) - (x, x _ {a _ {k}})\\&= 0.\end{array}
$$

而对 $x_{a} \in S, \alpha \neq \alpha_{k}, (x, x_{a}) = 0$ ，且 $(x_{a_{j}}, x_{a}) = 0, j = 1, 2, \cdots$ ，故

$$
\begin{array}{r l}(x - x ^ {\prime}, x _ {a})&= \left(x - \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}}, x _ {a}\right)\\&= (x, x _ {a}) - \lim _ {n \rightarrow \infty} \left(\sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}}, x _ {a}\right)\\&= \lim _ {n \rightarrow \infty} \left[ \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) (x _ {a _ {j}}, x _ {a}) \right]\\&= 0.\end{array}
$$

于是 $x - x'$ 与 $S$ 中一切元正交. 而 $S$ 是 $H$ 的正规正交基, 故 $x - x' = 0$ . 即

$$
\begin{array}{r l}x&= \lim _ {n \rightarrow \infty} \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}}\\&= \sum_ {j = 1} ^ {\infty} (x, x _ {a _ {j}}) x _ {a _ {j}} = \sum_ {a \in \mathcal {A}} (x, x _ {a}) x _ {a}.\end{array}
$$

至于第二个等式,根据定理1.1,对任意正整数n,

$$
\| x \| ^ {2} = \sum_ {j = 1} ^ {n} | (x, x _ {a _ {j}}) | ^ {2} + \| x - \sum_ {j = 1} ^ {n} (x, x _ {a _ {j}}) x _ {a _ {j}} \| ^ {2}.
$$

于是，令 $n\to \infty$ ，可得

$$
\| x \| ^ {2} = \sum_ {j = 1} ^ {\infty} | (x, x _ {a _ {j}}) | ^ {2} = \sum_ {a \in \mathcal {A}} | (x, x _ {a}) | ^ {2}.
$$

证毕.

作为这个定理的推论,可以证明下述重要事实.

推论任何一个可分 Hilbert 空间都与 $t^2$ 同构.

证设 $H$ 是可分 Hilbert 空间, 由定理 2.1, 存在正规正交基 $\{e_n\}_{n=1}^{\infty}$ . 又由定理 2.3, 任给 $x \in H$ ,

$$
x = \sum_ {n = 1} ^ {\infty} (x, e _ {n}) e _ {n},
$$

且

$$
\| x \| ^ {2} = \sum_ {n = 1} ^ {\infty} | (x, e _ {n}) | ^ {2}.
$$

于是 $\{(x,e_{n})\}=\{(x,e_{1}),(x,e_{2}),\cdots,(x,e_{n}),\cdots\}\in l^{2}$ ，定义映射 $U:H\to l^{2}$ 如下

$$
U x = \{(x, e _ {n}) \}, \quad \forall x \in H.
$$

设 $y \in H, \alpha \in \mathbf{C}$ , 则 $y = \sum_{n=1}^{\infty} (y, e_n) e_n$ ,

$$
x + y = \sum_ {n = 1} ^ {\infty} (x + y, e _ {n}) e _ {n}, \quad a x = \sum_ {n = 1} ^ {\infty} (a x, e _ {n}) e _ {n}.
$$

因为

$$
(x + y, e _ {n}) = (x, e _ {n}) + (y, e _ {n}), \quad (\alpha x, e _ {n}) = \alpha (x, e _ {n}),
$$

可见

$$
U (x + y) = U x + U y, \quad U (\alpha x) = \alpha U x.
$$

说明 $U$ 是线性的. 又由习题4，

$$
(x, y) = \sum_ {n = 1} ^ {\infty} (x, e _ {n}) \overline {{(y , e _ {n})}} = (U x, U y).
$$

说明 $U$ 是保内积的，从而也是单射的. 下面只须证明 $U$ 是满射的. 设 $\{\xi_n\} \in l^2$ 令

$$
x _ {k} = \sum_ {n = 1} ^ {k} \xi_ {n} e _ {n}, \quad k = 1, 2, \dots .
$$

则当 $m > k$ 时，

$$
\left\| x _ {m} - x _ {k} \right\| ^ {2} = \left\| \sum_ {n = k + 1} ^ {m} \xi_ {n} e _ {n} \right\| ^ {2} = \sum_ {n = k + 1} ^ {m} \left| \xi_ {n} \right| ^ {2}.
$$

因 $\sum_{n=1}^{\infty} |\xi_n|^2 < \infty$ ，可知 $\{x_k\}$ 是 Cauchy 序列。而 $H$ 是完备的，故 $\lim_{k \to \infty} x_k = x$ 存在。于是

$$
x = \lim _ {k \rightarrow \infty} \sum_ {n = 1} ^ {k} \xi_ {n} e _ {n} = \sum_ {n = 1} ^ {\infty} \xi_ {n} e _ {n}.
$$

显然

$$
(x, e _ {n}) = \xi_ {n}, \quad n = 1, 2, \dots .
$$

因此， $Ux = \{(x,e_n)\} = \{\xi_n\}$ ，即 $U$ 是满射的.证毕.

## § 3 射影定理, Fréchet-Riesz 表现定理设 $M$ 是Hilbert空间 $H$ 的线性流形，定义

$$
M ^ {\perp} \stackrel {d} {=} \{y \in H: (y, x) = 0, \quad \forall x \in M \},
$$

并称 $M^{\perp}$ 为 $M$ 的正交补.

从内积的线性与连续性, 易证 $M^{\perp}$ 是 $H$ 的子空间. 显然 $M$ 与 $M^{\perp}$ 的交为 $\{0\}$ .

定理3.1(射影定理）设 $M$ 是Hilbert空间 $H$ 的子空间，则每个 $x \in H$ 都可以唯一地表成

$$
x = y + z, \quad y \in M, \quad z \in M ^ {\perp}.
$$

人们称这个由 $x$ 与 $M$ 唯一确定的 $y$ 为 $x$ 在 $M$ 上的正交射影.

证·注意 M 也是 Hilbert 空间，根据定理 2.2, M 有一个正规正交基 $\{y_{\alpha}\}_{\alpha\in\mathcal{A}}$ . 任给 $x\in H$ ，由定理 2.3 证明第一段可知，最多只有可数多个 $(x,y_{\alpha})\neq0$ . 设它们是 $\{(x,y_{\alpha_{j}})\}_{j=1}^{\infty}$ ，则对 $\alpha\in\mathcal{A},\alpha\neq\alpha_{j},j=1,2,\cdots,(x,y_{\alpha})=0$ . 令

$$
y = \sum_ {j = 1} ^ {\infty} (x, y _ {a _ {j}}) y _ {a _ {j}}.
$$

$$
y \in M
$$

令 $z = x - y$ ，则对 $k = 1,2,\dots$ ，有

$$
\begin{array}{r l} (z, y _ {a _ {k}}) & = (x, y _ {a _ {k}}) - (y, y _ {a _ {k}}) \\ & = (x, y _ {a _ {k}}) - \left(\sum_ {j = 1} ^ {\infty} (x, y _ {a _ {j}}) y _ {a _ {j}}, y _ {a _ {k}}\right) \\ & = (x, y _ {a _ {k}}) - \sum_ {j = 1} ^ {\infty} (x, y _ {a _ {j}}) (y _ {a _ {j}}, y _ {a _ {k}}) \\ & = (x, y _ {a _ {k}}) - (x, y _ {a _ {k}}) \\ & = 0. \end{array}
$$

又当 $\alpha\in\mathcal{A}$ ，且 $\alpha\neq\alpha_{k}, k=1,2,\cdots,$

$$
\begin{array}{r l} (z, y _ {a}) & = (x, y _ {a}) - (y, y _ {a}) \\ & = (x, y _ {a}) - \left(\sum_ {j = 1} ^ {\infty} (x, y _ {a _ {j}}) y _ {a _ {j}}, y _ {a}\right) = 0. \end{array}
$$

总之，

$$
(z, y _ {a}) = 0, \quad \text {当} a \in \mathcal {A}.
$$

根据定理2.3, $M$ 中每个元 $\pmb{u}$ 都可表成 $\sum_{\alpha \in \mathcal{A}}(u,y_{\alpha})y_{\alpha}$ , 可见 $(z,u) = 0, \forall u \in$

$M$ ，即 $z\in M^{\perp}$ .因此

$$
x = y + z, \quad y \in M, \quad z \in M ^ {\perp}.
$$

至于唯一性, 可由 $M \cap M^{\perp} = \{0\}$ 得出. 证毕.

应该指出, 这个定理也可以看作是 Schmidt 正规正交法的推广. 因为对于任何子空间 $M$ , 若 $x_0 \notin M$ , 根据射影定理, 便有

$$
x _ {0} = y _ {0} + z _ {0}, \quad y _ {0} \in M, \quad z _ {0} \in M ^ {\perp}.
$$

显然 $z_0 \neq 0, z_0$ 是新的与 $M$ 中一切元都正交的元. 为什么说是推广呢? 因为现在的 $\dim M$ 不限于有限的.

区别于一般 Banach 空间, Hilbert 空间是几何性质最丰富的空间, 理由之一就在于它有射影定理. 早在 20 世纪 30 年代, 人们就已举出反例, 即使对前述的 $L^{p}(p \neq 2)$ 空间, 也不能有类似射影定理那样美好的性质. 关于这个反例可参见 [36].

命题3.1 设 $M$ 是 $H$ 的线性流形, 则 $\overline{M} = (M^{\perp})^{\perp}$ .

证设 $x \in (M^{\perp})^{\perp}$ , 因为 $\overline{M}$ 是 $H$ 的子空间, 根据射影定理,

$$
x = y + z, \quad y \in \overline {{{M}}}, \quad z \in (\overline {{{M}}}) ^ {\perp}.
$$

不难证明 $(\overline{M})^{\perp} = M^{\perp}$ . 于是, 用 $z$ 与上述表达式作内积有

$$
0 = (x, z) = (z, z),
$$

故 $z = 0$ ，从而 $x = y\in \overline{M}$ .可见 $(M^{\perp})^{\perp}\subset \overline{M}$

另一方面，由正交补定义有 $M \subset (M^{\perp})^{\perp}$ ，又因 $(M^{\perp})^{\perp}$ 是闭的，故 $\overline{M} \subset (M^{\perp})^{\perp}$ . 证毕.

例1 设

$$
f (x) = \int_ {a} ^ {b} x (t) \mathrm{d} t, x \in L ^ {2} [ a, b ].
$$

则 $f$ 是 $L^2 [a,b]$ 上的线性泛函，且

$$
\begin{array}{r l} \mid f (x) \mid & = \left| \int_ {a} ^ {b} x (t) \mathrm{d} t \right| \\ & \leqslant \left(\int_ {a} ^ {b} 1 \mathrm{d} t\right) ^ {1 / 2} \left(\int_ {a} ^ {b} \mid x (t) \mid^ {2} \mathrm{d} t\right) ^ {1 / 2} \\ & = (b - a) ^ {1 / 2} \| x \|. \end{array}
$$

可见 $f$ 是 $L^2 [a,b]$ 上的连续线性泛函.

第一章 §7 中引进的连续线性泛函的概念正是从积分这个最常见且重要的线性泛函抽象出来的. 例 1 表明 Hilbert 空间 $L^2[a, b]$ 上有非零的连续线性泛函. 设 $H^*$ 表示 Hilbert 空间 $H$ 上全体连续线性泛函按逐点定义的加法和数乘形成的线性空间. 对 $f \in H^*$ , 定义

$$
\| f \| = \sup _ {\| x \| \leqslant 1} | f (x) |,
$$

容易验证按这个范数, $H^{*}$ 是完备的赋范线性空间.通常称 $H^{*}$ 为H的共轭空间,或对偶空间.

定理 3.2(Fréchet-Riesz 表现定理,1907) 设 $f \in H^{*}$ ，则恰有一个 $z_{f} \in H$ ，使 f 可表为

$$
f (x) = \left(x, z _ {f}\right), \quad \forall x \in H,
$$

并且

$$
\| f \| _ {H ^ {*}} = \| z _ {f} \| _ {H},
$$

这里范数 $\| \cdot \|$ 的角标 $H^{*}, H$ 通常省略.

证令 $M = \{x \in H : f(x) = 0\}$ , 则 $M$ 是 $H$ 的一个子空间.

若 $M = H$ ，则

$$
f (x) = 0 = (x, 0), \quad \forall x \in H.
$$

取 $z_{f} = 0$ 即可.

若 $M \neq H$ ，则有 $x_0 \in H \setminus M$ . 根据射影定理有

$$
x _ {0} = y _ {0} + z _ {0}, \quad y _ {0} \in M, \quad z _ {0} \in M ^ {\perp}.
$$

显然 $z_0 \neq 0$ 且 $f(z_0) \neq 0$ . 现在对任给的 $x \in H$ , 取 $\beta = \frac{f(x)}{f(z_0)}$ , 则

$$
f (x) = \beta f (z _ {0}) = f (\beta z _ {0}).\tag{3.1}
$$

故 $f(x - \beta z_0) = 0$ ，从而 $x - \beta z_0\in M.$ 总之

$$
x = (x - \beta z _ {0}) + \beta z _ {0}, \quad x - \beta z _ {0} \in M.\tag{3.2}
$$

这表明 $M$ 与 $\{z_0\}$ 张成整个空间.

取(3.2)式与 $z_0$ 的内积，可得

$$
(x, z _ {0}) = \beta (z _ {0}, z _ {0}) = \beta \| z _ {0} \| ^ {2}.
$$

从而定出

$$
\beta = \frac {(x , z _ {0})}{\| z _ {0} \| ^ {2}} = \left(x, \frac {z _ {0}}{\| z _ {0} \| ^ {2}}\right).
$$

由(3.1)式即得

$$
f (x) = \beta f \left(z _ {0}\right) = \left(x, \frac {z _ {0}}{\| z _ {0} \| ^ {2}}\right) f \left(z _ {0}\right) = \left(x, \frac {\overline {{f \left(z _ {0}\right)}}}{\| z _ {0} \| ^ {2}} z _ {0}\right).
$$

于是

$$
z _ {f} = \frac {\overline {{f (z _ {0})}}}{\parallel z _ {0} \parallel^ {2}} z _ {0}
$$

即为所求者.

至于唯一性,若又有 $z_{j}^{\prime}\in H$ ,使

$$
f (x) = \left(x, z _ {f} ^ {\prime}\right), \quad \forall x \in H.
$$

则

$$
(x, z _ {f}) = (x, z _ {f} ^ {\prime}), \quad \forall x \in H.
$$

即

$$
(x, z _ {f} - z _ {f} ^ {\prime}) = 0, \quad \forall x \in H.
$$

可见必须 $z_{f} - z_{f}^{\prime} = 0$ ，即 $z_{f} = z_{f}^{\prime}$

最后，由

$$
\begin{array}{r l} \| f \| _ {H ^ {*}} & = \sup _ {\| x \| \leqslant 1} | f (x) | = \sup _ {\| x \| \leqslant 1} | (x, z _ {f}) | \\ & \leqslant \sup _ {\| x \| \leqslant 1} \| x \| \| z _ {f} \| = \| z _ {f} \| \end{array}
$$

和

$$
\begin{array}{r l} \| f \| _ {H ^ {*}} & = \sup _ {\| x \| \leqslant 1} | f (x) | \\ & \geqslant \left| f \left(\frac {z _ {f}}{\| z _ {f} \|}\right) \right| \\ & = \left| \left(\frac {z _ {f}}{\| z _ {f} \|}, z _ {f}\right) \right| \\ & = \| z _ {f} \| \end{array}
$$

可见

$$
\| f \| _ {H ^ {*}} = \| z _ {f} \|.
$$

证毕.

根据 Fréchet-Riesz 表现定理, 每个 $f \in H^{*}$ 对应唯一的 $z_{f} \in H$ , 使

$$
f (x) = \left(x, z _ {f}\right), \quad \forall x \in H.\tag{3.3}
$$

另一方面，对每个 $z \in H$ ，令

$$
f _ {z} (x) = (x, z), \quad \text {当} x \in H,
$$

易证 $f_{z}$ 是 $H$ 上连续线性泛函，即 $f_{z} \in H^{*}$ . 于是，如果我们定义映射 $\tau: H^{*} \to H$ 为

$$
\tau (f) = z _ {f}, \quad \text {当} f \in H ^ {*},
$$

这里 $z_{f}$ 是根据 Fréchet-Riesz 表现定理由 $f$ 确定的 $H$ 中满足 (3.3) 式的唯一元. 则 $\tau$ 是由 $H^{*}$ 到 $H$ 上的一一对应的保范映射. 但它不是线性的, 而是共轭线性的:

$$
\tau \left(\alpha_ {1} f _ {1} + \alpha_ {2} f _ {2}\right) = \bar {\alpha} _ {1} \tau \left(f _ {1}\right) + \bar {\alpha} _ {2} \tau \left(f _ {2}\right).
$$

因为对任意 $f_{1}, f_{2} \in H^{*}, \alpha_{1}, \alpha_{2} \in \mathbf{C}$ ,

$$
\begin{array}{r l} \left(\alpha_ {1} f _ {1} + \alpha_ {2} f _ {2}\right) (x) & = \alpha_ {1} f _ {1} (x) + \alpha_ {2} f _ {2} (x) \\ & = \alpha_ {1} (x, \tau (f _ {1})) + \alpha_ {2} (x, \tau (f _ {2})) \\ & = (x, \bar {\alpha} _ {1} \tau (f _ {1}) + \bar {\alpha} _ {2} \tau (f _ {2})). \end{array}
$$

如果在 $H^{*}$ 中定义内积

$$
(f _ {1}, f _ {2}) = \overline {{{(z _ {f _ {1}} , z _ {f _ {2}})}}}, \quad \text {当} f _ {1}, f _ {2} \in H ^ {*},\tag{3.4}
$$

容易验证 $H^{*}$ 成为 Hilbert 空间. 于是 $\tau: H^{*} \to H$ 是两个 Hilbert 空间之间的共轭同构 (即 $\tau$ 是保范的、双射的、共轭线性的映射). 如果我们对共轭同构的 Hilbert 空间不加区别, 视为同一空间, 可记 $H^{*} = H$ . Hilbert 空间的这种性质称为自共轭性. 这是 Hilbert 空间的基本性质之一.

在实际问题中,我们常会遇到双一次形式 $\varphi(x,y)$ , 抽象的线性算子特别是无界线性算子的问题有时转化成标量的双一次形式, 在运算上更为方便.

定义3.1 设 $\varphi(x, y)$ 是从 $H \times H$ 到 $\mathbf{C}$ 中的函数，具有性质：

(1) $\varphi(ax + \beta y, z) = \alpha \varphi(x, z) + \beta \varphi(y, z)$ ,

(2) $\varphi(x, \alpha y + \beta z) = \bar{\alpha} \varphi(x, y) + \bar{\beta} \varphi(x, z)$ ,

当 $x, y, z \in H, \alpha, \beta \in \mathbf{C}$ . 则称 $\varphi(x, y)$ 为 $H$ 上的共轭双线性泛函. 若更有常数 $C > 0$ , 使

(3) $|\varphi (x,y)|\leqslant C\| x\| \| y\|$ ，当 $x,y\in H$

则称 $\varphi(x, y)$ 为有界的.

在上述定义中,如果(2)换成下面的

$$
(2 ^ {\prime}) \varphi (x, \alpha y + \beta z) = \alpha \varphi (x, y) + \beta \varphi (x, z),
$$

就称 $\varphi(x, y)$ 为 $H$ 上的双线性泛函.

显然,如果共轭双线性泛函 $\varphi(x,y)$ 还满足

$$
\varphi (y, x) = \overline {{{{\varphi (x , y)}}}}, \quad \varphi (x, x) \geqslant 0, \quad \forall x, y \in H,
$$

以及

$$
\varphi (x, x) = 0 \Leftrightarrow x = 0.
$$

那么 $\varphi(x, y)$ 就是个内积了.

定理3.3 设 $\varphi(x, y)$ 是 $H$ 上有界的共轭双线性泛函，则恰有 $H$ 上一个有界线性算子 $A$ ，使

$$
\varphi (x, y) = (A x, y), \quad \text {当} x, y \in H,
$$

证对任给的 $x \in H$ , 令

$$
f (y) = \overline {{{{\varphi (x , y)}}}}, \quad \text {当} y \in H.
$$

易证 $f \in H^{*}$ , 且由 $x$ 唯一确定. 根据定理3.2, 恰有一个元 $z_{f} \in H$ , 使

$$
f (y) = (y, z _ {f}), \quad \text {当} y \in H.
$$

这个 $z_{f}$ 是由 $f$ ，从而由 $\pmb{x}$ 所唯一确定.定义 $Ax = z_{f}$ ，则

$$
\overline {{{{\varphi (x , y)}}}} = (y, A x),
$$

即

$$
\varphi (x, y) = (A x, y), \quad \text {当}   x, y \in H.
$$

不难验证,如此定义的 A 确是 H 上有界线性算子.至于唯一性是显然的.证毕.

例2 设 $\Omega$ 是 $\mathbb{R}^2$ 中区域, $\mathcal{D} = \{u \in C_0^1(\Omega): u \text{ 是实值的}\}$ . 则

$$
a (u, v) = \iint_ {\Omega} (u _ {x} v _ {x} + u _ {y} v _ {y}) \mathrm{d} x \mathrm{d} y, \quad u, v \in \mathcal {D},
$$

是 $\mathcal{D}$ 上按 $H_0^1 (\Omega)$ 的范数 $\| \cdot \| _1$ 有界的双线性泛函，这里 $C_0^1 (\Omega)$ 的定义参见 §1 中例4，

$$
u _ {x} = \frac {\partial u}{\partial x}, \quad u _ {y} = \frac {\partial u}{\partial y}, \text {当} u \in \mathcal {D}.
$$

因为我们只考虑实值函数， $H_0^1 (\Omega)$ 中内积定义为

$$
(u, v) _ {1} = \sum_ {| j | \leqslant 1} \iint_ {\Omega} \partial^ {j} u \partial^ {j} v \mathrm{d} x \mathrm{d} y,
$$

故

$$
\begin{array}{r l} \parallel u \parallel_ {1} & = [ (u, u) _ {1} ] ^ {1 / 2} = \left[ \sum_ {| j | \leqslant 1} \iint_ {\Omega} | \partial^ {j} u | ^ {2} \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2} \\ & = \left[ \iint_ {\Omega} (u ^ {2} + u _ {x} ^ {2} + u _ {y} ^ {2}) \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2}. \end{array}
$$

容易验证

$$
(u, v) \stackrel {\mathrm{d}} {=} \iint_ {\Omega} (u _ {x} v _ {x} + u _ {y} v _ {y}) \mathrm{d} x \mathrm{d} y, u, v \in \mathcal {D},
$$

也是一个内积,从而由 Schwarz 不等式

$$
\begin{array}{r l} \mid a (u, v) \mid & = \left| \iint_ {\Omega} (u _ {x} v _ {x} + u _ {y} v _ {y}) \mathrm{d} x \mathrm{d} y \right| \\ & \leqslant \left[ \iint_ {\Omega} (\mid u _ {x} \mid^ {2} + \mid u _ {y} \mid^ {2}) \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2} \left[ \iint_ {\Omega} (\mid v _ {x} \mid^ {2} + \mid v _ {y} \mid^ {2}) \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2} \\ & \leqslant \| u \| _ {1} \| v \| _ {1}, \end{array}
$$

可见 $a(u, v)$ 是按 $H_0^1(\Omega)$ 的范数 $\| \cdot \|_1$ 有界的，至于双线性是显然的。由 §1 中例 4, $\mathcal{D}$ 在 $H_0^1(\Omega)$ 中稠密。所以 $a(u, v)$ 可以扩张成 $H_0^1(\Omega)$ 上的有界双线性泛函。

从这个例子及下节例 2, $H_0^1(\Omega)$ 上范数的引进, 正好把关于微分算子的 $-\Delta u$ 转化成作为 $H_0^1(\Omega)$ 上的有界双线性泛函的 $a(u,v)$ .

## § 4 Hilbert 共轭算子, Lax-Milgram 定理

## 1. Hilbert 共轭算子设 $H_{1}, H_{2}$ 都是 Hilbert 空间, $T$ 是从 $H_{1}$ 到 $H_{2}$ 的有界线性算子. 对 $H_{2}$ 中每个固定元 $y$ , 设

$$
f (x) = (T x, y), \text {当} x \in H _ {1},
$$

则 $f(x)$ 是 $H_{1}$ 上以 $x$ 为变元的连续线性泛函. 由 Fréchet-Riesz 表现定理, 恰有一个 $\hat{y} \in H_{1}$ , 使

$$
f (x) = (x, \hat {y}), \text {当} x \in H _ {1}.
$$

这个 $\hat{y}$ 是由 $f$ , 从而由 $y$ 唯一确定的. 人们定义

$$
T ^ {*} y = \hat {y}.
$$

容易验证 $T^{*}$ 是从 $H_{2}$ 到 $H_{1}$ 的有界线性算子. 称 $T^{*}$ 为 $T$ 的 Hilbert 共轭算子, 通常也称为 $T$ 的伴随算子.

由 $T^{*}$ 的定义可见

$$
(T x, y) = (x, T ^ {*} y), \quad \forall x \in H _ {1}, y \in H _ {2}.\tag{4.1}
$$

总之，对每个从 $H_{1}$ 到 $H_{2}$ 的有界线性算子 $T$ ，总存在一个从 $H_{2}$ 到 $H_{1}$ 的有界线性算子 $T^{*}$ 使(4.1)式成立.显然 $T^{*}$ 是由 $T$ 唯一确定的.

例 1 设 $\{e_{1},\cdots,e_{n}\}$ 是 $R^{n}$ 的一个正规正交基. A 是 $R^{n}$ 上线性算子, $A=(a_{ij})_{n\times n}$ 是 A 在 $\{e_{1},\cdots,e_{n}\}$ 上的矩阵表示, 则从基底与矩阵表示的关系,

$$
\left(\mathbf {A} e _ {1}, \dots , \mathbf {A} e _ {n}\right) = \left(e _ {1}, \dots , e _ {n}\right) \left( \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right),
$$

即

$$
\mathbf {A} e _ {j} = \sum_ {i = 1} ^ {n} a _ {i j} e _ {i}, \quad j = 1, \dots , n.
$$

(参见[2], 第 274 页) 从而对每个 $k, j = 1, \cdots, n$ .

$$
(\mathbf {A} ^ {*} e _ {k}, e _ {j}) = (e _ {k}, \mathbf {A} e _ {j}) = (e _ {k}, \sum_ {i = 1} ^ {n} a _ {i j} e _ {i}) = \overline {{{a}}} _ {k j}.
$$

故

(4.2)

$$
\mathbf {A} ^ {*} e _ {k} = \sum_ {j = 1} ^ {n} \bar {a} _ {k j} e _ {j}, \quad k = 1, \dots , n.
$$

设 $A^{*}$ 在 $\{e_{1},\cdots,e_{n}\}$ 上矩阵表示为 $A^{*}=(a_{jk}^{*})_{n\times n}$ ，即

$$
\mathbf {A} ^ {*} e _ {k} = \sum_ {j = 1} ^ {n} a _ {j k} ^ {*} e _ {j}, \quad k = 1, \dots , n.
$$

与(4.2)式相比较可见

$$
a _ {j k} ^ {*} = \bar {a} _ {k j}, j, k = 1, \dots , n.
$$

即

$$
A ^ {*} = \left( \begin{array}{c c c c} \bar {a} _ {1 1} & \bar {a} _ {2 1} & \dots & \bar {a} _ {n 1} \\ \bar {a} _ {1 2} & \bar {a} _ {2 2} & \dots & \bar {a} _ {n 2} \\ \vdots & \vdots & & \vdots \\ \bar {a} _ {1 n} & \bar {a} _ {2 n} & \dots & \bar {a} _ {n n} \end{array} \right).
$$

以下，用 $L(H)$ 表示Hilbert空间 $H$ 上全体有界线性算子的集合.设 $S, T \in L(H), \alpha \in \mathbf{C}$ ，定义

$$
\begin{array}{l} (S + T) x = S x + T x, \\ (\alpha T) x = \alpha (T x), \\ (S T) x = S (T x), \end{array}
$$

当 $x \in H$ . 容易验证, $S + T, \alpha T, ST \in L(H)$ .

定理4.1 设 $S, T \in L(H)$ , 则

(1) $(S + T)^{*} = S^{*} + T^{*}$ ;

(2) $(ST)^{*} = T^{*}S^{*}$ ;

(3) $(T^{*})^{*} = T;$

(4) 对常数 $\alpha \in \mathbf{C}, (\alpha T)^* = \overline{\alpha} T^*$ ;

(5) 若 $T$ 有界可逆, 则 $T^{*}$ 亦有界可逆, 且

$$
(T ^ {*}) ^ {- 1} = (T ^ {- 1}) ^ {*};
$$

(6) $\| T^{*}\| = \| T\|$ .

证 (1), (2) 容易验证. 至于 (3), 对任意 $x, y \in H$ , 由 (4.1) 式,

$$
(x, (T ^ {*}) ^ {*} y) = (T ^ {*} x, y) = (\overline {{y , T ^ {*} x}}) = (\overline {{T y , x}}) = (x, T y),
$$

故 $(T^{*})^{*} = T$

关于(4). 对任意 $x, y \in H$ ,

$$
\begin{array}{r l} (x, (\alpha T) ^ {*} y) & = ((\alpha T) x, y) \\ & = \alpha (T x, y) \\ & = \alpha (x, T ^ {*} y) \\ & = (x, \tilde {\alpha} (T ^ {*} y)) \\ & = (x, (\bar {\alpha} T ^ {*}) y), \end{array}
$$

故 $(\alpha T)^{*} = \overline{\alpha} T^{*}$

(5) 对任意 $x, y \in H$ ,

$$
(x, I ^ {*} y) = (I x, y) = (x, y),
$$

这说明对 $H$ 上恒等算子 $I$ , 有 $I^{*} = I$ . 由假设及第一章习题27,

$$
T T ^ {- 1} = T ^ {- 1} T = I.
$$

根据前面的(2)，

$$
\begin{array}{l} T ^ {*} (T ^ {- 1}) ^ {*} = (T ^ {- 1} T) ^ {*} = I ^ {*} = I, \\ (T ^ {- 1}) ^ {*} T ^ {*} = (T T ^ {- 1}) ^ {*} = I ^ {*} = I. \end{array}
$$

再由第一章习题27, 知 $T^{*}$ 是有界可逆的, 且

$$
\left(T ^ {*}\right) ^ {- 1} = \left(T ^ {- 1}\right) ^ {*}.
$$

最后来证明(6).从

$$
\| T x \| = \sup _ {\| y \| \leqslant 1} | (T x, y) |,
$$

(见习题11)可见

$$
\begin{array}{r l} \| T \| & = \sup _ {\| x \| \leqslant 1} \| T x \| \\ & = \sup _ {\| x \| \leqslant 1} \sup _ {\| y \| \leqslant 1} | (T x, y) | \\ & = \sup _ {\| y \| \leqslant 1} \sup _ {\| x \| \leqslant 1} | (x, T ^ {*} y) | \\ & = \sup _ {\| y \| \leqslant 1} \| T ^ {*} y \| \\ & = \| T ^ {*} \|. \end{array}
$$

证毕.

设 $H_{1}$ 与 $H_{2}$ 都是Hilbert空间， $A$ 是从 $H_{1}$ 到 $H_{2}$ 的有界线性算子，引进如下记号：

$$
N (A) \stackrel {\mathrm{d}} {=} \left\{x \in H _ {1}: A x = 0 \right\},
$$

称为 $A$ 的零空间. 仍用 $R(A)$ 表示 $A$ 的值域, 即

$$
R (A) \stackrel {\mathrm{d}} {=} \left\{y \in H _ {2}: y = A x, x \in H _ {1} \right\}.
$$

定理4.2 在上述假设下，

$$
\begin{array}{l l} {N (A) = R (A ^ {*}) ^ {\perp},} & {N (A ^ {*}) = R (A) ^ {\perp},} \\ {\overline {{{R (A)}}} = N (A ^ {*}) ^ {\perp},} & {\overline {{{R (A ^ {*})}}} = N (A) ^ {\perp}.} \end{array}
$$

证设 $x \in N(A)$ , 则 $Ax = 0$ . 从而对任意 $y \in H_2$ ,

$$
(x, A ^ {*} y) = (A x, y) = 0.
$$

这说明， $x\in R(A^{*})^{\perp}$

如果 $x \in R(A^{*})^{\perp}$ , 则对任意 $y \in H_{2}$ ,

$$
(A x, y) = (x, A ^ {*} y) = 0.
$$

故 $Ax = 0$ ，即 $x\in N(A)$ .总之

$$
N (A) = R \left(A ^ {*}\right) ^ {\perp}.
$$

根据命题3.1，

$$
\overline {{{R (A ^ {*})}}} = (R (A ^ {*}) ^ {\perp}) ^ {\perp} = N (A) ^ {\perp}.
$$

其他两个等式可以类似证明.

## 2. Lax-Milgram 定理定理 4.3(Lax-Milgram 定理,1954) 设 $B(f,g)$ 是 Hilbert 空间 H 上有界的共轭双线性泛函,且有正的常数 r,使

$$
| B (f, f) | \geqslant r \| f \| ^ {2}, \text {当} f \in H.\tag{4.3}
$$

则于 $H$ 上任给的有界线性泛函 $\iota$ , 恰有一个 $g_0 \in H$ , 使

$$
l (f) = B \left(f, g _ {0}\right), \quad \forall f \in H,
$$

且

$$
\| g _ {0} \| \leqslant \frac {1}{r} \| l \|.
$$

这个定理也是关于连续线性泛函的表达式, 只不过把 Fréchet-Riesz 表现定理中的内积推广为满足控制条件(4.3)的有界共轭双线性泛函 $B(f,g)$ 而已, 但是这个貌不惊人的推广在偏微分方程之适定性的研究中却是很有用的.

证由定理3.3, 存在有界线性算子 $T$ , 使

$$
B (f, g) = (T f, g) = (f, T ^ {*} g), \quad \forall f, \quad g \in H.
$$

由(4.3)有

$$
r \parallel f \parallel^ {2} \leqslant | B (f, f) | = | (f, T ^ {*} f) | \leqslant \parallel f \parallel \parallel T ^ {*} f \parallel , \quad \forall f \in H.
$$

即

$$
r \parallel f \parallel \leqslant \parallel T ^ {*} f \parallel , \quad \forall f \in H.\tag{4.4}
$$

由此可见 $T^{*}$ 是单射的，从而 $(T^{*})^{-1}$ 存在.

往证 $T^{*}$ 的值域 $R(T^{*}) = H$ . 由(4.4)可见 $R(T^{*})$ 是闭子空间. 若 $R(T^{*}) \neq H$ . 根据射影定理有非零的 $\varphi \in H$ 与 $R(T^{*})$ 中每个元正交, 从而

$$
0 = \mid (\varphi , T ^ {*} \varphi) \mid = \mid B (\varphi , \varphi) \mid \geqslant r \parallel \varphi \parallel^ {2}.
$$

这导致 $\varphi = 0$ ，矛盾.故 $R(T^{*}) = H.$ 从而 $(T^{*})^{-1}$ 是从 $H$ 到 $H$ 的线性算子.

根据 Fréchet-Riesz 表现定理, 对 $H$ 上有界线性泛函 $\ell$ , 存在唯一的 $u \in H$ , 使

$$
l (f) = (f, u), \text {当} f \in H,
$$

且 $\| l\| = \| u\|$ .于是欲使 $l(f) = B(f,g_0),\forall f\in H$ ，即

$$
(f, u) = (f, T ^ {*} g _ {0}), \forall f \in H.
$$

必须且只须 $u = T^{*}g_{0}$ ，即 $g_{0} = (T^{*})^{-1}u.$ 从(4.4)式，

$$
\| g _ {0} \| \leqslant \frac {1}{r} \| T ^ {*} g _ {0} \| = \frac {1}{r} \| u \| = \frac {1}{r} \| t \|.
$$

至于 $g_{0}$ 的唯一性从 $\pmb{u}$ 的唯一性及 $T^{*}$ 是有逆的得出. 证毕.

推论(Lax-Milgram) 设 $A$ 是 $H$ 上有界线性算子，

$$
a (u, v) = (A u, v), \quad u, v \in H,
$$

满足

(4.5)

$$
\mid a (u, u) \mid \geqslant r \| u \| ^ {2}, \quad \forall u \in H,
$$

其中 $r$ 是正的常数，则 $A$ 是有界可逆的.

证如定理 4.3 的证明, 相应那里的 $B(f, g) = (Tf, g)$ , 现在是 $a(u, v) = (Au, v)$ . 根据 $R(A^{*}) = H$ 及 (4.5) 式知 $A^{*}$ 是双射的, 而且

$$
\parallel (A ^ {*}) ^ {- 1} u \parallel \leqslant \frac {1}{r} \parallel u \parallel , \text {当} u \in H,
$$

即 $(A^{*})^{-1}$ 是有界的. 根据定理4.1的(5), $A = (A^{*})^{*}$ 也是有界可逆的. 证毕.

例2 考察Dirichlet零边值问题

$$
\left\{ \begin{array}{l} - \Delta u = f, \\ u | _ {\partial \Omega} = 0. \end{array} \right.\tag{4.6}
$$

这里 $\Omega$ 是复平面上有界区域， $\partial \Omega$ 表示 $\Omega$ 的边界，

$$
\Delta u = \frac {\partial^ {2} u}{\partial x ^ {2}} + \frac {\partial^ {2} u}{\partial y ^ {2}}, \text {当} u \in C ^ {2} (\Omega),
$$

$f\in L^{2}(\Omega)$ .设

$\mathcal{D} = \{v: v \in C^2(\Omega)$ 是实值的，且 $v|_{\partial \Omega} = 0\}$ .

对 $u, v \in \mathcal{D}$ , 从 Green 公式

$$
\begin{array}{l} \iint_ {\Omega} (- \Delta u) v \mathrm{d} x \mathrm{d} y \\ = \iint_ {\Omega} \nabla u \cdot \nabla v \mathrm{d} x \mathrm{d} y - \int_ {\partial \Omega} \frac {\partial u}{\partial n} v \mathrm{d} \sigma \\ = \iint_ {\Omega} \nabla u \cdot \nabla v \mathrm{d} x \mathrm{d} y, \end{array}
$$

这里 $\nabla u\cdot \nabla v = u_xv_x + u_yv_y$ .于是从(4.6)的第一式有方程

$$
\iint_ {\Omega} \nabla u \cdot \nabla v \mathrm{d} x \mathrm{d} y = \iint_ {\Omega} f v \mathrm{d} x \mathrm{d} y, u, v \in \mathscr {D}.\tag{4.7}
$$

考察双线性泛函

$$
\begin{array}{r l} a (u, v) & = \iint_ {\Omega} \nabla u \cdot \nabla v \mathrm{d} x \mathrm{d} y \\ & = \iint_ {\Omega} (u _ {x} v _ {x} + u _ {y} v _ {y}) \mathrm{d} x \mathrm{d} y. \end{array}
$$

如 §3 中例 2, 已经证明它是实的 $C_0^1(\Omega)$ 上按 $H_0^1(\Omega)$ 的范数 $\| \cdot \|_1$ 有界的双线性泛函, 故可将 $a(u, v)$ 扩张到 $H_0^1(\Omega)$ 上, 而有 (4.7) 扩张后的方程

$$
a (u, v) = \iint_ {\Omega} f v \mathrm{d} x \mathrm{d} y = (f, v) _ {L ^ {2} (\Omega)}, u, v \in H _ {0} ^ {1} (\Omega).\tag{4.8}
$$

定义4.1 若有 $u \in H_0^1(\Omega)$ , 使

$$
a (u, v) = (f, v) _ {L ^ {2} (\Omega)}, \quad \forall v \in H _ {0} ^ {1} (\Omega),
$$

则称 u 为边值问题(4.6)的广义解.

为什么说它是广义解呢？因为 u 未必在 D 内。还该指出，从 $u \in H_{0}^{1}(\Omega)$ 的定义，应该有 $\varphi_{j} \in C_{0}^{1}(\Omega), j = 1, 2, \cdots$ ，按 $(\cdot, \cdot)_{1}$ 定义的范数收敛到 u。因此可以说，上述的 u“粗糙地”满足边界条件

$$
u \mid_ {\partial \Omega} = 0.
$$

注意 $H_0^1 (\Omega)$ 的范数

$$
\| u \| _ {1} = \left[ \iint_ {\Omega} \left(u ^ {2} + u _ {x} ^ {2} + u _ {y} ^ {2}\right) \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2} \geqslant \left[ \iint_ {\Omega} u ^ {2} \mathrm{d} x \mathrm{d} y \right] ^ {1 / 2} = \| u \| _ {L ^ {2} (\Omega)}.
$$

故 $(v, f)_{L^2(\Omega)}$ 也是 $H_0^1(\Omega)$ 上的以 $v$ 为变量的有界线性泛函，从而由 Fréchet-Riesz 表现定理，可以像 $T$ 之共轭算子 $T^*$ 一样定义从 $L^2(\Omega)$ 到 $H_0^1(\Omega)$ 上有界线性算子 $K$ 使

$$
(v, f) _ {L ^ {2} (\Omega)} = (v, K f) _ {1}, v \in H _ {0} ^ {1} (\Omega).
$$

而从定理3.3,则应有 $J \in L(H_0^1(\Omega))$ ，使

$$
a (u, v) = (J u, v) _ {1}, u, v \in H _ {0} ^ {1} (\Omega).
$$

现在方程(4.8)便可改写成

$$
(J u, v) _ {1} = (K f, v) _ {1}, \quad \forall v \in H _ {0} ^ {1} (\Omega).
$$

即

(4.9)

$$
J u = K f.
$$

从Friedrichs不等式([12],第117—118页)

$$
\mid a (u, u) \mid = \iint_ {\Omega} (u _ {x} ^ {2} + u _ {y} ^ {2}) \mathrm{d} x \mathrm{d} y \geqslant \chi \iint_ {\Omega} u ^ {2} \mathrm{d} x \mathrm{d} y,
$$

(这里 $\chi$ 是正的常数) 可得

$$
\left[ 1 + \frac {1}{\chi} \right] | a (u, u) | \geqslant \iint_ {\Omega} \left(u _ {x} ^ {2} + u _ {y} ^ {2}\right) \mathrm{d} x \mathrm{d} y + \iint_ {\Omega} u ^ {2} \mathrm{d} x \mathrm{d} y = \| u \| _ {1} ^ {2}.
$$

因此， $a(u,v)$ 满足定理4.3之推论中的控制条件，于是 $J$ 是有界可逆的.亦即上述边值问题的广义解存在且唯一，并且还是稳定的.

## 3. 可分 Hilbert 空间上有界线性算子的矩阵表达式以下总设 H 是可分无穷维的 Hilbert 空间， $\varphi_{1},\varphi_{2},\cdots,\varphi_{n},\cdots$ 是 H 上的正规正交基。任给 $x\in H$ ，则 x 可唯一地表成

$$
x = \sum_ {k = 1} ^ {\infty} \xi_ {k} \varphi_ {k},
$$

这里

$$
\xi_ {k} = (x, \varphi_ {k})
$$

称为 $x$ 对于坐标架 $\{\varphi_n\}_{n=1}^{\infty}$ 的第 $k$ 个坐标. 又

$$
\sum_ {k = 1} ^ {\infty} \mid \xi_ {k} \mid^ {2} = \parallel x \parallel^ {2} <   \infty ,
$$

即 $\{\xi_k\}_{k=1}^{\infty}\in l^2$

设 $y = \sum_{k=1}^{\infty} \zeta_k \varphi_k \in H$ ，则有内积表达式(见习题3)

(4.10)

$$
(x, y) = \sum_ {k = 1} ^ {\infty} \xi_ {k} \bar {\zeta} _ {k}.
$$

对 $A \in L(H)$ , 显然 $Ax = \sum_{k=1}^{\infty} \xi_k A \varphi_k$ , 从而 $Ax$ 的第 $n$ 个坐标为

$$
(A x, \varphi_ {n}) = \sum_ {k = 1} ^ {\infty} \xi_ {k} (A \varphi_ {k}, \varphi_ {n}) = \sum_ {k = 1} ^ {\infty} a _ {n k} \xi_ {k},
$$

这里

$$
a _ {n k} = \left(A \varphi_ {k}, \varphi_ {n}\right), \quad n = 1, 2, \dots .\tag{4.11}
$$

一般称 $(a_{nk})_{n,k = 1,2,\dots}$ （以下简写成 $(a_{nk})$ )为算子 $A$ 关于坐标架 $\{\varphi_n\}_{n = 1}^{\infty}$ 的矩阵.

同样对 $A$ 的共轭算子 $A^{*}$ , 与之相应的矩阵元便是

(4.12)

$$
a _ {n k} ^ {*} = \left(A ^ {*} \varphi_ {k}, \varphi_ {n}\right) = \left(\varphi_ {k}, A \varphi_ {n}\right) = \overline {{\left(A \varphi_ {n} , \varphi_ {k}\right)}} = \bar {a} _ {k n}.
$$

由定理2.3

$$
\sum_ {n = 1} ^ {\infty} \mid a _ {n k} \mid^ {2} = \sum_ {n = 1} ^ {\infty} \mid (A \varphi_ {k}, \varphi_ {n}) \mid^ {2} = \| A \varphi_ {k} \| ^ {2} <   \infty .
$$

同样

$$
\sum_ {n = 1} ^ {\infty} \mid a _ {k n} \mid^ {2} = \sum_ {n = 1} ^ {\infty} \mid a _ {n k} ^ {*} \mid^ {2} = \parallel A ^ {*} \varphi_ {k} \parallel^ {2} <   \infty .
$$

总之，无穷矩阵 $(a_{nk})$ 的列向量与行向量都是 $t^2$ 中的元素.

设算子 $A, B \in L(H)$ 关于坐标架 $\{\varphi_k\}_{k=1}^{\infty}$ 的矩阵依次为 $(a_{ij}), (b_{ij})$ . 考察 $C = BA$ 关于坐标架 $\{\varphi_k\}_{k=1}^{\infty}$ 的矩阵. 从

$$
c _ {i k} = (C \varphi_ {k}, \varphi_ {i}) = (B A \varphi_ {k}, \varphi_ {i}) = (A \varphi_ {k}, B ^ {*} \varphi_ {i}),
$$

与

$$
A \varphi_ {k} = \sum_ {n = 1} ^ {\infty} (A \varphi_ {k}, \varphi_ {n}) \varphi_ {n},
$$

$$
B ^ {*} \varphi_ {i} = \sum_ {n = 1} ^ {\infty} (B ^ {*} \varphi_ {i}, \varphi_ {n}) \varphi_ {n},
$$

由公式(4.10)以及(4.11)与(4.12)式,得

$$
\left(A \varphi_ {k}, B ^ {*} \varphi_ {i}\right) = \sum_ {n = 1} ^ {\infty} \left(A \varphi_ {k}, \varphi_ {n}\right) \overline {{\left(B ^ {*} \varphi_ {i} , \varphi_ {n}\right)}} = \sum_ {n = 1} ^ {\infty} a _ {n k} \bar {b} _ {n i} ^ {*} = \sum_ {n = 1} ^ {\infty} a _ {n k} b _ {i n},
$$

于是乘积 $C = BA$ 关于坐标架 $\{\varphi_j\}_{j=1}^{\infty}$ 的矩阵元为

$$
c _ {i k} = \sum_ {n = 1} ^ {\infty} b _ {i n} a _ {n k}.
$$

这与普通矩阵乘法的公式极相似.

## 习题

1. 设 $X$ 是内积空间, $x, y \in X$ 都是非零元, 试证明:

(i) 如果 $x$ 与 $y$ 正交, 则 $x$ 与 $y$ 线性无关;

(ii) $x$ 与 $y$ 正交的充要条件是对任意数 $\alpha$ ,

$$
\| x + \alpha y \| = \| x - \alpha y \|;
$$

(iii) $x$ 与 $y$ 正交的充要条件是对任意数 $\alpha$ ,

$$
\| x + \alpha y \| \geqslant \| x \|.
$$

2. 设 $\{e_n\}_{n=1}^{\infty}$ 是内积空间 $X$ 中的正规正交集, 则对任意 $x, y \in X$ ,

$$
\sum_ {n = 1} ^ {\infty} \mid (x, e _ {n}) (y, e _ {n}) \mid \leqslant \| x \| \| y \|.
$$

3. 设 $\{e_n\}_{n=1}^{\infty}$ 是 Hilbert 空间 $H$ 中的正规正交集，

$$
x = \sum_ {n = 1} ^ {\infty} \alpha_ {n} e _ {n}, \quad y = \sum_ {n = 1} ^ {\infty} \beta_ {n} e _ {n}.
$$

试证明

$$
(x, y) = \sum_ {n = 1} ^ {\infty} \alpha_ {n} \bar {\beta} _ {n},
$$

且右端级数绝对收敛.

4. 设 $\{e_n\}_{n=1}^{\infty}$ 是可分 Hilbert 空间 $H$ 的正规正交基. 证明: 任给 $x, y \in H$ ,

$$
(x, y) = \sum_ {n = 1} ^ {\infty} (x, e _ {n}) (\overline {{y , e _ {n}}}),
$$

且右端级数绝对收敛.

5. 设 $D$ 是 $\mathbf{R}^n$ 中一个区域. 令 $L^2(D)$ 表示所有的 $D$ 上平方可积的复值函数 $f(x)$ 按逐点定义的加法和数乘形成的线性空间, 设

$$
(f, g) = \int_ {D} f (x) \overline {{{{g (x)}}}} \mathrm{d} x, \text {当} f, g \in L ^ {2} (D).
$$

试证明: $L^{2}(D)$ 按如上定义的内积是一个 Hilbert 空间.

6. 证明: $l^p (p \neq 2)$ 不可能是内积空间.

7. 设 $\{u_{n}\}$ 是线性无关的, 验证按 Schmidt 正规正交法(2.1)得到的集 $\{v_{n}\}$ 是正规正交集.

8. 证明射影定理(定理3.1)中的唯一性.

9. 设 $M$ 是 Hilbert 空间 $H$ 的一个线性流形. 证明：

(i) $M^{\perp}$ 是 $H$ 的子空间.

(ii) $(\overline{M})^{\perp} = M^{\perp}$ .

(iii) 如果 $M_{1}$ 也是 $H$ 的线性流形, 使 $M \subset M_{1}$ , 则 $M_{1}^{\perp} \subset M^{\perp}$ .

10. 试证明 $H^{*}$ 按如下范数：

$$
\| f \| = \sup _ {\| x \| \leqslant 1} | f (x) |, \quad \text {当} f \in H ^ {*},
$$

是完备的赋范线性空间.

11. 证明: 对任意的 $x \in H$ ,

$$
\| x \| = \sup _ {\| y \| \leqslant 1} | (x, y) |.
$$

12. 验证定理 3.3 中的 A 是 H 上有界线性算子.

13. 设 $\{e_n\}_{n=1}^{\infty}$ 是 Hilbert 空间 $H$ 中一个正规正交集, 如果对每个 $x \in H$ ,

$$
\| x \| ^ {2} = \sum_ {n = 1} ^ {\infty} | (x, e _ {n}) | ^ {2},
$$

称 $\{e_n\}_{n=1}^{\infty}$ 是完备的.

设 $\{e_n\}_{n=1}^{\infty}, \{f_n\}_{n=1}^{\infty}$ 是 $H$ 中的两个正规正交集, 适合

$$
\sum_ {n = 1} ^ {\infty} \left\| e _ {n} - f _ {n} \right\| ^ {2} <   1.
$$

试证明： $\{e_n\}_{n = 1}^{\infty}$ 是完备的当且仅当 $\{f_n\}_{n = 1}^{\infty}$ 是完备的.

14. 设 $T$ 是从 Hilbert 空间 $H_{1}$ 到 $H_{2}$ 的有界线性算子, 证明 $T^{*}$ 是从 $H_{2}$ 到 $H_{1}$ 的有界线性算子.

15. 设 $T$ 是 Hilbert 空间 $H$ 上有界线性算子. 试证明: 若对一切 $x \in H$ , $\operatorname{Re}(Tx, x) = 0$ , 则 $T + T^{*} = 0$ .

16. 设 $T$ 是 $\ell^2$ 上的有界线性算子：

$$
T: x = (\xi_ {1}, \xi_ {2}, \dots , \xi_ {n}, \dots) \rightarrow T x = (\eta_ {1}, \eta_ {2}, \dots , \eta_ {n}, \dots),
$$

其中

$$
\eta_ {n} = \sum_ {k = 1} ^ {\infty} a _ {n k} \xi_ {k}, n = 1, 2, \dots .
$$

又设 $T^{*}$ 是 $T$ 的伴随算子：

$$
T ^ {*}: x = \left(\xi_ {1}, \xi_ {2}, \dots , \xi_ {n}, \dots\right)\rightarrow T ^ {*} x = \left(\eta_ {1} ^ {*}, \eta_ {2} ^ {*}, \dots , \eta_ {n} ^ {*}, \dots\right),
$$

而且

$$
\eta_ {n} ^ {*} = \sum_ {k = 1} ^ {\infty} a _ {n k} ^ {*} \xi_ {k}, \quad n = 1, 2, \dots .
$$

试证明：

$$
a _ {n k} ^ {*} = \bar {a} _ {k n}, n, k = 1, 2, \dots .
$$

# 第三章 Banach 空间上的有界线性算子

## § 1 有界线性算子

## 1. 算子的范数在第一章 §7 中我们引进了有界线性算子的概念. 设 $X, Y$ 是赋范线性空间, 以下记从 $X$ 到 $Y$ 的全体有界线性算子的集合为 $L(X, Y)$ , 而 $L(X, X)$ 简记为 $L(X)$ . 设 $A \in L(X, Y)$ , 我们知道 $A$ 的范数为

$$
\| A \| = \sup _ {\| x \| = 1} \| A x \| = \sup _ {\| x \| \leqslant 1} \| A x \| = \sup _ {x \neq 0} \frac {\| A x \|}{\| x \|}.
$$

诚如 L. Garding 所说：“事实证明，范数是一个强有力的工具，我们可以利用它干一大堆事情。”([1], 第 112 页)

例1 设 $K(s, t)$ 是 $0 \leqslant s, t \leqslant 1$ 上的连续函数，则 $C[0, 1]$ 上的积分算子

$$
(A x) (s) = \int_ {0} ^ {1} K (s, t) x (t) \mathrm{d} t, x = x (s) \in C [ 0, 1 ],
$$

的范数为

$$
\| A \| = \sup _ {0 \leqslant s \leqslant 1} \int_ {0} ^ {1} | K (s, t) | \mathrm{d} t.
$$

事实上，令

$$
M = \sup _ {0 \leqslant s \leqslant 1} \int_ {0} ^ {1} | K (s, t) | \mathrm{d} t.
$$

由于

$$
\begin{array}{r l} | (A x) (s) | & \leqslant \int_ {0} ^ {1} | K (s, t) | | x (t) | \mathrm{d} t \\ & \leqslant \| x \| \int_ {0} ^ {1} | K (s, t) | \mathrm{d} t, \end{array}
$$

故

$$
\begin{array}{r l} \parallel A x \parallel & = \sup _ {0 \leqslant s \leqslant 1} | (A x) (s) | \\ & \leqslant \parallel x \parallel \sup _ {0 \leqslant s \leqslant 1} \int_ {0} ^ {1} | K (s, t) | \mathrm{d} t \\ & = M \parallel x \parallel , \end{array}
$$

可见 $\| A\| \leqslant M$

另一方面， $\int_0^1 |K(s,t)|\mathrm{d}t$ 是 $0\leqslant s\leqslant 1$ 上的连续函数，因此有[0,1]上的点

$s_0$ ，使 $\int_0^1 |K(s_0,t)|\mathrm{d}t = M.$ 令

$$
k _ {0} (t) = \mathrm{sgn} K (s _ {0}, t) ^ {(1)}, 0 \leqslant t \leqslant 1.
$$

则 $k_{0}(t)$ 是 $[0,1]$ 上模不超过1的可测函数，且

$$
\int_ {0} ^ {1} K (s _ {0}, t) k _ {0} (t) \mathrm{d} t = \int_ {0} ^ {1} | K (s _ {0}, t) | \mathrm{d} t = M.
$$

根据 $\mathcal{L}\mathcal{Y}\mathcal{U}\mathcal{Z}\mathcal{H}$ 定理，对任何 $\delta > 0$ ，有[0,1]上连续函数 $x(t)$ ，使 $|x(t)| \leqslant 1$ 且

$$
m (\{t \in [ 0, 1 ]: x (t) \neq k _ {0} (t) \}) <   \delta .
$$

对任给 $\varepsilon > 0$ ，令 $\delta = \frac{\varepsilon}{2C}$ ，这里 $C = \sup_{0 \leqslant s, t \leqslant 1} |K(s, t)|$ ，由上述便有 $x \in C[0,1]$ ，使 $\| x \| \leqslant 1$ ，且 $E = \{t \in [0,1] : x(t) \neq k_0(t)\}$ 的测度 $mE$ 小于 $\delta$ ，从而

$$
\left| \int_ {0} ^ {1} K (s _ {0}, t) [ x (t) - k _ {0} (t) ] \mathrm{d} t \right| = \left| \int_ {E} K (s _ {0}, t) [ x (t) - k _ {0} (t) ] \mathrm{d} t \right| \leqslant 2 C m E <   \varepsilon .
$$

于是

$$
\begin{array}{r l} \mid (A x) (s _ {0}) \mid & = \left| \int_ {0} ^ {1} K (s _ {0}, t) x (t) \mathrm{d} t \right| \\ & = \left| \int_ {0} ^ {1} K (s _ {0}, t) k _ {0} (t) \mathrm{d} t + \int_ {0} ^ {1} K (s _ {0}, t) [ x (t) - k _ {0} (t) ] \mathrm{d} t \right| \\ & \geqslant \int_ {0} ^ {1} | K (s _ {0}, t) | \mathrm{d} t - \left| \int_ {0} ^ {1} K (s _ {0}, t) [ x (t) - k _ {0} (t) ] \mathrm{d} t \right|, \\ & \geqslant M - \varepsilon . \end{array}
$$

从而

$$
\| A x \| \geqslant M - \varepsilon .
$$

因为 $\| x\| \leqslant 1$ ，所以 $\| A\| \geqslant M - \varepsilon .$ 而 $\varepsilon$ 是任意的，故 $\| A\| \geqslant M$ ，总之 $\| A\| = M.$

命题1.1 若 $A, B \in L(X, Y), \alpha$ 是常数，则 $A + B, \alpha A \in L(X, Y)$ ，而且

$$
\| A + B \| \leqslant \| A \| + \| B \|, \| \alpha A \| = | \alpha | \| A \|.
$$

此外， $\| A \| = 0$ 当且仅当 $A = 0$ ，从而 $L(X, Y)$ 按算子范数是赋范线性空间.

这里 $A + B, \alpha A$ 是逐点定义的：

$$
(A + B) x = A x + B x, (\alpha A) x = \alpha (A x), \forall x \in X.
$$

证由算子范数定义，

$$
\begin{array}{r l} \left\| A + B \right\| & = \sup _ {\| x \| = 1} \left\| (A + B) x \right\| \\ & \leqslant \sup _ {\| x \| = 1} \left(\left\| A x \right\| + \left\| B x \right\|\right) \end{array}
$$

$$
\begin{array}{l} \leqslant \sup _ {\| x \| = 1} \| A x \| + \sup _ {\| x \| = 1} \| B x \| \\ = \| A \| + \| B \|. \end{array}
$$

其他结果由范数定义也不难证明.

命题 1.2 设 X 是赋范线性空间, Y 是 Banach 空间, 则 $L(X, Y)$ 也是 Banach 空间.

证由命题1.1, 只须证明 $L(X, Y)$ 是完备的. 设 $\{A_n\}_{n=1}^{\infty}$ 是 $L(X, Y)$ 中Cauchy序列, 则对任何 $x \in X$ , 从

$$
\parallel A _ {n} x - A _ {m} x \parallel \leqslant \parallel A _ {n} - A _ {m} \parallel \parallel x \parallel ,
$$

可见 $\left\{A_{n}x\right\}_{n=1}^{\infty}$ 是Y中Cauchy序列.而Y是完备的,故有唯一的 $y\in Y$ ,使 $\lim_{n\to\infty}A_{n}x=y$ .现在定义Ax=y.易见A是线性的.因为赋范线性空间的Cauchy序列是有界的(参见第一章习题6),故存在常数M>0,使 $\|A_{n}\|\leqslant M$ , $n=1,2,\cdots$ .则

$$
\| A x \| = \lim _ {n \rightarrow \infty} \| A _ {n} x \| \leqslant \lim _ {n \rightarrow \infty} \| A _ {n} \| \| x \| \leqslant M \| x \|.
$$

可见 $A \in L(X, Y)$ . 又

$$
\begin{array}{r l}\| A _ {n} - A \|&= \sup _ {\| x \| = 1} \| (A _ {n} - A) x \|\\&= \sup _ {\| x \| = 1} \lim _ {m \rightarrow \infty} \| (A _ {n} - A _ {m}) x \|\\&= \lim _ {m \rightarrow \infty} \sup _ {\| x \| = 1} \| (A _ {n} - A _ {m}) x \|\\&= \lim _ {m \rightarrow \infty} \| A _ {n} - A _ {m} \| \rightarrow 0,\end{array}
$$

当 $n\to \infty$ .证毕.

对于 Banach 空间 X, $L(X)$ 不仅是 Banach 空间, 而且是个代数(关于“代数”这个概念, 参见 [18], V.1.3). 因为对任何 A, $B \in L(X)$ , 可如下定义乘法:

$$
(A B) x = A (B x), \text {当} x \in X.
$$

容易证明命题1.3 设 $A, B \in L(X)$ , 则 $AB \in L(X)$ , 且

$$
\| A B \| \leqslant \| A \| \| B \|.
$$

特别,对任意正整数 n

$$
\| A ^ {n} \| \leqslant \| A \| ^ {n}.
$$

定义1.1 设 $\| \cdot \|_1$ 与 $\| \cdot \|_2$ 都是线性空间 $X$ 上的范数，如果对 $X$ 中任意点列 $\{x_n\}_{n=1}^{\infty}$ ， $\| x_n \|_1 \to 0$ 蕴含 $\| x_n \|_2 \to 0$ ，则称范数 $\| \cdot \|_1$ 强于 $\| \cdot \|_2$ 。如果两个范数中任何一个都强于另一个，则称它们是等价的范数。

考察从 $\langle X, \| \cdot \|_1 \rangle$ 到 $\langle X, \| \cdot \|_2 \rangle$ 的恒等映射 $I$ , 即

$$
I x = x, \forall x \in X.
$$

则所谓范数 $\| \cdot \|_1$ 强于 $\| \cdot \|_2$ ，实即 $I$ 为连续线性算子。从而存在常数 $\mu > 0$ ，使

$$
\| x \| _ {2} = \| I x \| _ {2} \leqslant \mu \| x \| _ {1}, \forall x \in X.
$$

由此我们容易得到命题1.4 线性空间 $X$ 上的范数 $\| \cdot \|_1$ 与 $\| \cdot \|_2$ 等价的充分必要条件是存在正数 $r_1, r_2$ 使

$$
r _ {1} \leqslant \frac {\parallel x \parallel_ {2}}{\parallel x \parallel_ {1}} \leqslant r _ {2}, \text {当} x \neq 0.
$$

## 2. 算子的逆数学中的众多问题导致寻求 $Ax = y$

这样方程的解,这里 A 是从赋范线性空间 X 到 Y 的线性算子.当 A 是单射的时候,如同在常微分方程论中常要讨论解的稳定性那样,我们还要问解 $A^{-1}y$ 关于 y 是否连续?

命题1.5 设 $X, Y$ 都是赋范线性空间, $A: X \to Y$ 是线性映射. 那么 $A$ 是单射的, 且定义在 $R(A)$ 上的算子 $A^{-1}$ 是连续的充分必要条件是存在常数 $m > 0$ 使 $\|Ax\| \geqslant m \|x\|$ , $\forall x \in X$ .

证先证充分性. 显然 $Ax = 0$ 蕴含 $x = 0$ , 故 $A$ 是单射的, 从而 $A^{-1}$ 是定义在 $R(A)$ 上的线性映射. 设 $y = Ax$ , 则 $x = A^{-1}y$ . 由假设 $\| y \| \geqslant m \| A^{-1}y \|$ , 足见 $A^{-1}$ 是有界的.

条件还是必要的. 否则, 对每个正整数 $n$ , 有 $x_{n} \in X$ , 使

$$
\| A x _ {n} \| <   \frac {1}{n} \| x _ {n} \|.
$$

设 $y_{n} = Ax_{n}$ ，则

$$
\| y _ {n} \| <   \frac {1}{n} \| A ^ {- 1} y _ {n} \|.
$$

可见 $A^{-1}$ 不是有界的，与假设 $A^{-1}$ 是连续的矛盾. 证毕.

定理1.1 设 $X$ 为Banach空间， $A \in L(X)$ ，且 $\| A \| < 1$ ，则 $I - A$ 是有界可逆的，且

$$
\begin{array}{r l} (I - A) ^ {- 1} & = \sum_ {n = 0} ^ {\infty} A ^ {n}, \\ \| (I - A) ^ {- 1} \| & \leqslant \frac {1}{1 - \| A \|}. \end{array}
$$

这里 $A^0 = I$ 是恒等算子.

证从 $\| A^n \| \leqslant \| A \|^n, n = 1,2,\dots, \| A \| < 1$ ，以及 $L(X)$ 为 Banach 空间，可知

$$
\sum_ {n = 0} ^ {\infty} A ^ {n} = I + A + A ^ {2} + \dots
$$

按算子范数收敛,且其和在 $L(X)$ 中.注意,对任意正整数 n .

$$
\begin{array}{r l} (I - A) (I + A + \dots + A ^ {n}) & = (I + A + \dots + A ^ {n}) (I - A) \\ & = I - A ^ {n + 1}, \end{array}
$$

而且 $\| A^{n + 1}\| \to 0$ ，当 $n\to \infty$ .令 $n\to \infty$ ，上式成为

$$
(I - A) \left(\sum_ {n = 0} ^ {\infty} A ^ {n}\right) = \left(\sum_ {n = 0} ^ {\infty} A ^ {n}\right) (I - A) = I.
$$

由第一章习题27, 可知 $I - A$ 是有界可逆的, 且

$$
(I - A) ^ {- 1} = \sum_ {n = 0} ^ {\infty} A ^ {n}.
$$

从而

$$
\| (I - A) ^ {- 1} \| = \left\| \sum_ {n = 0} ^ {\infty} A ^ {n} \right\| \leqslant \sum_ {n = 0} ^ {\infty} \| A \| ^ {n} = \frac {1}{1 - \| A \|}.
$$

证毕.

例2 考察积分方程

$$
f (x) - \int_ {0} ^ {1} K (x, y) f (y) \mathrm{d} y = g (x),\tag{1.1}
$$

这里 $K(x,y)$ 在 $0 \leqslant x, y \leqslant 1$ 上连续， $g \in C[0,1]$ .

引进算子

$$
(A f) (x) = \int_ {0} ^ {1} K (x, y) f (y) \mathrm{d} y, f \in C [ 0, 1 ].
$$

则(1.1)式可写成

(1.2)

$$
(I - A) f = g.
$$

根据定理1.1及例1,若

$$
\| A \| = \sup _ {0 \leqslant x \leqslant 1} \int_ {0} ^ {1} | K (x, y) | d y <   1,
$$

则方程(1.2)对任意 $g \in C[0,1]$ 都恰有一解

$$
f = (I - A) ^ {- 1} g = \sum_ {n = 0} ^ {\infty} A ^ {n} g.
$$

一般称上式右端的 $\sum_{n=0}^{\infty} A^{n} g$ 为 Neumann 级数.

正如标量情形一样,可以证明 Banach 空间中的级数 $\sum_{n=0}^{\infty} x_{n}$ 收敛(或发散), 当 $\varlimsup_{n\to\infty} (\|x_{n}\|)^{1/n}<1$ (或>1)(参见[8], 第322页),为此人们关心 $(\|A^{n}\|)^{1/n}$ 的极限.

定理1.2 对任何 $A \in L(X)$ ,

$$
\lim _ {n \rightarrow \infty} (\| A ^ {n} \|) ^ {1 / n} = \inf _ {n} (\| A ^ {n} \|) ^ {1 / n}.
$$

证记 $r = \inf_{n}(\| A^{n}\|)^{1 / n}$ . 显然 $\lim_{n\to \infty}(\| A^n\|)^{1 / n}\geqslant r$ . 为此只须求证

$$
\varlimsup_ {n \to \infty} (\| A ^ {n} \|) ^ {1 / n} \leqslant r.
$$

根据下确界定义,任给 $\varepsilon > 0$ , 必有正整数 m, 使

$$
\| A ^ {m} \| ^ {1 / m} <   r + \varepsilon .
$$

对任何正整数 $n$ ，必有非负整数 $k,j,0\leqslant j < m$ ，使 $n = km + j$ .于是由命题1.3可得

$$
\| A ^ {n} \| \leqslant \| A ^ {k m} \| \| A ^ {j} \| \leqslant \| A ^ {m} \| ^ {k} \| A \| ^ {j},
$$

从而

$$
\| A ^ {n} \| ^ {1 / n} \leqslant \| A ^ {m} \| ^ {k / n} \| A \| ^ {j / n} \leqslant (r + \varepsilon) ^ {k m / n} \| A \| ^ {j / n}.
$$

注意 $\frac{km}{n} \to 1, \frac{j}{n} \to 0$ ，当 $n \to \infty$ 。故

$$
\varlimsup_ {n \rightarrow \infty} \| A ^ {n} \| ^ {1 / n} \leqslant r + \varepsilon .
$$

$\varepsilon$ 是任意的, 即得所欲证不等式. 证毕.

例3 设 $K(s, t)$ 在 $a \leqslant s, t \leqslant b$ 上连续，对 $C[a, b]$ 上的 Volterra 积分算子

$$
(V x) (s) = \int_ {a} ^ {s} K (s, t) x (t) \mathrm{d} t, x = x (s) \in C [ a, b ],
$$

令 $\mu = \max_{a\leqslant s,t\leqslant b}|K(s,t)|$ ，则

$$
\begin{array}{r l} | (V x) (s) | = & \left| \int_ {a} ^ {s} K (s, t) x (t) \mathrm{d} t \right| \\ & \leqslant \int_ {a} ^ {s} | K (s, t) | | x (t) | \mathrm{d} t \\ & \leqslant \mu \| x \| (s - a), \end{array}
$$

$$
\begin{array}{r l} | (V ^ {2} x) (s) | & = \left| \int_ {a} ^ {s} K (s, t) (V x) (t) \mathrm{d} t \right| \\ & \leqslant \int_ {a} ^ {s} | K (s, t) | | (V x) (t) | \mathrm{d} t \\ & \leqslant \int_ {a} ^ {s} \mu^ {*} \mu \| x \| (t - a) \mathrm{d} t \\ & = \mu^ {2} \| x \| \frac {(s - a) ^ {2}}{2 !}, \end{array}
$$

一般地

$$
\mid (V ^ {n} x) (s) \mid \leqslant \mu^ {n} \| x \| \frac {(s - a) ^ {n}}{n !}, n = 1, 2, \dots .
$$

从而

$$
\begin{array}{r l} \| V ^ {n} x \| & = \max _ {a \leqslant s \leqslant b} | (V ^ {n} x) (s) | \\ & \leqslant \mu^ {n} \| x \| \frac {(b - a) ^ {n}}{n !}, n = 1, 2, \dots . \end{array}
$$

故

(2.1)

$$
\parallel V ^ {n} \parallel \leqslant \mu^ {n} \frac {(b - a) ^ {n}}{n !}, n = 1, 2, \dots .
$$

因为 $(n!)^{1 / n}\rightarrow \infty$ ，当 $n\to \infty$ .故

$$
\lim _ {n \rightarrow \infty} \| V ^ {n} \| ^ {1 / n} = 0.
$$

命题1.6 对有界可逆的 $A \in L(X)$ , 其逆 $A^{-1}$ 是 $A$ 的连续函数. 而且 $L(X)$ 中全体有界可逆元形成一个开集.

证设 $A_0 \in L(X)$ 是有界可逆的，从

$$
A = A _ {0} - (A _ {0} - A) = A _ {0} \left[ I - A _ {0} ^ {- 1} (A _ {0} - A) \right]
$$

及习题5可知，当 $\| A_0 - A\|$ 充分小时， $A$ 也是有界可逆的，且

$$
A ^ {- 1} = \left[ I - A _ {0} ^ {- 1} (A _ {0} - A) \right] ^ {- 1} A _ {0} ^ {- 1}
$$

$$
= A _ {0} ^ {- 1} + \sum_ {n = 1} ^ {\infty} \left[ A _ {0} ^ {- 1} (A _ {0} - A) \right] ^ {n} A _ {0} ^ {- 1}.
$$

因为当 $\| A_0 - A\|$ 充分小时， $\| A_0^{-1}(A_0 - A)\| < 1$ ，根据定理1.1， $I - A_0^{-1}(A_0 - A)$ 有界可逆，且上式右端级数收敛.于是

$$
\begin{array}{r l} \| A ^ {- 1} - A _ {0} ^ {- 1} \| & \leqslant \sum_ {n = 1} ^ {\infty} \| [ A _ {0} ^ {- 1} (A _ {0} - A) ] ^ {n} \| \| A _ {0} ^ {- 1} \| \\ & \leqslant \frac {\| A _ {0} ^ {- 1} (A _ {0} - A) \| \| A _ {0} ^ {- 1} \|}{1 - \| A _ {0} ^ {- 1} (A _ {0} - A) \|} \\ & \leqslant \frac {\| A _ {0} ^ {- 1} \| ^ {2}}{1 - \| A _ {0} ^ {- 1} \| \| A _ {0} - A \|} \| A _ {0} - A \|. \end{array}
$$

由此可见 $A^{-1}$ 是 $A$ 的连续函数. 证毕.

从上面的论述可见, 范数 $\| \cdot \|$ 起到绝对值的作用, 许多标量级数的结果大都可以推广到 Banach 空间 $L(X)$ 的情况. 但也不总是如此, 例如, 对标量级数有命题: 无条件收敛①当且仅当绝对收敛. 但在无穷维空间, 这命题是不成立的. 已有人证明, 这一命题的成立正是空间为有限维的特征. (见[28])

## § 2 Hahn-Banach 定理

## 1. 扩张定理

E. Schmidt 在 1908 年曾考察 Hilbert 空间 $l^2$ 中无穷维线性方程组

$$
\left(\alpha_ {n}, x\right) = c _ {n}, n = 1, 2, \dots ,
$$

这里 $\{\alpha_{n}\}_{n = 1}^{\infty}$ 是 $t^2$ 中任意的一串线性无关的向量，而 $\{c_n\}_{n = 1}^{\infty}$ 是一串复数.

例1 若有常数 $M > 0$ ，使对任意正整数 $n$ 及数列 $\{\lambda_k\}_{k=1}^{\infty}$ 都有

$$
\left| \sum_ {k = 1} ^ {n} \lambda_ {k} c _ {k} \right| \leqslant M \left\| \sum_ {k = 1} ^ {n} \lambda_ {k} \alpha_ {k} \right\|,\tag{2.2}
$$

则无穷维线性方程组(2.1)确有一解.

设由 $\{\alpha_{n}\}_{n = 1}^{\infty}$ 张成的子空间为 $\mathcal{M}$ . 定义

$$
f (\alpha_ {k}) = c _ {k}, k = 1, 2, \dots ,
$$

一般地

$$
f \left(\sum_ {k = 1} ^ {n} \lambda_ {k} \alpha_ {k}\right) = \sum_ {k = 1} ^ {n} \lambda_ {k} c _ {k}.
$$

由假设(2.2)，

$$
\left| f \left(\sum_ {k = 1} ^ {n} \lambda_ {k} \alpha_ {k}\right) \right| = \left| \sum_ {k = 1} ^ {n} \lambda_ {k} c _ {k} \right| \leqslant M \left\| \sum_ {k = 1} ^ {n} \lambda_ {k} \alpha_ {k} \right\|,
$$

故 $f$ 可连续扩张成空间 $\mathcal{M}$ 上的有界线性泛函. 如果 $f$ 可扩张成 Hilbert 空间 $t^2$ 上的有界线性泛函 $F$ , 根据 Fréchet-Riesz 表现定理, 存在 $x_0 \in t^2$ , 使

$$
F (x) = (x, x _ {0}), \text {当} x \in l ^ {2}.
$$

于是

$$
\left(\alpha_ {k}, x _ {0}\right) = F \left(\alpha_ {k}\right) = f \left(\alpha_ {k}\right) = c _ {k}, k = 1, 2, \dots .
$$

即 $x_0$ 是方程组(2.1)的一个解.

后来，F.Riesz研究 $L^p (I)(1 < p < \infty ,I$ 是单位区间)上的无穷维线性方程组

$$
\int_ {I} f (x) g _ {j} (x) \mathrm{d} x = c _ {j}, j = 1, 2, \dots ,
$$

这里 $g_{j} \in L^{q}(I)\left(\frac{1}{p} + \frac{1}{q} = 1, j = 1, 2, \cdots\right)$ 是线性无关的. 他试图寻求满足上述方程组的 $f \in L^{p}(I)$ ，并在类似于(2.2)的条件下证明方程组确有一解.

设 $\mathcal{E}$ 是由 $\{g_j\}_{j=1}^{\infty}$ 张成的 $L^q(I)$ 的子空间，又设线性泛函 $\ell$ 使

$$
\ell (g _ {j}) = c _ {j}, j = 1, 2, \dots .
$$

正是 E. Helly 在 1912 年首先看出在类似(2.2)的条件下, $l$ 可以扩张成整个 $L^q(I)$ 上的有界线性泛函. 从而存在 $f \in L^p(I)$ 使

$$
c _ {j} = \iota (g _ {j}) = \int_ {I} f (x) g _ {j} (x) \mathrm{d} x, j = 1, 2, \dots
$$

(参见 §4 中定理 4.4). 当时, Helly 还是就一般赋范的序列空间, 而不只是对特殊的 $l^p, L^p$ 或 $C[a, b]$ 来研究的. 其后, Hahn 在 1927 年又回到 Helly 的工作, 使用超穷归纳法解决了一般 Banach 空间上有界线性泛函的扩张问题.

定理 2.1(Banach 扩张定理,1929) 设 $f(x)$ 是实线性空间 X 中线性流形 G 上的实线性泛函. 如果有 X 上的实值泛函 $p(x)$ , 使

(1) $p(x + y) \leqslant p(x) + p(y), p(tx) = tp(x)$ , 当 $x, y \in X, t \geqslant 0$ ;

(2) $f(x)\leqslant p(x)$ ，当 $x\in G$

则存在 $X$ 上的实线性泛函 $F(x)$ ，使

$$
F (x) = f (x), \text {当} x \in G,
$$

且

$$
F (x) \leqslant p (x), \text {当} x \in X.
$$

证若 $G = X$ ，定理是显然的，下面假定 $G \neq X$ . 设 $x_0 \in X \setminus G$ ，考虑如下形式的点集：

$$
\mathcal {M} = \{\lambda x _ {0} + x: \lambda \text {是实数}, x \in G \}.
$$

它是包含 $x_0$ 与 $G$ 的最小线性流形. 先往证在 $\mathcal{M}$ 上存在实线性泛函 $F_1(x)$ , 使

$$
F _ {1} (x) = f (x), \text {当} x \in G,\tag{2.3}
$$

$$
F _ {1} (x) \leqslant p (x), \text {当} x \in \mathcal {M}.
$$

设 $F_{1}(x_{0}) = r_{0}$ （待定）.根据对 $F_{1}$ 的要求，必须

$$
F _ {1} (\lambda x _ {0} + x) = \lambda F _ {1} (x _ {0}) + f (x) \leqslant p (\lambda x _ {0} + x), \text {当} \lambda \in \mathbb {R}, x \in G.
$$

因此

$$
\lambda r _ {0} \leqslant p (\lambda x _ {0} + x) - f (x)\tag{2.4}
$$

对一切 $\lambda \neq 0, x \in G$ 都成立. 以下分两种情况来讨论.

当 $\lambda > 0$

$$
\begin{array}{r l} r _ {0} & \leqslant \frac {1}{\lambda} [ p (\lambda x _ {0} + x) - f (x) ] \\ & = p (x _ {0} + \frac {x}{\lambda}) - f (\frac {x}{\lambda}) \\ & = p (x _ {0} + x ^ {\prime}) - f (x ^ {\prime}), x ^ {\prime} \in G. \end{array}
$$

当 $\lambda < 0$

$$
\begin{array}{r l} r _ {0} & \geqslant \frac {1}{\lambda} [ p (\lambda x _ {0} + x) - f (x) ] \\ & = \frac {| \lambda |}{\lambda} \left[ p \left(\frac {\lambda x _ {0}}{| \lambda |} + \frac {x}{| \lambda |}\right) - f \left(\frac {x}{| \lambda |}\right) \right] \\ & = - [ p (- x _ {0} + x ^ {\prime \prime}) - f (x ^ {\prime \prime}) ], x ^ {\prime \prime} \in G. \end{array}
$$

总之，条件(2.4)相当于

$$
- p (- x _ {0} + x ^ {\prime \prime}) + f (x ^ {\prime \prime}) \leqslant r _ {0} \leqslant p (x _ {0} + x ^ {\prime}) - f (x ^ {\prime}), x ^ {\prime}, x ^ {\prime \prime} \in G. \tag {2.5}
$$

要想这样的 $r_0$ 存在必须且只须(2.5)式右端恒不小于左端.即

$$
f \left(x ^ {\prime}\right) + f \left(x ^ {\prime \prime}\right) \leqslant p \left(x _ {0} + x ^ {\prime}\right) + p \left(- x _ {0} + x ^ {\prime \prime}\right), \forall x ^ {\prime}, x ^ {\prime \prime} \in G.
$$

由假设(1)与(2)，

$$
\begin{array}{r l} f (x ^ {\prime}) + f (x ^ {\prime \prime}) & = f (x ^ {\prime} + x ^ {\prime \prime}) \\ & \leqslant p (x ^ {\prime} + x ^ {\prime \prime}) \end{array}
$$

$$
\begin{array}{l} = p \left(x _ {0} + x ^ {\prime} - x _ {0} + x ^ {\prime \prime}\right) \\ \leqslant p \left(x _ {0} + x ^ {\prime}\right) + p \left(- x _ {0} + x ^ {\prime \prime}\right), \end{array}
$$

$$
\forall x ^ {\prime}, x ^ {\prime \prime} \in G.
$$

由此可见(2.5)式右端确实恒不小于左端.兹令

$$
\sup _ {x ^ {\prime \prime} \in G} [ - p (x _ {0} + x ^ {\prime \prime}) + f (x ^ {\prime \prime}) ] \leqslant r _ {0} \leqslant \inf _ {x ^ {\prime} \in G} [ p (x _ {0} + x ^ {\prime}) - f (x ^ {\prime}) ].
$$

由如此 $r_0$ 所确定的线性泛函 $F_{1}(x)$ 显然满足(2.3).

考察实线性泛函 $g(x)$ , 其定义域记作 $\mathcal{D}(g)$ . 如果

$$
G \subset \mathscr {D} (g),
$$

且

$$
g (x) = f (x), \text {当} x \in G,
$$

$$
g (x) \leqslant p (x), \text {当} x \in \mathcal {D} (g),
$$

则称 $g$ 为 $f$ 的扩张. 设 $f$ 的所有扩张的集合为 $\mathcal{R}$ . 规定 $\mathcal{R}$ 中的序如下: 若 $g_1, g_2 \in \mathcal{R}$ , 且 $\mathcal{D}(g_1) \subset \mathcal{D}(g_2), g_1(x) = g_2(x)$ , 当 $x \in \mathcal{D}(g_1)$ , 则 $g_1 < g_2$ . 于是 $\mathcal{R}$ 是非空的部分有序集. 对 $\mathcal{R}$ 中任何完全有序子集 $\mathcal{S}$ , 可以作出实线性泛函 $h(x)$ , 使

$$
\begin{array}{c} {{\mathcal {D} (h) = \bigcup_ {g \in {\mathcal {S}}} \mathcal {D} (g)  ,}} \\ {{h (x) = g (x)  ,   \text {当}    x \in \mathcal {D} (g)  ,   g \in {\mathcal {S}}.}} \end{array}
$$

则 $h \in \mathcal{R}$ , 且对一切 $g \in \mathcal{S}$ , 都有 $g < h$ . 即 $h$ 是 $\mathcal{S}$ 的上界. 根据 Zorn 引理, $\mathcal{R}$ 中有极大元 $F$ . 当然 $F$ 是 $f$ 的扩张. 如果 $\mathcal{D}(F) \neq X$ , 则如前面第一部分的证明, $F$ 可以再扩张, 这与 $F$ 的极大性矛盾. 于是 $\mathcal{D}(F) = X$ , 即 $F$ 是 $X$ 上实线性泛函. 容易验证 $F$ 即为所求者. 证毕.

上述定理本质上是实的,在它出现十来年后才有下面的复扩张定理.

定理 2.2(Bohnenblust-Sobczyk,1938) 设 $f(x)$ 是复线性空间 X 之线性流形 G 上的线性泛函. 如果有 X 上实值泛函 $p(x)$ , 使

$$
p (x + y) \leqslant p (x) + p (y), p (\alpha x) = | \alpha | p (x), \forall x, y \in X, \alpha \in \mathbf {C}; \tag {1}
$$

(2) $|f(x)| \leqslant p(x)$ , 当 $x \in G$ ,

则存在 $X$ 上线性泛函 $F(x)$ ，使

$$
F (x) = f (x), \text {当} x \in G,
$$

且

$$
| F (x) | \leqslant p (x), \text {当} x \in X.
$$

证设 $f(x)$ 的实部为 $f_{1}(x)$ , 虚部为 $f_{2}(x)$ , 即

$$
f _ {1} (x) = \frac {f (x) + \overline {{f (x)}}}{2},
$$

$$
f _ {2} (x) = \frac {f (x) - \overline {{f (x)}}}{2 \mathrm{i}}.
$$

则

$$
f (x) = f _ {1} (x) + \mathrm{i} f _ {2} (x),
$$

而且 $f_{1}(x), f_{2}(x)$ 都是 $G$ 上的实线性泛函. 注意 $f(x)$ 是复线性空间上线性泛函, 因此

$$
\begin{array}{r l} \mathrm{i} [ f _ {1} (x) + \mathrm{i} f _ {2} (x) ] & = \mathrm{i} f (x) = f (\mathrm{i} x) \\ & = f _ {1} (\mathrm{i} x) + \mathrm{i} f _ {2} (\mathrm{i} x), x \in G. \end{array}
$$

比较两端的实部,便有

$$
f _ {1} (i x) = - f _ {2} (x), x \in G.
$$

从而

$$
f (x) = f _ {1} (x) - \mathrm{i} f _ {1} (\mathrm{i} x), x \in G.
$$

这说明 $f$ 可以由其实部唯一确定.

因为复线性空间也可以看作实线性空间, 故 $f_{1}$ 可视为实线性流形 G 上的实线性泛函, 而且

$$
f _ {1} (x) \leqslant | f (x) | \leqslant p (x), \text {当} x \in G.
$$

由定理 2.1, $f_{1}$ 可以扩张成线性空间 X 上的实线性泛函 $F_{1}$ ,且

$$
F _ {1} (x) = f _ {1} (x), \text {当} x \in G,
$$

$$
F _ {1} (x) \leqslant p (x), \text {当} x \in X.
$$

令

$$
F (x) = F _ {1} (x) - \mathrm{i} F _ {1} (\mathrm{i} x), x \in X.
$$

显然， $\forall x,y\in X,F(x + y) = F(x) + F(y)$ ，且当 $t$ 是实数时，

$$
F (t x) = t F (x).
$$

又

$$
\begin{array}{r l} F (\mathrm{i} x) & = F _ {1} (\mathrm{i} x) - \mathrm{i} F _ {1} (- x) = \mathrm{i} F _ {1} (x) + F _ {1} (\mathrm{i} x) \\ & = \mathrm{i} (F _ {1} (x) - \mathrm{i} F _ {1} (\mathrm{i} x)) = \mathrm{i} F (x). \end{array}
$$

故 $F(x)$ 是复线性空间 $X$ 上线性泛函.

当 $x \in G$ ，也有 $\mathrm{i}x \in G$ ，从而

$$
F (x) = F _ {1} (x) - \mathrm{i} F _ {1} (\mathrm{i} x) = f _ {1} (x) - \mathrm{i} f _ {1} (\mathrm{i} x) = f (x).
$$

当 $x \in X$ ，如果 $F(x) \neq 0$ ，令 $\theta = \arg F(x)$ ，则

$$
\begin{array}{r l} | F (x) | & = F (x) \mathrm{e} ^ {- \mathrm{i} \theta} = F (\mathrm{e} ^ {- \mathrm{i} \theta} x) \\ & = \operatorname{Re} F (\mathrm{e} ^ {- \mathrm{i} \theta} x) = F _ {1} (\mathrm{e} ^ {- \mathrm{i} \theta} x) \\ & \leqslant p (\mathrm{e} ^ {- \mathrm{i} \theta} x) = p (x). \end{array}
$$

如果 $F(x) = 0$ ，不等式显然成立.证毕.

定理 2.3(Hahn-Banach,1927) 对于赋范线性空间 X 之线性流形 G 上的连续线性泛函 $f(x)$ ，恒有 X 上的连续线性泛函 $F(x)$ ，使

(1) $F(x)=f(x)$ ，当 $x\in G$ ，

(2) $\| F \| = \| f \|_G$ .

这里 $\| f\| _G$ 表示 $f$ 作为 $G$ 上连续线性泛函的范数，下同.

证令

$$
p (x) = \parallel f \parallel_ {G} \parallel x \parallel , \text {当} x \in X.
$$

不难验证 $f, p$ 满足定理2.2的条件，于是存在 $X$ 上线性泛函 $F(x)$ ，使

$$
F (x) = f (x), \text {当} x \in G,
$$

且

$$
| F (x) | \leqslant p (x) = \| f \| _ {G} \| x \|, \text {当} x \in X.
$$

因此 $F$ 是 $X$ 上有界线性泛函，而且

$$
\| F \| \leqslant \| f \| _ {G}.
$$

但 $F$ 是 $f$ 的扩张，因而 $F$ 的范数不会小于 $f$ 的范数，即 $\| F\| \geqslant \| f\| _G$ .总之

$$
\| F \| = \| f \| _ {G}.
$$

证毕.

Hahn-Banach 定理的重要性首先在于下面的几个重要推论.例如,我们有命题2.1 设 $X$ 是赋范线性空间, 任给非零的 $x_0 \in X$ , 总存在 $X$ 上的连续线性泛函 $f$ 满足

(1) $\| f \| = 1$ ,

(2) $f(x_0) = \| x_0\|$ .

证取 $G = \{\alpha x_0:\alpha \in \mathbf{C}\}$ ，定义

$$
f _ {1} (\alpha x _ {0}) = \alpha \| x _ {0} \|, \alpha \in \mathbf {C}.
$$

则 $G$ 是 $X$ 中线性流形, $f_{1}$ 是 $G$ 上连续线性泛函, $\| f_{1} \|_{G} = 1$ , $f_{1}(x_{0}) = \| x_{0} \|$ . 根据定理2.3可见命题为真. 证毕.

这个命题说明在非零的赋范线性空间上,总存在非零的连续线性泛函.但是对一般的距离线性空间,这可不一定成立.试看第一章§8中例4所说的距离线性空间 $S[0,1]$ .

例2 $S[0,1]$ 上没有非零的连续线性泛函.

假设 $S[0,1]$ 上存在非零的连续线性泛函 $x'$ ，则存在非零元 $x_0 \in S[0,1]$ ，使 $x'(x_0) \neq 0$ ，取

$$
x _ {1 1} (t) = \left\{ \begin{array}{l l} x _ {0} (t), & \text {当} t \in \left[ 0, \frac {1}{2}\right), \\ 0, & \text {当} t \in \left[ \frac {1}{2}, 1 \right], \end{array} \right.
$$

$$
x _ {1 2} (t) = \left\{ \begin{array}{l l} 0, & \text {当} t \in \left[ 0, \frac {1}{2}\right), \\ x _ {0} (t), & \text {当} t \in \left[ \frac {1}{2}, 1 \right], \end{array} \right.
$$

则 $x_{11}, x_{12} \in S[0, 1]$ , 而且 $x_0 = x_{11} + x_{12}$ , 于是

$$
x ^ {\prime} (x _ {0}) = x ^ {\prime} (x _ {1 1}) + x ^ {\prime} (x _ {1 2}).
$$

可见 $x^{\prime}(x_{1j}), j = 1,2$ ，中必有一个非零，记满足 $x^{\prime}(x_{1j}) \neq 0$ 的某个 $x_{1j}$ 为 $x_{1}$ . 如此继续下去，将有一串 $\{x_{n}\}_{n=1}^{\infty} \subset S[0,1]$ ，使 $\alpha_{n} = x^{\prime}(x_{n}) \neq 0$ ，而且

$$
\overline {{\{t \in [ 0 , 1 ] : x _ {n} (t) \neq 0 \}}}
$$

包含在一个长度不大于 $\frac{1}{2^n}$ 的区间 $I_{n}$ 中，令

$$
y _ {n} (t) = \frac {x _ {n} (t)}{\alpha_ {n}}, n = 1, 2, \dots ,
$$

则 $y_{n}\in S[0,1]$ ，且

$$
\begin{array}{r l}\mathrm{d} (y _ {n}, 0)&= \int_ {0} ^ {1} \frac {| y _ {n} (t) |}{1 + | y _ {n} (t) |} \mathrm{d} t\\&= \int_ {I _ {n}} \frac {| y _ {n} (t) |}{1 + | y _ {n} (t) |} \mathrm{d} t\\&\leqslant m (I _ {n}) \leqslant \frac {1}{2 ^ {n}} \rightarrow 0, \text {当} n \rightarrow \infty .\end{array}
$$

但是

$$
x ^ {\prime} (y _ {n}) = \frac {x ^ {\prime} (x _ {n})}{\alpha_ {n}} = 1, n = 1, 2, \dots .
$$

这与 $x^{\prime}$ 的连续性矛盾.

命题2.2 设 $X$ 是赋范线性空间, $E$ 是 $X$ 的子空间, $x_0 \in X \setminus E$ , 则存在 $X$ 上有界线性泛函 $f$ 满足

(1) $f(x) = 0$ ，当 $x \in E$

(2) $f(x_0) = 1$

(3) $\| f \| = \frac{1}{d}$ ,

这里 $d = \mathrm{dist}(x_0,E) > 0$

证取 $G = \{\alpha x_0 + x: \alpha \in \mathbf{C}, x \in E\}$ , 定义

$$
f _ {1} (  \alpha x _ {0} + x) = \alpha  , \text {当}   \alpha x _ {0} + x \in G  .
$$

易见 $G$ 是 $X$ 中包含 $E$ 与 $x_0$ 的线性流形, $f_1$ 是 $G$ 上线性泛函. 往证 $f_1$ 是有界的, 且 $\| f_1 \|_G = \frac{1}{d}$ .

首先，对任意的 $ax_0 + x \in G$ ，只要 $\alpha \neq 0$

$$
\| \alpha x _ {0} + x \| = | \alpha | \| x _ {0} + \frac {x}{\alpha} \| \geqslant | \alpha | d.
$$

故

$$
\left| f _ {1} \left(a x _ {0} + x\right) \right| = | \alpha | \leqslant \frac {\left\| a x _ {0} + x \right\|}{d}.
$$

当 $\alpha = 0$ 时，上述不等式显然成立.由此可知， $f_{1}$ 是有界的，且

$$
\| f _ {1} \| _ {G} \leqslant \frac {1}{d}.
$$

另一方面，任给 $\varepsilon > 0$ ，存在 $x_{1} \in E$ ，使

$$
\| x _ {0} - x _ {1} \| <   d + \varepsilon ,
$$

于是，对任意的 $\alpha \in \mathbf{C}$

$$
\left\| \alpha x _ {0} - \alpha x _ {1} \right\| = | \alpha | \| x _ {0} - x _ {1} \| <   | \alpha | (d + \varepsilon),
$$

故

$$
\mid f _ {1} \left(\alpha x _ {0} - \alpha x _ {1}\right) \mid = \mid \alpha \mid \geqslant \frac {\parallel \alpha x _ {0} - \alpha x _ {1} \parallel}{d + \varepsilon}
$$

从而

$$
\| f _ {1} \| _ {G} \geqslant \frac {1}{d + \varepsilon}.
$$

$\varepsilon > 0$ 是任意的，故 $\|f_1\|_G \geqslant \frac{1}{d}$ . 总之， $\|f_1\|_G = \frac{1}{d}$ .

最后，对 $G, f_{1}$ 应用定理2.3便知命题为真. 证毕.

命题2.3 设 $M$ 是赋范线性空间 $X$ 中线性流形, $x_0 \in X$ , 则

$x_0 \in \overline{M} \Leftrightarrow$ 对 $X$ 上任何连续线性泛函 $f$ ,

$$
f (x) = 0, \forall   x \in M, \text {蕴含} f (x _ {0}) = 0.
$$

证这是命题2.2的直接推论.

推论设 $S$ 是赋范线性空间 $X$ 的子集, $x_0 \in X$ , 则

$x_0$ 可以用 $S$ 中向量的线性组合来逼近 $\Leftrightarrow$ 对 $X$ 上任何连续线性泛函 $f$ ,

$$
f (x) = 0, \forall   x \in S, \text {蕴含} f (x _ {0}) = 0.
$$

证只须取命题2.3中 $M$ 为 $S$ 中元张成的线性流形即可.

正是鉴于这个推论,人们才说 Hahn-Banach 定理是处理某些逼近问题之经典方法的基础.

命题2.4 设 $\mathcal{M}$ 是Banach空间 $X$ 的有限维子空间, 则有 $X$ 的子空间 $\mathcal{N}$ , 使

$$
X = \mathcal {M} + \mathcal {N}, \text {且} \mathcal {M} \cap \mathcal {N} = \{0 \}.
$$

证设 M 是 n 维子空间, 其基为 $\{x_{1}, \cdots, x_{n}\}$ . 假定删去 $x_{j}$ 后由 $x_{1}, \cdots, x_{j-1}, x_{j+1}, \cdots, x_{n}$ 张成的子空间为 $M_{j}, j = 1, \cdots, n$ . 根据命题 2.2, 存在 X 上的有界线性泛函 $x_{j}'$ 使

$$
x _ {j} ^ {\prime} (x _ {k}) = \delta_ {j k} = \left\{ \begin{array}{l l} 1, & \text {当} j = k, \\ 0, & \text {当} j \neq k. \end{array} \right.
$$

考察算子

$$
P (x) = \sum_ {j = 1} ^ {n} x _ {j} ^ {\prime} (x) x _ {j}, x \in X.
$$

易证 $P$ 是 $X$ 上连续线性算子，且 $P$ 的值域 $R(P) = \mathcal{M}$ . 显然

$$
x _ {k} ^ {\prime} (P (x)) = \sum_ {j = 1} ^ {n} x _ {j} ^ {\prime} (x) x _ {k} ^ {\prime} (x _ {j}) = x _ {k} ^ {\prime} (x).
$$

故对任何 $x \in X$

$$
P ^ {2} (x) = P (P (x)) = \sum_ {k = 1} ^ {n} x _ {k} ^ {\prime} (P (x)) x _ {k} = \sum_ {k = 1} ^ {n} x _ {k} ^ {\prime} (x) x _ {k} = P (x).
$$

设

$$
\mathcal {N} = N (P) = \{x \in X: P (x) = 0 \},
$$

易证 $\mathcal{N}$ 是 $X$ 的子空间.

设 $x \in \mathcal{M} \cap \mathcal{N}$ . 从 $x \in \mathcal{M}$ , 应有某个 $y \in X$ , 使 $x = P(y)$ . 又从 $x \in \mathcal{N}$ , 得

$$
0 = P (x) = P (P (y)) = P (y) = x.
$$

故 $\mathcal{M} \cap \mathcal{N} = \{0\}$ .

现在,对任给的 $x \in X$ ,总有

$$
x = P (x) + [ x - P (x) ].
$$

令 $x_{1} = P(x), x_{2} = x - P(x)$ ，则 $x_{1} \in \mathcal{M}$ ，而

$$
P (x _ {2}) = P (x) - P ^ {2} (x) = 0,
$$

故 $x_{2} \in \mathcal{N}$ . 总之

$$
X = \mathcal {M} + \mathcal {N}.
$$

证毕.

像命题2.4中的两个子空间 $\mathcal{M}$ 与 $\mathcal{N}$ 称为拓扑互补子空间. 把一个空间分解成拓扑互补的子空间, 这件事在算子的研究上是重要的. 可惜对于一般(甚至可以说相当多的) Banach 空间, 不是关于它的任何子空间都存在与之拓扑互补的子空间. 事实上, F.J. Murray 在1937年就已证明, 甚至在 $L^p$ (或 $t^p$ ) ( $p \neq 2$ ) 这样好的空间中都存在子空间, 没有与之拓扑互补的子空间 (参见[37]). 但对于Hilbert空间 $H$ , 因为有所谓的射影定理, 情形就好得多. 对于 $H$ 的任何子空间 $\mathcal{M}, \mathcal{M}^\perp$ 正是与 $\mathcal{M}$ 拓扑互补的子空间. 很有意思, J. Lindenstrauss 和 I. Tzafriri 证明, 在任何不与Hilbert空间拓扑同构的Banach空间中都存在子空间, 没有与之拓扑互补的子空间. (参见[35])

下面我们来谈谈 Hahn-Banach 定理的几何解释.

对三维空间上的线性泛函

$$
f (x, y, z) = a x + b y + c z.
$$

点集 $\{(x, y, z): f(x, y, z) = d$ (常数) 正是三维空间中的一个平面. 所以对一般无穷维的 Banach 空间 $X$ 上的连续线性泛函 $f(x)$ , 人们也就称点集

$$
\{x \in X: f (x) = c \}
$$

为 $X$ 中的超平面, 这里 $c$ 是常数. 设 $M$ 是 $X$ 中线性流形, $x_0 \in X \setminus M$ , 我们称点集 $g = x_0 + M = \{x_0 + x: x \in M\}$ 为 $X$ 中的线性簇. 下面的命题对于三维空间看上去是明显的.

定理 2.4(Hahn-Banach 定理的几何形式) 设 X 是赋范线性空间, 若 X 中的线性簇 g 与开球 K 不相交, 则有超平面 H 包含 g 而且与 K 不相交.

证不妨设 $K = \{x : \| x \| < 1\}$ . $g = x_0 + M, M$ 是线性流形, $x_0 \notin M$ . 则 $\overline{M}$ 是 $X$ 的子空间. 由假设 $g$ 与 $K$ 不相交, 故对任意 $x \in M, \| x_0 + x \| \geqslant 1$ , 于是 $\delta = \mathrm{dist}(x_0, \overline{M}) \geqslant 1$ . 根据命题2.2, 存在 $X$ 上线性泛函 $f$ , 使

(1) $f(x) = 0$ ，当 $x \in M$

(2) $f(x_0) = 1$

(3) $\| f \| = \frac{1}{\delta} \leqslant 1$ .

定义超平面 $H$ 为

$$
H = \{x \in X: f (x) = 1 \},
$$

则对任意 $x \in g$ ，有 $x = x_0 + x_1, x_1 \in M$ . 于是

$$
f (x) = f \left(x _ {0}\right) + f \left(x _ {1}\right) = 1,
$$

所以 $g \subset H$ . 又当 $x \in K$ 时, $\| x \| < 1$ , 故

$$
\mid f (x) \mid \leqslant \| f \| \| x \| <   1.
$$

可见， $x\notin H$ .证毕.

反之, 从上述之 Hahn-Banach 定理的几何形式也能推出 Hahn-Banach 定理的解析形式. 即定理 2.3.

假定定理2.4成立.对任给的线性流形 $G$ 及其上的非零连续线性泛函 $f(x)$ ，令

$$
\begin{array}{l} g = \{x \in G: f (x) = 1 \}, \\ K = \{x \in X: \| x \| <   \mu \}, \end{array}
$$

这里 $\mu = \frac{1}{\|\boldsymbol{f}\|_G}$ .

取定 $x_0 \in g$ ，则 $f(x_0) = 1$ . 令 $M = \operatorname{Ker} f = \{x \in G : f(x) = 0\}$ ，则 $g = x_0 + M$ ，即 $g$ 是线性簇. $K$ 是开球，如果 $x \in g$ ，则

$$
1 = | f (x) | \leqslant \| f \| _ {G} \| x \|,
$$

故 $\| x\| \geqslant \mu$ ，即 $x\notin K$ .所以 $g\cap K = \emptyset$

根据定理2.4，应有超平面

$$
H = \{x \in X: F (x) = c \},
$$

使

$$
H \supset g, \text {且} H \cap K = \varnothing .
$$

因 $H \cap K = \emptyset$ ，可知 $c \neq 0$ . 不失一般性，可设 $c = 1$ . 否则以 $F / c$ 代替 $F$ 即可. 因为 $g \subset H$ ，从 $f(x) = 1$ 恒有 $F(x) = 1$ ，可知 $F(x)$ 是 $f(x)$ 的扩张. 事实上，如果 $x \in G, f(x) = a \neq 0$ ，则 $f\left(\frac{x}{a}\right) = 1$ ，从而 $F\left(\frac{x}{a}\right) = 1$ ，故 $F(x) = a$ . 若 $f(x) = 0$ ，因取定 $x_0 \in g$ ，故

$$
f (x + \dot {x} _ {0}) = f (x) + f (x _ {0}) = 1,
$$

于是

$$
F (x + x _ {0}) = F (x _ {0}) = 1.
$$

故 $F(x) = 0$

从 $H \cap K = \emptyset$ ，可知 $K \subset \{x : |F(x)| < 1\}$ . 否则，有 $x_1 \in K$ 使 $|F(x_1)| \geqslant 1$ . 令 $x_2 = \frac{x_1}{F(x_1)}$ ，则 $x_2 \in K$ ，且 $F(x_2) = 1$ ，即 $x_2 \in H \cap K$ ，矛盾. 总之

$$
\{x: \| x \| <   \mu \} \subset \{x: | F (x) | <   1 \}.
$$

据此

$$
\sup _ {\| x \| \leqslant \mu} | F (x) | \leqslant 1.
$$

即

$$
\sup _ {\| x / \mu \| \leqslant 1} \left| F \left(\frac {x}{\mu}\right) \right| \mu \leqslant 1.
$$

从而

$$
\| F \| = \sup _ {\| z \| \leqslant 1} | F (z) | \leqslant \frac {1}{\mu} = \| f \| _ {G}.
$$

另一方面，已证 $F$ 是 $f$ 的扩张，故 $\| F\| \geqslant \| f\| _G$ .总之， $\| F\| = \| f\| _G$

这就证明了 Hahn-Banach 定理.

2. 分离定理定义2.1 对线性空间 $X$ 中的集合 $M$ ,

(1) 若对 $x, y \in M, 0 \leqslant \alpha \leqslant 1$ , 总有 $ax + (1 - \alpha)y \in M$ , 则称 $M$ 是凸的.

(2) 若 $x \in M, |\lambda| \leqslant 1$ , 总有 $\lambda x \in M$ , 则称 $M$ 是平衡的.

(3) 若对任意 $x \in X$ , 总有 $\varepsilon > 0$ , 使当 $0 < |\alpha| \leqslant \varepsilon$ 时, $\alpha x \in M$ , 则称 $M$ 是吸收的.

对任给的半范数 $p(x)$ (参见第一章 §8), 点集 $\{x: p(x) < r\} (r > 0)$ 便是凸集. 这正是凸集与泛函分析密切联系的一个原因. 事实上, 许多分析问题可化归为凸集之几何学的研究. 下面我们还将从一个凸集导出一种重要的半范数.

定义2.2 设 $K$ 是线性空间 $X$ 中凸的、吸收的集合，则

$$
p _ {K} (x) = \inf \{\alpha : \alpha > 0, \text {且} \alpha^ {- 1} x \in K \}
$$

称为 $K$ 的Minkowski泛函, 它与第一章 §8 中所说的半范数概念密切相关.

命题2.5 线性空间 $X$ 中凸的、平衡的、吸收的点集 $K$ 的Minkowski泛函 $p_K(x)$ 是 $X$ 上的半范数.

证由 Minkowski 泛函定义, 对任给的 $\varepsilon > 0$ , 有

$$
0 <   \alpha_ {x} <   p _ {K} (x) + \varepsilon , \text {使} \alpha_ {x} ^ {- 1} x \in K,
$$

$$
0 <   \alpha_ {y} <   p _ {K} (y) + \varepsilon , \text {使} \alpha_ {y} ^ {- 1} y \in K.
$$

由 $K$ 是凸的，

$$
\frac {\alpha_ {x}}{\alpha_ {x} + \alpha_ {y}} \alpha_ {x} ^ {- 1} x + \frac {\alpha_ {y}}{\alpha_ {x} + \alpha_ {y}} \alpha_ {y} ^ {- 1} y \in K,
$$

即 $(\alpha_{x} + \alpha_{y})^{-1}(x + y)\in K.$ 由 $p_K(\cdot)$ 的定义，

$$
p _ {K} (x + y) \leqslant a _ {x} + a _ {y} <   p _ {K} (x) + p _ {K} (y) + 2 \varepsilon .
$$

令 $\varepsilon \to 0$ ，则

$$
p _ {K} (x + y) \leqslant p _ {K} (x) + p _ {K} (y).
$$

设 $\lambda \neq 0, x \in X$ . 若 $\alpha > 0, \alpha^{-1}x \in K$ , 由 $K$ 是平衡的,

$$
(| \lambda | \alpha) ^ {- 1} \lambda x = \frac {\lambda}{| \lambda |} \alpha^ {- 1} x \in K,
$$

从而

$$
p _ {K} (\lambda x) \leqslant | \lambda | \alpha .
$$

关于这样的 $\alpha$ 取下确界, 根据 Minkowski 泛函定义便有

$$
p _ {K} (\lambda x) \leqslant | \lambda | p _ {K} (x).
$$

取 $y = \lambda x$ 代入上式后，再取 $\lambda = \frac{1}{\mu}$ ，则

$$
p _ {K} (y) \leqslant \frac {1}{| \mu |} p _ {K} (\mu y),
$$

即

$$
p _ {K} (\mu y) \geqslant | \mu | p _ {K} (y).
$$

总之

$$
p _ {K} (\lambda x) = | \lambda | p _ {K} (x).
$$

易证 $p_K(0) = 0$ 故当 $\lambda = 0$ 时，等式亦成立.证毕.

命题2.6 若只假设命题2.5中 $K$ 是凸的，吸收的，则 $p_K(x)$ 是次可加的，且

$$
p _ {K} (\lambda x) = \lambda p _ {K} (x), \text {当} \lambda \geqslant 0.
$$

证次可加性证明与命题 2.5 一样. 若于 $\alpha > 0, \alpha^{-1}x \in K$ , 则对 $\lambda > 0$ ,

$$
(\lambda \alpha) ^ {- 1} \lambda x = \alpha^ {- 1} x \in K.
$$

可知

$$
p _ {K} (\lambda x) \leqslant \lambda \alpha .
$$

从而由Minkowski泛函定义有

$$
p _ {K} (\lambda x) \leqslant \lambda p _ {K} (x).
$$

像命题 2.5 一样, 我们也可从此式得

$$
p _ {K} (x) \leqslant \frac {1}{\lambda} p _ {K} (\lambda x).
$$

总之

$$
p _ {K} (\lambda x) = \lambda p _ {K} (x).
$$

易证 $p_K(0) = 0$ 故当 $\lambda = 0$ 时，等式亦真.证毕.

定义2.3 设 $f(x)$ 是实距离线性空间 $X$ 上连续线性泛函. $E, F$ 是 $X$ 中子集, 若有实数 $r$ , 使

$f(x)\geqslant r$ ，当 $x\in E,f(x)\leqslant r$ ，当 $x\in F$

则称超平面 $H = \{x\in X:f(x) = r\}$ 分离 $E$ 与 $F$

这样, 前述的 Hahn-Banach 定理的几何形式实际上就是说那里的 $H$ 分离 $g$ 与 $K$ , 所以也是一种分离定理. 历史上, Minkowski 早在 1911 年就对 $n$ 维空间证明其中的有界凸闭集的每个边界点处都有一个承托平面 (即凸集在这平面的一侧). S. Mazur 在 1933 年首先想到把 Minkowski 这个关于有限维空间中凸闭集的分离定理推广到无穷维的赋范线性空间. 此外, 他还从几何的观点来陈述 Hahn-Banach 定理, 并且得到下列重要结果 (参见 [26], § VIII.2).

定理 2.5(Mazur,1933) 设 M 是实赋范线性空间 X 中的凸闭集. 若 $0 \in M$ ，而 $x_{0} \notin M$ . 则存在 X 上连续实线性泛函 f，使

(2.6) $f(x_0) > 1$ ，而 $f(x)\leqslant 1$ ，当 $x\in M$

证设 $\delta = \mathrm{dist}(x_0, M)$ , 因 $M$ 是闭的, $x_0 \notin M$ , 所以 $\delta > 0$ . 令

$$
U = \left\{x \in X: \| x \| <   \frac {\delta}{3} \right\},
$$

则 $U$ 是0的平衡的、吸收的凸邻域，且

$$
(M + U) \cap (x _ {0} + U) = \varnothing .
$$

这里， $M + U = \{x + y: x \in M, y \in U\}$ . 易见 $M + U$ 是凸的，吸收的，其闭包 $K$ 仍是凸的，吸收的闭集，且 $x_0 \notin K$ . 令

$$
p (x) = p _ {K} (x), x \in X.
$$

往证 $p(x)$ 在 $x = 0$ 处连续. 显然 $p(0) = 0$ , 又任给 $\varepsilon > 0$ , 取 $\rho = \varepsilon \frac{\delta}{3}$ . 当 $x \in X$ , $\| x \| < \rho$ ,

$$
\| \varepsilon^ {- 1} x \| <   \varepsilon^ {- 1} \rho = \frac {\delta}{3}.
$$

可见 $\varepsilon^{-1}x\in U\subset K$ .故

$$
0 \leqslant p (x) = p _ {K} (x) \leqslant \varepsilon .
$$

这表明 $p$ 在 $x = 0$ 处连续.

根据Minkowski泛函定义有

$$
p (x) \leqslant 1, \text {当} x \in K, p (x _ {0}) > 1.
$$

第一个不等式是显然的，往证第二个不等式. 若 $p(x_0) < 1$ ，则有 $0 < \alpha < 1$ ，使 $\alpha^{-1}x_0 \in K$ . 因 $0 \in K$ ，于是由 $K$ 是凸集可知，

$$
x _ {0} = \alpha (\alpha^ {- 1} x _ {0}) + (1 - \alpha) 0 \in K,
$$

与 $x_0 \notin K$ 矛盾. 若 $p(x_0) = 1$ , 则对任意正整数 $n$ , 存在正数 $\alpha_n$ , 使

$$
1 \leqslant \alpha_ {n} <   1 + \frac {1}{n},
$$

且 $\alpha_{n}^{-1}x_{0}\in K$ .因 $K$ 是闭的，故 $x_0 = \lim_{n\to \infty}\alpha_n^{-1}x_0\in K.$ 又产生矛盾.所以只可能 $p(x_0) > 1$

取 $G = \{\lambda x_0: \lambda \in \mathbb{R}\}$ , 令 $f_1(\lambda x_0) = \lambda p(x_0)$ , 则 $f_1$ 是 $G$ 上实线性泛函. 当 $\lambda \geqslant 0$ 时, 由命题2.6,

$$
f _ {1} (\lambda x _ {0}) = \lambda p (x _ {0}) = p (\lambda x _ {0}).
$$

当 $\lambda < 0$ 时，

$$
f _ {1} (\lambda x _ {0}) = \lambda p (x _ {0}) <   0 \leqslant p (\lambda x _ {0}).
$$

总之，

$$
f _ {1} (x) \leqslant p (x), \text {当} x \in G.
$$

再根据命题2.6和定理2.1，存在 $X$ 上实线性泛函 $f$ ，使

$$
f (x) = f _ {1} (x), \text {当} x \in G.
$$

$$
f (x) \leqslant p (x), \text {当} x \in X.
$$

于是

$$
f (x _ {0}) = f _ {1} (x _ {0}) = p (x _ {0}) > 1.
$$

注意 $M \subset K$ ，故

$$
f (x) \leqslant p (x) \leqslant 1, \text {当} x \in M.
$$

最后，证明 $f$ 是连续的线性泛函. 因 $f(x) \leqslant p(x), \forall x \in X$ . 故

$$
- f (x) = f (- x) \leqslant p (- x),
$$

从而

$$
- p (- x) \leqslant f (x) \leqslant p (x).
$$

由 $p(x)$ 在 $x = 0$ 处连续，可知 $f(x)$ 在 $x = 0$ 处连续. 根据第一章 §7 中定理 7.1, $f$ 是连续的线性泛函. 证毕.

注意, 定理 2.5 中 (2.6) 式是 $f(x_0) > 1$ . 一般把 (2.6) 说成超平面 $H = \{x \in X: f(x) = 1\}$ 将 $x_0$ 与 $M$ 严格分离. 定理 2.5 是关于严格分离性较早的研究. 此外, 它的证明也是典型的.

在 Mazur 之后又有下列更详尽的分离定理. (我们且只叙述, 但不予证明, 详情可参见 [39], §5.1.)

定理 2.6(M. Eidelheit, 1936) 设 A 和 B 是局部凸拓扑线性空间 X 中不相交凸集.

(1) 如果 A 是开的, 则它们可被一超平面分离;

(2) 如果 A, B 都是开的, 它们可被一超平面严格分离;

(3) 如果 $A$ 是紧的, $B$ 是闭的, 它们可被一超平面严格分离.

这些分离定理在理论上不只是对偶理论的基础,一些重要结果,诸如 Krein-Milman 定理,重极定理等等的证明都依赖于它们.此外,它们在凸分析及数量经济学中也有许多应用.

定义2.4 设 $M$ 是Banach空间 $X$ 中的点集. 如果存在 $M$ 中序列 $\{x_{n}\}_{n=1}^{\infty}$ , 对 $X$ 上任何连续线性泛函 $f$ , 都有

$$
\lim _ {n \rightarrow \infty} f (x _ {n}) = f (x _ {0}),
$$

则必有 $x_0 \in M$ . 我们称 $M$ 为弱序列闭的.

定理2.7 Banach空间中每个凸闭集都是弱序列闭的.

证假若不然, 存在 Banach 空间 $X$ 中凸闭集 $M$ , 及 $x_0 \in X$ 和 $M$ 中序列 $\{x_n\}_{n=1}^{\infty}$ , 对 $X$ 上任何连续线性泛函 $f$ , 都有

$$
\lim _ {n \rightarrow \infty} f (x _ {n}) = f (x _ {0}),
$$

但是 $x_0 \notin M$ .

不失一般性, 可设 $0 \in M$ . 根据定理 2.5, 存在 $X$ 上连续实线性泛函 $f$ , 使令

$$
f (x _ {0}) > 1, f (x) \leqslant 1, \text {当} x \in M.
$$

$$
F (x) = f (x) - \mathrm{i} f (\mathrm{i} x), \forall x \in X.
$$

如定理2.2一样可以证明. $F$ 是 $X$ 上连续线性泛函.于是

$$
\lim _ {n \rightarrow \infty} F (x _ {n}) = F (x _ {0}),
$$

进而 $\lim_{n\to \infty}\mathrm{Re}F(x_n) = \mathrm{Re}F(x_0)$ . 但是

$$
\operatorname{Re} F (x _ {n}) = f (x _ {n}) \leqslant 1, \operatorname{Re} F (x _ {0}) = f (x _ {0}) > 1,
$$

矛盾. 证毕.

以后我们将引进一般的弱拓扑,同样的方法可以证明

## Banach 空间中每个凸闭集都是弱闭的.

这是 Mazur 定理的一个很重要的推论.

## § 3 Baire 纲推理命题3.1 设 $X, Y$ 都是赋范线性空间, 则线性算子 $T: X \to Y$ 是有界的充分必要条件是 $T^{-1}\{y\in Y:\| y\| \leqslant 1\}$ 的内部为非空集.

证若 $T^{-1}\{y \in Y: \| y \| \leqslant 1\}$ 含有小球

$$
U = \{x \in X: \| x - x _ {0} \| <   \varepsilon \},
$$

对于 $x \in X, \| x \| < \varepsilon$ ，显然 $x + x_0 \in U$ . 从而

$$
\| T x \| \leqslant \| T (x + x _ {0}) \| + \| T x _ {0} \| \leqslant 1 + \| T x _ {0} \|.
$$

对于 $x \in X, x \neq 0, \left\| \frac{\varepsilon}{2 \| x \|} x \right\| < \varepsilon$ ，则

$$
\left\| T \left(\frac {\varepsilon}{2 \| x \|} x\right) \right\| \leqslant 1 + \| T x _ {0} \|,
$$

即

$$
\| T x \| \leqslant \frac {2}{\varepsilon} (1 + \| T x _ {0} \|) \| x \|.
$$

这表明 $T$ 是有界的. 至于必要性的证明是容易的. 证毕.

正如这个命题所表明的,人们对于内部不空的点集发生兴趣.

定义 3.1 设 X 是距离空间, $S \subset X$ , 如果 $\bar{S}$ 的内部是空集, 则称 S 是无处稠密的.

容易证明,如果 S 是无处稠密的,则 S 不在 X 中任何球内稠密.

定义3.2 在距离空间 $X$ 中，若 $E = \bigcup_{n=1}^{\infty} S_n$ ，而每个 $S_n$ 都是 $X$ 中无处稠密的，则称点集 $E$ 为第一纲的。非第一纲点集称为第二纲的。

定理 3.1(Baire 纲定理,1899) 完备的距离空间 X 必是第二纲的.

证否则, $X = \bigcup_{n=1}^{\infty} S_n$ , 每个 $S_n$ 都是无处稠密的. 因为 $S_1$ 无处稠密, 必有 $x_1 \notin \bar{S}_1$ . 从而有小球 $U_1 = \{x : d(x, x_1) < r_1\}$ 使

$$
U _ {1} \cap \bar {S} _ {1} = \varnothing .
$$

由于 $S_{2}$ 无处稠密，在 $U_{1}$ 中必有 $x_{2} \notin \bar{S}_{2}$ . 从而有以 $x_{2}$ 为心小球 $U_{2}$ , 使

$$
\overline {{{U}}} _ {2} \subset U _ {1}, U _ {2} \cap \bar {S} _ {2} = \varnothing .
$$

自然可设 $U_{2}$ 的半径 $r_2$ 小于 $\frac{1}{2}$ . 如此继续下去, 对每个自然数 $n \geqslant 2$ , 应有以 $x_{n}$ 为心小球 $U_{n}$ , 使

$$
\overline {{{U}}} _ {n} \subset U _ {n - 1}, U _ {n} \cap \overline {{{S}}} _ {n} = \varnothing .
$$

且 $U_{n}$ 的半径 $r_n$ 小于 $\frac{1}{2^{n - 1}}$ . 于是当 $m \geqslant n, x_m \in U_n$ , 故

$$
d \left(x _ {n}, x _ {m}\right) <   \frac {1}{2 ^ {n - 1}}.
$$

这说明 $\{x_{n}\}_{n=1}^{\infty}$ 是X中的Cauchy序列.从X的完备性,应有 $x_{n}\rightarrow x\in X$ .注意 $x_{m}\in U_{n}$ ,当 $m\geqslant n$ ,于是, $x\in\overline{U}_{n}\subset U_{n-1}$ .故 $x\notin S_{n-1},n=2,3,\cdots$ .这和 $X=\bigcup_{n=1}^{\infty}S_{n}$ 矛盾.证毕.

例1 在 $I = [0,1]$ 上存在处处连续但处处不可微的函数.

设 $E$ 是 $\mathbb{R}$ 上所有周期为1的连续函数组成的集合. 易见按范数

$$
\| f \| = \max _ {0 \leqslant x \leqslant 1} | f (x) |, f \in E,
$$

$E$ 构成完备赋范线性空间. 对每个正整数 $n$ , 令

$N_{n}=\{f\in E:$ 有一点 $x\in I$ ,使 $\frac{|f(x+h)-f(x)|}{h}\leqslant n,\forall h>0\}$ .

显然每个 $f \in E$ ，只要在 $I$ 中一点可微，便一定在某个 $N_{n}$ 中。以下来证明

(一) $\forall n \in N, N_{n}$ 是 E 中闭集.

设 $f_{k} \in N_{n}, k = 1, 2, \cdots$ . 且 $\{f_{k}\}_{k=1}^{\infty}$ 在 $[0,1]$ 上一致地收敛于 $f_{0}$ . 按 $N_{n}$ 的定义, 应有 $x_{k} \in I$ , 使

$$
\frac {\mid f _ {k} (x _ {k} + h) - f _ {k} (x _ {k}) \mid}{h} \leqslant n, \forall h > 0.\tag{3.1}
$$

注意 $\{x_{k}\}_{k = 1}^{\infty}$ 有收敛子序列，不妨设 $x_{k}\rightarrow x_{0}$ ，当 $k\to \infty$ ，则 $x_0\in I.$ 现在对任意 $h\geqslant 0$

$$
\begin{array}{r l} & {\mid f _ {k} (x _ {k} + h) - f _ {0} (x _ {0} + h) \mid} \\ & {\leqslant \mid f _ {k} (x _ {k} + h) - f _ {0} (x _ {k} + h) \mid + \mid f _ {0} (x _ {k} + h) - f _ {0} (x _ {0} + h) \mid ,} \end{array}
$$

据此和 $\{f_k\}_{k=1}^{\infty}$ 的一致收敛性可见在(3.1)式中令 $k \to \infty$ ，可得

$$
\frac {\left| f _ {0} \left(x _ {0} + h\right) - f _ {0} \left(x _ {0}\right) \right|}{h} \leqslant n, \forall h > 0.
$$

故 $f_0 \in N_n$ 。即 $N_n$ 是闭集。

(二) $\forall n \in N, N_{n}$ 无处稠密.

否则,有球 $K = \{f: \| f - f_0 \| < \varepsilon\} \subset N_n$ . 显然我们可以找到一个折线函数 $\varphi(x)$ , 使得

$$
\| \varphi - f _ {0} \| = \max _ {0 \leqslant x \leqslant 1} | \varphi (x) - f _ {0} (x) | <   \varepsilon ,
$$

而且 $\varphi$ 之每段斜率的绝对值都大于 $n$ . 于是 $\varphi \in K$ , 但 $\varphi \notin N_n$ , 矛盾.

总之，点集 $\bigcup_{n=1}^{\infty} N_n$ 是第一纲的。而根据Baire纲定理， $E$ 是第二纲的。故必有 $\psi \in E$ ，但 $\psi$ 不在任何 $N_n$ 中，显然这个 $\psi$ 便是处处连续且处处不可微的函数。

定理3.2(一致有界原理或共鸣定理,1927) 设 $X$ 是Banach空间, $Y$ 是赋范线性空间, $\{T_{\tau}\}_{\tau \in \mathcal{A}}$ 是 $L(X,Y)$ 中的一族元素. 若

$$
\sup _ {\tau \in \mathcal {A}} \| T _ {\tau} x \| <   \infty , \forall x \in X.\tag{3.2}
$$

则

$$
\sup _ {\tau \in \mathcal {V}} \| T _ {\tau} \| <   \infty .
$$

证设 $S_{n} = \{x \in X : \sup_{\tau \in \mathcal{A}} \| T_{\tau} x \| \leqslant n\}, n = 1,2,\dots$ . 则由(3.2)式可知, $X = \bigcup_{n=1}^{\infty} S_{n}$ . 由于每个 $T_{\tau}$ 都连续, 故每个 $S_{n}$ 都是闭的. 根据定理3.1, $X$ 是第二纲的, 所以必定有某个 $S_{N}$ 不是无处稠密的, 即 $S_{N}$ 内部不是空集. 从而存在小球 $U = \{x : \| x - x_{0} \| < \varepsilon\}$ , 使 $U \subset S_{N}$ .

若 $x \in X, \| x \| < \varepsilon$ ，则 $x + x_0 \in U$ . 于是， $x + x_0, x_0 \in S_N$ ，从而对任何 $\tau \in \mathcal{A}$ ，

$$
\| T _ {\tau} x \| \leqslant \| T _ {\tau} (x + x _ {0}) \| + \| T _ {\tau} x _ {0} \| \leqslant 2 N.
$$

设 $x \in X, x \neq 0$ ，则 $\left\| \frac{\varepsilon}{2 \| x \|} x \right\| < \varepsilon$ ，故

$$
\left\| T _ {\mathrm{r}} \left(\frac {\varepsilon}{2 \| x \|} x\right) \right\| \leqslant 2 N,
$$

即

$$
\parallel T _ {r} x \parallel \leqslant \frac {4 N}{\varepsilon} \parallel x \parallel .
$$

当 $x = 0$ ，上述不等式显然成立.总之

$$
\| T _ {r} x \| \leqslant \frac {4 N}{\varepsilon} \| x \|, \forall x \in X.
$$

所以，对任何 $\tau \in \mathcal{A}$ 都有

$$
\| T _ {\tau} \| \leqslant \frac {4 N}{\varepsilon}.
$$

证毕.

由证明可见, 只须假定(3.2)式在 X 中第二纲点集上成立, 即可保证定理为真.

例2 在19世纪,人们就已经提出连续函数之Fourier级数的收敛问题.许多人举例说明确有连续函数,其Fourier级数竟在某一点发散,现在我们利用一致有界原理来处理这个问题.

设 $\{\varphi_n\}_{n=1}^{\infty}$ 是 $L^2 [a,b]$ 中的一个正规正交基.对固定的 $x_0\in [a,b],f\in$ $L^2 [a,b]$ 在 $x_0$ 点之Fourier级数的 $n$ 项部分和为

$$
\begin{array}{r l} S _ {n} (x _ {0}, f) & = \sum_ {m = 1} ^ {n} \varphi_ {m} (x _ {0}) \int_ {a} ^ {b} f (t) \varphi_ {m} (t) \mathrm{d} t \\ & = \int_ {a} ^ {b} f (t) K _ {n} (x _ {0}, t) \mathrm{d} t, \end{array}
$$

这里

$$
K _ {n} (x _ {0}, t) = \sum_ {m = 1} ^ {n} \varphi_ {m} (x _ {0}) \varphi_ {m} (t).
$$

兹令

$$
\rho_ {n} (x _ {0}) \stackrel {\mathrm{d}} {=} \int_ {a} ^ {b} | K _ {n} (x _ {0}, t) | \mathrm{d} t.
$$

一般称之为Lebesgue函数.

若上述的 $f(x)$ 及 $\{\varphi_n(x)\}_{n=1}^{\infty}$ 都是 $[a, b]$ 上的连续函数，则 $S_n(x_0, f)$ 可以看作 $C[a, b]$ 上的线性泛函。仿照 §1 中例 1 可以证明

$$
\| S _ {n} \| = \sup _ {\| f \| \leqslant 1} \left| \int_ {a} ^ {b} f (t) K _ {n} \left(x _ {0}, t\right) d t \right| = \rho_ {n} \left(x _ {0}\right).
$$

命题3.2 若 $\lim_{n\to \infty}\rho_n(x_0) = \infty$ ，则有连续函数 $f$ ，其Fourier级数在 $x_0$ 处发散.

证否则， $\{S_n(x_0,f)\}_{n = 1}^{\infty}$ 在 $C[a,b]$ 上处处收敛，即

$$
\sup _ {1 \leqslant n <   \infty} | S _ {n} (x _ {0}, f) | <   \infty , \forall f \in C [ a, b ].
$$

由一致有界原理,应有常数 M>0,使

$$
\rho_ {n} (x _ {0}) = \parallel S _ {n} \parallel \leqslant M, \forall n \in \mathbf {N}.
$$

与假设矛盾. 证毕.

特别对三角系统

$$
\frac {1}{\sqrt {2 \pi}}, \frac {1}{\sqrt {\pi}} \cos x, \frac {1}{\sqrt {\pi}} \sin x, \dots , \frac {1}{\sqrt {\pi}} \cos k x, \frac {1}{\sqrt {\pi}} \sin k x, \dots ,
$$

我们有

$$
\begin{array}{r l} \rho_ {n} (x) & = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) (t - x)}{\sin \left(\frac {1}{2}\right) (t - x)} \right| \mathrm{d} t \\ & = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) t}{\sin \left(\frac {1}{2}\right) t} \right| \mathrm{d} t \\ & = \rho_ {n}. \end{array}
$$

(参见[7], 第七章)

引理3.1 $\rho_{n}\rightarrow \infty$ ，当 $n\to \infty$

证从 Jordan 不等式(参见[8], 第 141—142 页, 例 4):

$\frac{2}{\pi} \leqslant \frac{\sin x}{x} \leqslant 1$ ，当 $0 < x \leqslant \frac{\pi}{2}$ ，

可见

$$
\rho_ {n} \geqslant \frac {1}{2 \pi} \int_ {0} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) t}{\sin \left(\frac {1}{2}\right) t} \right| d t
$$

$$
\begin{array}{l} \geqslant \frac {1}{2 \pi} \int_ {0} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) t}{\left(\frac {1}{2}\right) t} \right| \mathrm{d} t \\ = \frac {1}{\pi} \int_ {0} ^ {\left(n + \frac {1}{2}\right) \pi} \left| \frac {\sin u}{u} \right| \mathrm{d} u \\ \geqslant \frac {1}{\pi} \left[ \int_ {0} ^ {\pi} \left| \frac {\sin u}{u} \right| \mathrm{d} u + \dots + \int_ {(n - 1) \pi} ^ {n \pi} \left| \frac {\sin u}{u} \right| \mathrm{d} u \right]. \end{array}
$$

而

$$
\begin{array}{r l} \int_ {k \pi} ^ {(k + 1) \pi} \left| \frac {\sin u}{u} \right| \mathrm{d} u & \geqslant \frac {1}{(k + 1) \pi} \int_ {k \pi} ^ {(k + 1) \pi} | \sin u | \mathrm{d} u \\ & = \frac {1}{(k + 1) \pi} \int_ {0} ^ {\pi} | \sin u | \mathrm{d} u \\ & = \frac {2}{(k + 1) \pi}, \end{array}
$$

$k=0,1,2,\cdots,n-1.$ 于是

$$
\rho_ {n} \geqslant \frac {2}{\pi^ {2}} \left(1 + \frac {1}{2} + \dots + \frac {1}{n}\right).
$$

故 $\rho_{n}\rightarrow \infty$ ，当 $n\to \infty$ .证毕.

由命题3.2和引理3.1可见，对 $(0,2\pi)$ 上任给一点，都存在 $f \in C[0,2\pi]$ ，其Fourier级数在该点发散。事实上对 $(0,2\pi)$ 中任意一串点 $\{x_m\}_{m=1}^{\infty}$ ，从前面结果有连续函数 $f_m(x) \in C[0,2\pi]$ ，使 $S_n(x_m, f_m)$ 发散。考察

$$
H _ {m} = \{f \in C [ 0, 2 \pi ]: S _ {n} (x _ {m}, f) \text {收敛} \}.
$$

注意,对于三角系统

$$
\parallel S _ {n} (x _ {m}, f) \parallel = \rho_ {n} (x _ {m}) = \rho_ {n} \rightarrow \infty , \text {当} n \rightarrow \infty .
$$

根据定理3.2下面的注， $H_{m}$ 必定是第一纲的，从而 $\bigcup_{m = 1}^{\infty}H_m$ 也是第一纲的.而 $C[0,2\pi ]$ 是第二纲的，故存在

$$
f \in C [ 0, 2 \pi ] \setminus \left[ \bigcup_ {m = 1} ^ {\infty} H _ {m} \right].
$$

如此之 $f(x)$ 的Fourier级数便在所有点 $\pmb{x}_{m}$ 处发散.

## 例3 机械求积法在定积分的近似计算中,通常以泛函

$$
f _ {n} (x) = \sum_ {k = 0} ^ {n} A _ {k} ^ {(n)} x (t _ {k} ^ {(n)}), 0 \leqslant t _ {0} ^ {(n)} <   t _ {1} ^ {(n)} <   \dots <   t _ {n} ^ {(n)} \leqslant 1.\tag{3.3}
$$

作为 $x(t)$ 的积分 $\int_0^1 x(t)\mathrm{d}t$ 的近似值.这就是通常所谓的机械求积法.(3.3)式称为机械求积公式. 一个自然提出的问题是: 在什么样条件下, 由(3.3)式定义的泛函 $f_{n}(x)$ 对每个连续函数 $x(t)$ 都收敛于积分 $\int_{0}^{1} x(t) \mathrm{d}t$ . 一个常见的结果是定理 3.3(Стеклов - Szegö, 1916) 对任意的 $x \in C[0,1]$ , $f_{n}(x)$ 都收敛于 $\int_{0}^{1} x(t) dt$ 的充分必要条件是

(1) 存在常数 M > 0，使 $\sum_{k=0}^{n}|A_{k}^{(n)}| \leqslant M$ ，

(2) 对任给的多项式 $x(t), f_n(x) \to \int_0^1 x(t) \mathrm{d}t$ ，当 $n \to \infty$ .

证必要性,首先,对任意的 $x \in C[0,1]$ ,

$$
\mid f _ {n} (x) \mid \leqslant \sum_ {k = 0} ^ {n} \mid A _ {k} ^ {(n)} \mid \mid x (t _ {k} ^ {(n)}) \mid \leqslant \left(\sum_ {k = 0} ^ {n} \mid A _ {k} ^ {(n)} \mid\right) \parallel x \parallel ,
$$

故

$$
\parallel f _ {n} \parallel \leqslant \sum_ {k = 0} ^ {n} | A _ {k} ^ {(n)} |.
$$

另一方面，对每个 $n$ ，可以取[0,1]上的连续函数 $x_{n}(t)$ ，使

$$
x _ {n} \left(t _ {k} ^ {(n)}\right) = \operatorname{sgn} A _ {k} ^ {(n)}, k = 0, 1, \dots , n.
$$

而且 $\| x_{n}\| = 1$ .于是

$$
\mid f _ {n} (x _ {n}) \mid = \sum_ {k = 0} ^ {n} A _ {k} ^ {(n)} x _ {n} (t _ {k} ^ {(n)}) = \sum_ {k = 0} ^ {n} \mid A _ {k} ^ {(n)} \mid ,
$$

总之，我们有

$$
\| f _ {n} \| = \sum_ {k = 0} ^ {n} | A _ {k} ^ {(n)} |.\tag{3.4}
$$

于是由一致有界原理可知条件(1)是必要的.至于(2)是自然的.

充分性. 任给 $x \in C[0,1]$ , 由 Weierstrass 定理, 存在多项式 $x_{1}$ , 使

$$
\| x - x _ {1} \| <   \epsilon / [ 2 (M + 1) ].
$$

根据(2)，存在正整数 N，使当 n > N，

$$
\left| f _ {n} \left(x _ {1}\right) - \int_ {0} ^ {1} x _ {1} (t) \mathrm{d} t \right| <   \frac {\varepsilon}{2}.
$$

于是由(1)与(3.4)式, 当 n > N,

$$
\begin{array}{r l} & {\left| f _ {n} (x) - \int_ {0} ^ {1} x (t) \mathrm{d} t \right| \leqslant \left| f _ {n} (x) - f _ {n} (x _ {1}) \right| + \left| f _ {n} (x _ {1}) - \int_ {0} ^ {1} x _ {1} (t) \mathrm{d} t \right| +} \\ & {\qquad \left| \int_ {0} ^ {1} x _ {1} (t) \mathrm{d} t - \int_ {0} ^ {1} x (t) \mathrm{d} t \right|} \\ & {\qquad \leqslant \| f _ {n} \| \| x - x _ {1} \| + \frac {\varepsilon}{2} + \| x _ {1} - x \|} \end{array}
$$

$$
\begin{array}{l} \leqslant (M + 1) \| x - x _ {1} \| + \frac {\varepsilon}{2} \\ <   \varepsilon . \end{array}
$$

证毕：

定义 3.3 对线性空间中的点集 A 与 B, 数 $\lambda$ 与 $\mu$ , 定义

$$
\lambda A + \mu B = \{\lambda x + \mu y: x \in A, y \in B \}.
$$

若 $A$ 是单点集 $\{x\}$ , 数 $\lambda$ 与 $\mu$ 皆为 1, 则 $A + B$ 简记为 $x + B$ .

引理3.2 在赋范线性空间中，

(1) $\overline{A} +\overline{B}\subset \overline{A + B};$

(2) 若 $y_j$ 是 $A_j$ 的内点, $j = 1, 2$ , 则 $y_1 + y_2$ 是 $A_1 + A_2$ 的内点.

证（1）是显然的.至于(2)，从 $y_{2}$ 是 $A_{2}$ 的内点，存在 $r > 0$ ，使 $U_{2} = \{y: \| y - y_{2} \| < r\} \subset A_{2}$ .注意

$$
y _ {1} + U _ {2} = \{z: \| z - (y _ {1} + y _ {2}) \| <   r \}
$$

是 $y_{1} + y_{2}$ 的邻域，且 $y_{1} + U_{2} \subset A_{1} + A_{2}$ . 故 $y_{1} + y_{2}$ 是 $A_{1} + A_{2}$ 的内点. 证毕.

定理3.4 设 $X$ 与 $Y$ 都是Banach空间， $T \in L(X, Y)$ . 如果 $R(T)$ 是第二纲的，则于任何 $\varepsilon > 0$ ，都有 $\eta > 0$ ，使开球 $\{x \in X: \| x \| < \varepsilon\}$ 在映射 $T$ 之下的像包含开球 $\{y \in Y: \| y \| < \eta\}$ .

## 证证明分两步进行.

（一）首先证明 $\forall r > 0, \exists \delta > 0$ ，使

$$
\overline {{{T \{x \in X : \| x \| <   r \}}}} \supset \{y \in Y: \| y \| <   \delta \}.
$$

设 $V = \{x\in X:\| x\| < r\}$ ，显然 $0\in \overline{TV}$ ，现在需要证明0是 $\overline{TV}$ 的内点.取

$$
W = \left\{x \in X: \| x \| <   \frac {r}{2} \right\},
$$

则 $W$ 是平衡的，而且 $W + W \subset V$ . 显然 $\bigcup_{k=1}^{\infty}(kW) = X$ ，于是

$$
\bigcup_ {k = 1} ^ {\infty} T (k W) = T (X) = R (T).
$$

由假设， $R(T)$ 是第二纲的.因此，至少有一个自然数 $k_{0}$ ，使 $k_{0}(\overline{TW}) = \overline{T(k_{0}W)}$ 包含内点.从而 $\overline{TW}$ 含有内点，设其为 $y^{\prime}$ .注意 $TW$ 是平衡的，从而 $\overline{TW}$ 也是平衡的，故 $-y^{\prime}$ 也是 $\overline{TW}$ 的内点.由引理3.2, $0 = y' - y'$ 便是 $\overline{TW} +\overline{TW}\subset$ $\overline{TW + TW}\subset \overline{TV}$ 的内点，即 $\overline{TV}$ 含有某个开球 $\{y\in Y:\| y\| <  \delta \}$

（二）对任意 $\varepsilon > 0$ ，令 $\varepsilon_{j} = \frac{\varepsilon}{2^{j}}, j = 1, 2, \cdots$ . 根据（一），应有 $\eta_{j} > 0, j = 1, 2, \cdots$ . 使

$$
\overline {{{T \{x \in X : \| x \| <   \varepsilon_ {j} \}}}} \supset \{y \in Y: \| y \| <   \eta_ {j} \}, j = 1, 2, \dots .\tag{3.5}
$$

不妨设 $\{\eta_j\}_{j=1}^{\infty}$ 单调减少且趋于零. 取 $\eta = \eta_1$ ，我们断言

$$
T \{x \in X: \| x \| <   \varepsilon \} \supset \{y \in Y: \| y \| <   \eta \}.
$$

即任给 $y_0 \in Y$ ，只要 $\| y_0 \| < \eta$ ，就有 $x_0 \in X, \| x_0 \| < \epsilon$ ，使 $y_0 = Tx_0$ ，从而定理为真。

事实上，由 $\| y_0\| < \eta_1$ ，从(3.5)式(取 $j = 1$ )， $y_{0}\in \overline{T\{x\in X:\| x\| < \varepsilon_{1}\}}$ 故应有 $x_{1}\in X$ 及 $y_{1} = Tx_{1}$ ，使

$$
\parallel x _ {1} \parallel <   \varepsilon_ {1}, \text {且} \parallel y _ {0} - y _ {1} \parallel <   \eta_ {2}.
$$

又由(3.5)式(取 $j = 2$ ), $y_0 - y_1 \in T \{x \in X : \| x \| < \epsilon_2\}$ , 应有 $x_2 \in X$ 及 $y_2 = Tx_2$ , 使

$$
\parallel x _ {2} \parallel <   \varepsilon_ {2}, \text {且} \parallel (y _ {0} - y _ {1}) - y _ {2} \parallel <   \eta_ {3}.
$$

如此继续下去得到 $x_{k} \in X$ 及 $y_{k} = Tx_{k}$ 使

$\| x_{k} \| < \varepsilon_{k}$ ，且 $\left\|(y_{0}-y_{1}-\cdots-y_{k-1})-y_{k}\right\| < \eta_{k+1}, k=1,2,\cdots$ 注意当 m > n，

$$
\left\| \sum_ {k = 1} ^ {m} x _ {k} - \sum_ {k = 1} ^ {n} x _ {k} \right\| \leqslant \sum_ {k = n + 1} ^ {m} \| x _ {k} \| <   \sum_ {k = n + 1} ^ {m} \varepsilon_ {k} = \sum_ {k = n + 1} ^ {m} \frac {\varepsilon}{2 ^ {k}}.
$$

可见 $\left\{\sum_{k=1}^{n} x_k\right\}_{n=1}^{\infty}$ 是一个 Cauchy 序列, 而 $X$ 是完备的, 故应有

$$
x _ {0} = \sum_ {k = 1} ^ {\infty} x _ {k} = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} x _ {k} \in X,
$$

且

$$
\| x _ {0} \| <   \sum_ {k = 1} ^ {\infty} \frac {\varepsilon}{2 ^ {k}} = \varepsilon .
$$

又 $\{\eta_j\}_{j=1}^{\infty}$ 单调减少且趋于零，故

$$
\sum_ {j = 1} ^ {k} y _ {j} \rightarrow y _ {0}, \text {当} k \rightarrow \infty .
$$

于是

$$
T x _ {0} = \sum_ {k = 1} ^ {\infty} T x _ {k} = \sum_ {k = 1} ^ {\infty} y _ {k} = y _ {0}.
$$

证毕.

经过平移,便可把前面定理叙述成定理3.5(开映射定理,1932) 设 $X$ 与 $Y$ 都是Banach空间, $T \in L(X, Y)$ . 如果 $R(T)$ 是第二纲的, 则映射 $T$ 变 $X$ 中开集为 $Y$ 中开集.

证设 G 是 X 中开集, 往证 $T(G)$ 是 Y 中开集.

$\forall y_0 \in T(G), \exists x_0 \in G$ ，使 $y_0 = Tx_0$ 。由于 $G$ 是开集， $x_0$ 是 $G$ 的内点，存在 $\varepsilon > 0$ ，使

$$
\{x \in X: \| x - x _ {0} \| <   \varepsilon \} \subset G.
$$

注意

$$
\{x \in X: \| x - x _ {0} \| <   \varepsilon \} = x _ {0} + \{x \in X: \| x \| <   \varepsilon \},
$$

由于 $T$ 是线性的，于是

$$
\begin{array}{r l} T (G) \supset & T \{x \in X: \| x - x _ {0} \| <   \varepsilon \} \\ & = T x _ {0} + T \{x \in X: \| x \| <   \varepsilon \} \\ & = y _ {0} + T \{x \in X: \| x \| <   \varepsilon \}. \end{array}
$$

由定理3.4存在 $\eta > 0$ ，使

$$
T \{x \in X: \| x \| <   \varepsilon \} \supset \{y \in Y: \| y \| <   \eta \}.
$$

于是

$$
\begin{array}{r l} T (G) \supset y _ {0} + T \{x \in X: \| x \| <   \epsilon \} \\ \supset y _ {0} + \{y \in Y: \| y \| <   \eta \}. \end{array}
$$

而

$$
y _ {0} + \{y \in Y: \| y \| <   \eta \} = \{y \in Y: \| y - y _ {0} \| <   \eta \},
$$

故

$$
\{y \in Y: \| y - y _ {0} \| <   \eta \} \subset T (G).
$$

可见 $y_0$ 是 $T(G)$ 的内点，又 $y_0 \in T(G)$ 是任意的，因而 $T(G)$ 是开集. 证毕.

从定理3.4易见命题 3.3 Banach 空间上连续线性算子的像或者构成第一纲点集, 或者充满全空间.

定理 3.6(Banach 逆算子定理,1929) 设 X 与 Y 都是 Banach 空间, $T \in L(X,Y)$ . 如果 T 是一对一而且满射的, 则 $T^{-1}$ 是连续的.

证根据开映射定理, 对 $X$ 中的任意开集 $O, (T^{-1})^{-1}(O) = T(O)$ 是开的. 于是由第一章 §4 中定理 4.1, $T^{-1}$ 是连续的. 证毕.

根据 Banach 逆算子定理可知, 如果 $T \in L(X, Y)$ 是双射的, 则 $T$ 必是有界可逆的, 即 $T^{-1} \in L(Y, X)$ .

命题3.4 设在同一个线性空间 $X$ 上存在着两个范数 $\| \cdot \|$ 与 $\| \cdot \|_1$ ，它们都使 $X$ 成为Banach空间，如果 $\| \cdot \|$ 强于 $\| \cdot \|_1$ ，则 $\| \cdot \|$ 与 $\| \cdot \|_1$ 等价。

证设 $X$ 在范数 $\| \cdot \|$ 及 $\| \cdot \|_1$ 下构成的 Banach 空间依次记为 $E$ 与 $E_1$ ，则 $Tx = x, \forall x \in X$ ，是变 $E$ 为 $E_1$ 的双射的连续线性算子，由 Banach 逆算子定理可见本命题成立。证毕。

定义3.4 设 $X$ 与 $Y$ 都是赋范线性空间, $M$ 是 $X$ 中线性流形, $T: M \to Y$ 是线性算子, $M$ 称为 $T$ 的定义域, 记为 $\mathcal{D}(T)$ .

如果从 $x_{n} \in \mathcal{D}(T)$ , $n = 1, 2, \cdots$ ,

$$
\lim _ {n \to \infty} x _ {n} = x _ {0} \text {与} \lim _ {n \to \infty} T x _ {n} = y _ {0}
$$

恒有 $x_0 \in \mathcal{D}(T)$ , 且 $Tx_0 = y_0$ , 则称 $T$ 为闭算子.

设 $X$ 与 $Y$ 都是赋范线性空间， $T: \mathcal{D}(T)(\subset X) \to Y$ 是线性算子。人们定义

$$
G (T) \stackrel {\mathrm{d}} {=} \{\langle x, y \rangle \in X \times Y: x \in \mathcal {D} (T), y = T x \},
$$

称 $G(T)$ 为算子 $T$ 的图形. 若对 $\langle x, y \rangle \in X \times Y$ , 引进范数

$$
\| \langle x, y \rangle \| = \| x \| + \| y \|,
$$

则 $X \times Y$ 是赋范线性空间. 所谓 $T$ 是闭算子即 $T$ 的图形 $G(T)$ 是 $X \times Y$ 中闭集.

例4 连续函数空间 $C[a, b]$ 上的微分算子是闭算子.

令 $M = \{x \in C[a, b] : x' \in C[a, b]\}$ , 这里 $x'$ 表示 $x$ 的导函数, 则 $M$ 是 $C[a, b]$ 的线性流形. 定义

$$
T x = x ^ {\prime}, \forall x \in M.
$$

易见 $T$ 是从 $M$ 到 $C[a, b]$ 的线性算子. 设 $x_{n} \in M, n = 1, 2, \cdots$ , 使

$$
x _ {n} \rightarrow x _ {0}, \quad T x _ {n} \rightarrow y _ {0}.
$$

即 $x_{n}$ 一致收敛于 $x_0, x_n$ 的导函数 $x_n'$ 一致收敛于 $y_0$ . 由数学分析可知, $x_0' = y_0$ . 则 $x_0 \in M$ , 且 $Tx_0 = y_0$ . 即 $T$ 是闭算子. 但是容易知道 $T$ 不是有界的.

定理3.7(闭图形定理,1931) 设 $T$ 是从Banach空间 $X$ 到Banach空间 $Y$ 的处处有定义的闭算子, 则 $T$ 是有界的.

证对 $x \in X$ ，引进新范数

$$
\| x \| _ {1} = \| x \| + \| T x \|. \tag {1}
$$

设 $\{x_{n}\}_{n = 1}^{\infty}$ 按 $\| \cdot \| _1$ 是Cauchy序列，即任给 $\varepsilon >0$ ，存在正整数 $N$ ，使

$$
\| x _ {n} - x _ {m} \| _ {1} = \| x _ {n} - x _ {m} \| + \| T x _ {n} - T x _ {m} \| <   \epsilon , \text {当} n, m \geqslant N,
$$

则 $\{x_{n}\}_{n = 1}^{\infty},\{Tx_{n}\}_{n = 1}^{\infty}$ 分别是 $X,Y$ 中Cauchy序列. $X,Y$ 都是完备的，故存在 $x_0\in X,y_0\in Y$ ，使

$$
\lim _ {n \rightarrow \infty} x _ {n} = x _ {0}, \quad \lim _ {n \rightarrow \infty} T x _ {n} = y _ {0}.
$$

由于 $T$ 是闭算子，故 $y_0 = Tx_0$ 。于是

$$
\parallel x _ {n} - x _ {0} \parallel_ {1} = \parallel x _ {n} - x _ {0} \parallel + \parallel T x _ {n} - T x _ {0} \parallel \rightarrow 0, \quad \text {当} n \rightarrow \infty .
$$

故 $X$ 按范数 $\| \cdot \| _1$ 也构成Banach空间，显然

$$
\| x \| \leqslant \| x \| _ {1}, \forall x \in X.
$$

即 $\| \cdot \|_1$ 强于 $\| \cdot \|$ . 根据命题3.4, $\| \cdot \|_1$ 与 $\| \cdot \|$ 等价. 于是, 当

$$
\| x _ {n} - x _ {0} \| \rightarrow 0,
$$

总有

$$
\parallel T x _ {n} - T x _ {0} \parallel \leqslant \parallel x _ {n} - x _ {0} \parallel_ {1} \rightarrow 0,
$$

即 $T$ 是连续的. 证毕.

要懂得闭图形定理的好处,可对线性算子 T 考察下面三个叙述:

(1) $x_{n}\rightarrow x_{0},$

(2) $Tx_{n}\rightarrow y_{0}$

(3) $Tx_{0} = y_{0}$ .

通常证明 $T$ 在 $x_0$ 处连续，需要从(1)推出(2)和(3)来.现在由闭图形定理，则只要从(1)和(2)推出(3)即可，多了一个假设，当然要省力些.

命题 3.5(Hellinger-Toeplitz 定理,1910) 设 A 是从 Hilbert 空间 H 到自身的处处定义的线性算子. 如果

$$
(A x, y) = (x, A y), \text {当} x, y \in H,
$$

则 A 是有界的.

证若 $\lim_{n\to \infty}x_n = x_0,\lim_{n\to \infty}Ax_n = y_0$ .则于任何 $y\in H$ ，从假设有

$$
\left(A x _ {n}, y\right) = \left(x _ {n}, A y\right), n = 1, 2, \dots ,
$$

令 $n\to \infty$ ，便有

$$
(y _ {0}, y) = (x _ {0}, A y).
$$

又由假设有

$$
(y _ {0}, y) = (A x _ {0}, y).
$$

可见 $Ax_0 = y_0$ ，故 $\pmb{A}$ 是闭算子.根据闭图形定理知 $\pmb{A}$ 是有界的.证毕.

量子力学中的力学量 A, 如能量算符, 动量算符等, 它们对 Hilbert 空间 H 中某些元 x, y 满足关系式

$$
(A x, y) = (x, A y).
$$

为了便于运算, 当然希望能把 $A$ 扩张到整个空间 $H$ 上去, 使得上述关系在 $H$ 上处处成立. 但我们容易证明这些力学量都是无界算子, 所以由命题3.5可知, 这种扩张是不可能的.

## § 4 对偶空间,二次对偶,自反空间

## 1. 对偶空间设 $X, Y$ 为 Banach 空间, 前面已讲过有界线性算子集合 $L(X, Y)$ 是 Banach 空间. 特别取 $Y = \mathbf{C}$ , 称 $L(X, \mathbf{C})$ 为 $X$ 的对偶空间 (或共轭空间), 记为 $X'$ . 显然, $X$ 的对偶空间 $X'$ 就是 $X$ 上全体连续线性泛函的空间.

$X$ 上的连续线性泛函实在是经典定积分概念的重要推广.例如

$$
f (x) = \int_ {a} ^ {b} x (t) \mathrm{d} t, \quad \text {当} x = x (t) \in C [ a, b ],
$$

就是 $C[a,b]$ 上的连续线性泛函.

在 $X = R^{n}$ 中，设 $\lambda_{j}(x)$ 为 $x = (x_{1}, \cdots, x_{n})$ 的第 j 个坐标，即

$$
\lambda_ {j} \left(\left(x _ {1}, \dots , x _ {n}\right)\right) = x _ {j}, j = 1, \dots , n.
$$

显然每个 $\lambda_{j}(x)$ 都是 $\mathbf{R}^{n}$ 上连续线性泛函. 而在无穷维空间, 特别有意思的是不可分情况, 连续线性泛函正类似于点的坐标. 即有对应

$$
x \mapsto \{f (x) \} _ {f \in X ^ {\prime}}.
$$

按坐标的想法, 自然要求 X 中不同的点 $x_{1}$ 与 $x_{2}$ 对应于不同的坐标, 亦即有 $f_{0} \in X'$ 使得

$$
f _ {0} (x _ {1}) \neq f _ {0} (x _ {2}).
$$

事实正是如此,这只须取 $x_0 = x_1 - x_2$ . 由命题2.1确有 $f_0 \in X'$ , 使得

$$
f _ {0} \left(x _ {0}\right) = \| x _ {0} \| \neq 0.
$$

这或者是命题2.1常被称为Hahn-Banach定理之重要推论的一个原因.历史上，Hahn也正是在证明了命题2.1之后才引进对偶空间概念.他当时称之为“polare Raum”(参见[26],第137页).

在泛函分析以后的发展和应用中,人们常把 Banach 空间与其对偶空间联系起来考虑,这就是所谓“对偶理论”的精神,对偶理论不只在泛函分析理论本身,而且在数学物理和近代偏微分方程理论上都起到重要的作用.

定理 4.1 对 Banach 空间 X, 如果 $X'$ 可分, 则 X 亦可分.

证由于 $X'$ 可分, 易知存在球面 $\{x' \in X': \| x' \| = 1\}$ 上可数稠密子集 $\{x_n'\}_{n=1}^{\infty}$ . 根据 $\| x'\|$ 的定义, 应有一串点 $\{x_n\}_{n=1}^{\infty} \subset X, \| x_n \| \leqslant 1$ , 使

$$
\left| x _ {n} ^ {\prime} \left(x _ {n}\right) \right| > \frac {1}{2}, \quad n = 1, 2, \dots .
$$

假设 X 不可分， $\left\{x_{n}\right\}_{n=1}^{\infty}$ 张开的子空间不是 X. 根据命题 2.2，应有 $x_{0}^{\prime} \in X^{\prime}$ ，使 $x_{0}^{\prime}(x_{n}) = 0, n = 1, 2, \cdots,$ 且 $\|x_{0}^{\prime}\| = 1$ .

从而

$$
\begin{array}{r l} \parallel x _ {0} ^ {\prime} - x _ {n} ^ {\prime} \parallel & \geqslant \mid x _ {0} ^ {\prime} (x _ {n}) - x _ {n} ^ {\prime} (x _ {n}) \mid \\ & = \mid x _ {n} ^ {\prime} (x _ {n}) \mid > \frac {1}{2}, \quad n = 1, 2, \dots . \end{array}
$$

这与 $\{x_{n}^{\prime}\}_{n = 1}^{\infty}$ 是 $X^{\prime}$ 之单位球面上的稠密子集矛盾.证毕.

## 2. 几个具体空间上的连续线性泛函定理4.2 $(\ell^1)'$ 中的元素 $f$ 可唯一地表为

$$
f (x) = \sum_ {n = 1} ^ {\infty} a _ {n} x _ {n}, \text {当} x = \{x _ {n} \} _ {n = 1} ^ {\infty} \in l ^ {1},\tag{4.1}
$$

其中 $a = \{a_n\}_{n=1}^{\infty} \in (m)$ (见第一章 §3 中例 1), 而且

$$
\| f \| = \sup _ {n} | a _ {n} | = \| a \|,
$$

这里 $\| a\|$ 表示 $a$ 作为 $(m)$ 中元的范数.

另一方面，对每个 $a = \{a_{n}\}_{n=1}^{\infty} \in (m)$ ，由(4.1)式右端定义的线性泛函 $f$ 在 $(t^{1})'$ 中.

证设 $f \in (l^1)'$ . 考察 $l^1$ 中点列

$$
e _ {1} = \{1, 0, 0, \dots \}, e _ {2} = \{0, 1, 0, \dots \}, \dots .
$$

则对任意 $x = \{x_{n}\}_{n = 1}^{\infty}\in l^{1}$ 有

$$
x = \sum_ {n = 1} ^ {\infty} x _ {n} e _ {n},
$$

这个级数在 $l^{1}$ 中收敛.于是

$$
f (x) = \sum_ {n = 1} ^ {\infty} x _ {n} f (e _ {n}).
$$

注意， $\| e_n\| = 1$ ，于是 $|f(e_n)|\leqslant \| f\|$ .设

$$
a _ {n} = f (e _ {n}), n = 1, 2, \dots ,
$$

则 $a = \{a_{n}\}_{n = 1}^{\infty}\in (m)$ ，且 $a$ 由 $f$ 唯一地确定.又

$$
f (x) = \sum_ {n = 1} ^ {\infty} a _ {n} x _ {n}.
$$

从 $a_{n} = f(e_{n}), |f(e_{n})| \leqslant \| f \|, n = 1,2,\dots,$

$$
\| a \| = \sup _ {n} | a _ {n} | \leqslant \| f \|.
$$

此外，

$$
\mid f (x) \mid \leqslant \sum_ {n = 1} ^ {\infty} \mid a _ {n} \mid \mid x _ {n} \mid \leqslant \sup _ {n} \mid a _ {n} \mid \sum_ {n = 1} ^ {\infty} \mid x _ {n} \mid = \parallel a \parallel \parallel x \parallel .
$$

可见， $\| f\| \leqslant \| a\|$ .总之

$$
\| f \| = \| a \|
$$

至于定理其他部分是容易验证的. 证毕.

以下考察 $C[0,1]$ 上的连续线性泛函.

定理4.3 设 $f \in (C[0,1])'$ ，则存在 $[0,1]$ 上的有界变差函数 $g(t)$ ，使

(4.2)

$f(x) = \int_{0}^{1} x(t) \mathrm{d}g(t)$ , 当 $x = x(t) \in C[0,1]$ ,

且

$$
\| f \| = \operatorname{var} (g),
$$

这里 $\operatorname{var}(g)$ 表示 $g(t)$ 在 $[0,1]$ 上的全变差. (参见[7], 第五章 §4 或 [8], 第四章 §6)

另一方面，对[0,1]上每个有界变差函数 $g(t)$ ，由(4.2)式右端定义的线性泛函 $f$ 在 $(C[0,1])'$ 中.

证设 $g(t)$ 是 $[0,1]$ 上的有界变差函数. 对任意 $x = x(t) \in C[0,1]$ , Lebesgue-Stieltjes 积分 $\int_{0}^{1} x(t) \mathrm{d}g(t)$ 存在. 对每个正整数 $n$ , 取阶层函数

$$
z _ {n} (t) = \sum_ {k = 1} ^ {n} x \left(\frac {k}{n}\right) \left[ u _ {\frac {k}{n}} (t) - u _ {\frac {k - 1}{n}} (t) \right],
$$

这里 $u_0(t)\equiv 0$ ，对 $\xi \in (0,1]$

$$
u _ {\xi} (t) = \left\{ \begin{array}{l l} 1, \text {当} 0 \leqslant t \leqslant \xi ; \\ 0, \text {当} \xi <   t \leqslant 1. \end{array} \right.
$$

因为 $x(t)$ 在 $[0,1]$ 上一致连续，故 $z_{n}(t)$ 在 $[0,1]$ 上一致收敛于 $x(t)$ . 而

$$
\begin{array}{r l} \int_ {0} ^ {1} z _ {n} (t) \mathrm{d} g (t) & = \sum_ {k = 1} ^ {n} \int_ {\frac {k - 1}{n}} ^ {\frac {k}{n}} z _ {n} (t) \mathrm{d} g (t) \\ & = \sum_ {k = 1} ^ {n} x \left(\frac {k}{n}\right) \int_ {\frac {k - 1}{n}} ^ {\frac {k}{n}} 1 \mathrm{d} g (t) \\ & = \sum_ {k = 1} ^ {n} x \left(\frac {k}{n}\right) \left[ g \left(\frac {k}{n}\right) - g \left(\frac {k - 1}{n}\right) \right]. \end{array}
$$

注意 $|z_{n}(t)| \leqslant \| x\|, 0 \leqslant t \leqslant 1, n = 1, 2, \cdots$ . 故

$$
\int_ {0} ^ {1} x (t) \mathrm{d} g (t) = \lim _ {n \rightarrow \infty} \int_ {0} ^ {1} z _ {n} (t) \mathrm{d} g (t) = \lim _ {n \rightarrow \infty} \sum_ {k = 1} ^ {n} x \left(\frac {k}{n}\right)\left[ g \left(\frac {k}{n}\right) - g \left(\frac {k - 1}{n}\right)\right]
$$

(参见[6], 第五章, §9). 从而

$$
\begin{array}{r l} \left| \int_ {0} ^ {1} x (t) \mathrm{d} g (t) \right| & \leqslant \sup _ {n} \sum_ {k = 1} ^ {n} \left| x \left(\frac {k}{n}\right) \right| \left| g \left(\frac {k}{n}\right) - g \left(\frac {k - 1}{n}\right) \right| \\ & \leqslant \| x \| \sup _ {n} \sum_ {k = 1} ^ {n} \left| g \left(\frac {k}{n}\right) - g \left(\frac {k - 1}{n}\right) \right| \\ & \leqslant \| x \| \operatorname{var} (g). \end{array}
$$

现在，对[0,1]上的有界变差函数 $g(t)$ ，易见

$$
f (x) = \int_ {0} ^ {1} x (t) \mathrm{d} g (t), x = x (t) \in C [ 0, 1 ],
$$

是 C[0,1]上的线性泛函,而且由前段

$$
\mid f (x) \mid = \left| \int_ {0} ^ {1} x (t) \mathrm{d} g (t) \right| \leqslant \| x \| \operatorname{var} (g).
$$

故 $f \in (C[0,1])'$ , 且 $\| f \| \leqslant \mathrm{var}(g)$ .

以下设 $f \in (C[0,1])'$ . 因为 $C[0,1]$ 可视为 $M[0,1]$ 的子空间（参见第一章习题17）. 由 Hahn-Banach 定理， $f$ 可以扩张成 $M[0,1]$ 上的连续线性泛函 $F$ 而且 $\| F \| = \| f \|$ .

对于每个 $x = x(t) \in C[0,1]$ , 易见前述的 $u_{\xi}(t), z_n(t) \in M[0,1]$ , 且 $z_n \to x$ 在 $M[0,1]$ 中. 于是

$$
F (x) = \lim _ {n \rightarrow \infty} F (z _ {n}) = \lim _ {n \rightarrow \infty} \left\{\sum_ {k = 1} ^ {n} x \left(\frac {k}{n}\right)\left[ F \left(u _ {\frac {k}{n}}\right) - F \left(u _ {\frac {k - 1}{n}}\right)\right]\right\}.\tag{4.3}
$$

$$
g (\xi) = F (u _ {\xi}), \quad \xi \in [ 0, 1 ].
$$

对于 $[0,1]$ 的任何分划

$$
0 = \xi_ {0} <   \xi_ {1} <   \dots <   \xi_ {n - 1} <   \xi_ {n} = 1,
$$

我们有

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} \left| g (\xi_ {j}) - g (\xi_ {j - 1}) \right| \\ = \sum_ {j = 1} ^ {n} \varepsilon_ {j} \left[ g (\xi_ {j}) - g (\xi_ {j - 1}) \right] \\ = \sum_ {j = 1} ^ {n} \varepsilon_ {j} \left[ F (u _ {\xi_ {j}}) - F (u _ {\xi_ {j - 1}}) \right] \\ = F \left(\sum_ {j = 1} ^ {n} \varepsilon_ {j} (u _ {\xi_ {j}} - u _ {\xi_ {j - 1}})\right), \end{array}
$$

这里 $\varepsilon_{j}, j=1,\cdots,n$ ，是模为 1 的常数。注意

$$
\left\| \sum_ {j = 1} ^ {n} \varepsilon_ {j} \left[ u _ {\xi_ {j}} - u _ {\xi_ {j - 1}} \right] \right\| = 1,
$$

从而

$$
\sum_ {j = 1} ^ {n} \left| g \left(\xi_ {j}\right) - g \left(\xi_ {j - 1}\right) \right| = \left| F \left(\sum_ {j = 1} ^ {n} \varepsilon_ {j} \left[ u _ {\xi_ {j}} - u _ {\xi_ {j - 1}} \right]\right) \right| \leqslant \| F \| = \| f \|.
$$

这说明 $g(\xi)$ 是 $[0,1]$ 上有界变差函数，而且

$$
\operatorname{var} (g) \leqslant \| f \|.
$$

从(4.3)式，

$$
\begin{array}{r l} & {f (x) = F (x) = \lim _ {n \to \infty}    \sum_ {k = 1} ^ {n}   x \left(\frac {k}{n}\right) \Big [ g \left(\frac {k}{n}\right) - g \left(\frac {k - 1}{n}\right) \Big ]} \\ & {\qquad = \int_ {0} ^ {1} x (t) \mathrm{d} g (t), \quad \text {当} x = x (t) \in C [ 0, 1 ],} \end{array}
$$

由第一部分证明， $\| f\| \leqslant \mathrm{var}(g)$ ，总之

$$
\| f \| = \operatorname{var} (g).
$$

证毕.

上述定理中的 $g(t)$ 不是唯一的，但如规定 $g(t) \in V_0[0,1]$ ，则 $g(t)$ 由 $f$ 唯一确定。于是有命题4.1 $(C[0,1])'$ 与 $V_{0}[0,1]$ 保范线性同构.即

$$
(C [ 0, 1 ]) ^ {\prime} \cong V _ {0} [ 0, 1 ].
$$

证明参见[43],第3章§5.这里

$V_{0}[0,1] = \{g:g(t)\text{是}[0,1]\text{上有界变差函数},g(0) = 0,$

且 $g(t)$ 于 $(0,1)$ 内是右连续的.

定理 4.3 是 F. Riesz 在 1909 年证明的, 它或者是最早从连续线性泛函导出测度的一个结果. 其后, 在 1937 年, Banach 将它推广到 $C(\Omega)$ 上, 其中 $\Omega$ 是距离空间中的紧集. 再以后, Kakutani 和 A. Markov 更将 $\Omega$ 换成一般紧的甚至局部紧的 Hausdorff 空间. 这类结果的意义在于分析中一些测度可以由线性泛函导出来, 例如自伴算子的谱测度和遍历定理中的不变测度等. (参见 [27], 第 55 页, 第 224 页)

定理4.4 设 $f$ 是 $L^p [a,b](1 < p < \infty)$ 上的有界线性泛函，则存在唯一的函数 $y\in L^{q}[a,b],q = p(p - 1)^{-1}$ ，使

$$
f (x) = \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t, \quad \text {当} x = x (t) \in L ^ {p} [ a, b ].\tag{4.4}
$$

且

$$
\| f \| = \| y \| \stackrel {d} {=} \left(\int_ {a} ^ {b} | y (t) | ^ {q} d t\right) ^ {1 / q}.
$$

反之，对任何 $y \in L^q[a, b]$ ，(4.4)式右端定义了 $L^p[a, b]$ 上的有界线性泛函。

证对 $s \in [a, b]$ , 令

$$
x _ {s} (t) = \left\{ \begin{array}{l l} 1, \text {当} a \leqslant t \leqslant s; \\ 0, \text {当} s <   t \leqslant b. \end{array} \right.
$$

则 $x_{s} \in L^{b}[a, b]$ . 记 $g(s) = f(x_{s})$ ，则 $g(s)$ 是 $[a, b]$ 上绝对连续函数. 事实上，设 $\delta_{j} = [s_{j}, t_{j}], j = 1, \cdots, n$ ，是任意一组包含于 $[a, b]$ 中且没有公共内点的闭区间. 记 $\varepsilon_{j} = \operatorname{sgn}[g(t_{j}) - g(s_{j})]$ ，则

$$
\begin{array}{r l} \sum_ {j = 1} ^ {n} | g (t _ {j}) - g (s _ {j}) | & = \sum_ {j = 1} ^ {n} \varepsilon_ {j} [ g (t _ {j}) - g (s _ {j}) ] \\ & = \sum_ {j = 1} ^ {n} \varepsilon_ {j} [ f (x _ {t _ {j}}) - f (x _ {s _ {j}}) ] \\ & = f \left(\sum_ {j = 1} ^ {n} \varepsilon_ {j} [ x _ {t _ {j}} - x _ {s _ {j}} ]\right) \\ & \leqslant \| f \| \left\| \sum_ {j = 1} ^ {n} \varepsilon_ {j} [ x _ {t _ {j}} - x _ {s _ {j}} ] \right\| \\ & = \| f \| \left(\int_ {a} ^ {b} \left| \sum_ {j = 1} ^ {n} \varepsilon_ {j} [ x _ {t _ {j}} (\xi) - x _ {s _ {j}} (\xi) ] \right| ^ {p} d \xi\right) ^ {1 / p} \\ & = \| f \| \left(\sum_ {j = 1} ^ {n} \int_ {\delta_ {j}} 1 d \xi\right) ^ {1 / p} \\ & = \| f \| \left(\sum_ {j = 1} ^ {n} m (\delta_ {j})\right) ^ {1 / p}, \end{array}
$$

可见 $g(s)$ 是绝对连续的.

令 $y(s) = g'(s), s \in (a, b)$ ，则 $y \in L^1[a, b]$ . 因为 $x_a(t) = 0, a.e.$ 于 $[a, b]$ ，故 $g(a) = f(x_a) = 0$ . 于是

$$
g (s) = g (a) + \int_ {a} ^ {s} y (t) \mathrm{d} t = \int_ {a} ^ {s} y (t) \mathrm{d} t.
$$

从而

$$
f (x _ {s}) = g (s) = \int_ {a} ^ {s} y (t) \mathrm{d} t = \int_ {a} ^ {b} x _ {s} (t) y (t) \mathrm{d} t.\tag{4.5}
$$

设 $x(t)$ 是 $[a, b]$ 上任一有界可测函数. 我们可取一致有界的阶层函数列 $\{x_{n}(t)\}_{n-1}^{\infty}$ 几乎处处收敛于 $x(t)$ . 根据(4.5)以及 $x_{n}(t)$ 是某些 $x_{s}(t)$ 的线性组合可知

$$
f (x _ {n}) = \int_ {a} ^ {b} x _ {n} (t) y (t) \mathrm{d} t,\tag{4.6}
$$

根据Lebesgue收敛定理有

$$
\int_ {a} ^ {b} x _ {n} (t) y (t) \mathrm{d} t \rightarrow \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t,
$$

$$
\left\| x _ {n} - x \right\| = \left(\int_ {a} ^ {b} | x _ {n} (t) - x (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p} \rightarrow 0.
$$

于是，在(4.6)式中令 $n \to \infty$ ，可得

$$
f (x) = \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t.\tag{4.7}
$$

往证 $y \in L^{q}[a, b]$ . 对每个正整数 $N$ 作如下有界可测函数

$$
y _ {N} (t) = \left\{ \begin{array}{l l} | y (t) | ^ {q - 1} \mathrm{sgn} y (t), & \text {当} | y (t) | \leqslant N; \\ 0, & \text {当} | y (t) | > N. \end{array} \right.
$$

记 $E_{N} = \{t\in [a,b]:|y(t)|\leqslant N\}$ ，则

$$
f (y _ {N}) = \int_ {a} ^ {b} y _ {N} (t) y (t) \mathrm{d} t = \int_ {E _ {N}} y _ {N} (t) y (t) \mathrm{d} t = \int_ {E _ {N}} | y (t) | ^ {q} \mathrm{d} t.
$$

另一方面，从 $q = p(p - 1)^{-1}$ ，知

$$
\mid y _ {N} (t) \mid^ {p} = \mid y (t) \mid^ {(q - 1) p} = \mid y (t) \mid^ {q}, \text {当} t \in E _ {N}.
$$

从而

$$
f \left(y _ {N}\right) \leqslant \| f \| \| y _ {N} \| = \| f \| \left(\int_ {E _ {N}} | y _ {N} (t) | ^ {p} d t\right) ^ {1 / p} = \| f \| \left(\int_ {E _ {N}} | y (t) | ^ {q} d t\right) ^ {1 / p}.
$$

于是

$$
\int_ {F _ {\mathrm{N}}} | y (t) | ^ {q} \mathrm{d} t \leqslant \| f \| \left(\int_ {F _ {\mathrm{N}}} | y (t) | ^ {q} \mathrm{d} t\right) ^ {1 / p}
$$

从 $1 - \frac{1}{p} = \frac{1}{q}$ ，可得

$$
\left(\int_ {F _ {N}} | y (t) | ^ {q} \mathrm{d} t\right) ^ {1 / q} \leqslant \| f \|,
$$

令 $N\to \infty ,E_N\to [a,b]$ ，可得

$$
\left(\int_ {a} ^ {b} | y (t) | ^ {q} \mathrm{d} t\right) ^ {1 / q} \leqslant \| f \|.
$$

这说明 $y \in L^{q}[a, b]$ , 且 $\| y \| \leqslant \| f \|$ .

现在证明, 对任何 $x \in L^{p}[a, b]$ , (4.7) 式成立. 取有界可测函数列 $\{x_{n}(t)\}_{n=1}^{\infty}$ , 使

$$
\parallel x _ {n} - x \parallel = \left(\int_ {a} ^ {b} \mid x _ {n} (t) - x (t) \mid^ {p} \mathrm{d} t\right) ^ {1 / p} \rightarrow 0, \text {当} n \rightarrow \infty .
$$

从(4.7)式有

$$
f (x _ {n}) = \int_ {a} ^ {b} x _ {n} (t) y (t) \mathrm{d} t, n = 1, 2, \dots .\tag{4.8}
$$

根据 Hölder 不等式

$$
\begin{array}{r l}&{\left| \int_ {a} ^ {b} x _ {n} (t) y (t) \mathrm{d} t - \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t \right|}\\&{= \left| \int_ {a} ^ {b} [ x _ {n} (t) - x (t) ] y (t) \mathrm{d} t \right|.}\\&{\leqslant \left(\int_ {a} ^ {b} | x _ {n} (t) - x (t) | ^ {p} \mathrm{d} t\right) ^ {1 / p} \left(\int_ {a} ^ {b} | y (t) | ^ {q} \mathrm{d} t\right) ^ {1 / q}}\\&{= \| x _ {n} - x \| \| y \| \rightarrow 0, \text {当} n \rightarrow \infty .}\end{array}
$$

在(4.8)式中，令 $n\to \infty$ ，可得

$$
f (x) = \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t.
$$

即(4.4)式成立.从(4.4)式利用 Hölder 不等式可得

$$
\mid f (x) \mid = \left| \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t \right| \leqslant \| x \| \| y \|, \quad \forall x \in L ^ {p} [ a, b ].
$$

因此， $\| f \| \leqslant \| y \|$ 。前已证明 $\| y \| \leqslant \| f \|$ ，于是 $\| f \| = \| y \|$ 。

假如又有 $y_{1} \in L^{q}[a, b]$ , 使

$$
f (x) = \int_ {a} ^ {b} x (t) y _ {1} (t) \mathrm{d} t, \text {当} x \in L ^ {p} [ a, b ].
$$

令 $x_{1}(t) = \mathrm{sgn}[y(t) - y_{1}(t)], t \in [a, b]$ ，则 $x_{1} \in L^{p}[a, b]$ . 从而

$$
\int_ {a} ^ {b} | y (t) - y _ {1} (t) | \mathrm{d} t = \int_ {a} ^ {b} x _ {1} (t) [ y (t) - y _ {1} (t) ] \mathrm{d} t = 0.
$$

故 $y(t) = y_1(t)$ , a.e. 于 $[a, b]$ , 即 $y = y_1$ . 唯一性得证.

反之，设 $y \in L^{q}[a, b]$ ，利用 Hölder 不等式易知，(4.4) 右端定义了 $L^{p}[a, b]$ 上的一个有界线性泛函。证毕。

定理4.5 $l^p (1 < p < \infty)$ 上的有界线性泛函 $f$ 可以表为

$$
f (x) = \sum_ {k = 1} ^ {\infty} c _ {k} \xi_ {k}, \text {当} x = \{\xi_ {k} \} _ {k = 1} ^ {\infty} \in t ^ {p},\tag{4.9}
$$

这里 $c = \{c_k\}_{k=1}^{\infty} \in t^q, q = p(p - 1)^{-1}$ , 由 $f$ 唯一确定, 且

$$
\| f \| = \| c \| \stackrel {{d}} {=} \left(\sum_ {k = 1} ^ {\infty} | c _ {k} | ^ {q}\right) ^ {1 / q}.
$$

反之，任给 $c = \{c_k\}_{k=1}^{\infty} \in l^q$ ，由(4.9)式右端定义了 $l^p$ 上一个有界线性泛函。

证考察 $\ell^p$ 中的点列

$$
e _ {1} = \{1, 0, 0, \dots \}, e _ {2} = \{0, 1, 0, \dots \}, \dots .
$$

则每个元 $x = \{\xi_k\}_{k=1}^{\infty}\in l^p$ 可以唯一地表成

$$
x = \sum_ {k = 1} ^ {\infty} \xi_ {k} e _ {k},
$$

这个级数在 $l^p$ 中收敛.

设 $f \in (l^p)'$ ，则

$$
f (x) = \sum_ {k = 1} ^ {\infty} \xi_ {k} f (e _ {k}).
$$

令 $c_{k}=f(e_{k}), k=1,2,\cdots,$ 则

$$
f (x) = \sum_ {k = 1} ^ {\infty} c _ {k} \xi_ {k}, x = \{\xi_ {k} \} _ {k = 1} ^ {\infty} \in l ^ {p}.\tag{4.10}
$$

往证, $c=\left\{c_{k}\right\}_{k=1}^{\infty}\in\ell^{q}$ . 选取 $x_{n}=\left\{\xi_{k}^{(n)}\right\}_{k=1}^{\infty}\in\ell^{p},n=1,2,\cdots$ ,其中

$$
\xi_ {k} ^ {(n)} = \left\{ \begin{array}{l l} | c _ {k} | ^ {q - 1} \mathrm{sgn} c _ {k}, & \text {当} k \leqslant n; \\ 0, & \text {当} k > n. \end{array} \right.
$$

则由(4.10)可知

$$
f (x _ {n}) = \sum_ {k = 1} ^ {n} | c _ {k} | ^ {q}.
$$

另一方面

$$
\begin{array}{r l} f (\dot {x} _ {n}) & \leqslant \| f \| \| x _ {n} \| = \| f \| \left(\sum_ {k = 1} ^ {\infty} | \xi_ {k} ^ {(n)} | ^ {p}\right) ^ {1 / p} \\ & = \| f \| \left(\sum_ {k = 1} ^ {n} | c _ {k} | ^ {q}\right) ^ {1 / p}, \end{array}
$$

由这两个式子可得

$$
\left(\sum_ {k = 1} ^ {n} \mid c _ {k} \mid^ {q}\right) ^ {1 / q} \leqslant \| f \|.
$$

令 $n\to \infty$ ，便有

$$
\left(\sum_ {k = 1} ^ {\infty} | c _ {k} | ^ {q}\right) ^ {1 / q} \leqslant \| f \|.
$$

这表明 $c = \{c_k\}_{k=1}^{\infty} \in t^q$ ，且 $\|c\| \leqslant \|f\|$ 。现在从(4.10)及 Hölder 不等式可得

$$
\begin{array}{r l} | f (x) | & = \left| \sum_ {k = 1} ^ {\infty} c _ {k} \xi_ {k} \right| \\ & \leqslant \left(\sum_ {k = 1} ^ {\infty} | c _ {k} | ^ {q}\right) ^ {1 / q} \left(\sum_ {k = 1} ^ {\infty} | \xi_ {k} | ^ {p}\right) ^ {1 / p} \\ & = \| c \| \| x \|. \end{array}
$$

从而， $\| f\| \leqslant \| c\|$ ，总之

$$
\| f \| = \| c \|
$$

假若又有 $c^{\prime} = \{c_{k}^{\prime}\}_{k = 1}^{\infty}\in l^{q}$ ，使

$$
f (x) = \sum_ {k = 1} ^ {\infty} c _ {k} ^ {'} \xi_ {k}, \text {当} x = \{\xi_ {k} \} _ {k = 1} ^ {\infty} \in l ^ {p}.
$$

则对任何 $x = \{\xi_k\}_{k=1}^{\infty}\in l^p$ ，总有

$$
\sum_ {k = 1} ^ {\infty} \left(c _ {k} - c _ {k} ^ {\prime}\right) \xi_ {k} = 0.
$$

依次取 $x = e_{n}, n = 1,2,\dots$ ，即得 $c_{n} - c_{n}^{\prime} = 0, n = 1,2,\dots$ . 故 $c = c^{\prime}$ . 唯一性得证.

反之，若 $c = \{c_k\}_{k=1}^{\infty} \in t^q$ ，利用 Hölder 不等式易见(4.9)式右端定义了 $t^p$ 上的一个有界线性泛函。证毕。

## 3. 二次对偶与典型映射设 $X$ 是Banach空间, $X'$ 是其对偶空间. $X'$ 的对偶空间 $X''$ 称为 $X$ 的二次对偶. 我们将要看到 $X$ 与 $X''$ 之间有密切的联系.

对 Banach 空间 X 中任意一点 $x_{0} \neq 0$ ，定义

$$
F (x ^ {\prime}) = x ^ {\prime} (x _ {0}), \forall x ^ {\prime} \in X ^ {\prime}.
$$

显然 $F$ 是 $X'$ 上的线性泛函，而且

$$
\| F \| = \sup _ {\| x ^ {\prime} \| \leqslant 1} | F (x ^ {\prime}) | = \sup _ {\| x ^ {\prime} \| \leqslant 1} | x ^ {\prime} (x _ {0}) | \leqslant \| x _ {0} \|.
$$

另一方面，由命题2.1，有 $x_0' \in X'$ ，使

$$
\mid x _ {0} ^ {\prime} (x _ {0}) \mid = \parallel x _ {0} \parallel , \text {且} \parallel x _ {0} ^ {\prime} \parallel = 1.
$$

于是

$$
\| F \| = \sup _ {\| x ^ {\prime} \| \leqslant 1} | x ^ {\prime} (x _ {0}) | \geqslant | x _ {0} ^ {\prime} (x _ {0}) | = \| x _ {0} \|.
$$

总之，

$$
\| F \| = \| x _ {0} \|
$$

由此可见 $F$ 由 $x_0$ 唯一确定，且 $F \in X''$ . 现在记 $x_0''$ 以代替 $F$ ，即

$$
x _ {0} ^ {\prime \prime} (x ^ {\prime}) = x ^ {\prime} (x _ {0}), \forall x ^ {\prime} \in X ^ {\prime}.
$$

则得到映射 $\tau : X \to X''$ ,

$$
\tau (x _ {0}) = x _ {0} ^ {\prime \prime},
$$

且

$$
\left\| x _ {0} ^ {\prime \prime} \right\| = \left\| x _ {0} \right\|.
$$

这表明映射 $\tau$ 把 $X$ 保范地嵌入到 $X''$ 中，人们称如此的 $\tau$ 为典型映射。我们有时把 $X$ 上的问题通过 $\tau$ 转化为 $X''$ 上的问题，这是泛函分析中一个常用的技巧。好处在于线性函数较之空间中的元更易处理，例如将 $\| x_0\|$ 转化成 $\| x_0''\|$ 来考察等等。

下面来看一个利用二次对偶证明 $X$ 与 $X'$ 之性质的例子.

命题 4.2 设 $\{x_{\alpha}\}_{\alpha\in\mathcal{N}}$ 是 Banach 空间 X 中的点集. 如果对任何 $f\in X'$ ，都有常数 $M_{f}>0$ ，使

$$
\sup _ {a \in \mathcal {A}} | f (x _ {a}) | \leqslant M _ {f},
$$

则

$$
\sup _ {a \in \mathcal {A}} \| x _ {a} \| <   \infty .
$$

这只须考察 $X^{\prime}$ 上的有界线性泛函

$$
F _ {a} (f) = f (x _ {a}), \forall f \in X ^ {\prime},
$$

注意， $\| F_{\alpha}\| = \| x_{\alpha}\|$ .然后由一致有界原理便知道

$$
\sup _ {a \in \mathcal {A}} \| x _ {a} \| = \sup _ {a \in \mathcal {A}} \| F _ {a} \| <   \infty .
$$

## 4. 自反空间对前段所说的典型映射 $\tau: X \to X''$ , 一般来说 $\tau(X) \neq X''$ .

定义 4.1 如果 $\tau(X)=X^{\prime\prime}$ ，则称 X 是自反空间.

Hahn 在 1927 年发现典型映射后便提出自反空间的概念, 当时他把这类空间称为正则的. 下面将证明, 有限维赋范线性空间都是自反的. 空间自反性的要求正是为了保证有限维赋范线性空间上的重要定理在无穷维空间上仍然成立. 例如下面讲到的算子的值域与零空间关系的定理就需要空间的自反性.

注意自反空间 $X$ 是经由一个特定的保范同构 $\tau$ 变 $X$ 为 $X''$ . R.C. James 曾构造出一个 Banach 空间 $X$ , 它和 $X''$ 保范同构, 但是 $X$ 并不自反 (参见 [33]). 这个反例提醒我们在证明空间自反性时要谨慎从事.

定理4.6 任何有限维赋范线性空间都是自反的.

证设 X 是 n 维赋范线性空间, $\{e_{1},\cdots,e_{n}\}$ 是 X 的基. 根据命题 2.2, 存在 $f_{1},\cdots,f_{n}\in X'$ , 使

$$
f _ {j} \left(e _ {k}\right) = \delta_ {j k}, j, k = 1, \dots , n,
$$

这里 $\delta_{jk}$ 是 Kronecker 常数. 易见 $f_{1}, \cdots, f_{n}$ 是线性无关的. 对任意 $x = \sum_{j=1}^{n} x_{j} e_{j} \in X$ ,

$$
f _ {k} (x) = \sum_ {j = 1} ^ {n} x _ {j} f _ {k} (e _ {j}) = x _ {k}, k = 1, \dots , n.
$$

故于任何 $f \in X'$ ,

$$
f (x) = \sum_ {j = 1} ^ {n} x _ {j} f \left(e _ {j}\right) = \sum_ {j = 1} ^ {n} f \left(e _ {j}\right) f _ {j} (x) = \left[ \sum_ {j = 1} ^ {n} f \left(e _ {j}\right) f _ {j} \right] (x).
$$

即

$$
f = \sum_ {j = 1} ^ {n} f (e _ {j}) f _ {j}.
$$

这表明 $\{f_{1},\cdots,f_{n}\}$ 是 $X'$ 的基，即 $X'$ 也是n维空间。从而 $X''$ 亦是n维空间。而典型映射 $\tau$ 是保范线性映射，所以 $\tau(X)$ 的维数与X的维数相同。从 $\tau(X)\subset X''$ ，可知， $\tau(X)=X''$ 。证毕。

定理4.7 $L^p [a,b](1 < p < \infty)$ 是自反的.

证只须证明任给 $F \in (L^p[a, b])''$ ，存在 $x_0 \in L^p[a, b]$ ，使

$$
F (f) = f (x _ {0}), \text {当} f \in (L ^ {p} [ a, b ]) ^ {\prime}.
$$

任给 $y \in L^{q}[a, b], q = p(p - 1)^{-1}$ , 考察映射 $\alpha: L^{q}[a, b] \to (L^{p}[a, b])'$ , $\alpha(y) = f$ . 这里

$$
f (x) = \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t, \text {当} x \in L ^ {p} [ a, b ].
$$

根据定理 4.4, $\alpha: L^{q}[a, b] \rightarrow (L^{p}[a, b])'$ 是保范同构. 设

$$
F ^ {\prime} (y) = F (\alpha (y)), \text {当} y \in L ^ {q} [ a, b ].
$$

易证 $F^{\prime}\in (L^{q}[a,b])^{\prime}$ .又由定理4.4，存在 $x_0\in L^p [a,b]$ ，使

$$
F ^ {\prime} (y) = \int_ {a} ^ {b} y (t) x _ {0} (t) \mathrm{d} t, \text {当} y \in L ^ {q} [ a, b ],
$$

现在对任意的 $f \in (L^p [a,b])'$ ，令 $y = a^{-1}(f)$ ，则 $y \in L^q [a,b]$ ，且

$$
f (x) = \int_ {a} ^ {b} x (t) y (t) \mathrm{d} t, \text {当} x \in L ^ {p} [ a, b ].
$$

于是

$$
F (f) = F (\alpha (y)) = F ^ {\prime} (y) = \int_ {a} ^ {b} y (t) x _ {0} (t) \mathrm{d} t = f (x _ {0}).
$$

证毕.

定理4.8 每个Hilbert空间都是自反的.

证设 $H$ 是 Hilbert 空间, 任给 $y \in H$ , 都确定 $H$ 上一个连续线性泛函 $y^{*}$ :

$$
y ^ {*} (x) = (x, y), \quad \text {当} x \in H.
$$

反之，由 Fréchet-Riesz 表现定理， $H$ 上每个连续线性泛函都具有这种形式.

现在只须证明,对任给的 $\varphi\in H^{**}$ , 存在 $x_{0}\in H$ , 使

$$
\varphi (y ^ {*}) = y ^ {*} \left(x _ {0}\right), \forall y ^ {*} \in H ^ {*}.
$$

由前述只须证明

$$
\varphi (y ^ {*}) = (x _ {0}, y) = \overline {{(y , x _ {0})}}, \forall y \in H.
$$

亦即

$$
\overline {{{{\varphi (y ^ {*})}}}} = (y, x _ {0}), \forall y \in H.
$$

要证明这点,由 Fréchet-Riesz 表现定理,只须证明

$$
\overline {{\varphi (y ^ {*})}} = \overline {{\varphi ((., y))}}
$$

是 $H$ 上关于 $y$ 的连续线性泛函，而这是易于直接验证的.证毕.

例空间 $l^{1}$ 不自反.

根据定理 4.2, $(t^{1})^{\prime}\cong(m)$ , 则 $(m)^{\prime}\cong(t^{1})^{\prime\prime}$ （见习题 20）. 如果 $t^{1}$ 自反，则 $(m)^{\prime}$ 与 $t^{1}$ 保范同构. 但 $t^{1}$ 是可分的, 从而 $(m)^{\prime}$ 也将是可分的了. 根据定理 4.1, (m)亦是可分的. 这与第一章 §4 中例 3 的结果矛盾. 故 $t^{1}$ 非自反.

定理 4.9 如果 Banach 空间 X 是自反的, 则 X 的任何子空间 M 也是自反的.

证只须证明任给 $m_0'' \in M''$ ，存在 $x_0 \in M$ ，使

$$
m _ {0} ^ {\prime \prime} (m ^ {\prime}) = m ^ {\prime} (x _ {0}), \text {当} m ^ {\prime} \in M ^ {\prime}.
$$

对每个 $x^{\prime}\in X^{\prime}$ ，我们用 $x_{M}^{\prime}$ 表示 $x^{\prime}$ 在 $M$ 上的限制，即

$$
x _ {M} ^ {\prime} (x) = x ^ {\prime} (x), \text {当} x \in M,
$$

则 $x_{M}^{\prime}\in M^{\prime}$

对 $m_0^{\prime \prime}\in M^{\prime \prime}$ ，定义

$$
x _ {0} ^ {\prime \prime} (x ^ {\prime}) = m _ {0} ^ {\prime \prime} (x _ {M} ^ {\prime}), \text {当} x ^ {\prime} \in X ^ {\prime}.
$$

易见 $x_0^{\prime \prime}$ 是 $X^{\prime}$ 上的线性泛函. 又

$$
\mid x _ {0} ^ {\prime \prime} (x ^ {\prime}) \mid = \mid m _ {0} ^ {\prime \prime} (x _ {M} ^ {\prime}) \mid \leqslant \parallel m _ {0} ^ {\prime \prime} \parallel \parallel x _ {M} ^ {\prime} \parallel \leqslant \parallel m _ {0} ^ {\prime \prime} \parallel \parallel x ^ {\prime} \parallel , \text {当} x ^ {\prime} \in X ^ {\prime}.
$$

故 $x_0'' \in X''$ . 由假设 $X$ 是自反的, 故存在 $x_0 \in X$ . 使

$$
x _ {0} ^ {\prime \prime} (x ^ {\prime}) = x ^ {\prime} (x _ {0}), \text {当} x ^ {\prime} \in X ^ {\prime}.
$$

特别, 如果 $x^{\prime} \in X^{\prime}$ , 使 $x^{\prime}(x) = 0, \forall x \in M$ , 则 $x_{M}^{\prime} = 0$ . 从而我们有

$$
x ^ {\prime} (x _ {0}) = x _ {0} ^ {\prime \prime} (x ^ {\prime}) = m _ {0} ^ {\prime \prime} (x _ {M} ^ {\prime}) = 0.
$$

根据命题 2.3, $x_{0}\in M$ . 现在对每个 $m^{\prime}\in M^{\prime}$ ，设 $x^{\prime}\in X^{\prime}$ 是 $m^{\prime}$ 的扩张，使 $x_{M}^{\prime}=m^{\prime}$ ，则

$$
\begin{array}{r l} m _ {0} ^ {\prime \prime} (m ^ {\prime}) & = m _ {0} ^ {\prime \prime} (x _ {M} ^ {\prime}) = x _ {0} ^ {\prime \prime} (x ^ {\prime}) \\ & = x ^ {\prime} (x _ {0}) = m ^ {\prime} (x _ {0}). \end{array}
$$

证毕.

自反空间是类乎 Hilbert 空间的 Banach 空间, 它具有丰富的几何性质. 因此自反空间上算子的结构也是比较整齐的, 这在下面讲算子的值域与零空间的关系时, 便可清楚地看到. 此外, 在应用方面自反空间也是重要的.

## § 5 Banach 共轭算子首先,从有限维空间上的线性算子或矩阵说起,对

$$
A x = \left( \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right) \left( \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right) = \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {n} \end{array} \right),
$$

我们有

$N(A)=\{x=(x_{1},\cdots,x_{n}):Ax=0\}=(A \text{ 的行向量空间 })^{\perp}.$

又

$$
\left( \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right) = \left( \begin{array}{c} \sum_ {j = 1} ^ {n} a _ {1 j} x _ {j} \\ \vdots \\ \sum_ {j = 1} ^ {n} a _ {n j} x _ {j} \end{array} \right) = \sum_ {j = 1} ^ {n} x _ {j} \left( \begin{array}{c} a _ {1 j} \\ \vdots \\ a _ {n j} \end{array} \right),
$$

故

$$
R (A) = \{y: y = A x \} = A \text {   的列向量空间.   }
$$

所以

$$
A x = y _ {0} \text {有解} \Leftrightarrow y _ {0} \perp N (A ^ {\prime}),\tag{5.1}
$$

这里 $A^{\prime}$ 是 $A$ 的转置矩阵.

理由是简单的：

$$
A x = y _ {0} \text {有解}
$$

$$
\begin{array}{r l} {\Leftrightarrow y _ {0} \in R (A) = A   \text {的列向量空间}} \\ & {\qquad = A ^ {\prime} \text {的行向量空间}} \\ & {\qquad = N (A ^ {\prime}) ^ {\perp}.} \end{array}
$$

定义 5.1 设 X 与 Y 都是 Banach 空间, $T \in L(X, Y)$ . 定义映射 $T'$ :

$$
(T ^ {\prime} y ^ {\prime}) (x) = y ^ {\prime} (T x), y ^ {\prime} \in Y ^ {\prime}, x \in X.
$$

显然 $T'$ 是从 $Y'$ 到 $X'$ 的有界线性算子. 人们称 $T'$ 为 $T$ 的 Banach 共轭算子.

设 $\{e_{1},\cdots,e_{n}\}$ 是 n 维空间 X 上的一个基，A 是 X 上线性算子，在这个基之下的矩阵表示为 $A=(a_{jk})_{n\times n}$ ，即

$$
\left(\mathbf {A} e _ {1}, \mathbf {A} e _ {2}, \dots , \mathbf {A} e _ {n}\right) = \left(e _ {1}, e _ {2}, \dots , e _ {n}\right) \left( \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right).
$$

由定理 4.6 的证明, 存在 X 上的有界线性泛函 $\{f_{1}, \cdots, f_{n}\}$ 使

$$
f _ {j} \left(e _ {k}\right) = \delta_ {j k}, j, k = 1, \dots , n,
$$

且 $\{f_{1},\cdots,f_{n}\}$ 是 $X'$ 的一个基.不难验证,对于Banach共轭算子 $A'$ 有

$$
\left(\mathbf {A} ^ {\prime} f _ {1}, \mathbf {A} ^ {\prime} f _ {2}, \dots , \mathbf {A} ^ {\prime} f _ {n}\right) = \left(f _ {1}, f _ {2}, \dots , f _ {n}\right) \left( \begin{array}{c c c c} a _ {1 1} & a _ {2 1} & \dots & a _ {n 1} \\ a _ {1 2} & a _ {2 2} & \dots & a _ {n 2} \\ \vdots & \vdots & & \vdots \\ a _ {1 n} & a _ {2 n} & \dots & a _ {n n} \end{array} \right).\tag{5.2}
$$

因为从定义与直接计算,对 $x=\sum_{j=1}^{n}x_{j}e_{j}\in X$ ,

$$
\mathbf {A} x = \sum_ {j = 1} ^ {n} x _ {j} \mathbf {A} e _ {j} = \sum_ {j = 1} ^ {n} x _ {j} \left(\sum_ {k = 1} ^ {n} a _ {k j} e _ {k}\right),
$$

其中， $a_{kj}=(\mathbf{A}e_{j},e_{k}),k,j=1,\cdots,n$ ．从而

$$
\begin{array}{r l} \left(\mathbf {A} ^ {\prime} f _ {i}\right) (x) & = f _ {i} (\mathbf {A} x) = \sum_ {j = 1} ^ {n} x _ {j} \left[ \sum_ {k = 1} ^ {n} a _ {k j} f _ {i} (e _ {k}) \right] \\ & = \sum_ {j = 1} ^ {n} x _ {j} \left[ \sum_ {k = 1} ^ {n} a _ {k j} \delta_ {i k} \right] = \sum_ {j = 1} ^ {n} a _ {i j} x _ {j}. \end{array}
$$

另一方面

$$
\begin{array}{r l} f _ {i} (x) & = \sum_ {j = 1} ^ {n} x _ {j} f _ {i} (e _ {j}) \\ & = \sum_ {j = 1} ^ {n} x _ {j} \delta_ {i j} = x _ {i}, i = 1, \dots , n. \end{array}
$$

于是

$$
(\mathbf {A} ^ {\prime} f _ {i}) (x) = \sum_ {j = 1} ^ {n} a _ {i j} f _ {j} (x), \forall x \in X.
$$

即

$$
\mathbf {A} ^ {\prime} f _ {i} = \sum_ {j = 1} ^ {n} a _ {i j} f _ {j}, i = 1, \dots , n.
$$

这正是(5.2)式,而(5.2)式右端的矩阵正是 A 的转置矩阵.

这表明Banach共轭算子是矩阵之转置矩阵的推广，应该强调指出这个推广完全摆脱了坐标系的束缚，适用于无穷维Banach空间上的一切有界线性算子.

还该指出, 比较 Banach 共轭算子 $\mathbf{A}'$ 的矩阵元与第二章 §4 中所谓 Hilbert 共轭算子 $\mathbf{A}^*$ 的矩阵元, 正好相差一个复共轭, 它们是不同的, 但是初学者却往往忽略这一点.

例1 设 $1 < p < \infty, \frac{1}{p} + \frac{1}{q} = 1, K(t, s)$ 是矩形 $a \leqslant t, s \leqslant b$ 上复值可测函数，且

$$
\int_ {a} ^ {b} \int_ {a} ^ {b} | K (t, s) | ^ {q} \mathrm{d} t \mathrm{d} s <   \infty ,
$$

则以 $K(t,s)$ 为核的积分算子

$$
(T x) (t) = \int_ {a} ^ {b} K (t, s) x (s) \mathrm{d} s, x = x (t) \in L ^ {p} [ a, b ],
$$

是从 $L^p [a,b]$ 到 $L^q [a,b]$ 的有界线性算子.事实上，由Hölder不等式

$$
\begin{array}{r l} \int_ {a} ^ {b} | (T x) (t) | ^ {q} \mathrm{d} t & = \int_ {a} ^ {b} \left| \int_ {a} ^ {b} K (t, s) x (s) \mathrm{d} s \right| ^ {q} \mathrm{d} t \\ & \leqslant \int_ {a} ^ {b} \left[ \int_ {a} ^ {b} | K (t, s) | ^ {q} \mathrm{d} s \right] \left[ \int_ {a} ^ {b} | x (s) | ^ {p} \mathrm{d} s \right] ^ {q / p} \mathrm{d} t \\ & \leqslant \int_ {a} ^ {b} \int_ {a} ^ {b} | K (t, s) | ^ {q} \mathrm{d} s \mathrm{d} t \| x \| ^ {q}. \end{array}
$$

从而

$$
\begin{array}{r l} \| T x \| & = \left(\int_ {a} ^ {b} | (T x) (t) | ^ {q} \mathrm{d} t\right) ^ {1 / q} \\ & \leqslant \left(\int_ {a} ^ {b} \int_ {a} ^ {b} | K (t, s) | ^ {q} \mathrm{d} s \mathrm{d} t\right) ^ {1 / q} \| x \|. \end{array}
$$

可见 $T$ 是有界的.

根据定理4.4，每个 $f\in (L^q [a,b])'$ 对应唯一的 $y = y(t)\in L^{p}[a,b]$ ，使

$$
f (z) = \int_ {a} ^ {b} z (t) y (t) \mathrm{d} t, \text {当} z = z (t) \in L ^ {q} [ a, b ].
$$

故对任何 $x = x(t) \in L^{p}[a, b]$ ,

$$
\begin{array}{r l} (T ^ {\prime} f) (x) & = f (T x) \\ & = \int_ {a} ^ {b} (T x) (t) y (t) \mathrm{d} t \\ & = \int_ {a} ^ {b} \left[ \int_ {a} ^ {b} K (t, s) x (s) \mathrm{d} s \right] y (t) \mathrm{d} t \\ & = \int_ {a} ^ {b} x (s) \left[ \int_ {a} ^ {b} K (t, s) y (t) \mathrm{d} t \right] \mathrm{d} s. \end{array}\tag{5.3}
$$

不计同构，把 $(L^p [a,b])'$ 与 $L^q [a,b]$ 等同， $(L^{q}[a,b])^{\prime}$ 与 $L^p [a,b]$ 等同.即 $f$ 与 $y$ 等同，则 $T^{\prime}f$ 对应着 $T^{\prime}y\in L^{q}[a,b]$ ，即

$$
(T ^ {\prime} f) (x) = \int_ {a} ^ {b} x (s) (T ^ {\prime} y) (s) \mathrm{d} s, \text {当} x = x (t) \in L ^ {p} [ a, b ].\tag{5.4}
$$

比较(5.3)与(5.4)，根据唯一性可得

$$
(T ^ {\prime} y) (s) = \int_ {a} ^ {b} K (t, s) y (t) \mathrm{d} t,
$$

即

$$
(T ^ {\prime} y) (t) = \int_ {a} ^ {b} K (s, t) y (s) \mathrm{d} s, y = y (t) \in L ^ {p} [ a, b ].
$$

积分算子 $T'$ 也是从 $L^p [a,b]$ 到 $L^q [a,b]$ 的有界线性算子.但是 $T'$ 的核 $K(s,t)$ 与积分算子 $T$ 的核 $K(t,s)$ 相比正好颠倒了 $s$ 和 $t$ 的位置.

例2 设 $K(x, y) \in L^2(S)$ , 其中 $S = \{(x, y): 0 \leqslant x, y \leqslant 1\}$ 是矩形. 则从例1可知积分算子

$$
(T f) (x) = \int_ {0} ^ {1} K (x, y) f (y) \mathrm{d} y, f = f (x) \in L ^ {2} [ 0, 1 ],
$$

是 $L^2 [0,1]$ 上的有界线性算子.

根据 Hilbert 共轭算子定义，

$$
\begin{array}{r l} (T ^ {*} f, g) & = (f, T g) \\ & = \int_ {0} ^ {1} f (x) \overline {{(T g) (x)}} d x \\ & = \int_ {0} ^ {1} f (x) \left[ \overline {{\int_ {0} ^ {1} K (x , y) g (y) d y}} \right] d x \\ & = \int_ {0} ^ {1} \overline {{g (y)}} \left[ \int_ {0} ^ {1} \overline {{K (x , y)}} f (x) d x \right] d y, \end{array}
$$

对任何 $f, g \in L^2[0,1]$ , 故

$$
(T ^ {*} f) (y) = \int_ {0} ^ {1} \overline {{{K (x , y)}}} f (x) \mathrm{d} x.
$$

或

$$
(T ^ {*} f) (x) = \int_ {0} ^ {1} \overline {{{{K (y , x)}}}} f (y) \mathrm{d} y.
$$

可见积分算子 $T^{*}$ 的核 $\overline{K(y,x)}$ 与积分算子 $T$ 的核 $K(x,y)$ 相比，不仅颠倒了 $x,y$ 的位置，而且差一个复共轭.

定理 5.1 设 X 与 Y 都是 Banach 空间, $T \in L(X, Y)$ , 则 $T'$ 是从 $Y'$ 到 $X'$ 的有界线性算子, 且

(1) $\| T^{\prime}\| = \| T\|$ .

(2) $(T + S)' = T' + S'$ .

(3) $(\alpha T)' = \alpha T'$ .

这里 $S \in L(X, Y), \alpha$ 是任意常数.

证 (2)与(3)显然,至于(1),由§4中3.,

$$
\| T x \| = \sup _ {\| y ^ {\prime} \| \leqslant 1} | y ^ {\prime} (T x) |,
$$

故

$$
\begin{array}{r l} \| T \| & = \sup _ {\| x \| \leqslant 1} \| T x \| \\ & = \sup _ {\| x \| \leqslant 1} \sup _ {\| y ^ {\prime} \| \leqslant 1} | y ^ {\prime} (T x) | \\ & = \sup _ {\| y ^ {\prime} \| \leqslant 1} \sup _ {\| x \| \leqslant 1} | (T ^ {\prime} y ^ {\prime}) (x) | \\ & = \sup _ {\| y ^ {\prime} \| \leqslant 1} \| T ^ {\prime} y ^ {\prime} \| \\ & = \| T ^ {\prime} \|. \end{array}
$$

证毕.

注意,本定理的(3)与 Hilbert 共轭算子相应的结果第二章 §4 中定理 4.1 的(4)不同.

定理5.2 设 $X$ 是Banach空间， $S, T \in L(X)$ ，则

(1) $(ST)' = T'S'$ .

(2) 若 $T$ 是有界可逆的, 则 $T'$ 亦是有界可逆的, 且

$$
\left(T ^ {\prime}\right) ^ {- 1} = \left(T ^ {- 1}\right) ^ {\prime}.
$$

证 (1) 对任给的 $x \in X, x' \in X'$ ,

$$
[ (S T) ^ {\prime} x ^ {\prime} ] (x) = x ^ {\prime} ([ S T ] x) = \left(S ^ {\prime} x ^ {\prime}\right) (T x) = \left(T ^ {\prime} S ^ {\prime} x ^ {\prime}\right) (x).
$$

故 $(ST)' = T'S'$ .

至于(2)，注意 $I' = I$ ，由(1)可知

$$
I = (T ^ {- 1} T) ^ {\prime} = T ^ {\prime} (T ^ {- 1}) ^ {\prime}, I = (T T ^ {- 1}) ^ {\prime} = (T ^ {- 1}) ^ {\prime} T ^ {\prime}.
$$

可见(2)成立.证毕.

定理 5.3 设 X, Y 都是 Banach 空间, $T \in L(X, Y)$ , 则 $T''$ 是 T 的扩张, 即对任何 $x \in X$ ,

$$
T ^ {\prime \prime} [ \tau (x) ] = \tau_ {1} (T x),
$$

这里 $\tau: X \to X'', \tau_1: Y \to Y''$ 都是典型映射.

证显然, $T'' \in L(X'', Y'')$ . 对 $x \in X$ , 根据典型映射 $\tau$ ,

$$
\tau (x) \left(x ^ {\prime}\right) = x ^ {\prime} (x), \forall x ^ {\prime} \in X ^ {\prime}.
$$

对 $y \in Y$ ，根据典型映射 $\tau_1$ ，

$$
\tau_ {1} (y) \left(y ^ {\prime}\right) = y ^ {\prime} (y), \forall y ^ {\prime} \in Y ^ {\prime}.
$$

于是对任给的 $y^{\prime} \in Y^{\prime}$ ,

$$
T ^ {\prime \prime} [ \tau (x) ] (y ^ {\prime}) = \tau (x) (T ^ {\prime} y ^ {\prime}) = (T ^ {\prime} y ^ {\prime}) (x) = y ^ {\prime} (T x) = \tau_ {1} (T x) (y ^ {\prime}).
$$

可见

$$
T ^ {\prime \prime} [ \tau (x) ] = \tau_ {1} (T x), \forall x \in X.
$$

证毕.

对 Hilbert 空间上有界线性算子 $T$ , 除了 Banach 共轭算子 $T'$ , 在第二章 §4 中, 我们还讲到 Hilbert 共轭算子 $T^{*}$ . 从例 1 和例 2 我们已经看到, $T^{*}$ 与 $T'$ 是不同的, 但它们也并非毫不相关, 下面我们来考察 $T^{*}$ 与 $T'$ 的关系.

设 $H_{1}$ 与 $H_{2}$ 都是Hilbert空间， $T \in L(H_{1}, H_{2})$ 。令

$$
f = T ^ {\prime} g, \quad f \in H _ {1} ^ {*}, g \in H _ {2} ^ {*}.\tag{5.5}
$$

按 $T^{\prime}$ 的定义

$$
f (x) = T ^ {\prime} g (x) = g (T x), \quad \forall x \in H _ {1}.\tag{5.6}
$$

根据 Fréchet-Riesz 表现定理, 对每个 $f \in H_1^*$ , 恰有一个 $x_f \in H_1$ , 使

$$
f (x) = \left(x, x _ {f}\right), \quad \forall x \in H _ {1},\tag{5.7}
$$

且

$$
\| x _ {f} \| = \| f \|
$$

引进算子 $A: H_1^* \to H_1$ ，如下：

$$
A f = x _ {f}. \text {当} f \in H _ {1} ^ {*},\tag{5.8}
$$

则 $A$ 是保范共轭同构(见第二章，§3). 同理, 存在保范共轭同构 $B: H_2^* \to H_2$ ，使

$$
B g = y _ {g}  , \text {当}   g \in H _ {2} ^ {*}  .\tag{5.9}
$$

这里 $y_{g} \in H_{2}$ 满足

$$
g (y) = \left(y, y _ {g}\right), \forall y \in H _ {2},\tag{5.10}
$$

且

$$
\| y _ {g} \| = \| g \|
$$

于是由(5.5)，(5.8)和(5.9)得

$$
A T ^ {\prime} B ^ {- 1} y _ {g} = A T ^ {\prime} g = A f = x _ {f}.\tag{5.11}
$$

而从(5.6)，(5.7)与(5.10)可见

$$
\begin{array}{r l} (x, x _ {f}) & = f (x) = g (T x) = (T x, y _ {g}) \\ & = (x, T ^ {*} y _ {g}), \forall x \in H _ {1}. \end{array}
$$

故

$$
x _ {f} = T ^ {*} y _ {g}.\tag{5.12}
$$

比较(5.11)与(5.12)可得

$$
T ^ {*} = A T ^ {\prime} B ^ {- 1}.
$$

总结上述,我们得到定理 5.4 设 $H_{1}$ 与 $H_{2}$ 都是 Hilbert 空间， $T \in L(H_{1}, H_{2})$ ， $T^{*}$ ， $T'$ 分别是 T 的 Hilbert 共轭算子与 Banach 共轭算子，则

$$
T ^ {*} = A T ^ {\prime} B ^ {- 1}.
$$

其中， $A:H_1^*\rightarrow H_1,B:H_2^*\rightarrow H_2$ 分别是保范共轭同构.

这表明了 Hilbert 空间上两种共轭算子之间的关系. 顺便该提到, 通常对 Hilbert 空间上有界线性算子谈论共轭时, 如不特别声明总是指 Hilbert 共轭算子.

## § 6 算子的值域与零空间,商空间

## 1. 算子的值域与零空间本节恒设 A 为 Banach 空间 X 上的有界线性算子, 和以前一样我们称

$$
N (A) = \{x: A x = 0 \}
$$

为 $A$ 的零空间，

$$
R (A) = \{y: y = A x, x \in X \}
$$

为 A 的值域.

在前一节我们已经从有限维空间情况看到算子的值域,零空间,以及共轭算子的概念与方程 Ax=y 的求解密切相关,所以它们是算子理论中极重要的概念.

在有限维空间的讨论,我们还涉及 $A'$ 的行向量空间以及它的正交补.但是在一般Banach空间中,并没有内积,需要引进下列概念.

定义6.1 设 $X$ 是Banach空间.

(1) 对线性流形 $M \subset X$ ，所谓 M 在 $X'$ 中的零化子，即

$$
M ^ {0} \stackrel {\mathrm{d}} {=} \left\{y ^ {\prime} \in X: y ^ {\prime} (x) = 0, \text {当} x \in M \right\}.
$$

(2) 对线性流形 $G \subset X'$ , 所谓 $G$ 在 $X$ 中的零化子, 即

$$
{ } ^ { 0 } G = \{ x \in X : y ^ { \prime } ( x ) = 0 , \text {当} y ^ { \prime } \in G \} .
$$

显然零化子是内积空间中正交补的推广.

在 Hilbert 空间中, 当 $M$ 是闭的, 则 $(M^{\perp})^{\perp} = M$ . 现在对于 Banach 空间, 有下列结果定理6.1 设 $X$ 是Banach空间.

(1) 如果 M 是 X 的子空间, 则 $^{0}(M^{0}) = M$ .

(2) 若 $X$ 是自反的, $G$ 是 $X'$ 的子空间, 则 $(^0 G)^0 = G$ .

证（1）显然 $M \subset^0 (M^0)$ . 如果 $x_0 \in {}^0 (M^0)$ , 则每当 $y' \in M^0, y'(x_0) = 0$ . 即对 $X$ 上任何连续线性泛函 $y', y'(x) = 0, \forall x \in M$ , 蕴含 $y'(x_0) = 0$ . 因 $M$ 是闭的, 根据命题2.3, $x_0 \in M$ . 总之, ${}^0 (M^0) = M$ .

(2) 显然 $G \subset (^{0} G)^{0}$ . 若 $y_{0}^{\prime} \in (^{0} G)^{0}$ , 必有 $y_{0}^{\prime} \in G$ . 否则, 由命题 2.2, 存在 $x_{0}^{\prime \prime} \in X^{\prime \prime}$ , 使

$$
x _ {0} ^ {\prime \prime} (y _ {0} ^ {\prime}) \neq 0, \text {且} x _ {0} ^ {\prime \prime} (x ^ {\prime}) = 0, \text {当} x ^ {\prime} \in G.
$$

因 $X$ 是自反的，必有 $x_0 \in X$ ，使

$x''_0(x') = x'(x_0)$ ，当 $x^{\prime}\in X$

于是

$y^{\prime}_{0}(x_{0})\neq 0$ ，但 $x^{\prime}(x_0) = 0$ ，当 $x^{\prime}\in G$

这与 $y_0^\prime \in (^0 G)^0$ 的假设矛盾. 证毕.

应该指出,对于非自反的 Banach 空间 X,(2)未必成立.(参见[43],§Ⅲ.7)

下面我们来讨论值域与零空间的关系.

引理6.1 $(\overline{R(A)})^0 = N(A')$

证设 $y' \in N(A')$ ，则 $A'y' = 0$ . 故对任意的 $x \in X$

$$
y ^ {\prime} (A x) = A ^ {\prime} y ^ {\prime} (x) = 0.
$$

任给 $y \in \overline{R(A)}$ ，应有 $x_{n} \in X, n = 1, 2, \cdots$ ，使 $y = \lim_{n \to \infty} Ax_{n}$ ，于是

$$
y ^ {\prime} (y) = \lim _ {n \rightarrow \infty} y ^ {\prime} (A x _ {n}) = 0.
$$

因此 $y' \in (\overline{R(A)})^0$ .

反之，若 $y' \in (\overline{R(A)})^0$ ，则任给 $x \in X, y'(Ax) = 0$ ，即 $A'y'(x) = 0$ . 故 $A'y' = 0$ ，亦即 $y' \in N(A)'$ . 证毕.

引理 6.2 $^{0}(\overline{R(A^{\prime})})=N(A)$ .

证设 $x \in N(A)$ , 则 $Ax = 0$ . 于是对任意的 $x' \in X'$ ,

$$
A ^ {\prime} x ^ {\prime} (x) = x ^ {\prime} (A x) = 0.
$$

任给 $y' \in \overline{R(A')}$ ，应有 $x_{n}' \in X', n = 1, 2, \cdots$ ，使 $y' = \lim_{n \to \infty} A' x_{n}'$ 。从而

$$
y ^ {\prime} (x) = \lim _ {n \rightarrow \infty} A ^ {\prime} x _ {n} ^ {\prime} (x) = 0.
$$

故 $x \in^{0}(\overline{R(A^{\prime})})$ .

反之，设 $x \in^{0}(\overline{R(A^{\prime})})$ ，则对任意的 $x^{\prime} \in X^{\prime}, A^{\prime} x^{\prime}(x) = 0$ ，即 $x^{\prime}(Ax) = 0$ 根据Hahn-Banach定理的推论(命题2.1)， $Ax = 0$ .即 $x \in N(A)$ .证毕.

引理 6.3 $^{0}N(A')=\overline{R(A)}$ .

引理6.4 $\overline{R(A')}\subset N(A)^0$

引理6.5 若 $X$ 是自反的, 则

$$
\overline {{{R (A ^ {\prime})}}} = N (A) ^ {0}.
$$

这三个引理可直接证明,也可用定理6.1与前面的两个引理来证.

以引理 6.5 为例,从引理 6.2,

$$
{ } ^ { 0 } ( \overline { { R ( A ^ { \prime } ) } } ) = N ( A ) .
$$

因为 $X$ 是自反的，且 $\overline{R(A')}$ 是 $X'$ 的子空间，根据定理6.1的(2)，由上式可得

$$
\overline {{{R (A ^ {\prime})}}} = \left[ ^ {0} (\overline {{{R (A ^ {\prime})}}}) \right] ^ {0} = N (A) ^ {0}.
$$

综上所述，有定理 6.2 设 A 是 Banach 空间 X 上的有界线性算子, 则

$$
N (A) = ^ {0} \left(\overline {{{R \left(A ^ {\prime}\right)}}}\right), N \left(A ^ {\prime}\right) = \left(\overline {{{R (A)}}}\right) ^ {0},
$$

$$
\overline {{{{R (A)}}}} = ^ {0} N \left(A ^ {\prime}\right), \quad \overline {{{{R (A ^ {\prime})}}}} \subset N (A) ^ {0}.
$$

若更设 $X$ 是自反的, 则

$$
\overline {{{R (A ^ {\prime})}}} = N (A) ^ {0}.
$$

这个定理已如前述来源于线性代数, 其实它也与积分方程论中的 Fredholm 交替定理密切相关. 此外, 如 Lorch 所指出, 这里正显示出自反空间概念对于算子结构理论的重要性(见[36], 第53页). 可以举出例子, 如果 $X$ 不是自反的, 等式

$$
\overline {{{R (A ^ {\prime})}}} = N (A) ^ {0}
$$

确实可以不成立.(参见文献[42]).

定理6.3 $\overline{R(A)} = X \Leftrightarrow A'$ 是单射的.

证 $\Rightarrow$ .从定理6.2，

$$
N (A ^ {\prime}) = (\overline {{{R (A)}}}) ^ {0} = X ^ {0} = \{0 \}.
$$

即 $A^{\prime}$ 是单射的.

至于 $\Leftarrow$ .从定理6.2，

$$
\overline {{{R (A)}}} = ^ {0} N \left(A ^ {\prime}\right) = ^ {0} \{0 \} = X.
$$

证毕.

同样可以证明当 $X$ 是自反空间时，

$$
\overline {{{{R (A ^ {\prime})}}}} = X ^ {\prime} \Leftrightarrow A \text {是单射的}.
$$

应该指出, 定理 6.2 是关于值域的闭包 $\overline{R(A)}$ , 还不是关于值域 $R(A)$ 的结果. 例如, 我们只有

$$
{ } ^ { 0 } N ( A ^ { \prime } ) = \overline { { R ( A ) } } .\tag{6.1}
$$

还没有达到有限维空间的结果(5.1).此外,从定理6.3也只是

$$
\overline {{{{R (A)}}}} = X \Leftrightarrow A ^ {\prime} \text {是单射的}.
$$

我们当然关心 $A'$ 的逆是否连续，从上面的讨论还不能知道。但如果 $R(A)$ 是闭的，情况就很好了。这使(6.1)成为

$$
{ } ^ { 0 } N ( A ^ { \prime } ) = R ( A ) .
$$

关于这方面的一个重要结果是 Banach 给出之著名的闭值域定理.

定理 6.4(闭值域定理) 设 X 与 Y 都是 Banach 空间, $T \in L(X, Y)$ , 则下列各命题等价:

(1) $R(T)$ 是闭集；

(2) $R(T^{\prime})$ 是闭集；

(3) $R(T) = ^0 N(T')$ ;

(4) $R(T') = N(T)^0$ ;

(5) $T$ 是开映射；

(6) $T'$ 是开映射.

所谓开映射即将开集映为开集的映射.这里所说 $T(T^{\prime})$ 是开映射，指的是将 $T(T^{\prime})$ 看作 $X(Y^{\prime})$ 到 $R(T)(R(T^{\prime}))$ 上的映射是开映射.

关于这个定理的证明,有兴趣的读者可参见[10],第101页.

历史地讲,线性代数理论确实提供了探索算子理论的背景和巨大的推动力.例如在第三章§5中我们已经看到Banach空间共轭算子与转置矩阵的关系,对于有限维空间上的线性变换A及与它相应的矩阵A,那里还讲到

$$
R (\mathbf {A}) = A \text {的列向量空间}.
$$

我们熟知,一个矩阵的行向量空间的维数等于列向量空间的维数(参见[2],第四章,§4,定理4).而

$$
R (\mathbf {A} ^ {\prime}) = A ^ {\prime} \text {的列向量空间} = A \text {的行向量空间}.
$$

故

$$
\dim R \left(\mathbf {A} ^ {\prime}\right) = \dim R (\mathbf {A}).\tag{6.2}
$$

现在,从闭值域定理立刻可见,对 n 维空间 X 上线性变换 T 总有

$$
\dim N (T) + \dim R (T) = \dim X = n.
$$

这是线性代数学中的重要公式.有人甚至说它“几乎包括了我们所知道的关于线性方程组的所有知识”(见[1],第107页),关于(6.2)式的简单且直接的证明可参见[2],第七章,§6.

从上面所说的可见,闭值域定理实为线性代数学上线性变换的值域与零空间的研究在无穷维空间的推广.再从下面第四章中定理3.9的证明,由闭值域定理立刻可推出著名的两择一定理,则是经典的线性积分方程论中熟知结果的推广.总之,闭值域定理来自经典的线性代数与积分方程理论,在线性算子方程可解性的理论中扮演着重要的角色.

根据定理 6.3 与定理 6.4, 可知

$$
R (A) = X \Leftrightarrow A ^ {\prime} \text {的逆是连续的.}
$$

及

$$
R (A ^ {\prime}) = X ^ {\prime} \Longleftrightarrow A \text {的逆是连续的.}
$$

如前所述, 对于一个算子 A, 其值域 $R(A)$ 是否闭是至关重要的. 当然绝非对每个有界线性算子 A, $R(A)$ 都是闭的. 例如, 在 $t^{1}$ 上, 对 $x = \{\xi_{1}, \xi_{2}, \xi_{3}, \cdots\} \in t^{1}$ , 定义

$$
A x = \left\{\xi_ {1}, \frac {\xi_ {2}}{2}, \frac {\xi_ {3}}{3}, \dots \right\}.
$$

则 $A$ 是 $\ell^1$ 上有界线性算子. 显然只有有限个坐标不为 0 的点的集合包含于 $R(A)$ 中, 且在 $\ell^1$ 中稠密, 故 $\overline{R(A)} = \ell^1$ . 但

$$
y = \left\{1, \frac {1}{2 ^ {2}}, \frac {1}{3 ^ {2}}, \dots \right\}
$$

不属于 $R(A)$ 而属于 $\ell^1$

注意定理 5.4 中的 A, B 都是保范双射算子, 从它和定理 6.4 不难得到关于 Hilbert 共轭算子的下列结果定理6.5 设 $H_{1}$ 与 $H_{2}$ 都是Hilbert空间， $T \in L(H_{1}, H_{2})$ ，则下列各命题等价：

(1) $R(T)$ 是闭集；

(2) $R(T^{*})$ 是闭集；

(3) $R(T) = N(T^{*})^{\perp}$ ;

(4) $R(T^{*}) = N(T)^{\perp}$ ;

(5) $T$ 是开映射；

(6) $T^{*}$ 是开映射.

这里所说 $T(T^{*})$ 是开映射，指的是将 $T(T^{*})$ 看作 $H_{1}(H_{2})$ 到 $R(T)(R(T^{*}))$ 上的映射是开映射.

## 2. 商空间及对偶定理闭值域定理的证明用到 Banach 空间的商空间, 而且商空间的理论和方法也是算子理论中常用的基本技巧, 因此有必要介绍一点关于商空间的基本知识. 我们就从集合的等价关系和等价类谈起.

设 $S$ 是一个非空集合, $R$ 表示 $S$ 中元素之间的某种关系, 若 $x, y \in S$ 具有这种关系, 记为 $xRy$ . 例如, 全体实数 $\mathbf{R}$ 是一个集合, “=” 表示两个实数之间的一种关系, “≥”也表示一种关系. 再比如, 平面上全体直线是一个集合, “//” (平行) 是一种关系, “⊥” (垂直) 是一种关系, 相交也是一种关系. 在各种关系中, 我们感兴趣的是所谓的等价关系.

定义 6.2 集合 S 上的关系 R 称为等价关系, 如果它具有下述性质:

(1) $xRx$ ，(反身性)

(2) 若 $xRy$ , 则 $yRx$ , (对称性)

(3) 若 $xRy, yRz$ , 则 $xRz$ , (传递性)

对任意的 $x, y, z \in S$ .

比如，R 上的关系“=”是等价关系，但“≥”不是等价关系；平面直线间的“//”是等价关系，但“⊥”不是等价关系。

设 $R$ 是集合 $S$ 上的一个等价关系， $\forall x \in S$ ，令

$$
[ x ] = \{y \in S: y R x \},
$$

称之为 $x$ 的等价类，或 $x$ 的陪集.

例如，在平面上全体直线集合中，令

$$
l _ {0}: y = 0
$$

表示实数轴,则其在平行关系下的等价类为

$$
[ l _ {0} ] = \{l: y = C   |   C \in \mathbf {R}   \text {是常数} \},
$$

即 $[l_0]$ 是平面上平行实数轴的全体直线的集合.

设 X 是(复)线性空间, M 是 X 的线性流形, 定义 X 上的关系 R 如下:

$$
x R y \text { 表示 } x - y \in M.
$$

容易验证 $R$ 是一个等价关系. 给定 $x \in X$ , 其陪集为

$$
[ x ] = x + M \stackrel {\mathrm{d}} {=} \left\{x + z: z \in M \right\}.
$$

现在我们考虑 X 中所有元的陪集做成的集合, 记为 X/M. 在其中可以定义线性运算

$$
\begin{array}{r l} {[ x ] + [ y ] = [ x + y ],} \\ {\alpha [ x ] = [ \alpha x ],} \end{array}
$$

对 $x, y \in X, \alpha \in \mathbf{C}$ . 容易验证定义是完善的, 按这样定义的线性运算, $X / M$ 也是线性空间. 称 $X / M$ 为 $X$ 关于 $M$ 之商空间. $X / M$ 中零元就是 $X$ 中零元 0 所在的陪集[0], 即 $M$ . 从 $X$ 到商空间 $X / M$ 有一个自然映射 $\pi: X \to X / M$ ,

$$
\pi (x) = [ x ], \forall x \in X.
$$

显然 $\pi$ 是线性映射,通常称 $\pi$ 为商映射或自然同态.

如果 X 是赋范线性空间, M 是 X 之子空间, 即 X 之闭的线性流形, 如上产生的商空间 X/M 也可以赋以范数使之成为赋范线性空间. 定义

$$
\| [ x ] \| = \inf \{\| y \|: \forall y \in [ x ] \}.
$$

由陪集定义实际上也有

$$
\| [ x ] \| = \inf \{\| x - m \|: \forall m \in M \} = \operatorname{dist} (x, M).
$$

往证 $\| [x]\|$ 确实是 $X / M$ 上的范数.

(1) $\| [x] \| \geqslant 0$ ，且 $\| [x] \| = 0$ 当且仅当 $[x] = 0$ .

只须证 $\| [x]\| = 0\Rightarrow [x] = 0$ ，即 $x\in M.$ 由 $\| [x]\|$ 定义，当 $\| [x]\| = 0$ 存在 $y_{n}\in M$ ，使 $\| y_n - x\| \to 0$ ，而 $M$ 是闭集，故 $x\in M$

(2) $\| \alpha[x] \| = |\alpha| \|[x]\|$ , 对任意 $\alpha \in \mathbf{C}$ .

事实上，对任意 $\alpha \neq 0$

$$
\begin{array}{r l} \parallel \alpha [ x ] \parallel & = \parallel [ \alpha x ] \parallel \\ & = \inf \{\parallel y \parallel : y \in [ \alpha x ] \} \\ & = \inf \{\parallel \alpha z \parallel : z \in [ x ] \} \\ & = \inf \{| \alpha | \parallel z \parallel : z \in [ x ] \} \\ & = | \alpha | \inf \{\parallel z \parallel : z \in [ x ] \} \\ & = | \alpha | \parallel [ x ] \|. \end{array}
$$

$$
[ x ] + [ y ] \| \leqslant \| [ x ] \| + \| [ y ]
$$

由 $\| [\cdot ]\|$ 定义， $\forall \varepsilon >0$ ，存在 $x_{1}\in [x],y_{1}\in [y]$ ，使

$$
\| x _ {1} \| <   \| [ x ] \| + \frac {\varepsilon}{2}, \quad \| y _ {1} \| <   \| [ y ] \| + \frac {\varepsilon}{2}.
$$

从而

$$
\begin{array}{r l} \left\| x _ {1} + y _ {1} \right\| & \leqslant \left\| x _ {1} \right\| + \left\| y _ {1} \right\| \\ & <   \left\| [ x ] \right\| + \left\| [ y ] \right\| + \varepsilon . \end{array}
$$

由于 $x_{1} - x\in M,y_{1} - y\in M$ ，则

$$
(x _ {1} + y _ {1}) - (x + y) = (x _ {1} - x) + (y _ {1} - y) \in M,
$$

故 $x_{1} + y_{1}\in [x + y]$ ，从而

$$
\begin{array}{r l} \| [ x ] + [ y ] \| & = \| [ x + y ] \| \leqslant \| x _ {1} + y _ {1} \| \\ & <   \| [ x ] \| + \| [ y ] \| + \varepsilon . \end{array}
$$

而 $\varepsilon$ 是任意的，所以

$$
\| [ x ] + [ y ] \| \leqslant \| [ x ] \| + \| [ y ] \|.
$$

总之 $\| [\cdot ]\|$ 确实是 $X / M$ 上范数，通常称为商范数.

这里需要注意的是 $M$ 必须是闭的, 否则, 不能由 $\| [x] \| = 0$ 得出 $[x] = 0$ , 即 $x \in M$ .

若 X 是赋范线性空间, 线性映射 $\pi: X \rightarrow X/M$ 是压缩的, 即

$$
\| \pi (x) \| = \| [ x ] \| \leqslant \| x \|, \forall x \in X.
$$

因而， $\pi: X \to X / M$ 一定是连续的。

进一步可以证明若 $X$ 是Banach空间， $M$ 是 $X$ 之子空间，则 $X / M$ 按商范数亦是Banach空间.

定理 6.6 设 X 是 Banach 空间, M 是 X 之子空间, 则 X/M 亦是 Banach 空间.

证只须证明 $X / M$ 是完备的. 由第一章习题23, 又只须证明 $X / M$ 中任何绝对收敛的级数都收敛.

设 $\sum_{n=1}^{\infty}[x]_n$ 是 $X / M$ 中绝对收敛的级数，即

$$
\sum_ {n = 1} ^ {\infty} \| [ x ] _ {n} \| <   \infty .
$$

由 $X / M$ 中范数的定义，对每个正整数 $n$ ，可取 $x_{n}\in [x]_{n}$ ，使

$$
\| x _ {n} \| \leqslant 2 \| [ x ] _ {n} \|,
$$

于是

$$
\sum_ {n = 1} ^ {\infty} \parallel x _ {n} \parallel <   \infty ,
$$

即 $\sum_{n=1}^{\infty} x_n$ 是 $X$ 中绝对收敛的级数. 而 $X$ 是 Banach 空间, 由第一章习题 23, $\sum_{n=1}^{\infty} x_n$ 收敛. 设 $y = \sum_{n=1}^{\infty} x_n$ , 则

$$
\left\| \sum_ {n = 1} ^ {N} [ x ] _ {n} - [ y ] \right\| = \left\| \left[ \sum_ {n = 1} ^ {N} x _ {n} - y \right] \right\|
$$

$$
\leqslant \left\| \sum_ {n = 1} ^ {N} x _ {n} - y \right\|\rightarrow 0, \text {当} N \rightarrow \infty .
$$

故 $\sum_{n=1}^{\infty}[x]_n = [y]$ , 即 $\sum_{n=1}^{\infty}[x]_n$ 收敛. 证毕.

给定一个 Banach 空间 X, 及其子空间 M, 得到商空间 X/M, 它们的对偶空间应有一种关系. 下面的对偶定理清楚地描述了这种关系.

定理 6.7 设 X 是 Banach 空间, M 是 X 之子空间, 则

(1) $M'$ 与 $X'/M^{0}$ 保范同构，

(2) $(X / M)'$ 与 $M^0$ 保范同构，这里 $M^0$ 表示 $M$ 在 $X'$ 中的零化子.

证（1）设 $f \in M'$ ，则 $f$ 是 $M$ 上连续线性泛函。由Hahn-Banach扩张定理，存在 $F \in X'$ ，使

$$
F (x) = f (x), \forall x \in M,
$$

且

$$
\| F \| = \| f \|
$$

假设 $F_{1} \in X'$ 是 $f$ 另一个扩张，即

$$
F _ {1} (x) = f (x), \forall x \in M.
$$

则

$$
(F - F _ {1}) (x) = F (x) - F _ {1} (x) = 0, \quad \forall x \in M.
$$

可见 $F - F_{1} \in M^{0}$ . 从而 $F_{1} \in [F] \in X' / M^{0}$ . 这说明每个 $f \in M'$ 唯一确定一个元 $[F] \in X' / M^{0}$ , 其中 $F$ 是 $f$ 之扩张.

定义映射 $\tau: M' \to X' / M^0$ 如下：

$$
\tau (f) = [ F ], \forall f \in M ^ {\prime},
$$

这里 $F$ 是 $f$ 的扩张. 显然 $\tau$ 是线性的. 如果 $\tau(f) = [F] = 0$ , 即零泛函亦是 $f$ 的扩张, 则 $f = 0$ . 所以 $\tau$ 是单射的. 往证 $\tau$ 是满射的. 设 $[F] \in X' / M^0$ , 任取 $F_1 \in [F]$ , 令 $f = F_1 \mid M$ , 即

$$
f (x) = F _ {1} (x), \forall x \in M,
$$

则 $f \in M'$ , 而 $F_{1}$ 是 $f$ 的扩张, 于是 $\tau(f) = [F_{1}] = [F]$ , 可见 $\tau$ 是满射的.

下面证 $\tau$ 是保范的. 设 $f \in M'$ , 则任意 $F_{1} \in [F] = \tau(f)$ 都是 $f$ 的扩张, 故 $\|F_{1}\| \geqslant \|f\|$ , 从而

$$
\| \tau (f) \| = \| [ F ] \| = \inf \{\| F _ {1} \|: F _ {1} \in [ F ] \} \geqslant \| f \|.
$$

设 $F_{0}$ 是 $f$ 之保范扩张，则

$$
\| \tau (f) \| = \| [ F _ {0} ] \| \leqslant \| F _ {0} \| = \| f \|.
$$

总之， $\| \tau(f) \| = \| f \|$ . 因而 $\tau: M' \to X'/M^0$ 是保范同构.

(2) 设 $f \in M^0$ . 定义

$$
\hat {f} ([ x ]) = f (x _ {1}), \forall x _ {1} \in [ x ] \in X / M.\tag{6.3}
$$

若又有 $x_{2} \in [x]$ , 则 $x_{1} - x_{2} \in M$ . 于是 $f(x_{1} - x_{2}) = 0$ , 即 $f(x_{1}) = f(x_{2})$ . 这说明 $\hat{f}$ 之定义是完善的. 易见 $\hat{f}$ 是 $X / M$ 上线性泛函, 而且

$$
| \hat {f} ([ x ]) | = | f (x _ {1}) | \leqslant \| f \| \| x _ {1} \|, \quad \forall x _ {1} \in [ x ],
$$

故

$$
\begin{array}{r l} | \hat {f} ([ x ]) | & \leqslant \| f \| \inf \{\| x _ {1} \|: x _ {1} \in [ x ] \} \\ & = \| f \| \| [ x ] \|. \end{array}
$$

这说明 $\hat{f} \in (X / M)'$ ，而且 $\| \hat{f} \| \leqslant \| f \|$ .

定义映射 $\phi : M^0 \to (X / M)'$ 为

$$
\phi (f) = \hat {f}, \forall f \in M ^ {0},
$$

这里 $\hat{f}$ 由(6.3)式确定. 易见 $\phi$ 是线性的, 单射, 往证 $\phi$ 是满射. 对 $F \in (X / M)'$ , 定义

$$
f (x) = F ([ x ]), \forall x \in X.
$$

易见 $f$ 是线性的，而且

$$
\left| f (x) \right| = \left| F ([ x ]) \right| \leqslant \| F \| \| [ x ] \| \leqslant \| F \| \| x \|.
$$

可见 $f$ 是连续的，且 $\| f\| \leqslant \| F\|$ .当 $x\in M$ 时， $[x] = 0$ ，故

$$
f (x) = F ([ x ]) = 0.
$$

于是 $f \in M^0$ . 又由 $\hat{f}$ 定义可见 $\hat{f} = F$ , 即

$$
\phi (f) = F.
$$

于是 $\phi$ 是满射的，又由前述可见

$$
\| \hat {f} \| \leqslant \| f \| \leqslant \| F \| = \| \hat {f} \|.
$$

故 $\| \phi(f) \| = \|f\|$ , 即 $\phi$ 是保范的. 这说明 $M^0$ 与 $(X/M)'$ 保范同构, 当然, $(X/M)'$ 亦与 $M^0$ 保范同构. 证毕.

## § 7\* 序列弱收敛与序列弱\*收敛

## 1. 序列弱收敛与弱列紧性回顾古典的数学分析,许多基本定理都是关于 $\mathbf{R}^n$ 中有界闭集(即自列紧集)的.例如连续函数的基本性质,聚点原则等等.在第一章§7中,Riesz引理却告诉我们,任何无穷维的赋范线性空间的单位球都不可能是列紧的.因此,若只限于赋范线性空间上的范数拓扑,那么一系列古典的数学分析的技巧就都用不上、行不通了.

远在20世纪之初，Hilbert在研究积分方程时已经看到下面所谓弱收敛的概念了，并且反复使用一个他叫做“选择原理”的工具(参见[26]，第115页).用现在的术语，这个“原理”即下文的定理7.1.因此历史上弱收敛概念一出现便与弱列紧性密切地联系着.

定理7.1 对可分的Hilbert空间 $H$ 的闭单位球 $U$ 中任何点列 $\{x_{n}\}_{n = 1}^{\infty}$ ，总可以抽出一个子列 $\{x_{n_k}\}_{k = 1}^{\infty}$ ，及一点 $x_0\in U$ ，使

$$
\lim _ {k \rightarrow \infty} (x _ {n _ {k}}, y) = (x _ {0}, y), \forall y \in H.
$$

即所谓 $\{x_{n_k}\}_{k = 1}^{\infty}$ 弱收敛到 $x_0$

证根据第二章定理2.3的推论,每个可分的Hilbert空间都与 $l^{2}$ 同构,因此不妨设H即 $l^{2}$ .设

$$
\begin{array}{c} x _ {1} = \{\xi_ {1 1}, \xi_ {1 2}, \dots , \xi_ {1 j}, \dots \}, \\ x _ {2} = \{\xi_ {2 1}, \xi_ {2 2}, \dots , \xi_ {2 j}, \dots \}, \\ \dots \quad \dots \quad \dots \quad \dots \\ x _ {n} = \{\xi_ {n 1}, \xi_ {n 2}, \dots , \xi_ {n j}, \dots \}, \\ \dots \quad \dots \quad \dots \quad \dots \end{array}
$$

从 $\sum_{j=1}^{\infty} |\xi_{nj}|^2 = \| x_n \|^2 \leqslant 1$ ，可见

$$
\mid \xi_ {n j} \mid^ {2} \leqslant 1, \quad n, j = 1, 2, \dots .
$$

由对角线方法,有子序列

$$
x _ {n _ {k}} = \{\xi_ {n _ {k} 1}, \xi_ {n _ {k} 2}, \dots , \xi_ {n _ {k} j}, \dots \}, k = 1, 2, \dots .
$$

使对所有的 $j=1,2,\cdots,$

$$
\lim _ {k \rightarrow \infty} \xi_ {n _ {k} j} = \xi_ {j},
$$

存在.对任何正整数 N,

$$
\sum_ {j = 1} ^ {N} \mid \xi_ {n _ {k} j} \mid^ {2} \leqslant \| x _ {n _ {k}} \| ^ {2} \leqslant 1.
$$

令 $k \to \infty$ ，便有

$$
\sum_ {j = 1} ^ {N} \mid \xi_ {j} \mid^ {2} \leqslant 1.
$$

从而

$$
\sum_ {j = 1} ^ {\infty} | \xi_ {j} | ^ {2} \leqslant 1.
$$

即 $x_{0}=\{\xi_{1},\xi_{2},\cdots,\xi_{j},\cdots\}\in U.$

现在，对任何 $y=\{\eta_{1},\eta_{2},\cdots,\eta_{j},\cdots\}\in H$ ，

$$
\begin{array}{r l} & \left| \left(x _ {n _ {k}}, y\right) - \left(x _ {0}, y\right) \right| \\ & = \left| \left(x _ {n _ {k}} - x _ {0}, y\right) \right| \\ & = \left| \sum_ {j = 1} ^ {\infty} \left(\xi_ {n _ {k} j} - \xi_ {j}\right) \bar {\eta} _ {j} \right| \end{array}
$$

$$
\begin{array}{l} \leqslant \left| \sum_ {j = 1} ^ {N} (\xi_ {n _ {k} j} - \xi_ {j}) \overline {{\eta}} _ {j} \right| + \left| \sum_ {j = N + 1} ^ {\infty} \xi_ {n _ {k} j} \overline {{\eta}} _ {j} \right| + \left| \sum_ {j = N + 1} ^ {\infty} \xi_ {j} \overline {{\eta}} _ {j} \right| \\ \leqslant \sum_ {j = 1} ^ {N} | \xi_ {n _ {k} j} - \xi_ {j} | | \eta_ {j} | + (\sum_ {j = N + 1} ^ {\infty} | \xi_ {n _ {k} j} | ^ {2}) ^ {1 / 2} (\sum_ {j = N + 1} ^ {\infty} | \eta_ {j} | ^ {2}) ^ {1 / 2} \\ \quad + \left(\sum_ {j = N + 1} ^ {\infty} | \xi_ {j} | ^ {2}\right) ^ {1 / 2} (\sum_ {j = N + 1} ^ {\infty} | \eta_ {j} | ^ {2}) ^ {1 / 2} \\ \leqslant \sum_ {j = 1} ^ {N} | \xi_ {n _ {k} j} - \xi_ {j} | | \eta_ {j} | + 2 (\sum_ {j = N + 1} ^ {\infty} | \eta_ {j} | ^ {2}) ^ {1 / 2}. \end{array}
$$

注意，当 $N$ 充分大， $\sum_{j = N + 1}^{\infty}\mid \eta_j\mid^2$ 可任意小，而对固定的 $N$ ，显然

$$
\lim _ {k \rightarrow \infty} \sum_ {j = 1} ^ {N} | \xi_ {n _ {k} j} - \xi_ {j} | | \eta_ {j} | = 0.
$$

证毕.

正是由于这个定理人们有了下面概念.

定义7.1 设 $H$ 是Hilbert空间， $\{x_{n}\}_{n=1}^{\infty} \subset H$ 。如果存在 $x_{0} \in H$ ，对任何 $y \in H$ ，都有

$$
\lim _ {n \rightarrow \infty} (x _ {n}, y) = (x _ {0}, y),
$$

则称 $\{x_{n}\}_{n = 1}^{\infty}$ 弱收敛到 $x_0$ .记作 $x_{n}\xrightarrow{w}x_{0}$

设 $J$ 是 $H$ 上的泛函，若对任意的 $\{x_{n}\}_{n = 1}^{\infty}\subset H,x_{n}\xrightarrow{w}x_{0}$ ，必有 $J(x_{n})\to J(x_{0})$ ，当 $n\to \infty$ ，称泛函 $J$ 是序列弱连续的.

例1 设 $J(u)$ 是可分Hilbert空间 $H$ 中有界的、弱序列闭的点集 $\mathcal{R}$ 上的序列弱连续的实值泛函. 如果有 $\{u_n\}_{n=1}^{\infty} \subset \mathcal{R}$ , 使

$$
J (u _ {n}) \to \inf _ {u \in \mathcal {R}} J (u)  ,   \text {当} n \to \infty  .
$$

因为 $\mathcal{R}$ 是有界的弱序列闭的，根据定理7.1，应有 $\{u_n\}_{n=1}^{\infty}$ 的子序列 $\{u_{n_k}\}_{k=1}^{\infty}$ 弱收敛到某点 $w \in \mathcal{R}$ . 从 $J(u)$ 的序列弱连续性，应有

$$
J (u _ {n _ {k}} \cdot) \rightarrow J (w), k \rightarrow \infty .
$$

故

$$
J (\omega) = \inf _ {u \in \mathcal {R}} J (u),
$$

即 $J(u)$ 在 $\mathcal{R}$ 上达到最小值.

很有意思, Hilbert 早在 1909 年便已看到序列弱收敛性的这个重要推论. 他说: “无穷多个变量的连续(按: 即序列弱连续)函数必定有一个极小值, 这个命题由于其普遍性及精确性可以代替 Dirichlet 原理.” (参见[1], 第 134 页)

对一般的Banach空间我们有如下概念.

定义 7.2 设 X 是 Banach 空间, $\{x_{n}\}_{n=1}^{\infty} \subset X, x_{0} \in X$ . 如果对任何 $f \in X'$ , 都有

$$
\lim _ {n \rightarrow \infty} f (x _ {n}) = f (x _ {0}).
$$

则称序列 $\{x_{n}\}_{n = 1}^{\infty}$ 弱收敛到 $x_0$ ，记作 $x_{n}\xrightarrow{w} x_{0}$

定义7.3 如果Banach空间之子集 $A$ 中的任何序列都有弱收敛的子序列，则称 $A$ 为弱列紧的.

命题7.1 设 $X$ 是Banach空间， $\{x_{n}\}_{n = 1}^{\infty}\subset X,x_{0}\in X.$ 则 $x_{n}\xrightarrow{w}x_{0}\Leftrightarrow$

(1) $\{\| x_n\| \}_{n = 1}^{\infty}$ 有界，

(2) 存在 $X'$ 中一个稠密子集 $M'$ , 使

$$
\lim _ {n \to \infty} f (x _ {n}) = f (x _ {0}), \text {当} f \in M ^ {\prime}.
$$

证先证 $\Leftarrow$ 。由(1)，存在常数 $K > 0$ 。使 $\| x_n \| \leqslant K, n = 0, 1, 2, \cdots$ 。因为 $M'$ 在 $X'$ 中稠密，于是对任何 $f \in X'$ ，及任意 $\varepsilon > 0$ ，有 $f_{\varepsilon} \in M'$ ，使

$$
\| f - f _ {\varepsilon} \| <   \varepsilon .
$$

从而

$$
\begin{array}{r l} | f (x _ {n}) - f (x _ {0}) | & \leqslant | f (x _ {n}) - f _ {\varepsilon} (x _ {n}) | + | f _ {\varepsilon} (x _ {n}) - f _ {\varepsilon} (x _ {0}) | + | f _ {\varepsilon} (x _ {0}) - f (x _ {0}) | \\ & \leqslant \| f - f _ {\varepsilon} \| \| x _ {n} \| + | f _ {\varepsilon} (x _ {n}) - f _ {\varepsilon} (x _ {0}) | + \| f - f _ {\varepsilon} \| \| x _ {0} \| \\ & \leqslant 2 K \varepsilon + | f _ {\varepsilon} (x _ {n}) - f _ {\varepsilon} (x _ {0}) |. \end{array}
$$

又根据假设(2)可见

$$
\lim _ {n \rightarrow \infty} f (x _ {n}) = f (x _ {0}).
$$

至于 $\Rightarrow$ .由假设，对任何 $f\in X^{\prime}$ ，存在常数 $M > 0$ ，使

$$
\sup _ {n} | f (x _ {n}) | \leqslant M.
$$

又根据命题4.2，

$$
\sup _ {n} \| x _ {n} \| <   \infty ,
$$

即(1)成立,而(2)则是显然的.证毕.

命题7.2 若 $X$ 是Banach空间， $\{x_{n}\}_{n=1}^{\infty} \subset X, x_{0} \in X.$ 如果 $x_{n} \xrightarrow{w} x_{0}$ ，则有凸组合

$$
\sum_ {j = 1} ^ {N _ {n}} \lambda_ {n j} x _ {j} \rightarrow x _ {0}, n \rightarrow \infty .
$$

这里 $\lambda_{nj} \geqslant 0, j = 1, \cdots, N_{n}$ ，且 $\sum_{j=1}^{N_{n}} \lambda_{nj} = 1$ .

证取 $E$ 为 $\{x_{n}\}_{n = 1}^{\infty}$ 张开的凸闭集, 根据定理2.7, $E$ 是弱序列闭的. 因 $x_{n} \xrightarrow{w} x_{0}$ , 故 $x_{0} \in E$ . 证毕.

定理 7.2 (Pettis,1938) 自反空间 X 的单位球是弱列紧的.

证设 $\{y_{n}\}_{n=1}^{\infty}$ 是 $X$ 的单位球 $U$ 中的序列, $Y$ 是 $\{y_{n}\}_{n=1}^{\infty}$ 张成的子空间, 则 $Y$ 是可分的. 根据定理 4.9, $Y$ 也是自反的. 因典型映射 $\tau$ 是等距同构, 故 $Y'' = \tau(Y)$ 是可分的. 由定理 4.1, $Y'$ 也是可分的.

设 $\left\{y_{k}^{\prime}\right\}_{k=1}^{\infty}$ 在 $Y^{\prime}$ 中稠密.对每个固定的k,数列 $\left\{y_{k}^{\prime}(y_{n})\right\}_{n=1}^{\infty}$ 是有界的.考虑数集 $\left\{y_{k}^{\prime}(y_{n})\right\}_{k,n=1}^{\infty}$ ,用对角线方法可抽出 $\left\{y_{n}\right\}_{n=1}^{\infty}$ 的子序列 $\left\{y_{n_{j}}\right\}_{j=1}^{\infty}$ ,使得对任意正整数k, $\left\{y_{k}^{\prime}(y_{n_{j}})\right\}_{j=1}^{\infty}$ 是收敛的.取 $x_{j}=y_{n_{j}},j=1,2,\cdots$ .这样我们得到 $\left\{y_{n}\right\}_{n=1}^{\infty}$ 的一个子序列 $\left\{x_{j}\right\}_{j=1}^{\infty}$ ,对每个 $k=1,2,\cdots.\lim_{i\to\infty}y_{k}^{\prime}(x_{j})$ 存在(且有限).

考察典型映射 $\tau: Y \to Y'', \tau(x_j) = x'_j$ :

$$
x _ {j} ^ {\prime \prime} (y ^ {\prime}) = y ^ {\prime} (x _ {j}), \text {当} y ^ {\prime} \in Y ^ {\prime}.
$$

由前段， $\lim_{j\to\infty}x_{j}^{\prime\prime}(y_{k}^{\prime})$ 存在，而 $\left\{y_{k}^{\prime}\right\}_{k=1}^{\infty}$ 在 $Y^{\prime}$ 中稠密，而且 $\|x_{j}^{\prime\prime}\|=\|x_{j}\|\leqslant1$ ， $j=1,2,\cdots$ 。于是对每个 $y^{\prime}\in Y^{\prime}$ ，可知 $\lim_{n\to\infty}x_{j}^{\prime\prime}(y^{\prime})$ 存在。定义

$$
y _ {0} ^ {\prime \prime} (y ^ {\prime}) = \lim _ {j \to \infty} x _ {j} ^ {\prime \prime} (y ^ {\prime}), \text {当} y ^ {\prime} \in Y ^ {\prime}.
$$

易证 $y''_0 \in Y''$ . 因 $Y$ 是自反的, 存在 $y_0 \in Y$ , 使

$$
y _ {0} ^ {\prime \prime} (y ^ {\prime}) = y ^ {\prime} (y _ {0}), \text {当} y ^ {\prime} \in Y ^ {\prime}.
$$

于是

$$
\lim _ {j \to \infty} y ^ {\prime} (x _ {j}) = y ^ {\prime} (y _ {0}), \text {当} y ^ {\prime} \in Y ^ {\prime}.
$$

现在，对任何 $x^{\prime}\in X^{\prime}$ ，令 $x_{Y}^{\prime}$ 表示 $x^\prime$ 在 $Y$ 上限制，则 $x_{Y}^{\prime}\in Y^{\prime}$ ，且

$$
x ^ {\prime} (y) = x _ {Y} ^ {\prime} (y), \text {当} y \in Y.
$$

于是由 $\{x_{j}\}_{j = 1}^{\infty}\subset Y,y_{0}\in Y$ 可见，对任何 $x^{\prime}\in X^{\prime}$

$$
\lim _ {j \rightarrow \infty} x ^ {\prime} (x _ {j}) = \lim _ {j \rightarrow \infty} x _ {Y} ^ {\prime} (x _ {j}) = x _ {Y} ^ {\prime} (y _ {0}) = x ^ {\prime} (y _ {0}).
$$

即 $\{x_{j}\}_{j = 1}^{\infty}$ 弱收敛到 $y_0$ .证毕.

## 2. 序列弱\*收敛与弱\*列紧性定义7.4 对Banach空间 $X$ ，设 $\{f_n\}_{n = 1}^{\infty}\subset X_{\bullet}^{\prime},f\in X^{\prime}$ .如果对任何 $x\in X$ 都有

$$
\lim _ {n \rightarrow \infty} f _ {n} (x) = f (x),
$$

则称序列 $\{f_n\}_{n=1}^{\infty}$ 弱\*收敛到 $f$ , 记作 $f_n \xrightarrow{w^*} f$ .

命题7.3 对Banach空间 $X$ ，设 $\{f_n\}_{n = 1}^{\infty}\subset X',f\in X'$ ，则

$f_{n}\xrightarrow{w^{*}}f\quad \Leftrightarrow (\mathrm{i})\{\| f_{n}\| |_{n = 1}^{\infty}\text{有界.}$

(ii) 存在 $X$ 中稠密子集 $M$ , 使

$$
\lim _ {n \to \infty} f _ {n} (x) = f (x), \text {当} x \in M.
$$

证明大体如命题 7.1, 故从略. 读者可作为习题自己完成.

定义 7.5 设 X 为 Banach 空间, 点集 $A \subset X'$ . 如果 A 中任何序列都有弱\*收敛的子序列, 则称 A 是弱\*列紧的.

定理 7.3 设 X 是可分的 Banach 空间, 则 $X'$ 中的单位球 U 是弱 \* 列紧的.

证因为 $X$ 是可分的, 所以 $X$ 有可数的稠密子集 $\{x_m\}_{m=1}^{\infty}$ . 设 $\{f_n\}_{n=1}^{\infty}$ 是 $U$ 中序列, 则对每个固定的 $m$ , $\{f_n(x_m)\}_{n=1}^{\infty}$ 是有界数列. 考察数集 $\{f_n(x_m)\}_{n,m=1}^{\infty}$ , 用对角线方法可以抽出 $\{f_n\}_{n=1}^{\infty}$ 的子序列 $\{f_{n_k}\}_{k=1}^{\infty}$ , 使得对任何正整数 $m$ , $\{f_{n_k}(x_m)\}_{k=1}^{\infty}$ 都是收敛数列. 再由 $\{x_m\}_{m=1}^{\infty}$ 在 $X$ 中稠密, $\{\|f_{n_k}\|\}_{k=1}^{\infty}$ 有界, 可见对任何 $x \in X$ , 数列 $\{f_{n_k}(x)\}_{k=1}^{\infty}$ 都收敛. 定义

$$
f (x) = \lim _ {k \to \infty} f _ {n _ {k}} (x), \text {当} x \in X.
$$

易证 $f \in X'$ . 故 $f_{n_k} \xrightarrow{w^*} f$ . 证毕.

这个定理已见于 Banach 的名著(见第一章 §7 末)中第 123 页. 当时没有一般拓扑的工具, 而且弱拓扑也刚被引进, 还未被人们熟悉. 一旦有了这些准备知识, 便不需要可分性的假设, 而有定理 7.4(Alaoglu,1940) 设 X 是 Banach 空间, 则 $X'$ 中的闭单位球是弱\*紧的.

这个定理的证明可参见[39], 定理 IV.21.

## 3. Banach 空间上的逼近问题定理7.5 设 $F$ 是自反Banach空间 $X$ 中非空的弱序列闭的子集. 则于任何的 $x_0 \in X \setminus F$ , 必有 $y_0 \in F$ , 使

$$
\left\| x _ {0} - y _ {0} \right\| = \inf _ {y \in F} \left\| x _ {0} - y \right\|.
$$

一般称 $y_0$ 为 $x_0$ 在 $F$ 上的最佳逼近元.

证记 $m = \inf_{n\in F}\| x_0 - y\|$ .由下确界定义，存在元列 $\{x_n\}_{n = 1}^{\infty}\subset F$ ，使

$$
\lim _ {n \rightarrow \infty} \| x _ {0} - x _ {n} \| = m. \bullet
$$

显然 $\{x_{n}\}_{n = 1}^{\infty}$ 是有界集.从定理7.2，存在 $\{x_{n}\}_{n = 1}^{\infty}$ 的子序列 $\{x_{n_j}\}_{j = 1}^{\infty}$ 弱收敛于某个元 $y_0$ ，因为 $F$ 是弱序列闭的，故 $y_0\in F$

设 $f \in X'$ , $\| f \| \leqslant 1$ , 则

$$
f (x _ {0} - y _ {0}) = \lim _ {j \rightarrow \infty} f (x _ {0} - x _ {n _ {j}}).
$$

从而

$$
\begin{array}{r l}\mid f (x _ {0} - y _ {0}) \mid =&\lim _ {j \rightarrow \infty} \mid f (x _ {0} - x _ {n _ {j}}) \mid\\&\leqslant \lim _ {j \rightarrow \infty} \| f \| \| x _ {0} - x _ {n _ {j}} \| \leqslant m.\end{array}
$$

由典型映射的性质，

$$
\| x _ {0} - y _ {0} \| = \sup _ {\| f \| \leqslant 1} | f (x _ {0} - y _ {0}) | \leqslant m.
$$

另外，由 $m$ 定义，显然 $\| x_0 - y_0\| \geqslant m$ .总之

$$
\| x _ {0} - y _ {0} \| = m = \inf _ {y \in F} \| x _ {0} - y \|.
$$

证毕.

根据定理 2.7, 每个凸闭集都是弱序列闭的. 所以定理 7.5 也可改写成定理 7.5 设 F 是自反 Banach 空间 X 中非空的凸闭集, 则于任何 $x_{0} \in X \setminus F$ , 必有 $y_{0} \in F$ , 使

$$
\| x _ {0} - y _ {0} \| = \inf _ {y \in F} \| x _ {0} - y \|.
$$

定义7.6 设 $< X, \| \cdot \| >$ 是Banach空间，如果对任何 $x, y \in X, x \neq y$ ， $\| x \| = \| y \| = 1$ ，恒有

$$
\parallel \alpha x + (1 - \alpha) y \parallel <   1, \text {当} 0 <   \alpha <   1.
$$

则称 Banach 空间 $< X, \| \cdot \|$ > 为严格凸的.

命题7.4 对Banach空间 $< X, \| \cdot \| >$ ，如果于任何非零的 $x, y \in X, x \neq y$ ，从 $\| x + y \| = \| x \| + \| y \|$ 恒有 $c > 0$ . 使 $x = cy$ ，则 $< X, \| \cdot \| >$ 是严格凸的.

证设 $x, y \in X, x \neq y$ ，且 $\|x\| = \|y\| = 1$ ，则于任何 $c > 0$ 及 $\alpha \in (0,1)$ ，都有

$$
\alpha x \neq c (1 - \alpha) y.
$$

否则，

$$
\alpha x = c (1 - \alpha) y,
$$

两边取范数得 $\alpha = c(1 - \alpha)$ ，与 $x \neq y$ 矛盾。由命题假设必有

$$
\| \alpha x + (1 - \alpha) y \| <   \| \alpha x \| + \| (1 - \alpha) y \| = 1, \text {当} 0 <   \alpha <   1.
$$

故 $<X,\|\cdot\|>$ 是严格凸的.

推论 $L^p [a,b](p > 1)$ 是严格凸的.

根据命题 7.4, 以及关于 Minkowski 不等式的讨论可得. (参见[7], 第 6 章, §1.)

定理7.6 在严格凸的自反Banach空间 $X$ 中， $x_0 \in X$ 在非空的凸闭集 $F \subset X$ 上恰有一个最佳逼近元.

证首先, 由定理 $7.5'$ , $x_0$ 在 $F$ 上有一个最佳逼近元. 如果 $x_0$ 在 $F$ 上有两个最佳逼近元 $u_1$ 与 $u_2$ . 即

$$
\| x _ {0} - u _ {1} \| = \| x _ {0} - u _ {2} \| = m = \inf _ {y \in F} \| x _ {0} - y \|.
$$

则于 $u = \frac{u_1 + u_2}{2} \in F$ ，从

$$
m \leqslant \| x _ {0} - u \| \leqslant \frac {\| x _ {0} - u _ {1} \|}{2} + \frac {\| x _ {0} - u _ {2} \|}{2} = m.
$$

可见 $\| x_0 - u\| = m$ ，从而

$$
\left\| \left(x _ {0} - u _ {1}\right) + \left(x _ {0} - u _ {2}\right) \right\| = \left\| 2 \left(x _ {0} - u\right) \right\| = 2 \| x _ {0} - u \| = 2 m.
$$

不妨设 $m > 0$ ，则

$$
\left\| \frac {\left(x _ {0} - u _ {1}\right) + \left(x _ {0} - u _ {2}\right)}{2} \right\| = m > 0.\tag{7.1}
$$

如果 $u_{1} \neq u_{2}$ , 则 $(x_{0} - u_{1}) / m \neq (x_{0} - u_{2}) / m$ , 由 $X$ 的严格凸性,

$$
\left\| \frac {1}{2} \left(\frac {x _ {0} - u _ {1}}{m} + \frac {x _ {0} - u _ {2}}{m}\right) \right\| <   1,
$$

即

$$
\left\| \frac {\left(x _ {0} - u _ {1}\right) + \left(x _ {0} - u _ {2}\right)}{2} \right\| <   m.
$$

与(7.1)矛盾.证毕.

定义7.7 设 $J(x)$ 是赋范线性空间 $X$ 上的泛函(不必线性), 如果任给 $x_{n} \xrightarrow{w} x_{0}$ 及 $\varepsilon > 0$ , 存在正整数 $N$ , 使当 $n > N$ 时,

$$
J (x _ {n}) > J (x _ {0}) - \varepsilon .
$$

则称 $J(x)$ 是下半弱连续的.

例 2 对 Banach 空间 <X, ||·|| >, $y_{0} \in X$ , 函数

$$
J (x) = \parallel x - y _ {0} \parallel , x \in X,
$$

是下半弱连续的.

事实上,如果 $x_{n} \xrightarrow{w} x_{0}$ 及 $\varepsilon > 0$ ,由于

$$
\| x _ {0} - y _ {0} \| = \sup _ {\| f \| \leqslant 1} | f (x _ {0} - y _ {0}) |,
$$

存在 $f_{\varepsilon} \in X'$ , $\| f_{\varepsilon} \| \leqslant 1$ , 使

$$
\left| f _ {\epsilon} \left(x _ {0} - y _ {0}\right) \right| > \left\| x _ {0} - y _ {0} \right\| - \frac {\varepsilon}{2}.
$$

而 $x_{n}\xrightarrow{w} x_{0}$ ，从而 $x_{n} - y_{0}\xrightarrow{w} x_{0} - y_{0}$ ，故

$$
\lim _ {n \rightarrow \infty} f _ {\varepsilon} (x _ {n} - y _ {0}) = f _ {\varepsilon} (x _ {0} - y _ {0}).
$$

于是存在正整数 N，使当 n > N 时，

$$
\left| f _ {\epsilon} \left(x _ {n} - y _ {0}\right) \right| > \left| f _ {\epsilon} \left(x _ {0} - y _ {0}\right) \right| - \frac {\varepsilon}{2}.
$$

则

$$
\left| f _ {\varepsilon} \left(x _ {n} - y _ {0}\right) \right| > \left\| x _ {0} - y _ {0} \right\| - \varepsilon .
$$

因 $\| f_{\epsilon}\| \leqslant 1$ ，所以

$$
\| x _ {n} - y _ {0} \| \geqslant | f _ {\varepsilon} (x _ {n} - y _ {0}) | > \| x _ {0} - y _ {0} \| - \varepsilon .
$$

即

$$
J (x _ {n}) > J (x _ {0}) - \varepsilon .
$$

这就说明 $J(x)$ 是下半弱连续的.

定理7.7 设 $J(x)$ 在自反Banach空间 $X$ 的凸闭集 $K$ 上是下半弱连续的. 若存在有界序列 $\{x_{n}\}_{n=1}^{\infty} \subset K$ , 使

$$
J (x _ {n}) \rightarrow \inf _ {x \in K} J (x),\tag{7.2}
$$

则 $J(x)$ 在 K 上达到极小值.

证由于 $X$ 是自反的， $\{x_{n}\}_{n=1}^{\infty}$ 有界，根据定理7.2， $\{x_{n}\}_{n=1}^{\infty}$ 有弱收敛子列。不妨设 $x_{n} \xrightarrow{w} x_{0}$ ，从定理2.7可知， $x_{0} \in K$ 。

因为 $J(x)$ 是下半弱连续的，所以任给 $\varepsilon > 0$ ，存在正整数 $N$ ，使当 $n > N$ 时，

$$
J (x _ {n}) > J (x _ {0}) - \varepsilon .
$$

从而由(7.2)可知

$$
\inf _ {x \in K} J (x) = \lim _ {n \rightarrow \infty} J (x _ {n}) \geqslant J (x _ {0}).
$$

故

$$
J (x _ {0}) = \inf _ {x \in K} J (x).
$$

证毕.

值得注意的是在控制理论等实际问题中,性能指标往往是下半连续的非线性泛函.

## § 8\* 弱拓扑

## 1. Banach 空间上弱拓扑历史上,从 Hilbert, F. Riesz 到 Banach 所研究的都是序列弱收敛. 弱收敛是 Banach 名著(见第一章 §7 末)的中心,正如 W. Rudin 所说,这肯定是 Banach 对泛函分析最重要的贡献之一.但若只限于序列弱收敛,即使把集合的所有弱收敛子序列的极限都添加上去也并不导致弱序列闭集.以致 Banach 被迫引入诸如超穷闭包等复杂的概念.其实,当时(1930 年)von Neumann 所引入的弱邻域概念却是非常简单明了而且极便于应用的.(参见[40],第 373 页)

定义8.1 设 $X$ 为Banach空间, $X'$ 为 $X$ 的对偶空间. $X$ 在点0的弱邻域基定义为所有形如下述的点集:

$$
N \left(x _ {1} ^ {\prime}, \dots , x _ {n} ^ {\prime}; \varepsilon\right) = \{x \in X: | x _ {j} ^ {\prime} (x) | <   \varepsilon_ {j}, j = 1, \dots , n \},
$$

这里 $n \in N, x_{j}^{\prime} \in X^{\prime}, \varepsilon = (\varepsilon_{1}, \cdots, \varepsilon_{n}), \varepsilon_{j} > 0, j = 1, \cdots, n$ ，都是任意给定的。

对 $x_0 \in X$ ，所有如下形式的点集：

$$
x _ {0} + N \left(x _ {1} ^ {\prime}, \dots , x _ {n} ^ {\prime}; \varepsilon\right) = \left\{x \in X: \left| x _ {j} ^ {\prime} \left(x - x _ {0}\right) \right| <   \varepsilon_ {j}, j = 1, \dots , n \right\},
$$

定义为在点 $x_0$ 的弱邻域基.

设 $G \subset X$ , 如果对任何 $x \in G$ , 都存在 $x$ 的弱邻域基中的 $V$ , 使得 $V \subset G$ , 则称 $G$ 为弱开集. 由弱开集生成之 $X$ 上的拓扑便称为 Banach 空间 $X$ 上的弱拓扑.

设 $\{x_{n}\}_{n = 1}^{\infty}\subset X,x_{0}\in X.$ 如果对 $x_0$ 的任何弱邻域 $V$ ，总存在正整数 $N$ ，使当 $n\geqslant N$ 时， $x_{n}\in V$ ，则称 $\{x_{n}\}_{n = 1}^{\infty}$ 按弱拓扑收敛到 $x_0$

容易证明：

序列 $\{x_{n}\}_{n = 1}^{\infty}\subset X$ 按弱拓扑收敛到 $x_0\Leftrightarrow x_n\xrightarrow{w}x_0$

例 1 （von Neumann, 1930） 存在 $l^{2}$ 中的点集 A，使点 0 是 A 的弱聚点，即弱拓扑下的聚点，但是没有 A 中的序列能弱收敛到 0.

von Neumann 曾考察 $t^{2}$ 中如下点集 A:

$$
\begin{array}{r l} & {x _ {1 2} = \left\{1, 1, 0, 0, \dots \right\},} \\ & {x _ {1 3} = \left\{1, 0, 1, 0, \dots \right\},} \\ & {\qquad \dots ,} \\ & {x _ {1 n} = \left\{1, 0, \dots , 0, 1, 0, \dots \right\},} \\ & {\qquad \dots} \\ & {x _ {2 3} = \left\{0, 1, 2, 0, \dots \right\},} \\ & {x _ {2 4} = \left\{0, 1, 0, 2, 0, \dots \right\},} \\ & {\qquad \dots ,} \\ & {x _ {2 n} = \left\{0, 1, \dots , 0, 2, 0, \dots \right\},} \\ & {\qquad \dots} \\ & {\qquad \dots \dots .} \\ & {x _ {n - 1, n} = \left\{0, \dots , 0, 1, n - 1, 0, 0, \dots \right\},} \\ & {x _ {n - 1, n + 1} = \left\{0, \dots , 0, 1, 0, n - 1, 0, \dots \right\},} \\ & {\qquad \dots ,} \\ & {\qquad \dots \dots .} \end{array}
$$

这里点 $x_{kn} (k < n)$ 只有第 $k$ 个坐标为 1, 第 $n$ 个坐标为 $k$ , 而其他坐标都为 0.

关于点集 A，首先点 $0 = \{0, 0, \cdots\}$ 是 A 的弱聚点。因为对任意给定的 $y = \{\eta_{1}, \eta_{2}, \cdots\} \in t^{2}$ ，及 $\varepsilon > 0$ ，适当选取 k 与 n 便有

$$
\left| \left(x _ {k n}, y\right) \right| = \left| \eta_ {k} + k \eta_ {n} \right| <   \epsilon .
$$

但是 $A$ 中任何序列 $\{z_j\}_{j=1}^{\infty}$ 都不能弱收敛到 0. 因为若 $\{z_j\}_{j=1}^{\infty}$ 弱收敛, 由命题 7.1, $\{\|z_j\|_{j=1}^{\infty}$ 有界. 于是 $\{z_j\}_{j=1}^{\infty}$ 只能是集合 $A$ 中前有限行挑出来的, 从而必有无限多个 $z_j$ 出现在同一行中. 这显然不弱收敛到 0. (例如, 有无限多个 $z_j$ 出现在第 5 行, 则这无限多个 $z_j$ 的第 5 坐标都为 1, 不可能趋于 0.)

熟知距离空间中的点 x 是点集 M 的聚点必须存在 M 中的点列 $\left\{x_{n}\right\}_{n=1}^{\infty}$ ， $x_{n} \neq x, n = 1, 2, \cdots$ ，使 $x_{n} \rightarrow x$ 。所以上述的例子表明弱拓扑空间不可能是距离空间。

设 $\ell(x)$ 是 Banach 空间 X 上的连续线性泛函. 显然

$$
p _ {t} (x) = | t (x) |
$$

就是 $X$ 上的一个半范数（见第一章，§8），且由Hahn-Banach定理可知， $\{p_{i}: t \in X'\}$ 分离 $X$ 的点.

推广弱拓扑的意思, 设 $\left\{\rho_{a}\right\}_{a\in\mathcal{A}}$ 是线性空间 X 上一族分离点的半范数, 以所有形如

$$
N \left(\alpha_ {1}, \dots , \alpha_ {n}; \varepsilon\right) = \{x \in X: \rho_ {\alpha_ {i}} (x) <   \varepsilon , j = 1, \dots , n \}
$$

的集合作为点0的邻域基，而以所有形如

$$
x _ {0} + N \left(\alpha_ {1}, \dots , \alpha_ {n}; \varepsilon\right) = \{x \in X: \rho_ {\alpha_ {i}} \left(x - x _ {0}\right) <   \varepsilon , j = 1, \dots , n \}
$$

的集合作为点 $x_0$ 的邻域基，这里 $n \in \mathbf{N}, \varepsilon > 0, \alpha_j \in \mathcal{A}, j = 1, \cdots, n$ ，是任意给定的，这样就由 $\{\rho_\alpha\}_{\alpha \in \mathcal{A}}$ 诱导了 $X$ 上一个拓扑.

不难验证,线性运算

$$
(x, y) \rightarrow x + y, (\lambda , x) \rightarrow \lambda x, x, y \in X, \lambda \in \mathbf {C}.
$$

按这个拓扑是连续的. 因此, 一般称如此的拓扑空间为拓扑线性空间.

我们在第三章，§2中已经讲过凸的，平衡的，吸收的点集的概念. 易见任何 $N(\alpha_{1}, \cdots, \alpha_{n}; \varepsilon)$ 及 $x_{0} + N(\alpha_{1}, \cdots, \alpha_{n}; \varepsilon)$ 都是凸的，平衡的，吸收的点集. 这就导致我们引进下列重要空间.

定义8.2 由一个分离点的半范数族 $\{\rho_{\alpha}\}_{\alpha \in \mathcal{A}}$ 所诱导的拓扑线性空间称为局部凸的拓扑线性空间.

在20世纪40年代中期以前，泛函分析学家的兴趣几乎集中在赋范线性空间.最早关于局部凸的拓扑线性空间的理论大约是J.Dieudonné和L.Schwartz在1949年的工作.它的一个主要推动力是分布理论.(引自[40],第373页)

定理8.1 设 $M$ 是局部凸的拓扑线性空间 $X$ 中的凸闭集, 若 $0 \in M$ 且 $x_0 \notin M$ , 则有 $X$ 上的连续实线性泛函 $f$ , 使

$$
f (x _ {0}) > 1, \text {且} f (x) \leqslant 1, \text {当} x \in M.
$$

证明与定理 2.5 相似,读者可以作为习题自己完成.

推论凡局部凸的非零的拓扑线性空间上都存在非零的连续线性泛函.

## 2. Fréchet 空间在第一章 §8 中, 我们讲到 $F-$ 空间, 许多作者都称 $F-$ 空间为 Fréchet 空间, 但本书将采用下列定义.

定义 8.3 凡局部凸的 F-空间都称为 Fréchet 空间.

这大约是 N. Bourbaki 首先采用的术语. 为什么要用这个术语? 因为有了局部凸性, 从定理8.1的推论便可保证一切非零的Fréchet空间上都存在非零的连续线性泛函. 事实上, §2中曾指出, $F-$ 空间 $S[0,1]$ 上竟没有非零的连续线性泛函, 对于这样的空间根本就谈不上对偶理论了.

在第一章 §8 中, 我们曾经通过可数多个半范数定义出空间 $\mathcal{C}(\Omega), \mathcal{C}^m(\Omega)$ 及 $\mathcal{S}(\mathbf{R}^n)$ , 它们都来源于分布理论, 在偏微分方程理论, Fourier 变换理论和量子力学上分别起到重要作用. 我们已经证明它们都是 $F-$ 空间. 既然它们都是由一族半范数生成的, 所以还都是局部凸的, 从而它们都是 Fréchet 空间.

应该指出, Fréchet 空间是性质最整齐且最常用的一类局部凸的拓扑线性空间, 几乎所有关于 Banach 空间的基本原理, 例如开映射定理, 逆算子定理, 闭图形定理, Hahn-Banach 定理, 一致有界原理等等在 Fréchet 空间上也都是成立的. (参见 [39], § V.2 和 [9], § II.5)

## 习题

1. 设无穷矩阵 $(a_{ij})_{i,j=1}^{\infty}$ 满足

$$
\sup _ {i} \left(\sum_ {j = 1} ^ {\infty} \mid a _ {i j} \mid\right) <   \infty .
$$

由它定义的线性算子 $T:y = Tx$ 为

$$
\eta_ {i} = \sum_ {j = 1} ^ {\infty} a _ {i j} \xi_ {j}, i = 1, 2, \dots ,
$$

其中 $x=\{\xi_{1},\xi_{2},\cdots,\xi_{n},\cdots\}=\{\xi_{n}\},y=\{\eta_{1},\eta_{2},\cdots,\eta_{n},\cdots\}=\{\eta_{n}\}$

试证明 $T$ 是从 $(m)$ 到自身的有界线性算子，且

$$
\| T \| = \sup _ {i} \left(\sum_ {j = 1} ^ {\infty} | a _ {i j} |\right).
$$

2. 设数列 $\{\alpha_{n}\}_{n=1}^{\infty}$ 有界. 在 $l^{1}$ 中定义线性算子

$$
y = T x: \eta_ {n} = \alpha_ {n} \xi_ {n}, \quad n = 1, 2, \dots ,
$$

其中 $x = \{\xi_n\}, y = \{\eta_n\}$ .

试证明 $T$ 是从 $\ell^1$ 到自身的有界线性算子，且

$$
\| T \| = \sup _ {n} | \alpha_ {n} |.
$$

3. 证明上题中算子 $T$ 是有界可逆的当且仅当

$$
\inf _ {n} | \alpha_ {n} | > 0.
$$

4. 设无穷矩阵 $(a_{ij})_{i,j=1}^{\infty}$ 满足

$$
\sum_ {i = 1} ^ {\infty} \left(\sum_ {j = 1} ^ {\infty} | a _ {i j} | ^ {q}\right) <   \infty .
$$

由它定义的算子 $T$ 为

$$
y = T x: \eta_ {i} = \sum_ {j = 1} ^ {\infty} a _ {i j} \xi_ {j}, i = 1, 2, \dots ,
$$

其中 $x = \{\xi_n\}, y = \{\eta_n\}$ .

证明 $T$ 是从 $\ell^p$ 到 $\ell^q$ 的有界线性算子，这里 $1 < p, q < \infty$ ，且 $\frac{1}{p} + \frac{1}{q} = 1$ .

5. 设 $X$ 是 Banach 空间, $A, B \in L(X)$ . 如果 $A, B$ 都是有界可逆的, 则 $AB$ 也是有界可逆的, 且

$$
(A B) ^ {- 1} = B ^ {- 1} A ^ {- 1}.
$$

6. 设 $X, Y$ 都是赋范线性空间, $T$ 是从 $X$ 到 $Y$ 之线性算子. 试证明, 如果 $T$ 是有界的, 则 $T$ 之零空间 $N(T)$ 是闭的.

反之，当 $N(T)$ 是闭的时， $T$ 一定有界吗？

7. 设 $X$ 是赋范线性空间, $x, y \in X$ . 如果对 $X$ 上任何连续线性泛函 $f$ , 都有 $f(x) = f(y)$ , 则 $x = y$ .

8. 设 $X$ 是 Banach 空间, 试证明, 对任给的 $x \in X$ ,

$$
\| x \| = \sup \left\{\mid f (x) \mid : f \in X ^ {\prime}, \| f \| \leqslant 1 \right\}.
$$

9. 设 $p(x)$ 是赋范线性空间 $X$ 上次可加, 正齐次实值泛函, 即对任意的 $x$ , $y \in X, \alpha \in \mathbf{C}$ ,

$$
\begin{array}{c} p (x + y) \leqslant p (x) + p (y), \\ p (a x) = | a | p (x). \end{array}
$$

如果 $p(x)$ 在 $x = 0$ 处连续，则 $p(x)$ 在 $X$ 中每点都连续.试证明之.

10. 设 $p(x)$ 是线性空间 $X$ 上的半范数, 则 $\{x: p(x) < r\} (r > 0)$ 是个凸集, 而且是平衡的, 吸收的.

11. 试证明凸集的闭包是凸的, 平衡集的闭包是平衡的, 吸收集的闭包是吸收的.

12. 试求出 $L^1 [a,b]$ 上有界线性泛函的一般形式.

13. 试利用一致有界原理证明 Hellinger-Toeplitz 定理(即命题 3.5).

14. 设 $A, B$ 都是 Hilbert 空间 $H$ 上处处有定义的线性算子，且

$$
(A x, y) = (x, B y), \forall x, y \in H.
$$

证明： $A, B$ 都是有界的，且 $B = A^{*}$ .

15. 设 $X, Y$ 都是 Banach 空间, $T \in L(X, Y)$ . 如果 $T$ 是单射的, 则 $T^{-1}$ 是闭算子.

16. 试证明: 如果 T 是闭算子, 则 T 的图形 $G(T)$ 是闭的.

17. 设 $\{x_{n}\}_{n=1}^{\infty}$ 是 Banach 空间 $X$ 中的点列, 如果对任何的 $f \in X'$ ,

$$
\sum_ {n = 1} ^ {\infty} | f (x _ {n}) | <   \infty ,
$$

---

则存在正数 $\mu$ ，对一切 $f\in X^{\prime}$ 都有

$$
\sum_ {n = 1} ^ {\infty} | f (x _ {n}) | \leqslant \mu \| f \|.
$$

18. 试证明:无穷维赋范线性空间的对偶空间是无穷维的,有限维赋范线性空间 X 的对偶空间 $X'$ 也是有限维的,且 $\dim X = \dim X'$ .

19. 试证明: Banach 空间 X 是自反的当且仅当 $X'$ 是自反的.

20. 设 $X, Y$ 都是 Banach 空间, $T: X \to Y$ 是保范同构映射. 证明 $T$ 的 Banach 共轭算子 $T'$ 是从 $Y'$ 到 $X'$ 的保范同构映射. 因此, 如果 $X \cong Y$ , 则 $X' \cong Y'$ . 这里“ $\cong$ ”表示两个 Banach 空间是保范同构的.

21. 设 $X, Y$ 都是 Banach 空间, $T \in L(X, Y)$ . 试证明: 如果 $T$ 是有限秩的, 即 $R(T)$ 是有限维的, 则 $T'$ 也是有限秩的, 且

$$
\dim R (T) = \dim R (T ^ {\prime}).
$$

22. 证明引理6.3和引理6.4.

23. 证明: $t^1$ 中点列的弱收敛与强收敛(即按范数收敛)等价.

24. 在 $L^p [a,b](1 < p < \infty)$ 中作一个弱收敛，但非强收敛的点列.

25. 设 $\{x_{n}\}_{n=1}^{\infty} \subset C[a, b], x \in C[a, b]$ . 证明: 如果 $x_{n} \xrightarrow{w} x$ , 则 $\{x_{n}\}_{n=1}^{\infty}$ 逐点收敛于 $x$ , 即任给 $t \in [a, b]$ , 都有 $\lim_{n \to \infty} x_{n}(t) = x(t)$ .

26. 设 $X, Y$ 都是 Banach 空间, $T \in L(X, Y)$ . 证明: 如果 $x_{n} \xrightarrow{w} x$ , 则 $Tx_{n} \xrightarrow{w} Tx$ .

27. 设 $M$ 是赋范线性空间 $X$ 的子空间, $\{x_{n}\}_{n=1}^{\infty} \subset M, x_{n} \xrightarrow{w} x_{0}$ , 则 $x_{0} \in M$ .

28. 设 $X, Y$ 都是赋范线性空间, $X \neq \{0\}$ . 试证明: 如果 $L(X, Y)$ 是Banach 空间, 则 $Y$ 必是Banach 空间.

29. 设 $X$ 是线性空间, $\| \cdot \|_1$ 与 $\| \cdot \|_2$ 分别是 $X$ 上范数. 如果凡按 $\| \cdot \|_1$ 连续的线性泛函也按 $\| \cdot \|_2$ 连续, 则必存在常数 $\alpha > 0$ , 使

$$
\| x \| _ {1} \leqslant \alpha \| x \| _ {2}, \forall x \in X.
$$

30. 设 $X, Y$ 都是 Banach 空间, $T \in L(X, Y)$ . 如果 $R(T) = Y$ , 则存在常数 $M > 0$ , 对任何 $y \in Y$ , 都有 $x \in X$ , 使

$$
y = T x  , \text {且}   \|   x   \| \leqslant M   \|   y   \|  .
$$

## 第四章有界线性算子谱论

## § 1 有界线性算子的谱还是回到线性代数,我们知道有限维空间 X 上的线性算子 T 的特征值概念是十分重要的.设 T 的特征值为 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{N}$ ，则 X 便可按这些特征值分解为 T 的 N 个不变子空间 $M_{1}, M_{2}, \cdots, M_{N}$ 的直接和

$$
X = M _ {1} \oplus M _ {2} \oplus \dots \oplus M _ {N}.
$$

这是关于算子 T 的结构的重要结果. 全体 $\lambda_{k}, k=1,\cdots,N$ ，按下面的定义来说，便是算子 T 的谱 $\sigma(T)$ ，它是重要的相似不变量. 这是对一般的线性变换 T 来说的，如果对自伴的线性变换，或 Hermite 矩阵来说，特征值的意义就更处于显要的地位了，无论是从纯数学或物理学来看都是如此.

## 1. 算子的预解式与谱以下总假定 $X$ 是非零的Banach空间， $T \in L(X), I$ 是 $X$ 上恒等算子.

定义1.1 设 $\lambda \in \mathbf{C}$ , 如果 $\lambda I - T$ 的值域 $R(\lambda I - T) = X$ , 且 $(\lambda I - T)^{-1} \in L(X)$ , 则称 $\lambda$ 在 $T$ 的预解集中, 记作 $\lambda \in \rho(T)$ . 以下有时也把 $(\lambda I - T)^{-1}$ 简记作 $R(\lambda, T)$ , 并称它为 $T$ 的预解式.

若有 $x \neq 0$ ，使 $(\lambda I - T)x = 0$ ，则称 $\lambda$ 为 $T$ 的特征值，或者说 $\lambda$ 在 $T$ 的点谱中，记作 $\lambda \in \sigma_p(T)$ . $x$ 称为 $T$ 相应于 $\lambda$ 的特征元或特征向量.

如果 $\lambda$ 不是 T 的特征值, 则 $\lambda I - T$ 是单射的, 此时 $\lambda I - T$ 的值域可分成三种情况:

(1) $R(\lambda I - T) = X$ ，此时 $\lambda I - T$ 是有界可逆的，即 $\lambda \in \rho(T)$

(2) $\overline{R(\lambda I - T)} = X$ ，但 $R(\lambda I - T) \neq X$ ，则称 $\lambda$ 在 $T$ 的连续谱中，记作 $\lambda \in \sigma_c(T)$ .

(3) $\overline{R(\lambda I - T)} \neq X$ , 则称 $\lambda$ 在 $T$ 的剩余谱中, 记作 $\lambda \in \sigma_r(T)$ .

显然， $\sigma_{p}(T), \sigma_{c}(T), \sigma_{r}(T)$ 彼此互不相交，且

$$
\sigma_ {p} (T) \bigcup \sigma_ {c} (T) \bigcup \sigma_ {r} (T) = \mathbf {C} \setminus \rho (T).
$$

我们定义 $T$ 的谱为

$$
\sigma (T) \stackrel {\mathrm{d}} {=} \mathbf {C} \setminus \rho (T),
$$

即

$$
\sigma (T) = \sigma_ {p} (T) \bigcup \sigma_ {c} (T) \bigcup \sigma_ {r} (T).
$$

如同第三章 §1 中对 $(I - A)^{-1}, A \in L(X)$ 的讨论, 现在对 $T \in L(X)$ , 形式上

$$
\frac {1}{\lambda - T} = \frac {1}{\lambda} \frac {1}{1 - \frac {T}{\lambda}} = \frac {1}{\lambda} \Big [ I + \sum_ {n = 1} ^ {\infty} \Big (\frac {T}{\lambda} \Big) ^ {n} \Big ], \text {当} | \lambda | > \| T \|.
$$

于是

$$
R (\lambda , T) = \frac {1}{\lambda} \Big [ I + \sum_ {n = 1} ^ {\infty} \Big (\frac {T}{\lambda} \Big) ^ {n} \Big ], \text {当} | \lambda | > \| T \|.
$$

因为用 $\lambda I - T$ 分别左、右乘上式右端，易见其结果皆为 $I$ 。一般称上式右端为 $R(\lambda, T)$ 的 Neumann 级数。由此可得定理1.1 若 $|\lambda| > \| T \|$ ，则 $\lambda \in \rho(T)$ ，或者说

$$
\sigma (T) \subset \{\lambda : | \lambda | \leqslant \| T \| \}.
$$

设 $\lambda_0\in \rho (T)$ ，形式上从

$$
\begin{array}{r l} \frac {1}{\lambda - T} & = \frac {1}{(\lambda - \lambda_ {0}) + (\lambda_ {0} - T)} \\ & = \frac {1}{\lambda_ {0} - T} \frac {1}{1 + \frac {\lambda - \lambda_ {0}}{\lambda_ {0} - T}} \\ & = \frac {1}{\lambda_ {0} - T} \left[ I + \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} \left(\frac {\lambda - \lambda_ {0}}{\lambda_ {0} - T}\right) ^ {n} \right], \end{array}
$$

$$
\text {当} \mid \lambda - \lambda_ {0} \mid <   \| (\lambda_ {0} I - T) ^ {- 1} \| ^ {- 1}.
$$

可见当 $|\lambda - \lambda_0| < \| (\lambda_0 I - T)^{-1} \|^{-1}$ 时， $\lambda \in \rho(T)$ ，并且 $R(\lambda, T)$ 在 $\lambda_0$ 附近能展成 $\lambda - \lambda_0$ 的幂级数，即

$$
\begin{array}{r l} {R (\lambda , T) = R (\lambda_ {0}, T) \Big [ I +  \sum_ {n = 1} ^ {\infty} (- 1) ^ {n} R (\lambda_ {0}, T) ^ {n} (\lambda - \lambda_ {0}) ^ {n} \Big ],} \\ & {\text {当} | \lambda - \lambda_ {0} | <   \| (\lambda_ {0} I - T) ^ {- 1} \| ^ {- 1}.} \end{array}
$$

据此可得定理1.2 $\rho (T)$ 是复平面上开集，从而 $\sigma (T)$ 是闭集.

定理1.3 设 $X$ 为Banach空间， $T \in L(X)$ . 则 $\sigma(T') = \sigma(T)$ ，且

$$
R (\lambda , T ^ {\prime}) = R (\lambda , T) ^ {\prime}, \quad \forall \lambda \in \rho (T).
$$

如果 $H$ 是Hilbert空间， $T \in L(H)$ ，则

$$
\sigma (T ^ {*}) = \{\overline {{{\lambda}}}: \lambda \in \sigma (T) \},
$$

且

$$
R (\overline {{{\lambda}}}, T ^ {*}) = R (\lambda , T) ^ {*}, \quad \forall \lambda \in \rho (T).
$$

证设 $T \in L(X)$ . 如果 $\lambda \in \rho(T)$ , 则 $\lambda I - T$ 是有界可逆的, 由第三章 §5 中定理 5.2 及定理 5.1 可知 $\lambda I - T' = (\lambda I - T)'$ 也是有界可逆的, 且

$$
\begin{array}{r l} R (\lambda , T ^ {\prime}) & = (\lambda I - T ^ {\prime}) ^ {- 1} = [ (\lambda I - T) ^ {\prime} ] ^ {- 1} \\ & = [ (\lambda I - T) ^ {- 1} ] ^ {\prime} = R (\lambda , T) ^ {\prime}. \end{array}
$$

即 $\lambda \in \rho(T')$ .

反之，若 $\lambda \in \rho (T^{\prime})$ ，则

$$
R (\lambda I - T ^ {\prime}) = X ^ {\prime} \text {且} N (\lambda I - T ^ {\prime}) = \{0 \}.
$$

根据闭值域定理(第三章§6定理6.4)可知 $R(\lambda I - T)$ 也是闭的，于是

$$
R (\lambda I - T) = ^ {0} N \left(\lambda I - T ^ {\prime}\right) = ^ {0} \{0 \} = X,
$$

$$
N (\lambda I - T) = ^ {0} R (\lambda I - T ^ {\prime}) = ^ {0} (X ^ {\prime}) = \{0 \}.
$$

故 $\lambda \in \rho(T)$ . 总之, $\rho(T) = \rho(T')$ . 即 $\sigma(T) = \sigma(T')$ .

对于 Hilbert 空间 $H$ 及 $T \in L(H)$ . 设 $\lambda \in \rho(T)$ , 则 $\lambda I - T$ 是有界可逆的. 于是由第二章 §4 定理 4.1, $\overline{\lambda} I - T^{*} = (\lambda I - T)^{*}$ 也是有界可逆的, 故 $\overline{\lambda} \in \rho(T^{*})$ , 且

$$
\begin{array}{r l} R (\overline {{\lambda}}, T ^ {*}) & = (\overline {{\lambda}} I - T ^ {*}) ^ {- 1} = [ (\lambda I - T) ^ {*} ] ^ {- 1} \\ & = [ (\lambda I - T) ^ {- 1} ] ^ {*} = R (\lambda , T) ^ {*}. \end{array}
$$

反之，若 $\overline{\lambda} \in \rho(T^{*})$ ，由前证， $\lambda = \overline{\lambda} \in \rho(T^{**})$ .但由前引定理4.1，还有 $T^{**} = T$ ，故 $\lambda \in \rho(T)$ .总之 $\rho(T^{*}) = \{\overline{\lambda} : \lambda \in \rho(T)\}$ ，亦即 $\sigma(T^{*}) = \{\overline{\lambda} : \lambda \in \sigma(T)\}$ .证毕.

例1 考察 $C[0,1]$ 上的算子

$$
(T x) (t) = \int_ {0} ^ {t} x (s) \mathrm{d} s, \quad x = x (t) \in C [ 0, 1 ],
$$

其值域为

$R(T) = \{y(t):y(t)\text{在}[0,1]\text{上有连续导数，且} y(0) = 0\}$ .

显然 $1 \notin \overline{R(T)}$ ，从而 $\overline{R(T)} \neq C[0,1]$ . 此外，从 $Tx = 0$ 易见 $x = 0$ ，故 $T$ 是单射的. 总之， $0 \in \sigma_r(T)$ .

事实上,0 是 T 的唯一谱点.如第三章 §1 中例 3,可以证明

$$
\lim _ {n \rightarrow \infty} \| T ^ {n} \| ^ {\frac {1}{n}} = 0.
$$

根据下文的定理1.7有 $\sigma (T) = \{0\}$

这种使 $\sigma(T) = \{0\}$ 的有界线性算子，通常称为拟幂零算子。它的谱虽然最简单，却是有界线性算子谱论中最难办的一类算子。

例2 考虑 $L^2[0,1]$ 上的乘法算子

$$
(T x) (t) = t x (t), x = x (t) \in L ^ {2} [ 0, 1 ].
$$

不难证明

$$
\sigma (T) = \sigma_ {c} (T) = [ 0, 1 ].
$$

事实上，对任意 $\lambda \notin [0,1], (\lambda - t)^{-1}$ 是 $[0,1]$ 上有界连续函数，而且乘以

$(\lambda - t)^{-1}$ 的乘法算子恰好是 $(\lambda I - T)^{-1}$ , 故 $\lambda \in \rho(T)$ . 当 $\lambda \in [0, 1]$ 时,

$$
[ (\lambda I - T) x ] (t) = (\lambda - t) x (t) = 0, \text {a.e.} \text {于} [ 0, 1 ],
$$

显然只有零解 $x(t) = 0$ ，a.e. 于 $[0,1]$ ，即 $\lambda I - T$ 是单射的。又因为 $(\lambda - t)^{-1} \notin L^2[0,1]$ ，故 $x(t) \equiv 1 \notin R(\lambda I - T)$ ，即 $R(\lambda I - T) \neq L^2[0,1]$ 。另一方面，假设 $y \in L^2[0,1]$ ，任给 $\varepsilon > 0$ ，由积分绝对连续性，存在 $\delta > 0$ ，使

$\int_{E}|y(t)|^{2}dt<\varepsilon^{2}$ ，当 $E\subset[0,1]$ 且 $m(E)<\delta$ .

记 $E_{\lambda} = [\lambda -\delta /3,\lambda +\delta /3]\cap [0,1]$ ，则 $m(E_{\lambda}) <   \delta$ ，令

$$
x _ {\epsilon} (t) = \left\{ \begin{array}{c l} {(\lambda - t) ^ {- 1} y (t),} & {\text {当} t \in [ 0, 1 ] \setminus E _ {\lambda}} \\ {0,} & {\text {当} t \in E _ {\lambda}} \end{array} \right.
$$

易见 $x_{\epsilon} \in L^{2}[0,1]$ , 且

$$
\begin{array}{r l} \left\| (\lambda I - T) x _ {\epsilon} - y \right\| ^ {2} & = \int_ {0} ^ {1} | (\lambda - t) x _ {\epsilon} (t) - y (t) | ^ {2} \mathrm{d} t \\ & = \int_ {E _ {\lambda}} | y (t) | ^ {2} \mathrm{d} t <   \varepsilon^ {2}, \end{array}
$$

故 $\overline{R(\lambda I - T)} = L^2 [0,1]$ . 总之， $\lambda \in \sigma_c(T)$ . 故

$$
\sigma (T) = \sigma_ {c} (T) = [ 0, 1 ].
$$

## 2. 抽象解析函数定义 1.2 设 $x(\lambda)$ 是定义在复平面的区域 D 内, 取值于 Banach 空间 X 中的抽象函数.

(1) 如果对任何 $\lambda_{0} \in D$ ,

$$
x ^ {\prime} \left(\lambda_ {0}\right) = \lim _ {h \rightarrow 0} \frac {x \left(\lambda_ {0} + h\right) - x \left(\lambda_ {0}\right)}{h}
$$

都存在,则称 $x(\lambda)$ 在 D 内强解析.

(2) 若于任何 $f \in X'$ , 复值函数 $f(x(\lambda))$ 都在 $D$ 内解析, 则称 $x(\lambda)$ 在 $D$ 内弱解析.

显然在 $D$ 内强解析的函数都在 $D$ 内弱解析, 其实我们还有定理1.4 在区域 $D$ 内弱解析的函数 $x(\lambda)$ 一定也在 $D$ 内强解析.

证对任何 $\lambda_0\in D$ ，当然有 $D$ 中的正向Jordan曲线 $C$ 及区域 $R_{0}$ ，使

$\lambda_0 \in R_0 \subset [C$ 的内部] $\subset C \cup [C$ 的内部] $\subset D$ .

(如图 4.1 所示).

由 Cauchy 积分公式, 对任何 $f \in X'$ 及 $\lambda_1 \in R_0$ 有

$$
f (x (\lambda_ {1})) = \frac {1}{2 \pi \mathrm{i}} \int_ {c} \frac {f (x (\lambda))}{\lambda - \lambda_ {1}} \mathrm{d} \lambda .\tag{1.1}
$$

设 $\lambda_0 + h, \lambda_0 + g$ 都在 $R_0$ 内，则由

![](../../../../04_Assets/Images/Courses/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90%28%E7%AC%AC2%E7%89%88%29%20%28%E6%B1%9F%E6%B3%BD%E5%9D%9A%2C%20%E5%AD%99%E5%96%84%E5%88%A9%29%20%28z-library.sk%2C%201lib.sk%2C%20z-li/images/batch_0001/67bbeca094da183d23d7198c4d91893f30ca1d5dc6ae0c118008c95ba0943703.jpg)  
图4.1

$$
\begin{array}{r l} \frac {1}{h - g} & \left\{\frac {1}{h} \left[ \frac {1}{\lambda - \lambda_ {0} - h} - \frac {1}{\lambda - \lambda_ {0}} \right] - \frac {1}{g} \left[ \frac {1}{\lambda - \lambda_ {0} - g} - \frac {1}{\lambda - \lambda_ {0}} \right] \right\} \\ & = \frac {1}{h - g} \left\{\frac {1}{(\lambda - \lambda_ {0} - h) (\lambda - \lambda_ {0})} - \frac {1}{(\lambda - \lambda_ {0} - g) (\lambda - \lambda_ {0})} \right\} \\ & = \frac {1}{(\lambda - \lambda_ {0} - h) (\lambda - \lambda_ {0} - g) (\lambda - \lambda_ {0})}, \end{array}
$$

便有

$$
\begin{array}{r l} \frac {1}{h - g} & \left\{\frac {f (x (\lambda_ {0} + h)) - f (x (\lambda_ {0}))}{h} - \frac {f (x (\lambda_ {0} + g)) - f (x (\lambda_ {0}))}{g} \right\} \\ & = \frac {1}{h - g} \left\{\frac {1}{2 \pi \mathrm{i} h} \int_ {c} \left[ \frac {f (x (\lambda))}{\lambda - \lambda_ {0} - h} - \frac {f (x (\lambda))}{\lambda - \lambda_ {0}} \right] \mathrm{d} \lambda - \right. \\ & \left. \frac {1}{2 \pi \mathrm{i} g} \int_ {c} \left[ \frac {f (x (\lambda))}{\lambda - \lambda_ {0} - g} - \frac {f (x (\lambda))}{\lambda - \lambda_ {0}} \right] \mathrm{d} \lambda \right\} \\ & = \frac {1}{2 \pi \mathrm{i}} \int_ {c} \frac {f (x (\lambda))}{(\lambda - \lambda_ {0} - h) (\lambda - \lambda_ {0} - g) (\lambda - \lambda_ {0})} \mathrm{d} \lambda . \end{array}\tag{1.2}
$$

注意 $\lambda_0, \lambda_0 + h, \lambda_0 + g$ 都在 $R_0$ 内，于是与 $C$ 上任何点的距离都大于某个正数，从而(1.2)式右端视为 $f \in X'$ 的泛函，关于 $\lambda_0 + h, \lambda_0 + g \in R_0$ 是有界的。考虑 $X$ 到 $X''$ 之典型映射的保范性质，根据一致有界原理，存在常数 $M > 0$ ，使

$$
\sup_{\substack{\lambda_{0} + h, \lambda_{0} + g\in R_{0}\\ h\neq g}}\frac{1}{|h - g|}\left\| \frac{x(\lambda_{0} + h) - x(\lambda_{0})}{h} - \right.\]\[\left. \frac{x(\lambda_{0} + g) - x(\lambda_{0})}{g}\right\| \leqslant M.
$$

于是对任何 $h_n \to 0, \left\{\frac{x(\lambda_0 + h_n) - x(\lambda_0)}{h_n}\right\}_{n=1}^{\infty}$ 是Cauchy序列. 因 $X$ 是完备的， $\left\{\frac{x(\lambda_0 + h_n) - x(\lambda_0)}{h_n}\right\}_{n=1}^{\infty}$ 收敛，可见

$$
\lim _ {h \rightarrow 0} \frac {x (\lambda_ {0} + h) - x (\lambda_ {0})}{h}
$$

存在. 证毕.

这个定理的好处在于弱解析性比之强解析性容易验证. 根据这个定理, 对抽象函数不必再区分强, 弱解析, 而统称之为解析.

命题1.1 设 $x(\lambda)$ 与 $y(\lambda)$ 都在区域 $D$ 内解析, 若互异的 $\{\lambda_n\}_{n=1}^{\infty} \subset D$ 有一极限点在 $D$ 内, 且

$$
x \left(\lambda_ {n}\right) = y \left(\lambda_ {n}\right), n = 1, 2, \dots ,
$$

则在 $D$ 内，

$$
x (\lambda) \equiv y (\lambda).
$$

这容易利用弱解析性及经典复变函数论中解析函数唯一性定理来证明.

定理1.5 (A.E.Taylor,1938) 对 $T \in L(X)$ , 恒有 $\sigma(T) \neq \emptyset$ .

证在定理1.1之前我们已经证明

$$
R (\lambda , T) = \frac {1}{\lambda} \left\{I + \sum_ {n = 1} ^ {\infty} \left(\frac {T}{\lambda}\right) ^ {n} \right\}
$$

在 $|\lambda| > \| T\|$ 时，按算子范数收敛.容易证明

$$
\parallel R (\lambda , T) \parallel \rightarrow 0, \text {当} | \lambda | \rightarrow \infty .
$$

如果 $\sigma(T) = \emptyset$ ，则如定理1.2的证明， $R(\lambda, T)$ 在复平面上任何点 $\lambda_0$ 附近都可展成 $\lambda - \lambda_0$ 的幂级数，因此 $R(\lambda, T)$ 在全平面上解析。从而对任给的 $f \in X'$ 及 $x \in X, f(R(\lambda, T)x)$ 是 $\lambda$ 的有界整函数。由经典复变函数论中的Liouville定理，

$$
f (R (\lambda , T) x) \equiv 0.
$$

由 $f$ 及 $x$ 的任意性可见， $R(\lambda, T) \equiv 0$ 。这不可能。证毕。

形式上

$$
\frac {1}{\lambda - T} - \frac {1}{\mu - T} = \frac {\mu - \lambda}{(\lambda - T) (\mu - T)}.
$$

故

(1.3) $R(\lambda, T) - R(\mu, T) = (\mu - \lambda)R(\lambda, T)R(\mu, T)$ , 当 $\lambda, \mu \in \rho(T)$ .

这只须用 $(\lambda I - T)(\mu I - T)$ 乘上式两端即可证出. 公式(1.3)证起来简单, 但是很有用, 人们特称之为第一预解公式.

## 3. 谱半径公式设 $T \in L(X)$ , 由第三章 §1 中定理 1.2, $\lim_{n \to \infty} \| T^n \|^{\frac{1}{n}}$ 总存在. 下面我们进一步证明定理1.6 设 $T \in L(X)$ , 则当 $|\lambda| > \lim_{n \to \infty} \| T^n \|^{\frac{1}{n}}$ 时, 级数 $\sum_{n=1}^{\infty} \lambda^{-n} T^{n-1}$ 按算子范数收敛.且

$$
R (\lambda , T) = \sum_ {n = 1} ^ {\infty} \lambda^ {- n} T ^ {n - 1},\tag{1.4}
$$

这里 $T^0 = I$

证令 $r = \lim_{n\to \infty}\| T^n\|^{\frac{1}{n}}$ .对任给 $\varepsilon >0$ ，若 $|\lambda |\geqslant r + \varepsilon$ ，注意当 $n$ 充分大时， $\| T^n\|^{\frac{1}{n}}\leqslant r + \frac{\varepsilon}{2}$ ，从而

$$
\| \lambda^ {- n} T ^ {n - 1} \| \leqslant | \lambda | ^ {- n} \| T ^ {n - 1} \| \leqslant (r + \varepsilon) ^ {- n} \left(r + \frac {\varepsilon}{2}\right) ^ {n - 1},
$$

故级数 $\sum_{n=1}^{\infty} \lambda^{-n} T^{n-1}$ 在 $|\lambda| > r$ 时是绝对收敛的，又 $L(X)$ 是完备的，故根据第一章习题23，级数按算子范数收敛.

通过直接验证可知，以 $\lambda I - T$ 左、右乘 $\sum_{n=1}^{\infty} \lambda^{-n} T^{n-1}$ 都得 $I$ ，故(1.4)式成立。证毕。

定义1.3 设 $T \in L(X)$ , 称

$$
r (T) \stackrel {\mathrm{d}} {=} \sup \left\{\mid \lambda \mid : \lambda \in \sigma (T) \right\}
$$

为 $T$ 的谱半径.

定理1.7（谱半径公式）若 $T \in L(X)$ ，则

$$
r (T) = \lim _ {n \rightarrow \infty} \| T ^ {n} \| ^ {\frac {1}{n}}.
$$

证令 $r = \lim_{n\to \infty}\| T^n\|^{\frac{1}{n}}$ .由定理1.6，当 $|\lambda | > r$ 时， $\lambda \in \rho (T)$ .故 $\sigma (T)\subset$ $\{\lambda :|\lambda |\leqslant r\}$ ，即 $r(T)\leqslant r$ .只须求证

$$
r (T) \geqslant r.
$$

由定理1.2证明可知， $R(\lambda ,T)$ 在 $|\lambda | > r(T)$ 上解析.于是对任意的 $f\in (L(X))'$ ， $f(R(\lambda ,T))$ 是 $|\lambda | > r(T)$ 上的复值解析函数.又由定理1.6

$$
R (\lambda , T) = \sum_ {n = 1} ^ {\infty} \lambda^ {- n} T ^ {n - 1}, \text {当} | \lambda | > r.
$$

于是得到 $f(R(\lambda, T))$ 的Laurent展式

$$
f (R (\lambda , T)) = \sum_ {n = 1} ^ {\infty} \lambda^ {- n} f (T ^ {n - 1}), | \lambda | > r.
$$

根据复值解析函数 Laurent 展式的唯一性, 上式在 $\left|\lambda\right|>r(T)$ 上亦成立. 于是对任何 $\varepsilon>0$ , 级数

$$
\sum_ {n = 1} ^ {\infty} \mid (r (T) + \varepsilon) ^ {- n} f (T ^ {n - 1}) \mid
$$

收敛. 故于任何 $f \in (L(X))'$ , 都有 $M_f > 0$ , 使

$$
\mid f ((r (T) + \varepsilon) ^ {- n} T ^ {n - 1}) \mid \leqslant M _ {f}, n = 1, 2, \dots .
$$

由第三章 §4 中命题 4.2, 存在常数 $M > 0$ , 使

$$
\| (r (T) + \varepsilon) ^ {- n} T ^ {n - 1} \| \leqslant M, n = 1, 2, \dots .
$$

于是

$$
\| T ^ {n} \| \leqslant M (r (T) + \epsilon) ^ {n + 1}, n = 1, 2, \dots .
$$

故

$$
r = \lim _ {n \rightarrow \infty} \| T ^ {n} \| ^ {\frac {1}{n}} \leqslant r (T) + \varepsilon .
$$

而 $\varepsilon$ 是任意的，所以 $r \leqslant r(T)$ . 证毕.

## 4. 移位算子

“最重要的,也是在 Hilbert 空间理论的一切部分中都起着重要作用的单个算子是单侧移位.”(见[17],第31页)

设 $\left\{e_{n}\right\}_{n=0}^{\infty}$ 是 Hilbert 空间 H 的一个正规正交基，由第二章定理 2.3, $\forall x\in H$ 唯一确定一个 $\left\{\xi_{n}\right\}=\left\{\xi_{0},\xi_{1},\xi_{2},\cdots\right\}\in t^{2}$ ，使

$$
x = \sum_ {n = 0} ^ {\infty} \xi_ {n} e _ {n},
$$

因此下面将 x 与 $\{\xi_{0},\xi_{1},\xi_{2},\cdots\}$ 等同，记为 $x=\{\xi_{0},\xi_{1},\xi_{2},\cdots\}$ .

$H$ 上单边移位算子 $S$ 定义如下：

$$
S e _ {n} = e _ {n + 1}, n = 0, 1, 2, \dots .
$$

即

$$
x = \{\xi_ {0}, \xi_ {1}, \xi_ {2}, \dots \} \mapsto S x = \{0, \xi_ {0}, \xi_ {1}, \xi_ {2}, \dots \}.
$$

易见 S 是线性算子,而且是保范的,即

$$
\| S x \| = \| x \|, \forall x \in H.
$$

设 $y=\{\eta_{0},\eta_{1},\eta_{2},\cdots\}$ , $S^{*}y=\{\zeta_{0},\zeta_{1},\zeta_{2},\cdots\}$ . 则

$$
(S x, y) = \sum_ {j = 0} ^ {\infty} \xi_ {j} \overline {{{{\eta}}}} _ {j + 1},
$$

$$
(x, S ^ {*} y) = \sum_ {j = 0} ^ {\infty} \xi_ {j} \bar {\zeta} _ {j}.
$$

因为

$$
(S x, y) = (x, S ^ {*} y), \forall x, y \in H.
$$

故可得

$$
\zeta_ {j} = \eta_ {j + 1}, j = 0, 1, 2, \dots .
$$

即

$$
S ^ {*} y = \{\eta_ {1}, \eta_ {2}, \eta_ {3}, \dots \}.
$$

一般称 $S^{*}$ 是向左(或向后)移位算子.

设 $T = S^{*}$ ，下面讨论 T 的一些性质。对 $y = \{\eta_{0}, \eta_{1}, \eta_{2}, \cdots\} \in H$ ，

$$
\begin{array}{r l} (T - \lambda I) y & = S ^ {*} \left\{\eta_ {0}, \eta_ {1}, \eta_ {2}, \dots \right\} - \lambda \left\{\eta_ {0}, \eta_ {1}, \eta_ {2}, \dots \right\} \\ & = \left\{\eta_ {1}, \eta_ {2}, \eta_ {3}, \dots \right\} - \left\{\lambda \eta_ {0}, \lambda \eta_ {1}, \lambda \eta_ {2}, \dots \right\} \\ & = \left\{\eta_ {1} - \lambda \eta_ {0}, \eta_ {2} - \lambda \eta_ {1}, \eta_ {3} - \lambda \eta_ {2}, \dots \right\}. \end{array}
$$

要想 $(T - \lambda I)y = 0$ ，必须且只须

$$
\eta_ {1} = \lambda \eta_ {0}, \eta_ {2} = \lambda \eta_ {1}, \eta_ {3} = \lambda \eta_ {2}, \dots ,
$$

即

$$
y = \{\eta_ {0}, \lambda \eta_ {0}, \lambda^ {2} \eta_ {0}, \dots \} = \eta_ {0} \{1, \lambda , \lambda^ {2}, \dots \}.\tag{1.5}
$$

显然， $y = \eta_{0}\{1, \lambda, \lambda^{2}, \cdots\} \in H(\eta_{0} \neq 0)$ 当且仅当 $|\lambda| < 1$ . 总之

$$
\sigma_ {p} (T) = D \stackrel {\mathrm{d}} {=} \{\lambda : | \lambda | <   1 \}.\tag{1.6}
$$

且

$$
\dim N (T - \lambda I) = 1, \text {当} \lambda \in D.\tag{1.7}
$$

因为 $S$ 是保范的, 故 $\| S \| = 1$ . 又从第二章 §4 中定理 4.1 有 $\| S^{*} \| = \| S \| = 1$ . 于是

$$
D = \sigma_ {p} (S ^ {*}) \subset \sigma (S ^ {*}) \subset \overline {{{{D}}}}.
$$

又因 $\sigma(S^{*})$ 是闭的，故 $\sigma(S^{*})=\overline{D}$ . 根据定理 1.3, $\sigma(S)=\overline{D}$ . 对 $x=\left|\xi_{0},\xi_{1},\xi_{2},\cdots\right|\in H$ , 从 $(S-\lambda I)x=0$ , 可得

$$
- \lambda \xi_ {0} = 0, \xi_ {n} - \lambda \xi_ {n + 1} = 0, n = 0, 1, 2, \dots .
$$

故满足 $|\lambda| \leqslant 1$ 的任何 $\lambda$ 都不是 $S$ 的特征值. 又 $S$ 的值域 $R(S)$ 显然不在 $H$ 中稠密, 所以关于 $S$ 还有

$$
\sigma_ {p} (S) = \varnothing , \quad 0 \in \sigma_ {r} (S).
$$

以下再看 $T$ 的另外两个重要性质.

命题1.2 $R(T - \lambda I) = H$ ，当 $\lambda \in D$

证先证 $R(T - \lambda I)$ 是闭的. 注意, $(S - \overline{\lambda} I)^* = S^* - \lambda I = T - \lambda I$ . 根据闭值域定理 (见第三章 §6 中定理 6.5), 只须证明 $R(S - \overline{\lambda} I)$ 是闭的. 因为 $S$ 是保范算子. 于是对 $\lambda \in D$ ,

$$
\| (S - \overline {{\lambda}} I) x \| \geqslant \| S x \| - \| \overline {{\lambda}} x \| = (1 - | \lambda |) \| x \|, \forall x \in H.
$$

由此可见 $R(S - \overline{\lambda} I)$ 是闭的.

又根据闭值域定理(见第三章 §6 中定理 6.5)可知

$$
R (T - \lambda I) = N (S - \overline {{{\lambda}}} I) ^ {\perp} = \{0 \} ^ {\perp} = H.
$$

证毕.

命题1.3 $\bigvee_{\lambda \in D}N(T - \lambda I) = H.$

这里 $\bigvee_{\alpha \in \mathcal{A}} \mathcal{M}_{\alpha}$ 表示线性流形 $\mathcal{M}_{\alpha}, \alpha \in \mathcal{A}$ , 线性张开的闭包.

证记上式左端为 $\mathcal{M}$ , 若 $\{a_0, a_1, a_2, \cdots\} \in H$ 与 $\mathcal{M}$ 正交, 即 $\{a_0, a_1, a_2, \cdots\}$ 与 $\mathcal{M}$ 中每个元正交. 由(1.5),

$$
\eta_ {0} \left(\overline {{{a}}} _ {0} + \overline {{{a}}} _ {1} \lambda + \overline {{{a}}} _ {2} \lambda^ {2} + \dots\right) = 0, \forall \lambda \in D.
$$

根据幂级数性质,便有

$$
a _ {0} = a _ {1} = a _ {2} = \dots = 0.
$$

证毕.

M. Cowen 和 R.G. Douglas 在 1978 年提出一类与复几何密切相关的算子类 $B_{n}(\Omega)$ , (详见[25])

设 $\Omega$ 是复平面区域, $B_{n}(\Omega)$ 表示 Hilbert 空间 $H$ 上满足如下条件的所有算子 $T$ 的集合:

(1) $\sigma_{p}(T) = \Omega$

(2) $\dim N(T - \lambda I) = n$ ，当 $\lambda \in \Omega$ ，

(3) $H = \bigvee_{\lambda \in \Omega}N(T - \lambda I),$

(4) $H = R(T - \lambda I)$ , 当 $\lambda \in \Omega$ .

综合以上向后移位 T 的性质: (1.6) 与 (1.7) 式, 命题 1.2 及命题 1.3, 正说明 $T \in B_{1}(D)$ .

## § 2 射影算子与约化

## 1. 射影在线性代数中,我们已经看到空间分解与算子的结构密切相关,所以下面要讲的射影的概念是自然的.

设 $X$ 是Banach空间，若有 $X$ 的线性流形 $X_{1}$ 与 $X_{2}$ ，使

$$
X = X _ {1} \oplus X _ {2},
$$

这里 $\oplus$ 表示直接和(参见第一章 §2).

考察变换

$$
P x = x _ {1}  , \text {当}   x = x _ {1} + x _ {2}  , x _ {j} \in X _ {j}  , j = 1, 2.
$$

容易从直接和的定义证明, 对每个 $x \in X$ , 恰有一个 $x_{1} \in X_{1}$ 与之对应, 因此变换 $P$ 的定义是完善的. 容易证明, $P$ 是 $X$ 上处处定义的线性算子. 人们称 $P$ 为与 $\{X_{1}, X_{2}\}$ 相关的从 $X$ 到 $X_{1}$ 的射影.

从几何的观点看， $P$ 就是从 $X$ 沿着 $X_{2}$ 的方向到 $X_{1}$ 上的射影.

定理2.1 设 $X_{1}$ 与 $X_{2}$ 都是Banach空间 $X$ 的子空间，使 $X = X_{1} \oplus X_{2}$ ，则从 X 到 $X_{1}$ 的射影 P 是有界的.

证根据闭图形定理, 只须证明 $P$ 是闭算子即可. 设 $\{x_{n}\}_{n=1}^{\infty} \subset X$ , 使

$$
x _ {n} \rightarrow x _ {0}, P x _ {n} \rightarrow x _ {0} ^ {(1)}.
$$

则

$$
\lim _ {n \rightarrow \infty} (x _ {n} - P x _ {n}) = x _ {0} - x _ {0} ^ {(1)}.
$$

设 $x_0^{(2)} = x_0 - x_0^{(1)}$ . 注意 $Px_n \in X_1, x_n - Px_n \in X_2$ ，而 $X_1, X_2$ 都是闭的，故 $x_0^{(1)} \in X_1, x_0^{(2)} \in X_2$ ，且 $x_0 = x_0^{(1)} + x_0^{(2)}$ . 由射影的定义，便有 $Px_0 = x_0^{(1)}$ . 即 $P$ 是闭算子. 证毕.

定义2.1 设 $X_{1}$ 与 $X_{2}$ 都是Banach空间 $X$ 的子空间，使 $X = X_{1} \oplus X_{2}$ ，则称 $X_{1}$ 与 $X_{2}$ 是拓扑互补子空间，称 $X_{2}$ 是 $X_{1}$ 的拓扑补.

在第三章 §2 中我们已经指出,一般无穷维的 Banach 空间 X 与欧氏空间不一样,并不是任意子空间都一定有拓扑补,即使 X 是 $L^{p}$ 或 $\ell^{p}(p \neq 2)$ 这样好的空间也不行.

对于射影算子,从定义显然

$$
P ^ {2}   x = P (  P x  ) = P x _ {1} = x _ {1} = P x  , \text {当}    x \in X  ,
$$

即算子 $P$ 是幂等的：

$$
P ^ {2} = P.
$$

从代数的观点看，

定理2.2 设 $P$ 是Banach空间 $X$ 上有界幂等的线性算子, 则

$$
\mathcal {M} \stackrel {\mathrm{d}} {=} \left\{x: P x = x \right\}, \mathcal {N} \stackrel {\mathrm{d}} {=} \left\{x: P x = 0 \right\}
$$

是拓扑互补子空间. 从而 $P$ 就是与 $\{\mathcal{M}, \mathcal{N}\}$ 相关的从 $X$ 到 $\mathcal{M}$ 的射影.

证从 $P$ 的线性和连续性, 易知 $\mathcal{M}, \mathcal{N}$ 都是 $X$ 的子空间. 若有 $x_0 \in \mathcal{M} \cap \mathcal{N}$ , 则 $Px_0 = x_0$ , 且 $Px_0 = 0$ , 故 $x_0 = 0$ . 可见 $\mathcal{M} \cap \mathcal{N} = \{0\}$ . 对任何 $x \in X$ , 当然有

$$
x = P x + (x - P x).
$$

因 $P$ 是幂等的, 所以 $Px \in \mathcal{M}, x - Px \in \mathcal{N}$ . 总之

$$
X = \mathcal {M} \oplus \mathcal {N}.
$$

证毕.

## 2. 有界线性算子的不变子空间与约化子空间泛函分析的一个迄今远未解决的重大问题是要对一般线性算子的结构得到完全的了解,而算子结构理论中最基本的概念,也是迄今研究的主要对象即下面要讲的不变子空间与约化子空间.

以下恒设 X 为 Banach 空间, $T \in L(X)$ .

定义2.2 对 $X$ 的子空间 $\mathcal{M}$ , 若

$$
T (\mathcal {M}) \subset \mathcal {M}.
$$

则称 $\mathcal{M}$ 为 $T$ 的不变子空间，通常简记为 $\mathcal{M} \in \operatorname{Lat} T$ .

定理2.3 如果 $T \in L(X), P$ 是 $X$ 到子空间 $\mathcal{M}$ 上的射影，则

$$
\mathcal {M} \in \operatorname{Lat} T \Leftrightarrow T P = P T P.
$$

证如果 $\mathcal{M} \in \operatorname{Lat} T$ ，任给 $x \in X, TPx \in T(\mathcal{M}) \subset \mathcal{M}$ . 故

$$
P (T P x) = T P x.
$$

反之，任给 $x \in \mathcal{M}, Px = x$ ，由假设 $TP = PTP$ ，则 $Tx = TPx = PTPx = PTx \in \mathcal{M}$ . 故 $\mathcal{M} \in \operatorname{Lat} T$ . 证毕.

不变子空间问题：

是否每个 $T \in L(X)$ 都有非平凡的（即异于 $\{0\}$ 与 $X$ 者）不变子空间？

自从 1954 年 Aronszajn 和 Smith $^{[24]}$ 证明 Banach 空间上的紧算子都有非平凡的不变子空间以来，这一直被认为是算子理论中的大问题，累攻不下。直到 1984 年，C.J.Read $^{[38]}$ 在 $t^{1}$ 上构造出一个有界线性算子，它没有非平凡的不变子空间。但是对 X 为自反空间，特别 Hilbert 空间的情况，不变子空间问题迄今仍没有答案。

显然对 $\mathcal{M} \in \mathrm{Lat}T$ ，可以产生一个从 $\mathcal{M}$ 到 $\mathcal{M}$ 的有界线性算子 $T|_{\mathcal{M}}$ ：

$$
(T | \mathcal {M}) x = T x, \text {当} x \in \mathcal {M}.
$$

称为 $T$ 在 $\mathcal{M}$ 上的限制.

定义2.3 若 $\mathcal{M}$ 与 $\mathcal{N}$ 是 $X$ 中拓扑互补的子空间，又都是 $T$ 的不变子空间，则称 $\{\mathcal{M},\mathcal{N}\}$ 约化 $T$ ，也称 $\mathcal{M}$ 与 $\mathcal{N}$ 为 $T$ 的约化子空间.

如果 $\{\mathcal{M},\mathcal{N}\}$ 约化 $T$ ，那么对 $T$ 的研究可转化为对较小空间上的算子 $T\mid \mathcal{M}$ 与 $T\mid \mathcal{N}$ 的研究，所以 $X$ 的这种按照 $T$ 之约化子空间的分解 $X = \mathcal{M} \oplus \mathcal{N}$ 是十分重要的.

定理2.4 $\{\mathcal{M},\mathcal{N}\}$ 约化 $T$ 必须且只须

$$
P T = T P,
$$

这里 $P$ 是与 $\{\mathcal{M},\mathcal{N}\}$ 相关的从 $X$ 到 $\mathcal{M}$ 的射影.

证由假设 $P$ 是从 $X$ 到 $\mathcal{M}$ 的射影, $I - P$ 是从 $X$ 到 $\mathcal{N}$ 的射影. 根据定理2.3,

$$
\begin{array}{r l} & {\{\mathcal {M}, \mathcal {N} \} \text {约化} T} \\ & {\Leftrightarrow T P = P T P, T (I - P) = (I - P) T (I - P).} \\ & {\Leftrightarrow T P = P T.} \end{array}
$$

证毕.

这个定理证明不难,但相当重要.它告诉我们,要考察 T 的约化子空间,只须研究 T 的换位

$$
\{T \} ^ {\prime} = \{A: A \in L (X), \text {且} A T = T A \}
$$

中的幂等算子.

## 3. F.Riesz 空间分解定理为了证明 Riesz 空间分解定理,我们需要考虑抽象函数的曲线积分.

设 $C: z = z(t), 0 \leqslant t \leqslant 1$ ，是复平面 $\mathbf{C}$ 上可求长的简单的光滑曲线。 $f(z)$ 是定义在 $C$ 上，取值于 Banach 空间 $X$ 中的连续的抽象函数。

对[0,1]的任意分划

$$
\mathcal {D}: 0 = t _ {0} <   t _ {1} <   t _ {2} <   \dots <   t _ {n} = 1,
$$

取 $z_{j}=z(t_{j}), z_{j}^{\prime}=z(t_{j}^{\prime}), t_{j-1}\leqslant t_{j}^{\prime}\leqslant t_{j}$ ，又 $\Delta z_{j}=z_{j}-z_{j-1}, j=1,2,\cdots,n.$ 令 $\|\mathscr{D}\|=\max\limits_{1\leqslant j\leqslant n}|t_{j}-t_{j-1}|$ . 如果极限

$$
\lim _ {\| \mathcal {D} \| \rightarrow 0} \sum_ {j = 1} ^ {n} f (z _ {j} ^ {\prime}) \Delta z _ {j}
$$

存在,则它也是 X 中一个元,称为 $f(z)$ 在 C 上的积分,记为

$$
\int_ {C} f (z) \mathrm{d} z = \lim _ {\| \mathcal {D} \| \rightarrow 0} \sum_ {j = 1} ^ {n} f (z _ {j} ^ {\prime}) \Delta z _ {j}.
$$

如一般复变函数论教科书上的处理(参见江泽坚《复变函数》，人民教育出版社，1951, § III.1)一样可以证明，对 $C$ 上连续的抽象函数 $f(z)$ ，积分 $\int_{C} f(z) \mathrm{d}z$ 必定存在。又如定理 1.4 的思想，我们总可以把强解析函数的问题转化成弱解析函数，从而可用经典的复变函数论来处理。由此不难证明。对于抽象解析函数也有 Cauchy 积分定理。

设 $T \in L(X)$ , 其谱 $\sigma(T)$ 被可求长的、简单的、光滑的正向的闭曲线 $C$ 分成 $\sigma_1$ 与 $\sigma_2$ 两部分, 其中 $\sigma_1$ 在 $C$ 之内, 而 $\sigma_2$ 在 $C$ 之外 (如图4.2). 则下面的 Riesz 空间分解定理告诉我们 $T$ 必有非平凡的约化子空间.

![](../../../../04_Assets/Images/Courses/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90%28%E7%AC%AC2%E7%89%88%29%20%28%E6%B1%9F%E6%B3%BD%E5%9D%9A%2C%20%E5%AD%99%E5%96%84%E5%88%A9%29%20%28z-library.sk%2C%201lib.sk%2C%20z-li/images/batch_0001/41869c63c87613f42519aeec2ee768cecb7f6fa1d260d0b351d10524049046fb.jpg)  
图4.2

定理 2.5(F. Riesz, 1913) 设 $T \in L(X)$ ，其谱如上所述，则有 T 的约化子空间 $M_{1}$ 与 $M_{2}$ ，使

$$
X = \mathcal {M} _ {1} \oplus \mathcal {M} _ {2},
$$

$$
\sigma (T | \mathcal {M} _ {j}) = \sigma_ {j}, j = 1, 2.
$$

证以下将 $R(\xi, T)$ 简记为 $R(\xi)$ , 定义

$$
P = \frac {1}{2 \pi \mathrm{i}} \int_ {C} R (\xi) \mathrm{d} \xi .
$$

则 $P \in L(X)$ , 往证 $P^2 = P$ .

注意 $R(\xi)$ 是 $\rho(T)$ 上的解析函数，设 $C'$ 是 $\rho(T)$ 内另一条可求长的、简单的、光滑的正向的闭曲线，使 $C$ 及 $\sigma_1$ 在 $C'$ 之内， $\sigma_2$ 在 $C'$ 之外（如图4.3）.

![](../../../../04_Assets/Images/Courses/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90%28%E7%AC%AC2%E7%89%88%29%20%28%E6%B1%9F%E6%B3%BD%E5%9D%9A%2C%20%E5%AD%99%E5%96%84%E5%88%A9%29%20%28z-library.sk%2C%201lib.sk%2C%20z-li/images/batch_0001/985f1d768f38a07c9562858ed76f2355c6aef4f45cc47f43306d68da62773130.jpg)  
图4.3

由抽象解析函数的 Cauchy 积分定理，

$$
P = \frac {1}{2 \pi \mathrm{i}} \int_ {C} R (\xi) \mathrm{d} \xi = \frac {1}{2 \pi \mathrm{i}} \int_ {C ^ {\prime}} R (\eta) \mathrm{d} \eta .
$$

于是

$$
(2 \pi \mathrm{i}) ^ {2} P ^ {2} = \int_ {C} R (\xi) \mathrm{d} \xi \int_ {C ^ {\prime}} R (\eta) \mathrm{d} \eta = \int_ {C} \mathrm{d} \xi \int_ {C ^ {\prime}} R (\xi) R (\eta) \mathrm{d} \eta .
$$

由第一预解公式,则

$$
\begin{array}{r l} (2 \pi \mathrm{i}) ^ {2} P ^ {2} & = \int_ {c} \mathrm{d} \xi \int_ {c ^ {\prime}} \frac {1}{\eta - \xi} [ R (\xi) - R (\eta) ] \mathrm{d} \eta \\ & = \int_ {c} R (\xi) \mathrm{d} \xi \int_ {c ^ {\prime}} \frac {1}{\eta - \xi} \mathrm{d} \eta - \int_ {c ^ {\prime}} R (\eta) \mathrm{d} \eta \int_ {c} \frac {1}{\eta - \xi} \mathrm{d} \xi \\ & = 2 \pi \mathrm{i} \int_ {c} R (\xi) \mathrm{d} \xi - 0 \\ & = (2 \pi \mathrm{i}) ^ {2} P. \end{array}
$$

故 $P^2 = P$ .令

$$
\mathcal {M} _ {1} = P X, \mathcal {M} _ {2} = (I - P) X.
$$

易见

$$
\mathcal {M} _ {1} = \{x: P x = x \}, \mathcal {M} _ {2} = \{x: P x = 0 \}.
$$

由定理2.2, $X = \mathcal{M}_1\oplus \mathcal{M}_2,P$ 是与 $\{\mathcal{M}_1,\mathcal{M}_2\}$ 相关的从 $X$ 到 $\mathcal{M}_1$ 的射影.

注意 $R(\xi)$ 与 $R(\eta)$ 总是可交换的，即

$$
R (\xi) R (\eta) = R (\eta) R (\xi), \text {当} \xi , \eta \in \rho (T),
$$

故由 $P$ 的定义有

$$
P R (\eta) = R (\eta) P.\tag{2.1}
$$

两边同时左乘并右乘以 $\eta I - T$ ，可得

$$
(\eta I - T) P = P (\eta I - T).
$$

故 $TP = PT$ . 由定理2.4, $\{\mathcal{M}_1, \mathcal{M}_2\}$ 约化 $T$ .

从(2.1)式可见 $\{\mathcal{M}_1, \mathcal{M}_2\}$ 也约化 $R(\eta)$ , 从而 $\mathcal{M}_1, \mathcal{M}_2$ 是 $R(\eta)$ 的不变子空间, 对任意的 $\eta \in \rho(T)$ . 这说明 $\rho(T) \subset \rho(T | \mathcal{M}_j)$ (习题7), 即

(2.2)

$$
\sigma (T | \mathcal {M} _ {j}) \subset \sigma (T), j = 1, 2.
$$

往证 $\sigma (T|\mathcal{M}_1)\subset \sigma_1$ .对 $\zeta \notin C$ ，令

$$
R _ {\zeta} = \frac {1}{2 \pi \mathrm{i}} \int_ {c} \frac {R (\xi)}{\xi - \zeta} \mathrm{d} \xi ,
$$

则 $R_{\xi} \in L(X)$ , 而且 $\mathcal{M}_j$ 也是 $R_{\xi}$ 的不变子空间. 又

$$
\begin{array}{r l} (\zeta I - T) R _ {\zeta} & = R _ {\zeta} (\zeta I - T) \\ & = \frac {1}{2 \pi \mathrm{i}} \int_ {C} \frac {(\zeta I - T) R (\xi)}{\xi - \zeta} \mathrm{d} \xi \\ & = \frac {1}{2 \pi \mathrm{i}} \int_ {C} \frac {[ (\zeta I - \xi I) + (\xi I - T) ] R (\xi)}{\xi - \zeta} \mathrm{d} \xi \\ & = - \frac {1}{2 \pi \mathrm{i}} \int_ {C} R (\xi) \mathrm{d} \xi + \frac {1}{2 \pi \mathrm{i}} \int_ {C} \frac {1}{\xi - \zeta} \mathrm{d} \xi \cdot I, \end{array}
$$

于是，当 $\zeta$ 在 $C$ 之外时，

$$
(\zeta I - T) R _ {\zeta} = - P.
$$

当 $\zeta$ 在 $C$ 之内时，

$$
(\zeta I - T) R _ {\zeta} = I - P.
$$

设 $x \in \mathcal{M}_1$ ，则当 $\zeta$ 在 $C$ 之外时，

$$
(\zeta I - T) (- R _ {\zeta}) x = (- R _ {\zeta}) (\zeta I - T) x = P x = x.
$$

故 $(\zeta I - T|\mathcal{M}_1)^{-1} = -R_{\xi}|\mathcal{M}_1$ 在 $C$ 之外存在，据此

$$
\rho (T | \mathcal {M} _ {1}) \supset C \text {之外部}.
$$

即

$$
\sigma (T | \mathcal {M} _ {1}) \subset [ C \cup C \text {   之内部   } ].
$$

再由(2.2)式，

$$
\sigma (T | \mathcal {M} _ {1}) \subset \sigma (T) \cap [ C \cup C \text {之内部} ] = \sigma_ {1}.\tag{2.3}
$$

同法可以证明

$$
\sigma (T | \mathcal {M} _ {2}) \subset \sigma_ {2}.\tag{2.4}
$$

以下来证， $\sigma(T|\mathcal{M}_1) = \sigma_1$ 。否则有 $\xi_0 \in \sigma_1 \setminus \sigma(T|\mathcal{M}_1)$ 。从(2.4)式，

$$
\rho (T | \mathcal {M} _ {2}) \supset \mathbf {C} \setminus \sigma_ {2} \supset \sigma_ {1},
$$

故 $\xi_0\in \rho (T|\mathcal{M}_1)\cap \rho (T|\mathcal{M}_2)$ .从而

$$
R _ {\mathcal {M} _ {j}} (\xi_ {0}) \stackrel {{d}} {{=}} (\xi_ {0} I - T | \mathcal {M} _ {j}) ^ {- 1}
$$

是 $\mathcal{M}_j$ 上的连续线性算子 $(j = 1,2)$ . 令

$$
\widetilde {R} _ {0} = R _ {\mathcal {M} _ {1}} (\xi_ {0}) P + R _ {\mathcal {M} _ {2}} (\xi_ {0}) (I - P),
$$

则 $\widetilde{R}_0\in L(X)$ .注意任给 $x\in X$ ，总可表示成

$$
x = x _ {1} + x _ {2}, x _ {j} \in \mathcal {M} _ {j}, j = 1, 2.
$$

于是

$$
\begin{array}{r l} \widetilde {R} _ {0} x & = R _ {\mathcal {M} _ {1}} (\xi_ {0}) P (x _ {1} + x _ {2}) + R _ {\mathcal {M} _ {2}} (\xi_ {0}) (I - P) (x _ {1} + x _ {2}) \\ & = R _ {\mathcal {M} _ {1}} (\xi_ {0}) x _ {1} + R _ {\mathcal {M} _ {2}} (\xi_ {0}) x _ {2}. \end{array}
$$

注意 $R_{\mathcal{M}_j}(\xi_0)x_j\in \mathcal{M}_j,j = 1,2$ ，于是

$$
\begin{array}{r l} (\xi_ {0} I - T) \widetilde {R _ {0}} x & = (\xi_ {0} I - T | \mathcal {M} _ {1}) R _ {\mathcal {M} _ {1}} (\xi_ {0}) x _ {1} + (\xi_ {0} I - T | \mathcal {M} _ {2}) R _ {\mathcal {M} _ {2}} (\xi_ {0}) x _ {2} \\ & = x _ {1} + x _ {2} = x. \end{array}
$$

故

$$
\left(\xi_ {0} I - T\right) \widetilde {R _ {0}} = I.
$$

同样可证出

$$
\widetilde {R} _ {0} (\xi_ {0} I - T) = I.
$$

所以 $\xi_0 I - T$ 是有界可逆的，即 $\xi_0 \in \rho(T)$ . 但这与 $\xi_0 \in \sigma_1 \subset \sigma(T)$ 矛盾. 总之，

$$
\sigma (T | \mathcal {M} _ {1}) = \sigma_ {1}.
$$

同理可证， $\sigma(T|\mathcal{M}_2) = \sigma_2$ 。证毕。

## §3 紧算子

## 1. 紧算子的定义及其性质数学物理方法中许多问题可以转化为积分方程来处理,所以积分算子是很重要的有界线性算子.1918年左右,F.Riesz把积分算子推广成下文所谓的紧算子.

以下恒设 $X$ 为Banach空间.

定义3.1 设 $A \in L(X)$ . 若 $A$ 把 $X$ 中每个有界集都变成列紧集（即于有界的 $\{x_{n}\}_{n=1}^{\infty} \subset X, \{Ax_{n}\}_{n=1}^{\infty}$ 恒有收敛的子序列），则称 $A$ 为紧算子，或者全连续算子.

定义 3.2 对 $A \in L(X)$ ，若 $\dim R(A) < \infty$ ，则称 A 为有限秩算子。

例1：凡有限秩算子都是紧算子.

设 $A \in L(X)$ 是有限秩算子, 从有界性可见 $A$ 变 $X$ 中有界集 $S$ 为 $R(A)$ 中的有界集 $A(S)$ . 现在, $\dim R(A) < \infty$ , 故 $A(S)$ 列紧, 于是 $A$ 为紧算子.

例2 设 $K(s, t)$ 是 $0 \leqslant s, t \leqslant 1$ 上的连续函数，则积分算子

$$
(\dot {A} x) (s) = \int_ {0} ^ {1} K (s, t) x (t) \mathrm{d} t, \text {当} x = x (t) \in C [ 0, 1 ],
$$

是 $X = C[0,1]$ 上的紧算子.

根据 Arzela-Ascoli 定理(即第一章 §6 中定理 6.4)，这只须证明 $X$ 中任何有界集 $\{x: \| x \| \leqslant B\}$ 在 $A$ 之下的像是一致有界且同等连续的。

设 $M = \sup_{0\leqslant s,t\leqslant 1}|K(s,t)|$ ，则

$$
\begin{array}{r l} | (A x) (s) | & \leqslant \int_ {0} ^ {1} | K (s, t) x (t) | \mathrm{d} t \\ & \leqslant \int_ {0} ^ {1} M B \mathrm{d} t = M B, \text {当} \| x \| \leqslant B. \end{array}
$$

这说明像集的一致有界性.

其次，从 $K(s,t)$ 的一致连续性，对任给的 $\varepsilon >0$ ，应有 $\delta >0$ ，使

$$
| K (s _ {1}, t) - K (s _ {2}, t) | <   \varepsilon , \text {当} | s _ {1} - s _ {2} | <   \delta , 0 {\leqslant} t {\leqslant} 1.
$$

从而

$$
\begin{array}{r l} & {\mid (A x) (s _ {1}) - (A x) (s _ {2}) \mid \leqslant \int_ {0} ^ {1} \mid K (s _ {1}, t) - K (s _ {2}, t) \mid \mid x (t) \mid \mathrm{d} t} \\ & {\quad \leqslant \varepsilon \int_ {0} ^ {1} \mid x (t) \mid \mathrm{d} t \leqslant B \varepsilon , \quad \text {当} \| x \| \leqslant B, \mid s _ {1} - s _ {2} \mid <   \delta .} \end{array}
$$

这表明像集的同等连续性.

例3 $\ell^2$ 上的恒等算子 $I$ 非紧算子.

考察

$$
e _ {n} = \{0, \dots , 0, 1, 0, \dots \}, n = 1, 2, \dots ,
$$

即 $e_n$ 之第 $n$ 个坐标是1, 其余的坐标是0, 则 $\| e_n \| = 1$ , 而

$$
\parallel e _ {j} - e _ {k} \parallel = \sqrt {2}, \text {当} j \neq k.
$$

故 $Ie_{n} = e_{n}, n = 1,2,\dots$ ，没有收敛的子序列。从而 $I$ 不是紧算子。

以后，用 $\mathcal{H}(X)$ 表示 $X$ 上全体紧算子构成的集合.

定理3.1 设 $A_{j} \in \mathcal{K}(X), \alpha_{j} \in \mathbf{C}, j = 1,2, B \in L(X)$ . 则

(1) $\alpha_{1}A_{1} + \alpha_{2}A_{2}\in \mathcal{H}(X)$ .

(2) $A_{1}B$ 与 $BA_{1}$ 都在 $\mathcal{K}(X)$ 中.

证 (1) 是明显的. 至于(2), 只须注意 $B$ 将有界集变为有界集, 将收敛序列变为收敛序列. 证毕.

定义3.3 设 $\mathcal{T}$ 是代数 $Q$ 的子集. $\mathcal{T}$ 称为 $Q$ 的左(右)理想, 如果从 $x, y \in \mathcal{T}$ , 总有

$$
\alpha x + \beta y \in \mathcal {T}, z x \in \mathcal {T} (x z \in \mathcal {T}),
$$

这里 $\alpha, \beta \in \mathbf{C}, z$ 是 $Q$ 中的任意元.

如果 $\mathcal{T}$ 既是 $Q$ 的左理想, 又是 $Q$ 的右理想, 则称 $\mathcal{T}$ 为 $Q$ 的双边理想, 或简称为理想.

从定理3.1可见，

全体紧算子 $\mathcal{X}(X)$ 是 $L(X)$ 的非零的理想.

定理3.2 设 $\{A_n\}_{n=1}^{\infty} \subset \mathcal{K}(X), \| A_n - A \| \to 0, n \to \infty$ , 则 $A \in \mathcal{K}(X)$ .

证设 $\{x_{n}\}_{n = 1}^{\infty}$ 是 $X$ 中任一有界序列，从 $A_{1}$ 的紧性，有 $\{x_{n}\}_{n = 1}^{\infty}$ 的子序列 $\{x_{1n}\}_{n = 1}^{\infty}$ ，使 $\{A_{1}x_{1n}\}_{n = 1}^{\infty}$ 收敛。从 $A_{2}$ 的紧性，又有 $\{x_{1n}\}_{n = 1}^{\infty}$ 的子序列 $\{x_{2n}\}_{n = 1}^{\infty}$ 使 $\{A_2x_{2n}\}_{n = 1}^{\infty}$ 收敛，如此继续下去，得到一串子序列

$$
\begin{array}{l} x _ {1 1}, x _ {1 2}, \dots , x _ {1 n}, \dots , \\ x _ {2 1}, x _ {2 2}, \dots , x _ {2 n}, \dots , \\ \dots \dots \\ x _ {k 1}, x _ {k 2}, \dots , x _ {k n}, \dots , \\ \dots \dots \end{array}
$$

这里 $\left\{x_{kn}\right\}_{n=1}^{\infty}$ 是 $\left\{x_{k-1n}\right\}_{n=1}^{\infty}$ 的子序列，且 $\left\{A_{k}x_{kn}\right\}_{n=1}^{\infty}$ 收敛。将对角线上的元选出来，得到 $\left\{x_{n}\right\}_{n=1}^{\infty}$ 的子序列 $\left\{x_{nn}\right\}_{n=1}^{\infty}$ ，使对一切 $j=1,2,\cdots,\left\{A_{j}x_{nn}\right\}_{n=1}^{\infty}$ 收敛。显然

$$
\begin{array}{r l} \left\| A x _ {n n} - A x _ {m m} \right\| & \leqslant \left\| A x _ {n n} - A _ {j} x _ {n n} \right\| + \left\| A _ {j} x _ {n n} - A _ {j} x _ {m m} \right\| + \\ & \quad \left\| A _ {j} x _ {m m} - A x _ {m m} \right\| \\ & \leqslant \left\| A - A _ {j} \right\| (\left\| x _ {n n} \right\| + \left\| x _ {m m} \right\|) + \\ & \quad \left\| A _ {j} x _ {n n} - A _ {j} x _ {m m} \right\|, \end{array}
$$

由假设, 上式右端第一项趋于 0 , 当 $j \to \infty$ . 而对充分大的固定的 $j$ , 当 $n, m$ 充分大时, 右端第二项可任意小. 这说明 $\{Ax_{nn}\}_{n=1}^{\infty}$ 是 Cauchy 序列. 而 $X$ 是完备的, 故 $\{Ax_{nn}\}_{n=1}^{\infty}$ 收敛. 证毕.

例4 设 $K(x, y) \in L^2(R)$ , 这里 $R = \{(x, y) : a \leqslant x, y \leqslant b\}$ , 则算子

$$
(A f) (x) = \int_ {a} ^ {b} K (x, y) f (y) \mathrm{d} y, f = f (y) \in L ^ {2} [ a, b ],
$$

是从 $L^2 [a,b]$ 到自身的紧算子.

为证明 $A$ 是紧算子, 我们先证明如下一个结果:

设 $\{e_j\}_{j=1}^{\infty}$ 是 $L^2 [a,b]$ 的一个正规正交基(参见[6],第六章),令

$$
\varphi_ {j k} (x, y) = e _ {j} (x) \overline {{{{e _ {k} (y)}}}}, (x, y) \in R,
$$

则 $\{\varphi_{jk}:j,k=1,2,\cdots\}$ 是 $L^{2}(R)$ 的一个正规正交基.

因为

$$
\int_ {a} ^ {b} \int_ {a} ^ {b} | \varphi_ {j k} (x, y) | ^ {2} \mathrm{d} x \mathrm{d} y = \int_ {a} ^ {b} | e _ {j} (x) | ^ {2} \mathrm{d} x \int_ {a} ^ {b} | e _ {k} (y) | ^ {2} \mathrm{d} y = 1.
$$

可见 $\varphi_{jk} \in L^2(R)$ , 且 $\| \varphi_{jk} \|_2 = 1$ . 这里及以下, $\| \cdot \|_2$ 表示 $L^2(R)$ 中的范数, $\langle \cdot, \cdot \rangle$ 表示 $L^2(R)$ 中内积. 如果 $(j, k) \neq (m, n)$ , 则 $j \neq m, k \neq n$ 至少有一个成立, 于是

$$
\begin{array}{r l} \langle \varphi_ {j k}, \varphi_ {m n} \rangle & = \int_ {a} ^ {b} \int_ {a} ^ {b} \varphi_ {j k} (x, y) \overline {{\varphi_ {m n} (x , y)}} \mathrm{d} x \mathrm{d} y \\ & = \int_ {a} ^ {b} \int_ {a} ^ {b} e _ {j} (x) \overline {{e _ {k} (y)}} \overline {{e _ {m} (x)}} e _ {n} (y) \mathrm{d} x \mathrm{d} y \\ & = \int_ {a} ^ {b} e _ {j} (x) \overline {{e _ {m} (x)}} \mathrm{d} x \int_ {a} ^ {b} e _ {n} (y) \overline {{e _ {k} (y)}} \mathrm{d} y \\ & = (e _ {j}, e _ {m}) (e _ {n}, e _ {k}) \\ & = 0. \end{array}
$$

因此 $\{\varphi_{jk}:j,k=1,2,\cdots\}$ 是 $L^{2}(R)$ 中正规正交集. 如果 $\varphi\in L^{2}(R)$ ，则

$$
\int_ {a} ^ {b} \int_ {a} ^ {b} | \varphi (x, y) | ^ {2} \mathrm{d} x \mathrm{d} y <   \infty .
$$

因此对几乎所有的 $y \in [a, b]$ ，都有

$$
\int_ {a} ^ {b} | \varphi (x, y) | ^ {2} \mathrm{d} x <   \infty .
$$

记 $\varphi_y(x) = \varphi(x, y), x \in [a, b]$ ，则 $\varphi_y \in L^2[a, b]$ ，对几乎所有的 $y \in [a, b]$ . 于是

$$
f _ {j} (y) \stackrel {\mathrm{d}} {=} \left(e _ {j}, \varphi_ {y}\right) = \int_ {a} ^ {b} e _ {j} (x) \overline {{{{\varphi (x , y)}}}} \mathrm{d} x,
$$

在 $[a, b]$ 上几乎处处有定义，而且

$$
\begin{array}{r l} \int_ {a} ^ {b} | f _ {j} (y) | ^ {2} \mathrm{d} y & = \int_ {a} ^ {b} \left| \int_ {a} ^ {b} e _ {j} (x) \overline {{{{\varphi (x , y)}}}} \mathrm{d} x \right| ^ {2} \mathrm{d} y \\ & \leqslant \int_ {a} ^ {b} \left(\int_ {a} ^ {b} | e _ {j} (x) | ^ {2} \mathrm{d} x \cdot \int_ {a} ^ {b} | \varphi (x, y) | ^ {2} \mathrm{d} x\right) \mathrm{d} y \\ & \leqslant \int_ {a} ^ {b} | e _ {j} (x) | ^ {2} \mathrm{d} x \int_ {a} ^ {b} \int_ {a} ^ {b} | \varphi (x, y) | ^ {2} \mathrm{d} x \mathrm{d} y <   \infty , \end{array}
$$

即 $f_{j} \in L^{2}[a, b]$ . 又由 Parseval 公式

$$
\begin{array}{r l} \left\| f _ {j} \right\| ^ {2} & = \sum_ {k = 1} ^ {\infty} \left| \left(f _ {j}, e _ {k}\right) \right| ^ {2} \\ & = \sum_ {k = 1} ^ {\infty} \left| \int_ {a} ^ {b} f _ {j} (y) \overline {{e _ {k} (y)}} d y \right| ^ {2} \\ & = \sum_ {k = 1} ^ {\infty} \left| \int_ {a} ^ {b} \int_ {a} ^ {b} \overline {{\varphi (x , y)}} e _ {j} (x) \overline {{e _ {k} (y)}} d x d y \right| ^ {2} \\ & = \sum_ {k = 1} ^ {\infty} \left| \int_ {a} ^ {b} \int_ {a} ^ {b} \varphi_ {j k} (x, y) \overline {{\varphi (x , y)}} d x d y \right| ^ {2} \\ & = \sum_ {k = 1} ^ {\infty} | \langle \varphi_ {j k}, \varphi \rangle | ^ {2}. \end{array}
$$

于是，如果 $\langle \varphi, \varphi_{jk} \rangle = 0, j, k = 1, 2, \cdots$ 。则 $f_j = 0, j = 1, 2, \cdots$ 。从而，由 $\{e_j\}_{j=1}^{\infty}$ 是 $L^2[a, b]$ 的正规正交基可知， $\varphi_y = 0$ ，对几乎所有的 $y$ 。故 $\varphi(x, y) = 0$ ，a.e. 于 $R$ 。事实上，已知存在零测度集 $E_1 \subset [a, b]$ ，使当 $y \in E_2 = [a, b] \setminus E_1$ ，便有

$$
\varphi_ {y} (x) = 0, \mathrm{a.e.} \text {于} [ a, b ].
$$

根据Fubini定理

$$
\begin{array}{r l} \iint_ {R} | \varphi (x, y) | ^ {2} \mathrm{d} x \mathrm{d} y & = \int_ {a} ^ {b} \mathrm{d} y \int_ {a} ^ {b} | \varphi (x, y) | ^ {2} \mathrm{d} x \\ & = \int_ {E _ {1}} \mathrm{d} y \int_ {a} ^ {b} | \varphi_ {y} (x) | ^ {2} \mathrm{d} x + \int_ {E _ {2}} \mathrm{d} y \int_ {a} ^ {b} | \varphi_ {y} (x) | ^ {2} \mathrm{d} x \\ & = 0. \end{array}
$$

所以 $\varphi(x,y)=0$ , a.e. 于 R. 因此 $\{\varphi_{jk}:j,k=1,2,\cdots\}$ 是 $L^{2}(R)$ 的正规正交基.
已知 $K(x,y)\in L^{2}(R)$ ，于是存在 $\alpha_{jk}\in C,j,k=1,2,\cdots$ ，使

$$
K (x, y) = \sum_ {j, k = 1} ^ {\infty} \alpha_ {j k} \varphi_ {j k} (x, y),
$$

且

$$
\sum_ {j, k = 1} ^ {\infty} \left| \alpha_ {j k} \right| ^ {2} <   \infty .
$$

令

$$
K _ {N} (x, y) = \sum_ {j, k = 1} ^ {N} a _ {j k} \varphi_ {j k} (x, y), N = 1, 2, \dots .
$$

则

$$
\parallel K _ {N} - K \parallel_ {2} ^ {2} = \sum_ {j \text {或} k > N} | \alpha_ {j k} | ^ {2} \rightarrow 0, \text {当} N \rightarrow \infty .
$$

设

$$
(A _ {N} f) (x) = \int_ {a} ^ {b} K _ {N} (x, y) f (y) \mathrm{d} y, f = f (x) \in L ^ {2} [ a, b ],
$$

则由 $\varphi_{jk}(x,y) = e_j(x)\overline{e_k(y)}$ ，可得

$$
\begin{array}{r l} (A _ {N} f) (x) & = \int_ {a} ^ {b} \sum_ {j, k = 1} ^ {N} \alpha_ {j k} e _ {j} (x) \overline {{e _ {k} (y)}} f (y) \mathrm{d} y \\ & = \sum_ {j, k = 1} ^ {N} \alpha_ {j k} \left[ \int_ {a} ^ {b} \overline {{e _ {k} (y)}} f (y) \mathrm{d} y \right] e _ {j} (x) \\ & = \sum_ {j, k = 1} ^ {N} \alpha_ {j k} (f, e _ {k}) e _ {j} (x). \end{array}
$$

可见 $A_{N}$ 的值域包含在 $\{e_{1},\cdots,e_{N}\}$ 张成的子空间中，因而 $A_{N}$ 是有限秩算子，而由 Schwarz 不等式

$$
\begin{array}{r l} {\| (A _ {N} - A) f \| = \Big [ \int_ {a} ^ {b} | [ (A _ {N} - A) f ] (x) | ^ {2} \mathrm{d} x \Big ] ^ {1 / 2}} \\ & {\leqslant \Big [ \int_ {a} ^ {b} | \int_ {a} ^ {b} (K _ {N} (x, y) - K (x, y)) f (y) \mathrm{d} y | ^ {2} \mathrm{d} x \Big ] ^ {1 / 2}} \\ & {\leqslant \Big [ \int_ {a} ^ {b} (\int_ {a} ^ {b} | K _ {N} (x, y) - K (x, y) | ^ {2} \mathrm{d} y \cdot} \\ & {\quad \int_ {a} ^ {b} | f (y) | ^ {2} \mathrm{d} y) \mathrm{d} x \Big ] ^ {1 / 2}} \\ & {\leqslant \Big [ \int_ {a} ^ {b} \int_ {a} ^ {b} | K _ {N} (x, y) - K (x, y) | ^ {2} \mathrm{d} x \mathrm{d} y \Big ] ^ {1 / 2}.} \\ & {\quad \Big [ \int_ {a} ^ {b} | f (y) | ^ {2} \mathrm{d} y \Big ] ^ {1 / 2}} \\ & {= \| K _ {N} - K \| _ {2} \| f \|, \text {当} f \in L ^ {2} [ a, b ].} \end{array}
$$

故

$$
\parallel A _ {N} - A \parallel \leqslant \parallel K _ {N} - K \parallel_ {2} \rightarrow 0, \text {当} N \rightarrow \infty .
$$

由定理3.2, $A$ 是紧算子.

这是个关于 $L^2 [a,b]$ 上积分算子之为紧算子的很有用的简单条件.

定理3.3 设 $A$ 是紧算子, 若 $x_{n} \xrightarrow{w} x_{0}$ , 则 $Ax_{n} \to Ax_{0}$ .

证若定理不真, 则有 $\varepsilon > 0$ , 及 $\{x_{n}\}_{n=1}^{\infty}$ 的子序列 $\{x_{n_{j}}\}_{j=1}^{\infty}$ , 使

(3.1)

$$
\| A x _ {n _ {i}} - A x _ {0} \| > \varepsilon , j = 1, 2, \dots .
$$

根据第三章 §7 中命题 7.1, $\{x_{n}\}_{n=1}^{\infty}$ 是有界序列, 因 $A$ 是紧算子, 故 $\{Ax_{n_j}\}_{j=1}^{\infty}$ 有收敛子序列. 我们不妨设

(3.2)

$$
A x _ {n _ {j}} \rightarrow y _ {0}  , \text { 当 } j \rightarrow \infty  .
$$

于是，对任何 $x^{\prime}\in X^{\prime}$ ，我们有

$$
\lim _ {j \rightarrow \infty} x ^ {\prime} (A x _ {n _ {j}}) = x ^ {\prime} (y _ {0}).
$$

设 $A'$ 是 $A$ 的Banach共轭算子，则 $A'x' \in X'$ . 由 $x_{n_i} \xrightarrow{w} x_0$ , 又有

$$
\lim _ {j \rightarrow \infty} x ^ {\prime} (A x _ {n _ {j}}) = \lim _ {j \rightarrow \infty} A ^ {\prime} x ^ {\prime} (x _ {n _ {j}}) = A ^ {\prime} x ^ {\prime} (x _ {0}) = x ^ {\prime} (A x _ {0}).
$$

于是

$$
x ^ {\prime} (y _ {0}) = x ^ {\prime} (A x _ {0}).
$$

根据 Hahn-Banach 定理, 必有 $y_{0}=Ax_{0}$ . 由 (3.1) 与 (3.2) 式这不可能. 证毕.

命题3.1 设 $X$ 是无穷维Banach空间， $A \in \mathcal{H}(X)$ ，且 $A$ 是单射的，则

$$
R (A) \neq X.
$$

证否则, $R(A) = X$ . 又 $A$ 是单射的, 由 Banach 逆算子定理, $A^{-1} \in L(X)$ . 从定理 3.1,(2),

$$
I = A ^ {- 1} A \in \mathscr {K} (X),
$$

据此 $X$ 的单位球是列紧集. 由第一章 §7 中的 Riesz 引理, 必有 $\dim X < \infty$ . 这与假设矛盾. 证毕.

定理3.4 设 $A \in \mathcal{K}(X)$ , 则 $R(A)$ 是可分的.

证令 $S_{n} = \{x\in X:\| x\| \leqslant n\}, n = 1,2,\dots$ ，则

$$
R (A) = \bigcup_ {n = 1} ^ {\infty} A S _ {n}.
$$

由 $A$ 是紧算子, 点集 $AS_{n}$ 是列紧的. 根据第一章 §6 中定理 6.1 与 6.2, $AS_{n}$ 含有一个可数的稠密子集, 设其为 $D_{n}$ , 显然 $\bigcup_{n=1}^{\infty} D_{n}$ 在 $R(A)$ 中稠密, 并且是可数的. 证毕.

定理 3.5(J. Schauder, 1930) 设 $A \in \mathcal{K}(X)$ ，则其共轭算子 $A' \in \mathcal{K}(X')$ .

证设 $x_{n}^{\prime}\in X^{\prime},\| x_{n}^{\prime}\| \leqslant M,n = 1,2,\dots .$ 由定理3.4， $R(A)$ 中有一个可数的稠密子集 $D$ .利用对角线方法，可从 $\{x_n^\prime \}_{n = 1}^{\infty}$ 中抽出子序列 $\{x_{n_j}^{\prime}\}_{j = 1}^{\infty}$ ，在 $D$ 上处处收敛.当然 $\| x_{n_j}^{\prime}\| \leqslant M$ ，故 $\{x_{n_j}^{\prime}\}_{j = 1}^{\infty}$ 亦在 $\overline{R(A)}$ 上处处收敛.

任给 $x \in \overline{R(A)}$ ，令

$$
f _ {0} (x) \stackrel {\mathrm{d}} {=} \lim _ {j \rightarrow \infty} x _ {n _ {j}} ^ {\prime} (x).
$$

易见 $f_{0}$ 是线性的，又

$$
\left| x _ {n _ {j}} ^ {\prime} (x) \right| \leqslant \left\| x _ {n _ {j}} ^ {\prime} \right\| \| x \| \leqslant M \| x \|,
$$

故

$$
\mid f _ {0} (x) \mid \leqslant M \| x \|. \tag {1}
$$

可见 $f_{0}$ 是 $\overline{R(A)}$ 上有界线性泛函. 根据 Hahn-Banach 定理, $f_{0}$ 可以扩张成 $X$

上有界线性泛函 $f$ ，往证

$$
\parallel A ^ {\prime} x _ {n _ {j}} ^ {\prime} - A ^ {\prime} f \parallel \rightarrow 0, \text {当} j \rightarrow \infty .
$$

否则，有 $\eta > 0$ ，及 $\{A'x_{n_j}'\}_{j=1}^{\infty}$ 的子序列 $\{A'x_{n_k}'\}_{k=1}^{\infty}$ ，使

$$
\| A ^ {\prime} x _ {n _ {k}} ^ {\prime} - A ^ {\prime} f \| > \eta , k = 1, 2, \dots .
$$

即有 $x_{k} \in X, \|x_{k}\| = 1, k = 1, 2, \cdots$ , 使

$$
\left| A ^ {\prime} x _ {n _ {k}} ^ {\prime} \left(x _ {k}\right) - A ^ {\prime} f (x _ {k}) \right| > \eta / 2, k = 1, 2, \dots .\tag{3.3}
$$

因 $A$ 是紧算子，不妨设 $Ax_{k} \to y_{0}$ ，则 $y_{0} \in \overline{R(A)}$ 。从而

$$
\begin{array}{r l}&{\mid A ^ {\prime} x _ {n _ {k}} ^ {\prime} (x _ {k}) - A ^ {\prime} f (x _ {k}) \mid = \mid x _ {n _ {k}} ^ {\prime} (A x _ {k}) - f (A x _ {k}) \mid}\\&{\qquad \leqslant \mid x _ {n _ {k}} ^ {\prime} (A x _ {k}) - x _ {n _ {k}} ^ {\prime} (y _ {0}) \mid + \mid x _ {n _ {k}} ^ {\prime} (y _ {0}) - f _ {0} (y _ {0}) \mid +}\\&{\qquad \mid f _ {0} (y _ {0}) - f _ {0} (A x _ {k}) \mid}\\&{\qquad \leqslant (M + \| f _ {0} \|) \| A x _ {k} - y _ {0} \| +}\\&{\qquad \mid x _ {n _ {k}} ^ {\prime} (y _ {0}) - f _ {0} (y _ {0}) \mid \rightarrow 0,}\end{array}
$$

当 $k \to \infty$ . 这与(3.3)矛盾. 证毕,

E. Schmidt 首先看到下列结果, 它告诉我们紧算子是仅比有限维空间上的线性变换稍复杂的算子.

定理3.6 设 $A$ 是可分Hilbert空间 $H$ 上的紧算子，则有 $H$ 上一串有限秩算子 $A_{n}$ ，使

$$
\lim _ {n \rightarrow \infty} \| A _ {n} - A \| = 0.
$$

证设 $\{e_n\}_{n=1}^{\infty}$ 是 $H$ 的一个正规正交基, 则对任给的 $x \in H$ , 有

$$
x = \sum_ {j = 1} ^ {\infty} (x, e _ {j}) e _ {j},
$$

从而

$$
A x = \sum_ {j = 1} ^ {\infty} (A x, e _ {j}) e _ {j},
$$

对每个正整数 $n$ ，令

$$
A _ {n} x = \sum_ {j = 1} ^ {n} (A x, e _ {j}) e _ {j}, x \in H.
$$

则每个 $A_{n}$ 都是 $H$ 上有限秩线性算子. 我们断言

$$
\lim _ {n \rightarrow \infty} \| A _ {n} - A \| = 0.
$$

若不然,存在 $\varepsilon>0$ 及一串正整数 $\{n_{k}\}$ ,使

$$
\parallel A _ {n _ {k}} - A \parallel > \varepsilon , k = 1, 2, \dots .
$$

从而存在元 $x_{k} \in H, \| x_{k} \| = 1, k = 1, 2, \cdots$ , 使

$$
\parallel A _ {n _ {k}} x _ {k} - A x _ {k} \parallel > \varepsilon / 2, k = 1, 2, \dots .\tag{3.4}
$$

但 $A$ 是紧算子， $\{Ax_k\}_{k=1}^{\infty}$ 有收敛子列，不妨设 $Ax_k \to y, k \to \infty$ 。注意

$$
A _ {n _ {k}} x _ {k} - A x _ {k} = \sum_ {j = n _ {k} + 1} ^ {\infty} (A x _ {k}, e _ {j}) e _ {j},
$$

和

$$
\left(A x _ {k}, e _ {j}\right) = \left(A x _ {k} - y, e _ {j}\right) + \left(y, e _ {j}\right), j = n _ {k} + 1, n _ {k} + 2, \dots .
$$

可知

$$
\begin{array}{r l}\parallel A _ {n _ {k}} x _ {k} - A x _ {k} \parallel&= \Big [ \sum_ {j = n _ {k} + 1} ^ {\infty} | (A x _ {k}, e _ {j}) | ^ {2} \Big ] ^ {1 / 2}\\&\leqslant \Big [ \sum_ {j = n _ {k} + 1} ^ {\infty} | (A x _ {k} - y, e _ {j}) | ^ {2} \Big ] ^ {1 / 2} + \Big (\sum_ {j = n _ {k} + 1} ^ {\infty} | (y, e _ {j}) | ^ {2} \Big) ^ {1 / 2}\\&\leqslant \parallel A x _ {k} - y \parallel + \Big [ \sum_ {j = n _ {k} + 1} ^ {\infty} | (y, e _ {j}) | ^ {2} \Big ] ^ {1 / 2} \rightarrow 0, k \rightarrow \infty .\end{array}
$$

这与(3.4)式矛盾. 故 $\lim_{n\to \infty}\| A_n - A\| = 0$ . 证毕.

这个定理还可推广到所谓有基底的 Banach 空间上去.

在可分 Banach 空间 X 中, 如果有一串向量 $\{e_{j}\}_{j=1}^{\infty}$ , 使得每个 $x \in X$ 都可以唯一地表示成

$$
x = \sum_ {j = 1} ^ {\infty} \xi_ {j} e _ {j},
$$

右端级数在 $X$ 中按范数收敛，则称 $\{e_j\}_{j=1}^{\infty}$ 为 $X$ 的基，而称 $X$ 为有基底的Banach空间.

关于定理3.6在有基底的Banach空间上的推广的证明参见[11],274—275页.许多讲积分方程的书,就在这基础上把积分方程的问题转化为有限维空间上的线性变换的问题.例如H.Γ.彼得罗夫斯基的《积分方程论讲义》等.

从 S. Banach 以来, 几十年之间, 人们研究定理 3.6 对一般可分的 Banach 空间是否也是对的? 近来, P. Enflo[29] 举出反例, 说明一般是不对的. 事实上, Enflo 所得到的刚好也是可分的, 但是没有基底的 Banach 空间的例子. 现在, 最简单的反例被认为是 A. M. Davie 构造的. (参见[43], 第 297 页)

## 2. Riesz-Schauder 理论命题3.2 设 $A \in \mathcal{K}(X), \lambda \neq 0$ ，则 $\dim N(A - \lambda I) < \infty$ .

证记 $T = A - \lambda I$ ，则 $N(T)$ 是 $X$ 的子空间。设 $\{x_n\}_{n=1}^{\infty} \subset N(T)$ ，且 $\| x_n \| \leqslant 1, n = 1, 2, \cdots$ 。从 $A$ 是紧算子，应有 $\{x_n\}_{n=1}^{\infty}$ 的子序列 $\{x_{n_j}\}_{j=1}^{\infty}$ ，使 $\{Ax_{n_j}\}_{j=1}^{\infty}$ 收敛。由 $Tx_{n_j} = 0$ ，有 $x_{n_j} = \frac{1}{\lambda} Ax_{n_j}$ ，故 $\{x_{n_j}\}_{j=1}^{\infty}$ 收敛。即空间 $N(T)$ 的单位球是列紧的. 根据第一章 §7 中的定理 7.2, 即 Riesz 引理后的说明, $\dim N(T) < \infty$ . 证毕.

定理 3.7(F.Riesz,1918) 设 $A \in \mathcal{K}(X), \lambda \neq 0$ ，则 $R(A - \lambda I)$ 是闭的.

证由命题3.2及第三章§2中命题2.4,存在X的子空间M,使

$$
X = N (A - \lambda I) \oplus \mathcal {M}.
$$

设 $T: \mathcal{M} \to X$ 定义如下：

$$
T x = (A - \lambda I) x, \text {当} x \in \mathcal {M}.
$$

显然 $T \in L(\mathcal{M}, X)$ , 且 $R(A - \lambda I) = R(T)$ . 只须往证 $R(T)$ 是闭的.

易见 $T$ 在 $\mathcal{M}$ 上是单射的，还存在 $\delta > 0$ ，使

$$
\parallel T x \parallel \geqslant \delta \parallel x \parallel , \text {当} x \in \mathcal {M} .\tag{3.5}
$$

否则，存在 $\{x_{n}\}_{n=1}^{\infty}\subset M,\|x_{n}\|=1,n=1,2,\cdots$ ，使 $Tx_{n}\to0$ 。因 A 是紧算子，不妨设 $Ax_{n}\to y_{0}$ ，现在 $Ax_{n}-\lambda x_{n}=Tx_{n}\to0$ ，故 M 中的 $\lambda x_{n}\to y_{0}$ 。注意 M 是闭的，所以 $y_{0}\in M$ 。于是

$$
T y _ {0} = \lim _ {n \rightarrow \infty} T (\lambda x _ {n}) = \lim _ {n \rightarrow \infty} \lambda (T x _ {n}) = 0.
$$

因 T 是单射的，故 $y_{0}=0$ . 另一方面， $\|x_{n}\|=1, n=1,2,\cdots,\lambda\neq0$ ，故

$$
\| y _ {0} \| = \lim _ {n \rightarrow \infty} \| \lambda x _ {n} \| = | \lambda | > 0.
$$

矛盾. 所以(3.5)式成立, 从而 $R(T)$ 是闭的. 证毕.

命题3.3 设 $A \in \mathcal{H}(X)$ , 若 $N(I - A) = \{0\}$ , 则

$$
R (I - A) = X.
$$

证否则, $R(I-A)\neq X$ .令

$$
X _ {0} = X, X _ {n} = (I - A) X _ {n - 1}, n = 1, 2, \dots ,
$$

则 $X_0 \supseteq X_1$ . 假设 $X_{n-1} \supseteq X_n$ , 则必有 $X_n \supseteq X_{n+1}$ . 否则,

$$
X _ {n} = X _ {n + 1} = (I - A) X _ {n}.
$$

对于任意的 $x \in X_{n-1}, (I - A)x \in X_n$ . 从而由上面的等式, 有 $y \in X_n$ , 使

$$
(I - A) x = (I - A) y.
$$

因 $I - A$ 是单射的，故 $x = y \in X_{n}$ ，这与 $X_{n-1} \neq X_{n}$ 矛盾。根据数学归纳法有

$$
X _ {0} \supsetneqq X _ {1} \supsetneqq X _ {2} \supsetneqq \dots .
$$

根据定理 3.7, $X_{1}$ 是闭的. 从而是 A 的不变子空间. $A|X_{1}$ 仍旧是紧算子, 又由定理 3.7, $X_{2}=R(I-A|X_{1})$ 是闭的. 如此类推, 每个 $X_{n}$ 都是闭的. 根据 Riesz 引理, 存在 $x_{n}\in X_{n},\|x_{n}\|=1$ , 使

$$
\rho (x _ {n}, X _ {n + 1}) \geqslant \frac {1}{2}, n = 1, 2, \dots .
$$

对于任意自然数 $n, m, m > n$

$$
\left\| A x _ {n} - A x _ {m} \right\| = \left\| x _ {n} - \left[ \left(x _ {n} - A x _ {n}\right) - \left(x _ {m} - A x _ {m}\right) + x _ {m} \right] \right\| \geqslant \frac {1}{2},
$$

因为

$$
\left(x _ {n} - A x _ {n}\right) - \left(x _ {m} - A x _ {m}\right) + x _ {m} \in X _ {n + 1},
$$

从而 $\{Ax_{n}\}_{n = 1}^{\infty}$ 不存在收敛子序列，与 $A$ 是紧算子矛盾.证毕.

事实上, 我们可以证明, 设 $A \in \mathcal{K}(X)$ , 则对任意的 $\lambda \neq 0$ , 从 $N(\lambda I - A) = \{0\}$ 也可得,

$$
R (\lambda I - A) = X.
$$

见习题11.

引理3.1 设 $A \in \mathcal{X}(X), T = I - A, T'$ 表示 $T$ 的共轭算子，则

$$
\dim N (T ^ {\prime}) = 0 \Leftrightarrow \dim N (T) = 0.
$$

证注意, $T' = I - A'$ , 由定理 3.5, $A'$ 也是紧算子.

先证“ $\Rightarrow$ ”，根据命题3.3， $R(T') = X'$ 。于是由第三章§6中定理6.2可知

$$
N (T) = ^ {0} R \left(T ^ {\prime}\right) = ^ {0} \left(X ^ {\prime}\right) = \{0 \}.
$$

至于“ $\Leftarrow$ ”. 根据命题 3.3, $R(T) = X$ . 又根据 Banach 逆算子定理, $T$ 是有界可逆的, 再由第三章 §5 中定理 5.2, $T'$ 也是有界可逆的. 故 $N(T') = \{0\}$ . 证毕.

引理3.2 设 $\mathcal{N}$ 是 $X$ 的子空间， $\mathcal{M}'$ 是 $X'$ 的子空间。又

$$
\dim \mathcal {N} = n > 0, \dim \mathcal {M} ^ {\prime} = m > 0
$$

更设

$$
\mathcal {N} = \mathrm{S} _ {\mathrm{p}} \left\{x _ {1}, \dots , x _ {n} \right\}, \mathcal {M} ^ {\prime} = \mathrm{S} _ {\mathrm{p}} \left\{x _ {1} ^ {\prime}, \dots , x _ {m} ^ {\prime} \right\}.
$$

则存在 $x_0 \in X, x_0' \in X'$ ，使得

$$
x _ {0} ^ {\prime} (x _ {j}) = 0, \text {当} 1 \leqslant j <   n, \text {而} x _ {0} ^ {\prime} (x _ {n}) \neq 0,
$$

且

$$
x _ {j} ^ {\prime} (x _ {0}) = 0, \text {当} 1 \leqslant j <   m, \text {而} x _ {m} ^ {\prime} (x _ {0}) \neq 0.
$$

证考虑 $x_{1}, \cdots, x_{n-1}$ 生成的子空间 $X_{0}$ , 则 $x_{n} \notin X_{0}$ . 由第三章 §2 中命题 2.2 可知 $x_{0}^{\prime}$ 是存在的. 故问题只在于 $x_{0}$ 的存在性. 我们用数学归纳法来证明. 假设对 $m = l - 1 \geqslant 1$ , 这样的元存在, 则存在 $z_{1}, \cdots, z_{l-1} \in X$ , 使

$$
x _ {j} ^ {\prime} (z _ {k}) = \delta_ {j k}, 1 \leqslant j, k <   l,
$$

这里 $\delta_{jk}$ 是 Kronecker 常数. 现在, 对任何的 $x \in X$ ,

$$
\begin{array}{r l} x _ {j} ^ {\prime} \left(x - \sum_ {k = 1} ^ {l - 1} x _ {k} ^ {\prime} (x) z _ {k}\right) & = x _ {j} ^ {\prime} (x) - \sum_ {k = 1} ^ {l - 1} x _ {k} ^ {\prime} (x) x _ {j} ^ {\prime} (z _ {k}) \\ & = x _ {j} ^ {\prime} (x) - x _ {j} ^ {\prime} (x) \\ & = 0, \quad j = 1, \dots , l - 1. \end{array}
$$

如果 $x_{i}^{\prime}$ 在 $^{0}S_{p}\left\{x_{1}^{\prime},\cdots,x_{i-1}^{\prime}\right\}$ 上为 0，由上式

$$
x - \sum_ {k = 1} ^ {l - 1} x _ {k} ^ {\prime} (x) z _ {k} \in^ {0} S _ {p} \left\{x _ {1} ^ {\prime}, \dots , x _ {l - 1} ^ {\prime} \right\},
$$

故

$$
x _ {i} ^ {\prime} \left(x - \sum_ {k = 1} ^ {i - 1} x _ {k} ^ {\prime} (x) z _ {k}\right) = 0.
$$

即

$$
x _ {i} ^ {\prime} (x) = \sum_ {k = 1} ^ {i - 1} x _ {k} ^ {\prime} (x) x _ {i} ^ {\prime} (z _ {k}).
$$

从而

$$
x _ {i} ^ {\prime} = \sum_ {k = 1} ^ {i - 1} x _ {i} ^ {\prime} (z _ {k}) x _ {k} ^ {\prime}.
$$

这不可能, 因为 $\{x_{1}^{\prime},\cdots,x_{l}^{\prime}\}$ 线性无关. 所以至少有一个 $x_{0}\in^{0}S_{p}\{x_{1}^{\prime},\cdots,x_{l-1}^{\prime}\}$ , 使 $x_{l}^{\prime}(x_{0})\neq0$ . 可见对 m=l, 引理中元 $x_{0}$ 亦存在. 而对 m=1 是平凡的, 归纳法完成. 证毕.

定理3.8 设 $A \in \mathcal{K}(X)$ , 令 $T = I - A$ , 则

$$
\dim N (T) = \dim N (T ^ {\prime}) <   \infty .
$$

证注意 $T' = I - A'$ , 根据定理 3.5, $A' \in \mathcal{K}(X')$ . 又根据命题 3.2, $\dim N(T) < \infty$ , $\dim N(T') < \infty$ . 现在设 $\dim N(T) = n > 0$ , $\dim N(T') = m > 0$ , 更设

$$
\begin{array}{l} N (T) = \mathrm{S} _ {\mathrm{p}} \left\{x _ {1}, \dots , x _ {n} \right\}, \\ N (T ^ {\prime}) = \mathrm{S} _ {\mathrm{p}} \left\{x _ {1} ^ {\prime}, \dots , x _ {m} ^ {\prime} \right\}. \end{array}
$$

由引理3.2,存在 $x_0\in X$ 和 $x_0^{\prime}\in X^{\prime}$ 使

$$
x _ {0} ^ {\prime} (x _ {j}) = 0, \text {当} 1 \leqslant j <   n, \text {而} x _ {0} ^ {\prime} (x _ {n}) \neq 0,
$$

$$
x _ {j} ^ {\prime} (x _ {0}) = 0, \text {当} 1 \leqslant j <   m, \text {而} x _ {m} ^ {\prime} (x _ {0}) \neq 0.
$$

令

$$
A _ {0} x = x _ {0} ^ {\prime} (x) x _ {0}, \text {当} x \in X.
$$

则 $A_0$ 是一秩算子，故 $A_0 \in \mathcal{K}(X)$ . 又

$$
A _ {0} ^ {\prime} x ^ {\prime} (x) = x ^ {\prime} (A _ {0} x) = x _ {0} ^ {\prime} (x) x ^ {\prime} (x _ {0}), \text {当} x ^ {\prime} \in X ^ {\prime}, x \in X.
$$

于是

$$
A _ {0} ^ {\prime} x ^ {\prime} = x ^ {\prime} (x _ {0}) x _ {0} ^ {\prime}, \text {当} x ^ {\prime} \in X ^ {\prime},
$$

可见 $A_0'$ 也是一秩算子.

设 $T_{1} = T - A_{0}$ ，假定能证明

$$
\dim N (T _ {1}) = n - 1, \dim N (T _ {1} ^ {\prime}) = m - 1.\tag{3.6}
$$

因为 $T_{1} = I - (A + A_{0})$ 与 $T$ 是同类算子，而 $T_{1}$ 与 $T_{1}^{\prime}$ 的零空间维数各减少一维,重复这个步骤有限次,最后将达到如下形式算子

$$
\widetilde {T} = I - \widetilde {A}, \widetilde {A} \in \mathscr {K} (X),
$$

而且 $\dim N(\widetilde{T}) = 0$ 或 $\dim N(\widetilde{T}') = 0$ . 根据引理3.1, 它们必均为0.于是 $m = n$ , 定理得证. 因此问题在于求证(3.6)式.

设 $x \in N(T_1)$ , 从 $T_1 = T - A_0$ , 有

$$
T x = A _ {0} x = x _ {0} ^ {\prime} (x) x _ {0}.
$$

根据假设, $x_{m}^{\prime}\in N(T^{\prime})$ ,故

$$
0 = T ^ {\prime} x _ {m} ^ {\prime} (x) = x _ {m} ^ {\prime} (T x) = x _ {0} ^ {\prime} (x) x _ {m} ^ {\prime} \left(x _ {0}\right).
$$

从 $x_0$ 的选择， $x_m'(x_0) \neq 0$ ，故 $x_0'(x) = 0$ . 从而

$$
T x = 0,
$$

即 $x \in N(T)$ . 所以

$$
x = \sum_ {j = 1} ^ {n} a _ {j} x _ {j}.
$$

因而

$$
0 = x _ {0} ^ {\prime} (x) = \sum_ {j = 1} ^ {n} \alpha_ {j} x _ {0} ^ {\prime} (x _ {j}) = \alpha_ {n} x _ {0} ^ {\prime} (x _ {n}).
$$

已知 $x_0'(x_n) \neq 0$ ，所以 $\alpha_n = 0$ 。于是

$$
x = \sum_ {j = 1} ^ {n - 1} \alpha_ {j} x _ {j}.
$$

反之, 任何如此形式的 $x$ 必在 $N(T_{1})$ 中. 事实上, 首先, $x \in N(T)$ , 又

$$
x _ {0} ^ {\prime} (x) = \sum_ {j = 1} ^ {n - 1} \alpha_ {j} x _ {0} ^ {\prime} (x _ {j}) = 0,
$$

于是 $A_0x = 0$ .从而

$$
T _ {1} x = T x - A _ {0} x = 0.
$$

总之， $N(T_{1})=S_{p}\{x_{1},\cdots,x_{n-1}\}$ ，即

$$
\dim N (T _ {1}) = n - 1.
$$

下面对 $T_{1}^{\prime}$ 求证(3.6)式. 设 $x^{\prime} \in N(T_{1}^{\prime})$ , 从 $0 = T_{1}^{\prime} x^{\prime} = T^{\prime} x^{\prime} - A_{0}^{\prime} x^{\prime}$ , 可得

$$
T ^ {\prime} x ^ {\prime} = A _ {0} ^ {\prime} x ^ {\prime} = x ^ {\prime} (x _ {0}) x _ {0} ^ {\prime}.
$$

由第三章 §6 中定理 6.2, $R(T') \subset N(T)^0$ . 而 $x_n \in N(T)$ , 故

$$
0 = T ^ {\prime} x ^ {\prime} (x _ {n}) = x ^ {\prime} (x _ {0}) x _ {0} ^ {\prime} (x _ {n}).
$$

已知 $x_0'(x_n) \neq 0$ ，故 $x'(x_0) = 0$ 。从而 $T'x' = 0$ ，即 $x' \in N(T')$ 。于是

$$
x ^ {\prime} = \sum_ {j = 1} ^ {m} \beta_ {j} x _ {j} ^ {\prime}.
$$

又

$$
0 = x ^ {\prime} (x _ {0}) = \sum_ {j = 1} ^ {m} \beta_ {j} x _ {j} ^ {\prime} (x _ {0}) = \beta_ {m} x _ {m} ^ {\prime} (x _ {0}),
$$

但 $x_{m}^{\prime}(x_{0})\neq 0$ ，故 $\beta_{m} = 0.$ 于是

$$
x ^ {\prime} = \sum_ {j = 1} ^ {m - 1} \beta_ {j} x _ {j} ^ {\prime}.
$$

反之，每个形如上式的 $x'$ 必在 $N(T_{1}')$ 中，因为 $x_{j}' \in N(T')$ , $j = 1, \cdots, m - 1$ ，故 $T'x' = 0$ 。又

$$
x ^ {\prime} (x _ {0}) = \sum_ {j = 1} ^ {m - 1} \beta_ {j} x _ {j} ^ {\prime} (x _ {0}) = 0,
$$

故

$$
A _ {0} ^ {\prime} x ^ {\prime} = x ^ {\prime} (x _ {0}) x _ {0} ^ {\prime} = 0.
$$

从而

$$
T _ {1} ^ {\prime} x ^ {\prime} = T ^ {\prime} x ^ {\prime} - A _ {0} ^ {\prime} x ^ {\prime} = 0.
$$

总之， $N(T_{1}^{\prime})=S_{p}\{x_{1}^{\prime},\cdots,x_{m-1}^{\prime}\}$ ，即

$$
\dim N (T _ {1} ^ {\prime}) = m - 1.
$$

至此可见(3.6)式成立.证毕.

事实上,我们可以证明,设 $A\in\mathcal{K}(X)$ ,则对任意的 $\lambda\neq0$ ,

$$
\dim N (\lambda I - A) = \dim N (\lambda I - A ^ {\prime}) <   \infty .
$$

见习题11.

定理3.9(两择一定理）设 $A \in \mathcal{H}(X)$ ，则于任何的 $\lambda \neq 0$ ，必有

$$
\lambda \in \rho (A) \text {或} \lambda \in \sigma_ {p} (A).
$$

证若 $\lambda \notin \sigma_p(A)$ , 则 $N(\lambda I - A) = \{0\}$ . 根据命题3.3后面的说明,

$$
R (\lambda I - A) = X
$$

于是 $\lambda I - A$ 既是单射也是满射，从Banach逆算子定理， $(\lambda I - A)^{-1} \in L(X)$ . 故 $\lambda \in \rho(A)$ . 证毕.

应该指出,两择一定理是很重要的.当非齐次方程

$$
A x - \lambda x = y, \lambda \neq 0,\tag{3.7}
$$

之解唯一时,方程

$$
A x - \lambda x = 0
$$

只有零解，即 $\lambda \notin \sigma_p(A)$ . 对紧算子 $A$ ，根据两择一定理，必有 $\lambda \in \rho(A)$ . 于是对任何的 $y \in X$ ，方程(3.7)都有解. 这就看出两择一定理的威力，从方程(3.7)解的唯一性可以导出这个方程解的存在性，而唯一性往往较之存在性要容易证明些.

命题3.4 设 $A \in \mathcal{K}(X)$ , 则

$$
\sigma (A) \setminus \{0 \} = \sigma_ {p} (A) \setminus \{0 \}.
$$

证显然, $\sigma_{\rho}(A) \setminus \{0\} \subset \sigma(A) \setminus \{0\}$ . 至于相反的包含关系, 设 $\lambda \in \sigma(A) \setminus \{0\}$ , 则 $\lambda \neq 0$ , 且 $\lambda \notin \rho(A)$ . 由两择一定理便有 $\lambda \in \sigma_{\rho}(A)$ . 证毕.

命题3.5 设 $A \in \mathcal{K}(X)$ , 则 $\sigma_{p}(A)$ 没有非零的聚点.

证否则,有一串互异的非零点 $\lambda_{n}\in\sigma_{p}(A)$ , 使 $\lambda_{n}\to\lambda\neq0$ . 设 A 相应于 $\lambda_{n}$ 的特征元为 $u_{n}, n=1,2,\cdots$ .

用数学归纳法往证 $\{u_{n}\}_{n = 1}^{\infty}$ 线性无关. 设 $u_{1},\dots ,u_{n - 1}$ 线性无关，如果 $u_{1},\dots ,$ $u_{n - 1},u_n$ 线性相关，则存在不全为零的数 $c_{j},j = 1,\dots ,n - 1$ ，使

$$
u _ {n} = \sum_ {j = 1} ^ {n - 1} c _ {j} u _ {j}.
$$

从而

$$
A u _ {n} = \sum_ {j = 1} ^ {n - 1} c _ {j} A u _ {j} = \sum_ {j = 1} ^ {n - 1} c _ {j} \lambda_ {j} u _ {j}.
$$

又

$$
A u _ {n} = \lambda_ {n} u _ {n} = \sum_ {j = 1} ^ {n - 1} c _ {j} \lambda_ {n} u _ {j}.
$$

故

$$
\sum_ {j = 1} ^ {n - 1} c _ {j} \left(\lambda_ {j} - \lambda_ {n}\right) u _ {j} = 0.
$$

由假设 $u_{1},\cdots,u_{n-1}$ 线性无关，故 $c_{j}\left(\lambda_{j}-\lambda_{n}\right)=0,j=1,\cdots,n-1.$ 又 $\lambda_{j}-\lambda_{n}\neq0$ ，所以 $c_{j}=0,j=1,\cdots,n-1$ ，矛盾。所以 $u_{1},\cdots,u_{n}$ 也线性无关。

设 $M_{n}=S_{p}\{u_{1},\cdots,u_{n}\},n=1,2,\cdots$ . 则 $M_{n}\in LatA$ ，且 $M_{n-1}\subsetneq M_{n}$ . 由第一章 §7 中的 Riesz 引理，存在 $v_{n}\in M_{n},\|v_{n}\|=1$ ，且

$$
\rho (v _ {n}, \mathcal {M} _ {n - 1}) > \frac {1}{2}, n = 1, 2, \dots .
$$

注意,对 m<n,考察

$$
\frac {1}{\lambda_ {n}} A v _ {n} - \frac {1}{\lambda_ {m}} A v _ {m} = v _ {n} - \left[ \frac {1}{\lambda_ {m}} A v _ {m} - \frac {1}{\lambda_ {n}} (A - \lambda_ {n}) v _ {n} \right],\tag{3.8}
$$

从 $v_{m} \in \mathcal{M}_{m} \subset \mathcal{M}_{n-1}, \mathcal{M}_{m} \in \mathrm{Lat}A$ ，可知 $\frac{1}{\lambda_m} A v_m \in \mathcal{M}_{n-1}$ ，又 $v_n = \sum_{j=1}^{n} a_j u_j \in \mathcal{M}_n$ ，于是

$$
\left(A - \lambda_ {n}\right) v _ {n} = \sum_ {j = 1} ^ {n} a _ {j} \left(A - \lambda_ {n}\right) u _ {j} = \sum_ {j = 1} ^ {n - 1} a _ {j} \left(A - \lambda_ {n}\right) u _ {j} \in \mathcal {M} _ {n - 1},
$$

可见(3.8)式右端第二项属于 $\mathcal{M}_{n - 1}$ ，故(3.8)式右端范数不小于 $\frac{1}{2}$ .即

$$
\parallel \frac {1}{\lambda_ {n}} A v _ {n} - \frac {1}{\lambda_ {m}} A v _ {m} \parallel \geqslant \frac {1}{2} \quad \text {当} m <   n.
$$

因为 $\lambda_{n}\rightarrow\lambda\neq0,\quad\|v_{n}\|=1,n=1,2,\cdots$ ，所以 $\left\{\frac{1}{\lambda_{n}}v_{n}\right\}_{n=1}^{\infty}$ 是有界的.但从上式可见 $\left\{A(1/\lambda_{n})v_{n}\right\}_{n=1}^{\infty}$ 没有收敛子序列.这与 A 是紧算子矛盾.证毕.

定理3.10 设 $A \in \mathcal{A}(X)$ , 则 $\sigma(A)$ 没有非零聚点.

证这是命题3.4与3.5的直接推论.

从定理 3.10 可见, C 中每个环域 $\left\{\lambda:\frac{1}{n}\leqslant\left|\lambda\right|\leqslant n\right\}, n=1,2,\cdots$ 最多只含有 $\sigma(A)$ 中有限多个点, 于是 $\sigma(A)$ 最多是可数的点集.

定理3.11 设 $A \in \mathcal{X}(X), \lambda \neq 0$ ，则

(1) 存在 $x \in X$ , 使 $(A - \lambda I)x = y \Leftrightarrow y \in {}^0 N(A' - \lambda I)$ .

(2) 存在 $f \in X'$ , 使 $(A' - \lambda I)f = g \Leftrightarrow g \in N(A - \lambda I)^0$ .

证由定理3.7, $R(A - \lambda I)$ 是闭的, 又 $(A - \lambda I)' = A' - \lambda I$ . 于是根据闭值域定理(第三章 §6 中定理6.4)可知

$$
\begin{array}{l} R (A - \lambda I) = ^ {0} N (A ^ {\prime} - \lambda I), \\ R (A ^ {\prime} - \lambda I) = N (A - \lambda I) ^ {0}. \end{array}
$$

据此可见定理成立. 证毕.

综合前面的定理 3.8, 以及定理 3.11, 便有定理 3.12(Fredholm 交替定理,1900) 设 $A \in \mathcal{A}(X), \lambda \neq 0$ ，则非齐次方程
(N) $(A - \lambda I)x = y$ $((N')$ $(A' - \lambda I)f = g)$

对任给的 $y \in X (g \in X')$ 恰有一解必须且只须相对应的齐次方程 $(H)$ $(A - \lambda I)x = 0$ $((H')$ $(A' - \lambda I)f = 0)$

只有零解. 此外, 若齐次方程 $(H)$ 或 $(H')$ 中的一个有非零解, 则 $(H)$ 或 $(H')$ 有同样多的线性无关解, 即

$$
\dim N (A - \lambda I) = \dim N (A ^ {\prime} - \lambda I);
$$

非齐次方程 $(\pmb{N})((\pmb{N}^{\prime}))$ 有解必须且只须 $y(g)$ 与 $(\pmb{H}^{\prime})$ 或 $((\pmb{H}))$ 的所有解“正交”，即

$$
y \in {} ^ {0} N (A ^ {\prime} - \lambda I) (g \in N (A - \lambda I) ^ {0}).
$$

这个定理事实上相当于无穷维空间的线性代数学, 它和定理 3.9(两择一定理)及定理 3.10 合称为 Riesz-Schauder 理论. 它的背景是 Fredholm 的积分方程理论, 那里严重地依赖于行列式理论, 现在则完全摆脱了这个束缚. 原来, F. Riesz(1918) 的工作在共轭算子方面, 并没有对一般的 Banach 空间都予以证明. 以上的理论是后来由 Hildebrandt(1928) 和 Schauder(1930) 完成的. 诚如许多人的评述, Riesz 的工作是完全几何的, 无论在语言或精神上都是如此, 它也是非常精致和初等的.

例5 Fredholm第一型积分方程

$$
\int_ {a} ^ {b} K (s, t) \varphi (t) \mathrm{d} t = g (s),
$$

在外观上比之第二型积分方程似乎更接近于有限维的线性代数方程组,但是实际上却相距更远.例如于

$$
K (s, t) = \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} \sin n s \sin n t,
$$

考察算子

$$
(T x) (s) = \int_ {0} ^ {\pi} K (s, t) x (t) \mathrm{d} t, \text {当} x (t) \in L ^ {2} [ 0, \pi ].
$$

显然， $K(s,t)\in L^2 (R)$ ，这里 $R = \{(s,t):0\leqslant s,t\leqslant \pi \}$ .故由例4， $T$ 是从 $L^2 [0,$ $\pi ]$ 到自身的紧算子.令

$$
e _ {n} = e _ {n} (t) = \left(\sqrt {\frac {2}{\pi}}\right) \sin n t, n = 1, 2, \dots .
$$

容易验证， $\{e_n\}_{n=1}^{\infty}$ 是 $L^2[0, \pi]$ 的正规正交集. 设 $x = x(t) \in L^2[0, \pi]$ 与所有 $e_n$ 正交，即

$$
\int_ {0} ^ {\pi} x (t) \sin (n t) \mathrm{d} t = 0, n = 1, 2, \dots .
$$

令

$$
y (t) = \left\{ \begin{array}{l l} x (t), & t \in (0, \pi ], \\ 0, & t = 0, \\ - x (- t), & t \in [ - \pi , 0), \end{array} \right.
$$

易见 $y(t) \in L^2[-\pi, \pi]$ , 且为奇函数. 故

$$
\int_ {- \pi} ^ {\pi} y (t) d t = 0, \int_ {- \pi} ^ {\pi} y (t) \cos n t d t = 0, n = 1, 2, \dots .
$$

又

$$
\begin{array}{r l} \int_ {- \pi} ^ {\pi} y (t) \sin n t \mathrm{d} t & = 2 \int_ {0} ^ {\pi} y (t) \sin n t \mathrm{d} t \\ & = 2 \int_ {0} ^ {\pi} x (t) \sin n t \mathrm{d} t \\ & = 0, n = 1, 2, \dots , \end{array}
$$

我们知道

$$
\frac {1}{\sqrt {2 \pi}}, \frac {1}{\sqrt {\pi}} \sin t, \frac {1}{\sqrt {\pi}} \cos t, \dots , \frac {1}{\sqrt {\pi}} \sin n t, \frac {1}{\sqrt {\pi}} \cos n t, \dots
$$

是 $L^2[-\pi, \pi]$ 的一个正规正交基(参见[6], 第六章, §8), 故 $y(t) = 0$ , a.e. 于 $[- \pi, \pi]$ . 于是 $x(t) = 0$ , a.e. 于 $[0, \pi]$ . 这说明 $\{e_n\}_{n=1}^{\infty}$ 是 $L^2[0, \pi]$ 的正规正交基.注意

$$
\int_ {0} ^ {\pi} K (s, t) \sin k t \mathrm{d} t = \frac {\pi}{2 k ^ {2}} \sin k s, k = 1, 2, \dots .
$$

所以

$$
T e _ {k} = \frac {\pi}{2 k ^ {2}} e _ {k}, k = 1, 2, \dots .\tag{3.9}
$$

而对任给的 $x \in L^2[0, \pi]$ , 必有

$$
x = \sum_ {k = 1} ^ {\infty} \xi_ {k} e _ {k},
$$

从而

$$
T x = \sum_ {k = 1} ^ {\infty} \frac {\pi}{2 k ^ {2}} \xi_ {k} e _ {k}.
$$

如果 Tx=0，则 $\left(\frac{\pi}{2k^{2}}\right)\xi_{k}=0, k=1,2,\cdots$ . 从而， $x=\sum_{k=1}^{\infty}\xi_{k}e_{k}=0$ . 所以方程 Tx=0 只有零解，即 T 是单射的. 但是从命题 3.1，可不是对任何 $y\in L^{2}[0,\pi]$ ，方程 Tx=y 都有解 $x\in L^{2}[0,\pi]$ . 这与线性代数方程组迥然不同.

尽管第一型积分方程性质奇特,但它在应用中却日益重要,因此20世纪70年代中期以来,也出现一些研究这类方程的工作.(参见[32],§7.4)

3. 关于 Fredholm 算子的注记设 $A$ 是Banach空间 $X$ 上的紧算子， $\lambda \neq 0$ ，定义

$$
T = \lambda I - A.
$$

从前段定理3.7与命题3.2知道 $T$ 有下列重要性质

$$
\left\{ \begin{array}{l l} (1) R (T) \text {是闭的;} \\ (2) \dim N (T) <   \infty , \text {且} \dim N (T ^ {\prime}) <   \infty . \end{array} \right.\tag{3.10}
$$

把这抽象出来,便有下列重要概念.

定义3.4 设 $X$ 是Banach空间， $T \in L(X)$ . 如果 $T$ 具有(3.10)中的两条性质，则称 $T$ 为Fredholm算子，简记作 $T \in \mathcal{F}(X)$ . 又称

$$
\operatorname{ind} (T) \stackrel {d} {=} \dim N (T) - \dim N (T ^ {\prime})
$$

为 $T$ 的指标.

例6 对 $\ell^2$ 上的单边移位算子 $S$ :

$$
x = \{\xi_ {0}, \xi_ {1}, \xi_ {2}, \dots \} \mapsto S x = \{0, \xi_ {0}, \xi_ {1}, \xi_ {2}, \dots \}.
$$

如 §1 中 4 所证, $S^{*}$ 为

$$
y = \left\{\eta_ {0}, \eta_ {1}, \eta_ {2}, \dots \right\} \mapsto S ^ {*} y = \left\{\eta_ {1}, \eta_ {2}, \eta_ {3}, \dots \right\}.
$$

而且

$$
N (S) = \{0 \}, N (S ^ {*}) = S _ {p} \left\{e _ {0} \right\},
$$

这里 $e_{0}=\{1,0,0,\cdots\}$ . 从 S 是保范的, 我们还知道 $R(S)$ 是闭的, 故 $S \in \mathcal{F}(l^{2})$ , 且指标 $\operatorname{ind}(S) = -1$ .

根据定理 3.7 与定理 3.8, 对紧算子 A, T = I - A 是指标为 0 的 Fredholm 算子. 历史上, 从 F. Noether, T. Carlemann 到 M. Γ. Крейн, 大约都因为研究奇异积分方程而发展 Fredholm 算子理论. 例如, Крейн 就曾对 Wiener-Hopf 型积分算子

$$
(K x) (s) = \int_ {0} ^ {\infty} k (s - t) x (t) \mathrm{d} t, s \geqslant 0,
$$

其中 $k(s) \in L^{1}(-\infty, \infty)$ , 证明 $T = I + K \in \mathcal{F}(L^{2}[0, \infty])$ , 并且给出计算 $\operatorname{ind}(T)$ 的公式. 从积分方程理论和闭值域定理来看, 若 $T \in \mathcal{F}(X)$ , 则方程 $Tf = g$ 有解必须且只须 $g \in {}^{0}N(T')$ . 因此 Fredholm 算子的引进和发展是很自然的. 也确有许多重要的算子是非紧的 Fredholm 算子. 特别对 Hilbert 空间 H, $\mathcal{F}(H)$ 的理论更加丰富深刻, 例如, 这时著名的 Atkinson 定理成立 (参见 [5], § III.5), 因此许多书单就 Hilbert 空间情况讲述.

Fredholm 算子理论在 1957 年左右发展到一个高峰, 出现所谓指标定理:

设 $T \in \mathcal{F}(X)$ , 则当 $A \in \mathcal{K}(X)$ , 或者 $\| A \|$ 充分小时, $T + A \in \mathcal{F}(X)$ , 且

$$
\mathbf {i n d} (\boldsymbol {T} + \boldsymbol {A}) = \mathbf {i n d} (\boldsymbol {T}).
$$

这个稳定性定理在许多方面是重要的,特别它是求证泛函方程解之存在性的有力工具.指标定理的证明可参见[10],第三章,§4.

最后, 还该提到由于整体微分几何和物理学(例如广义相对论)的需要, 逐渐发展起流形上的偏微分方程理论. 例如, Hodge 定理说的就是紧流形上的 Laplace 方程, 利用它可以证明紧 Riemann 曲面上最基本的 Riemann-Roch 定理 (参见[4], 第三章), 而紧流形上偏微分方程所确定的一大类算子都是 Fredholm 算子. 多年来人们直接或间接致力于它们指标的研究, 终于把算子的能解性与微分流形的拓扑不变量深刻地联系起来. 具体些说, 即算子的解析指标可用拓扑不变量来表述, 这便是著名的 Atiyah-Singer 定理.

## § 4 有界自伴算子在本节中， $H$ 都表示 Hilbert 空间。

## 1. 有界自伴算子的基本性质定义4.1 对 $T \in L(H)$ , 若 $T^{*} = T$ , 则称 $T$ 为自伴算子 (或自共轭算子).

例 1 有限维欧氏空间上的 Hermite 矩阵, 显然确定一个自伴算子. 因为从第二章 §4 可知, 有限维空间上算子的 Hilbert 共轭所对应的矩阵恰好是原来算子所对应的矩阵的共轭转置.

例2 设 $K(x, y) \in L^2(S)$ , 这里 $S$ 表示正方形 $\{(x, y): 0 \leqslant x, y \leqslant 1\}$ . 如果 $K(x,y)$ 是实的，而且还是对称的，即

$$
K (x, y) = K (y, x), \text {当} (x, y) \in S.
$$

则如下定义的积分算子

$$
(T f) (x) = \int_ {0} ^ {1} K (x, y) f (y) \mathrm{d} y, f = f (x) \in L ^ {2} [ 0, 1 ],
$$

是 $L^2 [0,1]$ 上的自伴算子.参见第三章 §5 中例 2.

定理4.1 如果 $T \in L(H)$ , 则

$T$ 是自伴的 $\Leftrightarrow (Tx, x), x \in H$ , 恒为实数.

证如果 $T$ 是自伴的, 则对任何的 $x \in H$ ,

$$
(T x, x) = (x, T x) = \overline {{(T x , x)}},
$$

可见 $(Tx, x)$ 为实数.

反之，若 $(Tx, x), x \in H$ ，恒为实数，则易见

$$
(T x, x) = (x, T x), \forall x \in H.\tag{4.1}
$$

对任何 $x, y \in H$ ，通过直接验算可知

$$
\begin{array}{r l} (T x, y) & = \frac {1}{4} [ (T (x + y), x + y) - (T (x - y), x - y) ] + \\ & \quad \frac {\mathrm{i}}{4} [ (T (x + \mathrm{i} y), x + \mathrm{i} y) - (T (x - \mathrm{i} y), x - \mathrm{i} y) ], \\ (x, T y) & = \frac {1}{4} [ (x + y, T (x + y)) - (x - y, T (x - y)) ] + \\ & \quad \frac {\mathrm{i}}{4} [ (x + \mathrm{i} y, T (x + \mathrm{i} y)) - (x - \mathrm{i} y, T (x - \mathrm{i} y)) ], \end{array}
$$

利用(4.1)式,便有

$$
(T x, y) = (x, T y), \forall x, y \in H.
$$

由伴随算子的定义，

$$
(T x, y) = (x, T ^ {*} y), \forall x, y \in H.
$$

于是

$$
(x, T ^ {*} y) = (x, T y), \forall x, y \in H.
$$

故 $T^{*} = T$ .证毕.

引理4.1 对 $T \in L(H)$ , 设

$$
\mu = \sup \left\{\mid (T x, y) \mid : \| x \| = 1, \| y \| = 1 \right\},
$$

则 $\| T\| = \mu$

证显然,对任何 $x, y \in H$ ,

$$
\mid (T x, y) \mid \leqslant \mu \| x \| \| y \|,
$$

故对任意的 $x \in H$ ,

$$
\| T x \| ^ {2} = (T x, T x) \leqslant \mu \| x \| \| T x \|,
$$

从而

$$
\| T x \| \leqslant \mu \| x \|, \forall x \in H.
$$

可见 $\| T\| \leqslant \mu$

另一方面，对任意的 $x, y \in H$

$$
\left| (T x, y) \right| \leqslant \| T x \| \| y \| \leqslant \| T \| \| x \| \| y \|,
$$

可见 $\mu \leqslant \| T\|$ .证毕.

定理4.2 若 $T \in L(H)$ 是自伴的, 则

$$
\| T \| = \sup \{| (T x, x) |: \| x \| = 1 \}.
$$

证令 $M = \sup \{|(Tx, x)| : \|x\| = 1\}$ . 从引理4.1现在只须求证 $\mu \leqslant M$ . 为此我们需要在下面把 $|(Tx, y)|$ 的估计式转化为二次形式. 设 $x, y \in H$ , $\|x\| = 1$ , $\|y\| = 1$ , 则

$$
\begin{array}{r l} (T (x + y), x + y) & = (T x, x) + (T y, x) + (T x, y) + (T y, y) \\ & = (T x, x) + (y, T x) + (T x, y) + (T y, y) \\ & = (T x, x) + 2 \mathrm{Re} (T x, y) + (T y, y), \end{array}
$$

$$
(T (x - y), x - y) = (T x, x) - 2 \operatorname{Re} (T x, y) + (T y, y).
$$

从第一个式子减去第二个式子,便有

$$
4 \operatorname{Re} (T x, y) = (T (x + y), x + y) - (T (x - y), x - y).
$$

对任意的 $f \in H$ ，从 $M$ 的定义，关于二次形式 $(Tf, f)$ 有

$$
\mid (T f, f) \mid \leqslant M \| f \| ^ {2}.
$$

故由平行四边形法则，

$$
\begin{array}{r l} 4 \mathrm{Re} (T x, y) & \leqslant | (T (x + y), x + y) | + | (T (x - y), x - y) | \\ & \leqslant M (\| x + y \| ^ {2} + \| x - y \| ^ {2}) \\ & = 2 M (\| x \| ^ {2} + \| y \| ^ {2}) \\ & = 4 M. \end{array}
$$

设 $(Tx, y) = \mathrm{e}^{\mathrm{i}\theta}|(Tx, y)|$ ，在上述不等式中以 $\mathrm{e}^{-\mathrm{i}\theta}x$ 代替 $x$ ，得到

$$
\left| (T x, y) \right| = \operatorname{Re} \left| (T x, y) \right| = \operatorname{Re} e ^ {- i \theta} (T x, y) = \operatorname{Re} (T \left(e ^ {- i \theta} x\right), y) \leqslant M.
$$

从而

$$
\mu = \sup _ {\| x \| = 1, \| y \| = 1} | (T x, y) | \leqslant M.
$$

证毕.

命题4.1 设 $T \in L(H)$ , 则

$$
\| T ^ {*} T \| = \| T \| ^ {2}.
$$

证由第二章 §4 中定理 4.1 易知, $T^{*} T$ 是自伴的, 故由定理 4.2,

$$
\begin{array}{r l} \left\| T ^ {*} T \right\| & = \sup _ {\left\| x \right\| ^ {4} = 1} \left| \left(T ^ {*} T x, x\right) \right| \\ & = \sup _ {\left\| x \right\| ^ {2}} \left\| T x \right\| ^ {2} \end{array}
$$

$$
\begin{array}{l} = (\sup _ {\| x \| = 1} \| T x \|) ^ {2} \\ = \| T \| ^ {2}. \end{array}
$$

命题4.2 设 $T \in L(H)$ 是自伴的, 则

$$
r (T) = \left\| T \right\|.
$$

证由命题4.1, $\| T^2 \| = \| T \|^2$ . 利用数学归纳法可知对一切正整数 $n$ ，有

$$
\| T ^ {2 ^ {n}} \| = \| T \| ^ {2 ^ {n}}.
$$

根据定理1.7，

$$
r (T) = \lim _ {n \rightarrow \infty} \| T ^ {2 ^ {n}} \| ^ {\frac {1}{2 ^ {n}}} = \| T \|.
$$

定义4.2 设 $P$ 是Hilbert空间 $H$ 上的射影, 如果 $PH$ 与 $(I - P)H$ 是相互正交的子空间, 即 $PH$ 中任意元与 $(I - P)H$ 中每个元正交, 则称 $P$ 为正交射影.

由定义可见, 若 P 是正交射影, 则

$$
\| x \| ^ {2} = \| P x \| ^ {2} + \| (I - P) x \| ^ {2}, \forall x \in H.
$$

故 $\| P\| \leqslant 1$

命题4.3 Hilbert空间 $H$ 上的有界射影 $P$ 是正交射影当且仅当 $P$ 是自伴的.

证如果射影 $P$ 是自伴的, 则对任意的 $x, y \in H$ ,

$$
(P x, (I - P) y) = (x, P (I - P) y) = (x, 0) = 0.
$$

可见 $P$ 是正交射影.

反之，若 $P$ 是正交射影，由于任何 $x, y \in H$ ，可表示为

$$
x = x _ {1} + x _ {2}, \quad y = y _ {1} + y _ {2},
$$

其中， $x_{1},y_{1}\in PH,x_{2},y_{2}\in (I - P)H.$ 于是

$$
(P x, y) = (x _ {1}, y _ {1} + y _ {2}) = (x _ {1}, y _ {1}),
$$

$$
(x, P y) = (x _ {1} + x _ {2}, y _ {1}) = (x _ {1}, y _ {1}),
$$

故

$$
(P x, y) = (x, P y).
$$

因为 $x, y \in H$ 是任意的，可见 $P$ 是自伴的. 证毕.

定义4.3 设 $A$ 与 $B$ 都是 $H$ 上有界自伴算子, 如果

$$
(A x, x) \geqslant (B x, x), \forall x \in H.
$$

则称 $A \geqslant B$ 或 $B \leqslant A$ .

特别, 如果 A 是 H 上有界自伴算子, $A \geqslant 0$ , 则称 A 是正算子.

定理4.3 设 $P_{1}$ 与 $P_{2}$ 都是 $H$ 上正交射影，则下述命题是等价的：

(1) $P_{1} \leqslant P_{2}$ .

(2) $\| P_1x\| \leqslant \| P_2x\|$ , 当 $x \in H$ .

(3) $R(P_{1})\subset R(P_{2}).$

(4) $P_{2}P_{1} = P_{1}$ .

(5) $P_{1}P_{2} = P_{1}$ .

证从命题4.3, $H$ 上正交射影 $\pmb{P}$ 是自伴的.于是

$$
(P x, x) = \left(P ^ {2} x, x\right) = (P x, P x) = \| P x \| ^ {2}, \forall x \in H.
$$

如果 $P_{1} \leqslant P_{2}$ , 则

$$
\left\| P _ {1} x \right\| ^ {2} = \left(P _ {1} x, x\right) \leqslant \left(P _ {2} x, x\right) = \left\| P _ {2} x \right\| ^ {2}, \forall x \in H.
$$

可见(1) $\Rightarrow$ (2).

若(2)成立,取 $x \in R(P_{1})$ , 则

$$
\| x \| = \| P _ {1} x \| \leqslant \| P _ {2} x \|.
$$

因 $P_{2}$ 是正交射影， $P_{2}x \perp (I - P_{2})x$ ，故

$$
\| x \| ^ {2} = \left\| P _ {2} x \right\| ^ {2} + \left\| (I - P _ {2}) x \right\| ^ {2}.
$$

由这两个式子可见必有 $(I - P_{2})x = 0$ ，即 $x = P_{2}x\in R(P_{2})$ .所以(2) $\Rightarrow (3)$

如果(3)成立,任给 $x \in H, P_{1}x \in R(P_{1}) \subset R(P_{2})$ . 于是

$$
\left(P _ {2} P _ {1}\right) x = P _ {2} \left(P _ {1} x\right) = P _ {1} x.
$$

故 $P_{2}P_{1} = P_{1}$ .即 $(3)\Rightarrow (4)$

若 $P_{2}P_{1} = P_{1}$ ，取Hilbert共轭，则 $P_{1}^{*}P_{2}^{*} = P_{1}^{*}$ .但 $P_{1},P_{2}$ 都是自伴的，故 $P_{1}P_{2} = P_{1}$ ，所以 $(4)\Rightarrow (5)$

若 $P_{1}P_{2} = P_{1}$ ，则对任给的 $x\in H$ ，有

$$
\| P _ {1} x \| = \| P _ {1} P _ {2} x \| \leqslant \| P _ {1} \| \| P _ {2} x \| \leqslant \| P _ {2} x \|,
$$

从(1)⇒(2)的证明，

$$
\parallel P _ {j} x \parallel^ {2} = (P _ {j} x, x), j = 1, 2.
$$

故

$$
(P _ {1} x, x) \leqslant (P _ {2} x, x),
$$

即 $P_{1} \leqslant P_{2}$ . 所以 $(5) \Rightarrow (1)$ . 证毕.

定义 4.4 设 T 是 Banach 空间 X 上有界线性算子, $\lambda \in C$ . 如果 $T - \lambda I$ 不下方有界, 即不存在 $\mu > 0$ , 使

$$
\| (T - \lambda I) x \| \geqslant \mu \| x \|, \forall x \in X.
$$

则称 $\lambda$ 属于 $T$ 的近似点谱，记作 $\lambda \in \sigma_{a}(T)$

由第三章 §1 中命题 1.5,

$$
\{\lambda \in \mathbf {C} \colon T - \lambda I   \text { 下方有界 } \} \supset \rho (T).
$$

两边取余集,可见

$$
\sigma_ {a} (T) \subset \sigma (T).
$$

命题 4.4 设 X 是 Banach 空间, $T \in L(X)$ . 若有 $\{x_{n}\}_{n=1}^{\infty} \subset X$ , 使 (4.2) $Tx_{n} - \lambda x_{n} \to 0, \| x_{n} \| = 1, n = 1, 2, \cdots$ ,
则 $\lambda\in\sigma_{u}(T)$ .

证从(4.2)，显然 $T - \lambda I$ 不下方有界，故 $\lambda \in \sigma_{a}(T)$ . 证毕.

从这个命题也可以看出， $\sigma_{a}(T)$ 所以取名近似点谱的理由。

定理4.4 设 $A \in L(H)$ 是自伴算子, 则

(1) $\sigma(A)$ 位于实轴上.

(2) $\sigma_r(A) = \varnothing$ .

(3) 设 $Ax_{j} = \lambda_{j}x_{j}, x_{j} \neq 0, j = 1,2$ ，且 $\lambda_{1} \neq \lambda_{2}$ ，则 $x_{1} \perp x_{2}$ .

证先证(1). 对实的 $\lambda, \mu$ , 注意

$$
((A - \lambda I) ^ {2} x, x) = ((A - \lambda I) x, (A - \lambda I) x) = \| (A - \lambda I) x \| ^ {2},
$$

便有

$$
\begin{array}{r l} \left\| [ A - (\lambda + \mathrm{i} \mu) I ] x \right\| ^ {2} & = ([ A - (\lambda + \mathrm{i} \mu) I ] x, [ A - (\lambda + \mathrm{i} \mu) I ] x) \\ & = ([ A - (\lambda + \mathrm{i} \mu) I ] ^ {*} [ A - (\lambda + \mathrm{i} \mu) I ] x, x) \\ & = ([ A - (\lambda - \mathrm{i} \mu) I ] [ A - (\lambda + \mathrm{i} \mu) I ] x, x) \\ & = ([ (A - \lambda I) ^ {2} + \mu^ {2} I ] x, x) \\ & = \| (A - \lambda I) x \| ^ {2} + \mu^ {2} \| x \| ^ {2}. \end{array}
$$

若 $\mu \neq 0$ ，则

$$
\| [ A - (\lambda + \mathrm{i} \mu) I ] x \| \geqslant \| \mu \| \| x \|.
$$

由此可见 $A - (\lambda +\mathrm{i}\mu)I$ 是单射的，且 $R(A - (\lambda +\mathrm{i}\mu)I)$ 是闭的.

假如 $R(A - (\lambda + \mathrm{i}\mu)I) \neq H$ . 根据第二章 §4 中定理 4.2 并注意 $(A - (\lambda + \mathrm{i}\mu)I)^{*} = A - (\lambda - \mathrm{i}\mu)I$ , 有

$$
N (A - (\lambda - \mathrm{i} \mu) I) = R (A - (\lambda + \mathrm{i} \mu) I) ^ {\perp} \neq \{0 \}.
$$

这与 $A - (\lambda -\mathrm{i}\mu)I$ 是单射矛盾.故 $R(A - (\lambda +\mathrm{i}\mu)I) = H.$ 所以 $A - (\lambda +\mathrm{i}\mu)I$ 是有界可逆的，即 $\lambda +\mathrm{i}\mu \in \rho (A)$ .总之 $\sigma (A)\subset \mathbb{R}$

(2) 设 $z_0 \in \sigma_r(A)$ , 根据 (1), $z_0$ 是实数. 则 $(A - z_0I)^* = A - z_0I$ . 由于 $\overline{R(A - z_0I)} \neq H$ . 根据第二章 §4 中定理 4.2,

$$
N (A - z _ {0} I) = \overline {{{R (A - z _ {0} I)}}} ^ {\perp} \neq \{0 \}.
$$

于是 $z_0 \in \sigma_p(A)$ . 从而

$$
z _ {0} \in \sigma_ {p} (A) \cap \sigma_ {r} (A) = \varnothing ,
$$

这不可能.

至于(3). 由(1), $\lambda_{1}, \lambda_{2}$ 都是实数. 于是

$$
\begin{array}{r l} \lambda_ {1} (x _ {1}, x _ {2}) & = (\lambda_ {1} x _ {1}, x _ {2}) = (A x _ {1}, x _ {2}) \\ & = (x _ {1}, A x _ {2}) = (x _ {1}, \lambda_ {2} x _ {2}) = \lambda_ {2} (x _ {1}, x _ {2}). \end{array}
$$

已知 $\lambda_1 \neq \lambda_2$ ，必须 $(x_1, x_2) = 0$ . 证毕.

对 Hilbert 空间 $H$ 上有界自伴算子 $A$ , 由定理 4.1 和定理 4.2, 可考察

$$
m = \inf _ {\| x \| = 1} (A x, x), M = \sup _ {\| x \| = 1} (A x, x).
$$

定理4.5 设 $A \in L(H)$ 是自伴算子, 则

$$
\sigma (A) \subset [ m, M ],
$$

且 $m, M$ 都在 $\sigma(A)$ 内.

证设 $\lambda = M + d, d > 0$ ，则任给 $x \in H$

$$
\begin{array}{r l} ((A - \lambda I) x, x) & = (A x, x) - \lambda (x, x) \\ & \leqslant M (x, x) - \lambda (x, x) \\ & = - d (x, x) \leqslant 0. \end{array}
$$

因此

$$
\mid ((A - \lambda I) x, x) \mid \geqslant d \| x \| ^ {2}.
$$

另一方面

$$
\left| \left(\left(A - \lambda I\right) x, x\right) \right| \leqslant \| (A - \lambda I) x \| \| x \|. \tag {1}
$$

两个不等式联立可得

$$
\| (A - \lambda I) x \| \geqslant d \| x \|, \forall x \in H.
$$

这说明 $A - \lambda I$ 是单射的，且 $R(A - \lambda I)$ 是闭的.再根据定理4.4的(2)， $R(A - \lambda I) = H.$ 故 $\lambda \in \rho(A)$ .于是 $(M, +\infty) \subset \rho(A)$ .同法可证， $(- \infty, m) \subset \rho(A)$ .再根据定理4.4的(1)，可见

$$
\sigma (A) \subset [ m, M ].
$$

对 $\alpha > 0$ ，考察算子 $A$ 的平移 $A + \alpha I$ ，则相应的 $m, M$ 以及谱 $\sigma(A)$ 都将向右平移 $\alpha$ 。因此不妨设 $0 \leqslant m \leqslant M$ 。从定理4.2，此时， $M = \| A \|$ 。由 $M$ 的定义，有点列 $\{x_n\}_{n=1}^{\infty} \subset H$ ，使

$$
\parallel x _ {n} \parallel = 1, n = 1, 2, \dots , \text {且} (A x _ {n}, x _ {n}) \rightarrow M, \text {当} n \rightarrow \infty .
$$

于是

$$
\begin{array}{r l}{\parallel A x _ {n} - M x _ {n} \parallel^ {2} = (A x _ {n} - M x _ {n}, A x _ {n} - M x _ {n})}\\&{= \parallel A x _ {n} \parallel^ {2} - 2 M (A x _ {n}, x _ {n}) + M ^ {2} \parallel x _ {n} \parallel^ {2}}\\&{\leqslant 2 M ^ {2} - 2 M (A x _ {n}, x _ {n}) \rightarrow 0, \text {当} n \rightarrow \infty .}\end{array}
$$

由命题 4.4, $M \in \sigma_{a}(A) \subset \sigma(A)$ .

对 $\alpha < 0$ ，考察算子 $A$ 向左的平移 $A + \alpha I$ ，类似地可以证明 $m \in \sigma(A)$ .证毕.

## 2. 紧自伴算子以下恒设 $A$ 为Hilbert空间 $H$ 上非零的紧自伴算子.

命题 4.5 A 必有非零的特征值.

证否则, 由两择一定理, 一切 $\lambda \neq 0$ 都在 $\rho(A)$ 中, 于是 $r(A) = 0$ . 因为 $A$ 是自伴的, 由命题4.2, $\| A \| = r(A) = 0$ . 故 $A = 0$ , 与假设矛盾. 证毕.

定理 4.6 (Hilbert-Schmidt, 1907) H 必有一个正规正交基 $\left|\varphi_{n}\right|_{n\in J}\cup\left|\psi_{a}\right|_{a\in A}$ ，使

(1) $A\varphi_{n} = \lambda_{n}\varphi_{n},\quad \lambda_{n}\neq 0$ ，当 $n\in J,A\psi_{a} = 0$ ，当 $\alpha \in \mathcal{A}$ 这里 $J$ 是有限或可数无穷集，若 $J$ 是可数无穷集，则 $\lim_{n\to \infty}\lambda_n = 0.$

(2)对任给的 $\psi \in H$ ，有展开式

$$
A \psi = \sum_ {n \in J} \lambda_ {n} (\psi , \varphi_ {n}) \varphi_ {n}.
$$

这里的级数在 H 中按范数收敛.

证对 $A$ 的每个非零的特征值 $\lambda_{n}$ , 把与之相应的所有线性无关的特征元正规正交化, 得到一个正规正交元小组. 然后把相应于一切非零特征值的正规正交元小组放在一起, 根据定理 4.4 的 (3), 得到一个正规正交集 $\{\varphi_{n}\}_{n \in J}$ . 取 $A$ 的零空间 $N(A)$ 的一个正规正交基 $\{\psi_{a}\}_{a \in \mathcal{A}}$ . 由定理 4.4 的 (3), $\{\varphi_{n}\}_{n \in J} \cup \{\psi_{a}\}_{a \in \mathcal{A}}$ 是 $H$ 中一个正规正交集.

设

$$
\mathcal {M} = \overline {{{\mathrm{S}}}} _ {\mathrm{p}} \left\{\left. \left\{\varphi_ {n}: n \in J \right\}, \left\{\psi_ {a}: a \in \mathscr {A} \right\} \right|, \right.
$$

这里 $\overline{\mathbf{S}}_{\mathfrak{p}}$ 表示线性张开的闭包. 显然 $\mathcal{M} \in \operatorname{Lat} A$ . 若 $f \in \mathcal{M}^{\perp}$ , 则于任何 $g \in \mathcal{M}$ ,

$$
(A f, g) = (f, A g) = 0,
$$

即 $Af \in \mathcal{M}^{\perp}$ . 故 $\mathcal{M}^{\perp} \in \mathrm{Lat}A$ .

设从 $H$ 到 $\mathcal{M}^{\perp}$ 的正交射影为 $P$ , 则 $A \mid \mathcal{M}^{\perp}$ 可表示为 $PAP$ , 于是 $A \mid \mathcal{M}^{\perp}$ 也是紧自伴算子. 如果 $A \mid \mathcal{M}^{\perp}$ 非零, 由命题4.5, 有 $\lambda \neq 0$ 及 $\varphi_0 \in \mathcal{M}^{\perp}$ , $\varphi_0 \neq 0$ , 使 $(A \mid \mathcal{M}^{\perp}) \varphi_0 = \lambda \varphi_0$ . 即 $A \varphi_0 = \lambda \varphi_0$ . 根据 $\mathcal{M}$ 定义, 却有 $\varphi_0 \in \mathcal{M}$ , 矛盾. 故 $A \mid \mathcal{M}^{\perp} = 0$ . 若 $\mathcal{M}^{\perp} \neq \{0\}$ , 则 $\mathcal{M}^{\perp} \subset N(A)$ . 而由 $\mathcal{M}$ 的定义, $N(A) \subset \mathcal{M}$ . 这又发生矛盾. 故 $\mathcal{M}^{\perp} = \{0\}$ . 于是 $\{\varphi_n\}_{n \in J} \cup \{\psi_a\}_{a \in A}$ 是 $H$ 中一个正规正交基.

由定理3.10, $A$ 的非零特征值至多有可数多个. 而对每个非零特征值 $\lambda$ , 由命题3.2, $\dim N(A - \lambda I)$ 是有限的, 故 $J$ 最多是可数集. 设 $\{\lambda_n\}_{n \in J}$ 是 $A$ 之所有非零特征值 $\lambda$ 按其重数 (即 $\dim N(A - \lambda I)$ ) 重复排列得到的集合. 由定理3.10, $\{\lambda_n\}_{n \in J}$ 唯一可能聚点是0. 故当 $J$ 是可数无穷集时, $\lim_{n \to \infty} \lambda_n = 0$ . 这证出(1).

至于(2)，由第二章§2中定理2.3，对任何 $\psi\in H$ ，有展式

$$
\psi = \sum_ {n \in J} (\psi , \varphi_ {n}) \varphi_ {n} + \sum_ {\alpha \in \mathcal {A}} (\psi , \psi_ {\alpha}) \psi_ {\alpha},
$$

其中第二个级数至多有可数项非零. 这两个级数都在 $H$ 中按范数收敛. 于是利用(1)可有

$$
\begin{array}{r l} A \psi & = \sum_ {n \in J} (\psi , \varphi_ {n}) A \varphi_ {n} + \sum_ {\alpha \in \mathcal {A}} (\psi , \psi_ {\alpha}) A \psi_ {\alpha} \\ & = \sum_ {n \in J} \lambda_ {n} (\psi , \varphi_ {n}) \varphi_ {n}. \end{array}
$$

证毕.

这个定理是 Hilbert 与 Schmidt 在 1907 年左右就 $L^2$ 上积分算子的情形证明的, 至于一般情况, 则是 von Neumann 在 1929 年对可分 Hilbert 空间建立的.

## § 5 有界自伴算子的谱测度与函数演算

## 1. 有限维欧氏空间上的自伴算子设 $H$ 是 $n$ 维欧氏空间, $A \in L(H)$ 是自伴的. 如 §4 中 Hilbert-Schmidt 定理(定理 4.6)的证明, 可见 $A$ 有 $n$ 个特征向量 $\{\varphi_1, \cdots, \varphi_n\}$ 构成的 $H$ 的一个正规正交基. 设

$$
A \varphi_ {j} = \alpha_ {j} \varphi_ {j}, j = 1, \dots , n.
$$

于任何的 $x \in H$ ，有展开式

$$
x = \sum_ {j = 1} ^ {n} (x, \varphi_ {j}) \varphi_ {j}.
$$

从而

$$
A x = \sum_ {j = 1} ^ {n} \alpha_ {j} (x, \varphi_ {j}) \varphi_ {j}.
$$

在 $\{\alpha_{1},\cdots,\alpha_{n}\}$ 中可以有零，也可以有许多彼此相同的，假定其中所有互异的是 $\lambda_{1}<\lambda_{2}<\cdots<\lambda_{t}$ .不妨设

$$
\begin{array}{r l} & \alpha_ {1} = \dots = \alpha_ {k _ {1}} = \lambda_ {1}, \\ & \alpha_ {k _ {1} + 1} = \dots = \alpha_ {k _ {2}} = \lambda_ {2}, \\ & \dots \dots \\ & \alpha_ {k _ {t - 1} + 1} = \dots = \alpha_ {k _ {t}} = \alpha_ {n} = \lambda_ {t}. \end{array}
$$

对 $x \in H$ , 定义

$$
\begin{array}{l} P _ {1} x = \sum_ {j = 1} ^ {k _ {1}} (x, \varphi_ {j}) \varphi_ {j}, \\ P _ {2} x = \sum_ {j = k _ {1} + 1} ^ {k _ {2}} (x, \varphi_ {j}) \varphi_ {j}, \\ \dots \dots \end{array}
$$

$$
P _ {t} x = \sum_ {j = k _ {t - 1} + 1} ^ {k _ {t}} (x, \varphi_ {j}) \varphi_ {j}.
$$

则 $P_{j}, j=1,\cdots,t$ 是将全空间 H 投影到 A 相应于特征值 $\lambda_{j}$ 的特征子空间 $M_{j}=S_{p}\{\varphi_{k_{j-1}+1},\cdots,\varphi_{k_{j}}\}$ 上的正交射影. 因为 $M_{i}\perp M_{j}$ (即 $x\perp y, \forall x\in M_{i}, y\in M_{j}$ ), 所以 $P_{i}P_{j}=0$ , 当 $i\neq j$ . 从 $x=\sum_{j=1}^{n}(x,\varphi_{j})\varphi_{j}$ , 可见

$$
P _ {1} + P _ {2} + \dots + P _ {t} = I.
$$

现在 $A$ 可以表成

$$
A = \sum_ {j = 1} ^ {t} \lambda_ {j} P _ {j}.
$$

不妨假定

$$
m = \lambda_ {1} <   \lambda_ {2} <   \dots <   \lambda_ {t - 1} <   \lambda_ {t} = M.
$$

定义

$$
E _ {\lambda} = \left\{ \begin{array}{l l} 0, & \text {当} \lambda <   \lambda_ {1} = m, \\ P _ {1}, & \text {当} \lambda \in [ \lambda_ {1}, \lambda_ {2}), \\ P _ {1} + P _ {2}, & \text {当} \lambda \in [ \lambda_ {2}, \lambda_ {3}), \\ \dots \dots & \dots \dots \\ P _ {1} + P _ {2} + \dots + P _ {t}, & \text {当} \lambda \geqslant \lambda_ {t} = M. \end{array} \right.
$$

易见每个 $E_{\lambda}$ 都是 $H$ 上有界射影算子.

对 $[m, M]$ 的任一分划

$$
\mathscr {D}: \mu_ {0} <   m <   \mu_ {1} <   \dots <   \mu_ {h - 1} <   \mu_ {h} = M.
$$

显然

$$
E _ {\mu_ {k}} - E _ {\mu_ {k - 1}} = \sum_ {\lambda_ {j} \in (\mu_ {k - 1}, \mu_ {k} ]} P _ {j}.
$$

对任意的 $\xi_{k}\in [\mu_{k - 1},\mu_{k}]$ ，作和

$$
\sum_ {k = 1} ^ {h} \xi_ {k} \left(E _ {\mu_ {k}} - E _ {\mu_ {k - 1}}\right).
$$

设 $\| \mathcal{D}\| = \max_{1\leqslant k\leqslant h}(\mu_k - \mu_{k - 1})$ .若 $\| \mathcal{D}\| \to 0$ ，则上式趋于

$$
\sum_ {j = 1} ^ {t} \lambda_ {j} P _ {j}.
$$

总之

(5.1)

$$
A = \lim _ {\| \mathscr {D} \| \rightarrow 0} \sum_ {k = 1} ^ {h} \xi_ {k} (E _ {\mu_ {k}} - E _ {\mu_ {k - 1}}).
$$

命题5.1 上述射影算子族 $\{E_{\lambda} : -\infty < \lambda < \infty\}$ 具有下列性质：

(1) $E_{\lambda}$ 都是正交射影.

(2) $E_{\lambda}$ 单调上升，即 $E_{\lambda} \leqslant E_{\mu}$ ，当 $\lambda \leqslant \mu$

(3) $E_{\lambda}$ 是右连续的，即 $\lim_{\lambda \to 0}E_{\lambda +\epsilon} = E_{\lambda}$

(4) $E_{\lambda} = 0$ ，当 $\lambda < m, E_{\lambda} = I$ ，当 $\lambda \geqslant M$ .

证（1）由定义可见各个 $P_{j}$ 是自伴的，从而 $E_{\lambda}$ 是自伴的.根据命题4.3， $E_{\lambda}$ 是正交射影.

(2) 由 $\lambda \leqslant \mu$ 以及 $E_{\lambda}$ 定义, 可设

$$
E _ {\lambda} = P _ {0} + P _ {1} + \dots + P _ {k},
$$

$$
E _ {\mu} = P _ {0} + P _ {1} + \dots + P _ {k} + P _ {k + 1} + \dots + P _ {k + h},
$$

这里 $k, h$ 为整数且 $0 \leqslant k, h \leqslant t$ , 而 $P_0 = 0$ . 于是

$$
\begin{array}{r l} E _ {\lambda} E _ {\mu} & = (P _ {0} + P _ {1} + \dots + P _ {k}) [ (P _ {0} + P _ {1} + \dots + P _ {k}) + (P _ {k + 1} + \dots + P _ {k + h}) ] \\ & = P _ {0} + P _ {1} + \dots + P _ {k} = E _ {\lambda}. \end{array}
$$

由定理4.3可知， $E_{\lambda}\leqslant E_{\mu}$

至于(3)与(4)，从 $E_{\lambda}$ 的定义是显然的.证毕.

一般称具有命题5.1中性质的正交射影族 $\{E_{\lambda} : -\infty < \lambda < \infty\}$ 为谱族.

## 2. 有界自伴算子的谱分解定理定义5.1 设 $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 是一个谱族, $f(\lambda)$ 为 $[m, M]$ 上的连续复值函数. 若存在 $B \in L(H)$ , 对任给的 $\varepsilon > 0$ , 都有 $\delta > 0$ , 使对实轴的任意如下分划

$$
\mathscr {D}: \mu_ {0} <   m <   \mu_ {1} <   \dots <   \mu_ {h - 1} <   \mu_ {h} = M,
$$

只要 $\| \mathcal{D}\| = \max_{1\leqslant k\leqslant h}(\mu_k - \mu_{k - 1}) <   \delta$ ，便总有

$$
\left\| \sum_ {k = 1} ^ {h} f (\xi_ {k}) (E _ {\mu_ {k}} - E _ {\mu_ {k - 1}}) - B \right\| <   \varepsilon ,
$$

这里 $\xi_{k}\in [\mu_{k - 1},\mu_{k}]$ ，且 $\xi_1\geqslant m$ ，则定义积分

$$
\int_ {m - 0} ^ {M} f (\lambda) \mathrm{d} E _ {\lambda} = B.
$$

据此，(5.1)式也可表成

$$
A = \int_ {m - 0} ^ {M} \lambda \mathrm{d} E _ {\lambda}.
$$

早在 1906 年时, Hilbert 已经发现无穷维空间自伴算子的谱可以是连续的, 这样前节的离散的 Hilbert-Schmidt 定理就有必要连续化. 事实上, Hilbert 果然于 1912 年证出定理5.1(有界自伴算子的谱分解定理）设 $T \in L(H)$ 是自伴算子，

$$
m = \inf _ {\| x \| = 1} (T x, x), M = \sup _ {\| x \| = 1} (T x, x).
$$

则存在唯一的谱族 $\{E_{\lambda} : -\infty < \lambda < \infty\}$ , 使得

$$
T = \int_ {m - 0} ^ {M} \lambda \mathrm{d} E _ {\lambda}.
$$

证明参见[16], 第202—203页.

以后称这个定理中的谱族 $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 为 $T$ 的谱族，也称为 $T$ 的(算子值)谱测度.

## 3. 有界自伴算子的函数演算以下总假设 $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 是Hilbert空间 $H$ 上有界自伴算子 $T$ 的谱族.

引理5.1 任给 $x, y \in H, (E_{\lambda}x, y)$ 是 $\lambda$ 的有界变差函数，且其全变差 $\bigvee_{m=0}^{M}\{(E_{\lambda}x, y)\} \leqslant \| x \| \| y \|$ .

证任取分划

$$
\mathscr {D}: \lambda_ {0} <   m <   \lambda_ {1} <   \dots <   \lambda_ {n - 1} <   \lambda_ {n} = M,
$$

记 $E(\Delta_k) = E_{\lambda_k} - E_{\lambda_{k-1}}$ ，则当 $k \neq j$ （以 $k < j$ 为例）时，由 $E_\lambda$ 的单调上升性质与定理4.3，有

$$
\begin{array}{r l} E (\Delta_ {k}) E (\Delta_ {j}) & = (E _ {\lambda_ {k}} - E _ {\lambda_ {k - 1}}) (E _ {\lambda_ {j}} - E _ {\lambda_ {j - 1}}) \\ & = E _ {\lambda_ {k}} - E _ {\lambda_ {k - 1}} - E _ {\lambda_ {k}} + E _ {\lambda_ {k - 1}} \\ & = 0. \end{array}
$$

因此，对任意的 $x, y \in H, E(\Delta_k) x \perp E(\Delta_j) y.$ 于是，任给 $x \in H$

$$
\sum_ {k = 1} ^ {n} \left\| E \left(\Delta_ {k}\right) x \right\| ^ {2} = \left\| \sum_ {k = 1} ^ {n} E \left(\Delta_ {k}\right) x \right\| ^ {2} = \| x \| ^ {2}.
$$

由 Schwarz 不等式, 任给 $x, y \in H$ ,

$$
\begin{array}{r l} \sum_ {k = 1} ^ {n} | (E (\Delta_ {k}) x, y) | & = \sum_ {k = 1} ^ {n} | (E (\Delta_ {k}) x, E (\Delta_ {k}) y) | \\ & \leqslant \sum_ {k = 1} ^ {n} \| E (\Delta_ {k}) x \| \| E (\Delta_ {k}) y \| \\ & \leqslant \left[ \sum_ {k = 1} ^ {n} \| E (\Delta_ {k}) x \| ^ {2} \right] ^ {1 / 2} \left[ \sum_ {k = 1} ^ {n} \| E (\Delta_ {k}) y \| ^ {2} \right] ^ {1 / 2} \\ & = \| x \| \| y \|. \end{array}
$$

这说明 $(E_{\lambda}x,y)$ 是有界变差函数，且其全变差

$$
\begin{array}{r l} \bigvee_ {m = 0} ^ {M} \{(E _ {\lambda} x, y) \} & = \sup _ {\mathscr {D}} \left\{\sum_ {k = 1} ^ {n} | (E (\Delta_ {k}) x, y) | \right\} \\ & \leqslant \| x \| \| y \|. \end{array}
$$

证毕.

根据这个引理， $(E_{\lambda}x, y)$ 确定了一个标量值的Lebesgue-Stieltjes测度，这个测度称为 $T$ 的标量值谱测度。前面定义的 $\int_{m \sim 0}^{M} f(\lambda) \mathrm{d}E_{\lambda}$ 可以说是算子值的Riemann-Stieltjes积分。为了运算方便，人们便把它推广为如下的算子值的Lebesgue-Stieltjes积分。

设 $u(\lambda)$ 是定义在 $[m, M]$ 上的有界复值 Borel 函数. 于是 $u(\lambda)$ 关于 $(E_{\lambda}x, y)$ 所确定的 Lebesgue-Stieltjes 测度是可积的, 即

$$
\int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} x, y)
$$

是存在的.(关于Lebesgue-Stieltjes测度与积分参见[6],第五章,§9).令

$$
\varphi (x, y) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} x, y), x, y \in H.
$$

易见 $\varphi(x, y)$ 是 $H$ 上共轭双线性泛函，且

$$
\mid \varphi (x, y) \mid = \left| \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} x, y) \right| \leqslant K \bigvee_ {m - 0} ^ {M} \{(E _ {\lambda} x, y) \} \leqslant K \| x \| \| y \|.
$$

这里 $K$ 是 $|u(\lambda)|$ 在 $[m, M]$ 上的上确界. 这说明 $\varphi(x, y)$ 是 $H$ 上有界共轭双线性泛函，且

$$
\| \varphi \| \leqslant K.
$$

根据第二章 §3 中定理 3.3, 恰存在 $H$ 上一个有界线性算子 $A$ , 使

$$
(A x, y) = \varphi (x, y) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} x, y), x, y \in H.\tag{5.2}
$$

而且

$$
\| A \| \leqslant \| \varphi \| \leqslant K.\tag{5.3}
$$

显然 $A$ 由 $u(\lambda)$ 唯一确定，记为 $u(T)$ ，称为 $T$ 对应 $u(\lambda)$ 的算子函数。于是

$$
(u (T) x, y) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} x, y), x, y \in H.\tag{5.4}
$$

这个自伴算子函数的定义是 von Neumann 和 M. H. Stone 在 1932 年给出的。(参见[22], $126^{\circ}$ )

关于 $H$ 上自伴算子 $T$ 的函数 $u(T)$ 有如下基本性质.

定理5.2 设 $u, u_1, u_2$ 都是 $[m, M]$ 上的有界Borel函数， $\alpha \in \mathbb{C}$ . 则

(1) $(u_{1} + u_{2})(T) = u_{1}(T) + u_{2}(T)$ .

(2) $(\alpha u)(T) = \alpha[u(T)]$

(3) $(u_{1}u_{2})(T) = u_{1}(T)u_{2}(T)$ .

(4) $[u(T)]^{*} = \bar{u}(T)$ ,

这里 $\bar{u} (\lambda)$ 是 $u(\lambda)$ 的复共轭. 特别, 当 $u(\lambda)$ 是实值函数时, $u(T)$ 是自伴算子.

(5) 设 $\{u_n(\lambda)\}_{n=1}^{\infty}$ 是 $[m, M]$ 上一致有界的 Borel 函数列，且处处收敛于 $u(\lambda)$ . 则对任何 $x \in H, \{u_n(T)x\}_{n=1}^{\infty}$ 收敛于 $u(T)x$ .

(6) 当 $u(\lambda)$ 是 $[m, M]$ 上的连续函数时，

$$
u (T) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} E _ {\lambda}.
$$

证 (1), (2) 可由 (5.4) 式立即导出.

(3) 由算子函数的定义, 对任意 $x, y \in H$ ,

$$
\begin{array}{r l} (u _ {1} (T) u _ {2} (T) x, y) & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) \mathrm{d} (E _ {\lambda} u _ {2} (T) x, y) \\ & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) \mathrm{d} (u _ {2} (T) x, E _ {\lambda} y) \\ & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) \mathrm{d} \int_ {m - 0} ^ {M} u _ {2} (\mu) \mathrm{d} (E _ {\mu} x, E _ {\lambda} y) \\ & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) \mathrm{d} \left[ \int_ {m - 0} ^ {\lambda} u _ {2} (\mu) \mathrm{d} (E _ {\lambda} E _ {\mu} x, y) + \int_ {\lambda} ^ {M} u _ {2} (\mu) \mathrm{d} (E _ {\lambda} E _ {\mu} x, y) \right] \\ & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) \mathrm{d} \int_ {m - 0} ^ {\lambda} u _ {2} (\mu) \mathrm{d} (E _ {\mu} x, y) \\ & = \int_ {m - 0} ^ {M} u _ {1} (\lambda) u _ {2} (\lambda) \mathrm{d} (E _ {\lambda} x, y) \\ & = ((u _ {1} u _ {2}) (T) x, y). \end{array}
$$

故

$$
u _ {1} (T) u _ {2} (T) = \left(u _ {1} u _ {2}\right) (T).
$$

(4) 由算子函数定义, 对任意的 $x, y \in H$ ,

$$
\begin{array}{r l} (\bar {u} (T) x, y) & = \int_ {m - 0} ^ {M} \bar {u} (\lambda) \mathrm{d} (E _ {\lambda} x, y) \\ & = \int_ {m - 0} ^ {M} \bar {u} (\lambda) \mathrm{d} (x, E _ {\lambda} y) \\ & = \overline {{\int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} (E _ {\lambda} y , x)}} \\ & = \overline {{(\bar {u} (T) y , x)}} \\ & = (x, u (T) y) \\ & = ([ u (T) ] ^ {*} x, y). \end{array}
$$

故

$$
\bar {u} (T) = [ u (T) ] ^ {*}.
$$

当 $u(\lambda)$ 是实值函数， $\bar{u}(\lambda) = u(\lambda)$ . 于是

$$
u (T) = \bar {u} (T) = [ u (T) ] ^ {*},
$$

即 $u(T)$ 是自伴的.

(5) 假设 $v_{n}(\lambda) = u_{n}(\lambda) - u(\lambda)$ ，则 $\{v_{n}(\lambda)\}_{n=1}^{\infty}$ 是 $[m, M]$ 上一致有界的 Borel 函数列，且 $v_{n}(\lambda) \to 0, n \to \infty$ . 由关于 Lebesgue-Stieltjes 积分的收敛定理（参见[6]，第五章，§9），对任意的 $x \in H$ ，

$$
\int_ {m - 0} ^ {M} \mid v _ {n} (\lambda) \mid^ {2} \mathrm{d} (E _ {\lambda} x, x) \to 0, \text {当} n \to \infty .
$$

于是由性质(1)，(3)，(4)，

$$
\begin{array}{r l} {\parallel u _ {n} (T) x - u (T) x \parallel^ {2}} & {= \parallel v _ {n} (T) x \parallel^ {2}} \\ & {= (v _ {n} (T) x, v _ {n} (T) x)} \\ & {= (\left[ v _ {n} (T) \right] ^ {*} v _ {n} (T) x, x)} \\ & {= (\overline {{{v}}} _ {n} (T) v _ {n} (T) x, x)} \\ & {= (\mid v _ {n} \mid^ {2} (T) x, x)} \\ & {=  \int_ {m - 0} ^ {M} \mid v _ {n} (\lambda) \mid^ {2} \mathrm{d} (E _ {\lambda} x, x) \to 0, \text {当} n \to \infty .} \end{array}
$$

即

$$
u _ {n} (T) x \rightarrow u (T) x, \text {当} n \rightarrow \infty .
$$

(6) 对实数轴的任意如下分划

$$
\mathscr {D}: \mu_ {0} <   m <   \mu_ {1} <   \dots <   \mu_ {n - 1} <   \mu_ {n} = M.
$$

及 $\xi_{k}\in[\mu_{k-1},\mu_{k}]$ , $k=1,2,\cdots,n$ , 且 $\xi_{1}\geqslant m$ . 作函数

$u_{n}(\lambda)=u(\xi_{k})$ ，当 $\lambda\in(\mu_{k-1},\mu_{k}]$ ， $k=1,2,\cdots,n$ 。

则 $u_{n}(\lambda)$ 是 $[m, M]$ 上有界Borel函数. 而

$$
\begin{array}{r l} (u _ {n} (T) x, y) & = \int_ {m - 0} ^ {M} u _ {n} (\lambda) \mathrm{d} (E _ {\lambda} x, y) \\ & = \sum_ {k = 1} ^ {n} \int_ {\mu_ {k - 1}} ^ {\mu_ {k}} u _ {n} (\lambda) \mathrm{d} (E _ {\lambda} x, y) \\ & = \sum_ {k = 1} ^ {n} \int_ {\mu_ {k - 1}} ^ {\mu_ {k}} u (\xi_ {k}) \mathrm{d} (E _ {\lambda} x, y) \\ & = \sum_ {k = 1} ^ {n} u (\xi_ {k}) (E (\Delta_ {k}) x, y) \\ & = \left(\left[ \sum_ {k = 1} ^ {n} u (\xi_ {k}) E (\Delta_ {k}) \right] x, y\right), \end{array}
$$

对任意的 $x, y \in H$ . 所以

$$
u _ {n} (T) = \sum_ {k = 1} ^ {n} u (\xi_ {k}) E (\Delta_ {k}),
$$

这里， $E(\Delta_{k})=E_{\mu_{k}}-E_{\mu_{k-1}},k=1,\cdots,n.$

任给 $\varepsilon > 0$ ，由 $u(\lambda)$ 的一致连续性，存在 $\delta > 0$ ，使

$$
| u (\lambda) - u (\lambda^ {\prime}) | <   \varepsilon , \text {当} | \lambda - \lambda^ {\prime} | <   \delta .
$$

于是当分划 $\mathcal{D}$ 满足 $\| \mathcal{D}\| = \max_{1\leqslant k\leqslant n}(\mu_k - \mu_{k - 1}) <   \delta$ 时，

$$
\mid u (\lambda) - u _ {n} (\lambda) \mid <   \varepsilon , \forall \lambda \in [ m, M ].
$$

由(5.2)和(5.3)可得

$$
\| u (T) - u _ {n} (T) \| \leqslant \varepsilon .
$$

于是

$$
\| u (T) - \sum_ {k = 1} ^ {n} u (\xi_ {k}) E (\Delta_ {k}) \| = \| u (T) - u _ {n} (T) \| \leqslant \varepsilon .
$$

即

$$
u (T) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} E _ {\lambda}.
$$

证毕.

由这个定理容易看出, 当 $u(\lambda)$ 是 $\lambda$ 的多项式 $p(\lambda)$ 时, $u(T)$ 恰好是 T 的多项式 $p(T)$ .

现在,对任给的实数 $\lambda$ ,令

$$
e _ {\lambda} (\mu) = 1, \text {当} \mu \leqslant \lambda , e _ {\lambda} (\mu) = 0, \text {当} \mu > \lambda .
$$

则 $e_{\lambda}$ 是 $[m, M]$ 上有界Borel函数，易证

$$
E _ {\lambda} = e _ {\lambda} (T).
$$

F. Riesz 最早发现下面的结果定理5.3 存在一串一致有界的多项式 $p_n(\mu)$ ，使

$$
E _ {\lambda} x = \lim _ {n \to \infty} p _ {n} (T) x, \text {当} x \in H.
$$

证利用 Weierstrass 逼近定理可以构造出一致有界的多项式序列 $\{p_n\}_{n=1}^{\infty}$ , 使得在 $[m, M]$ 上有

$$
\lim _ {n \rightarrow \infty} p _ {n} (\mu) = e _ {\lambda} (\mu).
$$

根据定理 5.2 的(5)，对任何 $x \in H$ ，

$$
E _ {\lambda} x = e _ {\lambda} (T) x = \lim _ {n \rightarrow \infty} p _ {n} (T) x.
$$

证毕.

这个定理使得我们对谱族有一个颇为生动直观的认识,而且在不少场合,它也是方便的工具.

命题5.2 若 $C \in L(H)$ 与有界自伴算子 $T$ 可交换, 即 $CT = TC$ . 则 $C$ 与每个 $E_{\lambda}$ 亦可交换.

证根据定理 5.3, 存在一致有界的多项式序列 $\left\{p_{n}\right\}_{n=1}^{\infty}$ , 使

$$
E _ {\lambda} x = \lim _ {n \to \infty} p _ {n} (T) x, \text {当} x \in H.\tag{5.5}
$$

由假设, $CT=TC$ ,从而对每个多项式 $p_{n}$ ,有

$$
C p _ {n} (T) = p _ {n} (T) C.
$$

故对任意的 $x \in H$

$$
C p _ {n} (T) x = p _ {n} (T) C x.
$$

令 $n\to \infty$ ，由(5.5)式可得

$$
C E _ {\lambda} x = E _ {\lambda} C x.
$$

因 $x \in H$ 是任意的，故 $CE_{\lambda} = E_{\lambda}C$ . 证毕.

定理5.4 设 $T \in L(H)$ 是自伴的， $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 是 $T$ 的谱族，

$$
m = \inf _ {\| x \| = 1} (T x, x), M = \sup _ {\| x \| = 1} (T x, x).
$$

则 $\lambda_0\in \rho (T)$ 当且仅当下列情形之一成立：

(1) $\lambda_0 \notin [m, M]$ .

(2) $\lambda_0 \in [m, M]$ , 存在 $[m, M]$ 的子区间 $[\alpha, \beta]$ , 使 $\alpha < \lambda_0 < \beta$ , 且 $E_{\lambda} = E_{\alpha}$ , 当 $\lambda \in [\alpha, \beta]$ .

证充分性. 根据定理 4.5, 只须证明当 $\lambda_0$ 属于(2)的情形时, $\lambda_0 I - T$ 是有界可逆的. 这时我们可以定义实轴上连续函数

$$
u (\lambda) = \left\{ \begin{array}{l l} \frac {1}{\lambda_ {0} - \lambda}, & \text {当} \lambda \leqslant \alpha \text {或} \lambda \geqslant \beta ; \\ \text {线性函数,当} \lambda \in (\alpha , \beta). \end{array} \right.
$$

由定理 5.2 的(6), $u(T)$ 可表为

$$
u (T) = \int_ {m - 0} ^ {M} u (\lambda) \mathrm{d} E _ {\lambda}.
$$

注意， $E_{\lambda} = E_{\alpha}$ ，当 $\lambda \in [\alpha ,\beta ]$ ，于是

$$
\begin{array}{r l} (\lambda_ {0} I - T) u (T) & = u (T) (\lambda_ {0} I - T) \\ & = \int_ {m - 0} ^ {M} u (\lambda) (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} \\ & = \int_ {m - 0} ^ {\alpha} + \int_ {\alpha} ^ {\beta} + \int_ {\beta} ^ {M} u (\lambda) (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} \\ & = \int_ {m - 0} ^ {\alpha} 1 \mathrm{d} E _ {\lambda} + \int_ {\alpha} ^ {\beta} u (\lambda) (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} + \int_ {\beta} ^ {M} 1 \mathrm{d} E _ {\lambda} \\ & = E _ {\alpha} - E _ {m - 0} + 0 + E _ {M} - E _ {\beta} \\ & = I. \end{array}
$$

故 $\lambda_0 I - T$ 是有界可逆的.

必要性. 设 $\lambda_0 \in \rho(T)$ , 且 $\lambda_0 \in [m, M]$ . 由定理 $4.5, \lambda_0 \neq m, M$ . 于是可作

$[m, M]$ 的子区间 $\Delta = [\alpha, \beta]$ , 使 $\alpha < \lambda_0 < \beta$ . 记 $R_0 = R(\lambda_0, T)$ . 在

$$
\lambda_ {0} I - T = \int_ {m - 0} ^ {M} (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda}
$$

两边同时左乘以 $R_0E(\Delta)(E(\Delta) = E_\beta -E_\alpha)$ ，由命题5.2可得，

$$
\begin{array}{r l} E (\Delta) & = R _ {0} E (\Delta) \int_ {m - 0} ^ {M} (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} \\ & = R _ {0} E (\Delta) \left[ \int_ {m - 0} ^ {a} + \int_ {a} ^ {\beta} + \int_ {\beta} ^ {M} (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} \right] \\ & = R _ {0} \int_ {a} ^ {\beta} (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda}. \end{array}
$$

根据算子值积分定义,可以证明

$$
\left\| \int_ {\alpha} ^ {\beta} (\lambda_ {0} - \lambda) \mathrm{d} E _ {\lambda} \right\| \leqslant k \| E (\Delta) \|.
$$

其中 $k = \max \{\beta -\lambda_0,\lambda_0 - \alpha \}$ .于是

$$
\| E (\Delta) \| \leqslant k \| R _ {0} \| \| E (\Delta) \|.
$$

选择 $\alpha, \beta$ 充分接近 $\lambda_0$ ，可使 $k \parallel R_0 \parallel \leqslant 1/2$ ，则

$$
\| E (\Delta) \| \leqslant (1 / 2) \| E (\Delta) \|.
$$

故 $E(\Delta) = 0$ ，即 $E_{\beta} = E_{\alpha}$ . 而 $E_{\lambda}$ 是单调上升的，所以 $E_{\lambda} = E_{\alpha}$ ，当 $\lambda \in [\alpha, \beta]$ . 证毕.

定理5.5 设 $T \in L(H)$ 是自伴算子， $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 是 $T$ 的谱族，则

(1) $\lambda_0$ 是 $T$ 的特征值当且仅当 $\lambda_0$ 是 $E_{\lambda}$ 的间断点，即 $E_{\lambda_0} \neq E_{\lambda_0 - 0}$ ，当 $\lambda_0$ 是 $T$ 的特征值时， $N(\lambda_0 I - T) = R(E_{\lambda_0} - E_{\lambda_0 - 0})$ .

(2) $\sigma_r(T) = \emptyset$ .

(3) $\lambda_0 \in \sigma_c(T)$ 当且仅当 $E_{\lambda}$ 在 $\lambda_0$ 处连续，且对于满足 $\lambda_1 < \lambda_0 < \lambda_2$ 的任何实数 $\lambda_1, \lambda_2$ 都有 $E_{\lambda_1} \neq E_{\lambda_2}$ .

证先证(1)的必要性. 设 $\lambda_0$ 是 $T$ 的特征值, $x_0 \neq 0$ 是相应的特征元, 即

$$
\left(\lambda_ {0} I - T\right) x _ {0} = 0,
$$

则

$$
\int_ {m - 0} ^ {M} \mid \lambda_ {0} - \lambda \mid^ {2} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) = ((\lambda_ {0} I - T) ^ {2} x _ {0}, x _ {0}) = 0.
$$

假如 $m < \lambda_0 < M$ ，由于 $(E_{\lambda}x_0, x_0)$ 是单调上升的，被积函数是非负的，则对任意小的 $\varepsilon > 0$ ，由

$$
\int_ {m - 0} ^ {\lambda_ {0} - \varepsilon} + \int_ {\lambda_ {0} - \varepsilon} ^ {\lambda_ {0} + \varepsilon} + \int_ {\lambda_ {0} + \varepsilon} ^ {M} | \lambda_ {0} - \lambda | ^ {2} d (E _ {\lambda} x _ {0}, x _ {0}) = 0
$$

可知每一个积分都为0,于是

$$
\begin{array}{r l} 0 & = \int_ {\lambda_ {0} + \varepsilon} ^ {M} | \lambda_ {0} - \lambda | ^ {2} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) \\ & \geqslant \varepsilon^ {2} \int_ {\lambda_ {0} + \varepsilon} ^ {M} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) \\ & = \varepsilon^ {2} ((I - E _ {\lambda_ {0} + \varepsilon}) x _ {0}, x _ {0}) \\ & = \varepsilon^ {2} \| (I - E _ {\lambda_ {0} + \varepsilon}) x _ {0} \| ^ {2}. \end{array}
$$

可见 $(I - E_{\lambda_0 + \varepsilon})x_0 = 0$ ，即

(5.6)

$$
E _ {\lambda_ {0} + \varepsilon} x _ {0} = x _ {0}.
$$

又

$$
\begin{array}{r l} 0 & = \int_ {m - 0} ^ {\lambda_ {0} - \varepsilon} | \lambda_ {0} - \lambda | ^ {2} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) \\ & \geqslant \varepsilon^ {2} \int_ {m - 0} ^ {\lambda_ {0} - \varepsilon} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) \\ & = \varepsilon^ {2} (E _ {\lambda_ {0} - \epsilon} x _ {0}, x _ {0}) \\ & = \varepsilon^ {2} \| E _ {\lambda_ {0} - \epsilon} x _ {0} \| ^ {2}. \end{array}
$$

可见

(5.7)

$$
E _ {\lambda_ {0} - \epsilon} x _ {0} = 0.
$$

于是

$$
\left(E _ {\lambda_ {0} + \epsilon} - E _ {\lambda_ {0} - \epsilon}\right) x _ {0} = x _ {0}.
$$

令 $\varepsilon \to 0$ ，根据 $E_{\lambda}$ 的右连续性可得

(5.8)

$$
\left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) x _ {0} = x _ {0}.
$$

若 $\lambda_0 = M$ ，则 $E_{\lambda_0} = I$ .于是 $E_{\lambda_0}x_0 = x_0$ .从

$$
\int_ {m - 0} ^ {\lambda_ {0} - \varepsilon} + \int_ {\lambda_ {0} - \varepsilon} ^ {M} | \lambda_ {0} - \lambda | ^ {2} \mathrm{d} (E _ {\lambda} x _ {0}, x _ {0}) = 0
$$

像(5.7)一样可以证明

$$
E _ {\lambda_ {0} - \varepsilon} x _ {0} = 0.
$$

故

$$
\left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - \epsilon}\right) x _ {0} = x _ {0}.
$$

令 $\varepsilon \rightarrow 0$ ，可得

$$
\left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) x _ {0} = x _ {0}.
$$

若 $\lambda_0 = m$ ，则像(5.6)一样从

$$
\int_ {m - 0} ^ {\lambda_ {0} + \epsilon} + \int_ {\lambda_ {0} + \varepsilon} ^ {M} | \lambda_ {0} - \lambda | ^ {2} d (E _ {\lambda} x _ {0}, x _ {0}) = 0
$$

可以证明

$$
E _ {\lambda_ {0} + \epsilon} x _ {0} = x _ {0}.
$$

而 $E_{\lambda_0 - \epsilon}x_0 = 0$ ，故

$$
\left(E _ {\lambda_ {0} + \varepsilon} - E _ {\lambda_ {0} - \varepsilon}\right) x _ {0} = x _ {0}.
$$

令 $\varepsilon \to 0$ ，再次得到(5.8).因 $x_0\neq 0$ ，由(5.8)可知 $E_{\lambda_0}\neq E_{\lambda_0 - 0}$

再证(1)的充分性. 设 $\lambda_0$ 是 $E_{\lambda}$ 的间断点, 即 $E_{\lambda_0} \neq E_{\lambda_0 - 0}$ , 任取 $R(E_{\lambda_0} - E_{\lambda_0 - 0})$ 中的非零元 $x_0$ , 注意

$$
E _ {\lambda} (E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}) = E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}, \text {当} \lambda \geqslant \lambda_ {0}.
$$

由 $x_0 = (E_{\lambda_0} - E_{\lambda_0 - 0})x_0$ ，可得

$$
E _ {\lambda} x _ {0} = E _ {\lambda} \left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) x _ {0} = \left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) x _ {0} = x _ {0}.
$$

于是

$$
E _ {\lambda} x _ {0} = x _ {0}, \text {当} \lambda \geqslant \lambda_ {0}.
$$

又

$$
E _ {\lambda} \left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) = E _ {\lambda} - E _ {\lambda} = 0, \text {当} \lambda <   \lambda_ {0}.
$$

故

$$
E _ {\lambda} x _ {0} = E _ {\lambda} \left(E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}\right) x _ {0} = 0, \text {当} \lambda <   \lambda_ {0}.
$$

因此

$$
\begin{array}{r l} T x _ {0} & = \int_ {m - 0} ^ {M} \lambda \mathrm{d} E _ {\lambda} x _ {0} \\ & = \int_ {m - 0} ^ {\lambda_ {0} - 0} \lambda \mathrm{d} E _ {\lambda} x _ {0} + \lambda_ {0} x _ {0} + \int_ {\lambda_ {0}} ^ {M} \lambda \mathrm{d} E _ {\lambda} x _ {0} \\ & = \lambda_ {0} x _ {0} \end{array}
$$

这说明 $\lambda_0$ 是 $T$ 的特征值，而且所取的 $x_0$ 正是相应的特征元，即 $R(E_{\lambda_0} - E_{\lambda_0 - 0}) \subset N(\lambda_0 I - T)$ . 而在 $x_0 \in N(\lambda_0 I - T)$ 时，前已证出(5.8)式，可见 $x_0 \in R(E_{\lambda_0} - E_{\lambda_0 - 0})$ . 总之，

$$
N (\lambda_ {0} I - T) = R (E _ {\lambda_ {0}} - E _ {\lambda_ {0} - 0}).
$$

(2) 由定理 4.4 可得.

往证(3)的充分性. 根据定理 5.4, $\lambda_0 \in \sigma(T)$ . 而由上面的(1)与(2)可知 $\lambda_0 \notin \sigma_p(T) \cup \sigma_r(T)$ , 故 $\lambda_0 \in \sigma_c(T)$ .

最后，(3)的必要性. 若 $\lambda_0 \in \sigma_c(T)$ , 由定理 $5.4, \lambda_0 \in [m, M]$ . 从 $\lambda_0 \notin \sigma_p(T)$ , 由(1)可知 $E_\lambda$ 在 $\lambda_0$ 处连续, 当然 $\lambda_0 \notin \rho(T)$ , 再根据定理 5.4, 可知对任意满足 $\lambda_1 < \lambda_0 < \lambda_2$ 的实数 $\lambda_1, \lambda_2$ , 必有 $E_{\lambda_1} \neq E_{\lambda_2}$ . 证毕.

## § 6 酉算子在本节中总假定 H 是具有内积 $(\cdot,\cdot)$ 的复的 Hilbert 空间.

定义 6.1 设 U 是映 H 到 H 上的有界线性算子, 而且对任给的 $x, y \in H$ , 都有

$$
(U x, U y) = (x, y),
$$

则称 $U$ 为酉算子.

在第二章 §1 中, 我们已指出过欧氏空间中长度与角度同内积的关系, 所以酉变换 $U$ 既保持长度也保持角度不变. 它正是刚体运动在 Hilbert 空间上的推广. 而在一切酉变换之下不变的性质的研究则可看作是欧氏几何学之无穷维空间的推广. 例如, 酉算子 $U$ 把 $H$ 中的线性流形变成 $H$ 中的线性流形, 把 $H$ 的子空间 (闭线性流形) 仍变成 $H$ 的子空间.

与酉算子密切相关的是下列概念.

定义6.2 设 $T: H \to H$ 是线性算子, 如果对任给的 $x \in H$ , 都有

$$
\| T x \| = \| x \|,
$$

则称 $T$ 是保范算子.

命题 6.1 设 $T: H \rightarrow H$ 是线性算子, 则 T 是保范算子当且仅当

$$
(T x, T y) = (x, y), \forall x, y \in H.
$$

证充分性是显然的. 至于必要性, 由极化恒等式(第二章 §1 中定理 1.3), 对任意的 $x, y \in H$ ,

$$
(x, y) = \frac {1}{4} \left[ \| x + y \| ^ {2} - \| x - y \| ^ {2} + i \| x + i y \| ^ {2} - i \| x - i y \| ^ {2} \right].
$$

分别以 $Tx, Ty$ 替换 $x, y$ 由上式又可得

$$
(T x, T y) = \frac {1}{4} [ \| T (x + y) \| ^ {2} - \| T (x - y) \| ^ {2} + i \| T (x + i y) \| ^ {2} - i \| T (x - i y) \| ^ {2} ].
$$

现在 $T$ 是保范算子，对任何 $f \in H, \| Tf \| = \| f \|$ . 故由上述两个等式可知

$$
(T x, T y) = (x, y), \forall x, y \in H.
$$

证毕.

推论保范算子 T 是酉算子必须且只须 $R(T)=H$ .

命题6.2 设 $T \in L(H)$ , 则 $T$ 是酉算子当且仅当

$$
T ^ {*} = T ^ {- 1}.
$$

证设 $T$ 是酉算子, 则 $T$ 既是单射的也是满射的, 从而 $T$ 是有界可逆的. 又对任给的 $x, y \in H$ ,

$$
(x, y) = (T x, T y) = (T ^ {*} T x, y).
$$

因而

$$
T ^ {*} T = I.
$$

以 $T^{-1}$ 右乘上式两端，即得 $T^{*} = T^{-1}$

反之，若 $T^{*} = T^{-1}$ ，则 $T^{*}T = I$ ，从而

$$
(T x, T y) = (T ^ {*} T x, y) = (x, y), \forall x, y \in H.
$$

又 $TT^{*} = I$ ，表明 $T$ 是满射的.因此 $T$ 是酉算子.证毕.

例1 设 $H = L^{2}(-\infty, \infty)$ , 对任意给定的实数 $\alpha$ , 定义

$$
(T x) (t) = x (t + \alpha), \quad \text {当}   x = x (t) \in L ^ {2} (- \infty , \infty).
$$

显然，若 $x(t)\in L^2 (-\infty ,\infty)$ ，则 $x(t + \alpha)\in L^2 (-\infty ,\infty)$ ，且

$$
\| T x \| ^ {2} = \int_ {- \infty} ^ {\infty} | x (t + \alpha) | ^ {2} d t = \int_ {- \infty} ^ {\infty} | x (t) | ^ {2} d t = \| x \| ^ {2}.
$$

故 $T: L^{2}(-\infty, \infty) \to L^{2}(-\infty, \infty)$ 是保范算子. 易见 $T$ 是满射的, 所以 $T$ 是酉算子.

通常人们称如此定义的 T 为平移算子.

例2 设 $H$ 是复可分 Hilbert 空间, $\{e_n\}_{n=-\infty}^{\infty}$ 是 $H$ 的正规正交基. 若 $U \in L(H)$ 使

$$
U e _ {n} = e _ {n + 1}, \text {对一切整数} n,
$$

则称 $U$ 为双边移位算子. 如 §1,4 中一样可以证明

$$
U ^ {*} e _ {n} = e _ {n - 1}, \text {对一切整数} n,
$$

于是

$$
U ^ {*} U = U U ^ {*} = I.
$$

根据命题 6.2, U 是酉算子.

令 $H_{0}=\overline{S}_{p}\left\{e_{n}:n=0,1,2,\cdots\right\}$ ，易见 $H_{0}$ 是 U 的不变子空间。而且 $U|H_{0}$ 恰是 §1,4 中的单边移位算子 S。

例3 设 $[a, b]$ 是实轴上一个区间， $\alpha$ 是给定的实数，考察 $L^2[a, b]$ 上的乘法算子

$$
(T x) (t) = \mathrm{e} ^ {\mathrm{i} a t} x (t), \text {当} x = x (t) \in L ^ {2} [ a, b ].
$$

显然

$$
\| T x \| ^ {2} = \int_ {a} ^ {b} | e ^ {i \alpha t} x (t) | ^ {2} d t = \int_ {a} ^ {b} | x (t) | ^ {2} d t = \| x \| ^ {2}.
$$

故 $T: L^2[a, b] \to L^2[a, b]$ 是保范算子. 易见它还是满射的. 所以 $T$ 是酉算子.

例4 设 $f \in L^{2}(-\infty, \infty)$ , 定义 $f$ 的Fourier变换 $\hat{f}$ 为

$$
\hat {f} (x) = \lim _ {n \rightarrow \infty} \frac {1}{\sqrt {2 \pi}} \int_ {- n} ^ {n} f (\xi) e ^ {- i \xi x} d \xi , x \in (- \infty , \infty).
$$

由[7], 第七章, §4, 如上定义的 Fourier 变换 $f \mapsto \hat{f}$ 把 $L^2(-\infty, \infty)$ 映到整个

$L^2 (-\infty ,\infty)$ 上，而且对任意的 $f\in L^{2}(-\infty ,\infty)$ 都有

$$
\| \hat {f} \| = \| f \|.
$$

因此,若定义算子 U 为

$$
U f = \hat {f}, \text {当} f \in L ^ {2} (- \infty , \infty),
$$

则 $U$ 是酉算子.

这个例子表明,重要的 Fourier 变换正是从 $L^{2}(-\infty,\infty)$ 到自身的酉算子.

命题6.3 $H$ 上全体酉算子 $\mathcal{U}$ 构成一个群.

证显然 $I \in \mathcal{U}$ , 若 $U \in \mathcal{U}$ , 则由命题6.2, $U^{*} = U^{-1}$ . 从而

$$
\left(U ^ {- 1}\right) ^ {*} = \left(U ^ {*}\right) ^ {- 1} = \left(U ^ {- 1}\right) ^ {- 1}.
$$

故由命题6.2, $U^{-1} \in \mathcal{U}$ . 此外, 对 $U_{1}, U_{2} \in \mathcal{U}$ , 由命题6.2,

$$
\left(U _ {2} U _ {1}\right) ^ {*} = U _ {1} ^ {*} U _ {2} ^ {*} = U _ {1} ^ {- 1} U _ {2} ^ {- 1} = \left(U _ {2} U _ {1}\right) ^ {- 1}
$$

所以 $U_{2}U_{1}\in \mathcal{U}$ .总之， $\mathcal{U}$ 是个群.证毕.

如同群论一样, 非常重要的是, 如用群 $\mathcal{U}$ 中的一个元 $U$ 去变换一个算子 $T$ , 成为 $\tilde{T} = U^{-1} TU$ , 可以证明, $T$ 的许多性质都为 $\tilde{T}$ 所保留. 因此, 可以通过 $\tilde{T}$ 来研究 $T$ . 这将在自伴算子的理论中充分地展示出来. 一般称上述的 $\tilde{T}$ 与 $T$ 相互酉等价.

例5 设 $T, U \in L(H), U$ 是酉算子, $\tilde{T} = U^{-1} TU$ . 如果 $\lambda_0$ 是 $T$ 的特征值, 则 $\lambda_0$ 也是 $\tilde{T}$ 的特征值.

设 $x \neq 0$ 使 $Tx = \lambda_0 x$ . 令 $y = U^{-1} x$ , 则

$$
\tilde {T} y = \left(U ^ {- 1} T U\right) U ^ {- 1} x = U ^ {- 1} T x = \lambda_ {0} U ^ {- 1} x = \lambda_ {0} y.
$$

例6 设 $T, U \in L(H), U$ 是酉算子, $\tilde{T} = U^{-1} TU$ . 如果 $T$ 是自伴算子, 则 $\tilde{T}$ 也是自伴算子.

因为 $T^{*} = T$ ，于是由 $U^{*} = U^{-1}$ 可知

$$
(\tilde {T}) ^ {*} = (U ^ {- 1} T U) ^ {*} = U ^ {*} T ^ {*} (U ^ {- 1}) ^ {*} = U ^ {- 1} T U = \tilde {T}.
$$

以下设 $\{\varphi_i\}_{i=1}^{\infty}, \{\psi_j\}_{j=1}^{\infty}$ 是 $H$ 的两组正规正交基. 则于任给的向量 $x \in H$ , 设它在 $\{\varphi_i\}_{i=1}^{\infty}$ 之下的坐标为

$$
a _ {i} = (x, \varphi_ {i}), i = 1, 2, \dots .
$$

而在 $\{\psi_j\}_{j=1}^{\infty}$ 之下的坐标为

$$
b _ {j} = (x, \psi_ {j}), j = 1, 2, \dots .
$$

命题6.4 $x$ 之两组坐标的联系是

$$
b _ {j} = \sum_ {k = 1} ^ {\infty} \bar {u} _ {j k} a _ {k}, \quad j = 1, 2, \dots .
$$

其中 $U = (u_{ij})$ 是酉矩阵，即按矩阵乘法有

$$
U U ^ {*} = U ^ {*} U = I,
$$

这里 $U^{*}$ 是 $U$ 的转置共轭矩阵.

证设

$$
\psi_ {j} = \sum_ {k = 1} ^ {\infty} u _ {j k} \varphi_ {k}, j = 1, 2, \dots .
$$

这里

$$
u _ {j k} = \left(\psi_ {j}, \varphi_ {k}\right), j, k = 1, 2, \dots .
$$

则

$$
b _ {j} = (x, \psi_ {j}) = (x, \sum_ {k = 1} ^ {\infty} u _ {j k} \varphi_ {k}) = \sum_ {k = 1} ^ {\infty} \bar {u} _ {j k} (x, \varphi_ {k}) = \sum_ {k = 1} ^ {\infty} \bar {u} _ {j k} a _ {k}.
$$

往证 $U = (u_{ij})$ 是酉矩阵.对任意的正整数 $m,n$

$$
\delta_ {m n} = (\psi_ {m}, \psi_ {n}) = \left(\sum_ {k = 1} ^ {\infty} u _ {m k} \varphi_ {k}, \sum_ {k = 1} ^ {\infty} u _ {n k} \varphi_ {k}\right) = \sum_ {k = 1} ^ {\infty} u _ {m k} \bar {u} _ {n k},
$$

这里 $\delta_{mn}$ 是 Kronecker 常数. 设 $U^{*} = (u_{ij}^{*})$ , 由 $U^{*}$ 是 $U$ 的转置共轭矩阵, 有 $u_{ij}^{*} = \overline{u}_{ji}$ . 故按无穷矩阵乘法(参见第二章 §4,3) $UU^{*}$ 的第 $m$ 行第 $n$ 列的元为

$$
\left(U U ^ {*}\right) _ {m n} = \sum_ {k = 1} ^ {\infty} u _ {m k} u _ {k n} ^ {*} = \sum_ {k = 1} ^ {\infty} u _ {m k} \bar {u} _ {n k} = \delta_ {m n}.
$$

所以， $UU^{*} = I$

设

$$
\varphi_ {i} = \sum_ {k = 1} ^ {\infty} v _ {i k} \psi_ {k}, i = 1, 2, \dots .
$$

其中

$$
v _ {i j} = \left(\varphi_ {i}, \psi_ {j}\right) = \overline {{\left(\psi_ {j} , \varphi_ {i}\right)}} = \bar {u} _ {j i},
$$

则

$$
\begin{array}{r l} \delta_ {m n} & = (\varphi_ {m}, \varphi_ {n}) ^ {\prime} = \left(\sum_ {k = 1} ^ {\infty} v _ {m k} \psi_ {k}, \sum_ {k = 1} ^ {\infty} v _ {n k} \psi_ {k}\right) \\ & = \sum_ {k = 1} ^ {\infty} v _ {m k} \bar {v} _ {n k} = \sum_ {k = 1} ^ {\infty} \bar {u} _ {k m} u _ {k n}. \end{array}
$$

如前

$$
\left(U ^ {*} U\right) _ {m n} = \sum_ {k = 1} ^ {\infty} u _ {m k} ^ {*} u _ {k n} = \sum_ {k = 1} ^ {\infty} \bar {u} _ {k m} u _ {k n} = \delta_ {m n}.
$$

故 $U^{*}U = I$ .证毕.

设 $T \in L(H)$ , 一般定义 $T$ 在 $\{\varphi_i\}_{i=1}^{\infty}$ 与 $\{\psi_j\}_{j=1}^{\infty}$ 下的表示矩阵为

$$
A = \left(\left(T \varphi_ {j}, \varphi_ {k}\right)\right) _ {j, k = 1} ^ {\infty}, B = \left(\left(T \psi_ {j}, \psi_ {k}\right)\right) _ {j, k = 1} ^ {\infty},
$$

可以证明命题 6.5 存在酉矩阵 U, 使

$$
B = U ^ {- 1} A U.
$$

证明可参见[41], § III.1中定理3.1的证明.

以上这两个命题表示向量在不同基底下坐标之间与算子在不同基底下矩阵表示之间的关系都可以通过酉矩阵(或酉算子)表达出来. 它们正是量子力学中表象理论的数学概括和解释.

命题6.6 $T \in L(H)$ 是酉算子当且仅当 $T^{*}$ 是酉算子.

证根据命题6.2，

$T$ 是酉算子 $\Leftrightarrow T^{*} = T^{-1}$

$$
\Leftrightarrow (T ^ {*}) ^ {*} = (T ^ {- 1}) ^ {*} = (T ^ {*}) ^ {- 1}
$$

$\Leftrightarrow T^{*}$ 是酉算子.

证毕.

定理6.1 设 $U \in L(H)$ 是酉算子, 则

$$
\sigma (U) \subset \{\lambda \in \mathbf {C}: | \lambda | = 1 \}.
$$

证设 $|\lambda| < 1$ ，则对任给的 $x \in H$

$$
\begin{array}{r l} \parallel (U - \lambda I) x \parallel & \geqslant \parallel U x \parallel - \parallel \lambda x \parallel \\ & = \parallel x \parallel - \mid \lambda \mid \parallel x \parallel \\ & = (1 - \mid \lambda \mid) \parallel x \parallel , \end{array}
$$

可见 $U - \lambda I$ 是单射的，且 $R(U - \lambda I)$ 是闭的.

由命题 6.6, $U^{*}$ 也是酉算子. 因此, $U^{*}-\bar{\lambda}I=(U-\lambda I)^{*}$ 也是单射的, 根据第二章 §4 中定理 4.2,

$$
R (U - \lambda I) = N ((U - \lambda I) ^ {*}) ^ {\perp} = \{0 \} ^ {\perp} = H.
$$

故 $U - \lambda I$ 是有界可逆的，即 $\lambda \in \rho(U)$

由定理1.7, $U$ 的谱半径 $r(U) \leqslant \| U \| = 1$ , 故当 $|\lambda| > 1$ 时, 必有 $\lambda \in \rho(U)$ . 总之,

$$
\sigma (U) \subset \{\lambda \in \mathbf {C}: | \lambda | = 1 \}.
$$

证毕.

定义6.3 设 $A \in L(H)$ 是自伴算子, 则

$$
U = (A + \mathrm{i} I) (A - \mathrm{i} I) ^ {- 1}
$$

称为 $A$ 的Cayley变换.

定理6.2 设 $A \in L(H)$ 是自伴算子, 则 $A$ 的Cayley变换 $U$ 是酉算子. 证设

$$
f (t) = (t + \mathrm{i}) (t - \mathrm{i}) ^ {- 1}, - \infty <   t <   \infty .
$$

则 $f$ 是实轴上的连续函数. 而且

$$
\bar {f} (t) = \overline {{(t + \mathrm{i}) (t - \mathrm{i})}} ^ {- 1} = (t - \mathrm{i}) (t + \mathrm{i}) ^ {- 1} = \frac {1}{f (t)}.
$$

根据自伴算子函数演算(定理 5.2)，

$$
U = f (A),
$$

而且

$$
U ^ {*} = \overline {{{f}}} (A) = [ f (A) ] ^ {- 1} = U ^ {- 1}.
$$

故 $U$ 是酉算子. 证毕.

## 习题

1. 设 $S$ 是 Hilbert 空间 $H$ 上单边移位算子 (见第四章 §1 第 4 小节), $R_{\lambda} = R(\lambda, S)$ 表示 $S$ 的预解式. 试证明

$$
\parallel R _ {\lambda} \parallel = (| \lambda | - 1) ^ {- 1}, \text {当} | \lambda | > 1.
$$

2. 设 $X$ 是 Banach 空间, $T_{1}, T_{2} \in L(X)$ , 且 $T_{1}T_{2} = T_{2}T_{1}$ . 如果 $\lambda \in \rho(T_{1}) \cap \rho(T_{2})$ , 则

$$
R (\lambda , T _ {1}) - R (\lambda , T _ {2}) = (T _ {1} - T _ {2}) R (\lambda , T _ {1}) R (\lambda , T _ {2}),
$$

这个等式称为第二预解公式. 试证明之.

3. 设 $X$ 是 Banach 空间, $T \in L(X), \alpha \in \rho(T), A = R(\alpha, T)$ , 证明:

(1) 如果 $\lambda, \mu \in \mathbf{C}$ , 使 $\mu(\alpha - \lambda) = 1$ , 则 $\mu \in \sigma(A)$ 当且仅当 $\lambda \in \sigma(T)$ .

(2) 如果 $\mu \in \rho(A)$ , 且 $\mu(\alpha - \lambda) = 1$ , 则

$$
R (\mu , A) = 1 / \mu + (1 / \mu^ {2}) R (\lambda , T).
$$

4. 设 $X$ 是 Banach 空间, $\{T_n\}_{n=1}^{\infty} \subset L(X), T \in L(X), \| T_n - T \| \to 0$ , 当 $n \to \infty$ . 试证明, 如果 $\lambda_0 \in \rho(T)$ , 则当 $n$ 充分大时, $\lambda_0 \in \rho(T_n)$ , 且

$$
\lim _ {n \rightarrow \infty} \left(\lambda_ {0} I - T _ {n}\right) ^ {- 1} = \left(\lambda_ {0} I - T\right) ^ {- 1}.
$$

5. 设 $X$ 是 Banach 空间, $T \in L(X)$ , $n$ 是正整数, $\lambda_0$ 是 $T^n$ 的特征值, 则必存在 $\lambda_0$ 的某个 $n$ 次根是 $T$ 的特征值.

6. 设 $F$ 是复平面上有界的无穷闭集. $\{\alpha_{n}\}_{n=1}^{\infty}$ 是 $F$ 的一个可数稠密子集, 在 $t^{l}$ 中定义算子 $T$ 为

$$
y = T x: y = \left\{\alpha_ {n} \xi_ {n} \right\}, x = \left\{\xi_ {n} \right\}.
$$

试证明：

(1) T 是从 $t^{1}$ 到 $t^{1}$ 的有界线性算子.

(2) 每个 $\alpha_{n}$ 都是 T 的特征值.

(3) $\sigma(T) = F$ .

(4) $F \setminus (\{\alpha_n\}_{n=1}^{\infty}) = \sigma_c(T).$

7. 设 $X$ 是 Banach 空间, $T \in L(X)$ , $\mathcal{M} \in \operatorname{Lat} T$ . 如果 $\eta \in \rho(T)$ , 且 $\mathcal{M} \in \operatorname{Lat} R(\eta, T)$ , 则 $\eta \in \rho(T | \mathcal{M})$ .

8. 设数列 $\{\alpha_{n}\}_{n-1}^{\infty}$ 满足 $\alpha_{n} \to 0, n \to \infty$ . 在 $l^{1}$ 中定义算子 $T$ 为

$$
y = T x: y = \left\{\alpha_ {n} \xi_ {n} \right\}, x = \left\{\xi_ {n} \right\}.
$$

试证明 $T$ 是 $\ell^1$ 上的紧算子.

9. 试证明: 当 X 是自反空间时, 定理 3.3 的逆亦真, 即如果每当 $x_{n} \xrightarrow{w} x_{0}$ , 必有 $Ax_{n} \to Ax_{0}$ , 则 A 必是紧算子.

10. 设 $X$ 是 Banach 空间, $T \in L(X)$ 是紧算子, $\mathcal{M} \in \operatorname{Lat} T$ . 则 $T \mid \mathcal{M}$ 也是 $\mathcal{M}$ 上的紧算子.

11. 设 $X$ 是 Banach 空间, $K \in \mathcal{K}(X), \lambda \neq 0, T = \lambda I - K$ , 则

(1) $N(T) = \{0\} \Leftrightarrow R(T) = X.$

(2) $\dim N(T) = 0 \Leftrightarrow \dim N(T') = 0$ .

(3) $\dim N(T) = \dim N(T') < \infty$ .

12. 设 $X$ 是 Banach 空间, $T \in L(X)$ . 如果存在正整数 $n$ , 使 $T^n$ 是紧算子, 证明:

(1) $\sigma_{p}(T)$ 至多是可数集.

(2) $\sigma_{p}(T)$ 唯一可能聚点是0.

13. 设 $T$ 是 Banach 空间 $X$ 上有界线性算子, 且 $T^2 = T$ . 试证明: 如果 $T \neq 0, I$ , 则 $\sigma(T) = \{0, 1\}$ .

14. 设 $P_{1}, P_{2}$ 是 Hilbert 空间 $H$ 上可交换的正交射影. 则

$$
P \stackrel {\mathrm{d}} {=} P _ {1} + P _ {2} - P _ {1} P _ {2}
$$

也是正交射影，且 $P \geqslant P_{1}, P \geqslant P_{2}$ . 另外，若正交射影 $Q$ ，使 $Q \geqslant P_{1}, Q \geqslant P_{2}$ ，则必有 $Q \geqslant P$ .

15. 设 $T$ 是 Hilbert 空间 $H$ 上有界线性算子, 且 $\| T \| \leqslant 1$ , 则

$$
\{x \in H: T x = x \} = \{x \in H: T ^ {*} x = x \}.
$$

16. 设 $P$ 是 Hilbert 空间 $H$ 上非零正交射影, 证明: $\| P \| = 1$ .

17. 证明: 定理 4.5 中, $(-∞, m) ⊂ ρ(A), m ∈ σ(A)$ .

18. 设 $\{e_n\}_{n=1}^{\infty}$ 是可分 Hilbert 空间 $H$ 的正规正交基, $T \in L(H)$ . 若对任何自然数 $m, n$ 都有

$$
\left(T e _ {n}, e _ {m}\right) = \left(e _ {n}, T e _ {m}\right),
$$

则 $T$ 是自伴的.

19. 设 $H$ 是 Hilbert 空间, $T, W \in L(H)$ . 如果 $T$ 是自伴的, 则 $W^{*}TW$ 也是自伴的.

20. 设 $H$ 是 Hilbert 空间, $T \in L(H)$ 是自伴算子. 试证明: $T \geqslant 0$ 当且仅当 $\sigma(T) \subset [0, \infty)$ .

21. 设 $H$ 是 Hilbert 空间, $T \in L(H)$ 是自伴算子, 且 $T \geqslant 0$ . 试证明: 对任给的 $x \in H, Tx = 0$ 当且仅当 $(Tx, x) = 0$ .

22. 设 $\{P_{n}\}_{n=1}^{\infty}$ 是 Hilbert 空间 $H$ 上的射影算子的序列, $P_{n} \to P$ . 证明: $P$ 亦是 $H$ 上射影, 进一步, 如果 $P_{n}$ 都是正交射影, 则 $P$ 亦是正交射影.

23. 设 $H$ 是无穷维的 Hilbert 空间, $T \in L(H)$ . 如果 $T$ 是下方有界的, 则 $T$ 必不是紧算子. 试证明之.

24. 设 $H$ 是 Hilbert 空间, $T \in L(H)$ 称为正规算子, 如果 $T^{*} T = TT^{*}$ . 试证明: 对正规算子 $T$ , 总有

(1) $\| T^2 \| = \| T \|^2$ .

(2) $r(T) = \| T\|$ .

(3) 若 $\lambda$ 与 $\mu$ 是 $T$ 之互异的特征值, $x, y$ 分别是 $T$ 相应于 $\lambda, \mu$ 的特征元, 则 $x$ 与 $y$ 正交.

(4) 假如 $T$ 还是紧的, 则必有 $H$ 的一个正规正交基 $\{\varphi_n\}_{n \in J} \cup \{\psi_a\}_{a \in J}$ , 使

(i) $T\varphi_{n} = \lambda_{n}\varphi_{n},\lambda_{n}\neq 0$ ，当 $n\in J,T\psi_{\alpha} = 0$ ，当 $\alpha \in \mathcal{A}$ 这里 $J$ 是有限或可数无穷集，若 $J$ 是可数无穷集，则 $\lim_{n\to \infty}\lambda_n = 0.$

(ii) 对任给的 $\psi \in H$ , 有展开式

$$
T \psi = \sum_ {n \in J} \lambda_ {n} (\psi , \varphi_ {n}) \varphi_ {n},
$$

这里右端级数是按范数收敛的.

25. 设 $T$ 是 Hilbert 空间 $H$ 上自伴算子, $\{E_{\lambda}: -\infty < \lambda < \infty\}$ 是 $T$ 的谱族. 证明: $T$ 的值域的闭包是 $[I - E_0 + E_{0-0}]H$ .

26. 设 $H$ 是 Hilbert 空间, $T, U \in L(H)$ , $U$ 是酉算子, 令 $\tilde{T} = U^{-1} TU$ . 试证明:

(1) $\| \tilde{T} \| = \| T \|$ .

(2) $\sigma (\widetilde{T}) = \sigma (T)$ .

27. 设 $H$ 是 Hilbert 空间, $T, U \in L(H)$ , $T$ 是自伴算子, $U$ 是酉算子, $\tilde{T} = U^{-1} TU$ . 试证明: 对任何的有界 Borel 函数 $f$ , 都有

$$
f (\tilde {T}) = U ^ {- 1} f (T) U,
$$

这里 $f(\tilde{T}), f(T)$ 分别表示 $\tilde{T}$ 与 $T$ 的函数演算.

28. 设 $H$ 是 Hilbert 空间, $U \in L(H)$ 是酉算子. 试证明:

(1) 如果 $P \in L(H)$ 是正交射影, 则 $U^{-1}PU$ 也是正交射影.

(2) 如果 $T \in L(H)$ 是正规算子, 则 $U^{-1} TU$ 也是正规算子.

(3) 如果 $A \in L(H)$ 是正算子, 则 $U^{-1}AU$ 也是正算子.

29. 设 $S$ 是 Hilbert 空间 $H$ 上的单边移位算子，

$$
S: \{x _ {0}, x _ {1}, x _ {2}, \dots \} \mapsto \{0, x _ {0}, x _ {1}, x _ {2}, \dots \}.
$$

求证 $S$ 不能表成

$$
S = U P,
$$

这里 U 是酉算子, P 是正算子.

30. 设无穷矩阵 $(u_{ij})$ 是个酉矩阵. 求证: 它是可分 Hilbert 空间 $H$ 上一个有界线性算子 $A$ 的矩阵表达式, 而且 $A$ 还是酉算子.

# 第五章\* 广义函数论大意

## 引言从纯数学的观点, 在 $L^{p}(p>1)$ 的对偶空间的研究中, 我们已经看到数值函数与线性泛函的密切联系了:

数值函数 $f \in L^q \longleftrightarrow$ 线性泛函 $\ell(\varphi) = \int f(x)\varphi(x)\mathrm{d}x, \varphi \in L^p$ ,

其中 $\frac{1}{p} +\frac{1}{q} = 1$

下面我们将看到把数值函数扩充为线性泛函可说是广义函数论的一个基本思想.

在近代微分方程理论中,人们为了要把微分学扩充到比可微函数广得多的对象上去,而想到对实数轴 R 上连续可微的函数 $f(x)$ 与 $\varphi(x)(\varphi(x))$ 的支集 $\operatorname{supp}\varphi=\overline{\{x:\quad\varphi(x)\neq0\}}$ 是有界的),由分部积分法有

$$
\int_ {- \infty} ^ {+ \infty} f ^ {\prime} (x) \varphi (x) \mathrm{d} x = - \int_ {- \infty} ^ {+ \infty} f (x) \varphi^ {\prime} (x) \mathrm{d} x.
$$

从而把对 $f(x)$ 的求导转化到 $\varphi(x)$ 上去. 这启发人们选取适当的函数空间 $K$ (比如具有紧的支集的无穷次可微函数的空间), 可以定义函数空间 $K$ 上的泛函 $F$ 的广义导数为

$$
\varphi \in K \mapsto - \langle F, \varphi^ {\prime} \rangle = - F (\varphi^ {\prime}),
$$

其中 $\varphi' = \varphi'(x)$ 是 $\varphi(x)$ 的导数, $F$ 的广义导数也记作 $DF$ . 这比之经典的导数要广泛得多. 例如, 对任何在 $\mathbf{R}$ 上局部可积的函数 $f$ (即在 $\mathbf{R}$ 的任何有限区间上都 Lebesgue 可积的函数), 它当然可以是不连续的, 但是由

$$
F (\varphi) = \int_ {- \infty} ^ {+ \infty} f (x) \varphi (x) \mathrm{d} x, \varphi \in K,
$$

定义的泛函 $F$ 的广义导数却是存在的，并且

$$
\mathrm{DF} = L (\varphi) \stackrel {\mathrm{d}} {=} - \int_ {- \infty} ^ {+ \infty} f (x) \varphi^ {\prime} (x) \mathrm{d} x, \varphi \in K.
$$

早在 Poincaré 的工作中, 他已经从这个想法定义微分方程的弱解(参见[26], 第 221 页). 设

$$
L = \sum_ {| s |, | t | \leqslant m} \mathrm{D} ^ {s} C _ {s t} (x) \mathrm{D} ^ {t},
$$

这里 s, t 都是重指标, 如 $s = (s_{1}, \cdots, s_{n})$ ,

$$
\begin{array}{r l} \mathrm{D} ^ {s} f (x) & = \frac {\partial^ {| s |}}{\left(\partial x _ {1} ^ {s _ {1}} \cdots \partial x _ {n} ^ {s _ {n}}\right)} f (x _ {1}, \dots , x _ {n}), \\ | s | & = | (s _ {1}, \dots , s _ {n}) | = s _ {1} + \dots + s _ {n}, \end{array}
$$

实系数 $C_{st}(x)$ 在 $\mathbf{R}^n$ 的某个有界区域 $G$ 上属于 $C^\infty$ .

考虑方程

$$
L u = f.\tag{0.1}
$$

其中 $f(x)$ 是已知的 $G$ 上的局部平方可积的函数. 一个在 $G$ 上局部平方可积的函数 $u(x)$ 称为方程(0.1)的弱解, 如果对任何 $\varphi \in C_0^\infty(G)$ , 都有

$$
(u, L \varphi) = (f, \varphi),
$$

这里

$$
L ^ {*} = \sum_ {| s |, | t | \leqslant m} (- 1) ^ {| s | + | t |} \mathrm{D} ^ {t} C _ {s t} (x) \mathrm{D} ^ {s},
$$

$(f,g)$ 表示 $f,g\in L^{2}(G)$ 的内积.

上面从数值函数扩充到线性泛函的想法也适用于Fourier变换的理论.在经典理论中,有所谓Parseval关系,即于 $f,g\in L^{1}(-\infty,\infty)$ 有

$$
\int_ {- \infty} ^ {+ \infty} \hat {f} (x) \varphi (x) d x = \int_ {- \infty} ^ {+ \infty} f (x) \hat {\varphi} (x) d x.\tag{0.2}
$$

这里 $\hat{f},\hat{\varphi}$ 分别代表 $f,\varphi$ 的Fourier变换(参见[7],第七章，§4).下面我们将引进基本空间 $\mathcal{S}(\mathbf{R}^n)$ ，对其上的连续线性泛函 $T\in \mathcal{S}'(\mathbf{R}^n)$ ，比照着(0.2)式，自然定义 $T$ 的Fourier变换 $F(T)$ 为

$$
\langle F (T), \varphi \rangle \stackrel {{d}} {=} \langle T, \hat {\varphi} \rangle , \quad \varphi \in \mathscr {S} (\mathbf {R} ^ {n}),
$$

这里及以后， $\langle T, \varphi \rangle$ 表示泛函 $T$ 作用在 $\varphi$ 上的值.

据[26], 第 228—230 页, 这一工作始于 A. Weil (1940), 而完成于 L. Schwartz (1950—1951).

## § 1 基本函数空间D上的广义函数及其导数设想在无限长的棒上有一质量分布, 只集中在 $x = 0$ 处, 总质量为一个单位. 设密度函数为 $\delta(x)$ , 意即

$$
\delta (x) = 0, \text {当} x \neq 0,
$$

且

$$
\int_ {- \infty} ^ {\infty} \delta (x) \mathrm{d} x = 1.
$$

从 Riemann 或 Lebesgue 积分论来看, 这样的 $\delta(x)$ 是不可理解的. 如果还要求能对 $\delta(x)$ 进行多次求导, 那就更不好办了. 但是如此的 $\delta(x)$ 在工程中却是常见的,例如在无线电工程中常考察的所谓脉冲,它在极短时间内爆发出一个单位能量的信号,这一物理现象的描述实与上述的质量分布类似,一些工程书上就用 $\delta(x)$ 来表达.

为了解像 $\delta(x)$ 这样的函数, 如引言所说, 先要选取适当的函数空间.

定义1.1(基本函数空间 $\mathcal{D}$ ) 设 $\mathcal{D}$ 是 $-\infty < x < \infty$ 上无穷次可微且在某有限区间外为零的函数全体, 按着通常的函数加法和数乘, 成为线性空间. 在其中定义极限概念如下:

设 $\{\varphi_n\}_{n=1}^{\infty}\subset\mathcal{D},\varphi\subset\mathcal{D}$ , 若

(1) 存在有限区间 $[a, b]$ , 使支集 $\operatorname{supp}(\varphi_n) \subset [a, b], n = 1, 2, \cdots$ .

(2) 对每个非负整数 $q$ ，在 $-\infty < x < \infty$ 上， $\{\varphi_n^{(q)}(x)\}_{n=1}^{\infty}$ 都一致收敛于 $\varphi^{(q)}(x)$ . 则称 $\{\varphi_n\}_{n=1}^{\infty}$ 在 $\mathcal{D}$ 中收敛于 $\varphi$ ，简记作 $\varphi_n \to \varphi(\mathcal{D})$ .

定义 1.2(2 广义函数) 2 上的按 $\varphi_{n} \rightarrow \varphi(\mathcal{D})$ 为连续的线性泛函 T 称为 2 广义函数，简记为 $T \in \mathcal{D}'(\mathbb{R})$ (或 $T \in D'$ ).

例1 凡 $\mathbf{R}$ 上局部可积函数都是 $\mathcal{D}$ 广义函数.

设 $f$ 是 $\mathbf{R}$ 上局部可积函数，则 $f$ 对应着如下定义的 $\mathcal{D}$ 广义函数 $T_{f}$

$$
\langle   T _ {f}, \varphi \rangle   = \int_ {- \infty} ^ {\mathrm{d}} f (  x  )   \varphi (  x  ) \mathrm{d} x  , \text {当}   \varphi \in   \mathcal {D}.\tag{1.1}
$$

首先， $T_{f}$ 的线性是显然的，其次设 $\{\varphi_n\}_{n = 1}^{\infty}\subset \mathcal{D},\varphi \in \mathcal{D}$ ，使 $\varphi_{n}\rightarrow \varphi (\mathcal{D})$ ，则存在有限区间 $[a,b]$ ，使

$$
\operatorname{supp} (\varphi_ {n}) \subset [ a, b ], n = 1, 2, \dots , \quad \operatorname{supp} (\varphi) \subset [ a, b ],
$$

且

$$
\max _ {a \leqslant x \leqslant b} | \varphi_ {n} (x) - \varphi (x) | \to 0, \text {当} n \to \infty .
$$

注意 $f(x)$ 在 $[a, b]$ 上可积，于是由Lebesgue控制收敛定理

$$
\begin{array}{r l} {\mid \langle T _ {f}, \varphi_ {n} \rangle - \langle T _ {f}, \varphi \rangle \mid = \mid \int_ {a} ^ {b} f (x)   \varphi_ {n} (x) \mathrm{d} x - \int_ {a} ^ {b} f (x)   \varphi (x) \mathrm{d} x \mid} \\ & {\leqslant \int_ {a} ^ {b} \mid f (x) \mid \mid \varphi_ {n} (x) - \varphi (x) \mid \mathrm{d} x \to 0, \text {当} n \to \infty .} \end{array}
$$

说明 $T_{f}$ 是 $\mathcal{D}$ 广义函数.

如果我们对几乎处处相等的局部可积函数不加区别,看作同一个元,则上述对应

$$
f \mapsto T _ {f} \in \mathcal {D} ^ {\prime} (\mathbf {R})
$$

是一对一的.事实上,只须证明,若 $f(x)$ 是局部可积函数,使

$$
\int_ {- \infty} ^ {\infty} f (x) \varphi (x) \mathrm{d} x = 0, \forall \varphi \in \mathcal {D},
$$

则 $f(x)$ 几乎处处等于0.为此又只须证明，对任意区间 $[x_0 - \delta, x_0 + \delta] \subset$

$(-\infty, \infty)$ 都有 $f(x) = 0, \mathrm{a.e.}$ 于 $[x_0 - \delta, x_0 + \delta]$ . 定义 $\mathbf{R}$ 上函数 $\tilde{f}$ 如下：

$$
\tilde {f} (x) = \left\{ \begin{array}{l l} \operatorname{sgn} f (x), \text {当} x \in [ x _ {0} - \delta , x _ {0} + \delta ]; \\ 0, & \text {当} x \notin [ x _ {0} - \delta , x _ {0} + \delta ]. \end{array} \right.
$$

显然有 $\tilde{f} \in L^{1}(\mathbb{R})$ . 利用 Weierstrass 定理可以证明, 存在 $\mathcal{D}$ 中函数列 $\{\tilde{f}_{n}\}_{n=1}^{\infty}$ , 使 $|\tilde{f}_{n}(x)| \leqslant 1, n = 1, 2, \cdots$ , 且

$$
\parallel \tilde {f} _ {n} - \tilde {f} \parallel_ {1} \rightarrow 0, \text {当} n \rightarrow \infty .
$$

从而由实变函数论中的Lebesgue收敛定理(参见[6],第五章,§9),有

$$
\begin{array}{r l}\int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} | f (x) | \mathrm{d} x&= \int_ {x _ {0} - \delta} ^ {x _ {0} + \delta} f (x) \tilde {f} (x) \mathrm{d} x\\&= \int_ {- \infty} ^ {\infty} f (x) \tilde {f} (x) \mathrm{d} x\\&= \lim _ {n \rightarrow \infty} \int_ {- \infty} ^ {\infty} f (x) \tilde {f} _ {n} (x) \mathrm{d} x\\&= 0,\end{array}
$$

故 $f(x) = 0$ ,a.e.于 $[x_0 - \delta ,x_0 + \delta ]$

总之, 每个局部可积函数按(1.1)对应一个 $\mathcal{D}$ 广义函数, 而且这个对应是一对一的. 从这个意义上说, 每个局部可积函数都是 $\mathcal{D}$ 广义函数, 而 $T_{f}$ 直接记为 $f$ .

例2 Dirac函数 $\delta (x)$ 是 $\mathcal{D}$ 广义函数.

定义

$$
\langle   \delta  , \varphi \rangle \stackrel {\mathrm{d}} {=} \varphi (0)  , \text {当}   \varphi \in \mathcal {D}.
$$

易见 $\delta$ 是线性的，而且当 $\varphi_{n} \to \varphi_{0}(\mathcal{D})$ ，我们有

$$
| \varphi_ {n} (0) - \varphi_ {0} (0) | \rightarrow 0, \text {当} n \rightarrow \infty .
$$

于是

$$
| \langle \delta , \varphi_ {n} \rangle - \langle \delta , \varphi_ {0} \rangle | = | \varphi_ {n} (0) - \varphi_ {0} (0) | \rightarrow 0, \text {当} n \rightarrow \infty .
$$

可见 $\delta$ 是 $\mathcal{D}$ 上连续线性泛函. 于是 $\delta(x)$ 是 $\mathcal{D}$ 广义函数, 称为 Dirac 函数.

如引言所说到的,可如下定义广义函数的导数.

定义1.3 设 $F \in \mathcal{D}'(\mathbf{R})$ ，定义

$$
\langle F ^ {\prime}, \varphi \rangle \stackrel {\mathrm{d}} {=} - \langle F, \varphi^ {\prime} \rangle , \text {当} \varphi \in \mathcal {D}.\tag{1.2}
$$

这里 $\varphi' = \varphi'(x)$ 是 $\varphi = \varphi(x)$ 的导数. $F'$ 有时也记为 $DF$ , 称为 $F$ 的导数.

$\varphi \in \mathcal{D}$ 是无穷次可微的，且在某个有限区间外恒为0.故 $\varphi^{\prime}$ 也是无穷次可微的，且在某个有限区间外恒为0.即 $\varphi^{\prime} \in \mathcal{D}$ . 从而 $\langle F, \varphi^{\prime} \rangle$ 有意义. 显然如此定义的 $F^{\prime}$ 是 $\mathcal{D}$ 上线性泛函. 如果 $\varphi_{n} \to \varphi(\mathcal{D})$ ，则 $\varphi_{n}$ 的各阶导数分别一致收敛到 $\varphi$ 的各阶导数,于是 $\varphi_{n}^{\prime}\rightarrow\varphi^{\prime}(\mathcal{D})$ . 故由 $F$ 的连续性可知 $F^{\prime}$ 也是连续的, 即 $F^{\prime}\in\mathcal{D}^{\prime}(\mathbf{R})$ .

例3 $\langle \delta',\varphi \rangle = -\varphi '(0),\forall \varphi \in \mathcal{D}.$

由广义函数的导数定义及例2可知，对任意的 $\varphi \in \mathcal{D}$

$$
\langle \delta^ {\prime}, \varphi \rangle = - \langle \delta , \varphi^ {\prime} \rangle = - \varphi^ {\prime} (0).
$$

例4 考察Heaviside函数

$$
H (x) = \left\{ \begin{array}{l l} 0, & \text {当} x <   0, \\ 1, & \text {当} x \geqslant 0, \end{array} \right.
$$

则 $H' = \delta$ .

显然 $H(x)$ 是 $\mathbb{R}$ 上局部可积函数，由例1， $H$ 是 $\mathcal{D}$ 广义函数。按广义函数导数定义，对任给的 $\varphi \in \mathcal{D}$ ，

$$
\begin{array}{r l} \langle H ^ {\prime}, \varphi \rangle & = - \langle H, \varphi^ {\prime} \rangle \\ & = - \int_ {- \infty} ^ {\infty} H (x) \varphi^ {\prime} (x) \mathrm{d} x \\ & = - \int_ {0} ^ {\infty} \varphi^ {\prime} (x) \mathrm{d} x \\ & = \varphi (0) = \langle \delta , \varphi \rangle . \end{array}
$$

故 $H^{\prime} = \delta$

定理1.1 设 $F \in \mathcal{D}'(\mathbf{R})$ ，则 $F$ 的各阶导数 $\mathrm{D}^p F$ 都存在，而且 $\mathrm{D}^p F \in \mathcal{D}'(\mathbf{R})$ . 证从广义函数导数定义下的注解可知，若 $F \in \mathcal{D}'(\mathbf{R})$ ，则 $\mathrm{DF} = F'$ 存在，且 $\mathrm{DF} \in \mathcal{D}'(\mathbf{R})$ . 从而，由数学归纳法，对任意自然数 $p, F$ 的 $p$ 阶导数 $\mathrm{D}^p F$ 存在，且 $\mathrm{D}^p F \in \mathcal{D}'(\mathbf{R})$ . 证毕.

定理1.2 设 $\{F_n\}_{n=1}^{\infty} \subset \mathcal{D}'(\mathbf{R}), F \in \mathcal{D}'(\mathbf{R})$ ，而且

$$
\lim _ {n \rightarrow \infty} F _ {n} (\varphi) = F (\varphi), \forall \varphi \in \mathscr {D}.
$$

则对任何自然数 $p$ ，

$$
\lim _ {n \rightarrow \infty} \left(\mathrm{D} ^ {p} F _ {n}\right) (\varphi) = \left(\mathrm{D} ^ {p} F\right) (\varphi), \forall \varphi \in \mathcal {D}.
$$

证当 $\varphi \in \mathcal{D}$ , 对任何自然数 $p, \varphi^{(p)} \in \mathcal{D}$ . 反复利用(1.2)式可得

$$
\left\langle \mathrm{D} ^ {p} F, \varphi \right\rangle = (- 1) ^ {p} \left\langle F, \varphi^ {(p)} \right\rangle , \varphi \in \mathscr {D}.
$$

即

$$
\left(\mathrm{D} ^ {p} F\right) (\varphi) = (- 1) ^ {p} F \left(\varphi^ {(p)}\right), \varphi \in \mathscr {D}.
$$

于是

$$
\begin{array}{r l}\lim _ {n \rightarrow \infty} (\mathrm{D} ^ {p} F _ {n}) (\varphi)&= \lim _ {n \rightarrow \infty} (- 1) ^ {p} F _ {n} (\varphi^ {(p)})\\&= (- 1) ^ {p} F (\varphi^ {(p)})\\&= (\mathrm{D} ^ {p} F) (\varphi).\end{array}
$$

证毕.

最后,我们应该指出,在前述基本空间 $\mathcal{D}$ 的定义中,只是给出 $\varphi_{n} \rightarrow \varphi(\mathcal{D})$ 的意义, 没有完整地给出 $\mathcal{D}$ 上的拓扑. 这在理论的进一步发展上是不方便的. 为此许多书的作者都要稍加费事地定义 $\mathcal{D}$ 上的拓扑为 $\mathcal{D}_K$ 空间的归纳极限, 这里 $K$ 是 $\mathbf{R}$ 的紧子集, $\mathcal{D}_K = \{\varphi \in C^\infty(\mathbb{R}) : \mathrm{supp} \varphi \subset K\}$ . 可以证明, 按前述 $\varphi_n \to \varphi(\mathcal{D})$ 为连续的线性泛函也是按 $\mathcal{D}$ 上拓扑为连续的线性泛函. (参见[40], §6.3-§6.5)

利用 $\mathcal{D}$ 上的拓扑可有定理1.3 设 $\{F_n\}_{n=1}^{\infty} \subset \mathcal{D}'(\mathbf{R})$ ，而且当 $\varphi \in \mathcal{D}$ 时， $\lim_{n \to \infty} \langle F_n, \varphi \rangle$ 总存在，则有 $F \in \mathcal{D}'(\mathbf{R})$ ，使

$$
\lim _ {n \rightarrow \infty} \left\langle F _ {n}, \varphi \right\rangle = \left\langle F, \varphi \right\rangle , \forall \varphi \in \mathcal {D}.
$$

证明可参见[40], §6.17. 这里正是因为有了上述由归纳极限定义的拓扑, 才得以将问题转化为 Fréchet 空间 $\mathcal{D}_K$ 上的一致有界原理.

从前面三个定理足见广义函数的求导是十分灵活的. 这比之数学分析上函数的可微性和函数级数的逐项微分定理, 真是惊人的大解放.

## § 2 基本函数空间 $\mathscr{S}$ 上的广义函数及其 Fourier 变换

Fourier 变换在许多领域(数学、物理与工程技术)中都是很重要的工具,但是它的经典理论却有不少缺陷.第一,它所能施用上去的函数要受到很多限制(一般只是 $L^1$ 与 $L^2$ 的理论比较完整.后来人们费了很大的劲研究 $L^p (1 < p < 2)$ 上的 Fourier 变换理论.至于 $p > 2$ 的情况,虽然 S. Bochner 与 N. Wiener 作出重要的贡献,但仍远不能令人满意).第二,它在运算上极不灵活,在视 Fourier 变换为算子时,甚至其值域也是很不清楚的.那么如何解决这些问题呢?出路仍在于扩充函数的概念.正像历史上极限概念的发展和确立,必须把有理数域扩充到实数域一样.(参见[5],第四章)

## 1. 基本空间 $\mathcal{S}$

回忆第一章 §8 的例 3 中急减函数空间 $\mathcal{S}(\mathbf{R}^n)$ .

定义 2.1 设 $\psi(x)$ 是 $R^{n}$ 上无穷次可微的函数, 而且对任何重指标 $\alpha = (\alpha_{1}, \cdots, \alpha_{n})$ 及 $p = (p_{1}, \cdots, p_{n})$ ,

$$
\psi \parallel_ {a, p} = \rho_ {a p} (\psi) = \sup _ {x \in \mathbb {R} ^ {n}} | x ^ {a} \partial^ {p} \psi (x) | <   \infty ,\tag{2.1}
$$

这里 $x^{\alpha} = x_{1}^{\alpha_{1}}\dots x_{n}^{\alpha_{n}}$ ，则称 $\psi (x)$ 为急减函数，记作 $\psi \in \mathcal{S}(\mathbb{R}^n),\mathcal{S}(\mathbb{R}^n)$ 有时简记为 $\mathcal{S}$ ：

在 $\mathcal{S}(\mathbf{R}^n)$ 中规定如下的极限概念：若 $\{\varphi_v\}_{v=1}^{\infty}\subset\mathcal{S}$ ，且

(1) 对任给的重指标 $\alpha$ 和 p，

$$
\sup _ {v} \| \varphi_ {v} \| _ {\alpha , p} <   \infty .
$$

(2) 对任给的重指标 $\alpha$ 和 $p$ , 都有 $\{x^{\alpha} \partial^{p} \varphi_{v}(x)\}_{v=1}^{\infty}$ 在 $\mathbf{R}^{n}$ 上一致趋于零, 当

$$
v \rightarrow \infty .
$$

则称 $\{\varphi_v\}_{v=1}^{\infty}$ 在 $\mathcal{S}$ 中收敛到 0. 记作 $\varphi_v \to 0(\mathcal{S})$ .

注意对 $\varphi \in \mathcal{S}$ , 由 (2.1) 可直接得出: 当 $\|x\| = (x_1^2 + \cdots + x_n^2)^{1/2} \to \infty$ 时, $\varphi(x) \to 0$ 衰减的速度比之任何 $\frac{1}{p(x)}$ 都快, 这里 $p(x)$ 是任何多项式, 所以人们称之为急减函数. 此外, $\mathcal{S}$ 中的函数是无穷次可微的, 所以是很光滑的, 显然这样的函数类比较狭窄. 为什么要考虑如此狭窄的函数空间呢? 一个原因在于所考虑的空间越小, 定义于其上的连续泛函的范围就越大. 如果把广义函数定义成基本空间 $\mathcal{S}(\mathbb{R}^n)$ 上按 $\varphi_v \to 0(\mathcal{S})$ 为连续的线性泛函, 那么 $f(x) = 1, x, \sin x$ 等都属于此类广义函数了, 下面我们将详细地说明这一点.

## 2. $\mathcal{S}$ 广义函数

$\mathcal{S}(\mathbf{R}^n)$ 上的按 $\varphi_v \to 0(\mathcal{S})$ 为连续的线性泛函 $T$ , 叫做 $\mathcal{S}$ 广义函数. 记作 $T \in \mathcal{S}'(\mathbf{R}^n)$ .

一般称 $\mathcal{S}(\mathbf{R}^n)$ 上由半范数族 $\{\| \psi \|_{a,p}\}$ 所定义的拓扑为 $\mathcal{S}(\mathbf{R}^n)$ 上的拓扑，在第一章 §8 例3中我们已经证明. 按这个拓扑 $\mathcal{S}(\mathbf{R}^n)$ 是 $F-$ 空间，在第三章 §8,2 中我们进一步指出它是 Fréchet 空间. 现在容易看出， $\mathcal{S}$ 广义函数正是按 $\mathcal{S}(\mathbf{R}^n)$ 上的拓扑为连续的线性泛函.

定义2.2 若 $f(x)$ 在 $\mathbf{R}^n$ 上连续，且有正整数 $k$ 及常数 $C > 0$ ，使

$$
\mid f (x) \mid \leqslant C (1 + \| x \| ^ {2}) ^ {k}, \forall x \in \mathbf {R} ^ {n},\tag{2.2}
$$

这里 $\| x\|^2 = \sum_{j=1}^{n}|x_j|^2$ ，则称 $f(x)$ 为缓增函数。

显然,这类函数的范围较为广泛,诸如常数,x, $\sin x$ ,以及许多在应用中起着重要作用的函数多包含在此类中,而这些函数在经典理论中却不可能有Fourier变换.

定理2.1 每个缓增函数 $f(x)$ 都确定一个 $\mathcal{S}$ 广义函数.

证对每个 $\varphi \in \mathcal{S}$ , 定义

$$
\langle f, \varphi \rangle \stackrel {\mathrm{d}} {=} \int_ {\mathbb {R} ^ {n}} f (x) \varphi (x) \mathrm{d} x.
$$

因 $\varphi(x)$ 满足(2.1), $f(x)$ 满足(2.2), 故右端积分存在. 易见 $\langle f, \varphi \rangle$ 是 $\mathcal{S}$ 上线性泛函.

若 $\varphi_{o} \to 0(\mathcal{S})$ ，由极限定义，对任给的正整数 $k_{1}, (1 + \|x\|^{2})^{k_{1}}$ 可展开成 $\sum_{j=1}^{n} c_{j} x^{\alpha_{j}}$ ，这里 $c_{j}$ 是常数， $\alpha_{j} = (\alpha_{j_{1}}, \cdots, \alpha_{j_{n}})$ 是重指标， $x^{\alpha_{j}} = x_{1j_{1}}^{\alpha_{j}} \cdots x_{nj_{n}}^{\alpha_{j}}$ 。故有常数 $M_{1} > 0$ ，使

$$
(1 + \parallel x \parallel^ {2}) ^ {k _ {1}} | \varphi_ {\upsilon} (x) | <   M _ {1}, \text {对一切} \upsilon ,\tag{2.3}
$$

且 $\{\varphi_v(x)\}_{v=1}^{\infty}$ 在 $\mathbf{R}^n$ 上一致趋于0.因 $f(x)$ 是缓增函数，由(2.2)，

$$
\begin{array}{l} \mid \langle f, \varphi_ {v} \rangle \mid = \mid \int_ {\mathbf {R} ^ {n}} f (x) \varphi_ {v} (x) \mathrm{d} x \mid \\ \leqslant \int_ {\| x \| \leqslant r} | f (x) \varphi_ {v} (x) | \mathrm{d} x + \int_ {\| x \| > r} C M _ {1} (1 + \| x \| ^ {2}) ^ {k - k _ {1}} \mathrm{d} x, \end{array}
$$

对任给 $\varepsilon > 0$ ，选取充分大的 $k_{1}$ 与 $r$ ，使上式右端第二项小于 $\varepsilon / 2$ ，然后，对这固定的 $r$ ，自然有

$$
\lim _ {v \to \infty} \int_ {\| x \| \leqslant r} | f (x) \varphi_ {v} (x) | \mathrm{d} x = 0.
$$

总之， $\langle f, \varphi_v \rangle \to 0$ ，当 $v \to \infty$ 。故 $\langle f, \varphi \rangle$ 是 $\mathscr{S}$ 广义函数。证毕。

例1 若 $f \in L^{p}(\mathbf{R}^{n})(p \geqslant 1)$ , 则

$$
\langle f, \varphi \rangle = \int_ {\mathbb {R} ^ {n}} ^ {d} f (x)   \varphi (x) \mathrm{d} x  , \text {当}   \varphi \in \mathcal {S} (\mathbb {R} ^ {n})  ,
$$

恒有意义，且

$$
\left| \langle f, \varphi \rangle \right| \leqslant \| f \| _ {p} \| \varphi \| _ {q},
$$

这里 $\frac{1}{p} +\frac{1}{q} = 1$ ，当 $p > 1;q = \infty$ ，当 $p = 1$

若 $\varphi_{\nu}\rightarrow 0(\mathcal{S})$ ，对 $1 < q < \infty (q = \infty$ 证明是类似的），注意

$$
\| \varphi_ {v} \| _ {q} ^ {q} = \int_ {\| x \| \leqslant r} + \int_ {\| x \| > r} | \varphi_ {v} (x) | ^ {q} d x.
$$

对任给的 $\varepsilon > 0$ ，由(2.3)式，选取充分大的 $r$ ，则上式右端第二项小于 $\varepsilon / 2$ ，然后对固定的 $r$ ，上式右端第一项自然小于 $\varepsilon / 2$ ，当 $\upsilon$ 充分大时。于是 $\| \varphi_v \|_q \to 0$ ，从而 $\langle f, \varphi_v \rangle \to 0$ 。这说明 $\langle f, \varphi \rangle$ 是 $\mathcal{S}$ 广义函数。

总之，每个 $f \in L^{p}(\mathbf{R}^{n})(p \geqslant 1)$ 都确定一个 $\mathcal{S}$ 广义函数.

## 3. 基本函数的 Fourier 变换设 $f(x)=f(x_{1},\cdots,x_{n})\in L^{1}(\mathbb{R}^{n})$ ，定义 $f(x)$ 的 Fourier 变换为

$$
F (f) (\zeta) = \int_ {\mathbf {R} ^ {n}} f (x) \mathrm{e} ^ {- \mathrm{i} x \zeta} \mathrm{d} x, \quad \zeta \in \mathbf {R} ^ {n}.\tag{2.4}
$$

这里及以下总采用记号

$$
\begin{array}{l} x = (x _ {1}, \dots , x _ {n}), \\ \zeta = (\zeta_ {1}, \dots , \zeta_ {n}), \\ x \zeta = x _ {1} \zeta_ {1} + \dots + x _ {n} \zeta_ {n}, \\ \mathrm{d} x = \mathrm{d} x _ {1} \dots \mathrm{d} x _ {n}. \end{array}
$$

可以证明，对于 $f \in \mathcal{S}(\mathbb{R}^n)$ ，设 $g(\zeta) = F(f)(\zeta)$ ，则有反演公式

$$
F ^ {- 1} (g) (x) = \frac {1}{(2 \pi) ^ {n}} \int_ {\mathbf {R} ^ {n}} g (\zeta) e ^ {i \zeta x} d \zeta .\tag{2.5}
$$

我们只对 $n = 3$ 的情况给出证明，对于一般情况证明也是类似的.设 $f(x)\in \mathcal{S}(\mathbb{R}^3)$ ，记

$$
f _ {1} (\zeta_ {1}, x _ {2}, x _ {3}) = \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1}.
$$

我们知道,对一元函数 $\varphi(x)$ , 当 $\varphi(x), \varphi'(x), \cdots, \varphi^{(m)}(x) \in L^{1}(-\infty, \infty)$ 时, 关于 $\varphi$ 的 Fourier 变换与求导之间有关系式

$$
F (\varphi^ {(k)}) (u) = (\mathrm{i} u) ^ {k} F (\varphi) (u), \text {对} k <   m.
$$

故

$$
\mathrm{i} ^ {k _ {1}} \zeta_ {1} ^ {k _ {1}} f _ {1} (\zeta_ {1}, x _ {2}, x _ {3}) = \int_ {- \infty} ^ {\infty} \left(\frac {\partial}{\partial x _ {1}}\right) ^ {k _ {1}} f (x _ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1},
$$

可见 $f_{1}(\zeta_{1}, x_{2}, x_{3}) \in \mathcal{S}(\mathbb{R}^{3})$ . 故由 Dini 定理(参见 Γ. E. 希洛夫《数学分析专门教程》, 第 365—368 页)

$$
f (x _ {1}, x _ {2}, x _ {3}) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f _ {1} (\zeta_ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {\mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} \zeta_ {1},
$$

同样设

$$
f _ {2} (\zeta_ {1}, \zeta_ {2}, x _ {3}) = \int_ {- \infty} ^ {\infty} f _ {1} (\zeta_ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} x _ {2},
$$

则如前也有 $f_{2}(\zeta_{1},\zeta_{2},x_{3})\in \mathcal{S}(\mathbf{R}^{3})$ ，再由Dini定理

$$
f _ {1} (\zeta_ {1}, x _ {2}, x _ {3}) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f _ {2} (\zeta_ {1}, \zeta_ {2}, x _ {3}) \mathrm{e} ^ {\mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} \zeta_ {2}.
$$

于是

$$
f (x _ {1}, x _ {2}, x _ {3}) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} \zeta_ {1} \cdot \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f _ {2} (\zeta_ {1}, \zeta_ {2}, x _ {3}) \mathrm{e} ^ {\mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} \zeta_ {2}.
$$

再设

$$
f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) = \int_ {- \infty} ^ {\infty} f _ {2} (\zeta_ {1}, \zeta_ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} x _ {3},
$$

则如前又有 $f_{3}(\zeta_{1},\zeta_{2},\zeta_{3})\in \mathcal{S}(\mathbf{R}^{3})$

$$
f _ {2} (\zeta_ {1}, \zeta_ {2}, x _ {3}) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) e ^ {i x _ {3} \zeta_ {3}} d \zeta_ {3}.
$$

从而

$$
\begin{array}{r l} & f (x _ {1}, x _ {2}, x _ {3}) \\ & = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} \zeta_ {1} \cdot \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} \zeta_ {2} \cdot \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) \mathrm{e} ^ {\mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} \zeta_ {3} \\ & = \frac {1}{(2 \pi) ^ {3}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} \zeta_ {1} \cdot \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} \zeta_ {2} \cdot \int_ {- \infty} ^ {\infty} f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) \mathrm{e} ^ {\mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} \zeta_ {3}. \end{array}\tag{2.6}
$$

根据Fubini定理,多重积分可以化为累次积分,于是由(2.4)定义的 $f$ 的Fourier变换可表为

$$
F (f) (\zeta) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} x _ {2} \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} x _ {3}.
$$

从 $f_{1}(\zeta_{1},x_{2},x_{3}),f_{2}(\zeta_{1},\zeta_{2},x_{3})$ 及 $f_{3}(\zeta_{1},\zeta_{2},\zeta_{3})$ 的表达式，我们得到

$$
\begin{array}{r l} f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) & = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} x _ {2} \int_ {- \infty} ^ {\infty} f (x _ {1}, x _ {2}, x _ {3}) \mathrm{e} ^ {- \mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} x _ {3} \\ & = F (f) (\zeta). \end{array}
$$

设 $g = F(f)$ ，则 $g(\zeta) = f_{3}(\zeta_{1},\zeta_{2},\zeta_{3})$ ，从(2.6)有

$$
\begin{array}{r l} & F ^ {- 1} (g) (x) \\ & = f (x) \\ & = \frac {1}{(2 \pi) ^ {3}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} \zeta_ {1} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} x _ {2} \zeta_ {2}} \mathrm{d} \zeta_ {2} \int_ {- \infty} ^ {\infty} f _ {3} (\zeta_ {1}, \zeta_ {2}, \zeta_ {3}) \mathrm{e} ^ {\mathrm{i} x _ {3} \zeta_ {3}} \mathrm{d} \zeta_ {3} \\ & = \frac {1}{(2 \pi) ^ {3}} \int_ {\mathbb {R} ^ {3}} g (\zeta) \mathrm{e} ^ {\mathrm{i} x \zeta} \mathrm{d} \zeta . \end{array}
$$

总之，反演公式(2.5)成立.

对于多元函数的 Fourier 变换, 假若函数相当光滑, 而且适当衰减, 特别对 $f \in \mathcal{S}(\mathbb{R}^{n})$ 有

(2.7)

$$
\begin{array}{c} F \left(\frac {\partial}{\partial x _ {j}} f\right) = \mathrm{i} \zeta_ {j} F (f), \\ F (\partial^ {a} f) = \mathrm{i} ^ {| a |} \zeta^ {a} F (f), \\ F (- \mathrm{i} x _ {j} f) = \frac {\partial}{\partial \zeta_ {j}} F (f), \\ F ((- \mathrm{i}) ^ {| a |} x ^ {a} f) = \partial^ {a} F (f), \end{array}
$$

这里 $\alpha=(\alpha_{1},\cdots,\alpha_{n})$ 是重指标， $|\alpha|=\alpha_{1}+\cdots+\alpha_{n}$ ，而

$$
\begin{array}{r l} x ^ {a} & = x _ {1} ^ {a _ {1}} \dots x _ {n} ^ {a _ {n}}, \\ \zeta^ {a} & = \zeta_ {1} ^ {a _ {1}} \dots \zeta_ {n} ^ {a _ {n}}, \\ \partial^ {a} f & = \frac {\partial^ {a _ {1} + \cdots + a _ {n}} f}{\partial x _ {1} ^ {a _ {1}} \cdots \partial x _ {n} ^ {a _ {n}}} = \frac {\partial^ {| a |}}{\partial x _ {1} ^ {a _ {1}} \cdots \partial x _ {n} ^ {a _ {n}}} f \end{array}
$$

我们不妨假定 $j = n$ ，来证明(2.7)第一式.首先，根据Fubini定理，

$$
\begin{array}{r l} F \left(\frac {\partial}{\partial x _ {n}} f\right) (\zeta) & = \int_ {\mathbb {R} ^ {n}} \frac {\partial}{\partial x _ {n}} f (x) e ^ {- i x \zeta} d x \\ & = \int_ {- \infty} ^ {\infty} e ^ {- i x _ {1} \zeta_ {1}} d x _ {1} \dots \int_ {- \infty} ^ {\infty} \frac {\partial}{\partial x _ {n}} f (x _ {1}, \dots , x _ {n}) e ^ {- i x _ {n} \zeta_ {n}} d x _ {n}. \end{array}
$$

利用分部积分, 注意 $f \in \mathcal{S}(\mathbf{R}^{n})$ 是急减函数而有

$$
\begin{array}{r l} F \left(\frac {\partial}{\partial x _ {n}} f\right) (\zeta) & = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \dots \left[ - \int_ {- \infty} ^ {\infty} f (x _ {1}, \dots , x _ {n}) \frac {\mathrm{d}}{\mathrm{d} x _ {n}} (\mathrm{e} ^ {- \mathrm{i} x _ {n} \zeta_ {n}}) \mathrm{d} x _ {n} \right] \\ & = \mathrm{i} \zeta_ {n} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, \dots , x _ {n}) \mathrm{e} ^ {- \mathrm{i} x _ {n} \zeta_ {n}} \mathrm{d} x _ {n} \end{array}
$$

$$
= \mathrm{i} \zeta_ {n} F (f) (\zeta).
$$

故(2.7)第一式成立,至于第二式可以通过反复使用第一式而得到.

对(2.7)第三式,从

$$
F (f) (\zeta) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \dots \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {j} \zeta_ {j}} \mathrm{d} x _ {j} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, \dots , x _ {n}) \mathrm{e} ^ {- \mathrm{i} x _ {n} \zeta_ {n}} \mathrm{d} x _ {n}
$$

在积分号下求导,则

$$
\left[ \frac {\partial}{\partial \zeta_ {j}} F (f) \right] (\zeta) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} x _ {1} \zeta_ {1}} \mathrm{d} x _ {1} \dots \int_ {- \infty} ^ {\infty} (- \mathrm{i} x _ {j}) \mathrm{e} ^ {- \mathrm{i} x _ {j} \zeta_ {j}} \mathrm{d} x _ {j} \dots \int_ {- \infty} ^ {\infty} f (x _ {1}, \dots , x _ {n}) \mathrm{e} ^ {- \mathrm{i} x _ {n} \zeta_ {n}} \mathrm{d} x _ {n}.
$$

因为 $f \in \mathcal{S}(\mathbb{R}^n)$ , 故上式右端关于 $\zeta$ 是一致收敛的, 因而在积分号下求导是可行的. 又根据Fubini定理, 上式右端即为

$$
F (- \mathrm{i} x _ {j} f) (\zeta).
$$

所以

$$
\frac {\partial}{\partial \zeta_ {j}} F (f) = F (- \mathrm{i} x _ {j} f).
$$

至于(2.7)第四式,通过反复利用第三式即可得到.

引理2.1 若 $f \in \mathcal{S}(\mathbf{R}^n)$ , 则 $F(f) \in \mathcal{S}(\mathbf{R}^n)$ .

证由(2.7)，对任意重指标 $\alpha$ 及 $p$ 有

$$
\begin{array}{r l} \int_ {\mathbb {R} ^ {n}} \partial^ {a} [ x ^ {p} f (x) ] e ^ {- i x \zeta} d x & = F (\partial^ {a} [ x ^ {p} f ]) (\zeta) \\ & = i ^ {| a |} \zeta^ {a} F (x ^ {p} f) (\zeta) \\ & = i ^ {| a |} \zeta^ {a} (- i) ^ {- | p |} \partial^ {p} F (f) (\zeta) \\ & = i ^ {| a | + | p |} \zeta^ {a} \partial^ {p} F (f) (\zeta). \end{array}
$$

由于 $\partial^a (x^p f(x))\in \mathcal{S}(\mathbf{R}^n)$ ，故对任意正整数 $k > n$

$$
(1 + \parallel x \parallel^ {2}) ^ {k} | \partial^ {a} (x ^ {p} f (x)) |
$$

在 $\mathbf{R}^n$ 上有界. 选取常数 $C$ , 使

$$
\int_ {\mathbf {R} ^ {n}} \frac {1}{(1 + \| x \| ^ {2}) ^ {k}} \mathrm{d} x = C.
$$

则有

(2.8)

$$
\begin{array}{r l} & {\mid \zeta^ {a} \partial^ {p} F (f) (\zeta) \mid} \\ & {\leqslant \int_ {\mathbb {R} ^ {n}} \mid \partial^ {a} [ x ^ {p} f (x) ] \mid \mathrm{d} x} \\ & {= \int_ {\mathbb {R} ^ {n}} \frac {1}{(1 + \| x \| ^ {2}) ^ {k}} (1 + \| x \| ^ {2}) ^ {k} \mid \partial^ {a} [ x ^ {p} f (x) ] \mid \mathrm{d} x} \\ & {\leqslant C \sup _ {x \in \mathbb {R} ^ {n}} \{(1 + \| x \| ^ {2}) ^ {k} \mid \partial^ {a} [ x ^ {p} f (x) ] \mid \}.} \end{array}
$$

可见 $F(f)$ 满足条件(2.1)，又由(2.7)第四式知道 $F(f)$ 在 $\mathbf{R}^n$ 上无穷次可微，故 $F(f)\in \mathcal{S}(\mathbf{R}^n)$ . 证毕.

这个引理显示出 $\mathcal{S}$ 空间的基本特点，表明 $\mathcal{S}$ 是对Fourier变换最合适的基本空间.此外，由反演公式的对称性，引理的推证对逆变换也一样成立.即有引理2.2 若 $\mathbf{g} \in \mathcal{S}(\mathbf{R}^n)$ , 则 $F^{-1}(g) \in \mathcal{S}(\mathbf{R}^n)$ .

定理2.2 变换 $g = F(f)$ 是变 $\mathcal{S}(\mathbf{R}^n)$ 为 $\mathcal{S}(\mathbf{R}^n)$ 的拓扑线性同构.

证若 $f_{0} \to 0(\mathcal{S})$ ，由(2.8)以及引理2.1证明中关于 $\zeta^{\alpha} \partial^{p} F(f)$ 的积分表达式容易证出 $F(f_{0}) \to 0(\mathcal{S})$ . 这表明 $F(f)$ 是从 $\mathcal{S}$ 到 $\mathcal{S}$ 的连续变换，关于 $F$ 的线性是显然的.

由反演公式, 逆变换 $F^{-1}(g)$ 与变换 $F(f)$ 的形式相似, 如前可证, $F^{-1}(g)$ 也是从 $\mathcal{S}$ 到 $\mathcal{S}$ 的连续线性变换. 又

$$
F (F ^ {- 1} (g)) = g.
$$

总之， $F(\mathcal{S}(\mathbf{R}^n)) = \mathcal{S}(\mathbf{R}^n)$ ，且 $F$ 是一对一的线性变换.证毕.

4. $\mathcal{S}$ 广义函数的Fourier变换对于 $f, g \in L^{1}(-\infty, \infty)$ , 由 Parseval 关系 (参见 [7], 第七章, §4), 有

$$
\int_ {- \infty} ^ {\infty} \hat {f} (u) g (u) \mathrm{d} u = \int_ {- \infty} ^ {\infty} f (u) \hat {g} (u) \mathrm{d} u,
$$

即

$$
\langle \hat {f}, g \rangle = \langle f, \hat {g} \rangle .
$$

这里 $\hat{f},\hat{g}$ 分别表示 $f,g$ 的Fourier变换.这便提示我们引进下面概念.

定义2.3 对 $T \in \mathcal{S}'(\mathbf{R}^n)$ , 其Fourier变换 $F(T)$ 定义为

$$
\langle F (T), \varphi \rangle \stackrel {d} {=} \langle T, F (\varphi) \rangle , \quad \text {当}   \varphi \in \mathcal {S} (\mathbf {R} ^ {n})  .
$$

注意,由定理2.2,上式右端是 $\mathcal{S}(\mathbf{R}^{n})$ 上的按 $\varphi_{v}\rightarrow0(\mathcal{S})$ 为连续的线性泛函,因此它确定一个S广义函数.即 $F(T)$ 是从 $\mathcal{S}^{\prime}(\mathbf{R}^{n})$ 到 $\mathcal{S}^{\prime}(\mathbf{R}^{n})$ 的变换.

设 $f(x)\in L^{1}(\mathbf{R}^{n})$ ，则 $f(x)$ 的经典Fourier变换为

$$
\hat {f} (\zeta) = \int_ {\mathbf {R} ^ {n}} f (x) \mathrm{e} ^ {- \mathrm{i} x \zeta} \mathrm{d} x.
$$

根据例 1, $f(x)$ 所确定的 S 广义函数为

$$
\langle   T, \varphi \rangle = \int_ {\mathbb {R} ^ {n}} f (x)   \varphi (x) \mathrm{d} x  , \text {当}   \varphi \in \mathcal {S} (\mathbb {R} ^ {n})  .
$$

显然，

$$
\begin{array}{r l} \langle F (T), \varphi \rangle & = \langle T, F (\varphi) \rangle \\ & = \int_ {\mathbb {R} ^ {n}} f (x) F (\varphi) (x) \mathrm{d} x \\ & = \int_ {\mathbb {R} ^ {n}} f (x) \int_ {\mathbb {R} ^ {n}} \varphi (\zeta) \mathrm{e} ^ {- \mathrm{i} \zeta x} \mathrm{d} \zeta \mathrm{d} x \end{array}
$$

$$
\begin{array}{l} = \int_ {\mathbf {R} ^ {n}} \varphi (\zeta) \mathrm{d} \zeta \int_ {\mathbf {R} ^ {n}} f (x) \mathrm{e} ^ {- \mathrm{i} \zeta x} \mathrm{d} x \\ = \int_ {\mathbf {R} ^ {n}} \varphi (\zeta) \hat {f} (\zeta) \mathrm{d} \zeta , \quad \varphi \in \mathcal {S} (\mathbf {R} ^ {n}). \end{array}
$$

故 $F(T)$ 恰是由 $f$ 的Fourier变换 $\hat{f}$ 确定的 $\mathcal{S}$ 广义函数. 这表明 $\mathcal{S}$ 广义函数的Fourier变换是经典Fourier变换的推广.

前面已经指出,任何缓增函数 f 都确定一个 S 广义函数

$$
T (\varphi) = \int_ {\mathbb {R} ^ {n}} f (x) \varphi (x) \mathrm{d} x, \text {当} \varphi \in \mathcal {S} (\mathbb {R} ^ {n}).
$$

从而有相应于 $f(x)$ 的广义的Fourier变换. 所以现在的理论比之经典理论的适用范围宽广多了.

例2 $F(\mathrm{e}^{\mathrm{i}ax})(\zeta) = 2\pi \delta (\zeta -a)$

这里，对 $a \in \mathbb{R}, \delta(\zeta - a)$ 是如下定义的 $\mathcal{S}$ 广义函数：

$$
\langle \delta (\zeta - a), \varphi \rangle \stackrel {\mathrm{d}} {=} \varphi (a), \text {当} \varphi \in \mathcal {S} (\mathbf {R}).
$$

因为对任意的 $\varphi \in \mathcal{S}(\mathbf{R})$

$$
\begin{array}{r l} \langle F (\mathrm{e} ^ {\mathrm{i} a x}), \varphi \rangle & = \langle \mathrm{e} ^ {\mathrm{i} a x}, F (\varphi) \rangle \\ & = \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} a x} \hat {\varphi} (x) \mathrm{d} x \\ & = 2 \pi \varphi (a) \\ & = 2 \pi \langle \delta (\zeta - a), \varphi \rangle . \end{array}
$$

故

$$
F \left(\mathrm{e} ^ {\mathrm{i} a x}\right) (\zeta) = 2 \pi \delta (\zeta - a).
$$

例3 $F(1) = 2\pi \delta$

因为对任意的 $\varphi \in \mathcal{S}(\mathbf{R})$

$$
\langle F (1), \varphi \rangle = \langle 1, F (\varphi) \rangle = \int_ {\mathbb {R}} \hat {\varphi} (x) \mathrm{d} x = \int_ {\mathbb {R}} \mathrm{e} ^ {i 0 x} \hat {\varphi} (x) \mathrm{d} x = 2 \pi \varphi (0) = 2 \pi \langle \delta , \varphi \rangle .
$$

故

$$
F (1) = 2 \pi \delta .
$$

定义2.4 对 $T \in \mathcal{S}'(\mathbf{R}^n)$ , 定义 $F^{-1}(T)$ 为

$$
\langle F ^ {- 1} (T), \varphi \rangle \stackrel {\mathrm{d}} {=} \langle T, F ^ {- 1} (\varphi) \rangle , \quad \text {当}   \varphi \in \mathcal {S} (\mathbf {R} ^ {n})  .
$$

由定理2.2，上式右端是 $\mathcal{S}(\mathbf{R}^n)$ 上按 $\varphi_v\to 0(\mathcal{S})$ 为连续的线性泛函，因此 $F^{-1}(T)$ 是 $\mathcal{S}$ 广义函数.

显然

$$
\begin{array}{r l} \langle F ^ {- 1} (F (T)), \varphi \rangle & = \langle F (T), F ^ {- 1} (\varphi) \rangle \\ & = \langle T, F (F ^ {- 1} (\varphi)) \rangle = \langle T, \varphi \rangle , \varphi \in \mathscr {S} (\mathbf {R} ^ {n}). \end{array}
$$

同理有

$$
\langle F (F ^ {- 1} (T)), \varphi \rangle = \langle T, \varphi \rangle , \quad \varphi \in \mathscr {S} (\mathbf {R} ^ {n}).
$$

这就得到极整齐的反演公式.

定理2.3 $F^{-1}(F(T)) = T, F(F^{-1}(T)) = T$ .

定理 2.4 $F(T)$ 是变 $\mathcal{S}^{\prime}(\mathbf{R}^{n})$ 为 $\mathcal{S}^{\prime}(\mathbf{R}^{n})$ 的拓扑线性同构.

这里 $\mathcal{S}'(\mathbf{R}^n)$ 上的拓扑理解为 $\mathcal{S}'(\mathbf{R}^n)$ 作为 Fréchet 空间 $\mathcal{S}(\mathbf{R}^n)$ 的对偶空间的弱\*拓扑. 即 $T_v \to 0(\mathcal{S}')$ 指的是对任给的 $\varphi \in \mathcal{S}(\mathbf{R}^n)$ ,

$$
\langle   T _ {v}  , \varphi \rangle \to 0  , \text {当}   v \to \infty  .
$$

证由 $F(T)$ 和 $F^{-1}(T)$ 的定义和定理2.3, 可见 $F(T)$ 是线性同构. 若 $T_{v} \to 0(\mathcal{S}')$ , 即对任给的 $\varphi \in \mathcal{S}(\mathbf{R}^{n})$ ,

$$
\langle T _ {\nu}, \varphi \rangle \rightarrow 0, \text {当} \nu \rightarrow \infty .
$$

因为 $F(\varphi) \in \mathcal{S}(\mathbf{R}^n)$ , 故

$$
\langle F (T _ {v}), \varphi \rangle = \langle T _ {v}, F (\varphi) \rangle \to 0, \text {当} v \to \infty .
$$

可见 $F(T_{\nu}) \to 0(\mathcal{S}^{\prime})$ . 所以 $F(T)$ 是连续的. 同样可以证明 $F^{-1}(T)$ 也是连续的. 证毕.

例4 $F(\sin x)(\zeta) = \pi i[\delta (\zeta +1) - \delta (\zeta -1)].$

因为

$$
\sin x = \frac {\mathrm{e} ^ {\mathrm{i} x} - \mathrm{e} ^ {- \mathrm{i} x}}{2 \mathrm{i}}.
$$

于是根据定理2.4与例2可得

$$
\begin{array}{r l} F (\sin x) (\zeta) & = \frac {1}{2 \mathrm{i}} \left[ F \left(\mathrm{e} ^ {\mathrm{i} x}\right) (\zeta) - F \left(\mathrm{e} ^ {- \mathrm{i} x}\right) (\zeta) \right] \\ & = \frac {1}{2 \mathrm{i}} \left[ 2 \pi \delta (\zeta - 1) - 2 \pi \delta (\zeta + 1) \right] \\ & = \pi \mathrm{i} \left[ \delta (\zeta + 1) - \delta (\zeta - 1) \right]. \end{array}
$$

定理 2.3 表明 S广义函数的 Fourier 变换的运算是对称的, 灵活的. 对于定理 2.4, 我们也可以认为它是 $L^{2}$ 理论中 Plancherel 定理的推广. 关于 Plancherel 定理及其证明可参见 [7], 第七章, §4.

广义函数有很多优点,在处理具体问题时,时常考察由通常函数 $f(x)$ 生成的特殊的广义函数

$$
\langle f, \varphi \rangle = \int_ {\mathbf {R} ^ {n}} f (x) \varphi (x) \mathrm{d} x.
$$

必须声明,不能认为广义函数的 Fourier 变换可以完全替代经典的理论,它只是从一个方面发展了原来的理论.

## 习题

1. 试证明 Dirac 函数 $\delta(x)$ 不是 $\mathbf{R}$ 上局部可积函数.

2. 设 $a \in \mathbb{R}$ , 令

$$
H _ {a} (x) \stackrel {\mathrm{d}} {=} \left\{ \begin{array}{l l} 0, & \text {当} x <   a, \\ 1, & \text {当} x \geqslant a. \end{array} \right.
$$

$$
\delta_ {a} (x) \stackrel {\mathrm{d}} {=} \delta (x - a), \forall x \in \mathbf {R}.
$$

证明 $H_{a}^{\prime} = \delta_{a}$

3. 设 $f$ 是 $\mathcal{S}(\mathbf{R})$ 广义函数, 则它也是 $\mathcal{D}(\mathbf{R})$ 广义函数, 且对任意多项式 $p$ ,

$$
\begin{array}{l} F (p (\mathrm{D}) f) (x) = p (x) F (f) (x), \\ F (p f) (x) = p (- \mathrm{D}) F (f) (x), \end{array}
$$

这里 D 表示求导, F 表示 Fourier 变换. 试证明之.

4. 求下列 $\mathcal{S}(\mathbf{R})$ 广义函数的Fourier变换：

(i) $x^{2}$

(ii) $\cos x$ ,

(iii) $\delta(x)$ .

## 附录拓扑空间定义 1 设 X 是一个非空集合, 如果 T 是 X 的子集组成的集合, 具有如下性质:

(1) $\varnothing, X \in \mathcal{T}$ .

(2) $\mathcal{T}$ 中任意多个子集的并集还在 $\mathcal{T}$ 中，即如果 $\{A_{a}\}_{a\in \mathcal{A}}\subset \mathcal{T}$ ，则 $\bigcup_{a\in \mathcal{A}}A_a\in \mathcal{T}$ .

(3) $\mathcal{T}$ 中有限个子集的交集在 $\mathcal{T}$ 中, 即如果 $\{A_j\}_{j=1}^n \subset \mathcal{T}$ , 则 $\bigcap_{j=1}^{\infty} A_j \in \mathcal{T}$ . 则称 $\mathcal{T}$ 为 $X$ 上的一个拓扑, 称 $\langle X, \mathcal{T} \rangle$ 为拓扑空间, 有时也简称 $X$ 为拓扑空间. $\mathcal{T}$ 中的子集称为 $X$ 的开集, $X$ 中的元素称为点.

例 1 设 $\langle X, d \rangle$ 是一个距离空间，令 T 是 X 中全体由距离定义的开集（见第一章，§4）组成的集合，则 T 满足定义 1 的所有条件，故 T 是 X 上一个拓扑，称为由距离 d 所诱导的拓扑。通常我们说距离空间是拓扑空间，指的就是这个拓扑空间 $\langle X, T \rangle$ 。

定义2 设 $\langle X, \mathcal{I} \rangle$ 是一个拓扑空间.

(1) 点 $x \in X, V \subset X$ 称为 $x$ 的邻域, 如果存在 $O \in \mathcal{T}$ , 使 $x \in O \subset V$ .

(2) 子集 $F \subset X$ 称为闭集, 如果 $F$ 的余集 $X \setminus F$ 是开集.

由拓扑和闭集的定义,根据取余集与交和并运算之间的关系式(见[6],第一章,§1),容易验证定理1 设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间，则

(1) $\varnothing, X$ 都是闭集.

(2) 任意多个闭集的交集是闭集.

(3) 有限个闭集的并集是闭集.

定义3 设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间， $\mathcal{U}(x)$ 表示点 $x \in X$ 的全体邻域的集合。 $\mathcal{U}(x)$ 的一个子集合 $\mathcal{V}(x)$ 称为点 $x$ 的邻域基，如果对任何 $U \in \mathcal{U}(x)$ ，总有 $V \in \mathcal{V}(x)$ ，使 $V \subset U$ 。

定理2 设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间， $\psi(x)$ 表示点 $x$ 的邻域基，则

(1) 任给 $V \in \mathcal{V}(x)$ , 必有 $x \in V$ ,

(2) 任给 $V_{1}, V_{2} \in \mathcal{V}(x)$ , 必有 $V_{3} \in \mathcal{V}(x)$ , 使 $V_{3} \subset V_{1} \cap V_{2}$ .

(3) 如果 $V \in \mathcal{V}(x)$ , 必有 $W \in \mathcal{V}(x)$ , 使 $W \subset V$ , 且任给 $y \in W$ , 存在 $U \in \mathcal{V}(y)$ , 使 $U \subset V$ .

证 (1) 是显然的.

(2) 设 $V_{1}, V_{2} \in \mathcal{V}(x)$ , 存在 $V_{1}', V_{2}' \in \mathcal{T}$ , 使 $x \in V_{1}' \subset V_{1}, x \in V_{2}' \subset V_{2}$ , 从而 $x \in V_{1}' \cap V_{2}' \subset V_{1} \cap V_{2}$ . 因为 $V_{1}' \cap V_{2}' \in \mathcal{T}$ , 则 $V_{1} \cap V_{2} \in \mathcal{U}(x)$ , 从而有 $V_{3} \in \mathcal{V}(x)$ , 使 $V_{3} \subset V_{1} \cap V_{2}$ .

(3) 设 $V \in \mathcal{V}(x)$ , 则存在 $V' \in \mathcal{T}$ , 使 $x \in V' \subset V$ . 显然 $V' \in \mathcal{U}(x)$ , 于是有 $W \in \mathcal{V}(x)$ , 使 $W \subset V' \subset V$ . 任给 $y \in W, y \in V'$ , 而 $V'$ 是开集, 所以 $V' \in \mathcal{U}(y)$ . 于是存在 $U \in \mathcal{V}(y)$ , 使 $U \subset V' \subset V$ . 证毕.

反之，我们有定理3 设 $X$ 是一个非空集合, 如果对任何的 $x \in X$ , 都给定 $X$ 子集的非空族 $\mathcal{V}(x)$ , 满足定理2的条件(1)—(3). 则必存在 $X$ 上唯一的拓扑 $\mathcal{T}$ , 在拓扑空间 $\langle X, \mathcal{T} \rangle$ 中每点 $x, \mathcal{V}(x)$ 是 $x$ 的一个邻域基.

这个拓扑 $\mathcal{I}$ 称为由邻域基诱导的拓扑.

证对每点 $x \in X$ , 记 $\mathcal{U}(x) = \{U \subset X: \text{存在 } V \in \mathcal{V}(x), \text{使 } V \subset U\}$ . 定义

$$
\mathcal {R} = \{E \subset X: \forall y \in E, E \in \mathcal {U} (y) \}.
$$

则任给 $E_{1}, E_{2} \in \mathcal{R}$ , 必有 $E_{1} \cap E_{2} \in \mathcal{R}$ . 事实上, $\forall y \in E_{1} \cap E_{2}$ , 由 $y \in E_{1} \in \mathcal{R}$ , 知 $E_{1} \in \mathcal{U}(y)$ , 从而有 $U_{1} \in \mathcal{V}(y)$ , 使 $U_{1} \subset E_{1}$ . 同理有 $U_{2} \in \mathcal{V}(y)$ , 使 $U_{2} \subset E_{2}$ . 于是由条件(2), 存在 $U_{3} \in \mathcal{V}(y)$ , 使 $U_{3} \subset U_{1} \cap U_{2} \subset E_{1} \cap E_{2}$ . 可见 $E_{1} \cap E_{2} \in \mathcal{U}(y)$ , 故 $E_{1} \cap E_{2} \in \mathcal{R}$ .

令 $\mathcal{I}$ 表示由 $\mathcal{R}$ 中任意元的并集形成的族, 则 $\varnothing, X \in \mathcal{I}$ . 又 $\mathcal{I}$ 中任意元的并集还是 $\mathcal{R}$ 中元的并, 因而在 $\mathcal{I}$ 中. 为证 $\mathcal{I}$ 中有限元的交集在 $\mathcal{I}$ 中, 只须证 $\mathcal{I}$ 中任意两个元的交集在 $\mathcal{I}$ 中. 设 $U, V \in \mathcal{I}$ , 如果 $x \in U \cap V$ , 因 $U, V$ 都是 $\mathcal{R}$ 中元的并, 应有 $U', V' \in \mathcal{R}$ , 使 $x \in U' \subset U, x \in V' \subset V$ . 由前证 $x \in U' \cap V' \in \mathcal{R}$ , 因此 $U \cap V = \bigcup \{W: W \in \mathcal{R}, W \subset U \cap V\}$ . 这表明 $U \cap V \in \mathcal{I}$ . 总之 $\mathcal{I}$ 是 $X$ 上一个拓扑.

往证在拓扑空间 $\langle X, \mathcal{T} \rangle$ 中，每点 $x$ 的全体邻域恰是 $\mathcal{U}(x)$ ，从而 $\mathcal{U}(x)$ 恰是点 $x$ 的一个邻域基。

设 $U \in \mathcal{U}(x)$ , 则有 $V \in \mathcal{U}(x)$ , 使 $x \in V \subset U$ . 令

$$
E ^ {\prime} = \bigcup \{y \in X: \text {存在} W \in \mathcal {V} (y), \text {使} W \subset V \}.
$$

任给 $y \in E'$ , 有 $W \in \mathcal{V}(y)$ , 使 $W \subset V$ . 由条件(3), 存在 $W_1 \in \mathcal{V}(y)$ , 使 $W_1 \subset W$ , 且对任意 $z \in W_1$ , 存在 $U_1 \in \mathcal{V}(z)$ , 使 $U_1 \subset W \subset V$ . 可见 $W_1 \subset E'$ , 故 $E' \in \mathcal{U}(y)$ , 因此 $E' \in \mathcal{R}$ . 由 $E'$ 的定义可见 $x \in E' \subset V \subset U$ , 所以 $U$ 是 $x$ 的邻域.

反之，设 $U$ 是 $\pmb{x}$ 的邻域，则存在 $E\in \mathcal{R}$ ，使 $x\in E\subset U$ .根据 $\mathcal{R}$ 的定义， $E\in \mathcal{U}(x)$ ，即有 $V\in \mathcal{V}(x)$ ，使 $V\subset E\subset U$ ，故 $U\in \mathcal{U}(x)$ .总之 $\mathcal{U}(x)$ 是点 $\pmb{x}$ 的全体邻域的集合.

最后证明唯一性. 设 $\mathcal{T}_1, \mathcal{T}_2$ 是 $X$ 上拓扑, 在每点 $x \in X$ , 都以 $\nu(x)$ 为其一个邻域基. 如果 $U \in \mathcal{T}_1$ , 任给 $x \in U, U$ 是 $x$ 的邻域, 因 $\mathcal{V}(x)$ 是 $x$ 的邻域基, 故有 $V \in \mathcal{V}(x)$ , 使 $V \subset U$ . 因此 $U = \bigcup_{x \in U} \{V: V \in \mathcal{V}(x)$ 且 $V \subset U\}$ . 在 $\mathcal{T}_2$ 中 $\mathcal{V}(x)$ 也是 $x$ 的一个邻域基, 故对每个 $V \in \mathcal{V}(x)$ 且 $V \subset U$ , 应有 $W \in \mathcal{T}_2$ , 使 $x \in W \subset V \subset U$ . 从而 $U = \bigcup_{x \in U} \{W: W \in \mathcal{T}_2$ 且 $x \in W \subset U\}$ . 故 $U$ 亦在 $\mathcal{T}_2$ 中, 即 $\mathcal{T}_1 \subset \mathcal{T}_2$ . 同样可以证明 $\mathcal{T}_2 \subset \mathcal{T}_1$ . 总之 $\mathcal{T}_1 = \mathcal{T}_2$ . 证毕.

这个定理告诉我们, 对一个非空集合, 可以通过在每点给定满足定理 2 的条件 (1)—(3) 的一族子集, 即在每点给定邻域基的方法引进拓扑. 本书在引进局部凸拓扑线性空间或 Banach 空间上弱拓扑时都是这样做的.

定义4 设 $\mathcal{V}_1(x), \mathcal{V}_2(x)$ 分别是拓扑 $\mathcal{T}_1, \mathcal{T}_2$ 在点 $x \in X$ 的邻域基. 如果任给 $V_1 \in \mathcal{V}_1(x)$ , 有 $V_2 \in \mathcal{V}_2(x)$ , 使 $V_2 \subset V_1$ , 而且任给 $V'_2 \in \mathcal{V}_2(x)$ , 也有 $V'_1 \in \mathcal{V}_1(x)$ , 使 $V'_1 \subset V'_2$ , 则称 $\mathcal{V}_1(x)$ 与 $\mathcal{V}_2(x)$ 等价.

根据定理2、定理3及其证明容易证出，如果一个非空集合 $X$ 上两个拓扑在每点 $x \in X$ 的邻域基都等价，则这两个拓扑相同.

定义5 设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间, 如果 $X$ 中任意两个不同的点都有不相交的邻域, 称 $X$ 为Hausdorff空间.

例2 距离空间 $\langle X, d \rangle$ 是 Hausdorff 空间.

设 $x_0, y_0 \in X, x_0 \neq y_0$ ，则 $\delta = d(x_0, y_0) > 0$ . 令

$$
U _ {0} = \left\{x: d (x, x _ {0}) <   \frac {\delta}{3} \right\},
$$

$$
V _ {0} = \{x: d (x, y _ {0}) <   \frac {\delta}{3} \}.
$$

则 $U_{0}, V_{0}$ 分别是 $x_{0}, y_{0}$ 的邻域，且 $U_{0} \cap V_{0} = \emptyset$

设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间， $E \subset X, \{A_{\alpha}\}_{\alpha \in \mathcal{A}} \subset \mathcal{T}$ . 如果

$$
E \subset \bigcup_ {\alpha \in \mathcal {A}} A _ {\alpha},
$$

称 $\{A_{\alpha}\}_{\alpha \in \mathcal{A}}$ 是 $E$ 的一个开覆盖. 如果 $\mathcal{A}_1 \subset \mathcal{A}$ , 而且

$$
E \subset \bigcup_ {\alpha \in \mathscr {A} _ {1}} A _ {\alpha}
$$

则称 $\{A_{a}\}_{a\in \mathcal{A}}$ 为 $\{A_{a}\}_{a\in \mathcal{A}}$ 的一个子覆盖.

定义6 设 $\langle X, \mathcal{T} \rangle$ 是拓扑空间, $E \subset X$ . 如果 $E$ 的每个开覆盖都有有限的子覆盖, 称 $E$ 为紧集. 如果 $X$ 是紧集, 称 $X$ 为紧空间. 如果 $X$ 的每一点都有紧的邻域, 称 $X$ 为局部紧的.

设 $\langle X, \mathcal{T} \rangle, \langle Y, \mathcal{S} \rangle$ 都是拓扑空间， $f: X \to Y$ 是映射， $x_0 \in X$ 。如果对 $f(x_0)$ 的每个邻域 $V$ ，存在 $x_0$ 的邻域 $U$ ，使 $f(U) \subset V$ ，则称 $f$ 在 $x_0$ 处连续。如果 $f$ 在 $X$ 上每点都连续，称 $f$ 为连续映射。

定理4 设 $X, Y$ 都是拓扑空间， $f: X \to Y$ 是映射，则下述等价：

(1) f 是连续映射.

(2) 对 $Y$ 中任意开集 $O, f^{-1}(O)$ 是 $X$ 中开集.

(3) 对 $Y$ 中任意闭集 $F, f^{-1}(F)$ 是 $X$ 中闭集.

这里 $f^{-1}(O), f^{-1}(F)$ 分别表示 $O, F$ 在 $X$ 中的原像.

(1)与(2)等价的证明完全类似于第一章§4中定理4.1的证明，(2)与(3)等价的证明由开集与闭集互为余集得到.

定义7 设 $\langle X, \mathcal{T} \rangle$ 与 $\langle Y, \mathcal{S} \rangle$ 都是拓扑空间，如果映射 $f: X \to Y$ 是双射的（单射且满射），而且 $f, f^{-1}$ 都是连续的，则称 $f$ 是同胚，并称拓扑空间 $\langle X, \mathcal{T} \rangle$ 与 $\langle Y, \mathcal{S} \rangle$ 是同胚的.

设 $\langle X, \mathcal{T} \rangle$ 是一个拓扑空间， $f(x)$ 是X上复值函数，则集合

$$
\operatorname{supp} (f) = \overline {{\{x \in X : f \mid x \mid \neq 0 \}}}
$$

称为 $f$ 的支集.

## 参考文献

[1] 戈丁 L. 数学概观. 胡作玄译. 北京: 科学出版社, 1984

[2] 北京大学数学力学系几何与代数教研室代数小组. 高等代数. 北京: 人民教育出版社, 1978

[3] 吉田耕作. 泛函分析. 吴元恺, 孙顺华, 唐志远, 黄发伦译. 北京: 人民教育出版社, 1980

[4] 伍鸿熙, 吕以辇, 陈志华. 紧黎曼曲面引论. 北京: 科学出版社, 1983

[5] 江泽坚. 线性泛函分析选讲. 成都: 中国科学院成都分院数理科学研究室, 1982

[6] 江泽坚, 吴智泉. 实变函数论. 北京: 人民教育出版社, 1973

[7] 江泽坚, 吴智泉. 实变函数论. 第二版. 北京: 高等教育出版社, 1994

[8] 江泽坚, 吴智泉, 周光亚. 数学分析上册. 北京: 人民教育出版社, 1964

[9] 关肇直. 泛函分析讲义. 北京: 高等教育出版社, 1958

[10] 关肇直, 张恭庆, 冯德兴. 线性泛函分析入门. 上海: 上海科学技术出版社, 1979

[11] 刘斯铁尔尼克 JIA, 索伯列夫 BИ. 泛函分析概要. 第二版. 杨从仁译. 北京: 科学出版社, 1985

[12] 米赫林 CΓ. 数学物理中的直接方法. 周先意译. 北京: 高等教育出版社, 1957

[13] 那汤松 И. П. 实变函数论. 徐瑞云译. 北京: 高等教育出版社. 1959

[14] 克列菌, 刘斯铁尔尼克. 三十年来的苏联数学: 泛函数分析. 关肇直译. 北京: 中国科学院出版, 1953

[15] 陈文塬. 非线性泛函分析. 兰州: 甘肃人民出版社, 1982

[16] 郑维行, 王声望. 实变函数与泛函分析概要第二册. 北京: 人民教育出版社, 1980

[17] 哈尔莫斯 PR. 希尔伯特空间问题集. 林辰译. 上海: 上海科学技术出版社, 1984

[18] 夏道行, 吴卓人, 严绍宗, 舒五昌. 实变函数论与泛函分析下册. 第二版. 北京: 高等教育出版社, 1985

[19] 夏道行, 严绍宗, 舒五昌, 童裕孙. 泛函分析第二教程. 北京: 高等教育出版社, 1983

[20] 索波列夫 C JI. 数学物理方程. 钱敏等译. 北京: 高等教育出版社, 1958

[21] 戚征. 选择公理与连续统假设. 数学进展, 1984, 13(1): 4\~22

[22] 黎茨 F. 塞克佛尔维 B-纳吉, 泛函分析讲义. 第二卷. 庄万等译. 北京: 科学出版社, 1981

[23] 葛锁网. 应用泛函分析基础. 北京: 高等教育出版社, 1990

[24] Aronszajn N, Smith K T. Invariant subspaces of completely continuous operators. Ann. Math., 1954(60):345\~350

[25] Cowen M, Douglas R G. Complex geometry and operator theory. Acta Math., 1978 (141): 187\~261

[26] Dieudonné J. History of Functional Analysis. Amsterdam: North-Holland Publishing Company, 1981

[27] Dunford N, Schwartz J T. Linear Operators, Part I, General Theory. New York: John Wiley & Sons, 1957

[28] Dvoretzky A, Rojers C A. Absolute and unconditional convergence in normed linear spaces. Proc. Nat. Acad. Sci. U. S. A., 1950(36): 192\~197

[29] Enflo P. A counterexample to the approximation problem in Banach spaces. Acta Math., 1973(130): 309\~317

[30] Fréchet M. Les espaces a abstraits topologiquement affines. Acta Math., 1926(47): 25\~52

[31] Horvath J. Topological Vector Spaces and Distributions. I. Addison-Wesley Reading. Mass., 1966

[32] Hutson V, Pym J S. Applications of Functional Analysis and Operator Theory. New York: Academic Press, 1980

[33] James R C. A non-reflexive Banach space isometric with its second conjugate space. Proc. Nat. Acad. Sci. U. S. A., 1951(37): 174\~177

[34] Kreyszig E. Introductory Functional Analysis with Applications. New York: John Wiley & Sons, 1978

[35] Lindenstrauss J, Tzafriri I. On the complemented subspaces problem. Israel J. Math., 1971 (9):263\~269

[36] Lorch E R. Spectral Theory. New York: Oxford University Press, 1962

[37] Murray F J. On complementary manifolds and projections in spaces $L_{p}$ and $l_{p}$ , Trans. Amer. Math. Soc., 1937 (41): 138\~152

[38] Read C J. A solution to the invariant subspace problem. Bull. London Math. Soc., 1984 (16):337\~401

[39] Reed M, Simon B. Methods of Modern Mathematical Physics, I: Functional Analysis. New York: Academic Press, 1972

[40] Rudin W. Functional Analysis. New York: McGraw-Hill Book Company, 1973

[41] Stone M H. Linear Transformations in Hilbert Space and Their Applications to Analysis. Amer. Math. Soc. Colloquium Pub. Vol. 15, 1932

[42] Taylor A E, Halberg C J A Jr., General theorems about a bounded linear operator and its conjugate. J. Reine Angew. Math., 1957 (198): 93-111.

[43] Taylor A E, Lay D C. Introduction to Functional Analysis. New York: John Wiley & Sons, 1989

[44] Zaanen A C. An Introduction to the Theory of Integration. Amsterdam: North-Holland Publishing Company, 1958

开的(open) I.4  
开映射(open mapping) III.6  
开映射定理(open mapping theorem) III.3  
开集(open set) 附录开覆盖(open cover) 附录无处稠密(nowhere dense) III.3  
无穷维的(infinite dimensional) I.2  
支集(support) 附录不动点(fixed point) I.9  
不变子空间(invariant subspace) IV.2  
内点(interior point) I.4  
内部(interior) I.4  
内积(inner product) II.1  
内积空间(inner product space) II.1  
分离(separate) III.2  
分离点(separate points) I.8  
双边理想(biside ideal) IV.3  
双边移位算子(bilateral shift operator) IV.6  
双线性泛函(bilinear functional) II.3

## 索引说明:以下数字Ⅲ.3表示第三章第三节,其余类推.

## 一一三画一致有界原理(uniform boundedness principle) Ⅲ.3

二次对偶(bidual) Ⅲ.4

下半弱连续的(weakly lower semi-continuous) Ⅲ.7

上界(upper bound) I.1

广义解(generalized solution) Ⅱ.4

子空间(subspace) I.7

子覆盖(subcover) 附录

## 四画

## 五画可分的(separable) I.4
正交的(orthogonal) II.1
正交补(orthogonal complement) II.3
正交射影(orthogonal projection) II.3, IV.4
正规正交基(orthonormal basis) II.2
正规正交集(orthonormal set) II.1
正规算子(normal operator) IV.习题正算子(positive operator) IV.4
本质上确界(essential least upper bound) I.3
本质有界可测函数(essentially bounded measurable function) I.3
本质有界可测函数空间(space of essentially bounded measurable functions) I.3
左理想(left ideal) IV.3
右理想(right ideal) IV.3
平行四边形法则(parallelogram law) II.1
平移算子(translation operator) IV.6
平衡的(balanced) III.2
凸的(covex) III.2
代数互补的(algebraic complementary) I.2
代数补(algebraic complement) I.2
半范数(semi-norm) I.8
加法(addition) I.2
对角线方法(diagonal method) I.6
对偶空间(dual space) II.3, III.4

## 六画共轭双线性泛函(conjugate bilinear functional) II.3  
共轭同构(conjugate isomorph) II.3  
共轭空间(cojugate space) II.3  
共轭线性的(conjugate linear) II.3  
共鸣定理(resonance theorem) III.3  
有序集(ordered set) I.1  
有限秩算子(finite rank operator) IV.3  
有限维的(finite dimensional) I.2  
有界的(bounded) I.习题有界可逆的(bounded invertible) I.7  
有界自伴算子谱分解定理(spectral decomposition theorem for

bounded selfadjoint operator) IV.5  
有界序列空间(space of bounded sequences) I.3  
有逆(have an inverse) I.7  
压缩(contraction) I.9  
压缩映象原理(contraction mapping principle) I.9  
列紧的(sequentially compact) I.6  
同胚(homeomorphism) 附录同胚的(homeomorphic) 附录同等连续的(equicontinuous) I.6  
吸收的(absorbing) III.2  
收敛序列空间(space of convergent sequences) I.3  
自反空间(reflexive space) III.4  
自共轭性(self-conjugacy) II.3  
自共轭算子(self-conjugate operator) IV.4  
自列紧集(self-sequentially compact set) I.6  
自伴算子(selfadjoint operator) IV.4  
自然同态(natural homomorphism) III.6  
向量(vector) I.2  
向量空间(vector space) I.2  
全连续算子(completely continuous operator) IV.3  
闭图形定理(closed graph theorem) III.3  
闭的(closed) I.4  
闭值域定理(closed range theorem) III.6  
闭集(closed set) 附录闭算子(closed operator) III.3  
导数(derivative) V.1  
约化子空间(reduced subspace) IV.2  
阶(order) I.8

## 七画酉等价(unitary equivalent) IV.6  
酉算子(unitary operator) IV.6  
极大元(maximal element) I.1  
极化恒等式(polarization identity) II.1  
极限点(cluster point) I.4  
严格凸的(strictly covex) III.7  
两择一定理(alternative theorem) IV.3  
拟幂零算子(quasinilpotent operator) IV.1

连续(continuous) I.4
连续函数(continuous function) I.4
连续函数空间(space of continuous functions) I.5
连续映射(continuous mapping) 附录连续谱(continuous spectrum) IV.1
伴随算子(adjoint operator) II.4
邻域(neighborhood) I.4,附录邻域基(base for neighborhoods) 附录近似点谱(approximate point spectrum) IV.4
良序的(well ordered) I.1
良序定理(well ordering theorem) I.1
序列 $\{f_{n}\}_{n=1}^{\infty}$ 弱\*收敛到 $f(\text{sequence}\{f_{n}\}_{n=1}^{\infty} \text{is weak}^{*}\text{convergent to } f)$ III.7
序列 $\{x_{n}\}_{n=1}^{\infty}$ 弱收敛到 $x_{0}(\text{sequence}\{x_{n}\}_{n=1}^{\infty} \text{is weak convergent to } x_{0})$ III.7
完全有序的(totally ordered) I.1
完全有界的(totally bounded) I.6
完备化(completion) I.5
完备的(complete) I.5
张成的(spanned) I.2
局部凸的(locally convex) III.8
局部紧的(locally compact) 附录

## 八画范数(norm) I.7  
范数 $\| \cdot \| _1$ 强于 $\| \cdot \| _2$ (norm $\| \cdot \| _1$ is stronger than $\| \cdot \| _2$ ) III.1  
直接和(direct sum) I.2  
拓扑(topology) 附录拓扑互补子空间(topological complementary subspace) III.2, IV.2  
拓扑补(topological complement) IV.2  
拓扑空间(topological space) 附录图形(graph) III.3  
典型映射(canonical mapping) III.4  
和(sum) I.2  
所有序列空间(space of all sequences) I.3  
单边移位算子(unilateral shift operator) IV.1  
单射的(injective) I.7  
空间 $L^p$ (space $L^p$ ) I.3  
空间 $I^p$ (space $I^p$ ) I.3  
定义域(domain) III.3

线性无关的(linearly independent) I.2  
线性泛函(linear functional) I.7  
线性组合(linear combination) I.2  
线性空间(linear space) I.2  
线性相关的(linear dependent) I.2  
线性流形(linear manifold) I.2  
距离线性空间(metric linear space) I.3  
赋范线性空间(normed linear space) I.7  
线性算子(linear operator) I.7  
线性簇(linear variety) III.2  
限制(restriction) IV.2

## 九画标量值谱测度(scalar spectral measure) IV.5  
指标(index) IV.3  
指标定理(index theorem) IV.3  
点(point) I.2  
点谱(point spectrum) IV.I  
恒等算子(identity operator) I.习题重指标(multiindex) I.8  
选择公理(axiom of choice) I.1  
保范算子(operator preserving norm) IV.6  
急减函数(rapidly decreasing function) V.2  
急减函数空间(space of rapidly decreasing functions) I.8  
逆算子(inverse operator) I.7

## 十画真的(proper) I.2  
换位(commutant) IV.2  
紧的(compact) I.6  
紧空间(compact space) 附录紧集(compact set) 附录紧算子(compact operator) IV.3  
特征元(eigenvector) IV.1  
特征值(eigenvalue) IV.1  
值域(range) I.7  
射影(projection) IV.2  
射影定理(projection theorem) II.3

部分有序的(partially ordered) I.1  
弱开集(weakly open set) III.8  
弱列紧的(weakly sequentially compact) III.7  
弱\*列紧的(weak\*sequentially compact) III.7  
弱邻域基(base for weak neighborhoods) III.8  
弱序列闭的(weakly sequentially closed) III.2  
弱拓扑(weak topology) III.8  
弱聚点(weak clusion) III.8  
弱解(weak solution) V.引言弱解析(weakly analytic) IV.1  
预解式(resolvent) IV.1  
预解集(resolvent set) IV.1  
陪集(coset) III.6

## 十一画球(ball) I.4  
理想(ideal) IV.3  
基(basis) I.2  
距离(metric) I.3  
距离空间(metric space) I.3  
第一纲点集(set of the first category) III.3  
第一预解公式(the first resolvent formula) IV.1  
第二纲点集(set of the second category) III.3  
第二预解公式(the second resolvent formula) IV.习题商范数(quotient norm) III.6  
商空间(quotient space) III.6  
商映射(quotient map) III.6  
隐函数存在定理(implicit function theorem) I.9  
维数(dimension) I.2

## 十二画超平面(hyperplane) Ⅲ.2
超限归纳法(transfinite induction) I.1
最佳逼近元(best approximation element) Ⅲ.7
剩余谱(residual spectrum) IV.1
等价关系(relation of equivalence) Ⅲ.6
等价范数(equivalent norm) Ⅲ.1
等价类(equivalent class) Ⅲ.6

幂等的(idempotent) IV.2  
强解析(strongly analytic) IV.1  
缓增函数(slowly increasing function) V.2

## 十三画零元(zero element) I.2  
零化子(annihilater) III.6  
零空间(null space) II.4  
稠密集(dense set) I.4  
解析的(analytic) IV.1  
满射的(surjective) I.7  
数乘(scalar multiplication) I.2

## 十四画算子函数(operator function) IV.5
谱(spectrum) IV.1
谱半径(spectral radius) IV.1
谱半径公式(spectral radius formula) IV.1
谱测度(spectral measure) IV.5
谱族(spectral family) IV.5
Baire 纲定理(Baire category theorem) III.3
Banach 共轭算子(Banach conjugate operator) III.5
Banach 扩张定理(Banach extension theorem) III.2
Banach 空间(Banach space) I.7
Banach 逆算子定理(Banach inverse operator theorem) III.3
Bessel 不等式(Bessel's inequality) II.1
Cauchy 序列(Cauchy sequence) I.5
Cayley 变换(Cayley transform) IV.6
Dirac 函数(Dirac function) V.1
D广义函数(Dgeneralized function) V.1
F-空间(F-space) I.8
Fréchet 可微(Fréchet differentiable) I.9
Fréchet 导数(Fréchet derivative) I.9
Fréchet 空间(Fréchet space) III.8
Fréchet-Riesz 表现定理(Fréchet-Riesz representation theorem) II.3
Fredholm 交替定理(Fredholm alternative theorem) IV.3
Fredholm 算子(Fredholm operator) IV.3

Hahn-Banach定理(Hahn-Banach theorem) III.2   
Hahn-Banach定理的几何形式(geometric form of the Hahn-Banach theorem) III.2   
Hamcl基(Hamel basis) I.2   
Hausdorff空间(Hausdorff space) 附录   
Hellinger-Toeplitz定理(Hellinger-Toeplitz theorem) III.3   
Hilbert共轭算子(Hilbert conjugate operator) II.4   
Hilbert空间(Hilbert space) II.1   
Jacobi矩阵(Jacobi matrix) I.9   
Lax-Milgram定理(Lax-Milgram theorem) II.4   
Lipschitz条件(Lipschitz condition) I.9   
Lipschitz常数(Lipschitz constant) I.9   
Minkowski泛函(Minkowski functional) III.2 $\{\mathcal{M},\mathcal{N}\}$ 约化 $T(\{\mathcal{M},\mathcal{N}|\text{reduce} T)$ IV.2   
Montel定理(Montel theorem) I.6   
Neumann级数(Neumann series) III.1,IV.1   
Parseval公式(Parseval formula) II.2 $p$ 阶平均收敛(mean convergence of order $p$ ) I.3 $p$ 幂可积函数 $(p$ -power integrable function) I.3 $\mathcal{S}$ 广义函数 $(\mathcal{S}$ generalized function) V.2   
Riesz引理(Riesz lemma) I.7   
Riesz-Schauder理论(Riesz-Schauder theory) IV.3   
Schmidt正规正交法(Schmidt orthogonalization process) II.2   
Schwarz不等式(Schwarz inequality) II.1   
Volterra积分算子(Volterra integral operator) III.1 $\psi_{1}(x)$ 与 $\psi_{2}(x)$ 等价 $(\psi_{1}(x)$ is equivalent to $\psi_{2}(x))$ 附录 $x$ 与 $A$ 的距离(distance from $x$ to $A)$ I习题   
Zorn引理(Zorn's lemma) I.1 $\varepsilon-\text{网}(\varepsilon-\text{net})$ I.6

## 记号表说明:数字IV.4表示第四章第四节,其余类推. $A \leqslant B$ IV.4 $A^{*}$ II.4 $A^{\prime}$ III.5 $A(\bar{D})$ I.7 $A^{2}(D)$ II.1 $A^{\prime}(x)$ I.9 $\arg z$ 复数z的辐角的主值 $B(x_{0},r)$ I.4 $B_{n}(\Omega)$ IV.1 $C[0,1]^{*}$ I.5 $C(\Omega)$ I.7 $C_{0}^{*}(\Omega)$ II.1
C 复数域 $\mathcal{C}(\Omega)$ I.8 $\mathcal{C}^{m}(\Omega)$ I.8
(c) I.3 $D^{p}(F)$ V.1 $\mathcal{Q}(T)$ III.3
G V.1 $\mathcal{D}^{\prime}(\mathbf{R})$ V.1
detA I.9
dimX I.2
d(x,y) I.3
dist( $x_{0},E$ ) I.习题 $\operatorname{esssup}_{t\in[0,1]}\left|f(t)\right|$ I.3 $\mathcal{F}(X)$ IV.3 $\hat{f}$ V.引言 $f^{-1}(O)$ I.4 $f_{n}\stackrel{w*}{\longrightarrow}f$ III.7 $^{0}G$ III.6 $G(T)$ III.3

$H^{*}$ II.3 $H^{p}$ I.7 $H^{\infty}$ I.7 $H_{0}^{+}(\Omega)$ II.1 $H\setminus H_{1}$ 集合 $H_{1}$ 在集合 $H$ 中的余集
ind(T) IV.3
intK I.8
kerf III.2 $\mathcal{X}(X)$ IV.3
LatT IV.2 $L^{2}[a,b]$ II.1 $L^{p}$ I.7 $L^{p}[a,b]$ I.3 $L^{p}(\Omega,\mu)$ I.7 $L^{\infty}[a,b]$ I.3 $L(H)$ II.4 $L(X)$ III.1 $L(X,Y)$ III.1
|t| I.8 $t^{2}$ II.1 $t^{p}$ I.3 $t^{\infty}$ I.3 $M^{0}$ III.6 $M[a,b]$ I.习题
(m) I.3
m(E) 集合 $E$ 的Lebesgue测度 $\max\{\alpha_{1},\cdots,\alpha_{n}\}$ 实数 $\alpha_{1},\cdots,\alpha_{n}$ 中最大数 $\min\{\alpha_{1},\cdots,\alpha_{n}\}$ 实数 $\alpha_{1},\cdots,\alpha_{n}$ 中最小数 $N(T)$ 算子 $T$ 的零空间 $N(x'_{1},\cdots,x'_{n};\varepsilon)$ III.8 $N^{n}$ I.8 $R(T)$ 算子 $T$ 的值域 $R(\lambda,T)$ IV.1
R 实数域 $R^{n}$ n维欧氏空间
S[0,1] I.8
sgnz III.1 $\mathcal{S}(R^{n})$ I.8,V.2

$S_{p}\{A\}$ I.2
supp{f} II.1,附录
(s) I.3
{T}' IV.2
T|M IV.2
<T,φ> V.引言 $u_{x},u_{y}$ II.3
V[a,b] I.习题 $V_{a}^{b}(x)$ I.习题
var(g) III.4 $X'$ III.4 $X''$ III.4
X/M III.6 $x^{i}$ I.8
[x] III.6
||x|| 元素x的范数 $x_{0}+M$ III.2 $x_{n}\rightarrow x$ I.4 $x_{n}\xrightarrow{w}x$ III.7
xRy III.6
x⊥y II.1
(x,y) II.1
〈x,y〉 III.3 $\varepsilon_{k}\searrow0$ 正数序列 $\{\varepsilon_{k}\}$ 单调下降趋于0 $\varphi_{n}\rightarrow\varphi(\mathcal{D})$ V.1 $\varphi_{v}\rightarrow0(\mathcal{S})$ V.2 $\sigma(T)$ IV.1 $\sigma_{a}(T)$ IV.4 $\sigma_{c}(T)$ IV.1 $\sigma_{p}(T)$ IV.1 $\sigma_{r}(T)$ IV.1 $\rho(T)$ IV.1 $p_{Kl}(f)$ I.8 $\rho_{lm}(f)$ I.8 $\Delta u$ II.4 $\nabla u$ II.4 $\delta_{jk}$ Kronecker常数，II.1本书第一版荣获国家教委第三届高等学校优秀教材一等奖国家教委 1997 年度科技进步二等奖

<table><tr><td> $\partial^{l}f$ </td><td>I.8</td></tr><tr><td> $\frac{\partial f}{\partial y}(x,y)$ </td><td>I.9</td></tr><tr><td> $\partial\Omega$ </td><td>I.6</td></tr><tr><td> $\lambda A+\mu B$ </td><td>III.3</td></tr><tr><td> $\emptyset$ </td><td>空集</td></tr><tr><td> $\oplus$ </td><td>直接和</td></tr><tr><td> $\prec$ </td><td>I.1</td></tr><tr><td> $\cong$ </td><td>保范同构</td></tr><tr><td> $\stackrel{d}{=}$ </td><td>表示左端由右端定义</td></tr><tr><td> $\Rightarrow$ </td><td>表示左端蕴含右端</td></tr><tr><td> $\Leftarrow$ </td><td>表示右端蕴含左端</td></tr><tr><td> $\Leftrightarrow$ </td><td>表示左,右两端等价</td></tr><tr><td> $V_{\alpha\in\mathcal{A}}M_{\alpha}$ </td><td>IV.1</td></tr></table>

![](../../../../04_Assets/Images/Courses/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90/%E6%B3%9B%E5%87%BD%E5%88%86%E6%9E%90%28%E7%AC%AC2%E7%89%88%29%20%28%E6%B1%9F%E6%B3%BD%E5%9D%9A%2C%20%E5%AD%99%E5%96%84%E5%88%A9%29%20%28z-library.sk%2C%201lib.sk%2C%20z-li/images/batch_0001/30dd6bc3aa30189a3e2e12d75cc119f9052ed94548e9e5ee0164226d775aacce.jpg)