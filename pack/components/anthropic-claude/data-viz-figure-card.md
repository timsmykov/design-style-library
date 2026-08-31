---
title: Design Style Component — anthropic-claude / data-viz-figure-card
type: design-style-component
style_id: anthropic-claude
component_id: data-viz-figure-card
component_type: data_viz
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/data-viz-figure-card.md
tags: anthropic, claude, data-viz, chart, figure
---

# Data visualization figure card

Style: `anthropic-claude`

Component: `data-viz-figure-card`

Mediums: data_viz, presentation, visual_note, report

Intents: chart, graph, figure card, analysis visualization, metric summary

Aliases: chart, graph, visualization, figure, metric card

Repo source: `styles/anthropic-claude/components/capsules/data-viz-figure-card.md`

## Capsule

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
