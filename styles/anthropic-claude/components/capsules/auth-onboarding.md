---
style_id: anthropic-claude
component_id: auth-onboarding
title: Auth / onboarding / verification
component_type: form_flow
mediums:
  - web_app
  - onboarding
intents:
  - login
  - signup
  - verification
  - first-run onboarding
  - account creation
aliases:
  - auth
  - login
  - signup
  - phone verification
  - onboarding
tags:
  - anthropic
  - claude
  - auth
  - onboarding
  - forms
evidence_paths:
  - evidence/mobbin/flows/flow-5a978c28-onboarding/
  - evidence/mobbin/flows/flow-0b72f658-onboarding/
  - evidence/mobbin/flows/flow-6bb1fc63-onboarding-login/
extracted_paths:
  - styles/anthropic-claude/components/extracted/browser-cdp/by-component/auth-onboarding
  - styles/anthropic-claude/components/extracted/from-mobbin-screenshots/auth-onboarding
confidence: extracted
updated_at: 2026-06-30
---

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
