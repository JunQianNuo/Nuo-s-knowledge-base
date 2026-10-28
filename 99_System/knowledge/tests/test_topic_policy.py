"""Topic targets are explicit role:moc notes; synthetic Vaults only."""
import base64, hashlib, json, sys, tempfile, unittest
from pathlib import Path

SYSTEM=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(SYSTEM))
import maintenance as m
import change_control as c
import knowledge as k
from test_advisory import AdvisoryFixture

class TopicPolicyTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.base=Path(self.tmp.name);self.root=self.base/'vault';self.root.mkdir()
  self.system=m.v.load_system(SYSTEM)
  self.put('概念/A.md',('''---
schema_version: 1
type: concept
topics: ["[[总览/T]]"]
---
Body
''').encode())
  self.put('总览/T.md',('''---
role: moc
---
# Route
''').encode())
 def put(self,path,raw):
  p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw);return raw
 def report(self):return m.audit(self.root,['概念'])
 def change(self,raw):
  p=self.root/'概念/A.md'
  return {'path':'概念/A.md','expected_sha256':c.sha(p.read_bytes()),'content_base64':base64.b64encode(raw).decode(),'reason':'test'}
 def test_explicit_moc_without_version_is_accepted(self):
  self.assertTrue(self.report()['ok'])
 def test_concept_target_is_error_even_when_link_resolves(self):
  self.put('总览/T.md',('''---
type: concept
---
# Object
''').encode())
  report=self.report();self.assertFalse(report['ok'])
  self.assertEqual(report['results'][0]['links'][0]['status'],'resolved')
 def test_historical_moc_requires_explicit_role(self):
  self.put('总览/T.md',('''---
type: MOC
---
# Route
''').encode())
  self.assertFalse(self.report()['ok'])
 def test_missing_target_is_not_valid_theme(self):
  (self.root/'总览/T.md').unlink();self.assertFalse(self.report()['ok'])
 def test_system_moc_is_not_eligible(self):
  self.put('99_System/knowledge/T.md',('''---
role: moc
---
# Test
''').encode())
  self.put('概念/A.md',('''---
type: concept
topics: ["[[99_System/knowledge/T]]"]
---
Body
''').encode())
  self.assertFalse(self.report()['ok'])
 def test_legacy_plain_topics_stay_compatible(self):
  self.put('概念/A.md','''---
type: 概念
topics: [旧关键词]
---
Body
'''.encode())
  self.assertTrue(self.report()['ok'])
 def test_new_rejects_concept_as_topic(self):
  self.put('总览/T.md',('''---
type: concept
---
# Object
''').encode())
  with self.assertRaises(ValueError):k.new_note(self.root,'概念/B.md','concept',self.base/'new',['总览/T.md'])
 def test_new_accepts_explicit_moc_without_writing_note(self):
  report=k.new_note(self.root,'概念/B.md','concept',self.base/'new',['总览/T.md'])
  self.assertEqual(report['planned'],1);self.assertFalse((self.root/'概念/B.md').exists())
 def test_plan_refuses_new_non_moc_topic(self):
  self.put('总览/T.md',('''---
type: concept
---
# Object
''').encode())
  raw=('''---
type: concept
topics: ["[[总览/T]]"]
---
Body
''').encode()
  with self.assertRaises(ValueError):c.plan(self.root,[self.change(raw)],self.base/'batch')
 def test_apply_rechecks_role_after_plan(self):
  raw=('''---
type: concept
topics: ["[[总览/T]]"]
---
Body
''').encode()
  report=c.plan(self.root,[self.change(raw)],self.base/'batch')
  original=(self.root/'概念/A.md').read_bytes()
  self.put('总览/T.md',('''---
type: concept
---
# Changed
''').encode())
  result=c.apply(report['plan'],report['plan_sha256'])
  self.assertEqual(result['applied'],0);self.assertEqual((self.root/'概念/A.md').read_bytes(),original)
 def test_restore_can_restore_historical_concept_topics(self):
  old=self.put('概念/A.md',('''---
type: concept
topics: ["[[概念/A]]"]
---
Body
''').encode())
  raw=('''---
type: concept
topics: ["[[总览/T]]"]
---
Body
''').encode()
  report=c.plan(self.root,[self.change(raw)],self.base/'batch')
  self.assertEqual(c.apply(report['plan'],report['plan_sha256'])['applied'],1)
  self.assertEqual(c.restore(report['plan'],report['plan_sha256'])['restored'],1)
  self.assertEqual((self.root/'概念/A.md').read_bytes(),old)

 def test_whole_note_index_preserves_ambiguity_and_paths(self):
  self.put('其他/T.md',b'# Other')
  index=m.links.build_index(self.root,self.system,namespace_only=True)
  rows=m.links.audit_links(b'[[T]] [[', 'Source.md',index,self.system)
  self.assertEqual(rows[0]['status'],'ambiguous')
  rows=m.links.audit_links('[[总览/T]] [[总览/T#Route]]'.encode(),'Source.md',index,self.system)
  self.assertEqual(rows[0]['status'],'resolved');self.assertEqual(rows[1]['status'],'unchecked')
  self.assertTrue(index.scope['namespace_only'])

class AdvisoryTopicTests(AdvisoryFixture):
 def target(self,metadata):
  raw=('''---
'''+metadata+'''
---
# Fatou
Fatou navigation and evidence.
''').encode()
  (self.root/'entities/Fatou.md').write_bytes(raw)
  self.manifest['samples'][1]['sha256']=hashlib.sha256(raw).hexdigest()
 def test_topic_cannot_select_atomic_target(self):
  packet=self.packet();response=self.response(packet);response['suggestions'][0]['field']='topics'
  self.assertFalse(self.a.check_response(self.root,self.manifest,packet,response)['ok'])
 def test_historical_moc_not_declared_navigation(self):
  self.target('type: MOC');packet=self.packet()
  self.assertEqual(packet['model_input']['candidates'][0]['eligibility'],'reference_only')
 def test_explicit_moc_topic_is_valid(self):
  self.target('role: moc');packet=self.packet();response=self.response(packet);response['suggestions'][0]['field']='topics'
  result=self.a.check_response(self.root,self.manifest,packet,response);self.assertTrue(result['ok'],result)
 def test_navigation_is_not_atomic_relation(self):
  self.target('role: moc');packet=self.packet();self.assertFalse(self.a.check_response(self.root,self.manifest,packet,self.response(packet))['ok'])

 def test_ambiguous_topics_also_reject_atomic_candidates(self):
  self.target('role: moc')
  raw=chr(10).join(['---','type: concept','---','# Fatou alternative','Different atomic object.']).encode()
  (self.root/'entities/Hidden.md').write_bytes(raw)
  self.manifest['samples'][2]['sha256']=hashlib.sha256(raw).hexdigest()
  self.manifest['scopes']['model_visible'].append('H')
  packet=self.packet();response=self.response(packet);item=response['suggestions'][0]
  item['field']='topics';item['resolution']='multiple';item['selected_target']=None
  other=next(doc for doc in packet['model_input']['candidates'] if doc['id']!=item['candidates'][0]['target_id'])
  span=other['spans'][-1];item['candidates'].append({'target_id':other['id'],'evidence':[{'document_id':other['id'],'span_id':span['id'],'quote':span['text']}]})
  self.assertFalse(self.a.check_response(self.root,self.manifest,packet,response)['ok'])
