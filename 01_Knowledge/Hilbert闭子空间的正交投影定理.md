---
schema_version: 2
type: proposition
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-泛函分析]]'
source:
- '[[03_Sources/Courses/泛函分析/课堂笔记/2026-11-03-第11节-希尔伯特空间定理授课]]'
---
# Hilbert闭子空间的正交投影定理

## 适用条件与结论

Hilbert空间H的闭线性子空间M对每个x给唯一分解x=P_Mx+z，P_Mx∈M，z∈M⊥。

可由M的正交基系数构造投影，闭性保证级数极限仍在M；交集M∩M⊥={0}给唯一性。

对m∈M，‖x−m‖²=‖z‖²+‖P_Mx−m‖²，故P_Mx是唯一最佳逼近。

非闭集可能不达到下确界；一般Banach范数即使闭线性子空间也未必唯一；闭凸集的最近点结论不能混成线性正交分解。
