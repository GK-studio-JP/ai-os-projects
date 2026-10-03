# AIOS Nightly Dream Contract v2

Status: active production contract under Work/Direct-AIOS revalidation
Status date: 2026-10-03

## Purpose

Turn verified AIOS work experience into durable knowledge after a settling period. Dream is delayed cross-task consolidation, not immediate post-task memory writing.

## Roles

- Scheduled Work/ChatGPT is the recurring AIOS entrypoint and resumes `ai-bulletin-board#66`.
- AIOS/ChatGPT is the executor for canonical collection, coordination, publish, and retrieval verification.
- GitHub is canonical for task history and repository mutation.
- Supabase is the rebuildable RAG/projection and retrieval-verification layer.
- Unauthenticated Gemini Web is the independent semantic evaluator for salience triage and deep synthesis.
- Browser transport is opened lazily for evaluator calls only; it is not the canonical mutation transport.
- `ai-bulletin-board` is the canonical work-event journal.
- `ai-os-memory` is canonical Global Memory.
- Each project repository is canonical for project-specific knowledge.

Gemini produces analysis/proposals only. AIOS deterministic policy and repository authority control writes.

## Source window

```text
window_start = previous successful window_end
window_end   = cycle start - settle_delay
source range = (window_start, window_end]
```

The watermark advances only after the full cycle succeeds.

## Source discovery

Dream reads canonical GitHub task history, not chat/model memory. Each candidate preserves authoritative timestamps, final replay state, corrections, RESULT/REVIEW evidence, artifacts, and a stable source fingerprint. Incomplete or unsafe histories cannot be promoted.

## Deterministic prefilter

Every candidate first enters a bounded `aios-dream-triage-capsule:v1`.

Before any Gemini/browser call:

- `history_unsafe` -> deterministic `skip`;
- incomplete/open/claimed -> deterministic `defer`;
- completed without verification evidence -> deterministic `defer`;
- unchanged source may reuse an existing triage result only when source fingerprint, triage version, and relevant routing policy version match.

Zero eligible candidates means zero Gemini/browser startup.

## Gemini salience result

Eligible completed/verified candidates are evaluated by unauthenticated Gemini Web.

Gemini returns the five dimensions:

- `operational_impact`
- `reuse_scope`
- `novelty`
- `recurrence`
- `evidence_strength`

AIOS validates the result and recomputes the weighted score itself. Gemini's own score or decision is never authoritative.

Default routing:

- `salience < 0.35`: `skip`
- `0.35 <= salience < 0.65`: `defer`
- `salience >= 0.65`: `deep`

If Gemini is unavailable or malformed after bounded retry, defer with `gemini_unavailable`. ChatGPT/GPT must not silently replace Gemini's salience judgment.

## Evaluator runtime contract

- Start browser transport lazily only after deterministic prefiltering finds at least one eligible candidate.
- Use at most one Gemini session per Dream cycle.
- Reuse one current Gemini page for all triage calls and deep synthesis where possible.
- Do not require `newPage` or `switchPage` when a usable current page exists.
- Prefer the browser transport available in the scheduled Work runtime when it can produce the required schema-valid result.
- The existing Browser Agent current-page path is an approved fallback evaluator transport.
- Evaluator transport failure does not grant GPT permission to self-evaluate; affected candidates remain deferred.

## Deep Dream

Only `deep` candidates and eligible deferred carryover enter Gemini deep synthesis.

Deep synthesis performs:

1. final-state reconstruction;
2. superseded-conclusion removal;
3. cross-task comparison;
4. existing-memory reconciliation;
5. duplicate/update/contradiction detection;
6. consolidation and pattern detection;
7. Global/Project/event-only scope classification;
8. structured proposal generation.

The output remains non-authoritative and uses `promote|noop|defer|reject|supersede`.

Recurring promoted patterns normally require at least three independent qualifying source tasks unless stronger authoritative evidence establishes the fact directly.

## Storage boundary

Every durable finding is classified as:

- `global`: reusable cross-project operational knowledge;
- `project`: project-specific knowledge retained in its project source/RAG;
- `event_only`: work-event state retained only in the bulletin board.

A finding must not be copied into Global Memory merely because it may be useful later.

## Publish gate

Before canonical mutation, deterministic validation confirms scope, evidence, source-history safety, target repository/path authority, conflict state, secret rejection, and branch+PR write mode.

Global candidates target `ai-os-memory`; project candidates target the relevant project repository; event-only candidates are not written to long-term Memory.

Gemini output, salience, browser success, or a GPT assertion is never sufficient proof by itself.

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

Each completed cycle records tasks scanned, triage counts, proposal decisions, evaluator status, canonical commits/PRs, index status, retrieval verification, and deferred items.

A successful no-op is valid. A partial failure has no RESULT, does not close the run, does not advance the watermark, and preserves a resumable HANDOFF.

## Acceptance

```text
canonical daily work
  -> scheduled Work / AIOS entrypoint
  -> structured source retrieval
  -> deterministic prefilter
  -> lazy Gemini salience + deep synthesis
  -> deterministic publish gate
  -> canonical Global/Project source
  -> RAG index/vector refresh
  -> retrieval verification
  -> canonical resumable cycle state
```
