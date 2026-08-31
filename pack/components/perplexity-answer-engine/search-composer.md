---
title: Design Style Component — perplexity-answer-engine / search-composer
type: design-style-component
style_id: perplexity-answer-engine
component_id: search-composer
component_type: input_command
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/search-composer.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Search Composer

Style: `perplexity-answer-engine`

Component: `search-composer`

Mediums: web_app, answer_engine

Intents: ask, answer search UI

Aliases: search composer

Repo source: `styles/perplexity-answer-engine/components/capsules/search-composer.md`

## Capsule

# Search Composer
## Use when
Use this component for ask anything search composer focus attach model in an answer-first, source-backed interface.
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
- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/search-composer`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
