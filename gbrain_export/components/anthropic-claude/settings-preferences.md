---
title: Design Style Component — anthropic-claude / settings-preferences
type: design-style-component
style_id: anthropic-claude
component_id: settings-preferences
component_type: settings_panel
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/settings-preferences.md
tags: anthropic, claude, settings, billing, preferences
---

# Settings / profile / billing / style preferences

Style: `anthropic-claude`

Component: `settings-preferences`

Mediums: web_app, account_settings

Intents: settings page, profile form, billing settings, style customization, preferences

Aliases: settings, profile, billing, customize styles, preferences

Repo source: `styles/anthropic-claude/components/capsules/settings-preferences.md`

## Capsule

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
