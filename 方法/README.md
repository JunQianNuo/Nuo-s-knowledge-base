---
title: 方法卡索引
type: 索引
status: 使用中
topics:
  - 方法
---

# 方法卡索引

方法卡用于记录可重复执行的解题或建模流程。结构要求见 [[规范/知识原子卡规范]]。

```dataview
TABLE file.link AS "方法", subject AS "课程", method_type AS "方法类型", topics AS "主题"
FROM "方法"
WHERE file.name != this.file.name
SORT subject ASC, file.name ASC
```
