---
style_id: notion-document-os
component_id: marketing-hero-section
title: Marketing hero / product narrative
component_type: editorial_hero
mediums:
  - web_app
  - document_workspace
intents:
  - homepage hero
  - product section
  - brand promise
aliases:
  - hero
  - landing page
  - product section
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/marketing-hero-section
confidence: visual_extracted
updated_at: 2026-06-30
---

# Marketing hero / product narrative

## Use when

Use this component for homepage hero, product section, brand promise in a calm document/workspace product.

## Structure

```text
marketing-hero-section
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

- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/marketing-hero-section/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
