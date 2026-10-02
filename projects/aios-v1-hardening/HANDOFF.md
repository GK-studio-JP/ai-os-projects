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
- AIOS hardening tasks #32 through #40, #43, and #44 are completed. Tasks #41 and #42 remain open for the final production GitHub-flow evidence.
- Global Memory search uses the canonical eight-argument RPC `public.aios_memory_search(text,text,integer,text[],text[],text[],text[],extensions.vector)`. The live Supabase signature and `ai-os-memory/db/001_memory_search.sql` agree; the earlier nine-argument failure was a caller assembly error, not a database signature migration.
- `ai-os-memory` PR #6 documents the eight-argument search contract and the `pg_proc` signature check on main. The AIOS normal-chat plugin is updated to v0.2.4 with typed eight-argument retrieval and the same failure diagnostic.
- Browser Agent PR #308 is merged as `67bb3aca2260f1b015e01b60757ce1c190be4ce5`. A successful `goto()` navigation is now preserved when only the immediate Light observation times out; the command returns an explicit deferred Light observation with `retrySuggested:true` instead of discarding the navigated page.
- Browser Agent regression suites and all three PR #308 CI workflows passed. The production VM repository is synchronized to `main@67bb3aca`, the `browser-agent` systemd service restarted on that main, and a live production `goto` to `ai-os-projects` PR #6 completed with a normal Light observation and no fatal recovery.
- Task #42 remains open only for final production GitHub-flow evidence using the fixed Browser Agent.
- Task #41 remains open because its original target, `ai-os-projects` PR #5, was closed without merge and cannot satisfy the acceptance literally. A fresh HANDOFF PR must be merged through the production Browser Agent and recorded explicitly as superseding evidence; do not claim PR #5 merged.

## Next action

1. Open a fresh HANDOFF PR from the current canonical state.
2. Use the production Browser Agent relay to observe and merge that PR through GitHub UI, then verify the resulting HANDOFF on `main`.
3. Record the fresh PR as superseding production evidence for #42 and #41, close those tasks if the live flow succeeds, and clean up merged or accidental branches.
