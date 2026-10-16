# SDD ledger — plan: D:/知识库/.context/claudian-dsh-compat-backup/2026-10-15-deepseek-chat-plan.md

User approved spec and plan, selected inline execution (option 1).
Tasks: 0 contract probe; 1 Roster; 2 Observer; 3 Journal/permissions; 4 execution/Stop; 5 real qualification/review/deployment.

Ruling: reuse the existing isolated extracted source workspace, which has no git repository — the approved plan explicitly prohibits initializing a repository or committing the Vault — checkpoints use logs, snapshots, and hashes; git-dependent sdd scripts are replaced by this ledger.

Pre-flight: Task 1 produces control(id), refreshControl(signal), DeepSeekJob and DeepSeekQueueItem consumed by Task 2. Task 2 produces rebaselineControl(signal), consumed by Task 4. Type ownership remains Roster and Observer only re-exports.
Pre-flight: Task 0's capability map gates Tasks 3/4 and deployment. Missing authenticated stopping or permission capability requires a separate bridge design review. No endpoint name may be guessed.
Pre-flight: Tasks 1/2 replace legacy NativeDefaults fixtures shared by Task 3/4; preserve behavior assertions and migrate fixture shape rather than normalizing inside fixtures.

Task 0: in progress. Active installed main.js expected hash 69d90e7f211385bd24879623bdc0e6676fad6333ae51c69cb922824c9d0c8422. No installed plugin changes yet.

Task 0: native probe exit 0. session/control, commands/execute, session/cancel, session/updateQueue and subagents/interruptByParent are registered. job/list, job/kill, session/projections and permissionPresets/catalog are not. collectSrcClaims has zero job namespace exports. Native jobs and permissionPresets services remain mounted. Current permission presets: read-only, workspace-write, danger-full-access.

Task 0: bridge design approved by user message “修”; native jobs.kill is a public process service, not a Remote export. Supplementary design: D:/知识库/.context/claudian-dsh-compat-backup/2026-10-15-deepseek-job-bridge-design.md.

Tasks 1/2: RED evidence prepared as explicitly permitted at Task 0 gate. Focused Roster + Observer integration run: 2 failed, 10 passed, 12 total; failures are current control queue/jobs stream rejection and unavailable job/list initialization. Log: current-protocol-red.log. These tasks are not complete.

Ruling: native control job rows omit ownership, while native jobs.list includes ownerless jobs — bucket membership alone does not prove ownership — supplemental bridge design includes an exact-owner list action as well as stop, with Roster remaining sole normalized-state owner. Incorrectly inferring all bucket jobs as owned could stop unrelated global work; this is rejected.

Ruling: permission catalog replacement needs no new privileged bridge — native permissions projection already advertises options and currentValue, and the original permission command remains available — retain semantic verification from permission/sandbox/approval events.

Tasks 1–4: source implementation and regression tests completed provisionally. Roster owns queue/job state; old job RPCs removed; exact-owner command bridge runs through native command authentication. Cold list projection replacement implemented, but final review found it incomplete (see below). Nested native tool-result correlation fixed with red/green evidence. No production console logging or dependencies added.

Task 5: real installed-native source harness passed first/second text messages, real file read tool completion, active-turn cancellation, exact-owner root background job stop and cross-root refusal, and persistent unseeded root cold history/resume. These are source-bundle results, not installed UI acceptance. Logs: real-chat-second.log, real-native-jobs.log, real-history-second.log. Persistent synthetic test records are retained; native records/locks were not deleted.

Verification: core integration 6 suites/150 tests passed with normal exit. Fresh complete Jest: 18 failed/515 passed suites, 38 failed/7727 passed/7 skipped tests, 7772 total. Exact failure names must be compared with original baseline; baseline had 38 failures. Two newly failing fixtures were migrated to current native wire shape and no longer fail. Typecheck/lint/build/performance had passed before these final fixture-only edits; repeat after review fixes.

Artifact: BuildCandidate.cjs produced a parseable, undeployed candidate by transplanting 12 changed global definitions plus six new dependencies. Reverse substitution proves every unrelated original byte is preserved. Candidate is NOT yet native-qualified or released. Installed main.js remains SHA-256 69d90e7f211385bd24879623bdc0e6676fad6333ae51c69cb922824c9d0c8422.

Independent final review: two Important findings accepted, release blocked. (1) Native command routing rejects live subagents, so querying child jobs through commands/list can retire the shared Host. Root-authorized descendant route needs native ownership verification and real child qualification. (2) Cold seeded/fork sessions deliberately lack list projections; list cache is not an authoritative cold projection contract. Need supported non-activating read and real seeded/cache-missing/stale-cache tests. No current claim of complete compatibility.

Ruling: do not deploy with either Important issue unresolved — ordinary chat success is insufficient to override Host isolation and cold-history requirements — cost is keeping current installed plugin unchanged until a safe candidate is qualified. A non-routine security-boundary question was sent asking whether to extend the bridge to native-verified descendants, without arbitrary caller-supplied agent IDs. Await that answer before implementation of the expanded bridge.
