r"""
批量将 Markdown 文件导出为带样式的 PDF。

用法：
    python export_pdfs.py <目录路径> [输出子目录名]

示例：
    python export_pdfs.py "D:/知识库/课程/马克思主义原理/复习"
    python export_pdfs.py "D:/知识库/课程/马克思主义原理/复习" pdf_output

依赖：
    - pandoc（需在 PATH 中）
    - Microsoft Edge（默认在 Program Files (x86)\Microsoft\Edge\Application）
"""

import subprocess, os, glob, sys, shutil

# ============== 配置 ==============
EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# ============== 内嵌 CSS ==============
CSS = r"""
:root {
  --text: #2c3e50;
  --heading: #1a1a2e;
  --accent: #6c5ce7;
  --callout-bg: #f8f9ff;
  --callout-border: #6c5ce7;
  --table-border: #e0e0e0;
  --table-header: #f0f0f5;
  --code-bg: #f5f5f8;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Microsoft YaHei', 'STSong', sans-serif;
  font-size: 14px; line-height: 1.8;
  color: var(--text);
  max-width: 780px; margin: 0 auto;
  padding: 40px 30px 60px;
}

h1 {
  font-size: 2em; color: var(--heading);
  border-bottom: 2px solid var(--accent);
  padding-bottom: 10px; margin: 30px 0 20px;
}

h2 {
  font-size: 1.5em; color: var(--heading);
  margin: 28px 0 14px; padding-left: 12px;
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
  border-radius: 0 6px 6px 0; color: #4a4a6a;
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
  border-radius: 3px; font-family: 'Consolas', monospace;
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
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" /><title>{title}</title>
<style>{css}</style>
</head>
<body>{body}</body>
</html>"""


def find_edge():
    for p in EDGE_PATHS:
        if os.path.exists(p):
            return p
    # fallback: try PATH
    found = shutil.which("msedge") or shutil.which("edge")
    if found:
        return found
    sys.exit("错误：找不到 Edge。请设置 EDGE_PATHS。")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    md_dir = sys.argv[1]
    out_name = sys.argv[2] if len(sys.argv) > 2 else "pdf_output"
    out_dir = os.path.join(md_dir, out_name)
    edge = find_edge()

    if not os.path.isdir(md_dir):
        sys.exit(f"错误：目录不存在: {md_dir}")

    os.makedirs(out_dir, exist_ok=True)
    md_files = sorted(glob.glob(os.path.join(md_dir, "*.md")))

    if not md_files:
        sys.exit(f"错误：目录中没有 .md 文件: {md_dir}")

    print(f"源目录: {md_dir}")
    print(f"输出目录: {out_dir}")
    print(f"Edge: {edge}")
    print(f"待处理: {len(md_files)} 个文件\n")

    for md_file in md_files:
        base = os.path.splitext(os.path.basename(md_file))[0]
        html_path = os.path.join(out_dir, f"{base}.html")
        pdf_path = os.path.join(out_dir, f"{base}.pdf")

        print(f"  {base} ...", end=" ", flush=True)

        # Step 1: pandoc MD -> HTML body
        r = subprocess.run(
            ["pandoc", md_file, "-t", "html", "--no-highlight"],
            capture_output=True, text=True, encoding='utf-8'
        )
        if r.returncode != 0:
            print(f"pandoc 错误: {r.stderr[:100]}")
            continue
        body = r.stdout

        # Step 2: embed CSS
        html = HTML_TEMPLATE.format(title=base, css=CSS, body=body)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

        # Step 3: Edge print to PDF
        abs_html = f"file:///{html_path.replace(chr(92), '/')}"
        subprocess.run(
            [edge, "--headless", "--disable-gpu",
             f"--print-to-pdf={pdf_path}",
             "--no-pdf-header-footer", abs_html],
            capture_output=True, timeout=30
        )

        kb = os.path.getsize(pdf_path) / 1024
        print(f"{kb:.0f} KB")

    # Cleanup
    for h in glob.glob(os.path.join(out_dir, "*.html")):
        os.remove(h)

    print(f"\n完成！{len(md_files)} 个 PDF → {out_dir}")


if __name__ == "__main__":
    main()
