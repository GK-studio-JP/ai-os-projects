# AIOS v1.0 Hardening

Status: active
Project ID: `aios-v1-hardening`
Canonical repository: `GK-studio-JP/ai-os-projects`
Operational state: continuous dogfooding / validation; not declared ready for operation.

## Objective

Use AIOS itself to drive and continuously test the hardening work required for v1.0 while preserving canonical boundaries, purpose recovery, and reproducible evidence.

## Current phase

Phase 2 — continuous orchestrator dogfooding and recovery validation.

## Current state

- Project registry v2 provides multi-repository registration for eight AIOS repositories.
- Per-task `target_repository` routing is active; project context refs remain canonical-repository `path:` references.
- `PROC-AIOS` is registered in Kernel with `explicit-repository-allowlist` routing across the eight registered repositories.
- `PROC-AIOS` mutation authority remains limited to branch/PR repository mutation.
- #32 completed target-repository propagation and end-to-end orchestration validation against `GK-studio-JP/ai-os-api`.
- #33 fixed Runtime lease-cycle-aware CLAIM reclaim; `ai-os-runtime` PR #6 is merged.
- #34 completed sustained operation against `GK-studio-JP/ai-os-context` without repository mutation.
- #35 hardened Browser Agent timeout recovery; `browser-agent` PR #281 is merged at `8102896dca8dfc496fa225415f0a164831af93ab`. Live verification confirmed heartbeat continuity, explicit failure of queued work on fatal browser recovery, no service restart, and explicit browser restart back to ready.
- #36 completed a second independent project-operation cycle against `GK-studio-JP/ai-os-scheduler`; completed prior tasks were excluded from runnable scheduling.
- #38/#37 verified Scheduler priority ordering and recovery: higher-priority #38 ran first, then a fresh projection dispatched lower-priority #37 after #38 completed.
- #39 verified ownership contention and recovery: another worker's live CLAIM forced `WAIT`; owner RELEASE made the old boot `STALE_CONTEXT`; rebuilding projection/plan/boot produced a fresh CLAIM, READY, gated RESULT, and final completed replay.
- #34–#39 use canonical CLAIM/RESULT lifecycle where applicable. A missing CLAIM discovered during #35 was reconciled and retested before later runs.
- At this handoff update there are no open `aios-v1-hardening` bulletin-board tasks.

## Recovery rule

A child defect or test task does not replace the parent project objective. When a child task completes, refresh canonical project/task state and return to the active project validation objective. ROADMAP backlog items do not override the current canonical objective or next action.

## Next action

Continue bounded operational dogfooding. Next, test task blocking/spec-change recovery: verify a task with non-empty `blocked_by` is withheld by Scheduler, then after an explicit task-spec update clearing the blocker, stale projections fail closed and a fresh projection can dispatch and complete the task.
