---
title: ROC评估流程
type: 方法
subject: 常用数据分析方法
source:
  - 知识点/源MD/常用数据分析方法-完整版
topics:
  - ROC评估流程
tags:
  - ROC评估流程
method_type: 基础方法
linked_knowledge:
  - 知识点/常用数据分析方法/常用参数与非参数检验
---

# ROC评估流程

## 适用场景

- 二分类模型比较与阈值选择

## 核心公式/步骤

1. 计算不同阈值 TPR/FPR
2. 绘制 ROC 与 AUC
3. 交叉验证
4. 结合代价选阈值
5. 检查校准

## 流程图

```mermaid
flowchart TD
  N0["计算不同阈值 TPR/FPR"]
  N1["绘制 ROC 与 AUC"]
  N0 --> N1
  N2["交叉验证"]
  N1 --> N2
  N3["结合代价选阈值"]
  N2 --> N3
  N4["检查校准"]
  N3 --> N4
```

## 典型例题

> [!example]- 示例
> 筛查常优先灵敏度，再控制假阳性。

## 知识链接

- [[常用参数与非参数检验]]

## 习题链接

- 后续链接到对应课程习题库。
