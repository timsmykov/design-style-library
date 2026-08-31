---
title: Design Style Component — anthropic-claude / editorial-hero-section
type: design-style-component
style_id: anthropic-claude
component_id: editorial-hero-section
component_type: marketing_hero
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/editorial-hero-section.md
tags: anthropic, claude, hero, editorial, marketing
---

# Editorial hero section

Style: `anthropic-claude`

Component: `editorial-hero-section`

Mediums: marketing_page, landing_page, presentation

Intents: hero, product intro, brand headline, top section

Aliases: hero, headline, landing intro, editorial top section

Repo source: `styles/anthropic-claude/components/capsules/editorial-hero-section.md`

## Capsule

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
