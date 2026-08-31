---
title: Design Style Component — perplexity-answer-engine / collections-library
type: design-style-component
style_id: perplexity-answer-engine
component_id: collections-library
component_type: knowledge_library
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/collections-library.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Collections Library

Style: `perplexity-answer-engine`

Component: `collections-library`

Mediums: web_app, answer_engine

Intents: collections, answer search UI

Aliases: collections library

Repo source: `styles/perplexity-answer-engine/components/capsules/collections-library.md`

## Capsule

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
