---
title: Design Style Component — perplexity-answer-engine / help-article-layout
type: design-style-component
style_id: perplexity-answer-engine
component_id: help-article-layout
component_type: docs_help
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/help-article-layout.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Help Article Layout

Style: `perplexity-answer-engine`

Component: `help-article-layout`

Mediums: web_app, answer_engine

Intents: faq, answer search UI

Aliases: help article layout

Repo source: `styles/perplexity-answer-engine/components/capsules/help-article-layout.md`

## Capsule

# Help Article Layout
## Use when
Use this component for faq help article detail support in an answer-first, source-backed interface.
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
- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/help-article-layout`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
