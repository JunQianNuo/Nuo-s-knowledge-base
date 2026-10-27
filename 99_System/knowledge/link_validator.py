"""Conservative static link auditing, independent of Obsidian's runtime resolver."""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True

from collections import Counter
from dataclasses import dataclass, replace
import importlib.util
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


SYSTEM = Path(__file__).resolve().parent


def _module(name, path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


v = _module("knowledge_validator", SYSTEM / "validator.py")
MD = MarkdownIt("commonmark")
# Auditing only: retain even file:/javascript: destinations to report unchecked.
# No rendering, navigation, URI retrieval or embedded media execution occurs.
MD.validateLink = lambda destination: True
STATUSES = ("resolved", "ambiguous", "unresolved", "unchecked", "invalid_syntax")
SKIP_DIRS = {"node_modules", "venv", "__pycache__", "raw"}
ATTACHMENTS = {".pdf", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".mp3", ".mp4", ".wav", ".pptx", ".docx", ".base", ".canvas", ".zip"}


def _escaped(text, start):
    count = 0
    while start > 0 and text[start - 1] == "\\":
        start -= 1; count += 1
    return count % 2 == 1


def _blank(text):
    return "".join(char if char in "\r\n" else " " for char in text)


def _opaque(text):
    # Spaces here could turn a following real link into an indented code block.
    return "".join(char if char in "\r\n" else "X" for char in text)


def _comments(text, original=None):
    original = text if original is None else original
    chars = list(original)
    for match in re.finditer(r"(?s)%%.*?%%|<!--.*?-->", text):
        start, end = match.span()
        line_start = text.rfind("\n", 0, start) + 1
        line_end = text.find("\n", end)
        line_end = len(text) if line_end < 0 else line_end
        alone = not text[line_start:start].strip() and not text[end:line_end].strip()
        chars[start:end] = (_blank if alone else _opaque)(original[start:end])
    return "".join(chars)


def _code_text(body):
    """Code must be masked before looking for comment or math delimiters."""
    masked = body
    offsets = [0]
    for line in masked.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    chars = list(masked)
    for token in MD.parse(masked):
        if token.type in ("fence", "code_block", "html_block") and token.map:
            start, end = token.map
            a, b = offsets[start], offsets[min(end, len(offsets) - 1)]
            chars[a:b] = _blank(masked[a:b])
    masked = "".join(chars)
    # CommonMark code spans use matching-length backtick runs, including newlines.
    i = 0; chars = list(masked)
    while i < len(masked):
        if masked[i] != "`" or _escaped(masked, i):
            i += 1; continue
        match = re.match(r"`+", masked[i:]); size = len(match[0])
        closing = re.search(r"(?<!`)" + "`" * size + r"(?!`)", masked[i + size:])
        if closing:
            end = i + size + closing.end()
            chars[i:end] = _opaque(masked[i:end]); i = end
        else:
            i += size
    return "".join(chars)


def _active_text(body):
    """Mask code/comments/math without changing character offsets or line breaks."""
    masked = _comments(_code_text(body)); chars = list(masked); i = 0
    while i < len(masked):
        if masked[i] != "$" or _escaped(masked, i):
            i += 1; continue
        delimiter = "$$" if masked.startswith("$$", i) else "$"
        end = i + len(delimiter)
        while True:
            end = masked.find(delimiter, end)
            if end < 0 or not _escaped(masked, end):
                break
            end += len(delimiter)
        if end >= 0 and (len(delimiter) == 2 or "\n" not in masked[i:end]):
            end += len(delimiter); chars[i:end] = _opaque(masked[i:end]); i = end
        else:
            i += len(delimiter)
    return "".join(chars)


def _parts(raw):
    metadata = v.parse_frontmatter(raw)
    text = raw.decode("utf-8-sig")
    if metadata is None:
        return {}, text, 0
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines[1:], 1):
        if re.fullmatch(r"---[ \t]*(?:\r?\n)?", line):
            return metadata, "".join(lines[i + 1:]), i + 1
    raise v.FrontmatterError("Missing closing frontmatter delimiter")


def _record(raw):
    metadata, body, _ = _parts(raw)
    headings = Counter()
    clean = _comments(_code_text(body), original=body)
    tokens = MD.parse(clean)
    for i, token in enumerate(tokens):
        if token.type == "heading_open" and i + 1 < len(tokens):
            inline = tokens[i + 1]
            plain = "".join(child.content for child in inline.children or [] if child.type in ("text", "code_inline"))
            for name in {inline.content.strip(), plain.strip()}:
                if name:headings[name.casefold()] += 1
    blocks = Counter(re.findall(r"(?m)(?:^|\s)\^([A-Za-z0-9-]+)[ \t]*\r?$", _active_text(body)))
    aliases = metadata.get("aliases", [])
    aliases = [x for x in aliases if isinstance(x, str)] if isinstance(aliases, list) else []
    return {"text_available": True, "headings": headings, "blocks": blocks, "aliases": aliases}


@dataclass
class Index:
    root: Path
    files: dict
    excluded: list
    errors: list

    @property
    def scope(self):
        return {"root": str(self.root), "target_namespace": "visible_files_except_exclusions", "excluded": self.excluded, "index_errors": self.errors}


def protected_reason(root, path):
    root = root.resolve(); path = path.absolute()
    if not path.resolve().is_relative_to(root):
        return "outside_vault"
    for current in (path, *path.parents):
        if current == root:
            break
        if current.is_symlink() or current.is_junction():
            return "symlink_or_junction"
        if current.is_dir() and (current / ".git").exists():
            return "independent_repository"
    return None


def build_index(root, system):
    root = Path(root).resolve()
    if not root.is_dir():
        raise v.ConfigurationError("Index root must be an existing directory")
    files = {}; excluded = []; errors = []
    for base, dirs, names in os.walk(root, followlinks=False, onerror=lambda error: errors.append(str(error))):
        parent = Path(base)
        kept = []
        for name in dirs:
            path = parent / name
            reason = protected_reason(root, path)
            if name.startswith(".") or name in SKIP_DIRS:
                reason = reason or "hidden_or_runtime_directory"
            if reason:
                excluded.append({"path": path.relative_to(root).as_posix(), "reason": reason})
            else:
                kept.append(name)
        dirs[:] = kept
        for name in names:
            path = parent / name; relative = path.relative_to(root).as_posix()
            reason = protected_reason(root, path)
            if name.startswith(".") or reason:
                excluded.append({"path": relative, "reason": reason or "hidden_file"}); continue
            record = {"text_available": False, "headings": {}, "blocks": {}, "aliases": []}
            if path.suffix.lower() == ".md":
                try:
                    record = _record(path.read_bytes())
                except (OSError, UnicodeError, ValueError, v.yaml.YAMLError, RecursionError) as error:
                    errors.append({"path": relative, "error_type": type(error).__name__})
            files[relative] = record
    return Index(root, files, excluded, errors)


def _new_link(source, syntax, raw, target, embed=False, field=None, line=None, column=None):
    return {"source": source, "syntax": syntax, "raw": raw, "target": target, "embed": embed, "field": field, "line": line, "column": column, "claim": "static_audit"}


def _wikilinks(text, source, line_offset=0, field=None):
    rows = []; spans = []; position = 0
    while True:
        start = text.find("[[", position)
        if start < 0:
            break
        position = start + 2
        if _escaped(text, start):
            continue
        end = text.find("]]", start + 2)
        if end < 0:
            newline = text.find("\n", start)
            end = len(text) if newline < 0 else newline
            inner = text[start + 2:end]; finish = end
            invalid = "unclosed_wikilink"
        else:
            finish = end + 2; inner = text[start + 2:end]
            invalid = "invalid_wikilink_target" if not inner.strip() or any(c in inner for c in "[]\r\n") else None
        embed = start > 0 and text[start - 1] == "!" and not _escaped(text, start - 1)
        actual_start = start - 1 if embed else start
        target = inner.split("|", 1)[0].rstrip("\\").strip()
        if not target:invalid = invalid or "empty_wikilink_target"
        row = _new_link(source, "wikilink", text[actual_start:finish], target, embed, field)
        if field is None:
            row["line"] = line_offset + text[:actual_start].count("\n") + 1
            row["column"] = actual_start - text.rfind("\n", 0, actual_start)
        if invalid:row["syntax_error"] = invalid
        rows.append(row); spans.append((actual_start, finish)); position = max(finish, start + 2)
    return rows, spans


def _metadata_links(value, source, field=""):
    rows = []
    if isinstance(value, dict):
        for name, item in value.items():
            if name not in ("title", "type", "role", "aliases", "tags"):
                rows.extend(_metadata_links(item, source, f"{field}/{name}".strip("/")))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            rows.extend(_metadata_links(item, source, f"{field}/{i}"))
    elif isinstance(value, str):
        rows.extend(_wikilinks(value, source, field=field)[0])
        if not rows and re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", value):
            rows.append(_new_link(source, "property_uri", value, value, field=field))
    return rows


def _resolve(row, index, system):
    row.update({"scope": index.scope, "candidates": [], "target_is_system": False})
    def outcome(status, basis, candidates=()):
        row.update({"status": status, "basis": basis, "candidates": sorted(candidates)})
        if len(candidates) == 1:
            row["target_is_system"] = v.is_system_path(next(iter(candidates)), system)
        return row
    if row.get("syntax_error"):
        return outcome("invalid_syntax", row["syntax_error"])
    raw = row["target"]
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", raw) or raw.startswith("//"):
        return outcome("unchecked", "external_or_uri_destination_not_retrieved")
    markdown = row["syntax"] == "markdown"
    if not markdown and re.search(r"%[0-9A-Fa-f]{2}", raw):
        # A Wiki filename is not a Markdown URI. Do not silently decode it or
        # claim which interpretation Obsidian will choose at runtime.
        candidates = set()
        for spelling in (raw, unquote(raw)):
            target = spelling.split("#", 1)[0]
            if not target:
                candidates.add(row["source"])
            else:
                forms = (target.casefold(), (target + ".md").casefold())
                candidates.update(path for path in index.files if path.casefold() in forms or ("/" not in target and PurePosixPath(path).name.casefold() in forms))
        return outcome("unchecked", "percent_encoded_wikilink_runtime_semantics_not_assumed", candidates)
    destination, separator, anchor = raw.partition("#")
    if markdown:
        destination, anchor = unquote(destination), unquote(anchor)
    if not destination:
        if separator or markdown:
            candidates = [row["source"]]; basis = "self_document_empty_or_fragment_uri"
        else:
            return outcome("invalid_syntax", "empty_destination")
    else:
        destination = destination.replace("\\", "/")
        if (markdown and not destination.startswith("/")) or destination.startswith(("./", "../")):
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(row["source"]), destination))
        else:
            destination = posixpath.normpath(destination.lstrip("/"))
        if destination == ".." or destination.startswith("../"):
            return outcome("unchecked", "outside_vault_not_read")
        if any(v._in_scope(destination, item["path"]) for item in index.excluded):
            return outcome("unchecked", "destination_in_excluded_scope")
        extension = PurePosixPath(destination).suffix.lower()
        explicit = extension in ATTACHMENTS or extension == ".md" or bool(extension and any(PurePosixPath(path).name.casefold() == PurePosixPath(destination).name.casefold() for path in index.files))
        forms = [destination] if explicit else [destination + ".md"]
        if markdown:
            candidates = [path for path in index.files if any(path.casefold() == form.casefold() for form in forms)]
            basis = "markdown_source_relative_or_explicit_root_path"
        elif "/" in destination:
            candidates = [path for path in index.files if any(path.casefold() == form.casefold() for form in forms)]
            basis = "explicit_or_relative_path"
            if not candidates:
                candidates = [path for path in index.files if any(path.casefold().endswith("/" + form.casefold()) for form in forms)]
                basis = "unique_path_suffix_candidate"
        else:
            candidates = [path for path in index.files if any(PurePosixPath(path).name.casefold() == form.casefold() for form in forms)]
            basis = "basename_candidates_md_preferred"
        if not candidates:
            aliases = [path for path, record in index.files.items() if any(a.casefold() == destination.casefold() for a in record["aliases"])]
            if aliases:
                return outcome("unchecked", "alias_only_candidate_is_not_a_file_destination", aliases)
            return outcome("unresolved", "not_found_in_static_index_only")
    if len(candidates) > 1:
        return outcome("ambiguous", basis, candidates)
    if separator and anchor:
        record = index.files.get(candidates[0], {})
        if not candidates[0].lower().endswith(".md") or not record.get("text_available"):
            return outcome("unchecked", "attachment_or_unreadable_fragment_not_checked", candidates)
        if "#" in anchor:
            return outcome("unchecked", "nested_heading_path_not_implemented", candidates)
        count = record["blocks"].get(anchor[1:], 0) if anchor.startswith("^") else record["headings"].get(anchor.casefold(), 0)
        if count == 0:
            return outcome("unresolved", "anchor_not_found_in_static_index_only", candidates)
        if count > 1:
            return outcome("ambiguous", "multiple_matching_anchors", candidates)
        basis += ";static_anchor_match"
    return outcome("resolved", basis, candidates)


def audit_links(raw, source, index, system):
    try:
        metadata, body, line_offset = _parts(raw)
    except (UnicodeError, ValueError, v.yaml.YAMLError, RecursionError):
        row = _new_link(source, "frontmatter", None, "", field="$frontmatter")
        row["syntax_error"] = "unreadable_encoding_or_frontmatter"
        return [_resolve(row, index, system)]
    # Self anchors use the exact bytes being audited, not a potentially older index.
    local_files = dict(index.files)
    local_files[source] = _record(raw)
    index = replace(index, files=local_files)
    active = _active_text(body)
    wiki, spans = _wikilinks(active, source, line_offset)
    # The mask is only for deciding whether a link is active. Text and targets
    # must always come from the original source, including $ and backticks.
    for row, (start, end) in zip(wiki, spans):
        original = body[start:end]
        parsed, _ = _wikilinks(original, source, field="$raw")
        row["raw"] = original
        if len(parsed) == 1 and parsed[0]["raw"] == original:
            row["target"] = parsed[0]["target"]
            if "syntax_error" in parsed[0]:row["syntax_error"] = parsed[0]["syntax_error"]
            else:row.pop("syntax_error", None)
        else:
            row["syntax_error"] = "unsupported_wikilink_boundary"
    rows = _metadata_links(metadata, source) + wiki
    chars = list(active)
    for start, end in spans:
        chars[start:end] = _opaque(active[start:end])
    markdown = "".join(chars)
    # Obsidian footnote markers must not become CommonMark reference-file links.
    markdown = re.sub(r"\[\^[^\]\r\n]+\]:?", lambda match: match[0] if _escaped(markdown, match.start()) else _opaque(match[0]), markdown)
    for token in MD.parse(markdown):
        for child in token.children or []:
            if child.type in ("link_open", "image"):
                target = child.attrGet("href" if child.type == "link_open" else "src") or ""
                rows.append(_new_link(source, "markdown", None, target, child.type == "image"))
    return [_resolve(row, index, system) for row in rows]
