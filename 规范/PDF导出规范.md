---
title: Markdown 批量导出 PDF 规范
type: 规范
topics:
  - PDF 导出
  - pandoc
  - Edge headless
  - CSS 样式
---

# Markdown 批量导出 PDF 规范

## 适用场景

将 vault 中的 Markdown 文件（复习资料、知识梳理等）批量导出为带样式的 PDF，效果接近 Obsidian 内置导出。

## 技术方案

选择标准：**优先用 Edge 无头打印**，其次 pandoc+xelatex。

| 方案 | 中文支持 | 样式效果 | 速度 | 结论 |
|------|:---:|:---:|:---:|------|
| pandoc + xelatex | ✅ | ❌ 裸 LaTeX 样式，丑陋 | 慢 | Office 文档场景可用，笔记不用 |
| **pandoc → HTML + Edge 无头** | ✅ | ✅ CSS 完全可控 | 快 | **推荐** |
| pandoc + weasyprint | ✅ | ✅ | 快 | 需安装，备选 |

## 快速使用

直接运行脚本，一行搞定：

```bash
python 规范/export_pdfs.py "课程/某课程/复习"
```

脚本文件：[[规范/export_pdfs.py]]（CSS 已内嵌，无需额外文件）

---

## 完整流程（手动版）

### 第一步：准备 CSS 样式文件

在导出目录创建 CSS 文件，核心要点：

- 使用 Noto Sans SC / Microsoft YaHei 中文字体（Google Fonts `@import` 在本地打印时不会加载，需额外处理）
- `max-width: 780px; margin: 0 auto;` 控制阅读宽度
- h1 底部色条、h2 左侧色条区分层级
- blockquote 模拟 Obsidian callout
- table 斑马纹 + 浅色表头
- `@page { margin: 1.5cm; }` 控制打印边距

> 完整 CSS 模板见本规范末尾"附录：CSS 模板"。

### 第二步：Python 构建脚本

脚本做三件事：
1. **pandoc MD → HTML body**：`pandoc <file>.md -t html --no-highlight`
2. **嵌入 CSS 包装为完整 HTML**：将 CSS 内联写入 `<style>` 标签
3. **Edge 无头打印为 PDF**：`msedge --headless --print-to-pdf=<out>.pdf --no-pdf-header-footer file:///<html>`

```python
import subprocess, os, glob

CSS_FILE = r"<导出入目录>/style.css"
MD_DIR   = r"<导出入目录>"
OUT_DIR  = r"<导出入目录>/pdf_output"
EDGE     = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" /><title>{title}</title>
<style>{css}</style>
</head>
<body>{body}</body>
</html>'''

os.makedirs(OUT_DIR, exist_ok=True)

for md_file in sorted(glob.glob(os.path.join(MD_DIR, "*.md"))):
    base = os.path.splitext(os.path.basename(md_file))[0]
    html_path = os.path.join(OUT_DIR, f"{base}.html")
    pdf_path  = os.path.join(OUT_DIR, f"{base}.pdf")

    print(f"Processing: {base}")

    # Step 1: pandoc MD -> HTML body
    result = subprocess.run(
        ["pandoc", md_file, "-t", "html", "--no-highlight"],
        capture_output=True, text=True, encoding='utf-8'
    )
    body = result.stdout

    # Step 2: embed CSS
    html = HTML_TEMPLATE.format(title=base, css=css, body=body)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Step 3: Edge print to PDF
    abs_html = f"file:///{html_path.replace(chr(92), '/')}"
    subprocess.run(
        [EDGE, "--headless", "--disable-gpu",
         f"--print-to-pdf={pdf_path}",
         "--no-pdf-header-footer", abs_html],
        capture_output=True, timeout=30
    )

    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  -> {base}.pdf ({size_kb:.0f} KB)")

print("\nDone.")
```

### 第三步：清理并打包

```bash
rm pdf_output/*.html           # 删除中间 HTML
zip <课程名>-复习资料.zip pdf_output/*.pdf
```

### 第四步：验证

```bash
ls -lh pdf_output/*.pdf | awk '{print $5, $NF}'
```

抽查 2-3 个 PDF，确认：
- 中文字符无乱码
- 表格边框完整
- 引用块左侧色条可见
- 各级标题层级清晰

---

## 编码注意事项

| 问题 | 原因 | 解决 |
|------|------|------|
| Git Bash 中文文件名乱码 | MinGW 终端使用 GBK | 不影响实际文件，用 `python` 或 `ls` 直接查看 |
| `subprocess` GBK 解码报错 | Edge stderr 含中文路径 | 非致命错误，PDF 正常生成。可加 `encoding='utf-8'` 缓解 |
| 所有 PDF 大小相同 | CSS 未嵌入或 HTML 为空 | 检查 pandoc 输出和模板中的 `{css}` 是否正确替换 |
| 中文字体不显示 | 字体名不匹配或未安装 | 使用系统内置字体（STSong / Microsoft YaHei），或 `@import` 在线字体 |
| Edge 不存在 | 路径不同 | `where msedge` 找不到时尝试 `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |

---

## 与 Obsidian 导出对比

| 维度 | Obsidian 内置 | 本方案 |
|------|:---:|:---:|
| 样式 | 依赖主题 | CSS 完全自定 |
| 批量 | 需逐个手动 | 脚本一键全出 |
| 一致性 | 依赖用户主题设置 | CSS 锁定，版本可追溯 |
| 离线 | 需打开 Obsidian | 纯命令行，CI 可用 |

---

## 反模式

| 反模式 | 正确做法 |
|--------|---------|
| 用 pandoc + xelatex 裸导出笔记类文件 | 用 HTML + Edge 方案 |
| 跳过 CSS 直接用 pandoc 默认样式 | 必须写 CSS，否则等于没导出 |
| CSS 中用 `@import url(Google Fonts)` | 打印时不会加载，用系统字体 |
| 批量脚本不验证输出 | 抽查 2-3 个 PDF 确认格式 |

---

## 附录：CSS 模板

```css
:root {
  --text: #2c3e50;
  --heading: #1a1a2e;
  --accent: #6c5ce7;
  --bg: #ffffff;
  --callout-bg: #f8f9ff;
  --callout-border: #6c5ce7;
  --table-border: #e0e0e0;
  --table-header: #f0f0f5;
  --code-bg: #f5f5f8;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Microsoft YaHei', 'STSong', 'Noto Sans SC', sans-serif;
  font-size: 14px; line-height: 1.8;
  color: var(--text);
  max-width: 780px; margin: 0 auto;
  padding: 40px 30px 60px;
  background: var(--bg);
}

h1 {
  font-size: 2em; color: var(--heading);
  border-bottom: 2px solid var(--accent);
  padding-bottom: 10px; margin: 30px 0 20px;
}

h2 {
  font-size: 1.5em; color: var(--heading);
  margin: 28px 0 14px;
  padding-left: 12px;
  border-left: 4px solid var(--accent);
}

h3 { font-size: 1.2em; color: var(--heading); margin: 22px 0 10px; }
h4 { font-size: 1.05em; color: var(--heading); margin: 18px 0 8px; }
p { margin: 8px 0; }
strong { color: var(--heading); }

blockquote {
  margin: 14px 0; padding: 12px 18px;
  border-left: 4px solid var(--callout-border);
  background: var(--callout-bg);
  border-radius: 0 6px 6px 0;
  color: #4a4a6a;
}

table {
  width: 100%; border-collapse: collapse;
  margin: 14px 0; font-size: 13px;
}

thead th {
  background: var(--table-header); color: var(--heading);
  font-weight: 700; padding: 10px 12px;
  text-align: left; border: 1px solid var(--table-border);
}

tbody td {
  padding: 8px 12px; border: 1px solid var(--table-border);
}

tbody tr:nth-child(even) { background: #fafafa; }

code {
  background: var(--code-bg); padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.9em; color: #e83e8c;
}

pre {
  background: var(--code-bg); padding: 14px 18px;
  border-radius: 6px; overflow-x: auto;
  margin: 12px 0; border: 1px solid #e8e8ee;
}

pre code { background: none; padding: 0; color: var(--text); }
hr { border: none; border-top: 1px solid var(--table-border); margin: 20px 0; }
ul, ol { margin: 8px 0 8px 20px; }
li { margin: 4px 0; }
a { color: var(--accent); text-decoration: none; }

@media print {
  body { padding: 20px 30px; }
  @page { margin: 1.5cm; }
}
```
