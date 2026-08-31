#!/usr/bin/env python3
# LEGACY: 已被 MinerU 替代，保留为备用方案
"""PPTX → 源MD 转换脚本
按照 PPTX处理规范.md 执行：解包PPTX → 提取文本+OMML→LaTeX → 后处理清理
"""

import zipfile
import re
import os
import sys
from collections import defaultdict

# ============================================================
# Unicode 数学斜体 → ASCII 映射表
# ============================================================
MATH_ITALIC_MAP = {
    # Latin lowercase
    0x1D44E: 'a', 0x1D44F: 'b', 0x1D450: 'c', 0x1D451: 'd', 0x1D452: 'e',
    0x1D453: 'f', 0x1D454: 'g', 0x210E: 'h', 0x1D455: 'h',  # Planck constant alt
    0x1D456: 'i', 0x1D457: 'j', 0x1D458: 'k', 0x1D459: 'l', 0x1D45A: 'm',
    0x1D45B: 'n', 0x1D45C: 'o', 0x1D45D: 'p', 0x1D45E: 'q', 0x1D45F: 'r',
    0x1D460: 's', 0x1D461: 't', 0x1D462: 'u', 0x1D463: 'v', 0x1D464: 'w',
    0x1D465: 'x', 0x1D466: 'y', 0x1D467: 'z',
    # Latin uppercase
    0x1D434: 'A', 0x1D435: 'B', 0x1D436: 'C', 0x1D437: 'D', 0x1D438: 'E',
    0x1D439: 'F', 0x1D43A: 'G', 0x1D43B: 'H', 0x1D43C: 'I', 0x1D43D: 'J',
    0x1D43E: 'K', 0x1D43F: 'L', 0x1D440: 'M', 0x1D441: 'N', 0x1D442: 'O',
    0x1D443: 'P', 0x1D444: 'Q', 0x1D445: 'R', 0x1D446: 'S', 0x1D447: 'T',
    0x1D448: 'U', 0x1D449: 'V', 0x1D44A: 'W', 0x1D44B: 'X', 0x1D44C: 'Y',
    0x1D44D: 'Z',
    # Additional math italic/bold/script codepoints beyond basic italic
    0x1D456: 'i',
}

def build_translation_table():
    """构建 Unicode 数学斜体 → ASCII 翻译表"""
    table = {}
    for cp in range(0x1D400, 0x1D800):
        ch = chr(cp)
        if cp in MATH_ITALIC_MAP:
            table[cp] = MATH_ITALIC_MAP[cp]
        elif 0x1D44E <= cp <= 0x1D467:  # lowercase a-z italic
            offset = cp - 0x1D44E
            table[cp] = chr(ord('a') + offset)
        elif 0x1D434 <= cp <= 0x1D44D:  # uppercase A-Z italic
            offset = cp - 0x1D434
            table[cp] = chr(ord('A') + offset)
        elif 0x1D482 <= cp <= 0x1D49B:  # bold italic lowercase
            offset = cp - 0x1D482
            table[cp] = chr(ord('a') + offset)
        elif 0x1D468 <= cp <= 0x1D481:  # bold italic uppercase
            offset = cp - 0x1D468
            table[cp] = chr(ord('A') + offset)
    return str.maketrans({cp: table[cp] for cp in table})

# Greek math italic to regular Greek
GREEK_MATH_ITALIC = {
    0x1D6FC: 'α', 0x1D6FD: 'β', 0x1D6FE: 'γ', 0x1D6FF: 'δ',
    0x1D700: 'ε', 0x1D701: 'ζ', 0x1D702: 'η', 0x1D703: 'θ',
    0x1D704: 'ι', 0x1D705: 'κ', 0x1D706: 'λ', 0x1D707: 'μ',
    0x1D708: 'ν', 0x1D709: 'ξ', 0x1D70B: 'π', 0x1D70C: 'ρ',
    0x1D70D: 'σ', 0x1D70E: 'ς', 0x1D70F: 'τ', 0x1D710: 'υ',
    0x1D711: 'φ', 0x1D712: 'χ', 0x1D713: 'ψ', 0x1D714: 'ω',
    0x1D71B: 'Δ', 0x1D71C: 'Θ', 0x1D71D: 'Λ', 0x1D71E: 'Ξ',
    0x1D71F: 'Π', 0x1D720: 'Σ', 0x1D721: 'Υ', 0x1D722: 'Φ',
    0x1D723: 'Ψ', 0x1D724: 'Ω',
}


def fix_math_unicode(text):
    """全局清理数学斜体 Unicode 字符"""
    translation = build_translation_table()
    # Also add Greek math italic
    for cp, ch in GREEK_MATH_ITALIC.items():
        translation[cp] = ch

    # Build full table
    full_table = {cp: ch for cp, ch in translation.items()}
    # Escape codes for other math Unicode
    for cp in range(0x1D400, 0x1D7FF + 1):
        if cp not in full_table:
            full_table[cp] = None  # will be removed

    result = []
    for ch in text:
        cp = ord(ch)
        if 0x1D400 <= cp <= 0x1D7FF:
            replacement = full_table.get(cp)
            if replacement:
                result.append(replacement)
            # else skip (math symbols that have no mapping)
        else:
            result.append(ch)
    return ''.join(result)


# ============================================================
# OMML → LaTeX 转换
# ============================================================
def omml_to_latex(omml_xml):
    """将 OMML XML 字符串转换为 LaTeX"""
    try:
        import xml.etree.ElementTree as ET
    except:
        return "$???$"

    # Register namespaces
    ns = {
        'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    }

    try:
        root = ET.fromstring(omml_xml)
    except:
        return "$???$"

    # Find the oMath element (could be root or child)
    omath = root if root.tag.endswith('oMath') else root.find('.//m:oMath', ns)
    if omath is None:
        omath = root

    result = parse_omml_element(omath, ns)

    # Clean the result
    result = result.strip()
    if not result:
        return ""

    # Determine inline vs display
    if len(result) > 40 or '\\frac' in result or '\\sum' in result or '\\int' in result or '\\prod' in result:
        return f"$$\n{result}\n$$"
    else:
        return f"${result}$"


def parse_omml_element(elem, ns):
    """递归解析 OMML 元素"""
    tag = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag

    # Text run
    if tag == 'r':
        return extract_omml_text(elem, ns)

    # Fraction
    elif tag == 'f':
        num = elem.find('m:num', ns)
        den = elem.find('m:den', ns)
        num_text = parse_omml_children(num, ns) if num is not None else ''
        den_text = parse_omml_children(den, ns) if den is not None else ''
        return f'\\frac{{{num_text}}}{{{den_text}}}'

    # Delimiters (parentheses, brackets, etc.)
    elif tag == 'd':
        beg_chr = elem.find('m:dPr/m:begChr', ns)
        end_chr = elem.find('m:dPr/m:endChr', ns)
        # Handle array/table separator
        if beg_chr is not None and beg_chr.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val') == '[':
            # Matrix bracket
            inner = parse_omml_children(elem, ns)
            return f'\\begin{{bmatrix}}{inner}\\end{{bmatrix}}'
        else:
            left = '\\left('
            right = '\\right)'
            if beg_chr is not None:
                val = beg_chr.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val')
                if val in ('{', '['):
                    left = '\\left' + val
            if end_chr is not None:
                val = end_chr.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val')
                if val in ('}', ']'):
                    right = '\\right' + val
            inner = parse_omml_children(elem, ns)
            return f'{left}{inner}{right}'

    # Superscript
    elif tag == 'sSup':
        base = elem.find('m:e', ns)
        sup = elem.find('m:sup', ns)
        base_text = parse_omml_children(base, ns) if base is not None else ''
        sup_text = parse_omml_children(sup, ns) if sup is not None else ''
        return f'{{{base_text}}}^{{{sup_text}}}'

    # Subscript
    elif tag == 'sSub':
        base = elem.find('m:e', ns)
        sub = elem.find('m:sub', ns)
        base_text = parse_omml_children(base, ns) if base is not None else ''
        sub_text = parse_omml_children(sub, ns) if sub is not None else ''
        return f'{{{base_text}}}_{{{sub_text}}}'

    # Sub+Sup
    elif tag == 'sSubSup':
        base = elem.find('m:e', ns)
        sub = elem.find('m:sub', ns)
        sup = elem.find('m:sup', ns)
        base_text = parse_omml_children(base, ns) if base is not None else ''
        sub_text = parse_omml_children(sub, ns) if sub is not None else ''
        sup_text = parse_omml_children(sup, ns) if sup is not None else ''
        return f'{{{base_text}}}_{{{sub_text}}}^{{{sup_text}}}'

    # Radical (sqrt)
    elif tag == 'rad':
        deg = elem.find('m:radPr/m:deg', ns)
        e = elem.find('m:e', ns)
        e_text = parse_omml_children(e, ns) if e is not None else ''
        if deg is not None:
            deg_text = parse_omml_children(deg, ns)
            return f'\\sqrt[{deg_text}]{{{e_text}}}'
        return f'\\sqrt{{{e_text}}}'

    # Nary (sum, prod, integral)
    elif tag == 'nary':
        chr_elem = elem.find('m:naryPr/m:chr', ns)
        chr_val = ''
        if chr_elem is not None:
            chr_val = chr_elem.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val', '')

        sub = elem.find('m:sub', ns)
        sup = elem.find('m:sup', ns)
        e = elem.find('m:e', ns)

        # Map Unicode characters to LaTeX
        nary_map = {
            '∑': '\\sum',
            '∫': '\\int',
            '∏': '\\prod',
            '∐': '\\coprod',
            '∬': '\\iint',
            '∭': '\\iiint',
            '⋃': '\\bigcup',
            '⋂': '\\bigcap',
        }
        latex_cmd = nary_map.get(chr_val, chr_val)

        limits = ''
        if sub is not None:
            limits += f'_{{{parse_omml_children(sub, ns)}}}'
        if sup is not None:
            limits += f'^{{{parse_omml_children(sup, ns)}}}'

        e_text = parse_omml_children(e, ns) if e is not None else ''
        return f'{latex_cmd}{limits}{{{e_text}}}'

    # Accent
    elif tag == 'acc':
        chr_elem = elem.find('m:accPr/m:chr', ns)
        e = elem.find('m:e', ns)
        e_text = parse_omml_children(e, ns) if e is not None else ''
        if chr_elem is not None:
            chr_val = chr_elem.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val', '')
            accent_map = {
                '̂': '\\hat',  # circumflex
                'ˆ': '\\hat',
                '̃': '\\tilde',  # tilde
                '̄': '\\bar',  # macron
                '̅': '\\overline',
                '̆': '\\breve',
                '̇': '\\dot',
                '̈': '\\ddot',
                '⃗': '\\vec',
                '→': '\\vec',  # right arrow (used as vector)
            }
            latex_accent = accent_map.get(chr_val, '\\widehat')
            return f'{latex_accent}{{{e_text}}}'
        return f'\\hat{{{e_text}}}'

    # Group character (overbrace/underbrace)
    elif tag == 'groupChr':
        chr_elem = elem.find('m:groupChrPr/m:chr', ns)
        pos = elem.find('m:groupChrPr/m:pos', ns)
        e = elem.find('m:e', ns)
        e_text = parse_omml_children(e, ns) if e is not None else ''
        is_under = False
        if pos is not None:
            is_under = pos.get('{http://schemas.openxmlformats.org/officeDocument/2006/math}val') == 'bot'
        if is_under:
            return f'\\underbrace{{{e_text}}}'
        else:
            return f'\\overbrace{{{e_text}}}'

    # Function
    elif tag == 'func':
        fname = elem.find('m:fName', ns)
        e = elem.find('m:e', ns)
        fname_text = parse_omml_children(fname, ns) if fname is not None else ''
        e_text = parse_omml_children(e, ns) if e is not None else ''
        return f'{fname_text}{{{e_text}}}'

    # Box
    elif tag == 'box':
        e = elem.find('m:e', ns)
        if e is not None:
            return parse_omml_children(e, ns)
        return ''

    # Equation array / Matrix
    elif tag == 'eqArr':
        rows = elem.findall('m:e', ns)
        return ' \\\\ '.join(parse_omml_children(r, ns) for r in rows)

    # Phantom
    elif tag == 'phant':
        return ''  # skip phantom

    # Bar (overline)
    elif tag == 'bar':
        e = elem.find('m:e', ns)
        e_text = parse_omml_children(e, ns) if e is not None else ''
        return f'\\overline{{{e_text}}}'

    # For oMath, oMathPara, and other containers: just process children
    elif tag in ('oMath', 'oMathPara', 'd', 'e', 'num', 'den', 'sup', 'sub', 'fName',
                  'm', 'lim', 'limLow', 'deg', 'borderBox'):
        return parse_omml_children(elem, ns)

    # Default: process children
    else:
        return parse_omml_children(elem, ns)


def parse_omml_children(elem, ns):
    """处理元素的所有子节点"""
    parts = []
    if elem.text:
        parts.append(elem.text.strip())
    for child in elem:
        parts.append(parse_omml_element(child, ns))
        if child.tail:
            parts.append(child.tail.strip())
    return ''.join(parts)


def extract_omml_text(elem, ns):
    """从 OMML 文本运行中提取文本"""
    text_parts = []
    for t_elem in elem.findall('.//m:t', ns):
        if t_elem.text:
            # Preserve the text as-is but remove extra whitespace
            text = t_elem.text.strip()
            # Handle special characters
            text = text.replace('‖', '||')  # double vertical line
            text_parts.append(text)
    return ' '.join(text_parts)


# ============================================================
# XML 命名空间
# ============================================================
NSMAP = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
}


def extract_slide_text_and_math(slide_xml):
    """从幻灯片XML中提取文本和公式，按出现顺序"""
    # First, replace all OMML elements with LaTeX markers and keep track of positions
    # Strategy: find all m:oMath sections, extract to LaTeX, replace in text

    # Find all OMML blocks
    omml_pattern = re.compile(
        r'<m:oMath.*?</m:oMath>|<m:oMathPara.*?</m:oMathPara>',
        re.DOTALL
    )

    # Extract text from a:t tags, but mark OMML positions
    result_parts = []
    last_end = 0

    for match in omml_pattern.finditer(slide_xml):
        # Text before this OMML
        before = slide_xml[last_end:match.start()]
        text_before = extract_a_t_text(before)
        if text_before.strip():
            result_parts.append(('text', text_before))

        # OMML
        omml = match.group()
        latex = omml_to_latex(omml)
        if latex:
            result_parts.append(('math', latex))

        last_end = match.end()

    # Remaining text after last OMML
    after = slide_xml[last_end:]
    text_after = extract_a_t_text(after)
    if text_after.strip():
        result_parts.append(('text', text_after))

    return result_parts


def extract_a_t_text(xml_fragment):
    """从XML片段中提取<a:t>标签内的文本"""
    texts = re.findall(r'<a:t[^>]*>(.*?)</a:t>', xml_fragment, re.DOTALL)
    # Join with space, strip whitespace
    cleaned = []
    for t in texts:
        t = t.strip()
        if t:
            cleaned.append(t)
    result = ' '.join(cleaned)
    return result


def check_has_blips(xml_content):
    """检查是否有图片引用"""
    return bool(re.search(r'<a:blip\s', xml_content))


def process_pptx(pptx_path):
    """主处理流程"""
    slides_content = []

    with zipfile.ZipFile(pptx_path, 'r') as z:
        # Get all slide files sorted
        slide_files = sorted(
            [f for f in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', f)],
            key=lambda x: int(re.search(r'slide(\d+)', x).group(1))
        )

        for sf in slide_files:
            slide_num = int(re.search(r'slide(\d+)', sf).group(1))
            with z.open(sf) as f:
                content = f.read().decode('utf-8', errors='replace')

            parts = extract_slide_text_and_math(content)
            has_blip = check_has_blips(content)

            slides_content.append({
                'num': slide_num,
                'parts': parts,
                'has_images': has_blip
            })

    return slides_content


def format_slides_to_md(slides_content):
    """将提取的内容格式化为源MD"""
    md_lines = []

    for slide in slides_content:
        sn = slide['num']
        parts = slide['parts']
        has_imgs = slide['has_images']

        # Slide header
        md_lines.append(f'## 幻灯片 {sn}')
        md_lines.append('')

        if has_imgs and not parts:
            md_lines.append('*（此幻灯片包含图片，暂无文本提取）*')
            md_lines.append('')

        for ptype, pcontent in parts:
            if ptype == 'text':
                # Clean text: remove excessive whitespace
                text = re.sub(r'\s+', ' ', pcontent).strip()
                if text:
                    # Check if it looks like a heading
                    if len(text) < 50 and not text.endswith(('。', '.', ',', '，')):
                        md_lines.append(f'### {text}')
                    else:
                        md_lines.append(text)

                    # Check if this text contains "总结" or looks like a bullet list from content
                    md_lines.append('')
            elif ptype == 'math':
                md_lines.append(pcontent)
                md_lines.append('')

        md_lines.append('')

    return '\n'.join(md_lines)


def post_process(text):
    """后处理清理"""
    # 1. 数学斜体 Unicode 清理
    text = fix_math_unicode(text)

    # 2. 损坏 LaTeX 修复
    text = text.replace('\\c\\dots', '\\cdots')
    text = text.replace('\\v\\dots', '\\vdots')
    text = text.replace('\\d\\dots', '\\ddots')

    # 3. 裸 \left...\right 包裹 $$ (check for display math that's missing $$)
    # Find \left...\right patterns not inside $...$ or $$...$$
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if re.search(r'\\left', stripped) and re.search(r'\\right', stripped):
            if not stripped.startswith('$') and not stripped.startswith('$$'):
                new_lines.append(f'$${stripped}$$')
                continue
        # Remove orphan single-char lines
        if len(stripped) <= 2 and stripped and not stripped.startswith(('#', '$', '>', '-', '*', '|')):
            continue
        new_lines.append(line)
    text = '\n'.join(new_lines)

    # 4. Remove empty slide headers (幻灯片 N with nothing below)
    text = re.sub(r'## 幻灯片 \d+\n\n(?=## 幻灯片)', '', text)

    # 5. Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text


def main():
    pptx_path = r'D:\知识库\课程\数值分析\课件\数值分析01BackgroundAndBasis.pptx'
    output_dir = r'D:\知识库\课程\数值分析\课件\MD'
    os.makedirs(output_dir, exist_ok=True)

    print("Processing PPTX...")
    slides = process_pptx(pptx_path)
    print(f"Extracted {len(slides)} slides")

    # Count math elements
    math_count = sum(1 for s in slides for p in s['parts'] if p[0] == 'math')
    img_count = sum(1 for s in slides if s['has_images'])
    print(f"Found {math_count} math elements, {img_count} slides with images")

    raw_md = format_slides_to_md(slides)
    print(f"Raw MD length: {len(raw_md)}")

    # Post-process
    cleaned_md = post_process(raw_md)
    print(f"Cleaned MD length: {len(cleaned_md)}")

    # Build frontmatter
    frontmatter = """---
raw_title: 数值分析01BackgroundAndBasis
subject: 数值分析
source: 数值分析01BackgroundAndBasis.pptx
status: PPTX转换（待校对）
topics:
  - 数值分析基础
  - 科学计算
  - 误差分析
  - 浮点数
  - 算法稳定性
---

"""

    full_md = frontmatter + cleaned_md

    output_path = os.path.join(output_dir, '数值分析01BackgroundAndBasis.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f"Written to: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")

    # Verification checks
    print("\n=== Verification ===")
    print(f"1. Math italic Unicode: ", 'PASS' if not re.findall(r'[\U0001D400-\U0001D7FF]', full_md) else 'FAIL')
    print(f"2. Damaged LaTeX: ", 'PASS' if ('\\c\\dots' not in full_md and '\\v\\dots' not in full_md and '\\d\\dots' not in full_md) else 'FAIL')
    print(f"3. Has ## headings: ", 'PASS' if full_md.count('\n## ') > 0 else 'FAIL')
    print(f"4. File > 5KB: ", 'PASS' if os.path.getsize(output_path) > 5000 else 'FAIL')

    # Print a sample
    lines = full_md.split('\n')
    print(f"\n=== First 50 lines ===")
    for l in lines[:50]:
        print(l)

    return full_md


if __name__ == '__main__':
    result = main()
