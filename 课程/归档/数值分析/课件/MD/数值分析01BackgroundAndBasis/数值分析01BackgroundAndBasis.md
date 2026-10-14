---
raw_title: 数值分析01BackgroundAndBasis
subject: 数值分析01BackgroundAndBasis
source: 数值分析01BackgroundAndBasis.pptx
status: mineru解析
parser: mineru
---

## 数值分析

## 电子科技大学，数学科学学院

## 申华教授

## huashen@uestc.edu.cn

## 课程概况

- 48学时，3学分
- 目标：

1. 理解并掌握经典算法的核心思想和理论
2. 编程实现算法的能力
3. 设计、分析算法的能力

- 先修课程：

数学分析、高等代数、任一程序设计语（C/C++/Python/Matlab）

- 考核方式：

平时成绩占40%（课堂、作业等；作业抄袭一次总成绩扣15分）

期末考试（闭卷）成绩占60%。

## 课程概况

- 教材与参考书

![](images/16d3b8377e3b7fa5c90c58a3c1b238dd5a384bd0c65fb7c716d5eaa2ea4f7402.png)

![](images/4a6360a58b9ba06a5c28294864bc35e3d8e72122c49f1cbb5d3b7e8d7cfb0a52.jpg)

## 课程概况

- 主要内容：

1. 背景与基础知识
2. 非线性方程求根方法
3. 解线性方程组的直接法和迭代法
4. 特征值与特征向量的计算
5. 插值与数据拟合
6. 数值微分与数值积分
7. 常微分方程数值解

- 需要自行回顾的基础知识

1. 一元函数及多元函数Taylor展式
2. 极限、连续函数介值定理、拉格朗日中值定理等
3. 线性代数的一些基本概念（行列式、特征值、特征向量、逆矩阵等）

## 数值分析基础

- 科学计算简介
- 误差的概念
- 计算机中数的表示
- 数值计算的基本原则
- 数值稳定性的概念

## 什么是科学计算？

- 科学计算是指利用计算设备(电子计算机)来解决科学和工程中的问题的一种手段。其核心研究内容是计算方法、数值分析、程序设计。
- 科学计算涉及的领域：计算数学（算法设计与理论分析）+计算机科学（硬件、软件）+X（应用方向）
- X=力学、物理、化学、生物学、金融学、工程。。。

## 一些历史

- 《九章算术注》，割圆术：割之弥细，所失弥少，割之又割，以至于不可割，则与圆周合体而无所失矣。
- 刘徽计算的圆周率：3.14（徽率，96边形），3.1416（3072边形）。

![](images/88617fb86c0ef86e007411ff54aef3a9c644ff3a45c8fbcc9f26f3a152637b88.jpg)

![](images/ed1e29e7a032fde999248a6e81456b41b04d057813feec31a275e83f2c093ba8.jpg)

刘徽（约225年—约295年，魏晋）

![](images/d3f422ab1238ac8b6e729f8a89e3e096dc38fc37cfcfc35e998b2c7d5b2e41f6.jpg)

九章算术成书于约公元前150年，

刘徽注本（约225年—约295年，魏晋）

## 一些历史

- 巴比伦人（3500年前），求平方根

![](images/95775aa98108cf3591928504bb9dc47e16548fe0edb5b9ced9831b849eb697ce.jpg)

## 一些历史

![](images/e9b7dc974cbc007b9cb513ecafb821cd4d479a16a6223269131cd931c3f5ba80.jpg)

(570BC\~490BC)

## 一些历史

![](images/2b226fce6f02b620796d80003676947adb225e6cb7550f6cacfd9fc4bccb88fe.jpg)

Pierre-Simon marquis de Laplace

(1749-1827)

![](images/610b534cbec9f5513167948dbc4ef83ce3abe815f7227e9fe0f83c465869b278.jpg)

“拉普拉斯妖”：一个知道宇宙过去和未来所有事情的恶魔

## 一些历史

- 1910年Lewis Fry Richardson 提出一种数值方法来求解偏微分方程第一次尝试预报未来天气。（耗时三个月预测未来24小时天气，估计需要6万人才能提前预报24小时天气）

![](images/b856371ae445b2455f771f81839ef062d84908df12eee68b725e5dbe17fceb65.jpg)

手摇计算机

![](images/8d866c901a5fc05c8527732b51b931ffbc67a27591357936e39c24c15586b91b.jpg)

## 一些历史

![](images/002c29efa817e9b069a7fec075e0826cb7a56d50998655659d8b0281b7602a89.jpg)

世界首台电子计算机ENIAC(1946年)：18000个电子管，占地170平方米，重达30吨，耗电功率约150千瓦，每秒钟可进行5000次运算

## 一些历史

![](images/053189e22e5f883f0d6da92c50b6fbde3fa30a9491756fca4347c4445592cf6b.png)

Moore’s law: the number of transistors in a dense integrated circuit (IC) doubles about every two years.

## 一些历史

- 最早的计算机指令：打孔纸带
- FORTRAN (FORmulaTRANslator, 1950s由IBM开发) :世界上最早的计算机高级程序设计语言，广泛应用于科学和工程计算领域
- MATLAB (MATrix LABoratory):源于数学家Cleve Moler 1960s的博士论文

![](images/35976f3764f12ff1231bf5fe674a95a24dd7f4ed11a3dd46dc231fc730d308d7.jpg)

## 科学计算的一些发展现状

![](images/618c589ed040195ce4068201e3af59c136b8abcb8c77a9d539aebc03915ef257.jpg)

- 硬件性能快速提升

![](images/81e030255e0de5c8c11c30cca24c2b973e998078b49bd276f91a1b0d2de00de7.jpg)

![](images/133aa826e8641d7b3c86e33fcd8bf9ff1551a977d02a896d56448e8c0ef92310.jpg)

![](images/2855321ee2c4e4e082708fb3da0569f6a7b50e76892a1b2b3bc4e597e0b72a9a.jpg)

![](images/ae9f8b52a339a36a10b219495f28e25e620d094a9b023d62da8d3aa8fbd447ef.png)

![](images/c653eaf52d628f5f416110f66a84c2cdd7e6fd043f94f48e094aa711110c2e3a.jpg)

![](images/6c6a17877503fb909fc2a7f34eaad72de5e6013cce5f94387a244fc060cc87ba.jpg)

- 计算能力是国家综合实力的重要指标

![](images/0b82a3a730dc7b68c61cd4ebe0a95ec418b7df2e177e3e26629b31376f96263c.jpg)

![](images/1775cb7a25d6610feb3fd9842500720327e15554566f03db32b41fb9630eb113.jpg)

![](images/4e2a5e91a5b13155d08c4a2cc71a6f4d4dcee24d6784b3772de6c207b0ba3f0f.jpg)

![](images/f6b2e1c2f9f526bde838ec7582a8642aae43f77100c69261e1ddd357f4ab3d54.jpg)

![](images/221e07ec9c42be05fec4900e3578514f22c3c6e91453c7fbb0006fd27cd3d2d2.jpg)

![](images/7479205f7af8f44f2177749fb4da9ea5ddef05f322746d72d64703035e0a597d.png)

2016年6月-2017年11月，排名第1

2025年11月，排名第24

2021年11月（TOP500 List)

2022年6月（TOP500 List)

2024年11月（TOP500 List)

2023年11月/2024年6月（TOP500 List)

2025年6月/11月（TOP500 List)

2022年11月/2023年6月（TOP500 List)

![](images/a673220bbac227e61b0d3bcb546fabc9410c5f345fa9879ec035b2c1ac23c0d5.jpg)

![](images/d004062735273f28bf456b3e90c137ffbe89e6bedf49a3e5b6231687a68094d3.jpg)

AIAA CFD Vision 2030

计算规模越来越大

![](images/2fdff6797a7631e15d1a246e0235f6994badb11e625051e47b27e806349738be.jpg)

![](images/66a345a20151e175e36e4cd612a672c0ac421e54a3e8d59cd47658094d86b3dd.jpg)

![](images/750245d5eb0cc3031b9ff7088e32c024b7ad71b9173f05efd609da6625c5c7ca.jpg)

![](images/51c8c061ed00a14459fd0c87602aeed499ed6188b7bee06afb8faacf033478b5.jpg)

![](images/67802befbd544ec1cdd14e0d78c7a4bfffdd104f08e95f773f9f423927a0c5d9.jpg)

- 科学计算的发展和工业发展的需求产生了大量的大型商业软件、开源代码

![](images/ca1002624e692595a96e037e9008f5dda9ab8b10e8ef7f08fceab5297bd093fa.jpg)

![](images/8f37065e3a3f799670cf7f4df4fea2d076940f8784dc229e739a94fc093dbaea.jpg)

![](images/d21f483a7ceb4f8e9600d1142efbb7b3d833974e982bbfdb6fcd4002cbc96836.jpg)

![](images/a2199f532a89915f3b86a1132f981e4426d63cf2165c8f750b61e85ad0533857.jpg)

![](images/2324d100242cf43ba0c8e9d36e3d1c7dc9c625f7ec1280edd33f371dc62bfeb0.jpg)

![](images/f838fde40aa5eb96ceb6e68c4491049a48b2c02fa2dca93adc74399f7d33cdb0.jpg)

![](images/017a4849bfe085b7f5e15dc54c6bfd4b180a15c32c08a5828a36062f37e180d6.jpg)

![](images/e10f2e457a6cef6c2c046b0f201c270864ae56cb34041b7e07b31eee6be52a62.jpg)

![](images/2d4722b58990484500063b1c0be19c94287027885112d3eae74e32f2366fe413.jpg)

![](images/09431fc635dc1d6772e454965cb4bf5a85b0a7a30a6df51f4b2f5005bc2739b5.jpg)

![](images/a9ae79636f18f8b73060f731fef52fcaf51df20065e7540f6bd49c45ea0d9381.jpg)

![](images/8f1e9b50e12cfca5973b34c7d54e5d569ca0032055404129afb3bdda5aa525b1.jpg)

- 科学计算的重要成果具有很大的学术和商业价值

- 第一届ICIAM工业奖授予Math Works公司创始人兼首席数学家Cleve Mole：MATLAB (MATrix LABoratory)源于他1960s的博士论文

![](images/4a99de93dd126b47ba64fbd7a6fa5d1010779ff46d9c98885e78b4404ca392da.jpg)

![](images/253dd4aeff2cd172da0c2081a5204a70dee23bd80f6b4edc14e9d6a6d9d18517.jpg)

- 美国当地时间2024年1月16日，全球电子设计自动化软件领军企业Synopsys以350亿美元的巨资收购了全球最大的HPC仿真软件公司Ansys。

- 工业软件的三座大山：计算机辅助设计(CAD)、计算机辅助工程(CAE)、电子设计自动化（EDA）
- 以美国为首的西方国家对中国实施高端芯片和工业软件的禁运

- 国产替代：通用科学计算软件https://www.baltamatica.com/

![](images/2888f138037423b6739ed90c8254624973add45f461d7b47e68c7087825c7b08.jpg)

![](images/c17fb1ced255ca2cdf0d510833223c3f9a6d14bcb83f62b73badf147f79aaad6.jpg)

![](images/3cec4904ab6be31d3c726f8c2b01b821dd9a775603f0f328cd10a24a74ba79a1.jpg)

- 国家数值风洞http://www.cardc.cn/nnw/

![](images/e82e27ed36f840d87b2bac45bc9b3b6d27ab7f359186e53e012a06d60f8ab4b3.jpg)

- 人工智能正在给科学计算带来深刻的变革

![](images/fcc983f39a22e16438035a7599c301e24302321758fe8a4664deae02f06552df.jpg)

![](images/5274c139e0b467a35cb4bb0879d4e732c25adbcdce696a81eca11e5236e6422c.jpg)

Google, Deep Mind

![](images/6083aa8e60cd04a0bce2f1692db645f8f7acb953a5dd37069d1c6344509af840.jpg)

OpenAI, 2022年11月发布GPT

2024年2月发布SORA

2016年3月,AlphaGo 4:1 李世石

![](images/6e043a6e4d83e63883de16fb8a5ce929bf7096c202518356a323d189945a4fe2.jpg)

![](images/2a1c768eb40f80a20b0b880bc4f797f78e178c9b394851f91174b93ed887a8e3.jpg)

![](images/f86f9ef18946256bdaf8acfe34fbfa4800672103c040e9a82ba8c5c982854a24.jpg)

![](images/e99d6693581ef074bedc805a8616bcaf6687ab87001554b08c61fd633d335fcd.jpg)

![](images/e50c23881eb2046563a6a3b9957f382b5b55c5ed907115c2c534fedc045c3987.jpg)

- 未来的科学计算还可能发生变革九章

![](images/d35a9122d0ec50b3e6bfa5622a50f91547170b6f18d4b4e6ac5bfe1d15437feb.jpg)

![](images/ed041db69621e772606a62e4752ae6389fa727b7c3b2b0e656a9e1d7bc58456d.jpg)

![](images/f57dc1afa85d604863ee7ea488859db90a3d1bb0665b196039939adbb366bdbb.jpg)

- 量子计算机

- 光子计算机

![](images/c26ef631d2ac501e5a1df95b9fa8e1548d76c8d7965eb448c68ae5add4b3e67c.jpg)

![](images/d7470a8d9c38187eaef00f3124f7cd29174215724d9fc8eef50dd16ccde0d4eb.jpg)

- 分子计算机

- 纳米计算机

## 科学计算的重要性

- Ever since the time of Newton, there have been two different paradigms for doing scientific research: the **Keplerian paradigm** and the **Newtonian paradigm**.(Weinan E)

**观测数据**

**第一性原理**

**科学计算**

**理论分析**

**数学模型**

**科学计算**

**理论分析**

## 科学计算的重要性

- “实验、理论、计算已成为科学方法上相辅相成的而又相对独立，可以相互补充替代而又彼此不可缺少的三个主要环节”-冯康
- 实际问题的特点：复杂、规模大；实验费用高、耗时长、可观测数据有限；有些问题不能进行实验（如核爆被禁止）
- 计算的天然优势：费用相对较低、可重复性强、不受问题的极端条件限制

## 科学计算的重要性

- 1983年一个由美国著名数学家拉克斯(P. Lax)为首的不同学科的专家委员会向美国政府提出的报告之中，强调“**科学计算是关系到国家安全、经济发展和科技进步的关键性环节，是事关国家命脉的大事**。”
- 1987年起美国NSF把“科学与工程计算”、“生物工程”“全局性科学”作为三大**优先资助**的领域。
- 80年代中期我国将“大规模科学与工程计算”列入国家资助**重大项目**。

## 科学计算的重要性

- Without understanding gained from CFD there would not have been a 737-300 program! (Walt Gillete, Manager 737 Aerodynamics, Vice President, 787 Engineering)

![](images/454a9f969b5a9e1bd5ea69cca3cb0a23443b6ffaef48f6307c050e952920ae1e.png)

CFD在波音787设计中的贡献

## 科学计算的重要性

![](images/2ebc1ce3d20c6d6c4fbe1691da300efe02c760af5baad335baeb27497b7f316c.jpg)

![](images/d64a87cd9bd8fd92735eed12b9fed3ea801cf06f20e00e292a5010febdc95307.jpg)

![](images/5a14848c1ae23c6832eecb99f8f67d49f1121e9a0f508f002f12e7c003c3f7bd.png)

![](images/fbe9fa1079cbccfceaaeda588c9883a8073f671c132b7edfb82b2c5c14d150bc.jpg)

心脏模拟动画特效汽车设计爆炸模拟

![](images/795a7dcf681bc37e963a61018a2ed75a5fc6d8a8ce9400e0e89b55ba208014fe.jpg)

城市设计

![](images/c2316724777e791c92546605056d1553bdb09eec1ecb5cb8929fcd0586c2f81c.jpg)

油藏模拟发动机模拟

## 数值分析的重要性

- As machines become more powerful, the efficiency of algorithms grows more important, not less. （L.N. Trefethen）
    - 误差多大？
    - 收敛？收敛速度？
    - 解是否稳定？
    - 计算效率？
    - 是否能大规模化（充分利用计算设备算力）？

![](images/86bb23fd872db354acd4dbb45f8356b5924e554ea07a66d3ca82897d28636f05.jpg)

![](images/df8dc1f74f2216f1252aebfd915f46d9ffe053011343e512ede8f61d06da2400.jpg)

![](images/19b0dcd2cc9d2ec52a834a740d10c4088ba1d170e5640eafd7901a8f57534090.jpg)

![](images/3b72572b3e0feb53023734ae4a1ddfb4168426df21b233e5f98a67ca39b96740.jpg)

![](images/164b5be0b42d16e2d05ab0558d71c91f8988b7909e6eecf01e7574a860fdf624.jpg)

<table>
  <tr>
    <th></th>
    <th>Training Dataset</th>
    <th>Total Parameters</th>
    <th>GPU number</th>
    <th>Training GPU-hours</th>
  </tr>
  <tr>
    <td>Grok3</td>
    <td>12.8T tokens</td>
    <td>2.7 trillion</td>
    <td>200,000 Nvidia H100</td>
    <td>200  million Nvidia H100</td>
  </tr>
  <tr>
    <td>GPT4</td>
    <td>13T tokens</td>
    <td>1.8 trillion</td>
    <td>25,000 Nvidia A100</td>
    <td>60 million Nvidia A100</td>
  </tr>
  <tr>
    <td>DeepSeek-V3</td>
    <td>14.8T tokens</td>
    <td>671 billion</td>
    <td>2,048 Nvidia H800</td>
    <td>2.8 million Nvidia H800</td>
  </tr>
</table>

![](images/a6e315e6f7e4de13e2ee02f14ce0e8a9f63ad81630f665c0ac2d1c3744b7d923.jpg)

![](images/6a3a0bb4cd8fb64019fb6a29a2af813d6eb833eed253ab7cb289bb88a476131f.png)

![](images/61604ea20c981faa8e3f96cabebe7743f96c72934e53ff0727426e2cedac0566.jpg)

![](images/56620f27ed7d1df445dacb6b1ddeb678b5ed04e9128394d2e8bef0301119a84e.jpg)

![](images/f017185795532bc53bab781d4e19b9dd7611749b3d2c153fc1a0fa66176dad28.jpg)

## 误差定义

- *假设某一数据的准确值为* $x^{*}$ *,其近似值为* $x$
    - *绝对误差：* $e\left(x\right)=x-x^{*}$
    - 相对误差： $er\left(x\right)=\frac{x-x^{*}}{x^{*}}$ , $x^{*}\ne 0$
    - *绝对误差限* $\epsilon$ *：* $\left|e\left(x\right)\right|=\left|x-x^{*}\right|\leq \epsilon$
    - *相对误差限* $\epsilon r$ *：* $\left|er\left(x\right)\right|=\left|\frac{x-x^{*}}{x^{*}}\right|\leq \epsilon r$

## 误差的基本运算

- $e\left(x\pm y\right)=e\left(x\right)\pm e\left(y\right)$ , 相近的数相减相对误差增大
- $e\left(xy\right)=ye\left(x\right)+x^{*}e\left(y\right)$
- $e\left(\frac{x}{y}\right)=\frac{ye\left(x\right)-xe(y)}{yy^{*}}，$ 小数作除数，绝对误差增大

## 误差的来源

- 模型误差：数学、物理模型带来的误差
- 观测误差：实验测量的误差
- 方法误差：求解数学模型时，用简单代替复杂,或者用有限过程代替无限过程所引起的误差（例：以直代曲求圆周率）
- 计算（舍入）误差：四舍五入取近似值（不可避免，计算机表示的数的位数有限）

## 有效数字

- 定义：当 $x$ 的绝对误差限为某一位的半个单位，则这一位到第一个非零位的位数称为 $x$ 的有效位数。
- 例： $n$ 位有效数字的十进制数 $x=0.a1a2\ldots an\times 10m$ 的绝对误差限？
- 例：圆周率 $\pi =3.1415926\ldots$

$3.14$ 有效数字为？

$0.00314\times 10^{3}$ 有效数字为？

3.91415926有效数字为？

## 有效数字

- 例：已知 $\sqrt{30}$ 的十进制浮点数第一位是5，要使近似值的相对误差限小于0.1%，问浮点数的有效数字的位数至少应该为多少？

$\left|e_{r}\left(x\right)\right|<\frac{0.5\times 10^{-\left(n-1\right)}}{5}=10^{-n}\leq 10^{-3}\rightarrow n\geq 3$

## 计算机浮点数表示

- 十进制与二进制的转换

$\left(\ldots b_{2}\times 2^{2}+b_{1}\times 2^{1}+b_{0}+b_{-1}\times 2^{-1}+b_{-2}\times 2^{-2}\ldots \right)_{10}=\left(\ldots b_{2}b_{1}b_{0}.b_{-1}b_{-2}\ldots \right)_{2}$

- 例： $\left(9.4\right)_{10}=\left(?\right)_{2}$

$\left(9.4\right)_{10}=\left(1001.\overbar{0110}\right)_{2}$

- 例： $\left(0.1\right)_{10}=\left(?\right)_{2}$

$\left(0.1\right)_{10}=\left(0.00\overbar{0110}\right)_{2}$

- IEEE754浮点数： $x=\pm 1.b_{1}b_{2}\ldots b_{n}\times 2^{p}$

机器数形式： $se_{1}e_{2}\ldots e_{m}b_{1}b_{2}\ldots b_{n}    s=0:+$

指数偏差: $Bias=2^{m-1}-1, p=\left(e_{1}e_{2}\ldots e_{m}\right)_{2}-Bias$

尾数指数符号

<table>
  <tr>
    <th>精度</th>
    <th>符号位</th>
    <th>指数位</th>
    <th>尾数位</th>
    <th>总占位</th>
    <th>指数偏差</th>
    <th>指数范围</th>
    <th>总范围</th>
  </tr>
  <tr>
    <td>单精度</td>
    <td>1</td>
    <td>8</td>
    <td>23</td>
    <td>32</td>
    <td>127</td>
    <td>[-126,127]</td>
    <td>$-3.4\times 10^{38} ~ 3.4\times 10^{38}$</td>
  </tr>
  <tr>
    <td>双精度</td>
    <td>1</td>
    <td>11</td>
    <td>52</td>
    <td>64</td>
    <td>1023</td>
    <td>[-1022,1023]</td>
    <td>$-1.7\times 10^{308} ~ 1.7\times 10^{308}$</td>
  </tr>
  <tr>
    <td>长双精度</td>
    <td>1</td>
    <td>15</td>
    <td>64</td>
    <td>80</td>
    <td>16383</td>
    <td>[-16382,16383]</td>
    <td>$-1.1\times 10^{4932} ~ 1.1\times 10^{4932}$</td>
  </tr>
</table>

IEEE754不同精度的浮点数

- 例：数字1的双精度机器数形式？

$1=+1.\underbrace{0000000000000000000000000000000000000000000000000000}_{52个0} \times 2^{0}$

<table>
  <tr>
    <th>0</th>
    <th>01111111111</th>
    <th>$0000000000000000000000000000000000000000000000000000$</th>
  </tr>
</table>

## 计算机浮点数表示

- 特殊指数 $\left(00000000000\right)_{2}$ 表示

$\pm 0.b_{1}b_{2}\ldots b_{n}\times 2^{-1022}$

- 例：最小的IEEE754双精度正浮点数？

$2^{-52}\times 2^{-1022}=2^{-1074}\approx 2.02\times 10^{-323}$

- 特殊指数 $\left(11111111111\right)_{2}$

<table>
  <tr>
    <th>0</th>
    <th>00000000000</th>
    <th>$0000000000000000000000000000000000000000000000000001$</th>
  </tr>
</table>

<table>
  <tr>
    <th>+Inf(1/0)</th>
    <th>0</th>
    <th>11111111111</th>
    <th>$0000000000000000000000000000000000000000000000000000$</th>
  </tr>
  <tr>
    <td>-Inf(-1/0)</td>
    <td>1</td>
    <td>11111111111</td>
    <td>$0000000000000000000000000000000000000000000000000000$</td>
  </tr>
  <tr>
    <td>NaN</td>
    <td>1</td>
    <td>11111111111</td>
    <td>非全0</td>
  </tr>
</table>

## 计算机浮点数表示

- 定义：机器精度 $\epsilon _{mach}$ 是1和比1大的最小浮点数之间的距离。 $n$ 位尾数的IEEE754浮点数 $\epsilon _{mach}=2^{-n}$
- 例：IEEE754双精度浮点数的机器精度

$\epsilon _{mach}=2^{-52}\approx 2.22\times 10^{-16}$

- 例：二进制系统 $b_{0}.b_{1}b_{2}\times 2^{p}$  ( $-1\leq p\leq 2$ )的分布

## 计算机浮点数表示

- IEEE舍入的最近法则（双精度）：

1、第53位尾数为0，则在第52位之后截断（舍去）

2、第53位尾数位1，53位之后非全零，则在第52位加1（进位）

3、第53位尾数位1，53位之后全零，依据使第52位等于0选择舍去或者进位

- IEEE舍入法则的绝对误差限和相对误差限为?
- 例：9.4的双精度浮点数的绝对误差及相对误差？

$9.4=\left(1001.\overbar{0110}\right)_{2}$

$=1.\underbrace{001011001100110011001100110011001100110011001100110}_{51位}\overbar{0110}\times 2^{3}$

$fl\left(9.4\right)=1.\overbrace{001011001100110011001100110011001100110011001100110}1\times 2^{3}$

$=9.4-\left(\overbar{0.0110}\right)_{2}\times 2^{-51}\times 2^{3}+2^{-52}\times 2^{3}=9.4+\left(1-0.8\right)\times 2^{-49}$

$e_{r}=\left|\frac{fl\left(9.4\right)-9.4}{9.4}\right|=\frac{0.2\times 2^{-49}}{9.4}=\frac{8}{47}\times 2^{-52}$

## 计算机浮点数表示

- 浮点数加法：对齐小数点位→高精度加法寄存器→舍入回相应精度
- 例：双精度 $1+2^{-53}$

$1.000...000\times 2^{0}+1.000...000\times 2^{-53}$

$=1.000...000  \times 2^{0}$

$+0.000\ldots 0001\times 2^{0}$

$=1.000\ldots 0001\times 2^{0}$

$=1.000\ldots 000\times 2^{0}$

例：双精度 $9.4-9-0.4$

$fl\left(9.4\right)-fl\left(9\right)-fl\left(0.4\right)=0.2\times 2^{-49}-0.1\times 2^{-52}=3\times 2^{-53}$

## 计算机浮点数表示

- 计算机实验（C语言）

![](images/4b7ebaf74589e7ec418cda1b850e5c2be9a8a779cb3cf5ec9c8a3b2fb59afc25.jpg)

![](images/2c435f8e8207ad0b6d2f4c508c71a20c5860bf508dfcab14743304212431c5e3.jpg)

## 数值计算的基本原则

- 避免绝对值小的数做除数例： $6/0.001=6000      6/0.0012=5000$

- 防止大数“吃”小数例：8位浮点数系统： $1.0000000 \times 109+ 0.000000009 \times 109$

- 避免相近的数相减例：方程 $x^{2}-16x+1=0的根x_{1}=8-\sqrt{63}=$ 0.0627460668…

取 $\sqrt{63}\approx 7.937，$  $x_{1}=8-\sqrt{63}=0.063$

$x_{1}=\frac{1}{8+\sqrt{63}}=0.062747$

## 数值计算的基本原则

- 尽量减少计算工作量(乘、除法次数)

多项式计算 $P\left(x\right)=1+2x+3x^{2}$  $+4x^{3}$  $+5x^{4}$

秦九韶（1208－1268年）算法

$P\left(x\right)=1+x(2+x(3$  $+x(4+5x)))$

应用：二进制转十进制、幂级数计算等。

## 数值计算的基本原则

- 计算机实验（C语言）

![](images/1d31ca6fbe85baf0f66d08f32fc885707e89609298c5c3a6ed44fbff7ad66e3e.jpg)

![](images/374b74fab85d4afb5e839eb43269e5976feee2b9c0aa41e9e0ac95feef1d5323.jpg)

## 数值计算的基本原则

- 速度与精度是重要指标
- 割圆术，刘徽，徽率3.1416（3072边形）
- 祖冲之3.1415926\~3.1415927，355/113\~22/7（相当于16000边形的精度，世界领先一千年, 目前的计算已经超过100万亿位）

$\boldsymbol{\mathit{L}}_{\mathbf{2}}$

$\boldsymbol{\mathit{L}}_{\mathbf{1}}$

## 数值计算的基本原则割圆术

n

误差

![](images/8fe4cddec7fea7b54181bc712e86d306763556fbbf92fedb69933832d700bc96.jpg)

外推法

$\hat{\pi }_{2n}=\frac{4\pi _{2n}-\pi _{n}}{3}$

## 数值稳定性

![](images/f9098b732ea89e2f92043eb37975ff8f7c678f2d9ddc5f4d8d1e8677bceb8d1a.jpg)

![](images/a6d5568edca5ff3d1ff0170264f316fbbdf61609a5325205d65d0407d5679042.jpg)

- 计算 $I_{n}=\int_{0}^{1}\frac{x^{n}}{x+5}dx$

$I_{0}=ln\frac{6}{5}$

$I_{n}+5I_{n-1}=\frac{1}{n}$

$I_{n}=\frac{1}{n}$  - $5I_{n-1}$

$e(I_{n})=\left(-5\right)^{n}e\left(I_{0}\right)$

## 数值稳定性

![](images/14778ea1bf090d3322e511851e2b77d75ec1fbf1916461bd47ece30a87fd5c72.jpg)

![](images/2e08f6fb4d13edd6679be9d12f7d6f87c87ab5e1648bd2e1b81700b30f1239a0.jpg)

$I_{n-1}=\frac{1}{5}(\frac{1}{n}$  - $I_{n})$

$\frac{1}{6(n+1)}<I_{n}<\frac{1}{5(n+1)}$

$I_{40}=\frac{1}{5\times 41}$

$e(I_{0})=\left(-\frac{1}{5}\right)^{n}e\left(I_{n}\right)$

## 数值稳定性

$I_{40}=100$

![](images/71482259d7a8b1741a11e6fc709d3b4a60d4c2bb45d559d5da6cdadade31e16e.jpg)

![](images/b9bb0053c88edd854183a186e2289d15699775e0970fd9fc4382778fb38b48c0.jpg)

## 病态问题

- 条件数：输入变化所造成的最大误差放大

$\left\{\begin{matrix}x+ay=1\\ax+y=0\end{matrix}\right.$

$a=0.99    x=50.25$

$a=0.991    x=55.81$

## 思考与练习

- 分析单精度计算 $fl\left(9.4\right)-fl\left(9\right)-fl\left(0.4\right)$ 的结果，并进行计算机实践。
- 设计高效的多项式算法 $P\left(x\right)=1+2x^{3}+3x^{7}$  $+4x^{11}$  $+5x^{15}+6x^{19}+7x^{23}$ , 计算机编程比较直接算法与优化算法的计算时间（采用双精度进行计算， $x=2.2,x=2.222222$ 分别循环 $10^{9}$ 次，循环次数可根据情况适当调整）
- 推导计算 $I_{n}=\int_{0}^{1}x^{n}e^{x}dx$ 的递推公式,用正向和逆向递推计算 $I_{0} \textasciitilde I_{20}$ ，比较并分析两种迭代的误差和稳定性。
- 计算机实践需同时提交源程序和结果分析，无特殊说明结果输出保留12位小数。

## 助教：王子毅

![](images/ea3ba8f33a49630d70adb821c55645aa9ad7d982bc834db43c39e1abdb786ce6.png)

群号：138911823