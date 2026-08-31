---
style_id: notion-document-os
component_id: app-shell-sidebar
title: Workspace app shell / sidebar
component_type: navigation_shell
mediums:
  - web_app
  - document_workspace
intents:
  - workspace navigation
  - teamspaces
  - private pages
  - settings access
aliases:
  - sidebar
  - left rail
  - workspace shell
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/app-shell-sidebar
confidence: visual_extracted
updated_at: 2026-06-30
---

# Workspace app shell / sidebar

## Use when

Use this component for workspace navigation, teamspaces, private pages in a calm document/workspace product.

## Structure

```text
app-shell-sidebar
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

- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/app-shell-sidebar/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
