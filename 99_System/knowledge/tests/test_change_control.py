import base64,hashlib,importlib,sys,tempfile,unittest,json
from pathlib import Path
SYSTEM=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(SYSTEM))
class ChangeControlTests(unittest.TestCase):
 def setUp(self):
  self.assertTrue((SYSTEM/"change_control.py").exists(),"safe maintenance implementation missing")
  self.c=importlib.import_module("change_control")
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.base=Path(self.tmp.name);self.root=self.base/"vault";self.root.mkdir();self.back=self.base/"back"
  self.p=self.root/"概念/A.md";self.p.parent.mkdir();self.raw=b"---\r\ntype: old\r\n---\r\nBody\r\n";self.p.write_bytes(self.raw)
 def change(self,content=None):
  raw=content or b"---\r\nschema_version: 1\r\ntype: concept\r\n---\r\nBody\r\n"
  return {"path":"概念/A.md","expected_sha256":hashlib.sha256(self.raw).hexdigest(),"content_base64":base64.b64encode(raw).decode(),"reason":"synthetic explicit review"}
 def test_plan_never_changes_note_and_restore_is_byte_exact(self):
  report=self.c.plan(self.root,[self.change()],self.back)
  self.assertEqual(self.p.read_bytes(),self.raw)
  self.assertTrue((self.back/"change.diff").read_text("utf-8"))
  result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["applied"],1)
  restored=self.c.restore(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(restored["restored"],1);self.assertEqual(self.p.read_bytes(),self.raw)
 def test_concurrent_edit_skips_apply_and_restore(self):
  report=self.c.plan(self.root,[self.change()],self.back)
  self.p.write_bytes(b"user edit")
  result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["conflicts"],1);self.assertEqual(self.p.read_bytes(),b"user edit")
 def test_body_changes_and_outside_paths_and_in_vault_backup_are_refused(self):
  with self.assertRaises(ValueError):self.c.plan(self.root,[self.change(b"---\ntype: concept\n---\nCHANGED")],self.back)
  item=self.change();item["path"]="../secret.md"
  with self.assertRaises(ValueError):self.c.plan(self.root,[item],self.back)
  with self.assertRaises(ValueError):self.c.plan(self.root,[self.change()],self.root/"backup")
  item=self.change();item["path"]="数学建模/x.md"
  with self.assertRaises(ValueError):self.c.plan(self.root,[item],self.back)
 def test_payload_tamper_and_wrong_approval_are_refused(self):
  report=self.c.plan(self.root,[self.change()],self.back)
  with self.assertRaises(ValueError):self.c.apply(self.back/"plan.json","0"*64)
  (self.back/"payload/0000.bin").write_bytes(b"tamper")
  with self.assertRaises(ValueError):self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(self.p.read_bytes(),self.raw)
 def test_new_files_are_not_deleted_by_restore(self):
  item={"path":"总览/New.md","expected_sha256":None,"content_base64":base64.b64encode(b"# New").decode(),"reason":"new navigation"}
  report=self.c.plan(self.root,[item],self.back);self.c.apply(self.back/"plan.json",report["plan_sha256"])
  result=self.c.restore(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["preserved_additions"],1);self.assertEqual((self.root/"总览/New.md").read_bytes(),b"# New")

 def test_windows_aliases_cannot_bypass_core_body_guard(self):
  item=self.change(b"---\ntype: concept\n---\nCHANGED")
  item["path"]="概念/A.MD"
  with self.assertRaises(ValueError):self.c.plan(self.root,[item],self.back)
  for name in ["概念/A.md.","概念/A.md ","概念./A.md"]:
   with self.assertRaises(ValueError):self.c.destination(self.root,name)
 def test_validated_payload_bytes_are_not_reopened_for_write(self):
  from unittest.mock import patch
  report=self.c.plan(self.root,[self.change()],self.back);load=self.c._load
  approved=(self.back/"payload/0000.bin").read_bytes()
  def swap(*args):
   result=load(*args);(self.back/"payload/0000.bin").write_bytes(b"UNAPPROVED BODY");return result
  with patch.object(self.c,"_load",side_effect=swap):result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["applied"],1);self.assertEqual(self.p.read_bytes(),approved)
 def test_plan_is_parsed_from_the_same_approved_bytes(self):
  from unittest.mock import patch
  report=self.c.plan(self.root,[self.change()],self.back)
  record=json.loads((self.back/"plan.json").read_text("utf-8"));record["entries"]=[]
  with patch.object(self.c,"_read_json",return_value=record):
   result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["applied"],1)
 def test_journal_hardlink_never_writes_into_note(self):
  import os
  report=self.c.plan(self.root,[self.change()],self.back)
  os.link(self.p,self.back/"journal.jsonl")
  with self.assertRaises((ValueError,OSError)):self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(self.p.read_bytes(),self.raw)
 def test_exclusive_guard_prevents_concurrent_writer(self):
  from unittest.mock import patch
  report=self.c.plan(self.root,[self.change()],self.back)
  original=self.c._replace
  def guarded(path,raw,expected):
   with self.p.open("r+b") as held:
    return original(path,raw,expected)
  with patch.object(self.c,"_replace",side_effect=guarded):
   result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["conflicts"],1);self.assertEqual(self.p.read_bytes(),self.raw)
 def test_hardlinked_target_is_skipped(self):
  import os
  report=self.c.plan(self.root,[self.change()],self.back);other=self.base/"protected-note.md";os.link(self.p,other)
  result=self.c.apply(self.back/"plan.json",report["plan_sha256"])
  self.assertEqual(result["conflicts"],1);self.assertEqual(other.read_bytes(),self.raw)
