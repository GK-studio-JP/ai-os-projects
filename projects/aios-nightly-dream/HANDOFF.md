# AIOS Nightly Dream

Status: active
Project ID: `aios-nightly-dream`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Consolidate AIOS work experience across tasks after a daily settling period and promote only verified, reusable operational knowledge into canonical Global or Project Memory.

## Current phase

Phase 5 — Hardening.

## Completed foundation

- Phase 0: project registration and `PROC-AIOS` repository authority are complete. `ai-os-memory` and `ai-bulletin-board` are explicit targets without adding Kernel capabilities.
- Phase 1: existing unauthenticated Gemini Web is the salience-triage provider. AIOS recomputes salience/routing deterministically; Gemini has no canonical write authority.
- Phase 2: `ai-os-context` provides deterministic nightly source bundles and non-authoritative Dream report validation.
- Phase 3: `ai-os-memory` provides the Memory publish gate, branch/PR-only writes, automatic main-push exact/FTS refresh without embeddings, and explicit workflow-dispatch vector rebuild.
- Phase 4: the first production Dream Run `GK-studio-JP/ai-bulletin-board#53` completed with canonical cycle state and RESULT. Authenticated offline source reconstruction was repaired by #54, and production Gemini current-page/fill/completion hardening was completed by #57, #59, and #60. The original scheduled-GPT mutation design was then found to repeat the known scheduled GitHub-write failure and is being replaced by the dedicated Gemini runner path.

## Production execution

- ChatGPT Automation is the nightly clock/launcher only; no timer daemon is introduced.
- Dedicated execution entrypoint: `GK-studio-JP/ai-os-runtime-browser-worker/nightly_dream_runner.py`; the generic Browser Worker route remains separate.
- Dream coordination writes are performed by the dedicated runner through Browser Agent. Gemini performs salience triage and deep synthesis.
- Canonical execution contract: `projects/aios-nightly-dream/AUTOMATION_RUNBOOK.md`.
- Timezone: `Asia/Tokyo`.
- Nominal schedule: nightly at 02:00 with flexible scheduling.
- Settling delay: 3600 seconds.
- Bootstrap watermark: `2026-10-02T00:00:00+09:00`.
- Permanent production serialization uses `GK-studio-JP/ai-bulletin-board#52`. Each Dream Run Issue is canonical cycle state; an identical/incomplete cycle is resumed rather than duplicated.
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

Phase 4 implementation task: `GK-studio-JP/ai-bulletin-board#49` — completed.

Production checkpoints:

- First production cycle: `GK-studio-JP/ai-bulletin-board#53` — completed with canonical cycle state and RESULT.
- Authenticated source reconstruction: `#54` — completed.
- Gemini current-page routing: `#57` — completed.
- Browser Agent prompt-fill fallback: `#59` — completed.
- Stable Gemini JSON completion detection: `#60` — completed.
- Permanent production control: `GK-studio-JP/ai-bulletin-board#52` — intentionally open and reusable.
- ChatGPT Automation: 02:00 production schedule is currently disabled pending a successful scheduled one-shot E2E of the dedicated Gemini runner path.

## Next action

Finish Phase 4 revalidation first: update the private Scheduled Runtime launcher, run a real scheduled one-shot E2E through the dedicated Gemini runner, verify canonical CLAIM → Dream Run → cycle state/RESULT → RELEASE, and only then restore the daily 02:00 schedule. Resume Phase 5 hardening after that acceptance passes.
