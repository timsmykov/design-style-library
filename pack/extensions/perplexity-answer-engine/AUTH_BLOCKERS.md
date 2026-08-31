# Auth Blockers — Perplexity Answer Engine

No login, OAuth, credentials, or account-specific browsing was used.

Known incomplete or blocked surfaces:

- Public `https://www.perplexity.ai/` and `https://www.perplexity.ai/pro` returned Cloudflare security verification to Chromium and local Firecrawl during this no-login run; the saved public DOM/screenshots therefore represent the challenge page, not full product CSS.
- Authenticated Library/collections with real user data.
- Account settings/profile/preferences.
- Billing/subscription management after checkout.
- Saved threads/spaces requiring account state.
- Hover/focus/selected states inside authenticated app panels.

The pack is therefore `offline_ready: false` until authenticated Browser/CDP extraction and fresh-agent eval are run.
