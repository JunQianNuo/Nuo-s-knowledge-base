# -*- coding: utf-8 -*-
"""
课堂录音归档 - 本地操作界面（Web UI）
======================================

提供浏览器界面：
- 定时拉取时间设置（注册/修改/删除 Windows 计划任务）
- 课表可视化编辑（增删改课程行、学期/开学日期/排除主题）
- 立即拉取一次 + 查看运行日志

由主程序 `--ui` 参数启动，零第三方依赖（标准库 http.server）。
"""

import json
import os
import re
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.stdout.reconfigure(encoding='utf-8')

try:
    import pull_tmeet_recordings as core
except ImportError:
    # 兼容从 scripts/ 目录直接运行
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import pull_tmeet_recordings as core

DEFAULT_PORT = 8766


# ---------------------------------------------------------------- 数据读写

def read_timetable():
    """读取 课表.md → {meta: {...}, rows: [...]}（原始单元格文本，供 UI 编辑）。"""
    text = core.timetable_text(core.TIMETABLE_PATH)
    fm = re.search(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    meta = {}
    if fm:
        for line in fm.group(1).splitlines():
            m = re.match(r'^\s*([^:#]+?)\s*:\s*(.*?)\s*$', line)
            if m:
                meta[m.group(1).strip()] = m.group(2).strip()
    rows = []
    for row in re.findall(r'^\|(.+)\|\s*$', text, re.MULTILINE):
        cells = [c.strip() for c in row.split('|')]
        if cells and cells[0] == '':
            cells = cells[1:]
        if cells and cells[-1] == '':
            cells = cells[:-1]
        if len(cells) < 5 or cells[0] in ('课程',) or cells[0].startswith('---') \
                or all(re.match(r'^:?-+:?$', c) for c in cells):
            continue
        rows.append({
            'course': cells[0],
            'weekday': cells[1] if len(cells) > 1 else '',
            'slots': cells[2] if len(cells) > 2 else '',
            'time_range': cells[3] if len(cells) > 3 else '',
            'weeks': cells[4] if len(cells) > 4 else '',
            'meeting_code': cells[5] if len(cells) > 5 else '',
            'teacher': cells[6] if len(cells) > 6 else '',
        })
    return {'meta': meta, 'rows': rows, 'path': core.TIMETABLE_PATH}


def save_timetable(meta, rows):
    """写回 课表.md。meta: {学期, 开学日期, 排除主题}；rows: 课程行 dict 列表。"""
    if core.TIMETABLE_PATH.endswith('学期设置.md'):
        from pathlib import Path
        import yaml
        target, folder = core.timetable_locations(core.TIMETABLE_PATH)
        # Preserve unknown settings and note bodies when updating known fields.
        previous = target.read_text(encoding='utf-8').split('---', 2)
        settings = yaml.safe_load(previous[1]) or {}
        settings.update(meta or {})
        def frontmatter(data, body=''):
            return '---\n' + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + '---' + body
        pending = {target: frontmatter(settings, previous[2])}
        if target.parent.name == '学期设置' and str(settings.get('学期')) != target.stem:
            raise ValueError('请新建学期目录及配置后，通过当前学期设置切换；不能直接改名覆盖旧学期。')
        existing = {}
        for note in folder.glob('*.md'):
            parts = note.read_text(encoding='utf-8').split('---', 2)
            record = yaml.safe_load(parts[1]) or {}
            existing[int(record.get('排序', 0))] = (note, record, parts[2])
        names = ['课程', '星期', '节次', '时间段', '周次', '会议号', '教师']
        keys = ['course', 'weekday', 'slots', 'time_range', 'weeks', 'meeting_code', 'teacher']
        for i, row in enumerate(rows, 1):
            note, data, body = existing.get(i, (folder / f'{i:02d}-课程.md', {}, '\n'))
            data.update({name: str(row.get(key, '') or '') for name, key in zip(names, keys)})
            data['排序'] = i
            if target.parent.name == '学期设置':
                data['学期'] = target.stem
            pending[note] = frontmatter(data, body)
        # Archive removed rows outside the Base filter, retaining their note bodies.
        for i, (note, _, _) in existing.items():
            if i > len(rows):
                archive = folder.parent.parent / '历史课程' / folder.name
                archive.mkdir(parents=True, exist_ok=True)
                destination = archive / note.name
                if destination.exists():
                    raise FileExistsError(destination)
                note.rename(destination)
        for note, content in pending.items():
            note.parent.mkdir(parents=True, exist_ok=True)
            note.write_text(content, encoding='utf-8')
        return core.TIMETABLE_PATH
    semester = (meta or {}).get('学期') or '本学期'
    lines = ['---']
    for k, v in (meta or {}).items():
        if v:
            lines.append(f'{k}: {v}')
    lines += ['---', '', f'# {semester} 学期课表', '',
              '> 由操作界面（`--ui`）或 `scripts/pull_tmeet_recordings.py` 维护。',
              '>', '> 字段说明：',
              '> - **星期**：一/二/三/四/五/六/日',
              '> - **时间段**：`HH:MM-HH:MM`（会议开始时间落在「开始前 30 分钟 ~ 结束后 45 分钟」窗口内即匹配）',
              '> - **周次**：`1-16`（每周）、`1-8单`、`2-16双`、`3,5,7`（指定周）均可',
              '> - **会议号**：可填，填写后优先按会议号强匹配',
              '> - **停课**：frontmatter 中填写停课日期，停课日不匹配课程且不计入学期课次',
              '', '## 作息时间（教务系统设置，2026-09-02 确认）', '',
              '| 节次 | 时间 | 节次 | 时间 |', '|:--|:--|:--|:--|',
              '| 第1节 | 08:30-09:15 | 第7节 | 16:20-17:05 |',
              '| 第2节 | 09:20-10:05 | 第8节 | 17:10-17:55 |',
              '| 第3节 | 10:20-11:05 | 第9节 | 19:30-20:15 |',
              '| 第4节 | 11:10-11:55 | 第10节 | 20:20-21:05 |',
              '| 第5节 | 14:30-15:15 | 第11节 | 21:10-21:55 |',
              '| 第6节 | 15:20-16:05 | | |', '', '## 课程安排', '',
              '| 课程 | 星期 | 节次 | 时间段 | 周次 | 会议号 | 教师 |',
              '|:--|:--|:--|:--|:--|:--|:--|']
    for r in rows:
        cells = [r.get('course', ''), r.get('weekday', ''), r.get('slots', ''),
                 r.get('time_range', ''), r.get('weeks', ''),
                 r.get('meeting_code', ''), r.get('teacher', '')]
        lines.append('| ' + ' | '.join(cells) + ' |')
    lines.append('')
    with open(core.TIMETABLE_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return core.TIMETABLE_PATH


def get_schedule_state():
    """计划任务状态（含注册信息）。"""
    rc, out = core._schtasks(['/Query', '/TN', core.SCHED_TASK_NAME, '/FO', 'LIST', '/V'])
    if rc != 0:
        return {'registered': False}
    info = {}
    for line in out.splitlines():
        m = re.match(r'^\s*(TaskName|Status|Next Run Time|Last Run Time|Last Result|Task To Run|Schedule Type)\s*:\s*(.*)$', line)
        if m:
            info[m.group(1).strip()] = m.group(2).strip()
    return {'registered': True, **info}


def self_cmd(extra):
    """调用自身（exe 或 python 脚本）的命令。"""
    if core.FROZEN:
        return [os.path.abspath(sys.executable), *extra]
    return [sys.executable, os.path.abspath(core.__file__), *extra]


def log_tail(lines=60):
    """最近运行日志尾部。"""
    try:
        with open(core.LOG_PATH, encoding='utf-8') as f:
            all_lines = f.read().splitlines()
        return '\n'.join(all_lines[-lines:])
    except OSError:
        return ''


# ---------------------------------------------------------------- HTTP 服务

PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>课堂录音自动归档</title>
<style>
  :root { --bg:#f6f7f9; --card:#fff; --line:#e3e6eb; --accent:#2f6fed; --text:#1f2329; --muted:#6b7280; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:"Microsoft YaHei","PingFang SC",sans-serif; background:var(--bg); color:var(--text); padding:24px; }
  h1 { font-size:20px; margin-bottom:4px; }
  .sub { color:var(--muted); font-size:13px; margin-bottom:20px; }
  .card { background:var(--card); border:1px solid var(--line); border-radius:10px; padding:18px 20px; margin-bottom:18px; }
  .card h2 { font-size:15px; margin-bottom:12px; }
  .row { display:flex; gap:10px; align-items:center; flex-wrap:wrap; }
  label { font-size:13px; color:var(--muted); }
  input, select, textarea { border:1px solid var(--line); border-radius:6px; padding:6px 8px; font-size:13px; font-family:inherit; }
  input:focus, select:focus, textarea:focus { outline:2px solid #d6e4ff; border-color:var(--accent); }
  button { background:var(--accent); color:#fff; border:none; border-radius:6px; padding:7px 14px; font-size:13px; cursor:pointer; }
  button:hover { opacity:.9; }
  button.ghost { background:#fff; color:var(--accent); border:1px solid var(--accent); }
  button.danger { background:#d9534f; }
  button.mini { padding:3px 9px; font-size:12px; }
  table { width:100%; border-collapse:collapse; font-size:13px; }
  th, td { border:1px solid var(--line); padding:5px 7px; text-align:left; }
  th { background:#f2f4f7; font-weight:600; white-space:nowrap; }
  td input, td select { width:100%; min-width:70px; padding:4px 6px; font-size:12px; }
  td.wide input { min-width:150px; }
  .status { font-size:12px; color:var(--muted); margin-top:8px; }
  .ok { color:#1a7f37; } .bad { color:#d1242f; }
  pre#log { background:#0f172a; color:#dbeafe; border-radius:8px; padding:12px; font-size:12px;
            max-height:260px; overflow:auto; white-space:pre-wrap; font-family:Consolas,monospace; }
  .kv { display:grid; grid-template-columns:auto 1fr; gap:4px 14px; font-size:13px; margin-bottom:10px; }
  .kv b { color:var(--muted); font-weight:400; }
  .meta-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; margin-bottom:12px; }
  .meta-grid label { display:block; margin-bottom:4px; }
  .meta-grid input, .meta-grid textarea { width:100%; }
  .footer { color:var(--muted); font-size:12px; margin-top:14px; }
</style>
</head>
<body>
<h1>📼 课堂录音自动归档</h1>
<div class="sub">腾讯会议录制拉取 · 课表匹配 · 定时归档 · 由 <code>pull_tmeet_recordings.exe --ui</code> 提供服务</div>

<div class="card">
  <h2>⏰ 自动拉取（Windows 计划任务）</h2>
  <div id="sched_info" class="kv"></div>
  <div class="row">
    <label>每天时间</label>
    <input id="sched_time" placeholder="如 19:30" value="19:30" style="width:90px">
    <button onclick="setSchedule()">设置 / 修改定时</button>
    <button class="ghost" onclick="refreshState()">刷新状态</button>
    <button class="danger" onclick="removeSchedule()">删除定时</button>
  </div>
  <div id="sched_msg" class="status"></div>
</div>

<div class="card">
  <h2>📅 课表管理</h2>
  <div class="meta-grid">
    <div><label>学期</label><input id="m_semester" placeholder="如 2026-2027-1"></div>
    <div><label>开学日期</label><input id="m_start" placeholder="如 2026-08-31"></div>
    <div><label>排除主题（逗号分隔）</label><input id="m_excluded" placeholder="如 公开课,测试"></div>
    <div><label>调休（日期=星期，逗号分隔）</label><input id="m_makeup" placeholder="如 2026-10-10=三, 2026-09-26=四"></div>
    <div><label>停课（日期，逗号分隔）</label><input id="m_cancelled" placeholder="如 2026-10-16, 2026-11-06"></div>
  </div>
  <table id="tt">
    <thead><tr><th>课程</th><th>星期</th><th>节次</th><th>时间段</th><th>周次</th><th>会议号</th><th>教师</th><th></th></tr></thead>
    <tbody></tbody>
  </table>
  <div class="row" style="margin-top:10px">
    <button onclick="addRow()">＋ 添加课程</button>
    <button onclick="saveTimetable()">💾 保存课表</button>
    <button class="ghost" onclick="refreshState()">撤销修改</button>
  </div>
  <div id="tt_msg" class="status"></div>
</div>

<div class="card">
  <h2>▶️ 立即拉取 / 运行日志</h2>
  <div class="row">
    <button onclick="runNow()">立即拉取最近 2 天</button>
    <label>（后台执行，期间界面可继续操作）</label>
  </div>
  <div id="run_msg" class="status"></div>
  <pre id="log" style="margin-top:10px"></pre>
</div>

<div class="footer">脚本：scripts/pull_tmeet_recordings.py ｜ 课表：04_Assets/Schedule/课表.base ｜ 日志：tmp/tmeet_sync.log</div>

<script>
let state = null;
const $ = id => document.getElementById(id);

async function api(path, method = 'GET', body = null) {
  const opt = { method, headers: { 'Content-Type': 'application/json' } };
  if (body) opt.body = JSON.stringify(body);
  const r = await fetch(path, opt);
  return r.json();
}

function esc(s) { return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;'); }

function renderSchedule() {
  const s = state.schedule;
  if (!s.registered) {
    $('sched_info').innerHTML = '<div><b>状态：</b><span class="bad">未注册</span></div>';
    return;
  }
  const kv = [
    ['任务名', s.TaskName || 'TmeetRecordingSync'],
    ['状态', s.Status || '-'],
    ['下次运行', s['Next Run Time'] || '-'],
    ['上次运行', s['Last Run Time'] || '-'],
    ['上次结果', s['Last Result'] || '-'],
    ['命令', (s['Task To Run'] || '-').replace(/&/g,'&amp;')],
  ];
  $('sched_info').innerHTML = kv.map(([k,v]) => `<div><b>${k}：</b>${esc(v)}</div>`).join('');
  if (s['Next Run Time']) {
    const m = s['Next Run Time'].match(/(\\d{1,2}):(\\d{2}):\\d{2}/);
    if (m) $('sched_time').value = m[1].padStart(2,'0') + ':' + m[2];
  }
}

function renderTimetable() {
  const t = state.timetable;
  $('m_semester').value = t.meta['学期'] || '';
  $('m_start').value = t.meta['开学日期'] || '';
  $('m_excluded').value = t.meta['排除主题'] || '';
  $('m_makeup').value = t.meta['调休'] || '';
  $('m_cancelled').value = t.meta['停课'] || '';
  const tb = $('tt').querySelector('tbody');
  tb.innerHTML = '';
  (t.rows || []).forEach(r => addRow(r));
  if (!(t.rows || []).length) addRow();
}

function addRow(r = {}) {
  const tb = $('tt').querySelector('tbody');
  const tr = document.createElement('tr');
  const days = ['一','二','三','四','五','六','日'];
  const dayOpts = days.map(d => `<option ${d === r.weekday ? 'selected' : ''}>${d}</option>`).join('');
  tr.innerHTML = `
    <td class="wide"><input class="c-course" value="${esc(r.course)}" placeholder="课程名"></td>
    <td><select class="c-weekday">${dayOpts}</select></td>
    <td><input class="c-slots" value="${esc(r.slots)}" placeholder="如 3-4"></td>
    <td><input class="c-time" value="${esc(r.time_range)}" placeholder="如 10:20-11:55"></td>
    <td><input class="c-weeks" value="${esc(r.weeks)}" placeholder="如 1-16"></td>
    <td><input class="c-code" value="${esc(r.meeting_code)}" placeholder="会议号(可选)"></td>
    <td><input class="c-teacher" value="${esc(r.teacher)}" placeholder="教师(可选)"></td>
    <td><button class="mini danger" onclick="this.closest('tr').remove()">删</button></td>`;
  tb.appendChild(tr);
}

function collectRows() {
  return [...$('tt').querySelectorAll('tbody tr')].map(tr => ({
    course: tr.querySelector('.c-course').value.trim(),
    weekday: tr.querySelector('.c-weekday').value,
    slots: tr.querySelector('.c-slots').value.trim(),
    time_range: tr.querySelector('.c-time').value.trim(),
    weeks: tr.querySelector('.c-weeks').value.trim(),
    meeting_code: tr.querySelector('.c-code').value.trim(),
    teacher: tr.querySelector('.c-teacher').value.trim(),
  })).filter(r => r.course);
}

async function refreshState() {
  state = await api('/api/state');
  renderSchedule();
  renderTimetable();
  const log = await api('/api/log');
  $('log').textContent = log.tail || '';
}

async function setSchedule() {
  const time = $('sched_time').value.trim();
  $('sched_msg').innerHTML = '正在设置…';
  const r = await api('/api/schedule', 'POST', { time });
  $('sched_msg').innerHTML = r.ok ? '<span class="ok">✅ ' + esc(r.message) + '</span>' : '<span class="bad">❌ ' + esc(r.message) + '</span>';
  await refreshState();
}

async function removeSchedule() {
  if (!confirm('确定删除定时拉取任务？')) return;
  const r = await api('/api/schedule/delete', 'POST');
  $('sched_msg').innerHTML = r.ok ? '<span class="ok">✅ ' + esc(r.message) + '</span>' : '<span class="bad">❌ ' + esc(r.message) + '</span>';
  await refreshState();
}

async function saveTimetable() {
  const body = {
    meta: { '学期': $('m_semester').value.trim(), '开学日期': $('m_start').value.trim(),
            '排除主题': $('m_excluded').value.trim(), '调休': $('m_makeup').value.trim(),
            '停课': $('m_cancelled').value.trim() },
    rows: collectRows(),
  };
  const r = await api('/api/timetable', 'POST', body);
  $('tt_msg').innerHTML = r.ok ? '<span class="ok">✅ ' + esc(r.message) + '</span>' : '<span class="bad">❌ ' + esc(r.message) + '</span>';
  if (r.ok) await refreshState();
}

async function runNow() {
  $('run_msg').innerHTML = '已启动拉取，正在后台运行…（日志每 3 秒刷新）';
  const r = await api('/api/run', 'POST');
  if (!r.ok) { $('run_msg').innerHTML = '<span class="bad">❌ ' + esc(r.message) + '</span>'; return; }
  const timer = setInterval(async () => {
    const log = await api('/api/log?lines=80');
    $('log').textContent = log.tail || '';
    if (!log.running) { clearInterval(timer); $('run_msg').innerHTML = '<span class="ok">✅ 拉取完成，详见上方日志。</span>'; }
  }, 3000);
}

refreshState();
setInterval(async () => {
  if (state?.schedule?.registered) {
    const log = await api('/api/log');
    if (log.tail !== $('log').textContent) $('log').textContent = log.tail;
  }
}, 10000);
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass  # 静默访问日志

    def _send(self, code, body, ctype='application/json; charset=utf-8'):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self._send(200, PAGE.encode('utf-8'), 'text/html; charset=utf-8')
        elif self.path.startswith('/api/state'):
            self._send(200, {'timetable': read_timetable(), 'schedule': get_schedule_state()})
        elif self.path.startswith('/api/log'):
            try:
                lines = int(self.path.split('lines=', 1)[1].split('&', 1)[0])
            except (IndexError, ValueError):
                lines = 60
            self._send(200, {'tail': log_tail(lines), 'running': RUNNING.is_set()})
        else:
            self._send(404, {'error': 'not found'})

    def do_POST(self):
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length).decode('utf-8')) if length else {}
        except (ValueError, json.JSONDecodeError):
            body = {}
        if self.path == '/api/timetable':
            try:
                save_timetable(body.get('meta'), body.get('rows') or [])
                self._send(200, {'ok': True, 'message': f"课表已保存（{len(body.get('rows') or [])} 门课）→ 04_Assets/Schedule"})
            except Exception as e:
                self._send(200, {'ok': False, 'message': f'保存失败: {e}'})
        elif self.path == '/api/schedule':
            time_str = (body.get('time') or '19:30').strip()
            if not re.match(r'^([01]?\d|2[0-3]):[0-5]\d$', time_str):
                self._send(200, {'ok': False, 'message': f'时间格式错误：{time_str}（应为 HH:MM）'})
            else:
                try:
                    core.install_schedule(time_str)
                    self._send(200, {'ok': True, 'message': f'定时已设为每天 {time_str}'})
                except SystemExit as e:
                    self._send(200, {'ok': False, 'message': str(e)})
        elif self.path == '/api/schedule/delete':
            try:
                core.remove_schedule()
                self._send(200, {'ok': True, 'message': '定时任务已删除'})
            except SystemExit as e:
                self._send(200, {'ok': False, 'message': str(e)})
        elif self.path == '/api/run':
            if RUNNING.is_set():
                self._send(200, {'ok': True, 'message': '已有拉取在运行'})
            else:
                RUNNING.set()
                threading.Thread(target=_run_pull, daemon=True).start()
                self._send(200, {'ok': True, 'message': '拉取已启动'})
        else:
            self._send(404, {'error': 'not found'})


RUNNING = threading.Event()


def _run_pull():
    """后台线程：调用自身执行一次拉取（最近 2 天）。"""
    try:
        subprocess.run(self_cmd(['--days', '2']), timeout=1800)
    except Exception:
        pass
    finally:
        RUNNING.clear()


def run_ui(port=None, vault=None):
    """启动 Web 界面服务。"""
    if vault:
        core.set_vault(vault)
    port = port or DEFAULT_PORT
    try:
        os.system('title 课堂录音自动归档 - 关闭此窗口即退出服务')
    except Exception:
        pass
    try:
        server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    except OSError as e:
        print(f'\n❌ 端口 {port} 启动失败: {e}')
        print(f'   界面可能已在运行 → 请直接打开浏览器访问 http://127.0.0.1:{port}')
        print(f'   或先关闭旧窗口后再启动；如需换端口：pull_tmeet_recordings.exe --ui 8000')
        try:
            input('按回车键关闭窗口…')
        except EOFError:
            pass
        return
    url = f'http://127.0.0.1:{port}'
    print()
    print('=' * 56)
    print('   📼 课堂录音自动归档 操作界面')
    print(f'   🌐 已启动：{url}')
    print(f'   📋 课表：{core.TIMETABLE_PATH}')
    print('   🖥  浏览器应已自动打开；若未打开请手动访问上面的地址')
    print('   ⏹  关闭本窗口 或 按 Ctrl+C 退出服务')
    print('=' * 56)
    print()
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n已退出。')
    except Exception as e:
        print(f'\n服务异常退出: {e}')
        try:
            input('按回车键关闭窗口…')
        except EOFError:
            pass


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='课堂录音归档 - 本地操作界面')
    ap.add_argument('--port', type=int, default=DEFAULT_PORT)
    ap.add_argument('--vault', help='知识库根目录')
    a = ap.parse_args()
    run_ui(a.port, a.vault)
