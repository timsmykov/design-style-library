---
style_id: anthropic-claude
component_id: data-viz-figure-card
title: Data visualization figure card
component_type: data_viz
mediums:
  - data_viz
  - presentation
  - visual_note
  - report
intents:
  - chart
  - graph
  - figure card
  - analysis visualization
  - metric summary
aliases:
  - chart
  - graph
  - visualization
  - figure
  - metric card
tags:
  - anthropic
  - claude
  - data-viz
  - chart
  - figure
evidence_paths:
  - evidence/mobbin/sections/section-008-claude-mobbin-23be18aa.webp
  - evidence/mobbin/screens/screen-019-claude-mobbin-98255484.webp
  - patterns/data-viz.md
extracted_paths:
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/data-viz-figure-card
confidence: extracted
updated_at: 2026-06-30
---

# Data visualization figure card

## Use when

Create charts, graphs, metric summaries, analysis cards, or visual-science explanatory figures.

## Structure

```text
Figure card
├── title stated as insight
├── compact chart/table/diagram
├── one clay-highlighted key series or annotation
├── muted supporting series
└── caption explaining what to notice
```

## Implementation recipe

- Warm ivory canvas, thin warm-gray gridlines, charcoal labels.
- Use one clay highlight for the main point.
- Use muted neutrals for comparisons.
- Pair visualization with a short explanatory caption.
- Prefer simple bar/line/table/diagram forms over complex dashboards.

## Code extraction targets

- Gridline color, label typography, legend placement.
- Figure card padding/radius/border.
- Highlight/annotation style.
- Caption and source note hierarchy.

## Avoid

- Rainbow palettes, glossy dashboard cards, raw chart dumps without interpretation.
