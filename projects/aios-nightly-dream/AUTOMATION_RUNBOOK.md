# AIOS Nightly Dream — Scheduled Trigger + Dedicated Gemini Runner

Status: active
Contract: `aios-dream-automation:v2`
Status date: 2026-10-02
Project ID: `aios-nightly-dream`

## Purpose

Run one delayed, cross-task memory-consolidation cycle each night without making scheduled ChatGPT responsible for canonical GitHub mutation.

ChatGPT Automation is the clock and **trigger only**. It creates one local trigger file on the authorized Browser Agent VM and stops. The persistent `browser-agent.service` consumes that file and launches the dedicated `nightly_dream_runner.py` with its existing runtime environment. Gemini performs salience triage, deep Dream synthesis, and bounded Memory drafting through that runner. GitHub remains canonical for project state, work-event history, Dream Run state, and long-term Memory.

## Production schedule

- timezone: `Asia/Tokyo`
- cadence: daily
- nominal run time: `02:00` after scheduled E2E acceptance
- scheduling mode: flexible nightly execution
- current rollout gate: keep the daily 02:00 automation disabled until the trigger-only scheduled E2E passes
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
5. Continue only when the Control Issue shows this dedicated runner as the live winning owner.
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

Production source acquisition is owned by the dedicated runner, never by scheduled ChatGPT:

1. List `ai-bulletin-board` issues with `state=all` and `since=<window_start>`, paginating to completion.
2. Fetch every selected issue's complete raw comment history and preserve GitHub's original timestamps, comment `id`, body, actor, and `author_association`.
3. Compare each Issue's declared comment count with the fetched complete history. A mismatch is source-inconsistent.
4. Reject rate-limit/error responses, missing pages, missing canonical timestamps, malformed rows, and incomplete pagination.
5. Feed the complete histories to the deterministic `ai-os-context` Dream bundle implementation in the runner process.
6. Scheduled ChatGPT must not fetch or reconstruct Dream source histories.

The dedicated runner may use a read-only GitHub REST source without granting that source write authority. Partial or rate-limited reads fail closed; they are never treated as canonical evidence.

If source acquisition is inconsistent, record HANDOFF when possible, do not call Gemini, do not perform deep synthesis or publishing, do not advance the watermark, and RELEASE Control #52.

Also load deferred candidates from the latest successful Dream cycle. Deferred candidates are analysis carryover, not Memory.

### 2. Salience triage

For each Phase 1 triage capsule:

- `history_unsafe` -> deterministic skip;
- unsettled/unverified work -> deterministic defer;
- verified completed work -> use the Gemini Web call path from the dedicated Nightly Dream runner.

Gemini only returns the five salience dimensions. AIOS code recomputes the weighted score and `skip/defer/deep` routing.

If Gemini is unavailable, malformed after bounded retry, or cannot be safely reached, do not substitute ChatGPT salience scoring. Persist the item as deferred with reason `gemini_unavailable` and retry in a later Dream cycle.

### 3. Gemini deep Dream

Only `deep` items and eligible deferred carryover enter Gemini synthesis through the dedicated runner. Scheduled ChatGPT does not receive the Dream bundle.

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

The installed ChatGPT Automation has one job: request startup of the dedicated runner. It must not read or write Dream GitHub state itself.

> Use Remote Desktop Commander on the authorized device `instance-20260926-031048`. Run exactly one local trigger operation in `/home/raku0220/browser-agent`: create or replace `tasks/aios-nightly-dream.trigger` with a small JSON object containing schema `aios-nightly-dream-trigger:v1`, source `chatgpt-automation`, and the current UTC request timestamp. Do not use GitHub, Supabase, Vercel, or Browser Agent tools directly. Do not acquire Control #52, create a Dream Run, perform Dream analysis, or write canonical state. After the trigger file is written successfully, stop.

The persistent Browser Agent service watches that file and launches the dedicated runner with its existing runtime credentials. The runner, not scheduled ChatGPT, owns Control #52, Dream Run state, Gemini calls, deterministic validation, and canonical write verification.

## Security and authority

- Never expose or persist secret values.
- Never use Dream to modify runtime/code/config outside explicitly allowed project or Memory paths.
- Dream may learn operational knowledge; it does not self-modify AIOS authority.
- GitHub canonical evidence outranks model output.
- Gemini scoring is routing input, not fact.
- Gemini synthesis is a proposal, not canonical truth.
- Scheduled ChatGPT has no Dream canonical-write role.
