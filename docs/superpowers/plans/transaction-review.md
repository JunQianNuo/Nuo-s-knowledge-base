# Transaction review — 2026-10-28

Verdict: changes required before applying the migration to real Vault files. Four actionable findings below were reproduced on native Windows using isolated temporary Vault/backup directories. No live Vault data or implementation files were modified. Reviewed `v2/transaction.py`, the optional `delete_access` extension in `change_control.py`, focused tests, design §§9–11, and plan Task 2. The existing eleven tests were read; they were not repeated because they do not exercise these fault windows.

## [P1] Anchor and protect ancestor directories through file creation and transfer

Location: `99_System/knowledge/v2/transaction.py:187–189` (also `250–255`; reused guard `change_control.py:125`).

The final `safe_path()` check occurs before the intent journal write, directory creation, and file open. Replacing a validated destination parent with a Windows junction during that gap redirects `_write()` outside the Vault. `_safe_stream()` does not stop it: the file itself is ordinary, and its actual handle path equals the newly resolved `path.resolve()`. The transfer then deletes the original source and returns `conflicts: 0`.

Reproduction: plan `old.md → dest/new.md`; wrap `_event()` so that after recording `intent` it renames `dest` to `dest-saved` and creates `dest` as a junction to a temporary directory outside the Vault. `apply()` succeeds, the external directory contains `new.md` with the approved payload, and `old.md` no longer exists. The same gap can redirect writes into an independent repository or redirect source lookup.

Protect/anchor every relevant ancestor before `mkdir`/`CREATE_NEW`, retain that protection through the operation, and bind final handles to the previously validated Vault namespace. Comparing the final handle only after `CREATE_NEW` is insufficient: it has already created an external file, and `mkdir` may already have created external directories. Add a native Windows junction-swap regression test.

## [P1] Verify the exact bytes used after reading each payload or original backup

Location: `99_System/knowledge/v2/transaction.py:252` and `277` (earlier verification is at `145–148`).

`_load()` verifies artifact hashes and closes the files, but `apply()`/`restore()` later reread them without checking those newly read bytes against the approved row hash. A backup artifact modified between these points is accepted. `_write()` only compares the result with `digest(payload)`, so this verifies the substituted bytes rather than the approved bytes. A move also deletes the valid source after writing the substitution.

Reproduction: wrap `_load()` to call the real loader, then change `payload/000000.bin` from `approved` to `unapproved` before returning. `apply()` returns `applied: 1, conflicts: 0`, writes `unapproved`, and deletes `old.md`. An equivalent change to `original/000000.bin` can make recovery overwrite or transfer unapproved original bytes. In a large batch the check/read interval spans the earlier operations, not merely a single file open.

Hash the exact immutable bytes passed into `_write()`/`_transfer()` against `after_sha256` or `before_sha256` immediately after reading, before any journaled mutation; alternatively retain and use the verified byte snapshots. Add post-load tampering tests for both apply and restore.

## [P2] Journal recovery intent and recognize completed recovery after interruption

Location: `99_System/knowledge/v2/transaction.py:278–292` (rejection at `231–232`).

Recovery changes data before appending `restored`, without first recording a recovery-specific intent. If the process stops after the mutation but before that journal append, the latest state remains `applied`. The next `restore()` requires the target still to have `after_sha256`, so it rejects an already restored entry as a later user edit. For a moved file, the restored source exists and the target is absent; for an in-place update, the target has `before_sha256`. Either case prevents recovery of all remaining rows because preflight is batch-wide.

Reproduction: apply an in-place change; wrap `_event()` to raise immediately before writing the `restored` event. The first restore writes the original bytes. Retrying restore raises `Later target edit must be preserved: old.md` even though `old.md` contains precisely the approved original bytes.

Persist recovery intent before mutation and reconcile the before/after namespace and hashes on restart, acknowledging an already completed recovery without overwriting any different user bytes. Test crash cuts after each successful restore mutation and before its terminal journal event.

## [P2] Recover the valid journal prefix when the final append is torn

Location: `99_System/knowledge/v2/transaction.py:152–158`.

The journal reader runs `json.loads()` on every split line with no incomplete-tail handling. A crash or disk-full condition while appending an event can leave a partial final JSON record. Thereafter both `apply()` and `restore()` fail while loading the journal, before using earlier durable records to recover the batch. `fsync` after a complete append does not make an interrupted append atomic.

Reproduction: apply a move successfully, append an unterminated final JSON object to `journal.jsonl`, then call `restore()`. It raises `JSONDecodeError` and cannot restore the already moved file through the supported recovery entry point.

Use framed/checksummed records or explicitly recover a valid prefix under an exclusive journal guard. Treat a malformed interior record as corruption, and preserve/reconcile an incomplete final append before writing further events. Add a truncated-tail recovery test.

## Coverage limits

The deterministic fault hooks model real gaps between existing calls; they are not changes to the implementation. The artifacts remain available in backups in these scenarios, but the current supported commands either perform an unapproved mutation or cannot complete recovery. No additional speculative findings are included.

## Remediation and verification — 2026-10-28

The four findings above are fixed in the current implementation, with a related existing-source recovery race also closed. This section supersedes the initial changes-required verdict for these verified findings; it does not constitute approval to execute a real migration.

- Directory ancestors from the approved root through both source and target parents are held with native Windows directory handles that deny write/delete sharing. Missing directories are created one component at a time under their already guarded parent, then opened without following reparse points and checked against the lexical absolute path before creating descendants. Handles remain held through journal events and transfer/recovery. The directory handle requests `FILE_LIST_DIRECTORY | FILE_READ_ATTRIBUTES`: native testing showed that attributes-only access does not enforce the needed rename protection. The approved `vault_root` is no longer freshly resolved during loading, preventing a root junction from rebinding the approved namespace. An opt-in `strict_path` parameter on the existing `_safe_stream` binds final file handles to the logical absolute path; existing v1 callers keep their default behavior.
- Apply and recovery hash the exact byte buffers read per row against the approved `after_sha256`/`before_sha256` before any mutation. Later artifact changes cannot substitute unapproved bytes.
- Recovery records durable `restore_intent`, recognizes already restored original bytes and paths after an interrupted terminal event, and reconciles them without rewriting different bytes. When an original source already exists, recovery exclusively locks and rechecks it, retaining its file lock until the migrated target has been checked and removed.
- Journal loading/appending holds an exclusive native file guard. Only an incomplete final append is discarded; a complete final JSON record lacking its newline is retained and terminated. Repair is flushed and synced before another append. Malformed terminated/interior records fail closed without altering the journal or Vault files.

TDD evidence: before implementation, the added regressions produced six expected assertion failures plus the three recovery-mode exceptions and the torn-tail exception. The additional recorded-root junction regression was separately observed failing before its fix. The original eleven tests continued to pass in that RED run. All 21 transaction tests are now green, covering existing and newly created ancestor junction swaps, recorded-root redirection, post-load payload/original tampering, terminal recovery-event loss for in-place/move/new-file operations, truncated journal tails, malformed interior records, and both recheck and lock retention for an existing restoration source.

Full verification: `python -B -m unittest discover -s 99_System/knowledge/tests -v` completed with **192 tests passing** in 97.144 seconds on native Windows, including the existing v1 `change_control` tests. `git diff --check` exited successfully; Git emitted only existing unrelated CRLF normalization warnings. Tests used temporary fixtures. No live Vault data, commits, or unrelated implementation files were changed.
