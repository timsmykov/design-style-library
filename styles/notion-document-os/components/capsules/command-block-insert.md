---
style_id: notion-document-os
component_id: command-block-insert
title: Block insert command and inline controls
component_type: command_surface
mediums:
  - web_app
  - document_workspace
intents:
  - add block
  - slash command
  - inline actions
aliases:
  - slash command
  - block menu
  - inline plus
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/command-block-insert
confidence: visual_extracted
updated_at: 2026-06-30
---

# Block insert command and inline controls

## Use when

Use this component for add block, slash command, inline actions in a calm document/workspace product.

## Structure

```text
command-block-insert
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

- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/command-block-insert/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
