"""Daily entry: Registry templates, existing audits, advisory, reviewed change plans."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
import argparse,base64,json,re
from pathlib import Path
import maintenance
import change_control
SYSTEM=Path(__file__).resolve().parent
def new_note(root,name,kind,backup_dir,topics):
    root=Path(root).resolve();system=maintenance.v.load_system(SYSTEM)
    path=change_control.destination(root,name)
    if path.exists():raise ValueError("Existing note is never overwritten")
    if kind not in system.registry["profiles"] or not name.endswith(".md"):raise ValueError("Registered note type and Markdown path required")
    template=system.root/system.registry["profiles"][kind]["template"]
    text=template.read_text("utf-8-sig").replace("{{title}}",Path(name).stem)
    index=maintenance.links.build_index(root,system,namespace_only=True) if topics else None
    values=[]
    for target in topics:
        change_control.destination(root,target)
        if target not in index.files or not target.endswith(".md"):raise ValueError("Topic must be an existing Markdown target")
        wiki="[["+target[:-3]+"]]"
        if wiki not in values:values.append(wiki)
    text=text.replace("topics: []","topics: "+("[]" if not values else "")+"".join("\n  - "+json.dumps(x,ensure_ascii=False) for x in values),1)
    raw=text.encode("utf-8")
    result=maintenance.v.validate_note(raw,name,system,"v1")
    if result["classification"]!="valid":raise ValueError("Generated template failed the existing Schema")
    if index:
        maintenance.topic_policy.require(raw,name,index,system)
        links=maintenance.links.audit_links(raw,name,index,system)
        if any(row["status"]!="resolved" for row in links):raise ValueError("Generated topic link is not uniquely resolved")
    return change_control.plan(root,[{"path":name,"expected_sha256":None,"content_base64":base64.b64encode(raw).decode(),"reason":"New registered template; review before creation"}],backup_dir)
def main(argv=None):
    argv=list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0]=="v2":
        from v2 import cli
        return cli.main(argv[1:])
    if argv and argv[0] in ("audit","plan","apply","restore","advisory","check","check-system"):
        command=argv[0];rest=argv[1:]
        if command=="advisory":
            import advisory;return advisory.main(rest)
        if command in ("plan","apply","restore"):return change_control.main([command]+rest)
        if command=="audit":return maintenance.main([command]+rest)
        return maintenance.v.main([command]+rest)
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest="command",required=True)
    p=sub.add_parser("new");p.add_argument("--vault-root",type=Path,required=True);p.add_argument("--path",required=True)
    p.add_argument("--type",choices=("concept","proposition","method","moc"),required=True)
    p.add_argument("--backup-dir",type=Path,required=True);p.add_argument("--topic",action="append",default=[])
    args=parser.parse_args(argv)
    try:print(json.dumps(new_note(args.vault_root,args.path,args.type,args.backup_dir,args.topic),ensure_ascii=False,indent=2));return 0
    except (ValueError,KeyError,OSError,maintenance.v.yaml.YAMLError) as error:
        print(json.dumps({"ok":False,"error":str(error)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8");sys.stderr.reconfigure(encoding="utf-8");raise SystemExit(main())
