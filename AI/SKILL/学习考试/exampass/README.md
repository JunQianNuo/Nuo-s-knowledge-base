---
title: exampass
type: Skill
status: 已安装
date: 2026-06-12
---

# exampass

课程期末复习引擎：课件 → 知识清单 + 交互式章节测试。

## 完整功能

### 执行流程

**第一步：提取（~30s）**
```bash
python scripts/run_exampass.py <目标目录>
```
扫描目录，提取 PPTX/DOCX/PDF/MD 的文字、表格、图片

**第二步：确认模式**

| 模式 | 风格 | 适用 |
|------|------|------|
| **考试** | 只列干货知识点（`.kp` 为主），公式+结论+考点标签，删掉推导 | 临考突击 |
| **平衡** | 知识点 + 配套解释（`.kp` + `.exp` 双色），回答是什么/为什么/怎么用 | 常规复习（默认） |
| **深度学习** | 直觉类比+动机推演+数学推导+横向对比+易错辨析 | 想真正学懂 |

**第三步：Claude 深度分析**，读取提取包按所选模式生成 HTML
**第四步**：浏览器打开 HTML，Ctrl+P 打印为 PDF

### 图片识别

- 多模态模型（Claude）：直读图片融入知识清单
- 非多模态模型：优先 MinerU → PaddleOCR/Tesseract 兜底

### 内容质量核心

**根本原则**：PPT 信息碎片化→重构因果链叙事，「因为遇到什么问题→所以提出什么方法→核心思想→具体怎么做→局限→怎么改进」

**重要程度标签**（四色 CSS）：必考(`tag-must`)、重点(`tag-key`)、高频(`tag-freq`)、了解(`tag-info`)

**双色标注**：`<span class="kp">` 核心知识点（黑色加粗扫读锚点）、`<span class="exp">` 解释说明（浅灰色细体辅助阅读）

**易错点**：blockquote 格式单独标出

### 交互式测试

| 题型 | type | 批改 |
|------|------|------|
| 单选 | `choice` | 自动 |
| 多选 | `multi` | 自动（少选部分分） |
| 判断 | `tf` | 自动 |
| 填空 | `fill` | 自动（`____` 标记空位） |
| 简答 | `short` | 显示参考答案 |
| 计算题 | `calc` | 显示参考答案+步骤+评分要点 |
| 代码题 | `code` | 等宽深色输入框+参考代码 |
| 问答 | `essay` | 显示参考答案 |
| 综合题 | `comprehensive` | 跨概念串联 |

### 题型按学科自动选择

| 学科 | 主力题型 | 禁出题型 |
|------|---------|---------|
| 数学/物理/工程 | choice+fill+**calc**+comprehensive | code（除非含编程） |
| 计算机/编程 | choice+multi+**code**+calc+short | — |
| 文科/历史/政治 | choice+tf+fill+short+**essay**+comprehensive | calc、code |
| 外语 | choice+fill+short+essay | calc、code |
| 生物/化学/医学 | choice+multi+fill+short+少量calc+essay | code（除生信） |

### 技能更新

`/exampass update` → PowerShell 脚本自动 git pull + pip install
