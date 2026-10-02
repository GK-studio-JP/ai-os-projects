# AIOS Nightly Dream — Scheduled Trigger + Gemini Runner

Status: active
Contract: `aios-dream-automation:v2`
Status date: 2026-10-02
Project ID: `aios-nightly-dream`

## Purpose

Run one delayed, cross-task memory-consolidation cycle each night without adding a timer daemon.

ChatGPT Automation is the clock and launcher only. It performs authenticated read-only source acquisition through the connected GitHub app, materializes the snapshot, starts the dedicated Nightly Dream Gemini runner through Remote Desktop Commander, and verifies the resulting canonical state. It must not append CLAIM/HEARTBEAT/PROGRESS/HANDOFF/RESULT itself and must not perform Dream synthesis.

The dedicated Nightly Dream runner owns Dream coordination writes through Browser Agent and uses Gemini for salience triage and deep synthesis. GitHub remains canonical for project state, work-event history, Dream Run state, and long-term Memory. Chat history and model memory are never authoritative inputs.

## Production schedule

- timezone: `Asia/Tokyo`
- cadence: daily
- nominal run time: `02:00`
- scheduling mode: flexible nightly execution
- settle delay: `3600` seconds
- effective source window end: automation start minus settle delay
- bootstrap watermark: `2026-10-02T00:00:00+09:00`

The actual automation may execute within the platform's flexible scheduling window. The source window is derived from canonical timestamps, never from an assumed exact trigger second.

## Existing contracts used

1. Gemini salience triage: `aios-dream-triage-capsule:v1` -> `aios-dream-triage-result:v1`.
2. Nightly source reconstruction: `aios-dream-source-bundle:v1`.
3. Gemini deep synthesis: `aios-dream-report:v1` / `aios-dream-proposal:v1`.
4. Global Memory publish gate: `aios-memory-publish-request:v1` -> `aios-memory-publish-plan:v1`.
5. Canonical work journal: `ai-bulletin-board`.
6. Canonical Global Memory: `ai-os-memory`.

## Dream Run identity

Each cycle has exactly one GitHub Issue in `GK-studio-JP/ai-bulletin-board`.

Title:

```text
[AIOS][aios-nightly-dream-run] <cycle-id>
```

The Issue body contains a normal `ai-os-task:v1` task envelope plus this immutable metadata block:

```json
{
  "schema": "aios-dream-run:v1",
  "cycle_id": "sha256:<hex>",
  "contract_version": 2,
  "window_start": "<ISO-8601>",
  "window_end": "<ISO-8601>",
  "settle_delay_seconds": 3600,
  "previous_success_issue": 0,
  "previous_success_window_end": "<ISO-8601 or null>"
}
```

`cycle_id` is the SHA-256 of the canonical string:

```text
aios-nightly-dream:v1|<window_start>|<window_end>
```

The same window therefore always resolves to the same cycle identity.

## Watermark rule

Determine `window_start` from the most recent successfully completed Dream Run. A run is successful only when:

- its Dream Run Issue contains a canonical RESULT event;
- it contains one `aios-dream-cycle:v1` state record with `status=completed`;
- that state record is bound to the same `cycle_id` and `window_end`.

If there is no previous successful run, use the bootstrap watermark above.

Never advance the watermark for a failed, interrupted, partially published, or otherwise incomplete cycle.

## Single-generation lock

Permanent control task: `GK-studio-JP/ai-bulletin-board#52`.

Before touching any Dream Run Issue:

1. Fetch Control Issue #52 and replay the canonical `ai-bb:v1` history.
2. If it is `history_unsafe`, abort the cycle without creating or mutating a Dream Run.
3. If another live owner holds the control lease, do not create a competing generation.
4. If open, append a CLAIM using an attempt-scoped idempotency key and immediately refetch/replay.
5. Continue only when the Control Issue shows the dedicated Nightly Dream runner as the live winning owner.
6. Renew the control lease with HEARTBEAT before 900 seconds elapse during a long cycle.
7. RELEASE the Control Issue after either successful completion or a safely recorded failure/handoff. Never append RESULT to the permanent Control Issue.

After the control lease is acquired:

1. Search open Dream Run Issues.
2. If an Issue with the same `cycle_id` exists, resume it instead of creating another.
3. If any older Dream Run Issue is still open, resume the oldest incomplete run before starting a newer window.
4. Create a new Issue only when no incomplete Dream Run exists.

This two-level rule prevents duplicate creation races and prevents a later window from skipping an unfinished earlier cycle.

Use normal `ai-bb:v1` CLAIM/HEARTBEAT/HANDOFF/RESULT semantics inside each Dream Run Issue. Reclaims after lease expiry use a new attempt-scoped idempotency key. RESULT uses one stable cycle-scoped idempotency key.

## Cycle procedure

### 1. Reconstruct the source window

Read canonical GitHub state and build the Phase 2 Dream source bundle for `(window_start, window_end]`. Preserve settling exclusions, canonical timeline, final replay state, corrections, RESULT/REVIEW evidence, and source fingerprints.

Production source acquisition is split from execution:

1. The scheduled ChatGPT launcher uses the connected GitHub application's raw REST fetch capability in read-only mode for `ai-bulletin-board` issue and issue-comment JSON.
2. Preserve GitHub's original `created_at`, `updated_at`, `closed_at`, `author_association`, comment `id`, and comment `body` fields.
3. Include Control Issue #52, every open Dream Run, the latest successful Dream Run needed to recover the watermark, and every source issue required for the resolved window.
4. Materialize the fetched histories as `aios-dream-histories:v1` on the authorized production VM.
5. Start the dedicated `nightly_dream_runner.py` with that snapshot and the persistent Browser Agent session.
6. The runner builds the deterministic Phase 2 bundle offline with `ai-os-context` code and owns all subsequent Dream mutations through Browser Agent.
7. After runner completion, the scheduled launcher may perform authenticated read-only verification of Control #52 and the Dream Run Issue. It must not repair failed writes itself.

The scheduled production path must not use `ai-os-context dream-bundle`, because that command constructs the live `GitHubClient()` and may fall back to anonymous REST. It also must not use a normalized issue-comment connector response as replay input when canonical timestamps are absent.

If authenticated source acquisition fails, do not start the runner. If the runner detects a malformed/incomplete snapshot or deterministic bundle failure after acquiring a lease, it records HANDOFF/RELEASE itself and does not call Gemini, publish, or advance the watermark.

Also load deferred candidates from the latest successful Dream cycle. Deferred candidates are analysis carryover, not Memory.

### 2. Salience triage

For each Phase 1 triage capsule:

- `history_unsafe` -> deterministic skip;
- unsettled/unverified work -> deterministic defer;
- verified completed work -> use the existing unauthenticated Gemini Browser Worker path.

Gemini only returns the five salience dimensions. AIOS code recomputes the weighted score and `skip/defer/deep` routing.

If Gemini is unavailable, malformed after bounded retry, or cannot be safely reached, do not substitute ChatGPT salience scoring. Persist the item as deferred with reason `gemini_unavailable` and retry in a later Dream cycle.

### 3. Gemini deep Dream

Only `deep` items and eligible deferred carryover enter Gemini synthesis through the dedicated Nightly Dream runner.

Gemini must:

- reconstruct final state across tasks;
- discard superseded intermediate conclusions;
- compare repeated successes/failures;
- reconcile against existing Global/Project Memory;
- emit only `promote/noop/defer/reject/supersede`;
- classify scope as `global/project/event_only`;
- require evidence for promote/supersede;
- require at least three source tasks for a promoted pattern unless a stronger canonical rule already establishes the fact;
- avoid psychological inference.

The output remains a non-authoritative `aios-dream-report:v1`.

### 4. Publish gate

For Global `promote/supersede` proposals, construct a Memory publish request and run the Phase 3 gate.

Only a valid `aios-memory-publish-plan:v1` may produce a repository change.

Rules:

- branch + PR only;
- no direct canonical write;
- initial Dream targets are limited to `knowledge/lessons/**.md` and `knowledge/troubleshooting/**.md`;
- reject secrets, path traversal, unknown evidence, unsafe sources, and scope violations;
- main-push exact/FTS projection refresh is automatic and embedding-free;
- full vector rebuild remains explicit `workflow_dispatch`.

If a Memory PR cannot be fully validated/merged during the cycle, persist that proposal as deferred with reason `publish_pending`; do not silently treat it as canonical Memory.

Project-scope proposals stay in the relevant project repository and must obey that repository's branch/PR authority. Event-only proposals are never published to Memory.

### 5. Persist cycle state

Append one trusted GitHub comment containing:

```json
{
  "schema": "aios-dream-cycle:v1",
  "cycle_id": "sha256:<hex>",
  "status": "completed",
  "window_start": "<ISO-8601>",
  "window_end": "<ISO-8601>",
  "bundle_fingerprint": "sha256:<hex>",
  "counts": {
    "selected": 0,
    "triage_skip": 0,
    "triage_defer": 0,
    "triage_deep": 0,
    "promote": 0,
    "noop": 0,
    "defer": 0,
    "reject": 0,
    "supersede": 0
  },
  "deferred": [],
  "memory_prs": [],
  "project_prs": []
}
```

Each deferred entry must carry enough provenance to retry without turning it into Memory:

- proposal/candidate identifier;
- source task(s);
- source fingerprint(s);
- reason;
- last evaluated cycle;
- relevant evidence refs.

Do not store secrets or raw transient browser contents.

Then append the canonical `ai-bb:v1` RESULT event and close the Dream Run Issue.

## Successful no-op cycles

A cycle with no promotable knowledge may still complete successfully. It must still persist its cycle summary and deferred carryover, append RESULT, and advance the watermark to `window_end`.

## Failure and retry

On an unrecoverable cycle failure:

- do not append RESULT;
- do not close the Dream Run Issue;
- do not advance the watermark;
- append PROGRESS or HANDOFF with the failure boundary and next action when possible;
- allow the lease to be reclaimed;
- the next automation run resumes the same `cycle_id`.

Never create a new generation merely to escape an unfinished older cycle.

## Automation prompt

The installed ChatGPT Automation must execute this instruction on every run:

> Launch one AIOS Nightly Dream production cycle. Read the current canonical `projects/aios-nightly-dream/AUTOMATION_RUNBOOK.md` and `DREAM_CONTRACT.md`. Do not perform Dream synthesis and do not mutate GitHub. Use the connected GitHub app only for authenticated raw REST reads needed to materialize one complete `aios-dream-histories:v1` snapshot containing Control #52, open Dream Runs, the latest successful Dream Run, and all source issues/comments required by the Dream window. Then use Remote Desktop Commander to materialize that snapshot on the authorized production VM and start the dedicated `nightly_dream_runner.py` against persistent Browser Agent session `gcp-browser-1`. The runner, not ChatGPT Automation, owns CLAIM/HEARTBEAT/HANDOFF/RESULT/RELEASE writes and uses Gemini for salience triage and deep synthesis. After the runner exits, use authenticated read-only GitHub fetches only to verify the canonical outcome. Do not repair or substitute runner writes from the scheduled GPT. Do not enable a new window if an older Dream Run remains incomplete.

## Security and authority

- Never expose or persist secret values.
- Never use Dream to modify runtime/code/config outside explicitly allowed project or Memory paths.
- Dream may learn operational knowledge; it does not self-modify AIOS authority.
- GitHub canonical evidence outranks model output.
- Gemini scoring is routing input, not fact.
- Gemini deep synthesis is a proposal, not canonical truth.
- ChatGPT Automation is a launcher/monitor and has no Dream mutation role.
