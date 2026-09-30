# AIOS v1.0 Hardening

Status: active
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Use AIOS itself to drive the final hardening work required for v1.0 while preserving canonical boundaries and leaving reproducible production evidence.

## Current phase

Bootstrap / dogfooding.

## Current state

- Project registry v2 adds backward-compatible multi-repository project registration.
- Per-task target repository routing is supported.
- Project context refs remain canonical-repository `path:` references.
- The bootstrap executor is `PROC-RUNTIME-BROWSER-WORKER` until a dedicated `PROC-AIOS` is established.

## Next action

Create the first AIOS task targeting `GK-studio-JP/ai-os-kernel` to establish dedicated AIOS self-development routing and register missing AIOS service repositories.
