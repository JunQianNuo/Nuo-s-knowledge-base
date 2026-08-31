---
title: MinerU
type: CLI
status: 已安装
source:
  - url: "https://github.com/opendatalab/MinerU"
date: 2026-06-12
---

# MinerU

开源 PDF/PPTX/图片解析工具，将文档转为结构化 Markdown，原生支持 LaTeX 公式、HTML 表格、标题层级检测、109 种语言 OCR。

## 推荐方案：MinerU 云 API ⭐

**优先使用 [mineru.net](https://mineru.net) 云服务**，免费 2000 页/天，官方 vlm 模型精度最高，无需本地 GPU。

```bash
# 使用云 API 脚本（自动分批、上传、下载）
python scripts/mineru_cloud.py --input <file.pdf> --output <dir>
```

流程：注册 → 获取 Token → 脚本上传 → 云端解析 → 下载 Markdown。

详见 [[#云 API 使用指南]]。

## 本地安装

```bash
uv pip install -U "mineru[all]" --system
mineru --version    # 预期 3.0+
```

## 后端选择指南

| 后端 | 说明 | 适用场景 | Windows 兼容 |
|------|------|----------|:--:|
| **mineru.net 云 API** | 官方 vlm 模型，远端处理 | **首选，无需 GPU** | ✅ |
| `pipeline` | 经典管道（OCR + 结构检测） | CPU，稳定可靠 | ✅ |
| `vlm-http-client` | VLM 远程推理（OpenAI 兼容） | 需 OpenAI 兼容 VLM 服务 | ⚠️ 模型格式限制 |
| `hybrid-auto-engine` | VLM + Pipeline 本地 | 需 16GB+ 显存 | ❌ 坑多 |
| `vlm-auto-engine` | VLM 本地推理 | 需 16GB+ 显存 | ❌ 坑多 |

**Windows 已知问题**：
- `hybrid/vlm-auto-engine`：httpx 连不上 localhost（需代理开）、页面文件太小、显存不足
- `vlm-http-client`：只有 MinerU 自家训练的模型输出格式兼容，Kimi/Qwen3 等外部模型返回空
- 批处理后台任务 PATH 丢失（需用完整路径 `C:\Users\...\Scripts\mineru.exe`）
- 中文路径在 cmd/PS 编码不一致（优先用英文路径）

## 核心用法

```bash
# 单个文件（默认 hybrid-auto-engine）
mineru -p input.pdf -o ./output/ -b hybrid-auto-engine -l ch

# 单文件（通用管道，无公式需求）
mineru -p input.pdf -o ./output/ -b pipeline -m ocr -l ch

# 指定语言（中文为主 + 英文混合）
mineru -p input.pdf -o ./output/ -l ch

# 指定页面范围
mineru -p input.pdf -o ./output/ -s 0 -e 10

# 禁用公式/表格解析（加速）
mineru -p input.pdf -o ./output/ -f false -t false

# PPTX 文件（mineru 原生支持 Office 格式）
mineru -p input.pptx -o ./output/ -b hybrid-auto-engine -l ch
```

### 本仓库实际示例

```bash
# 马克思主义原理 PDF
mineru -p "D:/知识库/课程/马克思主义原理/PDF/I-绪论与唯物论.pdf" \
       -o "D:/知识库/课程/马克思主义原理/课件/MD/" \
       -b hybrid-auto-engine -l ch

# 数值分析 PPTX
mineru -p "D:/知识库/课程/数值分析/课件/数值分析01BackgroundAndBasis.pptx" \
       -o "D:/知识库/课程/数值分析/课件/MD/" \
       -b hybrid-auto-engine -l ch
```

## 云 API 使用指南

### 注册获取 Token

1. 访问 [mineru.net](https://mineru.net) 注册
2. API 管理 → Token → 复制

### 脚本使用

```bash
python scripts/mineru_cloud.py --input "文件.pdf" --output "输出目录"
```

脚本自动处理：
- PDF 超 200 页自动分批
- 上传至 mineru.net → vlm 模型解析 → 下载 Markdown
- 多批自动合并为一个 MD

### API 限制

| 项目 | 限制 |
|------|------|
| 免费额度 | 2000 页/天 |
| 单文件 | ≤200 页 / 200MB |
| 模型 | vlm（默认）/ pipeline |
| Token 有效期 | 需定期续期 |

## 输出结构

MinerU 在输出目录中生成以下文件：

```
output/
├── input.md              # 结构化 Markdown（LaTeX 公式 + HTML 表格 + 标题层级）
└── images/               # 提取的图片（本地路径，不依赖外部 CDN）
    ├── image_0001.png
    ├── image_0002.png
    └── ...
```

**与 xparse-cli 的关键区别**：
- 图片存储在**本地**（`images/`），而非远程 CDN — 离线可用、不失效
- 公式输出为**原生 LaTeX**（`$...$` 和 `$$...$$`），而非 Unicode 数学斜体
- 表格输出为 **HTML `<table>`**，格式保留完整

## 与传统工具对比

| 维度 | MinerU | xparse-cli | pdftocairo + Tesseract |
|------|--------|------------|------------------------|
| 公式识别 | ✅ 原生 LaTeX | ✅ LaTeX（CDN 图片） | ❌ 无法识别 |
| 表格识别 | ✅ HTML 表格 | ⚠️ 部分支持 | ❌ 无法识别 |
| 标题层级 | ✅ 自动检测 | ✅ 自动检测 | ❌ 无层级 |
| 图片存储 | ✅ 本地 `images/` | ❌ 远程 CDN（离线失效） | N/A（仅 OCR 文本） |
| 中文 OCR 精度 | ✅ 高（109 语言支持） | ⚠️ 取决于后端 | ⚠️ 一般（chi_sim） |
| 多模态（VLM） | ✅ 支持 | ❌ 不支持 | ❌ 不支持 |
| PPTX 原生支持 | ✅ 直接解析 | ⚠️ 需 xparse-cli | ❌ 不支持 |
| 离线使用 | ✅ 完全离线 | ❌ 需联网 | ✅ 离线 |
| 输出格式 | Markdown | Markdown / JSON | 纯文本 |

## 本仓库的批处理

使用批处理脚本处理课程课件：

```bash
python scripts/mineru_batch.py --course "马克思主义原理"
```

批处理功能：
- 自动发现课程文件夹中的 PDF/PPTX 文件
- 串行处理（避免显存溢出）
- 自动添加 frontmatter（`status: mineru解析`、`parser: mineru`）
- 图片收集到 `_images/` 目录
- 跳过已有 MD 输出的文件

## 关联

- [[规范/课程资料转MD规范]] — PPTX 处理流程（MinerU 为推荐方案）
- [[AI/CLI/文档处理/pdftocairo/README|pdftocairo]] — 备用方案：PDF → PNG
- [[AI/CLI/文档处理/tesseract/README|Tesseract OCR]] — 备用方案：图片 OCR
- [[AI/CLI/文档处理/xparse-cli/README|xparse-cli]] — 备用方案：云文档解析
