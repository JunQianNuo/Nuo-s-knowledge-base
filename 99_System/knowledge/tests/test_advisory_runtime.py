import copy
import hashlib
import json
from test_advisory import AdvisoryFixture, SYSTEM

class RuntimeTests(AdvisoryFixture):
    def test_minimal_envelope_has_binding_but_no_audit(self):
        packet=self.packet()
        envelope=self.a.inference_envelope(packet)
        self.assertEqual(envelope["request_id"],packet["request_id"])
        self.assertNotIn("audit",envelope)
        self.assertNotIn("PRIVATE_BODY_SENTINEL",json.dumps(envelope))
        self.assertEqual(envelope["retrieval"][0]["hidden_count"],0)
        self.a.validate_schema("inference",envelope)

    def test_selected_identity_is_distinct_from_unique_retrieval(self):
        path=self.root/"entities/Hidden.md"
        raw=b"---\nschema_version: 1\ntype: concept\n---\n# Alternate\nFatou alternative tool.\n"
        path.write_bytes(raw)
        self.manifest["samples"][2]["sha256"]=hashlib.sha256(raw).hexdigest()
        packet=self.packet()
        response=self.response(packet)
        response["suggestions"][0]["resolution"]="selected"
        result=self.a.check_response(self.root,self.manifest,packet,response)
        self.assertTrue(result["ok"],result)
        self.assertIn("retrieval_not_unique",result["results"][0]["review_flags"])
        response["suggestions"][0]["resolution"]="unique"
        self.assertFalse(self.a.check_response(self.root,self.manifest,packet,response)["ok"])

    def test_real_export_requires_bound_authorization(self):
        self.manifest["dataset_kind"]="real_candidates"
        self.manifest["model_content_authorization"]="explicit_scope"
        with self.assertRaises(ValueError):self.packet()
        authorization=self.a.authorize(self.root,self.manifest,stages=["classify"])
        packet=self.a.prepare(self.root,self.manifest,stage="classify",authorization=authorization)
        self.assertEqual(len(packet["model_input"]["documents"]),1)
        with self.assertRaises(ValueError):self.a.prepare(self.root,self.manifest,stage="relations",authorization=authorization)
        forged=copy.deepcopy(self.manifest);forged["scopes"]["model_visible"].append("H")
        with self.assertRaises(ValueError):self.a.prepare(self.root,forged,authorization=authorization)

    def test_authorization_root_and_content_changes_are_rejected(self):
        self.manifest["dataset_kind"]="real_candidates"
        self.manifest["model_content_authorization"]="explicit_scope"
        auth=self.a.authorize(self.root,self.manifest,stages=["classify"])
        bad=copy.deepcopy(auth);bad["vault_root"]=str(self.root/"elsewhere")
        with self.assertRaises(ValueError):self.a.prepare(self.root,self.manifest,authorization=bad)
        (self.root/"notes/Source.md").write_text("changed",encoding="utf-8")
        with self.assertRaises(ValueError):self.a.prepare(self.root,self.manifest,authorization=auth)

    def test_manifest_builder_requires_explicit_visibility(self):
        m=self.a.retrieval.make_manifest(self.root,["notes/Source.md"],["entities/Fatou.md"],[])
        self.assertEqual(m["scopes"]["model_visible"],[])
        self.assertEqual(len(m["samples"]),2)
        with self.assertRaises(ValueError):self.a.retrieval.make_manifest(self.root,["../secret.md"],[],[])

    def test_envelope_cannot_silently_trust_forged_request_hash(self):
        packet=self.packet();packet["request_id"]="req_forged"
        with self.assertRaises(ValueError):self.a.inference_envelope(packet)

    def test_synthetic_vault_subtree_cannot_bypass_real_authorization(self):
        from dataclasses import replace
        system=self.a.retrieval.v.load_system(SYSTEM)
        system=replace(system,vault_root=self.root)
        scoped=copy.deepcopy(self.manifest)
        scoped["samples"]=[scoped["samples"][0]]
        scoped["samples"][0]["path"]="Source.md"
        scoped["scopes"]={"source":["S"],"retrieval":[],"model_visible":["S"]}
        with self.assertRaises(ValueError):
            self.a.retrieval.build_catalog(self.root/"notes",scoped,system=system)
