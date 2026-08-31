---
style_id: anthropic-claude
component_id: feature-tile-grid
title: Feature tiles / product cards
component_type: tile_grid
mediums:
  - marketing_page
  - product_page
  - presentation
intents:
  - feature grid
  - product card
  - capability section
  - use-case tiles
aliases:
  - tiles
  - cards
  - feature blocks
  - product grid
  - use case cards
tags:
  - anthropic
  - claude
  - tiles
  - cards
  - features
evidence_paths:
  - evidence/mobbin/sections/section-004-claude-products-6b3858df.webp
  - evidence/mobbin/sections/section-019-claude-mobbin-e3dc86d1.webp
  - evidence/mobbin/sections/section-014-claude-mobbin-ec60e21b.webp
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/by-component/feature-tile-grid
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/feature-tile-grid
confidence: extracted
updated_at: 2026-06-30
---

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
