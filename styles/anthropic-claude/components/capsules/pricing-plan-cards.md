---
style_id: anthropic-claude
component_id: pricing-plan-cards
title: Pricing / plan cards / upgrade flow
component_type: pricing_cards
mediums:
  - marketing_page
  - web_app
  - checkout
intents:
  - pricing section
  - plan comparison
  - upgrade modal
  - subscription cards
  - billing CTA
aliases:
  - pricing
  - plans
  - Free Pro Max
  - upgrade
  - subscription
tags:
  - anthropic
  - claude
  - pricing
  - plans
  - upgrade
evidence_paths:
  - evidence/mobbin/sections/section-021-claude-mobbin-2a178ff0.webp
  - evidence/mobbin/flows/flow-26759735-subscribing-to-a-plan/
  - evidence/mobbin/flows/flow-3f6157df-upgrading-plan/
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/by-component/pricing-plan-cards
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/pricing-plan-cards
confidence: extracted
updated_at: 2026-06-30
---

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
