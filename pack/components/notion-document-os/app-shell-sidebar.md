---
title: Design Style Component — notion-document-os / app-shell-sidebar
type: design-style-component
style_id: notion-document-os
component_id: app-shell-sidebar
component_type: navigation_shell
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/app-shell-sidebar.md
tags: notion, document-os, workspace, blocks
---

# Workspace app shell / sidebar

Style: `notion-document-os`

Component: `app-shell-sidebar`

Mediums: web_app, document_workspace

Intents: workspace navigation, teamspaces, private pages, settings access

Aliases: sidebar, left rail, workspace shell

Repo source: `styles/notion-document-os/components/capsules/app-shell-sidebar.md`

## Capsule

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
