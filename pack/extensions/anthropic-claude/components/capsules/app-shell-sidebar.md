---
style_id: anthropic-claude
component_id: app-shell-sidebar
title: App shell / sidebar
component_type: navigation_shell
mediums:
  - web_app
  - ai_workbench
intents:
  - AI app shell
  - workspace navigation
  - conversation/project/artifact navigation
aliases:
  - sidebar
  - navigation
  - left rail
  - workspace shell
tags:
  - anthropic
  - claude
  - shell
  - sidebar
  - navigation
evidence_paths:
  - evidence/mobbin/screens/
  - evidence/analysis/contact-screens.png
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/AUTH_BLOCKERS.md
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/app-shell-sidebar
confidence: extracted
updated_at: 2026-06-30
---

# App shell / sidebar

## Use when

Build the outer frame for an AI workspace: chat, projects, artifacts, code, settings, or document work.

## Structure

```text
Warm left sidebar
├── product mark / new chat
├── search
├── customize / instructions / styles
├── chats
├── projects
├── artifacts
├── code or work mode
└── account/settings affordance

Main canvas
├── welcome or current conversation
├── optional artifact/work panel
└── composer command card
```

## Implementation recipe

- Use a quiet warm sidebar surface adjacent to a warm paper main canvas.
- Sidebar rows are compact, with thin utility icons and short labels.
- Active rows use pale beige/tint fill and restrained text emphasis.
- Main canvas should feel more important than navigation.
- Keep chrome thin: no saturated active bars, no heavy nav shadows.

## Code extraction targets

- Sidebar container computed background, border, width.
- Row height, gap, icon size, active/hover/focus states.
- Main canvas background and shell grid/flex layout.
- Responsive collapse behavior if visible.

## Avoid

- Blue SaaS sidebars, neon active states, heavy icons, dashboard density.
