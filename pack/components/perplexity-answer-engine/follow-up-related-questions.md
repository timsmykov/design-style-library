---
title: Design Style Component — perplexity-answer-engine / follow-up-related-questions
type: design-style-component
style_id: perplexity-answer-engine
component_id: follow-up-related-questions
component_type: query_expansion
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/follow-up-related-questions.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Follow Up Related Questions

Style: `perplexity-answer-engine`

Component: `follow-up-related-questions`

Mediums: web_app, answer_engine

Intents: related, answer search UI

Aliases: follow up related questions

Repo source: `styles/perplexity-answer-engine/components/capsules/follow-up-related-questions.md`

## Capsule

# Follow Up Related Questions
## Use when
Use this component for related follow up question chips cards in an answer-first, source-backed interface.
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
- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/follow-up-related-questions`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
