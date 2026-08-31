---
title: Design Style Component — notion-document-os / command-block-insert
type: design-style-component
style_id: notion-document-os
component_id: command-block-insert
component_type: command_surface
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/command-block-insert.md
tags: notion, document-os, workspace, blocks
---

# Block insert command and inline controls

Style: `notion-document-os`

Component: `command-block-insert`

Mediums: web_app, document_workspace

Intents: add block, slash command, inline actions

Aliases: slash command, block menu, inline plus

Repo source: `styles/notion-document-os/components/capsules/command-block-insert.md`

## Capsule

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
