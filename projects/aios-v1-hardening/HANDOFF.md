# AIOS v1.0 Hardening

Status: active
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Use AIOS itself to drive the final hardening work required for v1.0 while preserving canonical boundaries and leaving reproducible production evidence.

## Current phase

Phase 2 — Orchestrator propagation / dogfooding.

## Current state

- Project registry v2 provides backward-compatible multi-repository project registration.
- Per-task `target_repository` routing is supported.
- Project context refs remain canonical-repository `path:` references.
- `PROC-AIOS` is registered in Kernel with `explicit-repository-allowlist` routing across the eight AIOS hardening repositories.
- `PROC-AIOS` mutation authority is limited to branch/PR repository mutation.
- `ai-os-projects` PR #1 and `ai-os-kernel` PR #7 are merged.

## Next action

Create the first post-bootstrap AIOS task targeting `GK-studio-JP/ai-os-api` to carry the selected target repository and project process end to end through the production orchestration path.
