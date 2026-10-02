# AIOS Nightly Dream Contract v1

Status: active production contract
Status date: 2026-10-02

## Purpose

Turn verified AIOS work experience into durable operational knowledge after a daily settling period. Dream is a delayed cross-task consolidation process, not an immediate post-task memory write.

## Execution roles

- **Nightly trigger / deep worker:** ChatGPT Automation.
- **Salience triage:** existing unauthenticated Gemini Web path in `ai-os-runtime-browser-worker`.
- **Canonical journal:** `GK-studio-JP/ai-bulletin-board`.
- **Global canonical memory:** `GK-studio-JP/ai-os-memory`.
- **Project canonical memory:** each project's own canonical repository.
- **Deterministic authority:** AIOS Kernel/runtime policy, repository permissions, evidence checks, and write allow-lists.

Gemini and ChatGPT produce analysis/proposals. They do not gain authority from model output.

## Dream window

The nightly schedule is configurable by timezone and trigger time. A configurable settling delay excludes work that is too recent to judge safely.

```text
window_start = previous successful Dream window_end
window_end   = trigger_time - settle_delay
source range = (window_start, window_end]
```

The watermark advances only after the full cycle succeeds. Failed cycles retry from the last successful watermark.

## Source discovery

Dream reads canonical GitHub task state, not Chat history.

For each task changed in the window:

1. fetch the Issue body and all canonical protocol comments;
2. replay `GITHUB_PROTOCOL.md`;
3. compute a stable source-history fingerprint;
4. identify final state, corrections, RESULT, immutable artifacts, and verification evidence;
5. treat `history_unsafe` as unusable evidence;
6. defer active/incomplete histories when final interpretation is not yet stable.

## Triage Capsule

Gemini receives a bounded canonical summary rather than an arbitrary full conversation.

```json
{
  "schema": "aios-dream-triage-capsule:v1",
  "task": "#123",
  "source_fingerprint": "sha256:...",
  "final_state": "completed|open|claimed|history_unsafe",
  "objective": "...",
  "result_summary": "...",
  "corrections": [],
  "artifacts": [],
  "verification": []
}
```

Secrets, credentials, cookies, authentication headers, and transient browser contents are excluded.

## Gemini salience result

```json
{
  "schema": "aios-dream-triage-result:v1",
  "source_fingerprint": "sha256:...",
  "triage_version": 1,
  "salience": 0.0,
  "dimensions": {
    "operational_impact": 0.0,
    "reuse_scope": 0.0,
    "novelty": 0.0,
    "recurrence": 0.0,
    "evidence_strength": 0.0
  },
  "decision": "skip|defer|deep",
  "reasons": []
}
```

The salience result is a routing signal only. It is not evidence and cannot authorize a canonical write.

Default configurable routing:

- `salience < 0.35`: skip/noop
- `0.35 <= salience < 0.65`: defer
- `salience >= 0.65`: deep analysis

High-authority primary evidence may force deep analysis regardless of score.

## Fingerprint and cache

A triage verdict may be reused only when all of these are unchanged:

- source-history fingerprint;
- triage contract/version;
- relevant routing policy version.

A changed task history must be re-triaged. Pattern analysis skips when there is no new evidence.

## Deep Dream

ChatGPT receives only deep-routed and carried-deferred candidates plus the relevant existing canonical Memory.

Deep Dream performs:

1. timeline/final-state reconstruction;
2. evidence validation and source attribution;
3. cross-task comparison;
4. existing-memory lookup;
5. duplicate/update/contradiction detection;
6. consolidation;
7. cross-task pattern detection;
8. Global/Project/event-only scope classification;
9. structured proposal generation.

## Memory proposal

```json
{
  "schema": "aios-memory-proposal:v1",
  "candidate_id": "sha256:...",
  "scope": "global|project|event-only",
  "kind": "fact|workflow|troubleshooting|architecture|pattern|relation",
  "claim": "...",
  "evidence": [],
  "existing_memory_refs": [],
  "decision": "promote|noop|defer|reject|supersede",
  "defer_reason": null,
  "target": null
}
```

Deferred reasons include `budget`, `incomplete`, `conflict`, `insufficient_evidence`, and `requires_review`.

## Pattern rule

Recurring operational patterns normally require a configurable minimum evidence count; default is 3 independent qualifying experiences. A single authoritative primary-source fact does not need to satisfy the recurring-pattern threshold.

## Publish gate

Before any canonical mutation, deterministic validation must confirm:

- target scope is correct;
- evidence references resolve;
- no secret or sensitive transient value is included;
- unresolved contradictions are not promoted;
- evidence quality satisfies the candidate kind;
- target repository/path is explicitly allowed;
- the mutation uses branch + PR;
- model output does not modify its own authority or write policy.

Dream must not use a successful UI action, model assertion, or salience score as proof.

## Write boundaries

Global Dream publishing is limited to approved knowledge/index/registry paths in `ai-os-memory`. Project publishing is limited to project-approved knowledge/documentation paths.

Runtime code, deployment configuration, database authority, security policy, and workflow authority are not self-modified by Nightly Dream unless a separate explicitly routed implementation task authorizes that change.

## Reindex and verification

After an accepted Global Memory merge:

1. rebuild/refresh the search projection;
2. verify an exact lookup;
3. verify a semantic/paraphrased lookup when vector search is available;
4. record the canonical commit and verification result in the Dream cycle result.

Supabase remains a rebuildable projection; GitHub remains canonical.

## Cycle state and locking

Only one Dream generation may publish for a source window at a time. The implementation must use a canonical/auditable run identity and idempotency keys so retries do not duplicate writes.

## Cycle summary

Each completed Dream records at least:

```json
{
  "tasks_scanned": 0,
  "cache_hits": 0,
  "triaged": 0,
  "deep_analyzed": 0,
  "promoted": 0,
  "updated": 0,
  "superseded": 0,
  "deferred": 0,
  "rejected": 0,
  "patterns_created": 0,
  "memory_prs": []
}
```

## Privacy and exclusions

Nightly Dream does not infer or persist psychological traits, emotional weighting, private credentials, cookies, browser profiles, or unrelated personal information. The system learns operational knowledge, not a psychological model of the user.

## Success invariant

```text
daytime experience
  -> canonical work journal
  -> Gemini salience triage
  -> ChatGPT cross-task Dream
  -> deterministic publish gate
  -> canonical Global/Project Memory
  -> reindex and verification
  -> next-day retrieval
```
