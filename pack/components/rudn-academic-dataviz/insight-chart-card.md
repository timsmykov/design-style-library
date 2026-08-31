---
title: Design Style Component — rudn-academic-dataviz / insight-chart-card
type: design-style-component
style_id: rudn-academic-dataviz
component_id: insight-chart-card
component_type: data_viz
confidence: adapted
repo_path: styles/rudn-academic-dataviz/components/capsules/insight-chart-card.md
tags: rudn, data-viz, chart, evidence
---

# Insight-first chart card

Style: `rudn-academic-dataviz`

Component: `insight-chart-card`

Mediums: presentation, report, web, worksheet

Intents: chart, comparison, ranking, trend, evidence visualization

Aliases: chart card, data figure, evidence chart

Repo source: `styles/rudn-academic-dataviz/components/capsules/insight-chart-card.md`

## Capsule

# Insight-first chart card
## Structure
Insight title -> unit/period -> chart -> direct annotation -> source/method note.
## Recipe
- Highlight one series or bar in `#2E6BFE`.
- Render comparisons in gray/charcoal.
- Use thin `#E8E8E8` gridlines and direct labels.
- Put exact source and method below or beside the visual.
- Use `#4950BC` only for interactive selection or link behavior.
## Avoid
Rainbow legends, raw chart-library defaults, unlabeled axes, 3D charts, and titles that merely repeat the metric name.
