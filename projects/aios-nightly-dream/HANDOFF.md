# AIOS Nightly Dream

Status: active
Project ID: `aios-nightly-dream`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Consolidate AIOS work experience across tasks at the end of each day and promote only verified, reusable operational knowledge into canonical Global or Project Memory.

## Current phase

Phase 0 — Bootstrap and authority.

## Current state

- ChatGPT Automation is the planned nightly clock and deep Dream executor. No new timer daemon is required.
- The existing unauthenticated Gemini Web path in `ai-os-runtime-browser-worker` is the salience-triage provider. It is used as a routing signal with no Gemini API billing.
- Gemini does not write canonical memory. ChatGPT performs deep synthesis and existing-memory reconciliation; deterministic gates enforce evidence, scope, and allowed write paths.
- `ai-bulletin-board` remains the canonical work-event journal. It is Dream input, not long-term memory.
- `ai-os-memory` remains the canonical Global Memory source; Supabase search data is a rebuildable projection.
- The project is registered under `PROC-AIOS`, but the current Kernel allowlist does not yet permit `PROC-AIOS` to target `GK-studio-JP/ai-os-memory` or `GK-studio-JP/ai-bulletin-board`.

## Next action

Extend `PROC-AIOS.routing.target_repositories` to include `GK-studio-JP/ai-os-memory` and `GK-studio-JP/ai-bulletin-board` without adding new capabilities. Then implement the Gemini salience-triage contract and Nightly Dream dry-run contract.
