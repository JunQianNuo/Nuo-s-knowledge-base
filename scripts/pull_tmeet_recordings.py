#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
腾讯会议课堂录音自动拉取与归档脚本
====================================

从腾讯会议拉取录制（课堂/讲座录音）的【逐字稿】与【智能纪要】，
按课表（vault 根目录 课表.md）匹配课程，计算学期第几节，
归档到 课程/<课程名>/课堂笔记/raw/ ，并在 课堂笔记/ 下生成"待润色"占位笔记。

润色环节由 Agent（Claude/Codex）手动触发：读取 raw 逐字稿，生成课堂内容梳理。

用法:
  python scripts/pull_tmeet_recordings.py                 # 默认查最近 7 天
  python scripts/pull_tmeet_recordings.py --days 3        # 最近 3 天
  python scripts/pull_tmeet_recordings.py --start 2026-09-01 --end 2026-09-07
  python scripts/pull_tmeet_recordings.py --dry-run       # 只列出待处理项，不下载
  python scripts/pull_tmeet_recordings.py --force         # 已存在的记录也重新下载
  python scripts/pull_tmeet_recordings.py --no-archive-unmatched  # 未匹配课表的会议跳过下载

依赖: tmeet CLI（npm i -g @tencentcloud/tmeet）已登录（tmeet auth status 确认）。
"""

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

FROZEN = getattr(sys, 'frozen', False)  # PyInstaller 打包后为 True

def default_vault():
    """知识库根目录：exe 模式 = exe 所在目录；脚本模式 = 脚本上级目录。"""
    if FROZEN:
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VAULT = default_vault()
TIMETABLE_PATH = os.path.join(VAULT, '课表.md')
NOTEBOOK_DIR = '课堂笔记'   # 每门课程下的课堂笔记目录
RAW_DIR = 'raw'            # 原始逐字稿/纪要存档子目录
UNMATCHED_DIR = os.path.join(VAULT, '未命名', '课堂录音')  # 未匹配课表的会议归档处
LOG_PATH = os.path.join(VAULT, 'tmp', 'tmeet_sync.log')   # 运行日志
SCHED_TASK_NAME = 'TmeetRecordingSync'                    # Windows 计划任务名

def set_vault(path):
    """--vault 覆盖知识库根目录（连带更新依赖路径）。"""
    global VAULT, TIMETABLE_PATH, UNMATCHED_DIR, LOG_PATH
    VAULT = os.path.abspath(path)
    TIMETABLE_PATH = os.path.join(VAULT, '课表.md')
    UNMATCHED_DIR = os.path.join(VAULT, '未命名', '课堂录音')
    LOG_PATH = os.path.join(VAULT, 'tmp', 'tmeet_sync.log')


class Tee:
    """同时输出到终端与日志文件。"""
    def __init__(self, stream, logfile):
        self.stream, self.logfile = stream, logfile
    def write(self, s):
        self.stream.write(s)
        self.logfile.write(s)
    def flush(self):
        self.stream.flush()
        self.logfile.flush()

WEEKDAY_MAP = {'一': 0, '二': 1, '三': 2, '四': 3, '五': 4, '六': 5, '日': 6,
               '天': 6, '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6}

TM_WINDOW_BEFORE = dt.timedelta(minutes=30)   # 会议开始时间允许早于课表开始的最大提前量
TM_WINDOW_AFTER = dt.timedelta(minutes=45)    # 会议开始时间允许晚于课表开始的窗口（课后开录）


# ---------------------------------------------------------------- tmeet 调用

def tmeet(*args, timeout=180):
    """调用 tmeet CLI，返回解析后的 JSON。失败抛 RuntimeError。"""
    cmd = ['tmeet', *args]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              encoding='utf-8', errors='replace',
                              timeout=timeout, shell=True)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f'tmeet 超时: {" ".join(args[:3])}...')
    out = (proc.stdout or '') + (proc.stderr or '')
    if proc.returncode != 0:
        raise RuntimeError(f'tmeet 失败({proc.returncode}): {out.strip()[:800]}')
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        raise RuntimeError(f'tmeet 输出非 JSON: {out.strip()[:800]}')


def _err_code(data):
    """业务错误码（data.code 非 0 视为业务错误）。"""
    d = data.get('data') or {}
    return d.get('code')


# ---------------------------------------------------------------- 课表解析

def parse_weeks(text):
    """解析周次描述，如 '1-16' '1-8单' '2-16双' '1,3,5' '3-17' → [(start, end, parity)]。
    parity: None=每周, 'odd'=单周, 'even'=双周。"""
    out = []
    for part in re.split(r'[,，、]', text.strip()):
        part = part.strip()
        if not part:
            continue
        parity = None
        if part.endswith('单'):
            parity = 'odd'
            part = part[:-1]
        elif part.endswith('双'):
            parity = 'even'
            part = part[:-1]
        m = re.match(r'^(\d+)\s*[-~至]\s*(\d+)$', part)
        if m:
            out.append((int(m.group(1)), int(m.group(2)), parity))
        elif re.match(r'^\d+$', part):
            n = int(part)
            out.append((n, n, parity))
        else:
            print(f'  [警告] 无法解析周次描述: {text!r}')
    return out


def parse_time_range(text):
    """'10:00-11:40' → (datetime.time, datetime.time)，解析失败返回 None。"""
    m = re.match(r'^(\d{1,2}):(\d{2})\s*[-~至]\s*(\d{1,2}):(\d{2})$', text.strip())
    if not m:
        return None
    try:
        return (dt.time(int(m.group(1)), int(m.group(2))),
                dt.time(int(m.group(3)), int(m.group(4))))
    except ValueError:
        return None


def load_timetable(path=None):
    """解析 课表.md → {courses: [...], semester_start: date, semester: str}。"""
    path = path or TIMETABLE_PATH
    if not os.path.isfile(path):
        return None
    with open(path, encoding='utf-8') as f:
        text = f.read()

    fm = re.search(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    meta = {}
    if fm:
        for line in fm.group(1).splitlines():
            m = re.match(r'^\s*([^:#]+?)\s*:\s*(.+?)\s*$', line)
            if m:
                meta[m.group(1).strip()] = m.group(2).strip()

    semester_start = None
    try:
        semester_start = dt.date.fromisoformat(meta.get('开学日期', ''))
    except ValueError:
        print(f'  [警告] 课表 frontmatter 缺少有效 开学日期，将无法计算学期周次')

    courses = []
    # 表格行：| 课程 | 星期 | 节次 | 时间段 | 周次 | 会议号 | 教师 |
    for row in re.findall(r'^\|(.+)\|\s*$', text, re.MULTILINE):
        cells = [c.strip() for c in row.split('|')]
        # row 以 | 开头结尾，split 后首尾各有一个空串；中间空单元格必须保留（占位）
        if cells and cells[0] == '':
            cells = cells[1:]
        if cells and cells[-1] == '':
            cells = cells[:-1]
        if not cells or all(re.match(r'^:?-+:?$', c) for c in cells):
            continue  # 表头分隔行
        if len(cells) < 5 or cells[0].startswith('课程') or cells[0].startswith('---'):
            continue
        course = cells[0]
        weekday = WEEKDAY_MAP.get(cells[1][:1])
        time_range = parse_time_range(cells[3]) if len(cells) > 3 else None
        weeks = parse_weeks(cells[4]) if len(cells) > 4 else []
        meeting_code = cells[5] if len(cells) > 5 else ''
        teacher = cells[6] if len(cells) > 6 else ''
        if course and weekday is not None and weeks:
            courses.append({
                'course': course,
                'weekday': weekday,
                'start': time_range[0] if time_range else None,
                'end': time_range[1] if time_range else None,
                'weeks': weeks,
                'meeting_code': meeting_code,
                'teacher': teacher,
            })
        elif course and weekday is not None:
            print(f'  [警告] 课表行解析不完整，已跳过: {row[:60]}')
    excluded = [s.strip() for s in re.split(r'[,，、]', meta.get('排除主题', '')) if s.strip()]
    # 调休：某些日期按其他星期的课表上课（如国庆调休 10/10 补周三课）
    # 写法：调休: 2026-10-10=三, 2026-09-26=四
    makeup = {}
    for item in re.split(r'[,，、;；]', meta.get('调休', '')):
        item = item.strip()
        if not item:
            continue
        m = re.match(r'^(\d{4}-\d{2}-\d{2})\s*[=:：]\s*周?([一二三四五六日天1-7])$', item)
        if m and WEEKDAY_MAP.get(m.group(2)) is not None:
            makeup[m.group(1)] = WEEKDAY_MAP[m.group(2)]
        else:
            print(f'  [警告] 无法解析调休配置: {item!r}（应形如 2026-10-10=三）')
    return {'semester': meta.get('学期', ''), 'semester_start': semester_start,
            'courses': courses, 'excluded_subjects': excluded, 'makeup': makeup}


def week_no(date, semester_start):
    """开学日期所在周为第 1 周。"""
    if semester_start is None:
        return None
    return (date - semester_start).days // 7 + 1


def in_weeks(week, weeks):
    for s, e, parity in weeks:
        if s <= week <= e:
            if parity is None:
                return True
            if parity == 'odd' and week % 2 == 1:
                return True
            if parity == 'even' and week % 2 == 0:
                return True
    return False


def class_no_for(course_row, date, timetable):
    """学期第几节 = 开学以来（含当日）该课程实际排课次数（支持一周多次）。"""
    semester_start = timetable['semester_start']
    if semester_start is None:
        return None
    rows = [c for c in timetable['courses'] if c['course'] == course_row['course']]
    count = 0
    w_now = week_no(date, semester_start)
    for r in rows:
        for k in range(1, w_now + 1):
            if not in_weeks(k, r['weeks']):
                continue
            # 第 k 周中该行星期对应的具体日期
            d = semester_start + dt.timedelta(
                days=(k - 1) * 7 + (r['weekday'] - semester_start.weekday()) % 7)
            if d <= date:
                count += 1
    return count


def match_course(meeting_dt, timetable):
    """按 星期 + 时间段 + 周次 + 会议号 匹配课表课程。
    支持调休映射（某日按其他星期的课表上课）。
    返回 (课程名, 学期第几节) 或 (None, None)。"""
    if not timetable:
        return None, None
    date = meeting_dt.date()
    # 调休日：用配置的星期替代实际星期
    weekday = (timetable.get('makeup') or {}).get(date.isoformat())
    if weekday is None:
        weekday = date.weekday()
    w = week_no(date, timetable['semester_start'])
    if w is None:
        return None, None
    t = meeting_dt.time()
    cands = []
    for c in timetable['courses']:
        if c['weekday'] != weekday or not in_weeks(w, c['weeks']):
            continue
        if c['start'] is not None and c['end'] is not None:
            tz = meeting_dt.tzinfo  # 会议时间为 +08:00 aware
            start = dt.datetime.combine(date, c['start'], tzinfo=tz)
            end = dt.datetime.combine(date, c['end'], tzinfo=tz)
            if not (start - TM_WINDOW_BEFORE <= meeting_dt <= end + TM_WINDOW_AFTER):
                continue
        cands.append(c)
    if not cands:
        return None, None
    # 会议号强匹配优先
    for c in cands:
        if c['meeting_code']:
            return c['course'], class_no_for(c, date, timetable)
    # 多个候选（如相邻课程）时，选会议开始时间与课程开始时间最接近的
    best = min(cands, key=lambda c: abs(
        (meeting_dt - dt.datetime.combine(date, c['start'], tzinfo=meeting_dt.tzinfo)).total_seconds()))
    return best['course'], class_no_for(best, date, timetable)


# ---------------------------------------------------------------- 文本整理

def clean_filename(s, maxlen=60):
    s = re.sub(r'[\\/:*?"<>|\r\n\t]+', '_', s).strip(' ._')
    return s[:maxlen] if len(s) > maxlen else s


def fmt_ts(mmss):
    """'01:56' / '01:00:12' → '00:01:56' / '01:00:12'"""
    parts = mmss.split(':')
    parts = ['0'] * (3 - len(parts)) + parts
    return ':'.join(parts)


def build_transcript(record_file_id, meeting_id=None):
    """分页拉取逐字稿 → (markdown 文本, 段落数)。
    部分录制类型（如"音频录制"）不支持 --pid/--limit 分页（带参返回空），
    此时自动降级为不带分页参数拉取全文。"""
    paragraphs = []
    pid = '0'
    limit = 50
    guard = 0
    while True:
        guard += 1
        if guard > 500:
            raise RuntimeError('逐字稿分页超过 500 次，疑似死循环')
        args = ['record', 'transcript-get', '--record-file-id', record_file_id,
                '--pid', pid, '--limit', str(limit)]
        if meeting_id:
            args += ['--meeting-id', meeting_id]
        data = tmeet(*args, timeout=300)
        if _err_code(data) not in (None, 0):
            raise RuntimeError(f'transcript-get 业务错误 code={_err_code(data)}')
        minutes = (data.get('data') or {}).get('minutes') or {}
        paras = minutes.get('paragraphs') or []
        if not paras:
            break
        paragraphs.extend(paras)
        # 服务端 more 字段不稳定（末页可能缺失），以"不足一页"作为终止条件
        if len(paras) < limit:
            break
        pid = str(int(paras[-1]['pid']) + 1)

    if not paragraphs:
        # 降级：不带分页参数拉全文（部分录制类型不支持 pid/limit 分页）
        print('    [提示] 分页拉取无内容，改用全文模式重试…')
        args = ['record', 'transcript-get', '--record-file-id', record_file_id]
        if meeting_id:
            args += ['--meeting-id', meeting_id]
        data = tmeet(*args, timeout=600)
        if _err_code(data) not in (None, 0):
            raise RuntimeError(f'transcript-get 业务错误 code={_err_code(data)}')
        minutes = (data.get('data') or {}).get('minutes') or {}
        paragraphs = minutes.get('paragraphs') or []

    lines = []
    for p in paragraphs:
        speaker = ((p.get('speaker') or {}).get('user_name') or '').strip()
        text = ''.join(
            w.get('text', '')
            for s in (p.get('sentences') or [])
            for w in (s.get('words') or [])
        )
        text = text.strip()
        if not text:
            continue
        ts = f"[{fmt_ts(p.get('start_time', ''))}]" if p.get('start_time') else ''
        if speaker:
            lines.append(f'**{speaker}**{ts}：{text}')
        else:
            lines.append(f'{ts} {text}')
    return '\n\n'.join(lines), len(paragraphs)


def fetch_minutes(record_file_id):
    """拉取智能纪要 → markdown 文本。"""
    data = tmeet('record', 'smart-minutes', '--record-file-id', record_file_id,
                 '--lang', 'zh', timeout=300)
    if _err_code(data) not in (None, 0):
        raise RuntimeError(f'smart-minutes 业务错误 code={_err_code(data)}')
    minute = ((data.get('data') or {}).get('meeting_minute') or {}).get('minute') or ''
    return minute.strip()


# ---------------------------------------------------------------- 归档

def raw_md_path(note_dir, date_str, subject, kind, rf_suffix=''):
    """kind: 逐字稿 / 纪要；rf_suffix 为 record_file_id 后 6 位，避免同日同名会议冲突"""
    tag = f'-{rf_suffix}' if rf_suffix else ''
    return os.path.join(note_dir, RAW_DIR, f'{date_str}-{clean_filename(subject)}{tag}-{kind}.md')


def ensure_dir(p):
    os.makedirs(p, exist_ok=True)


def cleanup_unmatched_copy(date_str, subject, rf_suffix):
    """素材已归位课程目录后，清理"未匹配"区里同一录制的旧副本。"""
    removed = []
    for kind in ('逐字稿', '纪要'):
        stale = raw_md_path(UNMATCHED_DIR, date_str, subject, kind, rf_suffix)
        if os.path.exists(stale):
            try:
                os.remove(stale)
                removed.append(os.path.basename(stale))
            except OSError:
                pass
    if removed:
        print(f'    [清理] 已归位课程，删除未匹配区旧副本：{"、".join(removed)}')


PLACEHOLDER_NAME = re.compile(r'^(\d{4}-\d{2}-\d{2})-第(\d+)节-(.+)\.md$')


def _list_placeholders(note_dir):
    """列出 课堂笔记/ 下的占位/梳理笔记（不含 README），按文件名排序。
    返回 [(date_str, class_no_str, subject, path)]"""
    out = []
    try:
        names = os.listdir(note_dir)
    except OSError:
        return out
    for name in sorted(names):
        m = PLACEHOLDER_NAME.match(name)
        if m:
            out.append((m.group(1), m.group(2), m.group(3),
                        os.path.join(note_dir, name)))
    return out


def _read_status(path):
    try:
        text = open(path, encoding='utf-8').read()
    except OSError:
        return ''
    m = re.search(r'^status:\s*(.+?)\s*$', text, re.MULTILINE)
    return m.group(1).strip() if m else ''


def _insert_material(text, add_lines):
    """把素材行插入「课堂内容梳理」小节之前（保持占位笔记结构）。"""
    marker = '\n## 课堂内容梳理\n'
    block = ''.join(add_lines)
    if not block.endswith('\n'):
        block += '\n'
    if marker in text:
        return text.replace(marker, block + marker, 1)
    return text.rstrip() + '\n\n' + block


def write_placeholder(note_dir, date_str, class_no, course, subject, meeting_code,
                      transcript_rel, minutes_rel, start_time):
    """生成待润色占位笔记。
    同一节课（同课程同日同节次）已有占位笔记时，只追加素材链接（多段录音合并）。"""
    # 同节次已有占位 → 追加本段素材（不新建第二份）
    for d, c, subj, path in _list_placeholders(note_dir):
        if d == date_str and c == str(class_no):
            with open(path, encoding='utf-8') as f:
                old = f.read()
            if transcript_rel not in old:
                add = f'- 补充素材（本课另一段录音「{subj}」）：[[{transcript_rel}]]、[[{minutes_rel}]]\n'
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(_insert_material(old, [add]))
            return path
    fname = f'{date_str}-第{class_no}节-{clean_filename(course)}.md'
    if subject and subject != course:
        fname = f'{date_str}-第{class_no}节-{clean_filename(subject)}.md'
    path = os.path.join(note_dir, fname)
    content = f'''---
title: {date_str} 第{class_no}节 {course}
subject: {course}
class_no: {class_no}
date: {date_str}
source: 腾讯会议录制（{subject}）
meeting_code: {meeting_code}
start_time: {start_time}
status: 待润色
topics:
  - （待整理）
---

# {date_str} 第{class_no}节 {course}

> [!info] 待润色
> 本节课录音已自动归档，原始素材见下方链接。请由 Agent 读取逐字稿与纪要后，
> 润色生成本次课堂内容梳理（按 [[规范/课程笔记生成规范|课程笔记生成规范]] 组织）。

- 原始逐字稿：[[{transcript_rel}]]
- 智能纪要：[[{minutes_rel}]]
- 会议号：{meeting_code}｜开始时间：{start_time}

## 课堂内容梳理

（待润色）
'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path


NOISE_SUBJECT = ('录音文件', '快速会议', 'ASR', '测试', '转写_', '未命名')


def _subject_noise(subj):
    """主题命名噪声分（越高越像自动生成的泛化命名）。"""
    return sum(1 for n in NOISE_SUBJECT if n in (subj or ''))


def consolidate_placeholders(note_dir):
    """合并同节课（同日期同节次）的多份【待润色】占位笔记为一份（素材链接汇总）。
    主文件优先保留主题最有意义的；任一文件已被人工处理（status 非"待润色"）时不合并。"""
    groups = {}
    for d, c, subj, path in _list_placeholders(note_dir):
        groups.setdefault((d, c), []).append((path, subj))
    merged_any = False
    for (d, c), items in groups.items():
        if len(items) < 2:
            continue
        if any(_read_status(p) != '待润色' for p, _ in items):
            continue
        # 主文件：噪声分低者优先（主题有意义），其次最早创建
        items.sort(key=lambda x: (_subject_noise(x[1]), os.path.getmtime(x[0])))
        main_path, main_subj = items[0]
        with open(main_path, encoding='utf-8') as f:
            main_text = f.read()
        add_lines = []
        for other_path, other_subj in items[1:]:
            try:
                with open(other_path, encoding='utf-8') as f:
                    text = f.read()
            except OSError:
                continue
            for line in re.findall(r'(?m)^- (?:原始逐字稿|智能纪要|补充素材).*$', text):
                if line not in main_text and line not in add_lines:
                    add_lines.append(line + '\n')
            add_lines.append(f'- 另段录音主题：{other_subj}\n')
            os.remove(other_path)
        if add_lines:
            with open(main_path, 'w', encoding='utf-8') as f:
                f.write(_insert_material(main_text, add_lines))
        merged_any = True
        print(f'    [合并] {d} 第{int(c)}节：{len(items)} 段录音占位已合并 → {os.path.basename(main_path)}')
    return merged_any


def rebuild_readme(note_dir, course):
    """从课堂笔记目录的占位/梳理文件重建 README 索引（反映实际状态）。"""
    entries = []
    for d, c, subj, path in _list_placeholders(note_dir):
        status = _read_status(path) or '待润色'
        entries.append((d, f'第{int(c)}节', subj, status))
    entries = sorted(set(entries), key=lambda e: (e[0], int(e[1].strip('第节'))))
    header = (f'# {course} 课堂笔记\n\n'
              f'> 由 `scripts/pull_tmeet_recordings.py` 自动维护：每节课的逐字稿/纪要归档在 '
              f'`raw/`，梳理笔记以 `YYYY-MM-DD-第N节-*.md` 命名（status: 待润色 表示尚未润色）。\n\n'
              f'## 课程记录\n\n| 日期 | 节次 | 主题 | 状态 |\n|:--|:--|:--|:--|\n')
    with open(os.path.join(note_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(header + ''.join(f'| {d} | {c} | {subj} | {st} |\n'
                                 for d, c, subj, st in entries))
    return entries


# ---------------------------------------------------------------- 计划任务

def _schtasks(args_list, timeout=60):
    """调用 schtasks（Windows 计划任务管理），返回 (returncode, output)。"""
    sch = shutil.which('schtasks') or 'schtasks'
    proc = subprocess.run([sch, *args_list], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', timeout=timeout)
    out = (proc.stdout or '') + (proc.stderr or '')
    return proc.returncode, out


def _sched_target():
    """计划任务要运行的目标命令（exe 模式用 exe；脚本模式用 python + 脚本）。"""
    if FROZEN:
        exe = os.path.abspath(sys.executable)
        return f'"{exe}" --days 2 --vault "{VAULT}"'
    py = shutil.which('python') or sys.executable
    return f'"{py}" "{os.path.abspath(__file__)}" --days 2 --vault "{VAULT}"'


def install_schedule(time_str):
    """注册每日定时拉取计划任务。time_str: HH:MM（默认 19:30）。"""
    time_str = time_str or '19:30'
    if not re.match(r'^([01]?\d|2[0-3]):[0-5]\d$', time_str):
        raise SystemExit(f'时间格式错误: {time_str!r}（应为 HH:MM，如 19:30）')
    target = _sched_target()
    print(f'注册计划任务 {SCHED_TASK_NAME}：每天 {time_str} 运行')
    print(f'  命令: {target}')
    rc, out = _schtasks(['/Create', '/TN', SCHED_TASK_NAME, '/F',
                         '/SC', 'DAILY', '/ST', time_str, '/TR', target])
    if rc == 0:
        print('✅ 已注册。可运行 --query-schedule 查看状态，--remove-schedule 删除。')
    else:
        print(f'❌ 注册失败: {out.strip()[:400]}')
        raise SystemExit(1)


def remove_schedule():
    """删除定时拉取计划任务。"""
    print(f'删除计划任务 {SCHED_TASK_NAME} …')
    rc, out = _schtasks(['/Delete', '/TN', SCHED_TASK_NAME, '/F'])
    if rc == 0:
        print('✅ 已删除。')
    else:
        print(f'ℹ️ 任务不存在或删除失败: {out.strip()[:300]}')


def query_schedule():
    """查询计划任务状态。"""
    rc, out = _schtasks(['/Query', '/TN', SCHED_TASK_NAME, '/FO', 'LIST', '/V'])
    if rc != 0:
        print(f'ℹ️ 计划任务 {SCHED_TASK_NAME} 未注册。注册命令: --install-schedule HH:MM')
        return
    keep = ('TaskName', '任务名', 'Status', '状态', 'Next Run Time', '下次运行时间',
            'Last Run Time', '上次运行时间', 'Last Result', '上次结果',
            'Task To Run', '要运行的任务', 'Schedule Type', '计划类型')
    for line in out.splitlines():
        if any(k in line for k in keep):
            print(' ', line.strip())


def main():
    ap = argparse.ArgumentParser(description='腾讯会议课堂录音拉取与归档')
    ap.add_argument('--days', type=int, default=7, help='查询最近 N 天（默认 7）')
    ap.add_argument('--start', help='开始日期 YYYY-MM-DD')
    ap.add_argument('--end', help='结束日期 YYYY-MM-DD')
    ap.add_argument('--dry-run', action='store_true', help='只列出待处理项，不下载')
    ap.add_argument('--force', action='store_true', help='已存在的记录也重新下载')
    ap.add_argument('--no-archive-unmatched', action='store_true',
                    help='未匹配课表的会议跳过（默认归档到 未命名/课堂录音/）')
    ap.add_argument('--vault', help='知识库根目录（默认：exe 所在目录或脚本上级目录）')
    ap.add_argument('--install-schedule', nargs='?', const='19:30', metavar='HH:MM',
                    help='注册每日定时拉取计划任务（默认 19:30）')
    ap.add_argument('--remove-schedule', action='store_true', help='删除定时拉取计划任务')
    ap.add_argument('--query-schedule', action='store_true', help='查询计划任务状态')
    ap.add_argument('--ui', nargs='?', const=8766, type=int, metavar='PORT',
                    help='启动本地操作界面（Web，默认端口 8766，自动打开浏览器）')
    args = ap.parse_args()

    if args.vault:
        set_vault(args.vault)

    # exe 无参数运行时（如双击）默认进入操作界面；显式给出拉取/定时参数时按命令执行
    has_pull_args = (args.days != 7 or args.start or args.end or args.dry_run
                     or args.force or args.no_archive_unmatched
                     or args.install_schedule or args.remove_schedule
                     or args.query_schedule)
    if args.ui or (FROZEN and not has_pull_args):
        try:
            from recording_ui import run_ui
            run_ui(args.ui, vault=args.vault)
        except ImportError:
            ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recording_ui.py')
            if os.path.isfile(ui_path):
                sys.path.insert(0, os.path.dirname(ui_path))
                from recording_ui import run_ui
                run_ui(args.ui, vault=args.vault)
            else:
                raise SystemExit('未找到 scripts/recording_ui.py（界面模块）')
        return

    if args.install_schedule:
        install_schedule(args.install_schedule)
        return
    if args.remove_schedule:
        remove_schedule()
        return
    if args.query_schedule:
        query_schedule()
        return

    # 运行日志（--dry-run 除外）
    if not args.dry_run:
        try:
            os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
            logf = open(LOG_PATH, 'a', encoding='utf-8')
            logf.write(f'\n===== {dt.datetime.now():%Y-%m-%d %H:%M:%S} =====\n')
            sys.stdout = Tee(sys.stdout, logf)
            sys.stderr = Tee(sys.stderr, logf)
        except OSError as e:
            print(f'  [提示] 日志文件不可写: {e}')

    if args.start or args.end:
        start = dt.date.fromisoformat(args.start) if args.start else None
        end = dt.date.fromisoformat(args.end) if args.end else None
        start = start or end
        end = end or start
    else:
        end = dt.date.today()
        start = end - dt.timedelta(days=args.days - 1)

    print(f'== 查询录制 {start} ~ {end} ==')
    timetable = load_timetable()
    if timetable:
        print(f'   课表已加载：{timetable["semester"]}（开学 {timetable["semester_start"]}，'
              f'{len(timetable["courses"])} 门课）')
    else:
        print('   [提示] 未找到 课表.md（vault 根目录），全部会议将按"未匹配课表"处理')

    # 1. 拉取录制列表（分页）
    meetings = []
    token = ''
    while True:
        args_list = ['record', 'list',
                     '--start', f'{start}T00:00:00+08:00',
                     '--end', f'{end}T23:59:59+08:00', '--compact']
        if token:
            args_list += ['--page-token', token]
        data = tmeet(*args_list)
        d = data.get('data') or {}
        meetings.extend(d.get('record_meetings') or [])
        token = d.get('next_page_token') or ''
        if not token or not d.get('has_more'):
            break
    print(f'   共 {len(meetings)} 条录制记录')

    if not meetings:
        print('   无新录制。')
        return

    todo = []
    excluded = (timetable or {}).get('excluded_subjects') or []
    for m in meetings:
        start_dt = m.get('media_start_time', '')
        subject = (m.get('subject') or '').strip() or '未命名会议'
        if any(ex in subject for ex in excluded):
            print(f'  [跳过] {start_dt[:10]} {subject}：命中课表"排除主题"')
            continue
        for rf in m.get('record_files') or []:
            todo.append({
                'meeting': m,
                'record_file_id': rf.get('record_file_id'),
                'rf_start': rf.get('record_start_time'),
                'rf_end': rf.get('record_end_time'),
                'subject': subject,
                'meeting_record_id': m.get('meeting_record_id'),
                'meeting_id': m.get('meeting_id'),
                'meeting_code': m.get('meeting_code'),
                'start_dt': start_dt,
            })
    todo.sort(key=lambda t: t['start_dt'])

    processed = []
    for t in todo:
        start_dt = t['start_dt']
        date_str = start_dt[:10] if start_dt else 'unknown'
        meeting_dt = dt.datetime.fromisoformat(start_dt) if start_dt else None
        subject = t['subject']

        course, class_no = (None, None)
        if meeting_dt:
            course, class_no = match_course(meeting_dt, timetable)

        if course:
            note_dir = os.path.join(VAULT, '课程', course, NOTEBOOK_DIR)
            label = f'{course}（第{class_no}节）'
        else:
            note_dir = UNMATCHED_DIR
            label = '未匹配课表'
            if args.no_archive_unmatched:
                print(f'  [跳过] {date_str} {subject}：未匹配课表（--no-archive-unmatched）')
                continue

        print(f'  [处理] {date_str} {label} {subject}')
        print(f'          会议号 {t["meeting_code"]}，录制 {t["record_file_id"]}')

        if args.dry_run:
            continue

        ensure_dir(os.path.join(note_dir, RAW_DIR))
        rf_suffix = (t['record_file_id'] or '')[-6:]
        tpath = raw_md_path(note_dir, date_str, subject, '逐字稿', rf_suffix)
        mpath = raw_md_path(note_dir, date_str, subject, '纪要', rf_suffix)
        exists = os.path.exists(tpath) and os.path.exists(mpath)
        if exists and not args.force:
            print(f'  [已存在] {date_str} {label} {subject}（{t["record_file_id"]}）')
            if course:
                cleanup_unmatched_copy(date_str, subject, rf_suffix)
            continue

        # 2. 拉取纪要
        try:
            minute_text = fetch_minutes(t['record_file_id'])
        except Exception as e:
            print(f'    [错误] 纪要拉取失败: {e}')
            minute_text = ''
        # 3. 拉取逐字稿
        try:
            transcript, npara = build_transcript(t['record_file_id'], t['meeting_id'])
        except Exception as e:
            print(f'    [错误] 逐字稿拉取失败: {e}')
            transcript = ''
            npara = 0

        # 4. 落盘（转写/纪要未生成时【不落盘】，下次运行自动重试，避免空白文件永久占位）
        wrote_any = False
        if transcript:
            with open(tpath, 'w', encoding='utf-8') as f:
                f.write(f'# 逐字稿：{subject}\n\n'
                        f'> 会议号：{t["meeting_code"]}｜录制文件：{t["record_file_id"]}｜'
                        f'会议时间：{start_dt}\n\n'
                        f'---\n\n{transcript}\n')
            print(f'    [存档] 逐字稿 {npara} 段 → {os.path.relpath(tpath, VAULT)}')
            wrote_any = True
        else:
            print('    [警告] 逐字稿暂为空（转写可能尚未完成）→ 未生成文件，下次运行将自动重试')
        if minute_text:
            with open(mpath, 'w', encoding='utf-8') as f:
                f.write(f'# 智能纪要：{subject}\n\n'
                        f'> 会议号：{t["meeting_code"]}｜录制文件：{t["record_file_id"]}｜'
                        f'会议时间：{start_dt}\n\n'
                        f'---\n\n{minute_text}\n')
            print(f'    [存档] 纪要 → {os.path.relpath(mpath, VAULT)}')
            wrote_any = True
        else:
            print('    [警告] 智能纪要暂未生成 → 未生成文件，下次运行将自动重试')

        # 5. 生成待润色占位笔记（至少一个素材落盘时）
        if course and class_no and wrote_any:
            placeholder = write_placeholder(
                note_dir, date_str, class_no, course, subject,
                t['meeting_code'],
                f'{RAW_DIR}/{os.path.basename(tpath)}',
                f'{RAW_DIR}/{os.path.basename(mpath)}',
                start_dt)
            print(f'    [占位] {os.path.relpath(placeholder, VAULT)}')
            processed.append((course, date_str, f'第{class_no}节', subject, '待润色'))
            # 素材已归位课程目录：清理"未匹配"区里同一录制的旧副本
            cleanup_unmatched_copy(date_str, subject, rf_suffix)

    if not args.dry_run:
        # 收尾：合并同节课多段录音的占位笔记 + 按文件实际状态重建 README（全部课程）
        for course in {x['course'] for x in (timetable['courses'] if timetable else [])}:
            note_dir = os.path.join(VAULT, '课程', course, NOTEBOOK_DIR)
            if not os.path.isdir(note_dir):
                continue
            consolidate_placeholders(note_dir)
            rebuild_readme(note_dir, course)
    else:
        print('\n[dry-run] 以上为待处理项，未执行下载。')


if __name__ == '__main__':
    main()
