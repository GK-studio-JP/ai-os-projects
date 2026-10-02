# AIOS Nightly Dream — Roadmap

Status: active
Status date: 2026-10-02

## Phase 0 — Bootstrap and authority

- register `aios-nightly-dream` in `ai-os-projects`
- codify Dream decisions, handoff, roadmap, and execution contract
- extend `PROC-AIOS.routing.target_repositories` to include `GK-studio-JP/ai-os-memory` and `GK-studio-JP/ai-bulletin-board`
- do not add new Kernel capabilities

Exit: AIOS can route Nightly Dream implementation tasks to every required repository through existing branch-write authority.

## Phase 1 — Gemini salience triage

- define the deterministic Triage Capsule built from canonical task history
- add a structured salience-triage mode to the existing unauthenticated Gemini Browser Worker
- return 0..1 salience plus operational-impact, reuse-scope, novelty, recurrence, and evidence-strength dimensions
- add source fingerprint, triage version, threshold routing, defer, and unchanged-source skip
- cover repeated, corrected, superseded, and incomplete task histories

Exit: existing Gemini Web can triage canonical work experience with no Gemini API billing and no canonical write authority.

## Phase 2 — Nightly Dream dry run

- define Dream Run window, settling delay, watermark, and source discovery
- replay canonical bulletin-board histories
- collect immutable evidence and reconstruct final state
- perform ChatGPT cross-task synthesis, existing-memory reconciliation, and pattern detection
- emit structured promote/noop/defer/reject/supersede proposals
- generate a deterministic cycle summary without canonical writes

Exit: a nightly dry run produces an auditable Dream Report.

## Phase 3 — Publish gate and Memory integration

- implement deterministic proposal validation
- enforce Global vs Project vs event-only routing
- reject secrets, unresolved contradictions, insufficient evidence, and disallowed paths
- publish allowed changes only through branch + PR
- reindex Global Memory after canonical merge
- verify exact and semantic retrieval where available

Exit: a verified candidate can safely become canonical operational memory.

## Phase 4 — ChatGPT Automation production

- install the Nightly Dream scheduled automation
- enforce one active Dream generation
- make retries idempotent
- advance watermark only after complete success
- persist cycle summary and deferred state

Exit: daytime experience is consolidated nightly and becomes available to next-day AIOS workers without manual triggering.

## Phase 5 — Hardening

- add `no_new_evidence` pattern skips
- configure minimum pattern evidence, default 3
- add dry-run/publish modes and quality metrics
- add memory-health lint, relation/orphan checks, and recovery tests
- test failed Dream runs, late events, conflicts, and repeated cycles

## Final acceptance

`daytime work → canonical journal → Gemini salience triage → ChatGPT deep Dream → deterministic publish gate → canonical Memory → reindex → next-day retrieval` works end to end while preserving AIOS authority and storage boundaries.
