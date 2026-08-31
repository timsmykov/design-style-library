---
title: Design Style Component — notion-document-os / document-page-editor
type: design-style-component
style_id: notion-document-os
component_id: document-page-editor
component_type: document_canvas
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/document-page-editor.md
tags: notion, document-os, workspace, blocks
---

# Document page editor / block canvas

Style: `notion-document-os`

Component: `document-page-editor`

Mediums: web_app, document_workspace

Intents: document editor, block page, knowledge base article, wiki page

Aliases: page editor, block canvas, document, wiki page

Repo source: `styles/notion-document-os/components/capsules/document-page-editor.md`

## Capsule

# Document page editor / block canvas
## Use when
Use this component for document editor, block page, knowledge base article in a calm document/workspace product.
## Structure
```text
document-page-editor
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/document-page-editor/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
