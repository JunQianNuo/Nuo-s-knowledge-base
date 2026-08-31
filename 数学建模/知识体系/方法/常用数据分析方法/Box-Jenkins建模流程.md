---
title: Box-Jenkins建模流程
type: 方法
subject: 常用数据分析方法
source:
  - 知识点/源MD/常用数据分析方法-完整版
topics:
  - Box-Jenkins建模流程
tags:
  - Box-Jenkins建模流程
method_type: 基础方法
linked_knowledge:
  - 知识点/常用数据分析方法/ARMA与ARIMA模型
---

# Box-Jenkins建模流程

## 适用场景

- 单变量时间序列预测

## 核心公式/步骤

1. 判断平稳性
2. 变换或差分
3. ACF/PACF 与 AIC/BIC 定阶
4. 估计
5. 白噪声诊断
6. 滚动预测

## 流程图

```mermaid
flowchart TD
  N0["判断平稳性"]
  N1["变换或差分"]
  N0 --> N1
  N2["ACF/PACF 与 AIC/BIC 定阶"]
  N1 --> N2
  N3["估计"]
  N2 --> N3
  N4["白噪声诊断"]
  N3 --> N4
  N5["滚动预测"]
  N4 --> N5
```

## 典型例题

> [!example]- 示例
> 残差仍显著自相关时必须重新定阶。

## 知识链接

- [[ARMA与ARIMA模型]]

## 习题链接

- 后续链接到对应课程习题库。
