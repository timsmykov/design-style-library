---
title: Design Style Component — notion-document-os / template-gallery
type: design-style-component
style_id: notion-document-os
component_id: template-gallery
component_type: template_gallery
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/template-gallery.md
tags: notion, document-os, workspace, blocks
---

# Template gallery / starter library

Style: `notion-document-os`

Component: `template-gallery`

Mediums: web_app, document_workspace

Intents: template selection, starter document, use-case gallery

Aliases: templates, gallery, starter kit

Repo source: `styles/notion-document-os/components/capsules/template-gallery.md`

## Capsule

# Template gallery / starter library
## Use when
Use this component for template selection, starter document, use-case gallery in a calm document/workspace product.
## Structure
```text
template-gallery
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/template-gallery/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
