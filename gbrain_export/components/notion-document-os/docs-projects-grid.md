---
title: Design Style Component — notion-document-os / docs-projects-grid
type: design-style-component
style_id: notion-document-os
component_id: docs-projects-grid
component_type: feature_grid
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/docs-projects-grid.md
tags: notion, document-os, workspace, blocks
---

# Docs/wiki/projects feature grid

Style: `notion-document-os`

Component: `docs-projects-grid`

Mediums: web_app, document_workspace

Intents: feature grid, docs wiki projects, product cards

Aliases: feature cards, product grid, use cases

Repo source: `styles/notion-document-os/components/capsules/docs-projects-grid.md`

## Capsule

# Docs/wiki/projects feature grid
## Use when
Use this component for feature grid, docs wiki projects, product cards in a calm document/workspace product.
## Structure
```text
docs-projects-grid
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/docs-projects-grid/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
