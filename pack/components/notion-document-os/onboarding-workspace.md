---
title: Design Style Component — notion-document-os / onboarding-workspace
type: design-style-component
style_id: notion-document-os
component_id: onboarding-workspace
component_type: onboarding_flow
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/onboarding-workspace.md
tags: notion, document-os, workspace, blocks
---

# Onboarding / workspace creation

Style: `notion-document-os`

Component: `onboarding-workspace`

Mediums: web_app, document_workspace

Intents: create workspace, invite team, choose use case, first page

Aliases: onboarding, workspace setup, invite flow

Repo source: `styles/notion-document-os/components/capsules/onboarding-workspace.md`

## Capsule

# Onboarding / workspace creation
## Use when
Use this component for create workspace, invite team, choose use case in a calm document/workspace product.
## Structure
```text
onboarding-workspace
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/onboarding-workspace/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
