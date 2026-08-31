---
title: 质量审查报告索引
type: 索引
status: 使用中
topics:
  - 质量审查
---

# 质量审查报告索引

## 运行方式

在仓库根目录执行：

```powershell
python scripts/audit_vault.py --root .
```

脚本只读扫描，会在本目录生成日期报告，检查：未解析 Wiki-link、空 Markdown、孤立笔记候选、课程未处理项。

## 处理规则

1. 报告仅列出候选项，不自动修改或删除文件；
2. 链接修复后必须重新运行审查；
3. 课程 OCR、闪卡和原子卡内容审查仍以 [[规范/质量审查规范]] 为准；
4. 批量整理前先确认 Git 状态，并创建可回退的提交或标签。

## 历史报告

```dataview
LIST
FROM "总览/审查报告"
WHERE file.name != this.file.name
SORT file.name DESC
```
