DFP vs BFGS 的核心区别？

---

| 维度 | DFP | BFGS |
|------|-----|------|
| 近似对象 | $H_k\approx[\nabla^2 f]^{-1}$ | $B_k\approx\nabla^2 f$ |
| 方向计算 | $d_k=-H_k g_k$ 直接 | 需解 $B_k d_k=-g_k$ |
| 对偶关系 | $H\leftrightarrow B$, $s\leftrightarrow y$ 互换 | |
| 数值表现 | 大规模可能停滞 | 更稳健，首选 |

实践中首选 BFGS（或 L-BFGS 有限内存版）。
