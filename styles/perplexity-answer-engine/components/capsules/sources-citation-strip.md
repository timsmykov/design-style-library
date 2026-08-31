---
style_id: perplexity-answer-engine
component_id: sources-citation-strip
title: Sources Citation Strip
component_type: evidence_trust
mediums:
  - web_app
  - answer_engine
intents:
  - sources
  - answer search UI
aliases:
  - sources citation strip
tags:
  - perplexity
  - answer-engine
  - no-login-wave-01
evidence_paths:
  - styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl
  - styles/perplexity-answer-engine/evidence/mobbin/
extracted_paths:
  - styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/sources-citation-strip
confidence: extracted
updated_at: 2026-06-30
---

# Sources Citation Strip

## Use when

Use this component for sources citations numbered references cards in an answer-first, source-backed interface.

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

- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/sources-citation-strip`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
