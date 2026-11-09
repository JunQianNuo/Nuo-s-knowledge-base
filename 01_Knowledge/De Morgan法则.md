---
schema_version: 2
type: proposition
time: '2026-11-08T09:15:41+08:00'
topics:
- '[[02_Maps/MOC-实变函数]]'
- '[[02_Maps/MOC-集合与空间]]'
source:
- '[[03_Sources/Courses/归档/实变函数/作业/01-集合论与点集拓扑基础/习题1.14-证明De Morgan法则-习题]]'
---
# De Morgan法则

## 适用条件与结论

在固定全集 $X$ 内，对任意指标族（不限可数）有

$$
\left(\bigcup_{\lambda\in I}A_\lambda\right)^c=\bigcap_{\lambda\in I}A_\lambda^c,\qquad
\left(\bigcap_{\lambda\in I}A_\lambda\right)^c=\bigcup_{\lambda\in I}A_\lambda^c.
$$

## 依据与推导

证明只需逐点翻译：“不属于并”就是“对所有指标都不属于”；“不属于交”就是“存在指标使不属于”。

这也证明双集合版本。

补运算将存在量词与全称量词、并与交互换；[[01_Knowledge/σ代数]] 的可数交封闭性由可数并封闭性和此律推出。
