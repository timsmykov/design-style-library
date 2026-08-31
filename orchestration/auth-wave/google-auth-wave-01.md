# Google Auth Wave 01 — Design Style Library

Approved by Tim in Telegram: use the third Google account for OAuth/test registration to collect observable UI evidence for design-style-library.

## Boundary

Allowed:
- OAuth/register/login with the third Google account only.
- Capture observable runtime evidence: DOM snapshots, CSS bundles, computed styles, screenshots, route maps, UI state maps.
- Store evidence under each `styles/<style>/evidence/authenticated/` directory.
- Use evidence for design distillation only.

Forbidden:
- Print/store passwords, OTPs, recovery codes, API tokens, cookies, session IDs, payment data, seed phrases, private keys.
- Create crypto wallets or handle seed phrases.
- Complete payments, KYC, business onboarding, bookings, reservations, paid subscriptions, or irreversible actions.
- Copy proprietary source as runtime dependency. Bundles/DOM/CSS are provenance/evidence only.

## Safe target set

Safe OAuth / test-access targets:
- `anthropic-claude` — Claude app surfaces if Google OAuth succeeds.
- `perplexity-answer-engine` — logged-in answer/workspace surfaces if Google OAuth succeeds.
- `notion-document-os` — workspace/editor surfaces.
- `linear-operational-workspace` — workspace issue/project surfaces if free workspace creation is possible.
- `vercel-developer-control-plane` — dashboard/project/import surfaces if no billing required.
- `figma-collaborative-canvas` — file browser/editor surfaces if free account allowed.
- `raycast-command-native` — account/dashboard/team/settings only if web OAuth exists without paid step.
- `cursor-ai-ide` — account/settings/dashboard if Google OAuth exists.
- `airbnb-marketplace-warm-consumer` — signed-in search/profile wishlist surfaces only; no booking/payment.

Restricted / likely no-go:
- `stripe-trust-commerce` — do not enter business/KYC/payment details; capture only docs/login/dashboard shell if accessible.
- `metamask-crypto-wallet-trust` — no wallet creation/import/seed phrase. Capture only public/app shell and dapp connect patterns from non-secret demo/public surfaces.

## Evidence done criteria per safe service

- Auth flow outcome documented.
- At least one authenticated or barrier state captured.
- DOM/computed/screenshot evidence saved.
- `AUTH_BLOCKERS.md` updated if auth or safety boundary stops deeper capture.
- `stylepack_verify.py` remains PASS.
