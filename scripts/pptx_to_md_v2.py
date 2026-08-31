#!/usr/bin/env python3
# LEGACY: 已被 MinerU 替代，保留为备用方案
"""PPTX → 源MD 转换脚本 v2 — 改进版OMML→LaTeX
"""

import zipfile
import re
import os
import sys

# ============================================================
# Unicode math italic → ASCII mapping
# ============================================================
def build_math_unicode_table():
    """Build translation table for math italic/bold/script Unicode"""
    table = {}
    # Math Italic lowercase a-z: U+1D44E to U+1D467
    for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz'):
        table[0x1D44E + i] = ch
    # Math Italic uppercase A-Z: U+1D434 to U+1D44D
    for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        table[0x1D434 + i] = ch
    # Math Bold Italic lowercase: U+1D482 to U+1D49B
    for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz'):
        table[0x1D482 + i] = ch
    # Math Bold Italic uppercase: U+1D468 to U+1D481
    for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        table[0x1D468 + i] = ch
    # Math Greek italic → regular Greek
    greek_map = {
        0x1D6FC: 'α', 0x1D6FD: 'β', 0x1D6FE: 'γ', 0x1D6FF: 'δ',
        0x1D700: 'ε', 0x1D701: 'ζ', 0x1D702: 'η', 0x1D703: 'θ',
        0x1D704: 'ι', 0x1D705: 'κ', 0x1D706: 'λ', 0x1D707: 'μ',
        0x1D708: 'ν', 0x1D709: 'ξ', 0x1D70B: 'π', 0x1D70C: 'ρ',
        0x1D70D: 'σ', 0x1D70E: 'ς', 0x1D70F: 'τ', 0x1D710: 'υ',
        0x1D711: 'φ', 0x1D712: 'χ', 0x1D713: 'ψ', 0x1D714: 'ω',
        0x1D71B: 'Δ', 0x1D71E: 'Ξ',
    }
    for cp, ch in greek_map.items():
        table[cp] = ch
    return table

MATH_TABLE = build_math_unicode_table()

def fix_math_unicode(text):
    """Replace math italic Unicode with ASCII"""
    result = []
    for ch in text:
        cp = ord(ch)
        if 0x1D400 <= cp <= 0x1D7FF:
            replacement = MATH_TABLE.get(cp, '')
            if replacement:
                result.append(replacement)
        else:
            result.append(ch)
    return ''.join(result)


# ============================================================
# OMML → LaTeX using regex-based recursive descent
# ============================================================
def extract_mt_text(content):
    """Extract text from m:t elements"""
    texts = re.findall(r'<m:t[^>]*>(.*?)</m:t>', content, re.DOTALL)
    return ''.join(t.strip() for t in texts)


def omml_fragment_to_latex(content):
    """Convert a single OMML element (m:oMath or inner element) to LaTeX.
    Uses regex matching from the inside out."""
    # Clean: remove control properties (m:ctrlPr, m:sSupPr, m:sSubPr, m:dPr, etc.)
    cleaned = re.sub(r'<m:\w+Pr>.*?</m:\w+Pr>', '', content, flags=re.DOTALL)
    cleaned = re.sub(r'<m:\w+Pr\s*/>', '', cleaned)

    # Remove non-math XML tags (a:rPr, formatting)
    cleaned = re.sub(r'<a:rPr\b.*?</a:rPr>', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'<a:latin\b[^>]*/>', '', cleaned)
    cleaned = re.sub(r'<a:cs\b[^>]*/>', '', cleaned)

    # Now process structurally: Find and convert nested elements
    return parse_omml_content(cleaned)


def parse_omml_content(content):
    """Recursively parse OMML content string into LaTeX"""
    # Remove outer m:oMath/m:oMathPara wrapper
    content = re.sub(r'^<m:oMath[^>]*>|</m:oMath>$', '', content.strip())
    content = re.sub(r'^<m:oMathPara[^>]*>|</m:oMathPara>$', '', content.strip())

    # Base case: if no more OMML tags, extract remaining text
    if not re.search(r'<m:', content):
        text = re.sub(r'<[^>]+>', '', content)
        text = fix_math_unicode(text)
        return text.strip()

    # Process from inner to outer
    # Handle m:r (run - text content)
    result = content

    # First handle innermost: m:r > m:t
    # Replace m:r with its text content
    def extract_run(m):
        inner = m.group(1)
        texts = re.findall(r'<m:t[^>]*>(.*?)</m:t>', inner, re.DOTALL)
        return ''.join(t.strip() for t in texts)

    result = re.sub(r'<m:r\b[^>]*>(.*?)</m:r>', extract_run, result, flags=re.DOTALL)

    # Handle m:f (fraction)
    def handle_frac(m):
        inner = m.group(1)
        num_match = re.search(r'<m:num>(.*?)</m:num>', inner, re.DOTALL)
        den_match = re.search(r'<m:den>(.*?)</m:den>', inner, re.DOTALL)
        num = parse_omml_content(num_match.group(1)) if num_match else ''
        den = parse_omml_content(den_match.group(1)) if den_match else ''
        return f'\\frac{{{num}}}{{{den}}}'
    result = re.sub(r'<m:f\b[^>]*>(.*?)</m:f>', handle_frac, result, flags=re.DOTALL)

    # Handle m:rad (radical/sqrt)
    def handle_rad(m):
        inner = m.group(1)
        deg_match = re.search(r'<m:deg>(.*?)</m:deg>', inner, re.DOTALL)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        if deg_match:
            deg = parse_omml_content(deg_match.group(1))
            return f'\\sqrt[{deg}]{{{e_text}}}'
        return f'\\sqrt{{{e_text}}}'
    result = re.sub(r'<m:rad\b[^>]*>(.*?)</m:rad>', handle_rad, result, flags=re.DOTALL)

    # Handle m:sSubSup (subscript and superscript)
    def handle_sSubSup(m):
        inner = m.group(1)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        sub_match = re.search(r'<m:sub>(.*?)</m:sub>', inner, re.DOTALL)
        sup_match = re.search(r'<m:sup>(.*?)</m:sup>', inner, re.DOTALL)
        base = parse_omml_content(e_match.group(1)) if e_match else ''
        sub = parse_omml_content(sub_match.group(1)) if sub_match else ''
        sup = parse_omml_content(sup_match.group(1)) if sup_match else ''
        return f'{{{base}}}_{{{sub}}}^{{{sup}}}'
    result = re.sub(r'<m:sSubSup\b[^>]*>(.*?)</m:sSubSup>', handle_sSubSup, result, flags=re.DOTALL)

    # Handle m:sSup (superscript) - must be after sSubSup
    def handle_sSup(m):
        inner = m.group(1)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        sup_match = re.search(r'<m:sup>(.*?)</m:sup>', inner, re.DOTALL)
        base = parse_omml_content(e_match.group(1)) if e_match else ''
        sup = parse_omml_content(sup_match.group(1)) if sup_match else ''
        return f'{{{base}}}^{{{sup}}}'
    result = re.sub(r'<m:sSup\b[^>]*>(.*?)</m:sSup>', handle_sSup, result, flags=re.DOTALL)

    # Handle m:sSub (subscript) - must be after sSubSup
    def handle_sSub(m):
        inner = m.group(1)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        sub_match = re.search(r'<m:sub>(.*?)</m:sub>', inner, re.DOTALL)
        base = parse_omml_content(e_match.group(1)) if e_match else ''
        sub = parse_omml_content(sub_match.group(1)) if sub_match else ''
        return f'{{{base}}}_{{{sub}}}'
    result = re.sub(r'<m:sSub\b[^>]*>(.*?)</m:sSub>', handle_sSub, result, flags=re.DOTALL)

    # Handle m:d (delimiter)
    def handle_delim(m):
        inner = m.group(1)
        # Get delimiter characters
        beg = re.search(r'<m:begChr[^>]*val="([^"]*)"', inner)
        end = re.search(r'<m:endChr[^>]*val="([^"]*)"', inner)
        left = '\\left('
        right = '\\right)'
        if beg:
            v = beg.group(1)
            if v == '[': left = '\\left['
            elif v == '{': left = '\\left\\{'
            elif v == '|': left = '\\left|'
            elif v == '||': left = '\\left\\|'
        if end:
            v = end.group(1)
            if v == ']': right = '\\right]'
            elif v == '}': right = '\\right\\}'
            elif v == '|': right = '\\right|'
            elif v == '||': right = '\\right\\|'
        # Inner content
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        if e_match:
            inner_text = parse_omml_content(e_match.group(1))
        else:
            # Case where d encloses multiple e elements
            es = re.findall(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
            inner_text = ' , '.join(parse_omml_content(e) for e in es)
        return f'{left}{inner_text}{right}'
    result = re.sub(r'<m:d\b[^>]*>(.*?)</m:d>', handle_delim, result, flags=re.DOTALL)

    # Handle m:e (element container - just recurse)
    def handle_e(m):
        return parse_omml_content(m.group(1))
    result = re.sub(r'<m:e>(.*?)</m:e>', handle_e, result, flags=re.DOTALL)

    # Handle m:func (function like sin, cos)
    def handle_func(m):
        inner = m.group(1)
        fname_match = re.search(r'<m:fName>(.*?)</m:fName>', inner, re.DOTALL)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        fname = parse_omml_content(fname_match.group(1)) if fname_match else ''
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        return f'{fname}{{{e_text}}}'
    result = re.sub(r'<m:func\b[^>]*>(.*?)</m:func>', handle_func, result, flags=re.DOTALL)

    # Handle m:nary (sum, integral, product)
    def handle_nary(m):
        inner = m.group(1)
        chr_match = re.search(r'<m:chr[^>]*val="([^"]*)"', inner)
        sub_match = re.search(r'<m:sub>(.*?)</m:sub>', inner, re.DOTALL)
        sup_match = re.search(r'<m:sup>(.*?)</m:sup>', inner, re.DOTALL)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        symbol_map = {'∑': '\\sum', '∫': '\\int', '∏': '\\prod'}
        sym = symbol_map.get(chr_match.group(1), chr_match.group(1)) if chr_match else '\\sum'
        limits = ''
        if sub_match:
            limits += f'_{{{parse_omml_content(sub_match.group(1))}}}'
        if sup_match:
            limits += f'^{{{parse_omml_content(sup_match.group(1))}}}'
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        return f'{sym}{limits}{{{e_text}}}'
    result = re.sub(r'<m:nary\b[^>]*>(.*?)</m:nary>', handle_nary, result, flags=re.DOTALL)

    # Handle m:acc (accent)
    def handle_acc(m):
        inner = m.group(1)
        chr_match = re.search(r'<m:chr[^>]*val="([^"]*)"', inner)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        accent_map = {'̂': '\\hat', '̃': '\\tilde', '̄': '\\bar', '̈': '\\ddot',
                       '→': '\\vec'}
        acc = accent_map.get(chr_match.group(1), '\\hat') if chr_match else '\\hat'
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        return f'{acc}{{{e_text}}}'
    result = re.sub(r'<m:acc\b[^>]*>(.*?)</m:acc>', handle_acc, result, flags=re.DOTALL)

    # Handle m:bar (overline)
    def handle_bar(m):
        inner = m.group(1)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        return f'\\overline{{{e_text}}}'
    result = re.sub(r'<m:bar\b[^>]*>(.*?)</m:bar>', handle_bar, result, flags=re.DOTALL)

    # Handle m:groupChr (overbrace/underbrace)
    def handle_groupChr(m):
        inner = m.group(1)
        pos_match = re.search(r'<m:pos[^>]*val="([^"]*)"', inner)
        e_match = re.search(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        e_text = parse_omml_content(e_match.group(1)) if e_match else ''
        if pos_match and pos_match.group(1) == 'bot':
            return f'\\underbrace{{{e_text}}}'
        return f'\\overbrace{{{e_text}}}'
    result = re.sub(r'<m:groupChr\b[^>]*>(.*?)</m:groupChr>', handle_groupChr, result, flags=re.DOTALL)

    # Handle m:eqArr (equation array)
    def handle_eqArr(m):
        inner = m.group(1)
        es = re.findall(r'<m:e>(.*?)</m:e>', inner, re.DOTALL)
        return ' \\\\ '.join(parse_omml_content(e) for e in es)
    result = re.sub(r'<m:eqArr\b[^>]*>(.*?)</m:eqArr>', handle_eqArr, result, flags=re.DOTALL)

    # Final cleanup: remove any remaining XML tags, fix math unicode
    result = re.sub(r'<[^>]+>', '', result)
    result = fix_math_unicode(result)
    result = result.strip()

    return result


def omml_to_latex(omml_string):
    """Convert OMML string to LaTeX display/inline math"""
    latex = omml_fragment_to_latex(omml_string)
    if not latex or latex == '':
        return "$???$"
    # Fix common issues
    latex = latex.replace('&amp;', '&')
    # Remove empty braces
    latex = re.sub(r'\{\}', '', latex)
    # Decide display vs inline
    if len(latex) > 35 or '\\frac' in latex or '\\sum' in latex:
        return f"$$\n{latex}\n$$"
    else:
        return f"${latex}$"


# ============================================================
# Main extraction
# ============================================================
def extract_slide_parts(slide_xml):
    """Extract text and math from slide XML, maintaining order"""
    # First, replace OMML sections with unique markers
    omml_pattern = re.compile(r'<m:oMath.*?</m:oMath>|<m:oMathPara.*?</m:oMathPara>', re.DOTALL)

    parts = []
    last_end = 0

    for match in omml_pattern.finditer(slide_xml):
        # Text before this OMML
        before = slide_xml[last_end:match.start()]
        text = clean_text(before)
        if text.strip():
            parts.append(('text', text))

        # OMML → LaTeX
        latex = omml_to_latex(match.group())
        parts.append(('math', latex))

        last_end = match.end()

    # Remaining text
    after = slide_xml[last_end:]
    text = clean_text(after)
    if text.strip():
        parts.append(('text', text))

    return parts


def clean_text(xml_fragment):
    """Extract text from a:t tags within XML fragment"""
    # Remove XML formatting tags (not text)
    cleaned = re.sub(r'<[^>]+>', '', xml_fragment)
    # Remove extra whitespace, but keep Chinese text
    cleaned = cleaned.strip()
    # Collapse multiple spaces
    cleaned = re.sub(r' +', ' ', cleaned)
    # Clean up special cases
    cleaned = cleaned.replace('\r', '')
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned


def check_blips(slide_xml):
    """Check for image references"""
    return bool(re.search(r'<a:blip\s', slide_xml))


def process_pptx(pptx_path):
    """Process PPTX and return slides content"""
    slides = []
    with zipfile.ZipFile(pptx_path, 'r') as z:
        slide_files = sorted(
            [f for f in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', f)],
            key=lambda x: int(re.search(r'slide(\d+)', x).group(1))
        )

        for sf in slide_files:
            sn = int(re.search(r'slide(\d+)', sf).group(1))
            with z.open(sf) as f:
                content = f.read().decode('utf-8', errors='replace')

            parts = extract_slide_parts(content)
            has_img = check_blips(content)
            slides.append({'num': sn, 'parts': parts, 'has_images': has_img})

    return slides


def format_md(slides):
    """Format slides to markdown"""
    lines = []
    for slide in slides:
        sn = slide['num']
        parts = slide['parts']
        has_img = slide['has_images']

        lines.append(f'## 幻灯片 {sn}')
        lines.append('')

        if has_img and not parts:
            lines.append('*（此幻灯片包含图片，暂无文本提取）*')
            lines.append('')
            continue

        # Check if this is purely an image slide with minimal text
        for ptype, pcontent in parts:
            if ptype == 'text':
                text = pcontent.strip()
                if not text:
                    continue
                # Clean out any remaining XML-like artifacts
                if re.search(r'xmlns:', text) or re.search(r'</a:\w+>', text):
                    # Skip heavy XML artifacts
                    if len(re.sub(r'<[^>]+>', '', text).strip()) < 10:
                        continue
                    text = clean_text(text)
                    if not text.strip():
                        continue

                # Detect if it's a heading-style short line
                if len(text) < 60 and '\n' not in text and not text.endswith(('。', '.', '，', ',', ';', '；')):
                    lines.append(f'### {text}')
                else:
                    for line in text.split('\n'):
                        line = line.strip()
                        if line:
                            lines.append(line)
                lines.append('')
            elif ptype == 'math':
                lines.append(pcontent)
                lines.append('')

    return '\n'.join(lines)


def post_process(text):
    """Final cleanup pass"""
    # 1. Math italic Unicode fix
    text = fix_math_unicode(text)

    # 2. Damaged LaTeX
    text = text.replace('\\c\\dots', '\\cdots')
    text = text.replace('\\v\\dots', '\\vdots')
    text = text.replace('\\d\\dots', '\\ddots')

    # 3. Remove orphan lines
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) <= 2 and stripped and not stripped.startswith(('#', '$', '>', '-', '*', '|')):
            continue
        # Remove lines with heavy XML artifacts
        if '<m:' in stripped or '<a:ln>' in stripped or '<a:effectLst>' in stripped:
            continue
        new_lines.append(line)

    text = '\n'.join(new_lines)

    # 4. Remove empty slide sections
    text = re.sub(r'## 幻灯片 \d+\n+\s*\n(?!###)', '', text)

    # 5. Collapse blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r'^###\s*\n', '', text, flags=re.MULTILINE)

    return text


def main():
    pptx_path = r'D:\知识库\课程\数值分析\课件\数值分析01BackgroundAndBasis.pptx'
    output_dir = r'D:\知识库\课程\数值分析\课件\MD'
    os.makedirs(output_dir, exist_ok=True)

    print("Processing PPTX v2...")
    slides = process_pptx(pptx_path)
    print(f"Extracted {len(slides)} slides")

    math_count = sum(1 for s in slides for p in s['parts'] if p[0] == 'math')
    img_count = sum(1 for s in slides if s['has_images'])
    print(f"Math: {math_count}, Image slides: {img_count}")

    raw_md = format_md(slides)
    print(f"Raw MD: {len(raw_md)} chars")

    cleaned = post_process(raw_md)
    print(f"Cleaned MD: {len(cleaned)} chars")

    frontmatter = """---
raw_title: 数值分析01BackgroundAndBasis
subject: 数值分析
source: 数值分析01BackgroundAndBasis.pptx
status: PPTX转换（待校对）
topics:
  - 数值分析基础
  - 科学计算
  - 误差分析
  - 有效数字
  - 浮点数
  - 算法稳定性
---

"""

    full_md = frontmatter + cleaned

    output_path = os.path.join(output_dir, '数值分析01BackgroundAndBasis.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_md)

    print(f"Written to: {output_path} ({os.path.getsize(output_path)} bytes)")

    # Verification
    print("\n=== Verification ===")
    v1 = not re.findall(r'[\U0001D400-\U0001D7FF]', full_md)
    print(f"1. Math italic Unicode: {'PASS' if v1 else 'FAIL'}")
    v2 = '\\c\\dots' not in full_md and '\\v\\dots' not in full_md and '\\d\\dots' not in full_md
    print(f"2. Damaged LaTeX: {'PASS' if v2 else 'FAIL'}")
    v3 = full_md.count('\n## ') > 0
    print(f"3. Has ## headings: {'PASS' if v3 else 'FAIL'}")
    v4 = os.path.getsize(output_path) > 5000
    print(f"4. File > 5KB: {'PASS' if v4 else 'FAIL'}")

    # Check for $???$ occurrences
    q_count = full_md.count('$???$')
    print(f"\n$???$ occurrences: {q_count}")

    return full_md


if __name__ == '__main__':
    result = main()
