---
schema_version: 2
topics:
- '[[02_Maps/MOC-数学]]'
legacy_topic_links:
- '[[01_Knowledge/Lebesgue积分]]'
source:
- '[[03_Sources/Courses/归档/实变函数/习题库/主题索引-收敛性与积分理论]]'
aliases:
- 收敛性与积分理论
type: moc
time: '2026-10-27T20:44:25+08:00'
tags: []
---

# 收敛性与积分理论

本页按积分与极限问题导航，动态范围为显式归属本 MOC 主题的三类原子笔记；完整入口见 [[99_System/knowledge/legacy_navigation/核心知识工作台]]。
[[03_Sources/Courses/归档/实变函数/习题库/主题索引-收敛性与积分理论]] 保留归档时的七大主题习题编排。
主题归属不表示所有可测函数都可积；本页也不表示正文已经完成数学质量复核。

## 人工学习路线

1. [[01_Knowledge/可测集]] → [[01_Knowledge/可测函数]]：先理解水平集可测的定义。
2. [[01_Knowledge/Lebesgue积分]]、[[01_Knowledge/几乎处处收敛]]：阅读 DCT 的前提语言。
3. [[01_Knowledge/Fatou引理]] → [[01_Knowledge/Lebesgue控制收敛定理]]：沿现有双向夹逼证明阅读。
4. [[01_Knowledge/DCT控制函数构造法]]：先验收统一可积上界，再交换积分与极限。
5. 回到[[03_Sources/Courses/归档/实变函数/习题库/主题索引-收敛性与积分理论]]的积分极限定理部分选择习题。

## 待复核事项

以下仅登记已发现的问题，原笔记正文尚未修订。

- DCT 定理笔记：“对几乎所有 n”的量词。
- DCT 定理笔记：“控制函数必须有界”的错误表述。
- 控制函数构造法笔记：$x^n e^{-x}$ 的最大值公式问题。

## 函数空间与积分变换

沿 [[01_Knowledge/L^p空间]] → [[01_Knowledge/Riesz-Fisher定理]]、[[01_Knowledge/对偶性定理]] 阅读函数空间，再比较 [[01_Knowledge/卷积]]、[[01_Knowledge/Fourier变换]] 与 [[01_Knowledge/Fourier变换与Plancherel积分计算法]]。集合及空间语言见 [[02_Maps/MOC-集合与空间]]；这里的路线不把积分收敛定理的假设扩展到所有变换问题。

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
    - 'list(topics).contains(link("总览/收敛性与积分理论-MOC"))'
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

<!-- v2-generated:start -->
## 主题知识

动态汇集自身及全部下层主题的原子知识，每篇笔记显示一次。新增原子自动出现；主题层级变化后运行 views 更新递归范围。

![[99_System/knowledge/v2/generated/topics/9b56f4ff16ea.base]]
<!-- v2-generated:end -->
