# Component Retrieval Architecture

Goal: let an agent build a UI from a large style library without reading the whole corpus.

## Decision

Use a hybrid architecture:

1. **Git repo is source of truth.** It stores evidence, extracted implementation facts, tokens, component capsules, golden examples, and evals.
2. **Gbrain is the semantic retrieval layer.** It indexes compact, curated component slices, not raw screenshots and not huge copied CSS dumps.
3. **Runtime agents follow a narrow read path.** They read global style primitives first, then retrieve only the component capsules needed for the requested artifact.

This keeps the library self-contained while avoiding context bloat when packs grow to hundreds of screenshots and dozens of component recipes.

## Why not “just repo”

A repo-only approach is enough for 1-3 small packs. It breaks down when we have:

- 10+ styles;
- hundreds of screenshots per style;
- component-level code evidence;
- multiple target media: apps, landing pages, decks, visual notes, charts;
- many overlapping components, e.g. auth, pricing, settings, tables, charts.

Without retrieval, the agent either reads too much or guesses from too little.

## Why not “just Gbrain”

Gbrain should not become the canonical store for raw style evidence.

Raw visual/coded evidence needs:

- deterministic file paths;
- git diffs;
- provenance audit;
- local binary assets;
- reproducible extraction scripts;
- offline eval fixtures.

Those belong in the repo. Gbrain stores *retrievable slices* generated from the repo.

## Data flow

```text
BUILD TIME

Mobbin / Firecrawl / Browser-CDP / Playwright
        │
        ▼
repo: evidence/raw + extracted facts
        │
        ▼
repo: distilled style pack
        ├── STYLE.md
        ├── dna/*
        ├── tokens/*
        ├── patterns/*
        ├── components/component-atlas.md
        └── components/capsules/*.md
        │
        ▼
tools/component_index.py
        ├── components/component-index.jsonl
        └── gbrain_export/components/<style>/<component>.md
        │
        ▼
Gbrain source: design-style-library

RUNTIME

User asks for UI / slide / visual note / chart
        │
        ▼
Agent reads repo global style primitives
        │
        ▼
Agent maps request → component intents
        │
        ▼
Gbrain semantic search over compact component slices
        │
        ▼
Agent reads only matched repo capsules/evidence snippets
        │
        ▼
Generate artifact + run eval checklist
```

## Runtime read ladder

Agents should not start by opening every file in a style pack.

```text
1. Select style_id from registry.yaml.
2. Read only:
   - styles/<style>/STYLE.md
   - styles/<style>/dna/principles.md
   - styles/<style>/tokens/tokens.json
   - styles/<style>/patterns/index.md
   - styles/<style>/eval/checklist.yaml
3. Infer needed components from the task.
4. Query Gbrain for: style_id + component intent + medium.
5. Read the matching component capsule(s) from repo.
6. If precision matters, read referenced extracted implementation facts, not all raw screenshots.
7. Generate artifact.
8. Run eval/checklist.yaml and component-specific acceptance checks.
```

## Component capsule

A component capsule is a small, self-contained design/implementation recipe.

It answers:

- When should this component be used?
- What does it look like structurally?
- Which tokens does it use?
- What implementation facts were actually observed/extracted?
- What mistakes should the agent avoid?
- Which evidence paths prove it?

It does **not** include copied production CSS as a dependency. Raw code extraction is evidence. Runtime output must be original/adapted.

## Real code extraction policy

We should extract real implementation facts, not blindly copy code.

Allowed evidence:

- public DOM skeletons with class names redacted or normalized where useful;
- computed CSS values: color, typography, spacing, radius, border, shadow, layout;
- SVG/icon structure notes where legally safe;
- CSS rule summaries and token candidates;
- interaction/state observations;
- screenshots and rendered diffs.

Do not use:

- proprietary CSS/JS as a runtime dependency;
- pixel-perfect clone recipes;
- private/authenticated assets unless explicitly allowed;
- logos/brand marks for generated outputs unless the user specifically needs an internal reference.

Recommended extracted-code layout:

```text
styles/<style>/components/extracted/<component_id>/
  dom.html                 # sanitized DOM skeleton
  computed.json            # measured computed styles
  css-candidates.css       # selected source rules or normalized snippets for evidence only
  tokens.json              # component-local token candidates
  states.json              # hover/focus/disabled/loading/etc.
  provenance.yaml          # URL, capture time, tool, selector, screenshot refs
  normalized-recipe.md     # original implementation recipe derived from evidence
```

## What goes into Gbrain

Index only compact, retrieval-friendly files:

- `gbrain_export/components/<style>/<component>.md`
- high-level style overview pages;
- taxonomy/category pages;
- maybe gold-example summaries and eval outcomes.

Do **not** index:

- raw screenshots;
- huge HTML dumps;
- raw CSS bundles;
- OCR dumps except selected facts;
- duplicate evidence files.

## Retrieval keys

Every Gbrain component slice should carry:

- `style_id`
- `component_id`
- `component_type`
- `mediums`
- `intents`
- `aliases`
- `tags`
- `repo_path`
- `evidence_paths`
- `confidence`
- `updated_at`

This makes queries like these work:

- `anthropic claude auth onboarding verification form`
- `anthropic pricing cards Free Pro Max plan comparison`
- `claude settings profile billing style customization`
- `anthropic graph model comparison chart figure card`

## Agent behavior contract

If a task names a concrete component, the agent must retrieve that capsule before generating.

Examples:

| User asks for | Agent retrieves |
|---|---|
| login page | `auth-onboarding` |
| pricing section | `pricing-plan-cards` |
| settings panel | `settings-preferences` |
| chart / graph | `model-comparison-figure` or `data-viz-figure-card` |
| AI app shell | `app-shell-sidebar` + `composer-command-card` |
| artifact/code workspace | `artifact-workbench-panel` |

If no capsule exists, the agent may fall back to `component-atlas.md`, but should mark the output as lower confidence and propose adding a capsule.

## Scale guardrails

- Keep capsules small: target 500-1500 words.
- Keep raw evidence local and deduped.
- Generate Gbrain slices from repo, never hand-edit them as source of truth.
- Use semantic retrieval for selection, then repo paths for exact grounding.
- Rebuild indexes after component changes.
- Run fresh-agent offline eval before marking a style pack `offline_ready: true`.

## Open implementation work

1. Build Browser/CDP computed-style extractor.
2. Build component extraction runners for common targets: buttons, cards, forms, nav, pricing, settings, charts.
3. Expand component capsules with extracted code facts.
4. Add `gbrain_export/` as a dedicated Gbrain source.
5. Add retrieval evals: query → expected component capsule.

## Current implementation status

Implemented in this repo:

- `schemas/component-capsule.schema.json`
- `tools/component_index.py`
- `tools/gbrain_export_sync.sh`
- `styles/anthropic-claude/components/capsules/*.md`
- `styles/anthropic-claude/components/component-index.jsonl`
- `gbrain_export/components/anthropic-claude/*.md`

Current Anthropic component capsules:

1. `app-shell-sidebar`
2. `composer-command-card`
3. `auth-onboarding`
4. `settings-preferences`
5. `pricing-plan-cards`
6. `artifact-workbench-panel`
7. `editorial-hero-section`
8. `feature-tile-grid`
9. `docs-help-layout`
10. `model-comparison-figure`
11. `data-viz-figure-card`

Build and sync command:

```bash
./tools/gbrain_export_sync.sh /root/hermes-workspace/design-style-library
```

Smoke query after sync:

```bash
gbrain query 'anthropic claude pricing cards upgrade subscription' \
  --source-id design-style-library \
  --limit 5 \
  --no-expand
```

Expected top hit: `design-style-library/components/anthropic-claude/pricing-plan-cards`.
