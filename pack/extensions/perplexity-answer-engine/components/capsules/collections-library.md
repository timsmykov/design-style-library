---
style_id: perplexity-answer-engine
component_id: collections-library
title: Collections Library
component_type: knowledge_library
mediums:
  - web_app
  - answer_engine
intents:
  - collections
  - answer search UI
aliases:
  - collections library
tags:
  - perplexity
  - answer-engine
  - no-login-wave-01
evidence_paths:
  - styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl
  - styles/perplexity-answer-engine/evidence/mobbin/
extracted_paths:
  - styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/collections-library
confidence: extracted
updated_at: 2026-06-30
---

# Collections Library

## Use when

Use this component for collections library spaces saved threads in an answer-first, source-backed interface.

## Structure

```text
Component
├── concise label/title
├── content or control body
├── evidence/context metadata
└── compact action row
```

## Implementation recipe

- Use white or cool-off-white surfaces with thin neutral borders.
- Keep typography crisp and utility-sized around the answer body.
- Use teal only for active/action/proof accents.
- Preserve traceability: show source, state, or query context near the control.
- Prefer compact chips/cards over bulky marketing blocks.

## Evidence

- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/collections-library`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
