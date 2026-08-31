---
style_id: anthropic-claude
component_id: docs-help-layout
title: Docs / help center / release layout
component_type: knowledge_layout
mediums:
  - docs
  - help_center
  - developer_page
intents:
  - documentation page
  - help center
  - API docs
  - release notes
  - support search
aliases:
  - docs
  - help center
  - API docs
  - release notes
  - knowledge base
tags:
  - anthropic
  - claude
  - docs
  - help
  - api
evidence_paths:
  - evidence/mobbin/sections/section-005-claude-4f7ea41a.webp
  - evidence/mobbin/sections/section-017-claude-mobbin-1cb7ca9a.webp
  - evidence/mobbin/sections/section-029-claude-mobbin-d145ac87.webp
extracted_paths:
confidence: observed
updated_at: 2026-06-30
---

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
