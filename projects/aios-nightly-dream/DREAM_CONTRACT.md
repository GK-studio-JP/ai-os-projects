# AIOS Nightly Dream Contract v2

Status: active production contract under direct-AIOS revalidation
Status date: 2026-10-03

## Purpose

Turn verified AIOS work experience into durable knowledge after a settling period. Dream is delayed cross-task consolidation, not immediate post-task memory writing.

## Roles

- Scheduled ChatGPT is the recurring AIOS entrypoint and resumes `ai-bulletin-board#66`.
- GitHub is the preferred structured integration for canonical task history and repository mutation.
- Supabase is the rebuildable RAG/projection and retrieval-verification layer.
- Browser Agent is an optional UI fallback only when no reliable structured/API operation exists.
- `ai-bulletin-board` is the canonical work-event journal.
- `ai-os-memory` is canonical Global Memory.
- Each project repository is canonical for project-specific knowledge.

Remote Desktop, Gemini, shell launchers, and dedicated browser runners do not form a required Nightly Dream execution chain.

## Source window

```text
window_start = previous successful window_end
window_end   = cycle start - settle_delay
source range = (window_start, window_end]
```

The watermark advances only after the full cycle succeeds.

## Source discovery

Dream reads canonical GitHub task history, not chat/model memory. Each candidate preserves authoritative timestamps, final replay state, corrections, RESULT/REVIEW evidence, artifacts, and a stable source fingerprint. Incomplete or unsafe histories are deferred and cannot be promoted.

## Storage boundary

Every durable finding is classified as:

- `global`: reusable cross-project operational knowledge;
- `project`: project-specific knowledge retained in its project source/RAG;
- `event-only`: work-event state retained only in the bulletin board.

A finding must not be copied into Global Memory merely because it may be useful later.

## Proposal decisions

Candidates use `promote|noop|defer|reject|supersede`.

Promotion/supersede requires canonical evidence. Secrets, credentials, cookies, tokens, transient browser content, psychological inference, unsupported claims, and unresolved contradictions are excluded.

Recurring patterns normally require at least three independent qualifying experiences unless a stronger authoritative source establishes the fact directly.

## Publish gate

Before canonical mutation, deterministic validation confirms scope, evidence, target repository/path authority, conflict state, and branch+PR write mode.

Global candidates target `ai-os-memory`; project candidates target the relevant project repository; event-only candidates are not written to long-term Memory.

## RAG/index contract

Canonical source is written first. Supabase is refreshed from canonical source.

A changed Global Memory candidate is complete only after:

1. canonical merge;
2. exact/FTS projection refresh;
3. exact retrieval verification;
4. vector rebuild when semantic search is required;
5. paraphrased/semantic retrieval verification after vectorization.

Do not describe lexical-only retrieval as hybrid.

## Coordination

Permanent control is `ai-bulletin-board#52`. Only one live generation owns a cycle. Incomplete cycles are resumed before newer windows. Idempotency keys prevent duplicate coordination writes.

## Cycle result

Each completed cycle records tasks scanned, storage classification counts, proposal decisions, canonical commits/PRs, index status, retrieval verification, and deferred items.

A successful no-op is valid. A partial failure has no RESULT, does not close the run, does not advance the watermark, and preserves a resumable HANDOFF.

## Acceptance

```text
canonical daily work
  -> scheduled AIOS entrypoint
  -> structured source retrieval
  -> boundary classification
  -> canonical Global/Project source
  -> RAG index/vector refresh
  -> retrieval verification
  -> canonical resumable cycle state
```
