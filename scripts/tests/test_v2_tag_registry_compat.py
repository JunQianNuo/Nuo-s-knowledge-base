from pathlib import Path
import sys
import tempfile
import unittest
import yaml

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tag_maintenance import Registry


class RetiredTagCompatibility(unittest.TestCase):
    def test_retired_synonym_record_is_not_a_second_canonical_tag(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            (root/'标签-标准.md').write_text('---\n'+yaml.safe_dump({'canonical_tag':'标准','tag_aliases':['旧名']},allow_unicode=True)+'---\n',encoding='utf-8')
            (root/'标签-旧名.md').write_text('---\n'+yaml.safe_dump({'legacy_canonical_tag':'旧名','synonym_of':'[[标签-标准]]'},allow_unicode=True)+'---\n',encoding='utf-8')
            registry=Registry.load(root)
            self.assertEqual(registry.resolve('旧名','',existing=True),'标准')
            self.assertEqual(len(registry.entries),1)


if __name__=='__main__':unittest.main()
