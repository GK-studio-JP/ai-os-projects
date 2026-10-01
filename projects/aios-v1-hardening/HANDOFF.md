# AIOS v1.0 Hardening

Status: active
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Use AIOS itself to drive the final hardening work required for v1.0 while preserving canonical boundaries and leaving reproducible production evidence.

## Current phase

Phase 3 — Production E2E evidence / continuous dogfooding.

## Current state

- Project registry v2, per-task `target_repository` routing, canonical-repository `path:` context refs, and dedicated `PROC-AIOS` routing are operational.
- AIOS hardening tasks #32 through #40 are completed; #44 is also completed.
- Production Browser Agent main is verified at `86165f7b21b1cc47c5f6751d4e093d40baffb2ff`; the production VM repository matches main and the `browser-agent` service is active.
- Browser Agent hardening through PR #307 includes Deep continuation/actionability, cold-start budgeting, page-first observation recovery, bounded full recovery, bounded Deep detail work, recovery launch-budget separation, and stale Chromium singleton cleanup.
- Task #43 remains open. Current `browser-agent` main still implements `goto()` as navigation followed by an immediate Light observation; when navigation succeeds but that post-navigation Light observation times out, `goto()` does not yet return the deferred Light result already used by `start()`.
- Task #42 remains open pending final production GitHub-flow verification after the remaining `goto()` observation behavior is fixed.
- Task #41 remains open, but its original target `ai-os-projects` PR #5 is closed without merge and its branch has been removed. The old PR can no longer satisfy the task literally; a fresh HANDOFF PR is required and must be treated as superseding evidence rather than silently assuming PR #5 merged.
- The previous HANDOFF next action to create the first post-bootstrap `ai-os-api` task is obsolete; that orchestration propagation work has already been exercised by the completed hardening tasks.

## Next action

1. Finish #43 by preserving a successful `goto()` navigation when only the post-navigation Light observation times out, returning an explicit deferred Light observation and adding regression coverage.
2. Retry the production GitHub flow and complete #42 once navigation/observation no longer discards a successfully navigated page.
3. Use a fresh HANDOFF PR as the replacement production artifact for #41, record the supersession explicitly in the Bulletin Board, verify the merged HANDOFF on `main`, and only then decide whether #41 can be closed or requires a replacement task because PR #5 is no longer mergeable.
