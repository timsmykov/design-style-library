---
title: Design Style Component — notion-document-os / pricing-plan-cards
type: design-style-component
style_id: notion-document-os
component_id: pricing-plan-cards
component_type: pricing
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/pricing-plan-cards.md
tags: notion, document-os, workspace, blocks
---

# Pricing / plan comparison

Style: `notion-document-os`

Component: `pricing-plan-cards`

Mediums: web_app, document_workspace

Intents: plan cards, upgrade, billing, feature comparison

Aliases: pricing, plans, upgrade

Repo source: `styles/notion-document-os/components/capsules/pricing-plan-cards.md`

## Capsule

# Pricing / plan comparison
## Use when
Use this component for plan cards, upgrade, billing in a calm document/workspace product.
## Structure
```text
pricing-plan-cards
├── quiet structural container
├── content-first title/label area
├── compact inline controls
└── secondary metadata/actions
```
## Implementation recipe
- Use white or muted gray surfaces, hairline borders, and minimal shadow.
- Make text/content structure the main hierarchy.
- Place controls close to the content they affect.
- Use selected/hover states as low-contrast gray fills.
- Keep iconography tiny, monochrome, and functional.
## Evidence
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/pricing-plan-cards/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
