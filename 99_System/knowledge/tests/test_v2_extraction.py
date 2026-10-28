"""Offline extraction protocol tests; content decisions stay with the operator."""
from copy import deepcopy
import hashlib
import importlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

SYSTEM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SYSTEM))
from v2 import model, transaction


SOURCE = "03_Sources/Courses/数学/课堂笔记/课堂.md"
ATOM = "01_Knowledge/定义.md"
MOC = "02_Maps/数学.md"
STAMP = "2026-10-28T10:00:00+08:00"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def meta(kind, **updates):
    value = {"schema_version": 2, "type": kind, "time": STAMP}
    if kind in model.ATOMIC_TYPES:
        value.update(topics=["[[02_Maps/数学]]"], source=["[[03_Sources/Courses/数学/课堂笔记/课堂]]"])
    elif kind == "moc":
        value.update(topics=[], aliases=["数学学科"])
    elif kind == "lecture":
        value.update(status="not done", polish_status="done", subject=["数学"], source=["[[03_Sources/Courses/数学/课堂笔记/raw/逐字稿]]"])
    value.update(updates)
    return value


def put(root, name, metadata, body=b"\n# source\n\nDefinition evidence.\n"):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(model.render_note(metadata, body))
    return path


class V2ExtractionTests(unittest.TestCase):
    def setUp(self):
        try:
            self.protocol = importlib.import_module("v2.extraction")
        except ModuleNotFoundError:
            self.fail("Extraction protocol is not implemented")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "vault"
        self.root.mkdir()
        self.source = put(self.root, SOURCE, meta("lecture", custom={"keep": [1, 2]}),
                          "\r\n原始正文 $x$ ^block  \r\n\r\n".encode())
        put(self.root, MOC, meta("moc"))

    def test_prepare_is_json_safe_read_only_and_returns_complete_scoped_body_and_candidates(self):
        put(self.root, ATOM, meta("concept", aliases=["同义定义"]))
        put(self.root, "03_Sources/Courses/数学/课堂笔记/raw/fake.md", meta("lecture"))
        put(self.root, "03_Sources/Courses/数学/PPT课件/MD/fake.md", meta("lecture"))
        put(self.root, "03_Sources/Courses/数学/index.md", {"title": "untyped resource"})
        put(self.root, "03_Sources/Courses/独立/other.md", meta("lecture"))
        (self.root / "03_Sources/Courses/独立/.git").write_text("gitdir: elsewhere")
        put(self.root, "03_Sources/Ideas/没有状态.md", {"type": "idea"})
        put(self.root, "99_System/knowledge/tags/标签-数学.md", {"canonical_tag": "数学", "tag_aliases": ["math"]})
        before = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        packet = self.protocol.prepare(self.root, ["03_Sources"])
        self.assertEqual(set(packet.get("sources", {})), {SOURCE})
        self.assertEqual(packet["sources"][SOURCE]["body"], "\r\n原始正文 $x$ ^block  \r\n\r\n")
        self.assertEqual(packet["sources"][SOURCE]["sha256"], sha(self.source.read_bytes()))
        self.assertTrue(packet["sources"][SOURCE]["needs_extraction"])
        self.assertIn("同义定义", packet["atoms"][0]["metadata"]["aliases"])
        self.assertEqual(packet["mocs"][0]["path"], MOC)
        self.assertEqual(packet["tags"][0]["canonical_tag"], "数学")
        self.assertIsInstance(json.dumps(packet, ensure_ascii=False, allow_nan=False), str)
        self.assertEqual(before, {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def packet(self):
        return self.protocol.prepare(self.root, [SOURCE])

    def response(self, packet):
        return {"packet_sha256": packet["packet_sha256"],
                "source_hashes": {path: row["sha256"] for path, row in packet["sources"].items()},
                "notes": [{"path": ATOM, "metadata": meta("concept"), "body": "\n# 定义\n\nExtracted definition.\n"}],
                "coverage": [{"source": SOURCE, "complete": True, "atoms": [ATOM], "skip_candidates": []}]}

    def propose(self, packet, response):
        self.assertTrue(callable(getattr(self.protocol, "propose", None)), "Proposal protocol is not implemented")
        return self.protocol.propose(self.root, packet, response)

    def projected(self, operations, name):
        for op in operations:
            if op["target"] == name:
                return op["content"]
        return (self.root / name).read_bytes()

    def apply(self, operations):
        index = len(list(Path(self.temp.name).glob("backup-*")))
        result = transaction.plan(self.root, operations, Path(self.temp.name) / f"backup-{index}")
        transaction.apply(Path(result["plan"]), result["plan_sha256"])

    def test_prepare_rejects_outside_raw_untyped_and_independent_explicit_scopes(self):
        put(self.root, "03_Sources/Courses/数学/raw/raw.md", meta("lecture"))
        put(self.root, "03_Sources/untyped.md", {})
        put(self.root, "03_Sources/independent/note.md", meta("lecture"))
        (self.root / "03_Sources/independent/.git").write_text("gitdir: elsewhere")
        for scope in ("../03_Sources", "01_Knowledge", "03_Sources/Courses/数学/raw", "03_Sources/untyped.md", "03_Sources/independent/note.md"):
            with self.subTest(scope=scope), self.assertRaises(ValueError):
                self.protocol.prepare(self.root, [scope])

    def test_complete_proposal_preserves_source_bytes_fields_and_binds_every_write_hash(self):
        packet = self.packet()
        original = self.source.read_bytes()
        operations = self.propose(packet, self.response(packet))
        self.assertEqual(self.source.read_bytes(), original)
        self.assertFalse((self.root / ATOM).exists())
        self.assertFalse((self.root / self.protocol.STATE_PATH).exists())
        self.assertEqual({op["target"] for op in operations}, {SOURCE, ATOM, self.protocol.STATE_PATH})
        for op in operations:
            self.assertIn("expected_sha256", op)
            self.assertIsInstance(op["content"], bytes)
        source_op = next(op for op in operations if op["target"] == SOURCE)
        self.assertEqual(source_op["source"], SOURCE)
        self.assertEqual(source_op["expected_sha256"], sha(original))
        data, body = model.read_note(source_op["content"])
        self.assertEqual(data["status"], "done")
        self.assertEqual(data["time"], STAMP)
        self.assertEqual(data["custom"], {"keep": [1, 2]})
        self.assertEqual(body, model.read_note(original)[1])
        self.assertEqual(source_op["content"], original.replace(b"status: not done", b'status: "done"', 1))

    def test_stale_source_packet_candidate_and_hash_echo_are_rejected(self):
        packet = self.packet()
        response = self.response(packet)
        self.source.write_bytes(self.source.read_bytes() + b"\nnew edit\n")
        with self.assertRaises(ValueError):
            self.propose(packet, response)
        packet = self.packet()
        response = self.response(packet)
        response["source_hashes"][SOURCE] = "0" * 64
        with self.assertRaises(ValueError):
            self.propose(packet, response)
        response = self.response(packet)
        put(self.root, MOC, meta("moc", aliases=["changed candidate"]))
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_root_or_forged_packet_does_not_authorize_proposal(self):
        packet = self.packet()
        response = self.response(packet)
        forged = deepcopy(packet)
        forged["sources"][SOURCE]["body"] = "invented evidence"
        with self.assertRaises(ValueError):
            self.propose(forged, response)
        forged = deepcopy(packet)
        forged["vault_root"] = str(self.root.parent)
        with self.assertRaises(ValueError):
            self.propose(forged, response)
        response["packet_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_invalid_atomic_roles_and_missing_or_ambiguous_links_are_rejected(self):
        put(self.root, "02_Maps/other/数学.md", meta("moc"))
        packet = self.packet()
        for change in ({"source": []}, {"topics": []}, {"topics": ["[[数学]]"]},
                       {"topics": ["[[03_Sources/Courses/数学/课堂笔记/课堂]]"]},
                       {"source": ["[[03_Sources/Courses/数学/课堂笔记/raw/逐字稿]]"]},
                       {"uses": ["[[missing]]"]}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                response = self.response(packet)
                response["notes"][0]["metadata"].update(change)
                self.propose(packet, response)

    def test_new_moc_can_be_created_with_atom_but_topic_cycles_are_rejected(self):
        packet = self.packet()
        response = self.response(packet)
        response["notes"][0]["metadata"]["topics"] = ["[[02_Maps/新主题]]"]
        response["notes"].append({"path": "02_Maps/新主题.md", "metadata": meta("moc", topics=["[[02_Maps/数学]]"]), "body": "# 新主题\n"})
        operations = self.propose(packet, response)
        self.assertIn("02_Maps/新主题.md", {op["target"] for op in operations})
        response["notes"][1]["metadata"]["topics"] = ["[[02_Maps/新主题]]"]
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_coverage_requires_actual_referenced_atoms_pointing_to_that_source(self):
        put(self.root, "03_Sources/Ideas/另一个.md", {"type": "idea", "status": "not done"})
        put(self.root, ATOM, meta("concept", source=["[[03_Sources/Ideas/另一个]]"]))
        packet = self.packet()
        for atom in (ATOM, MOC, "01_Knowledge/missing.md"):
            with self.subTest(atom=atom), self.assertRaises(ValueError):
                response = self.response(packet)
                response["notes"] = []
                response["coverage"][0]["atoms"] = [atom]
                self.propose(packet, response)
        response = self.response(packet)
        response["notes"] = []
        response["coverage"][0]["atoms"] = []
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_partial_coverage_and_self_claimed_human_approval_never_finish_source(self):
        packet = self.packet()
        response = self.response(packet)
        response["coverage"][0]["complete"] = False
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "not done")
        response["coverage"][0].update(complete=True, skip_candidates=["例子无需提炼"], human_approved_skips=["例子无需提炼"])
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "not done")
        state = json.loads(self.projected(operations, self.protocol.STATE_PATH))
        self.assertFalse(state["sources"][SOURCE]["complete"])

    def test_approval_claims_without_skip_candidates_are_still_pending(self):
        packet = self.packet()
        response = self.response(packet)
        response["coverage"][0]["human_approved_skips"] = ["claimed manual approval"]
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "not done")
        state = json.loads(self.projected(operations, self.protocol.STATE_PATH))
        self.assertFalse(state["sources"][SOURCE]["complete"])
        self.assertIn("claimed manual approval", state["sources"][SOURCE]["pending_skips"])

    def test_empty_existing_atom_cannot_prove_coverage(self):
        put(self.root, ATOM, meta("concept"), b"\n \n")
        packet = self.packet()
        response = self.response(packet)
        response["notes"] = []
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_unpolished_source_cannot_claim_completed_extraction(self):
        put(self.root, SOURCE, meta("lecture", polish_status="not done"))
        packet = self.packet()
        self.assertFalse(packet["sources"][SOURCE]["eligible"])
        with self.assertRaises(ValueError):
            self.propose(packet, self.response(packet))

    def test_reopened_polishing_prevents_old_fingerprint_from_appearing_done(self):
        packet = self.packet()
        self.apply(self.propose(packet, self.response(packet)))
        data, body = model.read_note(self.source.read_bytes())
        data["polish_status"] = "not done"
        self.source.write_bytes(model.render_note(data, body))
        packet = self.packet()
        self.assertTrue(packet["sources"][SOURCE]["needs_extraction"])
        self.assertEqual(packet["sources"][SOURCE]["effective_status"], "not done")

    def test_response_cannot_edit_sources_or_other_unrequested_paths(self):
        packet = self.packet()
        for name in (SOURCE, "00_Inbox/fake.md", "01_Knowledge/nested/fake.md", "../outside.md"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                response = self.response(packet)
                response["notes"][0]["path"] = name
                self.propose(packet, response)
        response = self.response(packet)
        response["coverage"][0]["source"] = "03_Sources/Ideas/unrequested.md"
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_reused_atom_keeps_custom_fields_time_body_and_existing_sources(self):
        previous_source = "03_Sources/Ideas/先前来源.md"
        put(self.root, previous_source, {"type": "idea", "status": "not done"})
        put(self.root, ATOM, meta("concept", custom={"user": True}, source=["[[03_Sources/Ideas/先前来源]]"]), b"\r\n# Original user text ^anchor\r\n")
        packet = self.packet()
        response = self.response(packet)
        response["notes"][0]["body"] = "\r\n# Original user text ^anchor\r\n\nEvidence from new source.\n"
        operations = self.propose(packet, response)
        data, body = model.read_note(self.projected(operations, ATOM))
        self.assertEqual(data["custom"], {"user": True})
        self.assertEqual(data["time"], STAMP)
        self.assertIn("[[03_Sources/Ideas/先前来源]]", data["source"])
        self.assertIn(b"# Original user text ^anchor\r\n", body)
        response["notes"][0]["metadata"]["time"] = "2026-10-28T11:00:00+08:00"
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_reuse_cannot_erase_manual_content_or_repurpose_note_type(self):
        put(self.root, ATOM, meta("concept"), b"# User material\n")
        packet = self.packet()
        response = self.response(packet)
        with self.assertRaises(ValueError):
            self.propose(packet, response)
        response["notes"][0]["body"] = "# User material\n\nNew evidence\n"
        response["notes"][0]["metadata"]["type"] = "method"
        with self.assertRaises(ValueError):
            self.propose(packet, response)

    def test_transaction_apply_repeat_and_metadata_only_edit_do_not_reextract_body(self):
        packet = self.packet()
        self.apply(self.propose(packet, self.response(packet)))
        fresh = self.packet()
        self.assertFalse(fresh["sources"][SOURCE]["needs_extraction"])
        empty = self.response(fresh)
        empty.update(notes=[], coverage=[])
        self.assertEqual(self.propose(fresh, empty), [])
        data, body = model.read_note(self.source.read_bytes())
        data["custom"]["new_metadata"] = True
        self.source.write_bytes(model.render_note(data, body))
        fresh = self.packet()
        self.assertFalse(fresh["sources"][SOURCE]["needs_extraction"])
        empty = self.response(fresh)
        empty.update(notes=[], coverage=[])
        self.assertEqual(self.propose(fresh, empty), [])

    def test_changed_done_source_body_reopens_status_and_preserves_new_user_bytes(self):
        packet = self.packet()
        self.apply(self.propose(packet, self.response(packet)))
        self.source.write_bytes(self.source.read_bytes() + b"\nNewly added user content ^new\n")
        fresh = self.packet()
        self.assertTrue(fresh["sources"][SOURCE]["needs_extraction"])
        empty = self.response(fresh)
        empty.update(notes=[], coverage=[])
        operations = self.propose(fresh, empty)
        data, body = model.read_note(self.projected(operations, SOURCE))
        self.assertEqual(data["status"], "not done")
        self.assertIn(b"Newly added user content ^new\n", body)

    def test_unknown_done_status_without_recorded_coverage_is_not_treated_as_archived(self):
        put(self.root, SOURCE, meta("lecture", status="done"))
        packet = self.packet()
        self.assertTrue(packet["sources"][SOURCE]["needs_extraction"])
        response = self.response(packet)
        response.update(notes=[], coverage=[])
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "not done")

    def test_manual_idea_status_update_does_not_invent_schema_time_or_source(self):
        idea = "03_Sources/Ideas/手记.md"
        path = put(self.root, idea, {"type": "idea", "status": "not done", "custom": "manual"})
        packet = self.protocol.prepare(self.root, [idea])
        response = self.response(packet)
        response["notes"][0]["metadata"]["source"] = ["[[03_Sources/Ideas/手记]]"]
        response["coverage"][0]["source"] = idea
        operations = self.propose(packet, response)
        data, body = model.read_note(self.projected(operations, idea))
        self.assertEqual(data, {"type": "idea", "status": "done", "custom": "manual"})
        self.assertEqual(body, model.read_note(path.read_bytes())[1])

    def test_deleted_coverage_atom_reopens_previously_completed_source(self):
        packet = self.packet()
        self.apply(self.propose(packet, self.response(packet)))
        (self.root / ATOM).unlink()
        packet = self.packet()
        self.assertTrue(packet["sources"][SOURCE]["needs_extraction"])

    def test_source_edit_between_proposal_and_transaction_plan_is_rejected(self):
        packet = self.packet()
        operations = self.propose(packet, self.response(packet))
        self.source.write_bytes(self.source.read_bytes() + b"\nConcurrent edit\n")
        with self.assertRaises(ValueError):
            transaction.plan(self.root, operations, Path(self.temp.name) / "conflict-backup")
        self.assertTrue(self.source.read_bytes().endswith(b"Concurrent edit\n"))

    def test_prepare_uses_legacy_tag_vocabulary_before_registry_migration(self):
        put(self.root, "总览/标签库/条目/标签-旧词.md", {"canonical_tag": "旧词", "tag_aliases": ["old-name"], "promote": False})
        packet = self.packet()
        self.assertEqual(packet["tags"][0]["canonical_tag"], "旧词")
        self.assertEqual(packet["tags"][0]["tag_aliases"], ["old-name"])
        self.assertFalse(packet["tags"][0]["metadata"]["promote"])

    def approve(self, items):
        self.assertTrue(callable(getattr(self.protocol, "approve_skips", None)), "Separate human approval API missing")
        return self.protocol.approve_skips(self.root, SOURCE, items, "Synthetic explicit human review fixture", human_approved=True)

    def test_separate_human_review_allows_exact_skips_with_atoms_or_all_content_skipped(self):
        item = {"section": "example", "reason": "No reusable knowledge"}
        self.apply(self.approve([item]))
        packet = self.packet()
        response = self.response(packet)
        response["coverage"][0]["skip_candidates"] = [item]
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "done")
        response["notes"] = []
        response["coverage"][0]["atoms"] = []
        self.apply(self.propose(packet, response))
        self.assertFalse(self.packet()["sources"][SOURCE]["needs_extraction"])

    def test_body_change_invalidates_registered_human_review(self):
        self.apply(self.approve(["whole source needs no atomic extraction"]))
        self.source.write_bytes(self.source.read_bytes() + b"\nNew body content\n")
        packet = self.packet()
        response = self.response(packet)
        response["notes"] = []
        response["coverage"][0].update(atoms=[], skip_candidates=["whole source needs no atomic extraction"])
        operations = self.propose(packet, response)
        self.assertEqual(model.read_note(self.projected(operations, SOURCE))[0]["status"], "not done")

    def test_approval_requires_explicit_human_attestation_and_stales_old_packet(self):
        self.assertTrue(callable(getattr(self.protocol, "approve_skips", None)), "Separate human approval API missing")
        with self.assertRaises(ValueError):
            self.protocol.approve_skips(self.root, SOURCE, ["skip"], "note")
        packet = self.packet()
        self.apply(self.approve(["skip"]))
        with self.assertRaises(ValueError):
            self.propose(packet, self.response(packet))


if __name__ == "__main__":
    unittest.main()
