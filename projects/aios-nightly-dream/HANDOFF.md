# AIOS Nightly Dream

Status: active
Status date: 2026-10-03
Project ID: `aios-nightly-dream`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Consolidate AIOS work experience across tasks after a daily settling period and promote only verified, reusable operational knowledge into canonical Global or Project Memory.

## Current phase

Phase 4 revalidation + Phase 5 hardening.

A personal Work scheduled task has been created successfully. The remaining acceptance work is to prove the evaluator and full Dream cycle under the Work/Direct-AIOS execution model.

## Completed foundation

- Phase 0: project registration and repository authority are complete.
- Phase 1: unauthenticated Gemini Web salience triage exists; AIOS recomputes salience/routing deterministically and Gemini has no canonical write authority.
- Phase 2: `ai-os-context` provides deterministic source bundles and non-authoritative Dream report validation.
- Phase 3: `ai-os-memory` provides the deterministic publish gate, branch/PR-only writes, exact/FTS refresh, explicit vector rebuild, and retrieval verification path.
- First production Dream Run `ai-bulletin-board#53` completed safely.
- Authenticated source reconstruction (#54), Gemini current-page routing (#57), prompt-fill fallback (#59), and stable JSON completion (#60) were production-verified.
- Manual Gemini operator E2E succeeded after Browser Agent stabilization.
- Direct-AIOS runbook migration PR #17 removed the unreliable scheduled RDP/launcher/browser chain from the mandatory execution path.

## Current architecture

- Work Scheduled Task is the recurring entrypoint.
- AIOS uses structured GitHub/Supabase integrations for source collection, coordination, canonical writes, and RAG verification.
- Gemini remains the independent semantic evaluator for salience triage and deep synthesis.
- Deterministic prefiltering runs before any browser start.
- Browser/Gemini starts only when at least one completed, verified candidate requires semantic evaluation.
- One Gemini current-page session is reused for all triage calls and deep synthesis in that cycle.
- Gemini failure defers affected candidates; GPT does not replace Gemini's salience role.
- Browser Agent is fallback evaluator transport only. It is no longer the production orchestration/mutation transport.

## Canonical boundaries

- Work experience: `GK-studio-JP/ai-bulletin-board`.
- Global long-term Memory: `GK-studio-JP/ai-os-memory`.
- Project-specific Memory: the relevant project repository.
- Search/vector data: rebuildable projection only.
- Chat/model memory is never authoritative Dream state.

## Existing evaluator implementation

- `GK-studio-JP/ai-os-runtime-browser-worker/ai_os_browser_worker/dream_triage.py`
- `GK-studio-JP/ai-os-runtime-browser-worker/dream_triage_runner.py`
- `GK-studio-JP/ai-os-runtime-browser-worker/test_dream_triage.py`

The evaluator code already validates source fingerprints/version, recomputes the five-dimension weighted score, and fails closed. Existing current-page reuse is production-verified.

The legacy `nightly_dream_runner.py` still starts Browser Agent before prefiltering and performs canonical GitHub operations through the browser. It is not the desired Work/Direct-AIOS production architecture and must not be treated as the new orchestrator.

## Next acceptance steps

1. Verify one fixed eligible triage capsule through the browser available to a scheduled Work run and unauthenticated Gemini Web.
2. Require a schema-valid `aios-dream-triage-result:v1` and confirm AIOS recomputation yields the expected routing.
3. Verify a zero-eligible dry run performs no Gemini/browser startup.
4. Verify one eligible multi-candidate dry run uses one Gemini session/current page, not one browser start per candidate.
5. Run a no-publish Dream dry run through collection -> prefilter -> Gemini -> report normalization.
6. Only after those pass, run the publish/index/retrieval portion and restore the production cadence.

Do not revive the old Scheduled Chat -> RDP/script -> Browser Agent launcher path.
