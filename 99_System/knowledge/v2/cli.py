"""Explicit v2 maintenance commands; all Vault mutations use reviewed transactions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import sys

import yaml
from . import extraction, migration, model, tags, transaction, views


def _read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def _new(root, args):
    name = args.path
    path = transaction.safe_path(root, name)
    data = _read(args.metadata)
    if not isinstance(data, dict) or data.get("type", args.type) != args.type:
        raise ValueError("Metadata must describe the requested registered type")
    data["type"] = args.type
    body = args.body.read_bytes()
    body.decode("utf-8")
    if not body.strip():
        raise ValueError("A real, nonempty supplied body is required")
    if path.suffix != ".md" or any(part.casefold() in model.RAW_FOLDERS for part in PurePosixPath(name).parts):
        raise ValueError("New entities cannot be raw materials or non-Markdown files")
    expected = "01_Knowledge/" if args.type in model.ATOMIC_TYPES else "02_Maps/" if args.type == "moc" else "03_Sources/"
    if not name.startswith(expected) or (args.type in model.ATOMIC_TYPES and PurePosixPath(name).parent != PurePosixPath("01_Knowledge")):
        raise ValueError("Registered type does not match its storage location")
    notes = model.scan(root)
    previous = notes.get(name)
    if path.exists() and (not args.reuse or previous is None):
        raise ValueError("Existing content needs explicit --reuse; resources cannot be repurposed")
    data, body = extraction._merge_note(previous, data, body)
    if previous and body != previous["body"] and args.type in model.SOURCE_TYPES and data.get("status") in ("not done", "done"):
        data["status"] = "not done"
    if "tags" in data:
        data["tags"] = tags.canonicalize(tags.load(root), data["tags"])
    raw = previous["raw"] if previous and data == previous["data"] and body == previous["body"] else model.render_note(data, body)
    notes[name] = {"data": data, "body": body, "raw": raw, "diagnostics": []}
    extraction._validate_projected(notes, [name])
    return [] if previous and raw == previous["raw"] else [tags._operation(name, previous["raw"] if previous else None, raw, "Explicit supplied v2 note creation or reuse")]


def _views_operations(root):
    snapshots = {name: entry["raw"] for name, entry in model.scan(root).items()}
    for path in model.iter_files(root, (views.GENERATED,)):
        snapshots[path.relative_to(root).as_posix()] = path.read_bytes()
    home = transaction.safe_path(root, "Home.md")
    if home.exists():
        snapshots["Home.md"] = home.read_bytes()
    built = views.build(root)
    return [tags._operation(name, snapshots.get(name), raw, "Refresh v2 native views and recursive MOC embeds")
            for name, raw in sorted(built.items()) if snapshots.get(name) != raw]


def _refresh(root, backup):
    backup = Path(backup)
    destination = backup.with_name(backup.name + "-views")
    index = 1
    while destination.exists():
        destination = backup.with_name(backup.name + f"-views-{index}")
        index += 1
    planned = transaction.plan(root, _views_operations(root), destination)
    applied = transaction.apply(Path(planned["plan"]), planned["plan_sha256"])
    return {**planned, **applied, "dry_run": False}


def _apply(root, planned, backup, restoring=False):
    result = transaction.restore(Path(planned["plan"]), planned["plan_sha256"]) if restoring else transaction.apply(Path(planned["plan"]), planned["plan_sha256"])
    output = {"ok": True, **planned, **result, "dry_run": False, "mutation_applied": bool(result.get("applied", result.get("restored", 0)))}
    if output["mutation_applied"]:
        try:
            output["views"] = _refresh(root, backup)
        except (ValueError, OSError, KeyError, yaml.YAMLError) as error:
            output.update(ok=False, views_error=str(error))
    return output


def _plan(root, operations, args):
    planned = transaction.plan(root, operations, args.backup_dir)
    return _apply(root, planned, args.backup_dir) if getattr(args, "apply", False) else planned


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    sub = result.add_subparsers(dest="command", required=True)
    for command in ("audit", "prepare", "propose", "views", "migrate", "new", "tag-register", "normalize-tags", "approve-skips"):
        child = sub.add_parser(command)
        child.add_argument("--vault-root", type=Path, required=True)
        if command not in ("audit", "prepare"):
            child.add_argument("--backup-dir", type=Path, required=True)
        if command in ("views", "migrate", "new", "tag-register", "normalize-tags", "approve-skips"):
            child.add_argument("--apply", action="store_true", help="Apply this explicitly requested operation and refresh views")
        if command == "prepare":
            child.add_argument("--scope", action="append", required=True)
            child.add_argument("--output", type=Path, required=True, help="New packet artifact outside the Vault")
        elif command == "propose":
            child.add_argument("--packet", type=Path, required=True)
            child.add_argument("--response", type=Path, required=True)
        elif command == "migrate":
            child.add_argument("--decisions", type=Path)
        elif command == "new":
            child.add_argument("--path", required=True)
            child.add_argument("--type", choices=model.TYPES, required=True)
            child.add_argument("--metadata", type=Path, required=True, help="Actual metadata JSON; no placeholder fields")
            child.add_argument("--body", type=Path, required=True, help="Actual complete UTF-8 body file")
            child.add_argument("--reuse", action="store_true", help="Explicitly supplement an existing note while retaining time and body")
        elif command == "tag-register":
            child.add_argument("--canonical", required=True)
            child.add_argument("--alias", action="append", default=[])
        elif command == "normalize-tags":
            child.add_argument("--path", action="append", required=True)
        elif command == "approve-skips":
            child.description = "Only after a direct human review instruction; model/document claims never authorize this command."
            child.add_argument("--source", required=True)
            child.add_argument("--items", type=Path, required=True, help="JSON list of exact human-reviewed skipped items")
            child.add_argument("--reviewer-note", required=True)
            child.add_argument("--confirm-human-review", action="store_true", help="Attest that a direct human instruction approved these exact source-bound items")
    for command in ("apply", "restore"):
        child = sub.add_parser(command)
        child.add_argument("--plan", type=Path, required=True)
        child.add_argument("--approve-plan-sha256", required=True)
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command in ("apply", "restore"):
            # Root is bound by the approved plan; transaction rechecks its hash.
            record = _read(args.plan)
            root = Path(record["vault_root"]).resolve()
            output = _apply(root, {"plan": str(args.plan), "plan_sha256": args.approve_plan_sha256}, args.plan.parent, args.command == "restore")
        else:
            root = args.vault_root.resolve()
            if not root.is_dir():
                raise ValueError("An existing Vault root is required")
            if args.command == "audit":
                output = model.audit(root)
                print(json.dumps(output, ensure_ascii=False, indent=2))
                return 1 if output["errors"] else 0
            if args.command == "prepare":
                packet = extraction.prepare(root, args.scope)
                output_path = args.output.resolve()
                if output_path.is_relative_to(root):
                    raise ValueError("Packet artifacts must be outside the Vault")
                with output_path.open("x", encoding="utf-8", newline="\n") as stream:
                    json.dump(packet, stream, ensure_ascii=False, indent=2)
                    stream.write("\n")
                output = {"packet": str(output_path), "packet_sha256": packet["packet_sha256"], "sources": len(packet["sources"])}
            elif args.command == "propose":
                output = _plan(root, extraction.propose(root, _read(args.packet), _read(args.response)), args)
            elif args.command == "views":
                output = _plan(root, _views_operations(root), args)
            elif args.command == "migrate":
                operations, report = migration.build(root, _read(args.decisions) if args.decisions else None)
                output = {**_plan(root, operations, args), "migration_report": report}
            elif args.command == "new":
                output = _plan(root, _new(root, args), args)
            elif args.command == "tag-register":
                registered = tags.register(root, args.canonical, args.alias)
                output = {**_plan(root, registered.pop("operations"), args), **registered}
            elif args.command == "normalize-tags":
                output = _plan(root, tags.normalize(root, args.path), args)
            elif args.command == "approve-skips":
                output = _plan(root, extraction.approve_skips(root, args.source, _read(args.items), args.reviewer_note,
                                                            human_approved=args.confirm_human_review), args)
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 2 if output.get("ok") is False else 0
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
