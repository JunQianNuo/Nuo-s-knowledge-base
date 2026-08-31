---
title: 闪卡与间隔复习
type: MOC
status: 使用中
topics:
  - 闪卡
  - 复习
---

# 闪卡与间隔复习

## 制卡流程

`课程笔记 / 概念卡 / 方法卡 / 错题 → 一卡一事 → 同步 → Anki 复习 → 回填易错点`

- 基础问答：[[模板/闪卡-基础问答模板|模板]]
- 填空：[[模板/闪卡-填空模板|模板]]
- 同步命令：`python scripts/sync_flashcards.py`
- 制卡与目录规则：[[规范/闪卡规范]]

## 现有牌组统计

```dataview
TABLE length(rows) AS "卡片文件数"
FROM "闪卡"
GROUP BY file.folder AS "牌组路径"
SORT file.folder ASC
```

> [!warning]
> 不在 `闪卡/` 内创建说明笔记或 MOC：同步脚本会将其中的 Markdown 视为卡片。所有管理页统一放在 `总览/`。
