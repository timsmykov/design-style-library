# Worker Prompt — Perplexity Answer Engine

Ты субагент Hermes. Отвечай итогом по-русски.

Durable coordinates:
- project_id: design-style-library
- board: design-style-library
- wave_id: no-login-wave-01
- card_id: t_ff773081
- component: perplexity-answer-engine
- owner_mode: implementation-worker

## Рабочее место

- Worktree/root: `/root/hermes-workspace/design-style-library-worktrees/perplexity-answer-engine`
- Branch: `style/perplexity-answer-engine-wave01`
- Target pack: `styles/perplexity-answer-engine/`
- Generated Gbrain slices: `gbrain_export/components/perplexity-answer-engine/`

## Source docs

Read in the worktree:
- `docs/no-login-style-factory.md`
- `extraction-plans/no-login-batch-01.yaml`
- `docs/style-pack-contract.md`
- `docs/extraction-pipeline.md`
- `docs/component-retrieval-architecture.md`
- use `styles/anthropic-claude/` as structural reference only; do not edit it.

## Goal

Build a draft no-login style pack for **Perplexity Answer Engine**. Mirror the Anthropic pipeline as much as feasible in one worker pass.

## Required work

1. Use Mobbin MCP if visible (`mcp_mobbin_search_screens`, `mcp_mobbin_search_sections`, `mcp_mobbin_search_flows`). If not visible, run/inspect the Mobbin smoke from `senior-ui-reference-research`; report a real blocker, do not fabricate evidence.
2. Save local screenshots/sections/flows under `styles/perplexity-answer-engine/evidence/mobbin/...`. Target 80+ local refs if feasible; truth beats quota.
3. Build `evidence/source-map/mobbin-source-map.jsonl` and `.csv` covering every local ref with local path, source type, Mobbin URL/image URL when available, OCR/palette/layout facts where available, component match, implementation status.
4. Build screenshot-derived component facts under `components/extracted/from-mobbin-screenshots/<component>/`.
5. Capture public no-login evidence for `https://www.perplexity.ai/` and `https://www.perplexity.ai/pro` if accessible: DOM/CSS/CDP/screenshots under `evidence/web/...` or `evidence/web/original-code/` consistently.
6. Create all required style pack files: `manifest.yaml`, `STYLE.md`, `agent-contract.md`, `evidence/sources.yaml`, `evidence/observations.yaml`, `dna/*`, `tokens/*`, `patterns/index.md`, `components/component-atlas.md`, `components/capsules/*.md`, `eval/*`.
7. Run `./tools/component_index.py .` if present.
8. Record `AUTH_BLOCKERS.md` for any login-only surfaces.
9. Run `./tools/stylepack_verify.py .` and JSON/JSONL sanity checks.
10. Commit changes on your branch. Do not merge to `main`.

## Constraints

Allowed paths:
- `styles/perplexity-answer-engine/`
- `gbrain_export/components/perplexity-answer-engine/`

Avoid global/shared edits. Forbidden:
- login/OAuth/credentials;
- modifying Anthropic or other packs;
- gateway lifecycle commands;
- printing secrets.

## Final self-report schema

Return:
- status: completed | partial | blocked | failed
- branch
- commit_sha
- files_changed
- counts: mobbin_refs, source_map_rows, components, public_pages, cdp_targets
- commands_run
- verification
- blockers
- parent_must_verify
