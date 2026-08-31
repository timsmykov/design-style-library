---
title: Design Style Component — notion-document-os / database-view-table-board
type: design-style-component
style_id: notion-document-os
component_id: database-view-table-board
component_type: data_workspace
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/database-view-table-board.md
tags: notion, document-os, workspace, blocks
---

# Database view: table, board, list, calendar

Style: `notion-document-os`

Component: `database-view-table-board`

Mediums: web_app, document_workspace

Intents: database, project tracker, task board, table view

Aliases: database, board, table, properties

Repo source: `styles/notion-document-os/components/capsules/database-view-table-board.md`

## Capsule

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
