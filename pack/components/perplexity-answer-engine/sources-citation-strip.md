---
title: Design Style Component — perplexity-answer-engine / sources-citation-strip
type: design-style-component
style_id: perplexity-answer-engine
component_id: sources-citation-strip
component_type: evidence_trust
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/sources-citation-strip.md
tags: perplexity, answer-engine, no-login-wave-01
---

# Sources Citation Strip

Style: `perplexity-answer-engine`

Component: `sources-citation-strip`

Mediums: web_app, answer_engine

Intents: sources, answer search UI

Aliases: sources citation strip

Repo source: `styles/perplexity-answer-engine/components/capsules/sources-citation-strip.md`

## Capsule

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
