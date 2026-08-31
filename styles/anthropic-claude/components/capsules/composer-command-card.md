---
style_id: anthropic-claude
component_id: composer-command-card
title: Composer / command card
component_type: input_command
mediums:
  - web_app
  - ai_workbench
intents:
  - prompt composer
  - AI input
  - command center
  - tool/source selector
aliases:
  - composer
  - prompt box
  - command card
  - input box
tags:
  - anthropic
  - claude
  - composer
  - input
  - chips
evidence_paths:
  - evidence/mobbin/screens/
  - evidence/mobbin/flows/
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/AUTH_BLOCKERS.md
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/composer-command-card
confidence: extracted
updated_at: 2026-06-30
---

# Composer / command card

## Use when

The user needs to ask, instruct, upload, select a model/style/tool, or run a task.

## Structure

```text
Composer card
├── input / textarea
├── context chips
│   ├── model
│   ├── style
│   ├── project/source
│   ├── connector/tool
│   └── research/code/artifact mode
└── compact send/run button
```

## Implementation recipe

- Treat the composer as a functional command surface, not a decorative hero search bar.
- Use off-white card, thin warm-gray border, subtle radius, minimal shadow.
- Put secondary controls as compact chips inside or directly under the input.
- Keep the primary run/send action visually available but small.
- Let whitespace around the composer communicate calm.

## Code extraction targets

- Textarea/input height, radius, border, placeholder color.
- Chip size, padding, border, icon spacing.
- Send button dimensions and dark/inverse state.
- Attachment/source/menu trigger styling.

## Avoid

- Giant gradient prompt bars, oversized CTA buttons, overloaded chip rows.
