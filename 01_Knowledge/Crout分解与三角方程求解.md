---
schema_version: 2
type: method
time: '2026-11-08T09:12:37+08:00'
topics:
- '[[02_Maps/MOC-数值计算]]'
- '[[02_Maps/MOC-数值分析]]'
source:
- '[[03_Sources/Courses/归档/数值分析/作业/03-线性方程组的直接解法/习题3.3]]'
---
# Crout分解与三角方程求解

Crout归一化固定$U$为单位上三角，$L$对角一般不为1。在无主元且所用$l_{kk}\ne0$时，每个$k$先算L的第k列再算U的第k行：

$$l_{ik}=a_{ik}-\sum_{s<k}l_{is}u_{sk}\quad(i\ge k),$$
$$u_{kj}=\frac{a_{kj}-\sum_{s<k}l_{ks}u_{sj}}{l_{kk}}\quad(j>k),\qquad u_{kk}=1.$$

分解后先$Ly=b$，再$Ux=y$；用$LU=A$和$Ax=b$双检验。源例得到$L=\left(\begin{smallmatrix}4&0&0\\2&4&0\\0&3&15/4\end{smallmatrix}\right)$、$U=\left(\begin{smallmatrix}1&1/2&0\\0&1&3/4\\0&0&1\end{smallmatrix}\right)$，前代$y=(2,11/4,1)^T$，回代$x=(1,2,1)^T$。与[[01_Knowledge/LU分解(Doolittle)]]是同一消元思想的不同对角归一化，不可混用中间系数。