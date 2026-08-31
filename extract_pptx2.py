#!/usr/bin/env python3
# LEGACY: 已被 MinerU 替代，保留为备用方案
"""Extract text from PPTX by treating it as a zip and parsing slide XML."""
import xml.etree.ElementTree as ET
import zipfile
import os
import re

PPTX_FILE = r"D:\知识库\课程\数值分析\课件\数值分析01BackgroundAndBasis.pptx"
# Try alternative path
if not os.path.exists(PPTX_FILE):
    PPTX_FILE = "/d/知识库/课程/数值分析/课件/数值分析01BackgroundAndBasis.pptx"

OUTPUT_DIR = r"D:\知识库\outputs"
if not os.path.exists(OUTPUT_DIR):
    OUTPUT_DIR = "/d/知识库/outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "数值分析01BackgroundAndBasis_source.md")

def extract_all_text_from_xml(xml_content):
    """Extract all text content from a slide XML string."""
    # Clean up namespace issues - some PPTX files have undeclared namespaces
    # Remove xmlns declarations that might cause parse issues
    root = ET.fromstring(xml_content)

    lines = []

    # Find all text paragraphs
    for p in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
        para_text = []

        for elem in p.iter():
            tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
            if tag == 't' and elem.text:
                text = elem.text.strip()
                if text:
                    para_text.append(text)

        if para_text:
            full = ''.join(para_text)
            if full.strip():
                lines.append(full.strip())

    return lines

print(f"Opening PPTX: {PPTX_FILE}")
print(f"File exists: {os.path.exists(PPTX_FILE)}")

# Read PPTX as zip
all_slides = []
with zipfile.ZipFile(PPTX_FILE, 'r') as zf:
    # Find all slide files
    slide_names = sorted(
        [n for n in zf.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml') and '/slide' in n],
        key=lambda n: int(re.search(r'slide(\d+)\.xml', n).group(1))
    )

    print(f"Found {len(slide_names)} slides in zip")

    for name in slide_names:
        slide_num = int(re.search(r'slide(\d+)', name).group(1))
        xml_content = zf.read(name)
        try:
            lines = extract_all_text_from_xml(xml_content)
        except ET.ParseError as e:
            print(f"  Parse error on {name}: {e}")
            lines = []
        all_slides.append((slide_num, lines))

# Write output
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("# 数值分析 第一章：Background and Basis\n\n")
    f.write("> 源文件：数值分析01BackgroundAndBasis.pptx\n\n")
    f.write("---\n\n")

    for slide_num, lines in all_slides:
        f.write(f"## 第 {slide_num} 页\n\n")
        for line in lines:
            f.write(f"{line}\n\n")
        f.write("\n")

print(f"Written to {OUTPUT_FILE}")
print(f"Total slides processed: {len(all_slides)}")
print(f"Total non-empty slides: {sum(1 for _, lines in all_slides if lines)}")
