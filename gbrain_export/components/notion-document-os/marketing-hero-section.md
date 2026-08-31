---
title: Design Style Component — notion-document-os / marketing-hero-section
type: design-style-component
style_id: notion-document-os
component_id: marketing-hero-section
component_type: editorial_hero
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/marketing-hero-section.md
tags: notion, document-os, workspace, blocks
---

# Marketing hero / product narrative

Style: `notion-document-os`

Component: `marketing-hero-section`

Mediums: web_app, document_workspace

Intents: homepage hero, product section, brand promise

Aliases: hero, landing page, product section

Repo source: `styles/notion-document-os/components/capsules/marketing-hero-section.md`

## Capsule

# Marketing hero / product narrative
## Use when
Use this component for homepage hero, product section, brand promise in a calm document/workspace product.
## Structure
```text
marketing-hero-section
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/marketing-hero-section/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
