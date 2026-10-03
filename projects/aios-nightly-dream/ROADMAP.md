# AIOS Nightly Dream — Roadmap

Status: active
Status date: 2026-10-03

## Phase 0 — Bootstrap and authority

Complete.

## Phase 1 — Gemini salience triage

Complete, with runtime optimization in progress.

- deterministic Triage Capsule from canonical history
- unauthenticated Gemini Web evaluator
- five dimensions: operational impact, reuse scope, novelty, recurrence, evidence strength
- AIOS-side score recomputation and threshold routing
- source fingerprint/version validation
- fail-closed defer when Gemini is unavailable

Current optimization: do not start any browser until deterministic prefiltering finds an eligible candidate; reuse one current-page Gemini session for the whole cycle.

## Phase 2 — Nightly Dream dry run

Core implementation complete.

- delayed source window and watermark
- canonical history replay
- immutable evidence/final-state reconstruction
- Gemini cross-task synthesis and memory reconciliation
- `promote|noop|defer|reject|supersede` proposals
- deterministic non-authoritative Dream Report

Revalidation target: execute this flow from Work/Direct AIOS without making Browser Agent the orchestrator.

## Phase 3 — Publish gate and Memory integration

Core implementation complete.

- deterministic proposal validation
- Global/Project/event-only routing
- secret/conflict/evidence/path checks
- branch + PR writes only
- exact/FTS refresh
- vector rebuild when required
- exact + semantic retrieval verification

## Phase 4 — Scheduled Work production

Status: revalidation in progress.

- personal Work scheduled task created successfully
- Work/AIOS is the scheduled executor
- structured GitHub/Supabase integrations are the normal collection/mutation path
- Gemini remains the independent evaluator
- browser transport is evaluator-only and lazy
- no browser startup on zero-eligible cycles
- at most one Gemini current-page session per cycle
- no GPT fallback salience scoring
- enforce one active Dream generation and idempotent retries
- advance watermark only after complete success
- pass one scheduled evaluator-only E2E and one full no-publish Dream dry run before restoring production cadence

Exit: a scheduled Work run completes canonical collection and independent Gemini evaluation without requiring the old RDP/script/browser orchestration chain.

## Phase 5 — Hardening

Status: active.

- unchanged-source/cache skips
- minimum recurring pattern evidence: 3
- dry-run/publish modes and quality metrics
- memory-health lint and relation/orphan checks
- failed-run, late-event, conflict, and repeated-cycle recovery tests
- evaluator/browser startup metrics
- prove zero-eligible cycles start no browser
- prove multi-candidate evaluation reuses one session/page

## Final acceptance

`daytime work -> canonical journal -> scheduled Work/AIOS -> deterministic prefilter -> lazy Gemini salience/deep Dream -> deterministic publish gate -> canonical Memory -> reindex -> next-day retrieval`

The design preserves AIOS authority and an independent evaluator while minimizing Browser Agent/Chromium runtime cost.
