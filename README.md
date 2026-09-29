# ai-os-projects

Project registry and external-project integration layer for the GitHub-native AI OS.

## Purpose

This repository connects external project repositories to the existing AI OS control plane.

It owns only:
- project identity
- references to canonical project state
- project-to-task linkage
- deterministic project + objective -> ai-os-task:v1 metadata

It does not own task coordination, scheduling, authority, execution, browser execution, or the external project's domain state.

## Boundary

Canonical responsibilities remain:
- ai-bulletin-board: task coordination journal
- ai-os-context: replay and Context Capsules
- ai-os-scheduler: scheduling
- ai-os-kernel: authority/capability checks
- ai-os-runtime: execution
- browser-agent: browser execution
- external project repository: project/domain source of truth

## Flow

External project repository
-> ai-os-projects
-> ai-bulletin-board
-> ai-os-context
-> ai-os-scheduler
-> ai-os-kernel
-> ai-os-runtime

## v0.1 scope

- register / get / find / list projects
- convert project + objective into ai-os-task:v1 metadata
- record project <-> bulletin-board Issue linkage

Out of scope: chat UI, RAG/vector DB, scheduling, authority, execution, and copying external project state.

## First integration target

GK-studio-JP/music-transcription-kb / projects/apocalyptic-march/
