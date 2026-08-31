# Worker Prompt — Stripe Trust Commerce

Ты субагент Hermes. Итоговый self-report дай по-русски.

Durable coordinates:
- project_id: design-style-library
- board: design-style-library
- wave_id: no-login-wave-02
- card_id: t_339d2d7a
- component: stripe-trust-commerce
- owner_mode: implementation-worker

## Рабочее место

- Worktree/root: `/root/hermes-workspace/design-style-library-worktrees/stripe-trust-commerce`
- Branch: `style/stripe-trust-commerce-no-login-wave-02`
- Target pack: `styles/stripe-trust-commerce/`
- Generated Gbrain slices: `gbrain_export/components/stripe-trust-commerce/`

## Source docs

Read in the worktree:
- `docs/no-login-style-factory.md`
- `extraction-plans/no-login-batch-01.yaml`
- `docs/style-pack-contract.md`
- `docs/extraction-pipeline.md`
- `docs/component-retrieval-architecture.md`
- use `styles/anthropic-claude/`, `styles/perplexity-answer-engine/`, and `styles/notion-document-os/` as structural references only; do not edit them.

## Goal

Build a draft/reference no-login style pack for **Stripe Trust Commerce**. Target the same standard as the current Perplexity/Notion packs: evidence-backed, componentized, offline-usable draft pack.

## Inputs

Category: `payments_trust`

Public URLs:
- https://stripe.com/
- https://stripe.com/pricing

Mobbin queries:
- screens: Stripe dashboard payments checkout invoices balances pricing settings web app
- sections: Stripe website pricing payments checkout cards trust compliance enterprise docs
- flows: Stripe onboarding business verification checkout payment subscription invoice payout settings

## Required work

1. Use Mobbin MCP if visible (`mcp_mobbin_search_screens`, `mcp_mobbin_search_sections`, `mcp_mobbin_search_flows`). If it is not visible, run/inspect the Mobbin smoke from `senior-ui-reference-research`; report a real blocker, do not fabricate evidence.
2. Save local screenshots/sections/flows under `styles/stripe-trust-commerce/evidence/mobbin/...`. Target 80+ local refs if feasible; truth and relevance beat quota.
3. Build `evidence/source-map/mobbin-source-map.jsonl` and `.csv` covering every local ref with local path, source type, Mobbin URL/image URL when available, OCR/palette/layout facts where available, component match, implementation status.
4. Build screenshot-derived component facts under `components/extracted/from-mobbin-screenshots/<component>/`.
5. Capture public no-login web evidence for the URLs above using available Firecrawl/browser/CDP/tools. Save DOM/CSS/computed/screenshots under `evidence/web/...` or `evidence/web/original-code/` consistently. Keep production CSS as evidence only, not runtime dependency.
6. Create all required pack files: `manifest.yaml`, `STYLE.md`, `agent-contract.md`, `evidence/sources.yaml`, `evidence/observations.yaml`, `dna/*`, `tokens/*`, `patterns/index.md`, `components/component-atlas.md`, `components/capsules/*.md`, `eval/*`.
7. Run `./tools/component_index.py .` if present and ensure `gbrain_export/components/stripe-trust-commerce/` exists.
8. Record `AUTH_BLOCKERS.md` for any login-only/app-only surfaces.
9. Ensure required evidence placeholder dirs exist even if empty: `evidence/web/pages`, `evidence/web/css`, `evidence/web/computed`, `evidence/web/fonts`.
10. Run `./tools/stylepack_verify.py .` and JSON/JSONL sanity checks.
11. Commit changes on your branch. Do not merge to `main`.

## Constraints

Allowed paths:
- `styles/stripe-trust-commerce/`
- `gbrain_export/components/stripe-trust-commerce/`

Avoid global/shared edits. Forbidden:
- login/OAuth/credentials;
- modifying Anthropic/Perplexity/Notion/other packs;
- gateway lifecycle commands;
- printing secrets;
- changing schemas/tools unless you only write a proposed patch note.

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
