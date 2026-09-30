# Roadmap

## Phase 0 — Bootstrap project registry

- Add backward-compatible multi-repository project registration.
- Add per-task target repository routing.
- Create canonical project state under `projects/aios-v1-hardening/`.

Exit: the project can resolve and render a task for any registered AIOS repository without breaking existing v1 projects.

## Phase 1 — Dedicated self-development process

- Add `PROC-AIOS` to Kernel.
- Register all AIOS service repositories required by the process.
- Define allowed mutation targets and branch/PR-only policy.

Exit: AIOS self-development tasks no longer depend on the bootstrap browser-worker process.

## Phase 2 — Orchestrator propagation

- Make `ai-os-api` carry the selected target repository and project process end to end.
- Verify context compile, scheduler plan, kernel validation, runtime preflight, CLAIM and invocation creation for a non-canonical target repository.

Exit: one live task can be started against a registered secondary AIOS repository.

## Phase 3 — Production E2E evidence

- Run one safe AIOS v1.0 hardening task through the production connector path.
- Finish the run and persist RESULT/PROGRESS evidence.
- Verify deterministic capsule, Global Memory attachment, invocation fingerprint refresh and runtime normalize/gate behavior.

Exit: reproducible production evidence exists for start → execute → finish.

## v1.0 acceptance

AIOS v1.0 hardening is complete when project routing, dedicated process routing, multi-repository task targeting and production start/finish evidence are all verified without direct-main mutation or secret exposure.
