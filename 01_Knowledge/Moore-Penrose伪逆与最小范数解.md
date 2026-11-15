---
schema_version: 2
type: concept
time: '2026-11-15T09:35:21+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-09-16-第6节-深度学习优化理论讲座]]'
---


# Moore-Penrose伪逆与最小范数解

实矩阵$A\in\mathbb R^{m\times n}$可矩形或秩亏，SVD写为$A=U\Sigma V^{\mathsf T}$，定义$A^+=V\Sigma^+U^{\mathsf T}$；$\Sigma^+$转置矩形对角形状，仅将正奇异值取倒数，零仍为零。它满足$AA^+A=A$、$A^+AA^+=A^+$及$AA^+,A^+A$对称，唯一确定Moore-Penrose伪逆。

$x_*=A^+b$是最小二乘解中欧氏范数最小者；若方程可解即最小范数精确解，若A可逆则回到普通逆。例$A=\operatorname{diag}(2,0)$，$A^+=\operatorname{diag}(1/2,0)$，$b=(4,1)^{\mathsf T}$给$x_*=(2,0)^{\mathsf T}$，残差第二分量仍非零。伪逆不是让不可解系统突然有精确解。

数值实现要给奇异值截断阈值，过小奇异值取倒数会放大误差；阈值会影响数值秩。用于历史梯度矩阵逆平方根时，按正特征值取逆平方根而非直接套$A^+$，见[[01_Knowledge/AdaGrad与RMSProp坐标缩放]]。[NumPy伪逆语义](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html)。SVD定义来自9月16日真实疑惑，具体2×2例为核对定义的补充解释。
