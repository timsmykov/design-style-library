---
style_id: notion-document-os
component_id: onboarding-workspace
title: Onboarding / workspace creation
component_type: onboarding_flow
mediums:
  - web_app
  - document_workspace
intents:
  - create workspace
  - invite team
  - choose use case
  - first page
aliases:
  - onboarding
  - workspace setup
  - invite flow
tags:
  - notion
  - document-os
  - workspace
  - blocks
evidence_paths:
  - evidence/source-map/mobbin-source-map.jsonl
  - evidence/mobbin/
extracted_paths:
  - styles/notion-document-os/components/extracted/from-mobbin-screenshots/onboarding-workspace
confidence: visual_extracted
updated_at: 2026-06-30
---

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
