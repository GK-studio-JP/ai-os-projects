# AIOS v1.0 Hardening

Status: completed
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Use AIOS itself to drive the final hardening work required for v1.0 while preserving canonical boundaries and leaving reproducible production evidence.

## Current phase

Phase 3 — Production E2E evidence / continuous dogfooding — completed.

## Current state

- Project registry v2, per-task `target_repository` routing, canonical-repository `path:` context refs, and dedicated `PROC-AIOS` routing are operational.
- AIOS hardening tasks #32 through #44 are completed. Tasks #41 and #42 have final RESULT evidence and are closed.
- Global Memory search uses the canonical eight-argument RPC `public.aios_memory_search(text,text,integer,text[],text[],text[],text[],extensions.vector)`. The live Supabase signature and `ai-os-memory/db/001_memory_search.sql` agree; the earlier nine-argument failure was a caller assembly error, not a database signature migration.
- `ai-os-memory` PR #6 documents the eight-argument search contract on main, and the AIOS normal-chat plugin is updated to v0.2.4 with typed eight-argument retrieval and live-signature diagnostics.
- Browser Agent PR #308 is merged as `67bb3aca2260f1b015e01b60757ce1c190be4ce5`. A successful `goto()` navigation is preserved when only the immediate Light observation times out, returning an explicit deferred Light observation instead of discarding the navigated page.
- Final production GitHub evidence used `ai-os-projects` PR #7 as the explicit superseding artifact for obsolete PR #5. The production Browser Agent opened PR #7, preserved the page through a transient `Loading merge status` observation, then re-observed `Ready to merge` with all checks passed and no fatal recovery.
- PR #7 was merged through the production GitHub UI as `f763244074d506374bbe9aef83e1fe06adf8370d`. PR #5 remains closed without merge; no history was rewritten to claim otherwise.
- The merged PR #7 branch and the remaining merged/stale branches in `ai-os-projects`, `browser-agent`, and `ai-os-memory` were deleted after confirming they were zero commits ahead of main. Those repositories now retain only `main`.
- The stale historical Browser Agent relay command left in `running` state since 2026-09-29 was closed during cleanup. The production Browser Agent service remains active on the current main.

## Next action

No remaining `aios-v1-hardening` task. Keep this HANDOFF as closure evidence. Future AIOS work should start a new task or project and retain the branch + PR mutation policy.
