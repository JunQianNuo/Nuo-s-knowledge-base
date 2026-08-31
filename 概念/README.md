---
title: 概念卡索引
type: 索引
status: 使用中
topics:
  - 概念
---

# 概念卡索引

概念卡用于记录跨章节复用的严格定义、由来与关系网络。结构要求见 [[规范/知识原子卡规范]]。

```dataview
TABLE file.link AS "概念", subject AS "课程", topics AS "主题", source AS "来源"
FROM "概念"
WHERE file.name != this.file.name
SORT subject ASC, file.name ASC
```
