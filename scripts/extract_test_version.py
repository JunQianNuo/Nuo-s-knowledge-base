"""Extract test-only version v4 — handle ALL irregular formats."""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

INPUT = r'D:\知识库\课程\英语\课件\MD\听力训练测试1-12_完整详细解析.md'
OUTPUT = r'D:\知识库\课程\英语\课件\MD\听力训练测试1-12_测试版.md'

with open(INPUT, 'r', encoding='utf-8') as f:
    text = f.read()

# Pre-process: convert HTML-commented options/answers to regular lines
# <!-- **★D.21** --> → **★D.21**
# <!-- **正确答案：A** --> → **正确答案：A**
def uncomment(m):
    inner = m.group(1).strip()
    return inner
text = re.sub(r'<!--\s*(.+?)\s*-->', lambda m: uncomment(m) if re.search(r'[A-D][.．]|正确答案|答案|★|✓', m.group(1)) else m.group(0), text)

# Re-split after preprocessing
lines = text.split('\n')

# ── Regex patterns ──
# Question start: any format (##/###/#### N., **N., ## Question N:, etc.)
Q_START = re.compile(
    r'^(?:#{1,4}\s*|\*\*)(\d+)[\.、．](?:\*\*)?\s*(.+)'  # ## 1. text / **1. text**
)
Q_NAMED = re.compile(
    r'^(?:#{1,4}\s*|#{1,4}\*\*|\*\*)(Question\s*\d+)(?:[：:].+?)?(?:\*\*)?\s*$'
)
Q_NAMED_WITH_TEXT = re.compile(
    r'^(?:#{1,4}\s*|#{1,4}\*\*|\*\*)(Question\s*\d+[：:].+?)(?:\*\*)?\s*$'
)

# Answer patterns (checked in order, most specific first)
ANS_STAR = re.compile(r'^(?:#{1,4}\s*)?(?:\*\*)?★\s*([A-D])[.．]?\s*(.+)')           # ★A. / **★A. / ### ★A.
ANS_BRACKET = re.compile(r'(?:\*\*)?(?:【正确答案】|【答案】)(?:\*\*)?\s*([A-D])[.．]?\s*(.+)')  # 【正确答案】A. or 【答案】A.
ANS_BOLD_COLON = re.compile(r'\*\*正确答案[：:]\s*([A-D])\s*\*\*')  # **正确答案：A**
ANS_BOLD_COLON2 = re.compile(r'\*\*正确答案[：:]\*\*\s*([A-D])')   # **正确答案：**A
ANS_PLAIN = re.compile(r'(?:答案|正确答案)[：:]\s*([A-D])\b')             # 答案：A or 正确答案：A
ANS_BOLD_ANSWER = re.compile(r'\*\*(?:答案|正确答案)[：:]\s*([A-D])[.．]?')  # **答案：D.** or **正确答案：A**
ANS_HEADING_ANSWER = re.compile(r'^#{1,4}\s*(?:答案|正确答案)[：:]\s*([A-D])[.．]?\s*(.*)')  # # 答案：D. or ## 正确答案：B
ANS_CHECK = re.compile(r'\*\*([A-D])\..*?✓')                    # **A.text✓**
ANS_SECTION = re.compile(r'^#{1,4}\s*【答案】[：:]?\s*([A-D])')   # # 【答案】B...

# Option: A. / B. / C. / D.
OPTION = re.compile(r'^(?:#{1,4}\s*)?(?:\*\*)?\s*([A-D])[.．]\s*(.+)')

# Translation
YI = re.compile(r'^(?:#{1,4}\s*)?(?:题意|翻译)[：:]\s*(.+)')

# Frontmatter
fm_end = 0
lines = text.split('\n')
if lines[0].strip() == '---':
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            fm_end = i + 1
            break

body_lines = lines[fm_end:]

# ── Pass 1: Extract all questions ──
questions = []
current_q = None
current_test = ''
current_section = ''

# Track section type for context
in_answer_section = False  # Inside 【答案】 block

for line in body_lines:
    stripped = line.strip()
    if not stripped:
        continue

    # ── Test heading ──
    tm = re.match(r'^#{1,2}\s*(?:听力训练)?(?:听力)?测试(\d+)', stripped)
    if tm:
        if current_q:
            questions.append(current_q)
            current_q = None
        current_test = f'测试{tm.group(1)}'
        current_section = ''
        in_answer_section = False
        # Extract passage/conversation from same line
        remaining = stripped[tm.end():].strip()
        if remaining:
            # e.g., "Passage 1-Conversation 1 (Questions 1-4）"
            sm2 = re.match(r'((?:Passage|Conversation|Talk|Lecture|Recording|填空)[^【\n]*)', remaining)
            if sm2:
                sec = sm2.group(1).strip().rstrip('*').strip()
                sec = re.sub(r'\*\*', '', sec)
                current_section = sec
        continue

    # ── Section heading (passage/conversation/etc) ──
    sm = re.match(
        r'^(?:#{1,4}\s*|\*\*)((?:Passage|Conversation|Talk|Lecture|Recording|填空)[^【\n]*)',
        stripped
    )
    if sm:
        if current_q:
            questions.append(current_q)
            current_q = None
        sec = sm.group(1).strip().rstrip('*').strip()
        sec = re.sub(r'\*\*', '', sec)
        current_section = sec
        in_answer_section = False
        continue

    # ── 【答案】 section ──
    if re.match(r'^#{1,4}\s*【答案】', stripped):
        in_answer_section = True
        # Check if this line contains the answer directly (# 【答案】B. text)
        am = ANS_SECTION.match(stripped)
        if not am:
            # Try: 【答案】B. text
            am = re.match(r'(?:#{1,4}\s*)?(?:【答案】)\s*([A-D])[.．]?\s*(.*)', stripped)
        if am and current_q:
            current_q['answer_letter'] = am.group(1)
            text = am.group(2).strip() if am.lastindex >= 2 else ''
            if text:
                text = re.sub(r'\*\*', '', text)
                current_q['answer_text'] = text
                if not any(o[0] == am.group(1) for o in current_q['options']):
                    current_q['options'].append((am.group(1), text))
        elif am:
            # Answer found but no current question — try the last question
            if questions:
                last = questions[-1]
                if not last['answer_letter']:
                    last['answer_letter'] = am.group(1)
                    text = am.group(2).strip() if am.lastindex >= 2 else ''
                    if text:
                        text = re.sub(r'\*\*', '', text)
                        last['answer_text'] = text
                        if not any(o[0] == am.group(1) for o in last['options']):
                            last['options'].append((am.group(1), text))
        continue

    # ── End of answer section ──
    if in_answer_section and re.match(r'^(?:#{1,4}\s*)?【(?:解析|文章大意|文章总结)】', stripped):
        in_answer_section = False
        continue

    # ── If in answer section, look for answer letter ──
    if in_answer_section:
        # Check for answer patterns
        for pat in [ANS_BOLD_COLON, ANS_BOLD_COLON2, ANS_PLAIN]:
            am = pat.search(stripped)
            if am and current_q:
                current_q['answer_letter'] = am.group(1)
                break
        continue

    # ── Named question start (## Question N or ## Question N: text) ──
    qm = Q_NAMED.match(stripped)
    if qm:
        if current_q:
            questions.append(current_q)
        current_q = {
            'test': current_test,
            'section': current_section,
            'yi': '',
            'options': [],
            'answer_letter': '',
            'answer_text': '',
            'explanation': '',
        }
        continue

    # ── Numbered question start ──
    qm2 = Q_START.match(stripped)
    if qm2:
        qtext = qm2.group(2).strip().rstrip('*').strip()
        # Skip non-questions
        if len(qtext) < 5:
            continue
        if re.match(r'^(?:测试|Passage|Conversation|Talk|Lecture|Recording|填空)', qtext):
            continue
        # Skip translation lines that start with numbers
        if any(kw in qtext for kw in ['翻译', '题意', '文章', '听力']):
            continue

        if current_q:
            questions.append(current_q)
        current_q = {
            'test': current_test,
            'section': current_section,
            'yi': '',
            'options': [],
            'answer_letter': '',
            'answer_text': '',
            'explanation': '',
        }
        continue

    if not current_q:
        continue

    # ── 题意/翻译 ──
    ym = YI.match(stripped)
    if ym:
        current_q['yi'] = ym.group(1).strip()
        continue

    # ── Answer: ★A. text ──
    sm_ = ANS_STAR.match(stripped)
    if sm_:
        letter = sm_.group(1)
        text = sm_.group(2).strip()
        text = re.sub(r'\*\*', '', text)
        current_q['answer_letter'] = letter
        current_q['answer_text'] = text
        if not any(o[0] == letter for o in current_q['options']):
            current_q['options'].append((letter, text))
        continue

    # ── Answer: 【正确答案】A. ──
    am = ANS_BRACKET.match(stripped)
    if am:
        letter = am.group(1)
        text = am.group(2).strip() if am.group(2) else ''
        text = re.sub(r'\*\*', '', text)
        current_q['answer_letter'] = letter
        if text:
            current_q['answer_text'] = text
        if not any(o[0] == letter for o in current_q['options']):
            current_q['options'].append((letter, text))
        continue

    # ── Answer: **正确答案：A** or **正确答案：**A ──
    for pat in [ANS_BOLD_COLON, ANS_BOLD_COLON2]:
        am = pat.search(stripped)
        if am:
            current_q['answer_letter'] = am.group(1)
            break
    if am:
        continue

    # ── Answer: # 答案：D.text or ## 正确答案：B.text ──
    am = ANS_HEADING_ANSWER.match(stripped)
    if am:
        letter = am.group(1)
        current_q['answer_letter'] = letter
        text = am.group(2).strip() if am.lastindex >= 2 else ''
        if text:
            text = re.sub(r'\*\*', '', text)
            if not any(o[0] == letter for o in current_q['options']):
                current_q['options'].append((letter, text))
        continue

    # ── Answer: **答案：A.text** or **正确答案：A.text** ──
    am = ANS_BOLD_ANSWER.search(stripped)
    if am:
        letter = am.group(1)
        current_q['answer_letter'] = letter
        # Check if option text follows the answer marker
        after = stripped[am.end():].strip()
        if after and not any(o[0] == letter for o in current_q['options']):
            text = re.sub(r'\*\*|✓|★', '', after).strip()
            if text:
                current_q['options'].append((letter, text))
        continue

    # ── Answer: 答案：A or 正确答案：A ──
    am = ANS_PLAIN.search(stripped)
    if am:
        current_q['answer_letter'] = am.group(1)
        continue

    # ── Answer: **A.text✓** ──
    cm = ANS_CHECK.search(stripped)
    if cm:
        letter = cm.group(1)
        current_q['answer_letter'] = letter
        # Also extract option text and add to options
        text_match = re.match(r'^(?:\*\*)?\s*([A-D])[.．]\s*(.+)', stripped)
        if text_match and text_match.group(1) == letter:
            text = text_match.group(2).strip()
            text = re.sub(r'\*\*|✓|★', '', text).strip()
            if not any(o[0] == letter for o in current_q['options']):
                current_q['options'].append((letter, text))
        continue

    # ── Option: A. / B. / C. / D. ──
    om = OPTION.match(stripped)
    if om:
        letter = om.group(1)
        text = om.group(2).strip()
        text = re.sub(r'\*\*|✓|★', '', text).strip()
        if not any(o[0] == letter for o in current_q['options']):
            current_q['options'].append((letter, text))
        continue

    # ── Explanation ──
    if re.match(r'^(?:解析|详解|【解析】)', stripped):
        expl = re.sub(r'^(?:解析|详解|【解析】)[：:]\s*', '', stripped)
        current_q['explanation'] = expl
        continue

# Flush last
if current_q:
    questions.append(current_q)

print(f'Total questions found: {len(questions)}')
with_ans = sum(1 for q in questions if q['answer_letter'])
with_opts = sum(1 for q in questions if q['options'])
print(f'With answer: {with_ans}, With options: {with_opts}')

# ── Filter: keep only questions with options ──
valid_qs = [q for q in questions if len(q['options']) >= 2]

# ── Build output ──
output = []
output.append('---\n')
output.append('title: 听力训练测试1-12 测试版\n')
output.append('subject: 英语\n')
output.append('source: 听力训练测试1-12_完整详细解析.docx\n')
output.append('status: 测试版\n')
output.append('topics:\n')
output.append('  - 听力训练\n')
output.append('  - 英语四级\n')
output.append('  - 自测练习\n')
output.append('---\n\n')

last_test = ''
last_section = ''
q_counter = 0

for q in valid_qs:
    q_counter += 1

    if q['test'] and q['test'] != last_test:
        output.append(f'# {q["test"]}\n\n')
        last_test = q['test']
        last_section = ''

    section_label = q['section'].strip()
    section_label = re.sub(r'\*\*', '', section_label).strip()
    if section_label and section_label != last_section:
        output.append(f'## {section_label}\n\n')
        last_section = section_label

    output.append(f'**Q{q_counter}**\n\n')

    if q['yi']:
        yi_clean = re.sub(r'\*\*', '', q['yi']).strip()
        output.append(f'> {yi_clean}\n\n')

    sorted_opts = sorted(q['options'], key=lambda x: x[0])
    for letter, text in sorted_opts:
        text = re.sub(r'-+\s*$', '', text).strip()
        if not text:
            text = '(选项文本缺失)'
        output.append(f'- {letter}. {text}\n')
    output.append('\n')

    if q['answer_letter']:
        output.append('> [!faq]- 点击查看答案\n')
        output.append(f'> **正确答案：{q["answer_letter"]}**\n')
        if q['answer_text']:
            ans_short = re.split(r'[。\n]', q['answer_text'])[0]
            ans_short = re.sub(r'\*\*', '', ans_short)
            if ans_short.strip():
                output.append(f'> {ans_short}\n')
        if q['explanation']:
            expl_clean = re.sub(r'\*\*', '', q['explanation'])
            expl_short = expl_clean[:250]
            if len(expl_clean) > 250:
                expl_short += '...'
            output.append(f'>\n> **解析**：{expl_short}\n')
        output.append('\n')

    output.append('---\n\n')

result = ''.join(output)
result = re.sub(r'\n{3,}', '\n\n', result)

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Written: {OUTPUT}')
print(f'Output questions: {q_counter}')
print(f'Size: {len(result)} chars, {result.count(chr(10))} lines')
