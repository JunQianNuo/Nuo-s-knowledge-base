---
title: 文档转 Markdown 规范
type: 规范
topics:
  - PDF 转 MD
  - PPTX 转 MD
  - MinerU
  - OCR
  - xparse
---

# 文档（PDF、PPTX)转 Markdown 规范

## 适用场景

将 PDF / PPTX / 图片等文档格式转换为可编辑的 Markdown 笔记。适用于课件导入、论文阅读、资料归档等场景。

> **注意**：PPTX 的后续处理（OMML 提取、后处理清单、习题图片处理）见 [[规范/PPTX处理规范]]。本规范聚焦于**选择哪个工具做初始转换**。

## 方案决策

按优先级依次尝试，失败或不可用时降级：

```
首选：MinerU 云 API（免费，精度最高）
  ↓ 不可用（无网络/无Token）
备选：MinerU 本地（需 GPU，精度 95%+）
  ↓ 不可用（无 GPU/Windows 坑多）
备用：pdftocairo + Tesseract OCR（纯 CPU，最后兜底）
  ↓ 图片/Office/HTML 格式
备用：xparse-cli（云解析，图片托管在远程 CDN）
```

## 方案一：MinerU 云 API（推荐）⭐

[MinerU 云服务](https://mineru.net) 提供免费 VLM 解析，2000 页/天，精度最高。

**流程**：上传 PDF → 云端 vlm 模型解析 → 下载 Markdown

```bash
# 使用脚本
python scripts/mineru_cloud.py --input <file.pdf> --output <dir>
```

**优势**：
- 免费，无需本地 GPU
- 使用官方 vlm 模型，LaTeX 公式 + 表格 + 标题全自动
- 支持 200 页/文件，超限自动分批

**限制**：需注册 [mineru.net](https://mineru.net) 获取 API Token，单文件 ≤200 页。

**PPTX 处理**：MinerU 同样支持 PPTX，直接输出结构化 Markdown：

```bash
mineru -p input.pptx -o 课件/MD/ -b hybrid-auto-engine -l ch
```

（PPTX 的详细流程和后处理见 [[规范/PPTX处理规范]]）

## 方案二：MinerU 本地（需 GPU）

[MinerU](https://github.com/opendatalab/MinerU) 本地部署，hybrid-auto-engine 精度 95.39%。

```bash
mineru -p <input> -o <output_dir> -b pipeline -l ch  # CPU，稳定
mineru -p <input> -o <output_dir> -b hybrid-auto-engine -l ch  # GPU，需要 16GB+ 显存
```

**注意**：本地 vlm/hybrid 后端在 Windows 上坑多（代理、httpx、页面文件、显存），优先用云 API。非要用本地就 `pipeline`（CPU）。

详见 [[AI/CLI/文档处理/mineru/README|MinerU CLI 文档]]。

## 方案三：pdftocairo + Tesseract OCR（最后兜底）

当 MinerU 不可用时使用。纯 CPU，无需 GPU。

```
pdftocairo -png -r 300 → Tesseract OCR (chi_sim+eng, --psm 4) → 后处理去空格 → 内容清理重构
```

**环境**：Tesseract 安装在 `C:/Program Files/Tesseract-OCR/tesseract.exe`，中文包需手动下载到 `tessdata/chi_sim.traineddata`。

**后处理规则**：
- 移除 CJK 字符间多余空格：`re.sub(r'(?<=[一-鿿])\s+(?=[一-鿿])', '', text)`
- 修复常见 OCR 错误：`矩防→矩阵`、`刑技大学→科技大学`、`孔→子`

**OCR 调参限制**：如果 OCR 结果始终不佳（≥3 次尝试），立即停止。将图片放到 vault 根目录，告诉用户需要协助查看。**禁止反复调参**。

## 方案四：xparse-cli（云解析）

```bash
xparse-cli parse <input.pdf> --output ./out/
```

支持 PDF/图片/Office/HTML 格式。

**注意**：图片托管在远程 CDN（`web-api.textin.com`），离线即失效。仅在 MinerU 和 Tesseract 均不可用时使用。

## 输出 frontmatter

转换完成后，源 MD 写入对应课程的 `课件/MD/` 目录。

### MinerU 输出

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

### OCR 输出

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

## 验证检查点

每章源 MD 交付前，执行以下检查：

```python
# 1. 数学斜体 Unicode 清零（如有）
re.findall(r'[\U0001D400-\U0001D7FF]', text)  # 必须返回 []

# 2. 损坏 LaTeX 清零
'\c\\dots' not in text and '\v\\dots' not in text and '\d\\dots' not in text

# 3. 至少有一个 ## 节标题
text.count('\n## ') > 0

# 4. 文件大小合理（> 5KB）
```

## 反模式

| 反模式 | 正确做法 |
|--------|---------|
| OCR 反复调参 ≥3 次 | 停止，将图片放 vault 根目录，告诉用户需要协助 |
| 文本提取不到 = 没有内容 | 检查源文件中是否有图片引用（PPTX: `<a:blip>`，PDF: 嵌入图片） |
| 源 MD 质量差就直接交付 | 必须走完整清理流程（Unicode → LaTeX修复 → 孤儿删除 → 验证） |
| 跳过 MinerU 直接用 OCR | 优先尝试 MinerU 云 API，免费且精度远高于 OCR |

## 相关规范

- [[规范/PPTX处理规范]] — PPTX 的 OMML 提取、后处理清单、习题图片处理
- [[规范/PDF导出规范]] — 反向流程：MD → PDF 批量导出
- [[规范/知识点解析梳理规范]] — 源 MD 生成后的进一步加工
