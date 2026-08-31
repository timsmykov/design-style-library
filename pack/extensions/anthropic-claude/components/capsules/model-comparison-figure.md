---
style_id: anthropic-claude
component_id: model-comparison-figure
title: Model comparison / pricing figure
component_type: comparison_figure
mediums:
  - marketing_page
  - docs
  - data_viz
  - presentation
intents:
  - model comparison
  - pricing table
  - capability comparison
  - plan comparison
  - chart-like block
aliases:
  - model chart
  - Opus Sonnet Haiku
  - comparison table
  - pricing table
  - figure card
tags:
  - anthropic
  - claude
  - models
  - comparison
  - chart
evidence_paths:
  - evidence/mobbin/sections/section-026-claude-mobbin-9a9ef5bc.webp
  - evidence/mobbin/sections/section-020-claude-mobbin-9a8549ad.webp
  - evidence/mobbin/sections/section-022-claude-mobbin-08f8d749.webp
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/by-component/model-comparison-figure
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/model-comparison-figure
confidence: extracted
updated_at: 2026-06-30
---

# Model comparison / pricing figure

## Use when

Compare models, capabilities, prices, plans, performance tiers, or analysis dimensions.

## Structure

```text
Comparison figure
├── title + short interpretive note
├── rows/cards for model or tier
│   ├── name
│   ├── role / best use
│   ├── metric or price
│   └── short explanation
└── single highlighted takeaway
```

## Implementation recipe

- Prefer editorial figure cards and simple ladders over glossy dashboards.
- Use charcoal labels, warm-gray dividers, and one clay highlight.
- For model comparison, show role and use case, not just numbers.
- For pricing, cards first, table second.
- Place interpretation near the data so users do not decode alone.

## Code extraction targets

- Row/card spacing, dividers, label typography, highlight token.
- Responsive table/card transformation.
- Tooltip/caption styling if present.

## Avoid

- Rainbow charts, 3D plots, overspecified dashboards, unlabeled metrics.
