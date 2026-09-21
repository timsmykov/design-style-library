---
type: design-style-component
title: Design Style Component — rudn-academic-dataviz / insight-chart-card
style_id: rudn-academic-dataviz
repo_path: styles/rudn-academic-dataviz/components/capsules/insight-chart-card.md
confidence: adapted
ingested_at: '2026-09-17T11:50:55.264Z'
source_kind: put_page
component_id: insight-chart-card
ingested_via: put_page
component_type: data_viz
tags:
  - chart
  - data-viz
  - evidence
  - rudn
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
