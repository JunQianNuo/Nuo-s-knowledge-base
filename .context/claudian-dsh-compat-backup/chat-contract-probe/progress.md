# SDD ledger — plan: D:/知识库/.context/claudian-dsh-compat-backup/2026-10-15-deepseek-chat-plan.md

User approved spec and plan, selected inline execution (option 1).
Tasks: 0 contract probe; 1 Roster; 2 Observer; 3 Journal/permissions; 4 execution/Stop; 5 real qualification/review/deployment.

Ruling: reuse the existing isolated extracted source workspace, which has no git repository — the approved plan explicitly prohibits initializing a repository or committing the Vault — checkpoints use logs, snapshots, and hashes; git-dependent sdd scripts are replaced by this ledger.

Pre-flight: Task 1 produces control(id), refreshControl(signal), DeepSeekJob and DeepSeekQueueItem consumed by Task 2. Task 2 produces rebaselineControl(signal), consumed by Task 4. Type ownership remains Roster and Observer only re-exports.
Pre-flight: Task 0's capability map gates Tasks 3/4 and deployment. Missing authenticated stopping or permission capability requires a separate bridge design review. No endpoint name may be guessed.
Pre-flight: Tasks 1/2 replace legacy NativeDefaults fixtures shared by Task 3/4; preserve behavior assertions and migrate fixture shape rather than normalizing inside fixtures.

Task 0: in progress. Active installed main.js expected hash 69d90e7f211385bd24879623bdc0e6676fad6333ae51c69cb922824c9d0c8422. No installed plugin changes yet.

Task 0: native probe exit 0. session/control, commands/execute, session/cancel, session/updateQueue and subagents/interruptByParent are registered. job/list, job/kill, session/projections and permissionPresets/catalog are not. collectSrcClaims has zero job namespace exports. Native jobs and permissionPresets services remain mounted. Current permission presets: read-only, workspace-write, danger-full-access.

Task 0: safety gate reached. Native jobs.kill exists only as a public process service, not a Remote export. Original spec and plan require separate bridge approval. Supplementary design saved to D:/知识库/.context/claudian-dsh-compat-backup/2026-10-15-deepseek-job-bridge-design.md. No production implementation or deployment while awaiting this approval.

Tasks 1/2: RED evidence prepared as explicitly permitted at Task 0 gate. Focused Roster + Observer integration run: 2 failed, 10 passed, 12 total; failures are current control queue/jobs stream rejection and unavailable job/list initialization. Log: current-protocol-red.log. These tasks are not complete.

Ruling: native control job rows omit ownership, while native jobs.list includes ownerless jobs — bucket membership alone does not prove ownership — supplemental bridge design includes an exact-owner list action as well as stop, with Roster remaining sole normalized-state owner. Incorrectly inferring all bucket jobs as owned could stop unrelated global work; this is rejected.

Ruling: permission catalog replacement needs no new privileged bridge — native permissions projection already advertises options and currentValue, and the original permission command remains available — retain semantic verification from permission/sandbox/approval events.
