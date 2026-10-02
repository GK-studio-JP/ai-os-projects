# AIOS Nightly Dream — Decisions

Status date: 2026-10-02

## D-001 — Project canonicality

Project identity, design, roadmap, and handoff are canonical in `GK-studio-JP/ai-os-projects`. Reusable cross-project operational knowledge remains canonical in `GK-studio-JP/ai-os-memory`.

## D-002 — Nightly execution

Use ChatGPT Automation only as the nightly clock/launcher. It may perform authenticated read-only snapshot acquisition and start/verify the dedicated Nightly Dream runner, but it does not own Dream mutations or synthesis. Do not introduce a new timer daemon solely for Dream scheduling.

## D-003 — Gemini salience triage

Use the existing unauthenticated Gemini Web path in `ai-os-runtime-browser-worker` for salience triage. It is treated as a no-Gemini-API-billing routing stage. Its score is not evidence and never directly authorizes a memory write.

## D-004 — Deep synthesis

Gemini performs cross-task reconstruction, evidence reconciliation, existing-memory comparison, consolidation, and pattern synthesis through the dedicated Nightly Dream runner. Chat history and model memory are not canonical inputs.

## D-005 — Storage boundaries

`ai-bulletin-board` remains the append-only work-event journal. Global reusable knowledge goes to `ai-os-memory`. Project-specific knowledge stays in the relevant project repository. Event-only facts remain only in the journal.

## D-006 — Publish safety

All Dream-generated canonical changes use branch + PR. LLM output is a proposal; deterministic validation controls scope, evidence sufficiency, secret rejection, write allow-lists, and publish eligibility.

## D-007 — Delayed consolidation

Do not promote durable operational memory immediately after an individual task. Consolidation occurs after the daily settling window so corrections, later results, and cross-task evidence can be evaluated together.

## D-008 — Deferred knowledge

Uncertain, conflicting, incomplete, or insufficiently evidenced candidates are deferred rather than forced into Memory. Deferred evidence may mature across later Dream cycles.

## D-009 — Idempotency

Use source-history fingerprints and contract/triage versions to skip unchanged work. Advance the Dream watermark only after a successful cycle.

## D-010 — Separate execution path

Nightly Dream uses a dedicated `nightly_dream_runner.py` entrypoint. The generic Browser Worker launch path remains separate and is not repurposed as the nightly scheduler path. Shared low-level Browser Agent/Gemini adapters may be reused, but routing, leases, cycle state, and failure handling remain Dream-specific.

## D-011 — GBrain adaptations

Adopt Hot→Cold consolidation, cheap triage before deep synthesis, fingerprint caching, deferred processing, evidence provenance, write allow-lists, pattern evidence thresholds, no-new-evidence skips, dry-run support, cycle summaries, and cycle locking. Do not adopt psychological reflection or emotional weighting.
