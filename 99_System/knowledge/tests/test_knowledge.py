import importlib,sys,tempfile,unittest,json
from pathlib import Path
SYSTEM=Path(__file__).resolve().parents[1];sys.path.insert(0,str(SYSTEM))
class KnowledgeTests(unittest.TestCase):
 def setUp(self):
  self.assertTrue((SYSTEM/"knowledge.py").exists(),"daily entry missing")
  self.k=importlib.import_module("knowledge");self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.base=Path(self.tmp.name);self.root=self.base/"vault";self.root.mkdir()
 def test_new_note_uses_registry_template_and_only_plans(self):
  report=self.k.new_note(self.root,"概念/新对象.md","concept",self.base/"backup",[])
  self.assertFalse((self.root/"概念/新对象.md").exists())
  plan=json.loads(Path(report["plan"]).read_text("utf-8"));raw=(self.base/"backup/payload/0000.bin").read_bytes()
  self.assertIn("# 新对象",raw.decode("utf-8"));self.assertNotIn("{{title}}",raw.decode("utf-8"))
  result=self.k.maintenance.v.validate_note(raw,"概念/新对象.md",self.k.maintenance.v.load_system(SYSTEM))
  self.assertEqual(result["classification"],"valid")
 def test_existing_note_and_missing_topic_are_refused(self):
  p=self.root/"概念/A.md";p.parent.mkdir();p.write_text("user",encoding="utf-8")
  with self.assertRaises(ValueError):self.k.new_note(self.root,"概念/A.md","concept",self.base/"backup",[])
  with self.assertRaises(ValueError):self.k.new_note(self.root,"概念/B.md","concept",self.base/"backup",["概念/不存在.md"])
  self.assertEqual(p.read_text("utf-8"),"user")
