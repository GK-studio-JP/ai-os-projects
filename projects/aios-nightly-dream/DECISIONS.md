# AIOS Nightly Dream — Decisions

Status date: 2026-10-06

## D-001 — Project canonicality

Project identity, design, roadmap, and handoff are canonical in `GK-studio-JP/ai-os-projects`. Reusable cross-project operational knowledge remains canonical in `GK-studio-JP/ai-os-memory`.

## D-002 — Nightly execution

The scheduled Work/ChatGPT turn executes one complete AIOS cycle through connected structured tools. It reads #66 and the current main runbook/contract at each invocation. It does not write a local trigger file or delegate cycle orchestration to Remote Desktop/Browser Agent. No second timer or additional scheduled task is introduced.

## D-003 — Gemini salience triage

Use the existing unauthenticated Gemini Web path in `ai-os-runtime-browser-worker` for salience triage. It is treated as a no-Gemini-API-billing routing stage. Its score is not evidence and never directly authorizes a memory write.

## D-004 — Deep synthesis

Gemini is an independent semantic evaluator, invoked lazily after deterministic prefiltering and using one current page/session for triage and deep synthesis. Work/AIOS performs canonical collection, weighted routing, publish gates, mutation, and verification. Chat history and model memory are not canonical inputs.

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

The legacy `nightly_dream_runner.py` and old scheduled-runtime launcher are not the scheduled orchestration path. Shared evaluator adapters may be reused; the Work/AIOS turn owns leases, canonical state, and failure handling. An existing authenticated Browser Agent UI may perform only a required approved vector-rebuild dispatch when structured dispatch is unavailable, following the runbook's relay-first readiness check.

## D-011 — GBrain adaptations

Adopt Hot→Cold consolidation, cheap triage before deep synthesis, fingerprint caching, deferred processing, evidence provenance, write allow-lists, pattern evidence thresholds, no-new-evidence skips, dry-run support, cycle summaries, and cycle locking. Do not adopt psychological reflection or emotional weighting.

## D-012 — Scheduled recovery and evidence

Desktop Commander connectivity and Browser Agent relay readiness are independent. Test the Supabase relay and current command before declaring the browser unavailable. Persist raw triage dimensions and fingerprints using canonical 0.30/0.25/0.15/0.15/0.15 weights. Fresh query embeddings and explicit completed-cycle + RESULT records are required; stored document vectors and PROGRESS summaries are insufficient.
