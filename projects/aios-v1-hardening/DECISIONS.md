# Decisions

## D-001 Canonical project repository

Use `GK-studio-JP/ai-os-projects` as the canonical project repository for AIOS v1.0 Hardening. Do not put project-specific state in Global Memory or the Bulletin Board.

## D-002 Multi-repository model

A project has one canonical repository plus an explicit repository allowlist. Each task selects one target repository. Cross-repository context refs are rejected in v0.2; context refs stay canonical `path:` references.

## D-003 Bootstrap process

Use `PROC-RUNTIME-BROWSER-WORKER` only as the bootstrap executor because it already has branch/PR mutation capability and registered-process target routing. Replace it with dedicated `PROC-AIOS` routing as the first project task.

## D-004 Mutation policy

Repository mutation remains branch + PR only. No direct main commits.
