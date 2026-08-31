#!/usr/bin/env python3
"""
闪卡同步脚本 — 替代 Yanki。
扫描 闪卡/ 下所有 .md → 解析 --- 格式（基础卡）或 ~~...~~ 格式（填空卡）→ 转 HTML → 通过 AnkiConnect 同步。
用法: python scripts/sync_flashcards.py
"""

import json, os, re, hashlib, urllib.request, sys
from markdown import markdown
sys.stdout.reconfigure(encoding='utf-8')

ANKI_URL = "http://127.0.0.1:8765"

def _protect_blocks(text, pattern, prefix):
    """保护特殊块，返回 (protected_text, {placeholder: original})"""
    blocks = {}
    counter = [0]
    def save(m):
        counter[0] += 1
        key = f"{prefix}{counter[0]}{prefix}"
        blocks[key] = m.group(0)
        return key
    text = re.sub(pattern, save, text, flags=re.DOTALL)
    return text, blocks

def md_to_html(text):
    """Convert Markdown to HTML while protecting LaTeX $...$ and $$...$$ blocks."""
    # Protect display math first ($$...$$), then inline ($...$)
    text, latex_blocks = _protect_blocks(text, r'\$\$.*?\$\$', 'DMATHBLOCK')
    text2, inline_latex = _protect_blocks(text, r'\$[^$]+?\$', 'IMATHBLOCK')
    # Merge block dictionaries
    latex_blocks.update(inline_latex)
    text = text2
    # Convert remaining Markdown
    html = markdown(text, extensions=['fenced_code', 'tables'])
    # Restore LaTeX
    for key, latex in latex_blocks.items():
        if latex.startswith('$$'):
            content = re.sub(r'(?<!\\)<', r'\\lt ', latex[2:-2])
            html = html.replace(key, r'\[' + content + r'\]')
        else:
            content = re.sub(r'(?<!\\)<', r'\\lt ', latex[1:-1])
            html = html.replace(key, r'\(' + content + r'\)')
    return html

def md_to_html_cloze(text):
    """Convert cloze Markdown to HTML for Anki Cloze model.
    Protects ~~...~~ markers, converts MD → HTML, then replaces ~~...~~ → {{c1::...}}."""
    # Protect cloze markers first (before LaTeX to avoid conflicts)
    text, cloze_blocks = _protect_blocks(text, r'~~((?:[^~]|~(?!~))*)~~', 'CLOZEBLOCK')
    # Then convert remaining markdown (incl. LaTeX)
    text, latex_blocks = _protect_blocks(text, r'\$\$.*?\$\$', 'DMATHBLOCK')
    text2, inline_latex = _protect_blocks(text, r'\$[^$]+?\$', 'IMATHBLOCK')
    latex_blocks.update(inline_latex)
    text = text2
    html = markdown(text, extensions=['fenced_code', 'tables'])
    # Restore LaTeX
    for key, latex in latex_blocks.items():
        if latex.startswith('$$'):
            content = re.sub(r'(?<!\\)<', r'\\lt ', latex[2:-2])
            html = html.replace(key, r'\[' + content + r'\]')
        else:
            content = re.sub(r'(?<!\\)<', r'\\lt ', latex[1:-1])
            html = html.replace(key, r'\(' + content + r'\)')
    # Restore cloze markers → Anki format.
    # - Convert $...$ → \(...\) and $$...$$ → \[...\] (only these render inside {{c1::}})
    # - Insert zero-width space (U+200B) to prevent Anki's cloze parser
    #   from misinterpreting LaTeX }} as cloze terminators.
    for key, cloze in cloze_blocks.items():
        inner = cloze[2:-2]  # strip ~~ markers
        # Convert math delimiters: $$ $$ → \[ \], $ $ → \( \)
        inner, display = _protect_blocks(inner, r'\$\$.*?\$\$', 'DMATH2')
        inner = re.sub(r'\$([^$]+?)\$', r'\\(\1\\)', inner)
        for dk, dv in display.items():
            inner = inner.replace(dk, '\\[' + dv[2:-2] + '\\]')
        # Break }} patterns that would fool Anki's cloze parser
        inner = inner.replace('}}', '}​}')
        html = html.replace(key, '{{c1::' + inner + '}}')
    # Post-process: move cloze outside of LaTeX delimiters.
    # Safety net for $~~X~~$ format → produces \(...{{c1::X}}...\) → fix
    html = _fix_cloze_inside_math(html)
    return html


def _fix_cloze_inside_math(html):
    r"""If {{c1::...}} appears inside \(...\) or \[...\], wrap the entire math block.
    Anki requires cloze to wrap MathJax, not the reverse."""
    result = []
    i = 0
    while i < len(html):
        # Check for inline math \(...\)
        m_start = html.find('\\(', i)
        d_start = html.find('\\[', i)
        # Pick whichever comes first
        if m_start == -1 and d_start == -1:
            result.append(html[i:])
            break
        if m_start == -1 or (d_start != -1 and d_start < m_start):
            # Display math \[...\]
            result.append(html[i:d_start])
            m_end = html.find('\\]', d_start + 2)
            if m_end == -1:
                result.append(html[d_start:])
                break
            inner = html[d_start+2:m_end]
            if '{{c1::' in inner:
                # Strip inner cloze markers (prevent nesting), wrap whole math
                inner = inner.replace('{{c1::', '').replace('}}', '')
                result.append('{{c1::\\[' + inner + '\\]}}')
            else:
                result.append(html[d_start:m_end+2])
            i = m_end + 2
        else:
            # Inline math \(...\)
            result.append(html[i:m_start])
            m_end = html.find('\\)', m_start + 2)
            if m_end == -1:
                result.append(html[m_start:])
                break
            inner = html[m_start+2:m_end]
            if '{{c1::' in inner:
                # Strip inner cloze markers (prevent nesting), wrap whole math
                inner = inner.replace('{{c1::', '').replace('}}', '')
                result.append('{{c1::\\(' + inner + '\\)}}')
            else:
                result.append(html[m_start:m_end+2])
            i = m_end + 2
    return ''.join(result)

# ---- Anki models ----
MODEL_BASIC = "Yanki - Basic"
MODEL_CLOZE = "填空题"
VAULT = r"D:\知识库"
CARD_DIR = os.path.join(VAULT, "闪卡")
STATE_FILE = os.path.join(VAULT, ".obsidian", "flashcards_sync_state.json")

def anki(action, **params):
    data = json.dumps({"action": action, "version": 6, "params": params}, ensure_ascii=False).encode('utf-8')
    return json.loads(urllib.request.urlopen(urllib.request.Request(ANKI_URL, data=data)).read().decode('utf-8'))

# ---- Load state ----
state = json.load(open(STATE_FILE, 'r', encoding='utf-8')) if os.path.exists(STATE_FILE) else {}

def main():
    # ---- Step 1: Scan all card files ----
    cards = {}
    cloze_cards = {}
    for root, dirs, files in os.walk(CARD_DIR):
        for fname in files:
            if not fname.endswith('.md'): continue
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, CARD_DIR).replace("\\", "/")
            parts = rel.split("/")
            deck = "::".join(parts[:-1]) if len(parts) > 1 else "闪卡"

            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            sections = content.split('\n\n---\n\n')

            if len(sections) >= 2:
                # Basic card (Q&A format)
                front_html = md_to_html(sections[0].strip())
                back_html = md_to_html(sections[1].strip())
                fid = hashlib.md5(rel.encode()).hexdigest()[:12]
                cards[fid] = {
                    'rel': rel, 'deck': deck, 'model': MODEL_BASIC,
                    'fields': {'Front': front_html, 'Back': back_html, 'YankiNamespace': rel},
                    'hash': hashlib.md5((front_html + back_html).encode()).hexdigest()
                }
            elif '~~' in content:
                # Cloze card (~~...~~ format, no --- separator)
                text_html = md_to_html_cloze(content.strip())
                fid = hashlib.md5(rel.encode()).hexdigest()[:12]
                cloze_cards[fid] = {
                    'rel': rel, 'deck': deck, 'model': MODEL_CLOZE,
                    'fields': {'文字': text_html},
                    'hash': hashlib.md5(text_html.encode()).hexdigest()
                }

    all_fids = set(cards.keys()) | set(cloze_cards.keys())
    print(f"扫描完成: {len(cards)} 基础卡 + {len(cloze_cards)} 填空卡 = {len(all_fids)} 张")

    # ---- Step 2: Check models exist ----
    r = anki("modelNames")
    if r is None or r.get('result') is None:
        print("  ❌ 无法连接 Anki！请确认 Anki 已打开并进入用户档案（非档案选择界面）。")
        sys.exit(1)
    existing_models = set(r['result'])
    if cloze_cards and MODEL_CLOZE not in existing_models:
        print(f"  ⚠️  Anki 中未找到「{MODEL_CLOZE}」模型，填空卡将无法创建！")
        print(f"     可用模型: {existing_models}")
        print(f"     请在 Anki 中确认 Cloze 笔记类型存在后重试。")
        sys.exit(1)

    # ---- Step 3: Ensure all decks exist ----
    needed = set(c['deck'] for c in list(cards.values()) + list(cloze_cards.values()))
    existing_decks = set(anki("deckNames")['result'])
    for deck in needed - existing_decks:
        anki("createDeck", deck=deck)
        print(f"  创建牌组: {deck}")

    # ---- Step 4: Find existing notes by tag ----
    existing = {}
    all_cards = {**cards, **cloze_cards}
    for batch in [list(all_fids)[i:i+30] for i in range(0, len(all_fids), 30)]:
        query = " OR ".join([f'"tag:fid_{fid}"' for fid in batch])
        try:
            ids = anki("findNotes", query=query)['result']
            for nid in ids:
                info = anki("notesInfo", notes=[nid])['result'][0]
                for tag in info.get('tags', []):
                    if tag.startswith('fid_') and tag[4:] in all_cards:
                        existing[tag[4:]] = nid
                        break
        except Exception as e:
            print(f"  搜索异常: {e}")

    # ---- Step 5: Delete stale notes ----
    for fid, nid in list(existing.items()):
        if fid not in all_cards:
            anki("deleteNotes", notes=[nid])
            print(f"  删除: {state.get(fid, {}).get('rel', fid)}")

    # ---- Step 6: Create or update ----
    created = updated = unchanged = 0
    deleted_stale_model = 0

    for fid, card in all_cards.items():
        deck = card['deck']
        model = card['model']
        fields = card['fields']
        tag = f'fid_{fid}'

        if fid in existing:
            nid = existing[fid]
            info = anki("notesInfo", notes=[nid])['result'][0]
            note_model = info.get('modelName', '')

            # If model changed (e.g. Basic → Cloze), delete and recreate
            if note_model != model:
                anki("deleteNotes", notes=[nid])
                del existing[fid]
                deleted_stale_model += 1
                # Fall through to create
            else:
                if model == MODEL_BASIC:
                    old_front = info['fields']['Front']['value']
                    old_back = info['fields']['Back']['value']
                    if old_front == fields['Front'] and old_back == fields['Back']:
                        unchanged += 1
                        continue
                    anki("updateNoteFields", note={'id': nid, 'fields': fields})
                else:  # Cloze
                    old_text = info['fields']['文字']['value']
                    if old_text == fields['文字']:
                        unchanged += 1
                        continue
                    anki("updateNoteFields", note={'id': nid, 'fields': fields})
                updated += 1
                state[fid] = {'rel': card['rel'], 'deck': deck, 'hash': card['hash']}
                continue

        # Create new note
        result = anki("addNote", note={
            'deckName': deck, 'modelName': model,
            'fields': fields, 'tags': [tag],
        })
        if result.get('error'):
            print(f"  创建失败 [{card['rel']}]: {result['error']}")
        else:
            created += 1

        state[fid] = {'rel': card['rel'], 'deck': deck, 'hash': card['hash']}

    # ---- Save state ----
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

    print(f"\n完成! 创建:{created}  更新:{updated}  未变:{unchanged}  总计:{len(all_cards)}", end='')
    if deleted_stale_model:
        print(f"  (模型变更重建:{deleted_stale_model})", end='')
    print()


if __name__ == "__main__":
    main()
