---
title: Design Style Component — perplexity-answer-engine / answer-results-thread
type: design-style-component
style_id: perplexity-answer-engine
component_id: answer-results-thread
component_type: answer_surface
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/answer-results-thread.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Answer Results Thread

Style: `perplexity-answer-engine`

Component: `answer-results-thread`

Mediums: web_app, answer_engine

Intents: answer, answer search UI

Aliases: answer results thread

Repo source: `styles/perplexity-answer-engine/components/capsules/answer-results-thread.md`

## Capsule

# Answer Results Thread
## Use when
Use this component for answer citations sources follow-up related question thread result in an answer-first, source-backed interface.
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
- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/answer-results-thread`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
