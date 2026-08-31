# Anthropic / Claude Visual Corpus

Status: expanded corpus pass, 2026-06-30.

## Counts

| Corpus lane | Count | Path |
|---|---:|---|
| Web/app screens | 65 | `evidence/mobbin/screens/` |
| Website sections | 34 | `evidence/mobbin/sections/` |
| Flow screens | 112 | `evidence/mobbin/flows/` |
| **Total local WebP refs** | **211** | `evidence/mobbin/` |

Machine-readable index: `evidence/mobbin/corpus-index.json`.

## What changed from the first draft

The first draft had only 28 Mobbin WebP files because it was a thin MVP dry-run: enough to prove the repo structure and factory, not enough to fully distill Anthropic.

This pass expands the corpus into a real style-study base:

- broad Claude app screens;
- Claude Code/workbench screens;
- settings/profile/billing/style customization;
- full sampled onboarding/login/API onboarding flows;
- subscription/upgrade flows;
- product/marketing/pricing/research/docs/news/help website sections.

## Archive model

Raw visual truth stays local. Runtime agents should normally read distilled files first:

- `STYLE.md`
- `dna/*`
- `patterns/*`
- `components/component-atlas.md`
- `tokens/*`
- `eval/*`

They inspect the corpus only when uncertain or when doing a new distillation pass.

## Analysis artifacts

- `evidence/analysis/contact-screens.png` / `.jpg`
- `evidence/analysis/contact-sections.png` / `.jpg`
- `evidence/analysis/contact-flows-1.png` / `.jpg`
- `evidence/analysis/contact-flows-2.png` / `.jpg`
- `evidence/analysis/auto/image-metadata.json`
- `evidence/analysis/auto/ocr-sample.json`

Vision QA on contact sheets hit a transient connection error; deterministic metadata/OCR extraction succeeded and the local corpus was still saved.

## Source map and extracted facts update

The corpus is now mapped and extracted into repo-native artifacts:

- `evidence/source-map/mobbin-source-map.jsonl` — 211 local refs mapped to source metadata.
- `evidence/source-map/mobbin-source-map.csv` — spreadsheet-friendly version.
- `components/extracted/from-mobbin-screenshots/<component>/screenshot-facts.jsonl` — OCR/color/layout/source facts grouped by component.
- `evidence/web/original-code/` — public Anthropic DOM/CSS evidence for Claude product, pricing, and API pages.

Coverage exceeds the requested half-corpus threshold: all 211 local refs were processed.
