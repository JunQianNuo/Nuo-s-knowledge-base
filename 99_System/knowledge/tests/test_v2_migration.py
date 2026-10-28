import importlib
from pathlib import Path
import sys
import tempfile
import unittest
import subprocess
import os

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from v2 import model
try:
    migration = importlib.import_module('v2.migration')
except ModuleNotFoundError:
    migration = None


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(migration, 'migration classifier is not implemented')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def put(self, path, data, body=b'original body\r\n'):
        p = self.root/path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(model.render_note(data, body))

    def test_homework_and_review_are_separate_from_raw_materials(self):
        self.put('课程/统计/习题库/题一.md', {'type':'习题','source':['教材第1题']})
        self.put('课程/统计/知识点解析梳理/章节.md', {'type':'知识梳理','source':['教材第一章']})
        self.put('课程/统计/PPT/MD/课件.md', {'type':'课件笔记','source':['课件.pdf']})
        ops, report = migration.build(self.root)
        by = {op['source']:op for op in ops}
        homework = by['课程/统计/习题库/题一.md']
        self.assertIn('/作业/', homework['target'])
        data, body = model.read_note(homework['content'])
        self.assertEqual((data['type'],data['subject'],data['status']), ('homework',['统计'],'not done'))
        self.assertEqual(body,b'original body\r\n')
        self.assertTrue(by['课程/统计/知识点解析梳理/章节.md']['target'].startswith('03_Sources/Reviews/统计/'))
        self.assertIsNone(by['课程/统计/PPT/MD/课件.md']['content'])

    def test_missing_provenance_goes_to_inbox_without_fabrication(self):
        self.put('方法/方法甲.md', {'type':'method','topics':['未知关键词']})
        ops, report = migration.build(self.root)
        op = next(x for x in ops if x['source']=='方法/方法甲.md')
        self.assertTrue(op['target'].startswith('00_Inbox/'))
        data, body = model.read_note(op['content'])
        self.assertNotIn('schema_version',data)
        self.assertEqual(data['legacy_type'],'method')
        self.assertEqual(body,b'original body\r\n')

    def test_source_and_moc_targets_rewrite_to_real_new_roles(self):
        self.put('课程/统计/知识点解析梳理/章节.md', {'type':'知识梳理','source':['教材']})
        self.put('总览/统计-MOC.md', {'role':'moc','topics':[]})
        self.put('概念/统计量.md', {'schema_version':1,'type':'concept','title':'统计量',
            'topics':['[[总览/统计-MOC]]'], 'source':['[[课程/统计/知识点解析梳理/章节]]']})
        ops, report = migration.build(self.root)
        op = next(x for x in ops if x['source']=='概念/统计量.md')
        self.assertEqual(op['target'],'01_Knowledge/统计量.md')
        data, _ = model.read_note(op['content'])
        self.assertNotIn('title',data)
        self.assertEqual(data['schema_version'],2)
        self.assertTrue(data['topics'][0].startswith('[[02_Maps/'))
        self.assertTrue(data['source'][0].startswith('[[03_Sources/Reviews/'))
        self.assertIn('expected_sha256',op)

    def test_relative_images_and_outside_links_are_targeted_without_touching_code(self):
        self.put('课程/统计/课堂笔记/课堂.md', {'type':'课堂笔记','source':['录音']},
                 '![图](图.png)\n`[[课程/统计/课堂笔记/课堂]]`\n'.encode())
        image = self.root/'课程/统计/课堂笔记/图.png'
        image.write_bytes(b'png bytes')
        self.put('每日疑惑/问题.md', {}, '[[课程/统计/课堂笔记/课堂]]\n正文保持\n'.encode())
        ops, report = migration.build(self.root)
        by = {op['source']:op for op in ops}
        self.assertTrue(by['课程/统计/课堂笔记/图.png']['target'].startswith('04_Assets/Images/'))
        self.assertIn(b'04_Assets',by['课程/统计/课堂笔记/课堂.md']['content'])
        outside = by['每日疑惑/问题.md']['content'].decode()
        self.assertIn('[[03_Sources/Courses/统计/课堂笔记/课堂]]',outside)
        self.assertIn('正文保持',outside)
        self.assertIn('`[[课程/统计/课堂笔记/课堂]]`',by['课程/统计/课堂笔记/课堂.md']['content'].decode())

    def test_ambiguous_short_and_escaped_literal_links_are_not_invented(self):
        self.put('概念/共享.md', {'type':'concept'})
        self.put('AI/共享.md', {})
        original='[[共享]]\n\\[[概念/共享]]\n'
        self.put('每日疑惑/问题.md',{},original.encode())
        ops,_=migration.build(self.root)
        changed=next((o for o in ops if o['source']=='每日疑惑/问题.md'),None)
        self.assertIsNone(changed)

    def test_balanced_markdown_references_and_canvas_file_targets(self):
        mapping={'概念/A(1).md':'01_Knowledge/A(1).md'}
        text='[直链](概念/A(1).md)\n[引文][a]\n\n[a]: 概念/A(1).md "标题"\n'
        changed=migration.rewrite_links(text,'Home.md','Home.md',mapping,{})
        self.assertIn('[直链](01_Knowledge/A%281%29.md)',changed)
        self.assertIn('[a]: 01_Knowledge/A%281%29.md "标题"',changed)
        canvas='{"nodes":[{"type":"file","file":"概念/A(1).md"}],"edges":[]}'
        changed=migration.rewrite_links(canvas,'图.canvas','图.canvas',mapping,{})
        self.assertIn('"file":"01_Knowledge/A(1).md"',changed)

    def test_table_alias_separator_is_preserved_while_destination_moves(self):
        original='| [[概念/对象\\|人工别名]] | `[[概念/对象\\|代码]]` |\n'
        changed=migration.rewrite_links(original,'Home.md','Home.md',{'概念/对象.md':'01_Knowledge/对象.md'},{})
        self.assertEqual(changed,'| [[01_Knowledge/对象\\|人工别名]] | `[[概念/对象\\|代码]]` |\n')

    def test_rejected_source_and_topics_survive_inbox_quarantine(self):
        self.put('概念/对象.md',{'type':'concept','source':['原始教材'],'topics':['旧主题']})
        ops,_=migration.build(self.root)
        data,_=model.read_note(next(o for o in ops if o['source']=='概念/对象.md')['content'])
        self.assertIn('原始教材',data.get('legacy_source',[]))
        self.assertIn('旧主题',data.get('legacy_topics',[]))

    def test_direct_moc_scan_respects_nested_repository(self):
        self.put('总览/主题-MOC.md',{'role':'moc'})
        (self.root/'总览/.git').write_text('gitdir: elsewhere')
        ops,_=migration.build(self.root)
        self.assertFalse(any(o['source']=='总览/主题-MOC.md' for o in ops))

    def test_unbound_semantic_decision_cannot_supply_provenance(self):
        self.put('方法/方法甲.md',{'type':'method'})
        with self.assertRaises(ValueError):
            migration.build(self.root,{'方法/方法甲.md':{'type':'method','disposition':'knowledge','sources':[]}})

    def test_creation_history_follows_rename_instead_of_recent_copy_time(self):
        helper=getattr(migration,'creation_history',None)
        self.assertIsNotNone(helper,'Git creation history resolver is not implemented')
        def git(*args,stamp=None):
            env=dict(os.environ)
            if stamp:env.update(GIT_AUTHOR_DATE=stamp,GIT_COMMITTER_DATE=stamp)
            subprocess.run(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid',*args],cwd=self.root,env=env,check=True,capture_output=True)
        git('init')
        self.put('概念/课程/对象.md',{'type':'concept'})
        git('add','.')
        git('commit','-m','initial',stamp='2020-01-02T03:04:05+08:00')
        git('mv','概念/课程/对象.md','概念/对象.md')
        git('commit','-m','rename',stamp='2021-02-03T04:05:06+08:00')
        self.assertEqual(helper(self.root)['概念/对象.md']['time'],'2020-01-02T03:04:05+08:00')


if __name__ == '__main__':
    unittest.main()
