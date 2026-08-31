---
style_id: notion-document-os
component_id: database-view-table-board
title: Database view: table, board, list, calendar
component_type: data_workspace
mediums:
  - web_app
  - document_workspace
intents:
  - database
  - project tracker
  - task board
  - table view
aliases:
  - database
  - board
  - table
  - properties
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/database-view-table-board
confidence: visual_extracted
updated_at: 2026-06-30
---

# Database view: table, board, list, calendar

## Use when

Use this component for database, project tracker, task board in a calm document/workspace product.

## Structure

```text
database-view-table-board
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

- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/database-view-table-board/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
