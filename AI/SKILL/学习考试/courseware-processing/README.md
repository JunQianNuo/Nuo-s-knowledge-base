---
title: courseware-processing
type: Skill
status: 新增
date: 2026-06-15
topics:
  - 课程资料处理
  - PDF 转 MD
  - PPTX 转 MD
  - OCR
  - MinerU
---

# courseware-processing

课程资料处理 skill。用于处理 PDF、PPTX、图片、网页等课程资料，将其转换为可编辑、可后续梳理的 Markdown。

## 完整功能

### 1. 适用场景

- PDF / PPTX / 图片 / 网页资料转 Markdown
- OCR 结果清洗与校对
- MinerU / xparse / Tesseract 方案选择
- 输出课程资料的初始 Markdown 版本
- 为后续知识组织、复习计划、闪卡制作准备材料

### 2. 方案选择

按优先级依次尝试：

1. **MinerU 云 API**：首选，适合 PDF / PPTX，公式、表格、标题识别较好
2. **MinerU 本地**：适合有本地环境或 GPU 的场景
3. **pdftocairo + Tesseract OCR**：纯 CPU 兜底方案
4. **xparse-cli**：支持 PDF / 图片 / Office / HTML，但依赖远程 CDN

详见：

- [[规范/课程资料转MD规范]]
- [[规范/课程资料转MD规范]]
- [[AI/CLI/文档处理/mineru/README]]

### 3. 标准流程

```text
确认源文件 → 判断格式 → 选择转换工具 → 生成 Markdown → 基础清洗 → 标注待校对问题 → 交给知识组织 skill
```

### 4. 输出模板

```markdown
## 资料处理结果

- 源文件：...
- 资料类型：PDF / PPTX / 图片 / 网页 / Office
- 处理方式：MinerU / OCR / xparse / 手工校对
- 输出目录：...
- 状态：待校对 / 已清洗 / 需人工确认

## 待处理问题

- ...
```

### 5. 质量检查清单

- 是否明确源文件和输出位置
- 是否说明处理方式
- 是否标注待校对问题
- 是否避免把 OCR 结果当作最终知识梳理
- 是否保留后续知识组织所需的章节结构
- 是否把 PDF/PPTX 转 Markdown 与后续知识点梳理区分开

## 不处理范围

- 不做知识图谱
- 不制定复习计划
- 不生成闪卡
- 不做考试策略
- 不替代 `knowledge-structuring` 做深度知识组织

## 关联

- [[AI/SKILL/学习考试/course-learning]]
- [[AI/SKILL/学习考试/knowledge-structuring]]
- [[规范/课程资料转MD规范]]
- [[规范/课程资料转MD规范]]
