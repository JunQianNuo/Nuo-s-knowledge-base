# MinerU 转 Markdown 工具

Windows 桌面小工具：拖拽文件/文件夹，一键把 PDF、PPTX、图片等转换成 Markdown。

## 功能

- 支持拖拽文件或文件夹到窗口
- 支持“选择文件夹”递归添加文件
- 每个源文件输出到一个独立文件夹：

```text
输出目录/
└── 文件名/
    ├── 文件名.md
    └── images/        # 如果有图片
```

- 转换方式：
  - 自动：优先 MinerU 云 API
  - MinerU 云 API
  - MinerU 本地 pipeline
  - OCR 兜底（pdftocairo + Tesseract）
- 设置界面可调整：
  - MinerU 云 API Token / URL / 模型版本
  - 本地 mineru 命令 / 后端 / 语言
  - Tesseract 路径
  - 默认输出目录
- 自动添加 frontmatter
- 转换后自动清理：
  - CJK 多余空格
  - Unicode 数学斜体
  - 损坏 LaTeX（`\c\dots` 等）

## 安装运行

```bash
cd /d D:\知识库\MinerU-MD工具
pip install -r requirements.txt
python app.py
```

或者直接双击 `run.bat`，首次运行会自动安装依赖。

## 配置

编辑 `config.json`：

| 字段 | 说明 |
|---|---|
| `mineru_api_token` | MinerU 云 API Token |
| `mineru_api_url` | 云 API 地址 |
| `mineru_model_version` | 云 API 模型版本，默认 `vlm` |
| `mineru_command` | 本地 mineru 命令 |
| `mineru_backend` | 本地后端，默认 `pipeline` |
| `mineru_lang` | 语言，默认 `ch` |
| `tesseract_path` | Tesseract 路径 |
| `default_output_dir` | 默认输出目录 |

## 打包成 exe（可选）

安装 PyInstaller 后：

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --name "MinerU转MD工具" app.py
```

打包后的 exe 在 `dist/MinerU_MD_Tool/` 下，文件名为 `MinerU_MD_Tool.exe`。
