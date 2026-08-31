---
style_id: notion-document-os
component_id: ai-assistant-panel
title: Notion AI assistant / rewrite panel
component_type: ai_assistant
mediums:
  - web_app
  - document_workspace
intents:
  - AI writing
  - summarize
  - rewrite
  - ask AI
aliases:
  - Notion AI
  - assistant
  - rewrite panel
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/ai-assistant-panel
confidence: visual_extracted
updated_at: 2026-06-30
---

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
