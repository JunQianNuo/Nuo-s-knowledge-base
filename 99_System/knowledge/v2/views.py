"""Read-only proposals for recursive MOC embeds and native Obsidian Bases."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re

import yaml

from . import model

GENERATED = "99_System/knowledge/v2/generated"
START = b"<!-- v2-generated:start -->"
END = b"<!-- v2-generated:end -->"


def _graph(notes):
    mocs = {path for path, entry in notes.items() if entry["data"].get("type") == "moc"}
    children = {path: set() for path in mocs}
    for path in sorted(mocs):
        if not path.startswith("02_Maps/"):
            raise ValueError(f"MOC must be stored in 02_Maps：{path}")
        if model.validate(notes[path]["data"]):
            raise ValueError(f"Invalid MOC metadata：{path}")
        for topic in notes[path]["data"]["topics"]:
            parent, error = model.resolve(notes, topic)
            if error or parent not in mocs:
                raise ValueError(f"Topic must resolve to an actual MOC：{path} → {topic}")
            children[parent].add(path)
    active, finished = set(), set()

    def visit(path):
        if path in active:
            raise ValueError(f"MOC cycle（主题环）：{path}")
        if path in finished:
            return
        active.add(path)
        for child in sorted(children[path]):
            visit(child)
        active.remove(path)
        finished.add(path)

    for path in sorted(mocs):
        visit(path)
    return children


def descendants(notes: dict, moc: str) -> set[str]:
    graph = _graph(notes)
    if moc not in graph:
        raise ValueError(f"Not a MOC：{moc}")
    found, pending = set(), list(graph[moc])
    while pending:
        child = pending.pop()
        if child not in found:
            found.add(child)
            pending.extend(graph[child])
    return found


def _scope_conditions(root, scope, include_resources=False):
    """Dynamic scope with small boundary exclusions, never a file manifest."""
    folders = model.RAW_FOLDERS - {"ppt课件", "pdf课件", "课件"} if include_resources else model.RAW_FOLDERS
    # New raw/hidden directories are excluded without needing view regeneration.
    pattern = r"(^|\/)(" + "|".join(re.escape(name) for name in sorted(folders)) + r"|\.[^\/]+)(\/|$)"
    conditions = [f"file.inFolder({json.dumps(scope, ensure_ascii=False)})", f"!/{pattern}/i.matches(file.path)"]
    start = root / scope
    ancestors = [start, *list(start.parents)[:len(start.relative_to(root).parts) - 1]]
    if any(path.is_symlink() or path.is_junction() or (path / ".git").exists() for path in ancestors):
        return conditions + ["false"]
    if not start.is_dir():
        return conditions
    for parent, dirs, names in os.walk(start, followlinks=False):
        parent = Path(parent)
        for name in list(dirs):
            path = parent / name
            if path.is_symlink() or path.is_junction() or (path / ".git").exists():
                conditions.append({"not": [f"file.inFolder({json.dumps(path.relative_to(root).as_posix(), ensure_ascii=False)})"]})
                dirs.remove(name)
            elif name.startswith(".") or name.casefold() in folders:
                dirs.remove(name)
        for name in names:
            path = parent / name
            if path.is_symlink() or path.is_junction():
                conditions.append({"not": [f"file.path == {json.dumps(path.relative_to(root).as_posix(), ensure_ascii=False)}"]})
    return conditions


def _type_filter(kinds):
    return {"or": [f'type == "{kind}"' for kind in kinds]}


def _typed_filter(root, scope, kinds):
    return {"and": [*_scope_conditions(root, scope), 'file.ext == "md"', "schema_version == 2", _type_filter(kinds)]}


def _sources_filter(root):
    return {"and": [*_scope_conditions(root, "03_Sources"), 'file.ext == "md"', {"or": ['type == "idea"', {"and": ["schema_version == 2", _type_filter(model.SOURCE_TYPES[:-1])]}]}]}


def _base(name, filters, order, **view_options):
    return yaml.safe_dump({"filters": filters, "views": [{"type": "table", "name": name, "order": order, **view_options}]}, allow_unicode=True, sort_keys=False, width=1000).encode("utf-8")


def _replace_generated(raw, content):
    """Preserve every manual byte, including frontmatter and CRLF text."""
    if raw.count(START) != raw.count(END) or raw.count(START) > 1:
        raise ValueError("Malformed or repeated v2 generated markers")
    block = START + b"\n" + content.rstrip(b"\n") + b"\n" + END
    if START in raw:
        start = raw.index(START)
        end = raw.index(END)
        if end < start:
            raise ValueError("Reversed v2 generated markers")
        return raw[:start] + block + raw[end + len(END):]
    return raw + (b"" if raw.endswith(b"\n") else b"\n") + b"\n" + block + b"\n"


def build(root: Path) -> dict[str, bytes]:
    root = Path(root)
    notes = model.scan(root)
    graph = _graph(notes)  # Reject all cycles, including disconnected components.
    valid = {path: entry for path, entry in notes.items() if not entry["diagnostics"] and not model.validate(entry["data"])}
    result = {}
    moc_paths = set(graph)
    atomic = {path: entry for path, entry in valid.items() if entry["data"].get("type") in model.ATOMIC_TYPES and path.startswith("01_Knowledge/")}
    source_paths = {path for path, entry in valid.items() if entry["data"].get("type") in model.SOURCE_TYPES and path.startswith("03_Sources/")}
    for path, entry in atomic.items():
        for source in entry["data"]["source"]:
            target, error = model.resolve(notes, source)
            if error or target not in source_paths:
                raise ValueError(f"Atomic source must resolve to a valid Sources note：{path} → {source}")
        for topic in entry["data"]["topics"]:
            target, error = model.resolve(notes, topic)
            if error or target not in moc_paths:
                raise ValueError(f"Atomic topic must resolve to a valid MOC：{path} → {topic}")
    result[f"{GENERATED}/主题数据库.base"] = _base("学科与主题", _typed_filter(root, "02_Maps", ("moc",)), ["file.name", "topics", "aliases", "tags", "time"])
    result[f"{GENERATED}/标签数据库.base"] = _base("标准标签与同义名称", {"and": ['file.inFolder("99_System")', "canonical_tag != null"]}, ["file.name", "canonical_tag", "tag_aliases"])
    source_filter = _sources_filter(root)
    result[f"{GENERATED}/来源管理.base"] = _base("来源提炼状态", source_filter, ["file.name", "type", "status", "polish_status", "subject", "source", "time"])
    result[f"{GENERATED}/待处理.base"] = _base("待处理来源与 Inbox", {"or": [{"and": _scope_conditions(root, "00_Inbox")}, {"and": [source_filter, 'status == "not done"']}]}, ["file.name", "type", "status", "polish_status", "subject"])
    # Course views include PDFs and slides. Entity views use explicit v2 type
    # identity; creation and audit validate their metadata and relationships.
    materials = list(model.iter_files(root, ("03_Sources/Courses",), include_resources=True))
    course_filters = {"or": [{"and": _scope_conditions(root, "03_Sources/Courses", include_resources=True)}, {"and": [source_filter, "subject != null"]}]}
    subjects = set()
    course_folders = {}
    for entry in valid.values():
        subject_values = entry["data"].get("subject", [])
        if isinstance(subject_values, list):
            subjects.update(value for value in subject_values if isinstance(value, str))
    for path in materials:
        parts = path.relative_to(root / "03_Sources/Courses").parts
        if len(parts) > 1:
            subject = parts[1] if parts[0] == "归档" and len(parts) > 2 else parts[0]
            subjects.add(subject)
            course_folder = "/".join(parts[:2] if parts[0] == "归档" and len(parts) > 2 else parts[:1])
            course_folders.setdefault(subject, set()).add("03_Sources/Courses/" + course_folder)
    course = yaml.safe_load(_base("全部课程资料", course_filters, ["file.name", "file.ext", "type", "subject", "status", "polish_status"]).decode("utf-8"))
    for subject in sorted(subjects):
        if not isinstance(subject, str):
            continue
        folders = course_folders.get(subject, set()) | {"03_Sources/Courses/" + subject}
        course["views"].append({"type": "table", "name": subject, "filters": {"or": [*[f"file.inFolder({json.dumps(folder, ensure_ascii=False)})" for folder in sorted(folders)], f"subject.contains({json.dumps(subject, ensure_ascii=False)})"]}, "order": ["file.name", "file.ext", "type", "status", "polish_status", "subject"]})
    result[f"{GENERATED}/课程资料.base"] = yaml.safe_dump(course, allow_unicode=True, sort_keys=False, width=1000).encode("utf-8")
    for moc in sorted(moc_paths):
        topics = descendants(notes, moc) | {moc}
        basename = PurePosixPath(moc).stem
        digest = hashlib.sha256(moc.encode("utf-8")).hexdigest()[:12]
        base_path = f"{GENERATED}/topics/{digest}.base"
        filters = _typed_filter(root, "01_Knowledge", model.ATOMIC_TYPES)
        filters["and"].append({"or": [f"topics.contains(link({json.dumps(path[:-3], ensure_ascii=False)}))" for path in sorted(topics)]})
        result[base_path] = _base(f"{basename}：递归原子知识", filters, ["file.name", "type", "topics", "source", "tags"])
        content = f"## 主题知识\n\n动态汇集自身及全部下层主题的原子知识，每篇笔记显示一次。新增原子自动出现；主题层级变化后运行 views 更新递归范围。\n\n![[{base_path}]]\n".encode("utf-8")
        result[moc] = _replace_generated(notes[moc]["raw"], content)
    home_path = root / "Home.md"
    if home_path.is_symlink() or home_path.is_junction():
        raise ValueError("Home cannot be a linked file")
    home = home_path.read_bytes() if home_path.exists() else "# 知识库\n".encode("utf-8")
    content = f"""## 学科与主题

![[{GENERATED}/主题数据库.base]]

## 来源、课程与待处理

- [[{GENERATED}/来源管理.base|来源提炼状态]]
- [[{GENERATED}/课程资料.base|课程资料（含课件与跨课程复习）]]
- [[{GENERATED}/待处理.base|待处理来源与 Inbox]]
- [[{GENERATED}/标签数据库.base|标准标签与同义名称]]

## 日常维护

[[99_System/knowledge/v2/README|v2 使用与审计入口]] · [[docs/KNOWLEDGE_DAILY_GUIDE|日常提炼指南]]

来源 status 记录原子提炼进度；polish_status 单独记录课堂笔记润色进度。提炼由用户指令触发。
""".encode("utf-8")
    result["Home.md"] = _replace_generated(home, content)
    return result
