---
title: deep-research
type: Skill
status: 已安装
date: 2026-06-12
---

# deep-research

深度研究引擎，多源搜索 → 交叉验证 → 综合引用报告。

## 完整功能

### 5 阶段流水线

| 阶段 | 内容 |
|------|------|
| **Scope** | 分解问题为 5 个搜索角度 |
| **Search** | 5 个并行 WebSearch agent，每角度一个 |
| **Fetch** | URL 去重，获取 Top 15 源，提取可证伪声明 |
| **Verify** | 每声明 3 票对抗验证（2/3 否决则剔除） |
| **Synthesize** | 合并语义重复，按置信度排序，引用来源 |

### 使用方式

`Workflow({ name: "deep-research" })` 传入研究问题

### 前置条件

问题需足够具体。如果过于宽泛（如"买什么车"缺少预算/用途/地区），先问 2-3 个澄清问题。
