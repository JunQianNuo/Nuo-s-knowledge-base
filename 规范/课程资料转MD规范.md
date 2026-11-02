---
title: 课程资料转 Markdown 规范
type: 规范
topics:
  - PDF 转 MD
  - PPTX 转 MD
  - MinerU
  - OCR
  - xparse
---

# 课程资料转 Markdown 规范

## 适用场景

将 PDF、PPTX、图片等课程资料转换为可编辑、可后续整理的 Markdown。适用于课件导入、课程资料归档、从源文件生成知识梳理、复习资料或习题库之前的初始处理。

## 方案决策

按优先级依次尝试，失败或不可用时降级：

```text
MinerU 云 API（首选，PDF/PPTX，精度最高）
  ↓ 不可用（无网络/无 Token/页数限制）
MinerU 本地 pipeline（备选，CPU 稳定）
  ↓ 不可用或效果差
pdftocairo + Tesseract OCR（兜底，纯 CPU）
  ↓ 图片/Office/HTML 或前述方案都不可用
xparse-cli（最后备用，注意远程 CDN 图片）
```

规范已有方案时直接执行，不问用户“选 A 还是 B”。

## MinerU 云 API（首选）

适合 PDF/PPTX 初始解析，优先保留标题层级、LaTeX 公式、表格和图片。

```bash
python scripts/mineru_cloud.py --input <file.pdf> --output <dir>
```

若处理 PPTX，可使用：

```bash
mineru -p input.pptx -o 课件/MD/ -b hybrid-auto-engine -l ch
```

输出后仍需做“后处理清单”和“验证检查点”。

## MinerU 本地（备选）

本地稳定优先用 CPU pipeline：

```bash
mineru -p <input> -o <output_dir> -b pipeline -l ch
```

`hybrid-auto-engine` 需要 GPU 和较高显存，Windows 环境容易遇到代理、页面文件、显存等问题；除非环境明确可用，否则不要优先走本地 VLM。

## pdftocairo + Tesseract OCR（兜底）

当 MinerU 不可用时使用：

```text
pdftocairo -png -r 300 → Tesseract OCR（chi_sim+eng, --psm 4）→ CJK 后处理 → 人工校对
```

Tesseract 路径：

```text
C:/Program Files/Tesseract-OCR/tesseract.exe
```

CJK 后处理规则：

```python
re.sub(r'(?<=[一-鿿])\s+(?=[一-鿿])', '', text)
```

常见 OCR 修复：`矩防→矩阵`、`刑技大学→科技大学`、`孔→子`。OCR 调参最多 3 次；若 3 次后仍不佳，停止，把图片放到 vault 根目录并请用户协助查看，禁止无限调参。

## xparse-cli（最后备用）

```bash
xparse-cli parse <input.pdf> --output ./out/
```

支持 PDF、图片、Office、HTML。注意：图片可能托管到远程 CDN，离线后失效；只有 MinerU 和 Tesseract 都不适合时才作为兜底。

## PPTX 专项规则

### 优先方案

PPTX 优先用 MinerU 直接解析，得到结构化 Markdown、本地图片和表格。

### OMML 手动兜底

当 MinerU 不可用或输出质量差时，才走手动 OMML 提取：

| OMML | LaTeX | 说明 |
|---|---|---|
| `m:f` | `\frac{num}{den}` | 分式 |
| `m:d` | `\left( ... \right)` | 分隔符，不是分式 |
| `m:func` | `\sin`, `\cos` 等 | 函数 |
| `m:rad` | `\sqrt{}` | 根式 |
| `m:sSub/sSup/sSubSup` | `_{}^{}` | 上下标 |
| `m:nary` | `\sum`, `\int`, `\prod` | 大型运算符 |

关键红线：`m:d` 是 delimiter，不是 fraction；分式只有 `m:f`。混淆会把括号错误转成 `\frac{}{}`。

### 习题图片

PPTX 最后几张“思考与练习/作业”常以图片嵌入。文本提取不到不代表没有内容：

1. 检查最后 5 张幻灯片 XML 中的 `<a:blip>`。
2. 从 `ppt/media/` 提取对应图片到 `未处理项/`。
3. OCR 后人工校对。
4. OCR 失败 3 次即停止求助。

## 输出 frontmatter

源 MD 写入对应课程的 `课件/MD/`、`PPT课件/MD/` 或课程已存在的课件 Markdown 目录。

```yaml
---
raw_title: 文件名（无后缀）
subject: 课程名
source: 源文件名.pdf
status: mineru解析
parser: mineru
topics:
  - 关键词1
  - 关键词2
---
```

OCR 输出可用：

```yaml
---
raw_title: 文件名（无后缀）
subject: 课程名
source: 源文件名.pdf
status: OCR转换（待校对）
topics:
  - 关键词1
  - 关键词2
---
```

## 后处理清单

- 全局转换 Unicode 数学字母（`[\U0001D400-\U0001D7FF]`），不只处理 `$...$` 内。
- 修复 `\c\dots`、`\v\dots`、`\d\dots` 为 `\cdots`、`\vdots`、`\ddots`。
- 长公式行使用 `$$...$$` 包裹，避免裸 `\left...\right`。
- 删除孤儿单字符行（非标题、非公式、非列表标记）。
- 检查 PPTX/PDF 是否含图片型习题。

## 验证检查点

交付源 MD 前至少检查：

```python
re.findall(r'[\U0001D400-\U0001D7FF]', text) == []
'\c\\dots' not in text and '\v\\dots' not in text and '\d\\dots' not in text
text.count('\n## ') > 0
len(text) > 5000  # 对完整章节而言
```

## 反模式

| 反模式 | 正确做法 |
|---|---|
| 跳过 MinerU 直接 OCR | 先按方案决策尝试 MinerU |
| OCR 反复调参超过 3 次 | 停止并请用户协助 |
| 文本提取不到就判断“没有内容” | 检查 PDF 嵌入图片或 PPTX `<a:blip>` |
| 源 MD 质量差直接交付 | 必须完成 Unicode、LaTeX、孤儿行、结构验证 |

## 相关规范

- [[规范/课程笔记生成规范]]
- [[规范/习题库规范]]
- [[规范/Obsidian写作规范]]
- [[规范/质量审查规范]]


## 2026-11-01 课程附件位置修正

课程源资料及其附件作为完整资料包保存：教材/课件转换的 images、assets 等目录保留在源文件原有相对位置，不集中迁入 04_Assets；引用优先保留原有相对路径。04_Assets 仅用于独立或确需共享的附件。
