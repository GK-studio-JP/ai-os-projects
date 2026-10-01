# AIOS v1.0 Hardening

Status: active
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`

## Objective

Use AIOS itself to drive the final hardening work required for v1.0 while preserving canonical boundaries and leaving reproducible production evidence.

## Host invariant

Normal ChatGPT is the canonical user-facing host for AIOS.

- AIOS must be usable directly from ordinary ChatGPT conversations through the AIOS plugin and connected apps.
- ChatGPT Work, Codex, the desktop app, and local CLIs may be optional implementation, debugging, or acceleration surfaces only.
- No AIOS capability is considered complete if its only supported path is Work/Codex-only.
- New orchestration or mutation capabilities must expose a normal-ChatGPT-callable plugin, MCP, or connected-app path.
- Do not solve missing normal-chat connectivity by extracting service tokens, browser cookies, or other secrets into chat or temporary operator files.

## Current phase

Phase 2.5 — normal-chat orchestration bridge, prerequisite to Phase 3 production connector E2E.

## Current state

- Project registry v2 provides backward-compatible multi-repository project registration.
- Per-task `target_repository` routing is supported.
- Project context refs remain canonical-repository `path:` references.
- `PROC-AIOS` is registered in Kernel with `explicit-repository-allowlist` routing across the eight AIOS hardening repositories.
- `PROC-AIOS` mutation authority is limited to branch/PR repository mutation.
- `ai-os-projects` PR #1 and `ai-os-kernel` PR #7 are merged.
- Phase 2 canonical dogfooding E2E is closed through tasks #32 and #33.
- Runtime reclaim CLAIM idempotency is lease-cycle aware and merged in `ai-os-runtime` PR #6.
- Task #32 was revalidated with the fixed Runtime through CLAIM/reclaim -> READY -> normalize -> gate -> RESULT -> canonical `completed`.
- AIOS private plugin v0.2.1 explicitly enforces the normal-ChatGPT host invariant.
- AIOS v0.2.x still lacks a dedicated authenticated normal-chat action that calls production `/api/runs` and `/api/runs/finish`; this is the blocker before Phase 3 can be considered a valid connector E2E.

## Next action

Implement the normal-ChatGPT orchestration bridge as a ChatGPT-callable plugin/MCP/connected-app action over the production AIOS orchestration service. The bridge must preserve authenticated execution without exposing or copying service secrets into chat, Work, Codex, local temporary token files, or Browser Agent state.

After that bridge is connected to @AIOS, run the Phase 3 production connector E2E through the normal ChatGPT conversation path: start -> execute -> finish -> canonical RESULT/completed, including Global Memory attachment and invocation fingerprint refresh evidence.
