---
style_id: notion-document-os
component_id: docs-projects-grid
title: Docs/wiki/projects feature grid
component_type: feature_grid
mediums:
  - web_app
  - document_workspace
intents:
  - feature grid
  - docs wiki projects
  - product cards
aliases:
  - feature cards
  - product grid
  - use cases
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/docs-projects-grid
confidence: visual_extracted
updated_at: 2026-06-30
---

# Docs/wiki/projects feature grid

## Use when

Use this component for feature grid, docs wiki projects, product cards in a calm document/workspace product.

## Structure

```text
docs-projects-grid
├── quiet structural container
├── content-first title/label area
├── compact inline controls
└── secondary metadata/actions
```

## Implementation recipe

- Use white or muted gray surfaces, hairline borders, and minimal shadow.
- Make text/content structure the main hierarchy.
- Place controls close to the content they affect.
- Use selected/hover states as low-contrast gray fills.
- Keep iconography tiny, monochrome, and functional.

## Evidence

- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/docs-projects-grid/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
