"""Static link audit contracts; all files are isolated synthetic data."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SYSTEM = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("knowledge_links", SYSTEM / "link_validator.py")
l = importlib.util.module_from_spec(spec); sys.modules[spec.name] = l; spec.loader.exec_module(l)


class LinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("Source.md", "# Source\n")
        self.write("Target.md", "---\naliases: [Alias]\n---\n# Heading\n\nParagraph ^block-id\n")
        self.write("Target.pdf", "synthetic attachment")
        self.write("概念/L^p空间.md", "# 空间\n")
        self.system = l.v.load_system(SYSTEM)

    def write(self, path, text):
        p = self.root / path; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def audit(self, text):
        return l.audit_links(text.encode(), "Source.md", l.build_index(self.root, self.system), self.system)

    def test_contract_cases(self):
        cases = json.loads((SYSTEM / "tests/link_cases.json").read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["id"]):
                result = self.audit(case["text"])
                self.assertEqual([r["status"] for r in result], case["statuses"])
                for row in result:
                    self.assertTrue(row["basis"])
                    self.assertIn("scope", row)
                    self.assertEqual(row["claim"], "static_audit")

    def test_code_comments_math_and_escapes_do_not_create_links(self):
        text = '```md\n[[Target]] [x](Target.md)\n```\n~~~\n[[Target]]\n~~~\n    [[Target]]\n\n`[[Target]]` ``[x](Target.md)``\n\\[[Target]] \\[x](Target.md)\n%% [[Target]] %% <!-- [[Target]] -->\n$[[Target]]$ $$[[Target]]$$\n[[Target]]\n'
        result = self.audit(text)
        self.assertEqual(len(result), 1, result)
        self.assertEqual(result[0]["status"], "resolved")

    def test_markdown_and_wiki_are_independent_parsers(self):
        self.write("with space.md", "# Space\n")
        text = '[[Target|display]] ![[Target.pdf]] [space](with%20space.md)\n[r][ref]\n\n[ref]: Target.md "title"\n'
        result = self.audit(text)
        self.assertEqual(len(result), 4, result)
        self.assertEqual({x["syntax"] for x in result}, {"wikilink", "markdown"})
        self.assertTrue(all(x["status"] == "resolved" for x in result))
        self.assertEqual(sum(x["embed"] for x in result), 1)

    def test_math_caret_is_part_of_filename(self):
        result = self.audit('[[概念/L^p空间]] [space](%E6%A6%82%E5%BF%B5/L%5Ep%E7%A9%BA%E9%97%B4.md)')
        self.assertEqual([r["status"] for r in result], ["resolved", "resolved"])
        self.assertTrue(all(r["candidates"] == ["概念/L^p空间.md"] for r in result))

    def test_ambiguity_and_explicit_extension(self):
        self.write("a/Same.md", "# A\n"); self.write("b/Same.md", "# B\n")
        result = self.audit('[[Same]] [[a/Same]] [[Target]] [[Target.pdf]]')
        self.assertEqual([r["status"] for r in result], ["ambiguous", "resolved", "resolved", "resolved"])
        self.assertEqual(result[0]["candidates"], ["a/Same.md", "b/Same.md"])
        self.assertEqual(result[2]["candidates"], ["Target.md"])

    def test_alias_is_candidate_not_automatic_destination(self):
        row = self.audit('[[Alias]]')[0]
        self.assertEqual(row["status"], "unchecked")
        self.assertEqual(row["candidates"], ["Target.md"])

    def test_position_is_exact_or_explicitly_unknown(self):
        text = '---\ntype: concept\ntopics:\n  - "[[Target]]"\n---\nText [[Target]] and [md](Target.md)\n'
        result = self.audit(text)
        prop = next(r for r in result if r.get("field") == "topics/0")
        body = next(r for r in result if r["syntax"] == "wikilink" and not r.get("field"))
        md = next(r for r in result if r["syntax"] == "markdown")
        self.assertIsNone(prop["line"]); self.assertIsNone(prop["column"])
        self.assertEqual((body["line"], body["column"]), (6, 6))
        self.assertIsNone(md["line"]); self.assertIsNone(md["column"])

    def test_independent_repos_and_external_paths_are_unchecked(self):
        self.write("project/.git", "synthetic marker")
        self.write("project/Hidden.md", "# Hidden")
        result = self.audit('[[project/Hidden]] [outside](../outside.md)')
        self.assertEqual([r["status"] for r in result], ["unchecked", "unchecked"])
        self.assertTrue(result[0]["scope"]["excluded"])

    def test_system_target_can_resolve_but_is_not_an_entity(self):
        self.write("规范/Rule.md", "# Rule")
        row = self.audit('[[规范/Rule]]')[0]
        self.assertEqual(row["status"], "resolved")
        self.assertTrue(row["target_is_system"])

    def test_scope_and_missing_heading_distinguished(self):
        result = self.audit('[[Target#Heading]] [[Target#^block-id]] [[Target#Missing]] [[Target.pdf#page=1]]')
        self.assertEqual([r["status"] for r in result], ["resolved", "resolved", "unresolved", "unchecked"])

    def test_no_writes_or_network(self):
        blocked = AssertionError("write/network")
        with patch.object(Path, "write_text", side_effect=blocked), patch.object(Path, "write_bytes", side_effect=blocked), patch("socket.socket", side_effect=blocked):
            self.assertEqual(self.audit('[[Target]]')[0]["status"], "resolved")

    def test_masked_inline_constructs_do_not_hide_following_real_links(self):
        for prefix in ('`code`', '`%%`', '%% comment %%', '$x^p$'):
            with self.subTest(prefix=prefix):
                result = self.audit(prefix + ' [md](Target.md) [[Target]]')
                self.assertEqual(len(result), 2, result)
                self.assertTrue(all(r["status"] == "resolved" for r in result))
        self.assertEqual(len(self.audit('`%%` [md](Target.md) %% comment %% [[Target]]')), 2)

    def test_footnotes_are_not_commonmark_file_reference_links(self):
        result = self.audit('Text[^1].\n\n[^1]: explanation [[Target]]\n')
        self.assertEqual(len(result), 1, result)
        self.assertEqual(result[0]["syntax"], "wikilink")
        self.assertEqual(self.audit('Text[^1].\n\n[^1]: Target.md\n'), [])

    def test_other_attachment_extensions(self):
        self.write('data.csv', 'x,y\n1,2\n')
        self.assertEqual(self.audit('[[data.csv]]')[0]["status"], "resolved")

    def test_markdown_paths_are_relative_to_source_not_wiki_candidates(self):
        self.write('assets/x.png', 'root')
        self.write('Notes/assets/x.png', 'local')
        self.write('Notes/Target.md', '# Local\n')
        index = l.build_index(self.root, self.system)
        rows = l.audit_links(b'[x](assets/x.png) [n](Target.md) [h](Target.md#Local)', 'Notes/Source.md', index, self.system)
        self.assertEqual([r["status"] for r in rows], ['resolved'] * 3)
        self.assertEqual(rows[0]["candidates"], ['Notes/assets/x.png'])
        self.assertEqual(rows[1]["candidates"], ['Notes/Target.md'])
        missing = l.audit_links(b'[x](assets/x.png)', 'MissingFolder/Source.md', index, self.system)[0]
        self.assertEqual(missing["status"], 'unresolved')

    def test_wiki_raw_and_target_are_original_not_masked(self):
        self.write('a`b`.md', '# Backtick')
        self.write('cash$x$.md', '# Dollar')
        text = '[[a`b`]] [[cash$x$]] [[Target|$x$]]'
        rows = self.audit(text)
        self.assertEqual([r["status"] for r in rows], ['resolved'] * 3)
        self.assertEqual([r["raw"] for r in rows], ['[[a`b`]]', '[[cash$x$]]', '[[Target|$x$]]'])
        self.assertEqual([r["target"] for r in rows], ['a`b`', 'cash$x$', 'Target'])

    def test_empty_markdown_uri_is_valid_self_document(self):
        row = self.audit('[x]()')[0]
        self.assertEqual(row["status"], 'resolved')
        self.assertEqual(row["candidates"], ['Source.md'])
        self.assertEqual(self.audit('[[]]')[0]["status"], 'invalid_syntax')

    def test_percent_encoded_wiki_is_conservatively_unchecked(self):
        self.write('A%20B.md', '# Literal')
        self.write('A B.md', '# Space')
        wiki = self.audit('[[A%20B]]')[0]
        self.assertEqual(wiki["status"], 'unchecked')
        self.assertEqual(wiki["raw"], '[[A%20B]]')
        self.assertEqual(set(wiki["candidates"]), {'A%20B.md', 'A B.md'})
        md = self.audit('[x](A%20B.md)')[0]
        self.assertEqual(md["status"], 'resolved')
        self.assertEqual(md["candidates"], ['A B.md'])


if __name__ == "__main__":
    unittest.main()
