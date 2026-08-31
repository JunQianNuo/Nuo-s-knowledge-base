#!/usr/bin/env python3
# LEGACY: 已被 MinerU 替代，保留为备用方案
"""Extract text and math from PPTX slide XML files into markdown."""
import xml.etree.ElementTree as ET
import os
import re
import glob

SLIDES_DIR = "/tmp/pptx_extract/ppt/slides"
OUTPUT_FILE = "/d/知识库/outputs/数值分析01BackgroundAndBasis_source.md"

# Ensure output dir exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

def extract_all_text_from_xml(filepath):
    """Extract all text content from a slide XML file."""
    tree = ET.parse(filepath)
    root = tree.getroot()

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

# Main extraction
all_slides = []

slide_files = sorted(
    glob.glob(os.path.join(SLIDES_DIR, "slide*.xml")),
    key=lambda f: int(re.search(r'slide(\d+)\.xml', f).group(1))
)

print(f"Found {len(slide_files)} slide files")

for sf in slide_files:
    slide_num = int(re.search(r'slide(\d+)', sf).group(1))
    lines = extract_all_text_from_xml(sf)
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
print(f"Total slides: {len(all_slides)}")
