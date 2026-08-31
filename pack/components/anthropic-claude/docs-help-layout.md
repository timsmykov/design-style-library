---
title: Design Style Component — anthropic-claude / docs-help-layout
type: design-style-component
style_id: anthropic-claude
component_id: docs-help-layout
component_type: knowledge_layout
confidence: observed
repo_path: styles/anthropic-claude/components/capsules/docs-help-layout.md
tags: anthropic, claude, docs, help, api
---

# Docs / help center / release layout

Style: `anthropic-claude`

Component: `docs-help-layout`

Mediums: docs, help_center, developer_page

Intents: documentation page, help center, API docs, release notes, support search

Aliases: docs, help center, API docs, release notes, knowledge base

Repo source: `styles/anthropic-claude/components/capsules/docs-help-layout.md`

## Capsule

# Docs / help center / release layout
## Use when
Build docs, help centers, API pages, release notes, or support knowledge surfaces.
## Structure
```text
Knowledge layout
├── top/header/search
├── side navigation or topic list
├── main content column
├── cards/links for common topics
└── support/language/footer utilities
```
## Implementation recipe
- More utilitarian than marketing, but still warm and spacious.
- Side nav selected states should be muted and readable.
- Search is a core object in help pages.
- Release/news cards follow editorial rhythm with compact metadata.
- Tables for API/model/pricing data should be quiet and legible.
## Code extraction targets
- Side-nav width/spacing, selected state, content max-width.
- Search input dimensions, border, icon placement.
- Article/card grid spacing.
- API table row height and typography.
## Avoid
- Blog-magazine chaos, overdecorated docs, dark developer portals unless code context needs inverse surfaces.
