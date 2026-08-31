# Auth Wave 01 Results

Third-Google-account OAuth wave for design-style-library. Evidence policy: observable UI/DOM/CSS/computed only; no cookies/localStorage/passwords/OTP/API tokens/seed phrases/payment/KYC data.

| style | outcome | captured title | path |
|---|---|---|---|
| `airbnb-marketplace-warm-consumer` / `airbnb-home` | `captured_surface` | Airbnb / Vacation rentals, cabins, beach houses, & more | `styles/airbnb-marketplace-warm-consumer/evidence/authenticated/browser-cdp/airbnb-home` |
| `anthropic-claude` / `claude-new` | `login_or_signup_barrier` | Sign in - Claude | `styles/anthropic-claude/evidence/authenticated/browser-cdp/claude-new` |
| `cursor-ai-ide` / `cursor-dashboard` | `security_checkpoint_barrier` | Vercel Security Checkpoint | `styles/cursor-ai-ide/evidence/authenticated/browser-cdp/cursor-dashboard` |
| `figma-collaborative-canvas` / `figma-files` | `captured_surface` | www.figma.com | `styles/figma-collaborative-canvas/evidence/authenticated/browser-cdp/figma-files` |
| `linear-operational-workspace` / `linear-home` | `login_or_signup_barrier` | Linear – The system for product development | `styles/linear-operational-workspace/evidence/authenticated/browser-cdp/linear-home` |
| `metamask-crypto-wallet-trust` / `metamask-portfolio` | `captured_surface` | MetaMask Portfolio | `styles/metamask-crypto-wallet-trust/evidence/authenticated/browser-cdp/metamask-portfolio` |
| `perplexity-answer-engine` / `perplexity-home` | `security_checkpoint_barrier` | Just a moment... | `styles/perplexity-answer-engine/evidence/authenticated/browser-cdp/perplexity-home` |
| `raycast-command-native` / `raycast-account` | `security_checkpoint_barrier` | Vercel Security Checkpoint | `styles/raycast-command-native/evidence/authenticated/browser-cdp/raycast-account` |
| `vercel-developer-control-plane` / `vercel-dashboard` | `login_or_signup_barrier` | Vercel | `styles/vercel-developer-control-plane/evidence/authenticated/browser-cdp/vercel-dashboard` |
| `notion-document-os` / `notion-third-account-oauth` | `discarded_ambient_session` | Not captured | `styles/notion-document-os/evidence/authenticated/README.md` |
| `stripe-trust-commerce` / `stripe-dashboard` | `restricted_billing_or_kyc_boundary` | Not captured | `styles/stripe-trust-commerce/evidence/authenticated/README.md` |
| `anthropic-claude` / `claude-google-oauth` | `google_verification_otp_required` | Google verification stopped | `styles/anthropic-claude/evidence/authenticated/GOOGLE_OAUTH_BLOCKER.md` |
| `figma-collaborative-canvas` / `figma-google-oauth` | `captcha_or_bot_check_barrier` | Figma verification stopped | `styles/figma-collaborative-canvas/evidence/authenticated/GOOGLE_OAUTH_BLOCKER.md` |

## Notes

- Notion ambient-session capture was discarded because it was not proven to be the approved third-account test context.
- Stripe authenticated capture was discarded/restricted because dashboard flows can lead to business, billing, KYC, or saved-account surfaces.
- MetaMask wallet creation/import was not attempted; no seed phrase/private key touched.
- Figma CAPTCHA and Google OTP verification were not bypassed.
