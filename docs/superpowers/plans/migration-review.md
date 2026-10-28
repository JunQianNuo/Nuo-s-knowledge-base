# Independent read-only migration review

Reviewed `99_System/knowledge/v2/migration.py`, its four migration tests, the approved design, `migration-preflight.json`, and `legacy-semantic-decisions.json`. This review changed no production code and did not apply any migration. Live `D:/知识库` was read only. All materialization and edge-case fixtures were under Windows TEMP.

## Projected role/relationship audit

The reviewer reran `migration.build(D:/知识库, decisions)` and materialized only migrated Markdown declaring schema version 2 and a recognized content type, including the newly created parent MOCs. No raw PDFs/PPTs, untitled resources, or pending Inbox records were copied into this projection.

Projection: `C:/Users/Nuo/AppData/Local/Temp/knowledge-migration-review-e22uyjq7/projected`

Machine-readable result: `C:/Users/Nuo/AppData/Local/Temp/knowledge-migration-review-e22uyjq7/results.json`

| Check | Result |
|---|---:|
| Proposed operations | 12,289 |
| Pending Inbox records | 249 |
| Projected typed notes/MOCs | 816 |
| Concept / proposition / method | 82 / 44 / 69 |
| Atomic total | 195 |
| Lecture / homework / review | 95 / 396 / 119 |
| MOCs, including new parents | 11 |
| Model structural diagnostics | 0 |
| Projected cross-note audit errors | 0 |
| Case-insensitive duplicate targets | 0 |
| Targets already existing in the live vault | 0 |
| Raw resource-tree entries promoted to lecture | 0 |
| Body differences beyond the link rewriter's output | 0 |

`model.audit(projected)` returned zero diagnostics, so the projected active sources and topics resolve to valid roles. This does not certify every body link or the correctness of the link rewriter itself; the defects below were reproduced independently.

The current four migration tests pass:

```text
python -B -m unittest discover -s 99_System/knowledge/tests -p 'test_v2_migration.py' -v
Ran 4 tests — OK
```

## Actionable findings before apply

### P1 — Short-link ambiguity is checked only inside the moving namespace

`short` is constructed only from `mapping` near lines 313–316. An unmoved note with the same basename is invisible to this ambiguity check. This can convert an originally ambiguous reference into a confident reference to the wrong moving note, including in scope-external user content.

Reproduced TEMP fixture:

- Moving `概念/共享.md` exists.
- Unmoved `AI/共享.md` also exists.
- `每日疑惑/问题.md` contains `[[共享]]`.
- Current output rewrites it to `[[00_Inbox/待核实核心/概念/共享]]`.

Expected: preserve `[[共享]]` and report ambiguity. A short name must be unique in the full visible vault namespace, respecting independent-project exclusions. Explicit full paths can still be repaired deterministically.

Controller has accepted this finding and owns the fix.

### P1 — Rejected source entries can disappear from a quarantined note

Atomic processing filters all old and added sources into `good`, assigns `data['source'] = good`, and only then calls `_inbox` when no valid typed Sources target remains (near lines 278–298). Rejected original evidence is not saved as `legacy_source`.

Actual affected entry in this preflight:

```text
概念/Fourier变换.md
original source: [[课程/归档/实变函数/课件/MD/2023-RA-28]]
pending reason: Missing valid Sources-note provenance; raw assets alone do not qualify
```

The raw courseware link correctly fails the new active atomic source rule, but the pending note should still retain that original evidence. Preserve the original source field when quarantining, or move rejected values into an explicit legacy evidence field. The same defect was reproduced in a fixture with `source: ['原始教材第3节']` plus a valid new Sources citation: the bibliographic original was silently omitted from the resulting active note. No such loss was found among the current 195 typed projected atoms; the Fourier Inbox case remains a concrete current-batch issue.

### P1 — The separate top-level MOC glob bypasses protected paths

The `总览/*.md` loop near line 180 reads candidates directly without `link_validator.protected_reason`, unlike `_files`.

Reproduced TEMP fixture: create `总览/.git` and a `总览/主题-MOC.md` with `role: moc`. `migration.build` still proposes moving that protected independent-repository note to `02_Maps/MOC-主题.md`.

Expected: exclude the independent scope before reading it and before generating an operation. Apply-time transaction protection may refuse the operation later, but the migration scanner itself must honor the approved isolation boundary. A native symlink fixture could not be created on this host (`WinError 1314`); the ordinary `.git` fixture reproduces the bypass without elevated privileges.

### P2 — Escaped literal Wiki-links are rewritten

`rewrite_links` searches masked active text with a regex but does not test whether the `[[` delimiter is escaped.

Reproduced input:

```text
\[[概念/共享]]
```

Current output changes the target after the backslash. Expected: preserve the escaped literal byte-for-byte. Existing link parsing has escape handling that can be reused.

### P2 — Parenthesized Markdown targets are corrupted

The Markdown URI regex stops at the first `)` and processes an incomplete target. In a fixture mapping `概念/A(1).md` to `01_Knowledge/A(1).md`, moving `概念/共享.md` produces:

```text
input:   [x](A(1).md)
current: [x](../%E6%A6%82%E5%BF%B5/A%281).md)
```

Expected: a valid link to the complete new `01_Knowledge/A(1).md` target. Recognize balanced Markdown destinations, escaped characters and angle destinations before applying a path mapping. Do not rewrite a prefix that is not the whole parsed destination.

### P2 — Markdown reference definitions and Canvas file fields are not repaired

Both deterministic consumers are omitted by `rewrite_links`:

```text
[x][r]

[r]: ../概念/共享.md
```

```json
{"nodes":[{"type":"file","file":"概念/共享.md"}]}
```

Current output is unchanged although the referenced note moves. Expected: repair the Markdown reference destination relative to the note, and the Canvas `file` property according to its vault-relative identity; preserve unrelated JSON/text. The current preflight mapping contains no moved `.canvas` files, so the Canvas reproduction is a supported-consumer coverage defect rather than evidence of an already identified current-batch broken canvas.

Controller has accepted the escaping, balanced Markdown, reference-definition and Canvas findings and owns those fixes.

### P2 — Semantic decision hashes are optional at the API boundary

Current code checks note/evidence hashes only when supplied. A fixture knowledge decision containing only `type`, `disposition` and `sources` is accepted and promotes the atom without any `note_sha256` or evidence records.

Expected: a knowledge-promoting semantic override must be bound to the reviewed original note and to each actually consulted source by required hashes and evidence. Reject a missing, malformed or stale binding rather than treating it as unprotected optional metadata. Also apply normal protected-path checks to evidence paths before reading them.

For this actual decision file, all 66 decisions have note hashes, every evidence record has a hash, and every added source path is represented by evidence. The reproduced missing-hash case is therefore a fail-open API gap, not an assertion that the current 66 decisions lack hashes. The current build completed its supplied stale-hash checks successfully.

## Evidence and scope observations

- Current raw-tree classification prevents the tested PPT/MD, raw transcript, board and unprocessed material folders from becoming lecture notes. The full projected lecture set contained no source paths under those raw-tree categories.
- New parent MOC times are creation times for genuinely new notes. Historical note times use declared creation fields where available, otherwise filesystem birthtime with an explicit limitation recorded in `time_basis`; no migration execution timestamp was used as an undocumented historical creation claim.
- The migration does not create book/paper/web records in this batch, so it does not invent `source_title` bibliographic metadata.
- All migrated Sources statuses are `not done`; legacy completion wording is not treated as proof of completed atom extraction. Lecture polish status remains separate. Source links in the projected atoms resolve to typed non-atomic Sources notes.
- Original code fences, inline code, `$...$` and `$$...$$` fixtures were preserved by the masking routine while a real adjacent Wiki-link was repaired. The escaped-link and destination-parser findings above are additional boundaries the current tests do not cover.
- The current batch has 12 outside-link-update files listed in the preflight. These remain targeted reference changes; the namespace ambiguity finding must be resolved before trusting their targets.
- Actual target collision checks found no duplicate casefolded targets and no pre-existing live targets. The transaction subsystem remains responsible for rechecking namespace and hash changes immediately before apply.

## Source semantics concern and controller adjudication

The reviewer flagged that 27 promoted knowledge decisions originally had no source and that their evidence is labeled `current_content_grounding`, explicitly disclaiming a claim about initial extraction history. The controller adjudicated that v2 `source` in these cases records material actually consulted and substantively used during the current consolidation, rather than asserting original authorship or historical derivation. The evidence report keeps `source_basis`, full source hashes, line excerpts and reasoning, and delivery must explicitly disclose this distinction. Partial or merely topical matches remain in Inbox.

This ruling resolves the general review concern for verified current consultation; this review does not mechanically veto all 27 citations. Sampled DCT/Euler-RK/Hölder records contain substantive formula/condition/step alignment rather than only a shared topic name. This is not an independent semantic re-review of all 31 promoting decisions. The concrete loss of rejected original source evidence described above remains separate and still needs preservation.

## Review conclusion

The typed projection has a clean structural and relationship audit. Apply should wait for the accepted link-repair fixes and the source-preservation/scope-isolation fixes above, followed by new edge-case regression tests and a fresh projected audit of the final proposal. Production code was not edited by this reviewer.
