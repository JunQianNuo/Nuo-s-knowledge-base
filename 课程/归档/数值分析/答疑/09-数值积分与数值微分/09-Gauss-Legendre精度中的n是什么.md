---
title: 第9章 答疑 — Gauss-Legendre精度中的n是什么
subject: 数值分析
chapter: 9
type: 答疑
topics:
  - Gauss求积
  - Gauss-Legendre
  - 代数精度
  - 节点数vs点数
source_context:
  - section: "六、Gauss 求积"
    file: "09-数值积分与数值微分-知识梳理.md"
    text: "两点 Gauss-Legendre 精度 3=2n+1"
related_notes:
  - "[[课程/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理]]"
tags:
- Gauss求积
- Gauss-Legendre
- 代数精度
---

# 第9章 答疑 — Gauss-Legendre精度中的 n 是什么

---

> 问题：两点 Gauss-Legendre 有 2 个点，$2n+1$ 不是 $2\times2+1=5$ 吗？为什么精度是 3？

> 来源：对话中提出（Q10 自测时对精度的困惑）。

---

### $n$ 是点数减 1

Gauss 求积公式的精度公式是 $2n+1$，其中 **$n+1$ 是节点数**（即用了几个 Gauss 点），$n$ 是"节点数 − 1"。

| 用几个点 ($n+1$) | $n$ | $2n+1$（精度） | 实例 |
|:---:|:---:|:---:|------|
| 1 | 0 | 1 | 中矩形 |
| **2** | **1** | **3** | 两点 Gauss-Legendre |
| 3 | 2 | 5 | 三点 Gauss-Legendre |
| 4 | 3 | 7 | 四点 Gauss-Legendre |

两点 Gauss-Legendre：$n+1=2 \implies n=1$，精度 $2\times1+1 = 3$。

### 为什么 $n$ 从 0 开始？

因为"$n+1$ 个节点的内插求积天然精确到 $n$ 次多项式"，Gauss 把精度翻倍到 $2n+1$。$n$ 是"天然精度"对应的次数。用 $n$（而非点数）命名精度公式更自然：**天然精度 $n$ → Gauss 精度 $2n+1$**。

### 验证

两点 Gauss-Legendre（$x_{0,1}=\pm\sqrt{3}/3$，$A_0=A_1=1$）：
- $f(x)=1,x,x^2,x^3$ → 精确 ✅
- $f(x)=x^4$ → 不精确 ❌
- 精度 = 3（对 $0\sim 3$ 次精确，$4$ 次不精确）。$2\times1+1=3$ ✓，不是 $2\times2+1$。

---

## 相关链接

- [[课程/归档/数值分析/知识点解析梳理/09-数值积分与数值微分-知识梳理]]
