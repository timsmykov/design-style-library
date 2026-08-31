---
title: Design Style Component — anthropic-claude / pricing-plan-cards
type: design-style-component
style_id: anthropic-claude
component_id: pricing-plan-cards
component_type: pricing_cards
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/pricing-plan-cards.md
tags: anthropic, claude, pricing, plans, upgrade
---

# Pricing / plan cards / upgrade flow

Style: `anthropic-claude`

Component: `pricing-plan-cards`

Mediums: marketing_page, web_app, checkout

Intents: pricing section, plan comparison, upgrade modal, subscription cards, billing CTA

Aliases: pricing, plans, Free Pro Max, upgrade, subscription

Repo source: `styles/anthropic-claude/components/capsules/pricing-plan-cards.md`

## Capsule

# Pricing / plan cards / upgrade flow
## Use when
Build pricing sections, plan cards, upgrade dialogs, plan comparison, or billing conversion surfaces.
## Structure
```text
Pricing block
├── heading + short trust copy
├── monthly/yearly toggle with savings note
├── plan cards: Free / Pro / Max / Team
│   ├── plan name
│   ├── plain-language fit
│   ├── price
│   ├── feature bullets
│   └── one CTA
└── optional comparison/details table
```
## Implementation recipe
- Cards are text-heavy and trust-oriented.
- Use warm card surfaces with restrained borders.
- Prefer check icons or tiny markers over colorful feature badges.
- Highlight the recommended/paid plan subtly, not with aggressive color.
- Explain model access, usage, projects, memory, connectors, code/research plainly.
## Code extraction targets
- Card grid breakpoints, card radius, border, pricing typography.
- Billing toggle dimensions/states.
- Feature row spacing and icon treatment.
- Primary/secondary plan CTA styles.
## Avoid
- Fintech-blue checkout styling, gamified urgency, excessive discount badges, aggressive shadows.
