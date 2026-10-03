# AIOS Nightly Dream — Scheduled AIOS Knowledge Maintenance

Status: active test/revalidation
Contract: `aios-dream-automation:v2`
Status date: 2026-10-03
Project ID: `aios-nightly-dream`
Canonical task: `GK-studio-JP/ai-bulletin-board#66`

## Purpose

At the end of each day, collect the day's canonical AIOS work across tasks, evaluate durable knowledge after the settling window, publish only validated knowledge to the correct canonical source, refresh the RAG projection/index, verify retrieval, and leave a resumable canonical cycle result for the next run.

## Execution model

The scheduled Work/ChatGPT turn is the recurring AIOS entrypoint. On every run it reads task #66 plus this runbook and `DREAM_CONTRACT.md`, then executes the cycle through connected AIOS integrations.

AIOS is the executor and canonical authority boundary:

- GitHub: canonical task history, project repositories, Global Memory source, branches/PRs, Dream cycle state.
- Supabase: rebuildable RAG/projection state and retrieval verification.
- Other connected structured APIs: only when required for canonical operational state.

Gemini Web is the independent semantic evaluator. It does not own scheduling, coordination, GitHub/Supabase mutation, Memory publication, or RAG indexing.

Browser execution is evaluator transport only. Do not use Browser Agent, Remote Desktop, shell launchers, or a dedicated browser runner to orchestrate the normal Dream cycle when structured integrations can perform the operation directly.

## Schedule

Production target is daily at 02:00 Asia/Tokyo with a 3600-second settle delay.

During acceptance, do not wait for the daily schedule. Use near-term one-shot Work scheduled runs for unattended dispatch/evaluator verification. Restore the production cadence only after one full dry-run boundary succeeds.

## Window and watermark

```text
window_start = previous successful Dream window_end
window_end   = cycle start - settle delay
source range = (window_start, window_end]
```

Bootstrap watermark: `2026-10-02T00:00:00+09:00`.

A successful watermark exists only when the Dream Run contains both an `aios-dream-cycle:v1` record with `status=completed` and a canonical `ai-bb:v1` RESULT for the same cycle. Partial/failed runs never advance the watermark.

## Coordination

Permanent serialization task: `GK-studio-JP/ai-bulletin-board#52`.

Use the GitHub integration directly to replay #52, acquire a CLAIM, verify the live owner, and RELEASE after success or safe failure. Resume the oldest incomplete Dream Run before starting a newer window. Retries use the same cycle identity and do not skip unfinished work.

## Cycle

### 1. Collect canonical work

Read `ai-bulletin-board` through authenticated GitHub access. For tasks changed in the source window, fetch the Issue body and complete canonical comment history. Preserve timestamps, IDs, final state, corrections, RESULT/REVIEW evidence, repository refs, and source fingerprints.

Exclude Dream control/cycle coordination from knowledge candidates. Fail closed on incomplete history or malformed canonical evidence.

### 2. Deterministic prefilter

Build the existing `aios-dream-triage-capsule:v1` for each candidate and apply deterministic gates before any browser is started:

- `history_unsafe` -> `skip`;
- incomplete/open/claimed work -> `defer`;
- completed work without verification evidence -> `defer`;
- a prior triage result may be reused only when source fingerprint, triage version, and relevant policy version are unchanged.

If no candidate remains eligible for semantic evaluation, complete the evaluation stage without starting Gemini or Chromium.

### 3. Gemini salience evaluation

For each eligible completed/verified candidate, use unauthenticated Gemini Web as the independent evaluator.

Runtime rules:

- start evaluator browser transport lazily only when at least one eligible candidate exists;
- start at most one Gemini browser session per Dream cycle;
- reuse the same current page for all triage calls and any later deep synthesis;
- avoid `newPage` / `switchPage` when a usable current page exists;
- Gemini receives only bounded canonical capsules/context and has no canonical write authority;
- Gemini returns the five dimensions: `operational_impact`, `reuse_scope`, `novelty`, `recurrence`, `evidence_strength`;
- AIOS validates schema/fingerprint/version and recomputes salience deterministically;
- routing thresholds remain: `<0.35 skip`, `0.35..<0.65 defer`, `>=0.65 deep`;
- if Gemini is unavailable or malformed after bounded retry, mark the candidate `defer` with `gemini_unavailable`; do not substitute GPT/ChatGPT salience scoring.

Prefer the browser transport already available to the scheduled Work run when it can return the required schema-valid Gemini result. The existing Browser Agent current-page evaluator path remains a fallback transport, not the normal Dream orchestrator.

### 4. Gemini deep synthesis and storage classification

Only `deep` candidates plus eligible deferred carryover enter deep synthesis. Reuse the same Gemini session when it is already open.

Deep synthesis must:

- reconstruct final state across tasks and discard superseded intermediate conclusions;
- reconcile against relevant existing Global/Project Memory;
- emit only `promote|noop|defer|reject|supersede`;
- classify each proposal as `global|project|event_only`;
- bind promote/supersede to canonical evidence;
- require at least three independent source tasks for a recurring promoted pattern unless stronger authoritative evidence establishes it directly;
- avoid psychological inference.

The Dream Report remains non-authoritative. Gemini output never directly authorizes a write.

### 5. Reconcile and deterministic publish gate

Before writing:

1. search the relevant RAG/projection for duplicates, updates, conflicts, and superseded knowledge;
2. page into canonical GitHub source when exact state matters;
3. reject secrets, credentials, cookies, tokens, transient browser state, unsupported inference, and unresolved contradictions;
4. prefer `noop` or `supersede` over duplicate knowledge;
5. pass the deterministic repository-specific publish gate.

Global knowledge targets `GK-studio-JP/ai-os-memory` using branch + PR. Project knowledge targets the relevant project canonical repository. Event-only findings remain on `ai-bulletin-board`.

Supabase is a rebuildable projection, never the canonical source.

### 6. Reindex and verify

After a canonical merge:

1. verify automatic main-push exact/FTS projection refresh;
2. verify exact/FTS retrieval in Supabase;
3. run the approved vector rebuild path when changed knowledge must be semantically searchable;
4. verify a paraphrased/semantic lookup after vectorization;
5. do not call the cycle successful while a required projection/index remains stale.

Use precise status language: Global Memory registered, FTS indexed, Vectorized, Hybrid verified.

### 7. Persist cycle result

Record `aios-dream-cycle:v1` with the cycle/window, tasks scanned, triage counts, proposal decisions, canonical PRs/commits, evaluator status, index verification, and deferred items.

On complete success, append canonical RESULT, close the Dream Run, and RELEASE #52. A no-new-knowledge cycle may still succeed if source collection and required index state are valid.

## Failure/retry

On partial failure:

- no RESULT;
- do not close the Dream Run;
- do not advance the watermark;
- record PROGRESS/HANDOFF with exact failure boundary and next action;
- RELEASE #52 when safe;
- resume the same cycle next time.

A Gemini transport failure is normally a candidate-level defer, not a reason to replace the evaluator with GPT.

## Scheduled task prompt

> Use AIOS to read and execute `GK-studio-JP/ai-bulletin-board#66`. Read the current Nightly Dream runbook and contract at run time. Use GitHub/Supabase structured integrations for collection, coordination, canonical writes, and retrieval verification. Apply deterministic prefiltering before browser work. For eligible completed/verified candidates, use unauthenticated Gemini Web as the independent semantic evaluator; AIOS must recompute the score and must not substitute GPT salience scoring if Gemini is unavailable. Do not start a browser when there are no eligible Gemini candidates. Reuse one Gemini current-page session for triage and deep synthesis when needed. Preserve resumable canonical state on partial failure.

## Success invariant

```text
daytime canonical work
  -> scheduled Work / AIOS entrypoint
  -> authenticated structured collection
  -> deterministic prefilter
  -> lazy Gemini independent evaluation
  -> AIOS deterministic routing + publish gate
  -> canonical Global/Project source
  -> RAG reindex/vectorization
  -> exact + semantic retrieval verification
  -> canonical cycle result
```
