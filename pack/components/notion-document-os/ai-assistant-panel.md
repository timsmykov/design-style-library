---
title: Design Style Component — notion-document-os / ai-assistant-panel
type: design-style-component
style_id: notion-document-os
component_id: ai-assistant-panel
component_type: ai_assistant
confidence: visual_extracted
repo_path: styles/notion-document-os/components/capsules/ai-assistant-panel.md
tags: notion, document-os, workspace, blocks
---

# Notion AI assistant / rewrite panel

Style: `notion-document-os`

Component: `ai-assistant-panel`

Mediums: web_app, document_workspace

Intents: AI writing, summarize, rewrite, ask AI

Aliases: Notion AI, assistant, rewrite panel

Repo source: `styles/notion-document-os/components/capsules/ai-assistant-panel.md`

## Capsule

# Notion AI assistant / rewrite panel
## Use when
Use this component for AI writing, summarize, rewrite in a calm document/workspace product.
## Structure
```text
ai-assistant-panel
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
- Local Mobbin facts: `components/extracted/from-mobbin-screenshots/ai-assistant-panel/`.
- Full source map: `evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Saturated blue SaaS chrome, heavy dashboard cards, glossy shadows, and brand-logo cloning.
