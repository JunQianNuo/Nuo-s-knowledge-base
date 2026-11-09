---
schema_version: 2
type: method
time: '2026-11-08T09:12:37+08:00'
topics:
- '[[02_Maps/MOC-数值计算]]'
- '[[02_Maps/MOC-最优化]]'
- '[[02_Maps/MOC-数值分析]]'
source:
- '[[03_Sources/Courses/归档/数值分析/作业/05-对称正定线性方程组/习题5.2]]'
---
# A共轭方向的构造与精确搜索

## 适用场景与操作步骤

对称正定A定义内积$\langle u,v\rangle_A=u^TAv$。

从线性无关种子$v_k$作A内积Gram-Schmidt：$p_k=v_k-\sum_{j<k}\frac{v_k^TAp_j}{p_j^TAp_j}p_j$。

得到非零A共轭方向后，为最小化$\frac12x^TAx-b^Tx$，依次取$r_k=b-Ax_k$、$\alpha_k=r_k^Tp_k/(p_k^TAp_k)$、$x_{k+1}=x_k+\alpha_kp_k$。

新残差与已用方向正交，后续A共轭方向不会破坏既有最优分量；精确算术下n个独立方向至多n步得到$Ax=b$解。

浮点误差会破坏该有限终止性。

[[01_Knowledge/共轭梯度法]]从残差递推生成这些方向，是共轭方向框架的具体算法。

源例A为(2,2；2,6)，取$p_0=(1,0)^T$、$p_1=(-1,1)^T$、$x_0=0$，步长3、1，得到$(3,0)$再到$(2,1)$并满足$Ax=b$。
