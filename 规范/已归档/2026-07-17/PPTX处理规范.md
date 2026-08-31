---
title: PPTX处理规范
type: 规范
---

# PPTX 课件处理规范

## 适用场景

用户上传 `.pptx` 课件后，需要将其转换为可阅读的 Markdown 笔记、生成知识梳理、或提取习题。

## 推荐方案：MinerU（优先使用）

**[MinerU](https://github.com/opendatalab/MinerU)** 原生支持 PPTX 解析，直接将 `.pptx` 转为结构化 Markdown，包含 LaTeX 公式、HTML 表格、本地图片和自动标题层级。

```bash
mineru -p input.pptx -o 课件/MD/ -b hybrid-auto-engine -l ch
```

**优势**：
- 公式输出为原生 LaTeX，无需手动 OMML 映射
- 图片提取为本地文件（`images/`），不依赖外部 CDN
- 自动检测标题层级（`#`, `##`, `###`）
- 表格保留为 HTML `<table>`，格式完整

**输出 frontmatter**：

```yaml
---
raw_title: 数值分析01BackgroundAndBasis
subject: 数值分析
source: 数值分析01BackgroundAndBasis.pptx
status: mineru解析
parser: mineru
topics:
  - 关键词1
  - 关键词2
---
```

## 备选方案：手动 OMML 提取（MinerU 不可用时）

以下为原有的手动管道，仅在 MinerU 不可用时使用。

### 整体流程

```
PPTX 上传 → OMML 提取公式(+文本) → Unicode 清理 → 源 MD 写入课件/MD/ →
按知识点解析梳理规范生成知识梳理 → 按习题库规范生成习题
```

### 第一阶段：PPTX → 源 MD（手动管道）

### 1.1 OMML 公式提取

PPTX 中的数学公式以 OMML（Office Math Markup Language）格式存储在 `a14:m > m:oMath` 标签中。直接按以下映射转换为 LaTeX：

| OMML | LaTeX | 说明 |
|------|-------|------|
| `m:f` | `\frac{num}{den}` | 分式 |
| `m:d` | 分隔符 `\left( \right)` | **不是分式！是括号** |
| `m:func` | 函数如 `\sin`, `\cos` | |
| `m:rad` | `\sqrt{}` | 根式 |
| `m:sSub/sSup/sSubSup` | 上下标 `_{}^{}` | |
| `m:nary` | `\sum\int\prod` | 大型运算符 |
| `m:groupChr` | `\overbrace{}` / `\underbrace{}` | |
| `m:acc` | `\tilde{}` / `\hat{}` 等 | 重音符号 |

**关键易错点**：
- `m:d` 是分隔符（有 `m:begChr`、`m:endChr`），**不是**分式。分式是 `m:f`（有 `m:num`、`m:den`）。混淆会导致所有括号变成 `\frac{}{}`。
- Unicode 数学斜体字符（如 `𝑥` `𝑓` `𝑔`）需**全局**转换为 ASCII，不要仅在 `$...$` 内转换——裸数学行也存在。

### 1.2 后处理清单

生成源 MD 后，**必须逐项验证**以下清理是否完成：

| 检查项 | 正则/方法 | 目标 |
|--------|-----------|------|
| 数学斜体 Unicode | `[\U0001D400-\U0001D7FF]` 全局 `str.translate` | 全部清零 |
| `\c\dots` 残留 | 全局 `replace` → `\cdots` | 全部清零 |
| `\v\dots` / `\d\dots` 残留 | 全局 `replace` → `\vdots` / `\ddots` | 全部清零 |
| 裸 `\left...\right`（无 `$` 或无 `$$`） | 检测长公式行 → 包裹 `$$` | 显示公式正确 |
| 孤儿单字符行 | 行长度 ≤2 且非 `$`/`#` 开头 | 删除 |
| 习题图片未提取 | 检查最后几张幻灯片是否有 `<a:blip>` 引用 | 提取图片备用 |

### 1.3 习题图片处理

PPTX 最后几张幻灯片（通常是"思考与练习"/"作业"）的习题可能以**图片形式**嵌入（`ppt/media/image*.png`），文本提取不到，不是真的没有习题。

**流程**：
1. 检查最后 5 张幻灯片的 XML，找 `<a:blip>` 引用
2. 从 PPTX (zip) 中提取对应 `ppt/media/image*.png` 到 `未处理项/`
3. OCR 处理：`tesseract image.png output -l chi_sim+eng --psm 4`
4. 后处理：移除 CJK 字符间多余空格，修复常见 OCR 错误
5. OCR 结果不理想时：① 放大图片 2x 重试 ② 换 `--psm 6` ③ 若仍差，将图片存至 vault 根目录请用户协助查看

**重要**：如果 OCR 结果始终不佳，**不要反复尝试不同参数**。将图片放到 vault 根目录，直接告诉用户"这几张习题是图片，OCR 效果不好，请帮我看看内容"。

### 1.4 源 MD 存放位置

源 MD 写入 `课件/MD/XX-章节名.md`，frontmatter 格式：

```yaml
---
raw_title: 数值分析01BackgroundAndBasis
subject: 数值分析
source: 数值分析01BackgroundAndBasis.pptx
status: PPTX转换（待校对）
topics:
  - 关键词1
  - 关键词2
---
```

## 第二阶段：源 MD → 知识梳理 / 习题

从源 MD 生成知识梳理或习题时，**必须先读对应的规范文件**：
- 知识梳理 → `[[规范/知识点解析梳理规范]]`
- 习题 → `[[规范/习题库规范]]`

## 反模式（禁止行为）

| 反模式 | 正确做法 |
|--------|---------|
| 跳过规范直接生成 | 动手前先 `Read 规范/xxx规范.md` |
| 脚本跑出来"差不多"就交付 | 逐章抽检：打开文件看前50行、搜 `\c\dots` 和 Unicode 数学斜体 |
| 文本提取不到 = 没内容 | 检查 XML 中是否有图片引用（`<a:blip>`） |
| OCR 反复调参（3次以上） | 停下来，把图片放 vault 根目录求援 |
| 遇到选项问用户"选A还是B"（规范已有方案时） | 按规范直接执行 |
| 源 MD 质量差就直接交付 | 必须走清理流程（Unicode → LaTeX修复 → 孤儿删除） |

## 验证检查点

每一章源 MD 交付前，执行以下检查：

```python
# 1. 数学斜体 Unicode 清零
re.findall(r'[\U0001D400-\U0001D7FF]', text)  # 必须返回 []

# 2. 损坏 LaTeX 清零
'\c\\dots' not in text and '\v\\dots' not in text and '\d\\dots' not in text

# 3. 至少有一个 ## 节标题
text.count('\n## ') > 0

# 4. 文件大小合理（> 5KB）
```
