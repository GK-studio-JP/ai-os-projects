# AIOS Nightly Dream — Scheduled AIOS Knowledge Maintenance

Status: active test/revalidation
Contract: `aios-dream-automation:v2`
Status date: 2026-10-03
Project ID: `aios-nightly-dream`
Canonical task: `GK-studio-JP/ai-bulletin-board#66`

## Purpose

At the end of each day, collect the day's canonical AIOS work across tasks, classify durable knowledge by AIOS storage boundary, publish it to the correct canonical source, refresh the RAG projection/index, verify retrieval, and leave a resumable canonical cycle result for the next run.

## Execution model

The scheduled ChatGPT turn is the recurring AIOS entrypoint. On every run it reads task #66 plus this runbook and `DREAM_CONTRACT.md`, then executes the cycle directly through connected AIOS integrations.

Preferred integrations:

- GitHub for canonical task history, project repositories, Global Memory source, branches, PRs, and Dream cycle state.
- Supabase for RAG/projection state and retrieval verification.
- Other connected structured APIs only when their canonical operational state is required.

Browser Agent, Remote Desktop Commander, Gemini, shell launchers, and dedicated browser runners are not prerequisites. Use Browser Agent only when a concrete required operation cannot be completed reliably through a structured integration.

## Schedule

Production target is daily at 02:00 Asia/Tokyo with a 3600-second settle delay.

During acceptance, do not wait for the daily schedule. Run the cycle directly from an interactive ChatGPT turn and use near-term one-shot scheduled runs only to validate unattended dispatch. After acceptance, restore the normal daily schedule.

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

### 2. Classify durable knowledge

Each candidate is classified into one destination:

- `global`: reusable across projects — AIOS architecture, shared tools, infrastructure facts, reusable workflows, troubleshooting, conventions, or cross-project lessons.
- `project`: project-specific requirements, decisions, designs, progress, deliverables, and domain knowledge.
- `event_only`: task ownership/progress/result facts that belong only in the bulletin-board journal.

Project-specific content must not be copied into Global Memory.

### 3. Reconcile

Before writing:

1. search the relevant RAG/projection for duplicates, updates, conflicts, and superseded knowledge;
2. page into the canonical GitHub source when exact current state matters;
3. reject secrets, credentials, cookies, tokens, transient browser state, unsupported inference, and unresolved contradictions;
4. prefer `noop` or `supersede` over duplicate knowledge.

### 4. Publish canonical source first

Global knowledge goes to `GK-studio-JP/ai-os-memory` using branch + PR. Project knowledge goes to the relevant project's canonical repository using its branch/PR authority. Event-only findings remain on `ai-bulletin-board`.

Supabase is a rebuildable projection, never the canonical source.

### 5. Reindex and verify

After a canonical merge:

1. verify the automatic main-push exact/FTS projection refresh;
2. verify exact/FTS retrieval in Supabase;
3. run the approved vector rebuild path when changed knowledge must be semantically searchable;
4. verify a paraphrased/semantic lookup after vectorization;
5. do not call the cycle successful while a required projection/index remains stale.

Use precise status language: Global Memory registered, FTS indexed, Vectorized, Hybrid verified.

### 6. Persist cycle result

Record `aios-dream-cycle:v1` with the cycle/window, tasks scanned, classification counts, decisions, canonical PRs/commits, index verification, and deferred items.

On complete success, append canonical RESULT, close the Dream Run, and RELEASE #52. A no-new-knowledge cycle may still succeed if source collection and index state are valid.

## Failure/retry

On partial failure:

- no RESULT;
- do not close the Dream Run;
- do not advance the watermark;
- record PROGRESS/HANDOFF with exact failure boundary and next action;
- RELEASE #52 when safe;
- resume the same cycle next time.

## Scheduled task prompt

> Use AIOS to read and execute `GK-studio-JP/ai-bulletin-board#66`. Read the current Nightly Dream runbook and contract at run time. Execute through connected structured integrations, preferring GitHub and Supabase. Browser Agent, Remote Desktop, Gemini, shell launchers, and dedicated browser runners are optional fallbacks only. Preserve resumable canonical state on partial failure.

## Success invariant

```text
daytime canonical work
  -> scheduled GPT AIOS entrypoint
  -> authenticated structured collection
  -> global/project/event-only classification
  -> canonical source write
  -> RAG reindex/vectorization
  -> exact + semantic retrieval verification
  -> canonical cycle result
```
