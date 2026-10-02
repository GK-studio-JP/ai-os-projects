# AIOS Nightly Dream

Status: active
Project ID: `aios-nightly-dream`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Consolidate AIOS work experience across tasks after a daily settling period and promote only verified, reusable operational knowledge into canonical Global or Project Memory.

## Current phase

Phase 4 — ChatGPT Automation production.

## Completed foundation

- Phase 0: project registration and `PROC-AIOS` repository authority are complete. `ai-os-memory` and `ai-bulletin-board` are explicit targets without adding Kernel capabilities.
- Phase 1: existing unauthenticated Gemini Web is the salience-triage provider. AIOS recomputes salience/routing deterministically; Gemini has no canonical write authority.
- Phase 2: `ai-os-context` provides deterministic nightly source bundles and non-authoritative ChatGPT dry-run report validation.
- Phase 3: `ai-os-memory` provides the Memory publish gate, branch/PR-only writes, automatic main-push exact/FTS refresh without embeddings, and explicit workflow-dispatch vector rebuild.

## Production execution

- ChatGPT Automation is the nightly clock and deep Dream executor; no timer daemon is introduced.
- Canonical execution contract: `projects/aios-nightly-dream/AUTOMATION_RUNBOOK.md`.
- Timezone: `Asia/Tokyo`.
- Nominal schedule: nightly at 02:00 with flexible scheduling.
- Settling delay: 3600 seconds.
- Bootstrap watermark: `2026-10-02T00:00:00+09:00`.
- One open Dream Run Issue is the cycle lock. An identical/incomplete cycle is resumed rather than duplicated.
- The watermark advances only after a canonical Dream cycle state plus `ai-bb:v1` RESULT.
- Deferred candidates remain Dream Run state and are retried later; they are not long-term Memory.
- If Gemini triage is unavailable, the candidate is deferred. ChatGPT must not replace Gemini's salience role.
- Global Memory publication requires the deterministic Phase 3 gate and branch + PR.

## Canonical boundaries

- Work experience: `GK-studio-JP/ai-bulletin-board`.
- Global long-term Memory: `GK-studio-JP/ai-os-memory`.
- Project-specific Memory: the relevant project repository.
- Search/vector data: rebuildable projection only.
- Chat/model memory is never authoritative Dream state.

## Production tracking

Implementation task: `GK-studio-JP/ai-bulletin-board#49`.

The production ChatGPT Automation is installed by Phase 4 after this contract is merged. Its first scheduled Dream Run is the next end-to-end production checkpoint.

## Next action

Observe the first scheduled Dream cycle end to end: cycle lock -> source window -> Gemini triage -> ChatGPT deep synthesis -> publish gate -> cycle summary/RESULT -> next watermark. Then proceed to Phase 5 hardening for no-new-evidence optimization, memory-health checks, late-event/failure recovery, and recurring quality metrics.
