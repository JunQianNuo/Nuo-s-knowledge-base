"""Behavioral tests: losing bytes, overwriting edits, or crossing boundaries is a bug."""
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
try:
    tx = importlib.import_module('v2.transaction')
except ModuleNotFoundError:
    tx = None


class TransactionTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(tx, 'v2 migration transaction is not implemented')
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.root = self.base / 'vault'
        self.root.mkdir()
        self.old = self.root / '课程/甲/课件.pdf'
        self.old.parent.mkdir(parents=True)
        self.old.write_bytes(b'original\x00binary\xff')

    def make(self, content=None):
        return tx.plan(self.root, [{'source': '课程/甲/课件.pdf',
                                   'target': '03_Sources/Courses/甲/课件.pdf',
                                   'content': content, 'reason': 'migration'}], self.base / 'backup')

    def test_plan_is_read_only_and_move_restores_original_bytes(self):
        result = self.make()
        self.assertTrue(self.old.exists())
        self.assertFalse((self.root / '03_Sources').exists())
        applied = tx.apply(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(applied['conflicts'], 0)
        moved = self.root / '03_Sources/Courses/甲/课件.pdf'
        self.assertEqual(moved.read_bytes(), b'original\x00binary\xff')
        self.assertFalse(self.old.exists())
        tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')
        self.assertFalse(moved.exists())

    def test_source_edit_after_plan_is_preserved(self):
        result = self.make(b'normalized')
        self.old.write_bytes(b'new user edit')
        with self.assertRaises(ValueError):
            tx.apply(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'new user edit')
        self.assertFalse((self.root / '03_Sources').exists())

    def test_source_edit_between_payload_build_and_plan_is_rejected(self):
        expected = __import__('hashlib').sha256(self.old.read_bytes()).hexdigest()
        self.old.write_bytes(b'user edited after reading')
        with self.assertRaisesRegex(ValueError, 'snapshot'):
            tx.plan(self.root, [{'source': '课程/甲/课件.pdf', 'target': '03_Sources/Courses/甲/课件.pdf',
                    'content': b'old normalized payload', 'reason': 'migration', 'expected_sha256': expected}], self.base/'stale')
        self.assertEqual(self.old.read_bytes(), b'user edited after reading')

    def test_current_explicit_snapshot_is_accepted(self):
        expected = __import__('hashlib').sha256(self.old.read_bytes()).hexdigest()
        result = tx.plan(self.root, [{'source': '课程/甲/课件.pdf', 'target': '03_Sources/Courses/甲/课件.pdf',
                    'content': b'normalized', 'reason': 'migration', 'expected_sha256': expected}], self.base/'fresh')
        self.assertEqual(result['planned'], 1)

    def test_existing_target_and_duplicate_case_are_rejected(self):
        target = self.root / '03_Sources/Courses/甲/课件.pdf'
        target.parent.mkdir(parents=True)
        target.write_bytes(b'keep')
        with self.assertRaises(ValueError):
            self.make()
        self.assertEqual(target.read_bytes(), b'keep')
        with self.assertRaises(ValueError):
            tx.plan(self.root, [
                {'source': None, 'target': '01_Knowledge/A.md', 'content': b'a', 'reason': 'a'},
                {'source': None, 'target': '01_Knowledge/a.md', 'content': b'b', 'reason': 'b'}], self.base / 'other')

    def test_restore_does_not_overwrite_later_user_edit(self):
        result = self.make(b'normalized')
        tx.apply(Path(result['plan']), result['plan_sha256'])
        moved = self.root / '03_Sources/Courses/甲/课件.pdf'
        moved.write_bytes(b'later edit')
        with self.assertRaises(ValueError):
            tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(moved.read_bytes(), b'later edit')
        self.assertFalse(self.old.exists())

    def test_tampered_payload_and_wrong_approval_are_rejected(self):
        result = self.make()
        with self.assertRaises(ValueError):
            tx.apply(Path(result['plan']), '0' * 64)
        payload = next((Path(result['plan']).parent / 'payload').iterdir())
        payload.write_bytes(b'tampered')
        with self.assertRaises(ValueError):
            tx.apply(Path(result['plan']), result['plan_sha256'])
        self.assertTrue(self.old.exists())

    def test_scope_escape_and_independent_repository_are_rejected(self):
        for name in ['../outside.md', '01_Knowledge/../outside.md', '.obsidian/config.json', '01_Knowledge/NUL.md']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                tx.plan(self.root, [{'source': None, 'target': name, 'content': b'x', 'reason': 'bad'}], self.base / 'invalid')
        nested = self.root / '数学建模/project'
        nested.mkdir(parents=True)
        (nested / '.git').write_text('gitdir: elsewhere')
        with self.assertRaises(ValueError):
            tx.plan(self.root, [{'source': None, 'target': '数学建模/project/a.md', 'content': b'x', 'reason': 'bad'}], self.base / 'invalid')

    def test_new_file_restored_only_if_actually_applied(self):
        result = tx.plan(self.root, [{'source': None, 'target': 'Home.md', 'content': b'# Home\n', 'reason': 'new'}], self.base / 'backup')
        tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertFalse((self.root / 'Home.md').exists())
        tx.apply(Path(result['plan']), result['plan_sha256'])
        tx.apply(Path(result['plan']), result['plan_sha256'])
        tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertFalse((self.root / 'Home.md').exists())

    def test_large_existing_binary_can_be_updated_and_restored(self):
        self.old.write_bytes(b'a' * (5 * 1024 * 1024))
        result = tx.plan(self.root, [{'source': '课程/甲/课件.pdf', 'target': '课程/甲/课件.pdf',
                        'content': b'b' * (5 * 1024 * 1024), 'reason': 'large binary'}], self.base / 'large')
        tx.apply(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'b' * (5 * 1024 * 1024))
        tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'a' * (5 * 1024 * 1024))

    def test_partial_intent_target_is_reported_without_deleting_unknown_bytes(self):
        result = self.make()
        record = json.loads(Path(result['plan']).read_text('utf-8'))
        (Path(result['plan']).parent / 'journal.jsonl').write_text(
            json.dumps({'id': record['entries'][0]['id'], 'state': 'intent'}) + '\n', encoding='utf-8')
        target = self.root / '03_Sources/Courses/甲/课件.pdf'
        target.parent.mkdir(parents=True)
        target.write_bytes(b'partial or later user content')
        with self.assertRaises(ValueError):
            tx.restore(Path(result['plan']), result['plan_sha256'])
        self.assertEqual(target.read_bytes(), b'partial or later user content')
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')

    def test_payload_changed_after_loading_cannot_be_applied(self):
        result = self.make(b'approved')
        real_load = tx._load
        def change_after_load(*args):
            loaded = real_load(*args)
            (Path(result['plan']).parent / 'payload/000000.bin').write_bytes(b'unapproved')
            return loaded
        with mock.patch.object(tx, '_load', side_effect=change_after_load):
            with self.assertRaises(ValueError):
                tx.apply(result['plan'], result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')
        self.assertFalse((self.root / '03_Sources').exists())

    def test_original_changed_after_loading_cannot_be_restored(self):
        result = self.make(b'approved')
        tx.apply(result['plan'], result['plan_sha256'])
        real_load = tx._load
        def change_after_load(*args):
            loaded = real_load(*args)
            (Path(result['plan']).parent / 'original/000000.bin').write_bytes(b'unapproved')
            return loaded
        with mock.patch.object(tx, '_load', side_effect=change_after_load):
            with self.assertRaises(ValueError):
                tx.restore(result['plan'], result['plan_sha256'])
        self.assertFalse(self.old.exists())
        self.assertEqual((self.root / '03_Sources/Courses/甲/课件.pdf').read_bytes(), b'approved')

    def junction(self, link, target):
        subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(target)],
                       check=True, capture_output=True)

    def test_destination_directory_cannot_be_replaced_during_intent(self):
        target_dir = self.root / '03_Sources/Courses/甲'
        target_dir.mkdir(parents=True)
        outside = self.base / 'outside'
        outside.mkdir()
        result = self.make(b'approved')
        real_event = tx._event
        def attempt_junction(path, row):
            real_event(path, row)
            if row['state'] == 'intent':
                try:
                    target_dir.rename(target_dir.with_name('saved'))
                except OSError:
                    return  # The real Windows directory guard blocked replacement.
                self.junction(target_dir, outside)
        with mock.patch.object(tx, '_event', side_effect=attempt_junction):
            tx.apply(result['plan'], result['plan_sha256'])
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse(target_dir.is_junction())
        self.assertEqual((target_dir / '课件.pdf').read_bytes(), b'approved')

    def test_new_parent_junction_is_rejected_before_creating_external_children(self):
        outside = self.base / 'outside'
        outside.mkdir()
        result = self.make(b'approved')
        first_parent = self.root / '03_Sources'
        real_mkdir = Path.mkdir
        def replace_after_creation(directory, *args, **kwargs):
            value = real_mkdir(directory, *args, **kwargs)
            if directory == first_parent:
                directory.rename(self.root / 'saved')
                self.junction(directory, outside)
            return value
        with mock.patch.object(Path, 'mkdir', new=replace_after_creation):
            with self.assertRaises((OSError, ValueError)):
                tx.apply(result['plan'], result['plan_sha256'])
        self.assertEqual(list(outside.iterdir()), [])
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')

    def test_recorded_vault_root_cannot_be_redirected_before_apply(self):
        result = self.make(b'approved')
        outside = self.base / 'outside'
        external_source = outside / '课程/甲/课件.pdf'
        external_source.parent.mkdir(parents=True)
        external_source.write_bytes(b'original\x00binary\xff')
        saved = self.base / 'saved-vault'
        self.root.rename(saved)
        self.junction(self.root, outside)
        with self.assertRaises((OSError, ValueError)):
            tx.apply(result['plan'], result['plan_sha256'])
        self.assertEqual(external_source.read_bytes(), b'original\x00binary\xff')
        self.assertFalse((outside / '03_Sources').exists())
        self.assertEqual((saved / '课程/甲/课件.pdf').read_bytes(), b'original\x00binary\xff')

    def test_recovery_restarts_after_terminal_event_is_lost(self):
        for mode in ('inplace', 'move', 'new'):
            with self.subTest(mode=mode):
                root = self.base / mode
                root.mkdir()
                source = None if mode == 'new' else 'old.md'
                target = 'old.md' if mode == 'inplace' else 'new.md'
                if source:
                    (root / source).write_bytes(b'original')
                result = tx.plan(root, [{'source': source, 'target': target,
                                  'content': b'approved', 'reason': 'recovery'}], self.base / (mode + '-backup'))
                tx.apply(result['plan'], result['plan_sha256'])
                real_event = tx._event
                def crash_before_terminal(path, row):
                    if row['state'] == 'restored':
                        raise RuntimeError('simulated process exit')
                    return real_event(path, row)
                with mock.patch.object(tx, '_event', side_effect=crash_before_terminal):
                    with self.assertRaises(RuntimeError):
                        tx.restore(result['plan'], result['plan_sha256'])
                tx.restore(result['plan'], result['plan_sha256'])
                tx.restore(result['plan'], result['plan_sha256'])
                if source:
                    self.assertEqual((root / source).read_bytes(), b'original')
                if target != source:
                    self.assertFalse((root / target).exists())

    def test_truncated_final_journal_record_is_repaired_before_recovery_append(self):
        result = self.make(b'approved')
        tx.apply(result['plan'], result['plan_sha256'])
        journal = Path(result['plan']).parent / 'journal.jsonl'
        with journal.open('ab') as stream:
            stream.write(b'{"id": "000000", "state": "restor')
        tx.restore(result['plan'], result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')
        self.assertFalse((self.root / '03_Sources/Courses/甲/课件.pdf').exists())
        rows = [json.loads(line) for line in journal.read_text('utf-8').splitlines()]
        self.assertEqual(rows[-1]['state'], 'restored')
        tx.restore(result['plan'], result['plan_sha256'])

    def test_malformed_interior_journal_record_is_never_ignored(self):
        result = self.make(b'approved')
        tx.apply(result['plan'], result['plan_sha256'])
        journal = Path(result['plan']).parent / 'journal.jsonl'
        with journal.open('ab') as stream:
            stream.write(b'{"id": broken}\n{"id": "000000", "state": "applied"}\n')
        raw = journal.read_bytes()
        with self.assertRaises(ValueError):
            tx.restore(result['plan'], result['plan_sha256'])
        self.assertEqual(journal.read_bytes(), raw)
        self.assertEqual((self.root / '03_Sources/Courses/甲/课件.pdf').read_bytes(), b'approved')

    def test_restore_rechecks_existing_origin_before_deleting_target(self):
        result = self.make(b'approved')
        tx.apply(result['plan'], result['plan_sha256'])
        self.old.write_bytes(b'original\x00binary\xff')
        real_preflight = tx._preflight
        def edit_after_preflight(*args):
            real_preflight(*args)
            self.old.write_bytes(b'later user edit')
        with mock.patch.object(tx, '_preflight', side_effect=edit_after_preflight):
            with self.assertRaises(ValueError):
                tx.restore(result['plan'], result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'later user edit')
        self.assertEqual((self.root / '03_Sources/Courses/甲/课件.pdf').read_bytes(), b'approved')

    def test_restore_keeps_existing_origin_locked_until_target_deletion(self):
        result = self.make(b'approved')
        tx.apply(result['plan'], result['plan_sha256'])
        self.old.write_bytes(b'original\x00binary\xff')
        real_remove = tx._remove_locked
        def edit_during_deletion(stream):
            try:
                self.old.write_bytes(b'later user edit')
            except OSError:
                pass
            return real_remove(stream)
        with mock.patch.object(tx, '_remove_locked', side_effect=edit_during_deletion):
            tx.restore(result['plan'], result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(), b'original\x00binary\xff')
        self.assertFalse((self.root / '03_Sources/Courses/甲/课件.pdf').exists())

    def test_journal_cannot_be_rewritten_between_validated_events(self):
        result=self.make(b'approved')
        journal=Path(result['plan']).parent/'journal.jsonl'
        real_event=tx._event
        def concurrent_journal_edit(path,row):
            if row['state']=='intent':
                with self.assertRaises(OSError):
                    journal.write_bytes(b'forged journal')
            return real_event(path,row)
        with mock.patch.object(tx,'_event',side_effect=concurrent_journal_edit):
            tx.apply(result['plan'],result['plan_sha256'])

    def test_apply_resumes_verified_copy_before_source_deletion(self):
        result=self.make()
        record=json.loads(Path(result['plan']).read_text('utf-8'))
        target=self.root/'03_Sources/Courses/甲/课件.pdf'
        target.parent.mkdir(parents=True)
        target.write_bytes(self.old.read_bytes())
        tx._event(Path(result['plan']),{'id':record['entries'][0]['id'],'state':'intent'})
        tx.apply(result['plan'],result['plan_sha256'])
        self.assertFalse(self.old.exists())
        self.assertEqual(target.read_bytes(),b'original\x00binary\xff')
        tx.restore(result['plan'],result['plan_sha256'])
        self.assertEqual(self.old.read_bytes(),b'original\x00binary\xff')
        self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
