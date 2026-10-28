"""Explicit plan/diff/backup/apply/restore for operator-reviewed changes; never executes AI output."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
import argparse,base64,difflib,hashlib,json,os,re
from pathlib import Path
import maintenance
v=maintenance.v
links=maintenance.links
PREFIXES=("概念","知识点","方法","总览","99_System/knowledge","docs")
CORE=("概念","知识点","方法")
def sha(raw):return hashlib.sha256(raw).hexdigest()
def body(raw):
    lines=raw.splitlines(keepends=True)
    if not lines or lines[0].lstrip(b"\xef\xbb\xbf").strip()!=b"---":return raw
    for i,line in enumerate(lines[1:],1):
        if line.strip()==b"---":return b"".join(lines[i+1:])
    raise ValueError("Unclosed frontmatter")
def destination(root,name):
    if not isinstance(name,str) or "\\" in name or ":" in name or name.startswith("/") or any(x in ("",".","..") for x in name.split("/")):
        raise ValueError("Non-canonical relative path")
    parts=name.split("/")
    if any(part.rstrip(" .")!=part or re.search(r'[<>:"|?*\x00-\x1f]',part) or re.fullmatch(r"(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?",part) for part in parts):
        raise ValueError("Windows path aliases/device names are forbidden")
    if not any(name==x or name.startswith(x+"/") for x in PREFIXES):
        raise ValueError("Path is outside maintenance allowlist")
    path=root/name
    if links.protected_reason(root,path):raise ValueError("Protected, linked or independent-repository path")
    return path
def _read_json(path):
    path=Path(path)
    if path.stat().st_size>32*1024*1024:raise ValueError("Plan input too large")
    return json.loads(path.read_text("utf-8-sig"))
def plan(root,changes,backup_dir):
    root=Path(root).resolve();backup=Path(backup_dir).absolute()
    if not root.is_dir() or backup.resolve().is_relative_to(root) or root.is_relative_to(backup.resolve()):
        raise ValueError("Backup must be separate from and not contain the Vault")
    if backup.exists() or not isinstance(changes,list) or not changes:raise ValueError("Use a new batch directory and explicit changes")
    # Validate every row before creating artifacts.
    rows=[];seen=set();topic_index=None;system=v.load_system(maintenance.SYSTEM)
    for item in changes:
        if not isinstance(item,dict) or set(item)!={"path","expected_sha256","content_base64","reason"}:raise ValueError("Invalid change record")
        name=item["path"];path=destination(root,name)
        if name.casefold() in seen:raise ValueError("Duplicate change path")
        seen.add(name.casefold())
        expected=item["expected_sha256"]
        if expected is not None and (not isinstance(expected,str) or not re.fullmatch("[0-9a-f]{64}",expected)):raise ValueError("Invalid expected hash")
        after=base64.b64decode(item["content_base64"],validate=True)
        if len(after)>4*1024*1024:raise ValueError("Payload too large")
        before=path.read_bytes() if path.exists() else None
        current=sha(before) if before is not None else None
        if current!=expected:
            rows.append({"path":name,"status":"conflict_skipped","expected_sha256":expected,"observed_sha256":current});continue
        if before==after:continue
        if before is not None and name.split("/")[0] in CORE and name.casefold().endswith(".md") and body(before)!=body(after):
            raise ValueError("Existing core note body must remain byte-identical")
        if maintenance.topic_policy.applies(after,name,system):
            if topic_index is None:topic_index=links.build_index(root,system,namespace_only=True)
            maintenance.topic_policy.require(after,name,topic_index,system)
        rows.append({"path":name,"status":"planned","before_sha256":current,"after_sha256":sha(after),
                     "reason":item["reason"],"_before":before,"_after":after})
    backup.mkdir(parents=True)
    (backup/"original").mkdir();(backup/"payload").mkdir()
    entries=[];diffs=[]
    for i,row in enumerate(rows):
        if row["status"]!="planned":entries.append(row);continue
        before=row.pop("_before");after=row.pop("_after");key=f"{i:04d}.bin"
        if before is not None:(backup/"original"/key).write_bytes(before)
        (backup/"payload"/key).write_bytes(after)
        row["key"]=key;entries.append(row)
        diffs.extend(difflib.unified_diff((before or b"").decode("utf-8-sig").splitlines(True),after.decode("utf-8-sig").splitlines(True),fromfile=row["path"],tofile=row["path"]))
    record={"plan_version":1,"vault_root":str(root),"entries":entries}
    raw=json.dumps(record,ensure_ascii=False,indent=2).encode("utf-8")
    (backup/"plan.json").write_bytes(raw);(backup/"change.diff").write_text("".join(diffs),encoding="utf-8")
    return {"dry_run":True,"plan":str(backup/"plan.json"),"plan_sha256":sha(raw),"planned":sum(x["status"]=="planned" for x in entries),"conflicts":sum(x["status"]!="planned" for x in entries)}
def _load(plan_path,approved):
    path=Path(plan_path).absolute();raw=path.read_bytes()
    if sha(raw)!=approved:raise ValueError("Exact approved plan SHA-256 required")
    if len(raw)>32*1024*1024:raise ValueError("Plan input too large")
    record=json.loads(raw.decode("utf-8-sig"));root=Path(record["vault_root"]).resolve()
    if record.get("plan_version")!=1 or path.resolve().is_relative_to(root):raise ValueError("Invalid plan placement/version")
    seen=set();payloads={};originals={}
    for row in record["entries"]:
        destination(root,row["path"])
        if row["path"].casefold() in seen:raise ValueError("Duplicate plan path")
        seen.add(row["path"].casefold())
        if row["status"]!="planned":continue
        if not re.fullmatch(r"[0-9]{4}\.bin",row["key"]):raise ValueError("Invalid backup key")
        payload=(path.parent/"payload"/row["key"]).read_bytes()
        if sha(payload)!=row["after_sha256"]:raise ValueError("Payload hash mismatch")
        payloads[row["key"]]=payload
        if row["before_sha256"] is not None:
            original=(path.parent/"original"/row["key"]).read_bytes()
            if sha(original)!=row["before_sha256"]:raise ValueError("Original backup hash mismatch")
            originals[row["key"]]=original
            if row["path"].split("/")[0] in CORE and row["path"].casefold().endswith(".md") and body(original)!=body(payload):raise ValueError("Core body change")
    return path,record,root,payloads,originals
class UnsafeFileError(ValueError):pass

def _safe_stream(path,disposition,delete_access=False,strict_path=False):
    # Fail closed on platforms without the required mandatory Windows sharing guard.
    if os.name!="nt":raise OSError("Writes require the Windows exclusive file guard")
    import ctypes as ct
    from ctypes import wintypes as wt
    import msvcrt
    kernel=ct.WinDLL("kernel32",use_last_error=True)
    create=kernel.CreateFileW;create.argtypes=[wt.LPCWSTR,wt.DWORD,wt.DWORD,ct.c_void_p,wt.DWORD,wt.DWORD,wt.HANDLE];create.restype=wt.HANDLE
    close=kernel.CloseHandle;close.argtypes=[wt.HANDLE];close.restype=wt.BOOL
    class Info(ct.Structure):
        _fields_=[("attributes",wt.DWORD),("creation",wt.FILETIME),("access",wt.FILETIME),("write",wt.FILETIME),("volume",wt.DWORD),("high",wt.DWORD),("low",wt.DWORD),("links",wt.DWORD),("index_high",wt.DWORD),("index_low",wt.DWORD)]
    info_fn=kernel.GetFileInformationByHandle;info_fn.argtypes=[wt.HANDLE,ct.POINTER(Info)];info_fn.restype=wt.BOOL
    name_fn=kernel.GetFinalPathNameByHandleW;name_fn.argtypes=[wt.HANDLE,wt.LPWSTR,wt.DWORD,wt.DWORD];name_fn.restype=wt.DWORD
    path=Path(path).absolute()
    handle=create(str(path),0x80000000|0x40000000|(0x10000 if delete_access else 0),0,None,disposition,0x80|0x00200000,None)
    if handle==ct.c_void_p(-1).value:raise ct.WinError(ct.get_last_error())
    try:
        info=Info()
        if not info_fn(handle,ct.byref(info)):raise ct.WinError(ct.get_last_error())
        if info.attributes & (0x400|0x10) or info.links!=1:raise UnsafeFileError("Linked/reparse/directory file refused")
        buffer=ct.create_unicode_buffer(32768);length=name_fn(handle,buffer,len(buffer),0)
        if not length or length>=len(buffer):raise UnsafeFileError("Cannot verify final handle path")
        actual=buffer.value
        if actual.startswith("\\\\?\\UNC\\"):actual="\\\\"+actual[8:]
        elif actual.startswith("\\\\?\\"):actual=actual[4:]
        expected=path if strict_path else path.resolve()
        if os.path.normcase(os.path.normpath(actual))!=os.path.normcase(str(expected)):raise UnsafeFileError("Handle path changed")
        fd=msvcrt.open_osfhandle(handle,os.O_RDWR|os.O_BINARY);handle=None
        return os.fdopen(fd,"r+b",buffering=0)
    finally:
        if handle is not None:close(handle)

def _write_all(stream,raw):
    remaining=memoryview(raw)
    while remaining:
        count=stream.write(remaining)
        if not count:raise OSError("Short write")
        remaining=remaining[count:]

def _replace(path,raw,expected):
    path.parent.mkdir(parents=True,exist_ok=True)
    try:stream=_safe_stream(path,1 if expected is None else 3) # CREATE_NEW / OPEN_EXISTING
    except UnsafeFileError:return False
    except OSError as error:
        if getattr(error,"winerror",None) in (2,3,5,32,33,80,183):return False
        raise
    with stream:
        current=stream.read(4*1024*1024+1)
        if expected is not None and sha(current)!=expected:return False
        if expected is None and current:raise UnsafeFileError("New file is not empty")
        stream.seek(0);_write_all(stream,raw);stream.truncate(len(raw));stream.flush();os.fsync(stream.fileno())
        stream.seek(0)
        if sha(stream.read(len(raw)+1))!=sha(raw):raise OSError("Write verification failed")
        return True

def _journal(path,row):
    # OPEN_ALWAYS without truncation; mandatory sharing and link checks precede the first byte.
    with _safe_stream(path,4) as stream:
        stream.seek(0,os.SEEK_END)
        _write_all(stream,(json.dumps(row,ensure_ascii=False)+"\n").encode("utf-8"))
        stream.flush();os.fsync(stream.fileno())
def _execute(plan_path,approved,restore_mode):
    path,record,root,payloads,originals=_load(plan_path,approved);results=[]
    topic_index=None;system=v.load_system(maintenance.SYSTEM)
    for row in record["entries"]:
        if row["status"]!="planned":results.append({"path":row["path"],"status":"conflict_skipped"});continue
        if restore_mode and row["before_sha256"] is None:
            results.append({"path":row["path"],"status":"preserved_addition"});continue
        target=destination(root,row["path"])
        expected=row["after_sha256"] if restore_mode else row["before_sha256"]
        raw=(originals if restore_mode else payloads)[row["key"]]
        if not restore_mode and maintenance.topic_policy.applies(raw,row["path"],system):
            if topic_index is None:topic_index=links.build_index(root,system,namespace_only=True)
            try:maintenance.topic_policy.require(raw,row["path"],topic_index,system)
            except ValueError as error:
                result={"path":row["path"],"status":"policy_skipped","error":str(error)}
                results.append(result);_journal(path.parent/"journal.jsonl",result);continue
        _journal(path.parent/"journal.jsonl",{"path":row["path"],"operation":"restore" if restore_mode else "apply","expected_sha256":expected,"state":"intent"})
        try:
            done=_replace(target,raw,expected)
            result={"path":row["path"],"status":("restored" if restore_mode else "applied") if done else "conflict_skipped"}
        except OSError as error:
            result={"path":row["path"],"status":"write_failed","error":str(error)}
        results.append(result);_journal(path.parent/"journal.jsonl",result)
    return {"policy_skipped":sum(x["status"]=="policy_skipped" for x in results),"failed":sum(x["status"]=="write_failed" for x in results),"applied":sum(x["status"]=="applied" for x in results),"restored":sum(x["status"]=="restored" for x in results),"conflicts":sum(x["status"]=="conflict_skipped" for x in results),"preserved_additions":sum(x["status"]=="preserved_addition" for x in results),"results":results}
def apply(plan_path,approved):return _execute(plan_path,approved,False)
def restore(plan_path,approved):return _execute(plan_path,approved,True)
def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest="command",required=True)
    p=sub.add_parser("plan");p.add_argument("--vault-root",type=Path,required=True);p.add_argument("--changes",type=Path,required=True);p.add_argument("--backup-dir",type=Path,required=True)
    for name in ("apply","restore"):
        p=sub.add_parser(name);p.add_argument("--plan",type=Path,required=True);p.add_argument("--approve-plan-sha256",required=True)
    args=parser.parse_args(argv)
    try:
        if args.command=="plan":result=plan(args.vault_root,_read_json(args.changes)["items"],args.backup_dir)
        else:result=(apply if args.command=="apply" else restore)(args.plan,args.approve_plan_sha256)
        print(json.dumps(result,ensure_ascii=False,indent=2));return 1 if result.get("conflicts",0) or result.get("failed",0) or result.get("policy_skipped",0) else 0
    except (ValueError,KeyError,TypeError,OSError,UnicodeError) as error:
        print(json.dumps({"ok":False,"error":str(error)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=="__main__":
    sys.stdout.reconfigure(encoding="utf-8");sys.stderr.reconfigure(encoding="utf-8");raise SystemExit(main())
