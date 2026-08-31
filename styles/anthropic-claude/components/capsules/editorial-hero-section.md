---
style_id: anthropic-claude
component_id: editorial-hero-section
title: Editorial hero section
component_type: marketing_hero
mediums:
  - marketing_page
  - landing_page
  - presentation
intents:
  - hero
  - product intro
  - brand headline
  - top section
aliases:
  - hero
  - headline
  - landing intro
  - editorial top section
tags:
  - anthropic
  - claude
  - hero
  - editorial
  - marketing
evidence_paths:
  - evidence/mobbin/sections/section-001-claude-hero-5456030e.webp
  - evidence/mobbin/sections/section-024-claude-mobbin-6eb09dee.webp
  - evidence/mobbin/sections/section-023-claude-mobbin-c6697f91.webp
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/by-component/editorial-hero-section
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/editorial-hero-section
confidence: extracted
updated_at: 2026-06-30
---

# Editorial hero section

## Use when

Introduce a product, feature, research area, or major page.

## Structure

```text
Hero
├── minimal nav/header
├── large editorial headline
├── short human subcopy
├── one primary CTA or paired CTA
└── optional human/symbolic/product-proof visual
```

## Implementation recipe

- Warm paper canvas first, typography second, decoration last.
- Headline should feel editorial and human, often with literary scale.
- Copy frames Claude-like work: thinking partner, problem solving, breaking down hard tasks.
- Use black/charcoal CTA; clay is accent, not default CTA fill.
- Visuals should be human/symbolic/product-proof, never robot/neon.

## Code extraction targets

- Container max-width, headline size/line-height, nav spacing.
- CTA button dimensions and pair spacing.
- Hero visual placement and responsive stacking.

## Avoid

- Generic AI gradient hero, huge fake chat mockups as the only visual idea, empty hype copy.
