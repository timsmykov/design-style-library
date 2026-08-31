---
title: Design Style Component — anthropic-claude / auth-onboarding
type: design-style-component
style_id: anthropic-claude
component_id: auth-onboarding
component_type: form_flow
confidence: extracted
repo_path: styles/anthropic-claude/components/capsules/auth-onboarding.md
tags: anthropic, claude, auth, onboarding, forms
---

# Auth / onboarding / verification

Style: `anthropic-claude`

Component: `auth-onboarding`

Mediums: web_app, onboarding

Intents: login, signup, verification, first-run onboarding, account creation

Aliases: auth, login, signup, phone verification, onboarding

Repo source: `styles/anthropic-claude/components/capsules/auth-onboarding.md`

## Capsule

# Auth / onboarding / verification
## Use when
Build login, signup, phone verification, social auth, or first-run education.
## Flow grammar
```text
Auth/onboarding
├── brand/header/nav
├── social auth or email field
├── phone/verification step if required
├── brief Claude-like self-introduction
├── safety/privacy capability caveats
├── plan selection if needed
└── handoff into app shell
```
## Implementation recipe
- Center forms on a warm paper canvas; keep fields wide, simple, and calm.
- Use Google/email/SSO first, then verification if needed.
- Verification screens should be sparse and reassuring.
- Explain safety/privacy limitations in plain language without alarm.
- Use one dominant action per step.
## Code extraction targets
- Form card width, field height/radius, label/helper typography.
- Verification code input spacing and focus state.
- Social auth button structure.
- Step transition and error states.
## Avoid
- Growth-hack urgency, dense registration forms, loud progress bars, mascot-heavy AI onboarding.
