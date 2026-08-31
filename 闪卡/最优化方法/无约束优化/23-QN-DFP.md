DFP 公式及其结构？

---

$H_{k+1}^{\text{DFP}}=H_k+\frac{s_k s_k^T}{s_k^T y_k}-\frac{H_k y_k y_k^T H_k}{y_k^T H_k y_k}$

结构: 1) $H_k$ 上一步近似 2) $+\frac{s s^T}{s^T y}$ 正贡献项 3) $-\frac{H_k y y^T H_k}{y^T H_k y}$ 负修正项

秩2校正，近似 Hessian 逆。性质: 正定性遗传。
