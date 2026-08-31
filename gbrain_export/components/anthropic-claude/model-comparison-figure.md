---
title: Design Style Component — anthropic-claude / model-comparison-figure
type: design-style-component
style_id: anthropic-claude
component_id: model-comparison-figure
component_type: comparison_figure
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/model-comparison-figure.md
tags: anthropic, claude, models, comparison, chart
---

# Model comparison / pricing figure

Style: `anthropic-claude`

Component: `model-comparison-figure`

Mediums: marketing_page, docs, data_viz, presentation

Intents: model comparison, pricing table, capability comparison, plan comparison, chart-like block

Aliases: model chart, Opus Sonnet Haiku, comparison table, pricing table, figure card

Repo source: `styles/anthropic-claude/components/capsules/model-comparison-figure.md`

## Capsule

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
