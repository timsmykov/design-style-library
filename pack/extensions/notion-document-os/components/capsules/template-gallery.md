---
style_id: notion-document-os
component_id: template-gallery
title: Template gallery / starter library
component_type: template_gallery
mediums:
  - web_app
  - document_workspace
intents:
  - template selection
  - starter document
  - use-case gallery
aliases:
  - templates
  - gallery
  - starter kit
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/template-gallery
confidence: visual_extracted
updated_at: 2026-06-30
---

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
