#!/usr/bin/env python
"""将概率论PDF转为Markdown：PyMuPDF → 图片 → Tesseract OCR → 后处理 → MD"""
import fitz  # PyMuPDF
import subprocess
import re
import os
import sys
import io

# 强制UTF-8输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

VAULT = r'D:\知识库'
PDF_PATH = os.path.join(VAULT, r'课程\概率论\C1.1 随机事件的直观意义及其运算.pdf')
OUTPUT_MD = os.path.join(VAULT, r'课程\概率论\PPT课件\MD\C1.1-随机事件的直观意义及其运算.md')
TEMP_DIR = os.path.join(VAULT, r'temp_ocr')
TESSERACT = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA = os.path.join(VAULT, r'.tessdata')
DPI = 300

# 后处理函数
def postprocess(text):
    """去除CJK字符间多余空格，修复常见OCR错误"""
    # 去CJK字符间空格
    text = re.sub(r'(?<=[一-鿿])\s+(?=[一-鿿])', '', text)
    # 去中文字符和数字/英文之间的多余空格
    text = re.sub(r'(?<=[一-鿿])\s+(?=[a-zA-Z0-9\(\[])', '', text)
    text = re.sub(r'(?<=[a-zA-Z0-9\)\]])\s+(?=[一-鿿])', '', text)
    # 修复常见错误
    text = text.replace('羹', '»')  # 常见乱码
    # 清理过多的空行
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text

def main():
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_MD), exist_ok=True)

    # 第一步：PDF转PNG
    print(f"Opening PDF: {PDF_PATH}")
    doc = fitz.open(PDF_PATH)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")

    env = os.environ.copy()
    env['TESSDATA_PREFIX'] = TESSDATA

    all_text = []

    for i, page in enumerate(doc):
        if i >= 5:  # TEST: only first 5 pages
            break
        page_num = i + 1
        png_path = os.path.join(TEMP_DIR, f'page_{page_num:02d}.png')

        # 渲染页面为图片
        pix = page.get_pixmap(dpi=DPI)
        pix.save(png_path)

        # OCR
        cmd = [TESSERACT, png_path, 'stdout', '-l', 'chi_sim+eng', '--psm', '6']
        result = subprocess.run(cmd, capture_output=True, env=env,
                                encoding='utf-8', errors='replace')
        text = result.stdout
        if text:
            text = text.strip()
        else:
            text = ""

        if not text or result.returncode != 0:
            print(f"  [Page {page_num}] OCR failed: {result.stderr[:100]}")
            text = f"[Page {page_num} - OCR failed]"

        # 后处理
        text = postprocess(text)
        all_text.append(text)

        # 清理临时图片
        try:
            os.remove(png_path)
        except:
            pass

        print(f"  [Page {page_num}/{total_pages}] OCR done ({len(text)} chars)")

    doc.close()

    # 合并所有文本
    full_text = f"# 1.1 随机事件的直观意义及其运算\n\n---\n\n"
    full_text += "\n\n---\n\n".join(all_text)

    # 写入MD
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(full_text)

    print(f"\nDone! Output: {OUTPUT_MD}")
    print(f"Total characters: {len(full_text)}")

if __name__ == '__main__':
    main()
