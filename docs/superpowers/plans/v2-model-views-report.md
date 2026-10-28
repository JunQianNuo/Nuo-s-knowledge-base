# V2 model / views implementation report

Scope: Task 1 of the approved 2026-10-28 restructure plan. All fixture writes were in temporary directories. No live `D:/知识库` writes and no commits were performed.

## Changed files

- `99_System/knowledge/v2/__init__.py`
- `99_System/knowledge/v2/model.py`
- `99_System/knowledge/v2/views.py`
- `99_System/knowledge/v2/schemas/note.schema.json`
- `99_System/knowledge/v2/templates/{concept,proposition,method,moc,lecture,review,homework,book,paper,web,idea}.md`
- `99_System/knowledge/tests/test_v2_model.py`
- `99_System/knowledge/tests/test_v2_views.py`
- This report.

## Delivered behavior

`model.read_note` reuses v1 `validator.parse_frontmatter`, rejecting duplicate YAML keys and preserving the exact original body bytes. `render_note` emits UTF-8 frontmatter while retaining the supplied body and extension metadata. The local Draft 2020-12 schema recognizes all eleven v2 types. Runtime validation additionally checks actual timezone-aware creation timestamps, actual calendar dates and whole-note property links. Literal filename carets such as `L^p空间` are accepted; anchors and display aliases in property links are rejected.

Atomic topics and sources must be nonempty; relation audit resolves actual notes without silently choosing between ambiguous short names. Atomic sources must be valid typed non-atomic notes under Sources. Topics must resolve to actual v2 MOCs under Maps. MOC aliases and tags are optional. Idea fields remain manually maintained; an explicit supported type suffices for the manual model, while extraction eligibility remains the extraction subsystem's responsibility. Templates declare schema version 2 and use explicit creation/source placeholders; they are system samples, not valid completed notes.

Scan entries contain `data`, `body`, `raw`, and parser `diagnostics`; keys are relative POSIX paths. Scanning excludes system, assets, raw/resource folders, links, junctions and nested repositories. Untyped course conversion material is excluded from entities. Audit returns integer `errors`, type counts, `entities`, `atomic`, and diagnostics; invalid relationships, Inbox pending notes and cyclic navigation do not inflate valid entity counts. Existing v1 files/interfaces were not edited.

`views.build` only returns proposed path-to-bytes values. It rejects cycles across the entire multi-parent MOC graph and rejects non-MOC topics/invalid atomic Sources targets. It produces native Bases, per-topic recursive Bases, Home, and marker-delimited MOC embed updates. Manual MOC/Home bytes outside generated markers are preserved, and rerunning proposals is idempotent.

## Dynamic query decisions

- The global topic database uses Maps folder + explicit `type: moc` + schema version 2. It does not maintain an enumerated MOC registry.
- Source and course databases likewise use dynamic scope/type/subject predicates. Courses include PDFs/PPTs and other materials; Sources entities remain restricted to typed notes.
- A per-topic Base contains an OR over its own and all descendant MOC link identities, combined with atomic type/schema/folder predicates. Each matching file appears once, including diamond inheritance. New atoms appear automatically without regenerating a list of file identities.
- New MOCs appear automatically in the global database. Changes to the topic hierarchy require `views` to refresh the ancestor closure. A new course's named view likewise requires refreshing discovery; its materials already appear in the global course view.
- Course discovery recognizes `Courses/归档/<课程>` and emits the actual course name with both archived and current course folders. Cross-course notes are matched through subject membership.
- Generic raw/hidden-folder exclusions remain dynamic. Existing link/junction/nested-repository boundaries are emitted as small explicit exclusion predicates rather than enumerating all material files. A newly introduced independent repository boundary requires refreshing views; native Bases cannot inspect filesystem `.git` markers itself.
- Native Bases display queries do not independently reproduce strict Python metadata/relationship validation. Creation and audit are the enforcement boundary. An externally edited invalid note may appear in a dynamic database until audited. No Obsidian UI rendering claim is made; emitted Bases YAML and query structures were fixture-verified.

Home currently links `99_System/knowledge/v2/README` and `docs/KNOWLEDGE_DAILY_GUIDE`; the controller owns writing those integrated guides. Generated databases live under `99_System/knowledge/v2/generated/`, and per-topic files use stable path hashes to avoid filename collisions.

## Verification

Test-first runs observed missing implementation failures, then assertion failures for invalid relation counts, cycle counts, unsafe material scope, invalid Sources publication, archived course discovery, literal caret names, optional MOC lists, dynamic new-note discovery and independent scope exclusion before their respective fixes.

Final focused runs:

```text
python -B -m unittest discover -s 99_System/knowledge/tests -p 'test_v2_model.py' -v
Ran 12 tests — OK
python -B -m unittest discover -s 99_System/knowledge/tests -p 'test_v2_views.py' -v
Ran 8 tests — OK
```

An earlier full shared-directory regression run completed before the final review additions:

```text
python -B -m unittest discover -s 99_System/knowledge/tests -v
Ran 143 tests in 88.952s — OK
```

During an earlier concurrent run, the transaction agent's then-in-progress tests `test_large_existing_binary_can_be_updated_and_restored` and `test_partial_intent_target_is_reported_without_deleting_unknown_bytes` were red; both subsequently passed in the 143-test full regression. The controller should perform the final integrated full regression after all agents finish.
