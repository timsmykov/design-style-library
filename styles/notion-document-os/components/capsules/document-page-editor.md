---
style_id: notion-document-os
component_id: document-page-editor
title: Document page editor / block canvas
component_type: document_canvas
mediums:
  - web_app
  - document_workspace
intents:
  - document editor
  - block page
  - knowledge base article
  - wiki page
aliases:
  - page editor
  - block canvas
  - document
  - wiki page
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/document-page-editor
confidence: visual_extracted
updated_at: 2026-06-30
---

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
