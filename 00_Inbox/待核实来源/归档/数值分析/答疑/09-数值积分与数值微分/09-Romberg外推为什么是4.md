---
subject:
- 数值分析
chapter: 9
source_context:
- section: 五、Romberg 积分
  file: 09-数值积分与数值微分-知识梳理.md
  text: $$\frac{I - T_n}{I - T_{2n}} \approx 4 \implies I \approx \frac{4T_{2n} - T_n}{4-1}$$
related_notes:
- '[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理]]'
tags:
- Romberg外推
aliases:
- 第9章 答疑 — Romberg外推为什么是4
time: "2026-08-31T11:44:20+08:00"
legacy_topics:
- Romberg外推
- Richardson外推
- 误差展开
- Euler-Maclaurin公式
source: []
status: not done
legacy_type: review
legacy_schema_version: 2
migration_reason: Missing traceable source in legacy source note
---

# 第9章 答疑 — Romberg外推为什么是 4

---

> 问题：Romberg 外推中 $\frac{I-T_n}{I-T_{2n}}\approx 4$ 的 4 是怎么来的？

> 来源：[[03_Sources/Reviews/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理#五、Romberg 积分（**难点**）|知识梳理 §五]]。

---

### 核心结论

来自误差展开的**主导项是 $O(h^2)$**，步长减半 → $h \to h/2$ → $h^2$ 项缩减到 $1/4$ → 比值 $4/1 = 4$。

---

### 推导

由 Euler-Maclaurin 公式，复化梯形的误差只有偶次幂：

$$I - T_n = c_2 h^2 + c_4 h^4 + c_6 h^6 + \cdots, \quad h = \frac{b-a}{n}$$

步长减半（$n \to 2n$，$h \to h/2$）：

$$I - T_{2n} = c_2\left(\frac{h}{2}\right)^2 + c_4\left(\frac{h}{2}\right)^4 + \cdots = \frac{c_2}{4}h^2 + \frac{c_4}{16}h^4 + \cdots$$

**只保留主导项 $h^2$**（$c_4, c_6$ 等随后被消掉）：

$$\frac{I - T_n}{I - T_{2n}} \approx \frac{c_2 h^2}{c_2 h^2/4} = 4$$

**解出 $I$**：$I - T_n \approx 4(I - T_{2n}) \implies I \approx \frac{4T_{2n} - T_n}{3}$。

---

### 为什么后面是 16、64？

外推一层消掉 $h^2$，得到 $S_n$（$O(h^4)$ 误差）。下一层误差主导项是 $c_4 h^4$，步长减半 → $h^4$ 缩减到 $1/16$ → 比值 $16$：

| 层 | 当前误差阶 | $h$ 指数 | $2^p$ | 外推公式 |
|:---|:---:|:---:|:---:|------|
| $T \to S$ | $O(h^2)$ | $p=2$ | $4$ | $\frac{4T_{2n}-T_n}{3}$ |
| $S \to C$ | $O(h^4)$ | $p=4$ | $16$ | $\frac{16S_{2n}-S_n}{15}$ |
| $C \to R$ | $O(h^6)$ | $p=6$ | $64$ | $\frac{64C_{2n}-C_n}{63}$ |

通式（Richardson 外推）：$I \approx \frac{2^p A(h/2) - A(h)}{2^p-1}$，$p$ 是当前主导误差的 $h$ 指数。

---

## 相关链接

- [[03_Sources/Reviews/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理]]
