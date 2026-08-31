# No-login Batch 01 — Wave 01

Status: launched as bounded two-worker canary wave.

## Why only two first

The target batch is 10 style packs, but first wave is intentionally two agents:

1. prove the no-login factory works outside Anthropic;
2. avoid concurrent edits to shared repo files;
3. verify Mobbin/CDP/source-map throughput before scaling to 4+ workers;
4. keep parent verification tractable.

## Workers

| Card | Style | Worktree | Branch | Scope |
|---|---|---|---|---|
| `t_ff773081` | `perplexity-answer-engine` | `/root/hermes-workspace/design-style-library-worktrees/perplexity-answer-engine` | `style/perplexity-answer-engine-wave01` | Full no-login draft pack |
| `t_a6b2ffb9` | `notion-document-os` | `/root/hermes-workspace/design-style-library-worktrees/notion-document-os` | `style/notion-document-os-wave01` | Full no-login draft pack |

## Worker contract

Each worker owns only:

- `styles/<style_id>/`
- `gbrain_export/components/<style_id>/`
- optional local notes under its worktree only

Forbidden without parent merge:

- editing another style pack;
- modifying Anthropic pack;
- changing global schemas/tools unless the worker only comments a proposed patch;
- printing secrets or submitting credentials;
- login/OAuth flows.

## Acceptance for worker self-report

Return:

- status: completed | partial | blocked | failed
- files changed
- exact local evidence counts
- Mobbin query count / source lanes
- public URLs captured
- component capsule count
- commands run
- verifier result
- blockers/auth gaps
- branch/commit SHA if committed

Parent must verify before merging to `main`.
