---
title: 知识点卡索引
type: 索引
status: 使用中
topics:
  - 知识点
---

# 知识点卡索引

知识点卡用于记录可单独考查的定理、关键知识与推导。结构要求见 [[规范/知识原子卡规范]]。

```dataview
TABLE file.link AS "知识点", subject AS "课程", topics AS "主题", source AS "来源"
FROM "知识点"
WHERE file.name != this.file.name
SORT subject ASC, file.name ASC
```
