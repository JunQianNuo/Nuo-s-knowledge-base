---
schema_version: 1
title: 收敛性与积分理论
role: moc
topics:
  - "[[概念/Lebesgue积分]]"
source:
  - "[[课程/归档/实变函数/习题库/主题索引-收敛性与积分理论]]"
---

# 收敛性与积分理论

本页是当前关系试点导航，当前动态范围为 Lebesgue 积分主题下的三类原子笔记。
[[课程/归档/实变函数/习题库/主题索引-收敛性与积分理论]] 保留归档时的七大主题习题编排。
主题归属不表示所有可测函数都可积；本页也不表示正文已经完成数学质量复核。

## 人工学习路线

1. [[概念/可测集]] → [[概念/可测函数]]：先理解水平集可测的定义。
2. [[概念/Lebesgue积分]]、[[概念/几乎处处收敛]]：阅读 DCT 的前提语言。
3. [[知识点/Fatou引理]] → [[知识点/Lebesgue控制收敛定理]]：沿现有双向夹逼证明阅读。
4. [[方法/DCT控制函数构造法]]：先验收统一可积上界，再交换积分与极限。
5. 回到[[课程/归档/实变函数/习题库/主题索引-收敛性与积分理论]]的积分极限定理部分选择习题。

## 待复核事项

以下仅登记已发现的问题，原笔记正文尚未修订。

- DCT 定理笔记：“对几乎所有 n”的量词。
- DCT 定理笔记：“控制函数必须有界”的错误表述。
- 控制函数构造法笔记：$x^n e^{-x}$ 的最大值公式问题。

## 动态主题视图

下面按显式版本、类型及 topics 聚合候选；列表不等同于 Validator 验证通过或已经掌握。

```base
filters:
  and:
    - 'file.ext == "md"'
    - 'schema_version == 1'
    - or:
        - 'type == "concept"'
        - 'type == "proposition"'
        - 'type == "method"'
    - or:
        - 'file.inFolder("概念")'
        - 'file.inFolder("知识点")'
        - 'file.inFolder("方法")'
    - 'list(topics).contains(link("概念/Lebesgue积分"))'
    - '!/(^|\/)\./.matches(file.path)'
    - '!/(^|\/)(AGENTS|CLAUDE)\.md$/.matches(file.path)'
    - not:
        - 'file.inFolder("99_System")'
        - 'file.inFolder("docs")'
        - 'file.inFolder("scripts")'
        - 'file.inFolder("模板")'
        - 'file.inFolder("规范")'
        - 'file.inFolder("总览/标签库")'
        - 'file.inFolder("总览/属性库")'
views:
  - type: table
    name: 主题原子笔记
    order:
      - file.name
      - type
      - prerequisites
      - about
      - uses
      - related
```
