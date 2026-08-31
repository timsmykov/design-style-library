---
style_id: anthropic-claude
component_id: settings-preferences
title: Settings / profile / billing / style preferences
component_type: settings_panel
mediums:
  - web_app
  - account_settings
intents:
  - settings page
  - profile form
  - billing settings
  - style customization
  - preferences
aliases:
  - settings
  - profile
  - billing
  - customize styles
  - preferences
tags:
  - anthropic
  - claude
  - settings
  - billing
  - preferences
evidence_paths:
  - evidence/mobbin/flows/flow-0ef2d31c-settings/
  - evidence/mobbin/flows/flow-f064eaa0-settings/
  - evidence/mobbin/screens/screen-060-claude-code-515551de.webp
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/AUTH_BLOCKERS.md
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/settings-preferences
confidence: extracted
updated_at: 2026-06-30
---

# Settings / profile / billing / style preferences

## Use when

Build account/profile settings, billing controls, model/style preferences, or customization panels.

## Structure

```text
Settings surface
├── left tab rail
│   ├── Profile
│   ├── Billing
│   ├── Account
│   └── Preferences / styles
└── right content panel
    ├── section heading
    ├── form rows
    ├── toggles/selectors
    └── isolated destructive/advanced actions
```

## Implementation recipe

- Settings should be boring, legible, and low-drama.
- Use a two-column layout on desktop, stacked sections on narrow screens.
- Preference rows need label + one-line helper text.
- Style choices can be tabs/pills/cards: Learning, Concise, Explanatory, Formal.
- Billing/subscription content should reuse pricing grammar, not a separate finance look.

## Code extraction targets

- Tab rail width, selected state, section spacing.
- Form row height and helper text color.
- Toggle/radio/pill states.
- Modal/page container radius and max-width.

## Avoid

- Dashboard-style settings overload, nested modals for simple choices, aggressive billing visuals.
