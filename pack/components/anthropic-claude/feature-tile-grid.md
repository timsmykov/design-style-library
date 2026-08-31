---
title: Design Style Component — anthropic-claude / feature-tile-grid
type: design-style-component
style_id: anthropic-claude
component_id: feature-tile-grid
component_type: tile_grid
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/feature-tile-grid.md
tags: anthropic, claude, tiles, cards, features
---

# Feature tiles / product cards

Style: `anthropic-claude`

Component: `feature-tile-grid`

Mediums: marketing_page, product_page, presentation

Intents: feature grid, product card, capability section, use-case tiles

Aliases: tiles, cards, feature blocks, product grid, use case cards

Repo source: `styles/anthropic-claude/components/capsules/feature-tile-grid.md`

## Capsule

# Feature tiles / product cards
## Use when
Show product split, use cases, capabilities, related posts, or feature choices.
## Structure
```text
Tile block
├── section eyebrow / heading
├── 2-4 large cards or 3-6 compact cards
├── each card: title, short body, proof cue/icon/mini visual
└── optional CTA/link row
```
## Implementation recipe
- One idea per tile.
- Use generous card padding and strong typography hierarchy.
- For developer/API cards, black/ivory contrast can appear.
- For consumer/productivity cards, warm light surfaces dominate.
- Icons are small, line/symbolic, and secondary.
## Code extraction targets
- Grid columns/gaps, card radius/padding, body typography.
- Icon size and placement.
- Hover/link affordances.
- Dark card inverse token variants.
## Avoid
- Dense dashboard widgets, colorful icon overload, six unrelated visual languages in one grid.
