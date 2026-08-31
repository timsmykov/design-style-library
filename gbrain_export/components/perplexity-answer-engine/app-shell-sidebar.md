---
title: Design Style Component — perplexity-answer-engine / app-shell-sidebar
type: design-style-component
style_id: perplexity-answer-engine
component_id: app-shell-sidebar
component_type: navigation_shell
confidence: extracted
repo_path: styles/perplexity-answer-engine/components/capsules/app-shell-sidebar.md
tags: perplexity, answer-engine, no-login-wave-01
---

# App Shell Sidebar

Style: `perplexity-answer-engine`

Component: `app-shell-sidebar`

Mediums: web_app, answer_engine

Intents: home, answer search UI

Aliases: app shell sidebar

Repo source: `styles/perplexity-answer-engine/components/capsules/app-shell-sidebar.md`

## Capsule

# App Shell Sidebar
## Use when
Use this component for home discover library spaces collections threads sidebar in an answer-first, source-backed interface.
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
- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/app-shell-sidebar`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.
## Avoid
- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
