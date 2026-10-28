"""Hash-bound move/write plans with byte backups and guarded, restartable recovery."""
from __future__ import annotations

import ctypes
from contextlib import contextmanager, ExitStack
from contextvars import ContextVar
from functools import wraps
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil

import change_control as guard

_SESSION=ContextVar('knowledge_v2_transaction',default=None)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_hash(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_path(root, name):
    if not isinstance(name, str) or not name or '\\' in name or name.startswith('/'):
        raise ValueError('Canonical Vault-relative path required')
    parts = name.split('/')
    for part in parts:
        if (not part or part in ('.', '..') or part.startswith('.') or part.rstrip(' .') != part
                or re.search(r'[<>:"|?*\x00-\x1f]', part)
                or re.fullmatch(r'(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', part)):
            raise ValueError('Unsafe Windows path: ' + name)
    path = root / name
    if guard.links.protected_reason(root, path):
        raise ValueError('Protected or independent path: ' + name)
    if path.exists() and (not path.is_file() or path.stat().st_nlink != 1):
        raise ValueError('Only ordinary, unlinked files are writable')
    return path


def _json(path, value):
    raw = json.dumps(value, ensure_ascii=False, indent=2).encode('utf-8')
    Path(path).write_bytes(raw)
    return digest(raw)


def plan(root, operations, backup):
    root = Path(root).resolve()
    backup = Path(backup).absolute()
    if not root.is_dir() or backup.exists() or backup.resolve().is_relative_to(root) or root.is_relative_to(backup.resolve()):
        raise ValueError('Use a new backup directory outside the Vault')
    rows, targets, sources = [], set(), set()
    # Inspect the whole namespace before producing any artifact or touching data.
    for index, op in enumerate(operations):
        if set(op) not in ({'source', 'target', 'content', 'reason'}, {'source', 'target', 'content', 'reason', 'expected_sha256'}):
            raise ValueError('Invalid operation fields')
        source = op['source']
        target = op['target']
        dest = safe_path(root, target)
        origin = safe_path(root, source) if source is not None else None
        if target.casefold() in targets or (source is not None and source.casefold() in sources):
            raise ValueError('Duplicate source/target')
        targets.add(target.casefold())
        if source is not None:
            sources.add(source.casefold())
        if origin is not None and not origin.is_file():
            raise ValueError('Missing source: ' + source)
        if dest.exists() and source != target:
            raise ValueError('Existing target: ' + target)
        content = op['content']
        if content is not None and not isinstance(content, bytes):
            raise ValueError('Content must be bytes or None')
        if origin is None and content is None:
            raise ValueError('New file needs content')
        before = file_hash(origin) if origin else None
        if 'expected_sha256' in op and op['expected_sha256'] != before:
            raise ValueError('Source snapshot changed before planning: ' + str(source))
        after = digest(content) if content is not None else before
        if source == target and before == after:
            continue
        rows.append({'id': f'{index:06d}', 'source': source, 'target': target,
                     'before_sha256': before, 'after_sha256': after, 'reason': str(op['reason']),
                     '_content': content})
    # Chained/cyclic namespace moves require a separate explicit batch.
    for row in rows:
        if row['source'] != row['target'] and row['target'].casefold() in sources:
            raise ValueError('Chained moves are not allowed in one batch')
    backup.mkdir(parents=True)
    (backup / 'original').mkdir()
    (backup / 'payload').mkdir()
    diff_dir = backup / 'diffs'
    diff_dir.mkdir()
    for row in rows:
        key = row['id'] + '.bin'
        origin = root / row['source'] if row['source'] else None
        original = backup / 'original' / key
        if origin:
            shutil.copyfile(origin, original)
            if file_hash(original) != row['before_sha256'] or file_hash(origin) != row['before_sha256']:
                raise ValueError('Source changed while preparing plan')
        content = row.pop('_content')
        payload = backup / 'payload' / key
        if content is None:
            shutil.copyfile(original, payload)
        else:
            payload.write_bytes(content)
        if file_hash(payload) != row['after_sha256']:
            raise ValueError('Payload verification failed')
        if Path(row['target']).suffix.lower() in ('.md', '.base', '.json', '.yaml', '.yml', '.py'):
            try:
                before = original.read_text('utf-8-sig') if origin else ''
                after = payload.read_text('utf-8-sig')
                delta = ''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                              fromfile=row['source'] or '/dev/null', tofile=row['target']))
                (diff_dir / (row['id'] + '.diff')).write_text(delta, encoding='utf-8')
            except UnicodeError:
                row['diff_kind'] = 'binary'
        else:
            row['diff_kind'] = 'binary'
    record = {'plan_version': 2, 'vault_root': str(root), 'entries': rows}
    checksum = _json(backup / 'plan.json', record)
    return {'dry_run': True, 'plan': str(backup / 'plan.json'), 'plan_sha256': checksum,
            'planned': len(rows), 'diffs': str(diff_dir), 'conflicts': 0}


def _load(plan_path, approved):
    path = Path(plan_path).absolute()
    raw = path.read_bytes()
    if digest(raw) != approved:
        raise ValueError('Exact plan SHA-256 required')
    record = json.loads(raw)
    # The approved namespace must not be rebound by resolving a newly inserted junction.
    root = Path(record['vault_root']).absolute()
    if record.get('plan_version') != 2 or path.resolve().is_relative_to(root):
        raise ValueError('Invalid plan version/placement')
    seen = set()
    for row in record['entries']:
        safe_path(root, row['target'])
        if row['source']:
            safe_path(root, row['source'])
        if not re.fullmatch(r'\d{6}', row['id']) or row['target'].casefold() in seen:
            raise ValueError('Invalid or duplicate plan entry')
        seen.add(row['target'].casefold())
        key = row['id'] + '.bin'
        if file_hash(path.parent / 'payload' / key) != row['after_sha256']:
            raise ValueError('Payload changed')
        if row['before_sha256'] is not None and file_hash(path.parent / 'original' / key) != row['before_sha256']:
            raise ValueError('Backup changed')
    return path, record, root


def _journal_records(stream):
    """Recover a torn final append, retaining every complete validated record."""
    raw = stream.read()
    end = raw.rfind(b'\n') + 1
    result = {}
    def accept(row):
        if (not isinstance(row, dict) or set(row) != {'id', 'state'}
                or not isinstance(row['id'], str) or not re.fullmatch(r'\d{6}', row['id'])
                or row['state'] not in ('intent', 'applied', 'restore_intent', 'restored')):
            raise ValueError('Invalid transaction journal record')
        result[row['id']] = row
    for line in raw[:end].splitlines():
        accept(json.loads(line))  # Interior/terminated corruption must fail closed.
    tail = raw[end:]
    if tail:
        try:
            final = json.loads(tail)
        except json.JSONDecodeError as error:
            text = tail.decode('utf-8')
            if not (error.msg.startswith('Unterminated string') or error.pos >= len(text.rstrip())):
                raise ValueError('Malformed transaction journal tail') from error
            repaired = raw[:end]
        else:
            accept(final)
            repaired = raw + b'\n'  # Complete JSON whose final newline was not written.
        stream.seek(0)
        guard._write_all(stream, repaired)
        stream.truncate(len(repaired))
        stream.flush()
        os.fsync(stream.fileno())
    return result


def _events(path):
    session=_SESSION.get()
    if session is not None and session['path']==path:
        session['stream'].seek(0)
        return _journal_records(session['stream'])
    with guard._safe_stream(path.parent / 'journal.jsonl', 4, strict_path=True) as stream:
        return _journal_records(stream)


def _event(path, value):
    session=_SESSION.get()
    if session is not None and session['path']==path:
        stream=session['stream']
        stream.seek(0,os.SEEK_END)
        guard._write_all(stream,(json.dumps(value,ensure_ascii=False)+'\n').encode('utf-8'))
        stream.flush()
        os.fsync(stream.fileno())
        return
    with guard._safe_stream(path.parent / 'journal.jsonl', 4, strict_path=True) as stream:
        _journal_records(stream)  # Repair under the same exclusive handle before appending.
        stream.seek(0, os.SEEK_END)
        guard._write_all(stream, (json.dumps(value, ensure_ascii=False) + '\n').encode('utf-8'))
        stream.flush()
        os.fsync(stream.fileno())


def _with_journal(function):
    """Validate once and exclusively hold the journal, avoiding quadratic reparsing."""
    @wraps(function)
    def execute(plan_path,approved):
        loaded=_load(plan_path,approved)
        path=loaded[0]
        with guard._safe_stream(path.parent/'journal.jsonl',4,strict_path=True) as stream:
            token=_SESSION.set({'path':path,'stream':stream,'loaded':loaded})
            try:
                return function(plan_path,approved)
            finally:
                _SESSION.reset(token)
    return execute


def _session_load(plan_path,approved):
    session=_SESSION.get()
    if session is not None and session['path']==Path(plan_path).absolute():
        return session['loaded']
    return _load(plan_path,approved)


def _remove_locked(stream):
    import msvcrt
    from ctypes import wintypes
    class Disposition(ctypes.Structure):
        _fields_ = [('delete', wintypes.BOOL)]
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    fn = kernel.SetFileInformationByHandle
    fn.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
    fn.restype = wintypes.BOOL
    info = Disposition(True)
    if not fn(msvcrt.get_osfhandle(stream.fileno()), 4, ctypes.byref(info), ctypes.sizeof(info)):
        raise ctypes.WinError(ctypes.get_last_error())


def _locked_hash(stream):
    stream.seek(0)
    result = hashlib.file_digest(stream, 'sha256').hexdigest()
    stream.seek(0)
    return result


@contextmanager
def _directory_guard(path):
    """Deny replacement/reparse writes while descendants are being accessed."""
    if os.name != 'nt':
        raise OSError('Writes require the Windows directory guard')
    from ctypes import wintypes
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    create = kernel.CreateFileW
    create.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p,
                       wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    create.restype = wintypes.HANDLE
    close = kernel.CloseHandle
    close.argtypes = [wintypes.HANDLE]
    close.restype = wintypes.BOOL
    attributes = kernel.GetFileInformationByHandleEx
    attributes.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
    attributes.restype = wintypes.BOOL
    name = kernel.GetFinalPathNameByHandleW
    name.argtypes = [wintypes.HANDLE, wintypes.LPWSTR, wintypes.DWORD, wintypes.DWORD]
    name.restype = wintypes.DWORD
    class AttributeTag(ctypes.Structure):
        _fields_ = [('attributes', wintypes.DWORD), ('tag', wintypes.DWORD)]
    path = Path(path).absolute()
    # FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES; share READ only; OPEN_EXISTING;
    # BACKUP_SEMANTICS |
    # OPEN_REPARSE_POINT. Open the directory itself, never follow a junction.
    handle = create(str(path), 0x81, 1, None, 3, 0x02000000 | 0x00200000, None)
    if handle == ctypes.c_void_p(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        info = AttributeTag()
        if not attributes(handle, 9, ctypes.byref(info), ctypes.sizeof(info)):
            raise ctypes.WinError(ctypes.get_last_error())
        if info.attributes & 0x400 or not info.attributes & 0x10:
            raise ValueError('Reparse/non-directory ancestor refused: ' + str(path))
        buffer = ctypes.create_unicode_buffer(32768)
        length = name(handle, buffer, len(buffer), 0)
        if not length or length >= len(buffer):
            raise ValueError('Cannot verify directory handle path')
        actual = buffer.value
        if actual.startswith('\\\\?\\UNC\\'):
            actual = '\\\\' + actual[8:]
        elif actual.startswith('\\\\?\\'):
            actual = actual[4:]
        if os.path.normcase(os.path.normpath(actual)) != os.path.normcase(str(path)):
            raise ValueError('Directory handle path changed: ' + str(path))
        yield
    finally:
        close(handle)


@contextmanager
def _guard_paths(root, paths):
    """Lock root-to-parent chains before creating any child directory or file."""
    root = Path(root).absolute()
    with ExitStack() as stack:
        stack.enter_context(_directory_guard(root))
        locked = {root}
        for path in paths:
            if path is None:
                continue
            current = root
            for part in path.parent.relative_to(root).parts:
                current = current / part
                if current in locked:
                    continue
                # The parent is already held against rename/reparse changes.
                try:
                    stack.enter_context(_directory_guard(current))
                except OSError as error:
                    if getattr(error, 'winerror', None) not in (2, 3):
                        raise
                    try:
                        current.mkdir()
                    except FileExistsError:
                        pass
                    stack.enter_context(_directory_guard(current))
                if (current / '.git').exists():
                    raise ValueError('Independent repository ancestor refused')
                locked.add(current)
        yield


def _write(path, payload, expected):
    with guard._safe_stream(path, 1 if expected is None else 3, strict_path=True) as stream:
        if expected is not None and _locked_hash(stream) != expected:
            raise ValueError('Concurrent target edit: ' + str(path))
        if expected is None and stream.read(1):
            raise ValueError('New file was not empty')
        _write_locked(stream, payload)


def _write_locked(stream, payload):
    stream.seek(0)
    guard._write_all(stream, payload)
    stream.truncate(len(payload))
    stream.flush()
    os.fsync(stream.fileno())
    if _locked_hash(stream) != digest(payload):
        raise OSError('Write verification failed')


def _transfer(origin, target, payload, expected):
    """Keep source exclusively locked until destination is durable and source is deleted."""
    with guard._safe_stream(origin, 3, delete_access=True, strict_path=True) as stream:
        if _locked_hash(stream) != expected:
            raise ValueError('Concurrent source edit: ' + str(origin))
        _write(target, payload, None)
        _remove_locked(stream)


def _preflight(root, entries, restoring, states):
    for row in entries:
        state = states.get(row['id'], {}).get('state')
        if restoring and state not in ('applied', 'intent', 'restore_intent'):
            continue
        if not restoring and state == 'applied':
            target = safe_path(root, row['target'])
            if not target.exists() or file_hash(target) != row['after_sha256']:
                raise ValueError('Previously applied target changed')
            continue
        origin = safe_path(root, row['source']) if row['source'] else None
        target = safe_path(root, row['target'])
        if restoring:
            # Data may already be restored when its terminal event was interrupted.
            if origin == target and target.exists() and file_hash(target) == row['before_sha256']:
                continue
            if not target.exists():
                if not origin or (origin.exists() and file_hash(origin) == row['before_sha256']):
                    continue  # Completed recovery or an apply intent with no effect.
            if not target.exists() or file_hash(target) != row['after_sha256']:
                raise ValueError('Later target edit must be preserved: ' + row['target'])
            if origin and origin != target and origin.exists() and file_hash(origin) != row['before_sha256']:
                raise ValueError('Restoration source path has a new user file')
        else:
            if origin and (not origin.exists() or file_hash(origin) != row['before_sha256']):
                raise ValueError('Source changed: ' + row['source'])
            if target.exists() and origin != target:
                if not (state=='intent' and origin is not None and file_hash(target)==row['after_sha256']):
                    raise ValueError('Target appeared: ' + row['target'])


@_with_journal
def apply(plan_path, approved):
    path, record, root = _session_load(plan_path, approved)
    states = _events(path)
    _preflight(root, record['entries'], False, states)
    count = 0
    for row in record['entries']:
        if states.get(row['id'], {}).get('state') == 'applied':
            continue
        source = safe_path(root, row['source']) if row['source'] else None
        target = safe_path(root, row['target'])
        payload = (path.parent / 'payload' / (row['id'] + '.bin')).read_bytes()
        if digest(payload) != row['after_sha256']:
            raise ValueError('Payload changed after loading')
        with _guard_paths(root, (source, target)):
            _event(path, {'id': row['id'], 'state': 'intent'})
            if source and source != target:
                if target.exists():
                    # Resume the durable copy stage of a journaled move.
                    with guard._safe_stream(source,3,delete_access=True,strict_path=True) as origin:
                        if _locked_hash(origin)!=row['before_sha256']:
                            raise ValueError('Concurrent source edit during move resumption')
                        with guard._safe_stream(target,3,strict_path=True) as copied:
                            if _locked_hash(copied)!=row['after_sha256']:
                                raise ValueError('Copied target changed during move resumption')
                            _remove_locked(origin)
                else:
                    _transfer(source, target, payload, row['before_sha256'])
            else:
                _write(target, payload, row['before_sha256'])
            _event(path, {'id': row['id'], 'state': 'applied'})
        count += 1
    return {'applied': count, 'conflicts': 0, 'plan': str(path)}


@_with_journal
def restore(plan_path, approved):
    path, record, root = _session_load(plan_path, approved)
    states = _events(path)
    _preflight(root, record['entries'], True, states)
    count = 0
    for row in reversed(record['entries']):
        state = states.get(row['id'], {}).get('state')
        if state not in ('applied', 'intent', 'restore_intent'):
            continue
        target = safe_path(root, row['target'])
        source = safe_path(root, row['source']) if row['source'] else None
        original = None
        if source:
            original = (path.parent / 'original' / (row['id'] + '.bin')).read_bytes()
            if digest(original) != row['before_sha256']:
                raise ValueError('Backup changed after loading')
        with _guard_paths(root, (source, target)):
            _event(path, {'id': row['id'], 'state': 'restore_intent'})
            count += _restore_row(source, target, original, row)
            _event(path, {'id': row['id'], 'state': 'restored'})
    return {'restored': count, 'conflicts': 0, 'plan': str(path)}


def _delete_target(target, expected):
    with guard._safe_stream(target, 3, delete_access=True, strict_path=True) as stream:
        if _locked_hash(stream) != expected:
            raise ValueError('Target changed during recovery')
        _remove_locked(stream)


def _restore_row(source, target, original, row):
    if source == target:
        with guard._safe_stream(source, 3, strict_path=True) as stream:
            current = _locked_hash(stream)
            if current == row['before_sha256']:
                return 0
            if current != row['after_sha256']:
                raise ValueError('Target changed during recovery')
            _write_locked(stream, original)
            return 1
    if source and source.exists():
        # Recovery can be interrupted after restoring source but before removing target.
        # Keep source locked and recheck its exact bytes until the target is removed.
        with guard._safe_stream(source, 3, strict_path=True) as stream:
            if _locked_hash(stream) != row['before_sha256']:
                raise ValueError('Restoration source path has a new user file')
            if not target.exists():
                return 0
            _delete_target(target, row['after_sha256'])
            return 1
    if not target.exists():
        if source:
            raise ValueError('Both recovery paths are missing')
        return 0
    if source:
        _transfer(target, source, original, row['after_sha256'])
    else:
        _delete_target(target, row['after_sha256'])
    return 1
